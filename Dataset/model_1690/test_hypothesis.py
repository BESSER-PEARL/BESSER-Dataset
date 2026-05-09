import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloworld150::Profession,
    helloworld150::World,
    helloworld150::Comment,
    helloworld150::NamedElement,
    NamedElement,
    helloworld150::Own,
    helloworld150::Person,
    helloworld150::Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld150::profession_is_not_abstract():
    assert not inspect.isabstract(helloworld150::Profession)


def test_helloworld150::profession_constructor_exists():
    assert callable(helloworld150::Profession.__init__)


def test_helloworld150::profession_constructor_args():
    sig = inspect.signature(helloworld150::Profession.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld150::profession_has_name():
    assert hasattr(helloworld150::Profession, "name")
    descriptor = None
    for klass in helloworld150::Profession.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworld150::world_is_not_abstract():
    assert not inspect.isabstract(helloworld150::World)


def test_helloworld150::world_constructor_exists():
    assert callable(helloworld150::World.__init__)


def test_helloworld150::world_constructor_args():
    sig = inspect.signature(helloworld150::World.__init__)
    params = list(sig.parameters.keys())



def test_helloworld150::comment_is_not_abstract():
    assert not inspect.isabstract(helloworld150::Comment)


def test_helloworld150::comment_constructor_exists():
    assert callable(helloworld150::Comment.__init__)


def test_helloworld150::comment_constructor_args():
    sig = inspect.signature(helloworld150::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_helloworld150::comment_has_content():
    assert hasattr(helloworld150::Comment, "content")
    descriptor = None
    for klass in helloworld150::Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_helloworld150::namedelement_is_not_abstract():
    assert not inspect.isabstract(helloworld150::NamedElement)


def test_helloworld150::namedelement_constructor_exists():
    assert callable(helloworld150::NamedElement.__init__)


def test_helloworld150::namedelement_constructor_args():
    sig = inspect.signature(helloworld150::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld150::namedelement_has_name():
    assert hasattr(helloworld150::NamedElement, "name")
    descriptor = None
    for klass in helloworld150::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_helloworld150::own_is_not_abstract():
    assert not inspect.isabstract(helloworld150::Own)


def test_helloworld150::own_constructor_exists():
    assert callable(helloworld150::Own.__init__)


def test_helloworld150::own_constructor_args():
    sig = inspect.signature(helloworld150::Own.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"
    assert "ownerName" in params, "Missing parameter 'ownerName'"

def test_helloworld150::own_has_since():
    assert hasattr(helloworld150::Own, "since")
    descriptor = None
    for klass in helloworld150::Own.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)

def test_helloworld150::own_has_ownerName():
    assert hasattr(helloworld150::Own, "ownerName")
    descriptor = None
    for klass in helloworld150::Own.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
            break
    assert isinstance(descriptor, property)



def test_helloworld150::person_is_not_abstract():
    assert not inspect.isabstract(helloworld150::Person)


def test_helloworld150::person_constructor_exists():
    assert callable(helloworld150::Person.__init__)


def test_helloworld150::person_constructor_args():
    sig = inspect.signature(helloworld150::Person.__init__)
    params = list(sig.parameters.keys())
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "forName" in params, "Missing parameter 'forName'"

def test_helloworld150::person_has_birthDate():
    assert hasattr(helloworld150::Person, "birthDate")
    descriptor = None
    for klass in helloworld150::Person.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_helloworld150::person_has_forName():
    assert hasattr(helloworld150::Person, "forName")
    descriptor = None
    for klass in helloworld150::Person.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)



def test_helloworld150::thing_is_not_abstract():
    assert not inspect.isabstract(helloworld150::Thing)


def test_helloworld150::thing_constructor_exists():
    assert callable(helloworld150::Thing.__init__)


def test_helloworld150::thing_constructor_args():
    sig = inspect.signature(helloworld150::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_helloworld150::thing_has_id():
    assert hasattr(helloworld150::Thing, "id")
    descriptor = None
    for klass in helloworld150::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
helloworld150::Profession_strategy = st.builds(
    helloworld150::Profession,
    name=
        safe_text
)
helloworld150::World_strategy = st.builds(
    helloworld150::World,
)
helloworld150::Comment_strategy = st.builds(
    helloworld150::Comment,
    content=
        safe_text
)
helloworld150::NamedElement_strategy = st.builds(
    helloworld150::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
helloworld150::Own_strategy = st.builds(
    helloworld150::Own,
    since=
        safe_text,
    ownerName=
        safe_text
)
helloworld150::Person_strategy = st.builds(
    helloworld150::Person,
    birthDate=
        safe_text,
    forName=
        safe_text
)
helloworld150::Thing_strategy = st.builds(
    helloworld150::Thing,
    id=
        st.integers()
)

@given(instance=helloworld150::Profession_strategy)
@settings(max_examples=50)
def test_helloworld150::profession_instantiation(instance):
    assert isinstance(instance, helloworld150::Profession)

@given(instance=helloworld150::Profession_strategy)
def test_helloworld150::profession_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloworld150::Profession_strategy)
def test_helloworld150::profession_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloworld150::World_strategy)
@settings(max_examples=50)
def test_helloworld150::world_instantiation(instance):
    assert isinstance(instance, helloworld150::World)

@given(instance=helloworld150::Comment_strategy)
@settings(max_examples=50)
def test_helloworld150::comment_instantiation(instance):
    assert isinstance(instance, helloworld150::Comment)

@given(instance=helloworld150::Comment_strategy)
def test_helloworld150::comment_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=helloworld150::Comment_strategy)
def test_helloworld150::comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=helloworld150::NamedElement_strategy)
@settings(max_examples=50)
def test_helloworld150::namedelement_instantiation(instance):
    assert isinstance(instance, helloworld150::NamedElement)

@given(instance=helloworld150::NamedElement_strategy)
def test_helloworld150::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloworld150::NamedElement_strategy)
def test_helloworld150::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=helloworld150::Own_strategy)
@settings(max_examples=50)
def test_helloworld150::own_instantiation(instance):
    assert isinstance(instance, helloworld150::Own)

@given(instance=helloworld150::Own_strategy)
def test_helloworld150::own_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=helloworld150::Own_strategy)
def test_helloworld150::own_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=helloworld150::Own_strategy)
def test_helloworld150::own_ownerName_type(instance):
    assert isinstance(instance.ownerName, str)


@given(instance=helloworld150::Own_strategy)
def test_helloworld150::own_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original

@given(instance=helloworld150::Person_strategy)
@settings(max_examples=50)
def test_helloworld150::person_instantiation(instance):
    assert isinstance(instance, helloworld150::Person)

@given(instance=helloworld150::Person_strategy)
def test_helloworld150::person_birthDate_type(instance):
    assert isinstance(instance.birthDate, str)


@given(instance=helloworld150::Person_strategy)
def test_helloworld150::person_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original

@given(instance=helloworld150::Person_strategy)
def test_helloworld150::person_forName_type(instance):
    assert isinstance(instance.forName, str)


@given(instance=helloworld150::Person_strategy)
def test_helloworld150::person_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original

@given(instance=helloworld150::Thing_strategy)
@settings(max_examples=50)
def test_helloworld150::thing_instantiation(instance):
    assert isinstance(instance, helloworld150::Thing)

@given(instance=helloworld150::Thing_strategy)
def test_helloworld150::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=helloworld150::Thing_strategy)
def test_helloworld150::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
