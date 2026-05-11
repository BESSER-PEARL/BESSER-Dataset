import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    school::SchoolDatabase,
    school::BooleanExpr,
    school::Where,
    school::Query,
    school::CourseResult,
    school::Teacher,
    school::Student,
    school::Course,
    school::CourseOfStudy,
    school::Faculty,
    school::School,
    SchoolElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school::schooldatabase_is_not_abstract():
    assert not inspect.isabstract(school::SchoolDatabase)


def test_school::schooldatabase_constructor_exists():
    assert callable(school::SchoolDatabase.__init__)


def test_school::schooldatabase_constructor_args():
    sig = inspect.signature(school::SchoolDatabase.__init__)
    params = list(sig.parameters.keys())



def test_school::booleanexpr_is_not_abstract():
    assert not inspect.isabstract(school::BooleanExpr)


def test_school::booleanexpr_constructor_exists():
    assert callable(school::BooleanExpr.__init__)


def test_school::booleanexpr_constructor_args():
    sig = inspect.signature(school::BooleanExpr.__init__)
    params = list(sig.parameters.keys())
    assert "rhs" in params, "Missing parameter 'rhs'"
    assert "lhs" in params, "Missing parameter 'lhs'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_school::booleanexpr_has_rhs():
    assert hasattr(school::BooleanExpr, "rhs")
    descriptor = None
    for klass in school::BooleanExpr.__mro__:
        if "rhs" in klass.__dict__:
            descriptor = klass.__dict__["rhs"]
            break
    assert isinstance(descriptor, property)

def test_school::booleanexpr_has_lhs():
    assert hasattr(school::BooleanExpr, "lhs")
    descriptor = None
    for klass in school::BooleanExpr.__mro__:
        if "lhs" in klass.__dict__:
            descriptor = klass.__dict__["lhs"]
            break
    assert isinstance(descriptor, property)

def test_school::booleanexpr_has_operator():
    assert hasattr(school::BooleanExpr, "operator")
    descriptor = None
    for klass in school::BooleanExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_school::where_is_not_abstract():
    assert not inspect.isabstract(school::Where)


def test_school::where_constructor_exists():
    assert callable(school::Where.__init__)


def test_school::where_constructor_args():
    sig = inspect.signature(school::Where.__init__)
    params = list(sig.parameters.keys())



def test_school::query_is_not_abstract():
    assert not inspect.isabstract(school::Query)


def test_school::query_constructor_exists():
    assert callable(school::Query.__init__)


