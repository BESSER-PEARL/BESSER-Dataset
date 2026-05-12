import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    private,
    general,
    login,
    loan,
    Bill,
    test,
    room,
    receptionist,
    doctor,
    patient,
    staff,
    department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_private_is_not_abstract():
    assert not inspect.isabstract(private)


def test_private_constructor_exists():
    assert callable(private.__init__)


def test_private_constructor_args():
    sig = inspect.signature(private.__init__)
    params = list(sig.parameters.keys())



def test_general_is_not_abstract():
    assert not inspect.isabstract(general)


def test_general_constructor_exists():
    assert callable(general.__init__)


def test_general_constructor_args():
    sig = inspect.signature(general.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(login)


def test_login_constructor_exists():
    assert callable(login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(login.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pass" in params, "Missing parameter 'pass'"
    assert "id" in params, "Missing parameter 'id'"

def test_login_has_name():
    assert hasattr(login, "name")
    descriptor = None
    for klass in login.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_login_has_pass():
    assert hasattr(login, "pass")
    descriptor = None
    for klass in login.__mro__:
        if "pass" in klass.__dict__:
            descriptor = klass.__dict__["pass"]
            break
    assert isinstance(descriptor, property)

def test_login_has_id():
    assert hasattr(login, "id")
    descriptor = None
    for klass in login.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_loan_is_not_abstract():
    assert not inspect.isabstract(loan)


def test_loan_constructor_exists():
    assert callable(loan.__init__)


def test_loan_constructor_args():
    sig = inspect.signature(loan.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "patient_name" in params, "Missing parameter 'patient_name'"

def test_loan_has_amount():
    assert hasattr(loan, "amount")
    descriptor = None
    for klass in loan.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_loan_has_patient_name():
    assert hasattr(loan, "patient_name")
    descriptor = None
    for klass in loan.__mro__:
        if "patient_name" in klass.__dict__:
            descriptor = klass.__dict__["patient_name"]
            break
    assert isinstance(descriptor, property)



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "patient_name" in params, "Missing parameter 'patient_name'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "bill_no" in params, "Missing parameter 'bill_no'"

def test_bill_has_patient_name():
    assert hasattr(Bill, "patient_name")
    descriptor = None
    for klass in Bill.__mro__:
        if "patient_name" in klass.__dict__:
            descriptor = klass.__dict__["patient_name"]
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

def test_bill_has_bill_no():
    assert hasattr(Bill, "bill_no")
    descriptor = None
    for klass in Bill.__mro__:
        if "bill_no" in klass.__dict__:
            descriptor = klass.__dict__["bill_no"]
            break
    assert isinstance(descriptor, property)



def test_test_is_not_abstract():
    assert not inspect.isabstract(test)


def test_test_constructor_exists():
    assert callable(test.__init__)


def test_test_constructor_args():
    sig = inspect.signature(test.__init__)
    params = list(sig.parameters.keys())
    assert "disease_name" in params, "Missing parameter 'disease_name'"

def test_test_has_disease_name():
    assert hasattr(test, "disease_name")
    descriptor = None
    for klass in test.__mro__:
        if "disease_name" in klass.__dict__:
            descriptor = klass.__dict__["disease_name"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(room)


def test_room_constructor_exists():
    assert callable(room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(room.__init__)
    params = list(sig.parameters.keys())
    assert "room_no" in params, "Missing parameter 'room_no'"

def test_room_has_room_no():
    assert hasattr(room, "room_no")
    descriptor = None
    for klass in room.__mro__:
        if "room_no" in klass.__dict__:
            descriptor = klass.__dict__["room_no"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(receptionist)


def test_receptionist_constructor_exists():
    assert callable(receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "rid" in params, "Missing parameter 'rid'"
    assert "name" in params, "Missing parameter 'name'"

def test_receptionist_has_rid():
    assert hasattr(receptionist, "rid")
    descriptor = None
    for klass in receptionist.__mro__:
        if "rid" in klass.__dict__:
            descriptor = klass.__dict__["rid"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_name():
    assert hasattr(receptionist, "name")
    descriptor = None
    for klass in receptionist.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(doctor)


def test_doctor_constructor_exists():
    assert callable(doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(doctor.__init__)
    params = list(sig.parameters.keys())
    assert "did" in params, "Missing parameter 'did'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dept" in params, "Missing parameter 'dept'"
    assert "phone_no" in params, "Missing parameter 'phone_no'"
    assert "specilization" in params, "Missing parameter 'specilization'"

def test_doctor_has_did():
    assert hasattr(doctor, "did")
    descriptor = None
    for klass in doctor.__mro__:
        if "did" in klass.__dict__:
            descriptor = klass.__dict__["did"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_name():
    assert hasattr(doctor, "name")
    descriptor = None
    for klass in doctor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_dept():
    assert hasattr(doctor, "dept")
    descriptor = None
    for klass in doctor.__mro__:
        if "dept" in klass.__dict__:
            descriptor = klass.__dict__["dept"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_phone_no():
    assert hasattr(doctor, "phone_no")
    descriptor = None
    for klass in doctor.__mro__:
        if "phone_no" in klass.__dict__:
            descriptor = klass.__dict__["phone_no"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_specilization():
    assert hasattr(doctor, "specilization")
    descriptor = None
    for klass in doctor.__mro__:
        if "specilization" in klass.__dict__:
            descriptor = klass.__dict__["specilization"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(patient)


def test_patient_constructor_exists():
    assert callable(patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(patient.__init__)
    params = list(sig.parameters.keys())
    assert "pid" in params, "Missing parameter 'pid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "room_no" in params, "Missing parameter 'room_no'"
    assert "phone_no" in params, "Missing parameter 'phone_no'"
    assert "address" in params, "Missing parameter 'address'"
    assert "age" in params, "Missing parameter 'age'"

def test_patient_has_pid():
    assert hasattr(patient, "pid")
    descriptor = None
    for klass in patient.__mro__:
        if "pid" in klass.__dict__:
            descriptor = klass.__dict__["pid"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_name():
    assert hasattr(patient, "name")
    descriptor = None
    for klass in patient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_room_no():
    assert hasattr(patient, "room_no")
    descriptor = None
    for klass in patient.__mro__:
        if "room_no" in klass.__dict__:
            descriptor = klass.__dict__["room_no"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_phone_no():
    assert hasattr(patient, "phone_no")
    descriptor = None
    for klass in patient.__mro__:
        if "phone_no" in klass.__dict__:
            descriptor = klass.__dict__["phone_no"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_address():
    assert hasattr(patient, "address")
    descriptor = None
    for klass in patient.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_age():
    assert hasattr(patient, "age")
    descriptor = None
    for klass in patient.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(staff)


def test_staff_constructor_exists():
    assert callable(staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(staff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_staff_has_name():
    assert hasattr(staff, "name")
    descriptor = None
    for klass in staff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_department_is_not_abstract():
    assert not inspect.isabstract(department)


def test_department_constructor_exists():
    assert callable(department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(department.__init__)
    params = list(sig.parameters.keys())
    assert "loacation" in params, "Missing parameter 'loacation'"
    assert "depart_id" in params, "Missing parameter 'depart_id'"

def test_department_has_loacation():
    assert hasattr(department, "loacation")
    descriptor = None
    for klass in department.__mro__:
        if "loacation" in klass.__dict__:
            descriptor = klass.__dict__["loacation"]
            break
    assert isinstance(descriptor, property)

def test_department_has_depart_id():
    assert hasattr(department, "depart_id")
    descriptor = None
    for klass in department.__mro__:
        if "depart_id" in klass.__dict__:
            descriptor = klass.__dict__["depart_id"]
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
private_strategy = st.builds(
    private,
)
general_strategy = st.builds(
    general,
)
login_strategy = st.builds(
    login,
    name=
        safe_text,
    pass=
        safe_text,
    id=
        safe_text
)
loan_strategy = st.builds(
    loan,
    amount=
        safe_text,
    patient_name=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    patient_name=
        safe_text,
    amount=
        safe_text,
    bill_no=
        safe_text
)
test_strategy = st.builds(
    test,
    disease_name=
        safe_text
)
room_strategy = st.builds(
    room,
    room_no=
        safe_text
)
receptionist_strategy = st.builds(
    receptionist,
    rid=
        safe_text,
    name=
        safe_text
)
doctor_strategy = st.builds(
    doctor,
    did=
        safe_text,
    name=
        safe_text,
    dept=
        safe_text,
    phone_no=
        safe_text,
    specilization=
        safe_text
)
patient_strategy = st.builds(
    patient,
    pid=
        safe_text,
    name=
        safe_text,
    room_no=
        safe_text,
    phone_no=
        safe_text,
    address=
        safe_text,
    age=
        safe_text
)
staff_strategy = st.builds(
    staff,
    name=
        safe_text
)
department_strategy = st.builds(
    department,
    loacation=
        safe_text,
    depart_id=
        safe_text
)

@given(instance=private_strategy)
@settings(max_examples=50)
def test_private_instantiation(instance):
    assert isinstance(instance, private)

@given(instance=general_strategy)
@settings(max_examples=50)
def test_general_instantiation(instance):
    assert isinstance(instance, general)

@given(instance=login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, login)



@given(instance=login_strategy)
def test_login_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=login_strategy)
def test_login_pass_setter(instance):
    original = instance.pass
    instance.pass = original
    assert instance.pass == original



@given(instance=login_strategy)
def test_login_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=loan_strategy)
@settings(max_examples=50)
def test_loan_instantiation(instance):
    assert isinstance(instance, loan)



@given(instance=loan_strategy)
def test_loan_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=loan_strategy)
def test_loan_patient_name_setter(instance):
    original = instance.patient_name
    instance.patient_name = original
    assert instance.patient_name == original

@given(instance=Bill_strategy)
@settings(max_examples=50)
def test_bill_instantiation(instance):
    assert isinstance(instance, Bill)



@given(instance=Bill_strategy)
def test_bill_patient_name_setter(instance):
    original = instance.patient_name
    instance.patient_name = original
    assert instance.patient_name == original



@given(instance=Bill_strategy)
def test_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Bill_strategy)
def test_bill_bill_no_setter(instance):
    original = instance.bill_no
    instance.bill_no = original
    assert instance.bill_no == original

@given(instance=test_strategy)
@settings(max_examples=50)
def test_test_instantiation(instance):
    assert isinstance(instance, test)



@given(instance=test_strategy)
def test_test_disease_name_setter(instance):
    original = instance.disease_name
    instance.disease_name = original
    assert instance.disease_name == original

@given(instance=room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, room)



@given(instance=room_strategy)
def test_room_room_no_setter(instance):
    original = instance.room_no
    instance.room_no = original
    assert instance.room_no == original

@given(instance=receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, receptionist)



@given(instance=receptionist_strategy)
def test_receptionist_rid_setter(instance):
    original = instance.rid
    instance.rid = original
    assert instance.rid == original



@given(instance=receptionist_strategy)
def test_receptionist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, doctor)



@given(instance=doctor_strategy)
def test_doctor_did_setter(instance):
    original = instance.did
    instance.did = original
    assert instance.did == original



@given(instance=doctor_strategy)
def test_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=doctor_strategy)
def test_doctor_dept_setter(instance):
    original = instance.dept
    instance.dept = original
    assert instance.dept == original



@given(instance=doctor_strategy)
def test_doctor_phone_no_setter(instance):
    original = instance.phone_no
    instance.phone_no = original
    assert instance.phone_no == original



@given(instance=doctor_strategy)
def test_doctor_specilization_setter(instance):
    original = instance.specilization
    instance.specilization = original
    assert instance.specilization == original

@given(instance=patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, patient)



@given(instance=patient_strategy)
def test_patient_pid_setter(instance):
    original = instance.pid
    instance.pid = original
    assert instance.pid == original



@given(instance=patient_strategy)
def test_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=patient_strategy)
def test_patient_room_no_setter(instance):
    original = instance.room_no
    instance.room_no = original
    assert instance.room_no == original



@given(instance=patient_strategy)
def test_patient_phone_no_setter(instance):
    original = instance.phone_no
    instance.phone_no = original
    assert instance.phone_no == original



@given(instance=patient_strategy)
def test_patient_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=patient_strategy)
def test_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, staff)



@given(instance=staff_strategy)
def test_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, department)



@given(instance=department_strategy)
def test_department_loacation_setter(instance):
    original = instance.loacation
    instance.loacation = original
    assert instance.loacation == original



@given(instance=department_strategy)
def test_department_depart_id_setter(instance):
    original = instance.depart_id
    instance.depart_id = original
    assert instance.depart_id == original
