import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trace_EStructuralFeature,
    trace_EObject,
    trace_InputElement,
    trace_OutputFile,
    trace_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(trace_EStructuralFeature)


def test_trace_estructuralfeature_constructor_exists():
    assert callable(trace_EStructuralFeature.__init__)


def test_trace_estructuralfeature_constructor_args():
    sig = inspect.signature(trace_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_trace_eobject_is_not_abstract():
    assert not inspect.isabstract(trace_EObject)


def test_trace_eobject_constructor_exists():
    assert callable(trace_EObject.__init__)


def test_trace_eobject_constructor_args():
    sig = inspect.signature(trace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_trace_inputelement_is_not_abstract():
    assert not inspect.isabstract(trace_InputElement)


def test_trace_inputelement_constructor_exists():
    assert callable(trace_InputElement.__init__)


def test_trace_inputelement_constructor_args():
    sig = inspect.signature(trace_InputElement.__init__)
    params = list(sig.parameters.keys())



def test_trace_outputfile_is_not_abstract():
    assert not inspect.isabstract(trace_OutputFile)


def test_trace_outputfile_constructor_exists():
    assert callable(trace_OutputFile.__init__)


def test_trace_outputfile_constructor_args():
    sig = inspect.signature(trace_OutputFile.__init__)
    params = list(sig.parameters.keys())
    assert "outlet" in params, "Missing parameter 'outlet'"
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_trace_outputfile_has_outlet():
    assert hasattr(trace_OutputFile, "outlet")
    descriptor = None
    for klass in trace_OutputFile.__mro__:
        if "outlet" in klass.__dict__:
            descriptor = klass.__dict__["outlet"]
            break
    assert isinstance(descriptor, property)

def test_trace_outputfile_has_fileName():
    assert hasattr(trace_OutputFile, "fileName")
    descriptor = None
    for klass in trace_OutputFile.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(trace_Trace.__init__)
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
trace_EStructuralFeature_strategy = st.builds(
    trace_EStructuralFeature,
)
trace_EObject_strategy = st.builds(
    trace_EObject,
)
trace_InputElement_strategy = st.builds(
    trace_InputElement,
)
trace_OutputFile_strategy = st.builds(
    trace_OutputFile,
    outlet=
        safe_text,
    fileName=
        safe_text
)
trace_Trace_strategy = st.builds(
    trace_Trace,
)

@given(instance=trace_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_trace_estructuralfeature_instantiation(instance):
    assert isinstance(instance, trace_EStructuralFeature)

@given(instance=trace_EObject_strategy)
@settings(max_examples=50)
def test_trace_eobject_instantiation(instance):
    assert isinstance(instance, trace_EObject)

@given(instance=trace_InputElement_strategy)
@settings(max_examples=50)
def test_trace_inputelement_instantiation(instance):
    assert isinstance(instance, trace_InputElement)

@given(instance=trace_OutputFile_strategy)
@settings(max_examples=50)
def test_trace_outputfile_instantiation(instance):
    assert isinstance(instance, trace_OutputFile)



@given(instance=trace_OutputFile_strategy)
def test_trace_outputfile_outlet_setter(instance):
    original = instance.outlet
    instance.outlet = original
    assert instance.outlet == original



@given(instance=trace_OutputFile_strategy)
def test_trace_outputfile_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)
