import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bowling_Playerlist,
    bowling_Game,
    bowling_Tournament,
    bowling_Matchup,
    bowling_Player,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowling_playerlist_is_not_abstract():
    assert not inspect.isabstract(bowling_Playerlist)


def test_bowling_playerlist_constructor_exists():
    assert callable(bowling_Playerlist.__init__)


def test_bowling_playerlist_constructor_args():
    sig = inspect.signature(bowling_Playerlist.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowling_playerlist_has_name():
    assert hasattr(bowling_Playerlist, "name")
    descriptor = None
    for klass in bowling_Playerlist.__mro__:
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
    assert "date" in params, "Missing parameter 'date'"

def test_bowling_game_has_frames():
    assert hasattr(bowling_Game, "frames")
    descriptor = None
    for klass in bowling_Game.__mro__:
        if "frames" in klass.__dict__:
            descriptor = klass.__dict__["frames"]
            break
    assert isinstance(descriptor, property)

def test_bowling_game_has_date():
    assert hasattr(bowling_Game, "date")
    descriptor = None
    for klass in bowling_Game.__mro__:
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
    assert "type" in params, "Missing parameter 'type'"
    assert "title" in params, "Missing parameter 'title'"

def test_bowling_tournament_has_type():
    assert hasattr(bowling_Tournament, "type")
    descriptor = None
    for klass in bowling_Tournament.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bowling_tournament_has_title():
    assert hasattr(bowling_Tournament, "title")
    descriptor = None
    for klass in bowling_Tournament.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bowling_matchup_is_not_abstract():
    assert not inspect.isabstract(bowling_Matchup)


def test_bowling_matchup_constructor_exists():
    assert callable(bowling_Matchup.__init__)


def test_bowling_matchup_constructor_args():
    sig = inspect.signature(bowling_Matchup.__init__)
    params = list(sig.parameters.keys())



def test_bowling_player_is_not_abstract():
    assert not inspect.isabstract(bowling_Player)


def test_bowling_player_constructor_exists():
    assert callable(bowling_Player.__init__)


def test_bowling_player_constructor_args():
    sig = inspect.signature(bowling_Player.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "height" in params, "Missing parameter 'height'"
    assert "city" in params, "Missing parameter 'city'"
    assert "streetnumber" in params, "Missing parameter 'streetnumber'"
    assert "street" in params, "Missing parameter 'street'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"

def test_bowling_player_has_lastname():
    assert hasattr(bowling_Player, "lastname")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_firstname():
    assert hasattr(bowling_Player, "firstname")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
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

def test_bowling_player_has_city():
    assert hasattr(bowling_Player, "city")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_bowling_player_has_streetnumber():
    assert hasattr(bowling_Player, "streetnumber")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "streetnumber" in klass.__dict__:
            descriptor = klass.__dict__["streetnumber"]
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

def test_bowling_player_has_dateOfBirth():
    assert hasattr(bowling_Player, "dateOfBirth")
    descriptor = None
    for klass in bowling_Player.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
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
bowling_Playerlist_strategy = st.builds(
    bowling_Playerlist,
    name=
        safe_text
)
bowling_Game_strategy = st.builds(
    bowling_Game,
    frames=
        st.integers(),
    date=
        st.dates()
)
bowling_Tournament_strategy = st.builds(
    bowling_Tournament,
    type=
        safe_text,
    title=
        safe_text
)
bowling_Matchup_strategy = st.builds(
    bowling_Matchup,
)
bowling_Player_strategy = st.builds(
    bowling_Player,
    lastname=
        safe_text,
    firstname=
        safe_text,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    city=
        safe_text,
    streetnumber=
        st.integers(),
    street=
        safe_text,
    dateOfBirth=
        st.dates(),
    isProfessional=
        st.booleans()
)

@given(instance=bowling_Playerlist_strategy)
@settings(max_examples=50)
def test_bowling_playerlist_instantiation(instance):
    assert isinstance(instance, bowling_Playerlist)



@given(instance=bowling_Playerlist_strategy)
def test_bowling_playerlist_name_setter(instance):
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



@given(instance=bowling_Game_strategy)
def test_bowling_game_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=bowling_Tournament_strategy)
@settings(max_examples=50)
def test_bowling_tournament_instantiation(instance):
    assert isinstance(instance, bowling_Tournament)



@given(instance=bowling_Tournament_strategy)
def test_bowling_tournament_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=bowling_Tournament_strategy)
def test_bowling_tournament_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bowling_Matchup_strategy)
@settings(max_examples=50)
def test_bowling_matchup_instantiation(instance):
    assert isinstance(instance, bowling_Matchup)

@given(instance=bowling_Player_strategy)
@settings(max_examples=50)
def test_bowling_player_instantiation(instance):
    assert isinstance(instance, bowling_Player)



@given(instance=bowling_Player_strategy)
def test_bowling_player_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_streetnumber_setter(instance):
    original = instance.streetnumber
    instance.streetnumber = original
    assert instance.streetnumber == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=bowling_Player_strategy)
def test_bowling_player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original
