import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CardDeckInterface,
    Class,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_carddeckinterface_is_not_abstract():
    assert not inspect.isabstract(CardDeckInterface)


def test_carddeckinterface_constructor_exists():
    assert callable(CardDeckInterface.__init__)


def test_carddeckinterface_constructor_args():
    sig = inspect.signature(CardDeckInterface.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "draw" in params, "Missing parameter 'draw'"
    assert "shuffle" in params, "Missing parameter 'shuffle'"

def test_carddeckinterface_has_size():
    assert hasattr(CardDeckInterface, "size")
    descriptor = None
    for klass in CardDeckInterface.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_carddeckinterface_has_draw():
    assert hasattr(CardDeckInterface, "draw")
    descriptor = None
    for klass in CardDeckInterface.__mro__:
        if "draw" in klass.__dict__:
            descriptor = klass.__dict__["draw"]
            break
    assert isinstance(descriptor, property)

def test_carddeckinterface_has_shuffle():
    assert hasattr(CardDeckInterface, "shuffle")
    descriptor = None
    for klass in CardDeckInterface.__mro__:
        if "shuffle" in klass.__dict__:
            descriptor = klass.__dict__["shuffle"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "Ace___14" in params, "Missing parameter 'Ace___14'"
    assert "Queen_12" in params, "Missing parameter 'Queen_12'"
    assert "Hearts" in params, "Missing parameter 'Hearts'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "Spades" in params, "Missing parameter 'Spades'"
    assert "Jack_11" in params, "Missing parameter 'Jack_11'"
    assert "Clubs" in params, "Missing parameter 'Clubs'"
    assert "King_13" in params, "Missing parameter 'King_13'"
    assert "Diamonds" in params, "Missing parameter 'Diamonds'"
    assert "face" in params, "Missing parameter 'face'"

def test_card_has_Ace___14():
    assert hasattr(Card, "Ace___14")
    descriptor = None
    for klass in Card.__mro__:
        if "Ace___14" in klass.__dict__:
            descriptor = klass.__dict__["Ace___14"]
            break
    assert isinstance(descriptor, property)

def test_card_has_Queen_12():
    assert hasattr(Card, "Queen_12")
    descriptor = None
    for klass in Card.__mro__:
        if "Queen_12" in klass.__dict__:
            descriptor = klass.__dict__["Queen_12"]
            break
    assert isinstance(descriptor, property)

def test_card_has_Hearts():
    assert hasattr(Card, "Hearts")
    descriptor = None
    for klass in Card.__mro__:
        if "Hearts" in klass.__dict__:
            descriptor = klass.__dict__["Hearts"]
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

def test_card_has_Spades():
    assert hasattr(Card, "Spades")
    descriptor = None
    for klass in Card.__mro__:
        if "Spades" in klass.__dict__:
            descriptor = klass.__dict__["Spades"]
            break
    assert isinstance(descriptor, property)

def test_card_has_Jack_11():
    assert hasattr(Card, "Jack_11")
    descriptor = None
    for klass in Card.__mro__:
        if "Jack_11" in klass.__dict__:
            descriptor = klass.__dict__["Jack_11"]
            break
    assert isinstance(descriptor, property)

def test_card_has_Clubs():
    assert hasattr(Card, "Clubs")
    descriptor = None
    for klass in Card.__mro__:
        if "Clubs" in klass.__dict__:
            descriptor = klass.__dict__["Clubs"]
            break
    assert isinstance(descriptor, property)

def test_card_has_King_13():
    assert hasattr(Card, "King_13")
    descriptor = None
    for klass in Card.__mro__:
        if "King_13" in klass.__dict__:
            descriptor = klass.__dict__["King_13"]
            break
    assert isinstance(descriptor, property)

def test_card_has_Diamonds():
    assert hasattr(Card, "Diamonds")
    descriptor = None
    for klass in Card.__mro__:
        if "Diamonds" in klass.__dict__:
            descriptor = klass.__dict__["Diamonds"]
            break
    assert isinstance(descriptor, property)

def test_card_has_face():
    assert hasattr(Card, "face")
    descriptor = None
    for klass in Card.__mro__:
        if "face" in klass.__dict__:
            descriptor = klass.__dict__["face"]
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
CardDeckInterface_strategy = st.builds(
    CardDeckInterface,
    size=
        st.integers(),
    draw=
        st.none(),
    shuffle=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
Card_strategy = st.builds(
    Card,
    Ace___14=
        st.integers(),
    Queen_12=
        st.integers(),
    Hearts=
        safe_text,
    suit=
        safe_text,
    Spades=
        safe_text,
    Jack_11=
        st.integers(),
    Clubs=
        safe_text,
    King_13=
        st.integers(),
    Diamonds=
        safe_text,
    face=
        st.integers()
)

@given(instance=CardDeckInterface_strategy)
@settings(max_examples=50)
def test_carddeckinterface_instantiation(instance):
    assert isinstance(instance, CardDeckInterface)



@given(instance=CardDeckInterface_strategy)
def test_carddeckinterface_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=CardDeckInterface_strategy)
def test_carddeckinterface_draw_setter(instance):
    original = instance.draw
    instance.draw = original
    assert instance.draw == original



@given(instance=CardDeckInterface_strategy)
def test_carddeckinterface_shuffle_setter(instance):
    original = instance.shuffle
    instance.shuffle = original
    assert instance.shuffle == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_Ace___14_setter(instance):
    original = instance.Ace___14
    instance.Ace___14 = original
    assert instance.Ace___14 == original



@given(instance=Card_strategy)
def test_card_Queen_12_setter(instance):
    original = instance.Queen_12
    instance.Queen_12 = original
    assert instance.Queen_12 == original



@given(instance=Card_strategy)
def test_card_Hearts_setter(instance):
    original = instance.Hearts
    instance.Hearts = original
    assert instance.Hearts == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_card_Spades_setter(instance):
    original = instance.Spades
    instance.Spades = original
    assert instance.Spades == original



@given(instance=Card_strategy)
def test_card_Jack_11_setter(instance):
    original = instance.Jack_11
    instance.Jack_11 = original
    assert instance.Jack_11 == original



@given(instance=Card_strategy)
def test_card_Clubs_setter(instance):
    original = instance.Clubs
    instance.Clubs = original
    assert instance.Clubs == original



@given(instance=Card_strategy)
def test_card_King_13_setter(instance):
    original = instance.King_13
    instance.King_13 = original
    assert instance.King_13 == original



@given(instance=Card_strategy)
def test_card_Diamonds_setter(instance):
    original = instance.Diamonds
    instance.Diamonds = original
    assert instance.Diamonds == original



@given(instance=Card_strategy)
def test_card_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original
