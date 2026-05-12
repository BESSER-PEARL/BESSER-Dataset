import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Iterable_Card__Interface,
    Comparable_BlackjackHand__Interface,
    genmymodelreverse_android_support_v7_app_AppCompatActivity,
    genmymodelreverse_C12,
    genmymodelreverse_java_lang_Iterable_Interface,
    genmymodelreverse_C11,
    genmymodelreverse_java_util_Iterator_Interface,
    genmymodelreverse_C1,
    genmymodelreverse_java_lang_Comparable_Interface,
    blackjack_ExampleUnitTest,
    blackjack_MainActivity,
    blackjack_Deck,
    blackjack_DealerBot,
    blackjack_CardSet,
    blackjack_Card,
    blackjack_BlackjackHand,
    blackjack_DeckShuffledListener_Interface,
    blackjack_BlackjackGame,
    blackjack_ExampleInstrumentedTest,
    blackjack_Suit,
    blackjack_Value,
    blackjack_GameState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iterable_card__interface_is_not_abstract():
    assert not inspect.isabstract(Iterable_Card__Interface)


def test_iterable_card__interface_constructor_exists():
    assert callable(Iterable_Card__Interface.__init__)


def test_iterable_card__interface_constructor_args():
    sig = inspect.signature(Iterable_Card__Interface.__init__)
    params = list(sig.parameters.keys())



def test_comparable_blackjackhand__interface_is_not_abstract():
    assert not inspect.isabstract(Comparable_BlackjackHand__Interface)


def test_comparable_blackjackhand__interface_constructor_exists():
    assert callable(Comparable_BlackjackHand__Interface.__init__)


def test_comparable_blackjackhand__interface_constructor_args():
    sig = inspect.signature(Comparable_BlackjackHand__Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_android_support_v7_app_appcompatactivity_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_android_support_v7_app_AppCompatActivity)


def test_genmymodelreverse_android_support_v7_app_appcompatactivity_constructor_exists():
    assert callable(genmymodelreverse_android_support_v7_app_AppCompatActivity.__init__)


def test_genmymodelreverse_android_support_v7_app_appcompatactivity_constructor_args():
    sig = inspect.signature(genmymodelreverse_android_support_v7_app_AppCompatActivity.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c12_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C12)


def test_genmymodelreverse_c12_constructor_exists():
    assert callable(genmymodelreverse_C12.__init__)


def test_genmymodelreverse_c12_constructor_args():
    sig = inspect.signature(genmymodelreverse_C12.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_lang_iterable_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Iterable_Interface)


def test_genmymodelreverse_java_lang_iterable_interface_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Iterable_Interface.__init__)


def test_genmymodelreverse_java_lang_iterable_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Iterable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c11_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C11)


def test_genmymodelreverse_c11_constructor_exists():
    assert callable(genmymodelreverse_C11.__init__)


def test_genmymodelreverse_c11_constructor_args():
    sig = inspect.signature(genmymodelreverse_C11.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_util_iterator_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_Iterator_Interface)


def test_genmymodelreverse_java_util_iterator_interface_constructor_exists():
    assert callable(genmymodelreverse_java_util_Iterator_Interface.__init__)


def test_genmymodelreverse_java_util_iterator_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_Iterator_Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c1_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C1)


def test_genmymodelreverse_c1_constructor_exists():
    assert callable(genmymodelreverse_C1.__init__)


def test_genmymodelreverse_c1_constructor_args():
    sig = inspect.signature(genmymodelreverse_C1.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_lang_comparable_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Comparable_Interface)


def test_genmymodelreverse_java_lang_comparable_interface_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Comparable_Interface.__init__)


def test_genmymodelreverse_java_lang_comparable_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Comparable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_exampleunittest_is_not_abstract():
    assert not inspect.isabstract(blackjack_ExampleUnitTest)


def test_blackjack_exampleunittest_constructor_exists():
    assert callable(blackjack_ExampleUnitTest.__init__)


