import pytest
from picpay.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_criar_usuario_com_sucesso():
    client = APIClient()
    response = client.post("/user/", {
        "nome_completo": "Matheus Teste",
        "email": "matheus@example.com",
        "senha": "123456",
        "cpf": "11122233344",
        "user_type": "C",
        "wallet": 100.00
    }, format='json')

    assert response.status_code == 201
    assert User.objects.filter(email="matheus@example.com").exists()

@pytest.mark.django_db
def test_nao_permitir_cpf_duplicado():
    client = APIClient()

    User.objects.create(
        nome_completo="User 1",
        email="um@example.com",
        senha="123",
        cpf="99988877766",
        user_type="C"
    )

    response = client.post("/user/", {
        "nome_completo": "User 2",
        "email": "dois@example.com",
        "senha": "456",
        "cpf": "99988877766",  # mesmo CPF
        "user_type": "C"
    }, format='json')

    assert response.status_code == 400
    assert "cpf" in response.data

@pytest.mark.django_db
def test_nao_permitir_email_duplicado():
    client = APIClient()

    User.objects.create(
        nome_completo="User 1",
        email="mesmo@example.com",
        senha="123",
        cpf="12345678900",
        user_type="C"
    )

    response = client.post("/user/", {
        "nome_completo": "User 2",
        "email": "mesmo@example.com",  # mesmo e-mail
        "senha": "456",
        "cpf": "09876543210",
        "user_type": "C"
    }, format='json')

    assert response.status_code == 400
    assert "email" in response.data
