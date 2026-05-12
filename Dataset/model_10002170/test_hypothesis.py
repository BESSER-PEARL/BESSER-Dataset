import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Application,
    Card,
    Deck,
    Show_Top_Results_UseCase,
    Play_Multiple_Times_UseCase,
    Play_Once_UseCase,
    Play_for_Me_UseCase,
    Amalgamate_UseCase,
    Current_over_two_UseCase,
    Current_onto_Previous_UseCase,
    Make_Move_UseCase,
    Deal_a_Card_UseCase,
    Show_Deck_UseCase,
    Shuffle_Deck_UseCase,
    User_Actor,
    Suit,
    CardValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_application_is_not_abstract():
    assert not inspect.isabstract(Application)


def test_application_constructor_exists():
    assert callable(Application.__init__)


def test_application_constructor_args():
    sig = inspect.signature(Application.__init__)
    params = list(sig.parameters.keys())
    assert "scan" in params, "Missing parameter 'scan'"
    assert "deck" in params, "Missing parameter 'deck'"

def test_application_has_scan():
    assert hasattr(Application, "scan")
    descriptor = None
    for klass in Application.__mro__:
        if "scan" in klass.__dict__:
            descriptor = klass.__dict__["scan"]
            break
    assert isinstance(descriptor, property)

def test_application_has_deck():
    assert hasattr(Application, "deck")
    descriptor = None
    for klass in Application.__mro__:
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
    assert "cardValue" in params, "Missing parameter 'cardValue'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_cardValue():
    assert hasattr(Card, "cardValue")
    descriptor = None
    for klass in Card.__mro__:
        if "cardValue" in klass.__dict__:
            descriptor = klass.__dict__["cardValue"]
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
    assert "_cards__" in params, "Missing parameter '_cards__'"
    assert "scan" in params, "Missing parameter 'scan'"

