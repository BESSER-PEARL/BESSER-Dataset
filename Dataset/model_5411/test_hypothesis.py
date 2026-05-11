import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Gate,
    dynamicFaultTree::Spare,
    dynamicFaultTree::POR,
    dynamicFaultTree::XOR,
    dynamicFaultTree::PAND,
    dynamicFaultTree::OR,
    dynamicFaultTree::AND,
    Dependency,
    dynamicFaultTree::FunctionalDependency,
    dynamicFaultTree::Sequence,
    Element,
    dynamicFaultTree::Gate,
    dynamicFaultTree::Element,
    dynamicFaultTree::Dependency,
    dynamicFaultTree::TopLevelEvent,
    dynamicFaultTree::DFT,
    dynamicFaultTree::Event,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gate_is_not_abstract():
    assert not inspect.isabstract(Gate)


def test_gate_constructor_exists():
    assert callable(Gate.__init__)


def test_gate_constructor_args():
    sig = inspect.signature(Gate.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::spare_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::Spare)


def test_dynamicfaulttree::spare_constructor_exists():
    assert callable(dynamicFaultTree::Spare.__init__)


def test_dynamicfaulttree::spare_constructor_args():
    sig = inspect.signature(dynamicFaultTree::Spare.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::por_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::POR)


def test_dynamicfaulttree::por_constructor_exists():
    assert callable(dynamicFaultTree::POR.__init__)


def test_dynamicfaulttree::por_constructor_args():
    sig = inspect.signature(dynamicFaultTree::POR.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::xor_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::XOR)


def test_dynamicfaulttree::xor_constructor_exists():
    assert callable(dynamicFaultTree::XOR.__init__)


def test_dynamicfaulttree::xor_constructor_args():
    sig = inspect.signature(dynamicFaultTree::XOR.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::pand_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::PAND)


def test_dynamicfaulttree::pand_constructor_exists():
    assert callable(dynamicFaultTree::PAND.__init__)


def test_dynamicfaulttree::pand_constructor_args():
    sig = inspect.signature(dynamicFaultTree::PAND.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::or_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::OR)


def test_dynamicfaulttree::or_constructor_exists():
    assert callable(dynamicFaultTree::OR.__init__)


def test_dynamicfaulttree::or_constructor_args():
    sig = inspect.signature(dynamicFaultTree::OR.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::and_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::AND)


def test_dynamicfaulttree::and_constructor_exists():
    assert callable(dynamicFaultTree::AND.__init__)


def test_dynamicfaulttree::and_constructor_args():
    sig = inspect.signature(dynamicFaultTree::AND.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::functionaldependency_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::FunctionalDependency)


def test_dynamicfaulttree::functionaldependency_constructor_exists():
    assert callable(dynamicFaultTree::FunctionalDependency.__init__)


def test_dynamicfaulttree::functionaldependency_constructor_args():
    sig = inspect.signature(dynamicFaultTree::FunctionalDependency.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::sequence_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::Sequence)


def test_dynamicfaulttree::sequence_constructor_exists():
    assert callable(dynamicFaultTree::Sequence.__init__)


def test_dynamicfaulttree::sequence_constructor_args():
    sig = inspect.signature(dynamicFaultTree::Sequence.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::gate_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::Gate)


def test_dynamicfaulttree::gate_constructor_exists():
    assert callable(dynamicFaultTree::Gate.__init__)


def test_dynamicfaulttree::gate_constructor_args():
    sig = inspect.signature(dynamicFaultTree::Gate.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::element_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::Element)


def test_dynamicfaulttree::element_constructor_exists():
    assert callable(dynamicFaultTree::Element.__init__)


def test_dynamicfaulttree::element_constructor_args():
    sig = inspect.signature(dynamicFaultTree::Element.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"
    assert "sequencePosition" in params, "Missing parameter 'sequencePosition'"
    assert "elementID" in params, "Missing parameter 'elementID'"
    assert "name" in params, "Missing parameter 'name'"

def test_dynamicfaulttree::element_has_probability():
    assert hasattr(dynamicFaultTree::Element, "probability")
    descriptor = None
    for klass in dynamicFaultTree::Element.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_dynamicfaulttree::element_has_sequencePosition():
    assert hasattr(dynamicFaultTree::Element, "sequencePosition")
    descriptor = None
    for klass in dynamicFaultTree::Element.__mro__:
        if "sequencePosition" in klass.__dict__:
            descriptor = klass.__dict__["sequencePosition"]
            break
    assert isinstance(descriptor, property)

def test_dynamicfaulttree::element_has_elementID():
    assert hasattr(dynamicFaultTree::Element, "elementID")
    descriptor = None
    for klass in dynamicFaultTree::Element.__mro__:
        if "elementID" in klass.__dict__:
            descriptor = klass.__dict__["elementID"]
            break
    assert isinstance(descriptor, property)

def test_dynamicfaulttree::element_has_name():
    assert hasattr(dynamicFaultTree::Element, "name")
    descriptor = None
    for klass in dynamicFaultTree::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dynamicfaulttree::dependency_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::Dependency)


def test_dynamicfaulttree::dependency_constructor_exists():
    assert callable(dynamicFaultTree::Dependency.__init__)


def test_dynamicfaulttree::dependency_constructor_args():
    sig = inspect.signature(dynamicFaultTree::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::toplevelevent_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::TopLevelEvent)


