import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EValue,
    trace::ETuplePartValue,
    trace::EMappingContext,
    trace::EMappingOperation,
    trace::ObjectToTraceRecordMapEntry,
    trace::MappingOperationToTraceRecordMapEntry,
    trace::TraceRecord,
    trace::EObject,
    MappingOperation,
    trace::EValue,
    trace::VarParameterValue,
    trace::EMappingResults,
    trace::EMappingParameters,
    trace::Trace,
    EDirectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_evalue_is_not_abstract():
    assert not inspect.isabstract(EValue)


def test_evalue_constructor_exists():
    assert callable(EValue.__init__)


def test_evalue_constructor_args():
    sig = inspect.signature(EValue.__init__)
    params = list(sig.parameters.keys())



def test_trace::etuplepartvalue_is_not_abstract():
    assert not inspect.isabstract(trace::ETuplePartValue)


def test_trace::etuplepartvalue_constructor_exists():
    assert callable(trace::ETuplePartValue.__init__)


def test_trace::etuplepartvalue_constructor_args():
    sig = inspect.signature(trace::ETuplePartValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trace::etuplepartvalue_has_name():
    assert hasattr(trace::ETuplePartValue, "name")
    descriptor = None
    for klass in trace::ETuplePartValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trace::emappingcontext_is_not_abstract():
    assert not inspect.isabstract(trace::EMappingContext)


def test_trace::emappingcontext_constructor_exists():
    assert callable(trace::EMappingContext.__init__)


def test_trace::emappingcontext_constructor_args():
    sig = inspect.signature(trace::EMappingContext.__init__)
    params = list(sig.parameters.keys())



def test_trace::emappingoperation_is_not_abstract():
    assert not inspect.isabstract(trace::EMappingOperation)


def test_trace::emappingoperation_constructor_exists():
    assert callable(trace::EMappingOperation.__init__)


def test_trace::emappingoperation_constructor_args():
    sig = inspect.signature(trace::EMappingOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "module" in params, "Missing parameter 'module'"
    assert "package" in params, "Missing parameter 'package'"

def test_trace::emappingoperation_has_name():
    assert hasattr(trace::EMappingOperation, "name")
    descriptor = None
    for klass in trace::EMappingOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_trace::emappingoperation_has_module():
    assert hasattr(trace::EMappingOperation, "module")
    descriptor = None
    for klass in trace::EMappingOperation.__mro__:
        if "module" in klass.__dict__:
            descriptor = klass.__dict__["module"]
            break
    assert isinstance(descriptor, property)

def test_trace::emappingoperation_has_package():
    assert hasattr(trace::EMappingOperation, "package")
    descriptor = None
    for klass in trace::EMappingOperation.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_trace::objecttotracerecordmapentry_is_not_abstract():
    assert not inspect.isabstract(trace::ObjectToTraceRecordMapEntry)


def test_trace::objecttotracerecordmapentry_constructor_exists():
    assert callable(trace::ObjectToTraceRecordMapEntry.__init__)


def test_trace::objecttotracerecordmapentry_constructor_args():
    sig = inspect.signature(trace::ObjectToTraceRecordMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_trace::objecttotracerecordmapentry_has_key():
    assert hasattr(trace::ObjectToTraceRecordMapEntry, "key")
    descriptor = None
    for klass in trace::ObjectToTraceRecordMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_trace::mappingoperationtotracerecordmapentry_is_not_abstract():
    assert not inspect.isabstract(trace::MappingOperationToTraceRecordMapEntry)


def test_trace::mappingoperationtotracerecordmapentry_constructor_exists():
    assert callable(trace::MappingOperationToTraceRecordMapEntry.__init__)


def test_trace::mappingoperationtotracerecordmapentry_constructor_args():
    sig = inspect.signature(trace::MappingOperationToTraceRecordMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_trace::tracerecord_is_not_abstract():
    assert not inspect.isabstract(trace::TraceRecord)


def test_trace::tracerecord_constructor_exists():
    assert callable(trace::TraceRecord.__init__)


def test_trace::tracerecord_constructor_args():
    sig = inspect.signature(trace::TraceRecord.__init__)
    params = list(sig.parameters.keys())



def test_trace::eobject_is_not_abstract():
    assert not inspect.isabstract(trace::EObject)


def test_trace::eobject_constructor_exists():
    assert callable(trace::EObject.__init__)


def test_trace::eobject_constructor_args():
    sig = inspect.signature(trace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mappingoperation_is_not_abstract():
    assert not inspect.isabstract(MappingOperation)


def test_mappingoperation_constructor_exists():
    assert callable(MappingOperation.__init__)


def test_mappingoperation_constructor_args():
    sig = inspect.signature(MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_trace::evalue_is_not_abstract():
    assert not inspect.isabstract(trace::EValue)


def test_trace::evalue_constructor_exists():
    assert callable(trace::EValue.__init__)


def test_trace::evalue_constructor_args():
    sig = inspect.signature(trace::EValue.__init__)
    params = list(sig.parameters.keys())
    assert "oclObject" in params, "Missing parameter 'oclObject'"
    assert "collectionType" in params, "Missing parameter 'collectionType'"
    assert "primitiveValue" in params, "Missing parameter 'primitiveValue'"

def test_trace::evalue_has_oclObject():
    assert hasattr(trace::EValue, "oclObject")
    descriptor = None
    for klass in trace::EValue.__mro__:
        if "oclObject" in klass.__dict__:
            descriptor = klass.__dict__["oclObject"]
            break
    assert isinstance(descriptor, property)

def test_trace::evalue_has_collectionType():
    assert hasattr(trace::EValue, "collectionType")
    descriptor = None
    for klass in trace::EValue.__mro__:
        if "collectionType" in klass.__dict__:
            descriptor = klass.__dict__["collectionType"]
            break
    assert isinstance(descriptor, property)

def test_trace::evalue_has_primitiveValue():
    assert hasattr(trace::EValue, "primitiveValue")
    descriptor = None
    for klass in trace::EValue.__mro__:
        if "primitiveValue" in klass.__dict__:
            descriptor = klass.__dict__["primitiveValue"]
            break
    assert isinstance(descriptor, property)



def test_trace::varparametervalue_is_not_abstract():
    assert not inspect.isabstract(trace::VarParameterValue)


def test_trace::varparametervalue_constructor_exists():
    assert callable(trace::VarParameterValue.__init__)


def test_trace::varparametervalue_constructor_args():
    sig = inspect.signature(trace::VarParameterValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_trace::varparametervalue_has_name():
    assert hasattr(trace::VarParameterValue, "name")
    descriptor = None
    for klass in trace::VarParameterValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_trace::varparametervalue_has_type():
    assert hasattr(trace::VarParameterValue, "type")
    descriptor = None
    for klass in trace::VarParameterValue.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_trace::varparametervalue_has_kind():
    assert hasattr(trace::VarParameterValue, "kind")
    descriptor = None
    for klass in trace::VarParameterValue.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_trace::emappingresults_is_not_abstract():
    assert not inspect.isabstract(trace::EMappingResults)


def test_trace::emappingresults_constructor_exists():
    assert callable(trace::EMappingResults.__init__)


def test_trace::emappingresults_constructor_args():
    sig = inspect.signature(trace::EMappingResults.__init__)
    params = list(sig.parameters.keys())



def test_trace::emappingparameters_is_not_abstract():
    assert not inspect.isabstract(trace::EMappingParameters)


def test_trace::emappingparameters_constructor_exists():
    assert callable(trace::EMappingParameters.__init__)


def test_trace::emappingparameters_constructor_args():
    sig = inspect.signature(trace::EMappingParameters.__init__)
    params = list(sig.parameters.keys())



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
    params = list(sig.parameters.keys())

def test_edirectionkind_exists():
    # Check that the Enumeration exists
    assert EDirectionKind is not None

def test_edirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EDirectionKind]
    expected_literals = [
        "INOUT",
        "IN",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EDirectionKind"


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
EValue_strategy = st.builds(
    EValue,
)
trace::ETuplePartValue_strategy = st.builds(
    trace::ETuplePartValue,
    name=
        safe_text
)
trace::EMappingContext_strategy = st.builds(
    trace::EMappingContext,
)
trace::EMappingOperation_strategy = st.builds(
    trace::EMappingOperation,
    name=
        safe_text,
    module=
        safe_text,
    package=
        safe_text
)
trace::ObjectToTraceRecordMapEntry_strategy = st.builds(
    trace::ObjectToTraceRecordMapEntry,
    key=
        safe_text
)
trace::MappingOperationToTraceRecordMapEntry_strategy = st.builds(
    trace::MappingOperationToTraceRecordMapEntry,
)
trace::TraceRecord_strategy = st.builds(
    trace::TraceRecord,
)
trace::EObject_strategy = st.builds(
    trace::EObject,
)
MappingOperation_strategy = st.builds(
    MappingOperation,
)
trace::EValue_strategy = st.builds(
    trace::EValue,
    oclObject=
        safe_text,
    collectionType=
        safe_text,
    primitiveValue=
        safe_text
)
trace::VarParameterValue_strategy = st.builds(
    trace::VarParameterValue,
    name=
        safe_text,
    type=
        safe_text,
    kind=
        safe_text
)
trace::EMappingResults_strategy = st.builds(
    trace::EMappingResults,
)
trace::EMappingParameters_strategy = st.builds(
    trace::EMappingParameters,
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)

@given(instance=EValue_strategy)
@settings(max_examples=50)
def test_evalue_instantiation(instance):
    assert isinstance(instance, EValue)

@given(instance=trace::ETuplePartValue_strategy)
@settings(max_examples=50)
def test_trace::etuplepartvalue_instantiation(instance):
    assert isinstance(instance, trace::ETuplePartValue)

@given(instance=trace::ETuplePartValue_strategy)
def test_trace::etuplepartvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trace::ETuplePartValue_strategy)
def test_trace::etuplepartvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trace::EMappingContext_strategy)
@settings(max_examples=50)
def test_trace::emappingcontext_instantiation(instance):
    assert isinstance(instance, trace::EMappingContext)

@given(instance=trace::EMappingOperation_strategy)
@settings(max_examples=50)
def test_trace::emappingoperation_instantiation(instance):
    assert isinstance(instance, trace::EMappingOperation)

@given(instance=trace::EMappingOperation_strategy)
def test_trace::emappingoperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trace::EMappingOperation_strategy)
def test_trace::emappingoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trace::EMappingOperation_strategy)
def test_trace::emappingoperation_module_type(instance):
    assert isinstance(instance.module, str)


@given(instance=trace::EMappingOperation_strategy)
def test_trace::emappingoperation_module_setter(instance):
    original = instance.module
    instance.module = original
    assert instance.module == original

@given(instance=trace::EMappingOperation_strategy)
def test_trace::emappingoperation_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=trace::EMappingOperation_strategy)
def test_trace::emappingoperation_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=trace::ObjectToTraceRecordMapEntry_strategy)
@settings(max_examples=50)
def test_trace::objecttotracerecordmapentry_instantiation(instance):
    assert isinstance(instance, trace::ObjectToTraceRecordMapEntry)

@given(instance=trace::ObjectToTraceRecordMapEntry_strategy)
def test_trace::objecttotracerecordmapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=trace::ObjectToTraceRecordMapEntry_strategy)
def test_trace::objecttotracerecordmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=trace::MappingOperationToTraceRecordMapEntry_strategy)
@settings(max_examples=50)
def test_trace::mappingoperationtotracerecordmapentry_instantiation(instance):
    assert isinstance(instance, trace::MappingOperationToTraceRecordMapEntry)

