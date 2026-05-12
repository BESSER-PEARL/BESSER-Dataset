import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Hospital,
    RFID_Reader,
    Staff,
    Room,
    Patient,
    Nurse,
    Doctor,
    Technical_staff,
    Administrative_staff,
    Operations_staff,
    Department,
    Nurse1,
    Staff1,
    Bill,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_hospital_has_phone():
    assert hasattr(Hospital, "phone")
    descriptor = None
    for klass in Hospital.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_name():
    assert hasattr(Hospital, "name")
    descriptor = None
    for klass in Hospital.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hospital_has_address():
    assert hasattr(Hospital, "address")
    descriptor = None
    for klass in Hospital.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_rfid_reader_is_not_abstract():
    assert not inspect.isabstract(RFID_Reader)


def test_rfid_reader_constructor_exists():
    assert callable(RFID_Reader.__init__)


def test_rfid_reader_constructor_args():
    sig = inspect.signature(RFID_Reader.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "address" in params, "Missing parameter 'address'"
    assert "RFID" in params, "Missing parameter 'RFID'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "CRC_code" in params, "Missing parameter 'CRC_code'"

def test_rfid_reader_has_phone():
    assert hasattr(RFID_Reader, "phone")
    descriptor = None
    for klass in RFID_Reader.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_rfid_reader_has_address():
    assert hasattr(RFID_Reader, "address")
    descriptor = None
    for klass in RFID_Reader.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_rfid_reader_has_RFID():
    assert hasattr(RFID_Reader, "RFID")
    descriptor = None
    for klass in RFID_Reader.__mro__:
        if "RFID" in klass.__dict__:
            descriptor = klass.__dict__["RFID"]
            break
    assert isinstance(descriptor, property)

def test_rfid_reader_has_Gender():
    assert hasattr(RFID_Reader, "Gender")
    descriptor = None
    for klass in RFID_Reader.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_rfid_reader_has_birthDate():
    assert hasattr(RFID_Reader, "birthDate")
    descriptor = None
    for klass in RFID_Reader.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_rfid_reader_has_CRC_code():
    assert hasattr(RFID_Reader, "CRC_code")
    descriptor = None
    for klass in RFID_Reader.__mro__:
        if "CRC_code" in klass.__dict__:
            descriptor = klass.__dict__["CRC_code"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "joined" in params, "Missing parameter 'joined'"
    assert "education" in params, "Missing parameter 'education'"

def test_staff_has_joined():
    assert hasattr(Staff, "joined")
    descriptor = None
    for klass in Staff.__mro__:
        if "joined" in klass.__dict__:
            descriptor = klass.__dict__["joined"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_education():
    assert hasattr(Staff, "education")
    descriptor = None
    for klass in Staff.__mro__:
        if "education" in klass.__dict__:
            descriptor = klass.__dict__["education"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "roomno" in params, "Missing parameter 'roomno'"

def test_room_has_location():
    assert hasattr(Room, "location")
    descriptor = None
    for klass in Room.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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
    assert "age" in params, "Missing parameter 'age'"
    assert "roomno" in params, "Missing parameter 'roomno'"
    assert "telno" in params, "Missing parameter 'telno'"
    assert "accepted" in params, "Missing parameter 'accepted'"
    assert "sickness" in params, "Missing parameter 'sickness'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "address" in params, "Missing parameter 'address'"

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

def test_patient_has_telno():
    assert hasattr(Patient, "telno")
    descriptor = None
    for klass in Patient.__mro__:
        if "telno" in klass.__dict__:
            descriptor = klass.__dict__["telno"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_accepted():
    assert hasattr(Patient, "accepted")
    descriptor = None
    for klass in Patient.__mro__:
        if "accepted" in klass.__dict__:
            descriptor = klass.__dict__["accepted"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_sickness():
    assert hasattr(Patient, "sickness")
    descriptor = None
    for klass in Patient.__mro__:
        if "sickness" in klass.__dict__:
            descriptor = klass.__dict__["sickness"]
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



def test_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())
    assert "doctorid" in params, "Missing parameter 'doctorid'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_nurse_has_doctorid():
    assert hasattr(Nurse, "doctorid")
    descriptor = None
    for klass in Nurse.__mro__:
        if "doctorid" in klass.__dict__:
            descriptor = klass.__dict__["doctorid"]
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

def test_nurse_has_id():
    assert hasattr(Nurse, "id")
    descriptor = None
    for klass in Nurse.__mro__:
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
    assert "department" in params, "Missing parameter 'department'"
    assert "name" in params, "Missing parameter 'name'"
    assert "docid" in params, "Missing parameter 'docid'"
    assert "phno" in params, "Missing parameter 'phno'"
    assert "specialization" in params, "Missing parameter 'specialization'"
    assert "address" in params, "Missing parameter 'address'"

def test_doctor_has_department():
    assert hasattr(Doctor, "department")
    descriptor = None
    for klass in Doctor.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
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

def test_doctor_has_docid():
    assert hasattr(Doctor, "docid")
    descriptor = None
    for klass in Doctor.__mro__:
        if "docid" in klass.__dict__:
            descriptor = klass.__dict__["docid"]
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

def test_doctor_has_address():
    assert hasattr(Doctor, "address")
    descriptor = None
    for klass in Doctor.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_technical_staff_is_not_abstract():
    assert not inspect.isabstract(Technical_staff)


def test_technical_staff_constructor_exists():
    assert callable(Technical_staff.__init__)


def test_technical_staff_constructor_args():
    sig = inspect.signature(Technical_staff.__init__)
    params = list(sig.parameters.keys())



def test_administrative_staff_is_not_abstract():
    assert not inspect.isabstract(Administrative_staff)


def test_administrative_staff_constructor_exists():
    assert callable(Administrative_staff.__init__)


def test_administrative_staff_constructor_args():
    sig = inspect.signature(Administrative_staff.__init__)
    params = list(sig.parameters.keys())



def test_operations_staff_is_not_abstract():
    assert not inspect.isabstract(Operations_staff)


def test_operations_staff_constructor_exists():
    assert callable(Operations_staff.__init__)


def test_operations_staff_constructor_args():
    sig = inspect.signature(Operations_staff.__init__)
    params = list(sig.parameters.keys())



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())



def test_nurse1_is_not_abstract():
    assert not inspect.isabstract(Nurse1)


def test_nurse1_constructor_exists():
    assert callable(Nurse1.__init__)


def test_nurse1_constructor_args():
    sig = inspect.signature(Nurse1.__init__)
    params = list(sig.parameters.keys())



def test_staff1_is_not_abstract():
    assert not inspect.isabstract(Staff1)


def test_staff1_constructor_exists():
    assert callable(Staff1.__init__)


def test_staff1_constructor_args():
    sig = inspect.signature(Staff1.__init__)
    params = list(sig.parameters.keys())



def test_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "billno" in params, "Missing parameter 'billno'"
    assert "patientname" in params, "Missing parameter 'patientname'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_bill_has_billno():
    assert hasattr(Bill, "billno")
    descriptor = None
    for klass in Bill.__mro__:
        if "billno" in klass.__dict__:
            descriptor = klass.__dict__["billno"]
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

def test_bill_has_amount():
    assert hasattr(Bill, "amount")
    descriptor = None
    for klass in Bill.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
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
Hospital_strategy = st.builds(
    Hospital,
    phone=
        st.integers(),
    name=
        safe_text,
    address=
        safe_text
)
RFID_Reader_strategy = st.builds(
    RFID_Reader,
    phone=
        st.integers(),
    address=
        safe_text,
    RFID=
        st.integers(),
    Gender=
        safe_text,
    birthDate=
        st.dates(),
    CRC_code=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    joined=
        st.dates(),
    education=
        safe_text
)
Room_strategy = st.builds(
    Room,
    location=
        safe_text,
    roomno=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    age=
        st.integers(),
    roomno=
        st.integers(),
    telno=
        st.integers(),
    accepted=
        st.dates(),
    sickness=
        safe_text,
    sex=
        safe_text,
    address=
        safe_text
)
Nurse_strategy = st.builds(
    Nurse,
    doctorid=
        st.integers(),
    name=
        safe_text,
    id=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    department=
        safe_text,
    name=
        safe_text,
    docid=
        st.integers(),
    phno=
        st.integers(),
    specialization=
        safe_text,
    address=
        safe_text
)
Technical_staff_strategy = st.builds(
    Technical_staff,
)
Administrative_staff_strategy = st.builds(
    Administrative_staff,
)
Operations_staff_strategy = st.builds(
    Operations_staff,
)
Department_strategy = st.builds(
    Department,
)
Nurse1_strategy = st.builds(
    Nurse1,
)
Staff1_strategy = st.builds(
    Staff1,
)
Bill_strategy = st.builds(
    Bill,
    billno=
        safe_text,
    patientname=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Hospital_strategy)
@settings(max_examples=50)
def test_hospital_instantiation(instance):
    assert isinstance(instance, Hospital)



@given(instance=Hospital_strategy)
def test_hospital_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Hospital_strategy)
def test_hospital_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Hospital_strategy)
def test_hospital_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=RFID_Reader_strategy)
@settings(max_examples=50)
def test_rfid_reader_instantiation(instance):
    assert isinstance(instance, RFID_Reader)



@given(instance=RFID_Reader_strategy)
def test_rfid_reader_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=RFID_Reader_strategy)
def test_rfid_reader_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=RFID_Reader_strategy)
def test_rfid_reader_RFID_setter(instance):
    original = instance.RFID
    instance.RFID = original
    assert instance.RFID == original



