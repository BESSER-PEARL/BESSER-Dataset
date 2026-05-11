import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bowling::Player,
    bowling::Matchup,
    bowling::Tournament,
    bowling::Game,
    bowling::league,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowling::player_is_not_abstract():
    assert not inspect.isabstract(bowling::Player)


def test_bowling::player_constructor_exists():
    assert callable(bowling::Player.__init__)


def test_bowling::player_constructor_args():
    sig = inspect.signature(bowling::Player.__init__)
    params = list(sig.parameters.keys())
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"
    assert "heigth" in params, "Missing parameter 'heigth'"
    assert "name" in params, "Missing parameter 'name'"

def test_bowling::player_has_dateOfBirth():
    assert hasattr(bowling::Player, "dateOfBirth")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_bowling::player_has_isProfessional():
    assert hasattr(bowling::Player, "isProfessional")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "isProfessional" in klass.__dict__:
            descriptor = klass.__dict__["isProfessional"]
            break
    assert isinstance(descriptor, property)

def test_bowling::player_has_heigth():
    assert hasattr(bowling::Player, "heigth")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "heigth" in klass.__dict__:
            descriptor = klass.__dict__["heigth"]
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



def test_bowling::matchup_is_not_abstract():
    assert not inspect.isabstract(bowling::Matchup)


def test_bowling::matchup_constructor_exists():
    assert callable(bowling::Matchup.__init__)


def test_bowling::matchup_constructor_args():
    sig = inspect.signature(bowling::Matchup.__init__)
    params = list(sig.parameters.keys())



def test_bowling::tournament_is_not_abstract():
    assert not inspect.isabstract(bowling::Tournament)


def test_bowling::tournament_constructor_exists():
    assert callable(bowling::Tournament.__init__)


def test_bowling::tournament_constructor_args():
    sig = inspect.signature(bowling::Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_bowling::tournament_has_Type():
    assert hasattr(bowling::Tournament, "Type")
    descriptor = None
    for klass in bowling::Tournament.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_bowling::game_is_not_abstract():
    assert not inspect.isabstract(bowling::Game)


def test_bowling::game_constructor_exists():
    assert callable(bowling::Game.__init__)


def test_bowling::game_constructor_args():
    sig = inspect.signature(bowling::Game.__init__)
    params = list(sig.parameters.keys())
    assert "frames" in params, "Missing parameter 'frames'"

def test_bowling::game_has_frames():
    assert hasattr(bowling::Game, "frames")
    descriptor = None
    for klass in bowling::Game.__mro__:
        if "frames" in klass.__dict__:
            descriptor = klass.__dict__["frames"]
            break
    assert isinstance(descriptor, property)



def test_bowling::league_is_not_abstract():
    assert not inspect.isabstract(bowling::league)


def test_bowling::league_constructor_exists():
    assert callable(bowling::league.__init__)


def test_bowling::league_constructor_args():
    sig = inspect.signature(bowling::league.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowling::league_has_name():
    assert hasattr(bowling::league, "name")
    descriptor = None
    for klass in bowling::league.__mro__:
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
        "Amateur",
        "Pro",
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
bowling::Player_strategy = st.builds(
    bowling::Player,
    dateOfBirth=
        st.dates(),
    isProfessional=
        st.booleans(),
    heigth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
bowling::Matchup_strategy = st.builds(
    bowling::Matchup,
)
bowling::Tournament_strategy = st.builds(
    bowling::Tournament,
    Type=
        safe_text
)
bowling::Game_strategy = st.builds(
    bowling::Game,
    frames=
        st.integers()
)
bowling::league_strategy = st.builds(
    bowling::league,
    name=
        safe_text
)

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
def test_bowling::player_isProfessional_type(instance):
    assert isinstance(instance.isProfessional, bool)


@given(instance=bowling::Player_strategy)
def test_bowling::player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original

@given(instance=bowling::Player_strategy)
def test_bowling::player_heigth_type(instance):
    assert isinstance(instance.heigth, float)


@given(instance=bowling::Player_strategy)
def test_bowling::player_heigth_setter(instance):
    original = instance.heigth
    instance.heigth = original
    assert instance.heigth == original

@given(instance=bowling::Player_strategy)
def test_bowling::player_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::Player_strategy)
def test_bowling::player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling::Matchup_strategy)
@settings(max_examples=50)
def test_bowling::matchup_instantiation(instance):
    assert isinstance(instance, bowling::Matchup)

@given(instance=bowling::Tournament_strategy)
@settings(max_examples=50)
def test_bowling::tournament_instantiation(instance):
    assert isinstance(instance, bowling::Tournament)

@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=bowling::Game_strategy)
@settings(max_examples=50)
def test_bowling::game_instantiation(instance):
    assert isinstance(instance, bowling::Game)

@given(instance=bowling::Game_strategy)
def test_bowling::game_frames_type(instance):
    assert isinstance(instance.frames, int)


@given(instance=bowling::Game_strategy)
def test_bowling::game_frames_setter(instance):
    original = instance.frames
    instance.frames = original
    assert instance.frames == original

@given(instance=bowling::league_strategy)
@settings(max_examples=50)
def test_bowling::league_instantiation(instance):
    assert isinstance(instance, bowling::league)

@given(instance=bowling::league_strategy)
def test_bowling::league_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::league_strategy)
def test_bowling::league_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
