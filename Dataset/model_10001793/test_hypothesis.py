import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Program,
    GameManager,
    Dealer,
    Player,
    Deck,
    Card,
    CardNumber,
    Suit1,
    Suit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_program_is_not_abstract():
    assert not inspect.isabstract(Program)


def test_program_constructor_exists():
    assert callable(Program.__init__)


def test_program_constructor_args():
    sig = inspect.signature(Program.__init__)
    params = list(sig.parameters.keys())



def test_gamemanager_is_not_abstract():
    assert not inspect.isabstract(GameManager)


def test_gamemanager_constructor_exists():
    assert callable(GameManager.__init__)


def test_gamemanager_constructor_args():
    sig = inspect.signature(GameManager.__init__)
    params = list(sig.parameters.keys())



def test_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "cardDeck" in params, "Missing parameter 'cardDeck'"

def test_dealer_has_cardDeck():
    assert hasattr(Dealer, "cardDeck")
    descriptor = None
    for klass in Dealer.__mro__:
        if "cardDeck" in klass.__dict__:
            descriptor = klass.__dict__["cardDeck"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "isSoft" in params, "Missing parameter 'isSoft'"
    assert "CardsInHand" in params, "Missing parameter 'CardsInHand'"

def test_player_has_isSoft():
    assert hasattr(Player, "isSoft")
    descriptor = None
    for klass in Player.__mro__:
        if "isSoft" in klass.__dict__:
            descriptor = klass.__dict__["isSoft"]
            break
    assert isinstance(descriptor, property)

def test_player_has_CardsInHand():
    assert hasattr(Player, "CardsInHand")
    descriptor = None
    for klass in Player.__mro__:
        if "CardsInHand" in klass.__dict__:
            descriptor = klass.__dict__["CardsInHand"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "List_card_" in params, "Missing parameter 'List_card_'"

def test_deck_has_List_card_():
    assert hasattr(Deck, "List_card_")
    descriptor = None
    for klass in Deck.__mro__:
        if "List_card_" in klass.__dict__:
            descriptor = klass.__dict__["List_card_"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "_CardNumber" in params, "Missing parameter '_CardNumber'"
    assert "_CardValue" in params, "Missing parameter '_CardValue'"
    assert "_Suit" in params, "Missing parameter '_Suit'"

def test_card_has__CardNumber():
    assert hasattr(Card, "_CardNumber")
    descriptor = None
    for klass in Card.__mro__:
        if "_CardNumber" in klass.__dict__:
            descriptor = klass.__dict__["_CardNumber"]
            break
    assert isinstance(descriptor, property)

def test_card_has__CardValue():
    assert hasattr(Card, "_CardValue")
    descriptor = None
    for klass in Card.__mro__:
        if "_CardValue" in klass.__dict__:
            descriptor = klass.__dict__["_CardValue"]
            break
    assert isinstance(descriptor, property)

def test_card_has__Suit():
    assert hasattr(Card, "_Suit")
    descriptor = None
    for klass in Card.__mro__:
        if "_Suit" in klass.__dict__:
            descriptor = klass.__dict__["_Suit"]
            break
    assert isinstance(descriptor, property)

def test_cardnumber_exists():
    # Check that the Enumeration exists
    assert CardNumber is not None

def test_cardnumber_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardNumber]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardNumber"

def test_suit1_exists():
    # Check that the Enumeration exists
    assert Suit1 is not None

def test_suit1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Suit1]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Suit1"

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
Program_strategy = st.builds(
    Program,
)
GameManager_strategy = st.builds(
    GameManager,
)
Dealer_strategy = st.builds(
    Dealer,
    cardDeck=
        st.none()
)
Player_strategy = st.builds(
    Player,
    isSoft=
        st.booleans(),
    CardsInHand=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    List_card_=
        st.none()
)
Card_strategy = st.builds(
    Card,
    _CardNumber=
        st.integers(),
    _CardValue=
        st.integers(),
    _Suit=
        st.integers()
)

@given(instance=Program_strategy)
@settings(max_examples=50)
def test_program_instantiation(instance):
    assert isinstance(instance, Program)

@given(instance=GameManager_strategy)
@settings(max_examples=50)
def test_gamemanager_instantiation(instance):
    assert isinstance(instance, GameManager)

@given(instance=Dealer_strategy)
@settings(max_examples=50)
def test_dealer_instantiation(instance):
    assert isinstance(instance, Dealer)



@given(instance=Dealer_strategy)
def test_dealer_cardDeck_setter(instance):
    original = instance.cardDeck
    instance.cardDeck = original
    assert instance.cardDeck == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_isSoft_setter(instance):
    original = instance.isSoft
    instance.isSoft = original
    assert instance.isSoft == original



@given(instance=Player_strategy)
def test_player_CardsInHand_setter(instance):
    original = instance.CardsInHand
    instance.CardsInHand = original
    assert instance.CardsInHand == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_List_card__setter(instance):
    original = instance.List_card_
    instance.List_card_ = original
    assert instance.List_card_ == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card__CardNumber_setter(instance):
    original = instance._CardNumber
    instance._CardNumber = original
    assert instance._CardNumber == original



@given(instance=Card_strategy)
def test_card__CardValue_setter(instance):
    original = instance._CardValue
    instance._CardValue = original
    assert instance._CardValue == original



@given(instance=Card_strategy)
def test_card__Suit_setter(instance):
    original = instance._Suit
    instance._Suit = original
    assert instance._Suit == original
