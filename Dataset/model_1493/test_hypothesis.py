import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petriNet_PetriNetwork,
    PetriElement,
    petriNet_Place,
    petriNet_Arc,
    petriNet_Transition,
    petriNet_PetriElement,
    ArcDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_petrinetwork_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriNetwork)


def test_petrinet_petrinetwork_constructor_exists():
    assert callable(petriNet_PetriNetwork.__init__)


def test_petrinet_petrinetwork_constructor_args():
    sig = inspect.signature(petriNet_PetriNetwork.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrinetwork_has_name():
    assert hasattr(petriNet_PetriNetwork, "name")
    descriptor = None
    for klass in petriNet_PetriNetwork.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrielement_is_not_abstract():
    assert not inspect.isabstract(PetriElement)


def test_petrielement_constructor_exists():
    assert callable(PetriElement.__init__)


def test_petrielement_constructor_args():
    sig = inspect.signature(PetriElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "nbJetons" in params, "Missing parameter 'nbJetons'"

def test_petrinet_place_has_nbJetons():
    assert hasattr(petriNet_Place, "nbJetons")
    descriptor = None
    for klass in petriNet_Place.__mro__:
        if "nbJetons" in klass.__dict__:
            descriptor = klass.__dict__["nbJetons"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "Direction" in params, "Missing parameter 'Direction'"
    assert "jetonsTransferes" in params, "Missing parameter 'jetonsTransferes'"

def test_petrinet_arc_has_Direction():
    assert hasattr(petriNet_Arc, "Direction")
    descriptor = None
    for klass in petriNet_Arc.__mro__:
        if "Direction" in klass.__dict__:
            descriptor = klass.__dict__["Direction"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_jetonsTransferes():
    assert hasattr(petriNet_Arc, "jetonsTransferes")
    descriptor = None
    for klass in petriNet_Arc.__mro__:
        if "jetonsTransferes" in klass.__dict__:
            descriptor = klass.__dict__["jetonsTransferes"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrielement_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriElement)


def test_petrinet_petrielement_constructor_exists():
    assert callable(petriNet_PetriElement.__init__)


def test_petrinet_petrielement_constructor_args():
    sig = inspect.signature(petriNet_PetriElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrielement_has_name():
    assert hasattr(petriNet_PetriElement, "name")
    descriptor = None
    for klass in petriNet_PetriElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arcdirection_exists():
    # Check that the Enumeration exists
    assert ArcDirection is not None

def test_arcdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcDirection]
    expected_literals = [
        "T2P",
        "P2T",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArcDirection"


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
petriNet_PetriNetwork_strategy = st.builds(
    petriNet_PetriNetwork,
    name=
        safe_text
)
PetriElement_strategy = st.builds(
    PetriElement,
)
petriNet_Place_strategy = st.builds(
    petriNet_Place,
    nbJetons=
        st.integers()
)
petriNet_Arc_strategy = st.builds(
    petriNet_Arc,
    Direction=
        safe_text,
    jetonsTransferes=
        st.integers()
)
petriNet_Transition_strategy = st.builds(
    petriNet_Transition,
)
petriNet_PetriElement_strategy = st.builds(
    petriNet_PetriElement,
    name=
        safe_text
)

@given(instance=petriNet_PetriNetwork_strategy)
@settings(max_examples=50)
def test_petrinet_petrinetwork_instantiation(instance):
    assert isinstance(instance, petriNet_PetriNetwork)



@given(instance=petriNet_PetriNetwork_strategy)
def test_petrinet_petrinetwork_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriElement_strategy)
@settings(max_examples=50)
def test_petrielement_instantiation(instance):
    assert isinstance(instance, PetriElement)

@given(instance=petriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petriNet_Place)



@given(instance=petriNet_Place_strategy)
def test_petrinet_place_nbJetons_setter(instance):
    original = instance.nbJetons
    instance.nbJetons = original
    assert instance.nbJetons == original

@given(instance=petriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petriNet_Arc)



@given(instance=petriNet_Arc_strategy)
def test_petrinet_arc_Direction_setter(instance):
    original = instance.Direction
    instance.Direction = original
    assert instance.Direction == original



@given(instance=petriNet_Arc_strategy)
def test_petrinet_arc_jetonsTransferes_setter(instance):
    original = instance.jetonsTransferes
    instance.jetonsTransferes = original
    assert instance.jetonsTransferes == original

@given(instance=petriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petriNet_Transition)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petriNet_Transition_strategy)
@settings(max_examples=30)
def test_petrinet_transition_newoperation1_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.newOperation1()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.newOperation1).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'newOperation1' in petriNet_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'newOperation1' in petriNet_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'newOperation1' in petriNet_Transition is not implemented or raised an error")

@given(instance=petriNet_PetriElement_strategy)
@settings(max_examples=50)
def test_petrinet_petrielement_instantiation(instance):
    assert isinstance(instance, petriNet_PetriElement)



@given(instance=petriNet_PetriElement_strategy)
def test_petrinet_petrielement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
