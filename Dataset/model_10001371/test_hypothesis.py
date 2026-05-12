import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Player,
    JButton,
    Strategy,
    Card,
    HandDeck,
    Deck,
    BlackjackGame,
    Dealer,
    Gambler,
    JLabel,
    UseCase_UseCase,
    User_Actor,
    BJPlayer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_jbutton_is_not_abstract():
    assert not inspect.isabstract(JButton)


def test_jbutton_constructor_exists():
    assert callable(JButton.__init__)


def test_jbutton_constructor_args():
    sig = inspect.signature(JButton.__init__)
    params = list(sig.parameters.keys())



def test_strategy_is_not_abstract():
    assert not inspect.isabstract(Strategy)


def test_strategy_constructor_exists():
    assert callable(Strategy.__init__)


def test_strategy_constructor_args():
    sig = inspect.signature(Strategy.__init__)
    params = list(sig.parameters.keys())
    assert "game" in params, "Missing parameter 'game'"

def test_strategy_has_game():
    assert hasattr(Strategy, "game")
    descriptor = None
    for klass in Strategy.__mro__:
        if "game" in klass.__dict__:
            descriptor = klass.__dict__["game"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "valueHard" in params, "Missing parameter 'valueHard'"
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "Count" in params, "Missing parameter 'Count'"
    assert "valueSoft" in params, "Missing parameter 'valueSoft'"
    assert "avatar" in params, "Missing parameter 'avatar'"
    assert "name" in params, "Missing parameter 'name'"

def test_card_has_valueHard():
    assert hasattr(Card, "valueHard")
    descriptor = None
    for klass in Card.__mro__:
        if "valueHard" in klass.__dict__:
            descriptor = klass.__dict__["valueHard"]
            break
    assert isinstance(descriptor, property)

def test_card_has_rank():
    assert hasattr(Card, "rank")
    descriptor = None
    for klass in Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
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

def test_card_has_Count():
    assert hasattr(Card, "Count")
    descriptor = None
    for klass in Card.__mro__:
        if "Count" in klass.__dict__:
            descriptor = klass.__dict__["Count"]
            break
    assert isinstance(descriptor, property)

def test_card_has_valueSoft():
    assert hasattr(Card, "valueSoft")
    descriptor = None
    for klass in Card.__mro__:
        if "valueSoft" in klass.__dict__:
            descriptor = klass.__dict__["valueSoft"]
            break
    assert isinstance(descriptor, property)

def test_card_has_avatar():
    assert hasattr(Card, "avatar")
    descriptor = None
    for klass in Card.__mro__:
        if "avatar" in klass.__dict__:
            descriptor = klass.__dict__["avatar"]
            break
    assert isinstance(descriptor, property)

def test_card_has_name():
    assert hasattr(Card, "name")
    descriptor = None
    for klass in Card.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_handdeck_is_not_abstract():
    assert not inspect.isabstract(HandDeck)


def test_handdeck_constructor_exists():
    assert callable(HandDeck.__init__)


def test_handdeck_constructor_args():
    sig = inspect.signature(HandDeck.__init__)
    params = list(sig.parameters.keys())
    assert "total" in params, "Missing parameter 'total'"
    assert "cards" in params, "Missing parameter 'cards'"

def test_handdeck_has_total():
    assert hasattr(HandDeck, "total")
    descriptor = None
    for klass in HandDeck.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_handdeck_has_cards():
    assert hasattr(HandDeck, "cards")
    descriptor = None
    for klass in HandDeck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)



def test_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"

