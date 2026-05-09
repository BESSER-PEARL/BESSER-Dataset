import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNet::PetriNet,
    PetriNet::PetriElement,
    PetriNet::Arc,
    PetriElement,
    PetriNet::Place,
    PetriNet::Transition,
    ArcType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(PetriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(PetriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(PetriNet::PetriNet, "name")
    descriptor = None
    for klass in PetriNet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriElement)


def test_petrinet::petrielement_constructor_exists():
    assert callable(PetriNet::PetriElement.__init__)


def test_petrinet::petrielement_constructor_args():
    sig = inspect.signature(PetriNet::PetriElement.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_petrinet::petrielement_has_nom():
    assert hasattr(PetriNet::PetriElement, "nom")
    descriptor = None
    for klass in PetriNet::PetriElement.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
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
    assert "arcType" in params, "Missing parameter 'arcType'"

def test_petrinet::arc_has_poids():
    assert hasattr(PetriNet::Arc, "poids")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "poids" in klass.__dict__:
            descriptor = klass.__dict__["poids"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_arcType():
    assert hasattr(PetriNet::Arc, "arcType")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "arcType" in klass.__dict__:
            descriptor = klass.__dict__["arcType"]
            break
    assert isinstance(descriptor, property)



def test_petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriElement)


def test_petrielement_constructor_exists():
    assert callable(PetriElement.__init__)


def test_petrielement_constructor_args():
    sig = inspect.signature(PetriElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "nbJetons" in params, "Missing parameter 'nbJetons'"

def test_petrinet::place_has_nbJetons():
    assert hasattr(PetriNet::Place, "nbJetons")
    descriptor = None
    for klass in PetriNet::Place.__mro__:
        if "nbJetons" in klass.__dict__:
            descriptor = klass.__dict__["nbJetons"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())

def test_arctype_exists():
    # Check that the Enumeration exists
    assert ArcType is not None

def test_arctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcType]
    expected_literals = [
        "Arc",
        "ReadArc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArcType"


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
PetriNet::PetriNet_strategy = st.builds(
    PetriNet::PetriNet,
    name=
        safe_text
)
PetriNet::PetriElement_strategy = st.builds(
    PetriNet::PetriElement,
    nom=
        safe_text
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    poids=
        st.integers(),
    arcType=
        safe_text
)
PetriElement_strategy = st.builds(
    PetriElement,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
    nbJetons=
        st.integers()
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)

@given(instance=PetriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriNet)

@given(instance=PetriNet::PetriNet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::PetriNet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::PetriElement_strategy)
@settings(max_examples=50)
def test_petrinet::petrielement_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriElement)

@given(instance=PetriNet::PetriElement_strategy)
def test_petrinet::petrielement_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=PetriNet::PetriElement_strategy)
def test_petrinet::petrielement_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

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
def test_petrinet::arc_arcType_type(instance):
    assert isinstance(instance.arcType, str)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_arcType_setter(instance):
    original = instance.arcType
    instance.arcType = original
    assert instance.arcType == original

@given(instance=PetriElement_strategy)
@settings(max_examples=50)
def test_petrielement_instantiation(instance):
    assert isinstance(instance, PetriElement)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_nbJetons_type(instance):
    assert isinstance(instance.nbJetons, int)


@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_nbJetons_setter(instance):
    original = instance.nbJetons
    instance.nbJetons = original
    assert instance.nbJetons == original

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)
