import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriElement,
    PetriNet::Noeud,
    PetriNet::Arc,
    Noeud,
    PetriNet::Place,
    PetriNet::PetriElement,
    PetriNet::ReseauPetri,
    PetriNet::Transition,
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



def test_petrinet::noeud_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Noeud)


def test_petrinet::noeud_constructor_exists():
    assert callable(PetriNet::Noeud.__init__)


def test_petrinet::noeud_constructor_args():
    sig = inspect.signature(PetriNet::Noeud.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::noeud_has_name():
    assert hasattr(PetriNet::Noeud, "name")
    descriptor = None
    for klass in PetriNet::Noeud.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(PetriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(PetriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "poids" in params, "Missing parameter 'poids'"
    assert "isReadArc" in params, "Missing parameter 'isReadArc'"

def test_petrinet::arc_has_poids():
    assert hasattr(PetriNet::Arc, "poids")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "poids" in klass.__dict__:
            descriptor = klass.__dict__["poids"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_isReadArc():
    assert hasattr(PetriNet::Arc, "isReadArc")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
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



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "jeton" in params, "Missing parameter 'jeton'"

def test_petrinet::place_has_jeton():
    assert hasattr(PetriNet::Place, "jeton")
    descriptor = None
    for klass in PetriNet::Place.__mro__:
        if "jeton" in klass.__dict__:
            descriptor = klass.__dict__["jeton"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriElement)


def test_petrinet::petrielement_constructor_exists():
    assert callable(PetriNet::PetriElement.__init__)


def test_petrinet::petrielement_constructor_args():
    sig = inspect.signature(PetriNet::PetriElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::reseaupetri_is_not_abstract():
    assert not inspect.isabstract(PetriNet::ReseauPetri)


def test_petrinet::reseaupetri_constructor_exists():
    assert callable(PetriNet::ReseauPetri.__init__)


def test_petrinet::reseaupetri_constructor_args():
    sig = inspect.signature(PetriNet::ReseauPetri.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::reseaupetri_has_name():
    assert hasattr(PetriNet::ReseauPetri, "name")
    descriptor = None
    for klass in PetriNet::ReseauPetri.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
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
PetriNet::Noeud_strategy = st.builds(
    PetriNet::Noeud,
    name=
        safe_text
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    poids=
        st.integers(),
    isReadArc=
        st.booleans()
)
Noeud_strategy = st.builds(
    Noeud,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
    jeton=
        st.integers()
)
PetriNet::PetriElement_strategy = st.builds(
    PetriNet::PetriElement,
)
PetriNet::ReseauPetri_strategy = st.builds(
    PetriNet::ReseauPetri,
    name=
        safe_text
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)

@given(instance=PetriElement_strategy)
@settings(max_examples=50)
def test_petrielement_instantiation(instance):
    assert isinstance(instance, PetriElement)

@given(instance=PetriNet::Noeud_strategy)
@settings(max_examples=50)
def test_petrinet::noeud_instantiation(instance):
    assert isinstance(instance, PetriNet::Noeud)

@given(instance=PetriNet::Noeud_strategy)
def test_petrinet::noeud_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::Noeud_strategy)
def test_petrinet::noeud_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_poids_type(instance):
    assert isinstance(instance.poids, int)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_poids_setter(instance):
    original = instance.poids
    instance.poids = original
    assert instance.poids == original

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_isReadArc_type(instance):
    assert isinstance(instance.isReadArc, bool)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_isReadArc_setter(instance):
    original = instance.isReadArc
    instance.isReadArc = original
    assert instance.isReadArc == original

@given(instance=Noeud_strategy)
@settings(max_examples=50)
def test_noeud_instantiation(instance):
    assert isinstance(instance, Noeud)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_jeton_type(instance):
    assert isinstance(instance.jeton, int)


@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_jeton_setter(instance):
    original = instance.jeton
    instance.jeton = original
    assert instance.jeton == original

@given(instance=PetriNet::PetriElement_strategy)
@settings(max_examples=50)
def test_petrinet::petrielement_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriElement)

@given(instance=PetriNet::ReseauPetri_strategy)
@settings(max_examples=50)
def test_petrinet::reseaupetri_instantiation(instance):
    assert isinstance(instance, PetriNet::ReseauPetri)

@given(instance=PetriNet::ReseauPetri_strategy)
def test_petrinet::reseaupetri_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::ReseauPetri_strategy)
def test_petrinet::reseaupetri_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)
