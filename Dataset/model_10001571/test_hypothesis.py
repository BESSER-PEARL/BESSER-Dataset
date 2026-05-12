import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cards_Deck_Interface,
    Cards_StarndardDeck,
    Cards_Card,
    Cards_Suit,
    Cards_Rank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cards_deck_interface_is_not_abstract():
    assert not inspect.isabstract(Cards_Deck_Interface)


def test_cards_deck_interface_constructor_exists():
    assert callable(Cards_Deck_Interface.__init__)


def test_cards_deck_interface_constructor_args():
    sig = inspect.signature(Cards_Deck_Interface.__init__)
    params = list(sig.parameters.keys())



def test_cards_starndarddeck_is_not_abstract():
    assert not inspect.isabstract(Cards_StarndardDeck)


def test_cards_starndarddeck_constructor_exists():
    assert callable(Cards_StarndardDeck.__init__)


def test_cards_starndarddeck_constructor_args():
    sig = inspect.signature(Cards_StarndardDeck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "rand" in params, "Missing parameter 'rand'"

def test_cards_starndarddeck_has_cards():
    assert hasattr(Cards_StarndardDeck, "cards")
    descriptor = None
    for klass in Cards_StarndardDeck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_cards_starndarddeck_has_rand():
    assert hasattr(Cards_StarndardDeck, "rand")
    descriptor = None
    for klass in Cards_StarndardDeck.__mro__:
        if "rand" in klass.__dict__:
            descriptor = klass.__dict__["rand"]
            break
    assert isinstance(descriptor, property)



def test_cards_card_is_not_abstract():
    assert not inspect.isabstract(Cards_Card)


def test_cards_card_constructor_exists():
    assert callable(Cards_Card.__init__)


def test_cards_card_constructor_args():
    sig = inspect.signature(Cards_Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_cards_card_has_suit():
    assert hasattr(Cards_Card, "suit")
    descriptor = None
    for klass in Cards_Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_cards_card_has_rank():
    assert hasattr(Cards_Card, "rank")
    descriptor = None
    for klass in Cards_Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_cards_suit_exists():
    # Check that the Enumeration exists
    assert Cards_Suit is not None

def test_cards_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cards_Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cards_Suit"

def test_cards_rank_exists():
    # Check that the Enumeration exists
    assert Cards_Rank is not None

def test_cards_rank_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cards_Rank]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cards_Rank"


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
Cards_Deck_Interface_strategy = st.builds(
    Cards_Deck_Interface,
)
Cards_StarndardDeck_strategy = st.builds(
    Cards_StarndardDeck,
    cards=
        st.none(),
    rand=
        safe_text
)
Cards_Card_strategy = st.builds(
    Cards_Card,
    suit=
        st.none(),
    rank=
        st.none()
)

@given(instance=Cards_Deck_Interface_strategy)
@settings(max_examples=50)
def test_cards_deck_interface_instantiation(instance):
    assert isinstance(instance, Cards_Deck_Interface)

@given(instance=Cards_StarndardDeck_strategy)
@settings(max_examples=50)
def test_cards_starndarddeck_instantiation(instance):
    assert isinstance(instance, Cards_StarndardDeck)



@given(instance=Cards_StarndardDeck_strategy)
def test_cards_starndarddeck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Cards_StarndardDeck_strategy)
def test_cards_starndarddeck_rand_setter(instance):
    original = instance.rand
    instance.rand = original
    assert instance.rand == original

@given(instance=Cards_Card_strategy)
@settings(max_examples=50)
def test_cards_card_instantiation(instance):
    assert isinstance(instance, Cards_Card)



@given(instance=Cards_Card_strategy)
def test_cards_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Cards_Card_strategy)
def test_cards_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original
