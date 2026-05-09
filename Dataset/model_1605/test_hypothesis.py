import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinetDsl::PutStatement,
    petrinetDsl::TakeStatement,
    petrinetDsl::AssureStatement,
    petrinetDsl::Storage,
    petrinetDsl::Transaction,
    petrinetDsl::Place,
    petrinetDsl::Resource,
    petrinetDsl::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetdsl::putstatement_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl::PutStatement)


def test_petrinetdsl::putstatement_constructor_exists():
    assert callable(petrinetDsl::PutStatement.__init__)


def test_petrinetdsl::putstatement_constructor_args():
    sig = inspect.signature(petrinetDsl::PutStatement.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_petrinetdsl::putstatement_has_count():
    assert hasattr(petrinetDsl::PutStatement, "count")
    descriptor = None
    for klass in petrinetDsl::PutStatement.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl::takestatement_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl::TakeStatement)


def test_petrinetdsl::takestatement_constructor_exists():
    assert callable(petrinetDsl::TakeStatement.__init__)


def test_petrinetdsl::takestatement_constructor_args():
    sig = inspect.signature(petrinetDsl::TakeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_petrinetdsl::takestatement_has_count():
    assert hasattr(petrinetDsl::TakeStatement, "count")
    descriptor = None
    for klass in petrinetDsl::TakeStatement.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl::assurestatement_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl::AssureStatement)


def test_petrinetdsl::assurestatement_constructor_exists():
    assert callable(petrinetDsl::AssureStatement.__init__)


def test_petrinetdsl::assurestatement_constructor_args():
    sig = inspect.signature(petrinetDsl::AssureStatement.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_petrinetdsl::assurestatement_has_count():
    assert hasattr(petrinetDsl::AssureStatement, "count")
    descriptor = None
    for klass in petrinetDsl::AssureStatement.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl::storage_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl::Storage)


def test_petrinetdsl::storage_constructor_exists():
    assert callable(petrinetDsl::Storage.__init__)


def test_petrinetdsl::storage_constructor_args():
    sig = inspect.signature(petrinetDsl::Storage.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "count" in params, "Missing parameter 'count'"

def test_petrinetdsl::storage_has_capacity():
    assert hasattr(petrinetDsl::Storage, "capacity")
    descriptor = None
    for klass in petrinetDsl::Storage.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_petrinetdsl::storage_has_count():
    assert hasattr(petrinetDsl::Storage, "count")
    descriptor = None
    for klass in petrinetDsl::Storage.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl::transaction_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl::Transaction)


def test_petrinetdsl::transaction_constructor_exists():
    assert callable(petrinetDsl::Transaction.__init__)


def test_petrinetdsl::transaction_constructor_args():
    sig = inspect.signature(petrinetDsl::Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetdsl::transaction_has_name():
    assert hasattr(petrinetDsl::Transaction, "name")
    descriptor = None
    for klass in petrinetDsl::Transaction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl::place_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl::Place)


def test_petrinetdsl::place_constructor_exists():
    assert callable(petrinetDsl::Place.__init__)


def test_petrinetdsl::place_constructor_args():
    sig = inspect.signature(petrinetDsl::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetdsl::place_has_name():
    assert hasattr(petrinetDsl::Place, "name")
    descriptor = None
    for klass in petrinetDsl::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl::resource_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl::Resource)


def test_petrinetdsl::resource_constructor_exists():
    assert callable(petrinetDsl::Resource.__init__)


def test_petrinetdsl::resource_constructor_args():
    sig = inspect.signature(petrinetDsl::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetdsl::resource_has_name():
    assert hasattr(petrinetDsl::Resource, "name")
    descriptor = None
    for klass in petrinetDsl::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl::PetriNet)


def test_petrinetdsl::petrinet_constructor_exists():
    assert callable(petrinetDsl::PetriNet.__init__)


