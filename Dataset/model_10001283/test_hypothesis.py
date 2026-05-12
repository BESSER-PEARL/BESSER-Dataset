import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Patient,
    Medicine,
    Symptoms,
    Instructions,
    Medical_test,
    Signs,
    Diagnosis,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "MedicalTest" in params, "Missing parameter 'MedicalTest'"
    assert "Medicine" in params, "Missing parameter 'Medicine'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "Allergies" in params, "Missing parameter 'Allergies'"
    assert "Surgeries" in params, "Missing parameter 'Surgeries'"
    assert "Height" in params, "Missing parameter 'Height'"
    assert "DiagnosisList" in params, "Missing parameter 'DiagnosisList'"

def test_patient_has_MedicalTest():
    assert hasattr(Patient, "MedicalTest")
    descriptor = None
    for klass in Patient.__mro__:
        if "MedicalTest" in klass.__dict__:
            descriptor = klass.__dict__["MedicalTest"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Medicine():
    assert hasattr(Patient, "Medicine")
    descriptor = None
    for klass in Patient.__mro__:
        if "Medicine" in klass.__dict__:
            descriptor = klass.__dict__["Medicine"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_weight():
    assert hasattr(Patient, "weight")
    descriptor = None
    for klass in Patient.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Allergies():
    assert hasattr(Patient, "Allergies")
    descriptor = None
    for klass in Patient.__mro__:
        if "Allergies" in klass.__dict__:
            descriptor = klass.__dict__["Allergies"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Surgeries():
    assert hasattr(Patient, "Surgeries")
    descriptor = None
    for klass in Patient.__mro__:
        if "Surgeries" in klass.__dict__:
            descriptor = klass.__dict__["Surgeries"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_Height():
    assert hasattr(Patient, "Height")
    descriptor = None
    for klass in Patient.__mro__:
        if "Height" in klass.__dict__:
            descriptor = klass.__dict__["Height"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_DiagnosisList():
    assert hasattr(Patient, "DiagnosisList")
    descriptor = None
    for klass in Patient.__mro__:
        if "DiagnosisList" in klass.__dict__:
            descriptor = klass.__dict__["DiagnosisList"]
            break
    assert isinstance(descriptor, property)



def test_medicine_is_not_abstract():
    assert not inspect.isabstract(Medicine)


def test_medicine_constructor_exists():
    assert callable(Medicine.__init__)


def test_medicine_constructor_args():
    sig = inspect.signature(Medicine.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "ActiveIngredient" in params, "Missing parameter 'ActiveIngredient'"

def test_medicine_has_ID():
    assert hasattr(Medicine, "ID")
    descriptor = None
    for klass in Medicine.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_Price():
    assert hasattr(Medicine, "Price")
    descriptor = None
    for klass in Medicine.__mro__:
        if "Price" in klass.__dict__:
            descriptor = klass.__dict__["Price"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_Type():
    assert hasattr(Medicine, "Type")
    descriptor = None
    for klass in Medicine.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
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

def test_medicine_has_ActiveIngredient():
    assert hasattr(Medicine, "ActiveIngredient")
    descriptor = None
    for klass in Medicine.__mro__:
        if "ActiveIngredient" in klass.__dict__:
            descriptor = klass.__dict__["ActiveIngredient"]
            break
    assert isinstance(descriptor, property)



def test_symptoms_is_not_abstract():
    assert not inspect.isabstract(Symptoms)


def test_symptoms_constructor_exists():
    assert callable(Symptoms.__init__)


def test_symptoms_constructor_args():
    sig = inspect.signature(Symptoms.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_symptoms_has_name():
    assert hasattr(Symptoms, "name")
    descriptor = None
    for klass in Symptoms.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_symptoms_has_ID():
    assert hasattr(Symptoms, "ID")
    descriptor = None
    for klass in Symptoms.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_instructions_is_not_abstract():
    assert not inspect.isabstract(Instructions)


def test_instructions_constructor_exists():
    assert callable(Instructions.__init__)


def test_instructions_constructor_args():
    sig = inspect.signature(Instructions.__init__)
    params = list(sig.parameters.keys())
    assert "descriptions" in params, "Missing parameter 'descriptions'"
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_instructions_has_descriptions():
    assert hasattr(Instructions, "descriptions")
    descriptor = None
    for klass in Instructions.__mro__:
        if "descriptions" in klass.__dict__:
            descriptor = klass.__dict__["descriptions"]
            break
    assert isinstance(descriptor, property)

def test_instructions_has_name():
    assert hasattr(Instructions, "name")
    descriptor = None
    for klass in Instructions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_instructions_has_ID():
    assert hasattr(Instructions, "ID")
    descriptor = None
    for klass in Instructions.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_medical_test_is_not_abstract():
    assert not inspect.isabstract(Medical_test)


def test_medical_test_constructor_exists():
    assert callable(Medical_test.__init__)


def test_medical_test_constructor_args():
    sig = inspect.signature(Medical_test.__init__)
    params = list(sig.parameters.keys())
    assert "Lab" in params, "Missing parameter 'Lab'"
    assert "Image" in params, "Missing parameter 'Image'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_medical_test_has_Lab():
    assert hasattr(Medical_test, "Lab")
    descriptor = None
    for klass in Medical_test.__mro__:
        if "Lab" in klass.__dict__:
            descriptor = klass.__dict__["Lab"]
            break
    assert isinstance(descriptor, property)

def test_medical_test_has_Image():
    assert hasattr(Medical_test, "Image")
    descriptor = None
    for klass in Medical_test.__mro__:
        if "Image" in klass.__dict__:
            descriptor = klass.__dict__["Image"]
            break
    assert isinstance(descriptor, property)

def test_medical_test_has_ID():
    assert hasattr(Medical_test, "ID")
    descriptor = None
    for klass in Medical_test.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_medical_test_has_name():
    assert hasattr(Medical_test, "name")
    descriptor = None
    for klass in Medical_test.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_medical_test_has_Date():
    assert hasattr(Medical_test, "Date")
    descriptor = None
    for klass in Medical_test.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_signs_is_not_abstract():
    assert not inspect.isabstract(Signs)


def test_signs_constructor_exists():
    assert callable(Signs.__init__)


def test_signs_constructor_args():
    sig = inspect.signature(Signs.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_signs_has_name():
    assert hasattr(Signs, "name")
    descriptor = None
    for klass in Signs.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_signs_has_ID():
    assert hasattr(Signs, "ID")
    descriptor = None
    for klass in Signs.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_diagnosis_is_not_abstract():
    assert not inspect.isabstract(Diagnosis)


def test_diagnosis_constructor_exists():
    assert callable(Diagnosis.__init__)


def test_diagnosis_constructor_args():
    sig = inspect.signature(Diagnosis.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "LIst_of_Instructions" in params, "Missing parameter 'LIst_of_Instructions'"
    assert "LIst_of_Diagnosis" in params, "Missing parameter 'LIst_of_Diagnosis'"
    assert "Doctor_Id" in params, "Missing parameter 'Doctor_Id'"
    assert "Condition" in params, "Missing parameter 'Condition'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "LIst_of_Symptoms" in params, "Missing parameter 'LIst_of_Symptoms'"
    assert "LIst_of_Medicine" in params, "Missing parameter 'LIst_of_Medicine'"
    assert "Patient_Id" in params, "Missing parameter 'Patient_Id'"
    assert "LIst_of_Medical_Test" in params, "Missing parameter 'LIst_of_Medical_Test'"

def test_diagnosis_has_ID():
    assert hasattr(Diagnosis, "ID")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_LIst_of_Instructions():
    assert hasattr(Diagnosis, "LIst_of_Instructions")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "LIst_of_Instructions" in klass.__dict__:
            descriptor = klass.__dict__["LIst_of_Instructions"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_LIst_of_Diagnosis():
    assert hasattr(Diagnosis, "LIst_of_Diagnosis")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "LIst_of_Diagnosis" in klass.__dict__:
            descriptor = klass.__dict__["LIst_of_Diagnosis"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_Doctor_Id():
    assert hasattr(Diagnosis, "Doctor_Id")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "Doctor_Id" in klass.__dict__:
            descriptor = klass.__dict__["Doctor_Id"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_Condition():
    assert hasattr(Diagnosis, "Condition")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "Condition" in klass.__dict__:
            descriptor = klass.__dict__["Condition"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_Date():
    assert hasattr(Diagnosis, "Date")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_LIst_of_Symptoms():
    assert hasattr(Diagnosis, "LIst_of_Symptoms")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "LIst_of_Symptoms" in klass.__dict__:
            descriptor = klass.__dict__["LIst_of_Symptoms"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_LIst_of_Medicine():
    assert hasattr(Diagnosis, "LIst_of_Medicine")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "LIst_of_Medicine" in klass.__dict__:
            descriptor = klass.__dict__["LIst_of_Medicine"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_Patient_Id():
    assert hasattr(Diagnosis, "Patient_Id")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "Patient_Id" in klass.__dict__:
            descriptor = klass.__dict__["Patient_Id"]
            break
    assert isinstance(descriptor, property)

def test_diagnosis_has_LIst_of_Medical_Test():
    assert hasattr(Diagnosis, "LIst_of_Medical_Test")
    descriptor = None
    for klass in Diagnosis.__mro__:
        if "LIst_of_Medical_Test" in klass.__dict__:
            descriptor = klass.__dict__["LIst_of_Medical_Test"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "PhoneNumeber" in params, "Missing parameter 'PhoneNumeber'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Lat" in params, "Missing parameter 'Lat'"
    assert "Balance" in params, "Missing parameter 'Balance'"
    assert "Image" in params, "Missing parameter 'Image'"
    assert "InsuranceNumber" in params, "Missing parameter 'InsuranceNumber'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Ssn" in params, "Missing parameter 'Ssn'"
    assert "Long" in params, "Missing parameter 'Long'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Last_Seen" in params, "Missing parameter 'Last_Seen'"

def test_person_has_PhoneNumeber():
    assert hasattr(Person, "PhoneNumeber")
    descriptor = None
    for klass in Person.__mro__:
        if "PhoneNumeber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumeber"]
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

def test_person_has_Lat():
    assert hasattr(Person, "Lat")
    descriptor = None
    for klass in Person.__mro__:
        if "Lat" in klass.__dict__:
            descriptor = klass.__dict__["Lat"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Balance():
    assert hasattr(Person, "Balance")
    descriptor = None
    for klass in Person.__mro__:
        if "Balance" in klass.__dict__:
            descriptor = klass.__dict__["Balance"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Image():
    assert hasattr(Person, "Image")
    descriptor = None
    for klass in Person.__mro__:
        if "Image" in klass.__dict__:
            descriptor = klass.__dict__["Image"]
            break
    assert isinstance(descriptor, property)

def test_person_has_InsuranceNumber():
    assert hasattr(Person, "InsuranceNumber")
    descriptor = None
    for klass in Person.__mro__:
        if "InsuranceNumber" in klass.__dict__:
            descriptor = klass.__dict__["InsuranceNumber"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Email():
    assert hasattr(Person, "Email")
    descriptor = None
    for klass in Person.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Password():
    assert hasattr(Person, "Password")
    descriptor = None
    for klass in Person.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
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

def test_person_has_Ssn():
    assert hasattr(Person, "Ssn")
    descriptor = None
    for klass in Person.__mro__:
        if "Ssn" in klass.__dict__:
            descriptor = klass.__dict__["Ssn"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Long():
    assert hasattr(Person, "Long")
    descriptor = None
    for klass in Person.__mro__:
        if "Long" in klass.__dict__:
            descriptor = klass.__dict__["Long"]
            break
    assert isinstance(descriptor, property)

def test_person_has_ID():
    assert hasattr(Person, "ID")
    descriptor = None
    for klass in Person.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Last_Seen():
    assert hasattr(Person, "Last_Seen")
    descriptor = None
    for klass in Person.__mro__:
        if "Last_Seen" in klass.__dict__:
            descriptor = klass.__dict__["Last_Seen"]
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
Patient_strategy = st.builds(
    Patient,
    MedicalTest=
        safe_text,
    Medicine=
        safe_text,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Allergies=
        safe_text,
    Surgeries=
        safe_text,
    Height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    DiagnosisList=
        safe_text
)
Medicine_strategy = st.builds(
    Medicine,
    ID=
        st.integers(),
    Price=
        safe_text,
    Type=
        safe_text,
    name=
        safe_text,
    ActiveIngredient=
        safe_text
)
Symptoms_strategy = st.builds(
    Symptoms,
    name=
        safe_text,
    ID=
        st.integers()
)
Instructions_strategy = st.builds(
    Instructions,
    descriptions=
        safe_text,
    name=
        safe_text,
    ID=
        st.integers()
)
Medical_test_strategy = st.builds(
    Medical_test,
    Lab=
        safe_text,
    Image=
        safe_text,
    ID=
        st.integers(),
    name=
        safe_text,
    Date=
        safe_text
)
Signs_strategy = st.builds(
    Signs,
    name=
        safe_text,
    ID=
        st.integers()
)
Diagnosis_strategy = st.builds(
    Diagnosis,
    ID=
        st.integers(),
    LIst_of_Instructions=
        safe_text,
    LIst_of_Diagnosis=
        safe_text,
    Doctor_Id=
        st.integers(),
    Condition=
        safe_text,
    Date=
        safe_text,
    LIst_of_Symptoms=
        safe_text,
    LIst_of_Medicine=
        safe_text,
    Patient_Id=
        st.integers(),
    LIst_of_Medical_Test=
        safe_text
)
Person_strategy = st.builds(
    Person,
    PhoneNumeber=
        safe_text,
    Gender=
        st.integers(),
    Lat=
        safe_text,
    Balance=
        safe_text,
    Image=
        safe_text,
    InsuranceNumber=
        safe_text,
    Email=
        safe_text,
    Password=
        safe_text,
    Name=
        safe_text,
    Ssn=
        safe_text,
    Long=
        safe_text,
    ID=
        st.integers(),
    Last_Seen=
        safe_text
)

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_MedicalTest_setter(instance):
    original = instance.MedicalTest
    instance.MedicalTest = original
    assert instance.MedicalTest == original



@given(instance=Patient_strategy)
def test_patient_Medicine_setter(instance):
    original = instance.Medicine
    instance.Medicine = original
    assert instance.Medicine == original



@given(instance=Patient_strategy)
def test_patient_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=Patient_strategy)
def test_patient_Allergies_setter(instance):
    original = instance.Allergies
    instance.Allergies = original
    assert instance.Allergies == original



@given(instance=Patient_strategy)
def test_patient_Surgeries_setter(instance):
    original = instance.Surgeries
    instance.Surgeries = original
    assert instance.Surgeries == original



@given(instance=Patient_strategy)
def test_patient_Height_setter(instance):
    original = instance.Height
    instance.Height = original
    assert instance.Height == original



@given(instance=Patient_strategy)
def test_patient_DiagnosisList_setter(instance):
    original = instance.DiagnosisList
    instance.DiagnosisList = original
    assert instance.DiagnosisList == original

@given(instance=Medicine_strategy)
@settings(max_examples=50)
def test_medicine_instantiation(instance):
    assert isinstance(instance, Medicine)



@given(instance=Medicine_strategy)
def test_medicine_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Medicine_strategy)
def test_medicine_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Medicine_strategy)
def test_medicine_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Medicine_strategy)
def test_medicine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Medicine_strategy)
def test_medicine_ActiveIngredient_setter(instance):
    original = instance.ActiveIngredient
    instance.ActiveIngredient = original
    assert instance.ActiveIngredient == original

@given(instance=Symptoms_strategy)
@settings(max_examples=50)
def test_symptoms_instantiation(instance):
    assert isinstance(instance, Symptoms)



@given(instance=Symptoms_strategy)
def test_symptoms_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Symptoms_strategy)
def test_symptoms_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Instructions_strategy)
@settings(max_examples=50)
def test_instructions_instantiation(instance):
    assert isinstance(instance, Instructions)



@given(instance=Instructions_strategy)
def test_instructions_descriptions_setter(instance):
    original = instance.descriptions
    instance.descriptions = original
    assert instance.descriptions == original



@given(instance=Instructions_strategy)
def test_instructions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Instructions_strategy)
def test_instructions_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Medical_test_strategy)
@settings(max_examples=50)
def test_medical_test_instantiation(instance):
    assert isinstance(instance, Medical_test)



@given(instance=Medical_test_strategy)
def test_medical_test_Lab_setter(instance):
    original = instance.Lab
    instance.Lab = original
    assert instance.Lab == original



@given(instance=Medical_test_strategy)
def test_medical_test_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original



@given(instance=Medical_test_strategy)
def test_medical_test_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Medical_test_strategy)
def test_medical_test_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Medical_test_strategy)
def test_medical_test_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Signs_strategy)
@settings(max_examples=50)
def test_signs_instantiation(instance):
    assert isinstance(instance, Signs)



@given(instance=Signs_strategy)
def test_signs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Signs_strategy)
def test_signs_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Diagnosis_strategy)
@settings(max_examples=50)
def test_diagnosis_instantiation(instance):
    assert isinstance(instance, Diagnosis)



@given(instance=Diagnosis_strategy)
def test_diagnosis_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_LIst_of_Instructions_setter(instance):
    original = instance.LIst_of_Instructions
    instance.LIst_of_Instructions = original
    assert instance.LIst_of_Instructions == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_LIst_of_Diagnosis_setter(instance):
    original = instance.LIst_of_Diagnosis
    instance.LIst_of_Diagnosis = original
    assert instance.LIst_of_Diagnosis == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_Doctor_Id_setter(instance):
    original = instance.Doctor_Id
    instance.Doctor_Id = original
    assert instance.Doctor_Id == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_Condition_setter(instance):
    original = instance.Condition
    instance.Condition = original
    assert instance.Condition == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_LIst_of_Symptoms_setter(instance):
    original = instance.LIst_of_Symptoms
    instance.LIst_of_Symptoms = original
    assert instance.LIst_of_Symptoms == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_LIst_of_Medicine_setter(instance):
    original = instance.LIst_of_Medicine
    instance.LIst_of_Medicine = original
    assert instance.LIst_of_Medicine == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_Patient_Id_setter(instance):
    original = instance.Patient_Id
    instance.Patient_Id = original
    assert instance.Patient_Id == original



@given(instance=Diagnosis_strategy)
def test_diagnosis_LIst_of_Medical_Test_setter(instance):
    original = instance.LIst_of_Medical_Test
    instance.LIst_of_Medical_Test = original
    assert instance.LIst_of_Medical_Test == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_PhoneNumeber_setter(instance):
    original = instance.PhoneNumeber
    instance.PhoneNumeber = original
    assert instance.PhoneNumeber == original



@given(instance=Person_strategy)
def test_person_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Person_strategy)
def test_person_Lat_setter(instance):
    original = instance.Lat
    instance.Lat = original
    assert instance.Lat == original



@given(instance=Person_strategy)
def test_person_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original



@given(instance=Person_strategy)
def test_person_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original



@given(instance=Person_strategy)
def test_person_InsuranceNumber_setter(instance):
    original = instance.InsuranceNumber
    instance.InsuranceNumber = original
    assert instance.InsuranceNumber == original



@given(instance=Person_strategy)
def test_person_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Person_strategy)
def test_person_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Person_strategy)
def test_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Person_strategy)
def test_person_Ssn_setter(instance):
    original = instance.Ssn
    instance.Ssn = original
    assert instance.Ssn == original



@given(instance=Person_strategy)
def test_person_Long_setter(instance):
    original = instance.Long
    instance.Long = original
    assert instance.Long == original



@given(instance=Person_strategy)
def test_person_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Person_strategy)
def test_person_Last_Seen_setter(instance):
    original = instance.Last_Seen
    instance.Last_Seen = original
    assert instance.Last_Seen == original
