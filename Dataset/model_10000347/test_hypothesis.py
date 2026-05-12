import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Computer,
    Human,
    Bank,
    HandStrength,
    Dealer,
    Deck,
    RecordBook,
    Player,
    Hand,
    Card,
    Poker,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_computer_is_not_abstract():
    assert not inspect.isabstract(Computer)


def test_computer_constructor_exists():
    assert callable(Computer.__init__)


def test_computer_constructor_args():
    sig = inspect.signature(Computer.__init__)
    params = list(sig.parameters.keys())



def test_human_is_not_abstract():
    assert not inspect.isabstract(Human)


def test_human_constructor_exists():
    assert callable(Human.__init__)


def test_human_constructor_args():
    sig = inspect.signature(Human.__init__)
    params = list(sig.parameters.keys())



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "total" in params, "Missing parameter 'total'"

def test_bank_has_total():
    assert hasattr(Bank, "total")
    descriptor = None
    for klass in Bank.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)



def test_handstrength_is_not_abstract():
    assert not inspect.isabstract(HandStrength)


def test_handstrength_constructor_exists():
    assert callable(HandStrength.__init__)


def test_handstrength_constructor_args():
    sig = inspect.signature(HandStrength.__init__)
    params = list(sig.parameters.keys())
    assert "STRAIGHT_FLUSH" in params, "Missing parameter 'STRAIGHT_FLUSH'"

def test_handstrength_has_STRAIGHT_FLUSH():
    assert hasattr(HandStrength, "STRAIGHT_FLUSH")
    descriptor = None
    for klass in HandStrength.__mro__:
        if "STRAIGHT_FLUSH" in klass.__dict__:
            descriptor = klass.__dict__["STRAIGHT_FLUSH"]
            break
    assert isinstance(descriptor, property)



def test_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"
    assert "analyzeHand" in params, "Missing parameter 'analyzeHand'"

