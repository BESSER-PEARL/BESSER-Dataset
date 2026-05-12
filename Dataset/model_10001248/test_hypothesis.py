import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AI,
    makeNewPlayer,
    Game,
    CommunityCards,
    Player,
    Card,
    Deck,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ai_is_not_abstract():
    assert not inspect.isabstract(AI)


def test_ai_constructor_exists():
    assert callable(AI.__init__)


def test_ai_constructor_args():
    sig = inspect.signature(AI.__init__)
    params = list(sig.parameters.keys())



def test_makenewplayer_is_not_abstract():
    assert not inspect.isabstract(makeNewPlayer)


def test_makenewplayer_constructor_exists():
    assert callable(makeNewPlayer.__init__)


def test_makenewplayer_constructor_args():
    sig = inspect.signature(makeNewPlayer.__init__)
    params = list(sig.parameters.keys())



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "pot" in params, "Missing parameter 'pot'"
    assert "players" in params, "Missing parameter 'players'"
    assert "bigBlindValue" in params, "Missing parameter 'bigBlindValue'"
    assert "currentDeck" in params, "Missing parameter 'currentDeck'"
    assert "currentCommunityCards" in params, "Missing parameter 'currentCommunityCards'"
    assert "currentBigBlind" in params, "Missing parameter 'currentBigBlind'"

def test_game_has_pot():
    assert hasattr(Game, "pot")
    descriptor = None
    for klass in Game.__mro__:
        if "pot" in klass.__dict__:
            descriptor = klass.__dict__["pot"]
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

def test_game_has_bigBlindValue():
    assert hasattr(Game, "bigBlindValue")
    descriptor = None
    for klass in Game.__mro__:
        if "bigBlindValue" in klass.__dict__:
            descriptor = klass.__dict__["bigBlindValue"]
            break
    assert isinstance(descriptor, property)

def test_game_has_currentDeck():
    assert hasattr(Game, "currentDeck")
    descriptor = None
    for klass in Game.__mro__:
        if "currentDeck" in klass.__dict__:
            descriptor = klass.__dict__["currentDeck"]
            break
    assert isinstance(descriptor, property)

def test_game_has_currentCommunityCards():
    assert hasattr(Game, "currentCommunityCards")
    descriptor = None
    for klass in Game.__mro__:
        if "currentCommunityCards" in klass.__dict__:
            descriptor = klass.__dict__["currentCommunityCards"]
            break
    assert isinstance(descriptor, property)

def test_game_has_currentBigBlind():
    assert hasattr(Game, "currentBigBlind")
    descriptor = None
    for klass in Game.__mro__:
        if "currentBigBlind" in klass.__dict__:
            descriptor = klass.__dict__["currentBigBlind"]
            break
    assert isinstance(descriptor, property)



def test_communitycards_is_not_abstract():
    assert not inspect.isabstract(CommunityCards)


def test_communitycards_constructor_exists():
    assert callable(CommunityCards.__init__)


