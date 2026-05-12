import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BlackJackMain,
    Game,
    Player,
    Deck,
    Card,
    List_Card__external,
    Rank,
    Suit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_blackjackmain_is_not_abstract():
    assert not inspect.isabstract(BlackJackMain)


def test_blackjackmain_constructor_exists():
    assert callable(BlackJackMain.__init__)


def test_blackjackmain_constructor_args():
    sig = inspect.signature(BlackJackMain.__init__)
    params = list(sig.parameters.keys())



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "playerCards" in params, "Missing parameter 'playerCards'"
    assert "dealerCards" in params, "Missing parameter 'dealerCards'"

def test_game_has_playerCards():
    assert hasattr(Game, "playerCards")
    descriptor = None
    for klass in Game.__mro__:
        if "playerCards" in klass.__dict__:
            descriptor = klass.__dict__["playerCards"]
            break
    assert isinstance(descriptor, property)

def test_game_has_dealerCards():
    assert hasattr(Game, "dealerCards")
    descriptor = None
    for klass in Game.__mro__:
        if "dealerCards" in klass.__dict__:
            descriptor = klass.__dict__["dealerCards"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"
    assert "name" in params, "Missing parameter 'name'"

def test_player_has_money():
    assert hasattr(Player, "money")
    descriptor = None
    for klass in Player.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
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



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cardsDealt" in params, "Missing parameter 'cardsDealt'"
    assert "deck" in params, "Missing parameter 'deck'"

def test_deck_has_cardsDealt():
    assert hasattr(Deck, "cardsDealt")
    descriptor = None
    for klass in Deck.__mro__:
        if "cardsDealt" in klass.__dict__:
            descriptor = klass.__dict__["cardsDealt"]
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



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
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



def test_list_card__external_is_not_abstract():
    assert not inspect.isabstract(List_Card__external)


def test_list_card__external_constructor_exists():
    assert callable(List_Card__external.__init__)


def test_list_card__external_constructor_args():
    sig = inspect.signature(List_Card__external.__init__)
    params = list(sig.parameters.keys())

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
BlackJackMain_strategy = st.builds(
    BlackJackMain,
)
Game_strategy = st.builds(
    Game,
    playerCards=
        safe_text,
    dealerCards=
        safe_text
)
Player_strategy = st.builds(
    Player,
    money=
        st.integers(),
    name=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    cardsDealt=
        safe_text,
    deck=
        safe_text
)
Card_strategy = st.builds(
    Card,
    suit=
        st.none(),
    rank=
        st.none()
)
List_Card__external_strategy = st.builds(
    List_Card__external,
)

@given(instance=BlackJackMain_strategy)
@settings(max_examples=50)
def test_blackjackmain_instantiation(instance):
    assert isinstance(instance, BlackJackMain)

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_playerCards_setter(instance):
    original = instance.playerCards
    instance.playerCards = original
    assert instance.playerCards == original



@given(instance=Game_strategy)
def test_game_dealerCards_setter(instance):
    original = instance.dealerCards
    instance.dealerCards = original
    assert instance.dealerCards == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_cardsDealt_setter(instance):
    original = instance.cardsDealt
    instance.cardsDealt = original
    assert instance.cardsDealt == original



@given(instance=Deck_strategy)
def test_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original

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
def test_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=List_Card__external_strategy)
@settings(max_examples=50)
def test_list_card__external_instantiation(instance):
    assert isinstance(instance, List_Card__external)