@given(instance=trace::TraceRecord_strategy)
@settings(max_examples=50)
def test_trace::tracerecord_instantiation(instance):
    assert isinstance(instance, trace::TraceRecord)

@given(instance=trace::EObject_strategy)
@settings(max_examples=50)
def test_trace::eobject_instantiation(instance):
    assert isinstance(instance, trace::EObject)

@given(instance=MappingOperation_strategy)
@settings(max_examples=50)
def test_mappingoperation_instantiation(instance):
    assert isinstance(instance, MappingOperation)

@given(instance=trace::EValue_strategy)
@settings(max_examples=50)
def test_trace::evalue_instantiation(instance):
    assert isinstance(instance, trace::EValue)

@given(instance=trace::EValue_strategy)
def test_trace::evalue_oclObject_type(instance):
    assert isinstance(instance.oclObject, str)


@given(instance=trace::EValue_strategy)
def test_trace::evalue_oclObject_setter(instance):
    original = instance.oclObject
    instance.oclObject = original
    assert instance.oclObject == original

@given(instance=trace::EValue_strategy)
def test_trace::evalue_collectionType_type(instance):
    assert isinstance(instance.collectionType, str)


@given(instance=trace::EValue_strategy)
def test_trace::evalue_collectionType_setter(instance):
    original = instance.collectionType
    instance.collectionType = original
    assert instance.collectionType == original

