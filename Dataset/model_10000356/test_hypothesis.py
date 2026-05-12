import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Health_Records,
    Sickness,
    Appointment,
    Patient,
    Medicine,
    Technician,
    Doctor,
    Nurse,
    Staff,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_health_records_is_not_abstract():
    assert not inspect.isabstract(Health_Records)


def test_health_records_constructor_exists():
    assert callable(Health_Records.__init__)


def test_health_records_constructor_args():
    sig = inspect.signature(Health_Records.__init__)
    params = list(sig.parameters.keys())
    assert "healthhistory" in params, "Missing parameter 'healthhistory'"

def test_health_records_has_healthhistory():
    assert hasattr(Health_Records, "healthhistory")
    descriptor = None
    for klass in Health_Records.__mro__:
        if "healthhistory" in klass.__dict__:
            descriptor = klass.__dict__["healthhistory"]
            break
    assert isinstance(descriptor, property)



def test_sickness_is_not_abstract():
    assert not inspect.isabstract(Sickness)


def test_sickness_constructor_exists():
    assert callable(Sickness.__init__)


def test_sickness_constructor_args():
    sig = inspect.signature(Sickness.__init__)
    params = list(sig.parameters.keys())
    assert "recommendations" in params, "Missing parameter 'recommendations'"
    assert "symptoms" in params, "Missing parameter 'symptoms'"
    assert "prescription" in params, "Missing parameter 'prescription'"

def test_sickness_has_recommendations():
    assert hasattr(Sickness, "recommendations")
    descriptor = None
    for klass in Sickness.__mro__:
        if "recommendations" in klass.__dict__:
            descriptor = klass.__dict__["recommendations"]
            break
    assert isinstance(descriptor, property)

def test_sickness_has_symptoms():
    assert hasattr(Sickness, "symptoms")
    descriptor = None
    for klass in Sickness.__mro__:
        if "symptoms" in klass.__dict__:
            descriptor = klass.__dict__["symptoms"]
            break
    assert isinstance(descriptor, property)

def test_sickness_has_prescription():
    assert hasattr(Sickness, "prescription")
    descriptor = None
    for klass in Sickness.__mro__:
        if "prescription" in klass.__dict__:
            descriptor = klass.__dict__["prescription"]
            break
    assert isinstance(descriptor, property)



def test_appointment_is_not_abstract():
    assert not inspect.isabstract(Appointment)


def test_appointment_constructor_exists():
    assert callable(Appointment.__init__)


