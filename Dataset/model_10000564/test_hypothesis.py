import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Card,
    Main,
    Croupier,
    Joueur,
    Blackjack,
    Stand_UseCase1,
    Ask_Player_to_Cut_Deck_UseCase,
    Reveal_Last_Card_UseCase,
    Call_for_Last_Bets_UseCase,
    Deal_UseCase,
    Cut_Deck_UseCase,
    Shuffle_Shoe_UseCase,
    Pay_Chips_UseCase,
    Take_Chips_UseCase,
    Hit_UseCase1,
    Leave_Table_UseCase,
    Sit_at_Table_UseCase,
    Hit_UseCase,
    Stand_UseCase,
    Double_Down_UseCase,
    Split_Hand_UseCase,
    Place_Bet_UseCase,
    Dealer__automated__Actor,
    Player_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
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



def test_main_is_not_abstract():
    assert not inspect.isabstract(Main)


def test_main_constructor_exists():
    assert callable(Main.__init__)


def test_main_constructor_args():
    sig = inspect.signature(Main.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "cartes" in params, "Missing parameter 'cartes'"
    assert "bet" in params, "Missing parameter 'bet'"

def test_main_has_value():
    assert hasattr(Main, "value")
    descriptor = None
    for klass in Main.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_main_has_cartes():
    assert hasattr(Main, "cartes")
    descriptor = None
    for klass in Main.__mro__:
        if "cartes" in klass.__dict__:
            descriptor = klass.__dict__["cartes"]
            break
    assert isinstance(descriptor, property)

def test_main_has_bet():
    assert hasattr(Main, "bet")
    descriptor = None
    for klass in Main.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)



def test_croupier_is_not_abstract():
    assert not inspect.isabstract(Croupier)


def test_croupier_constructor_exists():
    assert callable(Croupier.__init__)


def test_croupier_constructor_args():
    sig = inspect.signature(Croupier.__init__)
    params = list(sig.parameters.keys())
    assert "main" in params, "Missing parameter 'main'"

def test_croupier_has_main():
    assert hasattr(Croupier, "main")
    descriptor = None
    for klass in Croupier.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_joueur_is_not_abstract():
    assert not inspect.isabstract(Joueur)


def test_joueur_constructor_exists():
    assert callable(Joueur.__init__)


def test_joueur_constructor_args():
    sig = inspect.signature(Joueur.__init__)
    params = list(sig.parameters.keys())
    assert "main" in params, "Missing parameter 'main'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "playerbank" in params, "Missing parameter 'playerbank'"

def test_joueur_has_main():
    assert hasattr(Joueur, "main")
    descriptor = None
    for klass in Joueur.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)

def test_joueur_has_nom():
    assert hasattr(Joueur, "nom")
    descriptor = None
    for klass in Joueur.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_joueur_has_playerbank():
    assert hasattr(Joueur, "playerbank")
    descriptor = None
    for klass in Joueur.__mro__:
        if "playerbank" in klass.__dict__:
            descriptor = klass.__dict__["playerbank"]
            break
    assert isinstance(descriptor, property)



def test_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())
    assert "joueurs" in params, "Missing parameter 'joueurs'"
    assert "croupier" in params, "Missing parameter 'croupier'"

def test_blackjack_has_joueurs():
    assert hasattr(Blackjack, "joueurs")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "joueurs" in klass.__dict__:
            descriptor = klass.__dict__["joueurs"]
            break
    assert isinstance(descriptor, property)

def test_blackjack_has_croupier():
    assert hasattr(Blackjack, "croupier")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "croupier" in klass.__dict__:
            descriptor = klass.__dict__["croupier"]
            break
    assert isinstance(descriptor, property)



def test_stand_usecase1_is_not_abstract():
    assert not inspect.isabstract(Stand_UseCase1)


def test_stand_usecase1_constructor_exists():
    assert callable(Stand_UseCase1.__init__)


