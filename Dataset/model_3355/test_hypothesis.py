import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractType,
    entityDsl_IntType,
    entityDsl_EntityReference,
    entityDsl_StringType,
    entityDsl_BooleanType,
    entityDsl_Named,
    entityDsl_AbstractType,
    Named,
    entityDsl_Attribute,
    entityDsl_Entity,
    entityDsl_Module,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstracttype_is_not_abstract():
    assert not inspect.isabstract(AbstractType)


def test_abstracttype_constructor_exists():
    assert callable(AbstractType.__init__)


def test_abstracttype_constructor_args():
    sig = inspect.signature(AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_inttype_is_not_abstract():
    assert not inspect.isabstract(entityDsl_IntType)


def test_entitydsl_inttype_constructor_exists():
    assert callable(entityDsl_IntType.__init__)


def test_entitydsl_inttype_constructor_args():
    sig = inspect.signature(entityDsl_IntType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_entityreference_is_not_abstract():
    assert not inspect.isabstract(entityDsl_EntityReference)


def test_entitydsl_entityreference_constructor_exists():
    assert callable(entityDsl_EntityReference.__init__)


def test_entitydsl_entityreference_constructor_args():
    sig = inspect.signature(entityDsl_EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_stringtype_is_not_abstract():
    assert not inspect.isabstract(entityDsl_StringType)


def test_entitydsl_stringtype_constructor_exists():
    assert callable(entityDsl_StringType.__init__)


def test_entitydsl_stringtype_constructor_args():
    sig = inspect.signature(entityDsl_StringType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_booleantype_is_not_abstract():
    assert not inspect.isabstract(entityDsl_BooleanType)


def test_entitydsl_booleantype_constructor_exists():
    assert callable(entityDsl_BooleanType.__init__)


def test_entitydsl_booleantype_constructor_args():
    sig = inspect.signature(entityDsl_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_named_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Named)


def test_entitydsl_named_constructor_exists():
    assert callable(entityDsl_Named.__init__)


def test_entitydsl_named_constructor_args():
    sig = inspect.signature(entityDsl_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitydsl_named_has_name():
    assert hasattr(entityDsl_Named, "name")
    descriptor = None
    for klass in entityDsl_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitydsl_abstracttype_is_not_abstract():
    assert not inspect.isabstract(entityDsl_AbstractType)


def test_entitydsl_abstracttype_constructor_exists():
    assert callable(entityDsl_AbstractType.__init__)


def test_entitydsl_abstracttype_constructor_args():
    sig = inspect.signature(entityDsl_AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_attribute_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Attribute)


def test_entitydsl_attribute_constructor_exists():
    assert callable(entityDsl_Attribute.__init__)


def test_entitydsl_attribute_constructor_args():
    sig = inspect.signature(entityDsl_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_entity_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Entity)


def test_entitydsl_entity_constructor_exists():
    assert callable(entityDsl_Entity.__init__)


def test_entitydsl_entity_constructor_args():
    sig = inspect.signature(entityDsl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl_module_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Module)


def test_entitydsl_module_constructor_exists():
    assert callable(entityDsl_Module.__init__)


def test_entitydsl_module_constructor_args():
    sig = inspect.signature(entityDsl_Module.__init__)
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
AbstractType_strategy = st.builds(
    AbstractType,
)
entityDsl_IntType_strategy = st.builds(
    entityDsl_IntType,
)
entityDsl_EntityReference_strategy = st.builds(
    entityDsl_EntityReference,
)
entityDsl_StringType_strategy = st.builds(
    entityDsl_StringType,
)
entityDsl_BooleanType_strategy = st.builds(
    entityDsl_BooleanType,
)
entityDsl_Named_strategy = st.builds(
    entityDsl_Named,
    name=
        safe_text
)
entityDsl_AbstractType_strategy = st.builds(
    entityDsl_AbstractType,
)
Named_strategy = st.builds(
    Named,
)
entityDsl_Attribute_strategy = st.builds(
    entityDsl_Attribute,
)
entityDsl_Entity_strategy = st.builds(
    entityDsl_Entity,
)
entityDsl_Module_strategy = st.builds(
    entityDsl_Module,
)

@given(instance=AbstractType_strategy)
@settings(max_examples=50)
def test_abstracttype_instantiation(instance):
    assert isinstance(instance, AbstractType)

@given(instance=entityDsl_IntType_strategy)
@settings(max_examples=50)
def test_entitydsl_inttype_instantiation(instance):
    assert isinstance(instance, entityDsl_IntType)

@given(instance=entityDsl_EntityReference_strategy)
@settings(max_examples=50)
def test_entitydsl_entityreference_instantiation(instance):
    assert isinstance(instance, entityDsl_EntityReference)

@given(instance=entityDsl_StringType_strategy)
@settings(max_examples=50)
def test_entitydsl_stringtype_instantiation(instance):
    assert isinstance(instance, entityDsl_StringType)

@given(instance=entityDsl_BooleanType_strategy)
@settings(max_examples=50)
def test_entitydsl_booleantype_instantiation(instance):
    assert isinstance(instance, entityDsl_BooleanType)

@given(instance=entityDsl_Named_strategy)
@settings(max_examples=50)
def test_entitydsl_named_instantiation(instance):
    assert isinstance(instance, entityDsl_Named)



@given(instance=entityDsl_Named_strategy)
def test_entitydsl_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entityDsl_AbstractType_strategy)
@settings(max_examples=50)
def test_entitydsl_abstracttype_instantiation(instance):
    assert isinstance(instance, entityDsl_AbstractType)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=entityDsl_Attribute_strategy)
@settings(max_examples=50)
def test_entitydsl_attribute_instantiation(instance):
    assert isinstance(instance, entityDsl_Attribute)

@given(instance=entityDsl_Entity_strategy)
@settings(max_examples=50)
def test_entitydsl_entity_instantiation(instance):
    assert isinstance(instance, entityDsl_Entity)

@given(instance=entityDsl_Module_strategy)
@settings(max_examples=50)
def test_entitydsl_module_instantiation(instance):
    assert isinstance(instance, entityDsl_Module)
