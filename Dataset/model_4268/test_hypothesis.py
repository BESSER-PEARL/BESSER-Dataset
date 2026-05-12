import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bowling_Game,
    bowling_Matchup,
    bowling_Tournament,
    bowling_League,
    bowling_Player,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowling_game_is_not_abstract():
    assert not inspect.isabstract(bowling_Game)


def test_bowling_game_constructor_exists():
    assert callable(bowling_Game.__init__)


def test_bowling_game_constructor_args():
    sig = inspect.signature(bowling_Game.__init__)
    params = list(sig.parameters.keys())
    assert "frames" in params, "Missing parameter 'frames'"

def test_bowling_game_has_frames():
    assert hasattr(bowling_Game, "frames")
    descriptor = None
    for klass in bowling_Game.__mro__:
        if "frames" in klass.__dict__:
            descriptor = klass.__dict__["frames"]
            break
    assert isinstance(descriptor, property)



def test_bowling_matchup_is_not_abstract():
    assert not inspect.isabstract(bowling_Matchup)


def test_bowling_matchup_constructor_exists():
    assert callable(bowling_Matchup.__init__)


def test_bowling_matchup_constructor_args():
    sig = inspect.signature(bowling_Matchup.__init__)
    params = list(sig.parameters.keys())



def test_bowling_tournament_is_not_abstract():
    assert not inspect.isabstract(bowling_Tournament)


def test_bowling_tournament_constructor_exists():
    assert callable(bowling_Tournament.__init__)


def test_bowling_tournament_constructor_args():
    sig = inspect.signature(bowling_Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_bowling_tournament_has_type():
    assert hasattr(bowling_Tournament, "type")
    descriptor = None
    for klass in bowling_Tournament.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bowling_league_is_not_abstract():
    assert not inspect.isabstract(bowling_League)


def test_bowling_league_constructor_exists():
    assert callable(bowling_League.__init__)


def test_bowling_league_constructor_args():
    sig = inspect.signature(bowling_League.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowling_league_has_name():
    assert hasattr(bowling_League, "name")
    descriptor = None
    for klass in bowling_League.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bowling_player_is_not_abstract():
    assert not inspect.isabstract(bowling_Player)


def test_bowling_player_constructor_exists():
    assert callable(bowling_Player.__init__)


def test_bowling_player_constructor_args():
    sig = inspect.signature(bowling_Player.__init__)
    params = list(sig.parameters.keys())
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "height" in params, "Missing parameter 'height'"

def test_bowling_player_has_isProfessional():
    assert hasattr(bowling_Player, "isProfessional")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "isProfessional" in klass.__dict__:
            descriptor = klass.__dict__["isProfessional"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_name():
    assert hasattr(bowling_Player, "name")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_dateOfBirth():
    assert hasattr(bowling_Player, "dateOfBirth")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_height():
    assert hasattr(bowling_Player, "height")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
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
bowling_Game_strategy = st.builds(
    bowling_Game,
    frames=
        st.integers()
)
bowling_Matchup_strategy = st.builds(
    bowling_Matchup,
)
bowling_Tournament_strategy = st.builds(
    bowling_Tournament,
    type=
        safe_text
)
bowling_League_strategy = st.builds(
    bowling_League,
    name=
        safe_text
)
bowling_Player_strategy = st.builds(
    bowling_Player,
    isProfessional=
        st.booleans(),
    name=
        safe_text,
    dateOfBirth=
        st.dates(),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=bowling_Game_strategy)
@settings(max_examples=50)
def test_bowling_game_instantiation(instance):
    assert isinstance(instance, bowling_Game)



@given(instance=bowling_Game_strategy)
def test_bowling_game_frames_setter(instance):
    original = instance.frames
    instance.frames = original
    assert instance.frames == original

@given(instance=bowling_Matchup_strategy)
@settings(max_examples=50)
def test_bowling_matchup_instantiation(instance):
    assert isinstance(instance, bowling_Matchup)

@given(instance=bowling_Tournament_strategy)
@settings(max_examples=50)
def test_bowling_tournament_instantiation(instance):
    assert isinstance(instance, bowling_Tournament)



@given(instance=bowling_Tournament_strategy)
def test_bowling_tournament_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bowling_League_strategy)
@settings(max_examples=50)
def test_bowling_league_instantiation(instance):
    assert isinstance(instance, bowling_League)



@given(instance=bowling_League_strategy)
def test_bowling_league_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling_Player_strategy)
@settings(max_examples=50)
def test_bowling_player_instantiation(instance):
    assert isinstance(instance, bowling_Player)



@given(instance=bowling_Player_strategy)
def test_bowling_player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original
