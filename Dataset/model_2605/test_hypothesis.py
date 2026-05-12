import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    project_CommitterShip,
    project_Person,
    project_Project,
    project_Foundation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_project_committership_is_not_abstract():
    assert not inspect.isabstract(project_CommitterShip)


def test_project_committership_constructor_exists():
    assert callable(project_CommitterShip.__init__)


def test_project_committership_constructor_args():
    sig = inspect.signature(project_CommitterShip.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_project_committership_has_start():
    assert hasattr(project_CommitterShip, "start")
    descriptor = None
    for klass in project_CommitterShip.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_project_committership_has_end():
    assert hasattr(project_CommitterShip, "end")
    descriptor = None
    for klass in project_CommitterShip.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_project_person_is_not_abstract():
    assert not inspect.isabstract(project_Person)


def test_project_person_constructor_exists():
    assert callable(project_Person.__init__)


def test_project_person_constructor_args():
    sig = inspect.signature(project_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "image" in params, "Missing parameter 'image'"
    assert "email" in params, "Missing parameter 'email'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_project_person_has_lastname():
    assert hasattr(project_Person, "lastname")
    descriptor = None
    for klass in project_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_project_person_has_image():
    assert hasattr(project_Person, "image")
    descriptor = None
    for klass in project_Person.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_project_person_has_email():
    assert hasattr(project_Person, "email")
    descriptor = None
    for klass in project_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_project_person_has_firstname():
    assert hasattr(project_Person, "firstname")
    descriptor = None
    for klass in project_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_project_project_is_not_abstract():
    assert not inspect.isabstract(project_Project)


def test_project_project_constructor_exists():
    assert callable(project_Project.__init__)


def test_project_project_constructor_args():
    sig = inspect.signature(project_Project.__init__)
    params = list(sig.parameters.keys())
    assert "shortname" in params, "Missing parameter 'shortname'"
    assert "homepage" in params, "Missing parameter 'homepage'"
    assert "longname" in params, "Missing parameter 'longname'"
    assert "end" in params, "Missing parameter 'end'"
    assert "devmail" in params, "Missing parameter 'devmail'"
    assert "start" in params, "Missing parameter 'start'"

def test_project_project_has_shortname():
    assert hasattr(project_Project, "shortname")
    descriptor = None
    for klass in project_Project.__mro__:
        if "shortname" in klass.__dict__:
            descriptor = klass.__dict__["shortname"]
            break
    assert isinstance(descriptor, property)

def test_project_project_has_homepage():
    assert hasattr(project_Project, "homepage")
    descriptor = None
    for klass in project_Project.__mro__:
        if "homepage" in klass.__dict__:
            descriptor = klass.__dict__["homepage"]
            break
    assert isinstance(descriptor, property)

def test_project_project_has_longname():
    assert hasattr(project_Project, "longname")
    descriptor = None
    for klass in project_Project.__mro__:
        if "longname" in klass.__dict__:
            descriptor = klass.__dict__["longname"]
            break
    assert isinstance(descriptor, property)

def test_project_project_has_end():
    assert hasattr(project_Project, "end")
    descriptor = None
    for klass in project_Project.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project_project_has_devmail():
    assert hasattr(project_Project, "devmail")
    descriptor = None
    for klass in project_Project.__mro__:
        if "devmail" in klass.__dict__:
            descriptor = klass.__dict__["devmail"]
            break
    assert isinstance(descriptor, property)

def test_project_project_has_start():
    assert hasattr(project_Project, "start")
    descriptor = None
    for klass in project_Project.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project_foundation_is_not_abstract():
    assert not inspect.isabstract(project_Foundation)


def test_project_foundation_constructor_exists():
    assert callable(project_Foundation.__init__)


def test_project_foundation_constructor_args():
    sig = inspect.signature(project_Foundation.__init__)
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
project_CommitterShip_strategy = st.builds(
    project_CommitterShip,
    start=
        st.dates(),
    end=
        st.dates()
)
project_Person_strategy = st.builds(
    project_Person,
    lastname=
        safe_text,
    image=
        safe_text,
    email=
        safe_text,
    firstname=
        safe_text
)
project_Project_strategy = st.builds(
    project_Project,
    shortname=
        safe_text,
    homepage=
        safe_text,
    longname=
        safe_text,
    end=
        st.dates(),
    devmail=
        safe_text,
    start=
        st.dates()
)
project_Foundation_strategy = st.builds(
    project_Foundation,
)

@given(instance=project_CommitterShip_strategy)
@settings(max_examples=50)
def test_project_committership_instantiation(instance):
    assert isinstance(instance, project_CommitterShip)



@given(instance=project_CommitterShip_strategy)
def test_project_committership_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=project_CommitterShip_strategy)
def test_project_committership_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project_Person_strategy)
@settings(max_examples=50)
def test_project_person_instantiation(instance):
    assert isinstance(instance, project_Person)



@given(instance=project_Person_strategy)
def test_project_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=project_Person_strategy)
def test_project_person_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=project_Person_strategy)
def test_project_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=project_Person_strategy)
def test_project_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=project_Project_strategy)
@settings(max_examples=50)
def test_project_project_instantiation(instance):
    assert isinstance(instance, project_Project)



@given(instance=project_Project_strategy)
def test_project_project_shortname_setter(instance):
    original = instance.shortname
    instance.shortname = original
    assert instance.shortname == original



@given(instance=project_Project_strategy)
def test_project_project_homepage_setter(instance):
    original = instance.homepage
    instance.homepage = original
    assert instance.homepage == original



@given(instance=project_Project_strategy)
def test_project_project_longname_setter(instance):
    original = instance.longname
    instance.longname = original
    assert instance.longname == original



@given(instance=project_Project_strategy)
def test_project_project_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=project_Project_strategy)
def test_project_project_devmail_setter(instance):
    original = instance.devmail
    instance.devmail = original
    assert instance.devmail == original



@given(instance=project_Project_strategy)
def test_project_project_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project_Foundation_strategy)
@settings(max_examples=50)
def test_project_foundation_instantiation(instance):
    assert isinstance(instance, project_Foundation)
