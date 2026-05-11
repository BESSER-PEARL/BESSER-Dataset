import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    entity::NamedElement,
    Member,
    entity::Method,
    entity::Field,
    Type,
    entity::Service,
    entity::Entity,
    NamedElement,
    entity::Member,
    entity::Type,
    entity::Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity::namedelement_is_not_abstract():
    assert not inspect.isabstract(entity::NamedElement)


def test_entity::namedelement_constructor_exists():
    assert callable(entity::NamedElement.__init__)


def test_entity::namedelement_constructor_args():
    sig = inspect.signature(entity::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity::namedelement_has_name():
    assert hasattr(entity::NamedElement, "name")
    descriptor = None
    for klass in entity::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_entity::method_is_not_abstract():
    assert not inspect.isabstract(entity::Method)


def test_entity::method_constructor_exists():
    assert callable(entity::Method.__init__)


def test_entity::method_constructor_args():
    sig = inspect.signature(entity::Method.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_entity::method_has_isAbstract():
    assert hasattr(entity::Method, "isAbstract")
    descriptor = None
    for klass in entity::Method.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_entity::field_is_not_abstract():
    assert not inspect.isabstract(entity::Field)


def test_entity::field_constructor_exists():
    assert callable(entity::Field.__init__)


def test_entity::field_constructor_args():
    sig = inspect.signature(entity::Field.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entity::service_is_not_abstract():
    assert not inspect.isabstract(entity::Service)


def test_entity::service_constructor_exists():
    assert callable(entity::Service.__init__)


def test_entity::service_constructor_args():
    sig = inspect.signature(entity::Service.__init__)
    params = list(sig.parameters.keys())



def test_entity::entity_is_not_abstract():
    assert not inspect.isabstract(entity::Entity)


def test_entity::entity_constructor_exists():
    assert callable(entity::Entity.__init__)


def test_entity::entity_constructor_args():
    sig = inspect.signature(entity::Entity.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_entity::member_is_not_abstract():
    assert not inspect.isabstract(entity::Member)


def test_entity::member_constructor_exists():
    assert callable(entity::Member.__init__)


def test_entity::member_constructor_args():
    sig = inspect.signature(entity::Member.__init__)
    params = list(sig.parameters.keys())



def test_entity::type_is_not_abstract():
    assert not inspect.isabstract(entity::Type)


def test_entity::type_constructor_exists():
    assert callable(entity::Type.__init__)


def test_entity::type_constructor_args():
    sig = inspect.signature(entity::Type.__init__)
    params = list(sig.parameters.keys())



def test_entity::package_is_not_abstract():
    assert not inspect.isabstract(entity::Package)


def test_entity::package_constructor_exists():
    assert callable(entity::Package.__init__)


def test_entity::package_constructor_args():
    sig = inspect.signature(entity::Package.__init__)
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
entity::NamedElement_strategy = st.builds(
    entity::NamedElement,
    name=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
entity::Method_strategy = st.builds(
    entity::Method,
    isAbstract=
        st.booleans()
)
entity::Field_strategy = st.builds(
    entity::Field,
)
Type_strategy = st.builds(
    Type,
)
entity::Service_strategy = st.builds(
    entity::Service,
)
entity::Entity_strategy = st.builds(
    entity::Entity,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
entity::Member_strategy = st.builds(
    entity::Member,
)
entity::Type_strategy = st.builds(
    entity::Type,
)
entity::Package_strategy = st.builds(
    entity::Package,
)

@given(instance=entity::NamedElement_strategy)
@settings(max_examples=50)
def test_entity::namedelement_instantiation(instance):
    assert isinstance(instance, entity::NamedElement)

@given(instance=entity::NamedElement_strategy)
def test_entity::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=entity::NamedElement_strategy)
def test_entity::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=entity::Method_strategy)
@settings(max_examples=50)
def test_entity::method_instantiation(instance):
    assert isinstance(instance, entity::Method)

@given(instance=entity::Method_strategy)
def test_entity::method_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=entity::Method_strategy)
def test_entity::method_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=entity::Field_strategy)
@settings(max_examples=50)
def test_entity::field_instantiation(instance):
    assert isinstance(instance, entity::Field)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entity::Service_strategy)
@settings(max_examples=50)
def test_entity::service_instantiation(instance):
    assert isinstance(instance, entity::Service)

@given(instance=entity::Entity_strategy)
@settings(max_examples=50)
def test_entity::entity_instantiation(instance):
    assert isinstance(instance, entity::Entity)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=entity::Member_strategy)
@settings(max_examples=50)
def test_entity::member_instantiation(instance):
    assert isinstance(instance, entity::Member)

@given(instance=entity::Type_strategy)
@settings(max_examples=50)
def test_entity::type_instantiation(instance):
    assert isinstance(instance, entity::Type)

@given(instance=entity::Package_strategy)
@settings(max_examples=50)
def test_entity::package_instantiation(instance):
    assert isinstance(instance, entity::Package)
