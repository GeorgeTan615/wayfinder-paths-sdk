import pytest

from wayfinder_paths.core.strategies.active_perps import ActivePerpsStrategy


def _declare_strategy(tmp_path, hip3_dexes):
    ref = tmp_path / "ref.json"
    ref.write_text("{}")
    return type(
        "Hip3DexStrategy",
        (ActivePerpsStrategy,),
        {"REF": ref, "SIGNAL": "string:capwords", "HIP3_DEXES": hip3_dexes},
    )


@pytest.mark.parametrize("dex", ["xyz", "flx", "vntl", "hyna", "km", "para"])
def test_known_hip3_dex_is_accepted(tmp_path, dex):
    strategy_cls = _declare_strategy(tmp_path, [dex])
    assert strategy_cls.HIP3_DEXES == [dex]


def test_unknown_hip3_dex_is_rejected(tmp_path):
    with pytest.raises(RuntimeError, match="unknown dex 'nope'"):
        _declare_strategy(tmp_path, ["nope"])
