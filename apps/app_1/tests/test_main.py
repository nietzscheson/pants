import pytest


@pytest.mark.asyncio
async def test_root(
    http_client,
):
    response = await http_client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data == {"Hello": "World", "Message": "Pants <3 Python Uv"}
