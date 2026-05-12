import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Generate_Staff_s_Payroll_external,
    Authorise_Service_Improvement_Budget_external,
    Search_Patient_external,
    Create_Patient_appointment_external,
    Maintain_next_of_kind_details_external,
    Set_staff_weekly_Rota_external,
    Maintain_suppliers_external,
    of_ward_s_supplies_external,
    Maintain_ward_s_supplies_external,
    of_Services_Improvement_external,
    of_Monthly_profit_external,
    Register_Patient_payment_external,
    of_Patients_referred_to_the_out_patient_clinic_external,
    Maintain_Patients_referred_to_the_out_patients_clinic_external,
    Maintain_Patients_referred_to_the_hospital_external,
    of_Ward_s_Staff_external,
    Search_Staff_external,
    Maintain_Staff_external,
    Maintain_resources_external,
    of_Patients_on_waiting_list_external,
    of_Patients_in_wards_external,
    of_Patients__medication_external,
    Maintian_Patients__medication_external,
    Maintain_ward_s_Patients_external,
    Accountant_Actor,
    Payee_Actor,
    _Component1,
    Medication,
    OutPatient,
    Appointment,
    InPatient,
    WaitingList,
    Supplier,
    Pharmaceutical,
    Surgical_NonSurgical,
    Supply,
    Requisition,
    Bed,
    Ward,
    RegularDoctor,
    ChargeNurse,
    PersonnelOfficer,
    MedicalDirector,
    EmploymentContract,
    WorkExperience,
    Qualification,
    LocalDoctor,
    NextOfKind,
    Staff,
    Patient,
    Person,
    Patient_Actor,
    Medical_Director_Actor,
    Person_Actor,
    Charge_Nurse_Actor,
    Staff_Actor,
    _Component,
    Personnel_Officer_Actor,
    TypeContract,
    Relationship,
    Sex,
    MaritalStatus,
    SupplyType,
    SalaryPayment,
    Administration,
    Position,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_generate_staff_s_payroll_external_is_not_abstract():
    assert not inspect.isabstract(Generate_Staff_s_Payroll_external)


def test_generate_staff_s_payroll_external_constructor_exists():
    assert callable(Generate_Staff_s_Payroll_external.__init__)


def test_generate_staff_s_payroll_external_constructor_args():
    sig = inspect.signature(Generate_Staff_s_Payroll_external.__init__)
    params = list(sig.parameters.keys())



def test_authorise_service_improvement_budget_external_is_not_abstract():
    assert not inspect.isabstract(Authorise_Service_Improvement_Budget_external)


def test_authorise_service_improvement_budget_external_constructor_exists():
    assert callable(Authorise_Service_Improvement_Budget_external.__init__)


def test_authorise_service_improvement_budget_external_constructor_args():
    sig = inspect.signature(Authorise_Service_Improvement_Budget_external.__init__)
    params = list(sig.parameters.keys())



def test_search_patient_external_is_not_abstract():
    assert not inspect.isabstract(Search_Patient_external)


def test_search_patient_external_constructor_exists():
    assert callable(Search_Patient_external.__init__)


def test_search_patient_external_constructor_args():
    sig = inspect.signature(Search_Patient_external.__init__)
    params = list(sig.parameters.keys())



def test_create_patient_appointment_external_is_not_abstract():
    assert not inspect.isabstract(Create_Patient_appointment_external)


def test_create_patient_appointment_external_constructor_exists():
    assert callable(Create_Patient_appointment_external.__init__)


def test_create_patient_appointment_external_constructor_args():
    sig = inspect.signature(Create_Patient_appointment_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_next_of_kind_details_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_next_of_kind_details_external)


def test_maintain_next_of_kind_details_external_constructor_exists():
    assert callable(Maintain_next_of_kind_details_external.__init__)


def test_maintain_next_of_kind_details_external_constructor_args():
    sig = inspect.signature(Maintain_next_of_kind_details_external.__init__)
    params = list(sig.parameters.keys())



def test_set_staff_weekly_rota_external_is_not_abstract():
    assert not inspect.isabstract(Set_staff_weekly_Rota_external)


def test_set_staff_weekly_rota_external_constructor_exists():
    assert callable(Set_staff_weekly_Rota_external.__init__)


def test_set_staff_weekly_rota_external_constructor_args():
    sig = inspect.signature(Set_staff_weekly_Rota_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_suppliers_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_suppliers_external)


def test_maintain_suppliers_external_constructor_exists():
    assert callable(Maintain_suppliers_external.__init__)


def test_maintain_suppliers_external_constructor_args():
    sig = inspect.signature(Maintain_suppliers_external.__init__)
    params = list(sig.parameters.keys())



def test_of_ward_s_supplies_external_is_not_abstract():
    assert not inspect.isabstract(of_ward_s_supplies_external)


def test_of_ward_s_supplies_external_constructor_exists():
    assert callable(of_ward_s_supplies_external.__init__)


def test_of_ward_s_supplies_external_constructor_args():
    sig = inspect.signature(of_ward_s_supplies_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_ward_s_supplies_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_ward_s_supplies_external)


def test_maintain_ward_s_supplies_external_constructor_exists():
    assert callable(Maintain_ward_s_supplies_external.__init__)


def test_maintain_ward_s_supplies_external_constructor_args():
    sig = inspect.signature(Maintain_ward_s_supplies_external.__init__)
    params = list(sig.parameters.keys())



def test_of_services_improvement_external_is_not_abstract():
    assert not inspect.isabstract(of_Services_Improvement_external)


def test_of_services_improvement_external_constructor_exists():
    assert callable(of_Services_Improvement_external.__init__)


def test_of_services_improvement_external_constructor_args():
    sig = inspect.signature(of_Services_Improvement_external.__init__)
    params = list(sig.parameters.keys())



def test_of_monthly_profit_external_is_not_abstract():
    assert not inspect.isabstract(of_Monthly_profit_external)


def test_of_monthly_profit_external_constructor_exists():
    assert callable(of_Monthly_profit_external.__init__)


def test_of_monthly_profit_external_constructor_args():
    sig = inspect.signature(of_Monthly_profit_external.__init__)
    params = list(sig.parameters.keys())



def test_register_patient_payment_external_is_not_abstract():
    assert not inspect.isabstract(Register_Patient_payment_external)


def test_register_patient_payment_external_constructor_exists():
    assert callable(Register_Patient_payment_external.__init__)


def test_register_patient_payment_external_constructor_args():
    sig = inspect.signature(Register_Patient_payment_external.__init__)
    params = list(sig.parameters.keys())



def test_of_patients_referred_to_the_out_patient_clinic_external_is_not_abstract():
    assert not inspect.isabstract(of_Patients_referred_to_the_out_patient_clinic_external)


def test_of_patients_referred_to_the_out_patient_clinic_external_constructor_exists():
    assert callable(of_Patients_referred_to_the_out_patient_clinic_external.__init__)


def test_of_patients_referred_to_the_out_patient_clinic_external_constructor_args():
    sig = inspect.signature(of_Patients_referred_to_the_out_patient_clinic_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_patients_referred_to_the_out_patients_clinic_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_Patients_referred_to_the_out_patients_clinic_external)


def test_maintain_patients_referred_to_the_out_patients_clinic_external_constructor_exists():
    assert callable(Maintain_Patients_referred_to_the_out_patients_clinic_external.__init__)


def test_maintain_patients_referred_to_the_out_patients_clinic_external_constructor_args():
    sig = inspect.signature(Maintain_Patients_referred_to_the_out_patients_clinic_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_patients_referred_to_the_hospital_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_Patients_referred_to_the_hospital_external)


def test_maintain_patients_referred_to_the_hospital_external_constructor_exists():
    assert callable(Maintain_Patients_referred_to_the_hospital_external.__init__)


def test_maintain_patients_referred_to_the_hospital_external_constructor_args():
    sig = inspect.signature(Maintain_Patients_referred_to_the_hospital_external.__init__)
    params = list(sig.parameters.keys())



def test_of_ward_s_staff_external_is_not_abstract():
    assert not inspect.isabstract(of_Ward_s_Staff_external)


def test_of_ward_s_staff_external_constructor_exists():
    assert callable(of_Ward_s_Staff_external.__init__)


def test_of_ward_s_staff_external_constructor_args():
    sig = inspect.signature(of_Ward_s_Staff_external.__init__)
    params = list(sig.parameters.keys())



def test_search_staff_external_is_not_abstract():
    assert not inspect.isabstract(Search_Staff_external)


def test_search_staff_external_constructor_exists():
    assert callable(Search_Staff_external.__init__)


def test_search_staff_external_constructor_args():
    sig = inspect.signature(Search_Staff_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_staff_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_Staff_external)


def test_maintain_staff_external_constructor_exists():
    assert callable(Maintain_Staff_external.__init__)


def test_maintain_staff_external_constructor_args():
    sig = inspect.signature(Maintain_Staff_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_resources_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_resources_external)


def test_maintain_resources_external_constructor_exists():
    assert callable(Maintain_resources_external.__init__)


