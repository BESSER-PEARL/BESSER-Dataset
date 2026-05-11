import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smalluml::Role,
    smalluml::Methode,
    smalluml::Attribute,
    smalluml::Association,
    smalluml::SmallClass,
    smalluml::Generalisation,
    smalluml::SchemaUML,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smalluml::role_is_not_abstract():
    assert not inspect.isabstract(smalluml::Role)


def test_smalluml::role_constructor_exists():
    assert callable(smalluml::Role.__init__)


def test_smalluml::role_constructor_args():
    sig = inspect.signature(smalluml::Role.__init__)
    params = list(sig.parameters.keys())
    assert "Multiplicity" in params, "Missing parameter 'Multiplicity'"

def test_smalluml::role_has_Multiplicity():
    assert hasattr(smalluml::Role, "Multiplicity")
    descriptor = None
    for klass in smalluml::Role.__mro__:
        if "Multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["Multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::methode_is_not_abstract():
    assert not inspect.isabstract(smalluml::Methode)


def test_smalluml::methode_constructor_exists():
    assert callable(smalluml::Methode.__init__)


def test_smalluml::methode_constructor_args():
    sig = inspect.signature(smalluml::Methode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "returnType" in params, "Missing parameter 'returnType'"

def test_smalluml::methode_has_name():
    assert hasattr(smalluml::Methode, "name")
    descriptor = None
    for klass in smalluml::Methode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::methode_has_returnType():
    assert hasattr(smalluml::Methode, "returnType")
    descriptor = None
    for klass in smalluml::Methode.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml::Attribute)


def test_smalluml::attribute_constructor_exists():
    assert callable(smalluml::Attribute.__init__)


def test_smalluml::attribute_constructor_args():
    sig = inspect.signature(smalluml::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::attribute_has_type():
    assert hasattr(smalluml::Attribute, "type")
    descriptor = None
    for klass in smalluml::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::attribute_has_name():
    assert hasattr(smalluml::Attribute, "name")
    descriptor = None
    for klass in smalluml::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::association_is_not_abstract():
    assert not inspect.isabstract(smalluml::Association)


def test_smalluml::association_constructor_exists():
    assert callable(smalluml::Association.__init__)


def test_smalluml::association_constructor_args():
    sig = inspect.signature(smalluml::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::association_has_name():
    assert hasattr(smalluml::Association, "name")
    descriptor = None
    for klass in smalluml::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::smallclass_is_not_abstract():
    assert not inspect.isabstract(smalluml::SmallClass)


def test_smalluml::smallclass_constructor_exists():
    assert callable(smalluml::SmallClass.__init__)


def test_smalluml::smallclass_constructor_args():
    sig = inspect.signature(smalluml::SmallClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::smallclass_has_name():
    assert hasattr(smalluml::SmallClass, "name")
    descriptor = None
    for klass in smalluml::SmallClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::generalisation_is_not_abstract():
    assert not inspect.isabstract(smalluml::Generalisation)


def test_smalluml::generalisation_constructor_exists():
    assert callable(smalluml::Generalisation.__init__)


def test_smalluml::generalisation_constructor_args():
    sig = inspect.signature(smalluml::Generalisation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::schemauml_is_not_abstract():
    assert not inspect.isabstract(smalluml::SchemaUML)


def test_smalluml::schemauml_constructor_exists():
    assert callable(smalluml::SchemaUML.__init__)


def test_smalluml::schemauml_constructor_args():
    sig = inspect.signature(smalluml::SchemaUML.__init__)
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
smalluml::Role_strategy = st.builds(
    smalluml::Role,
    Multiplicity=
        safe_text
)
smalluml::Methode_strategy = st.builds(
    smalluml::Methode,
    name=
        safe_text,
    returnType=
        safe_text
)
smalluml::Attribute_strategy = st.builds(
    smalluml::Attribute,
    type=
        safe_text,
    name=
        safe_text
)
smalluml::Association_strategy = st.builds(
    smalluml::Association,
    name=
        safe_text
)
smalluml::SmallClass_strategy = st.builds(
    smalluml::SmallClass,
    name=
        safe_text
)
smalluml::Generalisation_strategy = st.builds(
    smalluml::Generalisation,
)
smalluml::SchemaUML_strategy = st.builds(
    smalluml::SchemaUML,
)

@given(instance=smalluml::Role_strategy)
@settings(max_examples=50)
def test_smalluml::role_instantiation(instance):
    assert isinstance(instance, smalluml::Role)

@given(instance=smalluml::Role_strategy)
def test_smalluml::role_Multiplicity_type(instance):
    assert isinstance(instance.Multiplicity, str)


@given(instance=smalluml::Role_strategy)
def test_smalluml::role_Multiplicity_setter(instance):
    original = instance.Multiplicity
    instance.Multiplicity = original
    assert instance.Multiplicity == original

@given(instance=smalluml::Methode_strategy)
@settings(max_examples=50)
def test_smalluml::methode_instantiation(instance):
    assert isinstance(instance, smalluml::Methode)

@given(instance=smalluml::Methode_strategy)
def test_smalluml::methode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::Methode_strategy)
def test_smalluml::methode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml::Methode_strategy)
def test_smalluml::methode_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=smalluml::Methode_strategy)
def test_smalluml::methode_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=smalluml::Attribute_strategy)
@settings(max_examples=50)
def test_smalluml::attribute_instantiation(instance):
    assert isinstance(instance, smalluml::Attribute)

@given(instance=smalluml::Attribute_strategy)
def test_smalluml::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=smalluml::Attribute_strategy)
def test_smalluml::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=smalluml::Attribute_strategy)
def test_smalluml::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::Attribute_strategy)
def test_smalluml::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml::Association_strategy)
@settings(max_examples=50)
def test_smalluml::association_instantiation(instance):
    assert isinstance(instance, smalluml::Association)

@given(instance=smalluml::Association_strategy)
def test_smalluml::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::Association_strategy)
def test_smalluml::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml::SmallClass_strategy)
@settings(max_examples=50)
def test_smalluml::smallclass_instantiation(instance):
    assert isinstance(instance, smalluml::SmallClass)

@given(instance=smalluml::SmallClass_strategy)
def test_smalluml::smallclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::SmallClass_strategy)
def test_smalluml::smallclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml::Generalisation_strategy)
@settings(max_examples=50)
def test_smalluml::generalisation_instantiation(instance):
    assert isinstance(instance, smalluml::Generalisation)

@given(instance=smalluml::SchemaUML_strategy)
@settings(max_examples=50)
def test_smalluml::schemauml_instantiation(instance):
    assert isinstance(instance, smalluml::SchemaUML)
