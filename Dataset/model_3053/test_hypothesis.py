import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Feature,
    hermes_DataType,
    hermes_Reference,
    hermes_NamedElement,
    NamedElement,
    hermes_Entity,
    hermes_Package,
    hermes_Feature,
    hermes_Module,
    FetureAnnotation,
    DataTypes,
    EntityAnnotation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hermes_datatype_is_not_abstract():
    assert not inspect.isabstract(hermes_DataType)


def test_hermes_datatype_constructor_exists():
    assert callable(hermes_DataType.__init__)


def test_hermes_datatype_constructor_args():
    sig = inspect.signature(hermes_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_hermes_datatype_has_type():
    assert hasattr(hermes_DataType, "type")
    descriptor = None
    for klass in hermes_DataType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hermes_reference_is_not_abstract():
    assert not inspect.isabstract(hermes_Reference)


def test_hermes_reference_constructor_exists():
    assert callable(hermes_Reference.__init__)


def test_hermes_reference_constructor_args():
    sig = inspect.signature(hermes_Reference.__init__)
    params = list(sig.parameters.keys())



def test_hermes_namedelement_is_not_abstract():
    assert not inspect.isabstract(hermes_NamedElement)


def test_hermes_namedelement_constructor_exists():
    assert callable(hermes_NamedElement.__init__)


def test_hermes_namedelement_constructor_args():
    sig = inspect.signature(hermes_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hermes_namedelement_has_name():
    assert hasattr(hermes_NamedElement, "name")
    descriptor = None
    for klass in hermes_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hermes_entity_is_not_abstract():
    assert not inspect.isabstract(hermes_Entity)


def test_hermes_entity_constructor_exists():
    assert callable(hermes_Entity.__init__)


def test_hermes_entity_constructor_args():
    sig = inspect.signature(hermes_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "annotations" in params, "Missing parameter 'annotations'"

def test_hermes_entity_has_annotations():
    assert hasattr(hermes_Entity, "annotations")
    descriptor = None
    for klass in hermes_Entity.__mro__:
        if "annotations" in klass.__dict__:
            descriptor = klass.__dict__["annotations"]
            break
    assert isinstance(descriptor, property)



def test_hermes_package_is_not_abstract():
    assert not inspect.isabstract(hermes_Package)


def test_hermes_package_constructor_exists():
    assert callable(hermes_Package.__init__)


def test_hermes_package_constructor_args():
    sig = inspect.signature(hermes_Package.__init__)
    params = list(sig.parameters.keys())



def test_hermes_feature_is_not_abstract():
    assert not inspect.isabstract(hermes_Feature)


def test_hermes_feature_constructor_exists():
    assert callable(hermes_Feature.__init__)


def test_hermes_feature_constructor_args():
    sig = inspect.signature(hermes_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "annotations" in params, "Missing parameter 'annotations'"

def test_hermes_feature_has_many():
    assert hasattr(hermes_Feature, "many")
    descriptor = None
    for klass in hermes_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_hermes_feature_has_annotations():
    assert hasattr(hermes_Feature, "annotations")
    descriptor = None
    for klass in hermes_Feature.__mro__:
        if "annotations" in klass.__dict__:
            descriptor = klass.__dict__["annotations"]
            break
    assert isinstance(descriptor, property)



def test_hermes_module_is_not_abstract():
    assert not inspect.isabstract(hermes_Module)


def test_hermes_module_constructor_exists():
    assert callable(hermes_Module.__init__)


def test_hermes_module_constructor_args():
    sig = inspect.signature(hermes_Module.__init__)
    params = list(sig.parameters.keys())

def test_fetureannotation_exists():
    # Check that the Enumeration exists
    assert FetureAnnotation is not None

def test_fetureannotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FetureAnnotation]
    expected_literals = [
        "Id",
        "Index",
        "Load",
        "Ignore",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FetureAnnotation"

def test_datatypes_exists():
    # Check that the Enumeration exists
    assert DataTypes is not None

def test_datatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypes]
    expected_literals = [
        "Long",
        "Integer",
        "Boolean",
        "String",
        "Object",
        "Double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypes"

def test_entityannotation_exists():
    # Check that the Enumeration exists
    assert EntityAnnotation is not None

def test_entityannotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityAnnotation]
    expected_literals = [
        "Cache",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityAnnotation"


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
Feature_strategy = st.builds(
    Feature,
)
hermes_DataType_strategy = st.builds(
    hermes_DataType,
    type=
        safe_text
)
hermes_Reference_strategy = st.builds(
    hermes_Reference,
)
hermes_NamedElement_strategy = st.builds(
    hermes_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hermes_Entity_strategy = st.builds(
    hermes_Entity,
    annotations=
        safe_text
)
hermes_Package_strategy = st.builds(
    hermes_Package,
)
hermes_Feature_strategy = st.builds(
    hermes_Feature,
    many=
        st.booleans(),
    annotations=
        safe_text
)
hermes_Module_strategy = st.builds(
    hermes_Module,
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=hermes_DataType_strategy)
@settings(max_examples=50)
def test_hermes_datatype_instantiation(instance):
    assert isinstance(instance, hermes_DataType)



@given(instance=hermes_DataType_strategy)
def test_hermes_datatype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=hermes_Reference_strategy)
@settings(max_examples=50)
def test_hermes_reference_instantiation(instance):
    assert isinstance(instance, hermes_Reference)

@given(instance=hermes_NamedElement_strategy)
@settings(max_examples=50)
def test_hermes_namedelement_instantiation(instance):
    assert isinstance(instance, hermes_NamedElement)



@given(instance=hermes_NamedElement_strategy)
def test_hermes_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hermes_Entity_strategy)
@settings(max_examples=50)
def test_hermes_entity_instantiation(instance):
    assert isinstance(instance, hermes_Entity)



@given(instance=hermes_Entity_strategy)
def test_hermes_entity_annotations_setter(instance):
    original = instance.annotations
    instance.annotations = original
    assert instance.annotations == original

@given(instance=hermes_Package_strategy)
@settings(max_examples=50)
def test_hermes_package_instantiation(instance):
    assert isinstance(instance, hermes_Package)

@given(instance=hermes_Feature_strategy)
@settings(max_examples=50)
def test_hermes_feature_instantiation(instance):
    assert isinstance(instance, hermes_Feature)



@given(instance=hermes_Feature_strategy)
def test_hermes_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=hermes_Feature_strategy)
def test_hermes_feature_annotations_setter(instance):
    original = instance.annotations
    instance.annotations = original
    assert instance.annotations == original

@given(instance=hermes_Module_strategy)
@settings(max_examples=50)
def test_hermes_module_instantiation(instance):
    assert isinstance(instance, hermes_Module)