@given(instance=trace::EValue_strategy)
def test_trace::evalue_primitiveValue_type(instance):
    assert isinstance(instance.primitiveValue, str)


@given(instance=trace::EValue_strategy)
def test_trace::evalue_primitiveValue_setter(instance):
    original = instance.primitiveValue
    instance.primitiveValue = original
    assert instance.primitiveValue == original

@given(instance=trace::VarParameterValue_strategy)
@settings(max_examples=50)
def test_trace::varparametervalue_instantiation(instance):
    assert isinstance(instance, trace::VarParameterValue)

@given(instance=trace::VarParameterValue_strategy)
def test_trace::varparametervalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trace::VarParameterValue_strategy)
def test_trace::varparametervalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=trace::VarParameterValue_strategy)
def test_trace::varparametervalue_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=trace::VarParameterValue_strategy)
def test_trace::varparametervalue_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=trace::VarParameterValue_strategy)
def test_trace::varparametervalue_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=trace::VarParameterValue_strategy)
def test_trace::varparametervalue_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=trace::EMappingResults_strategy)
@settings(max_examples=50)
def test_trace::emappingresults_instantiation(instance):
    assert isinstance(instance, trace::EMappingResults)

@given(instance=trace::EMappingParameters_strategy)
@settings(max_examples=50)
def test_trace::emappingparameters_instantiation(instance):
    assert isinstance(instance, trace::EMappingParameters)

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=trace::Trace_strategy)
@settings(max_examples=30)
def test_trace::trace_addrecordbysource_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addRecordBySource(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addRecordBySource).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addRecordBySource' in trace::Trace is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addRecordBySource' in trace::Trace did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addRecordBySource' in trace::Trace is not implemented or raised an error")
