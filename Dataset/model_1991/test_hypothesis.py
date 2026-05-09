import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trace::EStructuralFeature,
    trace::EObject,
    trace::InputElement,
    trace::OutputFile,
    trace::Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(trace::EStructuralFeature)


def test_trace::estructuralfeature_constructor_exists():
    assert callable(trace::EStructuralFeature.__init__)


def test_trace::estructuralfeature_constructor_args():
    sig = inspect.signature(trace::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_trace::eobject_is_not_abstract():
    assert not inspect.isabstract(trace::EObject)


def test_trace::eobject_constructor_exists():
    assert callable(trace::EObject.__init__)


def test_trace::eobject_constructor_args():
    sig = inspect.signature(trace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_trace::inputelement_is_not_abstract():
    assert not inspect.isabstract(trace::InputElement)


def test_trace::inputelement_constructor_exists():
    assert callable(trace::InputElement.__init__)


def test_trace::inputelement_constructor_args():
    sig = inspect.signature(trace::InputElement.__init__)
    params = list(sig.parameters.keys())



def test_trace::outputfile_is_not_abstract():
    assert not inspect.isabstract(trace::OutputFile)


def test_trace::outputfile_constructor_exists():
    assert callable(trace::OutputFile.__init__)


def test_trace::outputfile_constructor_args():
    sig = inspect.signature(trace::OutputFile.__init__)
    params = list(sig.parameters.keys())
    assert "outlet" in params, "Missing parameter 'outlet'"
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_trace::outputfile_has_outlet():
    assert hasattr(trace::OutputFile, "outlet")
    descriptor = None
    for klass in trace::OutputFile.__mro__:
        if "outlet" in klass.__dict__:
            descriptor = klass.__dict__["outlet"]
            break
    assert isinstance(descriptor, property)

def test_trace::outputfile_has_fileName():
    assert hasattr(trace::OutputFile, "fileName")
    descriptor = None
    for klass in trace::OutputFile.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
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
trace::EStructuralFeature_strategy = st.builds(
    trace::EStructuralFeature,
)
trace::EObject_strategy = st.builds(
    trace::EObject,
)
trace::InputElement_strategy = st.builds(
    trace::InputElement,
)
trace::OutputFile_strategy = st.builds(
    trace::OutputFile,
    outlet=
        safe_text,
    fileName=
        safe_text
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)

@given(instance=trace::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_trace::estructuralfeature_instantiation(instance):
    assert isinstance(instance, trace::EStructuralFeature)

@given(instance=trace::EObject_strategy)
@settings(max_examples=50)
def test_trace::eobject_instantiation(instance):
    assert isinstance(instance, trace::EObject)

@given(instance=trace::InputElement_strategy)
@settings(max_examples=50)
def test_trace::inputelement_instantiation(instance):
    assert isinstance(instance, trace::InputElement)

@given(instance=trace::OutputFile_strategy)
@settings(max_examples=50)
def test_trace::outputfile_instantiation(instance):
    assert isinstance(instance, trace::OutputFile)

@given(instance=trace::OutputFile_strategy)
def test_trace::outputfile_outlet_type(instance):
    assert isinstance(instance.outlet, str)


@given(instance=trace::OutputFile_strategy)
def test_trace::outputfile_outlet_setter(instance):
    original = instance.outlet
    instance.outlet = original
    assert instance.outlet == original

@given(instance=trace::OutputFile_strategy)
def test_trace::outputfile_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=trace::OutputFile_strategy)
def test_trace::outputfile_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)