def test_maintain_resources_external_constructor_args():
    sig = inspect.signature(Maintain_resources_external.__init__)
    params = list(sig.parameters.keys())



def test_of_patients_on_waiting_list_external_is_not_abstract():
    assert not inspect.isabstract(of_Patients_on_waiting_list_external)


def test_of_patients_on_waiting_list_external_constructor_exists():
    assert callable(of_Patients_on_waiting_list_external.__init__)


def test_of_patients_on_waiting_list_external_constructor_args():
    sig = inspect.signature(of_Patients_on_waiting_list_external.__init__)
    params = list(sig.parameters.keys())



def test_of_patients_in_wards_external_is_not_abstract():
    assert not inspect.isabstract(of_Patients_in_wards_external)


def test_of_patients_in_wards_external_constructor_exists():
    assert callable(of_Patients_in_wards_external.__init__)


def test_of_patients_in_wards_external_constructor_args():
    sig = inspect.signature(of_Patients_in_wards_external.__init__)
    params = list(sig.parameters.keys())



def test_of_patients__medication_external_is_not_abstract():
    assert not inspect.isabstract(of_Patients__medication_external)


def test_of_patients__medication_external_constructor_exists():
    assert callable(of_Patients__medication_external.__init__)


def test_of_patients__medication_external_constructor_args():
    sig = inspect.signature(of_Patients__medication_external.__init__)
    params = list(sig.parameters.keys())



def test_maintian_patients__medication_external_is_not_abstract():
    assert not inspect.isabstract(Maintian_Patients__medication_external)


def test_maintian_patients__medication_external_constructor_exists():
    assert callable(Maintian_Patients__medication_external.__init__)


def test_maintian_patients__medication_external_constructor_args():
    sig = inspect.signature(Maintian_Patients__medication_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_ward_s_patients_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_ward_s_Patients_external)


def test_maintain_ward_s_patients_external_constructor_exists():
    assert callable(Maintain_ward_s_Patients_external.__init__)


def test_maintain_ward_s_patients_external_constructor_args():
    sig = inspect.signature(Maintain_ward_s_Patients_external.__init__)
    params = list(sig.parameters.keys())



def test_accountant_actor_is_not_abstract():
    assert not inspect.isabstract(Accountant_Actor)


def test_accountant_actor_constructor_exists():
    assert callable(Accountant_Actor.__init__)


def test_accountant_actor_constructor_args():
    sig = inspect.signature(Accountant_Actor.__init__)
    params = list(sig.parameters.keys())



def test_payee_actor_is_not_abstract():
    assert not inspect.isabstract(Payee_Actor)


def test_payee_actor_constructor_exists():
    assert callable(Payee_Actor.__init__)


def test_payee_actor_constructor_args():
    sig = inspect.signature(Payee_Actor.__init__)
    params = list(sig.parameters.keys())



def test__component1_is_not_abstract():
    assert not inspect.isabstract(_Component1)


def test__component1_constructor_exists():
    assert callable(_Component1.__init__)


def test__component1_constructor_args():
    sig = inspect.signature(_Component1.__init__)
    params = list(sig.parameters.keys())



def test_medication_is_not_abstract():
    assert not inspect.isabstract(Medication)


def test_medication_constructor_exists():
    assert callable(Medication.__init__)


def test_medication_constructor_args():
    sig = inspect.signature(Medication.__init__)
    params = list(sig.parameters.keys())
    assert "start_date" in params, "Missing parameter 'start_date'"
    assert "units_per_day" in params, "Missing parameter 'units_per_day'"
    assert "drug" in params, "Missing parameter 'drug'"
    assert "finish_date" in params, "Missing parameter 'finish_date'"
    assert "administration" in params, "Missing parameter 'administration'"
    assert "patient" in params, "Missing parameter 'patient'"

def test_medication_has_start_date():
    assert hasattr(Medication, "start_date")
    descriptor = None
    for klass in Medication.__mro__:
        if "start_date" in klass.__dict__:
            descriptor = klass.__dict__["start_date"]
            break
    assert isinstance(descriptor, property)

def test_medication_has_units_per_day():
    assert hasattr(Medication, "units_per_day")
    descriptor = None
    for klass in Medication.__mro__:
        if "units_per_day" in klass.__dict__:
            descriptor = klass.__dict__["units_per_day"]
            break
    assert isinstance(descriptor, property)

def test_medication_has_drug():
    assert hasattr(Medication, "drug")
    descriptor = None
    for klass in Medication.__mro__:
        if "drug" in klass.__dict__:
            descriptor = klass.__dict__["drug"]
            break
    assert isinstance(descriptor, property)

def test_medication_has_finish_date():
    assert hasattr(Medication, "finish_date")
    descriptor = None
    for klass in Medication.__mro__:
        if "finish_date" in klass.__dict__:
            descriptor = klass.__dict__["finish_date"]
            break
    assert isinstance(descriptor, property)

def test_medication_has_administration():
    assert hasattr(Medication, "administration")
    descriptor = None
    for klass in Medication.__mro__:
        if "administration" in klass.__dict__:
            descriptor = klass.__dict__["administration"]
            break
    assert isinstance(descriptor, property)

def test_medication_has_patient():
    assert hasattr(Medication, "patient")
    descriptor = None
    for klass in Medication.__mro__:
        if "patient" in klass.__dict__:
            descriptor = klass.__dict__["patient"]
            break
    assert isinstance(descriptor, property)



def test_outpatient_is_not_abstract():
    assert not inspect.isabstract(OutPatient)


def test_outpatient_constructor_exists():
    assert callable(OutPatient.__init__)


