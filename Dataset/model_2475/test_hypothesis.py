import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    textlink_Region,
    textlink_EObject,
    ModelLocation,
    textlink_EmfModelLocation,
    TraceLinkEnd,
    textlink_TraceLinkEnd,
    textlink_TextLocation,
    textlink_TraceLink,
    textlink_Trace,
    textlink_ModelLocation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_textlink_region_is_not_abstract():
    assert not inspect.isabstract(textlink_Region)


def test_textlink_region_constructor_exists():
    assert callable(textlink_Region.__init__)


def test_textlink_region_constructor_args():
    sig = inspect.signature(textlink_Region.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_textlink_region_has_length():
    assert hasattr(textlink_Region, "length")
    descriptor = None
    for klass in textlink_Region.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_textlink_region_has_offset():
    assert hasattr(textlink_Region, "offset")
    descriptor = None
    for klass in textlink_Region.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_textlink_eobject_is_not_abstract():
    assert not inspect.isabstract(textlink_EObject)


def test_textlink_eobject_constructor_exists():
    assert callable(textlink_EObject.__init__)


def test_textlink_eobject_constructor_args():
    sig = inspect.signature(textlink_EObject.__init__)
    params = list(sig.parameters.keys())



def test_modellocation_is_not_abstract():
    assert not inspect.isabstract(ModelLocation)


def test_modellocation_constructor_exists():
    assert callable(ModelLocation.__init__)


def test_modellocation_constructor_args():
    sig = inspect.signature(ModelLocation.__init__)
    params = list(sig.parameters.keys())



def test_textlink_emfmodellocation_is_not_abstract():
    assert not inspect.isabstract(textlink_EmfModelLocation)


def test_textlink_emfmodellocation_constructor_exists():
    assert callable(textlink_EmfModelLocation.__init__)


def test_textlink_emfmodellocation_constructor_args():
    sig = inspect.signature(textlink_EmfModelLocation.__init__)
    params = list(sig.parameters.keys())



def test_tracelinkend_is_not_abstract():
    assert not inspect.isabstract(TraceLinkEnd)


def test_tracelinkend_constructor_exists():
    assert callable(TraceLinkEnd.__init__)


def test_tracelinkend_constructor_args():
    sig = inspect.signature(TraceLinkEnd.__init__)
    params = list(sig.parameters.keys())



def test_textlink_tracelinkend_is_not_abstract():
    assert not inspect.isabstract(textlink_TraceLinkEnd)


def test_textlink_tracelinkend_constructor_exists():
    assert callable(textlink_TraceLinkEnd.__init__)


def test_textlink_tracelinkend_constructor_args():
    sig = inspect.signature(textlink_TraceLinkEnd.__init__)
    params = list(sig.parameters.keys())



def test_textlink_textlocation_is_not_abstract():
    assert not inspect.isabstract(textlink_TextLocation)


def test_textlink_textlocation_constructor_exists():
    assert callable(textlink_TextLocation.__init__)


def test_textlink_textlocation_constructor_args():
    sig = inspect.signature(textlink_TextLocation.__init__)
    params = list(sig.parameters.keys())
    assert "resource" in params, "Missing parameter 'resource'"

def test_textlink_textlocation_has_resource():
    assert hasattr(textlink_TextLocation, "resource")
    descriptor = None
    for klass in textlink_TextLocation.__mro__:
        if "resource" in klass.__dict__:
            descriptor = klass.__dict__["resource"]
            break
    assert isinstance(descriptor, property)



def test_textlink_tracelink_is_not_abstract():
    assert not inspect.isabstract(textlink_TraceLink)


def test_textlink_tracelink_constructor_exists():
    assert callable(textlink_TraceLink.__init__)


def test_textlink_tracelink_constructor_args():
    sig = inspect.signature(textlink_TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_textlink_trace_is_not_abstract():
    assert not inspect.isabstract(textlink_Trace)


def test_textlink_trace_constructor_exists():
    assert callable(textlink_Trace.__init__)


def test_textlink_trace_constructor_args():
    sig = inspect.signature(textlink_Trace.__init__)
    params = list(sig.parameters.keys())



def test_textlink_modellocation_is_not_abstract():
    assert not inspect.isabstract(textlink_ModelLocation)


def test_textlink_modellocation_constructor_exists():
    assert callable(textlink_ModelLocation.__init__)


def test_textlink_modellocation_constructor_args():
    sig = inspect.signature(textlink_ModelLocation.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_textlink_modellocation_has_propertyName():
    assert hasattr(textlink_ModelLocation, "propertyName")
    descriptor = None
    for klass in textlink_ModelLocation.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)


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
textlink_Region_strategy = st.builds(
    textlink_Region,
    length=
        safe_text,
    offset=
        safe_text
)
textlink_EObject_strategy = st.builds(
    textlink_EObject,
)
ModelLocation_strategy = st.builds(
    ModelLocation,
)
textlink_EmfModelLocation_strategy = st.builds(
    textlink_EmfModelLocation,
)
TraceLinkEnd_strategy = st.builds(
    TraceLinkEnd,
)
textlink_TraceLinkEnd_strategy = st.builds(
    textlink_TraceLinkEnd,
)
textlink_TextLocation_strategy = st.builds(
    textlink_TextLocation,
    resource=
        safe_text
)
textlink_TraceLink_strategy = st.builds(
    textlink_TraceLink,
)
textlink_Trace_strategy = st.builds(
    textlink_Trace,
)
textlink_ModelLocation_strategy = st.builds(
    textlink_ModelLocation,
    propertyName=
        safe_text
)

@given(instance=textlink_Region_strategy)
@settings(max_examples=50)
def test_textlink_region_instantiation(instance):
    assert isinstance(instance, textlink_Region)



@given(instance=textlink_Region_strategy)
def test_textlink_region_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=textlink_Region_strategy)
def test_textlink_region_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=textlink_EObject_strategy)
@settings(max_examples=50)
def test_textlink_eobject_instantiation(instance):
    assert isinstance(instance, textlink_EObject)

