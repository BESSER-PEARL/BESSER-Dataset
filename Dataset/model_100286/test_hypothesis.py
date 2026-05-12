import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    pETRI::Transition,
    pETRI::Place,
    pETRI::PetriNet,
    PetriNetElement,
    pETRI::Arc,
    pETRI::Node,
    pETRI::PetriNetElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petri::transition_is_not_abstract():
    assert not inspect.isabstract(pETRI::Transition)


def test_petri::transition_constructor_exists():
    assert callable(pETRI::Transition.__init__)


def test_petri::transition_constructor_args():
    sig = inspect.signature(pETRI::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petri::place_is_not_abstract():
    assert not inspect.isabstract(pETRI::Place)


def test_petri::place_constructor_exists():
    assert callable(pETRI::Place.__init__)


def test_petri::place_constructor_args():
    sig = inspect.signature(pETRI::Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petri::place_has_marking():
    assert hasattr(pETRI::Place, "marking")
    descriptor = None
    for klass in pETRI::Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_petri::petrinet_is_not_abstract():
    assert not inspect.isabstract(pETRI::PetriNet)


def test_petri::petrinet_constructor_exists():
    assert callable(pETRI::PetriNet.__init__)


def test_petri::petrinet_constructor_args():
    sig = inspect.signature(pETRI::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri::petrinet_has_name():
    assert hasattr(pETRI::PetriNet, "name")
    descriptor = None
    for klass in pETRI::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetelement_is_not_abstract():
    assert not inspect.isabstract(PetriNetElement)


def test_petrinetelement_constructor_exists():
    assert callable(PetriNetElement.__init__)


def test_petrinetelement_constructor_args():
    sig = inspect.signature(PetriNetElement.__init__)
    params = list(sig.parameters.keys())



def test_petri::arc_is_not_abstract():
    assert not inspect.isabstract(pETRI::Arc)


def test_petri::arc_constructor_exists():
    assert callable(pETRI::Arc.__init__)


def test_petri::arc_constructor_args():
    sig = inspect.signature(pETRI::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_petri::arc_has_multiplicity():
    assert hasattr(pETRI::Arc, "multiplicity")
    descriptor = None
    for klass in pETRI::Arc.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_petri::arc_has_readOnly():
    assert hasattr(pETRI::Arc, "readOnly")
    descriptor = None
    for klass in pETRI::Arc.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_petri::node_is_not_abstract():
    assert not inspect.isabstract(pETRI::Node)


def test_petri::node_constructor_exists():
    assert callable(pETRI::Node.__init__)


def test_petri::node_constructor_args():
    sig = inspect.signature(pETRI::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri::node_has_name():
    assert hasattr(pETRI::Node, "name")
    descriptor = None
    for klass in pETRI::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri::petrinetelement_is_not_abstract():
    assert not inspect.isabstract(pETRI::PetriNetElement)


def test_petri::petrinetelement_constructor_exists():
    assert callable(pETRI::PetriNetElement.__init__)


def test_petri::petrinetelement_constructor_args():
    sig = inspect.signature(pETRI::PetriNetElement.__init__)
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
Node_strategy = st.builds(
    Node,
)
pETRI::Transition_strategy = st.builds(
    pETRI::Transition,
)
pETRI::Place_strategy = st.builds(
    pETRI::Place,
    marking=
        st.integers()
)
pETRI::PetriNet_strategy = st.builds(
    pETRI::PetriNet,
    name=
        safe_text
)
PetriNetElement_strategy = st.builds(
    PetriNetElement,
)
pETRI::Arc_strategy = st.builds(
    pETRI::Arc,
    multiplicity=
        st.integers(),
    readOnly=
        st.booleans()
)
pETRI::Node_strategy = st.builds(
    pETRI::Node,
    name=
        safe_text
)
pETRI::PetriNetElement_strategy = st.builds(
    pETRI::PetriNetElement,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=pETRI::Transition_strategy)
@settings(max_examples=50)
def test_petri::transition_instantiation(instance):
    assert isinstance(instance, pETRI::Transition)

@given(instance=pETRI::Place_strategy)
@settings(max_examples=50)
def test_petri::place_instantiation(instance):
    assert isinstance(instance, pETRI::Place)

@given(instance=pETRI::Place_strategy)
def test_petri::place_marking_type(instance):
    assert isinstance(instance.marking, int)


@given(instance=pETRI::Place_strategy)
def test_petri::place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=pETRI::PetriNet_strategy)
@settings(max_examples=50)
def test_petri::petrinet_instantiation(instance):
    assert isinstance(instance, pETRI::PetriNet)

@given(instance=pETRI::PetriNet_strategy)
def test_petri::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pETRI::PetriNet_strategy)
def test_petri::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetElement_strategy)
@settings(max_examples=50)
def test_petrinetelement_instantiation(instance):
    assert isinstance(instance, PetriNetElement)

@given(instance=pETRI::Arc_strategy)
@settings(max_examples=50)
def test_petri::arc_instantiation(instance):
    assert isinstance(instance, pETRI::Arc)

@given(instance=pETRI::Arc_strategy)
def test_petri::arc_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, int)


@given(instance=pETRI::Arc_strategy)
def test_petri::arc_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=pETRI::Arc_strategy)
def test_petri::arc_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=pETRI::Arc_strategy)
def test_petri::arc_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=pETRI::Node_strategy)
@settings(max_examples=50)
def test_petri::node_instantiation(instance):
    assert isinstance(instance, pETRI::Node)

@given(instance=pETRI::Node_strategy)
def test_petri::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pETRI::Node_strategy)
def test_petri::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pETRI::PetriNetElement_strategy)
@settings(max_examples=50)
def test_petri::petrinetelement_instantiation(instance):
    assert isinstance(instance, pETRI::PetriNetElement)
