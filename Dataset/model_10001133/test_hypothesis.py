import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GameController,
    int_Interface,
    MatchingGame,
    TrickGame,
    SheddingGame,
    GameBoard,
    Player,
    CardGame,
    Deck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gamecontroller_is_not_abstract():
    assert not inspect.isabstract(GameController)


def test_gamecontroller_constructor_exists():
    assert callable(GameController.__init__)


def test_gamecontroller_constructor_args():
    sig = inspect.signature(GameController.__init__)
    params = list(sig.parameters.keys())
    assert "cardGame" in params, "Missing parameter 'cardGame'"
    assert "gameView" in params, "Missing parameter 'gameView'"

def test_gamecontroller_has_cardGame():
    assert hasattr(GameController, "cardGame")
    descriptor = None
    for klass in GameController.__mro__:
        if "cardGame" in klass.__dict__:
            descriptor = klass.__dict__["cardGame"]
            break
    assert isinstance(descriptor, property)

def test_gamecontroller_has_gameView():
    assert hasattr(GameController, "gameView")
    descriptor = None
    for klass in GameController.__mro__:
        if "gameView" in klass.__dict__:
            descriptor = klass.__dict__["gameView"]
            break
    assert isinstance(descriptor, property)



def test_int_interface_is_not_abstract():
    assert not inspect.isabstract(int_Interface)


def test_int_interface_constructor_exists():
    assert callable(int_Interface.__init__)


def test_int_interface_constructor_args():
    sig = inspect.signature(int_Interface.__init__)
    params = list(sig.parameters.keys())



def test_matchinggame_is_not_abstract():
    assert not inspect.isabstract(MatchingGame)


def test_matchinggame_constructor_exists():
    assert callable(MatchingGame.__init__)


def test_matchinggame_constructor_args():
    sig = inspect.signature(MatchingGame.__init__)
    params = list(sig.parameters.keys())
    assert "matches" in params, "Missing parameter 'matches'"

def test_matchinggame_has_matches():
    assert hasattr(MatchingGame, "matches")
    descriptor = None
    for klass in MatchingGame.__mro__:
        if "matches" in klass.__dict__:
            descriptor = klass.__dict__["matches"]
            break
    assert isinstance(descriptor, property)



def test_trickgame_is_not_abstract():
    assert not inspect.isabstract(TrickGame)


def test_trickgame_constructor_exists():
    assert callable(TrickGame.__init__)


def test_trickgame_constructor_args():
    sig = inspect.signature(TrickGame.__init__)
    params = list(sig.parameters.keys())
    assert "trickRules" in params, "Missing parameter 'trickRules'"

def test_trickgame_has_trickRules():
    assert hasattr(TrickGame, "trickRules")
    descriptor = None
    for klass in TrickGame.__mro__:
        if "trickRules" in klass.__dict__:
            descriptor = klass.__dict__["trickRules"]
            break
    assert isinstance(descriptor, property)



def test_sheddinggame_is_not_abstract():
    assert not inspect.isabstract(SheddingGame)


def test_sheddinggame_constructor_exists():
    assert callable(SheddingGame.__init__)


def test_sheddinggame_constructor_args():
    sig = inspect.signature(SheddingGame.__init__)
    params = list(sig.parameters.keys())



def test_gameboard_is_not_abstract():
    assert not inspect.isabstract(GameBoard)


def test_gameboard_constructor_exists():
    assert callable(GameBoard.__init__)


def test_gameboard_constructor_args():
    sig = inspect.signature(GameBoard.__init__)
    params = list(sig.parameters.keys())
    assert "selectCard" in params, "Missing parameter 'selectCard'"
    assert "board" in params, "Missing parameter 'board'"
    assert "drawCard" in params, "Missing parameter 'drawCard'"
    assert "score" in params, "Missing parameter 'score'"
    assert "startGame" in params, "Missing parameter 'startGame'"