def test_petrinetdsl::petrinet_constructor_args():
    sig = inspect.signature(petrinetDsl::PetriNet.__init__)
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
petrinetDsl::PutStatement_strategy = st.builds(
    petrinetDsl::PutStatement,
    count=
        st.integers()
)
petrinetDsl::TakeStatement_strategy = st.builds(
    petrinetDsl::TakeStatement,
    count=
        st.integers()
)
petrinetDsl::AssureStatement_strategy = st.builds(
    petrinetDsl::AssureStatement,
    count=
        st.integers()
)
petrinetDsl::Storage_strategy = st.builds(
    petrinetDsl::Storage,
    capacity=
        st.integers(),
    count=
        st.integers()
)
petrinetDsl::Transaction_strategy = st.builds(
    petrinetDsl::Transaction,
    name=
        safe_text
)
petrinetDsl::Place_strategy = st.builds(
    petrinetDsl::Place,
    name=
        safe_text
)
petrinetDsl::Resource_strategy = st.builds(
    petrinetDsl::Resource,
    name=
        safe_text
)
petrinetDsl::PetriNet_strategy = st.builds(
    petrinetDsl::PetriNet,
)

@given(instance=petrinetDsl::PutStatement_strategy)
@settings(max_examples=50)
def test_petrinetdsl::putstatement_instantiation(instance):
    assert isinstance(instance, petrinetDsl::PutStatement)

@given(instance=petrinetDsl::PutStatement_strategy)
def test_petrinetdsl::putstatement_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=petrinetDsl::PutStatement_strategy)
def test_petrinetdsl::putstatement_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=petrinetDsl::TakeStatement_strategy)
@settings(max_examples=50)
def test_petrinetdsl::takestatement_instantiation(instance):
    assert isinstance(instance, petrinetDsl::TakeStatement)

@given(instance=petrinetDsl::TakeStatement_strategy)
def test_petrinetdsl::takestatement_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=petrinetDsl::TakeStatement_strategy)
def test_petrinetdsl::takestatement_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=petrinetDsl::AssureStatement_strategy)
@settings(max_examples=50)
def test_petrinetdsl::assurestatement_instantiation(instance):
    assert isinstance(instance, petrinetDsl::AssureStatement)

@given(instance=petrinetDsl::AssureStatement_strategy)
def test_petrinetdsl::assurestatement_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=petrinetDsl::AssureStatement_strategy)
def test_petrinetdsl::assurestatement_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=petrinetDsl::Storage_strategy)
@settings(max_examples=50)
def test_petrinetdsl::storage_instantiation(instance):
    assert isinstance(instance, petrinetDsl::Storage)

@given(instance=petrinetDsl::Storage_strategy)
def test_petrinetdsl::storage_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=petrinetDsl::Storage_strategy)
def test_petrinetdsl::storage_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=petrinetDsl::Storage_strategy)
def test_petrinetdsl::storage_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=petrinetDsl::Storage_strategy)
def test_petrinetdsl::storage_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=petrinetDsl::Transaction_strategy)
@settings(max_examples=50)
def test_petrinetdsl::transaction_instantiation(instance):
    assert isinstance(instance, petrinetDsl::Transaction)

@given(instance=petrinetDsl::Transaction_strategy)
def test_petrinetdsl::transaction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetDsl::Transaction_strategy)
def test_petrinetdsl::transaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetDsl::Place_strategy)
@settings(max_examples=50)
def test_petrinetdsl::place_instantiation(instance):
    assert isinstance(instance, petrinetDsl::Place)

@given(instance=petrinetDsl::Place_strategy)
def test_petrinetdsl::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetDsl::Place_strategy)
def test_petrinetdsl::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetDsl::Resource_strategy)
@settings(max_examples=50)
def test_petrinetdsl::resource_instantiation(instance):
    assert isinstance(instance, petrinetDsl::Resource)

@given(instance=petrinetDsl::Resource_strategy)
def test_petrinetdsl::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetDsl::Resource_strategy)
def test_petrinetdsl::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetDsl::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetdsl::petrinet_instantiation(instance):
    assert isinstance(instance, petrinetDsl::PetriNet)
