import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Type,
    hbmxml_Entity,
    hbmxml_DataType,
    NamedElement,
    hbmxml_Feature,
    hbmxml_Type,
    hbmxml_NamedElement,
    hbmxml_EntityModel,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hbmxml_entity_is_not_abstract():
    assert not inspect.isabstract(hbmxml_Entity)


def test_hbmxml_entity_constructor_exists():
    assert callable(hbmxml_Entity.__init__)


def test_hbmxml_entity_constructor_args():
    sig = inspect.signature(hbmxml_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_hbmxml_entity_has_abstract():
    assert hasattr(hbmxml_Entity, "abstract")
    descriptor = None
    for klass in hbmxml_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_hbmxml_datatype_is_not_abstract():
    assert not inspect.isabstract(hbmxml_DataType)


def test_hbmxml_datatype_constructor_exists():
    assert callable(hbmxml_DataType.__init__)


def test_hbmxml_datatype_constructor_args():
    sig = inspect.signature(hbmxml_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hbmxml_feature_is_not_abstract():
    assert not inspect.isabstract(hbmxml_Feature)


def test_hbmxml_feature_constructor_exists():
    assert callable(hbmxml_Feature.__init__)


def test_hbmxml_feature_constructor_args():
    sig = inspect.signature(hbmxml_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_hbmxml_feature_has_kind():
    assert hasattr(hbmxml_Feature, "kind")
    descriptor = None
    for klass in hbmxml_Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_hbmxml_type_is_not_abstract():
    assert not inspect.isabstract(hbmxml_Type)


def test_hbmxml_type_constructor_exists():
    assert callable(hbmxml_Type.__init__)


def test_hbmxml_type_constructor_args():
    sig = inspect.signature(hbmxml_Type.__init__)
    params = list(sig.parameters.keys())



def test_hbmxml_namedelement_is_not_abstract():
    assert not inspect.isabstract(hbmxml_NamedElement)


def test_hbmxml_namedelement_constructor_exists():
    assert callable(hbmxml_NamedElement.__init__)


def test_hbmxml_namedelement_constructor_args():
    sig = inspect.signature(hbmxml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hbmxml_namedelement_has_name():
    assert hasattr(hbmxml_NamedElement, "name")
    descriptor = None
    for klass in hbmxml_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hbmxml_entitymodel_is_not_abstract():
    assert not inspect.isabstract(hbmxml_EntityModel)


def test_hbmxml_entitymodel_constructor_exists():
    assert callable(hbmxml_EntityModel.__init__)


def test_hbmxml_entitymodel_constructor_args():
    sig = inspect.signature(hbmxml_EntityModel.__init__)
    params = list(sig.parameters.keys())

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
Type_strategy = st.builds(
    Type,
)
hbmxml_Entity_strategy = st.builds(
    hbmxml_Entity,
    abstract=
        st.booleans()
)
hbmxml_DataType_strategy = st.builds(
    hbmxml_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hbmxml_Feature_strategy = st.builds(
    hbmxml_Feature,
    kind=
        safe_text
)
hbmxml_Type_strategy = st.builds(
    hbmxml_Type,
)
hbmxml_NamedElement_strategy = st.builds(
    hbmxml_NamedElement,
    name=
        safe_text
)
hbmxml_EntityModel_strategy = st.builds(
    hbmxml_EntityModel,
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=hbmxml_Entity_strategy)
@settings(max_examples=50)
def test_hbmxml_entity_instantiation(instance):
    assert isinstance(instance, hbmxml_Entity)



@given(instance=hbmxml_Entity_strategy)
def test_hbmxml_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=hbmxml_DataType_strategy)
@settings(max_examples=50)
def test_hbmxml_datatype_instantiation(instance):
    assert isinstance(instance, hbmxml_DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hbmxml_Feature_strategy)
@settings(max_examples=50)
def test_hbmxml_feature_instantiation(instance):
    assert isinstance(instance, hbmxml_Feature)



@given(instance=hbmxml_Feature_strategy)
def test_hbmxml_feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=hbmxml_Type_strategy)
@settings(max_examples=50)
def test_hbmxml_type_instantiation(instance):
    assert isinstance(instance, hbmxml_Type)

@given(instance=hbmxml_NamedElement_strategy)
@settings(max_examples=50)
def test_hbmxml_namedelement_instantiation(instance):
    assert isinstance(instance, hbmxml_NamedElement)



@given(instance=hbmxml_NamedElement_strategy)
def test_hbmxml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hbmxml_EntityModel_strategy)
@settings(max_examples=50)
def test_hbmxml_entitymodel_instantiation(instance):
    assert isinstance(instance, hbmxml_EntityModel)
