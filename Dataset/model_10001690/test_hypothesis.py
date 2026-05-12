import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Show_to_Doctor_external,
    Doctor_Actor,
    Patient_Actor,
    Admin_Office_Component,
    Doctor,
    prescription,
    Patient,
    Person,
    Check_Patient_external,
    Give_Prescription_external,
    Take_Appointment_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_show_to_doctor_external_is_not_abstract():
    assert not inspect.isabstract(Show_to_Doctor_external)


def test_show_to_doctor_external_constructor_exists():
    assert callable(Show_to_Doctor_external.__init__)


def test_show_to_doctor_external_constructor_args():
    sig = inspect.signature(Show_to_Doctor_external.__init__)
    params = list(sig.parameters.keys())



def test_doctor_actor_is_not_abstract():
    assert not inspect.isabstract(Doctor_Actor)


def test_doctor_actor_constructor_exists():
    assert callable(Doctor_Actor.__init__)


def test_doctor_actor_constructor_args():
    sig = inspect.signature(Doctor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_patient_actor_is_not_abstract():
    assert not inspect.isabstract(Patient_Actor)


def test_patient_actor_constructor_exists():
    assert callable(Patient_Actor.__init__)


def test_patient_actor_constructor_args():
    sig = inspect.signature(Patient_Actor.__init__)
    params = list(sig.parameters.keys())



def test_admin_office_component_is_not_abstract():
    assert not inspect.isabstract(Admin_Office_Component)


def test_admin_office_component_constructor_exists():
    assert callable(Admin_Office_Component.__init__)


def test_admin_office_component_constructor_args():
    sig = inspect.signature(Admin_Office_Component.__init__)
    params = list(sig.parameters.keys())



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Dept" in params, "Missing parameter 'Dept'"
    assert "Doctor_id" in params, "Missing parameter 'Doctor_id'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"

def test_doctor_has_Dept():
    assert hasattr(Doctor, "Dept")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Dept" in klass.__dict__:
            descriptor = klass.__dict__["Dept"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Doctor_id():
    assert hasattr(Doctor, "Doctor_id")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Doctor_id" in klass.__dict__:
            descriptor = klass.__dict__["Doctor_id"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Specialization():
    assert hasattr(Doctor, "Specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)



def test_prescription_is_not_abstract():
    assert not inspect.isabstract(prescription)


def test_prescription_constructor_exists():
    assert callable(prescription.__init__)


def test_prescription_constructor_args():
    sig = inspect.signature(prescription.__init__)
    params = list(sig.parameters.keys())



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Admit_date" in params, "Missing parameter 'Admit_date'"
    assert "Patient_id" in params, "Missing parameter 'Patient_id'"
    assert "Sickness" in params, "Missing parameter 'Sickness'"

def test_patient_has_Admit_date():
    assert hasattr(Patient, "Admit_date")
    descriptor = None
    for klass in Patient.__mro__:
        if "Admit_date" in klass.__dict__:
            descriptor = klass.__dict__["Admit_date"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Patient_id():
    assert hasattr(Patient, "Patient_id")
    descriptor = None
    for klass in Patient.__mro__:
        if "Patient_id" in klass.__dict__:
            descriptor = klass.__dict__["Patient_id"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Sickness():
    assert hasattr(Patient, "Sickness")
    descriptor = None
    for klass in Patient.__mro__:
        if "Sickness" in klass.__dict__:
            descriptor = klass.__dict__["Sickness"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Birth_date" in params, "Missing parameter 'Birth_date'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Phone_no" in params, "Missing parameter 'Phone_no'"
    assert "Name1" in params, "Missing parameter 'Name1'"
    assert "Gender" in params, "Missing parameter 'Gender'"

def test_person_has_Id():
    assert hasattr(Person, "Id")
    descriptor = None
    for klass in Person.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Name():
    assert hasattr(Person, "Name")
    descriptor = None
    for klass in Person.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Birth_date():
    assert hasattr(Person, "Birth_date")
    descriptor = None
    for klass in Person.__mro__:
        if "Birth_date" in klass.__dict__:
            descriptor = klass.__dict__["Birth_date"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Age():
    assert hasattr(Person, "Age")
    descriptor = None
    for klass in Person.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Phone_no():
    assert hasattr(Person, "Phone_no")
    descriptor = None
    for klass in Person.__mro__:
        if "Phone_no" in klass.__dict__:
            descriptor = klass.__dict__["Phone_no"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Name1():
    assert hasattr(Person, "Name1")
    descriptor = None
    for klass in Person.__mro__:
        if "Name1" in klass.__dict__:
            descriptor = klass.__dict__["Name1"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Gender():
    assert hasattr(Person, "Gender")
    descriptor = None
    for klass in Person.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)



def test_check_patient_external_is_not_abstract():
    assert not inspect.isabstract(Check_Patient_external)


def test_check_patient_external_constructor_exists():
    assert callable(Check_Patient_external.__init__)


def test_check_patient_external_constructor_args():
    sig = inspect.signature(Check_Patient_external.__init__)
    params = list(sig.parameters.keys())



def test_give_prescription_external_is_not_abstract():
    assert not inspect.isabstract(Give_Prescription_external)


def test_give_prescription_external_constructor_exists():
    assert callable(Give_Prescription_external.__init__)


def test_give_prescription_external_constructor_args():
    sig = inspect.signature(Give_Prescription_external.__init__)
    params = list(sig.parameters.keys())



def test_take_appointment_external_is_not_abstract():
    assert not inspect.isabstract(Take_Appointment_external)


def test_take_appointment_external_constructor_exists():
    assert callable(Take_Appointment_external.__init__)


def test_take_appointment_external_constructor_args():
    sig = inspect.signature(Take_Appointment_external.__init__)
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
Show_to_Doctor_external_strategy = st.builds(
    Show_to_Doctor_external,
)
Doctor_Actor_strategy = st.builds(
    Doctor_Actor,
)
Patient_Actor_strategy = st.builds(
    Patient_Actor,
)
Admin_Office_Component_strategy = st.builds(
    Admin_Office_Component,
)
Doctor_strategy = st.builds(
    Doctor,
    Dept=
        safe_text,
    Doctor_id=
        st.integers(),
    Specialization=
        safe_text
)
prescription_strategy = st.builds(
    prescription,
)
Patient_strategy = st.builds(
    Patient,
    Admit_date=
        safe_text,
    Patient_id=
        st.integers(),
    Sickness=
        safe_text
)
Person_strategy = st.builds(
    Person,
    Id=
        safe_text,
    Name=
        safe_text,
    Birth_date=
        safe_text,
    Age=
        st.integers(),
    Phone_no=
        safe_text,
    Name1=
        safe_text,
    Gender=
        safe_text
)
Check_Patient_external_strategy = st.builds(
    Check_Patient_external,
)
Give_Prescription_external_strategy = st.builds(
    Give_Prescription_external,
)
Take_Appointment_external_strategy = st.builds(
    Take_Appointment_external,
)

@given(instance=Show_to_Doctor_external_strategy)
@settings(max_examples=50)
def test_show_to_doctor_external_instantiation(instance):
    assert isinstance(instance, Show_to_Doctor_external)

@given(instance=Doctor_Actor_strategy)
@settings(max_examples=50)
def test_doctor_actor_instantiation(instance):
    assert isinstance(instance, Doctor_Actor)

@given(instance=Patient_Actor_strategy)
@settings(max_examples=50)
def test_patient_actor_instantiation(instance):
    assert isinstance(instance, Patient_Actor)

@given(instance=Admin_Office_Component_strategy)
@settings(max_examples=50)
def test_admin_office_component_instantiation(instance):
    assert isinstance(instance, Admin_Office_Component)

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Dept_setter(instance):
    original = instance.Dept
    instance.Dept = original
    assert instance.Dept == original



@given(instance=Doctor_strategy)
def test_doctor_Doctor_id_setter(instance):
    original = instance.Doctor_id
    instance.Doctor_id = original
    assert instance.Doctor_id == original



@given(instance=Doctor_strategy)
def test_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original

@given(instance=prescription_strategy)
@settings(max_examples=50)
def test_prescription_instantiation(instance):
    assert isinstance(instance, prescription)

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_Admit_date_setter(instance):
    original = instance.Admit_date
    instance.Admit_date = original
    assert instance.Admit_date == original



@given(instance=Patient_strategy)
def test_patient_Patient_id_setter(instance):
    original = instance.Patient_id
    instance.Patient_id = original
    assert instance.Patient_id == original



@given(instance=Patient_strategy)
def test_patient_Sickness_setter(instance):
    original = instance.Sickness
    instance.Sickness = original
    assert instance.Sickness == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Person_strategy)
def test_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Person_strategy)
def test_person_Birth_date_setter(instance):
    original = instance.Birth_date
    instance.Birth_date = original
    assert instance.Birth_date == original



@given(instance=Person_strategy)
def test_person_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Person_strategy)
def test_person_Phone_no_setter(instance):
    original = instance.Phone_no
    instance.Phone_no = original
    assert instance.Phone_no == original



@given(instance=Person_strategy)
def test_person_Name1_setter(instance):
    original = instance.Name1
    instance.Name1 = original
    assert instance.Name1 == original



@given(instance=Person_strategy)
def test_person_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original

@given(instance=Check_Patient_external_strategy)
@settings(max_examples=50)
def test_check_patient_external_instantiation(instance):
    assert isinstance(instance, Check_Patient_external)

@given(instance=Give_Prescription_external_strategy)
@settings(max_examples=50)
def test_give_prescription_external_instantiation(instance):
    assert isinstance(instance, Give_Prescription_external)

@given(instance=Take_Appointment_external_strategy)
@settings(max_examples=50)
def test_take_appointment_external_instantiation(instance):
    assert isinstance(instance, Take_Appointment_external)
