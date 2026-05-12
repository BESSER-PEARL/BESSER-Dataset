import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinetDsl_PutStatement,
    petrinetDsl_TakeStatement,
    petrinetDsl_AssureStatement,
    petrinetDsl_Storage,
    petrinetDsl_Transaction,
    petrinetDsl_Place,
    petrinetDsl_Resource,
    petrinetDsl_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetdsl_putstatement_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl_PutStatement)


def test_petrinetdsl_putstatement_constructor_exists():
    assert callable(petrinetDsl_PutStatement.__init__)


def test_petrinetdsl_putstatement_constructor_args():
    sig = inspect.signature(petrinetDsl_PutStatement.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_petrinetdsl_putstatement_has_count():
    assert hasattr(petrinetDsl_PutStatement, "count")
    descriptor = None
    for klass in petrinetDsl_PutStatement.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl_takestatement_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl_TakeStatement)


def test_petrinetdsl_takestatement_constructor_exists():
    assert callable(petrinetDsl_TakeStatement.__init__)


def test_petrinetdsl_takestatement_constructor_args():
    sig = inspect.signature(petrinetDsl_TakeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_petrinetdsl_takestatement_has_count():
    assert hasattr(petrinetDsl_TakeStatement, "count")
    descriptor = None
    for klass in petrinetDsl_TakeStatement.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl_assurestatement_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl_AssureStatement)


def test_petrinetdsl_assurestatement_constructor_exists():
    assert callable(petrinetDsl_AssureStatement.__init__)


def test_petrinetdsl_assurestatement_constructor_args():
    sig = inspect.signature(petrinetDsl_AssureStatement.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"

def test_petrinetdsl_assurestatement_has_count():
    assert hasattr(petrinetDsl_AssureStatement, "count")
    descriptor = None
    for klass in petrinetDsl_AssureStatement.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl_storage_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl_Storage)


def test_petrinetdsl_storage_constructor_exists():
    assert callable(petrinetDsl_Storage.__init__)


def test_petrinetdsl_storage_constructor_args():
    sig = inspect.signature(petrinetDsl_Storage.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_petrinetdsl_storage_has_count():
    assert hasattr(petrinetDsl_Storage, "count")
    descriptor = None
    for klass in petrinetDsl_Storage.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_petrinetdsl_storage_has_capacity():
    assert hasattr(petrinetDsl_Storage, "capacity")
    descriptor = None
    for klass in petrinetDsl_Storage.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl_transaction_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl_Transaction)


def test_petrinetdsl_transaction_constructor_exists():
    assert callable(petrinetDsl_Transaction.__init__)


def test_petrinetdsl_transaction_constructor_args():
    sig = inspect.signature(petrinetDsl_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetdsl_transaction_has_name():
    assert hasattr(petrinetDsl_Transaction, "name")
    descriptor = None
    for klass in petrinetDsl_Transaction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl_place_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl_Place)


def test_petrinetdsl_place_constructor_exists():
    assert callable(petrinetDsl_Place.__init__)


def test_petrinetdsl_place_constructor_args():
    sig = inspect.signature(petrinetDsl_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetdsl_place_has_name():
    assert hasattr(petrinetDsl_Place, "name")
    descriptor = None
    for klass in petrinetDsl_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl_resource_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl_Resource)


def test_petrinetdsl_resource_constructor_exists():
    assert callable(petrinetDsl_Resource.__init__)


def test_petrinetdsl_resource_constructor_args():
    sig = inspect.signature(petrinetDsl_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetdsl_resource_has_name():
    assert hasattr(petrinetDsl_Resource, "name")
    descriptor = None
    for klass in petrinetDsl_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetdsl_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinetDsl_PetriNet)


def test_petrinetdsl_petrinet_constructor_exists():
    assert callable(petrinetDsl_PetriNet.__init__)


def test_petrinetdsl_petrinet_constructor_args():
    sig = inspect.signature(petrinetDsl_PetriNet.__init__)
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
petrinetDsl_PutStatement_strategy = st.builds(
    petrinetDsl_PutStatement,
    count=
        st.integers()
)
petrinetDsl_TakeStatement_strategy = st.builds(
    petrinetDsl_TakeStatement,
    count=
        st.integers()
)
petrinetDsl_AssureStatement_strategy = st.builds(
    petrinetDsl_AssureStatement,
    count=
        st.integers()
)
petrinetDsl_Storage_strategy = st.builds(
    petrinetDsl_Storage,
    count=
        st.integers(),
    capacity=
        st.integers()
)
petrinetDsl_Transaction_strategy = st.builds(
    petrinetDsl_Transaction,
    name=
        safe_text
)
petrinetDsl_Place_strategy = st.builds(
    petrinetDsl_Place,
    name=
        safe_text
)
petrinetDsl_Resource_strategy = st.builds(
    petrinetDsl_Resource,
    name=
        safe_text
)
petrinetDsl_PetriNet_strategy = st.builds(
    petrinetDsl_PetriNet,
)

@given(instance=petrinetDsl_PutStatement_strategy)
@settings(max_examples=50)
def test_petrinetdsl_putstatement_instantiation(instance):
    assert isinstance(instance, petrinetDsl_PutStatement)



@given(instance=petrinetDsl_PutStatement_strategy)
def test_petrinetdsl_putstatement_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=petrinetDsl_TakeStatement_strategy)
@settings(max_examples=50)
def test_petrinetdsl_takestatement_instantiation(instance):
    assert isinstance(instance, petrinetDsl_TakeStatement)



@given(instance=petrinetDsl_TakeStatement_strategy)
def test_petrinetdsl_takestatement_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=petrinetDsl_AssureStatement_strategy)
@settings(max_examples=50)
def test_petrinetdsl_assurestatement_instantiation(instance):
    assert isinstance(instance, petrinetDsl_AssureStatement)



@given(instance=petrinetDsl_AssureStatement_strategy)
def test_petrinetdsl_assurestatement_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=petrinetDsl_Storage_strategy)
@settings(max_examples=50)
def test_petrinetdsl_storage_instantiation(instance):
    assert isinstance(instance, petrinetDsl_Storage)



@given(instance=petrinetDsl_Storage_strategy)
def test_petrinetdsl_storage_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=petrinetDsl_Storage_strategy)
def test_petrinetdsl_storage_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=petrinetDsl_Transaction_strategy)
@settings(max_examples=50)
def test_petrinetdsl_transaction_instantiation(instance):
    assert isinstance(instance, petrinetDsl_Transaction)



@given(instance=petrinetDsl_Transaction_strategy)
def test_petrinetdsl_transaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetDsl_Place_strategy)
@settings(max_examples=50)
def test_petrinetdsl_place_instantiation(instance):
    assert isinstance(instance, petrinetDsl_Place)



@given(instance=petrinetDsl_Place_strategy)
def test_petrinetdsl_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetDsl_Resource_strategy)
@settings(max_examples=50)
def test_petrinetdsl_resource_instantiation(instance):
    assert isinstance(instance, petrinetDsl_Resource)



@given(instance=petrinetDsl_Resource_strategy)
def test_petrinetdsl_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetDsl_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetdsl_petrinet_instantiation(instance):
    assert isinstance(instance, petrinetDsl_PetriNet)