def test_dynamicfaulttree::toplevelevent_constructor_exists():
    assert callable(dynamicFaultTree::TopLevelEvent.__init__)


def test_dynamicfaulttree::toplevelevent_constructor_args():
    sig = inspect.signature(dynamicFaultTree::TopLevelEvent.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree::dft_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::DFT)


def test_dynamicfaulttree::dft_constructor_exists():
    assert callable(dynamicFaultTree::DFT.__init__)


def test_dynamicfaulttree::dft_constructor_args():
    sig = inspect.signature(dynamicFaultTree::DFT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dynamicfaulttree::dft_has_name():
    assert hasattr(dynamicFaultTree::DFT, "name")
    descriptor = None
    for klass in dynamicFaultTree::DFT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dynamicfaulttree::event_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree::Event)


def test_dynamicfaulttree::event_constructor_exists():
    assert callable(dynamicFaultTree::Event.__init__)


def test_dynamicfaulttree::event_constructor_args():
    sig = inspect.signature(dynamicFaultTree::Event.__init__)
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
Gate_strategy = st.builds(
    Gate,
)
dynamicFaultTree::Spare_strategy = st.builds(
    dynamicFaultTree::Spare,
)
dynamicFaultTree::POR_strategy = st.builds(
    dynamicFaultTree::POR,
)
dynamicFaultTree::XOR_strategy = st.builds(
    dynamicFaultTree::XOR,
)
dynamicFaultTree::PAND_strategy = st.builds(
    dynamicFaultTree::PAND,
)
dynamicFaultTree::OR_strategy = st.builds(
    dynamicFaultTree::OR,
)
dynamicFaultTree::AND_strategy = st.builds(
    dynamicFaultTree::AND,
)
Dependency_strategy = st.builds(
    Dependency,
)
dynamicFaultTree::FunctionalDependency_strategy = st.builds(
    dynamicFaultTree::FunctionalDependency,
)
dynamicFaultTree::Sequence_strategy = st.builds(
    dynamicFaultTree::Sequence,
)
Element_strategy = st.builds(
    Element,
)
dynamicFaultTree::Gate_strategy = st.builds(
    dynamicFaultTree::Gate,
)
dynamicFaultTree::Element_strategy = st.builds(
    dynamicFaultTree::Element,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    sequencePosition=
        st.integers(),
    elementID=
        st.integers(),
    name=
        safe_text
)
dynamicFaultTree::Dependency_strategy = st.builds(
    dynamicFaultTree::Dependency,
)
dynamicFaultTree::TopLevelEvent_strategy = st.builds(
    dynamicFaultTree::TopLevelEvent,
)
dynamicFaultTree::DFT_strategy = st.builds(
    dynamicFaultTree::DFT,
    name=
        safe_text
)
dynamicFaultTree::Event_strategy = st.builds(
    dynamicFaultTree::Event,
)

@given(instance=Gate_strategy)
@settings(max_examples=50)
def test_gate_instantiation(instance):
    assert isinstance(instance, Gate)

@given(instance=dynamicFaultTree::Spare_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::spare_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::Spare)

@given(instance=dynamicFaultTree::POR_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::por_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::POR)

@given(instance=dynamicFaultTree::XOR_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::xor_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::XOR)

@given(instance=dynamicFaultTree::PAND_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::pand_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::PAND)

@given(instance=dynamicFaultTree::OR_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::or_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::OR)

@given(instance=dynamicFaultTree::AND_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::and_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::AND)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=dynamicFaultTree::FunctionalDependency_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::functionaldependency_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::FunctionalDependency)

@given(instance=dynamicFaultTree::Sequence_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::sequence_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::Sequence)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=dynamicFaultTree::Gate_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::gate_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::Gate)

@given(instance=dynamicFaultTree::Element_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::element_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::Element)

@given(instance=dynamicFaultTree::Element_strategy)
def test_dynamicfaulttree::element_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=dynamicFaultTree::Element_strategy)
def test_dynamicfaulttree::element_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=dynamicFaultTree::Element_strategy)
def test_dynamicfaulttree::element_sequencePosition_type(instance):
    assert isinstance(instance.sequencePosition, int)


@given(instance=dynamicFaultTree::Element_strategy)
def test_dynamicfaulttree::element_sequencePosition_setter(instance):
    original = instance.sequencePosition
    instance.sequencePosition = original
    assert instance.sequencePosition == original

@given(instance=dynamicFaultTree::Element_strategy)
def test_dynamicfaulttree::element_elementID_type(instance):
    assert isinstance(instance.elementID, int)


@given(instance=dynamicFaultTree::Element_strategy)
def test_dynamicfaulttree::element_elementID_setter(instance):
    original = instance.elementID
    instance.elementID = original
    assert instance.elementID == original

@given(instance=dynamicFaultTree::Element_strategy)
def test_dynamicfaulttree::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dynamicFaultTree::Element_strategy)
def test_dynamicfaulttree::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dynamicFaultTree::Dependency_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::dependency_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::Dependency)

@given(instance=dynamicFaultTree::TopLevelEvent_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::toplevelevent_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::TopLevelEvent)

@given(instance=dynamicFaultTree::DFT_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::dft_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::DFT)

@given(instance=dynamicFaultTree::DFT_strategy)
def test_dynamicfaulttree::dft_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dynamicFaultTree::DFT_strategy)
def test_dynamicfaulttree::dft_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dynamicFaultTree::Event_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree::event_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree::Event)
