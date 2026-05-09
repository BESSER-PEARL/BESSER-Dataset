import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    PN::Transition,
    NamedElement,
    PN::Node,
    PN::NamedElement,
    PN::PetriNet,
    Arc,
    PN::InputArc,
    PN::OutputArc,
    PN::Arc,
    PN::Place,
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



def test_pn::transition_is_not_abstract():
    assert not inspect.isabstract(PN::Transition)


def test_pn::transition_constructor_exists():
    assert callable(PN::Transition.__init__)


def test_pn::transition_constructor_args():
    sig = inspect.signature(PN::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "minDelay" in params, "Missing parameter 'minDelay'"
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"

def test_pn::transition_has_minDelay():
    assert hasattr(PN::Transition, "minDelay")
    descriptor = None
    for klass in PN::Transition.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
            break
    assert isinstance(descriptor, property)

def test_pn::transition_has_maxDelay():
    assert hasattr(PN::Transition, "maxDelay")
    descriptor = None
    for klass in PN::Transition.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_pn::node_is_not_abstract():
    assert not inspect.isabstract(PN::Node)


def test_pn::node_constructor_exists():
    assert callable(PN::Node.__init__)


def test_pn::node_constructor_args():
    sig = inspect.signature(PN::Node.__init__)
    params = list(sig.parameters.keys())



def test_pn::namedelement_is_not_abstract():
    assert not inspect.isabstract(PN::NamedElement)


def test_pn::namedelement_constructor_exists():
    assert callable(PN::NamedElement.__init__)


def test_pn::namedelement_constructor_args():
    sig = inspect.signature(PN::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn::namedelement_has_name():
    assert hasattr(PN::NamedElement, "name")
    descriptor = None
    for klass in PN::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pn::petrinet_is_not_abstract():
    assert not inspect.isabstract(PN::PetriNet)


def test_pn::petrinet_constructor_exists():
    assert callable(PN::PetriNet.__init__)


def test_pn::petrinet_constructor_args():
    sig = inspect.signature(PN::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pn::petrinet_has_name():
    assert hasattr(PN::PetriNet, "name")
    descriptor = None
    for klass in PN::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_pn::inputarc_is_not_abstract():
    assert not inspect.isabstract(PN::InputArc)


def test_pn::inputarc_constructor_exists():
    assert callable(PN::InputArc.__init__)


def test_pn::inputarc_constructor_args():
    sig = inspect.signature(PN::InputArc.__init__)
    params = list(sig.parameters.keys())



def test_pn::outputarc_is_not_abstract():
    assert not inspect.isabstract(PN::OutputArc)


def test_pn::outputarc_constructor_exists():
    assert callable(PN::OutputArc.__init__)


def test_pn::outputarc_constructor_args():
    sig = inspect.signature(PN::OutputArc.__init__)
    params = list(sig.parameters.keys())



def test_pn::arc_is_not_abstract():
    assert not inspect.isabstract(PN::Arc)


def test_pn::arc_constructor_exists():
    assert callable(PN::Arc.__init__)


def test_pn::arc_constructor_args():
    sig = inspect.signature(PN::Arc.__init__)
    params = list(sig.parameters.keys())



def test_pn::place_is_not_abstract():
    assert not inspect.isabstract(PN::Place)


def test_pn::place_constructor_exists():
    assert callable(PN::Place.__init__)


def test_pn::place_constructor_args():
    sig = inspect.signature(PN::Place.__init__)
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
PN::Transition_strategy = st.builds(
    PN::Transition,
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
NamedElement_strategy = st.builds(
    NamedElement,
)
PN::Node_strategy = st.builds(
    PN::Node,
)
PN::NamedElement_strategy = st.builds(
    PN::NamedElement,
    name=
        safe_text
)
PN::PetriNet_strategy = st.builds(
    PN::PetriNet,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
PN::InputArc_strategy = st.builds(
    PN::InputArc,
)
PN::OutputArc_strategy = st.builds(
    PN::OutputArc,
)
PN::Arc_strategy = st.builds(
    PN::Arc,
)
PN::Place_strategy = st.builds(
    PN::Place,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PN::Transition_strategy)
@settings(max_examples=50)
def test_pn::transition_instantiation(instance):
    assert isinstance(instance, PN::Transition)

@given(instance=PN::Transition_strategy)
def test_pn::transition_minDelay_type(instance):
    assert isinstance(instance.minDelay, float)


@given(instance=PN::Transition_strategy)
def test_pn::transition_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original

@given(instance=PN::Transition_strategy)
def test_pn::transition_maxDelay_type(instance):
    assert isinstance(instance.maxDelay, float)


@given(instance=PN::Transition_strategy)
def test_pn::transition_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=PN::Node_strategy)
@settings(max_examples=50)
def test_pn::node_instantiation(instance):
    assert isinstance(instance, PN::Node)

@given(instance=PN::NamedElement_strategy)
@settings(max_examples=50)
def test_pn::namedelement_instantiation(instance):
    assert isinstance(instance, PN::NamedElement)

@given(instance=PN::NamedElement_strategy)
def test_pn::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PN::NamedElement_strategy)
def test_pn::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PN::PetriNet_strategy)
@settings(max_examples=50)
def test_pn::petrinet_instantiation(instance):
    assert isinstance(instance, PN::PetriNet)

@given(instance=PN::PetriNet_strategy)
def test_pn::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PN::PetriNet_strategy)
def test_pn::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PN::InputArc_strategy)
@settings(max_examples=50)
def test_pn::inputarc_instantiation(instance):
    assert isinstance(instance, PN::InputArc)

@given(instance=PN::OutputArc_strategy)
@settings(max_examples=50)
def test_pn::outputarc_instantiation(instance):
    assert isinstance(instance, PN::OutputArc)

@given(instance=PN::Arc_strategy)
@settings(max_examples=50)
def test_pn::arc_instantiation(instance):
    assert isinstance(instance, PN::Arc)

@given(instance=PN::Place_strategy)
@settings(max_examples=50)
def test_pn::place_instantiation(instance):
    assert isinstance(instance, PN::Place)
