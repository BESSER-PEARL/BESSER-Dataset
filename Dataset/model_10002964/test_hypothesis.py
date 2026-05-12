import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Faculty,
    Subject,
    Attendance,
    Access_Information,
    Authentication,
    Course,
    Department,
    HOD,
    Teacher,
    Employee_Interface,
    Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_faculty_is_not_abstract():
    assert not inspect.isabstract(Faculty)


def test_faculty_constructor_exists():
    assert callable(Faculty.__init__)


def test_faculty_constructor_args():
    sig = inspect.signature(Faculty.__init__)
    params = list(sig.parameters.keys())



def test_subject_is_not_abstract():
    assert not inspect.isabstract(Subject)


def test_subject_constructor_exists():
    assert callable(Subject.__init__)


def test_subject_constructor_args():
    sig = inspect.signature(Subject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "subjectTest" in params, "Missing parameter 'subjectTest'"
    assert "subjectCategory" in params, "Missing parameter 'subjectCategory'"
    assert "subjectType" in params, "Missing parameter 'subjectType'"
    assert "subjectID" in params, "Missing parameter 'subjectID'"

def test_subject_has_name():
    assert hasattr(Subject, "name")
    descriptor = None
    for klass in Subject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_subject_has_subjectTest():
    assert hasattr(Subject, "subjectTest")
    descriptor = None
    for klass in Subject.__mro__:
        if "subjectTest" in klass.__dict__:
            descriptor = klass.__dict__["subjectTest"]
            break
    assert isinstance(descriptor, property)

def test_subject_has_subjectCategory():
    assert hasattr(Subject, "subjectCategory")
    descriptor = None
    for klass in Subject.__mro__:
        if "subjectCategory" in klass.__dict__:
            descriptor = klass.__dict__["subjectCategory"]
            break
    assert isinstance(descriptor, property)

def test_subject_has_subjectType():
    assert hasattr(Subject, "subjectType")
    descriptor = None
    for klass in Subject.__mro__:
        if "subjectType" in klass.__dict__:
            descriptor = klass.__dict__["subjectType"]
            break
    assert isinstance(descriptor, property)

def test_subject_has_subjectID():
    assert hasattr(Subject, "subjectID")
    descriptor = None
    for klass in Subject.__mro__:
        if "subjectID" in klass.__dict__:
            descriptor = klass.__dict__["subjectID"]
            break
    assert isinstance(descriptor, property)



def test_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())



def test_access_information_is_not_abstract():
    assert not inspect.isabstract(Access_Information)


def test_access_information_constructor_exists():
    assert callable(Access_Information.__init__)


def test_access_information_constructor_args():
    sig = inspect.signature(Access_Information.__init__)
    params = list(sig.parameters.keys())



def test_authentication_is_not_abstract():
    assert not inspect.isabstract(Authentication)


def test_authentication_constructor_exists():
    assert callable(Authentication.__init__)


def test_authentication_constructor_args():
    sig = inspect.signature(Authentication.__init__)
    params = list(sig.parameters.keys())



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "CourseEndDate" in params, "Missing parameter 'CourseEndDate'"
    assert "CourseStartDate" in params, "Missing parameter 'CourseStartDate'"
    assert "courseDuration" in params, "Missing parameter 'courseDuration'"
    assert "subjects__" in params, "Missing parameter 'subjects__'"
    assert "courseName" in params, "Missing parameter 'courseName'"

def test_course_has_CourseEndDate():
    assert hasattr(Course, "CourseEndDate")
    descriptor = None
    for klass in Course.__mro__:
        if "CourseEndDate" in klass.__dict__:
            descriptor = klass.__dict__["CourseEndDate"]
            break
    assert isinstance(descriptor, property)

def test_course_has_CourseStartDate():
    assert hasattr(Course, "CourseStartDate")
    descriptor = None
    for klass in Course.__mro__:
        if "CourseStartDate" in klass.__dict__:
            descriptor = klass.__dict__["CourseStartDate"]
            break
    assert isinstance(descriptor, property)

