import asyncio

import pytest

from asyncjisho import Jisho


@pytest.fixture(scope="module")
async def jisho() -> Jisho:
    async with Jisho() as jisho:
        yield jisho

@pytest.fixture(scope="module")
def event_loop():
    return asyncio.get_event_loop()
