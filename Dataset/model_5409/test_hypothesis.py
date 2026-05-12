import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fta_FTA,
    Diagram,
    fta_Condition,
    fta_Event,
    fta_Hazard,
    fta_Diagram,
    GateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fta_fta_is_not_abstract():
    assert not inspect.isabstract(fta_FTA)


def test_fta_fta_constructor_exists():
    assert callable(fta_FTA.__init__)


def test_fta_fta_constructor_args():
    sig = inspect.signature(fta_FTA.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_fta_condition_is_not_abstract():
    assert not inspect.isabstract(fta_Condition)


def test_fta_condition_constructor_exists():
    assert callable(fta_Condition.__init__)


def test_fta_condition_constructor_args():
    sig = inspect.signature(fta_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "GateKind" in params, "Missing parameter 'GateKind'"

def test_fta_condition_has_GateKind():
    assert hasattr(fta_Condition, "GateKind")
    descriptor = None
    for klass in fta_Condition.__mro__:
        if "GateKind" in klass.__dict__:
            descriptor = klass.__dict__["GateKind"]
            break
    assert isinstance(descriptor, property)



def test_fta_event_is_not_abstract():
    assert not inspect.isabstract(fta_Event)


def test_fta_event_constructor_exists():
    assert callable(fta_Event.__init__)


def test_fta_event_constructor_args():
    sig = inspect.signature(fta_Event.__init__)
    params = list(sig.parameters.keys())
    assert "BaseEvent" in params, "Missing parameter 'BaseEvent'"

def test_fta_event_has_BaseEvent():
    assert hasattr(fta_Event, "BaseEvent")
    descriptor = None
    for klass in fta_Event.__mro__:
        if "BaseEvent" in klass.__dict__:
            descriptor = klass.__dict__["BaseEvent"]
            break
    assert isinstance(descriptor, property)



def test_fta_hazard_is_not_abstract():
    assert not inspect.isabstract(fta_Hazard)


def test_fta_hazard_constructor_exists():
    assert callable(fta_Hazard.__init__)


def test_fta_hazard_constructor_args():
    sig = inspect.signature(fta_Hazard.__init__)
    params = list(sig.parameters.keys())



def test_fta_diagram_is_not_abstract():
    assert not inspect.isabstract(fta_Diagram)


def test_fta_diagram_constructor_exists():
    assert callable(fta_Diagram.__init__)


def test_fta_diagram_constructor_args():
    sig = inspect.signature(fta_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "detail" in params, "Missing parameter 'detail'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_fta_diagram_has_detail():
    assert hasattr(fta_Diagram, "detail")
    descriptor = None
    for klass in fta_Diagram.__mro__:
        if "detail" in klass.__dict__:
            descriptor = klass.__dict__["detail"]
            break
    assert isinstance(descriptor, property)

def test_fta_diagram_has_name():
    assert hasattr(fta_Diagram, "name")
    descriptor = None
    for klass in fta_Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fta_diagram_has_id():
    assert hasattr(fta_Diagram, "id")
    descriptor = None
    for klass in fta_Diagram.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_gatetype_exists():
    # Check that the Enumeration exists
    assert GateType is not None

def test_gatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GateType]
    expected_literals = [
        "ORGate",
        "ANDGate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GateType"


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
fta_FTA_strategy = st.builds(
    fta_FTA,
)
Diagram_strategy = st.builds(
    Diagram,
)
fta_Condition_strategy = st.builds(
    fta_Condition,
    GateKind=
        safe_text
)
fta_Event_strategy = st.builds(
    fta_Event,
    BaseEvent=
        st.booleans()
)
fta_Hazard_strategy = st.builds(
    fta_Hazard,
)
fta_Diagram_strategy = st.builds(
    fta_Diagram,
    detail=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)

@given(instance=fta_FTA_strategy)
@settings(max_examples=50)
def test_fta_fta_instantiation(instance):
    assert isinstance(instance, fta_FTA)

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=fta_Condition_strategy)
@settings(max_examples=50)
def test_fta_condition_instantiation(instance):
    assert isinstance(instance, fta_Condition)



@given(instance=fta_Condition_strategy)
def test_fta_condition_GateKind_setter(instance):
    original = instance.GateKind
    instance.GateKind = original
    assert instance.GateKind == original

@given(instance=fta_Event_strategy)
@settings(max_examples=50)
def test_fta_event_instantiation(instance):
    assert isinstance(instance, fta_Event)



@given(instance=fta_Event_strategy)
def test_fta_event_BaseEvent_setter(instance):
    original = instance.BaseEvent
    instance.BaseEvent = original
    assert instance.BaseEvent == original

@given(instance=fta_Hazard_strategy)
@settings(max_examples=50)
def test_fta_hazard_instantiation(instance):
    assert isinstance(instance, fta_Hazard)

@given(instance=fta_Diagram_strategy)
@settings(max_examples=50)
def test_fta_diagram_instantiation(instance):
    assert isinstance(instance, fta_Diagram)



@given(instance=fta_Diagram_strategy)
def test_fta_diagram_detail_setter(instance):
    original = instance.detail
    instance.detail = original
    assert instance.detail == original



@given(instance=fta_Diagram_strategy)
def test_fta_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fta_Diagram_strategy)
def test_fta_diagram_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
