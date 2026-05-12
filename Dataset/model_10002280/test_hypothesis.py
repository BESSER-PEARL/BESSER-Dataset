import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Login,
    Course,
    Admin,
    Database,
    Teacher,
    Student,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "CourseName" in params, "Missing parameter 'CourseName'"
    assert "CourseNumber" in params, "Missing parameter 'CourseNumber'"
    assert "Course_Teacher" in params, "Missing parameter 'Course_Teacher'"

def test_course_has_CourseName():
    assert hasattr(Course, "CourseName")
    descriptor = None
    for klass in Course.__mro__:
        if "CourseName" in klass.__dict__:
            descriptor = klass.__dict__["CourseName"]
            break
    assert isinstance(descriptor, property)

def test_course_has_CourseNumber():
    assert hasattr(Course, "CourseNumber")
    descriptor = None
    for klass in Course.__mro__:
        if "CourseNumber" in klass.__dict__:
            descriptor = klass.__dict__["CourseNumber"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Course_Teacher():
    assert hasattr(Course, "Course_Teacher")
    descriptor = None
    for klass in Course.__mro__:
        if "Course_Teacher" in klass.__dict__:
            descriptor = klass.__dict__["Course_Teacher"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_database_constructor_exists():
    assert callable(Database.__init__)


def test_database_constructor_args():
    sig = inspect.signature(Database.__init__)
    params = list(sig.parameters.keys())
    assert "Grades" in params, "Missing parameter 'Grades'"
    assert "Schedules" in params, "Missing parameter 'Schedules'"
    assert "Accounts" in params, "Missing parameter 'Accounts'"
    assert "Materials" in params, "Missing parameter 'Materials'"

def test_database_has_Grades():
    assert hasattr(Database, "Grades")
    descriptor = None
    for klass in Database.__mro__:
        if "Grades" in klass.__dict__:
            descriptor = klass.__dict__["Grades"]
            break
    assert isinstance(descriptor, property)

def test_database_has_Schedules():
    assert hasattr(Database, "Schedules")
    descriptor = None
    for klass in Database.__mro__:
        if "Schedules" in klass.__dict__:
            descriptor = klass.__dict__["Schedules"]
            break
    assert isinstance(descriptor, property)

def test_database_has_Accounts():
    assert hasattr(Database, "Accounts")
    descriptor = None
    for klass in Database.__mro__:
        if "Accounts" in klass.__dict__:
            descriptor = klass.__dict__["Accounts"]
            break
    assert isinstance(descriptor, property)

def test_database_has_Materials():
    assert hasattr(Database, "Materials")
    descriptor = None
    for klass in Database.__mro__:
        if "Materials" in klass.__dict__:
            descriptor = klass.__dict__["Materials"]
            break
    assert isinstance(descriptor, property)



def test_teacher_is_not_abstract():
    assert not inspect.isabstract(Teacher)


def test_teacher_constructor_exists():
    assert callable(Teacher.__init__)


def test_teacher_constructor_args():
    sig = inspect.signature(Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "Assigned_Courses" in params, "Missing parameter 'Assigned_Courses'"

def test_teacher_has_Assigned_Courses():
    assert hasattr(Teacher, "Assigned_Courses")
    descriptor = None
    for klass in Teacher.__mro__:
        if "Assigned_Courses" in klass.__dict__:
            descriptor = klass.__dict__["Assigned_Courses"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "Year" in params, "Missing parameter 'Year'"

def test_student_has_Year():
    assert hasattr(Student, "Year")
    descriptor = None
    for klass in Student.__mro__:
        if "Year" in klass.__dict__:
            descriptor = klass.__dict__["Year"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "First_Name" in params, "Missing parameter 'First_Name'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "ID_Number" in params, "Missing parameter 'ID_Number'"

def test_user_has_First_Name():
    assert hasattr(User, "First_Name")
    descriptor = None
    for klass in User.__mro__:
        if "First_Name" in klass.__dict__:
            descriptor = klass.__dict__["First_Name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Last_Name():
    assert hasattr(User, "Last_Name")
    descriptor = None
    for klass in User.__mro__:
        if "Last_Name" in klass.__dict__:
            descriptor = klass.__dict__["Last_Name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_ID_Number():
    assert hasattr(User, "ID_Number")
    descriptor = None
    for klass in User.__mro__:
        if "ID_Number" in klass.__dict__:
            descriptor = klass.__dict__["ID_Number"]
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
Login_strategy = st.builds(
    Login,
)
Course_strategy = st.builds(
    Course,
    CourseName=
        safe_text,
    CourseNumber=
        safe_text,
    Course_Teacher=
        st.none()
)
Admin_strategy = st.builds(
    Admin,
)
Database_strategy = st.builds(
    Database,
    Grades=
        st.none(),
    Schedules=
        st.none(),
    Accounts=
        st.none(),
    Materials=
        st.none()
)
Teacher_strategy = st.builds(
    Teacher,
    Assigned_Courses=
        safe_text
)
Student_strategy = st.builds(
    Student,
    Year=
        safe_text
)
User_strategy = st.builds(
    User,
    First_Name=
        safe_text,
    Password=
        safe_text,
    Last_Name=
        safe_text,
    ID_Number=
        st.integers()
)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course_CourseName_setter(instance):
    original = instance.CourseName
    instance.CourseName = original
    assert instance.CourseName == original



@given(instance=Course_strategy)
def test_course_CourseNumber_setter(instance):
    original = instance.CourseNumber
    instance.CourseNumber = original
    assert instance.CourseNumber == original



@given(instance=Course_strategy)
def test_course_Course_Teacher_setter(instance):
    original = instance.Course_Teacher
    instance.Course_Teacher = original
    assert instance.Course_Teacher == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=Database_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, Database)



@given(instance=Database_strategy)
def test_database_Grades_setter(instance):
    original = instance.Grades
    instance.Grades = original
    assert instance.Grades == original



@given(instance=Database_strategy)
def test_database_Schedules_setter(instance):
    original = instance.Schedules
    instance.Schedules = original
    assert instance.Schedules == original



@given(instance=Database_strategy)
def test_database_Accounts_setter(instance):
    original = instance.Accounts
    instance.Accounts = original
    assert instance.Accounts == original



@given(instance=Database_strategy)
def test_database_Materials_setter(instance):
    original = instance.Materials
    instance.Materials = original
    assert instance.Materials == original

@given(instance=Teacher_strategy)
@settings(max_examples=50)
def test_teacher_instantiation(instance):
    assert isinstance(instance, Teacher)



@given(instance=Teacher_strategy)
def test_teacher_Assigned_Courses_setter(instance):
    original = instance.Assigned_Courses
    instance.Assigned_Courses = original
    assert instance.Assigned_Courses == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_Year_setter(instance):
    original = instance.Year
    instance.Year = original
    assert instance.Year == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_First_Name_setter(instance):
    original = instance.First_Name
    instance.First_Name = original
    assert instance.First_Name == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_user_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=User_strategy)
def test_user_ID_Number_setter(instance):
    original = instance.ID_Number
    instance.ID_Number = original
    assert instance.ID_Number == original
