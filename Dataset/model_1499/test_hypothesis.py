import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNet::ReseauPetri,
    PetriNet::PetriElement,
    PetriNet::Arc,
    PetriElement,
    PetriNet::Transition,
    PetriNet::Place,
    ArcType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_petrinet::petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriElement)


def test_petrinet::petrielement_constructor_exists():
    assert callable(PetriNet::PetriElement.__init__)


def test_petrinet::petrielement_constructor_args():
    sig = inspect.signature(PetriNet::PetriElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrielement_has_name():
    assert hasattr(PetriNet::PetriElement, "name")
    descriptor = None
    for klass in PetriNet::PetriElement.__mro__:
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
    assert "type" in params, "Missing parameter 'type'"

def test_petrinet::arc_has_poids():
    assert hasattr(PetriNet::Arc, "poids")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "poids" in klass.__dict__:
            descriptor = klass.__dict__["poids"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_type():
    assert hasattr(PetriNet::Arc, "type")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriElement)


def test_petrielement_constructor_exists():
    assert callable(PetriElement.__init__)


def test_petrielement_constructor_args():
    sig = inspect.signature(PetriElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "nbJeton" in params, "Missing parameter 'nbJeton'"
    assert "borne" in params, "Missing parameter 'borne'"

def test_petrinet::place_has_nbJeton():
    assert hasattr(PetriNet::Place, "nbJeton")
    descriptor = None
    for klass in PetriNet::Place.__mro__:
        if "nbJeton" in klass.__dict__:
            descriptor = klass.__dict__["nbJeton"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::place_has_borne():
    assert hasattr(PetriNet::Place, "borne")
    descriptor = None
    for klass in PetriNet::Place.__mro__:
        if "borne" in klass.__dict__:
            descriptor = klass.__dict__["borne"]
            break
    assert isinstance(descriptor, property)

def test_arctype_exists():
    # Check that the Enumeration exists
    assert ArcType is not None

def test_arctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcType]
    expected_literals = [
        "Normal",
        "Read_arc",
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
PetriNet::ReseauPetri_strategy = st.builds(
    PetriNet::ReseauPetri,
    name=
        safe_text
)
PetriNet::PetriElement_strategy = st.builds(
    PetriNet::PetriElement,
    name=
        safe_text
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    poids=
        safe_text,
    type=
        safe_text
)
PetriElement_strategy = st.builds(
    PetriElement,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
    nbJeton=
        safe_text,
    borne=
        safe_text
)

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

@given(instance=PetriNet::PetriElement_strategy)
@settings(max_examples=50)
def test_petrinet::petrielement_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriElement)

@given(instance=PetriNet::PetriElement_strategy)
def test_petrinet::petrielement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::PetriElement_strategy)
def test_petrinet::petrielement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_poids_type(instance):
    assert isinstance(instance.poids, str)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_poids_setter(instance):
    original = instance.poids
    instance.poids = original
    assert instance.poids == original

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PetriElement_strategy)
@settings(max_examples=50)
def test_petrielement_instantiation(instance):
    assert isinstance(instance, PetriElement)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_nbJeton_type(instance):
    assert isinstance(instance.nbJeton, str)


@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_nbJeton_setter(instance):
    original = instance.nbJeton
    instance.nbJeton = original
    assert instance.nbJeton == original

@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_borne_type(instance):
    assert isinstance(instance.borne, str)


@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_borne_setter(instance):
    original = instance.borne
    instance.borne = original
    assert instance.borne == original
