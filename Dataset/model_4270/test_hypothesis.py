import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bowlingTournament::Game,
    bowlingTournament::Matchup,
    bowlingTournament::Tournament,
    bowlingTournament::Player,
    bowlingTournament::League,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowlingtournament::game_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament::Game)


def test_bowlingtournament::game_constructor_exists():
    assert callable(bowlingTournament::Game.__init__)


def test_bowlingtournament::game_constructor_args():
    sig = inspect.signature(bowlingTournament::Game.__init__)
    params = list(sig.parameters.keys())
    assert "frames" in params, "Missing parameter 'frames'"

def test_bowlingtournament::game_has_frames():
    assert hasattr(bowlingTournament::Game, "frames")
    descriptor = None
    for klass in bowlingTournament::Game.__mro__:
        if "frames" in klass.__dict__:
            descriptor = klass.__dict__["frames"]
            break
    assert isinstance(descriptor, property)



def test_bowlingtournament::matchup_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament::Matchup)


def test_bowlingtournament::matchup_constructor_exists():
    assert callable(bowlingTournament::Matchup.__init__)


def test_bowlingtournament::matchup_constructor_args():
    sig = inspect.signature(bowlingTournament::Matchup.__init__)
    params = list(sig.parameters.keys())



def test_bowlingtournament::tournament_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament::Tournament)


def test_bowlingtournament::tournament_constructor_exists():
    assert callable(bowlingTournament::Tournament.__init__)


def test_bowlingtournament::tournament_constructor_args():
    sig = inspect.signature(bowlingTournament::Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_bowlingtournament::tournament_has_type():
    assert hasattr(bowlingTournament::Tournament, "type")
    descriptor = None
    for klass in bowlingTournament::Tournament.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bowlingtournament::player_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament::Player)


def test_bowlingtournament::player_constructor_exists():
    assert callable(bowlingTournament::Player.__init__)


def test_bowlingtournament::player_constructor_args():
    sig = inspect.signature(bowlingTournament::Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "height" in params, "Missing parameter 'height'"
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"

def test_bowlingtournament::player_has_name():
    assert hasattr(bowlingTournament::Player, "name")
    descriptor = None
    for klass in bowlingTournament::Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bowlingtournament::player_has_dateOfBirth():
    assert hasattr(bowlingTournament::Player, "dateOfBirth")
    descriptor = None
    for klass in bowlingTournament::Player.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_bowlingtournament::player_has_height():
    assert hasattr(bowlingTournament::Player, "height")
    descriptor = None
    for klass in bowlingTournament::Player.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_bowlingtournament::player_has_isProfessional():
    assert hasattr(bowlingTournament::Player, "isProfessional")
    descriptor = None
    for klass in bowlingTournament::Player.__mro__:
        if "isProfessional" in klass.__dict__:
            descriptor = klass.__dict__["isProfessional"]
            break
    assert isinstance(descriptor, property)



def test_bowlingtournament::league_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament::League)


def test_bowlingtournament::league_constructor_exists():
    assert callable(bowlingTournament::League.__init__)


def test_bowlingtournament::league_constructor_args():
    sig = inspect.signature(bowlingTournament::League.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowlingtournament::league_has_name():
    assert hasattr(bowlingTournament::League, "name")
    descriptor = None
    for klass in bowlingTournament::League.__mro__:
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
bowlingTournament::Game_strategy = st.builds(
    bowlingTournament::Game,
    frames=
        st.integers()
)
bowlingTournament::Matchup_strategy = st.builds(
    bowlingTournament::Matchup,
)
bowlingTournament::Tournament_strategy = st.builds(
    bowlingTournament::Tournament,
    type=
        safe_text
)
bowlingTournament::Player_strategy = st.builds(
    bowlingTournament::Player,
    name=
        safe_text,
    dateOfBirth=
        st.dates(),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isProfessional=
        st.booleans()
)
bowlingTournament::League_strategy = st.builds(
    bowlingTournament::League,
    name=
        safe_text
)

@given(instance=bowlingTournament::Game_strategy)
@settings(max_examples=50)
def test_bowlingtournament::game_instantiation(instance):
    assert isinstance(instance, bowlingTournament::Game)

@given(instance=bowlingTournament::Game_strategy)
def test_bowlingtournament::game_frames_type(instance):
    assert isinstance(instance.frames, int)


@given(instance=bowlingTournament::Game_strategy)
def test_bowlingtournament::game_frames_setter(instance):
    original = instance.frames
    instance.frames = original
    assert instance.frames == original

@given(instance=bowlingTournament::Matchup_strategy)
@settings(max_examples=50)
def test_bowlingtournament::matchup_instantiation(instance):
    assert isinstance(instance, bowlingTournament::Matchup)

@given(instance=bowlingTournament::Tournament_strategy)
@settings(max_examples=50)
def test_bowlingtournament::tournament_instantiation(instance):
    assert isinstance(instance, bowlingTournament::Tournament)

@given(instance=bowlingTournament::Tournament_strategy)
def test_bowlingtournament::tournament_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bowlingTournament::Tournament_strategy)
def test_bowlingtournament::tournament_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bowlingTournament::Player_strategy)
@settings(max_examples=50)
def test_bowlingtournament::player_instantiation(instance):
    assert isinstance(instance, bowlingTournament::Player)

@given(instance=bowlingTournament::Player_strategy)
def test_bowlingtournament::player_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowlingTournament::Player_strategy)
def test_bowlingtournament::player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowlingTournament::Player_strategy)
def test_bowlingtournament::player_dateOfBirth_type(instance):
    assert isinstance(instance.dateOfBirth, date)


@given(instance=bowlingTournament::Player_strategy)
def test_bowlingtournament::player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original

@given(instance=bowlingTournament::Player_strategy)
def test_bowlingtournament::player_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=bowlingTournament::Player_strategy)
def test_bowlingtournament::player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=bowlingTournament::Player_strategy)
def test_bowlingtournament::player_isProfessional_type(instance):
    assert isinstance(instance.isProfessional, bool)


@given(instance=bowlingTournament::Player_strategy)
def test_bowlingtournament::player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original

@given(instance=bowlingTournament::League_strategy)
@settings(max_examples=50)
def test_bowlingtournament::league_instantiation(instance):
    assert isinstance(instance, bowlingTournament::League)

@given(instance=bowlingTournament::League_strategy)
def test_bowlingtournament::league_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowlingTournament::League_strategy)
def test_bowlingtournament::league_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
