import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SuperType,
    smalluml::Enumeration,
    smalluml::Type,
    smalluml::Class,
    NamedElement,
    smalluml::Role,
    smalluml::Parameter,
    smalluml::Operation,
    smalluml::Package,
    smalluml::Association,
    smalluml::Attribute,
    smalluml::SuperType,
    smalluml::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_supertype_is_not_abstract():
    assert not inspect.isabstract(SuperType)


def test_supertype_constructor_exists():
    assert callable(SuperType.__init__)


def test_supertype_constructor_args():
    sig = inspect.signature(SuperType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml::Enumeration)


def test_smalluml::enumeration_constructor_exists():
    assert callable(smalluml::Enumeration.__init__)


def test_smalluml::enumeration_constructor_args():
    sig = inspect.signature(smalluml::Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "enumeration" in params, "Missing parameter 'enumeration'"

def test_smalluml::enumeration_has_enumeration():
    assert hasattr(smalluml::Enumeration, "enumeration")
    descriptor = None
    for klass in smalluml::Enumeration.__mro__:
        if "enumeration" in klass.__dict__:
            descriptor = klass.__dict__["enumeration"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::type_is_not_abstract():
    assert not inspect.isabstract(smalluml::Type)


def test_smalluml::type_constructor_exists():
    assert callable(smalluml::Type.__init__)


def test_smalluml::type_constructor_args():
    sig = inspect.signature(smalluml::Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::class_is_not_abstract():
    assert not inspect.isabstract(smalluml::Class)


def test_smalluml::class_constructor_exists():
    assert callable(smalluml::Class.__init__)


def test_smalluml::class_constructor_args():
    sig = inspect.signature(smalluml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_smalluml::class_has_isAbstract():
    assert hasattr(smalluml::Class, "isAbstract")
    descriptor = None
    for klass in smalluml::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::role_is_not_abstract():
    assert not inspect.isabstract(smalluml::Role)


def test_smalluml::role_constructor_exists():
    assert callable(smalluml::Role.__init__)


def test_smalluml::role_constructor_args():
    sig = inspect.signature(smalluml::Role.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_smalluml::role_has_lowerBound():
    assert hasattr(smalluml::Role, "lowerBound")
    descriptor = None
    for klass in smalluml::Role.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::role_has_upperBound():
    assert hasattr(smalluml::Role, "upperBound")
    descriptor = None
    for klass in smalluml::Role.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::parameter_is_not_abstract():
    assert not inspect.isabstract(smalluml::Parameter)


def test_smalluml::parameter_constructor_exists():
    assert callable(smalluml::Parameter.__init__)


def test_smalluml::parameter_constructor_args():
    sig = inspect.signature(smalluml::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::operation_is_not_abstract():
    assert not inspect.isabstract(smalluml::Operation)


def test_smalluml::operation_constructor_exists():
    assert callable(smalluml::Operation.__init__)


def test_smalluml::operation_constructor_args():
    sig = inspect.signature(smalluml::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_smalluml::operation_has_isAbstract():
    assert hasattr(smalluml::Operation, "isAbstract")
    descriptor = None
    for klass in smalluml::Operation.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::package_is_not_abstract():
    assert not inspect.isabstract(smalluml::Package)


def test_smalluml::package_constructor_exists():
    assert callable(smalluml::Package.__init__)


def test_smalluml::package_constructor_args():
    sig = inspect.signature(smalluml::Package.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::association_is_not_abstract():
    assert not inspect.isabstract(smalluml::Association)


def test_smalluml::association_constructor_exists():
    assert callable(smalluml::Association.__init__)


def test_smalluml::association_constructor_args():
    sig = inspect.signature(smalluml::Association.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml::Attribute)


def test_smalluml::attribute_constructor_exists():
    assert callable(smalluml::Attribute.__init__)


def test_smalluml::attribute_constructor_args():
    sig = inspect.signature(smalluml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::supertype_is_not_abstract():
    assert not inspect.isabstract(smalluml::SuperType)


def test_smalluml::supertype_constructor_exists():
    assert callable(smalluml::SuperType.__init__)


def test_smalluml::supertype_constructor_args():
    sig = inspect.signature(smalluml::SuperType.__init__)
    params = list(sig.parameters.keys())



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
SuperType_strategy = st.builds(
    SuperType,
)
smalluml::Enumeration_strategy = st.builds(
    smalluml::Enumeration,
    enumeration=
        safe_text
)
smalluml::Type_strategy = st.builds(
    smalluml::Type,
)
smalluml::Class_strategy = st.builds(
    smalluml::Class,
    isAbstract=
        st.booleans()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml::Role_strategy = st.builds(
    smalluml::Role,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)
smalluml::Parameter_strategy = st.builds(
    smalluml::Parameter,
)
smalluml::Operation_strategy = st.builds(
    smalluml::Operation,
    isAbstract=
        st.booleans()
)
smalluml::Package_strategy = st.builds(
    smalluml::Package,
)
smalluml::Association_strategy = st.builds(
    smalluml::Association,
)
smalluml::Attribute_strategy = st.builds(
    smalluml::Attribute,
)
smalluml::SuperType_strategy = st.builds(
    smalluml::SuperType,
)
smalluml::NamedElement_strategy = st.builds(
    smalluml::NamedElement,
    name=
        safe_text
)

@given(instance=SuperType_strategy)
@settings(max_examples=50)
def test_supertype_instantiation(instance):
    assert isinstance(instance, SuperType)

@given(instance=smalluml::Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml::enumeration_instantiation(instance):
    assert isinstance(instance, smalluml::Enumeration)

@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_enumeration_type(instance):
    assert isinstance(instance.enumeration, str)


@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_enumeration_setter(instance):
    original = instance.enumeration
    instance.enumeration = original
    assert instance.enumeration == original

@given(instance=smalluml::Type_strategy)
@settings(max_examples=50)
def test_smalluml::type_instantiation(instance):
    assert isinstance(instance, smalluml::Type)

@given(instance=smalluml::Class_strategy)
@settings(max_examples=50)
def test_smalluml::class_instantiation(instance):
    assert isinstance(instance, smalluml::Class)

@given(instance=smalluml::Class_strategy)
def test_smalluml::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=smalluml::Class_strategy)
def test_smalluml::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=smalluml::Role_strategy)
@settings(max_examples=50)
def test_smalluml::role_instantiation(instance):
    assert isinstance(instance, smalluml::Role)

@given(instance=smalluml::Role_strategy)
def test_smalluml::role_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=smalluml::Role_strategy)
def test_smalluml::role_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=smalluml::Role_strategy)
def test_smalluml::role_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=smalluml::Role_strategy)
def test_smalluml::role_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=smalluml::Parameter_strategy)
@settings(max_examples=50)
def test_smalluml::parameter_instantiation(instance):
    assert isinstance(instance, smalluml::Parameter)

@given(instance=smalluml::Operation_strategy)
@settings(max_examples=50)
def test_smalluml::operation_instantiation(instance):
    assert isinstance(instance, smalluml::Operation)

@given(instance=smalluml::Operation_strategy)
def test_smalluml::operation_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=smalluml::Operation_strategy)
def test_smalluml::operation_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=smalluml::Package_strategy)
@settings(max_examples=50)
def test_smalluml::package_instantiation(instance):
    assert isinstance(instance, smalluml::Package)

@given(instance=smalluml::Association_strategy)
@settings(max_examples=50)
def test_smalluml::association_instantiation(instance):
    assert isinstance(instance, smalluml::Association)

@given(instance=smalluml::Attribute_strategy)
@settings(max_examples=50)
def test_smalluml::attribute_instantiation(instance):
    assert isinstance(instance, smalluml::Attribute)

@given(instance=smalluml::SuperType_strategy)
@settings(max_examples=50)
def test_smalluml::supertype_instantiation(instance):
    assert isinstance(instance, smalluml::SuperType)

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
