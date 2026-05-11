import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ModelElement,
    umlsimp::Class,
    umlsimp::DataType,
    umlsimp::ModelElement,
    umlsimp::Model,
    umlsimp::TypedElement,
    TypedElement,
    umlsimp::Parameter,
    umlsimp::Property,
    umlsimp::Operation,
    visType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp::class_is_not_abstract():
    assert not inspect.isabstract(umlsimp::Class)


def test_umlsimp::class_constructor_exists():
    assert callable(umlsimp::Class.__init__)


def test_umlsimp::class_constructor_args():
    sig = inspect.signature(umlsimp::Class.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp::datatype_is_not_abstract():
    assert not inspect.isabstract(umlsimp::DataType)


def test_umlsimp::datatype_constructor_exists():
    assert callable(umlsimp::DataType.__init__)


def test_umlsimp::datatype_constructor_args():
    sig = inspect.signature(umlsimp::DataType.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp::modelelement_is_not_abstract():
    assert not inspect.isabstract(umlsimp::ModelElement)


def test_umlsimp::modelelement_constructor_exists():
    assert callable(umlsimp::ModelElement.__init__)


def test_umlsimp::modelelement_constructor_args():
    sig = inspect.signature(umlsimp::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlsimp::modelelement_has_name():
    assert hasattr(umlsimp::ModelElement, "name")
    descriptor = None
    for klass in umlsimp::ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlsimp::model_is_not_abstract():
    assert not inspect.isabstract(umlsimp::Model)


def test_umlsimp::model_constructor_exists():
    assert callable(umlsimp::Model.__init__)


def test_umlsimp::model_constructor_args():
    sig = inspect.signature(umlsimp::Model.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp::typedelement_is_not_abstract():
    assert not inspect.isabstract(umlsimp::TypedElement)


def test_umlsimp::typedelement_constructor_exists():
    assert callable(umlsimp::TypedElement.__init__)


def test_umlsimp::typedelement_constructor_args():
    sig = inspect.signature(umlsimp::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp::parameter_is_not_abstract():
    assert not inspect.isabstract(umlsimp::Parameter)


def test_umlsimp::parameter_constructor_exists():
    assert callable(umlsimp::Parameter.__init__)


def test_umlsimp::parameter_constructor_args():
    sig = inspect.signature(umlsimp::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp::property_is_not_abstract():
    assert not inspect.isabstract(umlsimp::Property)


def test_umlsimp::property_constructor_exists():
    assert callable(umlsimp::Property.__init__)


def test_umlsimp::property_constructor_args():
    sig = inspect.signature(umlsimp::Property.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_umlsimp::property_has_visibility():
    assert hasattr(umlsimp::Property, "visibility")
    descriptor = None
    for klass in umlsimp::Property.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_umlsimp::operation_is_not_abstract():
    assert not inspect.isabstract(umlsimp::Operation)


def test_umlsimp::operation_constructor_exists():
    assert callable(umlsimp::Operation.__init__)


def test_umlsimp::operation_constructor_args():
    sig = inspect.signature(umlsimp::Operation.__init__)
    params = list(sig.parameters.keys())

def test_vistype_exists():
    # Check that the Enumeration exists
    assert visType is not None

def test_vistype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in visType]
    expected_literals = [
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in visType"


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
ModelElement_strategy = st.builds(
    ModelElement,
)
umlsimp::Class_strategy = st.builds(
    umlsimp::Class,
)
umlsimp::DataType_strategy = st.builds(
    umlsimp::DataType,
)
umlsimp::ModelElement_strategy = st.builds(
    umlsimp::ModelElement,
    name=
        safe_text
)
umlsimp::Model_strategy = st.builds(
    umlsimp::Model,
)
umlsimp::TypedElement_strategy = st.builds(
    umlsimp::TypedElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
umlsimp::Parameter_strategy = st.builds(
    umlsimp::Parameter,
)
umlsimp::Property_strategy = st.builds(
    umlsimp::Property,
    visibility=
        safe_text
)
umlsimp::Operation_strategy = st.builds(
    umlsimp::Operation,
)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=umlsimp::Class_strategy)
@settings(max_examples=50)
def test_umlsimp::class_instantiation(instance):
    assert isinstance(instance, umlsimp::Class)

@given(instance=umlsimp::DataType_strategy)
@settings(max_examples=50)
def test_umlsimp::datatype_instantiation(instance):
    assert isinstance(instance, umlsimp::DataType)

@given(instance=umlsimp::ModelElement_strategy)
@settings(max_examples=50)
def test_umlsimp::modelelement_instantiation(instance):
    assert isinstance(instance, umlsimp::ModelElement)

@given(instance=umlsimp::ModelElement_strategy)
def test_umlsimp::modelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlsimp::ModelElement_strategy)
def test_umlsimp::modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlsimp::Model_strategy)
@settings(max_examples=50)
def test_umlsimp::model_instantiation(instance):
    assert isinstance(instance, umlsimp::Model)

@given(instance=umlsimp::TypedElement_strategy)
@settings(max_examples=50)
def test_umlsimp::typedelement_instantiation(instance):
    assert isinstance(instance, umlsimp::TypedElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=umlsimp::Parameter_strategy)
@settings(max_examples=50)
def test_umlsimp::parameter_instantiation(instance):
    assert isinstance(instance, umlsimp::Parameter)

@given(instance=umlsimp::Property_strategy)
@settings(max_examples=50)
def test_umlsimp::property_instantiation(instance):
    assert isinstance(instance, umlsimp::Property)

@given(instance=umlsimp::Property_strategy)
def test_umlsimp::property_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=umlsimp::Property_strategy)
def test_umlsimp::property_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=umlsimp::Operation_strategy)
@settings(max_examples=50)
def test_umlsimp::operation_instantiation(instance):
    assert isinstance(instance, umlsimp::Operation)
