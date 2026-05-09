import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trace::EClass,
    trace::ReferenceMapping,
    trace::AttributeMapping,
    trace::ClassMapping,
    trace::Trace,
    trace::EStructuralFeature,
    trace::EReference,
    trace::EAttribute,
    ReferenceMappingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::eclass_is_not_abstract():
    assert not inspect.isabstract(trace::EClass)


def test_trace::eclass_constructor_exists():
    assert callable(trace::EClass.__init__)


def test_trace::eclass_constructor_args():
    sig = inspect.signature(trace::EClass.__init__)
    params = list(sig.parameters.keys())



def test_trace::referencemapping_is_not_abstract():
    assert not inspect.isabstract(trace::ReferenceMapping)


def test_trace::referencemapping_constructor_exists():
    assert callable(trace::ReferenceMapping.__init__)


def test_trace::referencemapping_constructor_args():
    sig = inspect.signature(trace::ReferenceMapping.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_trace::referencemapping_has_type():
    assert hasattr(trace::ReferenceMapping, "type")
    descriptor = None
    for klass in trace::ReferenceMapping.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_trace::attributemapping_is_not_abstract():
    assert not inspect.isabstract(trace::AttributeMapping)


def test_trace::attributemapping_constructor_exists():
    assert callable(trace::AttributeMapping.__init__)


def test_trace::attributemapping_constructor_args():
    sig = inspect.signature(trace::AttributeMapping.__init__)
    params = list(sig.parameters.keys())



def test_trace::classmapping_is_not_abstract():
    assert not inspect.isabstract(trace::ClassMapping)


def test_trace::classmapping_constructor_exists():
    assert callable(trace::ClassMapping.__init__)


def test_trace::classmapping_constructor_args():
    sig = inspect.signature(trace::ClassMapping.__init__)
    params = list(sig.parameters.keys())



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
    params = list(sig.parameters.keys())



def test_trace::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(trace::EStructuralFeature)


def test_trace::estructuralfeature_constructor_exists():
    assert callable(trace::EStructuralFeature.__init__)


def test_trace::estructuralfeature_constructor_args():
    sig = inspect.signature(trace::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_trace::ereference_is_not_abstract():
    assert not inspect.isabstract(trace::EReference)


def test_trace::ereference_constructor_exists():
    assert callable(trace::EReference.__init__)


def test_trace::ereference_constructor_args():
    sig = inspect.signature(trace::EReference.__init__)
    params = list(sig.parameters.keys())



def test_trace::eattribute_is_not_abstract():
    assert not inspect.isabstract(trace::EAttribute)


def test_trace::eattribute_constructor_exists():
    assert callable(trace::EAttribute.__init__)


def test_trace::eattribute_constructor_args():
    sig = inspect.signature(trace::EAttribute.__init__)
    params = list(sig.parameters.keys())

def test_referencemappingtype_exists():
    # Check that the Enumeration exists
    assert ReferenceMappingType is not None

def test_referencemappingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceMappingType]
    expected_literals = [
        "MAPPED",
        "NONE",
        "TRANSLATED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceMappingType"


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
trace::EClass_strategy = st.builds(
    trace::EClass,
)
trace::ReferenceMapping_strategy = st.builds(
    trace::ReferenceMapping,
    type=
        safe_text
)
trace::AttributeMapping_strategy = st.builds(
    trace::AttributeMapping,
)
trace::ClassMapping_strategy = st.builds(
    trace::ClassMapping,
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)
trace::EStructuralFeature_strategy = st.builds(
    trace::EStructuralFeature,
)
trace::EReference_strategy = st.builds(
    trace::EReference,
)
trace::EAttribute_strategy = st.builds(
    trace::EAttribute,
)

@given(instance=trace::EClass_strategy)
@settings(max_examples=50)
def test_trace::eclass_instantiation(instance):
    assert isinstance(instance, trace::EClass)

@given(instance=trace::ReferenceMapping_strategy)
@settings(max_examples=50)
def test_trace::referencemapping_instantiation(instance):
    assert isinstance(instance, trace::ReferenceMapping)

@given(instance=trace::ReferenceMapping_strategy)
def test_trace::referencemapping_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=trace::ReferenceMapping_strategy)
def test_trace::referencemapping_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=trace::AttributeMapping_strategy)
@settings(max_examples=50)
def test_trace::attributemapping_instantiation(instance):
    assert isinstance(instance, trace::AttributeMapping)

@given(instance=trace::ClassMapping_strategy)
@settings(max_examples=50)
def test_trace::classmapping_instantiation(instance):
    assert isinstance(instance, trace::ClassMapping)

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

@given(instance=trace::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_trace::estructuralfeature_instantiation(instance):
    assert isinstance(instance, trace::EStructuralFeature)

@given(instance=trace::EReference_strategy)
@settings(max_examples=50)
def test_trace::ereference_instantiation(instance):
    assert isinstance(instance, trace::EReference)

@given(instance=trace::EAttribute_strategy)
@settings(max_examples=50)
def test_trace::eattribute_instantiation(instance):
    assert isinstance(instance, trace::EAttribute)
