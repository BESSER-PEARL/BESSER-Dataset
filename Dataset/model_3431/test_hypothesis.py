import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    school::SchoolModel,
    Person,
    school::Teacher,
    school::Student,
    school::Named,
    school::SchoolStatistics,
    Named,
    school::Person,
    school::School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school::schoolmodel_is_not_abstract():
    assert not inspect.isabstract(school::SchoolModel)


def test_school::schoolmodel_constructor_exists():
    assert callable(school::SchoolModel.__init__)


def test_school::schoolmodel_constructor_args():
    sig = inspect.signature(school::SchoolModel.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_school::teacher_is_not_abstract():
    assert not inspect.isabstract(school::Teacher)


def test_school::teacher_constructor_exists():
    assert callable(school::Teacher.__init__)


def test_school::teacher_constructor_args():
    sig = inspect.signature(school::Teacher.__init__)
    params = list(sig.parameters.keys())



def test_school::student_is_not_abstract():
    assert not inspect.isabstract(school::Student)


def test_school::student_constructor_exists():
    assert callable(school::Student.__init__)


def test_school::student_constructor_args():
    sig = inspect.signature(school::Student.__init__)
    params = list(sig.parameters.keys())
    assert "registrationNum" in params, "Missing parameter 'registrationNum'"

def test_school::student_has_registrationNum():
    assert hasattr(school::Student, "registrationNum")
    descriptor = None
    for klass in school::Student.__mro__:
        if "registrationNum" in klass.__dict__:
            descriptor = klass.__dict__["registrationNum"]
            break
    assert isinstance(descriptor, property)



def test_school::named_is_not_abstract():
    assert not inspect.isabstract(school::Named)


def test_school::named_constructor_exists():
    assert callable(school::Named.__init__)


def test_school::named_constructor_args():
    sig = inspect.signature(school::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::named_has_name():
    assert hasattr(school::Named, "name")
    descriptor = None
    for klass in school::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::schoolstatistics_is_not_abstract():
    assert not inspect.isabstract(school::SchoolStatistics)


def test_school::schoolstatistics_constructor_exists():
    assert callable(school::SchoolStatistics.__init__)


def test_school::schoolstatistics_constructor_args():
    sig = inspect.signature(school::SchoolStatistics.__init__)
    params = list(sig.parameters.keys())
    assert "teachersNumber" in params, "Missing parameter 'teachersNumber'"
    assert "studentsWithNoTeacher" in params, "Missing parameter 'studentsWithNoTeacher'"
    assert "studentsNumber" in params, "Missing parameter 'studentsNumber'"

def test_school::schoolstatistics_has_teachersNumber():
    assert hasattr(school::SchoolStatistics, "teachersNumber")
    descriptor = None
    for klass in school::SchoolStatistics.__mro__:
        if "teachersNumber" in klass.__dict__:
            descriptor = klass.__dict__["teachersNumber"]
            break
    assert isinstance(descriptor, property)

def test_school::schoolstatistics_has_studentsWithNoTeacher():
    assert hasattr(school::SchoolStatistics, "studentsWithNoTeacher")
    descriptor = None
    for klass in school::SchoolStatistics.__mro__:
        if "studentsWithNoTeacher" in klass.__dict__:
            descriptor = klass.__dict__["studentsWithNoTeacher"]
            break
    assert isinstance(descriptor, property)

def test_school::schoolstatistics_has_studentsNumber():
    assert hasattr(school::SchoolStatistics, "studentsNumber")
    descriptor = None
    for klass in school::SchoolStatistics.__mro__:
        if "studentsNumber" in klass.__dict__:
            descriptor = klass.__dict__["studentsNumber"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_school::person_is_not_abstract():
    assert not inspect.isabstract(school::Person)


def test_school::person_constructor_exists():
    assert callable(school::Person.__init__)


def test_school::person_constructor_args():
    sig = inspect.signature(school::Person.__init__)
    params = list(sig.parameters.keys())



def test_school::school_is_not_abstract():
    assert not inspect.isabstract(school::School)


def test_school::school_constructor_exists():
    assert callable(school::School.__init__)


def test_school::school_constructor_args():
    sig = inspect.signature(school::School.__init__)
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
school::SchoolModel_strategy = st.builds(
    school::SchoolModel,
)
Person_strategy = st.builds(
    Person,
)
school::Teacher_strategy = st.builds(
    school::Teacher,
)
school::Student_strategy = st.builds(
    school::Student,
    registrationNum=
        st.integers()
)
school::Named_strategy = st.builds(
    school::Named,
    name=
        safe_text
)
school::SchoolStatistics_strategy = st.builds(
    school::SchoolStatistics,
    teachersNumber=
        st.integers(),
    studentsWithNoTeacher=
        safe_text,
    studentsNumber=
        st.integers()
)
Named_strategy = st.builds(
    Named,
)
school::Person_strategy = st.builds(
    school::Person,
)
school::School_strategy = st.builds(
    school::School,
)

@given(instance=school::SchoolModel_strategy)
@settings(max_examples=50)
def test_school::schoolmodel_instantiation(instance):
    assert isinstance(instance, school::SchoolModel)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=school::Teacher_strategy)
@settings(max_examples=50)
def test_school::teacher_instantiation(instance):
    assert isinstance(instance, school::Teacher)

@given(instance=school::Student_strategy)
@settings(max_examples=50)
def test_school::student_instantiation(instance):
    assert isinstance(instance, school::Student)

@given(instance=school::Student_strategy)
def test_school::student_registrationNum_type(instance):
    assert isinstance(instance.registrationNum, int)


@given(instance=school::Student_strategy)
def test_school::student_registrationNum_setter(instance):
    original = instance.registrationNum
    instance.registrationNum = original
    assert instance.registrationNum == original

@given(instance=school::Named_strategy)
@settings(max_examples=50)
def test_school::named_instantiation(instance):
    assert isinstance(instance, school::Named)

@given(instance=school::Named_strategy)
def test_school::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Named_strategy)
def test_school::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::SchoolStatistics_strategy)
@settings(max_examples=50)
def test_school::schoolstatistics_instantiation(instance):
    assert isinstance(instance, school::SchoolStatistics)

