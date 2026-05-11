import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smalluml::Package,
    smalluml::Cardinality,
    smalluml::EnumerationElement,
    Type,
    smalluml::ConcreteType,
    smalluml::Enumeration,
    NamedElement,
    smalluml::Class,
    smalluml::Attribute,
    smalluml::Method,
    smalluml::Relation,
    smalluml::Type,
    smalluml::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smalluml::package_is_not_abstract():
    assert not inspect.isabstract(smalluml::Package)


def test_smalluml::package_constructor_exists():
    assert callable(smalluml::Package.__init__)


def test_smalluml::package_constructor_args():
    sig = inspect.signature(smalluml::Package.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::cardinality_is_not_abstract():
    assert not inspect.isabstract(smalluml::Cardinality)


def test_smalluml::cardinality_constructor_exists():
    assert callable(smalluml::Cardinality.__init__)


def test_smalluml::cardinality_constructor_args():
    sig = inspect.signature(smalluml::Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_smalluml::cardinality_has_upperBound():
    assert hasattr(smalluml::Cardinality, "upperBound")
    descriptor = None
    for klass in smalluml::Cardinality.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::cardinality_has_lowerBound():
    assert hasattr(smalluml::Cardinality, "lowerBound")
    descriptor = None
    for klass in smalluml::Cardinality.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::enumerationelement_is_not_abstract():
    assert not inspect.isabstract(smalluml::EnumerationElement)


def test_smalluml::enumerationelement_constructor_exists():
    assert callable(smalluml::EnumerationElement.__init__)


def test_smalluml::enumerationelement_constructor_args():
    sig = inspect.signature(smalluml::EnumerationElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalluml::enumerationelement_has_value():
    assert hasattr(smalluml::EnumerationElement, "value")
    descriptor = None
    for klass in smalluml::EnumerationElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::concretetype_is_not_abstract():
    assert not inspect.isabstract(smalluml::ConcreteType)


def test_smalluml::concretetype_constructor_exists():
    assert callable(smalluml::ConcreteType.__init__)


def test_smalluml::concretetype_constructor_args():
    sig = inspect.signature(smalluml::ConcreteType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml::Enumeration)


def test_smalluml::enumeration_constructor_exists():
    assert callable(smalluml::Enumeration.__init__)


def test_smalluml::enumeration_constructor_args():
    sig = inspect.signature(smalluml::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
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



def test_smalluml::attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml::Attribute)


def test_smalluml::attribute_constructor_exists():
    assert callable(smalluml::Attribute.__init__)


def test_smalluml::attribute_constructor_args():
    sig = inspect.signature(smalluml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::method_is_not_abstract():
    assert not inspect.isabstract(smalluml::Method)


def test_smalluml::method_constructor_exists():
    assert callable(smalluml::Method.__init__)


def test_smalluml::method_constructor_args():
    sig = inspect.signature(smalluml::Method.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::relation_is_not_abstract():
    assert not inspect.isabstract(smalluml::Relation)


def test_smalluml::relation_constructor_exists():
    assert callable(smalluml::Relation.__init__)


def test_smalluml::relation_constructor_args():
    sig = inspect.signature(smalluml::Relation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::type_is_not_abstract():
    assert not inspect.isabstract(smalluml::Type)


def test_smalluml::type_constructor_exists():
    assert callable(smalluml::Type.__init__)


def test_smalluml::type_constructor_args():
    sig = inspect.signature(smalluml::Type.__init__)
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
smalluml::Package_strategy = st.builds(
    smalluml::Package,
)
smalluml::Cardinality_strategy = st.builds(
    smalluml::Cardinality,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers()
)
smalluml::EnumerationElement_strategy = st.builds(
    smalluml::EnumerationElement,
    value=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
smalluml::ConcreteType_strategy = st.builds(
    smalluml::ConcreteType,
)
smalluml::Enumeration_strategy = st.builds(
    smalluml::Enumeration,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml::Class_strategy = st.builds(
    smalluml::Class,
    isAbstract=
        st.booleans()
)
smalluml::Attribute_strategy = st.builds(
    smalluml::Attribute,
)
smalluml::Method_strategy = st.builds(
    smalluml::Method,
)
smalluml::Relation_strategy = st.builds(
    smalluml::Relation,
)
smalluml::Type_strategy = st.builds(
    smalluml::Type,
)
smalluml::NamedElement_strategy = st.builds(
    smalluml::NamedElement,
    name=
        safe_text
)

@given(instance=smalluml::Package_strategy)
@settings(max_examples=50)
def test_smalluml::package_instantiation(instance):
    assert isinstance(instance, smalluml::Package)

@given(instance=smalluml::Cardinality_strategy)
@settings(max_examples=50)
def test_smalluml::cardinality_instantiation(instance):
    assert isinstance(instance, smalluml::Cardinality)

@given(instance=smalluml::Cardinality_strategy)
def test_smalluml::cardinality_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=smalluml::Cardinality_strategy)
def test_smalluml::cardinality_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=smalluml::Cardinality_strategy)
def test_smalluml::cardinality_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=smalluml::Cardinality_strategy)
def test_smalluml::cardinality_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=smalluml::EnumerationElement_strategy)
@settings(max_examples=50)
def test_smalluml::enumerationelement_instantiation(instance):
    assert isinstance(instance, smalluml::EnumerationElement)

@given(instance=smalluml::EnumerationElement_strategy)
def test_smalluml::enumerationelement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smalluml::EnumerationElement_strategy)
def test_smalluml::enumerationelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml::ConcreteType_strategy)
@settings(max_examples=50)
def test_smalluml::concretetype_instantiation(instance):
    assert isinstance(instance, smalluml::ConcreteType)

@given(instance=smalluml::Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml::enumeration_instantiation(instance):
    assert isinstance(instance, smalluml::Enumeration)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

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

@given(instance=smalluml::Attribute_strategy)
@settings(max_examples=50)
def test_smalluml::attribute_instantiation(instance):
    assert isinstance(instance, smalluml::Attribute)

@given(instance=smalluml::Method_strategy)
@settings(max_examples=50)
def test_smalluml::method_instantiation(instance):
    assert isinstance(instance, smalluml::Method)

@given(instance=smalluml::Relation_strategy)
@settings(max_examples=50)
def test_smalluml::relation_instantiation(instance):
    assert isinstance(instance, smalluml::Relation)

@given(instance=smalluml::Type_strategy)
@settings(max_examples=50)
def test_smalluml::type_instantiation(instance):
    assert isinstance(instance, smalluml::Type)

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
