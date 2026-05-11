import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Student,
    SourceModel::BachelorStudent,
    SourceModel::MasterStudent,
    Person,
    SourceModel::Professor,
    SourceModel::Student,
    SourceModel::Person,
    SourceModel::Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel::bachelorstudent_is_not_abstract():
    assert not inspect.isabstract(SourceModel::BachelorStudent)


def test_sourcemodel::bachelorstudent_constructor_exists():
    assert callable(SourceModel::BachelorStudent.__init__)


def test_sourcemodel::bachelorstudent_constructor_args():
    sig = inspect.signature(SourceModel::BachelorStudent.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel::masterstudent_is_not_abstract():
    assert not inspect.isabstract(SourceModel::MasterStudent)


def test_sourcemodel::masterstudent_constructor_exists():
    assert callable(SourceModel::MasterStudent.__init__)


def test_sourcemodel::masterstudent_constructor_args():
    sig = inspect.signature(SourceModel::MasterStudent.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel::professor_is_not_abstract():
    assert not inspect.isabstract(SourceModel::Professor)


def test_sourcemodel::professor_constructor_exists():
    assert callable(SourceModel::Professor.__init__)


def test_sourcemodel::professor_constructor_args():
    sig = inspect.signature(SourceModel::Professor.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel::student_is_not_abstract():
    assert not inspect.isabstract(SourceModel::Student)


def test_sourcemodel::student_constructor_exists():
    assert callable(SourceModel::Student.__init__)


def test_sourcemodel::student_constructor_args():
    sig = inspect.signature(SourceModel::Student.__init__)
    params = list(sig.parameters.keys())



def test_sourcemodel::person_is_not_abstract():
    assert not inspect.isabstract(SourceModel::Person)


def test_sourcemodel::person_constructor_exists():
    assert callable(SourceModel::Person.__init__)


def test_sourcemodel::person_constructor_args():
    sig = inspect.signature(SourceModel::Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"

def test_sourcemodel::person_has_age():
    assert hasattr(SourceModel::Person, "age")
    descriptor = None
    for klass in SourceModel::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_sourcemodel::container_is_not_abstract():
    assert not inspect.isabstract(SourceModel::Container)


def test_sourcemodel::container_constructor_exists():
    assert callable(SourceModel::Container.__init__)


def test_sourcemodel::container_constructor_args():
    sig = inspect.signature(SourceModel::Container.__init__)
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
Student_strategy = st.builds(
    Student,
)
SourceModel::BachelorStudent_strategy = st.builds(
    SourceModel::BachelorStudent,
)
SourceModel::MasterStudent_strategy = st.builds(
    SourceModel::MasterStudent,
)
Person_strategy = st.builds(
    Person,
)
SourceModel::Professor_strategy = st.builds(
    SourceModel::Professor,
)
SourceModel::Student_strategy = st.builds(
    SourceModel::Student,
)
SourceModel::Person_strategy = st.builds(
    SourceModel::Person,
    age=
        safe_text
)
SourceModel::Container_strategy = st.builds(
    SourceModel::Container,
)

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)

@given(instance=SourceModel::BachelorStudent_strategy)
@settings(max_examples=50)
def test_sourcemodel::bachelorstudent_instantiation(instance):
    assert isinstance(instance, SourceModel::BachelorStudent)

@given(instance=SourceModel::MasterStudent_strategy)
@settings(max_examples=50)
def test_sourcemodel::masterstudent_instantiation(instance):
    assert isinstance(instance, SourceModel::MasterStudent)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=SourceModel::Professor_strategy)
@settings(max_examples=50)
def test_sourcemodel::professor_instantiation(instance):
    assert isinstance(instance, SourceModel::Professor)

@given(instance=SourceModel::Student_strategy)
@settings(max_examples=50)
def test_sourcemodel::student_instantiation(instance):
    assert isinstance(instance, SourceModel::Student)

@given(instance=SourceModel::Person_strategy)
@settings(max_examples=50)
def test_sourcemodel::person_instantiation(instance):
    assert isinstance(instance, SourceModel::Person)

@given(instance=SourceModel::Person_strategy)
def test_sourcemodel::person_age_type(instance):
    assert isinstance(instance.age, str)


@given(instance=SourceModel::Person_strategy)
def test_sourcemodel::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=SourceModel::Container_strategy)
@settings(max_examples=50)
def test_sourcemodel::container_instantiation(instance):
    assert isinstance(instance, SourceModel::Container)
