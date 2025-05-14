from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.http import require_POST

from .models import Ad, ExchangeProposal
from .forms import AdForm, ExchangeProposalForm


# Список объявлений с фильтрацией и поиском

def ad_list(request):
    query = request.GET.get("q")
    category = request.GET.get("category")
    condition = request.GET.get("condition")

    ads = Ad.objects.all()

    if query:
        ads = ads.filter(Q(title__icontains=query) |
                         Q(description__icontains=query))

    if category:
        ads = ads.filter(category__iexact=category)

    if condition:
        ads = ads.filter(condition=condition)

    return render(request, "ads/ad_list.html", {"ads": ads})



@login_required
def ad_create(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            messages.success(request, "Объявление создано")

            return redirect("ad_list")

    else:
        form = AdForm()
    return render(request, "ads/ad_form.html", {"form": form,
                                                "title": "Создание объявления"})


@login_required
def ad_update(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    if ad.user != request.user:
        messages.error(request, "Вы не можете редактировать это объявление.")
        return redirect("ad_list")

    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            messages.success(request, "Объявление обновлено.")
            return redirect("ad_list")
    else:
        form = AdForm(instance=ad)

    return render(request, "ads/ad_form.html", {"form": form,
                                                "title": "Редактирование объявления"})


@login_required
def ad_delete(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    if ad.user != request.user:
        messages.error(request, "Вы не можете удалить это объявление.")
        return redirect("ad_list")

    if request.method == "POST":
        ad.delete()
        messages.success(request, "Объявление удалено.")
        return redirect("ad_list")

    return render(request, "ads/ad_confirm_delete.html", {"ad": ad})


@login_required
def create_proposal(request, ad_id):
    ad_receiver = get_object_or_404(Ad, id=ad_id)

    if request.method == "POST":
        form = ExchangeProposalForm(request.POST, user=request.user)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.ad_sender = form.cleaned_data['ad_sender']
            proposal.ad_receiver = ad_receiver  
            proposal.status = "pending"
            proposal.save()
            messages.success(request, "Предложение отправлено.")
            return redirect("ad_list")
    else:
        form = ExchangeProposalForm(user=request.user)

    return render(request, "ads/exchange_proposal_form.html",
                  {"form": form, "receiver_ad": ad_receiver})


# Список предложений

@login_required
def proposal_list(request):
    proposals = ExchangeProposal.objects.filter(
        Q(ad_sender__user=request.user) | Q(ad_receiver__user=request.user)
    )

    status = request.GET.get("status")
    if status:
        proposals = proposals.filter(status=status)

    return render(request, "ads/proposal_list.html",
                  {"proposals": proposals, "selected_status": status})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно")
            return redirect("ad_list")
    else:
        form = UserCreationForm()
    return render(request, "ads/register.html", {"form": form})


@login_required
@require_POST
def update_proposal_status(request, proposal_id):
    proposal = get_object_or_404(ExchangeProposal, id=proposal_id)

    if proposal.ad_receiver.user != request.user:
        messages.error(
            request, "Вы не можете изменить статус этого предложения")
        return redirect("proposal_list")

    new_status = request.POST.get("status")
    if new_status in ["accepted", "declined"]:
        proposal.status = new_status
        proposal.save()
        messages.success(request, "Статус обновлён")
    else:
        messages.error(request, "Неверный статус")

    return redirect("proposal_list")
