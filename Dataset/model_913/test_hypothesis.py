import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriElement,
    PetriNet_Noeud,
    PetriNet_Arc,
    Noeud,
    PetriNet_Place,
    PetriNet_PetriElement,
    PetriNet_ReseauPetri,
    PetriNet_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriElement)


def test_petrielement_constructor_exists():
    assert callable(PetriElement.__init__)


def test_petrielement_constructor_args():
    sig = inspect.signature(PetriElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_noeud_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Noeud)


def test_petrinet_noeud_constructor_exists():
    assert callable(PetriNet_Noeud.__init__)


def test_petrinet_noeud_constructor_args():
    sig = inspect.signature(PetriNet_Noeud.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_noeud_has_name():
    assert hasattr(PetriNet_Noeud, "name")
    descriptor = None
    for klass in PetriNet_Noeud.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "poids" in params, "Missing parameter 'poids'"
    assert "isReadArc" in params, "Missing parameter 'isReadArc'"

def test_petrinet_arc_has_poids():
    assert hasattr(PetriNet_Arc, "poids")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "poids" in klass.__dict__:
            descriptor = klass.__dict__["poids"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_isReadArc():
    assert hasattr(PetriNet_Arc, "isReadArc")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "isReadArc" in klass.__dict__:
            descriptor = klass.__dict__["isReadArc"]
            break
    assert isinstance(descriptor, property)



def test_noeud_is_not_abstract():
    assert not inspect.isabstract(Noeud)


def test_noeud_constructor_exists():
    assert callable(Noeud.__init__)


def test_noeud_constructor_args():
    sig = inspect.signature(Noeud.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "jeton" in params, "Missing parameter 'jeton'"

def test_petrinet_place_has_jeton():
    assert hasattr(PetriNet_Place, "jeton")
    descriptor = None
    for klass in PetriNet_Place.__mro__:
        if "jeton" in klass.__dict__:
            descriptor = klass.__dict__["jeton"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriElement)


def test_petrinet_petrielement_constructor_exists():
    assert callable(PetriNet_PetriElement.__init__)


def test_petrinet_petrielement_constructor_args():
    sig = inspect.signature(PetriNet_PetriElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_reseaupetri_is_not_abstract():
    assert not inspect.isabstract(PetriNet_ReseauPetri)


def test_petrinet_reseaupetri_constructor_exists():
    assert callable(PetriNet_ReseauPetri.__init__)


def test_petrinet_reseaupetri_constructor_args():
    sig = inspect.signature(PetriNet_ReseauPetri.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_reseaupetri_has_name():
    assert hasattr(PetriNet_ReseauPetri, "name")
    descriptor = None
    for klass in PetriNet_ReseauPetri.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
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
PetriElement_strategy = st.builds(
    PetriElement,
)
PetriNet_Noeud_strategy = st.builds(
    PetriNet_Noeud,
    name=
        safe_text
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    poids=
        st.integers(),
    isReadArc=
        st.booleans()
)
Noeud_strategy = st.builds(
    Noeud,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
    jeton=
        st.integers()
)
PetriNet_PetriElement_strategy = st.builds(
    PetriNet_PetriElement,
)
PetriNet_ReseauPetri_strategy = st.builds(
    PetriNet_ReseauPetri,
    name=
        safe_text
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)

@given(instance=PetriElement_strategy)
@settings(max_examples=50)
def test_petrielement_instantiation(instance):
    assert isinstance(instance, PetriElement)

@given(instance=PetriNet_Noeud_strategy)
@settings(max_examples=50)
def test_petrinet_noeud_instantiation(instance):
    assert isinstance(instance, PetriNet_Noeud)



@given(instance=PetriNet_Noeud_strategy)
def test_petrinet_noeud_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_poids_setter(instance):
    original = instance.poids
    instance.poids = original
    assert instance.poids == original



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_isReadArc_setter(instance):
    original = instance.isReadArc
    instance.isReadArc = original
    assert instance.isReadArc == original

@given(instance=Noeud_strategy)
@settings(max_examples=50)
def test_noeud_instantiation(instance):
    assert isinstance(instance, Noeud)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)



@given(instance=PetriNet_Place_strategy)
def test_petrinet_place_jeton_setter(instance):
    original = instance.jeton
    instance.jeton = original
    assert instance.jeton == original

@given(instance=PetriNet_PetriElement_strategy)
@settings(max_examples=50)
def test_petrinet_petrielement_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriElement)

@given(instance=PetriNet_ReseauPetri_strategy)
@settings(max_examples=50)
def test_petrinet_reseaupetri_instantiation(instance):
    assert isinstance(instance, PetriNet_ReseauPetri)



@given(instance=PetriNet_ReseauPetri_strategy)
def test_petrinet_reseaupetri_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)
