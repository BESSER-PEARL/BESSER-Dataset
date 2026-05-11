import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FaultTree::FaultTree,
    FaultTree::EObject,
    FaultTree::Event,
    LogicOperation,
    FaultTreeType,
    EventType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faulttree::faulttree_is_not_abstract():
    assert not inspect.isabstract(FaultTree::FaultTree)


def test_faulttree::faulttree_constructor_exists():
    assert callable(FaultTree::FaultTree.__init__)


def test_faulttree::faulttree_constructor_args():
    sig = inspect.signature(FaultTree::FaultTree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "message" in params, "Missing parameter 'message'"
    assert "faultTreeType" in params, "Missing parameter 'faultTreeType'"

def test_faulttree::faulttree_has_name():
    assert hasattr(FaultTree::FaultTree, "name")
    descriptor = None
    for klass in FaultTree::FaultTree.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::faulttree_has_message():
    assert hasattr(FaultTree::FaultTree, "message")
    descriptor = None
    for klass in FaultTree::FaultTree.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::faulttree_has_faultTreeType():
    assert hasattr(FaultTree::FaultTree, "faultTreeType")
    descriptor = None
    for klass in FaultTree::FaultTree.__mro__:
        if "faultTreeType" in klass.__dict__:
            descriptor = klass.__dict__["faultTreeType"]
            break
    assert isinstance(descriptor, property)



def test_faulttree::eobject_is_not_abstract():
    assert not inspect.isabstract(FaultTree::EObject)


def test_faulttree::eobject_constructor_exists():
    assert callable(FaultTree::EObject.__init__)


def test_faulttree::eobject_constructor_args():
    sig = inspect.signature(FaultTree::EObject.__init__)
    params = list(sig.parameters.keys())



def test_faulttree::event_is_not_abstract():
    assert not inspect.isabstract(FaultTree::Event)


def test_faulttree::event_constructor_exists():
    assert callable(FaultTree::Event.__init__)


def test_faulttree::event_constructor_args():
    sig = inspect.signature(FaultTree::Event.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "computedProbability" in params, "Missing parameter 'computedProbability'"
    assert "assignedProbability" in params, "Missing parameter 'assignedProbability'"
    assert "k" in params, "Missing parameter 'k'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "message" in params, "Missing parameter 'message'"
    assert "subEventLogic" in params, "Missing parameter 'subEventLogic'"
    assert "referenceCount" in params, "Missing parameter 'referenceCount'"

def test_faulttree::event_has_type():
    assert hasattr(FaultTree::Event, "type")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_computedProbability():
    assert hasattr(FaultTree::Event, "computedProbability")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "computedProbability" in klass.__dict__:
            descriptor = klass.__dict__["computedProbability"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_assignedProbability():
    assert hasattr(FaultTree::Event, "assignedProbability")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "assignedProbability" in klass.__dict__:
            descriptor = klass.__dict__["assignedProbability"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_k():
    assert hasattr(FaultTree::Event, "k")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "k" in klass.__dict__:
            descriptor = klass.__dict__["k"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_name():
    assert hasattr(FaultTree::Event, "name")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_scale():
    assert hasattr(FaultTree::Event, "scale")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_message():
    assert hasattr(FaultTree::Event, "message")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_subEventLogic():
    assert hasattr(FaultTree::Event, "subEventLogic")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "subEventLogic" in klass.__dict__:
            descriptor = klass.__dict__["subEventLogic"]
            break
    assert isinstance(descriptor, property)

def test_faulttree::event_has_referenceCount():
    assert hasattr(FaultTree::Event, "referenceCount")
    descriptor = None
    for klass in FaultTree::Event.__mro__:
        if "referenceCount" in klass.__dict__:
            descriptor = klass.__dict__["referenceCount"]
            break
    assert isinstance(descriptor, property)

def test_logicoperation_exists():
    # Check that the Enumeration exists
    assert LogicOperation is not None

def test_logicoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperation]
    expected_literals = [
        "kOf",
        "kOrless",
        "Xor",
        "kOrmore",
        "PriorityAnd",
        "Or",
        "And",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperation"

def test_faulttreetype_exists():
    # Check that the Enumeration exists
    assert FaultTreeType is not None

def test_faulttreetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FaultTreeType]
    expected_literals = [
        "CompositeParts",
        "FaultTrace",
        "MinimalCutSet",
        "FaultTree",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FaultTreeType"

def test_eventtype_exists():
    # Check that the Enumeration exists
    assert EventType is not None

def test_eventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventType]
    expected_literals = [
        "Basic",
        "Undeveloped",
        "Intermediate",
        "External",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventType"


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
FaultTree::FaultTree_strategy = st.builds(
    FaultTree::FaultTree,
    name=
        safe_text,
    message=
        safe_text,
    faultTreeType=
        safe_text
)
FaultTree::EObject_strategy = st.builds(
    FaultTree::EObject,
)
FaultTree::Event_strategy = st.builds(
    FaultTree::Event,
    type=
        safe_text,
    computedProbability=
        safe_text,
    assignedProbability=
        safe_text,
    k=
        st.integers(),
    name=
        safe_text,
    scale=
        safe_text,
    message=
        safe_text,
    subEventLogic=
        safe_text,
    referenceCount=
        st.integers()
)

@given(instance=FaultTree::FaultTree_strategy)
@settings(max_examples=50)
def test_faulttree::faulttree_instantiation(instance):
    assert isinstance(instance, FaultTree::FaultTree)

@given(instance=FaultTree::FaultTree_strategy)
def test_faulttree::faulttree_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FaultTree::FaultTree_strategy)
def test_faulttree::faulttree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FaultTree::FaultTree_strategy)
def test_faulttree::faulttree_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=FaultTree::FaultTree_strategy)
def test_faulttree::faulttree_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=FaultTree::FaultTree_strategy)
def test_faulttree::faulttree_faultTreeType_type(instance):
    assert isinstance(instance.faultTreeType, str)


@given(instance=FaultTree::FaultTree_strategy)
def test_faulttree::faulttree_faultTreeType_setter(instance):
    original = instance.faultTreeType
    instance.faultTreeType = original
    assert instance.faultTreeType == original

@given(instance=FaultTree::EObject_strategy)
@settings(max_examples=50)
def test_faulttree::eobject_instantiation(instance):
    assert isinstance(instance, FaultTree::EObject)

@given(instance=FaultTree::Event_strategy)
@settings(max_examples=50)
def test_faulttree::event_instantiation(instance):
    assert isinstance(instance, FaultTree::Event)

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_computedProbability_type(instance):
    assert isinstance(instance.computedProbability, str)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_computedProbability_setter(instance):
    original = instance.computedProbability
    instance.computedProbability = original
    assert instance.computedProbability == original

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_assignedProbability_type(instance):
    assert isinstance(instance.assignedProbability, str)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_assignedProbability_setter(instance):
    original = instance.assignedProbability
    instance.assignedProbability = original
    assert instance.assignedProbability == original

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_k_type(instance):
    assert isinstance(instance.k, int)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_k_setter(instance):
    original = instance.k
    instance.k = original
    assert instance.k == original

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_subEventLogic_type(instance):
    assert isinstance(instance.subEventLogic, str)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_subEventLogic_setter(instance):
    original = instance.subEventLogic
    instance.subEventLogic = original
    assert instance.subEventLogic == original

@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_referenceCount_type(instance):
    assert isinstance(instance.referenceCount, int)


@given(instance=FaultTree::Event_strategy)
def test_faulttree::event_referenceCount_setter(instance):
    original = instance.referenceCount
    instance.referenceCount = original
    assert instance.referenceCount == original
