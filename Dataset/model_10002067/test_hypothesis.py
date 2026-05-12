import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Controleur,
    Vue,
    Obsever_Interface,
    Cellule,
    Joueur,
    Wagon,
    Observable,
    ModelTraint,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_controleur_is_not_abstract():
    assert not inspect.isabstract(Controleur)


def test_controleur_constructor_exists():
    assert callable(Controleur.__init__)


def test_controleur_constructor_args():
    sig = inspect.signature(Controleur.__init__)
    params = list(sig.parameters.keys())
    assert "vue" in params, "Missing parameter 'vue'"
    assert "modeletrain" in params, "Missing parameter 'modeletrain'"

def test_controleur_has_vue():
    assert hasattr(Controleur, "vue")
    descriptor = None
    for klass in Controleur.__mro__:
        if "vue" in klass.__dict__:
            descriptor = klass.__dict__["vue"]
            break
    assert isinstance(descriptor, property)

def test_controleur_has_modeletrain():
    assert hasattr(Controleur, "modeletrain")
    descriptor = None
    for klass in Controleur.__mro__:
        if "modeletrain" in klass.__dict__:
            descriptor = klass.__dict__["modeletrain"]
            break
    assert isinstance(descriptor, property)



def test_vue_is_not_abstract():
    assert not inspect.isabstract(Vue)


def test_vue_constructor_exists():
    assert callable(Vue.__init__)


def test_vue_constructor_args():
    sig = inspect.signature(Vue.__init__)
    params = list(sig.parameters.keys())
    assert "modeltrain" in params, "Missing parameter 'modeltrain'"

def test_vue_has_modeltrain():
    assert hasattr(Vue, "modeltrain")
    descriptor = None
    for klass in Vue.__mro__:
        if "modeltrain" in klass.__dict__:
            descriptor = klass.__dict__["modeltrain"]
            break
    assert isinstance(descriptor, property)



def test_obsever_interface_is_not_abstract():
    assert not inspect.isabstract(Obsever_Interface)


def test_obsever_interface_constructor_exists():
    assert callable(Obsever_Interface.__init__)


def test_obsever_interface_constructor_args():
    sig = inspect.signature(Obsever_Interface.__init__)
    params = list(sig.parameters.keys())



def test_cellule_is_not_abstract():
    assert not inspect.isabstract(Cellule)


def test_cellule_constructor_exists():
    assert callable(Cellule.__init__)


def test_cellule_constructor_args():
    sig = inspect.signature(Cellule.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"

def test_cellule_has_model():
    assert hasattr(Cellule, "model")
    descriptor = None
    for klass in Cellule.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_joueur_is_not_abstract():
    assert not inspect.isabstract(Joueur)


def test_joueur_constructor_exists():
    assert callable(Joueur.__init__)


def test_joueur_constructor_args():
    sig = inspect.signature(Joueur.__init__)
    params = list(sig.parameters.keys())
    assert "a_b" in params, "Missing parameter 'a_b'"
    assert "model" in params, "Missing parameter 'model'"
    assert "x_y" in params, "Missing parameter 'x_y'"
    assert "nomJoueur" in params, "Missing parameter 'nomJoueur'"
    assert "wagon" in params, "Missing parameter 'wagon'"

def test_joueur_has_a_b():
    assert hasattr(Joueur, "a_b")
    descriptor = None
    for klass in Joueur.__mro__:
        if "a_b" in klass.__dict__:
            descriptor = klass.__dict__["a_b"]
            break
    assert isinstance(descriptor, property)

def test_joueur_has_model():
    assert hasattr(Joueur, "model")
    descriptor = None
    for klass in Joueur.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)

def test_joueur_has_x_y():
    assert hasattr(Joueur, "x_y")
    descriptor = None
    for klass in Joueur.__mro__:
        if "x_y" in klass.__dict__:
            descriptor = klass.__dict__["x_y"]
            break
    assert isinstance(descriptor, property)

def test_joueur_has_nomJoueur():
    assert hasattr(Joueur, "nomJoueur")
    descriptor = None
    for klass in Joueur.__mro__:
        if "nomJoueur" in klass.__dict__:
            descriptor = klass.__dict__["nomJoueur"]
            break
    assert isinstance(descriptor, property)

def test_joueur_has_wagon():
    assert hasattr(Joueur, "wagon")
    descriptor = None
    for klass in Joueur.__mro__:
        if "wagon" in klass.__dict__:
            descriptor = klass.__dict__["wagon"]
            break
    assert isinstance(descriptor, property)



def test_wagon_is_not_abstract():
    assert not inspect.isabstract(Wagon)


def test_wagon_constructor_exists():
    assert callable(Wagon.__init__)


