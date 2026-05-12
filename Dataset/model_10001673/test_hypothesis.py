import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Rules,
    Game,
    Player,
    Card,
    Deck,
    Face1,
    Face,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rules_is_not_abstract():
    assert not inspect.isabstract(Rules)


def test_rules_constructor_exists():
    assert callable(Rules.__init__)


def test_rules_constructor_args():
    sig = inspect.signature(Rules.__init__)
    params = list(sig.parameters.keys())
    assert "card2" in params, "Missing parameter 'card2'"
    assert "card1" in params, "Missing parameter 'card1'"
    assert "card3" in params, "Missing parameter 'card3'"

def test_rules_has_card2():
    assert hasattr(Rules, "card2")
    descriptor = None
    for klass in Rules.__mro__:
        if "card2" in klass.__dict__:
            descriptor = klass.__dict__["card2"]
            break
    assert isinstance(descriptor, property)

def test_rules_has_card1():
    assert hasattr(Rules, "card1")
    descriptor = None
    for klass in Rules.__mro__:
        if "card1" in klass.__dict__:
            descriptor = klass.__dict__["card1"]
            break
    assert isinstance(descriptor, property)

def test_rules_has_card3():
    assert hasattr(Rules, "card3")
    descriptor = None
    for klass in Rules.__mro__:
        if "card3" in klass.__dict__:
            descriptor = klass.__dict__["card3"]
            break
    assert isinstance(descriptor, property)



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "numLose" in params, "Missing parameter 'numLose'"
    assert "numWins" in params, "Missing parameter 'numWins'"
    assert "numGames" in params, "Missing parameter 'numGames'"

def test_game_has_numLose():
    assert hasattr(Game, "numLose")
    descriptor = None
    for klass in Game.__mro__:
        if "numLose" in klass.__dict__:
            descriptor = klass.__dict__["numLose"]
            break
    assert isinstance(descriptor, property)

def test_game_has_numWins():
    assert hasattr(Game, "numWins")
    descriptor = None
    for klass in Game.__mro__:
        if "numWins" in klass.__dict__:
            descriptor = klass.__dict__["numWins"]
            break
    assert isinstance(descriptor, property)

def test_game_has_numGames():
    assert hasattr(Game, "numGames")
    descriptor = None
    for klass in Game.__mro__:
        if "numGames" in klass.__dict__:
            descriptor = klass.__dict__["numGames"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "numMoves" in params, "Missing parameter 'numMoves'"

def test_player_has_numMoves():
    assert hasattr(Player, "numMoves")
    descriptor = None
    for klass in Player.__mro__:
        if "numMoves" in klass.__dict__:
            descriptor = klass.__dict__["numMoves"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "Enum" in params, "Missing parameter 'Enum'"

def test_card_has_Enum():
    assert hasattr(Card, "Enum")
    descriptor = None
    for klass in Card.__mro__:
        if "Enum" in klass.__dict__:
            descriptor = klass.__dict__["Enum"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "numCards" in params, "Missing parameter 'numCards'"

def test_deck_has_numCards():
    assert hasattr(Deck, "numCards")
    descriptor = None
    for klass in Deck.__mro__:
        if "numCards" in klass.__dict__:
            descriptor = klass.__dict__["numCards"]
            break
    assert isinstance(descriptor, property)

def test_face1_exists():
    # Check that the Enumeration exists
    assert Face1 is not None

def test_face1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Face1]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Face1"

def test_face_exists():
    # Check that the Enumeration exists
    assert Face is not None

def test_face_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Face]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Face"


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
Rules_strategy = st.builds(
    Rules,
    card2=
        st.none(),
    card1=
        st.none(),
    card3=
        st.none()
)
Game_strategy = st.builds(
    Game,
    numLose=
        st.integers(),
    numWins=
        st.integers(),
    numGames=
        st.integers()
)
Player_strategy = st.builds(
    Player,
    numMoves=
        st.integers()
)
Card_strategy = st.builds(
    Card,
    Enum=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    numCards=
        st.integers()
)

@given(instance=Rules_strategy)
@settings(max_examples=50)
def test_rules_instantiation(instance):
    assert isinstance(instance, Rules)



@given(instance=Rules_strategy)
def test_rules_card2_setter(instance):
    original = instance.card2
    instance.card2 = original
    assert instance.card2 == original



@given(instance=Rules_strategy)
def test_rules_card1_setter(instance):
    original = instance.card1
    instance.card1 = original
    assert instance.card1 == original



@given(instance=Rules_strategy)
def test_rules_card3_setter(instance):
    original = instance.card3
    instance.card3 = original
    assert instance.card3 == original

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_numLose_setter(instance):
    original = instance.numLose
    instance.numLose = original
    assert instance.numLose == original



@given(instance=Game_strategy)
def test_game_numWins_setter(instance):
    original = instance.numWins
    instance.numWins = original
    assert instance.numWins == original



@given(instance=Game_strategy)
def test_game_numGames_setter(instance):
    original = instance.numGames
    instance.numGames = original
    assert instance.numGames == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_numMoves_setter(instance):
    original = instance.numMoves
    instance.numMoves = original
    assert instance.numMoves == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_Enum_setter(instance):
    original = instance.Enum
    instance.Enum = original
    assert instance.Enum == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_numCards_setter(instance):
    original = instance.numCards
    instance.numCards = original
    assert instance.numCards == original
