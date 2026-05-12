import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Dealer_Interface,
    Gambler_Interface,
    HandDeck,
    BJPlayer,
    Deck,
    StandardCard,
    JokerCard,
    StandCard,
    PlayingCard,
    Player,
    CardName,
    Suit,
    CardName1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dealer_interface_is_not_abstract():
    assert not inspect.isabstract(Dealer_Interface)


def test_dealer_interface_constructor_exists():
    assert callable(Dealer_Interface.__init__)


def test_dealer_interface_constructor_args():
    sig = inspect.signature(Dealer_Interface.__init__)
    params = list(sig.parameters.keys())



def test_gambler_interface_is_not_abstract():
    assert not inspect.isabstract(Gambler_Interface)


def test_gambler_interface_constructor_exists():
    assert callable(Gambler_Interface.__init__)


def test_gambler_interface_constructor_args():
    sig = inspect.signature(Gambler_Interface.__init__)
    params = list(sig.parameters.keys())



def test_handdeck_is_not_abstract():
    assert not inspect.isabstract(HandDeck)


def test_handdeck_constructor_exists():
    assert callable(HandDeck.__init__)


def test_handdeck_constructor_args():
    sig = inspect.signature(HandDeck.__init__)
    params = list(sig.parameters.keys())
    assert "bust" in params, "Missing parameter 'bust'"
    assert "naturalBlackJack" in params, "Missing parameter 'naturalBlackJack'"
    assert "stand" in params, "Missing parameter 'stand'"
    assert "pair" in params, "Missing parameter 'pair'"

def test_handdeck_has_bust():
    assert hasattr(HandDeck, "bust")
    descriptor = None
    for klass in HandDeck.__mro__:
        if "bust" in klass.__dict__:
            descriptor = klass.__dict__["bust"]
            break
    assert isinstance(descriptor, property)

def test_handdeck_has_naturalBlackJack():
    assert hasattr(HandDeck, "naturalBlackJack")
    descriptor = None
    for klass in HandDeck.__mro__:
        if "naturalBlackJack" in klass.__dict__:
            descriptor = klass.__dict__["naturalBlackJack"]
            break
    assert isinstance(descriptor, property)

def test_handdeck_has_stand():
    assert hasattr(HandDeck, "stand")
    descriptor = None
    for klass in HandDeck.__mro__:
        if "stand" in klass.__dict__:
            descriptor = klass.__dict__["stand"]
            break
    assert isinstance(descriptor, property)

def test_handdeck_has_pair():
    assert hasattr(HandDeck, "pair")
    descriptor = None
    for klass in HandDeck.__mro__:
        if "pair" in klass.__dict__:
            descriptor = klass.__dict__["pair"]
            break
    assert isinstance(descriptor, property)



def test_bjplayer_is_not_abstract():
    assert not inspect.isabstract(BJPlayer)


def test_bjplayer_constructor_exists():
    assert callable(BJPlayer.__init__)


def test_bjplayer_constructor_args():
    sig = inspect.signature(BJPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "hands" in params, "Missing parameter 'hands'"
    assert "bet" in params, "Missing parameter 'bet'"

def test_bjplayer_has_hands():
    assert hasattr(BJPlayer, "hands")
    descriptor = None
    for klass in BJPlayer.__mro__:
        if "hands" in klass.__dict__:
            descriptor = klass.__dict__["hands"]
            break
    assert isinstance(descriptor, property)

def test_bjplayer_has_bet():
    assert hasattr(BJPlayer, "bet")
    descriptor = None
    for klass in BJPlayer.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())



def test_standardcard_is_not_abstract():
    assert not inspect.isabstract(StandardCard)


def test_standardcard_constructor_exists():
    assert callable(StandardCard.__init__)


def test_standardcard_constructor_args():
    sig = inspect.signature(StandardCard.__init__)
    params = list(sig.parameters.keys())
    assert "standardCard" in params, "Missing parameter 'standardCard'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "cardName" in params, "Missing parameter 'cardName'"

def test_standardcard_has_standardCard():
    assert hasattr(StandardCard, "standardCard")
    descriptor = None
    for klass in StandardCard.__mro__:
        if "standardCard" in klass.__dict__:
            descriptor = klass.__dict__["standardCard"]
            break
    assert isinstance(descriptor, property)