def test_stand_usecase1_constructor_args():
    sig = inspect.signature(Stand_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_ask_player_to_cut_deck_usecase_is_not_abstract():
    assert not inspect.isabstract(Ask_Player_to_Cut_Deck_UseCase)


def test_ask_player_to_cut_deck_usecase_constructor_exists():
    assert callable(Ask_Player_to_Cut_Deck_UseCase.__init__)


def test_ask_player_to_cut_deck_usecase_constructor_args():
    sig = inspect.signature(Ask_Player_to_Cut_Deck_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_reveal_last_card_usecase_is_not_abstract():
    assert not inspect.isabstract(Reveal_Last_Card_UseCase)


def test_reveal_last_card_usecase_constructor_exists():
    assert callable(Reveal_Last_Card_UseCase.__init__)


def test_reveal_last_card_usecase_constructor_args():
    sig = inspect.signature(Reveal_Last_Card_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_call_for_last_bets_usecase_is_not_abstract():
    assert not inspect.isabstract(Call_for_Last_Bets_UseCase)


def test_call_for_last_bets_usecase_constructor_exists():
    assert callable(Call_for_Last_Bets_UseCase.__init__)


def test_call_for_last_bets_usecase_constructor_args():
    sig = inspect.signature(Call_for_Last_Bets_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_deal_usecase_is_not_abstract():
    assert not inspect.isabstract(Deal_UseCase)


def test_deal_usecase_constructor_exists():
    assert callable(Deal_UseCase.__init__)


def test_deal_usecase_constructor_args():
    sig = inspect.signature(Deal_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_cut_deck_usecase_is_not_abstract():
    assert not inspect.isabstract(Cut_Deck_UseCase)


def test_cut_deck_usecase_constructor_exists():
    assert callable(Cut_Deck_UseCase.__init__)


def test_cut_deck_usecase_constructor_args():
    sig = inspect.signature(Cut_Deck_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_shuffle_shoe_usecase_is_not_abstract():
    assert not inspect.isabstract(Shuffle_Shoe_UseCase)


def test_shuffle_shoe_usecase_constructor_exists():
    assert callable(Shuffle_Shoe_UseCase.__init__)


def test_shuffle_shoe_usecase_constructor_args():
    sig = inspect.signature(Shuffle_Shoe_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_pay_chips_usecase_is_not_abstract():
    assert not inspect.isabstract(Pay_Chips_UseCase)


def test_pay_chips_usecase_constructor_exists():
    assert callable(Pay_Chips_UseCase.__init__)


def test_pay_chips_usecase_constructor_args():
    sig = inspect.signature(Pay_Chips_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_take_chips_usecase_is_not_abstract():
    assert not inspect.isabstract(Take_Chips_UseCase)


def test_take_chips_usecase_constructor_exists():
    assert callable(Take_Chips_UseCase.__init__)


def test_take_chips_usecase_constructor_args():
    sig = inspect.signature(Take_Chips_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hit_usecase1_is_not_abstract():
    assert not inspect.isabstract(Hit_UseCase1)


def test_hit_usecase1_constructor_exists():
    assert callable(Hit_UseCase1.__init__)


def test_hit_usecase1_constructor_args():
    sig = inspect.signature(Hit_UseCase1.__init__)
    params = list(sig.parameters.keys())



def test_leave_table_usecase_is_not_abstract():
    assert not inspect.isabstract(Leave_Table_UseCase)


def test_leave_table_usecase_constructor_exists():
    assert callable(Leave_Table_UseCase.__init__)


def test_leave_table_usecase_constructor_args():
    sig = inspect.signature(Leave_Table_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sit_at_table_usecase_is_not_abstract():
    assert not inspect.isabstract(Sit_at_Table_UseCase)


def test_sit_at_table_usecase_constructor_exists():
    assert callable(Sit_at_Table_UseCase.__init__)


def test_sit_at_table_usecase_constructor_args():
    sig = inspect.signature(Sit_at_Table_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hit_usecase_is_not_abstract():
    assert not inspect.isabstract(Hit_UseCase)


def test_hit_usecase_constructor_exists():
    assert callable(Hit_UseCase.__init__)


def test_hit_usecase_constructor_args():
    sig = inspect.signature(Hit_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_stand_usecase_is_not_abstract():
    assert not inspect.isabstract(Stand_UseCase)


def test_stand_usecase_constructor_exists():
    assert callable(Stand_UseCase.__init__)


def test_stand_usecase_constructor_args():
    sig = inspect.signature(Stand_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_double_down_usecase_is_not_abstract():
    assert not inspect.isabstract(Double_Down_UseCase)


def test_double_down_usecase_constructor_exists():
    assert callable(Double_Down_UseCase.__init__)


def test_double_down_usecase_constructor_args():
    sig = inspect.signature(Double_Down_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_split_hand_usecase_is_not_abstract():
    assert not inspect.isabstract(Split_Hand_UseCase)


def test_split_hand_usecase_constructor_exists():
    assert callable(Split_Hand_UseCase.__init__)


def test_split_hand_usecase_constructor_args():
    sig = inspect.signature(Split_Hand_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_place_bet_usecase_is_not_abstract():
    assert not inspect.isabstract(Place_Bet_UseCase)


def test_place_bet_usecase_constructor_exists():
    assert callable(Place_Bet_UseCase.__init__)


def test_place_bet_usecase_constructor_args():
    sig = inspect.signature(Place_Bet_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_dealer__automated__actor_is_not_abstract():
    assert not inspect.isabstract(Dealer__automated__Actor)


def test_dealer__automated__actor_constructor_exists():
    assert callable(Dealer__automated__Actor.__init__)


def test_dealer__automated__actor_constructor_args():
    sig = inspect.signature(Dealer__automated__Actor.__init__)
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
Card_strategy = st.builds(
    Card,
    suit=
        st.integers(),
    rank=
        safe_text
)
Main_strategy = st.builds(
    Main,
    value=
        st.integers(),
    cartes=
        safe_text,
    bet=
        safe_text
)
Croupier_strategy = st.builds(
    Croupier,
    main=
        safe_text
)
Joueur_strategy = st.builds(
    Joueur,
    main=
        safe_text,
    nom=
        safe_text,
    playerbank=
        st.integers()
)
Blackjack_strategy = st.builds(
    Blackjack,
    joueurs=
        safe_text,
    croupier=
        st.none()
)
Stand_UseCase1_strategy = st.builds(
    Stand_UseCase1,
)
Ask_Player_to_Cut_Deck_UseCase_strategy = st.builds(
    Ask_Player_to_Cut_Deck_UseCase,
)
Reveal_Last_Card_UseCase_strategy = st.builds(
    Reveal_Last_Card_UseCase,
)
Call_for_Last_Bets_UseCase_strategy = st.builds(
    Call_for_Last_Bets_UseCase,
)
Deal_UseCase_strategy = st.builds(
    Deal_UseCase,
)
Cut_Deck_UseCase_strategy = st.builds(
    Cut_Deck_UseCase,
)
Shuffle_Shoe_UseCase_strategy = st.builds(
    Shuffle_Shoe_UseCase,
)
Pay_Chips_UseCase_strategy = st.builds(
    Pay_Chips_UseCase,
)
Take_Chips_UseCase_strategy = st.builds(
    Take_Chips_UseCase,
)
Hit_UseCase1_strategy = st.builds(
    Hit_UseCase1,
)
Leave_Table_UseCase_strategy = st.builds(
    Leave_Table_UseCase,
)
Sit_at_Table_UseCase_strategy = st.builds(
    Sit_at_Table_UseCase,
)
Hit_UseCase_strategy = st.builds(
    Hit_UseCase,
)
Stand_UseCase_strategy = st.builds(
    Stand_UseCase,
)
Double_Down_UseCase_strategy = st.builds(
    Double_Down_UseCase,
)
Split_Hand_UseCase_strategy = st.builds(
    Split_Hand_UseCase,
)
Place_Bet_UseCase_strategy = st.builds(
    Place_Bet_UseCase,
)
Dealer__automated__Actor_strategy = st.builds(
    Dealer__automated__Actor,
)
Player_Actor_strategy = st.builds(
    Player_Actor,
)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=Main_strategy)
@settings(max_examples=50)
def test_main_instantiation(instance):
    assert isinstance(instance, Main)



@given(instance=Main_strategy)
def test_main_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Main_strategy)
def test_main_cartes_setter(instance):
    original = instance.cartes
    instance.cartes = original
    assert instance.cartes == original



@given(instance=Main_strategy)
def test_main_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original

@given(instance=Croupier_strategy)
@settings(max_examples=50)
def test_croupier_instantiation(instance):
    assert isinstance(instance, Croupier)



@given(instance=Croupier_strategy)
def test_croupier_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=Joueur_strategy)
@settings(max_examples=50)
def test_joueur_instantiation(instance):
    assert isinstance(instance, Joueur)



@given(instance=Joueur_strategy)
def test_joueur_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original



@given(instance=Joueur_strategy)
def test_joueur_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Joueur_strategy)
def test_joueur_playerbank_setter(instance):
    original = instance.playerbank
    instance.playerbank = original
    assert instance.playerbank == original

@given(instance=Blackjack_strategy)
@settings(max_examples=50)
def test_blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)



@given(instance=Blackjack_strategy)
def test_blackjack_joueurs_setter(instance):
    original = instance.joueurs
    instance.joueurs = original
    assert instance.joueurs == original



@given(instance=Blackjack_strategy)
def test_blackjack_croupier_setter(instance):
    original = instance.croupier
    instance.croupier = original
    assert instance.croupier == original

@given(instance=Stand_UseCase1_strategy)
@settings(max_examples=50)
def test_stand_usecase1_instantiation(instance):
    assert isinstance(instance, Stand_UseCase1)

@given(instance=Ask_Player_to_Cut_Deck_UseCase_strategy)
@settings(max_examples=50)
def test_ask_player_to_cut_deck_usecase_instantiation(instance):
    assert isinstance(instance, Ask_Player_to_Cut_Deck_UseCase)

@given(instance=Reveal_Last_Card_UseCase_strategy)
@settings(max_examples=50)
def test_reveal_last_card_usecase_instantiation(instance):
    assert isinstance(instance, Reveal_Last_Card_UseCase)

@given(instance=Call_for_Last_Bets_UseCase_strategy)
@settings(max_examples=50)
def test_call_for_last_bets_usecase_instantiation(instance):
    assert isinstance(instance, Call_for_Last_Bets_UseCase)

@given(instance=Deal_UseCase_strategy)
@settings(max_examples=50)
def test_deal_usecase_instantiation(instance):
    assert isinstance(instance, Deal_UseCase)

@given(instance=Cut_Deck_UseCase_strategy)
@settings(max_examples=50)
def test_cut_deck_usecase_instantiation(instance):
    assert isinstance(instance, Cut_Deck_UseCase)

@given(instance=Shuffle_Shoe_UseCase_strategy)
@settings(max_examples=50)
def test_shuffle_shoe_usecase_instantiation(instance):
    assert isinstance(instance, Shuffle_Shoe_UseCase)

@given(instance=Pay_Chips_UseCase_strategy)
@settings(max_examples=50)
def test_pay_chips_usecase_instantiation(instance):
    assert isinstance(instance, Pay_Chips_UseCase)

@given(instance=Take_Chips_UseCase_strategy)
@settings(max_examples=50)
def test_take_chips_usecase_instantiation(instance):
    assert isinstance(instance, Take_Chips_UseCase)

@given(instance=Hit_UseCase1_strategy)
@settings(max_examples=50)
def test_hit_usecase1_instantiation(instance):
    assert isinstance(instance, Hit_UseCase1)

@given(instance=Leave_Table_UseCase_strategy)
@settings(max_examples=50)
def test_leave_table_usecase_instantiation(instance):
    assert isinstance(instance, Leave_Table_UseCase)

@given(instance=Sit_at_Table_UseCase_strategy)
@settings(max_examples=50)
def test_sit_at_table_usecase_instantiation(instance):
    assert isinstance(instance, Sit_at_Table_UseCase)

@given(instance=Hit_UseCase_strategy)
@settings(max_examples=50)
def test_hit_usecase_instantiation(instance):
    assert isinstance(instance, Hit_UseCase)

@given(instance=Stand_UseCase_strategy)
@settings(max_examples=50)
def test_stand_usecase_instantiation(instance):
    assert isinstance(instance, Stand_UseCase)

@given(instance=Double_Down_UseCase_strategy)
@settings(max_examples=50)
def test_double_down_usecase_instantiation(instance):
    assert isinstance(instance, Double_Down_UseCase)

@given(instance=Split_Hand_UseCase_strategy)
@settings(max_examples=50)
def test_split_hand_usecase_instantiation(instance):
    assert isinstance(instance, Split_Hand_UseCase)

@given(instance=Place_Bet_UseCase_strategy)
@settings(max_examples=50)
def test_place_bet_usecase_instantiation(instance):
    assert isinstance(instance, Place_Bet_UseCase)

@given(instance=Dealer__automated__Actor_strategy)
@settings(max_examples=50)
def test_dealer__automated__actor_instantiation(instance):
    assert isinstance(instance, Dealer__automated__Actor)

@given(instance=Player_Actor_strategy)
@settings(max_examples=50)
def test_player_actor_instantiation(instance):
    assert isinstance(instance, Player_Actor)
