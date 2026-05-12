import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Patient_Check_In_aPatient,
    Patient_Check_In_aDoctor,
    Patient_Check_In__aReceptionist,
    Patient_Check_In_aNurse,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_patient_check_in_apatient_is_not_abstract():
    assert not inspect.isabstract(Patient_Check_In_aPatient)


def test_patient_check_in_apatient_constructor_exists():
    assert callable(Patient_Check_In_aPatient.__init__)


def test_patient_check_in_apatient_constructor_args():
    sig = inspect.signature(Patient_Check_In_aPatient.__init__)
    params = list(sig.parameters.keys())
    assert "Phone_Number" in params, "Missing parameter 'Phone_Number'"
    assert "MRN_Number" in params, "Missing parameter 'MRN_Number'"
    assert "Symptoms" in params, "Missing parameter 'Symptoms'"
    assert "Patient_s_Name" in params, "Missing parameter 'Patient_s_Name'"

def test_patient_check_in_apatient_has_Phone_Number():
    assert hasattr(Patient_Check_In_aPatient, "Phone_Number")
    descriptor = None
    for klass in Patient_Check_In_aPatient.__mro__:
        if "Phone_Number" in klass.__dict__:
            descriptor = klass.__dict__["Phone_Number"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in_apatient_has_MRN_Number():
    assert hasattr(Patient_Check_In_aPatient, "MRN_Number")
    descriptor = None
    for klass in Patient_Check_In_aPatient.__mro__:
        if "MRN_Number" in klass.__dict__:
            descriptor = klass.__dict__["MRN_Number"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in_apatient_has_Symptoms():
    assert hasattr(Patient_Check_In_aPatient, "Symptoms")
    descriptor = None
    for klass in Patient_Check_In_aPatient.__mro__:
        if "Symptoms" in klass.__dict__:
            descriptor = klass.__dict__["Symptoms"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in_apatient_has_Patient_s_Name():
    assert hasattr(Patient_Check_In_aPatient, "Patient_s_Name")
    descriptor = None
    for klass in Patient_Check_In_aPatient.__mro__:
        if "Patient_s_Name" in klass.__dict__:
            descriptor = klass.__dict__["Patient_s_Name"]
            break
    assert isinstance(descriptor, property)



def test_patient_check_in_adoctor_is_not_abstract():
    assert not inspect.isabstract(Patient_Check_In_aDoctor)


def test_patient_check_in_adoctor_constructor_exists():
    assert callable(Patient_Check_In_aDoctor.__init__)


def test_patient_check_in_adoctor_constructor_args():
    sig = inspect.signature(Patient_Check_In_aDoctor.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Rank" in params, "Missing parameter 'Rank'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"

def test_patient_check_in_adoctor_has_Name():
    assert hasattr(Patient_Check_In_aDoctor, "Name")
    descriptor = None
    for klass in Patient_Check_In_aDoctor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in_adoctor_has_ID():
    assert hasattr(Patient_Check_In_aDoctor, "ID")
    descriptor = None
    for klass in Patient_Check_In_aDoctor.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in_adoctor_has_Rank():
    assert hasattr(Patient_Check_In_aDoctor, "Rank")
    descriptor = None
    for klass in Patient_Check_In_aDoctor.__mro__:
        if "Rank" in klass.__dict__:
            descriptor = klass.__dict__["Rank"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in_adoctor_has_Specialization():
    assert hasattr(Patient_Check_In_aDoctor, "Specialization")
    descriptor = None
    for klass in Patient_Check_In_aDoctor.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)



def test_patient_check_in__areceptionist_is_not_abstract():
    assert not inspect.isabstract(Patient_Check_In__aReceptionist)


def test_patient_check_in__areceptionist_constructor_exists():
    assert callable(Patient_Check_In__aReceptionist.__init__)


def test_patient_check_in__areceptionist_constructor_args():
    sig = inspect.signature(Patient_Check_In__aReceptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Employee_ID" in params, "Missing parameter 'Employee_ID'"

def test_patient_check_in__areceptionist_has_Name():
    assert hasattr(Patient_Check_In__aReceptionist, "Name")
    descriptor = None
    for klass in Patient_Check_In__aReceptionist.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in__areceptionist_has_Employee_ID():
    assert hasattr(Patient_Check_In__aReceptionist, "Employee_ID")
    descriptor = None
    for klass in Patient_Check_In__aReceptionist.__mro__:
        if "Employee_ID" in klass.__dict__:
            descriptor = klass.__dict__["Employee_ID"]
            break
    assert isinstance(descriptor, property)



def test_patient_check_in_anurse_is_not_abstract():
    assert not inspect.isabstract(Patient_Check_In_aNurse)


def test_patient_check_in_anurse_constructor_exists():
    assert callable(Patient_Check_In_aNurse.__init__)


def test_patient_check_in_anurse_constructor_args():
    sig = inspect.signature(Patient_Check_In_aNurse.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Ranking" in params, "Missing parameter 'Ranking'"

def test_patient_check_in_anurse_has_Name():
    assert hasattr(Patient_Check_In_aNurse, "Name")
    descriptor = None
    for klass in Patient_Check_In_aNurse.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in_anurse_has_ID():
    assert hasattr(Patient_Check_In_aNurse, "ID")
    descriptor = None
    for klass in Patient_Check_In_aNurse.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_patient_check_in_anurse_has_Ranking():
    assert hasattr(Patient_Check_In_aNurse, "Ranking")
    descriptor = None
    for klass in Patient_Check_In_aNurse.__mro__:
        if "Ranking" in klass.__dict__:
            descriptor = klass.__dict__["Ranking"]
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
Patient_Check_In_aPatient_strategy = st.builds(
    Patient_Check_In_aPatient,
    Phone_Number=
        st.integers(),
    MRN_Number=
        st.integers(),
    Symptoms=
        safe_text,
    Patient_s_Name=
        safe_text
)
Patient_Check_In_aDoctor_strategy = st.builds(
    Patient_Check_In_aDoctor,
    Name=
        safe_text,
    ID=
        st.integers(),
    Rank=
        safe_text,
    Specialization=
        safe_text
)
Patient_Check_In__aReceptionist_strategy = st.builds(
    Patient_Check_In__aReceptionist,
    Name=
        safe_text,
    Employee_ID=
        st.integers()
)
Patient_Check_In_aNurse_strategy = st.builds(
    Patient_Check_In_aNurse,
    Name=
        safe_text,
    ID=
        st.integers(),
    Ranking=
        safe_text
)

@given(instance=Patient_Check_In_aPatient_strategy)
@settings(max_examples=50)
def test_patient_check_in_apatient_instantiation(instance):
    assert isinstance(instance, Patient_Check_In_aPatient)



@given(instance=Patient_Check_In_aPatient_strategy)
def test_patient_check_in_apatient_Phone_Number_setter(instance):
    original = instance.Phone_Number
    instance.Phone_Number = original
    assert instance.Phone_Number == original



@given(instance=Patient_Check_In_aPatient_strategy)
def test_patient_check_in_apatient_MRN_Number_setter(instance):
    original = instance.MRN_Number
    instance.MRN_Number = original
    assert instance.MRN_Number == original



@given(instance=Patient_Check_In_aPatient_strategy)
def test_patient_check_in_apatient_Symptoms_setter(instance):
    original = instance.Symptoms
    instance.Symptoms = original
    assert instance.Symptoms == original



@given(instance=Patient_Check_In_aPatient_strategy)
def test_patient_check_in_apatient_Patient_s_Name_setter(instance):
    original = instance.Patient_s_Name
    instance.Patient_s_Name = original
    assert instance.Patient_s_Name == original

@given(instance=Patient_Check_In_aDoctor_strategy)
@settings(max_examples=50)
def test_patient_check_in_adoctor_instantiation(instance):
    assert isinstance(instance, Patient_Check_In_aDoctor)



@given(instance=Patient_Check_In_aDoctor_strategy)
def test_patient_check_in_adoctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_Check_In_aDoctor_strategy)
def test_patient_check_in_adoctor_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Patient_Check_In_aDoctor_strategy)
def test_patient_check_in_adoctor_Rank_setter(instance):
    original = instance.Rank
    instance.Rank = original
    assert instance.Rank == original



@given(instance=Patient_Check_In_aDoctor_strategy)
def test_patient_check_in_adoctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original

@given(instance=Patient_Check_In__aReceptionist_strategy)
@settings(max_examples=50)
def test_patient_check_in__areceptionist_instantiation(instance):
    assert isinstance(instance, Patient_Check_In__aReceptionist)



@given(instance=Patient_Check_In__aReceptionist_strategy)
def test_patient_check_in__areceptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_Check_In__aReceptionist_strategy)
def test_patient_check_in__areceptionist_Employee_ID_setter(instance):
    original = instance.Employee_ID
    instance.Employee_ID = original
    assert instance.Employee_ID == original

@given(instance=Patient_Check_In_aNurse_strategy)
@settings(max_examples=50)
def test_patient_check_in_anurse_instantiation(instance):
    assert isinstance(instance, Patient_Check_In_aNurse)



@given(instance=Patient_Check_In_aNurse_strategy)
def test_patient_check_in_anurse_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_Check_In_aNurse_strategy)
def test_patient_check_in_anurse_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Patient_Check_In_aNurse_strategy)
def test_patient_check_in_anurse_Ranking_setter(instance):
    original = instance.Ranking
    instance.Ranking = original
    assert instance.Ranking == original