@given(instance=RFID_Reader_strategy)
def test_rfid_reader_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=RFID_Reader_strategy)
def test_rfid_reader_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=RFID_Reader_strategy)
def test_rfid_reader_CRC_code_setter(instance):
    original = instance.CRC_code
    instance.CRC_code = original
    assert instance.CRC_code == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_joined_setter(instance):
    original = instance.joined
    instance.joined = original
    assert instance.joined == original



@given(instance=Staff_strategy)
def test_staff_education_setter(instance):
    original = instance.education
    instance.education = original
    assert instance.education == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



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
def test_patient_telno_setter(instance):
    original = instance.telno
    instance.telno = original
    assert instance.telno == original



@given(instance=Patient_strategy)
def test_patient_accepted_setter(instance):
    original = instance.accepted
    instance.accepted = original
    assert instance.accepted == original



@given(instance=Patient_strategy)
def test_patient_sickness_setter(instance):
    original = instance.sickness
    instance.sickness = original
    assert instance.sickness == original



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

@given(instance=Nurse_strategy)
@settings(max_examples=50)
def test_nurse_instantiation(instance):
    assert isinstance(instance, Nurse)



@given(instance=Nurse_strategy)
def test_nurse_doctorid_setter(instance):
    original = instance.doctorid
    instance.doctorid = original
    assert instance.doctorid == original