def test_standardcard_has_suit():
    assert hasattr(StandardCard, "suit")
    descriptor = None
    for klass in StandardCard.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_standardcard_has_cardName():
    assert hasattr(StandardCard, "cardName")
    descriptor = None
    for klass in StandardCard.__mro__:
        if "cardName" in klass.__dict__:
            descriptor = klass.__dict__["cardName"]
            break
    assert isinstance(descriptor, property)



def test_jokercard_is_not_abstract():
    assert not inspect.isabstract(JokerCard)


def test_jokercard_constructor_exists():
    assert callable(JokerCard.__init__)


def test_jokercard_constructor_args():
    sig = inspect.signature(JokerCard.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "jokerCard" in params, "Missing parameter 'jokerCard'"

def test_jokercard_has_red():
    assert hasattr(JokerCard, "red")
    descriptor = None
    for klass in JokerCard.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_jokercard_has_jokerCard():
    assert hasattr(JokerCard, "jokerCard")
    descriptor = None
    for klass in JokerCard.__mro__:
        if "jokerCard" in klass.__dict__:
            descriptor = klass.__dict__["jokerCard"]
            break
    assert isinstance(descriptor, property)



def test_standcard_is_not_abstract():
    assert not inspect.isabstract(StandCard)


def test_standcard_constructor_exists():
    assert callable(StandCard.__init__)


def test_standcard_constructor_args():
    sig = inspect.signature(StandCard.__init__)
    params = list(sig.parameters.keys())



def test_playingcard_is_not_abstract():
    assert not inspect.isabstract(PlayingCard)


def test_playingcard_constructor_exists():
    assert callable(PlayingCard.__init__)


def test_playingcard_constructor_args():
    sig = inspect.signature(PlayingCard.__init__)
    params = list(sig.parameters.keys())
    assert "jokerCard" in params, "Missing parameter 'jokerCard'"
    assert "faceUp" in params, "Missing parameter 'faceUp'"
    assert "standardCard" in params, "Missing parameter 'standardCard'"

def test_playingcard_has_jokerCard():
    assert hasattr(PlayingCard, "jokerCard")
    descriptor = None
    for klass in PlayingCard.__mro__:
        if "jokerCard" in klass.__dict__:
            descriptor = klass.__dict__["jokerCard"]
            break
    assert isinstance(descriptor, property)

def test_playingcard_has_faceUp():
    assert hasattr(PlayingCard, "faceUp")
    descriptor = None
    for klass in PlayingCard.__mro__:
        if "faceUp" in klass.__dict__:
            descriptor = klass.__dict__["faceUp"]
            break
    assert isinstance(descriptor, property)

def test_playingcard_has_standardCard():
    assert hasattr(PlayingCard, "standardCard")
    descriptor = None
    for klass in PlayingCard.__mro__:
        if "standardCard" in klass.__dict__:
            descriptor = klass.__dict__["standardCard"]
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
    assert "pocket" in params, "Missing parameter 'pocket'"

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_has_pocket():
    assert hasattr(Player, "pocket")
    descriptor = None
    for klass in Player.__mro__:
        if "pocket" in klass.__dict__:
            descriptor = klass.__dict__["pocket"]
            break
    assert isinstance(descriptor, property)

def test_cardname_exists():
    # Check that the Enumeration exists
    assert CardName is not None

def test_cardname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardName]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardName"

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

def test_cardname1_exists():
    # Check that the Enumeration exists
    assert CardName1 is not None

def test_cardname1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardName1]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardName1"


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
Dealer_Interface_strategy = st.builds(
    Dealer_Interface,
)
Gambler_Interface_strategy = st.builds(
    Gambler_Interface,
)
HandDeck_strategy = st.builds(
    HandDeck,
    bust=
        st.booleans(),
    naturalBlackJack=
        st.booleans(),
    stand=
        st.booleans(),
    pair=
        st.booleans()
)
BJPlayer_strategy = st.builds(
    BJPlayer,
    hands=
        safe_text,
    bet=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
)
StandardCard_strategy = st.builds(
    StandardCard,
    standardCard=
        st.booleans(),
    suit=
        safe_text,
    cardName=
        st.none()
)
JokerCard_strategy = st.builds(
    JokerCard,
    red=
        st.booleans(),
    jokerCard=
        st.booleans()
)
StandCard_strategy = st.builds(
    StandCard,
)
PlayingCard_strategy = st.builds(
    PlayingCard,
    jokerCard=
        st.booleans(),
    faceUp=
        st.booleans(),
    standardCard=
        st.booleans()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    pocket=
        st.integers()
)

