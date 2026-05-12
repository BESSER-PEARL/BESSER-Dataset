import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    VALIDATE,
    STUDENT,
    EMPLOYEE,
    ADMIN,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_validate_is_not_abstract():
    assert not inspect.isabstract(VALIDATE)


def test_validate_constructor_exists():
    assert callable(VALIDATE.__init__)


def test_validate_constructor_args():
    sig = inspect.signature(VALIDATE.__init__)
    params = list(sig.parameters.keys())
    assert "USERNAME" in params, "Missing parameter 'USERNAME'"
    assert "PASSWORD" in params, "Missing parameter 'PASSWORD'"

def test_validate_has_USERNAME():
    assert hasattr(VALIDATE, "USERNAME")
    descriptor = None
    for klass in VALIDATE.__mro__:
        if "USERNAME" in klass.__dict__:
            descriptor = klass.__dict__["USERNAME"]
            break
    assert isinstance(descriptor, property)

def test_validate_has_PASSWORD():
    assert hasattr(VALIDATE, "PASSWORD")
    descriptor = None
    for klass in VALIDATE.__mro__:
        if "PASSWORD" in klass.__dict__:
            descriptor = klass.__dict__["PASSWORD"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(STUDENT)


def test_student_constructor_exists():
    assert callable(STUDENT.__init__)


def test_student_constructor_args():
    sig = inspect.signature(STUDENT.__init__)
    params = list(sig.parameters.keys())
    assert "EMAIL_ID" in params, "Missing parameter 'EMAIL_ID'"
    assert "CONTACT_NO" in params, "Missing parameter 'CONTACT_NO'"
    assert "NAME" in params, "Missing parameter 'NAME'"
    assert "QUALIFICATION" in params, "Missing parameter 'QUALIFICATION'"
    assert "COURSE" in params, "Missing parameter 'COURSE'"
    assert "STUD_ID" in params, "Missing parameter 'STUD_ID'"

def test_student_has_EMAIL_ID():
    assert hasattr(STUDENT, "EMAIL_ID")
    descriptor = None
    for klass in STUDENT.__mro__:
        if "EMAIL_ID" in klass.__dict__:
            descriptor = klass.__dict__["EMAIL_ID"]
            break
    assert isinstance(descriptor, property)

def test_student_has_CONTACT_NO():
    assert hasattr(STUDENT, "CONTACT_NO")
    descriptor = None
    for klass in STUDENT.__mro__:
        if "CONTACT_NO" in klass.__dict__:
            descriptor = klass.__dict__["CONTACT_NO"]
            break
    assert isinstance(descriptor, property)

def test_student_has_NAME():
    assert hasattr(STUDENT, "NAME")
    descriptor = None
    for klass in STUDENT.__mro__:
        if "NAME" in klass.__dict__:
            descriptor = klass.__dict__["NAME"]
            break
    assert isinstance(descriptor, property)

def test_student_has_QUALIFICATION():
    assert hasattr(STUDENT, "QUALIFICATION")
    descriptor = None
    for klass in STUDENT.__mro__:
        if "QUALIFICATION" in klass.__dict__:
            descriptor = klass.__dict__["QUALIFICATION"]
            break
    assert isinstance(descriptor, property)

def test_student_has_COURSE():
    assert hasattr(STUDENT, "COURSE")
    descriptor = None
    for klass in STUDENT.__mro__:
        if "COURSE" in klass.__dict__:
            descriptor = klass.__dict__["COURSE"]
            break
    assert isinstance(descriptor, property)

def test_student_has_STUD_ID():
    assert hasattr(STUDENT, "STUD_ID")
    descriptor = None
    for klass in STUDENT.__mro__:
        if "STUD_ID" in klass.__dict__:
            descriptor = klass.__dict__["STUD_ID"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(EMPLOYEE)


def test_employee_constructor_exists():
    assert callable(EMPLOYEE.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(EMPLOYEE.__init__)
    params = list(sig.parameters.keys())
    assert "EMAIL_ID" in params, "Missing parameter 'EMAIL_ID'"
    assert "QULIFICATION" in params, "Missing parameter 'QULIFICATION'"
    assert "NAME" in params, "Missing parameter 'NAME'"
    assert "EMP_ID" in params, "Missing parameter 'EMP_ID'"
    assert "CONTACT_NO" in params, "Missing parameter 'CONTACT_NO'"

def test_employee_has_EMAIL_ID():
    assert hasattr(EMPLOYEE, "EMAIL_ID")
    descriptor = None
    for klass in EMPLOYEE.__mro__:
        if "EMAIL_ID" in klass.__dict__:
            descriptor = klass.__dict__["EMAIL_ID"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_QULIFICATION():
    assert hasattr(EMPLOYEE, "QULIFICATION")
    descriptor = None
    for klass in EMPLOYEE.__mro__:
        if "QULIFICATION" in klass.__dict__:
            descriptor = klass.__dict__["QULIFICATION"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_NAME():
    assert hasattr(EMPLOYEE, "NAME")
    descriptor = None
    for klass in EMPLOYEE.__mro__:
        if "NAME" in klass.__dict__:
            descriptor = klass.__dict__["NAME"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EMP_ID():
    assert hasattr(EMPLOYEE, "EMP_ID")
    descriptor = None
    for klass in EMPLOYEE.__mro__:
        if "EMP_ID" in klass.__dict__:
            descriptor = klass.__dict__["EMP_ID"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_CONTACT_NO():
    assert hasattr(EMPLOYEE, "CONTACT_NO")
    descriptor = None
    for klass in EMPLOYEE.__mro__:
        if "CONTACT_NO" in klass.__dict__:
            descriptor = klass.__dict__["CONTACT_NO"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(ADMIN)


def test_admin_constructor_exists():
    assert callable(ADMIN.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(ADMIN.__init__)
    params = list(sig.parameters.keys())
    assert "PASSWORD" in params, "Missing parameter 'PASSWORD'"
    assert "NAME" in params, "Missing parameter 'NAME'"

def test_admin_has_PASSWORD():
    assert hasattr(ADMIN, "PASSWORD")
    descriptor = None
    for klass in ADMIN.__mro__:
        if "PASSWORD" in klass.__dict__:
            descriptor = klass.__dict__["PASSWORD"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_NAME():
    assert hasattr(ADMIN, "NAME")
    descriptor = None
    for klass in ADMIN.__mro__:
        if "NAME" in klass.__dict__:
            descriptor = klass.__dict__["NAME"]
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
VALIDATE_strategy = st.builds(
    VALIDATE,
    USERNAME=
        safe_text,
    PASSWORD=
        safe_text
)
STUDENT_strategy = st.builds(
    STUDENT,
    EMAIL_ID=
        safe_text,
    CONTACT_NO=
        st.integers(),
    NAME=
        safe_text,
    QUALIFICATION=
        safe_text,
    COURSE=
        safe_text,
    STUD_ID=
        st.integers()
)
EMPLOYEE_strategy = st.builds(
    EMPLOYEE,
    EMAIL_ID=
        safe_text,
    QULIFICATION=
        safe_text,
    NAME=
        safe_text,
    EMP_ID=
        st.integers(),
    CONTACT_NO=
        st.integers()
)
ADMIN_strategy = st.builds(
    ADMIN,
    PASSWORD=
        safe_text,
    NAME=
        safe_text
)

@given(instance=VALIDATE_strategy)
@settings(max_examples=50)
def test_validate_instantiation(instance):
    assert isinstance(instance, VALIDATE)



@given(instance=VALIDATE_strategy)
def test_validate_USERNAME_setter(instance):
    original = instance.USERNAME
    instance.USERNAME = original
    assert instance.USERNAME == original



@given(instance=VALIDATE_strategy)
def test_validate_PASSWORD_setter(instance):
    original = instance.PASSWORD
    instance.PASSWORD = original
    assert instance.PASSWORD == original

@given(instance=STUDENT_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, STUDENT)



@given(instance=STUDENT_strategy)
def test_student_EMAIL_ID_setter(instance):
    original = instance.EMAIL_ID
    instance.EMAIL_ID = original
    assert instance.EMAIL_ID == original



@given(instance=STUDENT_strategy)
def test_student_CONTACT_NO_setter(instance):
    original = instance.CONTACT_NO
    instance.CONTACT_NO = original
    assert instance.CONTACT_NO == original



@given(instance=STUDENT_strategy)
def test_student_NAME_setter(instance):
    original = instance.NAME
    instance.NAME = original
    assert instance.NAME == original



@given(instance=STUDENT_strategy)
def test_student_QUALIFICATION_setter(instance):
    original = instance.QUALIFICATION
    instance.QUALIFICATION = original
    assert instance.QUALIFICATION == original



@given(instance=STUDENT_strategy)
def test_student_COURSE_setter(instance):
    original = instance.COURSE
    instance.COURSE = original
    assert instance.COURSE == original



@given(instance=STUDENT_strategy)
def test_student_STUD_ID_setter(instance):
    original = instance.STUD_ID
    instance.STUD_ID = original
    assert instance.STUD_ID == original

@given(instance=EMPLOYEE_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, EMPLOYEE)



@given(instance=EMPLOYEE_strategy)
def test_employee_EMAIL_ID_setter(instance):
    original = instance.EMAIL_ID
    instance.EMAIL_ID = original
    assert instance.EMAIL_ID == original



@given(instance=EMPLOYEE_strategy)
def test_employee_QULIFICATION_setter(instance):
    original = instance.QULIFICATION
    instance.QULIFICATION = original
    assert instance.QULIFICATION == original



@given(instance=EMPLOYEE_strategy)
def test_employee_NAME_setter(instance):
    original = instance.NAME
    instance.NAME = original
    assert instance.NAME == original



@given(instance=EMPLOYEE_strategy)
def test_employee_EMP_ID_setter(instance):
    original = instance.EMP_ID
    instance.EMP_ID = original
    assert instance.EMP_ID == original



@given(instance=EMPLOYEE_strategy)
def test_employee_CONTACT_NO_setter(instance):
    original = instance.CONTACT_NO
    instance.CONTACT_NO = original
    assert instance.CONTACT_NO == original

@given(instance=ADMIN_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, ADMIN)



@given(instance=ADMIN_strategy)
def test_admin_PASSWORD_setter(instance):
    original = instance.PASSWORD
    instance.PASSWORD = original
    assert instance.PASSWORD == original



@given(instance=ADMIN_strategy)
def test_admin_NAME_setter(instance):
    original = instance.NAME
    instance.NAME = original
    assert instance.NAME == original
