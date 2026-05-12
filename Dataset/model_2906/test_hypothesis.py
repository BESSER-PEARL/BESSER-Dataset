import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bombXML_NamedElement,
    bombXML_EntityModel,
    Type,
    bombXML_Entity,
    bombXML_DataType,
    NamedElement,
    bombXML_Feature,
    bombXML_Type,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bombxml_namedelement_is_not_abstract():
    assert not inspect.isabstract(bombXML_NamedElement)


def test_bombxml_namedelement_constructor_exists():
    assert callable(bombXML_NamedElement.__init__)


def test_bombxml_namedelement_constructor_args():
    sig = inspect.signature(bombXML_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bombxml_namedelement_has_name():
    assert hasattr(bombXML_NamedElement, "name")
    descriptor = None
    for klass in bombXML_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bombxml_entitymodel_is_not_abstract():
    assert not inspect.isabstract(bombXML_EntityModel)


def test_bombxml_entitymodel_constructor_exists():
    assert callable(bombXML_EntityModel.__init__)


def test_bombxml_entitymodel_constructor_args():
    sig = inspect.signature(bombXML_EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_bombxml_entity_is_not_abstract():
    assert not inspect.isabstract(bombXML_Entity)


def test_bombxml_entity_constructor_exists():
    assert callable(bombXML_Entity.__init__)


def test_bombxml_entity_constructor_args():
    sig = inspect.signature(bombXML_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_bombxml_entity_has_abstract():
    assert hasattr(bombXML_Entity, "abstract")
    descriptor = None
    for klass in bombXML_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_bombxml_datatype_is_not_abstract():
    assert not inspect.isabstract(bombXML_DataType)


def test_bombxml_datatype_constructor_exists():
    assert callable(bombXML_DataType.__init__)


def test_bombxml_datatype_constructor_args():
    sig = inspect.signature(bombXML_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_bombxml_feature_is_not_abstract():
    assert not inspect.isabstract(bombXML_Feature)


def test_bombxml_feature_constructor_exists():
    assert callable(bombXML_Feature.__init__)


def test_bombxml_feature_constructor_args():
    sig = inspect.signature(bombXML_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_bombxml_feature_has_kind():
    assert hasattr(bombXML_Feature, "kind")
    descriptor = None
    for klass in bombXML_Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_bombxml_type_is_not_abstract():
    assert not inspect.isabstract(bombXML_Type)


def test_bombxml_type_constructor_exists():
    assert callable(bombXML_Type.__init__)


def test_bombxml_type_constructor_args():
    sig = inspect.signature(bombXML_Type.__init__)
    params = list(sig.parameters.keys())

def test_featurekind_exists():
    # Check that the Enumeration exists
    assert FeatureKind is not None

def test_featurekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureKind]
    expected_literals = [
        "reference",
        "containment",
        "attribute",
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
bombXML_NamedElement_strategy = st.builds(
    bombXML_NamedElement,
    name=
        safe_text
)
bombXML_EntityModel_strategy = st.builds(
    bombXML_EntityModel,
)
Type_strategy = st.builds(
    Type,
)
bombXML_Entity_strategy = st.builds(
    bombXML_Entity,
    abstract=
        st.booleans()
)
bombXML_DataType_strategy = st.builds(
    bombXML_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
bombXML_Feature_strategy = st.builds(
    bombXML_Feature,
    kind=
        safe_text
)
bombXML_Type_strategy = st.builds(
    bombXML_Type,
)

@given(instance=bombXML_NamedElement_strategy)
@settings(max_examples=50)
def test_bombxml_namedelement_instantiation(instance):
    assert isinstance(instance, bombXML_NamedElement)



@given(instance=bombXML_NamedElement_strategy)
def test_bombxml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bombXML_EntityModel_strategy)
@settings(max_examples=50)
def test_bombxml_entitymodel_instantiation(instance):
    assert isinstance(instance, bombXML_EntityModel)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=bombXML_Entity_strategy)
@settings(max_examples=50)
def test_bombxml_entity_instantiation(instance):
    assert isinstance(instance, bombXML_Entity)



@given(instance=bombXML_Entity_strategy)
def test_bombxml_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=bombXML_DataType_strategy)
@settings(max_examples=50)
def test_bombxml_datatype_instantiation(instance):
    assert isinstance(instance, bombXML_DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=bombXML_Feature_strategy)
@settings(max_examples=50)
def test_bombxml_feature_instantiation(instance):
    assert isinstance(instance, bombXML_Feature)



@given(instance=bombXML_Feature_strategy)
def test_bombxml_feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=bombXML_Type_strategy)
@settings(max_examples=50)
def test_bombxml_type_instantiation(instance):
    assert isinstance(instance, bombXML_Type)
