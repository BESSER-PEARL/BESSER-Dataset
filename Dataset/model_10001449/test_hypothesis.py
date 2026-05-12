import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Billing_Report,
    BloodBank,
    Prescription,
    Assistant,
    PatientProfile,
    DoctorDatabase,
    Appointment,
    Receptionist,
    Patients,
    Doctor,
    Hospital,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_billing_report_is_not_abstract():
    assert not inspect.isabstract(Billing_Report)


def test_billing_report_constructor_exists():
    assert callable(Billing_Report.__init__)


def test_billing_report_constructor_args():
    sig = inspect.signature(Billing_Report.__init__)
    params = list(sig.parameters.keys())
    assert "serviceCharges" in params, "Missing parameter 'serviceCharges'"
    assert "testCharges" in params, "Missing parameter 'testCharges'"

def test_billing_report_has_serviceCharges():
    assert hasattr(Billing_Report, "serviceCharges")
    descriptor = None
    for klass in Billing_Report.__mro__:
        if "serviceCharges" in klass.__dict__:
            descriptor = klass.__dict__["serviceCharges"]
            break
    assert isinstance(descriptor, property)

def test_billing_report_has_testCharges():
    assert hasattr(Billing_Report, "testCharges")
    descriptor = None
    for klass in Billing_Report.__mro__:
        if "testCharges" in klass.__dict__:
            descriptor = klass.__dict__["testCharges"]
            break
    assert isinstance(descriptor, property)



def test_bloodbank_is_not_abstract():
    assert not inspect.isabstract(BloodBank)


def test_bloodbank_constructor_exists():
    assert callable(BloodBank.__init__)


def test_bloodbank_constructor_args():
    sig = inspect.signature(BloodBank.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "bloodGroup" in params, "Missing parameter 'bloodGroup'"

def test_bloodbank_has_phone():
    assert hasattr(BloodBank, "phone")
    descriptor = None
    for klass in BloodBank.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)

def test_bloodbank_has_bloodGroup():
    assert hasattr(BloodBank, "bloodGroup")
    descriptor = None
    for klass in BloodBank.__mro__:
        if "bloodGroup" in klass.__dict__:
            descriptor = klass.__dict__["bloodGroup"]
            break
    assert isinstance(descriptor, property)



def test_prescription_is_not_abstract():
    assert not inspect.isabstract(Prescription)


def test_prescription_constructor_exists():
    assert callable(Prescription.__init__)


def test_prescription_constructor_args():
    sig = inspect.signature(Prescription.__init__)
    params = list(sig.parameters.keys())
    assert "tests" in params, "Missing parameter 'tests'"
    assert "medicines" in params, "Missing parameter 'medicines'"

def test_prescription_has_tests():
    assert hasattr(Prescription, "tests")
    descriptor = None
    for klass in Prescription.__mro__:
        if "tests" in klass.__dict__:
            descriptor = klass.__dict__["tests"]
            break
    assert isinstance(descriptor, property)

def test_prescription_has_medicines():
    assert hasattr(Prescription, "medicines")
    descriptor = None
    for klass in Prescription.__mro__:
        if "medicines" in klass.__dict__:
            descriptor = klass.__dict__["medicines"]
            break
    assert isinstance(descriptor, property)



def test_assistant_is_not_abstract():
    assert not inspect.isabstract(Assistant)


def test_assistant_constructor_exists():
    assert callable(Assistant.__init__)


def test_assistant_constructor_args():
    sig = inspect.signature(Assistant.__init__)
    params = list(sig.parameters.keys())
    assert "CNIC" in params, "Missing parameter 'CNIC'"
    assert "name" in params, "Missing parameter 'name'"

def test_assistant_has_CNIC():
    assert hasattr(Assistant, "CNIC")
    descriptor = None
    for klass in Assistant.__mro__:
        if "CNIC" in klass.__dict__:
            descriptor = klass.__dict__["CNIC"]
            break
    assert isinstance(descriptor, property)

def test_assistant_has_name():
    assert hasattr(Assistant, "name")
    descriptor = None
    for klass in Assistant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_patientprofile_is_not_abstract():
    assert not inspect.isabstract(PatientProfile)


