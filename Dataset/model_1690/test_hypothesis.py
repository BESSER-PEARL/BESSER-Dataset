import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloworld150_Profession,
    helloworld150_World,
    helloworld150_Comment,
    helloworld150_NamedElement,
    NamedElement,
    helloworld150_Thing,
    helloworld150_Own,
    helloworld150_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld150_profession_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Profession)


def test_helloworld150_profession_constructor_exists():
    assert callable(helloworld150_Profession.__init__)


def test_helloworld150_profession_constructor_args():
    sig = inspect.signature(helloworld150_Profession.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld150_profession_has_name():
    assert hasattr(helloworld150_Profession, "name")
    descriptor = None
    for klass in helloworld150_Profession.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworld150_world_is_not_abstract():
    assert not inspect.isabstract(helloworld150_World)


def test_helloworld150_world_constructor_exists():
    assert callable(helloworld150_World.__init__)


def test_helloworld150_world_constructor_args():
    sig = inspect.signature(helloworld150_World.__init__)
    params = list(sig.parameters.keys())



def test_helloworld150_comment_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Comment)


def test_helloworld150_comment_constructor_exists():
    assert callable(helloworld150_Comment.__init__)


def test_helloworld150_comment_constructor_args():
    sig = inspect.signature(helloworld150_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_helloworld150_comment_has_content():
    assert hasattr(helloworld150_Comment, "content")
    descriptor = None
    for klass in helloworld150_Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_helloworld150_namedelement_is_not_abstract():
    assert not inspect.isabstract(helloworld150_NamedElement)


def test_helloworld150_namedelement_constructor_exists():
    assert callable(helloworld150_NamedElement.__init__)


def test_helloworld150_namedelement_constructor_args():
    sig = inspect.signature(helloworld150_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld150_namedelement_has_name():
    assert hasattr(helloworld150_NamedElement, "name")
    descriptor = None
    for klass in helloworld150_NamedElement.__mro__:
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



def test_helloworld150_thing_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Thing)


def test_helloworld150_thing_constructor_exists():
    assert callable(helloworld150_Thing.__init__)


def test_helloworld150_thing_constructor_args():
    sig = inspect.signature(helloworld150_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_helloworld150_thing_has_id():
    assert hasattr(helloworld150_Thing, "id")
    descriptor = None
    for klass in helloworld150_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_helloworld150_own_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Own)


def test_helloworld150_own_constructor_exists():
    assert callable(helloworld150_Own.__init__)


def test_helloworld150_own_constructor_args():
    sig = inspect.signature(helloworld150_Own.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"
    assert "ownerName" in params, "Missing parameter 'ownerName'"

def test_helloworld150_own_has_since():
    assert hasattr(helloworld150_Own, "since")
    descriptor = None
    for klass in helloworld150_Own.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)

def test_helloworld150_own_has_ownerName():
    assert hasattr(helloworld150_Own, "ownerName")
    descriptor = None
    for klass in helloworld150_Own.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
            break
    assert isinstance(descriptor, property)



def test_helloworld150_person_is_not_abstract():
    assert not inspect.isabstract(helloworld150_Person)


def test_helloworld150_person_constructor_exists():
    assert callable(helloworld150_Person.__init__)


def test_helloworld150_person_constructor_args():
    sig = inspect.signature(helloworld150_Person.__init__)
    params = list(sig.parameters.keys())
    assert "forName" in params, "Missing parameter 'forName'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"

def test_helloworld150_person_has_forName():
    assert hasattr(helloworld150_Person, "forName")
    descriptor = None
    for klass in helloworld150_Person.__mro__:
        if "forName" in klass.__dict__:
            descriptor = klass.__dict__["forName"]
            break
    assert isinstance(descriptor, property)

def test_helloworld150_person_has_birthDate():
    assert hasattr(helloworld150_Person, "birthDate")
    descriptor = None
    for klass in helloworld150_Person.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
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
helloworld150_Profession_strategy = st.builds(
    helloworld150_Profession,
    name=
        safe_text
)
helloworld150_World_strategy = st.builds(
    helloworld150_World,
)
helloworld150_Comment_strategy = st.builds(
    helloworld150_Comment,
    content=
        safe_text
)
helloworld150_NamedElement_strategy = st.builds(
    helloworld150_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
helloworld150_Thing_strategy = st.builds(
    helloworld150_Thing,
    id=
        st.integers()
)
helloworld150_Own_strategy = st.builds(
    helloworld150_Own,
    since=
        safe_text,
    ownerName=
        safe_text
)
helloworld150_Person_strategy = st.builds(
    helloworld150_Person,
    forName=
        safe_text,
    birthDate=
        safe_text
)

@given(instance=helloworld150_Profession_strategy)
@settings(max_examples=50)
def test_helloworld150_profession_instantiation(instance):
    assert isinstance(instance, helloworld150_Profession)



@given(instance=helloworld150_Profession_strategy)
def test_helloworld150_profession_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloworld150_World_strategy)
@settings(max_examples=50)
def test_helloworld150_world_instantiation(instance):
    assert isinstance(instance, helloworld150_World)

@given(instance=helloworld150_Comment_strategy)
@settings(max_examples=50)
def test_helloworld150_comment_instantiation(instance):
    assert isinstance(instance, helloworld150_Comment)



@given(instance=helloworld150_Comment_strategy)
def test_helloworld150_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=helloworld150_NamedElement_strategy)
@settings(max_examples=50)
def test_helloworld150_namedelement_instantiation(instance):
    assert isinstance(instance, helloworld150_NamedElement)



@given(instance=helloworld150_NamedElement_strategy)
def test_helloworld150_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=helloworld150_Thing_strategy)
@settings(max_examples=50)
def test_helloworld150_thing_instantiation(instance):
    assert isinstance(instance, helloworld150_Thing)



@given(instance=helloworld150_Thing_strategy)
def test_helloworld150_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=helloworld150_Own_strategy)
@settings(max_examples=50)
def test_helloworld150_own_instantiation(instance):
    assert isinstance(instance, helloworld150_Own)



@given(instance=helloworld150_Own_strategy)
def test_helloworld150_own_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original



@given(instance=helloworld150_Own_strategy)
def test_helloworld150_own_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original

@given(instance=helloworld150_Person_strategy)
@settings(max_examples=50)
def test_helloworld150_person_instantiation(instance):
    assert isinstance(instance, helloworld150_Person)



@given(instance=helloworld150_Person_strategy)
def test_helloworld150_person_forName_setter(instance):
    original = instance.forName
    instance.forName = original
    assert instance.forName == original



@given(instance=helloworld150_Person_strategy)
def test_helloworld150_person_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original
