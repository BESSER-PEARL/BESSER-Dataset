import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MainWindow,
    appointment,
    Room,
    Patient,
    It,
    nurse,
    doctor,
    employee,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mainwindow_is_not_abstract():
    assert not inspect.isabstract(MainWindow)


def test_mainwindow_constructor_exists():
    assert callable(MainWindow.__init__)


def test_mainwindow_constructor_args():
    sig = inspect.signature(MainWindow.__init__)
    params = list(sig.parameters.keys())
    assert "patientss" in params, "Missing parameter 'patientss'"
    assert "roomss" in params, "Missing parameter 'roomss'"
    assert "UI" in params, "Missing parameter 'UI'"
    assert "nursess" in params, "Missing parameter 'nursess'"
    assert "_logininit" in params, "Missing parameter '_logininit'"
    assert "doctorss" in params, "Missing parameter 'doctorss'"
    assert "itss" in params, "Missing parameter 'itss'"
    assert "_logicdoc" in params, "Missing parameter '_logicdoc'"
    assert "_Loginnurs" in params, "Missing parameter '_Loginnurs'"

def test_mainwindow_has_patientss():
    assert hasattr(MainWindow, "patientss")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "patientss" in klass.__dict__:
            descriptor = klass.__dict__["patientss"]
            break
    assert isinstance(descriptor, property)

def test_mainwindow_has_roomss():
    assert hasattr(MainWindow, "roomss")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "roomss" in klass.__dict__:
            descriptor = klass.__dict__["roomss"]
            break
    assert isinstance(descriptor, property)

def test_mainwindow_has_UI():
    assert hasattr(MainWindow, "UI")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "UI" in klass.__dict__:
            descriptor = klass.__dict__["UI"]
            break
    assert isinstance(descriptor, property)

def test_mainwindow_has_nursess():
    assert hasattr(MainWindow, "nursess")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "nursess" in klass.__dict__:
            descriptor = klass.__dict__["nursess"]
            break
    assert isinstance(descriptor, property)

def test_mainwindow_has__logininit():
    assert hasattr(MainWindow, "_logininit")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "_logininit" in klass.__dict__:
            descriptor = klass.__dict__["_logininit"]
            break
    assert isinstance(descriptor, property)

def test_mainwindow_has_doctorss():
    assert hasattr(MainWindow, "doctorss")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "doctorss" in klass.__dict__:
            descriptor = klass.__dict__["doctorss"]
            break
    assert isinstance(descriptor, property)

def test_mainwindow_has_itss():
    assert hasattr(MainWindow, "itss")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "itss" in klass.__dict__:
            descriptor = klass.__dict__["itss"]
            break
    assert isinstance(descriptor, property)

def test_mainwindow_has__logicdoc():
    assert hasattr(MainWindow, "_logicdoc")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "_logicdoc" in klass.__dict__:
            descriptor = klass.__dict__["_logicdoc"]
            break
    assert isinstance(descriptor, property)

def test_mainwindow_has__Loginnurs():
    assert hasattr(MainWindow, "_Loginnurs")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "_Loginnurs" in klass.__dict__:
            descriptor = klass.__dict__["_Loginnurs"]
            break
    assert isinstance(descriptor, property)



def test_appointment_is_not_abstract():
    assert not inspect.isabstract(appointment)


def test_appointment_constructor_exists():
    assert callable(appointment.__init__)


