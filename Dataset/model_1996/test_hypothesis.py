import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trace_EClass,
    trace_ReferenceMapping,
    trace_AttributeMapping,
    trace_ClassMapping,
    trace_Trace,
    trace_EStructuralFeature,
    trace_EReference,
    trace_EAttribute,
    ReferenceMappingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace_eclass_is_not_abstract():
    assert not inspect.isabstract(trace_EClass)


def test_trace_eclass_constructor_exists():
    assert callable(trace_EClass.__init__)


def test_trace_eclass_constructor_args():
    sig = inspect.signature(trace_EClass.__init__)
    params = list(sig.parameters.keys())



def test_trace_referencemapping_is_not_abstract():
    assert not inspect.isabstract(trace_ReferenceMapping)


def test_trace_referencemapping_constructor_exists():
    assert callable(trace_ReferenceMapping.__init__)


def test_trace_referencemapping_constructor_args():
    sig = inspect.signature(trace_ReferenceMapping.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_trace_referencemapping_has_type():
    assert hasattr(trace_ReferenceMapping, "type")
    descriptor = None
    for klass in trace_ReferenceMapping.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_trace_attributemapping_is_not_abstract():
    assert not inspect.isabstract(trace_AttributeMapping)


def test_trace_attributemapping_constructor_exists():
    assert callable(trace_AttributeMapping.__init__)


def test_trace_attributemapping_constructor_args():
    sig = inspect.signature(trace_AttributeMapping.__init__)
    params = list(sig.parameters.keys())



def test_trace_classmapping_is_not_abstract():
    assert not inspect.isabstract(trace_ClassMapping)


def test_trace_classmapping_constructor_exists():
    assert callable(trace_ClassMapping.__init__)


def test_trace_classmapping_constructor_args():
    sig = inspect.signature(trace_ClassMapping.__init__)
    params = list(sig.parameters.keys())



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(trace_Trace.__init__)
    params = list(sig.parameters.keys())



def test_trace_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(trace_EStructuralFeature)


def test_trace_estructuralfeature_constructor_exists():
    assert callable(trace_EStructuralFeature.__init__)


def test_trace_estructuralfeature_constructor_args():
    sig = inspect.signature(trace_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_trace_ereference_is_not_abstract():
    assert not inspect.isabstract(trace_EReference)


def test_trace_ereference_constructor_exists():
    assert callable(trace_EReference.__init__)


def test_trace_ereference_constructor_args():
    sig = inspect.signature(trace_EReference.__init__)
    params = list(sig.parameters.keys())



def test_trace_eattribute_is_not_abstract():
    assert not inspect.isabstract(trace_EAttribute)


def test_trace_eattribute_constructor_exists():
    assert callable(trace_EAttribute.__init__)


def test_trace_eattribute_constructor_args():
    sig = inspect.signature(trace_EAttribute.__init__)
    params = list(sig.parameters.keys())

def test_referencemappingtype_exists():
    # Check that the Enumeration exists
    assert ReferenceMappingType is not None

def test_referencemappingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceMappingType]
    expected_literals = [
        "NONE",
        "MAPPED",
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
trace_EClass_strategy = st.builds(
    trace_EClass,
)
trace_ReferenceMapping_strategy = st.builds(
    trace_ReferenceMapping,
    type=
        safe_text
)
trace_AttributeMapping_strategy = st.builds(
    trace_AttributeMapping,
)
trace_ClassMapping_strategy = st.builds(
    trace_ClassMapping,
)
trace_Trace_strategy = st.builds(
    trace_Trace,
)
trace_EStructuralFeature_strategy = st.builds(
    trace_EStructuralFeature,
)
trace_EReference_strategy = st.builds(
    trace_EReference,
)
trace_EAttribute_strategy = st.builds(
    trace_EAttribute,
)

@given(instance=trace_EClass_strategy)
@settings(max_examples=50)
def test_trace_eclass_instantiation(instance):
    assert isinstance(instance, trace_EClass)

@given(instance=trace_ReferenceMapping_strategy)
@settings(max_examples=50)
def test_trace_referencemapping_instantiation(instance):
    assert isinstance(instance, trace_ReferenceMapping)



@given(instance=trace_ReferenceMapping_strategy)
def test_trace_referencemapping_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=trace_AttributeMapping_strategy)
@settings(max_examples=50)
def test_trace_attributemapping_instantiation(instance):
    assert isinstance(instance, trace_AttributeMapping)

@given(instance=trace_ClassMapping_strategy)
@settings(max_examples=50)
def test_trace_classmapping_instantiation(instance):
    assert isinstance(instance, trace_ClassMapping)

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)

@given(instance=trace_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_trace_estructuralfeature_instantiation(instance):
    assert isinstance(instance, trace_EStructuralFeature)

@given(instance=trace_EReference_strategy)
@settings(max_examples=50)
def test_trace_ereference_instantiation(instance):
    assert isinstance(instance, trace_EReference)

@given(instance=trace_EAttribute_strategy)
@settings(max_examples=50)
def test_trace_eattribute_instantiation(instance):
    assert isinstance(instance, trace_EAttribute)
