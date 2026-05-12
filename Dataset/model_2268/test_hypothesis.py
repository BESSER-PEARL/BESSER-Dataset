import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    school_SchoolDatabase,
    school_BooleanExpr,
    school_Where,
    school_Query,
    school_CourseResult,
    school_Teacher,
    school_Student,
    school_Course,
    school_CourseOfStudy,
    school_Faculty,
    school_School,
    SchoolElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school_schooldatabase_is_not_abstract():
    assert not inspect.isabstract(school_SchoolDatabase)


def test_school_schooldatabase_constructor_exists():
    assert callable(school_SchoolDatabase.__init__)


def test_school_schooldatabase_constructor_args():
    sig = inspect.signature(school_SchoolDatabase.__init__)
    params = list(sig.parameters.keys())



def test_school_booleanexpr_is_not_abstract():
    assert not inspect.isabstract(school_BooleanExpr)


def test_school_booleanexpr_constructor_exists():
    assert callable(school_BooleanExpr.__init__)


def test_school_booleanexpr_constructor_args():
    sig = inspect.signature(school_BooleanExpr.__init__)
    params = list(sig.parameters.keys())
    assert "lhs" in params, "Missing parameter 'lhs'"
    assert "operator" in params, "Missing parameter 'operator'"
    assert "rhs" in params, "Missing parameter 'rhs'"

def test_school_booleanexpr_has_lhs():
    assert hasattr(school_BooleanExpr, "lhs")
    descriptor = None
    for klass in school_BooleanExpr.__mro__:
        if "lhs" in klass.__dict__:
            descriptor = klass.__dict__["lhs"]
            break
    assert isinstance(descriptor, property)

def test_school_booleanexpr_has_operator():
    assert hasattr(school_BooleanExpr, "operator")
    descriptor = None
    for klass in school_BooleanExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_school_booleanexpr_has_rhs():
    assert hasattr(school_BooleanExpr, "rhs")
    descriptor = None
    for klass in school_BooleanExpr.__mro__:
        if "rhs" in klass.__dict__:
            descriptor = klass.__dict__["rhs"]
            break
    assert isinstance(descriptor, property)



def test_school_where_is_not_abstract():
    assert not inspect.isabstract(school_Where)


def test_school_where_constructor_exists():
    assert callable(school_Where.__init__)


def test_school_where_constructor_args():
    sig = inspect.signature(school_Where.__init__)
    params = list(sig.parameters.keys())



def test_school_query_is_not_abstract():
    assert not inspect.isabstract(school_Query)


def test_school_query_constructor_exists():
    assert callable(school_Query.__init__)