def test_blackjack_exampleunittest_constructor_args():
    sig = inspect.signature(blackjack_ExampleUnitTest.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_mainactivity_is_not_abstract():
    assert not inspect.isabstract(blackjack_MainActivity)


def test_blackjack_mainactivity_constructor_exists():
    assert callable(blackjack_MainActivity.__init__)


def test_blackjack_mainactivity_constructor_args():
    sig = inspect.signature(blackjack_MainActivity.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_deck_is_not_abstract():
    assert not inspect.isabstract(blackjack_Deck)


def test_blackjack_deck_constructor_exists():
    assert callable(blackjack_Deck.__init__)


def test_blackjack_deck_constructor_args():
    sig = inspect.signature(blackjack_Deck.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_dealerbot_is_not_abstract():
    assert not inspect.isabstract(blackjack_DealerBot)


def test_blackjack_dealerbot_constructor_exists():
    assert callable(blackjack_DealerBot.__init__)


def test_blackjack_dealerbot_constructor_args():
    sig = inspect.signature(blackjack_DealerBot.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_cardset_is_not_abstract():
    assert not inspect.isabstract(blackjack_CardSet)


def test_blackjack_cardset_constructor_exists():
    assert callable(blackjack_CardSet.__init__)


def test_blackjack_cardset_constructor_args():
    sig = inspect.signature(blackjack_CardSet.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_card_is_not_abstract():
    assert not inspect.isabstract(blackjack_Card)


def test_blackjack_card_constructor_exists():
    assert callable(blackjack_Card.__init__)


def test_blackjack_card_constructor_args():
    sig = inspect.signature(blackjack_Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "MAX_VALUE_OF_ACE" in params, "Missing parameter 'MAX_VALUE_OF_ACE'"
    assert "BLACKJACK_VALUE" in params, "Missing parameter 'BLACKJACK_VALUE'"
    assert "value" in params, "Missing parameter 'value'"

def test_blackjack_card_has_suit():
    assert hasattr(blackjack_Card, "suit")
    descriptor = None
    for klass in blackjack_Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_card_has_MAX_VALUE_OF_ACE():
    assert hasattr(blackjack_Card, "MAX_VALUE_OF_ACE")
    descriptor = None
    for klass in blackjack_Card.__mro__:
        if "MAX_VALUE_OF_ACE" in klass.__dict__:
            descriptor = klass.__dict__["MAX_VALUE_OF_ACE"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_card_has_BLACKJACK_VALUE():
    assert hasattr(blackjack_Card, "BLACKJACK_VALUE")
    descriptor = None
    for klass in blackjack_Card.__mro__:
        if "BLACKJACK_VALUE" in klass.__dict__:
            descriptor = klass.__dict__["BLACKJACK_VALUE"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_card_has_value():
    assert hasattr(blackjack_Card, "value")
    descriptor = None
    for klass in blackjack_Card.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_blackjackhand_is_not_abstract():
    assert not inspect.isabstract(blackjack_BlackjackHand)


def test_blackjack_blackjackhand_constructor_exists():
    assert callable(blackjack_BlackjackHand.__init__)


def test_blackjack_blackjackhand_constructor_args():
    sig = inspect.signature(blackjack_BlackjackHand.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_deckshuffledlistener_interface_is_not_abstract():
    assert not inspect.isabstract(blackjack_DeckShuffledListener_Interface)


def test_blackjack_deckshuffledlistener_interface_constructor_exists():
    assert callable(blackjack_DeckShuffledListener_Interface.__init__)


def test_blackjack_deckshuffledlistener_interface_constructor_args():
    sig = inspect.signature(blackjack_DeckShuffledListener_Interface.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_blackjackgame_is_not_abstract():
    assert not inspect.isabstract(blackjack_BlackjackGame)


def test_blackjack_blackjackgame_constructor_exists():
    assert callable(blackjack_BlackjackGame.__init__)


def test_blackjack_blackjackgame_constructor_args():
    sig = inspect.signature(blackjack_BlackjackGame.__init__)
    params = list(sig.parameters.keys())
    assert "gameResultTextView" in params, "Missing parameter 'gameResultTextView'"
    assert "hitButton" in params, "Missing parameter 'hitButton'"
    assert "MAX_CARDS_PULLED" in params, "Missing parameter 'MAX_CARDS_PULLED'"
    assert "MAX_HITS" in params, "Missing parameter 'MAX_HITS'"
    assert "dealersHandValueTextView" in params, "Missing parameter 'dealersHandValueTextView'"
    assert "playersHandTextView" in params, "Missing parameter 'playersHandTextView'"
    assert "playerHandValueTextView" in params, "Missing parameter 'playerHandValueTextView'"
    assert "stayButton" in params, "Missing parameter 'stayButton'"
    assert "dealersHandTextView" in params, "Missing parameter 'dealersHandTextView'"
    assert "gstate" in params, "Missing parameter 'gstate'"

def test_blackjack_blackjackgame_has_gameResultTextView():
    assert hasattr(blackjack_BlackjackGame, "gameResultTextView")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "gameResultTextView" in klass.__dict__:
            descriptor = klass.__dict__["gameResultTextView"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_hitButton():
    assert hasattr(blackjack_BlackjackGame, "hitButton")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "hitButton" in klass.__dict__:
            descriptor = klass.__dict__["hitButton"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_MAX_CARDS_PULLED():
    assert hasattr(blackjack_BlackjackGame, "MAX_CARDS_PULLED")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "MAX_CARDS_PULLED" in klass.__dict__:
            descriptor = klass.__dict__["MAX_CARDS_PULLED"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_MAX_HITS():
    assert hasattr(blackjack_BlackjackGame, "MAX_HITS")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "MAX_HITS" in klass.__dict__:
            descriptor = klass.__dict__["MAX_HITS"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_dealersHandValueTextView():
    assert hasattr(blackjack_BlackjackGame, "dealersHandValueTextView")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "dealersHandValueTextView" in klass.__dict__:
            descriptor = klass.__dict__["dealersHandValueTextView"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_playersHandTextView():
    assert hasattr(blackjack_BlackjackGame, "playersHandTextView")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "playersHandTextView" in klass.__dict__:
            descriptor = klass.__dict__["playersHandTextView"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_playerHandValueTextView():
    assert hasattr(blackjack_BlackjackGame, "playerHandValueTextView")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "playerHandValueTextView" in klass.__dict__:
            descriptor = klass.__dict__["playerHandValueTextView"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_stayButton():
    assert hasattr(blackjack_BlackjackGame, "stayButton")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "stayButton" in klass.__dict__:
            descriptor = klass.__dict__["stayButton"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_dealersHandTextView():
    assert hasattr(blackjack_BlackjackGame, "dealersHandTextView")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "dealersHandTextView" in klass.__dict__:
            descriptor = klass.__dict__["dealersHandTextView"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_blackjackgame_has_gstate():
    assert hasattr(blackjack_BlackjackGame, "gstate")
    descriptor = None
    for klass in blackjack_BlackjackGame.__mro__:
        if "gstate" in klass.__dict__:
            descriptor = klass.__dict__["gstate"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_exampleinstrumentedtest_is_not_abstract():
    assert not inspect.isabstract(blackjack_ExampleInstrumentedTest)


def test_blackjack_exampleinstrumentedtest_constructor_exists():
    assert callable(blackjack_ExampleInstrumentedTest.__init__)


def test_blackjack_exampleinstrumentedtest_constructor_args():
    sig = inspect.signature(blackjack_ExampleInstrumentedTest.__init__)
    params = list(sig.parameters.keys())

def test_blackjack_suit_exists():
    # Check that the Enumeration exists
    assert blackjack_Suit is not None

def test_blackjack_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in blackjack_Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in blackjack_Suit"

def test_blackjack_value_exists():
    # Check that the Enumeration exists
    assert blackjack_Value is not None

def test_blackjack_value_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in blackjack_Value]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in blackjack_Value"

def test_blackjack_gamestate_exists():
    # Check that the Enumeration exists
    assert blackjack_GameState is not None

def test_blackjack_gamestate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in blackjack_GameState]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in blackjack_GameState"


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
Iterable_Card__Interface_strategy = st.builds(
    Iterable_Card__Interface,
)
Comparable_BlackjackHand__Interface_strategy = st.builds(
    Comparable_BlackjackHand__Interface,
)
genmymodelreverse_android_support_v7_app_AppCompatActivity_strategy = st.builds(
    genmymodelreverse_android_support_v7_app_AppCompatActivity,
)
genmymodelreverse_C12_strategy = st.builds(
    genmymodelreverse_C12,
)
genmymodelreverse_java_lang_Iterable_Interface_strategy = st.builds(
    genmymodelreverse_java_lang_Iterable_Interface,
)
genmymodelreverse_C11_strategy = st.builds(
    genmymodelreverse_C11,
)
genmymodelreverse_java_util_Iterator_Interface_strategy = st.builds(
    genmymodelreverse_java_util_Iterator_Interface,
)
genmymodelreverse_C1_strategy = st.builds(
    genmymodelreverse_C1,
)
genmymodelreverse_java_lang_Comparable_Interface_strategy = st.builds(
    genmymodelreverse_java_lang_Comparable_Interface,
)
blackjack_ExampleUnitTest_strategy = st.builds(
    blackjack_ExampleUnitTest,
)
blackjack_MainActivity_strategy = st.builds(
    blackjack_MainActivity,
)
blackjack_Deck_strategy = st.builds(
    blackjack_Deck,
)
blackjack_DealerBot_strategy = st.builds(
    blackjack_DealerBot,
)
blackjack_CardSet_strategy = st.builds(
    blackjack_CardSet,
)
blackjack_Card_strategy = st.builds(
    blackjack_Card,
    suit=
        st.none(),
    MAX_VALUE_OF_ACE=
        st.integers(),
    BLACKJACK_VALUE=
        st.integers(),
    value=
        st.none()
)
blackjack_BlackjackHand_strategy = st.builds(
    blackjack_BlackjackHand,
)
blackjack_DeckShuffledListener_Interface_strategy = st.builds(
    blackjack_DeckShuffledListener_Interface,
)
blackjack_BlackjackGame_strategy = st.builds(
    blackjack_BlackjackGame,
    gameResultTextView=
        safe_text,
    hitButton=
        safe_text,
    MAX_CARDS_PULLED=
        st.integers(),
    MAX_HITS=
        st.integers(),
    dealersHandValueTextView=
        safe_text,
    playersHandTextView=
        safe_text,
    playerHandValueTextView=
        safe_text,
    stayButton=
        safe_text,
    dealersHandTextView=
        safe_text,
    gstate=
        st.none()
)
blackjack_ExampleInstrumentedTest_strategy = st.builds(
    blackjack_ExampleInstrumentedTest,
)

@given(instance=Iterable_Card__Interface_strategy)
@settings(max_examples=50)
def test_iterable_card__interface_instantiation(instance):
    assert isinstance(instance, Iterable_Card__Interface)

@given(instance=Comparable_BlackjackHand__Interface_strategy)
@settings(max_examples=50)
def test_comparable_blackjackhand__interface_instantiation(instance):
    assert isinstance(instance, Comparable_BlackjackHand__Interface)

@given(instance=genmymodelreverse_android_support_v7_app_AppCompatActivity_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_android_support_v7_app_appcompatactivity_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_android_support_v7_app_AppCompatActivity)

@given(instance=genmymodelreverse_C12_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c12_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C12)

@given(instance=genmymodelreverse_java_lang_Iterable_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_lang_iterable_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Iterable_Interface)

@given(instance=genmymodelreverse_C11_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c11_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C11)

@given(instance=genmymodelreverse_java_util_Iterator_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_util_iterator_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Iterator_Interface)

@given(instance=genmymodelreverse_C1_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c1_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C1)

@given(instance=genmymodelreverse_java_lang_Comparable_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_lang_comparable_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Comparable_Interface)

@given(instance=blackjack_ExampleUnitTest_strategy)
@settings(max_examples=50)
def test_blackjack_exampleunittest_instantiation(instance):
    assert isinstance(instance, blackjack_ExampleUnitTest)

@given(instance=blackjack_MainActivity_strategy)
@settings(max_examples=50)
def test_blackjack_mainactivity_instantiation(instance):
    assert isinstance(instance, blackjack_MainActivity)

@given(instance=blackjack_Deck_strategy)
@settings(max_examples=50)
def test_blackjack_deck_instantiation(instance):
    assert isinstance(instance, blackjack_Deck)

@given(instance=blackjack_DealerBot_strategy)
@settings(max_examples=50)
def test_blackjack_dealerbot_instantiation(instance):
    assert isinstance(instance, blackjack_DealerBot)

@given(instance=blackjack_CardSet_strategy)
@settings(max_examples=50)
def test_blackjack_cardset_instantiation(instance):
    assert isinstance(instance, blackjack_CardSet)

@given(instance=blackjack_Card_strategy)
@settings(max_examples=50)
def test_blackjack_card_instantiation(instance):
    assert isinstance(instance, blackjack_Card)



@given(instance=blackjack_Card_strategy)
def test_blackjack_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=blackjack_Card_strategy)
def test_blackjack_card_MAX_VALUE_OF_ACE_setter(instance):
    original = instance.MAX_VALUE_OF_ACE
    instance.MAX_VALUE_OF_ACE = original
    assert instance.MAX_VALUE_OF_ACE == original



@given(instance=blackjack_Card_strategy)
def test_blackjack_card_BLACKJACK_VALUE_setter(instance):
    original = instance.BLACKJACK_VALUE
    instance.BLACKJACK_VALUE = original
    assert instance.BLACKJACK_VALUE == original



@given(instance=blackjack_Card_strategy)
def test_blackjack_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blackjack_BlackjackHand_strategy)
@settings(max_examples=50)
def test_blackjack_blackjackhand_instantiation(instance):
    assert isinstance(instance, blackjack_BlackjackHand)

@given(instance=blackjack_DeckShuffledListener_Interface_strategy)
@settings(max_examples=50)
def test_blackjack_deckshuffledlistener_interface_instantiation(instance):
    assert isinstance(instance, blackjack_DeckShuffledListener_Interface)

@given(instance=blackjack_BlackjackGame_strategy)
@settings(max_examples=50)
def test_blackjack_blackjackgame_instantiation(instance):
    assert isinstance(instance, blackjack_BlackjackGame)



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_gameResultTextView_setter(instance):
    original = instance.gameResultTextView
    instance.gameResultTextView = original
    assert instance.gameResultTextView == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_hitButton_setter(instance):
    original = instance.hitButton
    instance.hitButton = original
    assert instance.hitButton == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_MAX_CARDS_PULLED_setter(instance):
    original = instance.MAX_CARDS_PULLED
    instance.MAX_CARDS_PULLED = original
    assert instance.MAX_CARDS_PULLED == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_MAX_HITS_setter(instance):
    original = instance.MAX_HITS
    instance.MAX_HITS = original
    assert instance.MAX_HITS == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_dealersHandValueTextView_setter(instance):
    original = instance.dealersHandValueTextView
    instance.dealersHandValueTextView = original
    assert instance.dealersHandValueTextView == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_playersHandTextView_setter(instance):
    original = instance.playersHandTextView
    instance.playersHandTextView = original
    assert instance.playersHandTextView == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_playerHandValueTextView_setter(instance):
    original = instance.playerHandValueTextView
    instance.playerHandValueTextView = original
    assert instance.playerHandValueTextView == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_stayButton_setter(instance):
    original = instance.stayButton
    instance.stayButton = original
    assert instance.stayButton == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_dealersHandTextView_setter(instance):
    original = instance.dealersHandTextView
    instance.dealersHandTextView = original
    assert instance.dealersHandTextView == original



@given(instance=blackjack_BlackjackGame_strategy)
def test_blackjack_blackjackgame_gstate_setter(instance):
    original = instance.gstate
    instance.gstate = original
    assert instance.gstate == original

@given(instance=blackjack_ExampleInstrumentedTest_strategy)
@settings(max_examples=50)
def test_blackjack_exampleinstrumentedtest_instantiation(instance):
    assert isinstance(instance, blackjack_ExampleInstrumentedTest)