def test_outpatient_constructor_args():
    sig = inspect.signature(OutPatient.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "patient" in params, "Missing parameter 'patient'"
    assert "date" in params, "Missing parameter 'date'"

def test_outpatient_has_location():
    assert hasattr(OutPatient, "location")
    descriptor = None
    for klass in OutPatient.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_outpatient_has_patient():
    assert hasattr(OutPatient, "patient")
    descriptor = None
    for klass in OutPatient.__mro__:
        if "patient" in klass.__dict__:
            descriptor = klass.__dict__["patient"]
            break
    assert isinstance(descriptor, property)

def test_outpatient_has_date():
    assert hasattr(OutPatient, "date")
    descriptor = None
    for klass in OutPatient.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_appointment_is_not_abstract():
    assert not inspect.isabstract(Appointment)


def test_appointment_constructor_exists():
    assert callable(Appointment.__init__)


def test_appointment_constructor_args():
    sig = inspect.signature(Appointment.__init__)
    params = list(sig.parameters.keys())
    assert "doctor" in params, "Missing parameter 'doctor'"
    assert "date" in params, "Missing parameter 'date'"
    assert "room" in params, "Missing parameter 'room'"
    assert "patient" in params, "Missing parameter 'patient'"
    assert "num" in params, "Missing parameter 'num'"

def test_appointment_has_doctor():
    assert hasattr(Appointment, "doctor")
    descriptor = None
    for klass in Appointment.__mro__:
        if "doctor" in klass.__dict__:
            descriptor = klass.__dict__["doctor"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_date():
    assert hasattr(Appointment, "date")
    descriptor = None
    for klass in Appointment.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_room():
    assert hasattr(Appointment, "room")
    descriptor = None
    for klass in Appointment.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_patient():
    assert hasattr(Appointment, "patient")
    descriptor = None
    for klass in Appointment.__mro__:
        if "patient" in klass.__dict__:
            descriptor = klass.__dict__["patient"]
            break
    assert isinstance(descriptor, property)

def test_appointment_has_num():
    assert hasattr(Appointment, "num")
    descriptor = None
    for klass in Appointment.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_inpatient_is_not_abstract():
    assert not inspect.isabstract(InPatient)


def test_inpatient_constructor_exists():
    assert callable(InPatient.__init__)


def test_inpatient_constructor_args():
    sig = inspect.signature(InPatient.__init__)
    params = list(sig.parameters.keys())
    assert "patient" in params, "Missing parameter 'patient'"
    assert "date_actual_leave" in params, "Missing parameter 'date_actual_leave'"
    assert "ward_required" in params, "Missing parameter 'ward_required'"
    assert "bed" in params, "Missing parameter 'bed'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "date_place" in params, "Missing parameter 'date_place'"
    assert "date_expected_leave" in params, "Missing parameter 'date_expected_leave'"

def test_inpatient_has_patient():
    assert hasattr(InPatient, "patient")
    descriptor = None
    for klass in InPatient.__mro__:
        if "patient" in klass.__dict__:
            descriptor = klass.__dict__["patient"]
            break
    assert isinstance(descriptor, property)

def test_inpatient_has_date_actual_leave():
    assert hasattr(InPatient, "date_actual_leave")
    descriptor = None
    for klass in InPatient.__mro__:
        if "date_actual_leave" in klass.__dict__:
            descriptor = klass.__dict__["date_actual_leave"]
            break
    assert isinstance(descriptor, property)

def test_inpatient_has_ward_required():
    assert hasattr(InPatient, "ward_required")
    descriptor = None
    for klass in InPatient.__mro__:
        if "ward_required" in klass.__dict__:
            descriptor = klass.__dict__["ward_required"]
            break
    assert isinstance(descriptor, property)

def test_inpatient_has_bed():
    assert hasattr(InPatient, "bed")
    descriptor = None
    for klass in InPatient.__mro__:
        if "bed" in klass.__dict__:
            descriptor = klass.__dict__["bed"]
            break
    assert isinstance(descriptor, property)

def test_inpatient_has_duration():
    assert hasattr(InPatient, "duration")
    descriptor = None
    for klass in InPatient.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_inpatient_has_date_place():
    assert hasattr(InPatient, "date_place")
    descriptor = None
    for klass in InPatient.__mro__:
        if "date_place" in klass.__dict__:
            descriptor = klass.__dict__["date_place"]
            break
    assert isinstance(descriptor, property)

def test_inpatient_has_date_expected_leave():
    assert hasattr(InPatient, "date_expected_leave")
    descriptor = None
    for klass in InPatient.__mro__:
        if "date_expected_leave" in klass.__dict__:
            descriptor = klass.__dict__["date_expected_leave"]
            break
    assert isinstance(descriptor, property)



def test_waitinglist_is_not_abstract():
    assert not inspect.isabstract(WaitingList)


def test_waitinglist_constructor_exists():
    assert callable(WaitingList.__init__)


def test_waitinglist_constructor_args():
    sig = inspect.signature(WaitingList.__init__)
    params = list(sig.parameters.keys())
    assert "patient" in params, "Missing parameter 'patient'"
    assert "ward_required" in params, "Missing parameter 'ward_required'"
    assert "date" in params, "Missing parameter 'date'"

def test_waitinglist_has_patient():
    assert hasattr(WaitingList, "patient")
    descriptor = None
    for klass in WaitingList.__mro__:
        if "patient" in klass.__dict__:
            descriptor = klass.__dict__["patient"]
            break
    assert isinstance(descriptor, property)

def test_waitinglist_has_ward_required():
    assert hasattr(WaitingList, "ward_required")
    descriptor = None
    for klass in WaitingList.__mro__:
        if "ward_required" in klass.__dict__:
            descriptor = klass.__dict__["ward_required"]
            break
    assert isinstance(descriptor, property)

def test_waitinglist_has_date():
    assert hasattr(WaitingList, "date")
    descriptor = None
    for klass in WaitingList.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_supplier_is_not_abstract():
    assert not inspect.isabstract(Supplier)


def test_supplier_constructor_exists():
    assert callable(Supplier.__init__)


def test_supplier_constructor_args():
    sig = inspect.signature(Supplier.__init__)
    params = list(sig.parameters.keys())
    assert "fax" in params, "Missing parameter 'fax'"
    assert "num" in params, "Missing parameter 'num'"

def test_supplier_has_fax():
    assert hasattr(Supplier, "fax")
    descriptor = None
    for klass in Supplier.__mro__:
        if "fax" in klass.__dict__:
            descriptor = klass.__dict__["fax"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_num():
    assert hasattr(Supplier, "num")
    descriptor = None
    for klass in Supplier.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_pharmaceutical_is_not_abstract():
    assert not inspect.isabstract(Pharmaceutical)


def test_pharmaceutical_constructor_exists():
    assert callable(Pharmaceutical.__init__)


def test_pharmaceutical_constructor_args():
    sig = inspect.signature(Pharmaceutical.__init__)
    params = list(sig.parameters.keys())
    assert "method_of_administration" in params, "Missing parameter 'method_of_administration'"
    assert "dosage" in params, "Missing parameter 'dosage'"

def test_pharmaceutical_has_method_of_administration():
    assert hasattr(Pharmaceutical, "method_of_administration")
    descriptor = None
    for klass in Pharmaceutical.__mro__:
        if "method_of_administration" in klass.__dict__:
            descriptor = klass.__dict__["method_of_administration"]
            break
    assert isinstance(descriptor, property)

def test_pharmaceutical_has_dosage():
    assert hasattr(Pharmaceutical, "dosage")
    descriptor = None
    for klass in Pharmaceutical.__mro__:
        if "dosage" in klass.__dict__:
            descriptor = klass.__dict__["dosage"]
            break
    assert isinstance(descriptor, property)



def test_surgical_nonsurgical_is_not_abstract():
    assert not inspect.isabstract(Surgical_NonSurgical)


def test_surgical_nonsurgical_constructor_exists():
    assert callable(Surgical_NonSurgical.__init__)


def test_surgical_nonsurgical_constructor_args():
    sig = inspect.signature(Surgical_NonSurgical.__init__)
    params = list(sig.parameters.keys())
    assert "supply_type" in params, "Missing parameter 'supply_type'"

def test_surgical_nonsurgical_has_supply_type():
    assert hasattr(Surgical_NonSurgical, "supply_type")
    descriptor = None
    for klass in Surgical_NonSurgical.__mro__:
        if "supply_type" in klass.__dict__:
            descriptor = klass.__dict__["supply_type"]
            break
    assert isinstance(descriptor, property)



def test_supply_is_not_abstract():
    assert not inspect.isabstract(Supply)


def test_supply_constructor_exists():
    assert callable(Supply.__init__)


def test_supply_constructor_args():
    sig = inspect.signature(Supply.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "cost_per_unit" in params, "Missing parameter 'cost_per_unit'"
    assert "reorder_level" in params, "Missing parameter 'reorder_level'"
    assert "description" in params, "Missing parameter 'description'"
    assert "num" in params, "Missing parameter 'num'"
    assert "stock" in params, "Missing parameter 'stock'"

def test_supply_has_name():
    assert hasattr(Supply, "name")
    descriptor = None
    for klass in Supply.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_supply_has_cost_per_unit():
    assert hasattr(Supply, "cost_per_unit")
    descriptor = None
    for klass in Supply.__mro__:
        if "cost_per_unit" in klass.__dict__:
            descriptor = klass.__dict__["cost_per_unit"]
            break
    assert isinstance(descriptor, property)

def test_supply_has_reorder_level():
    assert hasattr(Supply, "reorder_level")
    descriptor = None
    for klass in Supply.__mro__:
        if "reorder_level" in klass.__dict__:
            descriptor = klass.__dict__["reorder_level"]
            break
    assert isinstance(descriptor, property)

def test_supply_has_description():
    assert hasattr(Supply, "description")
    descriptor = None
    for klass in Supply.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_supply_has_num():
    assert hasattr(Supply, "num")
    descriptor = None
    for klass in Supply.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_supply_has_stock():
    assert hasattr(Supply, "stock")
    descriptor = None
    for klass in Supply.__mro__:
        if "stock" in klass.__dict__:
            descriptor = klass.__dict__["stock"]
            break
    assert isinstance(descriptor, property)



def test_requisition_is_not_abstract():
    assert not inspect.isabstract(Requisition)


def test_requisition_constructor_exists():
    assert callable(Requisition.__init__)


def test_requisition_constructor_args():
    sig = inspect.signature(Requisition.__init__)
    params = list(sig.parameters.keys())
    assert "date_ordered" in params, "Missing parameter 'date_ordered'"
    assert "quantity_required" in params, "Missing parameter 'quantity_required'"
    assert "responsable" in params, "Missing parameter 'responsable'"
    assert "supply" in params, "Missing parameter 'supply'"
    assert "num" in params, "Missing parameter 'num'"
    assert "ward" in params, "Missing parameter 'ward'"
    assert "date_delivered" in params, "Missing parameter 'date_delivered'"

def test_requisition_has_date_ordered():
    assert hasattr(Requisition, "date_ordered")
    descriptor = None
    for klass in Requisition.__mro__:
        if "date_ordered" in klass.__dict__:
            descriptor = klass.__dict__["date_ordered"]
            break
    assert isinstance(descriptor, property)

def test_requisition_has_quantity_required():
    assert hasattr(Requisition, "quantity_required")
    descriptor = None
    for klass in Requisition.__mro__:
        if "quantity_required" in klass.__dict__:
            descriptor = klass.__dict__["quantity_required"]
            break
    assert isinstance(descriptor, property)

def test_requisition_has_responsable():
    assert hasattr(Requisition, "responsable")
    descriptor = None
    for klass in Requisition.__mro__:
        if "responsable" in klass.__dict__:
            descriptor = klass.__dict__["responsable"]
            break
    assert isinstance(descriptor, property)

def test_requisition_has_supply():
    assert hasattr(Requisition, "supply")
    descriptor = None
    for klass in Requisition.__mro__:
        if "supply" in klass.__dict__:
            descriptor = klass.__dict__["supply"]
            break
    assert isinstance(descriptor, property)

def test_requisition_has_num():
    assert hasattr(Requisition, "num")
    descriptor = None
    for klass in Requisition.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_requisition_has_ward():
    assert hasattr(Requisition, "ward")
    descriptor = None
    for klass in Requisition.__mro__:
        if "ward" in klass.__dict__:
            descriptor = klass.__dict__["ward"]
            break
    assert isinstance(descriptor, property)

def test_requisition_has_date_delivered():
    assert hasattr(Requisition, "date_delivered")
    descriptor = None
    for klass in Requisition.__mro__:
        if "date_delivered" in klass.__dict__:
            descriptor = klass.__dict__["date_delivered"]
            break
    assert isinstance(descriptor, property)



def test_bed_is_not_abstract():
    assert not inspect.isabstract(Bed)


def test_bed_constructor_exists():
    assert callable(Bed.__init__)


def test_bed_constructor_args():
    sig = inspect.signature(Bed.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"

def test_bed_has_num():
    assert hasattr(Bed, "num")
    descriptor = None
    for klass in Bed.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_ward_is_not_abstract():
    assert not inspect.isabstract(Ward)


def test_ward_constructor_exists():
    assert callable(Ward.__init__)


def test_ward_constructor_args():
    sig = inspect.signature(Ward.__init__)
    params = list(sig.parameters.keys())
    assert "staff" in params, "Missing parameter 'staff'"
    assert "location" in params, "Missing parameter 'location'"
    assert "num" in params, "Missing parameter 'num'"
    assert "telephone_extension" in params, "Missing parameter 'telephone_extension'"
    assert "name" in params, "Missing parameter 'name'"
    assert "responsable" in params, "Missing parameter 'responsable'"

def test_ward_has_staff():
    assert hasattr(Ward, "staff")
    descriptor = None
    for klass in Ward.__mro__:
        if "staff" in klass.__dict__:
            descriptor = klass.__dict__["staff"]
            break
    assert isinstance(descriptor, property)

def test_ward_has_location():
    assert hasattr(Ward, "location")
    descriptor = None
    for klass in Ward.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_ward_has_num():
    assert hasattr(Ward, "num")
    descriptor = None
    for klass in Ward.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_ward_has_telephone_extension():
    assert hasattr(Ward, "telephone_extension")
    descriptor = None
    for klass in Ward.__mro__:
        if "telephone_extension" in klass.__dict__:
            descriptor = klass.__dict__["telephone_extension"]
            break
    assert isinstance(descriptor, property)

def test_ward_has_name():
    assert hasattr(Ward, "name")
    descriptor = None
    for klass in Ward.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ward_has_responsable():
    assert hasattr(Ward, "responsable")
    descriptor = None
    for klass in Ward.__mro__:
        if "responsable" in klass.__dict__:
            descriptor = klass.__dict__["responsable"]
            break
    assert isinstance(descriptor, property)



def test_regulardoctor_is_not_abstract():
    assert not inspect.isabstract(RegularDoctor)


def test_regulardoctor_constructor_exists():
    assert callable(RegularDoctor.__init__)


def test_regulardoctor_constructor_args():
    sig = inspect.signature(RegularDoctor.__init__)
    params = list(sig.parameters.keys())



def test_chargenurse_is_not_abstract():
    assert not inspect.isabstract(ChargeNurse)


def test_chargenurse_constructor_exists():
    assert callable(ChargeNurse.__init__)


def test_chargenurse_constructor_args():
    sig = inspect.signature(ChargeNurse.__init__)
    params = list(sig.parameters.keys())



def test_personnelofficer_is_not_abstract():
    assert not inspect.isabstract(PersonnelOfficer)


def test_personnelofficer_constructor_exists():
    assert callable(PersonnelOfficer.__init__)


def test_personnelofficer_constructor_args():
    sig = inspect.signature(PersonnelOfficer.__init__)
    params = list(sig.parameters.keys())



def test_medicaldirector_is_not_abstract():
    assert not inspect.isabstract(MedicalDirector)


def test_medicaldirector_constructor_exists():
    assert callable(MedicalDirector.__init__)


def test_medicaldirector_constructor_args():
    sig = inspect.signature(MedicalDirector.__init__)
    params = list(sig.parameters.keys())



def test_employmentcontract_is_not_abstract():
    assert not inspect.isabstract(EmploymentContract)


def test_employmentcontract_constructor_exists():
    assert callable(EmploymentContract.__init__)


def test_employmentcontract_constructor_args():
    sig = inspect.signature(EmploymentContract.__init__)
    params = list(sig.parameters.keys())
    assert "number_hours_per_week" in params, "Missing parameter 'number_hours_per_week'"
    assert "type_contract" in params, "Missing parameter 'type_contract'"
    assert "salary_payment" in params, "Missing parameter 'salary_payment'"

def test_employmentcontract_has_number_hours_per_week():
    assert hasattr(EmploymentContract, "number_hours_per_week")
    descriptor = None
    for klass in EmploymentContract.__mro__:
        if "number_hours_per_week" in klass.__dict__:
            descriptor = klass.__dict__["number_hours_per_week"]
            break
    assert isinstance(descriptor, property)

def test_employmentcontract_has_type_contract():
    assert hasattr(EmploymentContract, "type_contract")
    descriptor = None
    for klass in EmploymentContract.__mro__:
        if "type_contract" in klass.__dict__:
            descriptor = klass.__dict__["type_contract"]
            break
    assert isinstance(descriptor, property)

def test_employmentcontract_has_salary_payment():
    assert hasattr(EmploymentContract, "salary_payment")
    descriptor = None
    for klass in EmploymentContract.__mro__:
        if "salary_payment" in klass.__dict__:
            descriptor = klass.__dict__["salary_payment"]
            break
    assert isinstance(descriptor, property)



def test_workexperience_is_not_abstract():
    assert not inspect.isabstract(WorkExperience)


def test_workexperience_constructor_exists():
    assert callable(WorkExperience.__init__)


def test_workexperience_constructor_args():
    sig = inspect.signature(WorkExperience.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"
    assert "organization_name" in params, "Missing parameter 'organization_name'"
    assert "finish_date" in params, "Missing parameter 'finish_date'"
    assert "start_date" in params, "Missing parameter 'start_date'"

def test_workexperience_has_position():
    assert hasattr(WorkExperience, "position")
    descriptor = None
    for klass in WorkExperience.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_workexperience_has_organization_name():
    assert hasattr(WorkExperience, "organization_name")
    descriptor = None
    for klass in WorkExperience.__mro__:
        if "organization_name" in klass.__dict__:
            descriptor = klass.__dict__["organization_name"]
            break
    assert isinstance(descriptor, property)

def test_workexperience_has_finish_date():
    assert hasattr(WorkExperience, "finish_date")
    descriptor = None
    for klass in WorkExperience.__mro__:
        if "finish_date" in klass.__dict__:
            descriptor = klass.__dict__["finish_date"]
            break
    assert isinstance(descriptor, property)

def test_workexperience_has_start_date():
    assert hasattr(WorkExperience, "start_date")
    descriptor = None
    for klass in WorkExperience.__mro__:
        if "start_date" in klass.__dict__:
            descriptor = klass.__dict__["start_date"]
            break
    assert isinstance(descriptor, property)



def test_qualification_is_not_abstract():
    assert not inspect.isabstract(Qualification)


def test_qualification_constructor_exists():
    assert callable(Qualification.__init__)


def test_qualification_constructor_args():
    sig = inspect.signature(Qualification.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "type" in params, "Missing parameter 'type'"
    assert "institution_name" in params, "Missing parameter 'institution_name'"

def test_qualification_has_date():
    assert hasattr(Qualification, "date")
    descriptor = None
    for klass in Qualification.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_qualification_has_type():
    assert hasattr(Qualification, "type")
    descriptor = None
    for klass in Qualification.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_qualification_has_institution_name():
    assert hasattr(Qualification, "institution_name")
    descriptor = None
    for klass in Qualification.__mro__:
        if "institution_name" in klass.__dict__:
            descriptor = klass.__dict__["institution_name"]
            break
    assert isinstance(descriptor, property)



def test_localdoctor_is_not_abstract():
    assert not inspect.isabstract(LocalDoctor)


def test_localdoctor_constructor_exists():
    assert callable(LocalDoctor.__init__)


def test_localdoctor_constructor_args():
    sig = inspect.signature(LocalDoctor.__init__)
    params = list(sig.parameters.keys())
    assert "clinic_number" in params, "Missing parameter 'clinic_number'"

def test_localdoctor_has_clinic_number():
    assert hasattr(LocalDoctor, "clinic_number")
    descriptor = None
    for klass in LocalDoctor.__mro__:
        if "clinic_number" in klass.__dict__:
            descriptor = klass.__dict__["clinic_number"]
            break
    assert isinstance(descriptor, property)



def test_nextofkind_is_not_abstract():
    assert not inspect.isabstract(NextOfKind)


def test_nextofkind_constructor_exists():
    assert callable(NextOfKind.__init__)


def test_nextofkind_constructor_args():
    sig = inspect.signature(NextOfKind.__init__)
    params = list(sig.parameters.keys())
    assert "relationship" in params, "Missing parameter 'relationship'"

def test_nextofkind_has_relationship():
    assert hasattr(NextOfKind, "relationship")
    descriptor = None
    for klass in NextOfKind.__mro__:
        if "relationship" in klass.__dict__:
            descriptor = klass.__dict__["relationship"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "current_salary" in params, "Missing parameter 'current_salary'"
    assert "salary_scale" in params, "Missing parameter 'salary_scale'"
    assert "work_experience" in params, "Missing parameter 'work_experience'"
    assert "employment_contract" in params, "Missing parameter 'employment_contract'"
    assert "position" in params, "Missing parameter 'position'"
    assert "num" in params, "Missing parameter 'num'"
    assert "nin" in params, "Missing parameter 'nin'"
    assert "qualification" in params, "Missing parameter 'qualification'"

def test_staff_has_current_salary():
    assert hasattr(Staff, "current_salary")
    descriptor = None
    for klass in Staff.__mro__:
        if "current_salary" in klass.__dict__:
            descriptor = klass.__dict__["current_salary"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_salary_scale():
    assert hasattr(Staff, "salary_scale")
    descriptor = None
    for klass in Staff.__mro__:
        if "salary_scale" in klass.__dict__:
            descriptor = klass.__dict__["salary_scale"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_work_experience():
    assert hasattr(Staff, "work_experience")
    descriptor = None
    for klass in Staff.__mro__:
        if "work_experience" in klass.__dict__:
            descriptor = klass.__dict__["work_experience"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_employment_contract():
    assert hasattr(Staff, "employment_contract")
    descriptor = None
    for klass in Staff.__mro__:
        if "employment_contract" in klass.__dict__:
            descriptor = klass.__dict__["employment_contract"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_position():
    assert hasattr(Staff, "position")
    descriptor = None
    for klass in Staff.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_num():
    assert hasattr(Staff, "num")
    descriptor = None
    for klass in Staff.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_nin():
    assert hasattr(Staff, "nin")
    descriptor = None
    for klass in Staff.__mro__:
        if "nin" in klass.__dict__:
            descriptor = klass.__dict__["nin"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_qualification():
    assert hasattr(Staff, "qualification")
    descriptor = None
    for klass in Staff.__mro__:
        if "qualification" in klass.__dict__:
            descriptor = klass.__dict__["qualification"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "marital_status" in params, "Missing parameter 'marital_status'"
    assert "local_doctor" in params, "Missing parameter 'local_doctor'"
    assert "next_of_kind" in params, "Missing parameter 'next_of_kind'"

def test_patient_has_num():
    assert hasattr(Patient, "num")
    descriptor = None
    for klass in Patient.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_marital_status():
    assert hasattr(Patient, "marital_status")
    descriptor = None
    for klass in Patient.__mro__:
        if "marital_status" in klass.__dict__:
            descriptor = klass.__dict__["marital_status"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_local_doctor():
    assert hasattr(Patient, "local_doctor")
    descriptor = None
    for klass in Patient.__mro__:
        if "local_doctor" in klass.__dict__:
            descriptor = klass.__dict__["local_doctor"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_next_of_kind():
    assert hasattr(Patient, "next_of_kind")
    descriptor = None
    for klass in Patient.__mro__:
        if "next_of_kind" in klass.__dict__:
            descriptor = klass.__dict__["next_of_kind"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "first_name" in params, "Missing parameter 'first_name'"
    assert "date_of_birth" in params, "Missing parameter 'date_of_birth'"
    assert "last_name" in params, "Missing parameter 'last_name'"
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "sex" in params, "Missing parameter 'sex'"

def test_person_has_address():
    assert hasattr(Person, "address")
    descriptor = None
    for klass in Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_person_has_first_name():
    assert hasattr(Person, "first_name")
    descriptor = None
    for klass in Person.__mro__:
        if "first_name" in klass.__dict__:
            descriptor = klass.__dict__["first_name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_date_of_birth():
    assert hasattr(Person, "date_of_birth")
    descriptor = None
    for klass in Person.__mro__:
        if "date_of_birth" in klass.__dict__:
            descriptor = klass.__dict__["date_of_birth"]
            break
    assert isinstance(descriptor, property)

def test_person_has_last_name():
    assert hasattr(Person, "last_name")
    descriptor = None
    for klass in Person.__mro__:
        if "last_name" in klass.__dict__:
            descriptor = klass.__dict__["last_name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_telephone():
    assert hasattr(Person, "telephone")
    descriptor = None
    for klass in Person.__mro__:
        if "telephone" in klass.__dict__:
            descriptor = klass.__dict__["telephone"]
            break
    assert isinstance(descriptor, property)

def test_person_has_sex():
    assert hasattr(Person, "sex")
    descriptor = None
    for klass in Person.__mro__:
        if "sex" in klass.__dict__:
            descriptor = klass.__dict__["sex"]
            break
    assert isinstance(descriptor, property)



def test_patient_actor_is_not_abstract():
    assert not inspect.isabstract(Patient_Actor)


def test_patient_actor_constructor_exists():
    assert callable(Patient_Actor.__init__)


def test_patient_actor_constructor_args():
    sig = inspect.signature(Patient_Actor.__init__)
    params = list(sig.parameters.keys())



def test_medical_director_actor_is_not_abstract():
    assert not inspect.isabstract(Medical_Director_Actor)


def test_medical_director_actor_constructor_exists():
    assert callable(Medical_Director_Actor.__init__)


def test_medical_director_actor_constructor_args():
    sig = inspect.signature(Medical_Director_Actor.__init__)
    params = list(sig.parameters.keys())



def test_person_actor_is_not_abstract():
    assert not inspect.isabstract(Person_Actor)


def test_person_actor_constructor_exists():
    assert callable(Person_Actor.__init__)


def test_person_actor_constructor_args():
    sig = inspect.signature(Person_Actor.__init__)
    params = list(sig.parameters.keys())



def test_charge_nurse_actor_is_not_abstract():
    assert not inspect.isabstract(Charge_Nurse_Actor)


def test_charge_nurse_actor_constructor_exists():
    assert callable(Charge_Nurse_Actor.__init__)


def test_charge_nurse_actor_constructor_args():
    sig = inspect.signature(Charge_Nurse_Actor.__init__)
    params = list(sig.parameters.keys())



def test_staff_actor_is_not_abstract():
    assert not inspect.isabstract(Staff_Actor)


def test_staff_actor_constructor_exists():
    assert callable(Staff_Actor.__init__)


def test_staff_actor_constructor_args():
    sig = inspect.signature(Staff_Actor.__init__)
    params = list(sig.parameters.keys())



def test__component_is_not_abstract():
    assert not inspect.isabstract(_Component)


def test__component_constructor_exists():
    assert callable(_Component.__init__)


def test__component_constructor_args():
    sig = inspect.signature(_Component.__init__)
    params = list(sig.parameters.keys())



def test_personnel_officer_actor_is_not_abstract():
    assert not inspect.isabstract(Personnel_Officer_Actor)


def test_personnel_officer_actor_constructor_exists():
    assert callable(Personnel_Officer_Actor.__init__)


def test_personnel_officer_actor_constructor_args():
    sig = inspect.signature(Personnel_Officer_Actor.__init__)
    params = list(sig.parameters.keys())

def test_typecontract_exists():
    # Check that the Enumeration exists
    assert TypeContract is not None

def test_typecontract_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeContract]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeContract"

def test_relationship_exists():
    # Check that the Enumeration exists
    assert Relationship is not None

def test_relationship_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Relationship]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Relationship"

def test_sex_exists():
    # Check that the Enumeration exists
    assert Sex is not None

def test_sex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sex]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sex"

def test_maritalstatus_exists():
    # Check that the Enumeration exists
    assert MaritalStatus is not None

def test_maritalstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MaritalStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MaritalStatus"

def test_supplytype_exists():
    # Check that the Enumeration exists
    assert SupplyType is not None

def test_supplytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SupplyType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SupplyType"

def test_salarypayment_exists():
    # Check that the Enumeration exists
    assert SalaryPayment is not None

def test_salarypayment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SalaryPayment]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SalaryPayment"

def test_administration_exists():
    # Check that the Enumeration exists
    assert Administration is not None

def test_administration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Administration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Administration"

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"


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
Generate_Staff_s_Payroll_external_strategy = st.builds(
    Generate_Staff_s_Payroll_external,
)
Authorise_Service_Improvement_Budget_external_strategy = st.builds(
    Authorise_Service_Improvement_Budget_external,
)
Search_Patient_external_strategy = st.builds(
    Search_Patient_external,
)
Create_Patient_appointment_external_strategy = st.builds(
    Create_Patient_appointment_external,
)
Maintain_next_of_kind_details_external_strategy = st.builds(
    Maintain_next_of_kind_details_external,
)
Set_staff_weekly_Rota_external_strategy = st.builds(
    Set_staff_weekly_Rota_external,
)
Maintain_suppliers_external_strategy = st.builds(
    Maintain_suppliers_external,
)
of_ward_s_supplies_external_strategy = st.builds(
    of_ward_s_supplies_external,
)
Maintain_ward_s_supplies_external_strategy = st.builds(
    Maintain_ward_s_supplies_external,
)
of_Services_Improvement_external_strategy = st.builds(
    of_Services_Improvement_external,
)
of_Monthly_profit_external_strategy = st.builds(
    of_Monthly_profit_external,
)
Register_Patient_payment_external_strategy = st.builds(
    Register_Patient_payment_external,
)
of_Patients_referred_to_the_out_patient_clinic_external_strategy = st.builds(
    of_Patients_referred_to_the_out_patient_clinic_external,
)
Maintain_Patients_referred_to_the_out_patients_clinic_external_strategy = st.builds(
    Maintain_Patients_referred_to_the_out_patients_clinic_external,
)
Maintain_Patients_referred_to_the_hospital_external_strategy = st.builds(
    Maintain_Patients_referred_to_the_hospital_external,
)
of_Ward_s_Staff_external_strategy = st.builds(
    of_Ward_s_Staff_external,
)
Search_Staff_external_strategy = st.builds(
    Search_Staff_external,
)
Maintain_Staff_external_strategy = st.builds(
    Maintain_Staff_external,
)
Maintain_resources_external_strategy = st.builds(
    Maintain_resources_external,
)
of_Patients_on_waiting_list_external_strategy = st.builds(
    of_Patients_on_waiting_list_external,
)
of_Patients_in_wards_external_strategy = st.builds(
    of_Patients_in_wards_external,
)
of_Patients__medication_external_strategy = st.builds(
    of_Patients__medication_external,
)
Maintian_Patients__medication_external_strategy = st.builds(
    Maintian_Patients__medication_external,
)
Maintain_ward_s_Patients_external_strategy = st.builds(
    Maintain_ward_s_Patients_external,
)
Accountant_Actor_strategy = st.builds(
    Accountant_Actor,
)
Payee_Actor_strategy = st.builds(
    Payee_Actor,
)
_Component1_strategy = st.builds(
    _Component1,
)
Medication_strategy = st.builds(
    Medication,
    start_date=
        st.dates(),
    units_per_day=
        st.integers(),
    drug=
        st.none(),
    finish_date=
        st.dates(),
    administration=
        st.none(),
    patient=
        st.none()
)
OutPatient_strategy = st.builds(
    OutPatient,
    location=
        safe_text,
    patient=
        st.none(),
    date=
        st.dates()
)
Appointment_strategy = st.builds(
    Appointment,
    doctor=
        st.none(),
    date=
        st.dates(),
    room=
        safe_text,
    patient=
        st.none(),
    num=
        st.integers()
)
InPatient_strategy = st.builds(
    InPatient,
    patient=
        st.none(),
    date_actual_leave=
        st.dates(),
    ward_required=
        st.none(),
    bed=
        st.none(),
    duration=
        st.integers(),
    date_place=
        st.dates(),
    date_expected_leave=
        st.dates()
)
WaitingList_strategy = st.builds(
    WaitingList,
    patient=
        st.none(),
    ward_required=
        st.none(),
    date=
        st.dates()
)
Supplier_strategy = st.builds(
    Supplier,
    fax=
        safe_text,
    num=
        safe_text
)
Pharmaceutical_strategy = st.builds(
    Pharmaceutical,
    method_of_administration=
        safe_text,
    dosage=
        safe_text
)
Surgical_NonSurgical_strategy = st.builds(
    Surgical_NonSurgical,
    supply_type=
        st.none()
)
Supply_strategy = st.builds(
    Supply,
    name=
        safe_text,
    cost_per_unit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    reorder_level=
        st.integers(),
    description=
        safe_text,
    num=
        st.integers(),
    stock=
        st.integers()
)
Requisition_strategy = st.builds(
    Requisition,
    date_ordered=
        st.dates(),
    quantity_required=
        st.integers(),
    responsable=
        st.none(),
    supply=
        st.none(),
    num=
        st.integers(),
    ward=
        st.none(),
    date_delivered=
        st.dates()
)
Bed_strategy = st.builds(
    Bed,
    num=
        st.integers()
)
Ward_strategy = st.builds(
    Ward,
    staff=
        st.none(),
    location=
        safe_text,
    num=
        st.integers(),
    telephone_extension=
        st.integers(),
    name=
        safe_text,
    responsable=
        st.none()
)
RegularDoctor_strategy = st.builds(
    RegularDoctor,
)
ChargeNurse_strategy = st.builds(
    ChargeNurse,
)
PersonnelOfficer_strategy = st.builds(
    PersonnelOfficer,
)
MedicalDirector_strategy = st.builds(
    MedicalDirector,
)
EmploymentContract_strategy = st.builds(
    EmploymentContract,
    number_hours_per_week=
        st.integers(),
    type_contract=
        st.none(),
    salary_payment=
        st.none()
)
WorkExperience_strategy = st.builds(
    WorkExperience,
    position=
        safe_text,
    organization_name=
        safe_text,
    finish_date=
        st.dates(),
    start_date=
        st.dates()
)
Qualification_strategy = st.builds(
    Qualification,
    date=
        st.dates(),
    type=
        safe_text,
    institution_name=
        safe_text
)
LocalDoctor_strategy = st.builds(
    LocalDoctor,
    clinic_number=
        st.integers()
)
NextOfKind_strategy = st.builds(
    NextOfKind,
    relationship=
        st.none()
)
Staff_strategy = st.builds(
    Staff,
    current_salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    salary_scale=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    work_experience=
        st.none(),
    employment_contract=
        st.none(),
    position=
        st.none(),
    num=
        st.integers(),
    nin=
        st.integers(),
    qualification=
        st.none()
)
Patient_strategy = st.builds(
    Patient,
    num=
        st.integers(),
    marital_status=
        st.none(),
    local_doctor=
        st.none(),
    next_of_kind=
        st.none()
)
Person_strategy = st.builds(
    Person,
    address=
        safe_text,
    first_name=
        safe_text,
    date_of_birth=
        st.dates(),
    last_name=
        safe_text,
    telephone=
        safe_text,
    sex=
        st.none()
)
Patient_Actor_strategy = st.builds(
    Patient_Actor,
)
Medical_Director_Actor_strategy = st.builds(
    Medical_Director_Actor,
)
Person_Actor_strategy = st.builds(
    Person_Actor,
)
Charge_Nurse_Actor_strategy = st.builds(
    Charge_Nurse_Actor,
)
Staff_Actor_strategy = st.builds(
    Staff_Actor,
)
_Component_strategy = st.builds(
    _Component,
)
Personnel_Officer_Actor_strategy = st.builds(
    Personnel_Officer_Actor,
)

@given(instance=Generate_Staff_s_Payroll_external_strategy)
@settings(max_examples=50)
def test_generate_staff_s_payroll_external_instantiation(instance):
    assert isinstance(instance, Generate_Staff_s_Payroll_external)

@given(instance=Authorise_Service_Improvement_Budget_external_strategy)
@settings(max_examples=50)
def test_authorise_service_improvement_budget_external_instantiation(instance):
    assert isinstance(instance, Authorise_Service_Improvement_Budget_external)

@given(instance=Search_Patient_external_strategy)
@settings(max_examples=50)
def test_search_patient_external_instantiation(instance):
    assert isinstance(instance, Search_Patient_external)

@given(instance=Create_Patient_appointment_external_strategy)
@settings(max_examples=50)
def test_create_patient_appointment_external_instantiation(instance):
    assert isinstance(instance, Create_Patient_appointment_external)

@given(instance=Maintain_next_of_kind_details_external_strategy)
@settings(max_examples=50)
def test_maintain_next_of_kind_details_external_instantiation(instance):
    assert isinstance(instance, Maintain_next_of_kind_details_external)

@given(instance=Set_staff_weekly_Rota_external_strategy)
@settings(max_examples=50)
def test_set_staff_weekly_rota_external_instantiation(instance):
    assert isinstance(instance, Set_staff_weekly_Rota_external)

@given(instance=Maintain_suppliers_external_strategy)
@settings(max_examples=50)
def test_maintain_suppliers_external_instantiation(instance):
    assert isinstance(instance, Maintain_suppliers_external)

@given(instance=of_ward_s_supplies_external_strategy)
@settings(max_examples=50)
def test_of_ward_s_supplies_external_instantiation(instance):
    assert isinstance(instance, of_ward_s_supplies_external)

@given(instance=Maintain_ward_s_supplies_external_strategy)
@settings(max_examples=50)
def test_maintain_ward_s_supplies_external_instantiation(instance):
    assert isinstance(instance, Maintain_ward_s_supplies_external)

@given(instance=of_Services_Improvement_external_strategy)
@settings(max_examples=50)
def test_of_services_improvement_external_instantiation(instance):
    assert isinstance(instance, of_Services_Improvement_external)

@given(instance=of_Monthly_profit_external_strategy)
@settings(max_examples=50)
def test_of_monthly_profit_external_instantiation(instance):
    assert isinstance(instance, of_Monthly_profit_external)

@given(instance=Register_Patient_payment_external_strategy)
@settings(max_examples=50)
def test_register_patient_payment_external_instantiation(instance):
    assert isinstance(instance, Register_Patient_payment_external)

@given(instance=of_Patients_referred_to_the_out_patient_clinic_external_strategy)
@settings(max_examples=50)
def test_of_patients_referred_to_the_out_patient_clinic_external_instantiation(instance):
    assert isinstance(instance, of_Patients_referred_to_the_out_patient_clinic_external)

@given(instance=Maintain_Patients_referred_to_the_out_patients_clinic_external_strategy)
@settings(max_examples=50)
def test_maintain_patients_referred_to_the_out_patients_clinic_external_instantiation(instance):
    assert isinstance(instance, Maintain_Patients_referred_to_the_out_patients_clinic_external)

@given(instance=Maintain_Patients_referred_to_the_hospital_external_strategy)
@settings(max_examples=50)
def test_maintain_patients_referred_to_the_hospital_external_instantiation(instance):
    assert isinstance(instance, Maintain_Patients_referred_to_the_hospital_external)

@given(instance=of_Ward_s_Staff_external_strategy)
@settings(max_examples=50)
def test_of_ward_s_staff_external_instantiation(instance):
    assert isinstance(instance, of_Ward_s_Staff_external)

@given(instance=Search_Staff_external_strategy)
@settings(max_examples=50)
def test_search_staff_external_instantiation(instance):
    assert isinstance(instance, Search_Staff_external)

@given(instance=Maintain_Staff_external_strategy)
@settings(max_examples=50)
def test_maintain_staff_external_instantiation(instance):
    assert isinstance(instance, Maintain_Staff_external)

@given(instance=Maintain_resources_external_strategy)
@settings(max_examples=50)
def test_maintain_resources_external_instantiation(instance):
    assert isinstance(instance, Maintain_resources_external)

@given(instance=of_Patients_on_waiting_list_external_strategy)
@settings(max_examples=50)
def test_of_patients_on_waiting_list_external_instantiation(instance):
    assert isinstance(instance, of_Patients_on_waiting_list_external)

@given(instance=of_Patients_in_wards_external_strategy)
@settings(max_examples=50)
def test_of_patients_in_wards_external_instantiation(instance):
    assert isinstance(instance, of_Patients_in_wards_external)

@given(instance=of_Patients__medication_external_strategy)
@settings(max_examples=50)
def test_of_patients__medication_external_instantiation(instance):
    assert isinstance(instance, of_Patients__medication_external)

@given(instance=Maintian_Patients__medication_external_strategy)
@settings(max_examples=50)
def test_maintian_patients__medication_external_instantiation(instance):
    assert isinstance(instance, Maintian_Patients__medication_external)

@given(instance=Maintain_ward_s_Patients_external_strategy)
@settings(max_examples=50)
def test_maintain_ward_s_patients_external_instantiation(instance):
    assert isinstance(instance, Maintain_ward_s_Patients_external)

@given(instance=Accountant_Actor_strategy)
@settings(max_examples=50)
def test_accountant_actor_instantiation(instance):
    assert isinstance(instance, Accountant_Actor)

@given(instance=Payee_Actor_strategy)
@settings(max_examples=50)
def test_payee_actor_instantiation(instance):
    assert isinstance(instance, Payee_Actor)

@given(instance=_Component1_strategy)
@settings(max_examples=50)
def test__component1_instantiation(instance):
    assert isinstance(instance, _Component1)

@given(instance=Medication_strategy)
@settings(max_examples=50)
def test_medication_instantiation(instance):
    assert isinstance(instance, Medication)



@given(instance=Medication_strategy)
def test_medication_start_date_setter(instance):
    original = instance.start_date
    instance.start_date = original
    assert instance.start_date == original



@given(instance=Medication_strategy)
def test_medication_units_per_day_setter(instance):
    original = instance.units_per_day
    instance.units_per_day = original
    assert instance.units_per_day == original



@given(instance=Medication_strategy)
def test_medication_drug_setter(instance):
    original = instance.drug
    instance.drug = original
    assert instance.drug == original



@given(instance=Medication_strategy)
def test_medication_finish_date_setter(instance):
    original = instance.finish_date
    instance.finish_date = original
    assert instance.finish_date == original



@given(instance=Medication_strategy)
def test_medication_administration_setter(instance):
    original = instance.administration
    instance.administration = original
    assert instance.administration == original



@given(instance=Medication_strategy)
def test_medication_patient_setter(instance):
    original = instance.patient
    instance.patient = original
    assert instance.patient == original

@given(instance=OutPatient_strategy)
@settings(max_examples=50)
def test_outpatient_instantiation(instance):
    assert isinstance(instance, OutPatient)



@given(instance=OutPatient_strategy)
def test_outpatient_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=OutPatient_strategy)
def test_outpatient_patient_setter(instance):
    original = instance.patient
    instance.patient = original
    assert instance.patient == original



@given(instance=OutPatient_strategy)
def test_outpatient_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Appointment_strategy)
@settings(max_examples=50)
def test_appointment_instantiation(instance):
    assert isinstance(instance, Appointment)



@given(instance=Appointment_strategy)
def test_appointment_doctor_setter(instance):
    original = instance.doctor
    instance.doctor = original
    assert instance.doctor == original



@given(instance=Appointment_strategy)
def test_appointment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Appointment_strategy)
def test_appointment_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original



@given(instance=Appointment_strategy)
def test_appointment_patient_setter(instance):
    original = instance.patient
    instance.patient = original
    assert instance.patient == original



@given(instance=Appointment_strategy)
def test_appointment_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=InPatient_strategy)
@settings(max_examples=50)
def test_inpatient_instantiation(instance):
    assert isinstance(instance, InPatient)



@given(instance=InPatient_strategy)
def test_inpatient_patient_setter(instance):
    original = instance.patient
    instance.patient = original
    assert instance.patient == original



@given(instance=InPatient_strategy)
def test_inpatient_date_actual_leave_setter(instance):
    original = instance.date_actual_leave
    instance.date_actual_leave = original
    assert instance.date_actual_leave == original



@given(instance=InPatient_strategy)
def test_inpatient_ward_required_setter(instance):
    original = instance.ward_required
    instance.ward_required = original
    assert instance.ward_required == original



@given(instance=InPatient_strategy)
def test_inpatient_bed_setter(instance):
    original = instance.bed
    instance.bed = original
    assert instance.bed == original



@given(instance=InPatient_strategy)
def test_inpatient_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=InPatient_strategy)
def test_inpatient_date_place_setter(instance):
    original = instance.date_place
    instance.date_place = original
    assert instance.date_place == original



@given(instance=InPatient_strategy)
def test_inpatient_date_expected_leave_setter(instance):
    original = instance.date_expected_leave
    instance.date_expected_leave = original
    assert instance.date_expected_leave == original

@given(instance=WaitingList_strategy)
@settings(max_examples=50)
def test_waitinglist_instantiation(instance):
    assert isinstance(instance, WaitingList)



@given(instance=WaitingList_strategy)
def test_waitinglist_patient_setter(instance):
    original = instance.patient
    instance.patient = original
    assert instance.patient == original



@given(instance=WaitingList_strategy)
def test_waitinglist_ward_required_setter(instance):
    original = instance.ward_required
    instance.ward_required = original
    assert instance.ward_required == original



@given(instance=WaitingList_strategy)
def test_waitinglist_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Supplier_strategy)
@settings(max_examples=50)
def test_supplier_instantiation(instance):
    assert isinstance(instance, Supplier)



@given(instance=Supplier_strategy)
def test_supplier_fax_setter(instance):
    original = instance.fax
    instance.fax = original
    assert instance.fax == original



@given(instance=Supplier_strategy)
def test_supplier_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=Pharmaceutical_strategy)
@settings(max_examples=50)
def test_pharmaceutical_instantiation(instance):
    assert isinstance(instance, Pharmaceutical)



@given(instance=Pharmaceutical_strategy)
def test_pharmaceutical_method_of_administration_setter(instance):
    original = instance.method_of_administration
    instance.method_of_administration = original
    assert instance.method_of_administration == original



@given(instance=Pharmaceutical_strategy)
def test_pharmaceutical_dosage_setter(instance):
    original = instance.dosage
    instance.dosage = original
    assert instance.dosage == original

@given(instance=Surgical_NonSurgical_strategy)
@settings(max_examples=50)
def test_surgical_nonsurgical_instantiation(instance):
    assert isinstance(instance, Surgical_NonSurgical)



@given(instance=Surgical_NonSurgical_strategy)
def test_surgical_nonsurgical_supply_type_setter(instance):
    original = instance.supply_type
    instance.supply_type = original
    assert instance.supply_type == original

@given(instance=Supply_strategy)
@settings(max_examples=50)
def test_supply_instantiation(instance):
    assert isinstance(instance, Supply)



@given(instance=Supply_strategy)
def test_supply_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Supply_strategy)
def test_supply_cost_per_unit_setter(instance):
    original = instance.cost_per_unit
    instance.cost_per_unit = original
    assert instance.cost_per_unit == original



@given(instance=Supply_strategy)
def test_supply_reorder_level_setter(instance):
    original = instance.reorder_level
    instance.reorder_level = original
    assert instance.reorder_level == original



@given(instance=Supply_strategy)
def test_supply_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Supply_strategy)
def test_supply_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Supply_strategy)
def test_supply_stock_setter(instance):
    original = instance.stock
    instance.stock = original
    assert instance.stock == original

@given(instance=Requisition_strategy)
@settings(max_examples=50)
def test_requisition_instantiation(instance):
    assert isinstance(instance, Requisition)



@given(instance=Requisition_strategy)
def test_requisition_date_ordered_setter(instance):
    original = instance.date_ordered
    instance.date_ordered = original
    assert instance.date_ordered == original



@given(instance=Requisition_strategy)
def test_requisition_quantity_required_setter(instance):
    original = instance.quantity_required
    instance.quantity_required = original
    assert instance.quantity_required == original



@given(instance=Requisition_strategy)
def test_requisition_responsable_setter(instance):
    original = instance.responsable
    instance.responsable = original
    assert instance.responsable == original



@given(instance=Requisition_strategy)
def test_requisition_supply_setter(instance):
    original = instance.supply
    instance.supply = original
    assert instance.supply == original



@given(instance=Requisition_strategy)
def test_requisition_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Requisition_strategy)
def test_requisition_ward_setter(instance):
    original = instance.ward
    instance.ward = original
    assert instance.ward == original



@given(instance=Requisition_strategy)
def test_requisition_date_delivered_setter(instance):
    original = instance.date_delivered
    instance.date_delivered = original
    assert instance.date_delivered == original

@given(instance=Bed_strategy)
@settings(max_examples=50)
def test_bed_instantiation(instance):
    assert isinstance(instance, Bed)



@given(instance=Bed_strategy)
def test_bed_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=Ward_strategy)
@settings(max_examples=50)
def test_ward_instantiation(instance):
    assert isinstance(instance, Ward)



@given(instance=Ward_strategy)
def test_ward_staff_setter(instance):
    original = instance.staff
    instance.staff = original
    assert instance.staff == original



@given(instance=Ward_strategy)
def test_ward_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Ward_strategy)
def test_ward_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Ward_strategy)
def test_ward_telephone_extension_setter(instance):
    original = instance.telephone_extension
    instance.telephone_extension = original
    assert instance.telephone_extension == original



@given(instance=Ward_strategy)
def test_ward_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Ward_strategy)
def test_ward_responsable_setter(instance):
    original = instance.responsable
    instance.responsable = original
    assert instance.responsable == original

