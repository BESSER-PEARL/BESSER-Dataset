import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Card,
    Deck,
    Hand,
    Player,
    Game,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "strength" in params, "Missing parameter 'strength'"

def test_card_has_name():
    assert hasattr(Card, "name")
    descriptor = None
    for klass in Card.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_card_has_id():
    assert hasattr(Card, "id")
    descriptor = None
    for klass in Card.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_card_has_strength():
    assert hasattr(Card, "strength")
    descriptor = None
    for klass in Card.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "id" in params, "Missing parameter 'id'"
    assert "players" in params, "Missing parameter 'players'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "cards" in params, "Missing parameter 'cards'"

def test_deck_has_attribute():
    assert hasattr(Deck, "attribute")
    descriptor = None
    for klass in Deck.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_id():
    assert hasattr(Deck, "id")
    descriptor = None
    for klass in Deck.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_players():
    assert hasattr(Deck, "players")
    descriptor = None
    for klass in Deck.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_attribute2():
    assert hasattr(Deck, "attribute2")
    descriptor = None
    for klass in Deck.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
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



def test_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "game" in params, "Missing parameter 'game'"
    assert "id" in params, "Missing parameter 'id'"
    assert "player" in params, "Missing parameter 'player'"

def test_hand_has_cards():
    assert hasattr(Hand, "cards")
    descriptor = None
    for klass in Hand.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_game():
    assert hasattr(Hand, "game")
    descriptor = None
    for klass in Hand.__mro__:
        if "game" in klass.__dict__:
            descriptor = klass.__dict__["game"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_id():
    assert hasattr(Hand, "id")
    descriptor = None
    for klass in Hand.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hand_has_player():
    assert hasattr(Hand, "player")
    descriptor = None
    for klass in Hand.__mro__:
        if "player" in klass.__dict__:
            descriptor = klass.__dict__["player"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "game" in params, "Missing parameter 'game'"
    assert "cards" in params, "Missing parameter 'cards'"
    assert "name" in params, "Missing parameter 'name'"

def test_player_has_id():
    assert hasattr(Player, "id")
    descriptor = None
    for klass in Player.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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

def test_player_has_game():
    assert hasattr(Player, "game")
    descriptor = None
    for klass in Player.__mro__:
        if "game" in klass.__dict__:
            descriptor = klass.__dict__["game"]
            break
    assert isinstance(descriptor, property)

def test_player_has_cards():
    assert hasattr(Player, "cards")
    descriptor = None
    for klass in Player.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
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



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "players" in params, "Missing parameter 'players'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "status" in params, "Missing parameter 'status'"
    assert "name" in params, "Missing parameter 'name'"

def test_game_has_id():
    assert hasattr(Game, "id")
    descriptor = None
    for klass in Game.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_game_has_players():
    assert hasattr(Game, "players")
    descriptor = None
    for klass in Game.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_game_has_deck():
    assert hasattr(Game, "deck")
    descriptor = None
    for klass in Game.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_game_has_status():
    assert hasattr(Game, "status")
    descriptor = None
    for klass in Game.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_game_has_name():
    assert hasattr(Game, "name")
    descriptor = None
    for klass in Game.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Card_strategy = st.builds(
    Card,
    name=
        safe_text,
    id=
        st.integers(),
    strength=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    attribute=
        safe_text,
    id=
        st.integers(),
    players=
        safe_text,
    attribute2=
        safe_text,
    cards=
        safe_text
)
Hand_strategy = st.builds(
    Hand,
    cards=
        safe_text,
    game=
        st.none(),
    id=
        st.integers(),
    player=
        st.none()
)
Player_strategy = st.builds(
    Player,
    id=
        st.integers(),
    hand=
        st.none(),
    game=
        st.none(),
    cards=
        safe_text,
    name=
        safe_text
)
Game_strategy = st.builds(
    Game,
    id=
        safe_text,
    players=
        safe_text,
    deck=
        st.none(),
    status=
        safe_text,
    name=
        safe_text
)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Card_strategy)
def test_card_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Card_strategy)
def test_card_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Deck_strategy)
def test_deck_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Deck_strategy)
def test_deck_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Deck_strategy)
def test_deck_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Deck_strategy)
def test_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hand_instantiation(instance):
    assert isinstance(instance, Hand)



@given(instance=Hand_strategy)
def test_hand_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Hand_strategy)
def test_hand_game_setter(instance):
    original = instance.game
    instance.game = original
    assert instance.game == original



@given(instance=Hand_strategy)
def test_hand_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Hand_strategy)
def test_hand_player_setter(instance):
    original = instance.player
    instance.player = original
    assert instance.player == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Player_strategy)
def test_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Player_strategy)
def test_player_game_setter(instance):
    original = instance.game
    instance.game = original
    assert instance.game == original



@given(instance=Player_strategy)
def test_player_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Game_strategy)
def test_game_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Game_strategy)
def test_game_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=Game_strategy)
def test_game_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Game_strategy)
def test_game_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