def test_dealer_has_deck():
    assert hasattr(Dealer, "deck")
    descriptor = None
    for klass in Dealer.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_dealer_has_analyzeHand():
    assert hasattr(Dealer, "analyzeHand")
    descriptor = None
    for klass in Dealer.__mro__:
        if "analyzeHand" in klass.__dict__:
            descriptor = klass.__dict__["analyzeHand"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"

def test_deck_has_cards():
    assert hasattr(Deck, "cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)



def test_recordbook_is_not_abstract():
    assert not inspect.isabstract(RecordBook)


def test_recordbook_constructor_exists():
    assert callable(RecordBook.__init__)


def test_recordbook_constructor_args():
    sig = inspect.signature(RecordBook.__init__)
    params = list(sig.parameters.keys())
    assert "recordList" in params, "Missing parameter 'recordList'"

def test_recordbook_has_recordList():
    assert hasattr(RecordBook, "recordList")
    descriptor = None
    for klass in RecordBook.__mro__:
        if "recordList" in klass.__dict__:
            descriptor = klass.__dict__["recordList"]
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
    assert "bank" in params, "Missing parameter 'bank'"

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

def test_player_has_bank():
    assert hasattr(Player, "bank")
    descriptor = None
    for klass in Player.__mro__:
        if "bank" in klass.__dict__:
            descriptor = klass.__dict__["bank"]
            break
    assert isinstance(descriptor, property)



def test_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "handCollection" in params, "Missing parameter 'handCollection'"

def test_hand_has_handCollection():
    assert hasattr(Hand, "handCollection")
    descriptor = None
    for klass in Hand.__mro__:
        if "handCollection" in klass.__dict__:
            descriptor = klass.__dict__["handCollection"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "val" in params, "Missing parameter 'val'"
    assert "name" in params, "Missing parameter 'name'"
    assert "img" in params, "Missing parameter 'img'"

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_val():
    assert hasattr(Card, "val")
    descriptor = None
    for klass in Card.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)

def test_card_has_name():
    assert hasattr(Card, "name")
    descriptor = None
    for klass in Card.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_card_has_img():
    assert hasattr(Card, "img")
    descriptor = None
    for klass in Card.__mro__:
        if "img" in klass.__dict__:
            descriptor = klass.__dict__["img"]
            break
    assert isinstance(descriptor, property)



def test_poker_is_not_abstract():
    assert not inspect.isabstract(Poker)


def test_poker_constructor_exists():
    assert callable(Poker.__init__)


def test_poker_constructor_args():
    sig = inspect.signature(Poker.__init__)
    params = list(sig.parameters.keys())
    assert "dealer" in params, "Missing parameter 'dealer'"
    assert "player1" in params, "Missing parameter 'player1'"
    assert "player2" in params, "Missing parameter 'player2'"

def test_poker_has_dealer():
    assert hasattr(Poker, "dealer")
    descriptor = None
    for klass in Poker.__mro__:
        if "dealer" in klass.__dict__:
            descriptor = klass.__dict__["dealer"]
            break
    assert isinstance(descriptor, property)

def test_poker_has_player1():
    assert hasattr(Poker, "player1")
    descriptor = None
    for klass in Poker.__mro__:
        if "player1" in klass.__dict__:
            descriptor = klass.__dict__["player1"]
            break
    assert isinstance(descriptor, property)

def test_poker_has_player2():
    assert hasattr(Poker, "player2")
    descriptor = None
    for klass in Poker.__mro__:
        if "player2" in klass.__dict__:
            descriptor = klass.__dict__["player2"]
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
Computer_strategy = st.builds(
    Computer,
)
Human_strategy = st.builds(
    Human,
)
Bank_strategy = st.builds(
    Bank,
    total=
        safe_text
)
HandStrength_strategy = st.builds(
    HandStrength,
    STRAIGHT_FLUSH=
        st.integers()
)
Dealer_strategy = st.builds(
    Dealer,
    deck=
        st.none(),
    analyzeHand=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    cards=
        safe_text
)
RecordBook_strategy = st.builds(
    RecordBook,
    recordList=
        safe_text
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    hand=
        st.none(),
    bank=
        st.none()
)
Hand_strategy = st.builds(
    Hand,
    handCollection=
        safe_text
)
Card_strategy = st.builds(
    Card,
    suit=
        safe_text,
    val=
        safe_text,
    name=
        safe_text,
    img=
        safe_text
)
Poker_strategy = st.builds(
    Poker,
    dealer=
        st.none(),
    player1=
        st.none(),
    player2=
        st.none()
)

@given(instance=Computer_strategy)
@settings(max_examples=50)
def test_computer_instantiation(instance):
    assert isinstance(instance, Computer)

@given(instance=Human_strategy)
@settings(max_examples=50)
def test_human_instantiation(instance):
    assert isinstance(instance, Human)

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=HandStrength_strategy)
@settings(max_examples=50)
def test_handstrength_instantiation(instance):
    assert isinstance(instance, HandStrength)



@given(instance=HandStrength_strategy)
def test_handstrength_STRAIGHT_FLUSH_setter(instance):
    original = instance.STRAIGHT_FLUSH
    instance.STRAIGHT_FLUSH = original
    assert instance.STRAIGHT_FLUSH == original

@given(instance=Dealer_strategy)
@settings(max_examples=50)
def test_dealer_instantiation(instance):
    assert isinstance(instance, Dealer)



@given(instance=Dealer_strategy)
def test_dealer_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=Dealer_strategy)
def test_dealer_analyzeHand_setter(instance):
    original = instance.analyzeHand
    instance.analyzeHand = original
    assert instance.analyzeHand == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=RecordBook_strategy)
@settings(max_examples=50)
def test_recordbook_instantiation(instance):
    assert isinstance(instance, RecordBook)



@given(instance=RecordBook_strategy)
def test_recordbook_recordList_setter(instance):
    original = instance.recordList
    instance.recordList = original
    assert instance.recordList == original

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
def test_player_bank_setter(instance):
    original = instance.bank
    instance.bank = original
    assert instance.bank == original

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hand_instantiation(instance):
    assert isinstance(instance, Hand)



@given(instance=Hand_strategy)
def test_hand_handCollection_setter(instance):
    original = instance.handCollection
    instance.handCollection = original
    assert instance.handCollection == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_card_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original



@given(instance=Card_strategy)
def test_card_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Card_strategy)
def test_card_img_setter(instance):
    original = instance.img
    instance.img = original
    assert instance.img == original

@given(instance=Poker_strategy)
@settings(max_examples=50)
def test_poker_instantiation(instance):
    assert isinstance(instance, Poker)



@given(instance=Poker_strategy)
def test_poker_dealer_setter(instance):
    original = instance.dealer
    instance.dealer = original
    assert instance.dealer == original



@given(instance=Poker_strategy)
def test_poker_player1_setter(instance):
    original = instance.player1
    instance.player1 = original
    assert instance.player1 == original



@given(instance=Poker_strategy)
def test_poker_player2_setter(instance):
    original = instance.player2
    instance.player2 = original
    assert instance.player2 == original
