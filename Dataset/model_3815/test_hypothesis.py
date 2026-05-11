import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    example::InterfacePlayer,
    example::AbstractPlayer,
    example::Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example::interfaceplayer_is_not_abstract():
    assert not inspect.isabstract(example::InterfacePlayer)


def test_example::interfaceplayer_constructor_exists():
    assert callable(example::InterfacePlayer.__init__)


def test_example::interfaceplayer_constructor_args():
    sig = inspect.signature(example::InterfacePlayer.__init__)
    params = list(sig.parameters.keys())



def test_example::abstractplayer_is_not_abstract():
    assert not inspect.isabstract(example::AbstractPlayer)


def test_example::abstractplayer_constructor_exists():
    assert callable(example::AbstractPlayer.__init__)


def test_example::abstractplayer_constructor_args():
    sig = inspect.signature(example::AbstractPlayer.__init__)
    params = list(sig.parameters.keys())



def test_example::player_is_not_abstract():
    assert not inspect.isabstract(example::Player)


def test_example::player_constructor_exists():
    assert callable(example::Player.__init__)


def test_example::player_constructor_args():
    sig = inspect.signature(example::Player.__init__)
    params = list(sig.parameters.keys())


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
example::InterfacePlayer_strategy = st.builds(
    example::InterfacePlayer,
)
example::AbstractPlayer_strategy = st.builds(
    example::AbstractPlayer,
)
example::Player_strategy = st.builds(
    example::Player,
)

@given(instance=example::InterfacePlayer_strategy)
@settings(max_examples=50)
def test_example::interfaceplayer_instantiation(instance):
    assert isinstance(instance, example::InterfacePlayer)

@given(instance=example::AbstractPlayer_strategy)
@settings(max_examples=50)
def test_example::abstractplayer_instantiation(instance):
    assert isinstance(instance, example::AbstractPlayer)

@given(instance=example::Player_strategy)
@settings(max_examples=50)
def test_example::player_instantiation(instance):
    assert isinstance(instance, example::Player)
