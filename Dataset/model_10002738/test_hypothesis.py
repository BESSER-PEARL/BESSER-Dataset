import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DataBase_Component,
    Availability_Component,
    Login_Component,
    Patient,
    Admin,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database_component_is_not_abstract():
    assert not inspect.isabstract(DataBase_Component)


def test_database_component_constructor_exists():
    assert callable(DataBase_Component.__init__)


def test_database_component_constructor_args():
    sig = inspect.signature(DataBase_Component.__init__)
    params = list(sig.parameters.keys())



def test_availability_component_is_not_abstract():
    assert not inspect.isabstract(Availability_Component)


def test_availability_component_constructor_exists():
    assert callable(Availability_Component.__init__)


def test_availability_component_constructor_args():
    sig = inspect.signature(Availability_Component.__init__)
    params = list(sig.parameters.keys())



def test_login_component_is_not_abstract():
    assert not inspect.isabstract(Login_Component)


def test_login_component_constructor_exists():
    assert callable(Login_Component.__init__)


def test_login_component_constructor_args():
    sig = inspect.signature(Login_Component.__init__)
    params = list(sig.parameters.keys())



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "telno" in params, "Missing parameter 'telno'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "age" in params, "Missing parameter 'age'"
    assert "roomno" in params, "Missing parameter 'roomno'"
    assert "id" in params, "Missing parameter 'id'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_patient_has_telno():
    assert hasattr(Patient, "telno")
    descriptor = None
    for klass in Patient.__mro__:
        if "telno" in klass.__dict__:
            descriptor = klass.__dict__["telno"]
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

def test_patient_has_age():
    assert hasattr(Patient, "age")
    descriptor = None
    for klass in Patient.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_roomno():
    assert hasattr(Patient, "roomno")
    descriptor = None
    for klass in Patient.__mro__:
        if "roomno" in klass.__dict__:
            descriptor = klass.__dict__["roomno"]
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

def test_patient_has_address():
    assert hasattr(Patient, "address")
    descriptor = None
    for klass in Patient.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "doctorid" in params, "Missing parameter 'doctorid'"
    assert "id" in params, "Missing parameter 'id'"

def test_admin_has_name():
    assert hasattr(Admin, "name")
    descriptor = None
    for klass in Admin.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_doctorid():
    assert hasattr(Admin, "doctorid")
    descriptor = None
    for klass in Admin.__mro__:
        if "doctorid" in klass.__dict__:
            descriptor = klass.__dict__["doctorid"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_id():
    assert hasattr(Admin, "id")
    descriptor = None
    for klass in Admin.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "department" in params, "Missing parameter 'department'"
    assert "phno" in params, "Missing parameter 'phno'"
    assert "specialization" in params, "Missing parameter 'specialization'"
    assert "docid" in params, "Missing parameter 'docid'"

def test_doctor_has_name():
    assert hasattr(Doctor, "name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_doctor_has_department():
    assert hasattr(Doctor, "department")
    descriptor = None
    for klass in Doctor.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
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

def test_doctor_has_specialization():
    assert hasattr(Doctor, "specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "specialization" in klass.__dict__:
            descriptor = klass.__dict__["specialization"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_docid():
    assert hasattr(Doctor, "docid")
    descriptor = None
    for klass in Doctor.__mro__:
        if "docid" in klass.__dict__:
            descriptor = klass.__dict__["docid"]
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
DataBase_Component_strategy = st.builds(
    DataBase_Component,
)
Availability_Component_strategy = st.builds(
    Availability_Component,
)
Login_Component_strategy = st.builds(
    Login_Component,
)
Patient_strategy = st.builds(
    Patient,
    telno=
        st.integers(),
    sex=
        safe_text,
    age=
        st.integers(),
    roomno=
        st.integers(),
    id=
        st.integers(),
    address=
        safe_text,
    name=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    name=
        safe_text,
    doctorid=
        st.integers(),
    id=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    name=
        safe_text,
    address=
        safe_text,
    department=
        safe_text,
    phno=
        st.integers(),
    specialization=
        safe_text,
    docid=
        st.integers()
)

@given(instance=DataBase_Component_strategy)
@settings(max_examples=50)
def test_database_component_instantiation(instance):
    assert isinstance(instance, DataBase_Component)

@given(instance=Availability_Component_strategy)
@settings(max_examples=50)
def test_availability_component_instantiation(instance):
    assert isinstance(instance, Availability_Component)

@given(instance=Login_Component_strategy)
@settings(max_examples=50)
def test_login_component_instantiation(instance):
    assert isinstance(instance, Login_Component)

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_telno_setter(instance):
    original = instance.telno
    instance.telno = original
    assert instance.telno == original



@given(instance=Patient_strategy)
def test_patient_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=Patient_strategy)
def test_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Patient_strategy)
def test_patient_roomno_setter(instance):
    original = instance.roomno
    instance.roomno = original
    assert instance.roomno == original



@given(instance=Patient_strategy)
def test_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_patient_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Patient_strategy)
def test_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Admin_strategy)
def test_admin_doctorid_setter(instance):
    original = instance.doctorid
    instance.doctorid = original
    assert instance.doctorid == original



@given(instance=Admin_strategy)
def test_admin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Doctor_strategy)
def test_doctor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Doctor_strategy)
def test_doctor_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=Doctor_strategy)
def test_doctor_phno_setter(instance):
    original = instance.phno
    instance.phno = original
    assert instance.phno == original



@given(instance=Doctor_strategy)
def test_doctor_specialization_setter(instance):
    original = instance.specialization
    instance.specialization = original
    assert instance.specialization == original



@given(instance=Doctor_strategy)
def test_doctor_docid_setter(instance):
    original = instance.docid
    instance.docid = original
    assert instance.docid == original
