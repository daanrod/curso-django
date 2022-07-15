import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titutlo',
    [
        'Video Aperitivo: Motivação',
        'Instalação Windows'
    ]
)
def test_titulo_video(resp, titutlo):
    assert_contains(resp, titutlo)

#
#
# def test_conteudo_video(resp):
#     assert_contains(resp, 'src="https://www.youtube.com/embed/2aYplgJrPDU"')