def test_communitycards_constructor_args():
    sig = inspect.signature(CommunityCards.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"

def test_communitycards_has_cards():
    assert hasattr(CommunityCards, "cards")
    descriptor = None
    for klass in CommunityCards.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "isAllIn" in params, "Missing parameter 'isAllIn'"
    assert "chips" in params, "Missing parameter 'chips'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isFolded" in params, "Missing parameter 'isFolded'"
    assert "handValue" in params, "Missing parameter 'handValue'"
    assert "isSmallBlind" in params, "Missing parameter 'isSmallBlind'"
    assert "isBigBlind" in params, "Missing parameter 'isBigBlind'"
    assert "playerNumber" in params, "Missing parameter 'playerNumber'"
    assert "isAI" in params, "Missing parameter 'isAI'"

def test_player_has_isAllIn():
    assert hasattr(Player, "isAllIn")
    descriptor = None
    for klass in Player.__mro__:
        if "isAllIn" in klass.__dict__:
            descriptor = klass.__dict__["isAllIn"]
            break
    assert isinstance(descriptor, property)

def test_player_has_chips():
    assert hasattr(Player, "chips")
    descriptor = None
    for klass in Player.__mro__:
        if "chips" in klass.__dict__:
            descriptor = klass.__dict__["chips"]
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

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_has_isFolded():
    assert hasattr(Player, "isFolded")
    descriptor = None
    for klass in Player.__mro__:
        if "isFolded" in klass.__dict__:
            descriptor = klass.__dict__["isFolded"]
            break
    assert isinstance(descriptor, property)

def test_player_has_handValue():
    assert hasattr(Player, "handValue")
    descriptor = None
    for klass in Player.__mro__:
        if "handValue" in klass.__dict__:
            descriptor = klass.__dict__["handValue"]
            break
    assert isinstance(descriptor, property)

def test_player_has_isSmallBlind():
    assert hasattr(Player, "isSmallBlind")
    descriptor = None
    for klass in Player.__mro__:
        if "isSmallBlind" in klass.__dict__:
            descriptor = klass.__dict__["isSmallBlind"]
            break
    assert isinstance(descriptor, property)

def test_player_has_isBigBlind():
    assert hasattr(Player, "isBigBlind")
    descriptor = None
    for klass in Player.__mro__:
        if "isBigBlind" in klass.__dict__:
            descriptor = klass.__dict__["isBigBlind"]
            break
    assert isinstance(descriptor, property)

def test_player_has_playerNumber():
    assert hasattr(Player, "playerNumber")
    descriptor = None
    for klass in Player.__mro__:
        if "playerNumber" in klass.__dict__:
            descriptor = klass.__dict__["playerNumber"]
            break
    assert isinstance(descriptor, property)

def test_player_has_isAI():
    assert hasattr(Player, "isAI")
    descriptor = None
    for klass in Player.__mro__:
        if "isAI" in klass.__dict__:
            descriptor = klass.__dict__["isAI"]
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
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_value():
    assert hasattr(Card, "value")
    descriptor = None
    for klass in Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
    assert "positionInDeck" in params, "Missing parameter 'positionInDeck'"
    assert "cards" in params, "Missing parameter 'cards'"

def test_deck_has_positionInDeck():
    assert hasattr(Deck, "positionInDeck")
    descriptor = None
    for klass in Deck.__mro__:
        if "positionInDeck" in klass.__dict__:
            descriptor = klass.__dict__["positionInDeck"]
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
AI_strategy = st.builds(
    AI,
)
makeNewPlayer_strategy = st.builds(
    makeNewPlayer,
)
Game_strategy = st.builds(
    Game,
    pot=
        st.integers(),
    players=
        safe_text,
    bigBlindValue=
        st.integers(),
    currentDeck=
        st.none(),
    currentCommunityCards=
        st.none(),
    currentBigBlind=
        st.integers()
)
CommunityCards_strategy = st.builds(
    CommunityCards,
    cards=
        safe_text
)
Player_strategy = st.builds(
    Player,
    isAllIn=
        st.booleans(),
    chips=
        st.integers(),
    hand=
        safe_text,
    name=
        safe_text,
    isFolded=
        st.booleans(),
    handValue=
        st.integers(),
    isSmallBlind=
        st.booleans(),
    isBigBlind=
        st.booleans(),
    playerNumber=
        st.integers(),
    isAI=
        st.booleans()
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers(),
    suit=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    positionInDeck=
        st.integers(),
    cards=
        safe_text
)

@given(instance=AI_strategy)
@settings(max_examples=50)
def test_ai_instantiation(instance):
    assert isinstance(instance, AI)

@given(instance=makeNewPlayer_strategy)
@settings(max_examples=50)
def test_makenewplayer_instantiation(instance):
    assert isinstance(instance, makeNewPlayer)

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_pot_setter(instance):
    original = instance.pot
    instance.pot = original
    assert instance.pot == original



@given(instance=Game_strategy)
def test_game_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Game_strategy)
def test_game_bigBlindValue_setter(instance):
    original = instance.bigBlindValue
    instance.bigBlindValue = original
    assert instance.bigBlindValue == original



@given(instance=Game_strategy)
def test_game_currentDeck_setter(instance):
    original = instance.currentDeck
    instance.currentDeck = original
    assert instance.currentDeck == original



@given(instance=Game_strategy)
def test_game_currentCommunityCards_setter(instance):
    original = instance.currentCommunityCards
    instance.currentCommunityCards = original
    assert instance.currentCommunityCards == original



@given(instance=Game_strategy)
def test_game_currentBigBlind_setter(instance):
    original = instance.currentBigBlind
    instance.currentBigBlind = original
    assert instance.currentBigBlind == original

@given(instance=CommunityCards_strategy)
@settings(max_examples=50)
def test_communitycards_instantiation(instance):
    assert isinstance(instance, CommunityCards)



@given(instance=CommunityCards_strategy)
def test_communitycards_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_isAllIn_setter(instance):
    original = instance.isAllIn
    instance.isAllIn = original
    assert instance.isAllIn == original



@given(instance=Player_strategy)
def test_player_chips_setter(instance):
    original = instance.chips
    instance.chips = original
    assert instance.chips == original



@given(instance=Player_strategy)
def test_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_player_isFolded_setter(instance):
    original = instance.isFolded
    instance.isFolded = original
    assert instance.isFolded == original



@given(instance=Player_strategy)
def test_player_handValue_setter(instance):
    original = instance.handValue
    instance.handValue = original
    assert instance.handValue == original



@given(instance=Player_strategy)
def test_player_isSmallBlind_setter(instance):
    original = instance.isSmallBlind
    instance.isSmallBlind = original
    assert instance.isSmallBlind == original



@given(instance=Player_strategy)
def test_player_isBigBlind_setter(instance):
    original = instance.isBigBlind
    instance.isBigBlind = original
    assert instance.isBigBlind == original



@given(instance=Player_strategy)
def test_player_playerNumber_setter(instance):
    original = instance.playerNumber
    instance.playerNumber = original
    assert instance.playerNumber == original



@given(instance=Player_strategy)
def test_player_isAI_setter(instance):
    original = instance.isAI
    instance.isAI = original
    assert instance.isAI == original

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
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_positionInDeck_setter(instance):
    original = instance.positionInDeck
    instance.positionInDeck = original
    assert instance.positionInDeck == original



@given(instance=Deck_strategy)
def test_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original
