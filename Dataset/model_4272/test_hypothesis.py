import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bowling_Alley,
    bowling_Lane,
    bowling_Player,
    bowling_Game,
    bowling_Matchup,
    bowling_Tournament,
    bowling_League,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowling_alley_is_not_abstract():
    assert not inspect.isabstract(bowling_Alley)


def test_bowling_alley_constructor_exists():
    assert callable(bowling_Alley.__init__)


def test_bowling_alley_constructor_args():
    sig = inspect.signature(bowling_Alley.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowling_alley_has_name():
    assert hasattr(bowling_Alley, "name")
    descriptor = None
    for klass in bowling_Alley.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bowling_lane_is_not_abstract():
    assert not inspect.isabstract(bowling_Lane)


def test_bowling_lane_constructor_exists():
    assert callable(bowling_Lane.__init__)


def test_bowling_lane_constructor_args():
    sig = inspect.signature(bowling_Lane.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_bowling_lane_has_number():
    assert hasattr(bowling_Lane, "number")
    descriptor = None
    for klass in bowling_Lane.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_bowling_player_is_not_abstract():
    assert not inspect.isabstract(bowling_Player)


def test_bowling_player_constructor_exists():
    assert callable(bowling_Player.__init__)


def test_bowling_player_constructor_args():
    sig = inspect.signature(bowling_Player.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"

def test_bowling_player_has_height():
    assert hasattr(bowling_Player, "height")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
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

def test_bowling_player_has_name():
    assert hasattr(bowling_Player, "name")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_isProfessional():
    assert hasattr(bowling_Player, "isProfessional")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "isProfessional" in klass.__dict__:
            descriptor = klass.__dict__["isProfessional"]
            break
    assert isinstance(descriptor, property)



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
    assert "name" in params, "Missing parameter 'name'"

def test_bowling_matchup_has_name():
    assert hasattr(bowling_Matchup, "name")
    descriptor = None
    for klass in bowling_Matchup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bowling_tournament_is_not_abstract():
    assert not inspect.isabstract(bowling_Tournament)


def test_bowling_tournament_constructor_exists():
    assert callable(bowling_Tournament.__init__)


def test_bowling_tournament_constructor_args():
    sig = inspect.signature(bowling_Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_bowling_tournament_has_name():
    assert hasattr(bowling_Tournament, "name")
    descriptor = None
    for klass in bowling_Tournament.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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
bowling_Alley_strategy = st.builds(
    bowling_Alley,
    name=
        safe_text
)
bowling_Lane_strategy = st.builds(
    bowling_Lane,
    number=
        st.integers()
)
bowling_Player_strategy = st.builds(
    bowling_Player,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dateOfBirth=
        st.dates(),
    name=
        safe_text,
    isProfessional=
        st.booleans()
)
bowling_Game_strategy = st.builds(
    bowling_Game,
    frames=
        st.integers()
)
bowling_Matchup_strategy = st.builds(
    bowling_Matchup,
    name=
        safe_text
)
bowling_Tournament_strategy = st.builds(
    bowling_Tournament,
    name=
        safe_text,
    type=
        safe_text
)
bowling_League_strategy = st.builds(
    bowling_League,
    name=
        safe_text
)

@given(instance=bowling_Alley_strategy)
@settings(max_examples=50)
def test_bowling_alley_instantiation(instance):
    assert isinstance(instance, bowling_Alley)



@given(instance=bowling_Alley_strategy)
def test_bowling_alley_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling_Lane_strategy)
@settings(max_examples=50)
def test_bowling_lane_instantiation(instance):
    assert isinstance(instance, bowling_Lane)



@given(instance=bowling_Lane_strategy)
def test_bowling_lane_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bowling_Player_strategy)
@settings(max_examples=50)
def test_bowling_player_instantiation(instance):
    assert isinstance(instance, bowling_Player)



@given(instance=bowling_Player_strategy)
def test_bowling_player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original

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



@given(instance=bowling_Matchup_strategy)
def test_bowling_matchup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling_Tournament_strategy)
@settings(max_examples=50)
def test_bowling_tournament_instantiation(instance):
    assert isinstance(instance, bowling_Tournament)



@given(instance=bowling_Tournament_strategy)
def test_bowling_tournament_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



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
