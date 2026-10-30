import pytest
from erick_context import prepare_context


def test_unicode_whitespace_and_budget():
    result = prepare_context("  Cafe\u0301   claro\n\n segunda\t linea ", 10)
    assert result["text"] == "Café claro"
    assert result["truncated"] is True
    assert result["output_chars"] == 10
    assert prepare_context("  \n\t")["text"] == ""
    assert prepare_context("abc", 3)["truncated"] is False


@pytest.mark.parametrize("limit", [0, -1, True, 2.5])
def test_invalid_budget(limit):
    with pytest.raises(ValueError):
        prepare_context("abc", limit)