def test_course_has_courseDuration():
    assert hasattr(Course, "courseDuration")
    descriptor = None
    for klass in Course.__mro__:
        if "courseDuration" in klass.__dict__:
            descriptor = klass.__dict__["courseDuration"]
            break
    assert isinstance(descriptor, property)

def test_course_has_subjects__():
    assert hasattr(Course, "subjects__")
    descriptor = None
    for klass in Course.__mro__:
        if "subjects__" in klass.__dict__:
            descriptor = klass.__dict__["subjects__"]
            break
    assert isinstance(descriptor, property)

def test_course_has_courseName():
    assert hasattr(Course, "courseName")
    descriptor = None
    for klass in Course.__mro__:
        if "courseName" in klass.__dict__:
            descriptor = klass.__dict__["courseName"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "courseID" in params, "Missing parameter 'courseID'"
    assert "teachers__" in params, "Missing parameter 'teachers__'"
    assert "CourseName" in params, "Missing parameter 'CourseName'"
    assert "course" in params, "Missing parameter 'course'"
    assert "students__" in params, "Missing parameter 'students__'"

def test_department_has_courseID():
    assert hasattr(Department, "courseID")
    descriptor = None
    for klass in Department.__mro__:
        if "courseID" in klass.__dict__:
            descriptor = klass.__dict__["courseID"]
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

def test_department_has_CourseName():
    assert hasattr(Department, "CourseName")
    descriptor = None
    for klass in Department.__mro__:
        if "CourseName" in klass.__dict__:
            descriptor = klass.__dict__["CourseName"]
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

def test_department_has_students__():
    assert hasattr(Department, "students__")
    descriptor = None
    for klass in Department.__mro__:
        if "students__" in klass.__dict__:
            descriptor = klass.__dict__["students__"]
            break
    assert isinstance(descriptor, property)



def test_hod_is_not_abstract():
    assert not inspect.isabstract(HOD)


def test_hod_constructor_exists():
    assert callable(HOD.__init__)


def test_hod_constructor_args():
    sig = inspect.signature(HOD.__init__)
    params = list(sig.parameters.keys())



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
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "socialsecurity" in params, "Missing parameter 'socialsecurity'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "lastNAme" in params, "Missing parameter 'lastNAme'"
    assert "middleNAme" in params, "Missing parameter 'middleNAme'"

def test_student_has_firstName():
    assert hasattr(Student, "firstName")
    descriptor = None
    for klass in Student.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_student_has_socialsecurity():
    assert hasattr(Student, "socialsecurity")
    descriptor = None
    for klass in Student.__mro__:
        if "socialsecurity" in klass.__dict__:
            descriptor = klass.__dict__["socialsecurity"]
            break
    assert isinstance(descriptor, property)

def test_student_has_ID():
    assert hasattr(Student, "ID")
    descriptor = None
    for klass in Student.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_student_has_lastNAme():
    assert hasattr(Student, "lastNAme")
    descriptor = None
    for klass in Student.__mro__:
        if "lastNAme" in klass.__dict__:
            descriptor = klass.__dict__["lastNAme"]
            break
    assert isinstance(descriptor, property)

def test_student_has_middleNAme():
    assert hasattr(Student, "middleNAme")
    descriptor = None
    for klass in Student.__mro__:
        if "middleNAme" in klass.__dict__:
            descriptor = klass.__dict__["middleNAme"]
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
Faculty_strategy = st.builds(
    Faculty,
)
Subject_strategy = st.builds(
    Subject,
    name=
        safe_text,
    subjectTest=
        safe_text,
    subjectCategory=
        safe_text,
    subjectType=
        safe_text,
    subjectID=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
)
Access_Information_strategy = st.builds(
    Access_Information,
)
Authentication_strategy = st.builds(
    Authentication,
)
Course_strategy = st.builds(
    Course,
    CourseEndDate=
        st.dates(),
    CourseStartDate=
        st.dates(),
    courseDuration=
        safe_text,
    subjects__=
        st.none(),
    courseName=
        safe_text
)
Department_strategy = st.builds(
    Department,
    courseID=
        safe_text,
    teachers__=
        st.none(),
    CourseName=
        safe_text,
    course=
        st.none(),
    students__=
        st.none()
)
HOD_strategy = st.builds(
    HOD,
)
Teacher_strategy = st.builds(
    Teacher,
)
Employee_Interface_strategy = st.builds(
    Employee_Interface,
)
Student_strategy = st.builds(
    Student,
    firstName=
        safe_text,
    socialsecurity=
        safe_text,
    ID=
        safe_text,
    lastNAme=
        safe_text,
    middleNAme=
        safe_text
)

@given(instance=Faculty_strategy)
@settings(max_examples=50)
def test_faculty_instantiation(instance):
    assert isinstance(instance, Faculty)

@given(instance=Subject_strategy)
@settings(max_examples=50)
def test_subject_instantiation(instance):
    assert isinstance(instance, Subject)



@given(instance=Subject_strategy)
def test_subject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Subject_strategy)
def test_subject_subjectTest_setter(instance):
    original = instance.subjectTest
    instance.subjectTest = original
    assert instance.subjectTest == original



