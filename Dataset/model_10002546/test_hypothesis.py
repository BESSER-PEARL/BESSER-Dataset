import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    barcode,
    controller,
    staff_member,
    Department,
    course,
    Class,
    Interface_Interface,
    Admin,
    student,
    Person,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_barcode_is_not_abstract():
    assert not inspect.isabstract(barcode)


def test_barcode_constructor_exists():
    assert callable(barcode.__init__)


def test_barcode_constructor_args():
    sig = inspect.signature(barcode.__init__)
    params = list(sig.parameters.keys())



def test_controller_is_not_abstract():
    assert not inspect.isabstract(controller)


def test_controller_constructor_exists():
    assert callable(controller.__init__)


def test_controller_constructor_args():
    sig = inspect.signature(controller.__init__)
    params = list(sig.parameters.keys())



def test_staff_member_is_not_abstract():
    assert not inspect.isabstract(staff_member)


def test_staff_member_constructor_exists():
    assert callable(staff_member.__init__)


def test_staff_member_constructor_args():
    sig = inspect.signature(staff_member.__init__)
    params = list(sig.parameters.keys())



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "dept_id" in params, "Missing parameter 'dept_id'"
    assert "dept_name" in params, "Missing parameter 'dept_name'"

def test_department_has_dept_id():
    assert hasattr(Department, "dept_id")
    descriptor = None
    for klass in Department.__mro__:
        if "dept_id" in klass.__dict__:
            descriptor = klass.__dict__["dept_id"]
            break
    assert isinstance(descriptor, property)

def test_department_has_dept_name():
    assert hasattr(Department, "dept_name")
    descriptor = None
    for klass in Department.__mro__:
        if "dept_name" in klass.__dict__:
            descriptor = klass.__dict__["dept_name"]
            break
    assert isinstance(descriptor, property)



def test_course_is_not_abstract():
    assert not inspect.isabstract(course)