@given(instance=ModelLocation_strategy)
@settings(max_examples=50)
def test_modellocation_instantiation(instance):
    assert isinstance(instance, ModelLocation)

@given(instance=textlink_EmfModelLocation_strategy)
@settings(max_examples=50)
def test_textlink_emfmodellocation_instantiation(instance):
    assert isinstance(instance, textlink_EmfModelLocation)

@given(instance=TraceLinkEnd_strategy)
@settings(max_examples=50)
def test_tracelinkend_instantiation(instance):
    assert isinstance(instance, TraceLinkEnd)

@given(instance=textlink_TraceLinkEnd_strategy)
@settings(max_examples=50)
def test_textlink_tracelinkend_instantiation(instance):
    assert isinstance(instance, textlink_TraceLinkEnd)

@given(instance=textlink_TextLocation_strategy)
@settings(max_examples=50)
def test_textlink_textlocation_instantiation(instance):
    assert isinstance(instance, textlink_TextLocation)



@given(instance=textlink_TextLocation_strategy)
def test_textlink_textlocation_resource_setter(instance):
    original = instance.resource
    instance.resource = original
    assert instance.resource == original

@given(instance=textlink_TraceLink_strategy)
@settings(max_examples=50)
def test_textlink_tracelink_instantiation(instance):
    assert isinstance(instance, textlink_TraceLink)

@given(instance=textlink_Trace_strategy)
@settings(max_examples=50)
def test_textlink_trace_instantiation(instance):
    assert isinstance(instance, textlink_Trace)

@given(instance=textlink_ModelLocation_strategy)
@settings(max_examples=50)
def test_textlink_modellocation_instantiation(instance):
    assert isinstance(instance, textlink_ModelLocation)



@given(instance=textlink_ModelLocation_strategy)
def test_textlink_modellocation_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original
