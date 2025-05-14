import pytest
from picpay.models import User, Transaction
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_lojista_nao_pode_enviar_dinheiro():
    client = APIClient()

    # Cria usuários
    lojista = User.objects.create(
        nome_completo="Lojista",
        email="lojista@example.com",
        senha="123456",
        cpf="12345678901",
        user_type='L',
        wallet=100
    )

    cliente = User.objects.create(
        nome_completo="Cliente",
        email="cliente@example.com",
        senha="123456",
        cpf="10987654321",
        user_type='C',
        wallet=100
    )

    # Tenta enviar dinheiro
    response = client.post("/transaction/", {
        "sender": lojista.id,
        "receiver": cliente.id,
        "value": 10
    }, format='json')

    assert response.status_code == 400
    assert "Lojistas cannot send money!" in str(response.data)
