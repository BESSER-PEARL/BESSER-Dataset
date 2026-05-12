import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bowlingTournament_Game,
    bowlingTournament_Matchup,
    bowlingTournament_Tournament,
    bowlingTournament_Player,
    bowlingTournament_League,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowlingtournament_game_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament_Game)


def test_bowlingtournament_game_constructor_exists():
    assert callable(bowlingTournament_Game.__init__)


def test_bowlingtournament_game_constructor_args():
    sig = inspect.signature(bowlingTournament_Game.__init__)
    params = list(sig.parameters.keys())
    assert "frames" in params, "Missing parameter 'frames'"

def test_bowlingtournament_game_has_frames():
    assert hasattr(bowlingTournament_Game, "frames")
    descriptor = None
    for klass in bowlingTournament_Game.__mro__:
        if "frames" in klass.__dict__:
            descriptor = klass.__dict__["frames"]
            break
    assert isinstance(descriptor, property)



def test_bowlingtournament_matchup_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament_Matchup)


def test_bowlingtournament_matchup_constructor_exists():
    assert callable(bowlingTournament_Matchup.__init__)


def test_bowlingtournament_matchup_constructor_args():
    sig = inspect.signature(bowlingTournament_Matchup.__init__)
    params = list(sig.parameters.keys())



def test_bowlingtournament_tournament_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament_Tournament)


def test_bowlingtournament_tournament_constructor_exists():
    assert callable(bowlingTournament_Tournament.__init__)


def test_bowlingtournament_tournament_constructor_args():
    sig = inspect.signature(bowlingTournament_Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_bowlingtournament_tournament_has_type():
    assert hasattr(bowlingTournament_Tournament, "type")
    descriptor = None
    for klass in bowlingTournament_Tournament.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bowlingtournament_player_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament_Player)


def test_bowlingtournament_player_constructor_exists():
    assert callable(bowlingTournament_Player.__init__)


def test_bowlingtournament_player_constructor_args():
    sig = inspect.signature(bowlingTournament_Player.__init__)
    params = list(sig.parameters.keys())
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "height" in params, "Missing parameter 'height'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"

def test_bowlingtournament_player_has_dateOfBirth():
    assert hasattr(bowlingTournament_Player, "dateOfBirth")
    descriptor = None
    for klass in bowlingTournament_Player.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_bowlingtournament_player_has_height():
    assert hasattr(bowlingTournament_Player, "height")
    descriptor = None
    for klass in bowlingTournament_Player.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_bowlingtournament_player_has_name():
    assert hasattr(bowlingTournament_Player, "name")
    descriptor = None
    for klass in bowlingTournament_Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bowlingtournament_player_has_isProfessional():
    assert hasattr(bowlingTournament_Player, "isProfessional")
    descriptor = None
    for klass in bowlingTournament_Player.__mro__:
        if "isProfessional" in klass.__dict__:
            descriptor = klass.__dict__["isProfessional"]
            break
    assert isinstance(descriptor, property)



def test_bowlingtournament_league_is_not_abstract():
    assert not inspect.isabstract(bowlingTournament_League)


def test_bowlingtournament_league_constructor_exists():
    assert callable(bowlingTournament_League.__init__)


def test_bowlingtournament_league_constructor_args():
    sig = inspect.signature(bowlingTournament_League.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowlingtournament_league_has_name():
    assert hasattr(bowlingTournament_League, "name")
    descriptor = None
    for klass in bowlingTournament_League.__mro__:
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
bowlingTournament_Game_strategy = st.builds(
    bowlingTournament_Game,
    frames=
        st.integers()
)
bowlingTournament_Matchup_strategy = st.builds(
    bowlingTournament_Matchup,
)
bowlingTournament_Tournament_strategy = st.builds(
    bowlingTournament_Tournament,
    type=
        safe_text
)
bowlingTournament_Player_strategy = st.builds(
    bowlingTournament_Player,
    dateOfBirth=
        st.dates(),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    isProfessional=
        st.booleans()
)
bowlingTournament_League_strategy = st.builds(
    bowlingTournament_League,
    name=
        safe_text
)

@given(instance=bowlingTournament_Game_strategy)
@settings(max_examples=50)
def test_bowlingtournament_game_instantiation(instance):
    assert isinstance(instance, bowlingTournament_Game)



@given(instance=bowlingTournament_Game_strategy)
def test_bowlingtournament_game_frames_setter(instance):
    original = instance.frames
    instance.frames = original
    assert instance.frames == original

@given(instance=bowlingTournament_Matchup_strategy)
@settings(max_examples=50)
def test_bowlingtournament_matchup_instantiation(instance):
    assert isinstance(instance, bowlingTournament_Matchup)

@given(instance=bowlingTournament_Tournament_strategy)
@settings(max_examples=50)
def test_bowlingtournament_tournament_instantiation(instance):
    assert isinstance(instance, bowlingTournament_Tournament)



@given(instance=bowlingTournament_Tournament_strategy)
def test_bowlingtournament_tournament_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bowlingTournament_Player_strategy)
@settings(max_examples=50)
def test_bowlingtournament_player_instantiation(instance):
    assert isinstance(instance, bowlingTournament_Player)



@given(instance=bowlingTournament_Player_strategy)
def test_bowlingtournament_player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=bowlingTournament_Player_strategy)
def test_bowlingtournament_player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=bowlingTournament_Player_strategy)
def test_bowlingtournament_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bowlingTournament_Player_strategy)
def test_bowlingtournament_player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original

@given(instance=bowlingTournament_League_strategy)
@settings(max_examples=50)
def test_bowlingtournament_league_instantiation(instance):
    assert isinstance(instance, bowlingTournament_League)



@given(instance=bowlingTournament_League_strategy)
def test_bowlingtournament_league_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
