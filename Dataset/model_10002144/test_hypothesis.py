import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Slot,
    Pawn,
    King,
    Queen,
    Rook,
    Bishop,
    Knight,
    Piece,
    Chess,
    Level,
    ParkingSpot,
    ParkingLot,
    ParkingSpotType,
    PieceColor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_slot_is_not_abstract():
    assert not inspect.isabstract(Slot)


def test_slot_constructor_exists():
    assert callable(Slot.__init__)


def test_slot_constructor_args():
    sig = inspect.signature(Slot.__init__)
    params = list(sig.parameters.keys())
    assert "Occupied" in params, "Missing parameter 'Occupied'"
    assert "piece" in params, "Missing parameter 'piece'"

def test_slot_has_Occupied():
    assert hasattr(Slot, "Occupied")
    descriptor = None
    for klass in Slot.__mro__:
        if "Occupied" in klass.__dict__:
            descriptor = klass.__dict__["Occupied"]
            break
    assert isinstance(descriptor, property)

def test_slot_has_piece():
    assert hasattr(Slot, "piece")
    descriptor = None
    for klass in Slot.__mro__:
        if "piece" in klass.__dict__:
            descriptor = klass.__dict__["piece"]
            break
    assert isinstance(descriptor, property)



def test_pawn_is_not_abstract():
    assert not inspect.isabstract(Pawn)


def test_pawn_constructor_exists():
    assert callable(Pawn.__init__)


