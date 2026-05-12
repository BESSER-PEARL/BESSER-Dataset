import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDSL_EntityModel,
    myDSL_NamedElement,
    Type,
    myDSL_Entity,
    myDSL_DataType,
    NamedElement,
    myDSL_Feature,
    myDSL_Type,
    FeatureKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_entitymodel_is_not_abstract():
    assert not inspect.isabstract(myDSL_EntityModel)


def test_mydsl_entitymodel_constructor_exists():
    assert callable(myDSL_EntityModel.__init__)


def test_mydsl_entitymodel_constructor_args():
    sig = inspect.signature(myDSL_EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_namedelement_is_not_abstract():
    assert not inspect.isabstract(myDSL_NamedElement)


def test_mydsl_namedelement_constructor_exists():
    assert callable(myDSL_NamedElement.__init__)


def test_mydsl_namedelement_constructor_args():
    sig = inspect.signature(myDSL_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_namedelement_has_name():
    assert hasattr(myDSL_NamedElement, "name")
    descriptor = None
    for klass in myDSL_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_entity_is_not_abstract():
    assert not inspect.isabstract(myDSL_Entity)


def test_mydsl_entity_constructor_exists():
    assert callable(myDSL_Entity.__init__)


def test_mydsl_entity_constructor_args():
    sig = inspect.signature(myDSL_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_mydsl_entity_has_abstract():
    assert hasattr(myDSL_Entity, "abstract")
    descriptor = None
    for klass in myDSL_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_datatype_is_not_abstract():
    assert not inspect.isabstract(myDSL_DataType)


def test_mydsl_datatype_constructor_exists():
    assert callable(myDSL_DataType.__init__)


def test_mydsl_datatype_constructor_args():
    sig = inspect.signature(myDSL_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_feature_is_not_abstract():
    assert not inspect.isabstract(myDSL_Feature)


def test_mydsl_feature_constructor_exists():
    assert callable(myDSL_Feature.__init__)


def test_mydsl_feature_constructor_args():
    sig = inspect.signature(myDSL_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_mydsl_feature_has_kind():
    assert hasattr(myDSL_Feature, "kind")
    descriptor = None
    for klass in myDSL_Feature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_is_not_abstract():
    assert not inspect.isabstract(myDSL_Type)


def test_mydsl_type_constructor_exists():
    assert callable(myDSL_Type.__init__)


def test_mydsl_type_constructor_args():
    sig = inspect.signature(myDSL_Type.__init__)
    params = list(sig.parameters.keys())

def test_featurekind_exists():
    # Check that the Enumeration exists
    assert FeatureKind is not None

def test_featurekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureKind]
    expected_literals = [
        "attribute",
        "containment",
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
myDSL_EntityModel_strategy = st.builds(
    myDSL_EntityModel,
)
myDSL_NamedElement_strategy = st.builds(
    myDSL_NamedElement,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDSL_Entity_strategy = st.builds(
    myDSL_Entity,
    abstract=
        st.booleans()
)
myDSL_DataType_strategy = st.builds(
    myDSL_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
myDSL_Feature_strategy = st.builds(
    myDSL_Feature,
    kind=
        safe_text
)
myDSL_Type_strategy = st.builds(
    myDSL_Type,
)

@given(instance=myDSL_EntityModel_strategy)
@settings(max_examples=50)
def test_mydsl_entitymodel_instantiation(instance):
    assert isinstance(instance, myDSL_EntityModel)

@given(instance=myDSL_NamedElement_strategy)
@settings(max_examples=50)
def test_mydsl_namedelement_instantiation(instance):
    assert isinstance(instance, myDSL_NamedElement)



@given(instance=myDSL_NamedElement_strategy)
def test_mydsl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDSL_Entity_strategy)
@settings(max_examples=50)
def test_mydsl_entity_instantiation(instance):
    assert isinstance(instance, myDSL_Entity)



@given(instance=myDSL_Entity_strategy)
def test_mydsl_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=myDSL_DataType_strategy)
@settings(max_examples=50)
def test_mydsl_datatype_instantiation(instance):
    assert isinstance(instance, myDSL_DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=myDSL_Feature_strategy)
@settings(max_examples=50)
def test_mydsl_feature_instantiation(instance):
    assert isinstance(instance, myDSL_Feature)



@given(instance=myDSL_Feature_strategy)
def test_mydsl_feature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=myDSL_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDSL_Type)
