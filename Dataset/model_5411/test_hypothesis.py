import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Gate,
    dynamicFaultTree_OR,
    dynamicFaultTree_POR,
    dynamicFaultTree_XOR,
    dynamicFaultTree_Spare,
    dynamicFaultTree_PAND,
    dynamicFaultTree_AND,
    Dependency,
    dynamicFaultTree_FunctionalDependency,
    dynamicFaultTree_Sequence,
    Element,
    dynamicFaultTree_Gate,
    dynamicFaultTree_Element,
    dynamicFaultTree_Dependency,
    dynamicFaultTree_TopLevelEvent,
    dynamicFaultTree_DFT,
    dynamicFaultTree_Event,
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



def test_dynamicfaulttree_or_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_OR)


def test_dynamicfaulttree_or_constructor_exists():
    assert callable(dynamicFaultTree_OR.__init__)


def test_dynamicfaulttree_or_constructor_args():
    sig = inspect.signature(dynamicFaultTree_OR.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_por_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_POR)


def test_dynamicfaulttree_por_constructor_exists():
    assert callable(dynamicFaultTree_POR.__init__)


def test_dynamicfaulttree_por_constructor_args():
    sig = inspect.signature(dynamicFaultTree_POR.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_xor_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_XOR)


def test_dynamicfaulttree_xor_constructor_exists():
    assert callable(dynamicFaultTree_XOR.__init__)


def test_dynamicfaulttree_xor_constructor_args():
    sig = inspect.signature(dynamicFaultTree_XOR.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_spare_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_Spare)


def test_dynamicfaulttree_spare_constructor_exists():
    assert callable(dynamicFaultTree_Spare.__init__)


def test_dynamicfaulttree_spare_constructor_args():
    sig = inspect.signature(dynamicFaultTree_Spare.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_pand_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_PAND)


def test_dynamicfaulttree_pand_constructor_exists():
    assert callable(dynamicFaultTree_PAND.__init__)


def test_dynamicfaulttree_pand_constructor_args():
    sig = inspect.signature(dynamicFaultTree_PAND.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_and_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_AND)


def test_dynamicfaulttree_and_constructor_exists():
    assert callable(dynamicFaultTree_AND.__init__)


def test_dynamicfaulttree_and_constructor_args():
    sig = inspect.signature(dynamicFaultTree_AND.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_functionaldependency_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_FunctionalDependency)


def test_dynamicfaulttree_functionaldependency_constructor_exists():
    assert callable(dynamicFaultTree_FunctionalDependency.__init__)


def test_dynamicfaulttree_functionaldependency_constructor_args():
    sig = inspect.signature(dynamicFaultTree_FunctionalDependency.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_sequence_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_Sequence)


def test_dynamicfaulttree_sequence_constructor_exists():
    assert callable(dynamicFaultTree_Sequence.__init__)


def test_dynamicfaulttree_sequence_constructor_args():
    sig = inspect.signature(dynamicFaultTree_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_gate_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_Gate)


def test_dynamicfaulttree_gate_constructor_exists():
    assert callable(dynamicFaultTree_Gate.__init__)


def test_dynamicfaulttree_gate_constructor_args():
    sig = inspect.signature(dynamicFaultTree_Gate.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_element_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_Element)


def test_dynamicfaulttree_element_constructor_exists():
    assert callable(dynamicFaultTree_Element.__init__)


def test_dynamicfaulttree_element_constructor_args():
    sig = inspect.signature(dynamicFaultTree_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "elementID" in params, "Missing parameter 'elementID'"
    assert "sequencePosition" in params, "Missing parameter 'sequencePosition'"
    assert "probability" in params, "Missing parameter 'probability'"

def test_dynamicfaulttree_element_has_name():
    assert hasattr(dynamicFaultTree_Element, "name")
    descriptor = None
    for klass in dynamicFaultTree_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dynamicfaulttree_element_has_elementID():
    assert hasattr(dynamicFaultTree_Element, "elementID")
    descriptor = None
    for klass in dynamicFaultTree_Element.__mro__:
        if "elementID" in klass.__dict__:
            descriptor = klass.__dict__["elementID"]
            break
    assert isinstance(descriptor, property)

def test_dynamicfaulttree_element_has_sequencePosition():
    assert hasattr(dynamicFaultTree_Element, "sequencePosition")
    descriptor = None
    for klass in dynamicFaultTree_Element.__mro__:
        if "sequencePosition" in klass.__dict__:
            descriptor = klass.__dict__["sequencePosition"]
            break
    assert isinstance(descriptor, property)

def test_dynamicfaulttree_element_has_probability():
    assert hasattr(dynamicFaultTree_Element, "probability")
    descriptor = None
    for klass in dynamicFaultTree_Element.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_dynamicfaulttree_dependency_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_Dependency)


def test_dynamicfaulttree_dependency_constructor_exists():
    assert callable(dynamicFaultTree_Dependency.__init__)


def test_dynamicfaulttree_dependency_constructor_args():
    sig = inspect.signature(dynamicFaultTree_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_toplevelevent_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_TopLevelEvent)