@given(instance=Subject_strategy)
def test_subject_subjectCategory_setter(instance):
    original = instance.subjectCategory
    instance.subjectCategory = original
    assert instance.subjectCategory == original



@given(instance=Subject_strategy)
def test_subject_subjectType_setter(instance):
    original = instance.subjectType
    instance.subjectType = original
    assert instance.subjectType == original



@given(instance=Subject_strategy)
def test_subject_subjectID_setter(instance):
    original = instance.subjectID
    instance.subjectID = original
    assert instance.subjectID == original

@given(instance=Attendance_strategy)
@settings(max_examples=50)
def test_attendance_instantiation(instance):
    assert isinstance(instance, Attendance)

@given(instance=Access_Information_strategy)
@settings(max_examples=50)
def test_access_information_instantiation(instance):
    assert isinstance(instance, Access_Information)

@given(instance=Authentication_strategy)
@settings(max_examples=50)
def test_authentication_instantiation(instance):
    assert isinstance(instance, Authentication)

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course_CourseEndDate_setter(instance):
    original = instance.CourseEndDate
    instance.CourseEndDate = original
    assert instance.CourseEndDate == original



@given(instance=Course_strategy)
def test_course_CourseStartDate_setter(instance):
    original = instance.CourseStartDate
    instance.CourseStartDate = original
    assert instance.CourseStartDate == original



@given(instance=Course_strategy)
def test_course_courseDuration_setter(instance):
    original = instance.courseDuration
    instance.courseDuration = original
    assert instance.courseDuration == original



@given(instance=Course_strategy)
def test_course_subjects___setter(instance):
    original = instance.subjects__
    instance.subjects__ = original
    assert instance.subjects__ == original



@given(instance=Course_strategy)
def test_course_courseName_setter(instance):
    original = instance.courseName
    instance.courseName = original
    assert instance.courseName == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_courseID_setter(instance):
    original = instance.courseID
    instance.courseID = original
    assert instance.courseID == original



@given(instance=Department_strategy)
def test_department_teachers___setter(instance):
    original = instance.teachers__
    instance.teachers__ = original
    assert instance.teachers__ == original



@given(instance=Department_strategy)
def test_department_CourseName_setter(instance):
    original = instance.CourseName
    instance.CourseName = original
    assert instance.CourseName == original



@given(instance=Department_strategy)
def test_department_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original



@given(instance=Department_strategy)
def test_department_students___setter(instance):
    original = instance.students__
    instance.students__ = original
    assert instance.students__ == original

@given(instance=HOD_strategy)
@settings(max_examples=50)
def test_hod_instantiation(instance):
    assert isinstance(instance, HOD)

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
def test_student_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Student_strategy)
def test_student_socialsecurity_setter(instance):
    original = instance.socialsecurity
    instance.socialsecurity = original
    assert instance.socialsecurity == original



@given(instance=Student_strategy)
def test_student_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Student_strategy)
def test_student_lastNAme_setter(instance):
    original = instance.lastNAme
    instance.lastNAme = original
    assert instance.lastNAme == original



@given(instance=Student_strategy)
def test_student_middleNAme_setter(instance):
    original = instance.middleNAme
    instance.middleNAme = original
    assert instance.middleNAme == original
