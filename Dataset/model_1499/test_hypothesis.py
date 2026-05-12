import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNet_ReseauPetri,
    PetriNet_PetriElement,
    PetriNet_Arc,
    PetriElement,
    PetriNet_Transition,
    PetriNet_Place,
    ArcType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_petrinet_petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriElement)


def test_petrinet_petrielement_constructor_exists():
    assert callable(PetriNet_PetriElement.__init__)


def test_petrinet_petrielement_constructor_args():
    sig = inspect.signature(PetriNet_PetriElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrielement_has_name():
    assert hasattr(PetriNet_PetriElement, "name")
    descriptor = None
    for klass in PetriNet_PetriElement.__mro__:
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
    assert "type" in params, "Missing parameter 'type'"

def test_petrinet_arc_has_poids():
    assert hasattr(PetriNet_Arc, "poids")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "poids" in klass.__dict__:
            descriptor = klass.__dict__["poids"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_type():
    assert hasattr(PetriNet_Arc, "type")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
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



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "borne" in params, "Missing parameter 'borne'"
    assert "nbJeton" in params, "Missing parameter 'nbJeton'"

def test_petrinet_place_has_borne():
    assert hasattr(PetriNet_Place, "borne")
    descriptor = None
    for klass in PetriNet_Place.__mro__:
        if "borne" in klass.__dict__:
            descriptor = klass.__dict__["borne"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_place_has_nbJeton():
    assert hasattr(PetriNet_Place, "nbJeton")
    descriptor = None
    for klass in PetriNet_Place.__mro__:
        if "nbJeton" in klass.__dict__:
            descriptor = klass.__dict__["nbJeton"]
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
PetriNet_ReseauPetri_strategy = st.builds(
    PetriNet_ReseauPetri,
    name=
        safe_text
)
PetriNet_PetriElement_strategy = st.builds(
    PetriNet_PetriElement,
    name=
        safe_text
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    poids=
        safe_text,
    type=
        safe_text
)
PetriElement_strategy = st.builds(
    PetriElement,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
    borne=
        safe_text,
    nbJeton=
        safe_text
)

@given(instance=PetriNet_ReseauPetri_strategy)
@settings(max_examples=50)
def test_petrinet_reseaupetri_instantiation(instance):
    assert isinstance(instance, PetriNet_ReseauPetri)



@given(instance=PetriNet_ReseauPetri_strategy)
def test_petrinet_reseaupetri_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_PetriElement_strategy)
@settings(max_examples=50)
def test_petrinet_petrielement_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriElement)



@given(instance=PetriNet_PetriElement_strategy)
def test_petrinet_petrielement_name_setter(instance):
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
def test_petrinet_arc_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PetriElement_strategy)
@settings(max_examples=50)
def test_petrielement_instantiation(instance):
    assert isinstance(instance, PetriElement)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)



@given(instance=PetriNet_Place_strategy)
def test_petrinet_place_borne_setter(instance):
    original = instance.borne
    instance.borne = original
    assert instance.borne == original



@given(instance=PetriNet_Place_strategy)
def test_petrinet_place_nbJeton_setter(instance):
    original = instance.nbJeton
    instance.nbJeton = original
    assert instance.nbJeton == original
