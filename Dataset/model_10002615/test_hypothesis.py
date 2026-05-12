import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pharmacy,
    lab,
    Bursar,
    medicine,
    Bill,
    Receptionist,
    Room,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pharmacy_is_not_abstract():
    assert not inspect.isabstract(pharmacy)


def test_pharmacy_constructor_exists():
    assert callable(pharmacy.__init__)


def test_pharmacy_constructor_args():
    sig = inspect.signature(pharmacy.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "medicine" in params, "Missing parameter 'medicine'"

def test_pharmacy_has_price():
    assert hasattr(pharmacy, "price")
    descriptor = None
    for klass in pharmacy.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_pharmacy_has_medicine():
    assert hasattr(pharmacy, "medicine")
    descriptor = None
    for klass in pharmacy.__mro__:
        if "medicine" in klass.__dict__:
            descriptor = klass.__dict__["medicine"]
            break
    assert isinstance(descriptor, property)



def test_lab_is_not_abstract():
    assert not inspect.isabstract(lab)


def test_lab_constructor_exists():
    assert callable(lab.__init__)


def test_lab_constructor_args():
    sig = inspect.signature(lab.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "results" in params, "Missing parameter 'results'"

def test_lab_has_price():
    assert hasattr(lab, "price")
    descriptor = None
    for klass in lab.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_lab_has_results():
    assert hasattr(lab, "results")
    descriptor = None
    for klass in lab.__mro__:
        if "results" in klass.__dict__:
            descriptor = klass.__dict__["results"]
            break
    assert isinstance(descriptor, property)



def test_bursar_is_not_abstract():
    assert not inspect.isabstract(Bursar)


def test_bursar_constructor_exists():
    assert callable(Bursar.__init__)


def test_bursar_constructor_args():
    sig = inspect.signature(Bursar.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_bursar_has_lastname():
    assert hasattr(Bursar, "lastname")
    descriptor = None
    for klass in Bursar.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_bursar_has_firstname():
    assert hasattr(Bursar, "firstname")
    descriptor = None
    for klass in Bursar.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_medicine_is_not_abstract():
    assert not inspect.isabstract(medicine)


def test_medicine_constructor_exists():
    assert callable(medicine.__init__)


def test_medicine_constructor_args():
    sig = inspect.signature(medicine.__init__)
    params = list(sig.parameters.keys())
    assert "medicine" in params, "Missing parameter 'medicine'"
    assert "price" in params, "Missing parameter 'price'"
    assert "id" in params, "Missing parameter 'id'"

def test_medicine_has_medicine():
    assert hasattr(medicine, "medicine")
    descriptor = None
    for klass in medicine.__mro__:
        if "medicine" in klass.__dict__:
            descriptor = klass.__dict__["medicine"]
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

def test_medicine_has_id():
    assert hasattr(medicine, "id")
    descriptor = None
    for klass in medicine.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "billno" in params, "Missing parameter 'billno'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_bill_has_billno():
    assert hasattr(Bill, "billno")
    descriptor = None
    for klass in Bill.__mro__:
        if "billno" in klass.__dict__:
            descriptor = klass.__dict__["billno"]
            break
    assert isinstance(descriptor, property)

def test_bill_has_amount():
    assert hasattr(Bill, "amount")
    descriptor = None
    for klass in Bill.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_receptionist_has_firstname():
    assert hasattr(Receptionist, "firstname")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_lastname():
    assert hasattr(Receptionist, "lastname")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "roomno" in params, "Missing parameter 'roomno'"
    assert "roomname" in params, "Missing parameter 'roomname'"

def test_room_has_roomno():
    assert hasattr(Room, "roomno")
    descriptor = None
    for klass in Room.__mro__:
        if "roomno" in klass.__dict__:
            descriptor = klass.__dict__["roomno"]
            break
    assert isinstance(descriptor, property)

def test_room_has_roomname():
    assert hasattr(Room, "roomname")
    descriptor = None
    for klass in Room.__mro__:
        if "roomname" in klass.__dict__:
            descriptor = klass.__dict__["roomname"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "sex" in params, "Missing parameter 'sex'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "id" in params, "Missing parameter 'id'"
    assert "blood_group" in params, "Missing parameter 'blood_group'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "phonenumber" in params, "Missing parameter 'phonenumber'"
    assert "email" in params, "Missing parameter 'email'"
    assert "birthyear" in params, "Missing parameter 'birthyear'"
    assert "addr" in params, "Missing parameter 'addr'"

def test_patient_has_sex():
    assert hasattr(Patient, "sex")
    descriptor = None
    for klass in Patient.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_lastname():
    assert hasattr(Patient, "lastname")
    descriptor = None
    for klass in Patient.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
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

def test_patient_has_blood_group():
    assert hasattr(Patient, "blood_group")
    descriptor = None
    for klass in Patient.__mro__:
        if "blood_group" in klass.__dict__:
            descriptor = klass.__dict__["blood_group"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_firstname():
    assert hasattr(Patient, "firstname")
    descriptor = None
    for klass in Patient.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_phonenumber():
    assert hasattr(Patient, "phonenumber")
    descriptor = None
    for klass in Patient.__mro__:
        if "phonenumber" in klass.__dict__:
            descriptor = klass.__dict__["phonenumber"]
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

def test_patient_has_birthyear():
    assert hasattr(Patient, "birthyear")
    descriptor = None
    for klass in Patient.__mro__:
        if "birthyear" in klass.__dict__:
            descriptor = klass.__dict__["birthyear"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_addr():
    assert hasattr(Patient, "addr")
    descriptor = None
    for klass in Patient.__mro__:
        if "addr" in klass.__dict__:
            descriptor = klass.__dict__["addr"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "dentist" in params, "Missing parameter 'dentist'"
    assert "normal_doctor" in params, "Missing parameter 'normal_doctor'"
    assert "women_doctor" in params, "Missing parameter 'women_doctor'"

def test_doctor_has_dentist():
    assert hasattr(Doctor, "dentist")
    descriptor = None
    for klass in Doctor.__mro__:
        if "dentist" in klass.__dict__:
            descriptor = klass.__dict__["dentist"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_normal_doctor():
    assert hasattr(Doctor, "normal_doctor")
    descriptor = None
    for klass in Doctor.__mro__:
        if "normal_doctor" in klass.__dict__:
            descriptor = klass.__dict__["normal_doctor"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_women_doctor():
    assert hasattr(Doctor, "women_doctor")
    descriptor = None
    for klass in Doctor.__mro__:
        if "women_doctor" in klass.__dict__:
            descriptor = klass.__dict__["women_doctor"]
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
pharmacy_strategy = st.builds(
    pharmacy,
    price=
        st.integers(),
    medicine=
        safe_text
)
lab_strategy = st.builds(
    lab,
    price=
        st.integers(),
    results=
        safe_text
)
Bursar_strategy = st.builds(
    Bursar,
    lastname=
        safe_text,
    firstname=
        safe_text
)
medicine_strategy = st.builds(
    medicine,
    medicine=
        safe_text,
    price=
        st.integers(),
    id=
        st.integers()
)
Bill_strategy = st.builds(
    Bill,
    billno=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Receptionist_strategy = st.builds(
    Receptionist,
    firstname=
        safe_text,
    lastname=
        safe_text
)
Room_strategy = st.builds(
    Room,
    roomno=
        st.integers(),
    roomname=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    sex=
        safe_text,
    lastname=
        safe_text,
    id=
        st.integers(),
    blood_group=
        st.integers(),
    firstname=
        safe_text,
    phonenumber=
        st.integers(),
    email=
        safe_text,
    birthyear=
        st.integers(),
    addr=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    dentist=
        st.none(),
    normal_doctor=
        st.none(),
    women_doctor=
        st.none()
)

@given(instance=pharmacy_strategy)
@settings(max_examples=50)
def test_pharmacy_instantiation(instance):
    assert isinstance(instance, pharmacy)



@given(instance=pharmacy_strategy)
def test_pharmacy_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=pharmacy_strategy)
def test_pharmacy_medicine_setter(instance):
    original = instance.medicine
    instance.medicine = original
    assert instance.medicine == original

@given(instance=lab_strategy)
@settings(max_examples=50)
def test_lab_instantiation(instance):
    assert isinstance(instance, lab)



@given(instance=lab_strategy)
def test_lab_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=lab_strategy)
def test_lab_results_setter(instance):
    original = instance.results
    instance.results = original
    assert instance.results == original

@given(instance=Bursar_strategy)
@settings(max_examples=50)
def test_bursar_instantiation(instance):
    assert isinstance(instance, Bursar)



@given(instance=Bursar_strategy)
def test_bursar_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Bursar_strategy)
def test_bursar_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=medicine_strategy)
@settings(max_examples=50)
def test_medicine_instantiation(instance):
    assert isinstance(instance, medicine)



@given(instance=medicine_strategy)
def test_medicine_medicine_setter(instance):
    original = instance.medicine
    instance.medicine = original
    assert instance.medicine == original



@given(instance=medicine_strategy)
def test_medicine_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=medicine_strategy)
def test_medicine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_billno_setter(instance):
    original = instance.billno
    instance.billno = original
    assert instance.billno == original



@given(instance=Bill_strategy)
def test_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Receptionist_strategy)
def test_receptionist_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_roomno_setter(instance):
    original = instance.roomno
    instance.roomno = original
    assert instance.roomno == original



@given(instance=Room_strategy)
def test_room_roomname_setter(instance):
    original = instance.roomname
    instance.roomname = original
    assert instance.roomname == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=Patient_strategy)
def test_patient_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Patient_strategy)
def test_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_patient_blood_group_setter(instance):
    original = instance.blood_group
    instance.blood_group = original
    assert instance.blood_group == original



@given(instance=Patient_strategy)
def test_patient_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Patient_strategy)
def test_patient_phonenumber_setter(instance):
    original = instance.phonenumber
    instance.phonenumber = original
    assert instance.phonenumber == original



@given(instance=Patient_strategy)
def test_patient_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Patient_strategy)
def test_patient_birthyear_setter(instance):
    original = instance.birthyear
    instance.birthyear = original
    assert instance.birthyear == original



@given(instance=Patient_strategy)
def test_patient_addr_setter(instance):
    original = instance.addr
    instance.addr = original
    assert instance.addr == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_dentist_setter(instance):
    original = instance.dentist
    instance.dentist = original
    assert instance.dentist == original



@given(instance=Doctor_strategy)
def test_doctor_normal_doctor_setter(instance):
    original = instance.normal_doctor
    instance.normal_doctor = original
    assert instance.normal_doctor == original



@given(instance=Doctor_strategy)
def test_doctor_women_doctor_setter(instance):
    original = instance.women_doctor
    instance.women_doctor = original
    assert instance.women_doctor == original
