import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    training::TrainingOrganization,
    training::Person,
    training::Training,
    training::Session,
    Person,
    training::Trainer,
    training::Trainee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_training::trainingorganization_is_not_abstract():
    assert not inspect.isabstract(training::TrainingOrganization)


def test_training::trainingorganization_constructor_exists():
    assert callable(training::TrainingOrganization.__init__)


def test_training::trainingorganization_constructor_args():
    sig = inspect.signature(training::TrainingOrganization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_training::trainingorganization_has_name():
    assert hasattr(training::TrainingOrganization, "name")
    descriptor = None
    for klass in training::TrainingOrganization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_training::person_is_not_abstract():
    assert not inspect.isabstract(training::Person)


def test_training::person_constructor_exists():
    assert callable(training::Person.__init__)


def test_training::person_constructor_args():
    sig = inspect.signature(training::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_training::person_has_lastname():
    assert hasattr(training::Person, "lastname")
    descriptor = None
    for klass in training::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_training::person_has_firstname():
    assert hasattr(training::Person, "firstname")
    descriptor = None
    for klass in training::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_training::training_is_not_abstract():
    assert not inspect.isabstract(training::Training)


def test_training::training_constructor_exists():
    assert callable(training::Training.__init__)


def test_training::training_constructor_args():
    sig = inspect.signature(training::Training.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_training::training_has_title():
    assert hasattr(training::Training, "title")
    descriptor = None
    for klass in training::Training.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_training::session_is_not_abstract():
    assert not inspect.isabstract(training::Session)


def test_training::session_constructor_exists():
    assert callable(training::Session.__init__)


def test_training::session_constructor_args():
    sig = inspect.signature(training::Session.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_training::session_has_date():
    assert hasattr(training::Session, "date")
    descriptor = None
    for klass in training::Session.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_training::trainer_is_not_abstract():
    assert not inspect.isabstract(training::Trainer)


def test_training::trainer_constructor_exists():
    assert callable(training::Trainer.__init__)


def test_training::trainer_constructor_args():
    sig = inspect.signature(training::Trainer.__init__)
    params = list(sig.parameters.keys())



def test_training::trainee_is_not_abstract():
    assert not inspect.isabstract(training::Trainee)


def test_training::trainee_constructor_exists():
    assert callable(training::Trainee.__init__)


def test_training::trainee_constructor_args():
    sig = inspect.signature(training::Trainee.__init__)
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
training::TrainingOrganization_strategy = st.builds(
    training::TrainingOrganization,
    name=
        safe_text
)
training::Person_strategy = st.builds(
    training::Person,
    lastname=
        safe_text,
    firstname=
        safe_text
)
training::Training_strategy = st.builds(
    training::Training,
    title=
        safe_text
)
training::Session_strategy = st.builds(
    training::Session,
    date=
        st.dates()
)
Person_strategy = st.builds(
    Person,
)
training::Trainer_strategy = st.builds(
    training::Trainer,
)
training::Trainee_strategy = st.builds(
    training::Trainee,
)

@given(instance=training::TrainingOrganization_strategy)
@settings(max_examples=50)
def test_training::trainingorganization_instantiation(instance):
    assert isinstance(instance, training::TrainingOrganization)

@given(instance=training::TrainingOrganization_strategy)
def test_training::trainingorganization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=training::TrainingOrganization_strategy)
def test_training::trainingorganization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=training::Person_strategy)
@settings(max_examples=50)
def test_training::person_instantiation(instance):
    assert isinstance(instance, training::Person)

@given(instance=training::Person_strategy)
def test_training::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=training::Person_strategy)
def test_training::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=training::Person_strategy)
def test_training::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=training::Person_strategy)
def test_training::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=training::Training_strategy)
@settings(max_examples=50)
def test_training::training_instantiation(instance):
    assert isinstance(instance, training::Training)

@given(instance=training::Training_strategy)
def test_training::training_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=training::Training_strategy)
def test_training::training_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=training::Session_strategy)
@settings(max_examples=50)
def test_training::session_instantiation(instance):
    assert isinstance(instance, training::Session)

@given(instance=training::Session_strategy)
def test_training::session_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=training::Session_strategy)
def test_training::session_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=training::Trainer_strategy)
@settings(max_examples=50)
def test_training::trainer_instantiation(instance):
    assert isinstance(instance, training::Trainer)

@given(instance=training::Trainee_strategy)
@settings(max_examples=50)
def test_training::trainee_instantiation(instance):
    assert isinstance(instance, training::Trainee)
