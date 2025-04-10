import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_user_view(client):
    response = client.post(reverse('create_user'), {
        'name': 'Maria',
        'email': 'maria@email.com'
    })
    assert response.status_code in (200, 302)  # sucesso ou redirecionamento
