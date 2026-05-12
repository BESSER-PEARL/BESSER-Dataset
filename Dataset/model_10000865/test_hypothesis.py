import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Doctor,
    pay_bills_UseCase,
    Follow_doc_instrn_UseCase,
    Consult_the_doctor_UseCase,
    Takes_Appt_UseCase,
    Doctor_Actor,
    Patient_Actor,
    Staff,
    Rooms,
    Departmnt,
    Receptionist,
    Patient,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "specialization" in params, "Missing parameter 'specialization'"
    assert "Docid" in params, "Missing parameter 'Docid'"
    assert "Department" in params, "Missing parameter 'Department'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "phno" in params, "Missing parameter 'phno'"

def test_doctor_has_specialization():
    assert hasattr(Doctor, "specialization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "specialization" in klass.__dict__:
            descriptor = klass.__dict__["specialization"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Docid():
    assert hasattr(Doctor, "Docid")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Docid" in klass.__dict__:
            descriptor = klass.__dict__["Docid"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Department():
    assert hasattr(Doctor, "Department")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Department" in klass.__dict__:
            descriptor = klass.__dict__["Department"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Name():
    assert hasattr(Doctor, "Name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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



def test_pay_bills_usecase_is_not_abstract():
    assert not inspect.isabstract(pay_bills_UseCase)


def test_pay_bills_usecase_constructor_exists():
    assert callable(pay_bills_UseCase.__init__)


def test_pay_bills_usecase_constructor_args():
    sig = inspect.signature(pay_bills_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_follow_doc_instrn_usecase_is_not_abstract():
    assert not inspect.isabstract(Follow_doc_instrn_UseCase)


def test_follow_doc_instrn_usecase_constructor_exists():
    assert callable(Follow_doc_instrn_UseCase.__init__)


def test_follow_doc_instrn_usecase_constructor_args():
    sig = inspect.signature(Follow_doc_instrn_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_consult_the_doctor_usecase_is_not_abstract():
    assert not inspect.isabstract(Consult_the_doctor_UseCase)


def test_consult_the_doctor_usecase_constructor_exists():
    assert callable(Consult_the_doctor_UseCase.__init__)


def test_consult_the_doctor_usecase_constructor_args():
    sig = inspect.signature(Consult_the_doctor_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_takes_appt_usecase_is_not_abstract():
    assert not inspect.isabstract(Takes_Appt_UseCase)


def test_takes_appt_usecase_constructor_exists():
    assert callable(Takes_Appt_UseCase.__init__)


def test_takes_appt_usecase_constructor_args():
    sig = inspect.signature(Takes_Appt_UseCase.__init__)
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



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_staff_has_Name():
    assert hasattr(Staff, "Name")
    descriptor = None
    for klass in Staff.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_id():
    assert hasattr(Staff, "id")
    descriptor = None
    for klass in Staff.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_type():
    assert hasattr(Staff, "type")
    descriptor = None
    for klass in Staff.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "Roomno" in params, "Missing parameter 'Roomno'"

def test_rooms_has_location():
    assert hasattr(Rooms, "location")
    descriptor = None
    for klass in Rooms.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_rooms_has_Roomno():
    assert hasattr(Rooms, "Roomno")
    descriptor = None
    for klass in Rooms.__mro__:
        if "Roomno" in klass.__dict__:
            descriptor = klass.__dict__["Roomno"]
            break
    assert isinstance(descriptor, property)



def test_departmnt_is_not_abstract():
    assert not inspect.isabstract(Departmnt)


def test_departmnt_constructor_exists():
    assert callable(Departmnt.__init__)


def test_departmnt_constructor_args():
    sig = inspect.signature(Departmnt.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "docid" in params, "Missing parameter 'docid'"
    assert "name" in params, "Missing parameter 'name'"

def test_departmnt_has_id():
    assert hasattr(Departmnt, "id")
    descriptor = None
    for klass in Departmnt.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_departmnt_has_docid():
    assert hasattr(Departmnt, "docid")
    descriptor = None
    for klass in Departmnt.__mro__:
        if "docid" in klass.__dict__:
            descriptor = klass.__dict__["docid"]
            break
    assert isinstance(descriptor, property)

def test_departmnt_has_name():
    assert hasattr(Departmnt, "name")
    descriptor = None
    for klass in Departmnt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_receptionist_has_id():
    assert hasattr(Receptionist, "id")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_Name():
    assert hasattr(Receptionist, "Name")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Rno" in params, "Missing parameter 'Rno'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "TelNo" in params, "Missing parameter 'TelNo'"

def test_patient_has_Rno():
    assert hasattr(Patient, "Rno")
    descriptor = None
    for klass in Patient.__mro__:
        if "Rno" in klass.__dict__:
            descriptor = klass.__dict__["Rno"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Address():
    assert hasattr(Patient, "Address")
    descriptor = None
    for klass in Patient.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Sex():
    assert hasattr(Patient, "Sex")
    descriptor = None
    for klass in Patient.__mro__:
        if "Sex" in klass.__dict__:
            descriptor = klass.__dict__["Sex"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Age():
    assert hasattr(Patient, "Age")
    descriptor = None
    for klass in Patient.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Name():
    assert hasattr(Patient, "Name")
    descriptor = None
    for klass in Patient.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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

def test_patient_has_TelNo():
    assert hasattr(Patient, "TelNo")
    descriptor = None
    for klass in Patient.__mro__:
        if "TelNo" in klass.__dict__:
            descriptor = klass.__dict__["TelNo"]
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
Doctor_strategy = st.builds(
    Doctor,
    specialization=
        safe_text,
    Docid=
        st.integers(),
    Department=
        safe_text,
    Name=
        safe_text,
    phno=
        safe_text
)
pay_bills_UseCase_strategy = st.builds(
    pay_bills_UseCase,
)
Follow_doc_instrn_UseCase_strategy = st.builds(
    Follow_doc_instrn_UseCase,
)
Consult_the_doctor_UseCase_strategy = st.builds(
    Consult_the_doctor_UseCase,
)
Takes_Appt_UseCase_strategy = st.builds(
    Takes_Appt_UseCase,
)
Doctor_Actor_strategy = st.builds(
    Doctor_Actor,
)
Patient_Actor_strategy = st.builds(
    Patient_Actor,
)
Staff_strategy = st.builds(
    Staff,
    Name=
        safe_text,
    id=
        st.integers(),
    type=
        safe_text
)
Rooms_strategy = st.builds(
    Rooms,
    location=
        safe_text,
    Roomno=
        st.integers()
)
Departmnt_strategy = st.builds(
    Departmnt,
    id=
        st.integers(),
    docid=
        st.integers(),
    name=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    id=
        st.integers(),
    Name=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    Rno=
        st.integers(),
    Address=
        safe_text,
    Sex=
        safe_text,
    Age=
        st.integers(),
    Name=
        st.integers(),
    id=
        st.integers(),
    TelNo=
        st.integers()
)

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_specialization_setter(instance):
    original = instance.specialization
    instance.specialization = original
    assert instance.specialization == original



@given(instance=Doctor_strategy)
def test_doctor_Docid_setter(instance):
    original = instance.Docid
    instance.Docid = original
    assert instance.Docid == original



@given(instance=Doctor_strategy)
def test_doctor_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original



@given(instance=Doctor_strategy)
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_doctor_phno_setter(instance):
    original = instance.phno
    instance.phno = original
    assert instance.phno == original

@given(instance=pay_bills_UseCase_strategy)
@settings(max_examples=50)
def test_pay_bills_usecase_instantiation(instance):
    assert isinstance(instance, pay_bills_UseCase)

@given(instance=Follow_doc_instrn_UseCase_strategy)
@settings(max_examples=50)
def test_follow_doc_instrn_usecase_instantiation(instance):
    assert isinstance(instance, Follow_doc_instrn_UseCase)

@given(instance=Consult_the_doctor_UseCase_strategy)
@settings(max_examples=50)
def test_consult_the_doctor_usecase_instantiation(instance):
    assert isinstance(instance, Consult_the_doctor_UseCase)

@given(instance=Takes_Appt_UseCase_strategy)
@settings(max_examples=50)
def test_takes_appt_usecase_instantiation(instance):
    assert isinstance(instance, Takes_Appt_UseCase)

@given(instance=Doctor_Actor_strategy)
@settings(max_examples=50)
def test_doctor_actor_instantiation(instance):
    assert isinstance(instance, Doctor_Actor)

@given(instance=Patient_Actor_strategy)
@settings(max_examples=50)
def test_patient_actor_instantiation(instance):
    assert isinstance(instance, Patient_Actor)

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Staff_strategy)
def test_staff_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Staff_strategy)
def test_staff_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Rooms_strategy)
@settings(max_examples=50)
def test_rooms_instantiation(instance):
    assert isinstance(instance, Rooms)



@given(instance=Rooms_strategy)
def test_rooms_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Rooms_strategy)
def test_rooms_Roomno_setter(instance):
    original = instance.Roomno
    instance.Roomno = original
    assert instance.Roomno == original

@given(instance=Departmnt_strategy)
@settings(max_examples=50)
def test_departmnt_instantiation(instance):
    assert isinstance(instance, Departmnt)



@given(instance=Departmnt_strategy)
def test_departmnt_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Departmnt_strategy)
def test_departmnt_docid_setter(instance):
    original = instance.docid
    instance.docid = original
    assert instance.docid == original



@given(instance=Departmnt_strategy)
def test_departmnt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Receptionist_strategy)
def test_receptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_Rno_setter(instance):
    original = instance.Rno
    instance.Rno = original
    assert instance.Rno == original



@given(instance=Patient_strategy)
def test_patient_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Patient_strategy)
def test_patient_Sex_setter(instance):
    original = instance.Sex
    instance.Sex = original
    assert instance.Sex == original



@given(instance=Patient_strategy)
def test_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Patient_strategy)
def test_patient_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_strategy)
def test_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_patient_TelNo_setter(instance):
    original = instance.TelNo
    instance.TelNo = original
    assert instance.TelNo == original
