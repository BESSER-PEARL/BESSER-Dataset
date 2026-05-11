import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ValueChangeEvent,
    trace::NumberValueChangeEvent,
    trace::DataSizeValueChangeEvent,
    trace::DurationValueChangeEvent,
    trace::ObjectValueChangeEvent,
    trace::EObject,
    trace::EStructuralFeature,
    Event,
    trace::ValueChangeEvent,
    trace::ResourceEvent,
    trace::MessageEvent,
    trace::SchedulingEvent,
    EModelElement,
    trace::Slice,
    trace::Properties,
    trace::Event,
    trace::Trace,
    MessageEventKind,
    ResourceEventKind,
    SchedulingEventKind,
    SliceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_valuechangeevent_is_not_abstract():
    assert not inspect.isabstract(ValueChangeEvent)


def test_valuechangeevent_constructor_exists():
    assert callable(ValueChangeEvent.__init__)


def test_valuechangeevent_constructor_args():
    sig = inspect.signature(ValueChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_trace::numbervaluechangeevent_is_not_abstract():
    assert not inspect.isabstract(trace::NumberValueChangeEvent)


def test_trace::numbervaluechangeevent_constructor_exists():
    assert callable(trace::NumberValueChangeEvent.__init__)


def test_trace::numbervaluechangeevent_constructor_args():
    sig = inspect.signature(trace::NumberValueChangeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_trace::numbervaluechangeevent_has_value():
    assert hasattr(trace::NumberValueChangeEvent, "value")
    descriptor = None
    for klass in trace::NumberValueChangeEvent.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_trace::datasizevaluechangeevent_is_not_abstract():
    assert not inspect.isabstract(trace::DataSizeValueChangeEvent)


def test_trace::datasizevaluechangeevent_constructor_exists():
    assert callable(trace::DataSizeValueChangeEvent.__init__)


def test_trace::datasizevaluechangeevent_constructor_args():
    sig = inspect.signature(trace::DataSizeValueChangeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_trace::datasizevaluechangeevent_has_value():
    assert hasattr(trace::DataSizeValueChangeEvent, "value")
    descriptor = None
    for klass in trace::DataSizeValueChangeEvent.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_trace::durationvaluechangeevent_is_not_abstract():
    assert not inspect.isabstract(trace::DurationValueChangeEvent)


def test_trace::durationvaluechangeevent_constructor_exists():
    assert callable(trace::DurationValueChangeEvent.__init__)


def test_trace::durationvaluechangeevent_constructor_args():
    sig = inspect.signature(trace::DurationValueChangeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_trace::durationvaluechangeevent_has_value():
    assert hasattr(trace::DurationValueChangeEvent, "value")
    descriptor = None
    for klass in trace::DurationValueChangeEvent.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_trace::objectvaluechangeevent_is_not_abstract():
    assert not inspect.isabstract(trace::ObjectValueChangeEvent)


def test_trace::objectvaluechangeevent_constructor_exists():
    assert callable(trace::ObjectValueChangeEvent.__init__)


def test_trace::objectvaluechangeevent_constructor_args():
    sig = inspect.signature(trace::ObjectValueChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_trace::eobject_is_not_abstract():
    assert not inspect.isabstract(trace::EObject)


def test_trace::eobject_constructor_exists():
    assert callable(trace::EObject.__init__)


def test_trace::eobject_constructor_args():
    sig = inspect.signature(trace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_trace::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(trace::EStructuralFeature)


def test_trace::estructuralfeature_constructor_exists():
    assert callable(trace::EStructuralFeature.__init__)


def test_trace::estructuralfeature_constructor_args():
    sig = inspect.signature(trace::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_trace::valuechangeevent_is_not_abstract():
    assert not inspect.isabstract(trace::ValueChangeEvent)


def test_trace::valuechangeevent_constructor_exists():
    assert callable(trace::ValueChangeEvent.__init__)


def test_trace::valuechangeevent_constructor_args():
    sig = inspect.signature(trace::ValueChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_trace::resourceevent_is_not_abstract():
    assert not inspect.isabstract(trace::ResourceEvent)


def test_trace::resourceevent_constructor_exists():
    assert callable(trace::ResourceEvent.__init__)


def test_trace::resourceevent_constructor_args():
    sig = inspect.signature(trace::ResourceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_trace::resourceevent_has_kind():
    assert hasattr(trace::ResourceEvent, "kind")
    descriptor = None
    for klass in trace::ResourceEvent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_trace::messageevent_is_not_abstract():
    assert not inspect.isabstract(trace::MessageEvent)


def test_trace::messageevent_constructor_exists():
    assert callable(trace::MessageEvent.__init__)


def test_trace::messageevent_constructor_args():
    sig = inspect.signature(trace::MessageEvent.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_trace::messageevent_has_kind():
    assert hasattr(trace::MessageEvent, "kind")
    descriptor = None
    for klass in trace::MessageEvent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_trace::schedulingevent_is_not_abstract():
    assert not inspect.isabstract(trace::SchedulingEvent)


def test_trace::schedulingevent_constructor_exists():
    assert callable(trace::SchedulingEvent.__init__)


def test_trace::schedulingevent_constructor_args():
    sig = inspect.signature(trace::SchedulingEvent.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_trace::schedulingevent_has_kind():
    assert hasattr(trace::SchedulingEvent, "kind")
    descriptor = None
    for klass in trace::SchedulingEvent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_trace::slice_is_not_abstract():
    assert not inspect.isabstract(trace::Slice)


def test_trace::slice_constructor_exists():
    assert callable(trace::Slice.__init__)


def test_trace::slice_constructor_args():
    sig = inspect.signature(trace::Slice.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "kindLabel" in params, "Missing parameter 'kindLabel'"

def test_trace::slice_has_name():
    assert hasattr(trace::Slice, "name")
    descriptor = None
    for klass in trace::Slice.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_trace::slice_has_kind():
    assert hasattr(trace::Slice, "kind")
    descriptor = None
    for klass in trace::Slice.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_trace::slice_has_kindLabel():
    assert hasattr(trace::Slice, "kindLabel")
    descriptor = None
    for klass in trace::Slice.__mro__:
        if "kindLabel" in klass.__dict__:
            descriptor = klass.__dict__["kindLabel"]
            break
    assert isinstance(descriptor, property)



def test_trace::properties_is_not_abstract():
    assert not inspect.isabstract(trace::Properties)


def test_trace::properties_constructor_exists():
    assert callable(trace::Properties.__init__)


def test_trace::properties_constructor_args():
    sig = inspect.signature(trace::Properties.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"
    assert "absoluteDeadline" in params, "Missing parameter 'absoluteDeadline'"
    assert "executionTime" in params, "Missing parameter 'executionTime'"
    assert "index" in params, "Missing parameter 'index'"
    assert "responseTime" in params, "Missing parameter 'responseTime'"
    assert "blockingTime" in params, "Missing parameter 'blockingTime'"
    assert "remainingTime" in params, "Missing parameter 'remainingTime'"

def test_trace::properties_has_range():
    assert hasattr(trace::Properties, "range")
    descriptor = None
    for klass in trace::Properties.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_trace::properties_has_absoluteDeadline():
    assert hasattr(trace::Properties, "absoluteDeadline")
    descriptor = None
    for klass in trace::Properties.__mro__:
        if "absoluteDeadline" in klass.__dict__:
            descriptor = klass.__dict__["absoluteDeadline"]
            break
    assert isinstance(descriptor, property)

def test_trace::properties_has_executionTime():
    assert hasattr(trace::Properties, "executionTime")
    descriptor = None
    for klass in trace::Properties.__mro__:
        if "executionTime" in klass.__dict__:
            descriptor = klass.__dict__["executionTime"]
            break
    assert isinstance(descriptor, property)

def test_trace::properties_has_index():
    assert hasattr(trace::Properties, "index")
    descriptor = None
    for klass in trace::Properties.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_trace::properties_has_responseTime():
    assert hasattr(trace::Properties, "responseTime")
    descriptor = None
    for klass in trace::Properties.__mro__:
        if "responseTime" in klass.__dict__:
            descriptor = klass.__dict__["responseTime"]
            break
    assert isinstance(descriptor, property)

def test_trace::properties_has_blockingTime():
    assert hasattr(trace::Properties, "blockingTime")
    descriptor = None
    for klass in trace::Properties.__mro__:
        if "blockingTime" in klass.__dict__:
            descriptor = klass.__dict__["blockingTime"]
            break
    assert isinstance(descriptor, property)

def test_trace::properties_has_remainingTime():
    assert hasattr(trace::Properties, "remainingTime")
    descriptor = None
    for klass in trace::Properties.__mro__:
        if "remainingTime" in klass.__dict__:
            descriptor = klass.__dict__["remainingTime"]
            break
    assert isinstance(descriptor, property)



def test_trace::event_is_not_abstract():
    assert not inspect.isabstract(trace::Event)


def test_trace::event_constructor_exists():
    assert callable(trace::Event.__init__)


def test_trace::event_constructor_args():
    sig = inspect.signature(trace::Event.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"

def test_trace::event_has_timestamp():
    assert hasattr(trace::Event, "timestamp")
    descriptor = None
    for klass in trace::Event.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
    params = list(sig.parameters.keys())
    assert "hostId" in params, "Missing parameter 'hostId'"
    assert "range" in params, "Missing parameter 'range'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_trace::trace_has_hostId():
    assert hasattr(trace::Trace, "hostId")
    descriptor = None
    for klass in trace::Trace.__mro__:
        if "hostId" in klass.__dict__:
            descriptor = klass.__dict__["hostId"]
            break
    assert isinstance(descriptor, property)

def test_trace::trace_has_range():
    assert hasattr(trace::Trace, "range")
    descriptor = None
    for klass in trace::Trace.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_trace::trace_has_precision():
    assert hasattr(trace::Trace, "precision")
    descriptor = None
    for klass in trace::Trace.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_messageeventkind_exists():
    # Check that the Enumeration exists
    assert MessageEventKind is not None

def test_messageeventkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageEventKind]
    expected_literals = [
        "TRANSMITTED",
        "INSTANTIATED",
        "ERROR",
        "RECEIVED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageEventKind"

def test_resourceeventkind_exists():
    # Check that the Enumeration exists
    assert ResourceEventKind is not None

def test_resourceeventkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResourceEventKind]
    expected_literals = [
        "ACQUIRED",
        "REQUESTED",
        "RELEASED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResourceEventKind"

def test_schedulingeventkind_exists():
    # Check that the Enumeration exists
    assert SchedulingEventKind is not None

def test_schedulingeventkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchedulingEventKind]
    expected_literals = [
        "BLOCKED",
        "RUNNING",
        "SUSPENDED",
        "TERMINATED",
        "DEADLINE",
        "ACTIVATED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchedulingEventKind"

def test_slicekind_exists():
    # Check that the Enumeration exists
    assert SliceKind is not None

def test_slicekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SliceKind]
    expected_literals = [
        "OS",
        "TASK",
        "PACKET",
        "FUNCTION_INSTANCE",
        "RESOURCE",
        "AUTOMATON",
        "JOB",
        "FRAME",
        "OTHER",
        "TEMPORAL_CHAIN",
        "STATE",
        "LINK",
        "FUNCTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SliceKind"


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
ValueChangeEvent_strategy = st.builds(
    ValueChangeEvent,
)
trace::NumberValueChangeEvent_strategy = st.builds(
    trace::NumberValueChangeEvent,
    value=
        safe_text
)
trace::DataSizeValueChangeEvent_strategy = st.builds(
    trace::DataSizeValueChangeEvent,
    value=
        safe_text
)
trace::DurationValueChangeEvent_strategy = st.builds(
    trace::DurationValueChangeEvent,
    value=
        safe_text
)
trace::ObjectValueChangeEvent_strategy = st.builds(
    trace::ObjectValueChangeEvent,
)
trace::EObject_strategy = st.builds(
    trace::EObject,
)
trace::EStructuralFeature_strategy = st.builds(
    trace::EStructuralFeature,
)
Event_strategy = st.builds(
    Event,
)
trace::ValueChangeEvent_strategy = st.builds(
    trace::ValueChangeEvent,
)
trace::ResourceEvent_strategy = st.builds(
    trace::ResourceEvent,
    kind=
        safe_text
)
trace::MessageEvent_strategy = st.builds(
    trace::MessageEvent,
    kind=
        safe_text
)
trace::SchedulingEvent_strategy = st.builds(
    trace::SchedulingEvent,
    kind=
        safe_text
)
EModelElement_strategy = st.builds(
    EModelElement,
)
trace::Slice_strategy = st.builds(
    trace::Slice,
    name=
        safe_text,
    kind=
        safe_text,
    kindLabel=
        safe_text
)
trace::Properties_strategy = st.builds(
    trace::Properties,
    range=
        safe_text,
    absoluteDeadline=
        safe_text,
    executionTime=
        safe_text,
    index=
        safe_text,
    responseTime=
        safe_text,
    blockingTime=
        safe_text,
    remainingTime=
        safe_text
)
trace::Event_strategy = st.builds(
    trace::Event,
    timestamp=
        safe_text
)
trace::Trace_strategy = st.builds(
    trace::Trace,
    hostId=
        safe_text,
    range=
        safe_text,
    precision=
        safe_text
)

@given(instance=ValueChangeEvent_strategy)
@settings(max_examples=50)
def test_valuechangeevent_instantiation(instance):
    assert isinstance(instance, ValueChangeEvent)

@given(instance=trace::NumberValueChangeEvent_strategy)
@settings(max_examples=50)
def test_trace::numbervaluechangeevent_instantiation(instance):
    assert isinstance(instance, trace::NumberValueChangeEvent)

@given(instance=trace::NumberValueChangeEvent_strategy)
def test_trace::numbervaluechangeevent_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=trace::NumberValueChangeEvent_strategy)
def test_trace::numbervaluechangeevent_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=trace::DataSizeValueChangeEvent_strategy)
@settings(max_examples=50)
def test_trace::datasizevaluechangeevent_instantiation(instance):
    assert isinstance(instance, trace::DataSizeValueChangeEvent)

@given(instance=trace::DataSizeValueChangeEvent_strategy)
def test_trace::datasizevaluechangeevent_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=trace::DataSizeValueChangeEvent_strategy)
def test_trace::datasizevaluechangeevent_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=trace::DurationValueChangeEvent_strategy)
@settings(max_examples=50)
def test_trace::durationvaluechangeevent_instantiation(instance):
    assert isinstance(instance, trace::DurationValueChangeEvent)

@given(instance=trace::DurationValueChangeEvent_strategy)
def test_trace::durationvaluechangeevent_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=trace::DurationValueChangeEvent_strategy)
def test_trace::durationvaluechangeevent_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=trace::ObjectValueChangeEvent_strategy)
@settings(max_examples=50)
def test_trace::objectvaluechangeevent_instantiation(instance):
    assert isinstance(instance, trace::ObjectValueChangeEvent)

@given(instance=trace::EObject_strategy)
@settings(max_examples=50)
def test_trace::eobject_instantiation(instance):
    assert isinstance(instance, trace::EObject)

@given(instance=trace::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_trace::estructuralfeature_instantiation(instance):
    assert isinstance(instance, trace::EStructuralFeature)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=trace::ValueChangeEvent_strategy)
@settings(max_examples=50)
def test_trace::valuechangeevent_instantiation(instance):
    assert isinstance(instance, trace::ValueChangeEvent)

@given(instance=trace::ResourceEvent_strategy)
@settings(max_examples=50)
def test_trace::resourceevent_instantiation(instance):
    assert isinstance(instance, trace::ResourceEvent)

@given(instance=trace::ResourceEvent_strategy)
def test_trace::resourceevent_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=trace::ResourceEvent_strategy)
def test_trace::resourceevent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=trace::MessageEvent_strategy)
@settings(max_examples=50)
def test_trace::messageevent_instantiation(instance):
    assert isinstance(instance, trace::MessageEvent)

@given(instance=trace::MessageEvent_strategy)
def test_trace::messageevent_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=trace::MessageEvent_strategy)
def test_trace::messageevent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=trace::SchedulingEvent_strategy)
@settings(max_examples=50)
def test_trace::schedulingevent_instantiation(instance):
    assert isinstance(instance, trace::SchedulingEvent)

@given(instance=trace::SchedulingEvent_strategy)
def test_trace::schedulingevent_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=trace::SchedulingEvent_strategy)
def test_trace::schedulingevent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=trace::Slice_strategy)
@settings(max_examples=50)
def test_trace::slice_instantiation(instance):
    assert isinstance(instance, trace::Slice)

@given(instance=trace::Slice_strategy)
def test_trace::slice_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trace::Slice_strategy)
def test_trace::slice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trace::Slice_strategy)
def test_trace::slice_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=trace::Slice_strategy)
def test_trace::slice_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=trace::Slice_strategy)
def test_trace::slice_kindLabel_type(instance):
    assert isinstance(instance.kindLabel, str)


