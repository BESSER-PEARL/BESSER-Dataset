import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metamodel::HibernateAnnotation,
    metamodel::Attribute,
    Type,
    metamodel::Entity,
    metamodel::Datatype,
    metamodel::Type,
    metamodel::Model,
    HibernateCascadeTypes,
    HibernateAnnotationTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodel::hibernateannotation_is_not_abstract():
    assert not inspect.isabstract(metamodel::HibernateAnnotation)


def test_metamodel::hibernateannotation_constructor_exists():
    assert callable(metamodel::HibernateAnnotation.__init__)


def test_metamodel::hibernateannotation_constructor_args():
    sig = inspect.signature(metamodel::HibernateAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "annotationType" in params, "Missing parameter 'annotationType'"
    assert "cascade" in params, "Missing parameter 'cascade'"

def test_metamodel::hibernateannotation_has_unique():
    assert hasattr(metamodel::HibernateAnnotation, "unique")
    descriptor = None
    for klass in metamodel::HibernateAnnotation.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::hibernateannotation_has_annotationType():
    assert hasattr(metamodel::HibernateAnnotation, "annotationType")
    descriptor = None
    for klass in metamodel::HibernateAnnotation.__mro__:
        if "annotationType" in klass.__dict__:
            descriptor = klass.__dict__["annotationType"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::hibernateannotation_has_cascade():
    assert hasattr(metamodel::HibernateAnnotation, "cascade")
    descriptor = None
    for klass in metamodel::HibernateAnnotation.__mro__:
        if "cascade" in klass.__dict__:
            descriptor = klass.__dict__["cascade"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::attribute_is_not_abstract():
    assert not inspect.isabstract(metamodel::Attribute)


def test_metamodel::attribute_constructor_exists():
    assert callable(metamodel::Attribute.__init__)


def test_metamodel::attribute_constructor_args():
    sig = inspect.signature(metamodel::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "list" in params, "Missing parameter 'list'"

def test_metamodel::attribute_has_name():
    assert hasattr(metamodel::Attribute, "name")
    descriptor = None
    for klass in metamodel::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::attribute_has_list():
    assert hasattr(metamodel::Attribute, "list")
    descriptor = None
    for klass in metamodel::Attribute.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::entity_is_not_abstract():
    assert not inspect.isabstract(metamodel::Entity)


def test_metamodel::entity_constructor_exists():
    assert callable(metamodel::Entity.__init__)


def test_metamodel::entity_constructor_args():
    sig = inspect.signature(metamodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::datatype_is_not_abstract():
    assert not inspect.isabstract(metamodel::Datatype)


def test_metamodel::datatype_constructor_exists():
    assert callable(metamodel::Datatype.__init__)


def test_metamodel::datatype_constructor_args():
    sig = inspect.signature(metamodel::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::type_is_not_abstract():
    assert not inspect.isabstract(metamodel::Type)


def test_metamodel::type_constructor_exists():
    assert callable(metamodel::Type.__init__)


def test_metamodel::type_constructor_args():
    sig = inspect.signature(metamodel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::type_has_name():
    assert hasattr(metamodel::Type, "name")
    descriptor = None
    for klass in metamodel::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::model_is_not_abstract():
    assert not inspect.isabstract(metamodel::Model)


def test_metamodel::model_constructor_exists():
    assert callable(metamodel::Model.__init__)


def test_metamodel::model_constructor_args():
    sig = inspect.signature(metamodel::Model.__init__)
    params = list(sig.parameters.keys())

def test_hibernatecascadetypes_exists():
    # Check that the Enumeration exists
    assert HibernateCascadeTypes is not None

def test_hibernatecascadetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HibernateCascadeTypes]
    expected_literals = [
        "CascadeAll",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HibernateCascadeTypes"

def test_hibernateannotationtypes_exists():
    # Check that the Enumeration exists
    assert HibernateAnnotationTypes is not None

def test_hibernateannotationtypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HibernateAnnotationTypes]
    expected_literals = [
        "OneToOne",
        "OneToMany",
        "Column",
        "ManyToMany",
        "ManyToOne",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HibernateAnnotationTypes"


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
metamodel::HibernateAnnotation_strategy = st.builds(
    metamodel::HibernateAnnotation,
    unique=
        safe_text,
    annotationType=
        safe_text,
    cascade=
        safe_text
)
metamodel::Attribute_strategy = st.builds(
    metamodel::Attribute,
    name=
        safe_text,
    list=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
metamodel::Entity_strategy = st.builds(
    metamodel::Entity,
)
metamodel::Datatype_strategy = st.builds(
    metamodel::Datatype,
)
metamodel::Type_strategy = st.builds(
    metamodel::Type,
    name=
        safe_text
)
metamodel::Model_strategy = st.builds(
    metamodel::Model,
)

@given(instance=metamodel::HibernateAnnotation_strategy)
@settings(max_examples=50)
def test_metamodel::hibernateannotation_instantiation(instance):
    assert isinstance(instance, metamodel::HibernateAnnotation)

@given(instance=metamodel::HibernateAnnotation_strategy)
def test_metamodel::hibernateannotation_unique_type(instance):
    assert isinstance(instance.unique, str)


@given(instance=metamodel::HibernateAnnotation_strategy)
def test_metamodel::hibernateannotation_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=metamodel::HibernateAnnotation_strategy)
def test_metamodel::hibernateannotation_annotationType_type(instance):
    assert isinstance(instance.annotationType, str)


@given(instance=metamodel::HibernateAnnotation_strategy)
def test_metamodel::hibernateannotation_annotationType_setter(instance):
    original = instance.annotationType
    instance.annotationType = original
    assert instance.annotationType == original

@given(instance=metamodel::HibernateAnnotation_strategy)
def test_metamodel::hibernateannotation_cascade_type(instance):
    assert isinstance(instance.cascade, str)


@given(instance=metamodel::HibernateAnnotation_strategy)
def test_metamodel::hibernateannotation_cascade_setter(instance):
    original = instance.cascade
    instance.cascade = original
    assert instance.cascade == original

@given(instance=metamodel::Attribute_strategy)
@settings(max_examples=50)
def test_metamodel::attribute_instantiation(instance):
    assert isinstance(instance, metamodel::Attribute)

@given(instance=metamodel::Attribute_strategy)
def test_metamodel::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Attribute_strategy)
def test_metamodel::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Attribute_strategy)
def test_metamodel::attribute_list_type(instance):
    assert isinstance(instance.list, bool)


@given(instance=metamodel::Attribute_strategy)
def test_metamodel::attribute_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=metamodel::Entity_strategy)
@settings(max_examples=50)
def test_metamodel::entity_instantiation(instance):
    assert isinstance(instance, metamodel::Entity)

@given(instance=metamodel::Datatype_strategy)
@settings(max_examples=50)
def test_metamodel::datatype_instantiation(instance):
    assert isinstance(instance, metamodel::Datatype)

@given(instance=metamodel::Type_strategy)
@settings(max_examples=50)
def test_metamodel::type_instantiation(instance):
    assert isinstance(instance, metamodel::Type)

@given(instance=metamodel::Type_strategy)
def test_metamodel::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Type_strategy)
def test_metamodel::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Model_strategy)
@settings(max_examples=50)
def test_metamodel::model_instantiation(instance):
    assert isinstance(instance, metamodel::Model)
