import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ube_EntityModel,
    Type,
    ube_Entity,
    ube_DataType,
    NamedElement,
    ube_Feature,
    ube_Type,
    ube_NamedElement,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ube_entitymodel_is_not_abstract():
    assert not inspect.isabstract(ube_EntityModel)


def test_ube_entitymodel_constructor_exists():
    assert callable(ube_EntityModel.__init__)


def test_ube_entitymodel_constructor_args():
    sig = inspect.signature(ube_EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ube_entity_is_not_abstract():
    assert not inspect.isabstract(ube_Entity)


def test_ube_entity_constructor_exists():
    assert callable(ube_Entity.__init__)


def test_ube_entity_constructor_args():
    sig = inspect.signature(ube_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_ube_entity_has_abstract():
    assert hasattr(ube_Entity, "abstract")
    descriptor = None
    for klass in ube_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_ube_datatype_is_not_abstract():
    assert not inspect.isabstract(ube_DataType)


def test_ube_datatype_constructor_exists():
    assert callable(ube_DataType.__init__)


def test_ube_datatype_constructor_args():
    sig = inspect.signature(ube_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ube_feature_is_not_abstract():
    assert not inspect.isabstract(ube_Feature)


def test_ube_feature_constructor_exists():
    assert callable(ube_Feature.__init__)


def test_ube_feature_constructor_args():
    sig = inspect.signature(ube_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ube_feature_has_kind():
    assert hasattr(ube_Feature, "kind")
    descriptor = None
    for klass in ube_Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ube_type_is_not_abstract():
    assert not inspect.isabstract(ube_Type)


def test_ube_type_constructor_exists():
    assert callable(ube_Type.__init__)


def test_ube_type_constructor_args():
    sig = inspect.signature(ube_Type.__init__)
    params = list(sig.parameters.keys())



def test_ube_namedelement_is_not_abstract():
    assert not inspect.isabstract(ube_NamedElement)


def test_ube_namedelement_constructor_exists():
    assert callable(ube_NamedElement.__init__)


def test_ube_namedelement_constructor_args():
    sig = inspect.signature(ube_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ube_namedelement_has_name():
    assert hasattr(ube_NamedElement, "name")
    descriptor = None
    for klass in ube_NamedElement.__mro__:
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
        "containment",
        "attribute",
        "reference",
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
ube_EntityModel_strategy = st.builds(
    ube_EntityModel,
)
Type_strategy = st.builds(
    Type,
)
ube_Entity_strategy = st.builds(
    ube_Entity,
    abstract=
        st.booleans()
)
ube_DataType_strategy = st.builds(
    ube_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ube_Feature_strategy = st.builds(
    ube_Feature,
    kind=
        safe_text
)
ube_Type_strategy = st.builds(
    ube_Type,
)
ube_NamedElement_strategy = st.builds(
    ube_NamedElement,
    name=
        safe_text
)

@given(instance=ube_EntityModel_strategy)
@settings(max_examples=50)
def test_ube_entitymodel_instantiation(instance):
    assert isinstance(instance, ube_EntityModel)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ube_Entity_strategy)
@settings(max_examples=50)
def test_ube_entity_instantiation(instance):
    assert isinstance(instance, ube_Entity)



@given(instance=ube_Entity_strategy)
def test_ube_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=ube_DataType_strategy)
@settings(max_examples=50)
def test_ube_datatype_instantiation(instance):
    assert isinstance(instance, ube_DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ube_Feature_strategy)
@settings(max_examples=50)
def test_ube_feature_instantiation(instance):
    assert isinstance(instance, ube_Feature)



@given(instance=ube_Feature_strategy)
def test_ube_feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ube_Type_strategy)
@settings(max_examples=50)
def test_ube_type_instantiation(instance):
    assert isinstance(instance, ube_Type)

@given(instance=ube_NamedElement_strategy)
@settings(max_examples=50)
def test_ube_namedelement_instantiation(instance):
    assert isinstance(instance, ube_NamedElement)



@given(instance=ube_NamedElement_strategy)
def test_ube_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
