import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petriNet::PetriNetwork,
    PetriElement,
    petriNet::Place,
    petriNet::Arc,
    petriNet::Transition,
    petriNet::PetriElement,
    ArcDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::petrinetwork_is_not_abstract():
    assert not inspect.isabstract(petriNet::PetriNetwork)


def test_petrinet::petrinetwork_constructor_exists():
    assert callable(petriNet::PetriNetwork.__init__)


def test_petrinet::petrinetwork_constructor_args():
    sig = inspect.signature(petriNet::PetriNetwork.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinetwork_has_name():
    assert hasattr(petriNet::PetriNetwork, "name")
    descriptor = None
    for klass in petriNet::PetriNetwork.__mro__:
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



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "nbJetons" in params, "Missing parameter 'nbJetons'"

def test_petrinet::place_has_nbJetons():
    assert hasattr(petriNet::Place, "nbJetons")
    descriptor = None
    for klass in petriNet::Place.__mro__:
        if "nbJetons" in klass.__dict__:
            descriptor = klass.__dict__["nbJetons"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "jetonsTransferes" in params, "Missing parameter 'jetonsTransferes'"
    assert "Direction" in params, "Missing parameter 'Direction'"

def test_petrinet::arc_has_jetonsTransferes():
    assert hasattr(petriNet::Arc, "jetonsTransferes")
    descriptor = None
    for klass in petriNet::Arc.__mro__:
        if "jetonsTransferes" in klass.__dict__:
            descriptor = klass.__dict__["jetonsTransferes"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_Direction():
    assert hasattr(petriNet::Arc, "Direction")
    descriptor = None
    for klass in petriNet::Arc.__mro__:
        if "Direction" in klass.__dict__:
            descriptor = klass.__dict__["Direction"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrielement_is_not_abstract():
    assert not inspect.isabstract(petriNet::PetriElement)


def test_petrinet::petrielement_constructor_exists():
    assert callable(petriNet::PetriElement.__init__)


def test_petrinet::petrielement_constructor_args():
    sig = inspect.signature(petriNet::PetriElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrielement_has_name():
    assert hasattr(petriNet::PetriElement, "name")
    descriptor = None
    for klass in petriNet::PetriElement.__mro__:
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
petriNet::PetriNetwork_strategy = st.builds(
    petriNet::PetriNetwork,
    name=
        safe_text
)
PetriElement_strategy = st.builds(
    PetriElement,
)
petriNet::Place_strategy = st.builds(
    petriNet::Place,
    nbJetons=
        st.integers()
)
petriNet::Arc_strategy = st.builds(
    petriNet::Arc,
    jetonsTransferes=
        st.integers(),
    Direction=
        safe_text
)
petriNet::Transition_strategy = st.builds(
    petriNet::Transition,
)
petriNet::PetriElement_strategy = st.builds(
    petriNet::PetriElement,
    name=
        safe_text
)

@given(instance=petriNet::PetriNetwork_strategy)
@settings(max_examples=50)
def test_petrinet::petrinetwork_instantiation(instance):
    assert isinstance(instance, petriNet::PetriNetwork)

@given(instance=petriNet::PetriNetwork_strategy)
def test_petrinet::petrinetwork_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::PetriNetwork_strategy)
def test_petrinet::petrinetwork_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriElement_strategy)
@settings(max_examples=50)
def test_petrielement_instantiation(instance):
    assert isinstance(instance, PetriElement)

@given(instance=petriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petriNet::Place)

@given(instance=petriNet::Place_strategy)
def test_petrinet::place_nbJetons_type(instance):
    assert isinstance(instance.nbJetons, int)


@given(instance=petriNet::Place_strategy)
def test_petrinet::place_nbJetons_setter(instance):
    original = instance.nbJetons
    instance.nbJetons = original
    assert instance.nbJetons == original

@given(instance=petriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petriNet::Arc)

@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_jetonsTransferes_type(instance):
    assert isinstance(instance.jetonsTransferes, int)


@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_jetonsTransferes_setter(instance):
    original = instance.jetonsTransferes
    instance.jetonsTransferes = original
    assert instance.jetonsTransferes == original

@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_Direction_type(instance):
    assert isinstance(instance.Direction, str)


@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_Direction_setter(instance):
    original = instance.Direction
    instance.Direction = original
    assert instance.Direction == original

@given(instance=petriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petriNet::Transition)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=petriNet::Transition_strategy)
@settings(max_examples=30)
def test_petrinet::transition_newoperation1_changes_state(instance):
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
        assert has_statements, f"Function 'newOperation1' in petriNet::Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'newOperation1' in petriNet::Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'newOperation1' in petriNet::Transition is not implemented or raised an error")

@given(instance=petriNet::PetriElement_strategy)
@settings(max_examples=50)
def test_petrinet::petrielement_instantiation(instance):
    assert isinstance(instance, petriNet::PetriElement)

@given(instance=petriNet::PetriElement_strategy)
def test_petrinet::petrielement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::PetriElement_strategy)
def test_petrinet::petrielement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
