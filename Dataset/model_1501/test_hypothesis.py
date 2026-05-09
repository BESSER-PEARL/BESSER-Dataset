import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNetElt,
    petriNet::Arc,
    petriNet::Noeud,
    Noeud,
    petriNet::Transition,
    petriNet::Place,
    petriNet::PetriNet,
    petriNet::PetriNetElt,
    TypeArc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetelt_is_not_abstract():
    assert not inspect.isabstract(PetriNetElt)


def test_petrinetelt_constructor_exists():
    assert callable(PetriNetElt.__init__)


def test_petrinetelt_constructor_args():
    sig = inspect.signature(PetriNetElt.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "poids" in params, "Missing parameter 'poids'"
    assert "typeArc" in params, "Missing parameter 'typeArc'"

def test_petrinet::arc_has_poids():
    assert hasattr(petriNet::Arc, "poids")
    descriptor = None
    for klass in petriNet::Arc.__mro__:
        if "poids" in klass.__dict__:
            descriptor = klass.__dict__["poids"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_typeArc():
    assert hasattr(petriNet::Arc, "typeArc")
    descriptor = None
    for klass in petriNet::Arc.__mro__:
        if "typeArc" in klass.__dict__:
            descriptor = klass.__dict__["typeArc"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::noeud_is_not_abstract():
    assert not inspect.isabstract(petriNet::Noeud)


def test_petrinet::noeud_constructor_exists():
    assert callable(petriNet::Noeud.__init__)


def test_petrinet::noeud_constructor_args():
    sig = inspect.signature(petriNet::Noeud.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::noeud_has_name():
    assert hasattr(petriNet::Noeud, "name")
    descriptor = None
    for klass in petriNet::Noeud.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_noeud_is_not_abstract():
    assert not inspect.isabstract(Noeud)


def test_noeud_constructor_exists():
    assert callable(Noeud.__init__)


def test_noeud_constructor_args():
    sig = inspect.signature(Noeud.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "jeton" in params, "Missing parameter 'jeton'"

def test_petrinet::place_has_jeton():
    assert hasattr(petriNet::Place, "jeton")
    descriptor = None
    for klass in petriNet::Place.__mro__:
        if "jeton" in klass.__dict__:
            descriptor = klass.__dict__["jeton"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(petriNet::PetriNet, "name")
    descriptor = None
    for klass in petriNet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinetelt_is_not_abstract():
    assert not inspect.isabstract(petriNet::PetriNetElt)


def test_petrinet::petrinetelt_constructor_exists():
    assert callable(petriNet::PetriNetElt.__init__)


def test_petrinet::petrinetelt_constructor_args():
    sig = inspect.signature(petriNet::PetriNetElt.__init__)
    params = list(sig.parameters.keys())

def test_typearc_exists():
    # Check that the Enumeration exists
    assert TypeArc is not None

def test_typearc_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeArc]
    expected_literals = [
        "ArcSimple",
        "ReadArc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeArc"


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
PetriNetElt_strategy = st.builds(
    PetriNetElt,
)
petriNet::Arc_strategy = st.builds(
    petriNet::Arc,
    poids=
        st.integers(),
    typeArc=
        safe_text
)
petriNet::Noeud_strategy = st.builds(
    petriNet::Noeud,
    name=
        safe_text
)
Noeud_strategy = st.builds(
    Noeud,
)
petriNet::Transition_strategy = st.builds(
    petriNet::Transition,
)
petriNet::Place_strategy = st.builds(
    petriNet::Place,
    jeton=
        st.integers()
)
petriNet::PetriNet_strategy = st.builds(
    petriNet::PetriNet,
    name=
        safe_text
)
petriNet::PetriNetElt_strategy = st.builds(
    petriNet::PetriNetElt,
)

@given(instance=PetriNetElt_strategy)
@settings(max_examples=50)
def test_petrinetelt_instantiation(instance):
    assert isinstance(instance, PetriNetElt)

@given(instance=petriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petriNet::Arc)

@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_poids_type(instance):
    assert isinstance(instance.poids, int)


@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_poids_setter(instance):
    original = instance.poids
    instance.poids = original
    assert instance.poids == original

@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_typeArc_type(instance):
    assert isinstance(instance.typeArc, str)


@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_typeArc_setter(instance):
    original = instance.typeArc
    instance.typeArc = original
    assert instance.typeArc == original

@given(instance=petriNet::Noeud_strategy)
@settings(max_examples=50)
def test_petrinet::noeud_instantiation(instance):
    assert isinstance(instance, petriNet::Noeud)

@given(instance=petriNet::Noeud_strategy)
def test_petrinet::noeud_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::Noeud_strategy)
def test_petrinet::noeud_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Noeud_strategy)
@settings(max_examples=50)
def test_noeud_instantiation(instance):
    assert isinstance(instance, Noeud)

@given(instance=petriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petriNet::Transition)

@given(instance=petriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petriNet::Place)

@given(instance=petriNet::Place_strategy)
def test_petrinet::place_jeton_type(instance):
    assert isinstance(instance.jeton, int)


@given(instance=petriNet::Place_strategy)
def test_petrinet::place_jeton_setter(instance):
    original = instance.jeton
    instance.jeton = original
    assert instance.jeton == original

@given(instance=petriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petriNet::PetriNet)

@given(instance=petriNet::PetriNet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::PetriNet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet::PetriNetElt_strategy)
@settings(max_examples=50)
def test_petrinet::petrinetelt_instantiation(instance):
    assert isinstance(instance, petriNet::PetriNetElt)
