import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    nurse,
    medicine,
    appointment,
    Bill,
    Receptionist,
    Room,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(nurse)


def test_nurse_constructor_exists():
    assert callable(nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(nurse.__init__)
    params = list(sig.parameters.keys())
    assert "contact" in params, "Missing parameter 'contact'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "availability" in params, "Missing parameter 'availability'"

def test_nurse_has_contact():
    assert hasattr(nurse, "contact")
    descriptor = None
    for klass in nurse.__mro__:
        if "contact" in klass.__dict__:
            descriptor = klass.__dict__["contact"]
            break
    assert isinstance(descriptor, property)

def test_nurse_has_name():
    assert hasattr(nurse, "name")
    descriptor = None
    for klass in nurse.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nurse_has_id():
    assert hasattr(nurse, "id")
    descriptor = None
    for klass in nurse.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_nurse_has_availability():
    assert hasattr(nurse, "availability")
    descriptor = None
    for klass in nurse.__mro__:
        if "availability" in klass.__dict__:
            descriptor = klass.__dict__["availability"]
            break
    assert isinstance(descriptor, property)



def test_medicine_is_not_abstract():
    assert not inspect.isabstract(medicine)


def test_medicine_constructor_exists():
    assert callable(medicine.__init__)


def test_medicine_constructor_args():
    sig = inspect.signature(medicine.__init__)
    params = list(sig.parameters.keys())
    assert "m_code" in params, "Missing parameter 'm_code'"
    assert "m_name" in params, "Missing parameter 'm_name'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "price" in params, "Missing parameter 'price'"

def test_medicine_has_m_code():
    assert hasattr(medicine, "m_code")
    descriptor = None
    for klass in medicine.__mro__:
        if "m_code" in klass.__dict__:
            descriptor = klass.__dict__["m_code"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_m_name():
    assert hasattr(medicine, "m_name")
    descriptor = None
    for klass in medicine.__mro__:
        if "m_name" in klass.__dict__:
            descriptor = klass.__dict__["m_name"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_quantity():
    assert hasattr(medicine, "quantity")
    descriptor = None
    for klass in medicine.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_price():
    assert hasattr(medicine, "price")
    descriptor = None
    for klass in medicine.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_appointment_is_not_abstract():
    assert not inspect.isabstract(appointment)


def test_appointment_constructor_exists():
    assert callable(appointment.__init__)


def test_appointment_constructor_args():
    sig = inspect.signature(appointment.__init__)
    params = list(sig.parameters.keys())
    assert "p_name" in params, "Missing parameter 'p_name'"
    assert "time" in params, "Missing parameter 'time'"
    assert "p_id" in params, "Missing parameter 'p_id'"
    assert "A_no" in params, "Missing parameter 'A_no'"
    assert "d_name" in params, "Missing parameter 'd_name'"

def test_appointment_has_p_name():
    assert hasattr(appointment, "p_name")
    descriptor = None
    for klass in appointment.__mro__:
        if "p_name" in klass.__dict__:
            descriptor = klass.__dict__["p_name"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_time():
    assert hasattr(appointment, "time")
    descriptor = None
    for klass in appointment.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_p_id():
    assert hasattr(appointment, "p_id")
    descriptor = None
    for klass in appointment.__mro__:
        if "p_id" in klass.__dict__:
            descriptor = klass.__dict__["p_id"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_A_no():
    assert hasattr(appointment, "A_no")
    descriptor = None
    for klass in appointment.__mro__:
        if "A_no" in klass.__dict__:
            descriptor = klass.__dict__["A_no"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_d_name():
    assert hasattr(appointment, "d_name")
    descriptor = None
    for klass in appointment.__mro__:
        if "d_name" in klass.__dict__:
            descriptor = klass.__dict__["d_name"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "patientname" in params, "Missing parameter 'patientname'"
    assert "billno" in params, "Missing parameter 'billno'"

def test_bill_has_amount():
    assert hasattr(Bill, "amount")
    descriptor = None
    for klass in Bill.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_patientname():
    assert hasattr(Bill, "patientname")
    descriptor = None
    for klass in Bill.__mro__:
        if "patientname" in klass.__dict__:
            descriptor = klass.__dict__["patientname"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_billno():
    assert hasattr(Bill, "billno")
    descriptor = None
    for klass in Bill.__mro__:
        if "billno" in klass.__dict__:
            descriptor = klass.__dict__["billno"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "id" in params, "Missing parameter 'id'"

def test_receptionist_has_email():
    assert hasattr(Receptionist, "email")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_password():
    assert hasattr(Receptionist, "password")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_username():
    assert hasattr(Receptionist, "username")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_id():
    assert hasattr(Receptionist, "id")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "roomtype" in params, "Missing parameter 'roomtype'"
    assert "roomno" in params, "Missing parameter 'roomno'"

def test_room_has_roomtype():
    assert hasattr(Room, "roomtype")
    descriptor = None
    for klass in Room.__mro__:
        if "roomtype" in klass.__dict__:
            descriptor = klass.__dict__["roomtype"]
            break
    assert isinstance(descriptor, property)

def test_room_has_roomno():
    assert hasattr(Room, "roomno")
    descriptor = None
    for klass in Room.__mro__:
        if "roomno" in klass.__dict__:
            descriptor = klass.__dict__["roomno"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "roomno" in params, "Missing parameter 'roomno'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "address" in params, "Missing parameter 'address'"
    assert "telno" in params, "Missing parameter 'telno'"
    assert "age" in params, "Missing parameter 'age'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_patient_has_roomno():
    assert hasattr(Patient, "roomno")
    descriptor = None
    for klass in Patient.__mro__:
        if "roomno" in klass.__dict__:
            descriptor = klass.__dict__["roomno"]
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

def test_patient_has_address():
    assert hasattr(Patient, "address")
    descriptor = None
    for klass in Patient.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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

def test_patient_has_age():
    assert hasattr(Patient, "age")
    descriptor = None
    for klass in Patient.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "docid" in params, "Missing parameter 'docid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "specialization" in params, "Missing parameter 'specialization'"
    assert "department" in params, "Missing parameter 'department'"
    assert "address" in params, "Missing parameter 'address'"
    assert "phno" in params, "Missing parameter 'phno'"

def test_doctor_has_docid():
    assert hasattr(Doctor, "docid")
    descriptor = None
    for klass in Doctor.__mro__:
        if "docid" in klass.__dict__:
            descriptor = klass.__dict__["docid"]
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

def test_doctor_has_specialization():
    assert hasattr(Doctor, "specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "specialization" in klass.__dict__:
            descriptor = klass.__dict__["specialization"]
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

def test_doctor_has_address():
    assert hasattr(Doctor, "address")
    descriptor = None
    for klass in Doctor.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
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
nurse_strategy = st.builds(
    nurse,
    contact=
        st.integers(),
    name=
        safe_text,
    id=
        st.integers(),
    availability=
        st.booleans()
)
medicine_strategy = st.builds(
    medicine,
    m_code=
        st.integers(),
    m_name=
        safe_text,
    quantity=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
appointment_strategy = st.builds(
    appointment,
    p_name=
        safe_text,
    time=
        st.dates(),
    p_id=
        st.integers(),
    A_no=
        st.integers(),
    d_name=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    patientname=
        safe_text,
    billno=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    email=
        safe_text,
    password=
        safe_text,
    username=
        safe_text,
    id=
        st.integers()
)
Room_strategy = st.builds(
    Room,
    roomtype=
        safe_text,
    roomno=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    roomno=
        st.integers(),
    sex=
        safe_text,
    address=
        safe_text,
    telno=
        st.integers(),
    age=
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
    name=
        safe_text,
    specialization=
        safe_text,
    department=
        safe_text,
    address=
        safe_text,
    phno=
        st.integers()
)

@given(instance=nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, nurse)



@given(instance=nurse_strategy)
def test_nurse_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=nurse_strategy)
def test_nurse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=nurse_strategy)
def test_nurse_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=nurse_strategy)
def test_nurse_availability_setter(instance):
    original = instance.availability
    instance.availability = original
    assert instance.availability == original

@given(instance=medicine_strategy)
@settings(max_examples=50)
def test_medicine_instantiation(instance):
    assert isinstance(instance, medicine)



@given(instance=medicine_strategy)
def test_medicine_m_code_setter(instance):
    original = instance.m_code
    instance.m_code = original
    assert instance.m_code == original



@given(instance=medicine_strategy)
def test_medicine_m_name_setter(instance):
    original = instance.m_name
    instance.m_name = original
    assert instance.m_name == original



@given(instance=medicine_strategy)
def test_medicine_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=medicine_strategy)
def test_medicine_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=appointment_strategy)
@settings(max_examples=50)
def test_appointment_instantiation(instance):
    assert isinstance(instance, appointment)



@given(instance=appointment_strategy)
def test_appointment_p_name_setter(instance):
    original = instance.p_name
    instance.p_name = original
    assert instance.p_name == original



@given(instance=appointment_strategy)
def test_appointment_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=appointment_strategy)
def test_appointment_p_id_setter(instance):
    original = instance.p_id
    instance.p_id = original
    assert instance.p_id == original



@given(instance=appointment_strategy)
def test_appointment_A_no_setter(instance):
    original = instance.A_no
    instance.A_no = original
    assert instance.A_no == original



@given(instance=appointment_strategy)
def test_appointment_d_name_setter(instance):
    original = instance.d_name
    instance.d_name = original
    assert instance.d_name == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Bill_strategy)
def test_bill_patientname_setter(instance):
    original = instance.patientname
    instance.patientname = original
    assert instance.patientname == original



@given(instance=Bill_strategy)
def test_bill_billno_setter(instance):
    original = instance.billno
    instance.billno = original
    assert instance.billno == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Receptionist_strategy)
def test_receptionist_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Receptionist_strategy)
def test_receptionist_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Receptionist_strategy)
def test_receptionist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_roomtype_setter(instance):
    original = instance.roomtype
    instance.roomtype = original
    assert instance.roomtype == original



@given(instance=Room_strategy)
def test_room_roomno_setter(instance):
    original = instance.roomno
    instance.roomno = original
    assert instance.roomno == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_roomno_setter(instance):
    original = instance.roomno
    instance.roomno = original
    assert instance.roomno == original



@given(instance=Patient_strategy)
def test_patient_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=Patient_strategy)
def test_patient_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Patient_strategy)
def test_patient_telno_setter(instance):
    original = instance.telno
    instance.telno = original
    assert instance.telno == original



@given(instance=Patient_strategy)
def test_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



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
def test_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Doctor_strategy)
def test_doctor_specialization_setter(instance):
    original = instance.specialization
    instance.specialization = original
    assert instance.specialization == original



@given(instance=Doctor_strategy)
def test_doctor_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=Doctor_strategy)
def test_doctor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Doctor_strategy)
def test_doctor_phno_setter(instance):
    original = instance.phno
    instance.phno = original
    assert instance.phno == original