@given(instance=Dealer_Interface_strategy)
@settings(max_examples=50)
def test_dealer_interface_instantiation(instance):
    assert isinstance(instance, Dealer_Interface)

@given(instance=Gambler_Interface_strategy)
@settings(max_examples=50)
def test_gambler_interface_instantiation(instance):
    assert isinstance(instance, Gambler_Interface)

@given(instance=HandDeck_strategy)
@settings(max_examples=50)
def test_handdeck_instantiation(instance):
    assert isinstance(instance, HandDeck)



@given(instance=HandDeck_strategy)
def test_handdeck_bust_setter(instance):
    original = instance.bust
    instance.bust = original
    assert instance.bust == original



@given(instance=HandDeck_strategy)
def test_handdeck_naturalBlackJack_setter(instance):
    original = instance.naturalBlackJack
    instance.naturalBlackJack = original
    assert instance.naturalBlackJack == original



@given(instance=HandDeck_strategy)
def test_handdeck_stand_setter(instance):
    original = instance.stand
    instance.stand = original
    assert instance.stand == original



@given(instance=HandDeck_strategy)
def test_handdeck_pair_setter(instance):
    original = instance.pair
    instance.pair = original
    assert instance.pair == original

@given(instance=BJPlayer_strategy)
@settings(max_examples=50)
def test_bjplayer_instantiation(instance):
    assert isinstance(instance, BJPlayer)



@given(instance=BJPlayer_strategy)
def test_bjplayer_hands_setter(instance):
    original = instance.hands
    instance.hands = original
    assert instance.hands == original



@given(instance=BJPlayer_strategy)
def test_bjplayer_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)

@given(instance=StandardCard_strategy)
@settings(max_examples=50)
def test_standardcard_instantiation(instance):
    assert isinstance(instance, StandardCard)



@given(instance=StandardCard_strategy)
def test_standardcard_standardCard_setter(instance):
    original = instance.standardCard
    instance.standardCard = original
    assert instance.standardCard == original



@given(instance=StandardCard_strategy)
def test_standardcard_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=StandardCard_strategy)
def test_standardcard_cardName_setter(instance):
    original = instance.cardName
    instance.cardName = original
    assert instance.cardName == original

@given(instance=JokerCard_strategy)
@settings(max_examples=50)
def test_jokercard_instantiation(instance):
    assert isinstance(instance, JokerCard)



@given(instance=JokerCard_strategy)
def test_jokercard_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=JokerCard_strategy)
def test_jokercard_jokerCard_setter(instance):
    original = instance.jokerCard
    instance.jokerCard = original
    assert instance.jokerCard == original

@given(instance=StandCard_strategy)
@settings(max_examples=50)
def test_standcard_instantiation(instance):
    assert isinstance(instance, StandCard)

@given(instance=PlayingCard_strategy)
@settings(max_examples=50)
def test_playingcard_instantiation(instance):
    assert isinstance(instance, PlayingCard)



@given(instance=PlayingCard_strategy)
def test_playingcard_jokerCard_setter(instance):
    original = instance.jokerCard
    instance.jokerCard = original
    assert instance.jokerCard == original



@given(instance=PlayingCard_strategy)
def test_playingcard_faceUp_setter(instance):
    original = instance.faceUp
    instance.faceUp = original
    assert instance.faceUp == original



@given(instance=PlayingCard_strategy)
def test_playingcard_standardCard_setter(instance):
    original = instance.standardCard
    instance.standardCard = original
    assert instance.standardCard == original

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
def test_player_pocket_setter(instance):
    original = instance.pocket
    instance.pocket = original
    assert instance.pocket == original
