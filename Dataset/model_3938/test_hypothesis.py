import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    smalluml_Role,
    smalluml_Methode,
    smalluml_Attribute,
    smalluml_Association,
    smalluml_SmallClass,
    smalluml_Generalisation,
    smalluml_SchemaUML,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smalluml_role_is_not_abstract():
    assert not inspect.isabstract(smalluml_Role)


def test_smalluml_role_constructor_exists():
    assert callable(smalluml_Role.__init__)


def test_smalluml_role_constructor_args():
    sig = inspect.signature(smalluml_Role.__init__)
    params = list(sig.parameters.keys())
    assert "Multiplicity" in params, "Missing parameter 'Multiplicity'"

def test_smalluml_role_has_Multiplicity():
    assert hasattr(smalluml_Role, "Multiplicity")
    descriptor = None
    for klass in smalluml_Role.__mro__:
        if "Multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["Multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_methode_is_not_abstract():
    assert not inspect.isabstract(smalluml_Methode)


def test_smalluml_methode_constructor_exists():
    assert callable(smalluml_Methode.__init__)


def test_smalluml_methode_constructor_args():
    sig = inspect.signature(smalluml_Methode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "returnType" in params, "Missing parameter 'returnType'"

def test_smalluml_methode_has_name():
    assert hasattr(smalluml_Methode, "name")
    descriptor = None
    for klass in smalluml_Methode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smalluml_methode_has_returnType():
    assert hasattr(smalluml_Methode, "returnType")
    descriptor = None
    for klass in smalluml_Methode.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml_Attribute)


def test_smalluml_attribute_constructor_exists():
    assert callable(smalluml_Attribute.__init__)


def test_smalluml_attribute_constructor_args():
    sig = inspect.signature(smalluml_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_smalluml_attribute_has_name():
    assert hasattr(smalluml_Attribute, "name")
    descriptor = None
    for klass in smalluml_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smalluml_attribute_has_type():
    assert hasattr(smalluml_Attribute, "type")
    descriptor = None
    for klass in smalluml_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_association_is_not_abstract():
    assert not inspect.isabstract(smalluml_Association)


def test_smalluml_association_constructor_exists():
    assert callable(smalluml_Association.__init__)


def test_smalluml_association_constructor_args():
    sig = inspect.signature(smalluml_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_association_has_name():
    assert hasattr(smalluml_Association, "name")
    descriptor = None
    for klass in smalluml_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_smallclass_is_not_abstract():
    assert not inspect.isabstract(smalluml_SmallClass)


def test_smalluml_smallclass_constructor_exists():
    assert callable(smalluml_SmallClass.__init__)


def test_smalluml_smallclass_constructor_args():
    sig = inspect.signature(smalluml_SmallClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_smallclass_has_name():
    assert hasattr(smalluml_SmallClass, "name")
    descriptor = None
    for klass in smalluml_SmallClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_generalisation_is_not_abstract():
    assert not inspect.isabstract(smalluml_Generalisation)


def test_smalluml_generalisation_constructor_exists():
    assert callable(smalluml_Generalisation.__init__)


def test_smalluml_generalisation_constructor_args():
    sig = inspect.signature(smalluml_Generalisation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_schemauml_is_not_abstract():
    assert not inspect.isabstract(smalluml_SchemaUML)


def test_smalluml_schemauml_constructor_exists():
    assert callable(smalluml_SchemaUML.__init__)


def test_smalluml_schemauml_constructor_args():
    sig = inspect.signature(smalluml_SchemaUML.__init__)
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
smalluml_Role_strategy = st.builds(
    smalluml_Role,
    Multiplicity=
        safe_text
)
smalluml_Methode_strategy = st.builds(
    smalluml_Methode,
    name=
        safe_text,
    returnType=
        safe_text
)
smalluml_Attribute_strategy = st.builds(
    smalluml_Attribute,
    name=
        safe_text,
    type=
        safe_text
)
smalluml_Association_strategy = st.builds(
    smalluml_Association,
    name=
        safe_text
)
smalluml_SmallClass_strategy = st.builds(
    smalluml_SmallClass,
    name=
        safe_text
)
smalluml_Generalisation_strategy = st.builds(
    smalluml_Generalisation,
)
smalluml_SchemaUML_strategy = st.builds(
    smalluml_SchemaUML,
)

@given(instance=smalluml_Role_strategy)
@settings(max_examples=50)
def test_smalluml_role_instantiation(instance):
    assert isinstance(instance, smalluml_Role)



@given(instance=smalluml_Role_strategy)
def test_smalluml_role_Multiplicity_setter(instance):
    original = instance.Multiplicity
    instance.Multiplicity = original
    assert instance.Multiplicity == original

@given(instance=smalluml_Methode_strategy)
@settings(max_examples=50)
def test_smalluml_methode_instantiation(instance):
    assert isinstance(instance, smalluml_Methode)



@given(instance=smalluml_Methode_strategy)
def test_smalluml_methode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smalluml_Methode_strategy)
def test_smalluml_methode_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=smalluml_Attribute_strategy)
@settings(max_examples=50)
def test_smalluml_attribute_instantiation(instance):
    assert isinstance(instance, smalluml_Attribute)



@given(instance=smalluml_Attribute_strategy)
def test_smalluml_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smalluml_Attribute_strategy)
def test_smalluml_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=smalluml_Association_strategy)
@settings(max_examples=50)
def test_smalluml_association_instantiation(instance):
    assert isinstance(instance, smalluml_Association)



@given(instance=smalluml_Association_strategy)
def test_smalluml_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml_SmallClass_strategy)
@settings(max_examples=50)
def test_smalluml_smallclass_instantiation(instance):
    assert isinstance(instance, smalluml_SmallClass)



@given(instance=smalluml_SmallClass_strategy)
def test_smalluml_smallclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml_Generalisation_strategy)
@settings(max_examples=50)
def test_smalluml_generalisation_instantiation(instance):
    assert isinstance(instance, smalluml_Generalisation)

@given(instance=smalluml_SchemaUML_strategy)
@settings(max_examples=50)
def test_smalluml_schemauml_instantiation(instance):
    assert isinstance(instance, smalluml_SchemaUML)
