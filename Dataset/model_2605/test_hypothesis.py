import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    project::CommitterShip,
    project::Person,
    project::Project,
    project::Foundation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_project::committership_is_not_abstract():
    assert not inspect.isabstract(project::CommitterShip)


def test_project::committership_constructor_exists():
    assert callable(project::CommitterShip.__init__)


def test_project::committership_constructor_args():
    sig = inspect.signature(project::CommitterShip.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_project::committership_has_end():
    assert hasattr(project::CommitterShip, "end")
    descriptor = None
    for klass in project::CommitterShip.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_project::committership_has_start():
    assert hasattr(project::CommitterShip, "start")
    descriptor = None
    for klass in project::CommitterShip.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_project::person_is_not_abstract():
    assert not inspect.isabstract(project::Person)


def test_project::person_constructor_exists():
    assert callable(project::Person.__init__)


def test_project::person_constructor_args():
    sig = inspect.signature(project::Person.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "email" in params, "Missing parameter 'email'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_project::person_has_image():
    assert hasattr(project::Person, "image")
    descriptor = None
    for klass in project::Person.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_project::person_has_firstname():
    assert hasattr(project::Person, "firstname")
    descriptor = None
    for klass in project::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_project::person_has_email():
    assert hasattr(project::Person, "email")
    descriptor = None
    for klass in project::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_project::person_has_lastname():
    assert hasattr(project::Person, "lastname")
    descriptor = None
    for klass in project::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_project::project_is_not_abstract():
    assert not inspect.isabstract(project::Project)


def test_project::project_constructor_exists():
    assert callable(project::Project.__init__)


def test_project::project_constructor_args():
    sig = inspect.signature(project::Project.__init__)
    params = list(sig.parameters.keys())
    assert "longname" in params, "Missing parameter 'longname'"
    assert "devmail" in params, "Missing parameter 'devmail'"
    assert "start" in params, "Missing parameter 'start'"
    assert "shortname" in params, "Missing parameter 'shortname'"
    assert "homepage" in params, "Missing parameter 'homepage'"
    assert "end" in params, "Missing parameter 'end'"

def test_project::project_has_longname():
    assert hasattr(project::Project, "longname")
    descriptor = None
    for klass in project::Project.__mro__:
        if "longname" in klass.__dict__:
            descriptor = klass.__dict__["longname"]
            break
    assert isinstance(descriptor, property)

def test_project::project_has_devmail():
    assert hasattr(project::Project, "devmail")
    descriptor = None
    for klass in project::Project.__mro__:
        if "devmail" in klass.__dict__:
            descriptor = klass.__dict__["devmail"]
            break
    assert isinstance(descriptor, property)

def test_project::project_has_start():
    assert hasattr(project::Project, "start")
    descriptor = None
    for klass in project::Project.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_project::project_has_shortname():
    assert hasattr(project::Project, "shortname")
    descriptor = None
    for klass in project::Project.__mro__:
        if "shortname" in klass.__dict__:
            descriptor = klass.__dict__["shortname"]
            break
    assert isinstance(descriptor, property)

def test_project::project_has_homepage():
    assert hasattr(project::Project, "homepage")
    descriptor = None
    for klass in project::Project.__mro__:
        if "homepage" in klass.__dict__:
            descriptor = klass.__dict__["homepage"]
            break
    assert isinstance(descriptor, property)

def test_project::project_has_end():
    assert hasattr(project::Project, "end")
    descriptor = None
    for klass in project::Project.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_project::foundation_is_not_abstract():
    assert not inspect.isabstract(project::Foundation)


def test_project::foundation_constructor_exists():
    assert callable(project::Foundation.__init__)


def test_project::foundation_constructor_args():
    sig = inspect.signature(project::Foundation.__init__)
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
project::CommitterShip_strategy = st.builds(
    project::CommitterShip,
    end=
        st.dates(),
    start=
        st.dates()
)
project::Person_strategy = st.builds(
    project::Person,
    image=
        safe_text,
    firstname=
        safe_text,
    email=
        safe_text,
    lastname=
        safe_text
)
project::Project_strategy = st.builds(
    project::Project,
    longname=
        safe_text,
    devmail=
        safe_text,
    start=
        st.dates(),
    shortname=
        safe_text,
    homepage=
        safe_text,
    end=
        st.dates()
)
project::Foundation_strategy = st.builds(
    project::Foundation,
)

@given(instance=project::CommitterShip_strategy)
@settings(max_examples=50)
def test_project::committership_instantiation(instance):
    assert isinstance(instance, project::CommitterShip)

@given(instance=project::CommitterShip_strategy)
def test_project::committership_end_type(instance):
    assert isinstance(instance.end, date)


@given(instance=project::CommitterShip_strategy)
def test_project::committership_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project::CommitterShip_strategy)
def test_project::committership_start_type(instance):
    assert isinstance(instance.start, date)


@given(instance=project::CommitterShip_strategy)
def test_project::committership_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project::Person_strategy)
@settings(max_examples=50)
def test_project::person_instantiation(instance):
    assert isinstance(instance, project::Person)

@given(instance=project::Person_strategy)
def test_project::person_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=project::Person_strategy)
def test_project::person_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=project::Person_strategy)
def test_project::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=project::Person_strategy)
def test_project::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=project::Person_strategy)
def test_project::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=project::Person_strategy)
def test_project::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=project::Person_strategy)
def test_project::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=project::Person_strategy)
def test_project::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=project::Project_strategy)
@settings(max_examples=50)
def test_project::project_instantiation(instance):
    assert isinstance(instance, project::Project)

@given(instance=project::Project_strategy)
def test_project::project_longname_type(instance):
    assert isinstance(instance.longname, str)


@given(instance=project::Project_strategy)
def test_project::project_longname_setter(instance):
    original = instance.longname
    instance.longname = original
    assert instance.longname == original

@given(instance=project::Project_strategy)
def test_project::project_devmail_type(instance):
    assert isinstance(instance.devmail, str)


@given(instance=project::Project_strategy)
def test_project::project_devmail_setter(instance):
    original = instance.devmail
    instance.devmail = original
    assert instance.devmail == original

@given(instance=project::Project_strategy)
def test_project::project_start_type(instance):
    assert isinstance(instance.start, date)


@given(instance=project::Project_strategy)
def test_project::project_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=project::Project_strategy)
def test_project::project_shortname_type(instance):
    assert isinstance(instance.shortname, str)


@given(instance=project::Project_strategy)
def test_project::project_shortname_setter(instance):
    original = instance.shortname
    instance.shortname = original
    assert instance.shortname == original

@given(instance=project::Project_strategy)
def test_project::project_homepage_type(instance):
    assert isinstance(instance.homepage, str)


@given(instance=project::Project_strategy)
def test_project::project_homepage_setter(instance):
    original = instance.homepage
    instance.homepage = original
    assert instance.homepage == original

@given(instance=project::Project_strategy)
def test_project::project_end_type(instance):
    assert isinstance(instance.end, date)


@given(instance=project::Project_strategy)
def test_project::project_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=project::Foundation_strategy)
@settings(max_examples=50)
def test_project::foundation_instantiation(instance):
    assert isinstance(instance, project::Foundation)
