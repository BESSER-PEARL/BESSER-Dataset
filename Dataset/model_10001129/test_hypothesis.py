import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    choose_scissor_external,
    choose_rock_external,
    choose_paper_external,
    PLAYER_Actor,
    COMPUTER_Actor,
    T,
    Library_Management_Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_choose_scissor_external_is_not_abstract():
    assert not inspect.isabstract(choose_scissor_external)


def test_choose_scissor_external_constructor_exists():
    assert callable(choose_scissor_external.__init__)


def test_choose_scissor_external_constructor_args():
    sig = inspect.signature(choose_scissor_external.__init__)
    params = list(sig.parameters.keys())



def test_choose_rock_external_is_not_abstract():
    assert not inspect.isabstract(choose_rock_external)


def test_choose_rock_external_constructor_exists():
    assert callable(choose_rock_external.__init__)


def test_choose_rock_external_constructor_args():
    sig = inspect.signature(choose_rock_external.__init__)
    params = list(sig.parameters.keys())



def test_choose_paper_external_is_not_abstract():
    assert not inspect.isabstract(choose_paper_external)


def test_choose_paper_external_constructor_exists():
    assert callable(choose_paper_external.__init__)


def test_choose_paper_external_constructor_args():
    sig = inspect.signature(choose_paper_external.__init__)
    params = list(sig.parameters.keys())



def test_player_actor_is_not_abstract():
    assert not inspect.isabstract(PLAYER_Actor)


def test_player_actor_constructor_exists():
    assert callable(PLAYER_Actor.__init__)


def test_player_actor_constructor_args():
    sig = inspect.signature(PLAYER_Actor.__init__)
    params = list(sig.parameters.keys())



def test_computer_actor_is_not_abstract():
    assert not inspect.isabstract(COMPUTER_Actor)


def test_computer_actor_constructor_exists():
    assert callable(COMPUTER_Actor.__init__)


def test_computer_actor_constructor_args():
    sig = inspect.signature(COMPUTER_Actor.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_library_management_component_is_not_abstract():
    assert not inspect.isabstract(Library_Management_Component)


def test_library_management_component_constructor_exists():
    assert callable(Library_Management_Component.__init__)


def test_library_management_component_constructor_args():
    sig = inspect.signature(Library_Management_Component.__init__)
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
choose_scissor_external_strategy = st.builds(
    choose_scissor_external,
)
choose_rock_external_strategy = st.builds(
    choose_rock_external,
)
choose_paper_external_strategy = st.builds(
    choose_paper_external,
)
PLAYER_Actor_strategy = st.builds(
    PLAYER_Actor,
)
COMPUTER_Actor_strategy = st.builds(
    COMPUTER_Actor,
)
T_strategy = st.builds(
    T,
)
Library_Management_Component_strategy = st.builds(
    Library_Management_Component,
)

@given(instance=choose_scissor_external_strategy)
@settings(max_examples=50)
def test_choose_scissor_external_instantiation(instance):
    assert isinstance(instance, choose_scissor_external)

@given(instance=choose_rock_external_strategy)
@settings(max_examples=50)
def test_choose_rock_external_instantiation(instance):
    assert isinstance(instance, choose_rock_external)

@given(instance=choose_paper_external_strategy)
@settings(max_examples=50)
def test_choose_paper_external_instantiation(instance):
    assert isinstance(instance, choose_paper_external)

@given(instance=PLAYER_Actor_strategy)
@settings(max_examples=50)
def test_player_actor_instantiation(instance):
    assert isinstance(instance, PLAYER_Actor)

@given(instance=COMPUTER_Actor_strategy)
@settings(max_examples=50)
def test_computer_actor_instantiation(instance):
    assert isinstance(instance, COMPUTER_Actor)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=Library_Management_Component_strategy)
@settings(max_examples=50)
def test_library_management_component_instantiation(instance):
    assert isinstance(instance, Library_Management_Component)
