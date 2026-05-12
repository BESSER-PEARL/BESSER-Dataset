import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FaultTree_EObject,
    FaultTree_Event,
    FaultTree_FaultTree,
    FaultTreeType,
    EventType,
    LogicOperation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faulttree_eobject_is_not_abstract():
    assert not inspect.isabstract(FaultTree_EObject)


def test_faulttree_eobject_constructor_exists():
    assert callable(FaultTree_EObject.__init__)


def test_faulttree_eobject_constructor_args():
    sig = inspect.signature(FaultTree_EObject.__init__)
    params = list(sig.parameters.keys())



def test_faulttree_event_is_not_abstract():
    assert not inspect.isabstract(FaultTree_Event)


def test_faulttree_event_constructor_exists():
    assert callable(FaultTree_Event.__init__)


def test_faulttree_event_constructor_args():
    sig = inspect.signature(FaultTree_Event.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sharedEvent" in params, "Missing parameter 'sharedEvent'"
    assert "subEventLogic" in params, "Missing parameter 'subEventLogic'"
    assert "k" in params, "Missing parameter 'k'"
    assert "assignedProbability" in params, "Missing parameter 'assignedProbability'"
    assert "message" in params, "Missing parameter 'message'"
    assert "computedProbability" in params, "Missing parameter 'computedProbability'"
    assert "referenceCount" in params, "Missing parameter 'referenceCount'"

def test_faulttree_event_has_type():
    assert hasattr(FaultTree_Event, "type")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_name():
    assert hasattr(FaultTree_Event, "name")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_sharedEvent():
    assert hasattr(FaultTree_Event, "sharedEvent")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "sharedEvent" in klass.__dict__:
            descriptor = klass.__dict__["sharedEvent"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_subEventLogic():
    assert hasattr(FaultTree_Event, "subEventLogic")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "subEventLogic" in klass.__dict__:
            descriptor = klass.__dict__["subEventLogic"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_k():
    assert hasattr(FaultTree_Event, "k")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "k" in klass.__dict__:
            descriptor = klass.__dict__["k"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_assignedProbability():
    assert hasattr(FaultTree_Event, "assignedProbability")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "assignedProbability" in klass.__dict__:
            descriptor = klass.__dict__["assignedProbability"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_message():
    assert hasattr(FaultTree_Event, "message")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_computedProbability():
    assert hasattr(FaultTree_Event, "computedProbability")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "computedProbability" in klass.__dict__:
            descriptor = klass.__dict__["computedProbability"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_event_has_referenceCount():
    assert hasattr(FaultTree_Event, "referenceCount")
    descriptor = None
    for klass in FaultTree_Event.__mro__:
        if "referenceCount" in klass.__dict__:
            descriptor = klass.__dict__["referenceCount"]
            break
    assert isinstance(descriptor, property)



def test_faulttree_faulttree_is_not_abstract():
    assert not inspect.isabstract(FaultTree_FaultTree)


def test_faulttree_faulttree_constructor_exists():
    assert callable(FaultTree_FaultTree.__init__)


def test_faulttree_faulttree_constructor_args():
    sig = inspect.signature(FaultTree_FaultTree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "message" in params, "Missing parameter 'message'"
    assert "faultTreeType" in params, "Missing parameter 'faultTreeType'"

def test_faulttree_faulttree_has_name():
    assert hasattr(FaultTree_FaultTree, "name")
    descriptor = None
    for klass in FaultTree_FaultTree.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_faulttree_has_message():
    assert hasattr(FaultTree_FaultTree, "message")
    descriptor = None
    for klass in FaultTree_FaultTree.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_faulttree_faulttree_has_faultTreeType():
    assert hasattr(FaultTree_FaultTree, "faultTreeType")
    descriptor = None
    for klass in FaultTree_FaultTree.__mro__:
        if "faultTreeType" in klass.__dict__:
            descriptor = klass.__dict__["faultTreeType"]
            break
    assert isinstance(descriptor, property)

def test_faulttreetype_exists():
    # Check that the Enumeration exists
    assert FaultTreeType is not None

def test_faulttreetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FaultTreeType]
    expected_literals = [
        "FaultTrace",
        "CompositeParts",
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
        "Intermediate",
        "Undeveloped",
        "Basic",
        "External",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventType"

def test_logicoperation_exists():
    # Check that the Enumeration exists
    assert LogicOperation is not None

def test_logicoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperation]
    expected_literals = [
        "kOrless",
        "PriorityAnd",
        "kOrmore",
        "Or",
        "Xor",
        "And",
        "kOf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperation"


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
FaultTree_EObject_strategy = st.builds(
    FaultTree_EObject,
)
FaultTree_Event_strategy = st.builds(
    FaultTree_Event,
    type=
        safe_text,
    name=
        safe_text,
    sharedEvent=
        st.booleans(),
    subEventLogic=
        safe_text,
    k=
        st.integers(),
    assignedProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    message=
        safe_text,
    computedProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    referenceCount=
        st.integers()
)
FaultTree_FaultTree_strategy = st.builds(
    FaultTree_FaultTree,
    name=
        safe_text,
    message=
        safe_text,
    faultTreeType=
        safe_text
)

@given(instance=FaultTree_EObject_strategy)
@settings(max_examples=50)
def test_faulttree_eobject_instantiation(instance):
    assert isinstance(instance, FaultTree_EObject)

@given(instance=FaultTree_Event_strategy)
@settings(max_examples=50)
def test_faulttree_event_instantiation(instance):
    assert isinstance(instance, FaultTree_Event)



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_sharedEvent_setter(instance):
    original = instance.sharedEvent
    instance.sharedEvent = original
    assert instance.sharedEvent == original



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_subEventLogic_setter(instance):
    original = instance.subEventLogic
    instance.subEventLogic = original
    assert instance.subEventLogic == original



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_k_setter(instance):
    original = instance.k
    instance.k = original
    assert instance.k == original



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_assignedProbability_setter(instance):
    original = instance.assignedProbability
    instance.assignedProbability = original
    assert instance.assignedProbability == original



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_computedProbability_setter(instance):
    original = instance.computedProbability
    instance.computedProbability = original
    assert instance.computedProbability == original



@given(instance=FaultTree_Event_strategy)
def test_faulttree_event_referenceCount_setter(instance):
    original = instance.referenceCount
    instance.referenceCount = original
    assert instance.referenceCount == original

@given(instance=FaultTree_FaultTree_strategy)
@settings(max_examples=50)
def test_faulttree_faulttree_instantiation(instance):
    assert isinstance(instance, FaultTree_FaultTree)



@given(instance=FaultTree_FaultTree_strategy)
def test_faulttree_faulttree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FaultTree_FaultTree_strategy)
def test_faulttree_faulttree_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=FaultTree_FaultTree_strategy)
def test_faulttree_faulttree_faultTreeType_setter(instance):
    original = instance.faultTreeType
    instance.faultTreeType = original
    assert instance.faultTreeType == original
