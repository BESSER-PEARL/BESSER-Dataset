import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Blackjack,
    Joueur,
    Main,
    Croupier,
    Carte,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_joueur_is_not_abstract():
    assert not inspect.isabstract(Joueur)


def test_joueur_constructor_exists():
    assert callable(Joueur.__init__)


def test_joueur_constructor_args():
    sig = inspect.signature(Joueur.__init__)
    params = list(sig.parameters.keys())
    assert "playerbank" in params, "Missing parameter 'playerbank'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "main" in params, "Missing parameter 'main'"

def test_joueur_has_playerbank():
    assert hasattr(Joueur, "playerbank")
    descriptor = None
    for klass in Joueur.__mro__:
        if "playerbank" in klass.__dict__:
            descriptor = klass.__dict__["playerbank"]
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

def test_joueur_has_main():
    assert hasattr(Joueur, "main")
    descriptor = None
    for klass in Joueur.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_main_is_not_abstract():
    assert not inspect.isabstract(Main)


def test_main_constructor_exists():
    assert callable(Main.__init__)


def test_main_constructor_args():
    sig = inspect.signature(Main.__init__)
    params = list(sig.parameters.keys())
    assert "bet" in params, "Missing parameter 'bet'"
    assert "value" in params, "Missing parameter 'value'"
    assert "cartes" in params, "Missing parameter 'cartes'"

def test_main_has_bet():
    assert hasattr(Main, "bet")
    descriptor = None
    for klass in Main.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)

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



def test_carte_is_not_abstract():
    assert not inspect.isabstract(Carte)


def test_carte_constructor_exists():
    assert callable(Carte.__init__)


def test_carte_constructor_args():
    sig = inspect.signature(Carte.__init__)
    params = list(sig.parameters.keys())
    assert "ordre" in params, "Missing parameter 'ordre'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_carte_has_ordre():
    assert hasattr(Carte, "ordre")
    descriptor = None
    for klass in Carte.__mro__:
        if "ordre" in klass.__dict__:
            descriptor = klass.__dict__["ordre"]
            break
    assert isinstance(descriptor, property)

def test_carte_has_suit():
    assert hasattr(Carte, "suit")
    descriptor = None
    for klass in Carte.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
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
Blackjack_strategy = st.builds(
    Blackjack,
    joueurs=
        safe_text,
    croupier=
        st.none()
)
Joueur_strategy = st.builds(
    Joueur,
    playerbank=
        st.integers(),
    nom=
        safe_text,
    main=
        safe_text
)
Main_strategy = st.builds(
    Main,
    bet=
        safe_text,
    value=
        st.integers(),
    cartes=
        safe_text
)
Croupier_strategy = st.builds(
    Croupier,
    main=
        safe_text
)
Carte_strategy = st.builds(
    Carte,
    ordre=
        safe_text,
    suit=
        st.integers()
)

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

@given(instance=Joueur_strategy)
@settings(max_examples=50)
def test_joueur_instantiation(instance):
    assert isinstance(instance, Joueur)



@given(instance=Joueur_strategy)
def test_joueur_playerbank_setter(instance):
    original = instance.playerbank
    instance.playerbank = original
    assert instance.playerbank == original



@given(instance=Joueur_strategy)
def test_joueur_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Joueur_strategy)
def test_joueur_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=Main_strategy)
@settings(max_examples=50)
def test_main_instantiation(instance):
    assert isinstance(instance, Main)



@given(instance=Main_strategy)
def test_main_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original



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

@given(instance=Croupier_strategy)
@settings(max_examples=50)
def test_croupier_instantiation(instance):
    assert isinstance(instance, Croupier)



@given(instance=Croupier_strategy)
def test_croupier_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=Carte_strategy)
@settings(max_examples=50)
def test_carte_instantiation(instance):
    assert isinstance(instance, Carte)



@given(instance=Carte_strategy)
def test_carte_ordre_setter(instance):
    original = instance.ordre
    instance.ordre = original
    assert instance.ordre == original



@given(instance=Carte_strategy)
def test_carte_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original