def test_wagon_constructor_args():
    sig = inspect.signature(Wagon.__init__)
    params = list(sig.parameters.keys())
    assert "numeroWagon" in params, "Missing parameter 'numeroWagon'"
    assert "isInWagon" in params, "Missing parameter 'isInWagon'"
    assert "modele" in params, "Missing parameter 'modele'"

def test_wagon_has_numeroWagon():
    assert hasattr(Wagon, "numeroWagon")
    descriptor = None
    for klass in Wagon.__mro__:
        if "numeroWagon" in klass.__dict__:
            descriptor = klass.__dict__["numeroWagon"]
            break
    assert isinstance(descriptor, property)

def test_wagon_has_isInWagon():
    assert hasattr(Wagon, "isInWagon")
    descriptor = None
    for klass in Wagon.__mro__:
        if "isInWagon" in klass.__dict__:
            descriptor = klass.__dict__["isInWagon"]
            break
    assert isinstance(descriptor, property)

def test_wagon_has_modele():
    assert hasattr(Wagon, "modele")
    descriptor = None
    for klass in Wagon.__mro__:
        if "modele" in klass.__dict__:
            descriptor = klass.__dict__["modele"]
            break
    assert isinstance(descriptor, property)



def test_observable_is_not_abstract():
    assert not inspect.isabstract(Observable)


def test_observable_constructor_exists():
    assert callable(Observable.__init__)


def test_observable_constructor_args():
    sig = inspect.signature(Observable.__init__)
    params = list(sig.parameters.keys())
    assert "listObservers__" in params, "Missing parameter 'listObservers__'"

def test_observable_has_listObservers__():
    assert hasattr(Observable, "listObservers__")
    descriptor = None
    for klass in Observable.__mro__:
        if "listObservers__" in klass.__dict__:
            descriptor = klass.__dict__["listObservers__"]
            break
    assert isinstance(descriptor, property)



def test_modeltraint_is_not_abstract():
    assert not inspect.isabstract(ModelTraint)


def test_modeltraint_constructor_exists():
    assert callable(ModelTraint.__init__)


def test_modeltraint_constructor_args():
    sig = inspect.signature(ModelTraint.__init__)
    params = list(sig.parameters.keys())
    assert "listeWagon__" in params, "Missing parameter 'listeWagon__'"
    assert "indiceWagonCourant" in params, "Missing parameter 'indiceWagonCourant'"
    assert "joueurs__" in params, "Missing parameter 'joueurs__'"
    assert "cellule____" in params, "Missing parameter 'cellule____'"
    assert "indiceJoueurCourant" in params, "Missing parameter 'indiceJoueurCourant'"

def test_modeltraint_has_listeWagon__():
    assert hasattr(ModelTraint, "listeWagon__")
    descriptor = None
    for klass in ModelTraint.__mro__:
        if "listeWagon__" in klass.__dict__:
            descriptor = klass.__dict__["listeWagon__"]
            break
    assert isinstance(descriptor, property)

def test_modeltraint_has_indiceWagonCourant():
    assert hasattr(ModelTraint, "indiceWagonCourant")
    descriptor = None
    for klass in ModelTraint.__mro__:
        if "indiceWagonCourant" in klass.__dict__:
            descriptor = klass.__dict__["indiceWagonCourant"]
            break
    assert isinstance(descriptor, property)

def test_modeltraint_has_joueurs__():
    assert hasattr(ModelTraint, "joueurs__")
    descriptor = None
    for klass in ModelTraint.__mro__:
        if "joueurs__" in klass.__dict__:
            descriptor = klass.__dict__["joueurs__"]
            break
    assert isinstance(descriptor, property)

def test_modeltraint_has_cellule____():
    assert hasattr(ModelTraint, "cellule____")
    descriptor = None
    for klass in ModelTraint.__mro__:
        if "cellule____" in klass.__dict__:
            descriptor = klass.__dict__["cellule____"]
            break
    assert isinstance(descriptor, property)

def test_modeltraint_has_indiceJoueurCourant():
    assert hasattr(ModelTraint, "indiceJoueurCourant")
    descriptor = None
    for klass in ModelTraint.__mro__:
        if "indiceJoueurCourant" in klass.__dict__:
            descriptor = klass.__dict__["indiceJoueurCourant"]
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
Controleur_strategy = st.builds(
    Controleur,
    vue=
        st.none(),
    modeletrain=
        st.none()
)
Vue_strategy = st.builds(
    Vue,
    modeltrain=
        st.none()
)
Obsever_Interface_strategy = st.builds(
    Obsever_Interface,
)
Cellule_strategy = st.builds(
    Cellule,
    model=
        st.none()
)
Joueur_strategy = st.builds(
    Joueur,
    a_b=
        st.integers(),
    model=
        st.none(),
    x_y=
        st.integers(),
    nomJoueur=
        safe_text,
    wagon=
        st.none()
)
Wagon_strategy = st.builds(
    Wagon,
    numeroWagon=
        st.integers(),
    isInWagon=
        st.booleans(),
    modele=
        st.none()
)
Observable_strategy = st.builds(
    Observable,
    listObservers__=
        safe_text
)
ModelTraint_strategy = st.builds(
    ModelTraint,
    listeWagon__=
        st.none(),
    indiceWagonCourant=
        st.integers(),
    joueurs__=
        st.none(),
    cellule____=
        st.none(),
    indiceJoueurCourant=
        st.integers()
)

