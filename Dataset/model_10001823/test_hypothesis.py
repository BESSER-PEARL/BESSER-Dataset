import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Nurse,
    Patient,
    System_Admin,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_nurse_has_id():
    assert hasattr(Nurse, "id")
    descriptor = None
    for klass in Nurse.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_nurse_has_attribute2():
    assert hasattr(Nurse, "attribute2")
    descriptor = None
    for klass in Nurse.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "telno" in params, "Missing parameter 'telno'"
    assert "address" in params, "Missing parameter 'address'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_patient_has_age():
    assert hasattr(Patient, "age")
    descriptor = None
    for klass in Patient.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_telno():
    assert hasattr(Patient, "telno")
    descriptor = None
    for klass in Patient.__mro__:
        if "telno" in klass.__dict__:
            descriptor = klass.__dict__["telno"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_address():
    assert hasattr(Patient, "address")
    descriptor = None
    for klass in Patient.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_id():
    assert hasattr(Patient, "id")
    descriptor = None
    for klass in Patient.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_name():
    assert hasattr(Patient, "name")
    descriptor = None
    for klass in Patient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_sex():
    assert hasattr(Patient, "sex")
    descriptor = None
    for klass in Patient.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_system_admin_is_not_abstract():
    assert not inspect.isabstract(System_Admin)


def test_system_admin_constructor_exists():
    assert callable(System_Admin.__init__)


def test_system_admin_constructor_args():
    sig = inspect.signature(System_Admin.__init__)
    params = list(sig.parameters.keys())
    assert "adminid" in params, "Missing parameter 'adminid'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_system_admin_has_adminid():
    assert hasattr(System_Admin, "adminid")
    descriptor = None
    for klass in System_Admin.__mro__:
        if "adminid" in klass.__dict__:
            descriptor = klass.__dict__["adminid"]
            break
    assert isinstance(descriptor, property)

def test_system_admin_has_id():
    assert hasattr(System_Admin, "id")
    descriptor = None
    for klass in System_Admin.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_system_admin_has_name():
    assert hasattr(System_Admin, "name")
    descriptor = None
    for klass in System_Admin.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "docid" in params, "Missing parameter 'docid'"
    assert "address" in params, "Missing parameter 'address'"
    assert "specialization" in params, "Missing parameter 'specialization'"
    assert "phno" in params, "Missing parameter 'phno'"
    assert "name" in params, "Missing parameter 'name'"
    assert "department" in params, "Missing parameter 'department'"

def test_doctor_has_docid():
    assert hasattr(Doctor, "docid")
    descriptor = None
    for klass in Doctor.__mro__:
        if "docid" in klass.__dict__:
            descriptor = klass.__dict__["docid"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_address():
    assert hasattr(Doctor, "address")
    descriptor = None
    for klass in Doctor.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_specialization():
    assert hasattr(Doctor, "specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "specialization" in klass.__dict__:
            descriptor = klass.__dict__["specialization"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_phno():
    assert hasattr(Doctor, "phno")
    descriptor = None
    for klass in Doctor.__mro__:
        if "phno" in klass.__dict__:
            descriptor = klass.__dict__["phno"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_name():
    assert hasattr(Doctor, "name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_department():
    assert hasattr(Doctor, "department")
    descriptor = None
    for klass in Doctor.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
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
Nurse_strategy = st.builds(
    Nurse,
    id=
        st.integers(),
    attribute2=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    age=
        st.integers(),
    telno=
        st.integers(),
    address=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text,
    sex=
        safe_text
)
System_Admin_strategy = st.builds(
    System_Admin,
    adminid=
        st.integers(),
    id=
        st.integers(),
    name=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    docid=
        st.integers(),
    address=
        safe_text,
    specialization=
        safe_text,
    phno=
        st.integers(),
    name=
        safe_text,
    department=
        safe_text
)

@given(instance=Nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, Nurse)



@given(instance=Nurse_strategy)
def test_nurse_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Nurse_strategy)
def test_nurse_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Patient_strategy)
def test_patient_telno_setter(instance):
    original = instance.telno
    instance.telno = original
    assert instance.telno == original



@given(instance=Patient_strategy)
def test_patient_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Patient_strategy)
def test_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patient_strategy)
def test_patient_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=System_Admin_strategy)
@settings(max_examples=50)
def test_system_admin_instantiation(instance):
    assert isinstance(instance, System_Admin)



@given(instance=System_Admin_strategy)
def test_system_admin_adminid_setter(instance):
    original = instance.adminid
    instance.adminid = original
    assert instance.adminid == original



@given(instance=System_Admin_strategy)
def test_system_admin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=System_Admin_strategy)
def test_system_admin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_docid_setter(instance):
    original = instance.docid
    instance.docid = original
    assert instance.docid == original



@given(instance=Doctor_strategy)
def test_doctor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Doctor_strategy)
def test_doctor_specialization_setter(instance):
    original = instance.specialization
    instance.specialization = original
    assert instance.specialization == original



@given(instance=Doctor_strategy)
def test_doctor_phno_setter(instance):
    original = instance.phno
    instance.phno = original
    assert instance.phno == original



@given(instance=Doctor_strategy)
def test_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Doctor_strategy)
def test_doctor_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original
