import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Game,
    Player,
    Board,
    Boat,
    Coordinate,
    Direction,
    CoordState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "done" in params, "Missing parameter 'done'"
    assert "p1" in params, "Missing parameter 'p1'"
    assert "p2" in params, "Missing parameter 'p2'"

def test_game_has_done():
    assert hasattr(Game, "done")
    descriptor = None
    for klass in Game.__mro__:
        if "done" in klass.__dict__:
            descriptor = klass.__dict__["done"]
            break
    assert isinstance(descriptor, property)

def test_game_has_p1():
    assert hasattr(Game, "p1")
    descriptor = None
    for klass in Game.__mro__:
        if "p1" in klass.__dict__:
            descriptor = klass.__dict__["p1"]
            break
    assert isinstance(descriptor, property)

def test_game_has_p2():
    assert hasattr(Game, "p2")
    descriptor = None
    for klass in Game.__mro__:
        if "p2" in klass.__dict__:
            descriptor = klass.__dict__["p2"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "turn" in params, "Missing parameter 'turn'"
    assert "name" in params, "Missing parameter 'name'"
    assert "won" in params, "Missing parameter 'won'"

def test_player_has_turn():
    assert hasattr(Player, "turn")
    descriptor = None
    for klass in Player.__mro__:
        if "turn" in klass.__dict__:
            descriptor = klass.__dict__["turn"]
            break
    assert isinstance(descriptor, property)

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_has_won():
    assert hasattr(Player, "won")
    descriptor = None
    for klass in Player.__mro__:
        if "won" in klass.__dict__:
            descriptor = klass.__dict__["won"]
            break
    assert isinstance(descriptor, property)



def test_board_is_not_abstract():
    assert not inspect.isabstract(Board)


def test_board_constructor_exists():
    assert callable(Board.__init__)


def test_board_constructor_args():
    sig = inspect.signature(Board.__init__)
    params = list(sig.parameters.keys())
    assert "submarine" in params, "Missing parameter 'submarine'"
    assert "destroyer" in params, "Missing parameter 'destroyer'"
    assert "aircraftCarrier" in params, "Missing parameter 'aircraftCarrier'"
    assert "patrolBoat" in params, "Missing parameter 'patrolBoat'"
    assert "battleship" in params, "Missing parameter 'battleship'"

def test_board_has_submarine():
    assert hasattr(Board, "submarine")
    descriptor = None
    for klass in Board.__mro__:
        if "submarine" in klass.__dict__:
            descriptor = klass.__dict__["submarine"]
            break
    assert isinstance(descriptor, property)

def test_board_has_destroyer():
    assert hasattr(Board, "destroyer")
    descriptor = None
    for klass in Board.__mro__:
        if "destroyer" in klass.__dict__:
            descriptor = klass.__dict__["destroyer"]
            break
    assert isinstance(descriptor, property)

def test_board_has_aircraftCarrier():
    assert hasattr(Board, "aircraftCarrier")
    descriptor = None
    for klass in Board.__mro__:
        if "aircraftCarrier" in klass.__dict__:
            descriptor = klass.__dict__["aircraftCarrier"]
            break
    assert isinstance(descriptor, property)

def test_board_has_patrolBoat():
    assert hasattr(Board, "patrolBoat")
    descriptor = None
    for klass in Board.__mro__:
        if "patrolBoat" in klass.__dict__:
            descriptor = klass.__dict__["patrolBoat"]
            break
    assert isinstance(descriptor, property)

def test_board_has_battleship():
    assert hasattr(Board, "battleship")
    descriptor = None
    for klass in Board.__mro__:
        if "battleship" in klass.__dict__:
            descriptor = klass.__dict__["battleship"]
            break
    assert isinstance(descriptor, property)



def test_boat_is_not_abstract():
    assert not inspect.isabstract(Boat)


def test_boat_constructor_exists():
    assert callable(Boat.__init__)


def test_boat_constructor_args():
    sig = inspect.signature(Boat.__init__)
    params = list(sig.parameters.keys())
    assert "startCoord" in params, "Missing parameter 'startCoord'"
    assert "length" in params, "Missing parameter 'length'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "MAX_LENGTH" in params, "Missing parameter 'MAX_LENGTH'"

def test_boat_has_startCoord():
    assert hasattr(Boat, "startCoord")
    descriptor = None
    for klass in Boat.__mro__:
        if "startCoord" in klass.__dict__:
            descriptor = klass.__dict__["startCoord"]
            break
    assert isinstance(descriptor, property)

def test_boat_has_length():
    assert hasattr(Boat, "length")
    descriptor = None
    for klass in Boat.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_boat_has_direction():
    assert hasattr(Boat, "direction")
    descriptor = None
    for klass in Boat.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_boat_has_MAX_LENGTH():
    assert hasattr(Boat, "MAX_LENGTH")
    descriptor = None
    for klass in Boat.__mro__:
        if "MAX_LENGTH" in klass.__dict__:
            descriptor = klass.__dict__["MAX_LENGTH"]
            break
    assert isinstance(descriptor, property)



def test_coordinate_is_not_abstract():
    assert not inspect.isabstract(Coordinate)


def test_coordinate_constructor_exists():
    assert callable(Coordinate.__init__)


def test_coordinate_constructor_args():
    sig = inspect.signature(Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "state" in params, "Missing parameter 'state'"
    assert "y" in params, "Missing parameter 'y'"

def test_coordinate_has_x():
    assert hasattr(Coordinate, "x")
    descriptor = None
    for klass in Coordinate.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_coordinate_has_state():
    assert hasattr(Coordinate, "state")
    descriptor = None
    for klass in Coordinate.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_coordinate_has_y():
    assert hasattr(Coordinate, "y")
    descriptor = None
    for klass in Coordinate.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_coordstate_exists():
    # Check that the Enumeration exists
    assert CoordState is not None

def test_coordstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CoordState]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CoordState"


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
Game_strategy = st.builds(
    Game,
    done=
        st.booleans(),
    p1=
        st.none(),
    p2=
        st.none()
)
Player_strategy = st.builds(
    Player,
    turn=
        st.booleans(),
    name=
        safe_text,
    won=
        st.booleans()
)
Board_strategy = st.builds(
    Board,
    submarine=
        st.booleans(),
    destroyer=
        st.booleans(),
    aircraftCarrier=
        st.booleans(),
    patrolBoat=
        st.booleans(),
    battleship=
        st.booleans()
)
Boat_strategy = st.builds(
    Boat,
    startCoord=
        st.none(),
    length=
        st.integers(),
    direction=
        st.none(),
    MAX_LENGTH=
        st.integers()
)
Coordinate_strategy = st.builds(
    Coordinate,
    x=
        st.integers(),
    state=
        st.none(),
    y=
        st.integers()
)

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_done_setter(instance):
    original = instance.done
    instance.done = original
    assert instance.done == original



@given(instance=Game_strategy)
def test_game_p1_setter(instance):
    original = instance.p1
    instance.p1 = original
    assert instance.p1 == original



@given(instance=Game_strategy)
def test_game_p2_setter(instance):
    original = instance.p2
    instance.p2 = original
    assert instance.p2 == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_turn_setter(instance):
    original = instance.turn
    instance.turn = original
    assert instance.turn == original



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_player_won_setter(instance):
    original = instance.won
    instance.won = original
    assert instance.won == original

@given(instance=Board_strategy)
@settings(max_examples=50)
def test_board_instantiation(instance):
    assert isinstance(instance, Board)



@given(instance=Board_strategy)
def test_board_submarine_setter(instance):
    original = instance.submarine
    instance.submarine = original
    assert instance.submarine == original



@given(instance=Board_strategy)
def test_board_destroyer_setter(instance):
    original = instance.destroyer
    instance.destroyer = original
    assert instance.destroyer == original



@given(instance=Board_strategy)
def test_board_aircraftCarrier_setter(instance):
    original = instance.aircraftCarrier
    instance.aircraftCarrier = original
    assert instance.aircraftCarrier == original



@given(instance=Board_strategy)
def test_board_patrolBoat_setter(instance):
    original = instance.patrolBoat
    instance.patrolBoat = original
    assert instance.patrolBoat == original



@given(instance=Board_strategy)
def test_board_battleship_setter(instance):
    original = instance.battleship
    instance.battleship = original
    assert instance.battleship == original

@given(instance=Boat_strategy)
@settings(max_examples=50)
def test_boat_instantiation(instance):
    assert isinstance(instance, Boat)



@given(instance=Boat_strategy)
def test_boat_startCoord_setter(instance):
    original = instance.startCoord
    instance.startCoord = original
    assert instance.startCoord == original



@given(instance=Boat_strategy)
def test_boat_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=Boat_strategy)
def test_boat_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=Boat_strategy)
def test_boat_MAX_LENGTH_setter(instance):
    original = instance.MAX_LENGTH
    instance.MAX_LENGTH = original
    assert instance.MAX_LENGTH == original

@given(instance=Coordinate_strategy)
@settings(max_examples=50)
def test_coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)



@given(instance=Coordinate_strategy)
def test_coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Coordinate_strategy)
def test_coordinate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Coordinate_strategy)
def test_coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original
