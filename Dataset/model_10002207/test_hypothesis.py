import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BlackJackPlayer,
    Deck,
    BlackJackDriver,
    Card,
    BlackJack,
    Blackjack_Exit_UseCase,
    Blackjack_Play_Again_UseCase,
    Blackjack_Start_Game_UseCase,
    Blackjack_Bet_UseCase,
    Blackjack_Double_Down_UseCase,
    Blackjack_Split_UseCase,
    Blackjack_Stay_UseCase,
    Blackjack_Check_Win_Condition_UseCase,
    Blackjack_Deal_UseCase,
    Blackjack_Hit_UseCase,
    Dealer_Actor,
    Player_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_blackjackplayer_is_not_abstract():
    assert not inspect.isabstract(BlackJackPlayer)


def test_blackjackplayer_constructor_exists():
    assert callable(BlackJackPlayer.__init__)


def test_blackjackplayer_constructor_args():
    sig = inspect.signature(BlackJackPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "MaxNumCards" in params, "Missing parameter 'MaxNumCards'"
    assert "cards__" in params, "Missing parameter 'cards__'"
    assert "cardCount" in params, "Missing parameter 'cardCount'"

def test_blackjackplayer_has_MaxNumCards():
    assert hasattr(BlackJackPlayer, "MaxNumCards")
    descriptor = None
    for klass in BlackJackPlayer.__mro__:
        if "MaxNumCards" in klass.__dict__:
            descriptor = klass.__dict__["MaxNumCards"]
            break
    assert isinstance(descriptor, property)

def test_blackjackplayer_has_cards__():
    assert hasattr(BlackJackPlayer, "cards__")
    descriptor = None
    for klass in BlackJackPlayer.__mro__:
        if "cards__" in klass.__dict__:
            descriptor = klass.__dict__["cards__"]
            break
    assert isinstance(descriptor, property)

def test_blackjackplayer_has_cardCount():
    assert hasattr(BlackJackPlayer, "cardCount")
    descriptor = None
    for klass in BlackJackPlayer.__mro__:
        if "cardCount" in klass.__dict__:
            descriptor = klass.__dict__["cardCount"]
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
    assert "cardsUsed" in params, "Missing parameter 'cardsUsed'"

def test_deck_has_deck():
    assert hasattr(Deck, "deck")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_deck_has_cardsUsed():
    assert hasattr(Deck, "cardsUsed")
    descriptor = None
    for klass in Deck.__mro__:
        if "cardsUsed" in klass.__dict__:
            descriptor = klass.__dict__["cardsUsed"]
            break
    assert isinstance(descriptor, property)



def test_blackjackdriver_is_not_abstract():
    assert not inspect.isabstract(BlackJackDriver)


def test_blackjackdriver_constructor_exists():
    assert callable(BlackJackDriver.__init__)


def test_blackjackdriver_constructor_args():
    sig = inspect.signature(BlackJackDriver.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "faceValue" in params, "Missing parameter 'faceValue'"
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_card_has_faceValue():
    assert hasattr(Card, "faceValue")
    descriptor = None
    for klass in Card.__mro__:
        if "faceValue" in klass.__dict__:
            descriptor = klass.__dict__["faceValue"]
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

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_is_not_abstract():
    assert not inspect.isabstract(BlackJack)


def test_blackjack_constructor_exists():
    assert callable(BlackJack.__init__)


def test_blackjack_constructor_args():
    sig = inspect.signature(BlackJack.__init__)
    params = list(sig.parameters.keys())
    assert "playersHand" in params, "Missing parameter 'playersHand'"
    assert "bet" in params, "Missing parameter 'bet'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "money" in params, "Missing parameter 'money'"
    assert "dealersHand" in params, "Missing parameter 'dealersHand'"
    assert "handCount" in params, "Missing parameter 'handCount'"

def test_blackjack_has_playersHand():
    assert hasattr(BlackJack, "playersHand")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "playersHand" in klass.__dict__:
            descriptor = klass.__dict__["playersHand"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_bet():
    assert hasattr(BlackJack, "bet")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_deck():
    assert hasattr(BlackJack, "deck")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_money():
    assert hasattr(BlackJack, "money")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_dealersHand():
    assert hasattr(BlackJack, "dealersHand")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "dealersHand" in klass.__dict__:
            descriptor = klass.__dict__["dealersHand"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_handCount():
    assert hasattr(BlackJack, "handCount")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "handCount" in klass.__dict__:
            descriptor = klass.__dict__["handCount"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_exit_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Exit_UseCase)


def test_blackjack_exit_usecase_constructor_exists():
    assert callable(Blackjack_Exit_UseCase.__init__)


def test_blackjack_exit_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Exit_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_play_again_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Play_Again_UseCase)


def test_blackjack_play_again_usecase_constructor_exists():
    assert callable(Blackjack_Play_Again_UseCase.__init__)


def test_blackjack_play_again_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Play_Again_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_start_game_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Start_Game_UseCase)


def test_blackjack_start_game_usecase_constructor_exists():
    assert callable(Blackjack_Start_Game_UseCase.__init__)


def test_blackjack_start_game_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Start_Game_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_bet_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Bet_UseCase)


def test_blackjack_bet_usecase_constructor_exists():
    assert callable(Blackjack_Bet_UseCase.__init__)


def test_blackjack_bet_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Bet_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_double_down_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Double_Down_UseCase)


