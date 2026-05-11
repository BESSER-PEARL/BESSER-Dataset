import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    example::Codec,
    example::Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example::codec_is_not_abstract():
    assert not inspect.isabstract(example::Codec)


def test_example::codec_constructor_exists():
    assert callable(example::Codec.__init__)


def test_example::codec_constructor_args():
    sig = inspect.signature(example::Codec.__init__)
    params = list(sig.parameters.keys())



def test_example::player_is_not_abstract():
    assert not inspect.isabstract(example::Player)


def test_example::player_constructor_exists():
    assert callable(example::Player.__init__)


def test_example::player_constructor_args():
    sig = inspect.signature(example::Player.__init__)
    params = list(sig.parameters.keys())
    assert "compression1" in params, "Missing parameter 'compression1'"

def test_example::player_has_compression1():
    assert hasattr(example::Player, "compression1")
    descriptor = None
    for klass in example::Player.__mro__:
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
example::Codec_strategy = st.builds(
    example::Codec,
)
example::Player_strategy = st.builds(
    example::Player,
    compression1=
        safe_text
)

@given(instance=example::Codec_strategy)
@settings(max_examples=50)
def test_example::codec_instantiation(instance):
    assert isinstance(instance, example::Codec)

@given(instance=example::Player_strategy)
@settings(max_examples=50)
def test_example::player_instantiation(instance):
    assert isinstance(instance, example::Player)

@given(instance=example::Player_strategy)
def test_example::player_compression1_type(instance):
    assert isinstance(instance.compression1, str)


@given(instance=example::Player_strategy)
def test_example::player_compression1_setter(instance):
    original = instance.compression1
    instance.compression1 = original
    assert instance.compression1 == original
