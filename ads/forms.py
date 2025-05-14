from django import forms
from .models import Ad, ExchangeProposal


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ["title", "description", "image_url", "category", "condition"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image_url": forms.URLInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "condition": forms.Select(attrs={"class": "form-control"}),

        }
        labels = {
            "title": "Заголовок",
            "description": "Описание",
            "image_url": "Ссылка на изображение",
            "category": "Категория",
            "condition": "Состояние",
        }


class ExchangeProposalForm(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ["ad_sender", "ad_receiver", "comment"]
        widgets = {
            "ad_sender": forms.Select(attrs={"class": "form-control"}),
            "ad_receiver": forms.Select(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control"}),

        }
        labels = {
            "ad_sender": "Ваше объявление",
            "ad_receiver": "Объявление получателя",
            "comment": "Комментарий",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["ad_sender"].queryset = Ad.objects.filter(user=user)
