import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_JAVAID,
    Type,
    myDsl_Interface,
    myDsl_Attribute,
    myDsl_TypeDef,
    myDsl_Type,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_javaid_is_not_abstract():
    assert not inspect.isabstract(myDsl_JAVAID)


def test_mydsl_javaid_constructor_exists():
    assert callable(myDsl_JAVAID.__init__)


def test_mydsl_javaid_constructor_args():
    sig = inspect.signature(myDsl_JAVAID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_javaid_has_name():
    assert hasattr(myDsl_JAVAID, "name")
    descriptor = None
    for klass in myDsl_JAVAID.__mro__:
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



def test_mydsl_interface_is_not_abstract():
    assert not inspect.isabstract(myDsl_Interface)


def test_mydsl_interface_constructor_exists():
    assert callable(myDsl_Interface.__init__)


def test_mydsl_interface_constructor_args():
    sig = inspect.signature(myDsl_Interface.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl_Attribute)


def test_mydsl_attribute_constructor_exists():
    assert callable(myDsl_Attribute.__init__)


def test_mydsl_attribute_constructor_args():
    sig = inspect.signature(myDsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_mydsl_attribute_has_many():
    assert hasattr(myDsl_Attribute, "many")
    descriptor = None
    for klass in myDsl_Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_typedef_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeDef)


def test_mydsl_typedef_constructor_exists():
    assert callable(myDsl_TypeDef.__init__)


def test_mydsl_typedef_constructor_args():
    sig = inspect.signature(myDsl_TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type)


def test_mydsl_type_constructor_exists():
    assert callable(myDsl_Type.__init__)


def test_mydsl_type_constructor_args():
    sig = inspect.signature(myDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_type_has_name():
    assert hasattr(myDsl_Type, "name")
    descriptor = None
    for klass in myDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
    params = list(sig.parameters.keys())


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
myDsl_JAVAID_strategy = st.builds(
    myDsl_JAVAID,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl_Interface_strategy = st.builds(
    myDsl_Interface,
)
myDsl_Attribute_strategy = st.builds(
    myDsl_Attribute,
    many=
        st.booleans()
)
myDsl_TypeDef_strategy = st.builds(
    myDsl_TypeDef,
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
    name=
        safe_text
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=myDsl_JAVAID_strategy)
@settings(max_examples=50)
def test_mydsl_javaid_instantiation(instance):
    assert isinstance(instance, myDsl_JAVAID)



@given(instance=myDsl_JAVAID_strategy)
def test_mydsl_javaid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl_Interface_strategy)
@settings(max_examples=50)
def test_mydsl_interface_instantiation(instance):
    assert isinstance(instance, myDsl_Interface)

@given(instance=myDsl_Attribute_strategy)
@settings(max_examples=50)
def test_mydsl_attribute_instantiation(instance):
    assert isinstance(instance, myDsl_Attribute)



@given(instance=myDsl_Attribute_strategy)
def test_mydsl_attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myDsl_TypeDef_strategy)
@settings(max_examples=50)
def test_mydsl_typedef_instantiation(instance):
    assert isinstance(instance, myDsl_TypeDef)

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)



@given(instance=myDsl_Type_strategy)
def test_mydsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)