@given(instance=Nurse_strategy)
def test_nurse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Nurse_strategy)
def test_nurse_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=Doctor_strategy)
def test_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Doctor_strategy)
def test_doctor_docid_setter(instance):
    original = instance.docid
    instance.docid = original
    assert instance.docid == original



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
def test_doctor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Technical_staff_strategy)
@settings(max_examples=50)
def test_technical_staff_instantiation(instance):
    assert isinstance(instance, Technical_staff)

@given(instance=Administrative_staff_strategy)
@settings(max_examples=50)
def test_administrative_staff_instantiation(instance):
    assert isinstance(instance, Administrative_staff)

@given(instance=Operations_staff_strategy)
@settings(max_examples=50)
def test_operations_staff_instantiation(instance):
    assert isinstance(instance, Operations_staff)

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)

@given(instance=Nurse1_strategy)
@settings(max_examples=50)
def test_nurse1_instantiation(instance):
    assert isinstance(instance, Nurse1)

@given(instance=Staff1_strategy)
@settings(max_examples=50)
def test_staff1_instantiation(instance):
    assert isinstance(instance, Staff1)

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
def test_bill_patientname_setter(instance):
    original = instance.patientname
    instance.patientname = original
    assert instance.patientname == original



@given(instance=Bill_strategy)
def test_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original