def test_deck_has_cards():
    assert hasattr(Deck, "cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)



def test_blackjackgame_is_not_abstract():
    assert not inspect.isabstract(BlackjackGame)


def test_blackjackgame_constructor_exists():
    assert callable(BlackjackGame.__init__)


def test_blackjackgame_constructor_args():
    sig = inspect.signature(BlackjackGame.__init__)
    params = list(sig.parameters.keys())
    assert "player" in params, "Missing parameter 'player'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "dealer" in params, "Missing parameter 'dealer'"
    assert "bet" in params, "Missing parameter 'bet'"

def test_blackjackgame_has_player():
    assert hasattr(BlackjackGame, "player")
    descriptor = None
    for klass in BlackjackGame.__mro__:
        if "player" in klass.__dict__:
            descriptor = klass.__dict__["player"]
            break
    assert isinstance(descriptor, property)

def test_blackjackgame_has_deck():
    assert hasattr(BlackjackGame, "deck")
    descriptor = None
    for klass in BlackjackGame.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_blackjackgame_has_dealer():
    assert hasattr(BlackjackGame, "dealer")
    descriptor = None
    for klass in BlackjackGame.__mro__:
        if "dealer" in klass.__dict__:
            descriptor = klass.__dict__["dealer"]
            break
    assert isinstance(descriptor, property)

def test_blackjackgame_has_bet():
    assert hasattr(BlackjackGame, "bet")
    descriptor = None
    for klass in BlackjackGame.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)



def test_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "cardTotalLimit" in params, "Missing parameter 'cardTotalLimit'"
    assert "hand" in params, "Missing parameter 'hand'"

def test_dealer_has_cardTotalLimit():
    assert hasattr(Dealer, "cardTotalLimit")
    descriptor = None
    for klass in Dealer.__mro__:
        if "cardTotalLimit" in klass.__dict__:
            descriptor = klass.__dict__["cardTotalLimit"]
            break
    assert isinstance(descriptor, property)

def test_dealer_has_hand():
    assert hasattr(Dealer, "hand")
    descriptor = None
    for klass in Dealer.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)



def test_gambler_is_not_abstract():
    assert not inspect.isabstract(Gambler)


def test_gambler_constructor_exists():
    assert callable(Gambler.__init__)


def test_gambler_constructor_args():
    sig = inspect.signature(Gambler.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "profile" in params, "Missing parameter 'profile'"

def test_gambler_has_money():
    assert hasattr(Gambler, "money")
    descriptor = None
    for klass in Gambler.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_gambler_has_hand():
    assert hasattr(Gambler, "hand")
    descriptor = None
    for klass in Gambler.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)

def test_gambler_has_profile():
    assert hasattr(Gambler, "profile")
    descriptor = None
    for klass in Gambler.__mro__:
        if "profile" in klass.__dict__:
            descriptor = klass.__dict__["profile"]
            break
    assert isinstance(descriptor, property)



def test_jlabel_is_not_abstract():
    assert not inspect.isabstract(JLabel)


def test_jlabel_constructor_exists():
    assert callable(JLabel.__init__)


def test_jlabel_constructor_args():
    sig = inspect.signature(JLabel.__init__)
    params = list(sig.parameters.keys())



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
    params = list(sig.parameters.keys())



def test_bjplayer_is_not_abstract():
    assert not inspect.isabstract(BJPlayer)


def test_bjplayer_constructor_exists():
    assert callable(BJPlayer.__init__)


