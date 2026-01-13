import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from apps.app_1.src.main import app


@pytest_asyncio.fixture
async def http_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
        await client.aclose()
