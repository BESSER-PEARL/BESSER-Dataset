import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    entity_NamedElement,
    Member,
    entity_Method,
    entity_Field,
    Type,
    entity_Service,
    entity_Entity,
    NamedElement,
    entity_Member,
    entity_Type,
    entity_Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity_namedelement_is_not_abstract():
    assert not inspect.isabstract(entity_NamedElement)


def test_entity_namedelement_constructor_exists():
    assert callable(entity_NamedElement.__init__)


def test_entity_namedelement_constructor_args():
    sig = inspect.signature(entity_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity_namedelement_has_name():
    assert hasattr(entity_NamedElement, "name")
    descriptor = None
    for klass in entity_NamedElement.__mro__:
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



def test_entity_method_is_not_abstract():
    assert not inspect.isabstract(entity_Method)


def test_entity_method_constructor_exists():
    assert callable(entity_Method.__init__)


def test_entity_method_constructor_args():
    sig = inspect.signature(entity_Method.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_entity_method_has_isAbstract():
    assert hasattr(entity_Method, "isAbstract")
    descriptor = None
    for klass in entity_Method.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_entity_field_is_not_abstract():
    assert not inspect.isabstract(entity_Field)


def test_entity_field_constructor_exists():
    assert callable(entity_Field.__init__)


def test_entity_field_constructor_args():
    sig = inspect.signature(entity_Field.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_entity_service_is_not_abstract():
    assert not inspect.isabstract(entity_Service)


def test_entity_service_constructor_exists():
    assert callable(entity_Service.__init__)


def test_entity_service_constructor_args():
    sig = inspect.signature(entity_Service.__init__)
    params = list(sig.parameters.keys())



def test_entity_entity_is_not_abstract():
    assert not inspect.isabstract(entity_Entity)


def test_entity_entity_constructor_exists():
    assert callable(entity_Entity.__init__)


def test_entity_entity_constructor_args():
    sig = inspect.signature(entity_Entity.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_entity_member_is_not_abstract():
    assert not inspect.isabstract(entity_Member)


def test_entity_member_constructor_exists():
    assert callable(entity_Member.__init__)


def test_entity_member_constructor_args():
    sig = inspect.signature(entity_Member.__init__)
    params = list(sig.parameters.keys())



def test_entity_type_is_not_abstract():
    assert not inspect.isabstract(entity_Type)


def test_entity_type_constructor_exists():
    assert callable(entity_Type.__init__)


def test_entity_type_constructor_args():
    sig = inspect.signature(entity_Type.__init__)
    params = list(sig.parameters.keys())



def test_entity_package_is_not_abstract():
    assert not inspect.isabstract(entity_Package)


def test_entity_package_constructor_exists():
    assert callable(entity_Package.__init__)


def test_entity_package_constructor_args():
    sig = inspect.signature(entity_Package.__init__)
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
entity_NamedElement_strategy = st.builds(
    entity_NamedElement,
    name=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
entity_Method_strategy = st.builds(
    entity_Method,
    isAbstract=
        st.booleans()
)
entity_Field_strategy = st.builds(
    entity_Field,
)
Type_strategy = st.builds(
    Type,
)
entity_Service_strategy = st.builds(
    entity_Service,
)
entity_Entity_strategy = st.builds(
    entity_Entity,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
entity_Member_strategy = st.builds(
    entity_Member,
)
entity_Type_strategy = st.builds(
    entity_Type,
)
entity_Package_strategy = st.builds(
    entity_Package,
)

@given(instance=entity_NamedElement_strategy)
@settings(max_examples=50)
def test_entity_namedelement_instantiation(instance):
    assert isinstance(instance, entity_NamedElement)



@given(instance=entity_NamedElement_strategy)
def test_entity_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=entity_Method_strategy)
@settings(max_examples=50)
def test_entity_method_instantiation(instance):
    assert isinstance(instance, entity_Method)



@given(instance=entity_Method_strategy)
def test_entity_method_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=entity_Field_strategy)
@settings(max_examples=50)
def test_entity_field_instantiation(instance):
    assert isinstance(instance, entity_Field)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entity_Service_strategy)
@settings(max_examples=50)
def test_entity_service_instantiation(instance):
    assert isinstance(instance, entity_Service)

@given(instance=entity_Entity_strategy)
@settings(max_examples=50)
def test_entity_entity_instantiation(instance):
    assert isinstance(instance, entity_Entity)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=entity_Member_strategy)
@settings(max_examples=50)
def test_entity_member_instantiation(instance):
    assert isinstance(instance, entity_Member)

@given(instance=entity_Type_strategy)
@settings(max_examples=50)
def test_entity_type_instantiation(instance):
    assert isinstance(instance, entity_Type)

@given(instance=entity_Package_strategy)
@settings(max_examples=50)
def test_entity_package_instantiation(instance):
    assert isinstance(instance, entity_Package)
