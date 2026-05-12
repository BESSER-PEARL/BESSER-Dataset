import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    coral_Type,
    coral_EntityModel,
    coral_Feature,
    Type,
    coral_Entity,
    coral_DataType,
    coral_NamedElement,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_coral_type_is_not_abstract():
    assert not inspect.isabstract(coral_Type)


def test_coral_type_constructor_exists():
    assert callable(coral_Type.__init__)


def test_coral_type_constructor_args():
    sig = inspect.signature(coral_Type.__init__)
    params = list(sig.parameters.keys())



def test_coral_entitymodel_is_not_abstract():
    assert not inspect.isabstract(coral_EntityModel)


def test_coral_entitymodel_constructor_exists():
    assert callable(coral_EntityModel.__init__)


def test_coral_entitymodel_constructor_args():
    sig = inspect.signature(coral_EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_coral_feature_is_not_abstract():
    assert not inspect.isabstract(coral_Feature)


def test_coral_feature_constructor_exists():
    assert callable(coral_Feature.__init__)


def test_coral_feature_constructor_args():
    sig = inspect.signature(coral_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_coral_feature_has_kind():
    assert hasattr(coral_Feature, "kind")
    descriptor = None
    for klass in coral_Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_coral_entity_is_not_abstract():
    assert not inspect.isabstract(coral_Entity)


def test_coral_entity_constructor_exists():
    assert callable(coral_Entity.__init__)


def test_coral_entity_constructor_args():
    sig = inspect.signature(coral_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_coral_entity_has_abstract():
    assert hasattr(coral_Entity, "abstract")
    descriptor = None
    for klass in coral_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_coral_datatype_is_not_abstract():
    assert not inspect.isabstract(coral_DataType)


def test_coral_datatype_constructor_exists():
    assert callable(coral_DataType.__init__)


def test_coral_datatype_constructor_args():
    sig = inspect.signature(coral_DataType.__init__)
    params = list(sig.parameters.keys())



def test_coral_namedelement_is_not_abstract():
    assert not inspect.isabstract(coral_NamedElement)


def test_coral_namedelement_constructor_exists():
    assert callable(coral_NamedElement.__init__)


def test_coral_namedelement_constructor_args():
    sig = inspect.signature(coral_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_coral_namedelement_has_name():
    assert hasattr(coral_NamedElement, "name")
    descriptor = None
    for klass in coral_NamedElement.__mro__:
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
        "reference",
        "attribute",
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
NamedElement_strategy = st.builds(
    NamedElement,
)
coral_Type_strategy = st.builds(
    coral_Type,
)
coral_EntityModel_strategy = st.builds(
    coral_EntityModel,
)
coral_Feature_strategy = st.builds(
    coral_Feature,
    kind=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
coral_Entity_strategy = st.builds(
    coral_Entity,
    abstract=
        st.booleans()
)
coral_DataType_strategy = st.builds(
    coral_DataType,
)
coral_NamedElement_strategy = st.builds(
    coral_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=coral_Type_strategy)
@settings(max_examples=50)
def test_coral_type_instantiation(instance):
    assert isinstance(instance, coral_Type)

@given(instance=coral_EntityModel_strategy)
@settings(max_examples=50)
def test_coral_entitymodel_instantiation(instance):
    assert isinstance(instance, coral_EntityModel)

@given(instance=coral_Feature_strategy)
@settings(max_examples=50)
def test_coral_feature_instantiation(instance):
    assert isinstance(instance, coral_Feature)



@given(instance=coral_Feature_strategy)
def test_coral_feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=coral_Entity_strategy)
@settings(max_examples=50)
def test_coral_entity_instantiation(instance):
    assert isinstance(instance, coral_Entity)



@given(instance=coral_Entity_strategy)
def test_coral_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=coral_DataType_strategy)
@settings(max_examples=50)
def test_coral_datatype_instantiation(instance):
    assert isinstance(instance, coral_DataType)

@given(instance=coral_NamedElement_strategy)
@settings(max_examples=50)
def test_coral_namedelement_instantiation(instance):
    assert isinstance(instance, coral_NamedElement)



@given(instance=coral_NamedElement_strategy)
def test_coral_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
