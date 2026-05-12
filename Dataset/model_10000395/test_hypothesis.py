import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    PlayerOne_external,
    PlayerTwo_external,
    Function,
    Players,
    Card_Interface,
    Deck,
    WAR,
    en,
    Suit,
    en2,
    Rank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_playerone_external_is_not_abstract():
    assert not inspect.isabstract(PlayerOne_external)


def test_playerone_external_constructor_exists():
    assert callable(PlayerOne_external.__init__)


def test_playerone_external_constructor_args():
    sig = inspect.signature(PlayerOne_external.__init__)
    params = list(sig.parameters.keys())



def test_playertwo_external_is_not_abstract():
    assert not inspect.isabstract(PlayerTwo_external)


def test_playertwo_external_constructor_exists():
    assert callable(PlayerTwo_external.__init__)


def test_playertwo_external_constructor_args():
    sig = inspect.signature(PlayerTwo_external.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())
    assert "Score" in params, "Missing parameter 'Score'"
    assert "removedCard" in params, "Missing parameter 'removedCard'"

def test_function_has_Score():
    assert hasattr(Function, "Score")
    descriptor = None
    for klass in Function.__mro__:
        if "Score" in klass.__dict__:
            descriptor = klass.__dict__["Score"]
            break
    assert isinstance(descriptor, property)

def test_function_has_removedCard():
    assert hasattr(Function, "removedCard")
    descriptor = None
    for klass in Function.__mro__:
        if "removedCard" in klass.__dict__:
            descriptor = klass.__dict__["removedCard"]
            break
    assert isinstance(descriptor, property)



def test_players_is_not_abstract():
    assert not inspect.isabstract(Players)


def test_players_constructor_exists():
    assert callable(Players.__init__)


def test_players_constructor_args():
    sig = inspect.signature(Players.__init__)
    params = list(sig.parameters.keys())
    assert "Player1" in params, "Missing parameter 'Player1'"
    assert "Player2" in params, "Missing parameter 'Player2'"

def test_players_has_Player1():
    assert hasattr(Players, "Player1")
    descriptor = None
    for klass in Players.__mro__:
        if "Player1" in klass.__dict__:
            descriptor = klass.__dict__["Player1"]
            break
    assert isinstance(descriptor, property)

def test_players_has_Player2():
    assert hasattr(Players, "Player2")
    descriptor = None
    for klass in Players.__mro__:
        if "Player2" in klass.__dict__:
            descriptor = klass.__dict__["Player2"]
            break
    assert isinstance(descriptor, property)



def test_card_interface_is_not_abstract():
    assert not inspect.isabstract(Card_Interface)


def test_card_interface_constructor_exists():
    assert callable(Card_Interface.__init__)


def test_card_interface_constructor_args():
    sig = inspect.signature(Card_Interface.__init__)
    params = list(sig.parameters.keys())



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "topcard" in params, "Missing parameter 'topcard'"
    assert "isEmpty__" in params, "Missing parameter 'isEmpty__'"
    assert "draw__" in params, "Missing parameter 'draw__'"
    assert "shuffle__" in params, "Missing parameter 'shuffle__'"
    assert "deck__" in params, "Missing parameter 'deck__'"

