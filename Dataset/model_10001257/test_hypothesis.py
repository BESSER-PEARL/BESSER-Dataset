import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Session,
    Card,
    Player,
    Rank,
    Suit,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_session_is_not_abstract():
    assert not inspect.isabstract(Session)


def test_session_constructor_exists():
    assert callable(Session.__init__)


def test_session_constructor_args():
    sig = inspect.signature(Session.__init__)
    params = list(sig.parameters.keys())
    assert "humanPointer" in params, "Missing parameter 'humanPointer'"
    assert "currentPlayerPointer" in params, "Missing parameter 'currentPlayerPointer'"
    assert "gameStatus" in params, "Missing parameter 'gameStatus'"
    assert "players" in params, "Missing parameter 'players'"
    assert "gameStatusCode" in params, "Missing parameter 'gameStatusCode'"
    assert "humanTurn" in params, "Missing parameter 'humanTurn'"
    assert "id" in params, "Missing parameter 'id'"
    assert "cardDeck" in params, "Missing parameter 'cardDeck'"
    assert "discardPile" in params, "Missing parameter 'discardPile'"

def test_session_has_humanPointer():
    assert hasattr(Session, "humanPointer")
    descriptor = None
    for klass in Session.__mro__:
        if "humanPointer" in klass.__dict__:
            descriptor = klass.__dict__["humanPointer"]
            break
    assert isinstance(descriptor, property)

def test_session_has_currentPlayerPointer():
    assert hasattr(Session, "currentPlayerPointer")
    descriptor = None
    for klass in Session.__mro__:
        if "currentPlayerPointer" in klass.__dict__:
            descriptor = klass.__dict__["currentPlayerPointer"]
            break
    assert isinstance(descriptor, property)

def test_session_has_gameStatus():
    assert hasattr(Session, "gameStatus")
    descriptor = None
    for klass in Session.__mro__:
        if "gameStatus" in klass.__dict__:
            descriptor = klass.__dict__["gameStatus"]
            break
    assert isinstance(descriptor, property)

def test_session_has_players():
    assert hasattr(Session, "players")
    descriptor = None
    for klass in Session.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_session_has_gameStatusCode():
    assert hasattr(Session, "gameStatusCode")
    descriptor = None
    for klass in Session.__mro__:
        if "gameStatusCode" in klass.__dict__:
            descriptor = klass.__dict__["gameStatusCode"]
            break
    assert isinstance(descriptor, property)

def test_session_has_humanTurn():
    assert hasattr(Session, "humanTurn")
    descriptor = None
    for klass in Session.__mro__:
        if "humanTurn" in klass.__dict__:
            descriptor = klass.__dict__["humanTurn"]
            break
    assert isinstance(descriptor, property)

def test_session_has_id():
    assert hasattr(Session, "id")
    descriptor = None
    for klass in Session.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_session_has_cardDeck():
    assert hasattr(Session, "cardDeck")
    descriptor = None
    for klass in Session.__mro__:
        if "cardDeck" in klass.__dict__:
            descriptor = klass.__dict__["cardDeck"]
            break
    assert isinstance(descriptor, property)

def test_session_has_discardPile():
    assert hasattr(Session, "discardPile")
    descriptor = None
    for klass in Session.__mro__:
        if "discardPile" in klass.__dict__:
            descriptor = klass.__dict__["discardPile"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_color():
    assert hasattr(Card, "color")
    descriptor = None
    for klass in Card.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_card_has_rank():
    assert hasattr(Card, "rank")
    descriptor = None
    for klass in Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "id" in params, "Missing parameter 'id'"

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_has_hand():
    assert hasattr(Player, "hand")
    descriptor = None
    for klass in Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)

def test_player_has_id():
    assert hasattr(Player, "id")
    descriptor = None
    for klass in Player.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rank_exists():
    # Check that the Enumeration exists
    assert Rank is not None

def test_rank_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Rank]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Rank"

def test_suit_exists():
    # Check that the Enumeration exists
    assert Suit is not None

def test_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Suit"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
Session_strategy = st.builds(
    Session,
    humanPointer=
        st.integers(),
    currentPlayerPointer=
        st.integers(),
    gameStatus=
        safe_text,
    players=
        safe_text,
    gameStatusCode=
        st.integers(),
    humanTurn=
        st.booleans(),
    id=
        st.integers(),
    cardDeck=
        safe_text,
    discardPile=
        safe_text
)
Card_strategy = st.builds(
    Card,
    color=
        st.none(),
    rank=
        st.none(),
    suit=
        st.none()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    hand=
        st.none(),
    id=
        st.integers()
)

@given(instance=Session_strategy)
@settings(max_examples=50)
def test_session_instantiation(instance):
    assert isinstance(instance, Session)



@given(instance=Session_strategy)
def test_session_humanPointer_setter(instance):
    original = instance.humanPointer
    instance.humanPointer = original
    assert instance.humanPointer == original



@given(instance=Session_strategy)
def test_session_currentPlayerPointer_setter(instance):
    original = instance.currentPlayerPointer
    instance.currentPlayerPointer = original
    assert instance.currentPlayerPointer == original



@given(instance=Session_strategy)
def test_session_gameStatus_setter(instance):
    original = instance.gameStatus
    instance.gameStatus = original
    assert instance.gameStatus == original



@given(instance=Session_strategy)
def test_session_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Session_strategy)
def test_session_gameStatusCode_setter(instance):
    original = instance.gameStatusCode
    instance.gameStatusCode = original
    assert instance.gameStatusCode == original



@given(instance=Session_strategy)
def test_session_humanTurn_setter(instance):
    original = instance.humanTurn
    instance.humanTurn = original
    assert instance.humanTurn == original



@given(instance=Session_strategy)
def test_session_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Session_strategy)
def test_session_cardDeck_setter(instance):
    original = instance.cardDeck
    instance.cardDeck = original
    assert instance.cardDeck == original



@given(instance=Session_strategy)
def test_session_discardPile_setter(instance):
    original = instance.discardPile
    instance.discardPile = original
    assert instance.discardPile == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Card_strategy)
def test_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Player_strategy)
def test_player_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
