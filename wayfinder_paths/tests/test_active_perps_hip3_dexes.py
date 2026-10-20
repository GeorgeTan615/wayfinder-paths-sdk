from __future__ import annotations

import pytest

from wayfinder_paths.core.strategies.active_perps import (
    KNOWN_HIP3_DEXES,
    ActivePerpsStrategy,
)


def _signal(*args, **kwargs):
    return None


@pytest.mark.parametrize(
    "dex",
    ["xyz", "flx", "vntl", "hyna", "km", "abcd", "cash", "para", "mkts", "io"],
)
def test_live_hip3_dex_is_accepted_in_hip3_dexes(tmp_path, dex):
    ref = tmp_path / "ref.json"
    ref.write_text("{}")

    class _Strategy(ActivePerpsStrategy):
        REF = ref
        SIGNAL = f"{__name__}:_signal"
        HIP3_DEXES = [dex]

    assert dex in KNOWN_HIP3_DEXES
    assert _Strategy.HIP3_DEXES == [dex]


def test_unknown_hip3_dex_is_rejected(tmp_path):
    ref = tmp_path / "ref.json"
    ref.write_text("{}")

    with pytest.raises(RuntimeError, match="has unknown dex 'nope'"):

        class _Strategy(ActivePerpsStrategy):
            REF = ref
            SIGNAL = f"{__name__}:_signal"
            HIP3_DEXES = ["nope"]
