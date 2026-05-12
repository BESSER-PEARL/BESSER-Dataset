import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MatchingGame,
    TrickGame,
    SheddingGame,
    Player,
    Game,
    Deck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_matchinggame_is_not_abstract():
    assert not inspect.isabstract(MatchingGame)


def test_matchinggame_constructor_exists():
    assert callable(MatchingGame.__init__)


def test_matchinggame_constructor_args():
    sig = inspect.signature(MatchingGame.__init__)
    params = list(sig.parameters.keys())



def test_trickgame_is_not_abstract():
    assert not inspect.isabstract(TrickGame)


def test_trickgame_constructor_exists():
    assert callable(TrickGame.__init__)


def test_trickgame_constructor_args():
    sig = inspect.signature(TrickGame.__init__)
    params = list(sig.parameters.keys())



def test_sheddinggame_is_not_abstract():
    assert not inspect.isabstract(SheddingGame)


def test_sheddinggame_constructor_exists():
    assert callable(SheddingGame.__init__)


def test_sheddinggame_constructor_args():
    sig = inspect.signature(SheddingGame.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "hand" in params, "Missing parameter 'hand'"
    assert "score" in params, "Missing parameter 'score'"

def test_player_has_hand():
    assert hasattr(Player, "hand")
    descriptor = None
    for klass in Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)

def test_player_has_score():
    assert hasattr(Player, "score")
    descriptor = None
    for klass in Player.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "players" in params, "Missing parameter 'players'"
    assert "round" in params, "Missing parameter 'round'"
    assert "winner" in params, "Missing parameter 'winner'"

def test_game_has_players():
    assert hasattr(Game, "players")
    descriptor = None
    for klass in Game.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_game_has_round():
    assert hasattr(Game, "round")
    descriptor = None
    for klass in Game.__mro__:
        if "round" in klass.__dict__:
            descriptor = klass.__dict__["round"]
            break
    assert isinstance(descriptor, property)

def test_game_has_winner():
    assert hasattr(Game, "winner")
    descriptor = None
    for klass in Game.__mro__:
        if "winner" in klass.__dict__:
            descriptor = klass.__dict__["winner"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"

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
    assert "value" in params, "Missing parameter 'value'"

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_value():
    assert hasattr(Card, "value")
    descriptor = None
    for klass in Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
MatchingGame_strategy = st.builds(
    MatchingGame,
)
TrickGame_strategy = st.builds(
    TrickGame,
)
SheddingGame_strategy = st.builds(
    SheddingGame,
)
Player_strategy = st.builds(
    Player,
    hand=
        safe_text,
    score=
        st.integers()
)
Game_strategy = st.builds(
    Game,
    players=
        safe_text,
    round=
        st.integers(),
    winner=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    deck=
        safe_text
)
Card_strategy = st.builds(
    Card,
    suit=
        safe_text,
    value=
        st.integers()
)

@given(instance=MatchingGame_strategy)
@settings(max_examples=50)
def test_matchinggame_instantiation(instance):
    assert isinstance(instance, MatchingGame)

@given(instance=TrickGame_strategy)
@settings(max_examples=50)
def test_trickgame_instantiation(instance):
    assert isinstance(instance, TrickGame)

@given(instance=SheddingGame_strategy)
@settings(max_examples=50)
def test_sheddinggame_instantiation(instance):
    assert isinstance(instance, SheddingGame)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Player_strategy)
def test_player_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Game_strategy)
def test_game_round_setter(instance):
    original = instance.round
    instance.round = original
    assert instance.round == original



@given(instance=Game_strategy)
def test_game_winner_setter(instance):
    original = instance.winner
    instance.winner = original
    assert instance.winner == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



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
def test_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
