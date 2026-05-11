import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smalluml::Operation,
    Type,
    smalluml::RealType,
    smalluml::IntegerType,
    smalluml::BooleanType,
    smalluml::Enumeration,
    smalluml::Attribute,
    Entity,
    smalluml::Class,
    smalluml::Association,
    smalluml::Cardinalities,
    smalluml::Parameter,
    smalluml::Type,
    smalluml::Entity,
    smalluml::ClassDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smalluml::operation_is_not_abstract():
    assert not inspect.isabstract(smalluml::Operation)


def test_smalluml::operation_constructor_exists():
    assert callable(smalluml::Operation.__init__)


def test_smalluml::operation_constructor_args():
    sig = inspect.signature(smalluml::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::operation_has_name():
    assert hasattr(smalluml::Operation, "name")
    descriptor = None
    for klass in smalluml::Operation.__mro__:
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



def test_smalluml::realtype_is_not_abstract():
    assert not inspect.isabstract(smalluml::RealType)


def test_smalluml::realtype_constructor_exists():
    assert callable(smalluml::RealType.__init__)


def test_smalluml::realtype_constructor_args():
    sig = inspect.signature(smalluml::RealType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::integertype_is_not_abstract():
    assert not inspect.isabstract(smalluml::IntegerType)


def test_smalluml::integertype_constructor_exists():
    assert callable(smalluml::IntegerType.__init__)


def test_smalluml::integertype_constructor_args():
    sig = inspect.signature(smalluml::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::booleantype_is_not_abstract():
    assert not inspect.isabstract(smalluml::BooleanType)


def test_smalluml::booleantype_constructor_exists():
    assert callable(smalluml::BooleanType.__init__)


def test_smalluml::booleantype_constructor_args():
    sig = inspect.signature(smalluml::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml::Enumeration)


def test_smalluml::enumeration_constructor_exists():
    assert callable(smalluml::Enumeration.__init__)


def test_smalluml::enumeration_constructor_args():
    sig = inspect.signature(smalluml::Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "variable" in params, "Missing parameter 'variable'"

def test_smalluml::enumeration_has_name():
    assert hasattr(smalluml::Enumeration, "name")
    descriptor = None
    for klass in smalluml::Enumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::enumeration_has_variable():
    assert hasattr(smalluml::Enumeration, "variable")
    descriptor = None
    for klass in smalluml::Enumeration.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml::Attribute)


def test_smalluml::attribute_constructor_exists():
    assert callable(smalluml::Attribute.__init__)


def test_smalluml::attribute_constructor_args():
    sig = inspect.signature(smalluml::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::attribute_has_name():
    assert hasattr(smalluml::Attribute, "name")
    descriptor = None
    for klass in smalluml::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::class_is_not_abstract():
    assert not inspect.isabstract(smalluml::Class)


def test_smalluml::class_constructor_exists():
    assert callable(smalluml::Class.__init__)


def test_smalluml::class_constructor_args():
    sig = inspect.signature(smalluml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_smalluml::class_has_abstract():
    assert hasattr(smalluml::Class, "abstract")
    descriptor = None
    for klass in smalluml::Class.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::association_is_not_abstract():
    assert not inspect.isabstract(smalluml::Association)


def test_smalluml::association_constructor_exists():
    assert callable(smalluml::Association.__init__)


def test_smalluml::association_constructor_args():
    sig = inspect.signature(smalluml::Association.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::cardinalities_is_not_abstract():
    assert not inspect.isabstract(smalluml::Cardinalities)


def test_smalluml::cardinalities_constructor_exists():
    assert callable(smalluml::Cardinalities.__init__)


def test_smalluml::cardinalities_constructor_args():
    sig = inspect.signature(smalluml::Cardinalities.__init__)
    params = list(sig.parameters.keys())
    assert "upperbound" in params, "Missing parameter 'upperbound'"
    assert "lowerbound" in params, "Missing parameter 'lowerbound'"

def test_smalluml::cardinalities_has_upperbound():
    assert hasattr(smalluml::Cardinalities, "upperbound")
    descriptor = None
    for klass in smalluml::Cardinalities.__mro__:
        if "upperbound" in klass.__dict__:
            descriptor = klass.__dict__["upperbound"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::cardinalities_has_lowerbound():
    assert hasattr(smalluml::Cardinalities, "lowerbound")
    descriptor = None
    for klass in smalluml::Cardinalities.__mro__:
        if "lowerbound" in klass.__dict__:
            descriptor = klass.__dict__["lowerbound"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::parameter_is_not_abstract():
    assert not inspect.isabstract(smalluml::Parameter)


def test_smalluml::parameter_constructor_exists():
    assert callable(smalluml::Parameter.__init__)


def test_smalluml::parameter_constructor_args():
    sig = inspect.signature(smalluml::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::parameter_has_name():
    assert hasattr(smalluml::Parameter, "name")
    descriptor = None
    for klass in smalluml::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::type_is_not_abstract():
    assert not inspect.isabstract(smalluml::Type)


def test_smalluml::type_constructor_exists():
    assert callable(smalluml::Type.__init__)


def test_smalluml::type_constructor_args():
    sig = inspect.signature(smalluml::Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::entity_is_not_abstract():
    assert not inspect.isabstract(smalluml::Entity)


def test_smalluml::entity_constructor_exists():
    assert callable(smalluml::Entity.__init__)


def test_smalluml::entity_constructor_args():
    sig = inspect.signature(smalluml::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::entity_has_name():
    assert hasattr(smalluml::Entity, "name")
    descriptor = None
    for klass in smalluml::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::classdiagram_is_not_abstract():
    assert not inspect.isabstract(smalluml::ClassDiagram)


def test_smalluml::classdiagram_constructor_exists():
    assert callable(smalluml::ClassDiagram.__init__)


def test_smalluml::classdiagram_constructor_args():
    sig = inspect.signature(smalluml::ClassDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::classdiagram_has_name():
    assert hasattr(smalluml::ClassDiagram, "name")
    descriptor = None
    for klass in smalluml::ClassDiagram.__mro__:
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
smalluml::Operation_strategy = st.builds(
    smalluml::Operation,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
smalluml::RealType_strategy = st.builds(
    smalluml::RealType,
)
smalluml::IntegerType_strategy = st.builds(
    smalluml::IntegerType,
)
smalluml::BooleanType_strategy = st.builds(
    smalluml::BooleanType,
)
smalluml::Enumeration_strategy = st.builds(
    smalluml::Enumeration,
    name=
        safe_text,
    variable=
        safe_text
)
smalluml::Attribute_strategy = st.builds(
    smalluml::Attribute,
    name=
        safe_text
)
Entity_strategy = st.builds(
    Entity,
)
smalluml::Class_strategy = st.builds(
    smalluml::Class,
    abstract=
        st.booleans()
)
smalluml::Association_strategy = st.builds(
    smalluml::Association,
)
smalluml::Cardinalities_strategy = st.builds(
    smalluml::Cardinalities,
    upperbound=
        st.integers(),
    lowerbound=
        st.integers()
)
smalluml::Parameter_strategy = st.builds(
    smalluml::Parameter,
    name=
        safe_text
)
smalluml::Type_strategy = st.builds(
    smalluml::Type,
)
smalluml::Entity_strategy = st.builds(
    smalluml::Entity,
    name=
        safe_text
)
smalluml::ClassDiagram_strategy = st.builds(
    smalluml::ClassDiagram,
    name=
        safe_text
)

@given(instance=smalluml::Operation_strategy)
@settings(max_examples=50)
def test_smalluml::operation_instantiation(instance):
    assert isinstance(instance, smalluml::Operation)

@given(instance=smalluml::Operation_strategy)
def test_smalluml::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::Operation_strategy)
def test_smalluml::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml::RealType_strategy)
@settings(max_examples=50)
def test_smalluml::realtype_instantiation(instance):
    assert isinstance(instance, smalluml::RealType)

@given(instance=smalluml::IntegerType_strategy)
@settings(max_examples=50)
def test_smalluml::integertype_instantiation(instance):
    assert isinstance(instance, smalluml::IntegerType)

@given(instance=smalluml::BooleanType_strategy)
@settings(max_examples=50)
def test_smalluml::booleantype_instantiation(instance):
    assert isinstance(instance, smalluml::BooleanType)

@given(instance=smalluml::Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml::enumeration_instantiation(instance):
    assert isinstance(instance, smalluml::Enumeration)

@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=smalluml::Attribute_strategy)
@settings(max_examples=50)
def test_smalluml::attribute_instantiation(instance):
    assert isinstance(instance, smalluml::Attribute)

@given(instance=smalluml::Attribute_strategy)
def test_smalluml::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::Attribute_strategy)
def test_smalluml::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=smalluml::Class_strategy)
@settings(max_examples=50)
def test_smalluml::class_instantiation(instance):
    assert isinstance(instance, smalluml::Class)

@given(instance=smalluml::Class_strategy)
def test_smalluml::class_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=smalluml::Class_strategy)
def test_smalluml::class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=smalluml::Association_strategy)
@settings(max_examples=50)
def test_smalluml::association_instantiation(instance):
    assert isinstance(instance, smalluml::Association)

@given(instance=smalluml::Cardinalities_strategy)
@settings(max_examples=50)
def test_smalluml::cardinalities_instantiation(instance):
    assert isinstance(instance, smalluml::Cardinalities)

@given(instance=smalluml::Cardinalities_strategy)
def test_smalluml::cardinalities_upperbound_type(instance):
    assert isinstance(instance.upperbound, int)


@given(instance=smalluml::Cardinalities_strategy)
def test_smalluml::cardinalities_upperbound_setter(instance):
    original = instance.upperbound
    instance.upperbound = original
    assert instance.upperbound == original

@given(instance=smalluml::Cardinalities_strategy)
def test_smalluml::cardinalities_lowerbound_type(instance):
    assert isinstance(instance.lowerbound, int)


@given(instance=smalluml::Cardinalities_strategy)
def test_smalluml::cardinalities_lowerbound_setter(instance):
    original = instance.lowerbound
    instance.lowerbound = original
    assert instance.lowerbound == original

@given(instance=smalluml::Parameter_strategy)
@settings(max_examples=50)
def test_smalluml::parameter_instantiation(instance):
    assert isinstance(instance, smalluml::Parameter)

@given(instance=smalluml::Parameter_strategy)
def test_smalluml::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::Parameter_strategy)
def test_smalluml::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml::Type_strategy)
@settings(max_examples=50)
def test_smalluml::type_instantiation(instance):
    assert isinstance(instance, smalluml::Type)

@given(instance=smalluml::Entity_strategy)
@settings(max_examples=50)
def test_smalluml::entity_instantiation(instance):
    assert isinstance(instance, smalluml::Entity)

@given(instance=smalluml::Entity_strategy)
def test_smalluml::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::Entity_strategy)
def test_smalluml::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml::ClassDiagram_strategy)
@settings(max_examples=50)
def test_smalluml::classdiagram_instantiation(instance):
    assert isinstance(instance, smalluml::ClassDiagram)

@given(instance=smalluml::ClassDiagram_strategy)
def test_smalluml::classdiagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::ClassDiagram_strategy)
def test_smalluml::classdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
