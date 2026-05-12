import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNetElt,
    petriNet_Arc,
    petriNet_Noeud,
    Noeud,
    petriNet_Transition,
    petriNet_Place,
    petriNet_PetriNet,
    petriNet_PetriNetElt,
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



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "poids" in params, "Missing parameter 'poids'"
    assert "typeArc" in params, "Missing parameter 'typeArc'"

def test_petrinet_arc_has_poids():
    assert hasattr(petriNet_Arc, "poids")
    descriptor = None
    for klass in petriNet_Arc.__mro__:
        if "poids" in klass.__dict__:
            descriptor = klass.__dict__["poids"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_typeArc():
    assert hasattr(petriNet_Arc, "typeArc")
    descriptor = None
    for klass in petriNet_Arc.__mro__:
        if "typeArc" in klass.__dict__:
            descriptor = klass.__dict__["typeArc"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_noeud_is_not_abstract():
    assert not inspect.isabstract(petriNet_Noeud)


def test_petrinet_noeud_constructor_exists():
    assert callable(petriNet_Noeud.__init__)


def test_petrinet_noeud_constructor_args():
    sig = inspect.signature(petriNet_Noeud.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_noeud_has_name():
    assert hasattr(petriNet_Noeud, "name")
    descriptor = None
    for klass in petriNet_Noeud.__mro__:
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



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "jeton" in params, "Missing parameter 'jeton'"

def test_petrinet_place_has_jeton():
    assert hasattr(petriNet_Place, "jeton")
    descriptor = None
    for klass in petriNet_Place.__mro__:
        if "jeton" in klass.__dict__:
            descriptor = klass.__dict__["jeton"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrinet_has_name():
    assert hasattr(petriNet_PetriNet, "name")
    descriptor = None
    for klass in petriNet_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinetelt_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriNetElt)


def test_petrinet_petrinetelt_constructor_exists():
    assert callable(petriNet_PetriNetElt.__init__)


def test_petrinet_petrinetelt_constructor_args():
    sig = inspect.signature(petriNet_PetriNetElt.__init__)
    params = list(sig.parameters.keys())

def test_typearc_exists():
    # Check that the Enumeration exists
    assert TypeArc is not None

def test_typearc_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeArc]
    expected_literals = [
        "ReadArc",
        "ArcSimple",
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
petriNet_Arc_strategy = st.builds(
    petriNet_Arc,
    poids=
        st.integers(),
    typeArc=
        safe_text
)
petriNet_Noeud_strategy = st.builds(
    petriNet_Noeud,
    name=
        safe_text
)
Noeud_strategy = st.builds(
    Noeud,
)
petriNet_Transition_strategy = st.builds(
    petriNet_Transition,
)
petriNet_Place_strategy = st.builds(
    petriNet_Place,
    jeton=
        st.integers()
)
petriNet_PetriNet_strategy = st.builds(
    petriNet_PetriNet,
    name=
        safe_text
)
petriNet_PetriNetElt_strategy = st.builds(
    petriNet_PetriNetElt,
)

@given(instance=PetriNetElt_strategy)
@settings(max_examples=50)
def test_petrinetelt_instantiation(instance):
    assert isinstance(instance, PetriNetElt)

@given(instance=petriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petriNet_Arc)



@given(instance=petriNet_Arc_strategy)
def test_petrinet_arc_poids_setter(instance):
    original = instance.poids
    instance.poids = original
    assert instance.poids == original



@given(instance=petriNet_Arc_strategy)
def test_petrinet_arc_typeArc_setter(instance):
    original = instance.typeArc
    instance.typeArc = original
    assert instance.typeArc == original

@given(instance=petriNet_Noeud_strategy)
@settings(max_examples=50)
def test_petrinet_noeud_instantiation(instance):
    assert isinstance(instance, petriNet_Noeud)



@given(instance=petriNet_Noeud_strategy)
def test_petrinet_noeud_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Noeud_strategy)
@settings(max_examples=50)
def test_noeud_instantiation(instance):
    assert isinstance(instance, Noeud)

@given(instance=petriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petriNet_Transition)

@given(instance=petriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petriNet_Place)



@given(instance=petriNet_Place_strategy)
def test_petrinet_place_jeton_setter(instance):
    original = instance.jeton
    instance.jeton = original
    assert instance.jeton == original

@given(instance=petriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petriNet_PetriNet)



@given(instance=petriNet_PetriNet_strategy)
def test_petrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet_PetriNetElt_strategy)
@settings(max_examples=50)
def test_petrinet_petrinetelt_instantiation(instance):
    assert isinstance(instance, petriNet_PetriNetElt)
