import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Person,
    family::Woman,
    family::Man,
    family::Person,
    family::Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_family::woman_is_not_abstract():
    assert not inspect.isabstract(family::Woman)


def test_family::woman_constructor_exists():
    assert callable(family::Woman.__init__)


def test_family::woman_constructor_args():
    sig = inspect.signature(family::Woman.__init__)
    params = list(sig.parameters.keys())



def test_family::man_is_not_abstract():
    assert not inspect.isabstract(family::Man)


def test_family::man_constructor_exists():
    assert callable(family::Man.__init__)


def test_family::man_constructor_args():
    sig = inspect.signature(family::Man.__init__)
    params = list(sig.parameters.keys())



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "fechaNacimiento" in params, "Missing parameter 'fechaNacimiento'"
    assert "provincia" in params, "Missing parameter 'provincia'"
    assert "name" in params, "Missing parameter 'name'"
    assert "eCivil" in params, "Missing parameter 'eCivil'"

def test_family::person_has_fechaNacimiento():
    assert hasattr(family::Person, "fechaNacimiento")
    descriptor = None
    for klass in family::Person.__mro__:
        if "fechaNacimiento" in klass.__dict__:
            descriptor = klass.__dict__["fechaNacimiento"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_provincia():
    assert hasattr(family::Person, "provincia")
    descriptor = None
    for klass in family::Person.__mro__:
        if "provincia" in klass.__dict__:
            descriptor = klass.__dict__["provincia"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_name():
    assert hasattr(family::Person, "name")
    descriptor = None
    for klass in family::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_eCivil():
    assert hasattr(family::Person, "eCivil")
    descriptor = None
    for klass in family::Person.__mro__:
        if "eCivil" in klass.__dict__:
            descriptor = klass.__dict__["eCivil"]
            break
    assert isinstance(descriptor, property)



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::family_has_name():
    assert hasattr(family::Family, "name")
    descriptor = None
    for klass in family::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
Person_strategy = st.builds(
    Person,
)
family::Woman_strategy = st.builds(
    family::Woman,
)
family::Man_strategy = st.builds(
    family::Man,
)
family::Person_strategy = st.builds(
    family::Person,
    fechaNacimiento=
        safe_text,
    provincia=
        safe_text,
    name=
        safe_text,
    eCivil=
        safe_text
)
family::Family_strategy = st.builds(
    family::Family,
    name=
        safe_text
)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=family::Woman_strategy)
@settings(max_examples=50)
def test_family::woman_instantiation(instance):
    assert isinstance(instance, family::Woman)

@given(instance=family::Man_strategy)
@settings(max_examples=50)
def test_family::man_instantiation(instance):
    assert isinstance(instance, family::Man)

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_fechaNacimiento_type(instance):
    assert isinstance(instance.fechaNacimiento, str)


@given(instance=family::Person_strategy)
def test_family::person_fechaNacimiento_setter(instance):
    original = instance.fechaNacimiento
    instance.fechaNacimiento = original
    assert instance.fechaNacimiento == original

@given(instance=family::Person_strategy)
def test_family::person_provincia_type(instance):
    assert isinstance(instance.provincia, str)


@given(instance=family::Person_strategy)
def test_family::person_provincia_setter(instance):
    original = instance.provincia
    instance.provincia = original
    assert instance.provincia == original

@given(instance=family::Person_strategy)
def test_family::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Person_strategy)
def test_family::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::Person_strategy)
def test_family::person_eCivil_type(instance):
    assert isinstance(instance.eCivil, str)


@given(instance=family::Person_strategy)
def test_family::person_eCivil_setter(instance):
    original = instance.eCivil
    instance.eCivil = original
    assert instance.eCivil == original

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Family_strategy)
def test_family::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Family_strategy)
def test_family::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