@given(instance=Controleur_strategy)
@settings(max_examples=50)
def test_controleur_instantiation(instance):
    assert isinstance(instance, Controleur)



@given(instance=Controleur_strategy)
def test_controleur_vue_setter(instance):
    original = instance.vue
    instance.vue = original
    assert instance.vue == original



@given(instance=Controleur_strategy)
def test_controleur_modeletrain_setter(instance):
    original = instance.modeletrain
    instance.modeletrain = original
    assert instance.modeletrain == original

@given(instance=Vue_strategy)
@settings(max_examples=50)
def test_vue_instantiation(instance):
    assert isinstance(instance, Vue)



@given(instance=Vue_strategy)
def test_vue_modeltrain_setter(instance):
    original = instance.modeltrain
    instance.modeltrain = original
    assert instance.modeltrain == original

@given(instance=Obsever_Interface_strategy)
@settings(max_examples=50)
def test_obsever_interface_instantiation(instance):
    assert isinstance(instance, Obsever_Interface)

@given(instance=Cellule_strategy)
@settings(max_examples=50)
def test_cellule_instantiation(instance):
    assert isinstance(instance, Cellule)



@given(instance=Cellule_strategy)
def test_cellule_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=Joueur_strategy)
@settings(max_examples=50)
def test_joueur_instantiation(instance):
    assert isinstance(instance, Joueur)



@given(instance=Joueur_strategy)
def test_joueur_a_b_setter(instance):
    original = instance.a_b
    instance.a_b = original
    assert instance.a_b == original



@given(instance=Joueur_strategy)
def test_joueur_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=Joueur_strategy)
def test_joueur_x_y_setter(instance):
    original = instance.x_y
    instance.x_y = original
    assert instance.x_y == original



@given(instance=Joueur_strategy)
def test_joueur_nomJoueur_setter(instance):
    original = instance.nomJoueur
    instance.nomJoueur = original
    assert instance.nomJoueur == original



@given(instance=Joueur_strategy)
def test_joueur_wagon_setter(instance):
    original = instance.wagon
    instance.wagon = original
    assert instance.wagon == original

@given(instance=Wagon_strategy)
@settings(max_examples=50)
def test_wagon_instantiation(instance):
    assert isinstance(instance, Wagon)



@given(instance=Wagon_strategy)
def test_wagon_numeroWagon_setter(instance):
    original = instance.numeroWagon
    instance.numeroWagon = original
    assert instance.numeroWagon == original



@given(instance=Wagon_strategy)
def test_wagon_isInWagon_setter(instance):
    original = instance.isInWagon
    instance.isInWagon = original
    assert instance.isInWagon == original



@given(instance=Wagon_strategy)
def test_wagon_modele_setter(instance):
    original = instance.modele
    instance.modele = original
    assert instance.modele == original

@given(instance=Observable_strategy)
@settings(max_examples=50)
def test_observable_instantiation(instance):
    assert isinstance(instance, Observable)



@given(instance=Observable_strategy)
def test_observable_listObservers___setter(instance):
    original = instance.listObservers__
    instance.listObservers__ = original
    assert instance.listObservers__ == original

@given(instance=ModelTraint_strategy)
@settings(max_examples=50)
def test_modeltraint_instantiation(instance):
    assert isinstance(instance, ModelTraint)



@given(instance=ModelTraint_strategy)
def test_modeltraint_listeWagon___setter(instance):
    original = instance.listeWagon__
    instance.listeWagon__ = original
    assert instance.listeWagon__ == original



@given(instance=ModelTraint_strategy)
def test_modeltraint_indiceWagonCourant_setter(instance):
    original = instance.indiceWagonCourant
    instance.indiceWagonCourant = original
    assert instance.indiceWagonCourant == original



@given(instance=ModelTraint_strategy)
def test_modeltraint_joueurs___setter(instance):
    original = instance.joueurs__
    instance.joueurs__ = original
    assert instance.joueurs__ == original



@given(instance=ModelTraint_strategy)
def test_modeltraint_cellule_____setter(instance):
    original = instance.cellule____
    instance.cellule____ = original
    assert instance.cellule____ == original



@given(instance=ModelTraint_strategy)
def test_modeltraint_indiceJoueurCourant_setter(instance):
    original = instance.indiceJoueurCourant
    instance.indiceJoueurCourant = original
    assert instance.indiceJoueurCourant == original
