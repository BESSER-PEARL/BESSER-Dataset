import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Money_PlayerMoney,
    GUI_Interface,
    Comparable_Interface,
    Main_StartGame,
    Player_Players,
    Game_EvaluateHand,
    Game_Display,
    Game_Ranking,
    Card_Cards,
    Card_Deck,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_money_playermoney_is_not_abstract():
    assert not inspect.isabstract(Money_PlayerMoney)


def test_money_playermoney_constructor_exists():
    assert callable(Money_PlayerMoney.__init__)


def test_money_playermoney_constructor_args():
    sig = inspect.signature(Money_PlayerMoney.__init__)
    params = list(sig.parameters.keys())
    assert "totalmoney" in params, "Missing parameter 'totalmoney'"
    assert "numofplayers" in params, "Missing parameter 'numofplayers'"

def test_money_playermoney_has_totalmoney():
    assert hasattr(Money_PlayerMoney, "totalmoney")
    descriptor = None
    for klass in Money_PlayerMoney.__mro__:
        if "totalmoney" in klass.__dict__:
            descriptor = klass.__dict__["totalmoney"]
            break
    assert isinstance(descriptor, property)

def test_money_playermoney_has_numofplayers():
    assert hasattr(Money_PlayerMoney, "numofplayers")
    descriptor = None
    for klass in Money_PlayerMoney.__mro__:
        if "numofplayers" in klass.__dict__:
            descriptor = klass.__dict__["numofplayers"]
            break
    assert isinstance(descriptor, property)



def test_gui_interface_is_not_abstract():
    assert not inspect.isabstract(GUI_Interface)


def test_gui_interface_constructor_exists():
    assert callable(GUI_Interface.__init__)


def test_gui_interface_constructor_args():
    sig = inspect.signature(GUI_Interface.__init__)
    params = list(sig.parameters.keys())



def test_comparable_interface_is_not_abstract():
    assert not inspect.isabstract(Comparable_Interface)


def test_comparable_interface_constructor_exists():
    assert callable(Comparable_Interface.__init__)