def test_dynamicfaulttree_toplevelevent_constructor_exists():
    assert callable(dynamicFaultTree_TopLevelEvent.__init__)


def test_dynamicfaulttree_toplevelevent_constructor_args():
    sig = inspect.signature(dynamicFaultTree_TopLevelEvent.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfaulttree_dft_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_DFT)


def test_dynamicfaulttree_dft_constructor_exists():
    assert callable(dynamicFaultTree_DFT.__init__)


def test_dynamicfaulttree_dft_constructor_args():
    sig = inspect.signature(dynamicFaultTree_DFT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dynamicfaulttree_dft_has_name():
    assert hasattr(dynamicFaultTree_DFT, "name")
    descriptor = None
    for klass in dynamicFaultTree_DFT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dynamicfaulttree_event_is_not_abstract():
    assert not inspect.isabstract(dynamicFaultTree_Event)


def test_dynamicfaulttree_event_constructor_exists():
    assert callable(dynamicFaultTree_Event.__init__)


def test_dynamicfaulttree_event_constructor_args():
    sig = inspect.signature(dynamicFaultTree_Event.__init__)
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
dynamicFaultTree_OR_strategy = st.builds(
    dynamicFaultTree_OR,
)
dynamicFaultTree_POR_strategy = st.builds(
    dynamicFaultTree_POR,
)
dynamicFaultTree_XOR_strategy = st.builds(
    dynamicFaultTree_XOR,
)
dynamicFaultTree_Spare_strategy = st.builds(
    dynamicFaultTree_Spare,
)
dynamicFaultTree_PAND_strategy = st.builds(
    dynamicFaultTree_PAND,
)
dynamicFaultTree_AND_strategy = st.builds(
    dynamicFaultTree_AND,
)
Dependency_strategy = st.builds(
    Dependency,
)
dynamicFaultTree_FunctionalDependency_strategy = st.builds(
    dynamicFaultTree_FunctionalDependency,
)
dynamicFaultTree_Sequence_strategy = st.builds(
    dynamicFaultTree_Sequence,
)
Element_strategy = st.builds(
    Element,
)
dynamicFaultTree_Gate_strategy = st.builds(
    dynamicFaultTree_Gate,
)
dynamicFaultTree_Element_strategy = st.builds(
    dynamicFaultTree_Element,
    name=
        safe_text,
    elementID=
        st.integers(),
    sequencePosition=
        st.integers(),
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dynamicFaultTree_Dependency_strategy = st.builds(
    dynamicFaultTree_Dependency,
)
dynamicFaultTree_TopLevelEvent_strategy = st.builds(
    dynamicFaultTree_TopLevelEvent,
)
dynamicFaultTree_DFT_strategy = st.builds(
    dynamicFaultTree_DFT,
    name=
        safe_text
)
dynamicFaultTree_Event_strategy = st.builds(
    dynamicFaultTree_Event,
)

@given(instance=Gate_strategy)
@settings(max_examples=50)
def test_gate_instantiation(instance):
    assert isinstance(instance, Gate)

@given(instance=dynamicFaultTree_OR_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_or_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_OR)

@given(instance=dynamicFaultTree_POR_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_por_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_POR)

@given(instance=dynamicFaultTree_XOR_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_xor_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_XOR)

@given(instance=dynamicFaultTree_Spare_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_spare_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_Spare)

@given(instance=dynamicFaultTree_PAND_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_pand_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_PAND)

@given(instance=dynamicFaultTree_AND_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_and_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_AND)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=dynamicFaultTree_FunctionalDependency_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_functionaldependency_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_FunctionalDependency)

@given(instance=dynamicFaultTree_Sequence_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_sequence_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_Sequence)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=dynamicFaultTree_Gate_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_gate_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_Gate)

@given(instance=dynamicFaultTree_Element_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_element_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_Element)



@given(instance=dynamicFaultTree_Element_strategy)
def test_dynamicfaulttree_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dynamicFaultTree_Element_strategy)
def test_dynamicfaulttree_element_elementID_setter(instance):
    original = instance.elementID
    instance.elementID = original
    assert instance.elementID == original



@given(instance=dynamicFaultTree_Element_strategy)
def test_dynamicfaulttree_element_sequencePosition_setter(instance):
    original = instance.sequencePosition
    instance.sequencePosition = original
    assert instance.sequencePosition == original



@given(instance=dynamicFaultTree_Element_strategy)
def test_dynamicfaulttree_element_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=dynamicFaultTree_Dependency_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_dependency_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_Dependency)

@given(instance=dynamicFaultTree_TopLevelEvent_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_toplevelevent_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_TopLevelEvent)

@given(instance=dynamicFaultTree_DFT_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_dft_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_DFT)



@given(instance=dynamicFaultTree_DFT_strategy)
def test_dynamicfaulttree_dft_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dynamicFaultTree_Event_strategy)
@settings(max_examples=50)
def test_dynamicfaulttree_event_instantiation(instance):
    assert isinstance(instance, dynamicFaultTree_Event)