def test_bjplayer_constructor_args():
    sig = inspect.signature(BJPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "isBusted" in params, "Missing parameter 'isBusted'"

def test_bjplayer_has_isBusted():
    assert hasattr(BJPlayer, "isBusted")
    descriptor = None
    for klass in BJPlayer.__mro__:
        if "isBusted" in klass.__dict__:
            descriptor = klass.__dict__["isBusted"]
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
Player_strategy = st.builds(
    Player,
)
JButton_strategy = st.builds(
    JButton,
)
Strategy_strategy = st.builds(
    Strategy,
    game=
        st.none()
)
Card_strategy = st.builds(
    Card,
    valueHard=
        safe_text,
    rank=
        safe_text,
    suit=
        safe_text,
    Count=
        st.integers(),
    valueSoft=
        safe_text,
    avatar=
        safe_text,
    name=
        safe_text
)
HandDeck_strategy = st.builds(
    HandDeck,
    total=
        st.integers(),
    cards=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    cards=
        st.none()
)
BlackjackGame_strategy = st.builds(
    BlackjackGame,
    player=
        st.none(),
    deck=
        st.none(),
    dealer=
        st.none(),
    bet=
        st.integers()
)
Dealer_strategy = st.builds(
    Dealer,
    cardTotalLimit=
        st.integers(),
    hand=
        st.none()
)
Gambler_strategy = st.builds(
    Gambler,
    money=
        st.integers(),
    hand=
        st.none(),
    profile=
        safe_text
)
JLabel_strategy = st.builds(
    JLabel,
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
User_Actor_strategy = st.builds(
    User_Actor,
)
BJPlayer_strategy = st.builds(
    BJPlayer,
    isBusted=
        st.booleans()
)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=JButton_strategy)
@settings(max_examples=50)
def test_jbutton_instantiation(instance):
    assert isinstance(instance, JButton)

@given(instance=Strategy_strategy)
@settings(max_examples=50)
def test_strategy_instantiation(instance):
    assert isinstance(instance, Strategy)



@given(instance=Strategy_strategy)
def test_strategy_game_setter(instance):
    original = instance.game
    instance.game = original
    assert instance.game == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_valueHard_setter(instance):
    original = instance.valueHard
    instance.valueHard = original
    assert instance.valueHard == original



@given(instance=Card_strategy)
def test_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_card_Count_setter(instance):
    original = instance.Count
    instance.Count = original
    assert instance.Count == original



@given(instance=Card_strategy)
def test_card_valueSoft_setter(instance):
    original = instance.valueSoft
    instance.valueSoft = original
    assert instance.valueSoft == original



@given(instance=Card_strategy)
def test_card_avatar_setter(instance):
    original = instance.avatar
    instance.avatar = original
    assert instance.avatar == original



@given(instance=Card_strategy)
def test_card_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HandDeck_strategy)
@settings(max_examples=50)
def test_handdeck_instantiation(instance):
    assert isinstance(instance, HandDeck)



@given(instance=HandDeck_strategy)
def test_handdeck_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=HandDeck_strategy)
def test_handdeck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=BlackjackGame_strategy)
@settings(max_examples=50)
def test_blackjackgame_instantiation(instance):
    assert isinstance(instance, BlackjackGame)



@given(instance=BlackjackGame_strategy)
def test_blackjackgame_player_setter(instance):
    original = instance.player
    instance.player = original
    assert instance.player == original



@given(instance=BlackjackGame_strategy)
def test_blackjackgame_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=BlackjackGame_strategy)
def test_blackjackgame_dealer_setter(instance):
    original = instance.dealer
    instance.dealer = original
    assert instance.dealer == original



@given(instance=BlackjackGame_strategy)
def test_blackjackgame_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original

@given(instance=Dealer_strategy)
@settings(max_examples=50)
def test_dealer_instantiation(instance):
    assert isinstance(instance, Dealer)



@given(instance=Dealer_strategy)
def test_dealer_cardTotalLimit_setter(instance):
    original = instance.cardTotalLimit
    instance.cardTotalLimit = original
    assert instance.cardTotalLimit == original



@given(instance=Dealer_strategy)
def test_dealer_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original

@given(instance=Gambler_strategy)
@settings(max_examples=50)
def test_gambler_instantiation(instance):
    assert isinstance(instance, Gambler)



@given(instance=Gambler_strategy)
def test_gambler_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Gambler_strategy)
def test_gambler_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Gambler_strategy)
def test_gambler_profile_setter(instance):
    original = instance.profile
    instance.profile = original
    assert instance.profile == original

@given(instance=JLabel_strategy)
@settings(max_examples=50)
def test_jlabel_instantiation(instance):
    assert isinstance(instance, JLabel)

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=User_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, User_Actor)

@given(instance=BJPlayer_strategy)
@settings(max_examples=50)
def test_bjplayer_instantiation(instance):
    assert isinstance(instance, BJPlayer)



@given(instance=BJPlayer_strategy)
def test_bjplayer_isBusted_setter(instance):
    original = instance.isBusted
    instance.isBusted = original
    assert instance.isBusted == original
