import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MainGame_Hand,
    MainGame_GUI,
    MainGame_Deck,
    MainGame_Main,
    Players_Player,
    Cards_Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_maingame_hand_is_not_abstract():
    assert not inspect.isabstract(MainGame_Hand)


def test_maingame_hand_constructor_exists():
    assert callable(MainGame_Hand.__init__)


def test_maingame_hand_constructor_args():
    sig = inspect.signature(MainGame_Hand.__init__)
    params = list(sig.parameters.keys())
    assert "flush" in params, "Missing parameter 'flush'"
    assert "fullHouse" in params, "Missing parameter 'fullHouse'"
    assert "straight" in params, "Missing parameter 'straight'"
    assert "straightFlush" in params, "Missing parameter 'straightFlush'"
    assert "highCard" in params, "Missing parameter 'highCard'"
    assert "Hand" in params, "Missing parameter 'Hand'"
    assert "threeKing" in params, "Missing parameter 'threeKing'"
    assert "fourKind" in params, "Missing parameter 'fourKind'"
    assert "twoPair" in params, "Missing parameter 'twoPair'"
    assert "onePair" in params, "Missing parameter 'onePair'"

def test_maingame_hand_has_flush():
    assert hasattr(MainGame_Hand, "flush")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "flush" in klass.__dict__:
            descriptor = klass.__dict__["flush"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_fullHouse():
    assert hasattr(MainGame_Hand, "fullHouse")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "fullHouse" in klass.__dict__:
            descriptor = klass.__dict__["fullHouse"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_straight():
    assert hasattr(MainGame_Hand, "straight")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "straight" in klass.__dict__:
            descriptor = klass.__dict__["straight"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_straightFlush():
    assert hasattr(MainGame_Hand, "straightFlush")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "straightFlush" in klass.__dict__:
            descriptor = klass.__dict__["straightFlush"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_highCard():
    assert hasattr(MainGame_Hand, "highCard")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "highCard" in klass.__dict__:
            descriptor = klass.__dict__["highCard"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_Hand():
    assert hasattr(MainGame_Hand, "Hand")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "Hand" in klass.__dict__:
            descriptor = klass.__dict__["Hand"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_threeKing():
    assert hasattr(MainGame_Hand, "threeKing")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "threeKing" in klass.__dict__:
            descriptor = klass.__dict__["threeKing"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_fourKind():
    assert hasattr(MainGame_Hand, "fourKind")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "fourKind" in klass.__dict__:
            descriptor = klass.__dict__["fourKind"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_twoPair():
    assert hasattr(MainGame_Hand, "twoPair")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "twoPair" in klass.__dict__:
            descriptor = klass.__dict__["twoPair"]
            break
    assert isinstance(descriptor, property)

def test_maingame_hand_has_onePair():
    assert hasattr(MainGame_Hand, "onePair")
    descriptor = None
    for klass in MainGame_Hand.__mro__:
        if "onePair" in klass.__dict__:
            descriptor = klass.__dict__["onePair"]
            break
    assert isinstance(descriptor, property)



def test_maingame_gui_is_not_abstract():
    assert not inspect.isabstract(MainGame_GUI)


def test_maingame_gui_constructor_exists():
    assert callable(MainGame_GUI.__init__)


def test_maingame_gui_constructor_args():
    sig = inspect.signature(MainGame_GUI.__init__)
    params = list(sig.parameters.keys())



def test_maingame_deck_is_not_abstract():
    assert not inspect.isabstract(MainGame_Deck)


def test_maingame_deck_constructor_exists():
    assert callable(MainGame_Deck.__init__)


def test_maingame_deck_constructor_args():
    sig = inspect.signature(MainGame_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "Cards" in params, "Missing parameter 'Cards'"

def test_maingame_deck_has_Cards():
    assert hasattr(MainGame_Deck, "Cards")
    descriptor = None
    for klass in MainGame_Deck.__mro__:
        if "Cards" in klass.__dict__:
            descriptor = klass.__dict__["Cards"]
            break
    assert isinstance(descriptor, property)



def test_maingame_main_is_not_abstract():
    assert not inspect.isabstract(MainGame_Main)


def test_maingame_main_constructor_exists():
    assert callable(MainGame_Main.__init__)


def test_maingame_main_constructor_args():
    sig = inspect.signature(MainGame_Main.__init__)
    params = list(sig.parameters.keys())
    assert "dealNumber" in params, "Missing parameter 'dealNumber'"
    assert "deck" in params, "Missing parameter 'deck'"

def test_maingame_main_has_dealNumber():
    assert hasattr(MainGame_Main, "dealNumber")
    descriptor = None
    for klass in MainGame_Main.__mro__:
        if "dealNumber" in klass.__dict__:
            descriptor = klass.__dict__["dealNumber"]
            break
    assert isinstance(descriptor, property)

def test_maingame_main_has_deck():
    assert hasattr(MainGame_Main, "deck")
    descriptor = None
    for klass in MainGame_Main.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)



def test_players_player_is_not_abstract():
    assert not inspect.isabstract(Players_Player)


def test_players_player_constructor_exists():
    assert callable(Players_Player.__init__)


def test_players_player_constructor_args():
    sig = inspect.signature(Players_Player.__init__)
    params = list(sig.parameters.keys())
    assert "bet" in params, "Missing parameter 'bet'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "name" in params, "Missing parameter 'name'"

def test_players_player_has_bet():
    assert hasattr(Players_Player, "bet")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)

def test_players_player_has_hand():
    assert hasattr(Players_Player, "hand")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)

def test_players_player_has_name():
    assert hasattr(Players_Player, "name")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cards_card_is_not_abstract():
    assert not inspect.isabstract(Cards_Card)


def test_cards_card_constructor_exists():
    assert callable(Cards_Card.__init__)


def test_cards_card_constructor_args():
    sig = inspect.signature(Cards_Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_cards_card_has_value():
    assert hasattr(Cards_Card, "value")
    descriptor = None
    for klass in Cards_Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_cards_card_has_suit():
    assert hasattr(Cards_Card, "suit")
    descriptor = None
    for klass in Cards_Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
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
MainGame_Hand_strategy = st.builds(
    MainGame_Hand,
    flush=
        st.booleans(),
    fullHouse=
        st.booleans(),
    straight=
        st.booleans(),
    straightFlush=
        st.booleans(),
    highCard=
        st.booleans(),
    Hand=
        safe_text,
    threeKing=
        st.booleans(),
    fourKind=
        st.booleans(),
    twoPair=
        st.booleans(),
    onePair=
        st.booleans()
)
MainGame_GUI_strategy = st.builds(
    MainGame_GUI,
)
MainGame_Deck_strategy = st.builds(
    MainGame_Deck,
    Cards=
        safe_text
)
MainGame_Main_strategy = st.builds(
    MainGame_Main,
    dealNumber=
        st.integers(),
    deck=
        st.none()
)
Players_Player_strategy = st.builds(
    Players_Player,
    bet=
        st.integers(),
    hand=
        st.none(),
    name=
        safe_text
)
Cards_Card_strategy = st.builds(
    Cards_Card,
    value=
        st.integers(),
    suit=
        safe_text
)

@given(instance=MainGame_Hand_strategy)
@settings(max_examples=50)
def test_maingame_hand_instantiation(instance):
    assert isinstance(instance, MainGame_Hand)



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_flush_setter(instance):
    original = instance.flush
    instance.flush = original
    assert instance.flush == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_fullHouse_setter(instance):
    original = instance.fullHouse
    instance.fullHouse = original
    assert instance.fullHouse == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_straight_setter(instance):
    original = instance.straight
    instance.straight = original
    assert instance.straight == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_straightFlush_setter(instance):
    original = instance.straightFlush
    instance.straightFlush = original
    assert instance.straightFlush == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_highCard_setter(instance):
    original = instance.highCard
    instance.highCard = original
    assert instance.highCard == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_Hand_setter(instance):
    original = instance.Hand
    instance.Hand = original
    assert instance.Hand == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_threeKing_setter(instance):
    original = instance.threeKing
    instance.threeKing = original
    assert instance.threeKing == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_fourKind_setter(instance):
    original = instance.fourKind
    instance.fourKind = original
    assert instance.fourKind == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_twoPair_setter(instance):
    original = instance.twoPair
    instance.twoPair = original
    assert instance.twoPair == original



@given(instance=MainGame_Hand_strategy)
def test_maingame_hand_onePair_setter(instance):
    original = instance.onePair
    instance.onePair = original
    assert instance.onePair == original

@given(instance=MainGame_GUI_strategy)
@settings(max_examples=50)
def test_maingame_gui_instantiation(instance):
    assert isinstance(instance, MainGame_GUI)

@given(instance=MainGame_Deck_strategy)
@settings(max_examples=50)
def test_maingame_deck_instantiation(instance):
    assert isinstance(instance, MainGame_Deck)



@given(instance=MainGame_Deck_strategy)
def test_maingame_deck_Cards_setter(instance):
    original = instance.Cards
    instance.Cards = original
    assert instance.Cards == original

@given(instance=MainGame_Main_strategy)
@settings(max_examples=50)
def test_maingame_main_instantiation(instance):
    assert isinstance(instance, MainGame_Main)



@given(instance=MainGame_Main_strategy)
def test_maingame_main_dealNumber_setter(instance):
    original = instance.dealNumber
    instance.dealNumber = original
    assert instance.dealNumber == original



@given(instance=MainGame_Main_strategy)
def test_maingame_main_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original

@given(instance=Players_Player_strategy)
@settings(max_examples=50)
def test_players_player_instantiation(instance):
    assert isinstance(instance, Players_Player)



@given(instance=Players_Player_strategy)
def test_players_player_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original



@given(instance=Players_Player_strategy)
def test_players_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Players_Player_strategy)
def test_players_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Cards_Card_strategy)
@settings(max_examples=50)
def test_cards_card_instantiation(instance):
    assert isinstance(instance, Cards_Card)



@given(instance=Cards_Card_strategy)
def test_cards_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Cards_Card_strategy)
def test_cards_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
