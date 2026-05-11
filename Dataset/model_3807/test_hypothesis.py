import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    example::Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example::player_is_not_abstract():
    assert not inspect.isabstract(example::Player)


def test_example::player_constructor_exists():
    assert callable(example::Player.__init__)


def test_example::player_constructor_args():
    sig = inspect.signature(example::Player.__init__)
    params = list(sig.parameters.keys())
    assert "volume" in params, "Missing parameter 'volume'"

def test_example::player_has_volume():
    assert hasattr(example::Player, "volume")
    descriptor = None
    for klass in example::Player.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
example::Player_strategy = st.builds(
    example::Player,
    volume=
        safe_text
)

@given(instance=example::Player_strategy)
@settings(max_examples=50)
def test_example::player_instantiation(instance):
    assert isinstance(instance, example::Player)

@given(instance=example::Player_strategy)
def test_example::player_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=example::Player_strategy)
def test_example::player_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original
