import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PowerUps,
    GameMap,
    Monster,
    Game,
    BomberMan,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_powerups_is_not_abstract():
    assert not inspect.isabstract(PowerUps)


def test_powerups_constructor_exists():
    assert callable(PowerUps.__init__)


def test_powerups_constructor_args():
    sig = inspect.signature(PowerUps.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "speciliaty" in params, "Missing parameter 'speciliaty'"
    assert "locations" in params, "Missing parameter 'locations'"

def test_powerups_has_points():
    assert hasattr(PowerUps, "points")
    descriptor = None
    for klass in PowerUps.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_powerups_has_speciliaty():
    assert hasattr(PowerUps, "speciliaty")
    descriptor = None
    for klass in PowerUps.__mro__:
        if "speciliaty" in klass.__dict__:
            descriptor = klass.__dict__["speciliaty"]
            break
    assert isinstance(descriptor, property)

def test_powerups_has_locations():
    assert hasattr(PowerUps, "locations")
    descriptor = None
    for klass in PowerUps.__mro__:
        if "locations" in klass.__dict__:
            descriptor = klass.__dict__["locations"]
            break
    assert isinstance(descriptor, property)



def test_gamemap_is_not_abstract():
    assert not inspect.isabstract(GameMap)


def test_gamemap_constructor_exists():
    assert callable(GameMap.__init__)


def test_gamemap_constructor_args():
    sig = inspect.signature(GameMap.__init__)
    params = list(sig.parameters.keys())
    assert "poerups" in params, "Missing parameter 'poerups'"
    assert "transitions" in params, "Missing parameter 'transitions'"
    assert "walls" in params, "Missing parameter 'walls'"

def test_gamemap_has_poerups():
    assert hasattr(GameMap, "poerups")
    descriptor = None
    for klass in GameMap.__mro__:
        if "poerups" in klass.__dict__:
            descriptor = klass.__dict__["poerups"]
            break
    assert isinstance(descriptor, property)

def test_gamemap_has_transitions():
    assert hasattr(GameMap, "transitions")
    descriptor = None
    for klass in GameMap.__mro__:
        if "transitions" in klass.__dict__:
            descriptor = klass.__dict__["transitions"]
            break
    assert isinstance(descriptor, property)

def test_gamemap_has_walls():
    assert hasattr(GameMap, "walls")
    descriptor = None
    for klass in GameMap.__mro__:
        if "walls" in klass.__dict__:
            descriptor = klass.__dict__["walls"]
            break
    assert isinstance(descriptor, property)



def test_monster_is_not_abstract():
    assert not inspect.isabstract(Monster)


def test_monster_constructor_exists():
    assert callable(Monster.__init__)


def test_monster_constructor_args():
    sig = inspect.signature(Monster.__init__)
    params = list(sig.parameters.keys())
    assert "lives" in params, "Missing parameter 'lives'"
    assert "location" in params, "Missing parameter 'location'"
    assert "specilization" in params, "Missing parameter 'specilization'"
    assert "type" in params, "Missing parameter 'type'"

def test_monster_has_lives():
    assert hasattr(Monster, "lives")
    descriptor = None
    for klass in Monster.__mro__:
        if "lives" in klass.__dict__:
            descriptor = klass.__dict__["lives"]
            break
    assert isinstance(descriptor, property)

def test_monster_has_location():
    assert hasattr(Monster, "location")
    descriptor = None
    for klass in Monster.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_monster_has_specilization():
    assert hasattr(Monster, "specilization")
    descriptor = None
    for klass in Monster.__mro__:
        if "specilization" in klass.__dict__:
            descriptor = klass.__dict__["specilization"]
            break
    assert isinstance(descriptor, property)

def test_monster_has_type():
    assert hasattr(Monster, "type")
    descriptor = None
    for klass in Monster.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "Timer" in params, "Missing parameter 'Timer'"

def test_game_has_Timer():
    assert hasattr(Game, "Timer")
    descriptor = None
    for klass in Game.__mro__:
        if "Timer" in klass.__dict__:
            descriptor = klass.__dict__["Timer"]
            break
    assert isinstance(descriptor, property)



def test_bomberman_is_not_abstract():
    assert not inspect.isabstract(BomberMan)


def test_bomberman_constructor_exists():
    assert callable(BomberMan.__init__)


def test_bomberman_constructor_args():
    sig = inspect.signature(BomberMan.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "lives" in params, "Missing parameter 'lives'"
    assert "location" in params, "Missing parameter 'location'"

def test_bomberman_has_points():
    assert hasattr(BomberMan, "points")
    descriptor = None
    for klass in BomberMan.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_bomberman_has_lives():
    assert hasattr(BomberMan, "lives")
    descriptor = None
    for klass in BomberMan.__mro__:
        if "lives" in klass.__dict__:
            descriptor = klass.__dict__["lives"]
            break
    assert isinstance(descriptor, property)

def test_bomberman_has_location():
    assert hasattr(BomberMan, "location")
    descriptor = None
    for klass in BomberMan.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)


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
PowerUps_strategy = st.builds(
    PowerUps,
    points=
        st.integers(),
    speciliaty=
        safe_text,
    locations=
        safe_text
)
GameMap_strategy = st.builds(
    GameMap,
    poerups=
        safe_text,
    transitions=
        safe_text,
    walls=
        safe_text
)
Monster_strategy = st.builds(
    Monster,
    lives=
        st.integers(),
    location=
        safe_text,
    specilization=
        safe_text,
    type=
        safe_text
)
Game_strategy = st.builds(
    Game,
    Timer=
        st.integers()
)
BomberMan_strategy = st.builds(
    BomberMan,
    points=
        st.integers(),
    lives=
        st.integers(),
    location=
        safe_text
)

@given(instance=PowerUps_strategy)
@settings(max_examples=50)
def test_powerups_instantiation(instance):
    assert isinstance(instance, PowerUps)



@given(instance=PowerUps_strategy)
def test_powerups_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=PowerUps_strategy)
def test_powerups_speciliaty_setter(instance):
    original = instance.speciliaty
    instance.speciliaty = original
    assert instance.speciliaty == original



