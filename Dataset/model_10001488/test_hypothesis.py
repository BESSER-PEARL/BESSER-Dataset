import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Insurance,
    Admin,
    Patient,
    Doctor,
    user,
    UseCase3_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_insurance_is_not_abstract():
    assert not inspect.isabstract(Insurance)


def test_insurance_constructor_exists():
    assert callable(Insurance.__init__)


def test_insurance_constructor_args():
    sig = inspect.signature(Insurance.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"

def test_insurance_has_password():
    assert hasattr(Insurance, "password")
    descriptor = None
    for klass in Insurance.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_insurance_has_email():
    assert hasattr(Insurance, "email")
    descriptor = None
    for klass in Insurance.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "uname" in params, "Missing parameter 'uname'"

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_uname():
    assert hasattr(Admin, "uname")
    descriptor = None
    for klass in Admin.__mro__:
        if "uname" in klass.__dict__:
            descriptor = klass.__dict__["uname"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"

def test_patient_has_password():
    assert hasattr(Patient, "password")
    descriptor = None
    for klass in Patient.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_email():
    assert hasattr(Patient, "email")
    descriptor = None
    for klass in Patient.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"

def test_doctor_has_password():
    assert hasattr(Doctor, "password")
    descriptor = None
    for klass in Doctor.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_email():
    assert hasattr(Doctor, "email")
    descriptor = None
    for klass in Doctor.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_user_constructor_exists():
    assert callable(user.__init__)


def test_user_constructor_args():
    sig = inspect.signature(user.__init__)
    params = list(sig.parameters.keys())
    assert "phone_number" in params, "Missing parameter 'phone_number'"
    assert "address" in params, "Missing parameter 'address'"
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"

def test_user_has_phone_number():
    assert hasattr(user, "phone_number")
    descriptor = None
    for klass in user.__mro__:
        if "phone_number" in klass.__dict__:
            descriptor = klass.__dict__["phone_number"]
            break
    assert isinstance(descriptor, property)

def test_user_has_address():
    assert hasattr(user, "address")
    descriptor = None
    for klass in user.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_user_has_email():
    assert hasattr(user, "email")
    descriptor = None
    for klass in user.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(user, "password")
    descriptor = None
    for klass in user.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_name():
    assert hasattr(user, "name")
    descriptor = None
    for klass in user.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_usecase3_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase3_UseCase)


def test_usecase3_usecase_constructor_exists():
    assert callable(UseCase3_UseCase.__init__)


def test_usecase3_usecase_constructor_args():
    sig = inspect.signature(UseCase3_UseCase.__init__)
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
Insurance_strategy = st.builds(
    Insurance,
    password=
        safe_text,
    email=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    password=
        safe_text,
    uname=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    password=
        safe_text,
    email=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    password=
        safe_text,
    email=
        safe_text
)
user_strategy = st.builds(
    user,
    phone_number=
        st.integers(),
    address=
        safe_text,
    email=
        safe_text,
    password=
        safe_text,
    name=
        safe_text
)
UseCase3_UseCase_strategy = st.builds(
    UseCase3_UseCase,
)

@given(instance=Insurance_strategy)
@settings(max_examples=50)
def test_insurance_instantiation(instance):
    assert isinstance(instance, Insurance)



@given(instance=Insurance_strategy)
def test_insurance_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Insurance_strategy)
def test_insurance_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_admin_uname_setter(instance):
    original = instance.uname
    instance.uname = original
    assert instance.uname == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Patient_strategy)
def test_patient_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Doctor_strategy)
def test_doctor_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=user_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, user)



@given(instance=user_strategy)
def test_user_phone_number_setter(instance):
    original = instance.phone_number
    instance.phone_number = original
    assert instance.phone_number == original



@given(instance=user_strategy)
def test_user_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=user_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=user_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=user_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UseCase3_UseCase_strategy)
@settings(max_examples=50)
def test_usecase3_usecase_instantiation(instance):
    assert isinstance(instance, UseCase3_UseCase)