def test_deck_has__cards__():
    assert hasattr(Deck, "_cards__")
    descriptor = None
    for klass in Deck.__mro__:
        if "_cards__" in klass.__dict__:
            descriptor = klass.__dict__["_cards__"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_scan():
    assert hasattr(Deck, "scan")
    descriptor = None
    for klass in Deck.__mro__:
        if "scan" in klass.__dict__:
            descriptor = klass.__dict__["scan"]
            break
    assert isinstance(descriptor, property)



def test_show_top_results_usecase_is_not_abstract():
    assert not inspect.isabstract(Show_Top_Results_UseCase)


def test_show_top_results_usecase_constructor_exists():
    assert callable(Show_Top_Results_UseCase.__init__)


def test_show_top_results_usecase_constructor_args():
    sig = inspect.signature(Show_Top_Results_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_play_multiple_times_usecase_is_not_abstract():
    assert not inspect.isabstract(Play_Multiple_Times_UseCase)


def test_play_multiple_times_usecase_constructor_exists():
    assert callable(Play_Multiple_Times_UseCase.__init__)


def test_play_multiple_times_usecase_constructor_args():
    sig = inspect.signature(Play_Multiple_Times_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_play_once_usecase_is_not_abstract():
    assert not inspect.isabstract(Play_Once_UseCase)


def test_play_once_usecase_constructor_exists():
    assert callable(Play_Once_UseCase.__init__)


def test_play_once_usecase_constructor_args():
    sig = inspect.signature(Play_Once_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_play_for_me_usecase_is_not_abstract():
    assert not inspect.isabstract(Play_for_Me_UseCase)


def test_play_for_me_usecase_constructor_exists():
    assert callable(Play_for_Me_UseCase.__init__)


def test_play_for_me_usecase_constructor_args():
    sig = inspect.signature(Play_for_Me_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_amalgamate_usecase_is_not_abstract():
    assert not inspect.isabstract(Amalgamate_UseCase)


def test_amalgamate_usecase_constructor_exists():
    assert callable(Amalgamate_UseCase.__init__)


def test_amalgamate_usecase_constructor_args():
    sig = inspect.signature(Amalgamate_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_current_over_two_usecase_is_not_abstract():
    assert not inspect.isabstract(Current_over_two_UseCase)


def test_current_over_two_usecase_constructor_exists():
    assert callable(Current_over_two_UseCase.__init__)


def test_current_over_two_usecase_constructor_args():
    sig = inspect.signature(Current_over_two_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_current_onto_previous_usecase_is_not_abstract():
    assert not inspect.isabstract(Current_onto_Previous_UseCase)


def test_current_onto_previous_usecase_constructor_exists():
    assert callable(Current_onto_Previous_UseCase.__init__)


def test_current_onto_previous_usecase_constructor_args():
    sig = inspect.signature(Current_onto_Previous_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_make_move_usecase_is_not_abstract():
    assert not inspect.isabstract(Make_Move_UseCase)


def test_make_move_usecase_constructor_exists():
    assert callable(Make_Move_UseCase.__init__)


def test_make_move_usecase_constructor_args():
    sig = inspect.signature(Make_Move_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_deal_a_card_usecase_is_not_abstract():
    assert not inspect.isabstract(Deal_a_Card_UseCase)


def test_deal_a_card_usecase_constructor_exists():
    assert callable(Deal_a_Card_UseCase.__init__)


def test_deal_a_card_usecase_constructor_args():
    sig = inspect.signature(Deal_a_Card_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_show_deck_usecase_is_not_abstract():
    assert not inspect.isabstract(Show_Deck_UseCase)


def test_show_deck_usecase_constructor_exists():
    assert callable(Show_Deck_UseCase.__init__)


def test_show_deck_usecase_constructor_args():
    sig = inspect.signature(Show_Deck_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_shuffle_deck_usecase_is_not_abstract():
    assert not inspect.isabstract(Shuffle_Deck_UseCase)


def test_shuffle_deck_usecase_constructor_exists():
    assert callable(Shuffle_Deck_UseCase.__init__)


def test_shuffle_deck_usecase_constructor_args():
    sig = inspect.signature(Shuffle_Deck_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
    params = list(sig.parameters.keys())

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

def test_cardvalue_exists():
    # Check that the Enumeration exists
    assert CardValue is not None

def test_cardvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardValue]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardValue"


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
Application_strategy = st.builds(
    Application,
    scan=
        safe_text,
    deck=
        st.none()
)
Card_strategy = st.builds(
    Card,
    cardValue=
        st.none(),
    suit=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    _cards__=
        st.none(),
    scan=
        safe_text
)
Show_Top_Results_UseCase_strategy = st.builds(
    Show_Top_Results_UseCase,
)
Play_Multiple_Times_UseCase_strategy = st.builds(
    Play_Multiple_Times_UseCase,
)
Play_Once_UseCase_strategy = st.builds(
    Play_Once_UseCase,
)
Play_for_Me_UseCase_strategy = st.builds(
    Play_for_Me_UseCase,
)
Amalgamate_UseCase_strategy = st.builds(
    Amalgamate_UseCase,
)
Current_over_two_UseCase_strategy = st.builds(
    Current_over_two_UseCase,
)
Current_onto_Previous_UseCase_strategy = st.builds(
    Current_onto_Previous_UseCase,
)
Make_Move_UseCase_strategy = st.builds(
    Make_Move_UseCase,
)
Deal_a_Card_UseCase_strategy = st.builds(
    Deal_a_Card_UseCase,
)
Show_Deck_UseCase_strategy = st.builds(
    Show_Deck_UseCase,
)
Shuffle_Deck_UseCase_strategy = st.builds(
    Shuffle_Deck_UseCase,
)
User_Actor_strategy = st.builds(
    User_Actor,
)

@given(instance=Application_strategy)
@settings(max_examples=50)
def test_application_instantiation(instance):
    assert isinstance(instance, Application)



@given(instance=Application_strategy)
def test_application_scan_setter(instance):
    original = instance.scan
    instance.scan = original
    assert instance.scan == original



@given(instance=Application_strategy)
def test_application_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_cardValue_setter(instance):
    original = instance.cardValue
    instance.cardValue = original
    assert instance.cardValue == original



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
def test_deck__cards___setter(instance):
    original = instance._cards__
    instance._cards__ = original
    assert instance._cards__ == original



@given(instance=Deck_strategy)
def test_deck_scan_setter(instance):
    original = instance.scan
    instance.scan = original
    assert instance.scan == original

@given(instance=Show_Top_Results_UseCase_strategy)
@settings(max_examples=50)
def test_show_top_results_usecase_instantiation(instance):
    assert isinstance(instance, Show_Top_Results_UseCase)

@given(instance=Play_Multiple_Times_UseCase_strategy)
@settings(max_examples=50)
def test_play_multiple_times_usecase_instantiation(instance):
    assert isinstance(instance, Play_Multiple_Times_UseCase)

@given(instance=Play_Once_UseCase_strategy)
@settings(max_examples=50)
def test_play_once_usecase_instantiation(instance):
    assert isinstance(instance, Play_Once_UseCase)

@given(instance=Play_for_Me_UseCase_strategy)
@settings(max_examples=50)
def test_play_for_me_usecase_instantiation(instance):
    assert isinstance(instance, Play_for_Me_UseCase)

@given(instance=Amalgamate_UseCase_strategy)
@settings(max_examples=50)
def test_amalgamate_usecase_instantiation(instance):
    assert isinstance(instance, Amalgamate_UseCase)

@given(instance=Current_over_two_UseCase_strategy)
@settings(max_examples=50)
def test_current_over_two_usecase_instantiation(instance):
    assert isinstance(instance, Current_over_two_UseCase)

@given(instance=Current_onto_Previous_UseCase_strategy)
@settings(max_examples=50)
def test_current_onto_previous_usecase_instantiation(instance):
    assert isinstance(instance, Current_onto_Previous_UseCase)

@given(instance=Make_Move_UseCase_strategy)
@settings(max_examples=50)
def test_make_move_usecase_instantiation(instance):
    assert isinstance(instance, Make_Move_UseCase)

@given(instance=Deal_a_Card_UseCase_strategy)
@settings(max_examples=50)
def test_deal_a_card_usecase_instantiation(instance):
    assert isinstance(instance, Deal_a_Card_UseCase)

@given(instance=Show_Deck_UseCase_strategy)
@settings(max_examples=50)
def test_show_deck_usecase_instantiation(instance):
    assert isinstance(instance, Show_Deck_UseCase)

@given(instance=Shuffle_Deck_UseCase_strategy)
@settings(max_examples=50)
def test_shuffle_deck_usecase_instantiation(instance):
    assert isinstance(instance, Shuffle_Deck_UseCase)

@given(instance=User_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, User_Actor)