@given(instance=RegularDoctor_strategy)
@settings(max_examples=50)
def test_regulardoctor_instantiation(instance):
    assert isinstance(instance, RegularDoctor)

@given(instance=ChargeNurse_strategy)
@settings(max_examples=50)
def test_chargenurse_instantiation(instance):
    assert isinstance(instance, ChargeNurse)

@given(instance=PersonnelOfficer_strategy)
@settings(max_examples=50)
def test_personnelofficer_instantiation(instance):
    assert isinstance(instance, PersonnelOfficer)

@given(instance=MedicalDirector_strategy)
@settings(max_examples=50)
def test_medicaldirector_instantiation(instance):
    assert isinstance(instance, MedicalDirector)

@given(instance=EmploymentContract_strategy)
@settings(max_examples=50)
def test_employmentcontract_instantiation(instance):
    assert isinstance(instance, EmploymentContract)



@given(instance=EmploymentContract_strategy)
def test_employmentcontract_number_hours_per_week_setter(instance):
    original = instance.number_hours_per_week
    instance.number_hours_per_week = original
    assert instance.number_hours_per_week == original



@given(instance=EmploymentContract_strategy)
def test_employmentcontract_type_contract_setter(instance):
    original = instance.type_contract
    instance.type_contract = original
    assert instance.type_contract == original