def test_course_constructor_exists():
    assert callable(course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(course.__init__)
    params = list(sig.parameters.keys())
    assert "course_name" in params, "Missing parameter 'course_name'"
    assert "course_id" in params, "Missing parameter 'course_id'"
    assert "course_preq" in params, "Missing parameter 'course_preq'"
    assert "credit_hours" in params, "Missing parameter 'credit_hours'"

def test_course_has_course_name():
    assert hasattr(course, "course_name")
    descriptor = None
    for klass in course.__mro__:
        if "course_name" in klass.__dict__:
            descriptor = klass.__dict__["course_name"]
            break
    assert isinstance(descriptor, property)

def test_course_has_course_id():
    assert hasattr(course, "course_id")
    descriptor = None
    for klass in course.__mro__:
        if "course_id" in klass.__dict__:
            descriptor = klass.__dict__["course_id"]
            break
    assert isinstance(descriptor, property)

def test_course_has_course_preq():
    assert hasattr(course, "course_preq")
    descriptor = None
    for klass in course.__mro__:
        if "course_preq" in klass.__dict__:
            descriptor = klass.__dict__["course_preq"]
            break
    assert isinstance(descriptor, property)

def test_course_has_credit_hours():
    assert hasattr(course, "credit_hours")
    descriptor = None
    for klass in course.__mro__:
        if "credit_hours" in klass.__dict__:
            descriptor = klass.__dict__["credit_hours"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_student_is_not_abstract():
    assert not inspect.isabstract(student)


def test_student_constructor_exists():
    assert callable(student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(student.__init__)
    params = list(sig.parameters.keys())
    assert "major_dept" in params, "Missing parameter 'major_dept'"
    assert "minor_dept" in params, "Missing parameter 'minor_dept'"

def test_student_has_major_dept():
    assert hasattr(student, "major_dept")
    descriptor = None
    for klass in student.__mro__:
        if "major_dept" in klass.__dict__:
            descriptor = klass.__dict__["major_dept"]
            break
    assert isinstance(descriptor, property)

def test_student_has_minor_dept():
    assert hasattr(student, "minor_dept")
    descriptor = None
    for klass in student.__mro__:
        if "minor_dept" in klass.__dict__:
            descriptor = klass.__dict__["minor_dept"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "department" in params, "Missing parameter 'department'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "id" in params, "Missing parameter 'id'"
    assert "date_of_birth" in params, "Missing parameter 'date_of_birth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"

def test_person_has_address():
    assert hasattr(Person, "address")
    descriptor = None
    for klass in Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_person_has_department():
    assert hasattr(Person, "department")
    descriptor = None
    for klass in Person.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_person_has_password():
    assert hasattr(Person, "password")
    descriptor = None
    for klass in Person.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_person_has_username():
    assert hasattr(Person, "username")
    descriptor = None
    for klass in Person.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_person_has_id():
    assert hasattr(Person, "id")
    descriptor = None
    for klass in Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_person_has_date_of_birth():
    assert hasattr(Person, "date_of_birth")
    descriptor = None
    for klass in Person.__mro__:
        if "date_of_birth" in klass.__dict__:
            descriptor = klass.__dict__["date_of_birth"]
            break
    assert isinstance(descriptor, property)

def test_person_has_name():
    assert hasattr(Person, "name")
    descriptor = None
    for klass in Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_email():
    assert hasattr(Person, "email")
    descriptor = None
    for klass in Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
barcode_strategy = st.builds(
    barcode,
)
controller_strategy = st.builds(
    controller,
)
staff_member_strategy = st.builds(
    staff_member,
)
Department_strategy = st.builds(
    Department,
    dept_id=
        st.integers(),
    dept_name=
        safe_text
)
course_strategy = st.builds(
    course,
    course_name=
        safe_text,
    course_id=
        st.integers(),
    course_preq=
        safe_text,
    credit_hours=
        st.integers()
)
Class_strategy = st.builds(
    Class,
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
Admin_strategy = st.builds(
    Admin,
)
student_strategy = st.builds(
    student,
    major_dept=
        safe_text,
    minor_dept=
        safe_text
)
Person_strategy = st.builds(
    Person,
    address=
        safe_text,
    department=
        safe_text,
    password=
        st.integers(),
    username=
        safe_text,
    id=
        st.integers(),
    date_of_birth=
        safe_text,
    name=
        safe_text,
    email=
        safe_text
)

@given(instance=barcode_strategy)
@settings(max_examples=50)
def test_barcode_instantiation(instance):
    assert isinstance(instance, barcode)

@given(instance=controller_strategy)
@settings(max_examples=50)
def test_controller_instantiation(instance):
    assert isinstance(instance, controller)

@given(instance=staff_member_strategy)
@settings(max_examples=50)
def test_staff_member_instantiation(instance):
    assert isinstance(instance, staff_member)

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_dept_id_setter(instance):
    original = instance.dept_id
    instance.dept_id = original
    assert instance.dept_id == original



@given(instance=Department_strategy)
def test_department_dept_name_setter(instance):
    original = instance.dept_name
    instance.dept_name = original
    assert instance.dept_name == original

@given(instance=course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, course)



@given(instance=course_strategy)
def test_course_course_name_setter(instance):
    original = instance.course_name
    instance.course_name = original
    assert instance.course_name == original



@given(instance=course_strategy)
def test_course_course_id_setter(instance):
    original = instance.course_id
    instance.course_id = original
    assert instance.course_id == original



@given(instance=course_strategy)
def test_course_course_preq_setter(instance):
    original = instance.course_preq
    instance.course_preq = original
    assert instance.course_preq == original



@given(instance=course_strategy)
def test_course_credit_hours_setter(instance):
    original = instance.credit_hours
    instance.credit_hours = original
    assert instance.credit_hours == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, student)



@given(instance=student_strategy)
def test_student_major_dept_setter(instance):
    original = instance.major_dept
    instance.major_dept = original
    assert instance.major_dept == original



@given(instance=student_strategy)
def test_student_minor_dept_setter(instance):
    original = instance.minor_dept
    instance.minor_dept = original
    assert instance.minor_dept == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Person_strategy)
def test_person_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=Person_strategy)
def test_person_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Person_strategy)
def test_person_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Person_strategy)
def test_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Person_strategy)
def test_person_date_of_birth_setter(instance):
    original = instance.date_of_birth
    instance.date_of_birth = original
    assert instance.date_of_birth == original



@given(instance=Person_strategy)
def test_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original
