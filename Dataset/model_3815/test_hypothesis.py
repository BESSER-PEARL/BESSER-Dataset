import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    example_InterfacePlayer,
    example_AbstractPlayer,
    example_Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example_interfaceplayer_is_not_abstract():
    assert not inspect.isabstract(example_InterfacePlayer)


def test_example_interfaceplayer_constructor_exists():
    assert callable(example_InterfacePlayer.__init__)


def test_example_interfaceplayer_constructor_args():
    sig = inspect.signature(example_InterfacePlayer.__init__)
    params = list(sig.parameters.keys())



def test_example_abstractplayer_is_not_abstract():
    assert not inspect.isabstract(example_AbstractPlayer)


def test_example_abstractplayer_constructor_exists():
    assert callable(example_AbstractPlayer.__init__)


def test_example_abstractplayer_constructor_args():
    sig = inspect.signature(example_AbstractPlayer.__init__)
    params = list(sig.parameters.keys())



def test_example_player_is_not_abstract():
    assert not inspect.isabstract(example_Player)


def test_example_player_constructor_exists():
    assert callable(example_Player.__init__)


def test_example_player_constructor_args():
    sig = inspect.signature(example_Player.__init__)
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
example_InterfacePlayer_strategy = st.builds(
    example_InterfacePlayer,
)
example_AbstractPlayer_strategy = st.builds(
    example_AbstractPlayer,
)
example_Player_strategy = st.builds(
    example_Player,
)

@given(instance=example_InterfacePlayer_strategy)
@settings(max_examples=50)
def test_example_interfaceplayer_instantiation(instance):
    assert isinstance(instance, example_InterfacePlayer)

@given(instance=example_AbstractPlayer_strategy)
@settings(max_examples=50)
def test_example_abstractplayer_instantiation(instance):
    assert isinstance(instance, example_AbstractPlayer)

@given(instance=example_Player_strategy)
@settings(max_examples=50)
def test_example_player_instantiation(instance):
    assert isinstance(instance, example_Player)