def test_patientprofile_constructor_exists():
    assert callable(PatientProfile.__init__)


def test_patientprofile_constructor_args():
    sig = inspect.signature(PatientProfile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "appointment" in params, "Missing parameter 'appointment'"

def test_patientprofile_has_name():
    assert hasattr(PatientProfile, "name")
    descriptor = None
    for klass in PatientProfile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_patientprofile_has_appointment():
    assert hasattr(PatientProfile, "appointment")
    descriptor = None
    for klass in PatientProfile.__mro__:
        if "appointment" in klass.__dict__:
            descriptor = klass.__dict__["appointment"]
            break
    assert isinstance(descriptor, property)



def test_doctordatabase_is_not_abstract():
    assert not inspect.isabstract(DoctorDatabase)


def test_doctordatabase_constructor_exists():
    assert callable(DoctorDatabase.__init__)


def test_doctordatabase_constructor_args():
    sig = inspect.signature(DoctorDatabase.__init__)
    params = list(sig.parameters.keys())
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "doctorName" in params, "Missing parameter 'doctorName'"

def test_doctordatabase_has_Specialization():
    assert hasattr(DoctorDatabase, "Specialization")
    descriptor = None
    for klass in DoctorDatabase.__mro__:
        if "Specialization" in klass.__dict__:
            descriptor = klass.__dict__["Specialization"]
            break
    assert isinstance(descriptor, property)

def test_doctordatabase_has_doctorName():
    assert hasattr(DoctorDatabase, "doctorName")
    descriptor = None
    for klass in DoctorDatabase.__mro__:
        if "doctorName" in klass.__dict__:
            descriptor = klass.__dict__["doctorName"]
            break
    assert isinstance(descriptor, property)



def test_appointment_is_not_abstract():
    assert not inspect.isabstract(Appointment)


def test_appointment_constructor_exists():
    assert callable(Appointment.__init__)


def test_appointment_constructor_args():
    sig = inspect.signature(Appointment.__init__)
    params = list(sig.parameters.keys())
    assert "Patient" in params, "Missing parameter 'Patient'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Doctor" in params, "Missing parameter 'Doctor'"

def test_appointment_has_Patient():
    assert hasattr(Appointment, "Patient")
    descriptor = None
    for klass in Appointment.__mro__:
        if "Patient" in klass.__dict__:
            descriptor = klass.__dict__["Patient"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_Time():
    assert hasattr(Appointment, "Time")
    descriptor = None
    for klass in Appointment.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_Doctor():
    assert hasattr(Appointment, "Doctor")
    descriptor = None
    for klass in Appointment.__mro__:
        if "Doctor" in klass.__dict__:
            descriptor = klass.__dict__["Doctor"]
            break
    assert isinstance(descriptor, property)



def test_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "CNIC" in params, "Missing parameter 'CNIC'"
    assert "name" in params, "Missing parameter 'name'"

def test_receptionist_has_CNIC():
    assert hasattr(Receptionist, "CNIC")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "CNIC" in klass.__dict__:
            descriptor = klass.__dict__["CNIC"]
            break
    assert isinstance(descriptor, property)

def test_receptionist_has_name():
    assert hasattr(Receptionist, "name")
    descriptor = None
    for klass in Receptionist.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_patients_is_not_abstract():
    assert not inspect.isabstract(Patients)


def test_patients_constructor_exists():
    assert callable(Patients.__init__)


def test_patients_constructor_args():
    sig = inspect.signature(Patients.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Symptoms" in params, "Missing parameter 'Symptoms'"
    assert "History" in params, "Missing parameter 'History'"
    assert "BP" in params, "Missing parameter 'BP'"

def test_patients_has_weight():
    assert hasattr(Patients, "weight")
    descriptor = None
    for klass in Patients.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_patients_has_name():
    assert hasattr(Patients, "name")
    descriptor = None
    for klass in Patients.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_patients_has_Symptoms():
    assert hasattr(Patients, "Symptoms")
    descriptor = None
    for klass in Patients.__mro__:
        if "Symptoms" in klass.__dict__:
            descriptor = klass.__dict__["Symptoms"]
            break
    assert isinstance(descriptor, property)

def test_patients_has_History():
    assert hasattr(Patients, "History")
    descriptor = None
    for klass in Patients.__mro__:
        if "History" in klass.__dict__:
            descriptor = klass.__dict__["History"]
            break
    assert isinstance(descriptor, property)

def test_patients_has_BP():
    assert hasattr(Patients, "BP")
    descriptor = None
    for klass in Patients.__mro__:
        if "BP" in klass.__dict__:
            descriptor = klass.__dict__["BP"]
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
    assert "privateConsultancy" in params, "Missing parameter 'privateConsultancy'"
    assert "timing" in params, "Missing parameter 'timing'"
    assert "specilization" in params, "Missing parameter 'specilization'"

def test_doctor_has_name():
    assert hasattr(Doctor, "name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_privateConsultancy():
    assert hasattr(Doctor, "privateConsultancy")
    descriptor = None
    for klass in Doctor.__mro__:
        if "privateConsultancy" in klass.__dict__:
            descriptor = klass.__dict__["privateConsultancy"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_timing():
    assert hasattr(Doctor, "timing")
    descriptor = None
    for klass in Doctor.__mro__:
        if "timing" in klass.__dict__:
            descriptor = klass.__dict__["timing"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_specilization():
    assert hasattr(Doctor, "specilization")
    descriptor = None
    for klass in Doctor.__mro__:
        if "specilization" in klass.__dict__:
            descriptor = klass.__dict__["specilization"]
            break
    assert isinstance(descriptor, property)



def test_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"

def test_hospital_has_phone():
    assert hasattr(Hospital, "phone")
    descriptor = None
    for klass in Hospital.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
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

def test_hospital_has_name():
    assert hasattr(Hospital, "name")
    descriptor = None
    for klass in Hospital.__mro__:
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
Billing_Report_strategy = st.builds(
    Billing_Report,
    serviceCharges=
        safe_text,
    testCharges=
        safe_text
)
BloodBank_strategy = st.builds(
    BloodBank,
    phone=
        safe_text,
    bloodGroup=
        safe_text
)
Prescription_strategy = st.builds(
    Prescription,
    tests=
        safe_text,
    medicines=
        safe_text
)
Assistant_strategy = st.builds(
    Assistant,
    CNIC=
        safe_text,
    name=
        safe_text
)
PatientProfile_strategy = st.builds(
    PatientProfile,
    name=
        safe_text,
    appointment=
        safe_text
)
DoctorDatabase_strategy = st.builds(
    DoctorDatabase,
    Specialization=
        safe_text,
    doctorName=
        safe_text
)
Appointment_strategy = st.builds(
    Appointment,
    Patient=
        safe_text,
    Time=
        safe_text,
    Doctor=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    CNIC=
        safe_text,
    name=
        safe_text
)
Patients_strategy = st.builds(
    Patients,
    weight=
        st.integers(),
    name=
        safe_text,
    Symptoms=
        safe_text,
    History=
        safe_text,
    BP=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    name=
        safe_text,
    privateConsultancy=
        st.booleans(),
    timing=
        safe_text,
    specilization=
        safe_text
)
Hospital_strategy = st.builds(
    Hospital,
    phone=
        st.integers(),
    address=
        safe_text,
    name=
        safe_text
)

@given(instance=Billing_Report_strategy)
@settings(max_examples=50)
def test_billing_report_instantiation(instance):
    assert isinstance(instance, Billing_Report)



@given(instance=Billing_Report_strategy)
def test_billing_report_serviceCharges_setter(instance):
    original = instance.serviceCharges
    instance.serviceCharges = original
    assert instance.serviceCharges == original



@given(instance=Billing_Report_strategy)
def test_billing_report_testCharges_setter(instance):
    original = instance.testCharges
    instance.testCharges = original
    assert instance.testCharges == original

@given(instance=BloodBank_strategy)
@settings(max_examples=50)
def test_bloodbank_instantiation(instance):
    assert isinstance(instance, BloodBank)



@given(instance=BloodBank_strategy)
def test_bloodbank_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=BloodBank_strategy)
def test_bloodbank_bloodGroup_setter(instance):
    original = instance.bloodGroup
    instance.bloodGroup = original
    assert instance.bloodGroup == original

@given(instance=Prescription_strategy)
@settings(max_examples=50)
def test_prescription_instantiation(instance):
    assert isinstance(instance, Prescription)



@given(instance=Prescription_strategy)
def test_prescription_tests_setter(instance):
    original = instance.tests
    instance.tests = original
    assert instance.tests == original



@given(instance=Prescription_strategy)
def test_prescription_medicines_setter(instance):
    original = instance.medicines
    instance.medicines = original
    assert instance.medicines == original

@given(instance=Assistant_strategy)
@settings(max_examples=50)
def test_assistant_instantiation(instance):
    assert isinstance(instance, Assistant)



@given(instance=Assistant_strategy)
def test_assistant_CNIC_setter(instance):
    original = instance.CNIC
    instance.CNIC = original
    assert instance.CNIC == original



@given(instance=Assistant_strategy)
def test_assistant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PatientProfile_strategy)
@settings(max_examples=50)
def test_patientprofile_instantiation(instance):
    assert isinstance(instance, PatientProfile)



@given(instance=PatientProfile_strategy)
def test_patientprofile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PatientProfile_strategy)
def test_patientprofile_appointment_setter(instance):
    original = instance.appointment
    instance.appointment = original
    assert instance.appointment == original

@given(instance=DoctorDatabase_strategy)
@settings(max_examples=50)
def test_doctordatabase_instantiation(instance):
    assert isinstance(instance, DoctorDatabase)



@given(instance=DoctorDatabase_strategy)
def test_doctordatabase_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=DoctorDatabase_strategy)
def test_doctordatabase_doctorName_setter(instance):
    original = instance.doctorName
    instance.doctorName = original
    assert instance.doctorName == original

@given(instance=Appointment_strategy)
@settings(max_examples=50)
def test_appointment_instantiation(instance):
    assert isinstance(instance, Appointment)



@given(instance=Appointment_strategy)
def test_appointment_Patient_setter(instance):
    original = instance.Patient
    instance.Patient = original
    assert instance.Patient == original



@given(instance=Appointment_strategy)
def test_appointment_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Appointment_strategy)
def test_appointment_Doctor_setter(instance):
    original = instance.Doctor
    instance.Doctor = original
    assert instance.Doctor == original

@given(instance=Receptionist_strategy)
@settings(max_examples=50)
def test_receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



@given(instance=Receptionist_strategy)
def test_receptionist_CNIC_setter(instance):
    original = instance.CNIC
    instance.CNIC = original
    assert instance.CNIC == original



@given(instance=Receptionist_strategy)
def test_receptionist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Patients_strategy)
@settings(max_examples=50)
def test_patients_instantiation(instance):
    assert isinstance(instance, Patients)



@given(instance=Patients_strategy)
def test_patients_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=Patients_strategy)
def test_patients_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patients_strategy)
def test_patients_Symptoms_setter(instance):
    original = instance.Symptoms
    instance.Symptoms = original
    assert instance.Symptoms == original



@given(instance=Patients_strategy)
def test_patients_History_setter(instance):
    original = instance.History
    instance.History = original
    assert instance.History == original



@given(instance=Patients_strategy)
def test_patients_BP_setter(instance):
    original = instance.BP
    instance.BP = original
    assert instance.BP == original

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
def test_doctor_privateConsultancy_setter(instance):
    original = instance.privateConsultancy
    instance.privateConsultancy = original
    assert instance.privateConsultancy == original



@given(instance=Doctor_strategy)
def test_doctor_timing_setter(instance):
    original = instance.timing
    instance.timing = original
    assert instance.timing == original



@given(instance=Doctor_strategy)
def test_doctor_specilization_setter(instance):
    original = instance.specilization
    instance.specilization = original
    assert instance.specilization == original

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
def test_hospital_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Hospital_strategy)
def test_hospital_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