def test_school::query_constructor_args():
    sig = inspect.signature(school::Query.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_school::query_has_type():
    assert hasattr(school::Query, "type")
    descriptor = None
    for klass in school::Query.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_school::courseresult_is_not_abstract():
    assert not inspect.isabstract(school::CourseResult)


def test_school::courseresult_constructor_exists():
    assert callable(school::CourseResult.__init__)


def test_school::courseresult_constructor_args():
    sig = inspect.signature(school::CourseResult.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"

def test_school::courseresult_has_grade():
    assert hasattr(school::CourseResult, "grade")
    descriptor = None
    for klass in school::CourseResult.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_school::teacher_is_not_abstract():
    assert not inspect.isabstract(school::Teacher)


def test_school::teacher_constructor_exists():
    assert callable(school::Teacher.__init__)


def test_school::teacher_constructor_args():
    sig = inspect.signature(school::Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::teacher_has_name():
    assert hasattr(school::Teacher, "name")
    descriptor = None
    for klass in school::Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::student_is_not_abstract():
    assert not inspect.isabstract(school::Student)


def test_school::student_constructor_exists():
    assert callable(school::Student.__init__)


def test_school::student_constructor_args():
    sig = inspect.signature(school::Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentNumber" in params, "Missing parameter 'studentNumber'"
    assert "name" in params, "Missing parameter 'name'"

def test_school::student_has_studentNumber():
    assert hasattr(school::Student, "studentNumber")
    descriptor = None
    for klass in school::Student.__mro__:
        if "studentNumber" in klass.__dict__:
            descriptor = klass.__dict__["studentNumber"]
            break
    assert isinstance(descriptor, property)

def test_school::student_has_name():
    assert hasattr(school::Student, "name")
    descriptor = None
    for klass in school::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::course_is_not_abstract():
    assert not inspect.isabstract(school::Course)


def test_school::course_constructor_exists():
    assert callable(school::Course.__init__)


def test_school::course_constructor_args():
    sig = inspect.signature(school::Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseNumber" in params, "Missing parameter 'courseNumber'"
    assert "name" in params, "Missing parameter 'name'"

def test_school::course_has_courseNumber():
    assert hasattr(school::Course, "courseNumber")
    descriptor = None
    for klass in school::Course.__mro__:
        if "courseNumber" in klass.__dict__:
            descriptor = klass.__dict__["courseNumber"]
            break
    assert isinstance(descriptor, property)

def test_school::course_has_name():
    assert hasattr(school::Course, "name")
    descriptor = None
    for klass in school::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::courseofstudy_is_not_abstract():
    assert not inspect.isabstract(school::CourseOfStudy)


def test_school::courseofstudy_constructor_exists():
    assert callable(school::CourseOfStudy.__init__)


def test_school::courseofstudy_constructor_args():
    sig = inspect.signature(school::CourseOfStudy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::courseofstudy_has_name():
    assert hasattr(school::CourseOfStudy, "name")
    descriptor = None
    for klass in school::CourseOfStudy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::faculty_is_not_abstract():
    assert not inspect.isabstract(school::Faculty)


def test_school::faculty_constructor_exists():
    assert callable(school::Faculty.__init__)


def test_school::faculty_constructor_args():
    sig = inspect.signature(school::Faculty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::faculty_has_name():
    assert hasattr(school::Faculty, "name")
    descriptor = None
    for klass in school::Faculty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::school_is_not_abstract():
    assert not inspect.isabstract(school::School)


def test_school::school_constructor_exists():
    assert callable(school::School.__init__)


def test_school::school_constructor_args():
    sig = inspect.signature(school::School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::school_has_name():
    assert hasattr(school::School, "name")
    descriptor = None
    for klass in school::School.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_schoolelement_exists():
    # Check that the Enumeration exists
    assert SchoolElement is not None

def test_schoolelement_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchoolElement]
    expected_literals = [
        "Course",
        "CourseOfStudy",
        "School",
        "Teacher",
        "Faculty",
        "Student",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchoolElement"


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
school::SchoolDatabase_strategy = st.builds(
    school::SchoolDatabase,
)
school::BooleanExpr_strategy = st.builds(
    school::BooleanExpr,
    rhs=
        safe_text,
    lhs=
        safe_text,
    operator=
        safe_text
)
school::Where_strategy = st.builds(
    school::Where,
)
school::Query_strategy = st.builds(
    school::Query,
    type=
        safe_text
)
school::CourseResult_strategy = st.builds(
    school::CourseResult,
    grade=
        safe_text
)
school::Teacher_strategy = st.builds(
    school::Teacher,
    name=
        safe_text
)
school::Student_strategy = st.builds(
    school::Student,
    studentNumber=
        safe_text,
    name=
        safe_text
)
school::Course_strategy = st.builds(
    school::Course,
    courseNumber=
        safe_text,
    name=
        safe_text
)
school::CourseOfStudy_strategy = st.builds(
    school::CourseOfStudy,
    name=
        safe_text
)
school::Faculty_strategy = st.builds(
    school::Faculty,
    name=
        safe_text
)
school::School_strategy = st.builds(
    school::School,
    name=
        safe_text
)

@given(instance=school::SchoolDatabase_strategy)
@settings(max_examples=50)
def test_school::schooldatabase_instantiation(instance):
    assert isinstance(instance, school::SchoolDatabase)

@given(instance=school::BooleanExpr_strategy)
@settings(max_examples=50)
def test_school::booleanexpr_instantiation(instance):
    assert isinstance(instance, school::BooleanExpr)

@given(instance=school::BooleanExpr_strategy)
def test_school::booleanexpr_rhs_type(instance):
    assert isinstance(instance.rhs, str)


@given(instance=school::BooleanExpr_strategy)
def test_school::booleanexpr_rhs_setter(instance):
    original = instance.rhs
    instance.rhs = original
    assert instance.rhs == original

@given(instance=school::BooleanExpr_strategy)
def test_school::booleanexpr_lhs_type(instance):
    assert isinstance(instance.lhs, str)


@given(instance=school::BooleanExpr_strategy)
def test_school::booleanexpr_lhs_setter(instance):
    original = instance.lhs
    instance.lhs = original
    assert instance.lhs == original

@given(instance=school::BooleanExpr_strategy)
def test_school::booleanexpr_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=school::BooleanExpr_strategy)
def test_school::booleanexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=school::Where_strategy)
@settings(max_examples=50)
def test_school::where_instantiation(instance):
    assert isinstance(instance, school::Where)

@given(instance=school::Query_strategy)
@settings(max_examples=50)
def test_school::query_instantiation(instance):
    assert isinstance(instance, school::Query)

@given(instance=school::Query_strategy)
def test_school::query_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=school::Query_strategy)
def test_school::query_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=school::CourseResult_strategy)
@settings(max_examples=50)
def test_school::courseresult_instantiation(instance):
    assert isinstance(instance, school::CourseResult)

@given(instance=school::CourseResult_strategy)
def test_school::courseresult_grade_type(instance):
    assert isinstance(instance.grade, str)


@given(instance=school::CourseResult_strategy)
def test_school::courseresult_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=school::Teacher_strategy)
@settings(max_examples=50)
def test_school::teacher_instantiation(instance):
    assert isinstance(instance, school::Teacher)

@given(instance=school::Teacher_strategy)
def test_school::teacher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Teacher_strategy)
def test_school::teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::Student_strategy)
@settings(max_examples=50)
def test_school::student_instantiation(instance):
    assert isinstance(instance, school::Student)

@given(instance=school::Student_strategy)
def test_school::student_studentNumber_type(instance):
    assert isinstance(instance.studentNumber, str)


@given(instance=school::Student_strategy)
def test_school::student_studentNumber_setter(instance):
    original = instance.studentNumber
    instance.studentNumber = original
    assert instance.studentNumber == original

@given(instance=school::Student_strategy)
def test_school::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Student_strategy)
def test_school::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::Course_strategy)
@settings(max_examples=50)
def test_school::course_instantiation(instance):
    assert isinstance(instance, school::Course)

@given(instance=school::Course_strategy)
def test_school::course_courseNumber_type(instance):
    assert isinstance(instance.courseNumber, str)


@given(instance=school::Course_strategy)
def test_school::course_courseNumber_setter(instance):
    original = instance.courseNumber
    instance.courseNumber = original
    assert instance.courseNumber == original

@given(instance=school::Course_strategy)
def test_school::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Course_strategy)
def test_school::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::CourseOfStudy_strategy)
@settings(max_examples=50)
def test_school::courseofstudy_instantiation(instance):
    assert isinstance(instance, school::CourseOfStudy)

@given(instance=school::CourseOfStudy_strategy)
def test_school::courseofstudy_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::CourseOfStudy_strategy)
def test_school::courseofstudy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::Faculty_strategy)
@settings(max_examples=50)
def test_school::faculty_instantiation(instance):
    assert isinstance(instance, school::Faculty)

@given(instance=school::Faculty_strategy)
def test_school::faculty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Faculty_strategy)
def test_school::faculty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::School_strategy)
@settings(max_examples=50)
def test_school::school_instantiation(instance):
    assert isinstance(instance, school::School)

@given(instance=school::School_strategy)
def test_school::school_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::School_strategy)
def test_school::school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
