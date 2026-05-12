import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Hand,
    Card,
    Deck,
    BlackJack_Hra,
    BlackJackApp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "must_hit" in params, "Missing parameter 'must_hit'"
    assert "under" in params, "Missing parameter 'under'"
    assert "blackjack" in params, "Missing parameter 'blackjack'"
    assert "addcard" in params, "Missing parameter 'addcard'"
    assert "bestscore" in params, "Missing parameter 'bestscore'"
    assert "busted" in params, "Missing parameter 'busted'"
    assert "num_card" in params, "Missing parameter 'num_card'"
    assert "max_cards" in params, "Missing parameter 'max_cards'"
    assert "hand" in params, "Missing parameter 'hand'"

def test_hand_has_must_hit():
    assert hasattr(Hand, "must_hit")
    descriptor = None
    for klass in Hand.__mro__:
        if "must_hit" in klass.__dict__:
            descriptor = klass.__dict__["must_hit"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_under():
    assert hasattr(Hand, "under")
    descriptor = None
    for klass in Hand.__mro__:
        if "under" in klass.__dict__:
            descriptor = klass.__dict__["under"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_blackjack():
    assert hasattr(Hand, "blackjack")
    descriptor = None
    for klass in Hand.__mro__:
        if "blackjack" in klass.__dict__:
            descriptor = klass.__dict__["blackjack"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_addcard():
    assert hasattr(Hand, "addcard")
    descriptor = None
    for klass in Hand.__mro__:
        if "addcard" in klass.__dict__:
            descriptor = klass.__dict__["addcard"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_bestscore():
    assert hasattr(Hand, "bestscore")
    descriptor = None
    for klass in Hand.__mro__:
        if "bestscore" in klass.__dict__:
            descriptor = klass.__dict__["bestscore"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_busted():
    assert hasattr(Hand, "busted")
    descriptor = None
    for klass in Hand.__mro__:
        if "busted" in klass.__dict__:
            descriptor = klass.__dict__["busted"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_num_card():
    assert hasattr(Hand, "num_card")
    descriptor = None
    for klass in Hand.__mro__:
        if "num_card" in klass.__dict__:
            descriptor = klass.__dict__["num_card"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_max_cards():
    assert hasattr(Hand, "max_cards")
    descriptor = None
    for klass in Hand.__mro__:
        if "max_cards" in klass.__dict__:
            descriptor = klass.__dict__["max_cards"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_hand():
    assert hasattr(Hand, "hand")
    descriptor = None
    for klass in Hand.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "cards" in params, "Missing parameter 'cards'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_value():
    assert hasattr(Card, "value")
    descriptor = None
    for klass in Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cards():
    assert hasattr(Card, "cards")
    descriptor = None
    for klass in Card.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
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



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "top_card" in params, "Missing parameter 'top_card'"
    assert "shuffle" in params, "Missing parameter 'shuffle'"
    assert "deal_card" in params, "Missing parameter 'deal_card'"
    assert "random_cards" in params, "Missing parameter 'random_cards'"
    assert "cards" in params, "Missing parameter 'cards'"
    assert "random" in params, "Missing parameter 'random'"
    assert "deck" in params, "Missing parameter 'deck'"

def test_deck_has_top_card():
    assert hasattr(Deck, "top_card")
    descriptor = None
    for klass in Deck.__mro__:
        if "top_card" in klass.__dict__:
            descriptor = klass.__dict__["top_card"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_shuffle():
    assert hasattr(Deck, "shuffle")
    descriptor = None
    for klass in Deck.__mro__:
        if "shuffle" in klass.__dict__:
            descriptor = klass.__dict__["shuffle"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_deal_card():
    assert hasattr(Deck, "deal_card")
    descriptor = None
    for klass in Deck.__mro__:
        if "deal_card" in klass.__dict__:
            descriptor = klass.__dict__["deal_card"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_random_cards():
    assert hasattr(Deck, "random_cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "random_cards" in klass.__dict__:
            descriptor = klass.__dict__["random_cards"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_cards():
    assert hasattr(Deck, "cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_random():
    assert hasattr(Deck, "random")
    descriptor = None
    for klass in Deck.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_deck():
    assert hasattr(Deck, "deck")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_hra_is_not_abstract():
    assert not inspect.isabstract(BlackJack_Hra)


def test_blackjack_hra_constructor_exists():
    assert callable(BlackJack_Hra.__init__)


def test_blackjack_hra_constructor_args():
    sig = inspect.signature(BlackJack_Hra.__init__)
    params = list(sig.parameters.keys())
    assert "show_result" in params, "Missing parameter 'show_result'"
    assert "bet" in params, "Missing parameter 'bet'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "dealer_wins" in params, "Missing parameter 'dealer_wins'"
    assert "deal" in params, "Missing parameter 'deal'"
    assert "money" in params, "Missing parameter 'money'"
    assert "placebet" in params, "Missing parameter 'placebet'"
    assert "dealers_hand" in params, "Missing parameter 'dealers_hand'"
    assert "player_wins" in params, "Missing parameter 'player_wins'"
    assert "tie" in params, "Missing parameter 'tie'"
    assert "players_hand" in params, "Missing parameter 'players_hand'"
    assert "play" in params, "Missing parameter 'play'"
    assert "player_asks_for_card" in params, "Missing parameter 'player_asks_for_card'"

def test_blackjack_hra_has_show_result():
    assert hasattr(BlackJack_Hra, "show_result")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "show_result" in klass.__dict__:
            descriptor = klass.__dict__["show_result"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_bet():
    assert hasattr(BlackJack_Hra, "bet")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_deck():
    assert hasattr(BlackJack_Hra, "deck")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_dealer_wins():
    assert hasattr(BlackJack_Hra, "dealer_wins")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "dealer_wins" in klass.__dict__:
            descriptor = klass.__dict__["dealer_wins"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_deal():
    assert hasattr(BlackJack_Hra, "deal")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "deal" in klass.__dict__:
            descriptor = klass.__dict__["deal"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_money():
    assert hasattr(BlackJack_Hra, "money")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_placebet():
    assert hasattr(BlackJack_Hra, "placebet")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "placebet" in klass.__dict__:
            descriptor = klass.__dict__["placebet"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_dealers_hand():
    assert hasattr(BlackJack_Hra, "dealers_hand")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "dealers_hand" in klass.__dict__:
            descriptor = klass.__dict__["dealers_hand"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_player_wins():
    assert hasattr(BlackJack_Hra, "player_wins")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "player_wins" in klass.__dict__:
            descriptor = klass.__dict__["player_wins"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_tie():
    assert hasattr(BlackJack_Hra, "tie")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "tie" in klass.__dict__:
            descriptor = klass.__dict__["tie"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_players_hand():
    assert hasattr(BlackJack_Hra, "players_hand")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "players_hand" in klass.__dict__:
            descriptor = klass.__dict__["players_hand"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_play():
    assert hasattr(BlackJack_Hra, "play")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "play" in klass.__dict__:
            descriptor = klass.__dict__["play"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_hra_has_player_asks_for_card():
    assert hasattr(BlackJack_Hra, "player_asks_for_card")
    descriptor = None
    for klass in BlackJack_Hra.__mro__:
        if "player_asks_for_card" in klass.__dict__:
            descriptor = klass.__dict__["player_asks_for_card"]
            break
    assert isinstance(descriptor, property)



def test_blackjackapp_is_not_abstract():
    assert not inspect.isabstract(BlackJackApp)


def test_blackjackapp_constructor_exists():
    assert callable(BlackJackApp.__init__)


def test_blackjackapp_constructor_args():
    sig = inspect.signature(BlackJackApp.__init__)
    params = list(sig.parameters.keys())


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
Hand_strategy = st.builds(
    Hand,
    must_hit=
        st.booleans(),
    under=
        safe_text,
    blackjack=
        st.booleans(),
    addcard=
        safe_text,
    bestscore=
        safe_text,
    busted=
        safe_text,
    num_card=
        st.integers(),
    max_cards=
        st.integers(),
    hand=
        safe_text
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers(),
    cards=
        safe_text,
    suit=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    top_card=
        safe_text,
    shuffle=
        safe_text,
    deal_card=
        safe_text,
    random_cards=
        safe_text,
    cards=
        safe_text,
    random=
        safe_text,
    deck=
        safe_text
)
BlackJack_Hra_strategy = st.builds(
    BlackJack_Hra,
    show_result=
        safe_text,
    bet=
        safe_text,
    deck=
        safe_text,
    dealer_wins=
        safe_text,
    deal=
        safe_text,
    money=
        safe_text,
    placebet=
        safe_text,
    dealers_hand=
        safe_text,
    player_wins=
        safe_text,
    tie=
        safe_text,
    players_hand=
        safe_text,
    play=
        safe_text,
    player_asks_for_card=
        safe_text
)
BlackJackApp_strategy = st.builds(
    BlackJackApp,
)

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hand_instantiation(instance):
    assert isinstance(instance, Hand)



@given(instance=Hand_strategy)
def test_hand_must_hit_setter(instance):
    original = instance.must_hit
    instance.must_hit = original
    assert instance.must_hit == original



@given(instance=Hand_strategy)
def test_hand_under_setter(instance):
    original = instance.under
    instance.under = original
    assert instance.under == original



@given(instance=Hand_strategy)
def test_hand_blackjack_setter(instance):
    original = instance.blackjack
    instance.blackjack = original
    assert instance.blackjack == original



@given(instance=Hand_strategy)
def test_hand_addcard_setter(instance):
    original = instance.addcard
    instance.addcard = original
    assert instance.addcard == original



@given(instance=Hand_strategy)
def test_hand_bestscore_setter(instance):
    original = instance.bestscore
    instance.bestscore = original
    assert instance.bestscore == original



@given(instance=Hand_strategy)
def test_hand_busted_setter(instance):
    original = instance.busted
    instance.busted = original
    assert instance.busted == original



@given(instance=Hand_strategy)
def test_hand_num_card_setter(instance):
    original = instance.num_card
    instance.num_card = original
    assert instance.num_card == original



@given(instance=Hand_strategy)
def test_hand_max_cards_setter(instance):
    original = instance.max_cards
    instance.max_cards = original
    assert instance.max_cards == original



@given(instance=Hand_strategy)
def test_hand_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Card_strategy)
def test_card_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_top_card_setter(instance):
    original = instance.top_card
    instance.top_card = original
    assert instance.top_card == original



@given(instance=Deck_strategy)
def test_deck_shuffle_setter(instance):
    original = instance.shuffle
    instance.shuffle = original
    assert instance.shuffle == original



@given(instance=Deck_strategy)
def test_deck_deal_card_setter(instance):
    original = instance.deal_card
    instance.deal_card = original
    assert instance.deal_card == original



@given(instance=Deck_strategy)
def test_deck_random_cards_setter(instance):
    original = instance.random_cards
    instance.random_cards = original
    assert instance.random_cards == original



@given(instance=Deck_strategy)
def test_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Deck_strategy)
def test_deck_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original



@given(instance=Deck_strategy)
def test_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original

@given(instance=BlackJack_Hra_strategy)
@settings(max_examples=50)
def test_blackjack_hra_instantiation(instance):
    assert isinstance(instance, BlackJack_Hra)



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_show_result_setter(instance):
    original = instance.show_result
    instance.show_result = original
    assert instance.show_result == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_dealer_wins_setter(instance):
    original = instance.dealer_wins
    instance.dealer_wins = original
    assert instance.dealer_wins == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_deal_setter(instance):
    original = instance.deal
    instance.deal = original
    assert instance.deal == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_placebet_setter(instance):
    original = instance.placebet
    instance.placebet = original
    assert instance.placebet == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_dealers_hand_setter(instance):
    original = instance.dealers_hand
    instance.dealers_hand = original
    assert instance.dealers_hand == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_player_wins_setter(instance):
    original = instance.player_wins
    instance.player_wins = original
    assert instance.player_wins == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_tie_setter(instance):
    original = instance.tie
    instance.tie = original
    assert instance.tie == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_players_hand_setter(instance):
    original = instance.players_hand
    instance.players_hand = original
    assert instance.players_hand == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_play_setter(instance):
    original = instance.play
    instance.play = original
    assert instance.play == original



@given(instance=BlackJack_Hra_strategy)
def test_blackjack_hra_player_asks_for_card_setter(instance):
    original = instance.player_asks_for_card
    instance.player_asks_for_card = original
    assert instance.player_asks_for_card == original

@given(instance=BlackJackApp_strategy)
@settings(max_examples=50)
def test_blackjackapp_instantiation(instance):
    assert isinstance(instance, BlackJackApp)