def test_appointment_constructor_args():
    sig = inspect.signature(appointment.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "title" in params, "Missing parameter 'title'"

def test_appointment_has_day():
    assert hasattr(appointment, "day")
    descriptor = None
    for klass in appointment.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

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

def test_appointment_has_hour():
    assert hasattr(appointment, "hour")
    descriptor = None
    for klass in appointment.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_title():
    assert hasattr(appointment, "title")
    descriptor = None
    for klass in appointment.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "capasittity" in params, "Missing parameter 'capasittity'"
    assert "available" in params, "Missing parameter 'available'"
    assert "room_type" in params, "Missing parameter 'room_type'"
    assert "num" in params, "Missing parameter 'num'"
    assert "_nurs" in params, "Missing parameter '_nurs'"
    assert "patients" in params, "Missing parameter 'patients'"

def test_room_has_capasittity():
    assert hasattr(Room, "capasittity")
    descriptor = None
    for klass in Room.__mro__:
        if "capasittity" in klass.__dict__:
            descriptor = klass.__dict__["capasittity"]
            break
    assert isinstance(descriptor, property)

def test_room_has_available():
    assert hasattr(Room, "available")
    descriptor = None
    for klass in Room.__mro__:
        if "available" in klass.__dict__:
            descriptor = klass.__dict__["available"]
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

def test_room_has_num():
    assert hasattr(Room, "num")
    descriptor = None
    for klass in Room.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_room_has__nurs():
    assert hasattr(Room, "_nurs")
    descriptor = None
    for klass in Room.__mro__:
        if "_nurs" in klass.__dict__:
            descriptor = klass.__dict__["_nurs"]
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
    assert "hasdoc" in params, "Missing parameter 'hasdoc'"
    assert "disease" in params, "Missing parameter 'disease'"
    assert "hasroom" in params, "Missing parameter 'hasroom'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "room" in params, "Missing parameter 'room'"

def test_patient_has_hasdoc():
    assert hasattr(Patient, "hasdoc")
    descriptor = None
    for klass in Patient.__mro__:
        if "hasdoc" in klass.__dict__:
            descriptor = klass.__dict__["hasdoc"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_disease():
    assert hasattr(Patient, "disease")
    descriptor = None
    for klass in Patient.__mro__:
        if "disease" in klass.__dict__:
            descriptor = klass.__dict__["disease"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_hasroom():
    assert hasattr(Patient, "hasroom")
    descriptor = None
    for klass in Patient.__mro__:
        if "hasroom" in klass.__dict__:
            descriptor = klass.__dict__["hasroom"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_duration():
    assert hasattr(Patient, "duration")
    descriptor = None
    for klass in Patient.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_room():
    assert hasattr(Patient, "room")
    descriptor = None
    for klass in Patient.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)



def test_it_is_not_abstract():
    assert not inspect.isabstract(It)


def test_it_constructor_exists():
    assert callable(It.__init__)


def test_it_constructor_args():
    sig = inspect.signature(It.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"

def test_it_has_name():
    assert hasattr(It, "name")
    descriptor = None
    for klass in It.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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
    assert "password" in params, "Missing parameter 'password'"

def test_employee_has_department():
    assert hasattr(employee, "department")
    descriptor = None
    for klass in employee.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
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



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_person_has_name():
    assert hasattr(Person, "name")
    descriptor = None
    for klass in Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_age():
    assert hasattr(Person, "age")
    descriptor = None
    for klass in Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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
MainWindow_strategy = st.builds(
    MainWindow,
    patientss=
        safe_text,
    roomss=
        safe_text,
    UI=
        safe_text,
    nursess=
        safe_text,
    _logininit=
        st.none(),
    doctorss=
        safe_text,
    itss=
        safe_text,
    _logicdoc=
        st.none(),
    _Loginnurs=
        st.none()
)
appointment_strategy = st.builds(
    appointment,
    day=
        st.integers(),
    duration=
        st.integers(),
    minute=
        st.integers(),
    hour=
        st.integers(),
    title=
        safe_text
)
Room_strategy = st.builds(
    Room,
    capasittity=
        st.integers(),
    available=
        st.booleans(),
    room_type=
        safe_text,
    num=
        st.integers(),
    _nurs=
        st.none(),
    patients=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    hasdoc=
        st.booleans(),
    disease=
        safe_text,
    hasroom=
        st.booleans(),
    duration=
        st.integers(),
    room=
        st.integers()
)
It_strategy = st.builds(
    It,
    name=
        safe_text,
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
    password=
        safe_text
)
Person_strategy = st.builds(
    Person,
    name=
        safe_text,
    age=
        st.integers()
)

@given(instance=MainWindow_strategy)
@settings(max_examples=50)
def test_mainwindow_instantiation(instance):
    assert isinstance(instance, MainWindow)



@given(instance=MainWindow_strategy)
def test_mainwindow_patientss_setter(instance):
    original = instance.patientss
    instance.patientss = original
    assert instance.patientss == original



@given(instance=MainWindow_strategy)
def test_mainwindow_roomss_setter(instance):
    original = instance.roomss
    instance.roomss = original
    assert instance.roomss == original



@given(instance=MainWindow_strategy)
def test_mainwindow_UI_setter(instance):
    original = instance.UI
    instance.UI = original
    assert instance.UI == original



@given(instance=MainWindow_strategy)
def test_mainwindow_nursess_setter(instance):
    original = instance.nursess
    instance.nursess = original
    assert instance.nursess == original



@given(instance=MainWindow_strategy)
def test_mainwindow__logininit_setter(instance):
    original = instance._logininit
    instance._logininit = original
    assert instance._logininit == original



@given(instance=MainWindow_strategy)
def test_mainwindow_doctorss_setter(instance):
    original = instance.doctorss
    instance.doctorss = original
    assert instance.doctorss == original



@given(instance=MainWindow_strategy)
def test_mainwindow_itss_setter(instance):
    original = instance.itss
    instance.itss = original
    assert instance.itss == original



@given(instance=MainWindow_strategy)
def test_mainwindow__logicdoc_setter(instance):
    original = instance._logicdoc
    instance._logicdoc = original
    assert instance._logicdoc == original



@given(instance=MainWindow_strategy)
def test_mainwindow__Loginnurs_setter(instance):
    original = instance._Loginnurs
    instance._Loginnurs = original
    assert instance._Loginnurs == original

@given(instance=appointment_strategy)
@settings(max_examples=50)
def test_appointment_instantiation(instance):
    assert isinstance(instance, appointment)



@given(instance=appointment_strategy)
def test_appointment_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



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
def test_appointment_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=appointment_strategy)
def test_appointment_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_capasittity_setter(instance):
    original = instance.capasittity
    instance.capasittity = original
    assert instance.capasittity == original



@given(instance=Room_strategy)
def test_room_available_setter(instance):
    original = instance.available
    instance.available = original
    assert instance.available == original



@given(instance=Room_strategy)
def test_room_room_type_setter(instance):
    original = instance.room_type
    instance.room_type = original
    assert instance.room_type == original



@given(instance=Room_strategy)
def test_room_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Room_strategy)
def test_room__nurs_setter(instance):
    original = instance._nurs
    instance._nurs = original
    assert instance._nurs == original



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
def test_patient_hasdoc_setter(instance):
    original = instance.hasdoc
    instance.hasdoc = original
    assert instance.hasdoc == original



@given(instance=Patient_strategy)
def test_patient_disease_setter(instance):
    original = instance.disease
    instance.disease = original
    assert instance.disease == original



@given(instance=Patient_strategy)
def test_patient_hasroom_setter(instance):
    original = instance.hasroom
    instance.hasroom = original
    assert instance.hasroom == original



@given(instance=Patient_strategy)
def test_patient_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=Patient_strategy)
def test_patient_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original

@given(instance=It_strategy)
@settings(max_examples=50)
def test_it_instantiation(instance):
    assert isinstance(instance, It)



@given(instance=It_strategy)
def test_it_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



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
def test_employee_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original