def test_appointment_constructor_args():
    sig = inspect.signature(Appointment.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "location" in params, "Missing parameter 'location'"
    assert "date" in params, "Missing parameter 'date'"

def test_appointment_has_time():
    assert hasattr(Appointment, "time")
    descriptor = None
    for klass in Appointment.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_location():
    assert hasattr(Appointment, "location")
    descriptor = None
    for klass in Appointment.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_date():
    assert hasattr(Appointment, "date")
    descriptor = None
    for klass in Appointment.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "healthrecords" in params, "Missing parameter 'healthrecords'"

def test_patient_has_name():
    assert hasattr(Patient, "name")
    descriptor = None
    for klass in Patient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_patient_has_healthrecords():
    assert hasattr(Patient, "healthrecords")
    descriptor = None
    for klass in Patient.__mro__:
        if "healthrecords" in klass.__dict__:
            descriptor = klass.__dict__["healthrecords"]
            break
    assert isinstance(descriptor, property)



def test_medicine_is_not_abstract():
    assert not inspect.isabstract(Medicine)


def test_medicine_constructor_exists():
    assert callable(Medicine.__init__)


def test_medicine_constructor_args():
    sig = inspect.signature(Medicine.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_medicine_has_code():
    assert hasattr(Medicine, "code")
    descriptor = None
    for klass in Medicine.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_price():
    assert hasattr(Medicine, "price")
    descriptor = None
    for klass in Medicine.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_name():
    assert hasattr(Medicine, "name")
    descriptor = None
    for klass in Medicine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_amount():
    assert hasattr(Medicine, "amount")
    descriptor = None
    for klass in Medicine.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_technician_is_not_abstract():
    assert not inspect.isabstract(Technician)


def test_technician_constructor_exists():
    assert callable(Technician.__init__)


def test_technician_constructor_args():
    sig = inspect.signature(Technician.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_technician_has_name():
    assert hasattr(Technician, "name")
    descriptor = None
    for klass in Technician.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_technician_has_id():
    assert hasattr(Technician, "id")
    descriptor = None
    for klass in Technician.__mro__:
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
    assert "id" in params, "Missing parameter 'id'"
    assert "speciality" in params, "Missing parameter 'speciality'"

def test_doctor_has_name():
    assert hasattr(Doctor, "name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_id():
    assert hasattr(Doctor, "id")
    descriptor = None
    for klass in Doctor.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_speciality():
    assert hasattr(Doctor, "speciality")
    descriptor = None
    for klass in Doctor.__mro__:
        if "speciality" in klass.__dict__:
            descriptor = klass.__dict__["speciality"]
            break
    assert isinstance(descriptor, property)



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_nurse_has_id():
    assert hasattr(Nurse, "id")
    descriptor = None
    for klass in Nurse.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_nurse_has_name():
    assert hasattr(Nurse, "name")
    descriptor = None
    for klass in Nurse.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "job" in params, "Missing parameter 'job'"

def test_staff_has_name():
    assert hasattr(Staff, "name")
    descriptor = None
    for klass in Staff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_job():
    assert hasattr(Staff, "job")
    descriptor = None
    for klass in Staff.__mro__:
        if "job" in klass.__dict__:
            descriptor = klass.__dict__["job"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "job" in params, "Missing parameter 'job'"

def test_person_has_id():
    assert hasattr(Person, "id")
    descriptor = None
    for klass in Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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

def test_person_has_name():
    assert hasattr(Person, "name")
    descriptor = None
    for klass in Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_job():
    assert hasattr(Person, "job")
    descriptor = None
    for klass in Person.__mro__:
        if "job" in klass.__dict__:
            descriptor = klass.__dict__["job"]
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
Health_Records_strategy = st.builds(
    Health_Records,
    healthhistory=
        safe_text
)
Sickness_strategy = st.builds(
    Sickness,
    recommendations=
        safe_text,
    symptoms=
        safe_text,
    prescription=
        safe_text
)
Appointment_strategy = st.builds(
    Appointment,
    time=
        st.integers(),
    location=
        safe_text,
    date=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    name=
        safe_text,
    id=
        st.integers(),
    healthrecords=
        safe_text
)
Medicine_strategy = st.builds(
    Medicine,
    code=
        st.integers(),
    price=
        safe_text,
    name=
        safe_text,
    amount=
        st.integers()
)
Technician_strategy = st.builds(
    Technician,
    name=
        safe_text,
    id=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    name=
        safe_text,
    id=
        st.integers(),
    speciality=
        safe_text
)
Nurse_strategy = st.builds(
    Nurse,
    id=
        st.integers(),
    name=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    name=
        safe_text,
    job=
        safe_text
)
Person_strategy = st.builds(
    Person,
    id=
        st.integers(),
    email=
        safe_text,
    name=
        safe_text,
    job=
        safe_text
)

@given(instance=Health_Records_strategy)
@settings(max_examples=50)
def test_health_records_instantiation(instance):
    assert isinstance(instance, Health_Records)



@given(instance=Health_Records_strategy)
def test_health_records_healthhistory_setter(instance):
    original = instance.healthhistory
    instance.healthhistory = original
    assert instance.healthhistory == original

@given(instance=Sickness_strategy)
@settings(max_examples=50)
def test_sickness_instantiation(instance):
    assert isinstance(instance, Sickness)



@given(instance=Sickness_strategy)
def test_sickness_recommendations_setter(instance):
    original = instance.recommendations
    instance.recommendations = original
    assert instance.recommendations == original



@given(instance=Sickness_strategy)
def test_sickness_symptoms_setter(instance):
    original = instance.symptoms
    instance.symptoms = original
    assert instance.symptoms == original



@given(instance=Sickness_strategy)
def test_sickness_prescription_setter(instance):
    original = instance.prescription
    instance.prescription = original
    assert instance.prescription == original

@given(instance=Appointment_strategy)
@settings(max_examples=50)
def test_appointment_instantiation(instance):
    assert isinstance(instance, Appointment)



@given(instance=Appointment_strategy)
def test_appointment_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Appointment_strategy)
def test_appointment_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Appointment_strategy)
def test_appointment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patient_strategy)
def test_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_patient_healthrecords_setter(instance):
    original = instance.healthrecords
    instance.healthrecords = original
    assert instance.healthrecords == original

@given(instance=Medicine_strategy)
@settings(max_examples=50)
def test_medicine_instantiation(instance):
    assert isinstance(instance, Medicine)



@given(instance=Medicine_strategy)
def test_medicine_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=Medicine_strategy)
def test_medicine_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Medicine_strategy)
def test_medicine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Medicine_strategy)
def test_medicine_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Technician_strategy)
@settings(max_examples=50)
def test_technician_instantiation(instance):
    assert isinstance(instance, Technician)



@given(instance=Technician_strategy)
def test_technician_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Technician_strategy)
def test_technician_id_setter(instance):
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
def test_doctor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Doctor_strategy)
def test_doctor_speciality_setter(instance):
    original = instance.speciality
    instance.speciality = original
    assert instance.speciality == original

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
def test_nurse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Staff_strategy)
def test_staff_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Person_strategy)
def test_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Person_strategy)
def test_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_person_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original
