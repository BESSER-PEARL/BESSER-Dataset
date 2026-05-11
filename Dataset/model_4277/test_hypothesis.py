import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bowling::Matchup,
    bowling::Tournament,
    bowling::Lane,
    bowling::Alley,
    bowling::Game,
    bowling::League,
    bowling::Player,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowling::matchup_is_not_abstract():
    assert not inspect.isabstract(bowling::Matchup)


def test_bowling::matchup_constructor_exists():
    assert callable(bowling::Matchup.__init__)


def test_bowling::matchup_constructor_args():
    sig = inspect.signature(bowling::Matchup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowling::matchup_has_name():
    assert hasattr(bowling::Matchup, "name")
    descriptor = None
    for klass in bowling::Matchup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bowling::tournament_is_not_abstract():
    assert not inspect.isabstract(bowling::Tournament)


def test_bowling::tournament_constructor_exists():
    assert callable(bowling::Tournament.__init__)


def test_bowling::tournament_constructor_args():
    sig = inspect.signature(bowling::Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_bowling::tournament_has_name():
    assert hasattr(bowling::Tournament, "name")
    descriptor = None
    for klass in bowling::Tournament.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bowling::tournament_has_type():
    assert hasattr(bowling::Tournament, "type")
    descriptor = None
    for klass in bowling::Tournament.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bowling::lane_is_not_abstract():
    assert not inspect.isabstract(bowling::Lane)


def test_bowling::lane_constructor_exists():
    assert callable(bowling::Lane.__init__)


def test_bowling::lane_constructor_args():
    sig = inspect.signature(bowling::Lane.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_bowling::lane_has_number():
    assert hasattr(bowling::Lane, "number")
    descriptor = None
    for klass in bowling::Lane.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_bowling::alley_is_not_abstract():
    assert not inspect.isabstract(bowling::Alley)


def test_bowling::alley_constructor_exists():
    assert callable(bowling::Alley.__init__)


def test_bowling::alley_constructor_args():
    sig = inspect.signature(bowling::Alley.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowling::alley_has_name():
    assert hasattr(bowling::Alley, "name")
    descriptor = None
    for klass in bowling::Alley.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"
    assert "height" in params, "Missing parameter 'height'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "name" in params, "Missing parameter 'name'"

def test_bowling::player_has_isProfessional():
    assert hasattr(bowling::Player, "isProfessional")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "isProfessional" in klass.__dict__:
            descriptor = klass.__dict__["isProfessional"]
            break
    assert isinstance(descriptor, property)

def test_bowling::player_has_height():
    assert hasattr(bowling::Player, "height")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

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
bowling::Matchup_strategy = st.builds(
    bowling::Matchup,
    name=
        safe_text
)
bowling::Tournament_strategy = st.builds(
    bowling::Tournament,
    name=
        safe_text,
    type=
        safe_text
)
bowling::Lane_strategy = st.builds(
    bowling::Lane,
    number=
        st.integers()
)
bowling::Alley_strategy = st.builds(
    bowling::Alley,
    name=
        safe_text
)
bowling::Game_strategy = st.builds(
    bowling::Game,
    frames=
        st.integers()
)
bowling::League_strategy = st.builds(
    bowling::League,
    name=
        safe_text
)
bowling::Player_strategy = st.builds(
    bowling::Player,
    isProfessional=
        st.booleans(),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dateOfBirth=
        st.dates(),
    name=
        safe_text
)

@given(instance=bowling::Matchup_strategy)
@settings(max_examples=50)
def test_bowling::matchup_instantiation(instance):
    assert isinstance(instance, bowling::Matchup)

@given(instance=bowling::Matchup_strategy)
def test_bowling::matchup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::Matchup_strategy)
def test_bowling::matchup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling::Tournament_strategy)
@settings(max_examples=50)
def test_bowling::tournament_instantiation(instance):
    assert isinstance(instance, bowling::Tournament)

@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bowling::Lane_strategy)
@settings(max_examples=50)
def test_bowling::lane_instantiation(instance):
    assert isinstance(instance, bowling::Lane)

@given(instance=bowling::Lane_strategy)
def test_bowling::lane_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=bowling::Lane_strategy)
def test_bowling::lane_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bowling::Alley_strategy)
@settings(max_examples=50)
def test_bowling::alley_instantiation(instance):
    assert isinstance(instance, bowling::Alley)

@given(instance=bowling::Alley_strategy)
def test_bowling::alley_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::Alley_strategy)
def test_bowling::alley_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_bowling::player_isProfessional_type(instance):
    assert isinstance(instance.isProfessional, bool)


@given(instance=bowling::Player_strategy)
def test_bowling::player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original

@given(instance=bowling::Player_strategy)
def test_bowling::player_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=bowling::Player_strategy)
def test_bowling::player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

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