def test_blackjack_double_down_usecase_constructor_exists():
    assert callable(Blackjack_Double_Down_UseCase.__init__)


def test_blackjack_double_down_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Double_Down_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_split_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Split_UseCase)


def test_blackjack_split_usecase_constructor_exists():
    assert callable(Blackjack_Split_UseCase.__init__)


def test_blackjack_split_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Split_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_stay_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Stay_UseCase)


def test_blackjack_stay_usecase_constructor_exists():
    assert callable(Blackjack_Stay_UseCase.__init__)


def test_blackjack_stay_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Stay_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_check_win_condition_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Check_Win_Condition_UseCase)


def test_blackjack_check_win_condition_usecase_constructor_exists():
    assert callable(Blackjack_Check_Win_Condition_UseCase.__init__)


def test_blackjack_check_win_condition_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Check_Win_Condition_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_deal_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Deal_UseCase)


def test_blackjack_deal_usecase_constructor_exists():
    assert callable(Blackjack_Deal_UseCase.__init__)


def test_blackjack_deal_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Deal_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_blackjack_hit_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Hit_UseCase)


def test_blackjack_hit_usecase_constructor_exists():
    assert callable(Blackjack_Hit_UseCase.__init__)


def test_blackjack_hit_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Hit_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_dealer_actor_is_not_abstract():
    assert not inspect.isabstract(Dealer_Actor)


def test_dealer_actor_constructor_exists():
    assert callable(Dealer_Actor.__init__)