@given(instance=EmploymentContract_strategy)
def test_employmentcontract_salary_payment_setter(instance):
    original = instance.salary_payment
    instance.salary_payment = original
    assert instance.salary_payment == original

@given(instance=WorkExperience_strategy)
@settings(max_examples=50)
def test_workexperience_instantiation(instance):
    assert isinstance(instance, WorkExperience)



@given(instance=WorkExperience_strategy)
def test_workexperience_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=WorkExperience_strategy)
def test_workexperience_organization_name_setter(instance):
    original = instance.organization_name
    instance.organization_name = original
    assert instance.organization_name == original



@given(instance=WorkExperience_strategy)
def test_workexperience_finish_date_setter(instance):
    original = instance.finish_date
    instance.finish_date = original
    assert instance.finish_date == original



@given(instance=WorkExperience_strategy)
def test_workexperience_start_date_setter(instance):
    original = instance.start_date
    instance.start_date = original
    assert instance.start_date == original

@given(instance=Qualification_strategy)
@settings(max_examples=50)
def test_qualification_instantiation(instance):
    assert isinstance(instance, Qualification)



@given(instance=Qualification_strategy)
def test_qualification_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Qualification_strategy)
def test_qualification_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Qualification_strategy)
def test_qualification_institution_name_setter(instance):
    original = instance.institution_name
    instance.institution_name = original
    assert instance.institution_name == original