def test_school_query_constructor_args():
    sig = inspect.signature(school_Query.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_school_query_has_type():
    assert hasattr(school_Query, "type")
    descriptor = None
    for klass in school_Query.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_school_courseresult_is_not_abstract():
    assert not inspect.isabstract(school_CourseResult)


def test_school_courseresult_constructor_exists():
    assert callable(school_CourseResult.__init__)


def test_school_courseresult_constructor_args():
    sig = inspect.signature(school_CourseResult.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"

def test_school_courseresult_has_grade():
    assert hasattr(school_CourseResult, "grade")
    descriptor = None
    for klass in school_CourseResult.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_school_teacher_is_not_abstract():
    assert not inspect.isabstract(school_Teacher)


def test_school_teacher_constructor_exists():
    assert callable(school_Teacher.__init__)


def test_school_teacher_constructor_args():
    sig = inspect.signature(school_Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_teacher_has_name():
    assert hasattr(school_Teacher, "name")
    descriptor = None
    for klass in school_Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_student_is_not_abstract():
    assert not inspect.isabstract(school_Student)


def test_school_student_constructor_exists():
    assert callable(school_Student.__init__)


def test_school_student_constructor_args():
    sig = inspect.signature(school_Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentNumber" in params, "Missing parameter 'studentNumber'"
    assert "name" in params, "Missing parameter 'name'"

def test_school_student_has_studentNumber():
    assert hasattr(school_Student, "studentNumber")
    descriptor = None
    for klass in school_Student.__mro__:
        if "studentNumber" in klass.__dict__:
            descriptor = klass.__dict__["studentNumber"]
            break
    assert isinstance(descriptor, property)

def test_school_student_has_name():
    assert hasattr(school_Student, "name")
    descriptor = None
    for klass in school_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_course_is_not_abstract():
    assert not inspect.isabstract(school_Course)


def test_school_course_constructor_exists():
    assert callable(school_Course.__init__)


def test_school_course_constructor_args():
    sig = inspect.signature(school_Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseNumber" in params, "Missing parameter 'courseNumber'"
    assert "name" in params, "Missing parameter 'name'"

def test_school_course_has_courseNumber():
    assert hasattr(school_Course, "courseNumber")
    descriptor = None
    for klass in school_Course.__mro__:
        if "courseNumber" in klass.__dict__:
            descriptor = klass.__dict__["courseNumber"]
            break
    assert isinstance(descriptor, property)

def test_school_course_has_name():
    assert hasattr(school_Course, "name")
    descriptor = None
    for klass in school_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_courseofstudy_is_not_abstract():
    assert not inspect.isabstract(school_CourseOfStudy)


def test_school_courseofstudy_constructor_exists():
    assert callable(school_CourseOfStudy.__init__)


def test_school_courseofstudy_constructor_args():
    sig = inspect.signature(school_CourseOfStudy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_courseofstudy_has_name():
    assert hasattr(school_CourseOfStudy, "name")
    descriptor = None
    for klass in school_CourseOfStudy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_faculty_is_not_abstract():
    assert not inspect.isabstract(school_Faculty)


def test_school_faculty_constructor_exists():
    assert callable(school_Faculty.__init__)


def test_school_faculty_constructor_args():
    sig = inspect.signature(school_Faculty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_faculty_has_name():
    assert hasattr(school_Faculty, "name")
    descriptor = None
    for klass in school_Faculty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_school_is_not_abstract():
    assert not inspect.isabstract(school_School)


def test_school_school_constructor_exists():
    assert callable(school_School.__init__)


def test_school_school_constructor_args():
    sig = inspect.signature(school_School.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_school_has_name():
    assert hasattr(school_School, "name")
    descriptor = None
    for klass in school_School.__mro__:
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
        "Student",
        "Teacher",
        "Faculty",
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
school_SchoolDatabase_strategy = st.builds(
    school_SchoolDatabase,
)
school_BooleanExpr_strategy = st.builds(
    school_BooleanExpr,
    lhs=
        safe_text,
    operator=
        safe_text,
    rhs=
        safe_text
)
school_Where_strategy = st.builds(
    school_Where,
)
school_Query_strategy = st.builds(
    school_Query,
    type=
        safe_text
)
school_CourseResult_strategy = st.builds(
    school_CourseResult,
    grade=
        safe_text
)
school_Teacher_strategy = st.builds(
    school_Teacher,
    name=
        safe_text
)
school_Student_strategy = st.builds(
    school_Student,
    studentNumber=
        safe_text,
    name=
        safe_text
)
school_Course_strategy = st.builds(
    school_Course,
    courseNumber=
        safe_text,
    name=
        safe_text
)
school_CourseOfStudy_strategy = st.builds(
    school_CourseOfStudy,
    name=
        safe_text
)
school_Faculty_strategy = st.builds(
    school_Faculty,
    name=
        safe_text
)
school_School_strategy = st.builds(
    school_School,
    name=
        safe_text
)

@given(instance=school_SchoolDatabase_strategy)
@settings(max_examples=50)
def test_school_schooldatabase_instantiation(instance):
    assert isinstance(instance, school_SchoolDatabase)

@given(instance=school_BooleanExpr_strategy)
@settings(max_examples=50)
def test_school_booleanexpr_instantiation(instance):
    assert isinstance(instance, school_BooleanExpr)



@given(instance=school_BooleanExpr_strategy)
def test_school_booleanexpr_lhs_setter(instance):
    original = instance.lhs
    instance.lhs = original
    assert instance.lhs == original



@given(instance=school_BooleanExpr_strategy)
def test_school_booleanexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=school_BooleanExpr_strategy)
def test_school_booleanexpr_rhs_setter(instance):
    original = instance.rhs
    instance.rhs = original
    assert instance.rhs == original

@given(instance=school_Where_strategy)
@settings(max_examples=50)
def test_school_where_instantiation(instance):
    assert isinstance(instance, school_Where)

@given(instance=school_Query_strategy)
@settings(max_examples=50)
def test_school_query_instantiation(instance):
    assert isinstance(instance, school_Query)



@given(instance=school_Query_strategy)
def test_school_query_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=school_CourseResult_strategy)
@settings(max_examples=50)
def test_school_courseresult_instantiation(instance):
    assert isinstance(instance, school_CourseResult)



@given(instance=school_CourseResult_strategy)
def test_school_courseresult_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=school_Teacher_strategy)
@settings(max_examples=50)
def test_school_teacher_instantiation(instance):
    assert isinstance(instance, school_Teacher)



@given(instance=school_Teacher_strategy)
def test_school_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_Student_strategy)
@settings(max_examples=50)
def test_school_student_instantiation(instance):
    assert isinstance(instance, school_Student)



@given(instance=school_Student_strategy)
def test_school_student_studentNumber_setter(instance):
    original = instance.studentNumber
    instance.studentNumber = original
    assert instance.studentNumber == original



@given(instance=school_Student_strategy)
def test_school_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_Course_strategy)
@settings(max_examples=50)
def test_school_course_instantiation(instance):
    assert isinstance(instance, school_Course)



@given(instance=school_Course_strategy)
def test_school_course_courseNumber_setter(instance):
    original = instance.courseNumber
    instance.courseNumber = original
    assert instance.courseNumber == original



@given(instance=school_Course_strategy)
def test_school_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_CourseOfStudy_strategy)
@settings(max_examples=50)
def test_school_courseofstudy_instantiation(instance):
    assert isinstance(instance, school_CourseOfStudy)



@given(instance=school_CourseOfStudy_strategy)
def test_school_courseofstudy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_Faculty_strategy)
@settings(max_examples=50)
def test_school_faculty_instantiation(instance):
    assert isinstance(instance, school_Faculty)



@given(instance=school_Faculty_strategy)
def test_school_faculty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_School_strategy)
@settings(max_examples=50)
def test_school_school_instantiation(instance):
    assert isinstance(instance, school_School)



@given(instance=school_School_strategy)
def test_school_school_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