@given(instance=trace::Slice_strategy)
def test_trace::slice_kindLabel_setter(instance):
    original = instance.kindLabel
    instance.kindLabel = original
    assert instance.kindLabel == original

@given(instance=trace::Properties_strategy)
@settings(max_examples=50)
def test_trace::properties_instantiation(instance):
    assert isinstance(instance, trace::Properties)

@given(instance=trace::Properties_strategy)
def test_trace::properties_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=trace::Properties_strategy)
def test_trace::properties_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=trace::Properties_strategy)
def test_trace::properties_absoluteDeadline_type(instance):
    assert isinstance(instance.absoluteDeadline, str)


@given(instance=trace::Properties_strategy)
def test_trace::properties_absoluteDeadline_setter(instance):
    original = instance.absoluteDeadline
    instance.absoluteDeadline = original
    assert instance.absoluteDeadline == original

@given(instance=trace::Properties_strategy)
def test_trace::properties_executionTime_type(instance):
    assert isinstance(instance.executionTime, str)


@given(instance=trace::Properties_strategy)
def test_trace::properties_executionTime_setter(instance):
    original = instance.executionTime
    instance.executionTime = original
    assert instance.executionTime == original

@given(instance=trace::Properties_strategy)
def test_trace::properties_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=trace::Properties_strategy)
def test_trace::properties_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=trace::Properties_strategy)
def test_trace::properties_responseTime_type(instance):
    assert isinstance(instance.responseTime, str)