def test_pawn_constructor_args():
    sig = inspect.signature(Pawn.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"

def test_pawn_has_pieceColor():
    assert hasattr(Pawn, "pieceColor")
    descriptor = None
    for klass in Pawn.__mro__:
        if "pieceColor" in klass.__dict__:
            descriptor = klass.__dict__["pieceColor"]
            break
    assert isinstance(descriptor, property)



def test_king_is_not_abstract():
    assert not inspect.isabstract(King)


def test_king_constructor_exists():
    assert callable(King.__init__)


def test_king_constructor_args():
    sig = inspect.signature(King.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"

def test_king_has_pieceColor():
    assert hasattr(King, "pieceColor")
    descriptor = None
    for klass in King.__mro__:
        if "pieceColor" in klass.__dict__:
            descriptor = klass.__dict__["pieceColor"]
            break
    assert isinstance(descriptor, property)



def test_queen_is_not_abstract():
    assert not inspect.isabstract(Queen)


def test_queen_constructor_exists():
    assert callable(Queen.__init__)


def test_queen_constructor_args():
    sig = inspect.signature(Queen.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"

def test_queen_has_pieceColor():
    assert hasattr(Queen, "pieceColor")
    descriptor = None
    for klass in Queen.__mro__:
        if "pieceColor" in klass.__dict__:
            descriptor = klass.__dict__["pieceColor"]
            break
    assert isinstance(descriptor, property)



def test_rook_is_not_abstract():
    assert not inspect.isabstract(Rook)


def test_rook_constructor_exists():
    assert callable(Rook.__init__)


def test_rook_constructor_args():
    sig = inspect.signature(Rook.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"

def test_rook_has_pieceColor():
    assert hasattr(Rook, "pieceColor")
    descriptor = None
    for klass in Rook.__mro__:
        if "pieceColor" in klass.__dict__:
            descriptor = klass.__dict__["pieceColor"]
            break
    assert isinstance(descriptor, property)



def test_bishop_is_not_abstract():
    assert not inspect.isabstract(Bishop)


def test_bishop_constructor_exists():
    assert callable(Bishop.__init__)


def test_bishop_constructor_args():
    sig = inspect.signature(Bishop.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"

def test_bishop_has_pieceColor():
    assert hasattr(Bishop, "pieceColor")
    descriptor = None
    for klass in Bishop.__mro__:
        if "pieceColor" in klass.__dict__:
            descriptor = klass.__dict__["pieceColor"]
            break
    assert isinstance(descriptor, property)



def test_knight_is_not_abstract():
    assert not inspect.isabstract(Knight)


def test_knight_constructor_exists():
    assert callable(Knight.__init__)


def test_knight_constructor_args():
    sig = inspect.signature(Knight.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"

def test_knight_has_pieceColor():
    assert hasattr(Knight, "pieceColor")
    descriptor = None
    for klass in Knight.__mro__:
        if "pieceColor" in klass.__dict__:
            descriptor = klass.__dict__["pieceColor"]
            break
    assert isinstance(descriptor, property)



def test_piece_is_not_abstract():
    assert not inspect.isabstract(Piece)


def test_piece_constructor_exists():
    assert callable(Piece.__init__)


def test_piece_constructor_args():
    sig = inspect.signature(Piece.__init__)
    params = list(sig.parameters.keys())
    assert "pieceColor" in params, "Missing parameter 'pieceColor'"

def test_piece_has_pieceColor():
    assert hasattr(Piece, "pieceColor")
    descriptor = None
    for klass in Piece.__mro__:
        if "pieceColor" in klass.__dict__:
            descriptor = klass.__dict__["pieceColor"]
            break
    assert isinstance(descriptor, property)



def test_chess_is_not_abstract():
    assert not inspect.isabstract(Chess)


def test_chess_constructor_exists():
    assert callable(Chess.__init__)


def test_chess_constructor_args():
    sig = inspect.signature(Chess.__init__)
    params = list(sig.parameters.keys())
    assert "board" in params, "Missing parameter 'board'"

def test_chess_has_board():
    assert hasattr(Chess, "board")
    descriptor = None
    for klass in Chess.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)



def test_level_is_not_abstract():
    assert not inspect.isabstract(Level)


def test_level_constructor_exists():
    assert callable(Level.__init__)


def test_level_constructor_args():
    sig = inspect.signature(Level.__init__)
    params = list(sig.parameters.keys())
    assert "numofSpots" in params, "Missing parameter 'numofSpots'"
    assert "levelId" in params, "Missing parameter 'levelId'"
    assert "parkingSpots" in params, "Missing parameter 'parkingSpots'"

def test_level_has_numofSpots():
    assert hasattr(Level, "numofSpots")
    descriptor = None
    for klass in Level.__mro__:
        if "numofSpots" in klass.__dict__:
            descriptor = klass.__dict__["numofSpots"]
            break
    assert isinstance(descriptor, property)

def test_level_has_levelId():
    assert hasattr(Level, "levelId")
    descriptor = None
    for klass in Level.__mro__:
        if "levelId" in klass.__dict__:
            descriptor = klass.__dict__["levelId"]
            break
    assert isinstance(descriptor, property)

def test_level_has_parkingSpots():
    assert hasattr(Level, "parkingSpots")
    descriptor = None
    for klass in Level.__mro__:
        if "parkingSpots" in klass.__dict__:
            descriptor = klass.__dict__["parkingSpots"]
            break
    assert isinstance(descriptor, property)



def test_parkingspot_is_not_abstract():
    assert not inspect.isabstract(ParkingSpot)


def test_parkingspot_constructor_exists():
    assert callable(ParkingSpot.__init__)


def test_parkingspot_constructor_args():
    sig = inspect.signature(ParkingSpot.__init__)
    params = list(sig.parameters.keys())
    assert "spotType" in params, "Missing parameter 'spotType'"
    assert "parkingSpotId" in params, "Missing parameter 'parkingSpotId'"
    assert "occupied" in params, "Missing parameter 'occupied'"

def test_parkingspot_has_spotType():
    assert hasattr(ParkingSpot, "spotType")
    descriptor = None
    for klass in ParkingSpot.__mro__:
        if "spotType" in klass.__dict__:
            descriptor = klass.__dict__["spotType"]
            break
    assert isinstance(descriptor, property)

def test_parkingspot_has_parkingSpotId():
    assert hasattr(ParkingSpot, "parkingSpotId")
    descriptor = None
    for klass in ParkingSpot.__mro__:
        if "parkingSpotId" in klass.__dict__:
            descriptor = klass.__dict__["parkingSpotId"]
            break
    assert isinstance(descriptor, property)

def test_parkingspot_has_occupied():
    assert hasattr(ParkingSpot, "occupied")
    descriptor = None
    for klass in ParkingSpot.__mro__:
        if "occupied" in klass.__dict__:
            descriptor = klass.__dict__["occupied"]
            break
    assert isinstance(descriptor, property)



def test_parkinglot_is_not_abstract():
    assert not inspect.isabstract(ParkingLot)


def test_parkinglot_constructor_exists():
    assert callable(ParkingLot.__init__)


def test_parkinglot_constructor_args():
    sig = inspect.signature(ParkingLot.__init__)
    params = list(sig.parameters.keys())
    assert "hours" in params, "Missing parameter 'hours'"
    assert "numOfLevels" in params, "Missing parameter 'numOfLevels'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "spotsOccupied" in params, "Missing parameter 'spotsOccupied'"
    assert "levels" in params, "Missing parameter 'levels'"

def test_parkinglot_has_hours():
    assert hasattr(ParkingLot, "hours")
    descriptor = None
    for klass in ParkingLot.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_parkinglot_has_numOfLevels():
    assert hasattr(ParkingLot, "numOfLevels")
    descriptor = None
    for klass in ParkingLot.__mro__:
        if "numOfLevels" in klass.__dict__:
            descriptor = klass.__dict__["numOfLevels"]
            break
    assert isinstance(descriptor, property)

def test_parkinglot_has_capacity():
    assert hasattr(ParkingLot, "capacity")
    descriptor = None
    for klass in ParkingLot.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_parkinglot_has_spotsOccupied():
    assert hasattr(ParkingLot, "spotsOccupied")
    descriptor = None
    for klass in ParkingLot.__mro__:
        if "spotsOccupied" in klass.__dict__:
            descriptor = klass.__dict__["spotsOccupied"]
            break
    assert isinstance(descriptor, property)

def test_parkinglot_has_levels():
    assert hasattr(ParkingLot, "levels")
    descriptor = None
    for klass in ParkingLot.__mro__:
        if "levels" in klass.__dict__:
            descriptor = klass.__dict__["levels"]
            break
    assert isinstance(descriptor, property)

def test_parkingspottype_exists():
    # Check that the Enumeration exists
    assert ParkingSpotType is not None

def test_parkingspottype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParkingSpotType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParkingSpotType"

def test_piececolor_exists():
    # Check that the Enumeration exists
    assert PieceColor is not None

def test_piececolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PieceColor]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PieceColor"


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
Slot_strategy = st.builds(
    Slot,
    Occupied=
        st.booleans(),
    piece=
        st.none()
)
Pawn_strategy = st.builds(
    Pawn,
    pieceColor=
        safe_text
)
King_strategy = st.builds(
    King,
    pieceColor=
        safe_text
)
Queen_strategy = st.builds(
    Queen,
    pieceColor=
        safe_text
)
Rook_strategy = st.builds(
    Rook,
    pieceColor=
        safe_text
)
Bishop_strategy = st.builds(
    Bishop,
    pieceColor=
        safe_text
)
Knight_strategy = st.builds(
    Knight,
    pieceColor=
        safe_text
)
Piece_strategy = st.builds(
    Piece,
    pieceColor=
        st.none()
)
Chess_strategy = st.builds(
    Chess,
    board=
        safe_text
)
Level_strategy = st.builds(
    Level,
    numofSpots=
        st.integers(),
    levelId=
        st.integers(),
    parkingSpots=
        safe_text
)
ParkingSpot_strategy = st.builds(
    ParkingSpot,
    spotType=
        st.none(),
    parkingSpotId=
        st.integers(),
    occupied=
        st.booleans()
)
ParkingLot_strategy = st.builds(
    ParkingLot,
    hours=
        safe_text,
    numOfLevels=
        st.integers(),
    capacity=
        st.integers(),
    spotsOccupied=
        st.integers(),
    levels=
        safe_text
)

@given(instance=Slot_strategy)
@settings(max_examples=50)
def test_slot_instantiation(instance):
    assert isinstance(instance, Slot)



@given(instance=Slot_strategy)
def test_slot_Occupied_setter(instance):
    original = instance.Occupied
    instance.Occupied = original
    assert instance.Occupied == original



@given(instance=Slot_strategy)
def test_slot_piece_setter(instance):
    original = instance.piece
    instance.piece = original
    assert instance.piece == original

@given(instance=Pawn_strategy)
@settings(max_examples=50)
def test_pawn_instantiation(instance):
    assert isinstance(instance, Pawn)



@given(instance=Pawn_strategy)
def test_pawn_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original

@given(instance=King_strategy)
@settings(max_examples=50)
def test_king_instantiation(instance):
    assert isinstance(instance, King)



@given(instance=King_strategy)
def test_king_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original

@given(instance=Queen_strategy)
@settings(max_examples=50)
def test_queen_instantiation(instance):
    assert isinstance(instance, Queen)



@given(instance=Queen_strategy)
def test_queen_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original

@given(instance=Rook_strategy)
@settings(max_examples=50)
def test_rook_instantiation(instance):
    assert isinstance(instance, Rook)



@given(instance=Rook_strategy)
def test_rook_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original

@given(instance=Bishop_strategy)
@settings(max_examples=50)
def test_bishop_instantiation(instance):
    assert isinstance(instance, Bishop)



@given(instance=Bishop_strategy)
def test_bishop_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original

@given(instance=Knight_strategy)
@settings(max_examples=50)
def test_knight_instantiation(instance):
    assert isinstance(instance, Knight)



@given(instance=Knight_strategy)
def test_knight_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original

@given(instance=Piece_strategy)
@settings(max_examples=50)
def test_piece_instantiation(instance):
    assert isinstance(instance, Piece)



@given(instance=Piece_strategy)
def test_piece_pieceColor_setter(instance):
    original = instance.pieceColor
    instance.pieceColor = original
    assert instance.pieceColor == original

@given(instance=Chess_strategy)
@settings(max_examples=50)
def test_chess_instantiation(instance):
    assert isinstance(instance, Chess)



@given(instance=Chess_strategy)
def test_chess_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original

@given(instance=Level_strategy)
@settings(max_examples=50)
def test_level_instantiation(instance):
    assert isinstance(instance, Level)



@given(instance=Level_strategy)
def test_level_numofSpots_setter(instance):
    original = instance.numofSpots
    instance.numofSpots = original
    assert instance.numofSpots == original



@given(instance=Level_strategy)
def test_level_levelId_setter(instance):
    original = instance.levelId
    instance.levelId = original
    assert instance.levelId == original



@given(instance=Level_strategy)
def test_level_parkingSpots_setter(instance):
    original = instance.parkingSpots
    instance.parkingSpots = original
    assert instance.parkingSpots == original

@given(instance=ParkingSpot_strategy)
@settings(max_examples=50)
def test_parkingspot_instantiation(instance):
    assert isinstance(instance, ParkingSpot)



@given(instance=ParkingSpot_strategy)
def test_parkingspot_spotType_setter(instance):
    original = instance.spotType
    instance.spotType = original
    assert instance.spotType == original



@given(instance=ParkingSpot_strategy)
def test_parkingspot_parkingSpotId_setter(instance):
    original = instance.parkingSpotId
    instance.parkingSpotId = original
    assert instance.parkingSpotId == original



@given(instance=ParkingSpot_strategy)
def test_parkingspot_occupied_setter(instance):
    original = instance.occupied
    instance.occupied = original
    assert instance.occupied == original

@given(instance=ParkingLot_strategy)
@settings(max_examples=50)
def test_parkinglot_instantiation(instance):
    assert isinstance(instance, ParkingLot)



@given(instance=ParkingLot_strategy)
def test_parkinglot_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original



@given(instance=ParkingLot_strategy)
def test_parkinglot_numOfLevels_setter(instance):
    original = instance.numOfLevels
    instance.numOfLevels = original
    assert instance.numOfLevels == original



@given(instance=ParkingLot_strategy)
def test_parkinglot_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=ParkingLot_strategy)
def test_parkinglot_spotsOccupied_setter(instance):
    original = instance.spotsOccupied
    instance.spotsOccupied = original
    assert instance.spotsOccupied == original



@given(instance=ParkingLot_strategy)
def test_parkinglot_levels_setter(instance):
    original = instance.levels
    instance.levels = original
    assert instance.levels == original