@given(instance=school::SchoolStatistics_strategy)
def test_school::schoolstatistics_teachersNumber_type(instance):
    assert isinstance(instance.teachersNumber, int)


@given(instance=school::SchoolStatistics_strategy)
def test_school::schoolstatistics_teachersNumber_setter(instance):
    original = instance.teachersNumber
    instance.teachersNumber = original
    assert instance.teachersNumber == original

@given(instance=school::SchoolStatistics_strategy)
def test_school::schoolstatistics_studentsWithNoTeacher_type(instance):
    assert isinstance(instance.studentsWithNoTeacher, str)


@given(instance=school::SchoolStatistics_strategy)
def test_school::schoolstatistics_studentsWithNoTeacher_setter(instance):
    original = instance.studentsWithNoTeacher
    instance.studentsWithNoTeacher = original
    assert instance.studentsWithNoTeacher == original

@given(instance=school::SchoolStatistics_strategy)
def test_school::schoolstatistics_studentsNumber_type(instance):
    assert isinstance(instance.studentsNumber, int)


@given(instance=school::SchoolStatistics_strategy)
def test_school::schoolstatistics_studentsNumber_setter(instance):
    original = instance.studentsNumber
    instance.studentsNumber = original
    assert instance.studentsNumber == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=school::Person_strategy)
@settings(max_examples=50)
def test_school::person_instantiation(instance):
    assert isinstance(instance, school::Person)

@given(instance=school::School_strategy)
@settings(max_examples=50)
def test_school::school_instantiation(instance):
    assert isinstance(instance, school::School)