@given(instance=trace::Properties_strategy)
def test_trace::properties_responseTime_setter(instance):
    original = instance.responseTime
    instance.responseTime = original
    assert instance.responseTime == original

@given(instance=trace::Properties_strategy)
def test_trace::properties_blockingTime_type(instance):
    assert isinstance(instance.blockingTime, str)


@given(instance=trace::Properties_strategy)
def test_trace::properties_blockingTime_setter(instance):
    original = instance.blockingTime
    instance.blockingTime = original
    assert instance.blockingTime == original

@given(instance=trace::Properties_strategy)
def test_trace::properties_remainingTime_type(instance):
    assert isinstance(instance.remainingTime, str)


@given(instance=trace::Properties_strategy)
def test_trace::properties_remainingTime_setter(instance):
    original = instance.remainingTime
    instance.remainingTime = original
    assert instance.remainingTime == original

@given(instance=trace::Event_strategy)
@settings(max_examples=50)
def test_trace::event_instantiation(instance):
    assert isinstance(instance, trace::Event)

@given(instance=trace::Event_strategy)
def test_trace::event_timestamp_type(instance):
    assert isinstance(instance.timestamp, str)


@given(instance=trace::Event_strategy)
def test_trace::event_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

@given(instance=trace::Trace_strategy)
def test_trace::trace_hostId_type(instance):
    assert isinstance(instance.hostId, str)


@given(instance=trace::Trace_strategy)
def test_trace::trace_hostId_setter(instance):
    original = instance.hostId
    instance.hostId = original
    assert instance.hostId == original

@given(instance=trace::Trace_strategy)
def test_trace::trace_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=trace::Trace_strategy)
def test_trace::trace_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=trace::Trace_strategy)
def test_trace::trace_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=trace::Trace_strategy)
def test_trace::trace_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original
