import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smalluml::NamedElement,
    NamedElement,
    smalluml::Type,
    smalluml::Property,
    smalluml::Operation,
    Type,
    smalluml::TypeInteger,
    smalluml::TypeUnlimitedNatural,
    smalluml::TypeReal,
    smalluml::Class,
    smalluml::TypeString,
    smalluml::Root,
    smalluml::TypeBoolean,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smalluml::namedelement_is_not_abstract():
    assert not inspect.isabstract(smalluml::NamedElement)


def test_smalluml::namedelement_constructor_exists():
    assert callable(smalluml::NamedElement.__init__)


def test_smalluml::namedelement_constructor_args():
    sig = inspect.signature(smalluml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::namedelement_has_name():
    assert hasattr(smalluml::NamedElement, "name")
    descriptor = None
    for klass in smalluml::NamedElement.__mro__:
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



def test_smalluml::type_is_not_abstract():
    assert not inspect.isabstract(smalluml::Type)


def test_smalluml::type_constructor_exists():
    assert callable(smalluml::Type.__init__)


def test_smalluml::type_constructor_args():
    sig = inspect.signature(smalluml::Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::property_is_not_abstract():
    assert not inspect.isabstract(smalluml::Property)


def test_smalluml::property_constructor_exists():
    assert callable(smalluml::Property.__init__)


def test_smalluml::property_constructor_args():
    sig = inspect.signature(smalluml::Property.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_smalluml::property_has_upperBound():
    assert hasattr(smalluml::Property, "upperBound")
    descriptor = None
    for klass in smalluml::Property.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::property_has_lowerBound():
    assert hasattr(smalluml::Property, "lowerBound")
    descriptor = None
    for klass in smalluml::Property.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::operation_is_not_abstract():
    assert not inspect.isabstract(smalluml::Operation)


def test_smalluml::operation_constructor_exists():
    assert callable(smalluml::Operation.__init__)


def test_smalluml::operation_constructor_args():
    sig = inspect.signature(smalluml::Operation.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::typeinteger_is_not_abstract():
    assert not inspect.isabstract(smalluml::TypeInteger)


def test_smalluml::typeinteger_constructor_exists():
    assert callable(smalluml::TypeInteger.__init__)


def test_smalluml::typeinteger_constructor_args():
    sig = inspect.signature(smalluml::TypeInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalluml::typeinteger_has_value():
    assert hasattr(smalluml::TypeInteger, "value")
    descriptor = None
    for klass in smalluml::TypeInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::typeunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(smalluml::TypeUnlimitedNatural)


def test_smalluml::typeunlimitednatural_constructor_exists():
    assert callable(smalluml::TypeUnlimitedNatural.__init__)


def test_smalluml::typeunlimitednatural_constructor_args():
    sig = inspect.signature(smalluml::TypeUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalluml::typeunlimitednatural_has_value():
    assert hasattr(smalluml::TypeUnlimitedNatural, "value")
    descriptor = None
    for klass in smalluml::TypeUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::typereal_is_not_abstract():
    assert not inspect.isabstract(smalluml::TypeReal)


def test_smalluml::typereal_constructor_exists():
    assert callable(smalluml::TypeReal.__init__)


def test_smalluml::typereal_constructor_args():
    sig = inspect.signature(smalluml::TypeReal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalluml::typereal_has_value():
    assert hasattr(smalluml::TypeReal, "value")
    descriptor = None
    for klass in smalluml::TypeReal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::class_is_not_abstract():
    assert not inspect.isabstract(smalluml::Class)


def test_smalluml::class_constructor_exists():
    assert callable(smalluml::Class.__init__)


def test_smalluml::class_constructor_args():
    sig = inspect.signature(smalluml::Class.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::typestring_is_not_abstract():
    assert not inspect.isabstract(smalluml::TypeString)


def test_smalluml::typestring_constructor_exists():
    assert callable(smalluml::TypeString.__init__)


def test_smalluml::typestring_constructor_args():
    sig = inspect.signature(smalluml::TypeString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalluml::typestring_has_value():
    assert hasattr(smalluml::TypeString, "value")
    descriptor = None
    for klass in smalluml::TypeString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::root_is_not_abstract():
    assert not inspect.isabstract(smalluml::Root)


def test_smalluml::root_constructor_exists():
    assert callable(smalluml::Root.__init__)


def test_smalluml::root_constructor_args():
    sig = inspect.signature(smalluml::Root.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::typeboolean_is_not_abstract():
    assert not inspect.isabstract(smalluml::TypeBoolean)


def test_smalluml::typeboolean_constructor_exists():
    assert callable(smalluml::TypeBoolean.__init__)


def test_smalluml::typeboolean_constructor_args():
    sig = inspect.signature(smalluml::TypeBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalluml::typeboolean_has_value():
    assert hasattr(smalluml::TypeBoolean, "value")
    descriptor = None
    for klass in smalluml::TypeBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)


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
smalluml::NamedElement_strategy = st.builds(
    smalluml::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml::Type_strategy = st.builds(
    smalluml::Type,
)
smalluml::Property_strategy = st.builds(
    smalluml::Property,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers()
)
smalluml::Operation_strategy = st.builds(
    smalluml::Operation,
)
Type_strategy = st.builds(
    Type,
)
smalluml::TypeInteger_strategy = st.builds(
    smalluml::TypeInteger,
    value=
        safe_text
)
smalluml::TypeUnlimitedNatural_strategy = st.builds(
    smalluml::TypeUnlimitedNatural,
    value=
        safe_text
)
smalluml::TypeReal_strategy = st.builds(
    smalluml::TypeReal,
    value=
        safe_text
)
smalluml::Class_strategy = st.builds(
    smalluml::Class,
)
smalluml::TypeString_strategy = st.builds(
    smalluml::TypeString,
    value=
        safe_text
)
smalluml::Root_strategy = st.builds(
    smalluml::Root,
)
smalluml::TypeBoolean_strategy = st.builds(
    smalluml::TypeBoolean,
    value=
        safe_text
)

@given(instance=smalluml::NamedElement_strategy)
@settings(max_examples=50)
def test_smalluml::namedelement_instantiation(instance):
    assert isinstance(instance, smalluml::NamedElement)

@given(instance=smalluml::NamedElement_strategy)
def test_smalluml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::NamedElement_strategy)
def test_smalluml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=smalluml::Type_strategy)
@settings(max_examples=50)
def test_smalluml::type_instantiation(instance):
    assert isinstance(instance, smalluml::Type)

@given(instance=smalluml::Property_strategy)
@settings(max_examples=50)
def test_smalluml::property_instantiation(instance):
    assert isinstance(instance, smalluml::Property)

@given(instance=smalluml::Property_strategy)
def test_smalluml::property_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=smalluml::Property_strategy)
def test_smalluml::property_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=smalluml::Property_strategy)
def test_smalluml::property_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=smalluml::Property_strategy)
def test_smalluml::property_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=smalluml::Operation_strategy)
@settings(max_examples=50)
def test_smalluml::operation_instantiation(instance):
    assert isinstance(instance, smalluml::Operation)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml::TypeInteger_strategy)
@settings(max_examples=50)
def test_smalluml::typeinteger_instantiation(instance):
    assert isinstance(instance, smalluml::TypeInteger)

@given(instance=smalluml::TypeInteger_strategy)
def test_smalluml::typeinteger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smalluml::TypeInteger_strategy)
def test_smalluml::typeinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smalluml::TypeUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_smalluml::typeunlimitednatural_instantiation(instance):
    assert isinstance(instance, smalluml::TypeUnlimitedNatural)

@given(instance=smalluml::TypeUnlimitedNatural_strategy)
def test_smalluml::typeunlimitednatural_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smalluml::TypeUnlimitedNatural_strategy)
def test_smalluml::typeunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smalluml::TypeReal_strategy)
@settings(max_examples=50)
def test_smalluml::typereal_instantiation(instance):
    assert isinstance(instance, smalluml::TypeReal)

@given(instance=smalluml::TypeReal_strategy)
def test_smalluml::typereal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smalluml::TypeReal_strategy)
def test_smalluml::typereal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smalluml::Class_strategy)
@settings(max_examples=50)
def test_smalluml::class_instantiation(instance):
    assert isinstance(instance, smalluml::Class)

@given(instance=smalluml::TypeString_strategy)
@settings(max_examples=50)
def test_smalluml::typestring_instantiation(instance):
    assert isinstance(instance, smalluml::TypeString)

@given(instance=smalluml::TypeString_strategy)
def test_smalluml::typestring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smalluml::TypeString_strategy)
def test_smalluml::typestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smalluml::Root_strategy)
@settings(max_examples=50)
def test_smalluml::root_instantiation(instance):
    assert isinstance(instance, smalluml::Root)

@given(instance=smalluml::TypeBoolean_strategy)
@settings(max_examples=50)
def test_smalluml::typeboolean_instantiation(instance):
    assert isinstance(instance, smalluml::TypeBoolean)

@given(instance=smalluml::TypeBoolean_strategy)
def test_smalluml::typeboolean_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smalluml::TypeBoolean_strategy)
def test_smalluml::typeboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