def test_dealer_actor_constructor_args():
    sig = inspect.signature(Dealer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_player_actor_is_not_abstract():
    assert not inspect.isabstract(Player_Actor)


def test_player_actor_constructor_exists():
    assert callable(Player_Actor.__init__)


def test_player_actor_constructor_args():
    sig = inspect.signature(Player_Actor.__init__)
    params = list(sig.parameters.keys())


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
BlackJackPlayer_strategy = st.builds(
    BlackJackPlayer,
    MaxNumCards=
        st.integers(),
    cards__=
        st.none(),
    cardCount=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    deck=
        st.none(),
    cardsUsed=
        st.integers()
)
BlackJackDriver_strategy = st.builds(
    BlackJackDriver,
)
Card_strategy = st.builds(
    Card,
    faceValue=
        safe_text,
    value=
        st.integers(),
    suit=
        safe_text
)
BlackJack_strategy = st.builds(
    BlackJack,
    playersHand=
        st.none(),
    bet=
        st.integers(),
    deck=
        st.none(),
    money=
        st.integers(),
    dealersHand=
        st.none(),
    handCount=
        st.integers()
)
Blackjack_Exit_UseCase_strategy = st.builds(
    Blackjack_Exit_UseCase,
)
Blackjack_Play_Again_UseCase_strategy = st.builds(
    Blackjack_Play_Again_UseCase,
)
Blackjack_Start_Game_UseCase_strategy = st.builds(
    Blackjack_Start_Game_UseCase,
)
Blackjack_Bet_UseCase_strategy = st.builds(
    Blackjack_Bet_UseCase,
)
Blackjack_Double_Down_UseCase_strategy = st.builds(
    Blackjack_Double_Down_UseCase,
)
Blackjack_Split_UseCase_strategy = st.builds(
    Blackjack_Split_UseCase,
)
Blackjack_Stay_UseCase_strategy = st.builds(
    Blackjack_Stay_UseCase,
)
Blackjack_Check_Win_Condition_UseCase_strategy = st.builds(
    Blackjack_Check_Win_Condition_UseCase,
)
Blackjack_Deal_UseCase_strategy = st.builds(
    Blackjack_Deal_UseCase,
)
Blackjack_Hit_UseCase_strategy = st.builds(
    Blackjack_Hit_UseCase,
)
Dealer_Actor_strategy = st.builds(
    Dealer_Actor,
)
Player_Actor_strategy = st.builds(
    Player_Actor,
)

@given(instance=BlackJackPlayer_strategy)
@settings(max_examples=50)
def test_blackjackplayer_instantiation(instance):
    assert isinstance(instance, BlackJackPlayer)



@given(instance=BlackJackPlayer_strategy)
def test_blackjackplayer_MaxNumCards_setter(instance):
    original = instance.MaxNumCards
    instance.MaxNumCards = original
    assert instance.MaxNumCards == original



@given(instance=BlackJackPlayer_strategy)
def test_blackjackplayer_cards___setter(instance):
    original = instance.cards__
    instance.cards__ = original
    assert instance.cards__ == original



@given(instance=BlackJackPlayer_strategy)
def test_blackjackplayer_cardCount_setter(instance):
    original = instance.cardCount
    instance.cardCount = original
    assert instance.cardCount == original

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
def test_deck_cardsUsed_setter(instance):
    original = instance.cardsUsed
    instance.cardsUsed = original
    assert instance.cardsUsed == original

@given(instance=BlackJackDriver_strategy)
@settings(max_examples=50)
def test_blackjackdriver_instantiation(instance):
    assert isinstance(instance, BlackJackDriver)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_faceValue_setter(instance):
    original = instance.faceValue
    instance.faceValue = original
    assert instance.faceValue == original



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

@given(instance=BlackJack_strategy)
@settings(max_examples=50)
def test_blackjack_instantiation(instance):
    assert isinstance(instance, BlackJack)



@given(instance=BlackJack_strategy)
def test_blackjack_playersHand_setter(instance):
    original = instance.playersHand
    instance.playersHand = original
    assert instance.playersHand == original



@given(instance=BlackJack_strategy)
def test_blackjack_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original



@given(instance=BlackJack_strategy)
def test_blackjack_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=BlackJack_strategy)
def test_blackjack_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=BlackJack_strategy)
def test_blackjack_dealersHand_setter(instance):
    original = instance.dealersHand
    instance.dealersHand = original
    assert instance.dealersHand == original



@given(instance=BlackJack_strategy)
def test_blackjack_handCount_setter(instance):
    original = instance.handCount
    instance.handCount = original
    assert instance.handCount == original

@given(instance=Blackjack_Exit_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_exit_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Exit_UseCase)

@given(instance=Blackjack_Play_Again_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_play_again_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Play_Again_UseCase)

@given(instance=Blackjack_Start_Game_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_start_game_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Start_Game_UseCase)

@given(instance=Blackjack_Bet_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_bet_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Bet_UseCase)

@given(instance=Blackjack_Double_Down_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_double_down_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Double_Down_UseCase)

@given(instance=Blackjack_Split_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_split_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Split_UseCase)

@given(instance=Blackjack_Stay_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_stay_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Stay_UseCase)

@given(instance=Blackjack_Check_Win_Condition_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_check_win_condition_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Check_Win_Condition_UseCase)

@given(instance=Blackjack_Deal_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_deal_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Deal_UseCase)

@given(instance=Blackjack_Hit_UseCase_strategy)
@settings(max_examples=50)
def test_blackjack_hit_usecase_instantiation(instance):
    assert isinstance(instance, Blackjack_Hit_UseCase)

@given(instance=Dealer_Actor_strategy)
@settings(max_examples=50)
def test_dealer_actor_instantiation(instance):
    assert isinstance(instance, Dealer_Actor)

@given(instance=Player_Actor_strategy)
@settings(max_examples=50)
def test_player_actor_instantiation(instance):
    assert isinstance(instance, Player_Actor)
