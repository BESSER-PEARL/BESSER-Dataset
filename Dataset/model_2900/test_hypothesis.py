import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    forms_EntityModel,
    Type,
    forms_Entity,
    forms_DataType,
    NamedElement,
    forms_Feature,
    forms_Type,
    forms_NamedElement,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_forms_entitymodel_is_not_abstract():
    assert not inspect.isabstract(forms_EntityModel)


def test_forms_entitymodel_constructor_exists():
    assert callable(forms_EntityModel.__init__)


def test_forms_entitymodel_constructor_args():
    sig = inspect.signature(forms_EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_forms_entity_is_not_abstract():
    assert not inspect.isabstract(forms_Entity)


def test_forms_entity_constructor_exists():
    assert callable(forms_Entity.__init__)


def test_forms_entity_constructor_args():
    sig = inspect.signature(forms_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_forms_entity_has_abstract():
    assert hasattr(forms_Entity, "abstract")
    descriptor = None
    for klass in forms_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_forms_datatype_is_not_abstract():
    assert not inspect.isabstract(forms_DataType)


def test_forms_datatype_constructor_exists():
    assert callable(forms_DataType.__init__)


def test_forms_datatype_constructor_args():
    sig = inspect.signature(forms_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_forms_feature_is_not_abstract():
    assert not inspect.isabstract(forms_Feature)


def test_forms_feature_constructor_exists():
    assert callable(forms_Feature.__init__)


def test_forms_feature_constructor_args():
    sig = inspect.signature(forms_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_forms_feature_has_kind():
    assert hasattr(forms_Feature, "kind")
    descriptor = None
    for klass in forms_Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_forms_type_is_not_abstract():
    assert not inspect.isabstract(forms_Type)


def test_forms_type_constructor_exists():
    assert callable(forms_Type.__init__)


def test_forms_type_constructor_args():
    sig = inspect.signature(forms_Type.__init__)
    params = list(sig.parameters.keys())



def test_forms_namedelement_is_not_abstract():
    assert not inspect.isabstract(forms_NamedElement)


def test_forms_namedelement_constructor_exists():
    assert callable(forms_NamedElement.__init__)


def test_forms_namedelement_constructor_args():
    sig = inspect.signature(forms_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_forms_namedelement_has_name():
    assert hasattr(forms_NamedElement, "name")
    descriptor = None
    for klass in forms_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featurekind_exists():
    # Check that the Enumeration exists
    assert FeatureKind is not None

def test_featurekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureKind]
    expected_literals = [
        "attribute",
        "reference",
        "containment",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeatureKind"


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
forms_EntityModel_strategy = st.builds(
    forms_EntityModel,
)
Type_strategy = st.builds(
    Type,
)
forms_Entity_strategy = st.builds(
    forms_Entity,
    abstract=
        st.booleans()
)
forms_DataType_strategy = st.builds(
    forms_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
forms_Feature_strategy = st.builds(
    forms_Feature,
    kind=
        safe_text
)
forms_Type_strategy = st.builds(
    forms_Type,
)
forms_NamedElement_strategy = st.builds(
    forms_NamedElement,
    name=
        safe_text
)

@given(instance=forms_EntityModel_strategy)
@settings(max_examples=50)
def test_forms_entitymodel_instantiation(instance):
    assert isinstance(instance, forms_EntityModel)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=forms_Entity_strategy)
@settings(max_examples=50)
def test_forms_entity_instantiation(instance):
    assert isinstance(instance, forms_Entity)



@given(instance=forms_Entity_strategy)
def test_forms_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=forms_DataType_strategy)
@settings(max_examples=50)
def test_forms_datatype_instantiation(instance):
    assert isinstance(instance, forms_DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=forms_Feature_strategy)
@settings(max_examples=50)
def test_forms_feature_instantiation(instance):
    assert isinstance(instance, forms_Feature)



@given(instance=forms_Feature_strategy)
def test_forms_feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=forms_Type_strategy)
@settings(max_examples=50)
def test_forms_type_instantiation(instance):
    assert isinstance(instance, forms_Type)

@given(instance=forms_NamedElement_strategy)
@settings(max_examples=50)
def test_forms_namedelement_instantiation(instance):
    assert isinstance(instance, forms_NamedElement)



@given(instance=forms_NamedElement_strategy)
def test_forms_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
