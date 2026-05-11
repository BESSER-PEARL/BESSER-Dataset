import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    textlink::Region,
    textlink::EObject,
    ModelLocation,
    textlink::EmfModelLocation,
    TraceLinkEnd,
    textlink::TraceLinkEnd,
    textlink::TextLocation,
    textlink::TraceLink,
    textlink::Trace,
    textlink::ModelLocation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_textlink::region_is_not_abstract():
    assert not inspect.isabstract(textlink::Region)


def test_textlink::region_constructor_exists():
    assert callable(textlink::Region.__init__)


def test_textlink::region_constructor_args():
    sig = inspect.signature(textlink::Region.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_textlink::region_has_length():
    assert hasattr(textlink::Region, "length")
    descriptor = None
    for klass in textlink::Region.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_textlink::region_has_offset():
    assert hasattr(textlink::Region, "offset")
    descriptor = None
    for klass in textlink::Region.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_textlink::eobject_is_not_abstract():
    assert not inspect.isabstract(textlink::EObject)


def test_textlink::eobject_constructor_exists():
    assert callable(textlink::EObject.__init__)


def test_textlink::eobject_constructor_args():
    sig = inspect.signature(textlink::EObject.__init__)
    params = list(sig.parameters.keys())



def test_modellocation_is_not_abstract():
    assert not inspect.isabstract(ModelLocation)


def test_modellocation_constructor_exists():
    assert callable(ModelLocation.__init__)


def test_modellocation_constructor_args():
    sig = inspect.signature(ModelLocation.__init__)
    params = list(sig.parameters.keys())



def test_textlink::emfmodellocation_is_not_abstract():
    assert not inspect.isabstract(textlink::EmfModelLocation)


def test_textlink::emfmodellocation_constructor_exists():
    assert callable(textlink::EmfModelLocation.__init__)


def test_textlink::emfmodellocation_constructor_args():
    sig = inspect.signature(textlink::EmfModelLocation.__init__)
    params = list(sig.parameters.keys())



def test_tracelinkend_is_not_abstract():
    assert not inspect.isabstract(TraceLinkEnd)


def test_tracelinkend_constructor_exists():
    assert callable(TraceLinkEnd.__init__)


def test_tracelinkend_constructor_args():
    sig = inspect.signature(TraceLinkEnd.__init__)
    params = list(sig.parameters.keys())



def test_textlink::tracelinkend_is_not_abstract():
    assert not inspect.isabstract(textlink::TraceLinkEnd)


def test_textlink::tracelinkend_constructor_exists():
    assert callable(textlink::TraceLinkEnd.__init__)


def test_textlink::tracelinkend_constructor_args():
    sig = inspect.signature(textlink::TraceLinkEnd.__init__)
    params = list(sig.parameters.keys())



def test_textlink::textlocation_is_not_abstract():
    assert not inspect.isabstract(textlink::TextLocation)


def test_textlink::textlocation_constructor_exists():
    assert callable(textlink::TextLocation.__init__)


def test_textlink::textlocation_constructor_args():
    sig = inspect.signature(textlink::TextLocation.__init__)
    params = list(sig.parameters.keys())
    assert "resource" in params, "Missing parameter 'resource'"

def test_textlink::textlocation_has_resource():
    assert hasattr(textlink::TextLocation, "resource")
    descriptor = None
    for klass in textlink::TextLocation.__mro__:
        if "resource" in klass.__dict__:
            descriptor = klass.__dict__["resource"]
            break
    assert isinstance(descriptor, property)



def test_textlink::tracelink_is_not_abstract():
    assert not inspect.isabstract(textlink::TraceLink)


def test_textlink::tracelink_constructor_exists():
    assert callable(textlink::TraceLink.__init__)


def test_textlink::tracelink_constructor_args():
    sig = inspect.signature(textlink::TraceLink.__init__)
    params = list(sig.parameters.keys())



def test_textlink::trace_is_not_abstract():
    assert not inspect.isabstract(textlink::Trace)


def test_textlink::trace_constructor_exists():
    assert callable(textlink::Trace.__init__)


def test_textlink::trace_constructor_args():
    sig = inspect.signature(textlink::Trace.__init__)
    params = list(sig.parameters.keys())



def test_textlink::modellocation_is_not_abstract():
    assert not inspect.isabstract(textlink::ModelLocation)


def test_textlink::modellocation_constructor_exists():
    assert callable(textlink::ModelLocation.__init__)


def test_textlink::modellocation_constructor_args():
    sig = inspect.signature(textlink::ModelLocation.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_textlink::modellocation_has_propertyName():
    assert hasattr(textlink::ModelLocation, "propertyName")
    descriptor = None
    for klass in textlink::ModelLocation.__mro__:
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
textlink::Region_strategy = st.builds(
    textlink::Region,
    length=
        safe_text,
    offset=
        safe_text
)
textlink::EObject_strategy = st.builds(
    textlink::EObject,
)
ModelLocation_strategy = st.builds(
    ModelLocation,
)
textlink::EmfModelLocation_strategy = st.builds(
    textlink::EmfModelLocation,
)
TraceLinkEnd_strategy = st.builds(
    TraceLinkEnd,
)
textlink::TraceLinkEnd_strategy = st.builds(
    textlink::TraceLinkEnd,
)
textlink::TextLocation_strategy = st.builds(
    textlink::TextLocation,
    resource=
        safe_text
)
textlink::TraceLink_strategy = st.builds(
    textlink::TraceLink,
)
textlink::Trace_strategy = st.builds(
    textlink::Trace,
)
textlink::ModelLocation_strategy = st.builds(
    textlink::ModelLocation,
    propertyName=
        safe_text
)

@given(instance=textlink::Region_strategy)
@settings(max_examples=50)
def test_textlink::region_instantiation(instance):
    assert isinstance(instance, textlink::Region)

@given(instance=textlink::Region_strategy)
def test_textlink::region_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=textlink::Region_strategy)
def test_textlink::region_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=textlink::Region_strategy)
def test_textlink::region_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=textlink::Region_strategy)
def test_textlink::region_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=textlink::EObject_strategy)
@settings(max_examples=50)
def test_textlink::eobject_instantiation(instance):
    assert isinstance(instance, textlink::EObject)

