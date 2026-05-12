import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    appointment,
    Room,
    Patient,
    Receptionist,
    It,
    nurse,
    doctor,
    employee,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_appointment_is_not_abstract():
    assert not inspect.isabstract(appointment)


def test_appointment_constructor_exists():
    assert callable(appointment.__init__)


def test_appointment_constructor_args():
    sig = inspect.signature(appointment.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "day" in params, "Missing parameter 'day'"
    assert "hour" in params, "Missing parameter 'hour'"

def test_appointment_has_duration():
    assert hasattr(appointment, "duration")
    descriptor = None
    for klass in appointment.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_minute():
    assert hasattr(appointment, "minute")
    descriptor = None
    for klass in appointment.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_day():
    assert hasattr(appointment, "day")
    descriptor = None
    for klass in appointment.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_hour():
    assert hasattr(appointment, "hour")
    descriptor = None
    for klass in appointment.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "available" in params, "Missing parameter 'available'"
    assert "capasittity" in params, "Missing parameter 'capasittity'"
    assert "num" in params, "Missing parameter 'num'"
    assert "room_type" in params, "Missing parameter 'room_type'"
    assert "patients" in params, "Missing parameter 'patients'"

def test_room_has_available():
    assert hasattr(Room, "available")
    descriptor = None
    for klass in Room.__mro__:
        if "available" in klass.__dict__:
            descriptor = klass.__dict__["available"]
            break
    assert isinstance(descriptor, property)

def test_room_has_capasittity():
    assert hasattr(Room, "capasittity")
    descriptor = None
    for klass in Room.__mro__:
        if "capasittity" in klass.__dict__:
            descriptor = klass.__dict__["capasittity"]
            break
    assert isinstance(descriptor, property)

def test_room_has_num():
    assert hasattr(Room, "num")
    descriptor = None
    for klass in Room.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_room_has_room_type():
    assert hasattr(Room, "room_type")
    descriptor = None
    for klass in Room.__mro__:
        if "room_type" in klass.__dict__:
            descriptor = klass.__dict__["room_type"]
            break
    assert isinstance(descriptor, property)

def test_room_has_patients():
    assert hasattr(Room, "patients")
    descriptor = None
    for klass in Room.__mro__:
        if "patients" in klass.__dict__:
            descriptor = klass.__dict__["patients"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "_doc" in params, "Missing parameter '_doc'"
    assert "id" in params, "Missing parameter 'id'"
    assert "_nur" in params, "Missing parameter '_nur'"
    assert "illness" in params, "Missing parameter 'illness'"

def test_patient_has__doc():
    assert hasattr(Patient, "_doc")
    descriptor = None
    for klass in Patient.__mro__:
        if "_doc" in klass.__dict__:
            descriptor = klass.__dict__["_doc"]
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

def test_patient_has__nur():
    assert hasattr(Patient, "_nur")
    descriptor = None
    for klass in Patient.__mro__:
        if "_nur" in klass.__dict__:
            descriptor = klass.__dict__["_nur"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_illness():
    assert hasattr(Patient, "illness")
    descriptor = None
    for klass in Patient.__mro__:
        if "illness" in klass.__dict__:
            descriptor = klass.__dict__["illness"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())



def test_it_is_not_abstract():
    assert not inspect.isabstract(It)


def test_it_constructor_exists():
    assert callable(It.__init__)


def test_it_constructor_args():
    sig = inspect.signature(It.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"

def test_it_has_password():
    assert hasattr(It, "password")
    descriptor = None
    for klass in It.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(nurse)


def test_nurse_constructor_exists():
    assert callable(nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(nurse.__init__)
    params = list(sig.parameters.keys())
    assert "_rom" in params, "Missing parameter '_rom'"

def test_nurse_has__rom():
    assert hasattr(nurse, "_rom")
    descriptor = None
    for klass in nurse.__mro__:
        if "_rom" in klass.__dict__:
            descriptor = klass.__dict__["_rom"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(doctor)


def test_doctor_constructor_exists():
    assert callable(doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(doctor.__init__)
    params = list(sig.parameters.keys())
    assert "weekappointment" in params, "Missing parameter 'weekappointment'"
    assert "patient" in params, "Missing parameter 'patient'"

def test_doctor_has_weekappointment():
    assert hasattr(doctor, "weekappointment")
    descriptor = None
    for klass in doctor.__mro__:
        if "weekappointment" in klass.__dict__:
            descriptor = klass.__dict__["weekappointment"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_patient():
    assert hasattr(doctor, "patient")
    descriptor = None
    for klass in doctor.__mro__:
        if "patient" in klass.__dict__:
            descriptor = klass.__dict__["patient"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(employee)


def test_employee_constructor_exists():
    assert callable(employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(employee.__init__)
    params = list(sig.parameters.keys())
    assert "department" in params, "Missing parameter 'department'"
    assert "Salary" in params, "Missing parameter 'Salary'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"

def test_employee_has_department():
    assert hasattr(employee, "department")
    descriptor = None
    for klass in employee.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Salary():
    assert hasattr(employee, "Salary")
    descriptor = None
    for klass in employee.__mro__:
        if "Salary" in klass.__dict__:
            descriptor = klass.__dict__["Salary"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_password():
    assert hasattr(employee, "password")
    descriptor = None
    for klass in employee.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_id():
    assert hasattr(employee, "id")
    descriptor = None
    for klass in employee.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"

def test_person_has_age():
    assert hasattr(Person, "age")
    descriptor = None
    for klass in Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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
appointment_strategy = st.builds(
    appointment,
    duration=
        st.integers(),
    minute=
        st.integers(),
    day=
        st.integers(),
    hour=
        st.integers()
)
Room_strategy = st.builds(
    Room,
    available=
        st.booleans(),
    capasittity=
        st.integers(),
    num=
        st.integers(),
    room_type=
        safe_text,
    patients=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    _doc=
        st.none(),
    id=
        safe_text,
    _nur=
        st.none(),
    illness=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
)
It_strategy = st.builds(
    It,
    password=
        safe_text
)
nurse_strategy = st.builds(
    nurse,
    _rom=
        st.none()
)
doctor_strategy = st.builds(
    doctor,
    weekappointment=
        safe_text,
    patient=
        safe_text
)
employee_strategy = st.builds(
    employee,
    department=
        safe_text,
    Salary=
        st.integers(),
    password=
        safe_text,
    id=
        safe_text
)
Person_strategy = st.builds(
    Person,
    age=
        st.integers(),
    name=
        safe_text
)

@given(instance=appointment_strategy)
@settings(max_examples=50)
def test_appointment_instantiation(instance):
    assert isinstance(instance, appointment)



@given(instance=appointment_strategy)
def test_appointment_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=appointment_strategy)
def test_appointment_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=appointment_strategy)
def test_appointment_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=appointment_strategy)
def test_appointment_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_available_setter(instance):
    original = instance.available
    instance.available = original
    assert instance.available == original



@given(instance=Room_strategy)
def test_room_capasittity_setter(instance):
    original = instance.capasittity
    instance.capasittity = original
    assert instance.capasittity == original



@given(instance=Room_strategy)
def test_room_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Room_strategy)
def test_room_room_type_setter(instance):
    original = instance.room_type
    instance.room_type = original
    assert instance.room_type == original



@given(instance=Room_strategy)
def test_room_patients_setter(instance):
    original = instance.patients
    instance.patients = original
    assert instance.patients == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient__doc_setter(instance):
    original = instance._doc
    instance._doc = original
    assert instance._doc == original



@given(instance=Patient_strategy)
def test_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_patient__nur_setter(instance):
    original = instance._nur
    instance._nur = original
    assert instance._nur == original



@given(instance=Patient_strategy)
def test_patient_illness_setter(instance):
    original = instance.illness
    instance.illness = original
    assert instance.illness == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)

@given(instance=It_strategy)
@settings(max_examples=50)
def test_it_instantiation(instance):
    assert isinstance(instance, It)



@given(instance=It_strategy)
def test_it_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, nurse)



@given(instance=nurse_strategy)
def test_nurse__rom_setter(instance):
    original = instance._rom
    instance._rom = original
    assert instance._rom == original

@given(instance=doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, doctor)



@given(instance=doctor_strategy)
def test_doctor_weekappointment_setter(instance):
    original = instance.weekappointment
    instance.weekappointment = original
    assert instance.weekappointment == original



@given(instance=doctor_strategy)
def test_doctor_patient_setter(instance):
    original = instance.patient
    instance.patient = original
    assert instance.patient == original

@given(instance=employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, employee)



@given(instance=employee_strategy)
def test_employee_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=employee_strategy)
def test_employee_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original



@given(instance=employee_strategy)
def test_employee_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=employee_strategy)
def test_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Person_strategy)
def test_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
