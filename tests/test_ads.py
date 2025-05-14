import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from ads.models import Ad, ExchangeProposal


@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def logged_client(client, user):
    client.login(username='testuser', password='testpass')
    return client


@pytest.mark.django_db
def test_ad_creation(logged_client):
    response = logged_client.post(reverse('ad_create'), {
        'title': 'Test Ad',
        'description': 'Test desc',
        'category': 'Test',
        'condition': 'new'
    })
    assert response.status_code == 302
    assert Ad.objects.filter(title='Test Ad').exists()


@pytest.mark.django_db
def test_ad_update(logged_client, user):
    ad = Ad.objects.create(user=user, title='Old',
                           description='...', category='Cat', condition='used')
    response = logged_client.post(reverse('ad_update', args=[ad.id]), {
        'title': 'Updated',
        'description': 'Updated',
        'category': 'NewCat',
        'condition': 'new'
    })
    ad.refresh_from_db()
    assert ad.title == 'Updated'


@pytest.mark.django_db
def test_ad_delete(logged_client, user):
    ad = Ad.objects.create(user=user, title='To delete',
                           category='Cat', condition='new')
    response = logged_client.post(reverse('ad_delete', args=[ad.id]))
    assert response.status_code == 302
    assert not Ad.objects.filter(id=ad.id).exists()


@pytest.mark.django_db
def test_search_ads(client, user):
    Ad.objects.create(user=user, title='Laptop',
                      description='...', category='Tech', condition='new')
    Ad.objects.create(user=user, title='Table',
                      description='...', category='Home', condition='used')
    response = client.get(reverse('ad_list'), {'q': 'Laptop'})
    assert 'Laptop' in response.content.decode()
    assert 'Table' not in response.content.decode()


@pytest.mark.django_db
def test_exchange_proposal(logged_client, user):
    receiver = Ad.objects.create(
        user=user, title='iPhone', description='...', category='Tech', condition='new')
    sender = Ad.objects.create(
        user=user, title='Table', description='...', category='Home', condition='used')

    response = logged_client.post(reverse('create_proposal', args=[receiver.id]), {
        'ad_receiver': receiver.id,
        'ad_sender': sender.id,
        'comment': 'Ready to trade!'
    })

    assert response.status_code == 302
    assert ExchangeProposal.objects.filter(
        ad_sender=sender, ad_receiver=receiver).exists()