def test_gameboard_has_selectCard():
    assert hasattr(GameBoard, "selectCard")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "selectCard" in klass.__dict__:
            descriptor = klass.__dict__["selectCard"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_board():
    assert hasattr(GameBoard, "board")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_drawCard():
    assert hasattr(GameBoard, "drawCard")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "drawCard" in klass.__dict__:
            descriptor = klass.__dict__["drawCard"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_score():
    assert hasattr(GameBoard, "score")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_gameboard_has_startGame():
    assert hasattr(GameBoard, "startGame")
    descriptor = None
    for klass in GameBoard.__mro__:
        if "startGame" in klass.__dict__:
            descriptor = klass.__dict__["startGame"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"
    assert "hand" in params, "Missing parameter 'hand'"

def test_player_has_score():
    assert hasattr(Player, "score")
    descriptor = None
    for klass in Player.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
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



def test_cardgame_is_not_abstract():
    assert not inspect.isabstract(CardGame)


def test_cardgame_constructor_exists():
    assert callable(CardGame.__init__)


def test_cardgame_constructor_args():
    sig = inspect.signature(CardGame.__init__)
    params = list(sig.parameters.keys())
    assert "players" in params, "Missing parameter 'players'"
    assert "winner" in params, "Missing parameter 'winner'"
    assert "round" in params, "Missing parameter 'round'"

def test_cardgame_has_players():
    assert hasattr(CardGame, "players")
    descriptor = None
    for klass in CardGame.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_cardgame_has_winner():
    assert hasattr(CardGame, "winner")
    descriptor = None
    for klass in CardGame.__mro__:
        if "winner" in klass.__dict__:
            descriptor = klass.__dict__["winner"]
            break
    assert isinstance(descriptor, property)

def test_cardgame_has_round():
    assert hasattr(CardGame, "round")
    descriptor = None
    for klass in CardGame.__mro__:
        if "round" in klass.__dict__:
            descriptor = klass.__dict__["round"]
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
    assert "size" in params, "Missing parameter 'size'"

def test_deck_has_deck():
    assert hasattr(Deck, "deck")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_size():
    assert hasattr(Deck, "size")
    descriptor = None
    for klass in Deck.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "face" in params, "Missing parameter 'face'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_face():
    assert hasattr(Card, "face")
    descriptor = None
    for klass in Card.__mro__:
        if "face" in klass.__dict__:
            descriptor = klass.__dict__["face"]
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
GameController_strategy = st.builds(
    GameController,
    cardGame=
        st.none(),
    gameView=
        st.none()
)
int_Interface_strategy = st.builds(
    int_Interface,
)
MatchingGame_strategy = st.builds(
    MatchingGame,
    matches=
        st.integers()
)
TrickGame_strategy = st.builds(
    TrickGame,
    trickRules=
        safe_text
)
SheddingGame_strategy = st.builds(
    SheddingGame,
)
GameBoard_strategy = st.builds(
    GameBoard,
    selectCard=
        safe_text,
    board=
        safe_text,
    drawCard=
        safe_text,
    score=
        safe_text,
    startGame=
        safe_text
)
Player_strategy = st.builds(
    Player,
    score=
        st.integers(),
    hand=
        safe_text
)
CardGame_strategy = st.builds(
    CardGame,
    players=
        safe_text,
    winner=
        st.none(),
    round=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    deck=
        safe_text,
    size=
        st.integers()
)
Card_strategy = st.builds(
    Card,
    face=
        st.integers(),
    suit=
        safe_text
)

@given(instance=GameController_strategy)
@settings(max_examples=50)
def test_gamecontroller_instantiation(instance):
    assert isinstance(instance, GameController)



@given(instance=GameController_strategy)
def test_gamecontroller_cardGame_setter(instance):
    original = instance.cardGame
    instance.cardGame = original
    assert instance.cardGame == original



@given(instance=GameController_strategy)
def test_gamecontroller_gameView_setter(instance):
    original = instance.gameView
    instance.gameView = original
    assert instance.gameView == original

@given(instance=int_Interface_strategy)
@settings(max_examples=50)
def test_int_interface_instantiation(instance):
    assert isinstance(instance, int_Interface)

@given(instance=MatchingGame_strategy)
@settings(max_examples=50)
def test_matchinggame_instantiation(instance):
    assert isinstance(instance, MatchingGame)



@given(instance=MatchingGame_strategy)
def test_matchinggame_matches_setter(instance):
    original = instance.matches
    instance.matches = original
    assert instance.matches == original

@given(instance=TrickGame_strategy)
@settings(max_examples=50)
def test_trickgame_instantiation(instance):
    assert isinstance(instance, TrickGame)



@given(instance=TrickGame_strategy)
def test_trickgame_trickRules_setter(instance):
    original = instance.trickRules
    instance.trickRules = original
    assert instance.trickRules == original

@given(instance=SheddingGame_strategy)
@settings(max_examples=50)
def test_sheddinggame_instantiation(instance):
    assert isinstance(instance, SheddingGame)

@given(instance=GameBoard_strategy)
@settings(max_examples=50)
def test_gameboard_instantiation(instance):
    assert isinstance(instance, GameBoard)



@given(instance=GameBoard_strategy)
def test_gameboard_selectCard_setter(instance):
    original = instance.selectCard
    instance.selectCard = original
    assert instance.selectCard == original



@given(instance=GameBoard_strategy)
def test_gameboard_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original



@given(instance=GameBoard_strategy)
def test_gameboard_drawCard_setter(instance):
    original = instance.drawCard
    instance.drawCard = original
    assert instance.drawCard == original



@given(instance=GameBoard_strategy)
def test_gameboard_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=GameBoard_strategy)
def test_gameboard_startGame_setter(instance):
    original = instance.startGame
    instance.startGame = original
    assert instance.startGame == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=Player_strategy)
def test_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original

@given(instance=CardGame_strategy)
@settings(max_examples=50)
def test_cardgame_instantiation(instance):
    assert isinstance(instance, CardGame)



@given(instance=CardGame_strategy)
def test_cardgame_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=CardGame_strategy)
def test_cardgame_winner_setter(instance):
    original = instance.winner
    instance.winner = original
    assert instance.winner == original



@given(instance=CardGame_strategy)
def test_cardgame_round_setter(instance):
    original = instance.round
    instance.round = original
    assert instance.round == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=Deck_strategy)
def test_deck_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
