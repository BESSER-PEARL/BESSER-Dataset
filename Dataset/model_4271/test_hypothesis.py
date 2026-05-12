import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bowling_Matchup,
    bowling_Tournament,
    bowling_League,
    bowling_Game,
    bowling_Player,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowling_matchup_is_not_abstract():
    assert not inspect.isabstract(bowling_Matchup)


def test_bowling_matchup_constructor_exists():
    assert callable(bowling_Matchup.__init__)


def test_bowling_matchup_constructor_args():
    sig = inspect.signature(bowling_Matchup.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_bowling_matchup_has_date():
    assert hasattr(bowling_Matchup, "date")
    descriptor = None
    for klass in bowling_Matchup.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_bowling_tournament_is_not_abstract():
    assert not inspect.isabstract(bowling_Tournament)


def test_bowling_tournament_constructor_exists():
    assert callable(bowling_Tournament.__init__)


def test_bowling_tournament_constructor_args():
    sig = inspect.signature(bowling_Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "type" in params, "Missing parameter 'type'"

def test_bowling_tournament_has_title():
    assert hasattr(bowling_Tournament, "title")
    descriptor = None
    for klass in bowling_Tournament.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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



def test_bowling_player_is_not_abstract():
    assert not inspect.isabstract(bowling_Player)


def test_bowling_player_constructor_exists():
    assert callable(bowling_Player.__init__)


def test_bowling_player_constructor_args():
    sig = inspect.signature(bowling_Player.__init__)
    params = list(sig.parameters.keys())
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "eMail" in params, "Missing parameter 'eMail'"
    assert "street" in params, "Missing parameter 'street'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"
    assert "height" in params, "Missing parameter 'height'"
    assert "streetNumber" in params, "Missing parameter 'streetNumber'"

def test_bowling_player_has_dateOfBirth():
    assert hasattr(bowling_Player, "dateOfBirth")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_eMail():
    assert hasattr(bowling_Player, "eMail")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "eMail" in klass.__dict__:
            descriptor = klass.__dict__["eMail"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_street():
    assert hasattr(bowling_Player, "street")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
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

def test_bowling_player_has_height():
    assert hasattr(bowling_Player, "height")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_streetNumber():
    assert hasattr(bowling_Player, "streetNumber")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "streetNumber" in klass.__dict__:
            descriptor = klass.__dict__["streetNumber"]
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
bowling_Matchup_strategy = st.builds(
    bowling_Matchup,
    date=
        st.dates()
)
bowling_Tournament_strategy = st.builds(
    bowling_Tournament,
    title=
        safe_text,
    type=
        safe_text
)
bowling_League_strategy = st.builds(
    bowling_League,
    name=
        safe_text
)
bowling_Game_strategy = st.builds(
    bowling_Game,
    frames=
        st.integers()
)
bowling_Player_strategy = st.builds(
    bowling_Player,
    dateOfBirth=
        st.dates(),
    eMail=
        safe_text,
    street=
        safe_text,
    name=
        safe_text,
    isProfessional=
        st.booleans(),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    streetNumber=
        st.integers()
)

@given(instance=bowling_Matchup_strategy)
@settings(max_examples=50)
def test_bowling_matchup_instantiation(instance):
    assert isinstance(instance, bowling_Matchup)



@given(instance=bowling_Matchup_strategy)
def test_bowling_matchup_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=bowling_Tournament_strategy)
@settings(max_examples=50)
def test_bowling_tournament_instantiation(instance):
    assert isinstance(instance, bowling_Tournament)



@given(instance=bowling_Tournament_strategy)
def test_bowling_tournament_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



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

@given(instance=bowling_Game_strategy)
@settings(max_examples=50)
def test_bowling_game_instantiation(instance):
    assert isinstance(instance, bowling_Game)



@given(instance=bowling_Game_strategy)
def test_bowling_game_frames_setter(instance):
    original = instance.frames
    instance.frames = original
    assert instance.frames == original

@given(instance=bowling_Player_strategy)
@settings(max_examples=50)
def test_bowling_player_instantiation(instance):
    assert isinstance(instance, bowling_Player)



@given(instance=bowling_Player_strategy)
def test_bowling_player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_eMail_setter(instance):
    original = instance.eMail
    instance.eMail = original
    assert instance.eMail == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



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



@given(instance=bowling_Player_strategy)
def test_bowling_player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_streetNumber_setter(instance):
    original = instance.streetNumber
    instance.streetNumber = original
    assert instance.streetNumber == original