def test_deck_has_topcard():
    assert hasattr(Deck, "topcard")
    descriptor = None
    for klass in Deck.__mro__:
        if "topcard" in klass.__dict__:
            descriptor = klass.__dict__["topcard"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_isEmpty__():
    assert hasattr(Deck, "isEmpty__")
    descriptor = None
    for klass in Deck.__mro__:
        if "isEmpty__" in klass.__dict__:
            descriptor = klass.__dict__["isEmpty__"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_draw__():
    assert hasattr(Deck, "draw__")
    descriptor = None
    for klass in Deck.__mro__:
        if "draw__" in klass.__dict__:
            descriptor = klass.__dict__["draw__"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_shuffle__():
    assert hasattr(Deck, "shuffle__")
    descriptor = None
    for klass in Deck.__mro__:
        if "shuffle__" in klass.__dict__:
            descriptor = klass.__dict__["shuffle__"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_deck__():
    assert hasattr(Deck, "deck__")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck__" in klass.__dict__:
            descriptor = klass.__dict__["deck__"]
            break
    assert isinstance(descriptor, property)



def test_war_is_not_abstract():
    assert not inspect.isabstract(WAR)


def test_war_constructor_exists():
    assert callable(WAR.__init__)


def test_war_constructor_args():
    sig = inspect.signature(WAR.__init__)
    params = list(sig.parameters.keys())

def test_en_exists():
    # Check that the Enumeration exists
    assert en is not None

def test_en_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in en]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in en"

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

def test_en2_exists():
    # Check that the Enumeration exists
    assert en2 is not None

def test_en2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in en2]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in en2"

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
PlayerOne_external_strategy = st.builds(
    PlayerOne_external,
)
PlayerTwo_external_strategy = st.builds(
    PlayerTwo_external,
)
Function_strategy = st.builds(
    Function,
    Score=
        st.integers(),
    removedCard=
        st.integers()
)
Players_strategy = st.builds(
    Players,
    Player1=
        st.none(),
    Player2=
        st.none()
)
Card_Interface_strategy = st.builds(
    Card_Interface,
)
Deck_strategy = st.builds(
    Deck,
    topcard=
        st.integers(),
    isEmpty__=
        st.booleans(),
    draw__=
        safe_text,
    shuffle__=
        safe_text,
    deck__=
        st.none()
)
WAR_strategy = st.builds(
    WAR,
)

@given(instance=PlayerOne_external_strategy)
@settings(max_examples=50)
def test_playerone_external_instantiation(instance):
    assert isinstance(instance, PlayerOne_external)

@given(instance=PlayerTwo_external_strategy)
@settings(max_examples=50)
def test_playertwo_external_instantiation(instance):
    assert isinstance(instance, PlayerTwo_external)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=Function_strategy)
def test_function_Score_type(instance):
    assert isinstance(instance.Score, int)


@given(instance=Function_strategy)
def test_function_Score_setter(instance):
    original = instance.Score
    instance.Score = original
    assert instance.Score == original

@given(instance=Function_strategy)
def test_function_removedCard_type(instance):
    assert isinstance(instance.removedCard, int)


@given(instance=Function_strategy)
def test_function_removedCard_setter(instance):
    original = instance.removedCard
    instance.removedCard = original
    assert instance.removedCard == original

@given(instance=Players_strategy)
@settings(max_examples=50)
def test_players_instantiation(instance):
    assert isinstance(instance, Players)

@given(instance=Players_strategy)
def test_players_Player1_type(instance):
    assert isinstance(instance.Player1, card_interface)


@given(instance=Players_strategy)
def test_players_Player1_setter(instance):
    original = instance.Player1
    instance.Player1 = original
    assert instance.Player1 == original

@given(instance=Players_strategy)
def test_players_Player2_type(instance):
    assert isinstance(instance.Player2, card_interface)


@given(instance=Players_strategy)
def test_players_Player2_setter(instance):
    original = instance.Player2
    instance.Player2 = original
    assert instance.Player2 == original

@given(instance=Card_Interface_strategy)
@settings(max_examples=50)
def test_card_interface_instantiation(instance):
    assert isinstance(instance, Card_Interface)

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)

@given(instance=Deck_strategy)
def test_deck_topcard_type(instance):
    assert isinstance(instance.topcard, int)


@given(instance=Deck_strategy)
def test_deck_topcard_setter(instance):
    original = instance.topcard
    instance.topcard = original
    assert instance.topcard == original

@given(instance=Deck_strategy)
def test_deck_isEmpty___type(instance):
    assert isinstance(instance.isEmpty__, bool)


@given(instance=Deck_strategy)
def test_deck_isEmpty___setter(instance):
    original = instance.isEmpty__
    instance.isEmpty__ = original
    assert instance.isEmpty__ == original

@given(instance=Deck_strategy)
def test_deck_draw___type(instance):
    assert isinstance(instance.draw__, str)


@given(instance=Deck_strategy)
def test_deck_draw___setter(instance):
    original = instance.draw__
    instance.draw__ = original
    assert instance.draw__ == original

@given(instance=Deck_strategy)
def test_deck_shuffle___type(instance):
    assert isinstance(instance.shuffle__, str)


@given(instance=Deck_strategy)
def test_deck_shuffle___setter(instance):
    original = instance.shuffle__
    instance.shuffle__ = original
    assert instance.shuffle__ == original

@given(instance=Deck_strategy)
def test_deck_deck___type(instance):
    assert isinstance(instance.deck__, deck)


@given(instance=Deck_strategy)
def test_deck_deck___setter(instance):
    original = instance.deck__
    instance.deck__ = original
    assert instance.deck__ == original

@given(instance=WAR_strategy)
@settings(max_examples=50)
def test_war_instantiation(instance):
    assert isinstance(instance, WAR)
