import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bowling::Matchup,
    bowling::Tournament,
    bowling::League,
    bowling::Game,
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
    assert "date" in params, "Missing parameter 'date'"

def test_bowling::matchup_has_date():
    assert hasattr(bowling::Matchup, "date")
    descriptor = None
    for klass in bowling::Matchup.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_bowling::tournament_is_not_abstract():
    assert not inspect.isabstract(bowling::Tournament)


def test_bowling::tournament_constructor_exists():
    assert callable(bowling::Tournament.__init__)


def test_bowling::tournament_constructor_args():
    sig = inspect.signature(bowling::Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "title" in params, "Missing parameter 'title'"

def test_bowling::tournament_has_type():
    assert hasattr(bowling::Tournament, "type")
    descriptor = None
    for klass in bowling::Tournament.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bowling::tournament_has_title():
    assert hasattr(bowling::Tournament, "title")
    descriptor = None
    for klass in bowling::Tournament.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
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



def test_bowling::player_is_not_abstract():
    assert not inspect.isabstract(bowling::Player)


def test_bowling::player_constructor_exists():
    assert callable(bowling::Player.__init__)


def test_bowling::player_constructor_args():
    sig = inspect.signature(bowling::Player.__init__)
    params = list(sig.parameters.keys())
    assert "street" in params, "Missing parameter 'street'"
    assert "streetNumber" in params, "Missing parameter 'streetNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"
    assert "height" in params, "Missing parameter 'height'"
    assert "eMail" in params, "Missing parameter 'eMail'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"

def test_bowling::player_has_street():
    assert hasattr(bowling::Player, "street")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_bowling::player_has_streetNumber():
    assert hasattr(bowling::Player, "streetNumber")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "streetNumber" in klass.__dict__:
            descriptor = klass.__dict__["streetNumber"]
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

def test_bowling::player_has_eMail():
    assert hasattr(bowling::Player, "eMail")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "eMail" in klass.__dict__:
            descriptor = klass.__dict__["eMail"]
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
bowling::Matchup_strategy = st.builds(
    bowling::Matchup,
    date=
        st.dates()
)
bowling::Tournament_strategy = st.builds(
    bowling::Tournament,
    type=
        safe_text,
    title=
        safe_text
)
bowling::League_strategy = st.builds(
    bowling::League,
    name=
        safe_text
)
bowling::Game_strategy = st.builds(
    bowling::Game,
    frames=
        st.integers()
)
bowling::Player_strategy = st.builds(
    bowling::Player,
    street=
        safe_text,
    streetNumber=
        st.integers(),
    name=
        safe_text,
    isProfessional=
        st.booleans(),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    eMail=
        safe_text,
    dateOfBirth=
        st.dates()
)

@given(instance=bowling::Matchup_strategy)
@settings(max_examples=50)
def test_bowling::matchup_instantiation(instance):
    assert isinstance(instance, bowling::Matchup)

@given(instance=bowling::Matchup_strategy)
def test_bowling::matchup_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=bowling::Matchup_strategy)
def test_bowling::matchup_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

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

@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bowling::Tournament_strategy)
def test_bowling::tournament_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

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

@given(instance=bowling::Player_strategy)
@settings(max_examples=50)
def test_bowling::player_instantiation(instance):
    assert isinstance(instance, bowling::Player)

@given(instance=bowling::Player_strategy)
def test_bowling::player_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=bowling::Player_strategy)
def test_bowling::player_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original

@given(instance=bowling::Player_strategy)
def test_bowling::player_streetNumber_type(instance):
    assert isinstance(instance.streetNumber, int)


@given(instance=bowling::Player_strategy)
def test_bowling::player_streetNumber_setter(instance):
    original = instance.streetNumber
    instance.streetNumber = original
    assert instance.streetNumber == original

@given(instance=bowling::Player_strategy)
def test_bowling::player_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::Player_strategy)
def test_bowling::player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_bowling::player_eMail_type(instance):
    assert isinstance(instance.eMail, str)


@given(instance=bowling::Player_strategy)
def test_bowling::player_eMail_setter(instance):
    original = instance.eMail
    instance.eMail = original
    assert instance.eMail == original

@given(instance=bowling::Player_strategy)
def test_bowling::player_dateOfBirth_type(instance):
    assert isinstance(instance.dateOfBirth, date)


@given(instance=bowling::Player_strategy)
def test_bowling::player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original
