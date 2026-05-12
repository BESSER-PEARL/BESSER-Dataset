import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JFrame,
    Board,
    player_Deck,
    player_Player,
    Card,
    Comparable_Interface,
    card_Card,
    poker_GameRun,
    poker_Game,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jframe_is_not_abstract():
    assert not inspect.isabstract(JFrame)


def test_jframe_constructor_exists():
    assert callable(JFrame.__init__)


def test_jframe_constructor_args():
    sig = inspect.signature(JFrame.__init__)
    params = list(sig.parameters.keys())



def test_board_is_not_abstract():
    assert not inspect.isabstract(Board)


def test_board_constructor_exists():
    assert callable(Board.__init__)


def test_board_constructor_args():
    sig = inspect.signature(Board.__init__)
    params = list(sig.parameters.keys())
    assert "cardArea" in params, "Missing parameter 'cardArea'"
    assert "playAagain" in params, "Missing parameter 'playAagain'"

def test_board_has_cardArea():
    assert hasattr(Board, "cardArea")
    descriptor = None
    for klass in Board.__mro__:
        if "cardArea" in klass.__dict__:
            descriptor = klass.__dict__["cardArea"]
            break
    assert isinstance(descriptor, property)

def test_board_has_playAagain():
    assert hasattr(Board, "playAagain")
    descriptor = None
    for klass in Board.__mro__:
        if "playAagain" in klass.__dict__:
            descriptor = klass.__dict__["playAagain"]
            break
    assert isinstance(descriptor, property)



def test_player_deck_is_not_abstract():
    assert not inspect.isabstract(player_Deck)


def test_player_deck_constructor_exists():
    assert callable(player_Deck.__init__)


