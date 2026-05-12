import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    example_Codec,
    example_Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example_codec_is_not_abstract():
    assert not inspect.isabstract(example_Codec)


def test_example_codec_constructor_exists():
    assert callable(example_Codec.__init__)


def test_example_codec_constructor_args():
    sig = inspect.signature(example_Codec.__init__)
    params = list(sig.parameters.keys())



def test_example_player_is_not_abstract():
    assert not inspect.isabstract(example_Player)


def test_example_player_constructor_exists():
    assert callable(example_Player.__init__)


def test_example_player_constructor_args():
    sig = inspect.signature(example_Player.__init__)
    params = list(sig.parameters.keys())
    assert "compression1" in params, "Missing parameter 'compression1'"

def test_example_player_has_compression1():
    assert hasattr(example_Player, "compression1")
    descriptor = None
    for klass in example_Player.__mro__:
        if "compression1" in klass.__dict__:
            descriptor = klass.__dict__["compression1"]
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
example_Codec_strategy = st.builds(
    example_Codec,
)
example_Player_strategy = st.builds(
    example_Player,
    compression1=
        safe_text
)

@given(instance=example_Codec_strategy)
@settings(max_examples=50)
def test_example_codec_instantiation(instance):
    assert isinstance(instance, example_Codec)

@given(instance=example_Player_strategy)
@settings(max_examples=50)
def test_example_player_instantiation(instance):
    assert isinstance(instance, example_Player)



@given(instance=example_Player_strategy)
def test_example_player_compression1_setter(instance):
    original = instance.compression1
    instance.compression1 = original
    assert instance.compression1 == original
