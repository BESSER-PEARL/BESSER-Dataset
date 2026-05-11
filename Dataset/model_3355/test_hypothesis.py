import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractType,
    entityDsl::IntType,
    entityDsl::EntityReference,
    entityDsl::StringType,
    entityDsl::BooleanType,
    entityDsl::Named,
    entityDsl::AbstractType,
    Named,
    entityDsl::Entity,
    entityDsl::Attribute,
    entityDsl::Module,
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



def test_entitydsl::inttype_is_not_abstract():
    assert not inspect.isabstract(entityDsl::IntType)


def test_entitydsl::inttype_constructor_exists():
    assert callable(entityDsl::IntType.__init__)


def test_entitydsl::inttype_constructor_args():
    sig = inspect.signature(entityDsl::IntType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::entityreference_is_not_abstract():
    assert not inspect.isabstract(entityDsl::EntityReference)


def test_entitydsl::entityreference_constructor_exists():
    assert callable(entityDsl::EntityReference.__init__)


def test_entitydsl::entityreference_constructor_args():
    sig = inspect.signature(entityDsl::EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::stringtype_is_not_abstract():
    assert not inspect.isabstract(entityDsl::StringType)


def test_entitydsl::stringtype_constructor_exists():
    assert callable(entityDsl::StringType.__init__)


def test_entitydsl::stringtype_constructor_args():
    sig = inspect.signature(entityDsl::StringType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::booleantype_is_not_abstract():
    assert not inspect.isabstract(entityDsl::BooleanType)


def test_entitydsl::booleantype_constructor_exists():
    assert callable(entityDsl::BooleanType.__init__)


def test_entitydsl::booleantype_constructor_args():
    sig = inspect.signature(entityDsl::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::named_is_not_abstract():
    assert not inspect.isabstract(entityDsl::Named)


def test_entitydsl::named_constructor_exists():
    assert callable(entityDsl::Named.__init__)


def test_entitydsl::named_constructor_args():
    sig = inspect.signature(entityDsl::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entitydsl::named_has_name():
    assert hasattr(entityDsl::Named, "name")
    descriptor = None
    for klass in entityDsl::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entitydsl::abstracttype_is_not_abstract():
    assert not inspect.isabstract(entityDsl::AbstractType)


def test_entitydsl::abstracttype_constructor_exists():
    assert callable(entityDsl::AbstractType.__init__)


def test_entitydsl::abstracttype_constructor_args():
    sig = inspect.signature(entityDsl::AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::entity_is_not_abstract():
    assert not inspect.isabstract(entityDsl::Entity)


def test_entitydsl::entity_constructor_exists():
    assert callable(entityDsl::Entity.__init__)


def test_entitydsl::entity_constructor_args():
    sig = inspect.signature(entityDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::attribute_is_not_abstract():
    assert not inspect.isabstract(entityDsl::Attribute)


def test_entitydsl::attribute_constructor_exists():
    assert callable(entityDsl::Attribute.__init__)


def test_entitydsl::attribute_constructor_args():
    sig = inspect.signature(entityDsl::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_entitydsl::module_is_not_abstract():
    assert not inspect.isabstract(entityDsl::Module)


def test_entitydsl::module_constructor_exists():
    assert callable(entityDsl::Module.__init__)


def test_entitydsl::module_constructor_args():
    sig = inspect.signature(entityDsl::Module.__init__)
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
entityDsl::IntType_strategy = st.builds(
    entityDsl::IntType,
)
entityDsl::EntityReference_strategy = st.builds(
    entityDsl::EntityReference,
)
entityDsl::StringType_strategy = st.builds(
    entityDsl::StringType,
)
entityDsl::BooleanType_strategy = st.builds(
    entityDsl::BooleanType,
)
entityDsl::Named_strategy = st.builds(
    entityDsl::Named,
    name=
        safe_text
)
entityDsl::AbstractType_strategy = st.builds(
    entityDsl::AbstractType,
)
Named_strategy = st.builds(
    Named,
)
entityDsl::Entity_strategy = st.builds(
    entityDsl::Entity,
)
entityDsl::Attribute_strategy = st.builds(
    entityDsl::Attribute,
)
entityDsl::Module_strategy = st.builds(
    entityDsl::Module,
)

@given(instance=AbstractType_strategy)
@settings(max_examples=50)
def test_abstracttype_instantiation(instance):
    assert isinstance(instance, AbstractType)

@given(instance=entityDsl::IntType_strategy)
@settings(max_examples=50)
def test_entitydsl::inttype_instantiation(instance):
    assert isinstance(instance, entityDsl::IntType)

@given(instance=entityDsl::EntityReference_strategy)
@settings(max_examples=50)
def test_entitydsl::entityreference_instantiation(instance):
    assert isinstance(instance, entityDsl::EntityReference)

@given(instance=entityDsl::StringType_strategy)
@settings(max_examples=50)
def test_entitydsl::stringtype_instantiation(instance):
    assert isinstance(instance, entityDsl::StringType)

@given(instance=entityDsl::BooleanType_strategy)
@settings(max_examples=50)
def test_entitydsl::booleantype_instantiation(instance):
    assert isinstance(instance, entityDsl::BooleanType)

@given(instance=entityDsl::Named_strategy)
@settings(max_examples=50)
def test_entitydsl::named_instantiation(instance):
    assert isinstance(instance, entityDsl::Named)

@given(instance=entityDsl::Named_strategy)
def test_entitydsl::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entityDsl::Named_strategy)
def test_entitydsl::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entityDsl::AbstractType_strategy)
@settings(max_examples=50)
def test_entitydsl::abstracttype_instantiation(instance):
    assert isinstance(instance, entityDsl::AbstractType)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=entityDsl::Entity_strategy)
@settings(max_examples=50)
def test_entitydsl::entity_instantiation(instance):
    assert isinstance(instance, entityDsl::Entity)

@given(instance=entityDsl::Attribute_strategy)
@settings(max_examples=50)
def test_entitydsl::attribute_instantiation(instance):
    assert isinstance(instance, entityDsl::Attribute)

@given(instance=entityDsl::Module_strategy)
@settings(max_examples=50)
def test_entitydsl::module_instantiation(instance):
    assert isinstance(instance, entityDsl::Module)