def test_comparable_interface_constructor_args():
    sig = inspect.signature(Comparable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_main_startgame_is_not_abstract():
    assert not inspect.isabstract(Main_StartGame)


def test_main_startgame_constructor_exists():
    assert callable(Main_StartGame.__init__)


def test_main_startgame_constructor_args():
    sig = inspect.signature(Main_StartGame.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"
    assert "handsize" in params, "Missing parameter 'handsize'"
    assert "player" in params, "Missing parameter 'player'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "scanner" in params, "Missing parameter 'scanner'"

def test_main_startgame_has_deck():
    assert hasattr(Main_StartGame, "deck")
    descriptor = None
    for klass in Main_StartGame.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_main_startgame_has_handsize():
    assert hasattr(Main_StartGame, "handsize")
    descriptor = None
    for klass in Main_StartGame.__mro__:
        if "handsize" in klass.__dict__:
            descriptor = klass.__dict__["handsize"]
            break
    assert isinstance(descriptor, property)

def test_main_startgame_has_player():
    assert hasattr(Main_StartGame, "player")
    descriptor = None
    for klass in Main_StartGame.__mro__:
        if "player" in klass.__dict__:
            descriptor = klass.__dict__["player"]
            break
    assert isinstance(descriptor, property)

def test_main_startgame_has_hand():
    assert hasattr(Main_StartGame, "hand")
    descriptor = None
    for klass in Main_StartGame.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)

def test_main_startgame_has_scanner():
    assert hasattr(Main_StartGame, "scanner")
    descriptor = None
    for klass in Main_StartGame.__mro__:
        if "scanner" in klass.__dict__:
            descriptor = klass.__dict__["scanner"]
            break
    assert isinstance(descriptor, property)



def test_player_players_is_not_abstract():
    assert not inspect.isabstract(Player_Players)


def test_player_players_constructor_exists():
    assert callable(Player_Players.__init__)


def test_player_players_constructor_args():
    sig = inspect.signature(Player_Players.__init__)
    params = list(sig.parameters.keys())



def test_game_evaluatehand_is_not_abstract():
    assert not inspect.isabstract(Game_EvaluateHand)


def test_game_evaluatehand_constructor_exists():
    assert callable(Game_EvaluateHand.__init__)


def test_game_evaluatehand_constructor_args():
    sig = inspect.signature(Game_EvaluateHand.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_game_evaluatehand_has_card():
    assert hasattr(Game_EvaluateHand, "card")
    descriptor = None
    for klass in Game_EvaluateHand.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_game_display_is_not_abstract():
    assert not inspect.isabstract(Game_Display)


def test_game_display_constructor_exists():
    assert callable(Game_Display.__init__)


def test_game_display_constructor_args():
    sig = inspect.signature(Game_Display.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"
    assert "card" in params, "Missing parameter 'card'"

def test_game_display_has_money():
    assert hasattr(Game_Display, "money")
    descriptor = None
    for klass in Game_Display.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_game_display_has_card():
    assert hasattr(Game_Display, "card")
    descriptor = None
    for klass in Game_Display.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_game_ranking_is_not_abstract():
    assert not inspect.isabstract(Game_Ranking)


def test_game_ranking_constructor_exists():
    assert callable(Game_Ranking.__init__)


def test_game_ranking_constructor_args():
    sig = inspect.signature(Game_Ranking.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_game_ranking_has_card():
    assert hasattr(Game_Ranking, "card")
    descriptor = None
    for klass in Game_Ranking.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_card_cards_is_not_abstract():
    assert not inspect.isabstract(Card_Cards)


def test_card_cards_constructor_exists():
    assert callable(Card_Cards.__init__)


def test_card_cards_constructor_args():
    sig = inspect.signature(Card_Cards.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_cards_has_rank():
    assert hasattr(Card_Cards, "rank")
    descriptor = None
    for klass in Card_Cards.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_card_cards_has_suit():
    assert hasattr(Card_Cards, "suit")
    descriptor = None
    for klass in Card_Cards.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)



def test_card_deck_is_not_abstract():
    assert not inspect.isabstract(Card_Deck)


def test_card_deck_constructor_exists():
    assert callable(Card_Deck.__init__)


def test_card_deck_constructor_args():
    sig = inspect.signature(Card_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "random" in params, "Missing parameter 'random'"
    assert "handsize" in params, "Missing parameter 'handsize'"
    assert "remainder" in params, "Missing parameter 'remainder'"
    assert "decksize" in params, "Missing parameter 'decksize'"
    assert "shuffletimes" in params, "Missing parameter 'shuffletimes'"
    assert "deck" in params, "Missing parameter 'deck'"

def test_card_deck_has_random():
    assert hasattr(Card_Deck, "random")
    descriptor = None
    for klass in Card_Deck.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)

def test_card_deck_has_handsize():
    assert hasattr(Card_Deck, "handsize")
    descriptor = None
    for klass in Card_Deck.__mro__:
        if "handsize" in klass.__dict__:
            descriptor = klass.__dict__["handsize"]
            break
    assert isinstance(descriptor, property)

def test_card_deck_has_remainder():
    assert hasattr(Card_Deck, "remainder")
    descriptor = None
    for klass in Card_Deck.__mro__:
        if "remainder" in klass.__dict__:
            descriptor = klass.__dict__["remainder"]
            break
    assert isinstance(descriptor, property)

def test_card_deck_has_decksize():
    assert hasattr(Card_Deck, "decksize")
    descriptor = None
    for klass in Card_Deck.__mro__:
        if "decksize" in klass.__dict__:
            descriptor = klass.__dict__["decksize"]
            break
    assert isinstance(descriptor, property)

def test_card_deck_has_shuffletimes():
    assert hasattr(Card_Deck, "shuffletimes")
    descriptor = None
    for klass in Card_Deck.__mro__:
        if "shuffletimes" in klass.__dict__:
            descriptor = klass.__dict__["shuffletimes"]
            break
    assert isinstance(descriptor, property)

def test_card_deck_has_deck():
    assert hasattr(Card_Deck, "deck")
    descriptor = None
    for klass in Card_Deck.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
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
Money_PlayerMoney_strategy = st.builds(
    Money_PlayerMoney,
    totalmoney=
        safe_text,
    numofplayers=
        safe_text
)
GUI_Interface_strategy = st.builds(
    GUI_Interface,
)
Comparable_Interface_strategy = st.builds(
    Comparable_Interface,
)
Main_StartGame_strategy = st.builds(
    Main_StartGame,
    deck=
        safe_text,
    handsize=
        st.integers(),
    player=
        safe_text,
    hand=
        safe_text,
    scanner=
        safe_text
)
Player_Players_strategy = st.builds(
    Player_Players,
)
Game_EvaluateHand_strategy = st.builds(
    Game_EvaluateHand,
    card=
        safe_text
)
Game_Display_strategy = st.builds(
    Game_Display,
    money=
        safe_text,
    card=
        safe_text
)
Game_Ranking_strategy = st.builds(
    Game_Ranking,
    card=
        safe_text
)
Card_Cards_strategy = st.builds(
    Card_Cards,
    rank=
        st.integers(),
    suit=
        st.integers()
)
Card_Deck_strategy = st.builds(
    Card_Deck,
    random=
        safe_text,
    handsize=
        st.integers(),
    remainder=
        st.integers(),
    decksize=
        st.integers(),
    shuffletimes=
        st.integers(),
    deck=
        safe_text
)

@given(instance=Money_PlayerMoney_strategy)
@settings(max_examples=50)
def test_money_playermoney_instantiation(instance):
    assert isinstance(instance, Money_PlayerMoney)



@given(instance=Money_PlayerMoney_strategy)
def test_money_playermoney_totalmoney_setter(instance):
    original = instance.totalmoney
    instance.totalmoney = original
    assert instance.totalmoney == original



@given(instance=Money_PlayerMoney_strategy)
def test_money_playermoney_numofplayers_setter(instance):
    original = instance.numofplayers
    instance.numofplayers = original
    assert instance.numofplayers == original

@given(instance=GUI_Interface_strategy)
@settings(max_examples=50)
def test_gui_interface_instantiation(instance):
    assert isinstance(instance, GUI_Interface)

@given(instance=Comparable_Interface_strategy)
@settings(max_examples=50)
def test_comparable_interface_instantiation(instance):
    assert isinstance(instance, Comparable_Interface)

@given(instance=Main_StartGame_strategy)
@settings(max_examples=50)
def test_main_startgame_instantiation(instance):
    assert isinstance(instance, Main_StartGame)



@given(instance=Main_StartGame_strategy)
def test_main_startgame_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=Main_StartGame_strategy)
def test_main_startgame_handsize_setter(instance):
    original = instance.handsize
    instance.handsize = original
    assert instance.handsize == original



@given(instance=Main_StartGame_strategy)
def test_main_startgame_player_setter(instance):
    original = instance.player
    instance.player = original
    assert instance.player == original



@given(instance=Main_StartGame_strategy)
def test_main_startgame_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Main_StartGame_strategy)
def test_main_startgame_scanner_setter(instance):
    original = instance.scanner
    instance.scanner = original
    assert instance.scanner == original

@given(instance=Player_Players_strategy)
@settings(max_examples=50)
def test_player_players_instantiation(instance):
    assert isinstance(instance, Player_Players)

@given(instance=Game_EvaluateHand_strategy)
@settings(max_examples=50)
def test_game_evaluatehand_instantiation(instance):
    assert isinstance(instance, Game_EvaluateHand)



@given(instance=Game_EvaluateHand_strategy)
def test_game_evaluatehand_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=Game_Display_strategy)
@settings(max_examples=50)
def test_game_display_instantiation(instance):
    assert isinstance(instance, Game_Display)



@given(instance=Game_Display_strategy)
def test_game_display_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Game_Display_strategy)
def test_game_display_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=Game_Ranking_strategy)
@settings(max_examples=50)
def test_game_ranking_instantiation(instance):
    assert isinstance(instance, Game_Ranking)