@given(instance=ModelLocation_strategy)
@settings(max_examples=50)
def test_modellocation_instantiation(instance):
    assert isinstance(instance, ModelLocation)

@given(instance=textlink::EmfModelLocation_strategy)
@settings(max_examples=50)
def test_textlink::emfmodellocation_instantiation(instance):
    assert isinstance(instance, textlink::EmfModelLocation)

@given(instance=TraceLinkEnd_strategy)
@settings(max_examples=50)
def test_tracelinkend_instantiation(instance):
    assert isinstance(instance, TraceLinkEnd)

@given(instance=textlink::TraceLinkEnd_strategy)
@settings(max_examples=50)
def test_textlink::tracelinkend_instantiation(instance):
    assert isinstance(instance, textlink::TraceLinkEnd)

@given(instance=textlink::TextLocation_strategy)
@settings(max_examples=50)
def test_textlink::textlocation_instantiation(instance):
    assert isinstance(instance, textlink::TextLocation)

@given(instance=textlink::TextLocation_strategy)
def test_textlink::textlocation_resource_type(instance):
    assert isinstance(instance.resource, str)


@given(instance=textlink::TextLocation_strategy)
def test_textlink::textlocation_resource_setter(instance):
    original = instance.resource
    instance.resource = original
    assert instance.resource == original

@given(instance=textlink::TraceLink_strategy)
@settings(max_examples=50)
def test_textlink::tracelink_instantiation(instance):
    assert isinstance(instance, textlink::TraceLink)

@given(instance=textlink::Trace_strategy)
@settings(max_examples=50)
def test_textlink::trace_instantiation(instance):
    assert isinstance(instance, textlink::Trace)

@given(instance=textlink::ModelLocation_strategy)
@settings(max_examples=50)
def test_textlink::modellocation_instantiation(instance):
    assert isinstance(instance, textlink::ModelLocation)

@given(instance=textlink::ModelLocation_strategy)
def test_textlink::modellocation_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=textlink::ModelLocation_strategy)
def test_textlink::modellocation_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original