def test_player_deck_constructor_args():
    sig = inspect.signature(player_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "hand_size" in params, "Missing parameter 'hand_size'"
    assert "numberofShuffles" in params, "Missing parameter 'numberofShuffles'"
    assert "deck_size" in params, "Missing parameter 'deck_size'"
    assert "remainofDeck" in params, "Missing parameter 'remainofDeck'"

def test_player_deck_has_hand_size():
    assert hasattr(player_Deck, "hand_size")
    descriptor = None
    for klass in player_Deck.__mro__:
        if "hand_size" in klass.__dict__:
            descriptor = klass.__dict__["hand_size"]
            break
    assert isinstance(descriptor, property)

def test_player_deck_has_numberofShuffles():
    assert hasattr(player_Deck, "numberofShuffles")
    descriptor = None
    for klass in player_Deck.__mro__:
        if "numberofShuffles" in klass.__dict__:
            descriptor = klass.__dict__["numberofShuffles"]
            break
    assert isinstance(descriptor, property)

def test_player_deck_has_deck_size():
    assert hasattr(player_Deck, "deck_size")
    descriptor = None
    for klass in player_Deck.__mro__:
        if "deck_size" in klass.__dict__:
            descriptor = klass.__dict__["deck_size"]
            break
    assert isinstance(descriptor, property)

def test_player_deck_has_remainofDeck():
    assert hasattr(player_Deck, "remainofDeck")
    descriptor = None
    for klass in player_Deck.__mro__:
        if "remainofDeck" in klass.__dict__:
            descriptor = klass.__dict__["remainofDeck"]
            break
    assert isinstance(descriptor, property)



def test_player_player_is_not_abstract():
    assert not inspect.isabstract(player_Player)


def test_player_player_constructor_exists():
    assert callable(player_Player.__init__)


def test_player_player_constructor_args():
    sig = inspect.signature(player_Player.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())



def test_comparable_interface_is_not_abstract():
    assert not inspect.isabstract(Comparable_Interface)


def test_comparable_interface_constructor_exists():
    assert callable(Comparable_Interface.__init__)


def test_comparable_interface_constructor_args():
    sig = inspect.signature(Comparable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_card_card_is_not_abstract():
    assert not inspect.isabstract(card_Card)


def test_card_card_constructor_exists():
    assert callable(card_Card.__init__)


def test_card_card_constructor_args():
    sig = inspect.signature(card_Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_card_card_has_suit():
    assert hasattr(card_Card, "suit")
    descriptor = None
    for klass in card_Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_card_card_has_rank():
    assert hasattr(card_Card, "rank")
    descriptor = None
    for klass in card_Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_poker_gamerun_is_not_abstract():
    assert not inspect.isabstract(poker_GameRun)


def test_poker_gamerun_constructor_exists():
    assert callable(poker_GameRun.__init__)


def test_poker_gamerun_constructor_args():
    sig = inspect.signature(poker_GameRun.__init__)
    params = list(sig.parameters.keys())



def test_poker_game_is_not_abstract():
    assert not inspect.isabstract(poker_Game)


def test_poker_game_constructor_exists():
    assert callable(poker_Game.__init__)


def test_poker_game_constructor_args():
    sig = inspect.signature(poker_Game.__init__)
    params = list(sig.parameters.keys())
    assert "hand_size" in params, "Missing parameter 'hand_size'"
    assert "tryagain" in params, "Missing parameter 'tryagain'"

def test_poker_game_has_hand_size():
    assert hasattr(poker_Game, "hand_size")
    descriptor = None
    for klass in poker_Game.__mro__:
        if "hand_size" in klass.__dict__:
            descriptor = klass.__dict__["hand_size"]
            break
    assert isinstance(descriptor, property)

def test_poker_game_has_tryagain():
    assert hasattr(poker_Game, "tryagain")
    descriptor = None
    for klass in poker_Game.__mro__:
        if "tryagain" in klass.__dict__:
            descriptor = klass.__dict__["tryagain"]
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
JFrame_strategy = st.builds(
    JFrame,
)
Board_strategy = st.builds(
    Board,
    cardArea=
        safe_text,
    playAagain=
        safe_text
)
player_Deck_strategy = st.builds(
    player_Deck,
    hand_size=
        st.integers(),
    numberofShuffles=
        st.integers(),
    deck_size=
        st.integers(),
    remainofDeck=
        st.integers()
)
player_Player_strategy = st.builds(
    player_Player,
)
Card_strategy = st.builds(
    Card,
)
Comparable_Interface_strategy = st.builds(
    Comparable_Interface,
)
card_Card_strategy = st.builds(
    card_Card,
    suit=
        st.integers(),
    rank=
        st.integers()
)
poker_GameRun_strategy = st.builds(
    poker_GameRun,
)
poker_Game_strategy = st.builds(
    poker_Game,
    hand_size=
        st.integers(),
    tryagain=
        st.integers()
)

@given(instance=JFrame_strategy)
@settings(max_examples=50)
def test_jframe_instantiation(instance):
    assert isinstance(instance, JFrame)

@given(instance=Board_strategy)
@settings(max_examples=50)
def test_board_instantiation(instance):
    assert isinstance(instance, Board)



@given(instance=Board_strategy)
def test_board_cardArea_setter(instance):
    original = instance.cardArea
    instance.cardArea = original
    assert instance.cardArea == original



@given(instance=Board_strategy)
def test_board_playAagain_setter(instance):
    original = instance.playAagain
    instance.playAagain = original
    assert instance.playAagain == original

@given(instance=player_Deck_strategy)
@settings(max_examples=50)
def test_player_deck_instantiation(instance):
    assert isinstance(instance, player_Deck)



@given(instance=player_Deck_strategy)
def test_player_deck_hand_size_setter(instance):
    original = instance.hand_size
    instance.hand_size = original
    assert instance.hand_size == original



@given(instance=player_Deck_strategy)
def test_player_deck_numberofShuffles_setter(instance):
    original = instance.numberofShuffles
    instance.numberofShuffles = original
    assert instance.numberofShuffles == original



@given(instance=player_Deck_strategy)
def test_player_deck_deck_size_setter(instance):
    original = instance.deck_size
    instance.deck_size = original
    assert instance.deck_size == original



@given(instance=player_Deck_strategy)
def test_player_deck_remainofDeck_setter(instance):
    original = instance.remainofDeck
    instance.remainofDeck = original
    assert instance.remainofDeck == original

@given(instance=player_Player_strategy)
@settings(max_examples=50)
def test_player_player_instantiation(instance):
    assert isinstance(instance, player_Player)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)

@given(instance=Comparable_Interface_strategy)
@settings(max_examples=50)
def test_comparable_interface_instantiation(instance):
    assert isinstance(instance, Comparable_Interface)

@given(instance=card_Card_strategy)
@settings(max_examples=50)
def test_card_card_instantiation(instance):
    assert isinstance(instance, card_Card)



@given(instance=card_Card_strategy)
def test_card_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=card_Card_strategy)
def test_card_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=poker_GameRun_strategy)
@settings(max_examples=50)
def test_poker_gamerun_instantiation(instance):
    assert isinstance(instance, poker_GameRun)

@given(instance=poker_Game_strategy)
@settings(max_examples=50)
def test_poker_game_instantiation(instance):
    assert isinstance(instance, poker_Game)



@given(instance=poker_Game_strategy)
def test_poker_game_hand_size_setter(instance):
    original = instance.hand_size
    instance.hand_size = original
    assert instance.hand_size == original



@given(instance=poker_Game_strategy)
def test_poker_game_tryagain_setter(instance):
    original = instance.tryagain
    instance.tryagain = original
    assert instance.tryagain == original
