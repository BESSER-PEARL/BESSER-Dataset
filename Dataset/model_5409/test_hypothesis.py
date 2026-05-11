import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fta::FTA,
    Diagram,
    fta::Condition,
    fta::Event,
    fta::Hazard,
    fta::Diagram,
    GateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fta::fta_is_not_abstract():
    assert not inspect.isabstract(fta::FTA)


def test_fta::fta_constructor_exists():
    assert callable(fta::FTA.__init__)


def test_fta::fta_constructor_args():
    sig = inspect.signature(fta::FTA.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_fta::condition_is_not_abstract():
    assert not inspect.isabstract(fta::Condition)


def test_fta::condition_constructor_exists():
    assert callable(fta::Condition.__init__)


def test_fta::condition_constructor_args():
    sig = inspect.signature(fta::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "GateKind" in params, "Missing parameter 'GateKind'"

def test_fta::condition_has_GateKind():
    assert hasattr(fta::Condition, "GateKind")
    descriptor = None
    for klass in fta::Condition.__mro__:
        if "GateKind" in klass.__dict__:
            descriptor = klass.__dict__["GateKind"]
            break
    assert isinstance(descriptor, property)



def test_fta::event_is_not_abstract():
    assert not inspect.isabstract(fta::Event)


def test_fta::event_constructor_exists():
    assert callable(fta::Event.__init__)


def test_fta::event_constructor_args():
    sig = inspect.signature(fta::Event.__init__)
    params = list(sig.parameters.keys())
    assert "BaseEvent" in params, "Missing parameter 'BaseEvent'"

def test_fta::event_has_BaseEvent():
    assert hasattr(fta::Event, "BaseEvent")
    descriptor = None
    for klass in fta::Event.__mro__:
        if "BaseEvent" in klass.__dict__:
            descriptor = klass.__dict__["BaseEvent"]
            break
    assert isinstance(descriptor, property)



def test_fta::hazard_is_not_abstract():
    assert not inspect.isabstract(fta::Hazard)


def test_fta::hazard_constructor_exists():
    assert callable(fta::Hazard.__init__)


def test_fta::hazard_constructor_args():
    sig = inspect.signature(fta::Hazard.__init__)
    params = list(sig.parameters.keys())



def test_fta::diagram_is_not_abstract():
    assert not inspect.isabstract(fta::Diagram)


def test_fta::diagram_constructor_exists():
    assert callable(fta::Diagram.__init__)


def test_fta::diagram_constructor_args():
    sig = inspect.signature(fta::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "detail" in params, "Missing parameter 'detail'"
    assert "name" in params, "Missing parameter 'name'"

def test_fta::diagram_has_id():
    assert hasattr(fta::Diagram, "id")
    descriptor = None
    for klass in fta::Diagram.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_fta::diagram_has_detail():
    assert hasattr(fta::Diagram, "detail")
    descriptor = None
    for klass in fta::Diagram.__mro__:
        if "detail" in klass.__dict__:
            descriptor = klass.__dict__["detail"]
            break
    assert isinstance(descriptor, property)

def test_fta::diagram_has_name():
    assert hasattr(fta::Diagram, "name")
    descriptor = None
    for klass in fta::Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gatetype_exists():
    # Check that the Enumeration exists
    assert GateType is not None

def test_gatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GateType]
    expected_literals = [
        "ANDGate",
        "ORGate",
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
fta::FTA_strategy = st.builds(
    fta::FTA,
)
Diagram_strategy = st.builds(
    Diagram,
)
fta::Condition_strategy = st.builds(
    fta::Condition,
    GateKind=
        safe_text
)
fta::Event_strategy = st.builds(
    fta::Event,
    BaseEvent=
        st.booleans()
)
fta::Hazard_strategy = st.builds(
    fta::Hazard,
)
fta::Diagram_strategy = st.builds(
    fta::Diagram,
    id=
        safe_text,
    detail=
        safe_text,
    name=
        safe_text
)

@given(instance=fta::FTA_strategy)
@settings(max_examples=50)
def test_fta::fta_instantiation(instance):
    assert isinstance(instance, fta::FTA)

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=fta::Condition_strategy)
@settings(max_examples=50)
def test_fta::condition_instantiation(instance):
    assert isinstance(instance, fta::Condition)

@given(instance=fta::Condition_strategy)
def test_fta::condition_GateKind_type(instance):
    assert isinstance(instance.GateKind, str)


@given(instance=fta::Condition_strategy)
def test_fta::condition_GateKind_setter(instance):
    original = instance.GateKind
    instance.GateKind = original
    assert instance.GateKind == original

@given(instance=fta::Event_strategy)
@settings(max_examples=50)
def test_fta::event_instantiation(instance):
    assert isinstance(instance, fta::Event)

@given(instance=fta::Event_strategy)
def test_fta::event_BaseEvent_type(instance):
    assert isinstance(instance.BaseEvent, bool)


@given(instance=fta::Event_strategy)
def test_fta::event_BaseEvent_setter(instance):
    original = instance.BaseEvent
    instance.BaseEvent = original
    assert instance.BaseEvent == original

@given(instance=fta::Hazard_strategy)
@settings(max_examples=50)
def test_fta::hazard_instantiation(instance):
    assert isinstance(instance, fta::Hazard)

@given(instance=fta::Diagram_strategy)
@settings(max_examples=50)
def test_fta::diagram_instantiation(instance):
    assert isinstance(instance, fta::Diagram)

@given(instance=fta::Diagram_strategy)
def test_fta::diagram_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=fta::Diagram_strategy)
def test_fta::diagram_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=fta::Diagram_strategy)
def test_fta::diagram_detail_type(instance):
    assert isinstance(instance.detail, str)


@given(instance=fta::Diagram_strategy)
def test_fta::diagram_detail_setter(instance):
    original = instance.detail
    instance.detail = original
    assert instance.detail == original

@given(instance=fta::Diagram_strategy)
def test_fta::diagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fta::Diagram_strategy)
def test_fta::diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
