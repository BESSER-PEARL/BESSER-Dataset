import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    training_Training,
    training_Session,
    Person,
    training_Trainee,
    training_Trainer,
    training_TrainingOrganization,
    training_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_training_training_is_not_abstract():
    assert not inspect.isabstract(training_Training)


def test_training_training_constructor_exists():
    assert callable(training_Training.__init__)


def test_training_training_constructor_args():
    sig = inspect.signature(training_Training.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_training_training_has_title():
    assert hasattr(training_Training, "title")
    descriptor = None
    for klass in training_Training.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_training_session_is_not_abstract():
    assert not inspect.isabstract(training_Session)


def test_training_session_constructor_exists():
    assert callable(training_Session.__init__)


def test_training_session_constructor_args():
    sig = inspect.signature(training_Session.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_training_session_has_date():
    assert hasattr(training_Session, "date")
    descriptor = None
    for klass in training_Session.__mro__:
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



def test_training_trainee_is_not_abstract():
    assert not inspect.isabstract(training_Trainee)


def test_training_trainee_constructor_exists():
    assert callable(training_Trainee.__init__)


def test_training_trainee_constructor_args():
    sig = inspect.signature(training_Trainee.__init__)
    params = list(sig.parameters.keys())



def test_training_trainer_is_not_abstract():
    assert not inspect.isabstract(training_Trainer)


def test_training_trainer_constructor_exists():
    assert callable(training_Trainer.__init__)


def test_training_trainer_constructor_args():
    sig = inspect.signature(training_Trainer.__init__)
    params = list(sig.parameters.keys())



def test_training_trainingorganization_is_not_abstract():
    assert not inspect.isabstract(training_TrainingOrganization)


def test_training_trainingorganization_constructor_exists():
    assert callable(training_TrainingOrganization.__init__)


def test_training_trainingorganization_constructor_args():
    sig = inspect.signature(training_TrainingOrganization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_training_trainingorganization_has_name():
    assert hasattr(training_TrainingOrganization, "name")
    descriptor = None
    for klass in training_TrainingOrganization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_training_person_is_not_abstract():
    assert not inspect.isabstract(training_Person)


def test_training_person_constructor_exists():
    assert callable(training_Person.__init__)


def test_training_person_constructor_args():
    sig = inspect.signature(training_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_training_person_has_lastname():
    assert hasattr(training_Person, "lastname")
    descriptor = None
    for klass in training_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_training_person_has_firstname():
    assert hasattr(training_Person, "firstname")
    descriptor = None
    for klass in training_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
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
training_Training_strategy = st.builds(
    training_Training,
    title=
        safe_text
)
training_Session_strategy = st.builds(
    training_Session,
    date=
        st.dates()
)
Person_strategy = st.builds(
    Person,
)
training_Trainee_strategy = st.builds(
    training_Trainee,
)
training_Trainer_strategy = st.builds(
    training_Trainer,
)
training_TrainingOrganization_strategy = st.builds(
    training_TrainingOrganization,
    name=
        safe_text
)
training_Person_strategy = st.builds(
    training_Person,
    lastname=
        safe_text,
    firstname=
        safe_text
)

@given(instance=training_Training_strategy)
@settings(max_examples=50)
def test_training_training_instantiation(instance):
    assert isinstance(instance, training_Training)



@given(instance=training_Training_strategy)
def test_training_training_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=training_Session_strategy)
@settings(max_examples=50)
def test_training_session_instantiation(instance):
    assert isinstance(instance, training_Session)



@given(instance=training_Session_strategy)
def test_training_session_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=training_Trainee_strategy)
@settings(max_examples=50)
def test_training_trainee_instantiation(instance):
    assert isinstance(instance, training_Trainee)

@given(instance=training_Trainer_strategy)
@settings(max_examples=50)
def test_training_trainer_instantiation(instance):
    assert isinstance(instance, training_Trainer)

@given(instance=training_TrainingOrganization_strategy)
@settings(max_examples=50)
def test_training_trainingorganization_instantiation(instance):
    assert isinstance(instance, training_TrainingOrganization)



@given(instance=training_TrainingOrganization_strategy)
def test_training_trainingorganization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=training_Person_strategy)
@settings(max_examples=50)
def test_training_person_instantiation(instance):
    assert isinstance(instance, training_Person)



@given(instance=training_Person_strategy)
def test_training_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=training_Person_strategy)
def test_training_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original
