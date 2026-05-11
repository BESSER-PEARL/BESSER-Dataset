import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bowling::Tournament,
    bowling::Game,
    bowling::Matchup,
    bowling::League,
    bowling::Player,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowling::tournament_is_not_abstract():
    assert not inspect.isabstract(bowling::Tournament)


def test_bowling::tournament_constructor_exists():
    assert callable(bowling::Tournament.__init__)


def test_bowling::tournament_constructor_args():
    sig = inspect.signature(bowling::Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_bowling::tournament_has_type():
    assert hasattr(bowling::Tournament, "type")
    descriptor = None
    for klass in bowling::Tournament.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bowling::game_is_not_abstract():
    assert not inspect.isabstract(bowling::Game)


def test_bowling::game_constructor_exists():
    assert callable(bowling::Game.__init__)


def test_bowling::game_constructor_args():
    sig = inspect.signature(bowling::Game.__init__)
    params = list(sig.parameters.keys())



def test_bowling::matchup_is_not_abstract():
    assert not inspect.isabstract(bowling::Matchup)


def test_bowling::matchup_constructor_exists():
    assert callable(bowling::Matchup.__init__)


def test_bowling::matchup_constructor_args():
    sig = inspect.signature(bowling::Matchup.__init__)
    params = list(sig.parameters.keys())



def test_bowling::league_is_not_abstract():
    assert not inspect.isabstract(bowling::League)


def test_bowling::league_constructor_exists():
    assert callable(bowling::League.__init__)


def test_bowling::league_constructor_args():
    sig = inspect.signature(bowling::League.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowling::league_has_name():
    assert hasattr(bowling::League, "name")
    descriptor = None
    for klass in bowling::League.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bowling::player_is_not_abstract():
    assert not inspect.isabstract(bowling::Player)


def test_bowling::player_constructor_exists():
    assert callable(bowling::Player.__init__)


def test_bowling::player_constructor_args():
    sig = inspect.signature(bowling::Player.__init__)
    params = list(sig.parameters.keys())
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "name" in params, "Missing parameter 'name'"

def test_bowling::player_has_dateOfBirth():
    assert hasattr(bowling::Player, "dateOfBirth")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_bowling::player_has_name():
    assert hasattr(bowling::Player, "name")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tournamenttype_exists():
    # Check that the Enumeration exists
    assert TournamentType is not None

def test_tournamenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TournamentType]
    expected_literals = [
        "Pro",
        "Amateur",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TournamentType"


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
bowling::Tournament_strategy = st.builds(
    bowling::Tournament,
    type=
        safe_text
)
bowling::Game_strategy = st.builds(
    bowling::Game,
)
bowling::Matchup_strategy = st.builds(
    bowling::Matchup,
)
bowling::League_strategy = st.builds(
    bowling::League,
    name=
        safe_text
)
bowling::Player_strategy = st.builds(
    bowling::Player,
    dateOfBirth=
        st.dates(),
    name=
        safe_text
)

@given(instance=bowling::Tournament_strategy)
@settings(max_examples=50)
def test_bowling::tournament_instantiation(instance):
    assert isinstance(instance, bowling::Tournament)

@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bowling::Game_strategy)
@settings(max_examples=50)
def test_bowling::game_instantiation(instance):
    assert isinstance(instance, bowling::Game)

@given(instance=bowling::Matchup_strategy)
@settings(max_examples=50)
def test_bowling::matchup_instantiation(instance):
    assert isinstance(instance, bowling::Matchup)

@given(instance=bowling::League_strategy)
@settings(max_examples=50)
def test_bowling::league_instantiation(instance):
    assert isinstance(instance, bowling::League)

@given(instance=bowling::League_strategy)
def test_bowling::league_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::League_strategy)
def test_bowling::league_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling::Player_strategy)
@settings(max_examples=50)
def test_bowling::player_instantiation(instance):
    assert isinstance(instance, bowling::Player)

@given(instance=bowling::Player_strategy)
def test_bowling::player_dateOfBirth_type(instance):
    assert isinstance(instance.dateOfBirth, date)


@given(instance=bowling::Player_strategy)
def test_bowling::player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original

@given(instance=bowling::Player_strategy)
def test_bowling::player_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::Player_strategy)
def test_bowling::player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
