import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ModelElement,
    umlsimp_Class,
    umlsimp_DataType,
    umlsimp_ModelElement,
    umlsimp_Model,
    umlsimp_TypedElement,
    TypedElement,
    umlsimp_Operation,
    umlsimp_Parameter,
    umlsimp_Property,
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



def test_umlsimp_class_is_not_abstract():
    assert not inspect.isabstract(umlsimp_Class)


def test_umlsimp_class_constructor_exists():
    assert callable(umlsimp_Class.__init__)


def test_umlsimp_class_constructor_args():
    sig = inspect.signature(umlsimp_Class.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp_datatype_is_not_abstract():
    assert not inspect.isabstract(umlsimp_DataType)


def test_umlsimp_datatype_constructor_exists():
    assert callable(umlsimp_DataType.__init__)


def test_umlsimp_datatype_constructor_args():
    sig = inspect.signature(umlsimp_DataType.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp_modelelement_is_not_abstract():
    assert not inspect.isabstract(umlsimp_ModelElement)


def test_umlsimp_modelelement_constructor_exists():
    assert callable(umlsimp_ModelElement.__init__)


def test_umlsimp_modelelement_constructor_args():
    sig = inspect.signature(umlsimp_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlsimp_modelelement_has_name():
    assert hasattr(umlsimp_ModelElement, "name")
    descriptor = None
    for klass in umlsimp_ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlsimp_model_is_not_abstract():
    assert not inspect.isabstract(umlsimp_Model)


def test_umlsimp_model_constructor_exists():
    assert callable(umlsimp_Model.__init__)


def test_umlsimp_model_constructor_args():
    sig = inspect.signature(umlsimp_Model.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp_typedelement_is_not_abstract():
    assert not inspect.isabstract(umlsimp_TypedElement)


def test_umlsimp_typedelement_constructor_exists():
    assert callable(umlsimp_TypedElement.__init__)


def test_umlsimp_typedelement_constructor_args():
    sig = inspect.signature(umlsimp_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp_operation_is_not_abstract():
    assert not inspect.isabstract(umlsimp_Operation)


def test_umlsimp_operation_constructor_exists():
    assert callable(umlsimp_Operation.__init__)


def test_umlsimp_operation_constructor_args():
    sig = inspect.signature(umlsimp_Operation.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp_parameter_is_not_abstract():
    assert not inspect.isabstract(umlsimp_Parameter)


def test_umlsimp_parameter_constructor_exists():
    assert callable(umlsimp_Parameter.__init__)


def test_umlsimp_parameter_constructor_args():
    sig = inspect.signature(umlsimp_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_umlsimp_property_is_not_abstract():
    assert not inspect.isabstract(umlsimp_Property)


def test_umlsimp_property_constructor_exists():
    assert callable(umlsimp_Property.__init__)


def test_umlsimp_property_constructor_args():
    sig = inspect.signature(umlsimp_Property.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_umlsimp_property_has_visibility():
    assert hasattr(umlsimp_Property, "visibility")
    descriptor = None
    for klass in umlsimp_Property.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

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
umlsimp_Class_strategy = st.builds(
    umlsimp_Class,
)
umlsimp_DataType_strategy = st.builds(
    umlsimp_DataType,
)
umlsimp_ModelElement_strategy = st.builds(
    umlsimp_ModelElement,
    name=
        safe_text
)
umlsimp_Model_strategy = st.builds(
    umlsimp_Model,
)
umlsimp_TypedElement_strategy = st.builds(
    umlsimp_TypedElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
umlsimp_Operation_strategy = st.builds(
    umlsimp_Operation,
)
umlsimp_Parameter_strategy = st.builds(
    umlsimp_Parameter,
)
umlsimp_Property_strategy = st.builds(
    umlsimp_Property,
    visibility=
        safe_text
)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=umlsimp_Class_strategy)
@settings(max_examples=50)
def test_umlsimp_class_instantiation(instance):
    assert isinstance(instance, umlsimp_Class)

@given(instance=umlsimp_DataType_strategy)
@settings(max_examples=50)
def test_umlsimp_datatype_instantiation(instance):
    assert isinstance(instance, umlsimp_DataType)

@given(instance=umlsimp_ModelElement_strategy)
@settings(max_examples=50)
def test_umlsimp_modelelement_instantiation(instance):
    assert isinstance(instance, umlsimp_ModelElement)



@given(instance=umlsimp_ModelElement_strategy)
def test_umlsimp_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlsimp_Model_strategy)
@settings(max_examples=50)
def test_umlsimp_model_instantiation(instance):
    assert isinstance(instance, umlsimp_Model)

@given(instance=umlsimp_TypedElement_strategy)
@settings(max_examples=50)
def test_umlsimp_typedelement_instantiation(instance):
    assert isinstance(instance, umlsimp_TypedElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=umlsimp_Operation_strategy)
@settings(max_examples=50)
def test_umlsimp_operation_instantiation(instance):
    assert isinstance(instance, umlsimp_Operation)

@given(instance=umlsimp_Parameter_strategy)
@settings(max_examples=50)
def test_umlsimp_parameter_instantiation(instance):
    assert isinstance(instance, umlsimp_Parameter)

@given(instance=umlsimp_Property_strategy)
@settings(max_examples=50)
def test_umlsimp_property_instantiation(instance):
    assert isinstance(instance, umlsimp_Property)



@given(instance=umlsimp_Property_strategy)
def test_umlsimp_property_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original