@given(instance=LocalDoctor_strategy)
@settings(max_examples=50)
def test_localdoctor_instantiation(instance):
    assert isinstance(instance, LocalDoctor)



@given(instance=LocalDoctor_strategy)
def test_localdoctor_clinic_number_setter(instance):
    original = instance.clinic_number
    instance.clinic_number = original
    assert instance.clinic_number == original

@given(instance=NextOfKind_strategy)
@settings(max_examples=50)
def test_nextofkind_instantiation(instance):
    assert isinstance(instance, NextOfKind)



@given(instance=NextOfKind_strategy)
def test_nextofkind_relationship_setter(instance):
    original = instance.relationship
    instance.relationship = original
    assert instance.relationship == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_current_salary_setter(instance):
    original = instance.current_salary
    instance.current_salary = original
    assert instance.current_salary == original



@given(instance=Staff_strategy)
def test_staff_salary_scale_setter(instance):
    original = instance.salary_scale
    instance.salary_scale = original
    assert instance.salary_scale == original



@given(instance=Staff_strategy)
def test_staff_work_experience_setter(instance):
    original = instance.work_experience
    instance.work_experience = original
    assert instance.work_experience == original



@given(instance=Staff_strategy)
def test_staff_employment_contract_setter(instance):
    original = instance.employment_contract
    instance.employment_contract = original
    assert instance.employment_contract == original



