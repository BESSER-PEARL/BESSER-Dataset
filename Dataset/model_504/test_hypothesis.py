import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    families::NamedElement,
    families::Member,
    families::Service,
    Member,
    families::Child,
    families::Parent,
    families::Family,
    NamedElement,
    families::Neighborhood,
    families::School,
    families::City,
    families::Company,
    families::Country,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families::namedelement_is_not_abstract():
    assert not inspect.isabstract(families::NamedElement)


def test_families::namedelement_constructor_exists():
    assert callable(families::NamedElement.__init__)


def test_families::namedelement_constructor_args():
    sig = inspect.signature(families::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_families::namedelement_has_name():
    assert hasattr(families::NamedElement, "name")
    descriptor = None
    for klass in families::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_families::member_is_not_abstract():
    assert not inspect.isabstract(families::Member)


def test_families::member_constructor_exists():
    assert callable(families::Member.__init__)


def test_families::member_constructor_args():
    sig = inspect.signature(families::Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_families::member_has_firstName():
    assert hasattr(families::Member, "firstName")
    descriptor = None
    for klass in families::Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_families::service_is_not_abstract():
    assert not inspect.isabstract(families::Service)


def test_families::service_constructor_exists():
    assert callable(families::Service.__init__)


def test_families::service_constructor_args():
    sig = inspect.signature(families::Service.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_families::child_is_not_abstract():
    assert not inspect.isabstract(families::Child)


def test_families::child_constructor_exists():
    assert callable(families::Child.__init__)


def test_families::child_constructor_args():
    sig = inspect.signature(families::Child.__init__)
    params = list(sig.parameters.keys())



def test_families::parent_is_not_abstract():
    assert not inspect.isabstract(families::Parent)


def test_families::parent_constructor_exists():
    assert callable(families::Parent.__init__)


def test_families::parent_constructor_args():
    sig = inspect.signature(families::Parent.__init__)
    params = list(sig.parameters.keys())



def test_families::family_is_not_abstract():
    assert not inspect.isabstract(families::Family)


def test_families::family_constructor_exists():
    assert callable(families::Family.__init__)


def test_families::family_constructor_args():
    sig = inspect.signature(families::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families::family_has_lastName():
    assert hasattr(families::Family, "lastName")
    descriptor = None
    for klass in families::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_families::neighborhood_is_not_abstract():
    assert not inspect.isabstract(families::Neighborhood)


def test_families::neighborhood_constructor_exists():
    assert callable(families::Neighborhood.__init__)


def test_families::neighborhood_constructor_args():
    sig = inspect.signature(families::Neighborhood.__init__)
    params = list(sig.parameters.keys())



def test_families::school_is_not_abstract():
    assert not inspect.isabstract(families::School)


def test_families::school_constructor_exists():
    assert callable(families::School.__init__)


def test_families::school_constructor_args():
    sig = inspect.signature(families::School.__init__)
    params = list(sig.parameters.keys())



def test_families::city_is_not_abstract():
    assert not inspect.isabstract(families::City)


def test_families::city_constructor_exists():
    assert callable(families::City.__init__)


def test_families::city_constructor_args():
    sig = inspect.signature(families::City.__init__)
    params = list(sig.parameters.keys())



def test_families::company_is_not_abstract():
    assert not inspect.isabstract(families::Company)


def test_families::company_constructor_exists():
    assert callable(families::Company.__init__)


def test_families::company_constructor_args():
    sig = inspect.signature(families::Company.__init__)
    params = list(sig.parameters.keys())



def test_families::country_is_not_abstract():
    assert not inspect.isabstract(families::Country)


def test_families::country_constructor_exists():
    assert callable(families::Country.__init__)


def test_families::country_constructor_args():
    sig = inspect.signature(families::Country.__init__)
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
families::NamedElement_strategy = st.builds(
    families::NamedElement,
    name=
        safe_text
)
families::Member_strategy = st.builds(
    families::Member,
    firstName=
        safe_text
)
families::Service_strategy = st.builds(
    families::Service,
)
Member_strategy = st.builds(
    Member,
)
families::Child_strategy = st.builds(
    families::Child,
)
families::Parent_strategy = st.builds(
    families::Parent,
)
families::Family_strategy = st.builds(
    families::Family,
    lastName=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
families::Neighborhood_strategy = st.builds(
    families::Neighborhood,
)
families::School_strategy = st.builds(
    families::School,
)
families::City_strategy = st.builds(
    families::City,
)
families::Company_strategy = st.builds(
    families::Company,
)
families::Country_strategy = st.builds(
    families::Country,
)

@given(instance=families::NamedElement_strategy)
@settings(max_examples=50)
def test_families::namedelement_instantiation(instance):
    assert isinstance(instance, families::NamedElement)

@given(instance=families::NamedElement_strategy)
def test_families::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=families::NamedElement_strategy)
def test_families::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=families::Member_strategy)
@settings(max_examples=50)
def test_families::member_instantiation(instance):
    assert isinstance(instance, families::Member)

@given(instance=families::Member_strategy)
def test_families::member_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=families::Member_strategy)
def test_families::member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=families::Service_strategy)
@settings(max_examples=50)
def test_families::service_instantiation(instance):
    assert isinstance(instance, families::Service)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=families::Child_strategy)
@settings(max_examples=50)
def test_families::child_instantiation(instance):
    assert isinstance(instance, families::Child)

@given(instance=families::Parent_strategy)
@settings(max_examples=50)
def test_families::parent_instantiation(instance):
    assert isinstance(instance, families::Parent)

@given(instance=families::Family_strategy)
@settings(max_examples=50)
def test_families::family_instantiation(instance):
    assert isinstance(instance, families::Family)

@given(instance=families::Family_strategy)
def test_families::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=families::Family_strategy)
def test_families::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=families::Neighborhood_strategy)
@settings(max_examples=50)
def test_families::neighborhood_instantiation(instance):
    assert isinstance(instance, families::Neighborhood)

@given(instance=families::School_strategy)
@settings(max_examples=50)
def test_families::school_instantiation(instance):
    assert isinstance(instance, families::School)

@given(instance=families::City_strategy)
@settings(max_examples=50)
def test_families::city_instantiation(instance):
    assert isinstance(instance, families::City)

@given(instance=families::Company_strategy)
@settings(max_examples=50)
def test_families::company_instantiation(instance):
    assert isinstance(instance, families::Company)

@given(instance=families::Country_strategy)
@settings(max_examples=50)
def test_families::country_instantiation(instance):
    assert isinstance(instance, families::Country)
