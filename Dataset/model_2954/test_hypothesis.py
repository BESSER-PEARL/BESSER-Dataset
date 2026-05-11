import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::JAVAID,
    Type,
    myDsl::Interface,
    myDsl::Attribute,
    myDsl::TypeDef,
    myDsl::Type,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::javaid_is_not_abstract():
    assert not inspect.isabstract(myDsl::JAVAID)


def test_mydsl::javaid_constructor_exists():
    assert callable(myDsl::JAVAID.__init__)


def test_mydsl::javaid_constructor_args():
    sig = inspect.signature(myDsl::JAVAID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::javaid_has_name():
    assert hasattr(myDsl::JAVAID, "name")
    descriptor = None
    for klass in myDsl::JAVAID.__mro__:
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



def test_mydsl::interface_is_not_abstract():
    assert not inspect.isabstract(myDsl::Interface)


def test_mydsl::interface_constructor_exists():
    assert callable(myDsl::Interface.__init__)


def test_mydsl::interface_constructor_args():
    sig = inspect.signature(myDsl::Interface.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl::Attribute)


def test_mydsl::attribute_constructor_exists():
    assert callable(myDsl::Attribute.__init__)


def test_mydsl::attribute_constructor_args():
    sig = inspect.signature(myDsl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_mydsl::attribute_has_many():
    assert hasattr(myDsl::Attribute, "many")
    descriptor = None
    for klass in myDsl::Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::typedef_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeDef)


def test_mydsl::typedef_constructor_exists():
    assert callable(myDsl::TypeDef.__init__)


def test_mydsl::typedef_constructor_args():
    sig = inspect.signature(myDsl::TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::type_has_name():
    assert hasattr(myDsl::Type, "name")
    descriptor = None
    for klass in myDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
myDsl::JAVAID_strategy = st.builds(
    myDsl::JAVAID,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl::Interface_strategy = st.builds(
    myDsl::Interface,
)
myDsl::Attribute_strategy = st.builds(
    myDsl::Attribute,
    many=
        st.booleans()
)
myDsl::TypeDef_strategy = st.builds(
    myDsl::TypeDef,
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    name=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=myDsl::JAVAID_strategy)
@settings(max_examples=50)
def test_mydsl::javaid_instantiation(instance):
    assert isinstance(instance, myDsl::JAVAID)

@given(instance=myDsl::JAVAID_strategy)
def test_mydsl::javaid_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::JAVAID_strategy)
def test_mydsl::javaid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl::Interface_strategy)
@settings(max_examples=50)
def test_mydsl::interface_instantiation(instance):
    assert isinstance(instance, myDsl::Interface)

@given(instance=myDsl::Attribute_strategy)
@settings(max_examples=50)
def test_mydsl::attribute_instantiation(instance):
    assert isinstance(instance, myDsl::Attribute)

@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=myDsl::TypeDef_strategy)
@settings(max_examples=50)
def test_mydsl::typedef_instantiation(instance):
    assert isinstance(instance, myDsl::TypeDef)

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