@given(instance=Staff_strategy)
def test_staff_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Staff_strategy)
def test_staff_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Staff_strategy)
def test_staff_nin_setter(instance):
    original = instance.nin
    instance.nin = original
    assert instance.nin == original



@given(instance=Staff_strategy)
def test_staff_qualification_setter(instance):
    original = instance.qualification
    instance.qualification = original
    assert instance.qualification == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Patient_strategy)
def test_patient_marital_status_setter(instance):
    original = instance.marital_status
    instance.marital_status = original
    assert instance.marital_status == original



@given(instance=Patient_strategy)
def test_patient_local_doctor_setter(instance):
    original = instance.local_doctor
    instance.local_doctor = original
    assert instance.local_doctor == original



@given(instance=Patient_strategy)
def test_patient_next_of_kind_setter(instance):
    original = instance.next_of_kind
    instance.next_of_kind = original
    assert instance.next_of_kind == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Person_strategy)
def test_person_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original



@given(instance=Person_strategy)
def test_person_date_of_birth_setter(instance):
    original = instance.date_of_birth
    instance.date_of_birth = original
    assert instance.date_of_birth == original



@given(instance=Person_strategy)
def test_person_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original



@given(instance=Person_strategy)
def test_person_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original



@given(instance=Person_strategy)
def test_person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original

@given(instance=Patient_Actor_strategy)
@settings(max_examples=50)
def test_patient_actor_instantiation(instance):
    assert isinstance(instance, Patient_Actor)

@given(instance=Medical_Director_Actor_strategy)
@settings(max_examples=50)
def test_medical_director_actor_instantiation(instance):
    assert isinstance(instance, Medical_Director_Actor)

@given(instance=Person_Actor_strategy)
@settings(max_examples=50)
def test_person_actor_instantiation(instance):
    assert isinstance(instance, Person_Actor)

@given(instance=Charge_Nurse_Actor_strategy)
@settings(max_examples=50)
def test_charge_nurse_actor_instantiation(instance):
    assert isinstance(instance, Charge_Nurse_Actor)

@given(instance=Staff_Actor_strategy)
@settings(max_examples=50)
def test_staff_actor_instantiation(instance):
    assert isinstance(instance, Staff_Actor)

@given(instance=_Component_strategy)
@settings(max_examples=50)
def test__component_instantiation(instance):
    assert isinstance(instance, _Component)

@given(instance=Personnel_Officer_Actor_strategy)
@settings(max_examples=50)
def test_personnel_officer_actor_instantiation(instance):
    assert isinstance(instance, Personnel_Officer_Actor)
