import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StructuralFeature,
    uml_15_to_20_associationEndToProperty_StructuralFeature,
    uml_15_to_20_associationEndToProperty_Operation,
    uml_15_to_20_associationEndToProperty_Property,
    uml_15_to_20_associationEndToProperty_Association,
    uml_15_to_20_associationEndToProperty_Class,
    uml_15_to_20_associationEndToProperty_Model,
    AggregationKind,
    ScopeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml_15_to_20_associationendtoproperty_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(uml_15_to_20_associationEndToProperty_StructuralFeature)


def test_uml_15_to_20_associationendtoproperty_structuralfeature_constructor_exists():
    assert callable(uml_15_to_20_associationEndToProperty_StructuralFeature.__init__)


def test_uml_15_to_20_associationendtoproperty_structuralfeature_constructor_args():
    sig = inspect.signature(uml_15_to_20_associationEndToProperty_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_uml_15_to_20_associationendtoproperty_structuralfeature_has_isStatic():
    assert hasattr(uml_15_to_20_associationEndToProperty_StructuralFeature, "isStatic")
    descriptor = None
    for klass in uml_15_to_20_associationEndToProperty_StructuralFeature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_uml_15_to_20_associationendtoproperty_operation_is_not_abstract():
    assert not inspect.isabstract(uml_15_to_20_associationEndToProperty_Operation)


def test_uml_15_to_20_associationendtoproperty_operation_constructor_exists():
    assert callable(uml_15_to_20_associationEndToProperty_Operation.__init__)


def test_uml_15_to_20_associationendtoproperty_operation_constructor_args():
    sig = inspect.signature(uml_15_to_20_associationEndToProperty_Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml_15_to_20_associationendtoproperty_property_is_not_abstract():
    assert not inspect.isabstract(uml_15_to_20_associationEndToProperty_Property)


def test_uml_15_to_20_associationendtoproperty_property_constructor_exists():
    assert callable(uml_15_to_20_associationEndToProperty_Property.__init__)


def test_uml_15_to_20_associationendtoproperty_property_constructor_args():
    sig = inspect.signature(uml_15_to_20_associationEndToProperty_Property.__init__)
    params = list(sig.parameters.keys())



def test_uml_15_to_20_associationendtoproperty_association_is_not_abstract():
    assert not inspect.isabstract(uml_15_to_20_associationEndToProperty_Association)


def test_uml_15_to_20_associationendtoproperty_association_constructor_exists():
    assert callable(uml_15_to_20_associationEndToProperty_Association.__init__)


def test_uml_15_to_20_associationendtoproperty_association_constructor_args():
    sig = inspect.signature(uml_15_to_20_associationEndToProperty_Association.__init__)
    params = list(sig.parameters.keys())



def test_uml_15_to_20_associationendtoproperty_class_is_not_abstract():
    assert not inspect.isabstract(uml_15_to_20_associationEndToProperty_Class)


def test_uml_15_to_20_associationendtoproperty_class_constructor_exists():
    assert callable(uml_15_to_20_associationEndToProperty_Class.__init__)


def test_uml_15_to_20_associationendtoproperty_class_constructor_args():
    sig = inspect.signature(uml_15_to_20_associationEndToProperty_Class.__init__)
    params = list(sig.parameters.keys())



def test_uml_15_to_20_associationendtoproperty_model_is_not_abstract():
    assert not inspect.isabstract(uml_15_to_20_associationEndToProperty_Model)


def test_uml_15_to_20_associationendtoproperty_model_constructor_exists():
    assert callable(uml_15_to_20_associationEndToProperty_Model.__init__)


def test_uml_15_to_20_associationendtoproperty_model_constructor_args():
    sig = inspect.signature(uml_15_to_20_associationEndToProperty_Model.__init__)
    params = list(sig.parameters.keys())

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "shared",
        "none",
        "composite",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"

def test_scopekind_exists():
    # Check that the Enumeration exists
    assert ScopeKind is not None

def test_scopekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScopeKind]
    expected_literals = [
        "instance",
        "classifier",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeKind"


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
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
uml_15_to_20_associationEndToProperty_StructuralFeature_strategy = st.builds(
    uml_15_to_20_associationEndToProperty_StructuralFeature,
    isStatic=
        st.booleans()
)
uml_15_to_20_associationEndToProperty_Operation_strategy = st.builds(
    uml_15_to_20_associationEndToProperty_Operation,
)
uml_15_to_20_associationEndToProperty_Property_strategy = st.builds(
    uml_15_to_20_associationEndToProperty_Property,
)
uml_15_to_20_associationEndToProperty_Association_strategy = st.builds(
    uml_15_to_20_associationEndToProperty_Association,
)
uml_15_to_20_associationEndToProperty_Class_strategy = st.builds(
    uml_15_to_20_associationEndToProperty_Class,
)
uml_15_to_20_associationEndToProperty_Model_strategy = st.builds(
    uml_15_to_20_associationEndToProperty_Model,
)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=uml_15_to_20_associationEndToProperty_StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml_15_to_20_associationendtoproperty_structuralfeature_instantiation(instance):
    assert isinstance(instance, uml_15_to_20_associationEndToProperty_StructuralFeature)



@given(instance=uml_15_to_20_associationEndToProperty_StructuralFeature_strategy)
def test_uml_15_to_20_associationendtoproperty_structuralfeature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=uml_15_to_20_associationEndToProperty_Operation_strategy)
@settings(max_examples=50)
def test_uml_15_to_20_associationendtoproperty_operation_instantiation(instance):
    assert isinstance(instance, uml_15_to_20_associationEndToProperty_Operation)

@given(instance=uml_15_to_20_associationEndToProperty_Property_strategy)
@settings(max_examples=50)
def test_uml_15_to_20_associationendtoproperty_property_instantiation(instance):
    assert isinstance(instance, uml_15_to_20_associationEndToProperty_Property)

@given(instance=uml_15_to_20_associationEndToProperty_Association_strategy)
@settings(max_examples=50)
def test_uml_15_to_20_associationendtoproperty_association_instantiation(instance):
    assert isinstance(instance, uml_15_to_20_associationEndToProperty_Association)

@given(instance=uml_15_to_20_associationEndToProperty_Class_strategy)
@settings(max_examples=50)
def test_uml_15_to_20_associationendtoproperty_class_instantiation(instance):
    assert isinstance(instance, uml_15_to_20_associationEndToProperty_Class)

@given(instance=uml_15_to_20_associationEndToProperty_Model_strategy)
@settings(max_examples=50)
def test_uml_15_to_20_associationendtoproperty_model_instantiation(instance):
    assert isinstance(instance, uml_15_to_20_associationEndToProperty_Model)