@given(instance=PowerUps_strategy)
def test_powerups_locations_setter(instance):
    original = instance.locations
    instance.locations = original
    assert instance.locations == original

@given(instance=GameMap_strategy)
@settings(max_examples=50)
def test_gamemap_instantiation(instance):
    assert isinstance(instance, GameMap)



@given(instance=GameMap_strategy)
def test_gamemap_poerups_setter(instance):
    original = instance.poerups
    instance.poerups = original
    assert instance.poerups == original



@given(instance=GameMap_strategy)
def test_gamemap_transitions_setter(instance):
    original = instance.transitions
    instance.transitions = original
    assert instance.transitions == original



@given(instance=GameMap_strategy)
def test_gamemap_walls_setter(instance):
    original = instance.walls
    instance.walls = original
    assert instance.walls == original

@given(instance=Monster_strategy)
@settings(max_examples=50)
def test_monster_instantiation(instance):
    assert isinstance(instance, Monster)



@given(instance=Monster_strategy)
def test_monster_lives_setter(instance):
    original = instance.lives
    instance.lives = original
    assert instance.lives == original



@given(instance=Monster_strategy)
def test_monster_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Monster_strategy)
def test_monster_specilization_setter(instance):
    original = instance.specilization
    instance.specilization = original
    assert instance.specilization == original



@given(instance=Monster_strategy)
def test_monster_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_Timer_setter(instance):
    original = instance.Timer
    instance.Timer = original
    assert instance.Timer == original

@given(instance=BomberMan_strategy)
@settings(max_examples=50)
def test_bomberman_instantiation(instance):
    assert isinstance(instance, BomberMan)



@given(instance=BomberMan_strategy)
def test_bomberman_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=BomberMan_strategy)
def test_bomberman_lives_setter(instance):
    original = instance.lives
    instance.lives = original
    assert instance.lives == original



@given(instance=BomberMan_strategy)
def test_bomberman_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