@given(instance=Game_Ranking_strategy)
def test_game_ranking_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=Card_Cards_strategy)
@settings(max_examples=50)
def test_card_cards_instantiation(instance):
    assert isinstance(instance, Card_Cards)



@given(instance=Card_Cards_strategy)
def test_card_cards_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_Cards_strategy)
def test_card_cards_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original

@given(instance=Card_Deck_strategy)
@settings(max_examples=50)
def test_card_deck_instantiation(instance):
    assert isinstance(instance, Card_Deck)



@given(instance=Card_Deck_strategy)
def test_card_deck_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original



@given(instance=Card_Deck_strategy)
def test_card_deck_handsize_setter(instance):
    original = instance.handsize
    instance.handsize = original
    assert instance.handsize == original



@given(instance=Card_Deck_strategy)
def test_card_deck_remainder_setter(instance):
    original = instance.remainder
    instance.remainder = original
    assert instance.remainder == original



@given(instance=Card_Deck_strategy)
def test_card_deck_decksize_setter(instance):
    original = instance.decksize
    instance.decksize = original
    assert instance.decksize == original



@given(instance=Card_Deck_strategy)
def test_card_deck_shuffletimes_setter(instance):
    original = instance.shuffletimes
    instance.shuffletimes = original
    assert instance.shuffletimes == original



@given(instance=Card_Deck_strategy)
def test_card_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original
