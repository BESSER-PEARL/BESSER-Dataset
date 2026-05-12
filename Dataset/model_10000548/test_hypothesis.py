import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Department,
    HOD,
    Teacher,
    Employee_Interface,
    Student,
    administrator,
    subject,
    department,
    students,
    Admin,
    Subject,
    Attendance,
    Access_Information,
    Authentication,
    Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "students__" in params, "Missing parameter 'students__'"
    assert "teachers__" in params, "Missing parameter 'teachers__'"
    assert "hod" in params, "Missing parameter 'hod'"
    assert "course" in params, "Missing parameter 'course'"

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

def test_department_has_hod():
    assert hasattr(Department, "hod")
    descriptor = None
    for klass in Department.__mro__:
        if "hod" in klass.__dict__:
            descriptor = klass.__dict__["hod"]
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
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_student_has_Name():
    assert hasattr(Student, "Name")
    descriptor = None
    for klass in Student.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(administrator)


def test_administrator_constructor_exists():
    assert callable(administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(administrator.__init__)
    params = list(sig.parameters.keys())



def test_subject_is_not_abstract():
    assert not inspect.isabstract(subject)


def test_subject_constructor_exists():
    assert callable(subject.__init__)


def test_subject_constructor_args():
    sig = inspect.signature(subject.__init__)
    params = list(sig.parameters.keys())
    assert "subjectName" in params, "Missing parameter 'subjectName'"
    assert "subjectid" in params, "Missing parameter 'subjectid'"

def test_subject_has_subjectName():
    assert hasattr(subject, "subjectName")
    descriptor = None
    for klass in subject.__mro__:
        if "subjectName" in klass.__dict__:
            descriptor = klass.__dict__["subjectName"]
            break
    assert isinstance(descriptor, property)

def test_subject_has_subjectid():
    assert hasattr(subject, "subjectid")
    descriptor = None
    for klass in subject.__mro__:
        if "subjectid" in klass.__dict__:
            descriptor = klass.__dict__["subjectid"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(department)


def test_department_constructor_exists():
    assert callable(department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(department.__init__)
    params = list(sig.parameters.keys())
    assert "director" in params, "Missing parameter 'director'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "address" in params, "Missing parameter 'address'"

def test_department_has_director():
    assert hasattr(department, "director")
    descriptor = None
    for klass in department.__mro__:
        if "director" in klass.__dict__:
            descriptor = klass.__dict__["director"]
            break
    assert isinstance(descriptor, property)

def test_department_has_name():
    assert hasattr(department, "name")
    descriptor = None
    for klass in department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_department_has_id():
    assert hasattr(department, "id")
    descriptor = None
    for klass in department.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_department_has_address():
    assert hasattr(department, "address")
    descriptor = None
    for klass in department.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_students_is_not_abstract():
    assert not inspect.isabstract(students)


def test_students_constructor_exists():
    assert callable(students.__init__)


def test_students_constructor_args():
    sig = inspect.signature(students.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "id" in params, "Missing parameter 'id'"
    assert "address" in params, "Missing parameter 'address'"
    assert "birthdate" in params, "Missing parameter 'birthdate'"

def test_students_has_name():
    assert hasattr(students, "name")
    descriptor = None
    for klass in students.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_students_has_gender():
    assert hasattr(students, "gender")
    descriptor = None
    for klass in students.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_students_has_id():
    assert hasattr(students, "id")
    descriptor = None
    for klass in students.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_students_has_address():
    assert hasattr(students, "address")
    descriptor = None
    for klass in students.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_students_has_birthdate():
    assert hasattr(students, "birthdate")
    descriptor = None
    for klass in students.__mro__:
        if "birthdate" in klass.__dict__:
            descriptor = klass.__dict__["birthdate"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_subject_is_not_abstract():
    assert not inspect.isabstract(Subject)


def test_subject_constructor_exists():
    assert callable(Subject.__init__)


def test_subject_constructor_args():
    sig = inspect.signature(Subject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_subject_has_name():
    assert hasattr(Subject, "name")
    descriptor = None
    for klass in Subject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Department_strategy = st.builds(
    Department,
    students__=
        st.none(),
    teachers__=
        st.none(),
    hod=
        st.none(),
    course=
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
    Name=
        safe_text,
    ID=
        safe_text
)
administrator_strategy = st.builds(
    administrator,
)
subject_strategy = st.builds(
    subject,
    subjectName=
        safe_text,
    subjectid=
        safe_text
)
department_strategy = st.builds(
    department,
    director=
        safe_text,
    name=
        safe_text,
    id=
        safe_text,
    address=
        safe_text
)
students_strategy = st.builds(
    students,
    name=
        safe_text,
    gender=
        safe_text,
    id=
        safe_text,
    address=
        safe_text,
    birthdate=
        st.dates()
)
Admin_strategy = st.builds(
    Admin,
)
Subject_strategy = st.builds(
    Subject,
    name=
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
    subjects__=
        st.none(),
    duration=
        safe_text
)

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
def test_department_hod_setter(instance):
    original = instance.hod
    instance.hod = original
    assert instance.hod == original



@given(instance=Department_strategy)
def test_department_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original

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
def test_student_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Student_strategy)
def test_student_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, administrator)

@given(instance=subject_strategy)
@settings(max_examples=50)
def test_subject_instantiation(instance):
    assert isinstance(instance, subject)



@given(instance=subject_strategy)
def test_subject_subjectName_setter(instance):
    original = instance.subjectName
    instance.subjectName = original
    assert instance.subjectName == original



@given(instance=subject_strategy)
def test_subject_subjectid_setter(instance):
    original = instance.subjectid
    instance.subjectid = original
    assert instance.subjectid == original

@given(instance=department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, department)



@given(instance=department_strategy)
def test_department_director_setter(instance):
    original = instance.director
    instance.director = original
    assert instance.director == original



@given(instance=department_strategy)
def test_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=department_strategy)
def test_department_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=department_strategy)
def test_department_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=students_strategy)
@settings(max_examples=50)
def test_students_instantiation(instance):
    assert isinstance(instance, students)



@given(instance=students_strategy)
def test_students_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=students_strategy)
def test_students_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=students_strategy)
def test_students_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=students_strategy)
def test_students_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=students_strategy)
def test_students_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=Subject_strategy)
@settings(max_examples=50)
def test_subject_instantiation(instance):
    assert isinstance(instance, Subject)



@given(instance=Subject_strategy)
def test_subject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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
def test_course_subjects___setter(instance):
    original = instance.subjects__
    instance.subjects__ = original
    assert instance.subjects__ == original



@given(instance=Course_strategy)
def test_course_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original
