import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyClass,
    Admin,
    Course,
    Department,
    Teacher,
    Employee_Interface,
    Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "subjects__" in params, "Missing parameter 'subjects__'"
    assert "duration" in params, "Missing parameter 'duration'"

def test_course_has_subjects__():
    assert hasattr(Course, "subjects__")
    descriptor = None
    for klass in Course.__mro__:
        if "subjects__" in klass.__dict__:
            descriptor = klass.__dict__["subjects__"]
            break
    assert isinstance(descriptor, property)

def test_course_has_duration():
    assert hasattr(Course, "duration")
    descriptor = None
    for klass in Course.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "students__" in params, "Missing parameter 'students__'"
    assert "teachers__" in params, "Missing parameter 'teachers__'"
    assert "course" in params, "Missing parameter 'course'"
    assert "hod" in params, "Missing parameter 'hod'"

def test_department_has_students__():
    assert hasattr(Department, "students__")
    descriptor = None
    for klass in Department.__mro__:
        if "students__" in klass.__dict__:
            descriptor = klass.__dict__["students__"]
            break
    assert isinstance(descriptor, property)

def test_department_has_teachers__():
    assert hasattr(Department, "teachers__")
    descriptor = None
    for klass in Department.__mro__:
        if "teachers__" in klass.__dict__:
            descriptor = klass.__dict__["teachers__"]
            break
    assert isinstance(descriptor, property)

def test_department_has_course():
    assert hasattr(Department, "course")
    descriptor = None
    for klass in Department.__mro__:
        if "course" in klass.__dict__:
            descriptor = klass.__dict__["course"]
            break
    assert isinstance(descriptor, property)

def test_department_has_hod():
    assert hasattr(Department, "hod")
    descriptor = None
    for klass in Department.__mro__:
        if "hod" in klass.__dict__:
            descriptor = klass.__dict__["hod"]
            break
    assert isinstance(descriptor, property)



def test_teacher_is_not_abstract():
    assert not inspect.isabstract(Teacher)


def test_teacher_constructor_exists():
    assert callable(Teacher.__init__)


def test_teacher_constructor_args():
    sig = inspect.signature(Teacher.__init__)
    params = list(sig.parameters.keys())



def test_employee_interface_is_not_abstract():
    assert not inspect.isabstract(Employee_Interface)


def test_employee_interface_constructor_exists():
    assert callable(Employee_Interface.__init__)


def test_employee_interface_constructor_args():
    sig = inspect.signature(Employee_Interface.__init__)
    params = list(sig.parameters.keys())



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_student_has_ID():
    assert hasattr(Student, "ID")
    descriptor = None
    for klass in Student.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_student_has_Name():
    assert hasattr(Student, "Name")
    descriptor = None
    for klass in Student.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
MyClass_strategy = st.builds(
    MyClass,
)
Admin_strategy = st.builds(
    Admin,
)
Course_strategy = st.builds(
    Course,
    subjects__=
        safe_text,
    duration=
        safe_text
)
Department_strategy = st.builds(
    Department,
    students__=
        st.none(),
    teachers__=
        st.none(),
    course=
        st.none(),
    hod=
        safe_text
)
Teacher_strategy = st.builds(
    Teacher,
)
Employee_Interface_strategy = st.builds(
    Employee_Interface,
)
Student_strategy = st.builds(
    Student,
    ID=
        safe_text,
    Name=
        safe_text
)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course_subjects___setter(instance):
    original = instance.subjects__
    instance.subjects__ = original
    assert instance.subjects__ == original



@given(instance=Course_strategy)
def test_course_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_students___setter(instance):
    original = instance.students__
    instance.students__ = original
    assert instance.students__ == original



@given(instance=Department_strategy)
def test_department_teachers___setter(instance):
    original = instance.teachers__
    instance.teachers__ = original
    assert instance.teachers__ == original



@given(instance=Department_strategy)
def test_department_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original



@given(instance=Department_strategy)
def test_department_hod_setter(instance):
    original = instance.hod
    instance.hod = original
    assert instance.hod == original

@given(instance=Teacher_strategy)
@settings(max_examples=50)
def test_teacher_instantiation(instance):
    assert isinstance(instance, Teacher)

@given(instance=Employee_Interface_strategy)
@settings(max_examples=50)
def test_employee_interface_instantiation(instance):
    assert isinstance(instance, Employee_Interface)

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Student_strategy)
def test_student_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
