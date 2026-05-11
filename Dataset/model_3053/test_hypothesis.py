import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Feature,
    hermes::DataType,
    hermes::Reference,
    hermes::NamedElement,
    NamedElement,
    hermes::Feature,
    hermes::Package,
    hermes::Entity,
    hermes::Module,
    DataTypes,
    FetureAnnotation,
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



def test_hermes::datatype_is_not_abstract():
    assert not inspect.isabstract(hermes::DataType)


def test_hermes::datatype_constructor_exists():
    assert callable(hermes::DataType.__init__)


def test_hermes::datatype_constructor_args():
    sig = inspect.signature(hermes::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_hermes::datatype_has_type():
    assert hasattr(hermes::DataType, "type")
    descriptor = None
    for klass in hermes::DataType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hermes::reference_is_not_abstract():
    assert not inspect.isabstract(hermes::Reference)


def test_hermes::reference_constructor_exists():
    assert callable(hermes::Reference.__init__)


def test_hermes::reference_constructor_args():
    sig = inspect.signature(hermes::Reference.__init__)
    params = list(sig.parameters.keys())



def test_hermes::namedelement_is_not_abstract():
    assert not inspect.isabstract(hermes::NamedElement)


def test_hermes::namedelement_constructor_exists():
    assert callable(hermes::NamedElement.__init__)


def test_hermes::namedelement_constructor_args():
    sig = inspect.signature(hermes::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hermes::namedelement_has_name():
    assert hasattr(hermes::NamedElement, "name")
    descriptor = None
    for klass in hermes::NamedElement.__mro__:
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



def test_hermes::feature_is_not_abstract():
    assert not inspect.isabstract(hermes::Feature)


def test_hermes::feature_constructor_exists():
    assert callable(hermes::Feature.__init__)


def test_hermes::feature_constructor_args():
    sig = inspect.signature(hermes::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "annotations" in params, "Missing parameter 'annotations'"
    assert "many" in params, "Missing parameter 'many'"

def test_hermes::feature_has_annotations():
    assert hasattr(hermes::Feature, "annotations")
    descriptor = None
    for klass in hermes::Feature.__mro__:
        if "annotations" in klass.__dict__:
            descriptor = klass.__dict__["annotations"]
            break
    assert isinstance(descriptor, property)

def test_hermes::feature_has_many():
    assert hasattr(hermes::Feature, "many")
    descriptor = None
    for klass in hermes::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_hermes::package_is_not_abstract():
    assert not inspect.isabstract(hermes::Package)


def test_hermes::package_constructor_exists():
    assert callable(hermes::Package.__init__)


def test_hermes::package_constructor_args():
    sig = inspect.signature(hermes::Package.__init__)
    params = list(sig.parameters.keys())



def test_hermes::entity_is_not_abstract():
    assert not inspect.isabstract(hermes::Entity)


def test_hermes::entity_constructor_exists():
    assert callable(hermes::Entity.__init__)


def test_hermes::entity_constructor_args():
    sig = inspect.signature(hermes::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "annotations" in params, "Missing parameter 'annotations'"

def test_hermes::entity_has_annotations():
    assert hasattr(hermes::Entity, "annotations")
    descriptor = None
    for klass in hermes::Entity.__mro__:
        if "annotations" in klass.__dict__:
            descriptor = klass.__dict__["annotations"]
            break
    assert isinstance(descriptor, property)



def test_hermes::module_is_not_abstract():
    assert not inspect.isabstract(hermes::Module)


def test_hermes::module_constructor_exists():
    assert callable(hermes::Module.__init__)


def test_hermes::module_constructor_args():
    sig = inspect.signature(hermes::Module.__init__)
    params = list(sig.parameters.keys())

def test_datatypes_exists():
    # Check that the Enumeration exists
    assert DataTypes is not None

def test_datatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypes]
    expected_literals = [
        "Boolean",
        "Long",
        "Integer",
        "Double",
        "Object",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypes"

def test_fetureannotation_exists():
    # Check that the Enumeration exists
    assert FetureAnnotation is not None

def test_fetureannotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FetureAnnotation]
    expected_literals = [
        "Ignore",
        "Id",
        "Index",
        "Load",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FetureAnnotation"

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
hermes::DataType_strategy = st.builds(
    hermes::DataType,
    type=
        safe_text
)
hermes::Reference_strategy = st.builds(
    hermes::Reference,
)
hermes::NamedElement_strategy = st.builds(
    hermes::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
hermes::Feature_strategy = st.builds(
    hermes::Feature,
    annotations=
        safe_text,
    many=
        st.booleans()
)
hermes::Package_strategy = st.builds(
    hermes::Package,
)
hermes::Entity_strategy = st.builds(
    hermes::Entity,
    annotations=
        safe_text
)
hermes::Module_strategy = st.builds(
    hermes::Module,
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=hermes::DataType_strategy)
@settings(max_examples=50)
def test_hermes::datatype_instantiation(instance):
    assert isinstance(instance, hermes::DataType)

@given(instance=hermes::DataType_strategy)
def test_hermes::datatype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=hermes::DataType_strategy)
def test_hermes::datatype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=hermes::Reference_strategy)
@settings(max_examples=50)
def test_hermes::reference_instantiation(instance):
    assert isinstance(instance, hermes::Reference)

@given(instance=hermes::NamedElement_strategy)
@settings(max_examples=50)
def test_hermes::namedelement_instantiation(instance):
    assert isinstance(instance, hermes::NamedElement)

@given(instance=hermes::NamedElement_strategy)
def test_hermes::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hermes::NamedElement_strategy)
def test_hermes::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=hermes::Feature_strategy)
@settings(max_examples=50)
def test_hermes::feature_instantiation(instance):
    assert isinstance(instance, hermes::Feature)

@given(instance=hermes::Feature_strategy)
def test_hermes::feature_annotations_type(instance):
    assert isinstance(instance.annotations, str)


@given(instance=hermes::Feature_strategy)
def test_hermes::feature_annotations_setter(instance):
    original = instance.annotations
    instance.annotations = original
    assert instance.annotations == original

@given(instance=hermes::Feature_strategy)
def test_hermes::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=hermes::Feature_strategy)
def test_hermes::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=hermes::Package_strategy)
@settings(max_examples=50)
def test_hermes::package_instantiation(instance):
    assert isinstance(instance, hermes::Package)

@given(instance=hermes::Entity_strategy)
@settings(max_examples=50)
def test_hermes::entity_instantiation(instance):
    assert isinstance(instance, hermes::Entity)

@given(instance=hermes::Entity_strategy)
def test_hermes::entity_annotations_type(instance):
    assert isinstance(instance.annotations, str)


@given(instance=hermes::Entity_strategy)
def test_hermes::entity_annotations_setter(instance):
    original = instance.annotations
    instance.annotations = original
    assert instance.annotations == original

@given(instance=hermes::Module_strategy)
@settings(max_examples=50)
def test_hermes::module_instantiation(instance):
    assert isinstance(instance, hermes::Module)
