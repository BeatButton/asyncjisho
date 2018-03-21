from asyncjisho import Jisho

import pytest

pytestmark = pytest.mark.asyncio

async def test_lookup(jisho: Jisho):
    result = (await jisho.lookup('water'))[0]
    assert set(result['readings']) == {'みず', 'み'}
    assert result['words'] == ['水']
    assert result['parts_of_speech'] == ['Noun']
    assert 'Water' in result['english']
    