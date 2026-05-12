import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    school_SchoolModel,
    Person,
    school_Teacher,
    school_Student,
    school_Named,
    school_SchoolStatistics,
    Named,
    school_Person,
    school_School,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school_schoolmodel_is_not_abstract():
    assert not inspect.isabstract(school_SchoolModel)


def test_school_schoolmodel_constructor_exists():
    assert callable(school_SchoolModel.__init__)


def test_school_schoolmodel_constructor_args():
    sig = inspect.signature(school_SchoolModel.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_school_teacher_is_not_abstract():
    assert not inspect.isabstract(school_Teacher)


def test_school_teacher_constructor_exists():
    assert callable(school_Teacher.__init__)


def test_school_teacher_constructor_args():
    sig = inspect.signature(school_Teacher.__init__)
    params = list(sig.parameters.keys())



def test_school_student_is_not_abstract():
    assert not inspect.isabstract(school_Student)


def test_school_student_constructor_exists():
    assert callable(school_Student.__init__)


def test_school_student_constructor_args():
    sig = inspect.signature(school_Student.__init__)
    params = list(sig.parameters.keys())
    assert "registrationNum" in params, "Missing parameter 'registrationNum'"

def test_school_student_has_registrationNum():
    assert hasattr(school_Student, "registrationNum")
    descriptor = None
    for klass in school_Student.__mro__:
        if "registrationNum" in klass.__dict__:
            descriptor = klass.__dict__["registrationNum"]
            break
    assert isinstance(descriptor, property)



def test_school_named_is_not_abstract():
    assert not inspect.isabstract(school_Named)


def test_school_named_constructor_exists():
    assert callable(school_Named.__init__)


def test_school_named_constructor_args():
    sig = inspect.signature(school_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_named_has_name():
    assert hasattr(school_Named, "name")
    descriptor = None
    for klass in school_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_schoolstatistics_is_not_abstract():
    assert not inspect.isabstract(school_SchoolStatistics)


def test_school_schoolstatistics_constructor_exists():
    assert callable(school_SchoolStatistics.__init__)


def test_school_schoolstatistics_constructor_args():
    sig = inspect.signature(school_SchoolStatistics.__init__)
    params = list(sig.parameters.keys())
    assert "studentsNumber" in params, "Missing parameter 'studentsNumber'"
    assert "teachersNumber" in params, "Missing parameter 'teachersNumber'"
    assert "studentsWithNoTeacher" in params, "Missing parameter 'studentsWithNoTeacher'"

def test_school_schoolstatistics_has_studentsNumber():
    assert hasattr(school_SchoolStatistics, "studentsNumber")
    descriptor = None
    for klass in school_SchoolStatistics.__mro__:
        if "studentsNumber" in klass.__dict__:
            descriptor = klass.__dict__["studentsNumber"]
            break
    assert isinstance(descriptor, property)

def test_school_schoolstatistics_has_teachersNumber():
    assert hasattr(school_SchoolStatistics, "teachersNumber")
    descriptor = None
    for klass in school_SchoolStatistics.__mro__:
        if "teachersNumber" in klass.__dict__:
            descriptor = klass.__dict__["teachersNumber"]
            break
    assert isinstance(descriptor, property)

def test_school_schoolstatistics_has_studentsWithNoTeacher():
    assert hasattr(school_SchoolStatistics, "studentsWithNoTeacher")
    descriptor = None
    for klass in school_SchoolStatistics.__mro__:
        if "studentsWithNoTeacher" in klass.__dict__:
            descriptor = klass.__dict__["studentsWithNoTeacher"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_school_person_is_not_abstract():
    assert not inspect.isabstract(school_Person)


def test_school_person_constructor_exists():
    assert callable(school_Person.__init__)


def test_school_person_constructor_args():
    sig = inspect.signature(school_Person.__init__)
    params = list(sig.parameters.keys())



def test_school_school_is_not_abstract():
    assert not inspect.isabstract(school_School)


def test_school_school_constructor_exists():
    assert callable(school_School.__init__)


def test_school_school_constructor_args():
    sig = inspect.signature(school_School.__init__)
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
school_SchoolModel_strategy = st.builds(
    school_SchoolModel,
)
Person_strategy = st.builds(
    Person,
)
school_Teacher_strategy = st.builds(
    school_Teacher,
)
school_Student_strategy = st.builds(
    school_Student,
    registrationNum=
        st.integers()
)
school_Named_strategy = st.builds(
    school_Named,
    name=
        safe_text
)
school_SchoolStatistics_strategy = st.builds(
    school_SchoolStatistics,
    studentsNumber=
        st.integers(),
    teachersNumber=
        st.integers(),
    studentsWithNoTeacher=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
school_Person_strategy = st.builds(
    school_Person,
)
school_School_strategy = st.builds(
    school_School,
)

@given(instance=school_SchoolModel_strategy)
@settings(max_examples=50)
def test_school_schoolmodel_instantiation(instance):
    assert isinstance(instance, school_SchoolModel)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=school_Teacher_strategy)
@settings(max_examples=50)
def test_school_teacher_instantiation(instance):
    assert isinstance(instance, school_Teacher)

@given(instance=school_Student_strategy)
@settings(max_examples=50)
def test_school_student_instantiation(instance):
    assert isinstance(instance, school_Student)



@given(instance=school_Student_strategy)
def test_school_student_registrationNum_setter(instance):
    original = instance.registrationNum
    instance.registrationNum = original
    assert instance.registrationNum == original

@given(instance=school_Named_strategy)
@settings(max_examples=50)
def test_school_named_instantiation(instance):
    assert isinstance(instance, school_Named)



@given(instance=school_Named_strategy)
def test_school_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_SchoolStatistics_strategy)
@settings(max_examples=50)
def test_school_schoolstatistics_instantiation(instance):
    assert isinstance(instance, school_SchoolStatistics)



@given(instance=school_SchoolStatistics_strategy)
def test_school_schoolstatistics_studentsNumber_setter(instance):
    original = instance.studentsNumber
    instance.studentsNumber = original
    assert instance.studentsNumber == original



@given(instance=school_SchoolStatistics_strategy)
def test_school_schoolstatistics_teachersNumber_setter(instance):
    original = instance.teachersNumber
    instance.teachersNumber = original
    assert instance.teachersNumber == original



@given(instance=school_SchoolStatistics_strategy)
def test_school_schoolstatistics_studentsWithNoTeacher_setter(instance):
    original = instance.studentsWithNoTeacher
    instance.studentsWithNoTeacher = original
    assert instance.studentsWithNoTeacher == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=school_Person_strategy)
@settings(max_examples=50)
def test_school_person_instantiation(instance):
    assert isinstance(instance, school_Person)

@given(instance=school_School_strategy)
@settings(max_examples=50)
def test_school_school_instantiation(instance):
    assert isinstance(instance, school_School)
