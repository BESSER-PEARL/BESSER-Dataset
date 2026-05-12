import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    course,
    Billing_system,
    Register,
    Professor,
    student,
    kiosk1,
    individual,
    Groups,
    booking_clerk,
    Passenger,
    teacher,
    Parents,
    School_administrator,
    attendance_manager,
    students,
    kiosk,
    Owner,
    compuer,
    customer,
    duties_manager,
    pharmacy,
    bank,
    income_manager,
    clinical,
    doctor,
    int_Interface,
    patient,
    bo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_course_is_not_abstract():
    assert not inspect.isabstract(course)


def test_course_constructor_exists():
    assert callable(course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(course.__init__)
    params = list(sig.parameters.keys())
    assert "course_name" in params, "Missing parameter 'course_name'"
    assert "placed_on" in params, "Missing parameter 'placed_on'"
    assert "course_id" in params, "Missing parameter 'course_id'"
    assert "teached_by" in params, "Missing parameter 'teached_by'"

def test_course_has_course_name():
    assert hasattr(course, "course_name")
    descriptor = None
    for klass in course.__mro__:
        if "course_name" in klass.__dict__:
            descriptor = klass.__dict__["course_name"]
            break
    assert isinstance(descriptor, property)

def test_course_has_placed_on():
    assert hasattr(course, "placed_on")
    descriptor = None
    for klass in course.__mro__:
        if "placed_on" in klass.__dict__:
            descriptor = klass.__dict__["placed_on"]
            break
    assert isinstance(descriptor, property)

def test_course_has_course_id():
    assert hasattr(course, "course_id")
    descriptor = None
    for klass in course.__mro__:
        if "course_id" in klass.__dict__:
            descriptor = klass.__dict__["course_id"]
            break
    assert isinstance(descriptor, property)

def test_course_has_teached_by():
    assert hasattr(course, "teached_by")
    descriptor = None
    for klass in course.__mro__:
        if "teached_by" in klass.__dict__:
            descriptor = klass.__dict__["teached_by"]
            break
    assert isinstance(descriptor, property)



def test_billing_system_is_not_abstract():
    assert not inspect.isabstract(Billing_system)


def test_billing_system_constructor_exists():
    assert callable(Billing_system.__init__)


def test_billing_system_constructor_args():
    sig = inspect.signature(Billing_system.__init__)
    params = list(sig.parameters.keys())
    assert "course_fees" in params, "Missing parameter 'course_fees'"
    assert "course_status" in params, "Missing parameter 'course_status'"

def test_billing_system_has_course_fees():
    assert hasattr(Billing_system, "course_fees")
    descriptor = None
    for klass in Billing_system.__mro__:
        if "course_fees" in klass.__dict__:
            descriptor = klass.__dict__["course_fees"]
            break
    assert isinstance(descriptor, property)

def test_billing_system_has_course_status():
    assert hasattr(Billing_system, "course_status")
    descriptor = None
    for klass in Billing_system.__mro__:
        if "course_status" in klass.__dict__:
            descriptor = klass.__dict__["course_status"]
            break
    assert isinstance(descriptor, property)



def test_register_is_not_abstract():
    assert not inspect.isabstract(Register)


def test_register_constructor_exists():
    assert callable(Register.__init__)


def test_register_constructor_args():
    sig = inspect.signature(Register.__init__)
    params = list(sig.parameters.keys())
    assert "student_name" in params, "Missing parameter 'student_name'"
    assert "professer_id" in params, "Missing parameter 'professer_id'"
    assert "course_id" in params, "Missing parameter 'course_id'"
    assert "course_name" in params, "Missing parameter 'course_name'"
    assert "student_id" in params, "Missing parameter 'student_id'"
    assert "professor_name" in params, "Missing parameter 'professor_name'"

def test_register_has_student_name():
    assert hasattr(Register, "student_name")
    descriptor = None
    for klass in Register.__mro__:
        if "student_name" in klass.__dict__:
            descriptor = klass.__dict__["student_name"]
            break
    assert isinstance(descriptor, property)

def test_register_has_professer_id():
    assert hasattr(Register, "professer_id")
    descriptor = None
    for klass in Register.__mro__:
        if "professer_id" in klass.__dict__:
            descriptor = klass.__dict__["professer_id"]
            break
    assert isinstance(descriptor, property)

def test_register_has_course_id():
    assert hasattr(Register, "course_id")
    descriptor = None
    for klass in Register.__mro__:
        if "course_id" in klass.__dict__:
            descriptor = klass.__dict__["course_id"]
            break
    assert isinstance(descriptor, property)

def test_register_has_course_name():
    assert hasattr(Register, "course_name")
    descriptor = None
    for klass in Register.__mro__:
        if "course_name" in klass.__dict__:
            descriptor = klass.__dict__["course_name"]
            break
    assert isinstance(descriptor, property)

def test_register_has_student_id():
    assert hasattr(Register, "student_id")
    descriptor = None
    for klass in Register.__mro__:
        if "student_id" in klass.__dict__:
            descriptor = klass.__dict__["student_id"]
            break
    assert isinstance(descriptor, property)

def test_register_has_professor_name():
    assert hasattr(Register, "professor_name")
    descriptor = None
    for klass in Register.__mro__:
        if "professor_name" in klass.__dict__:
            descriptor = klass.__dict__["professor_name"]
            break
    assert isinstance(descriptor, property)



def test_professor_is_not_abstract():
    assert not inspect.isabstract(Professor)


def test_professor_constructor_exists():
    assert callable(Professor.__init__)


def test_professor_constructor_args():
    sig = inspect.signature(Professor.__init__)
    params = list(sig.parameters.keys())
    assert "professor_name" in params, "Missing parameter 'professor_name'"
    assert "course_name" in params, "Missing parameter 'course_name'"
    assert "course_id" in params, "Missing parameter 'course_id'"
    assert "professor_id" in params, "Missing parameter 'professor_id'"

def test_professor_has_professor_name():
    assert hasattr(Professor, "professor_name")
    descriptor = None
    for klass in Professor.__mro__:
        if "professor_name" in klass.__dict__:
            descriptor = klass.__dict__["professor_name"]
            break
    assert isinstance(descriptor, property)

def test_professor_has_course_name():
    assert hasattr(Professor, "course_name")
    descriptor = None
    for klass in Professor.__mro__:
        if "course_name" in klass.__dict__:
            descriptor = klass.__dict__["course_name"]
            break
    assert isinstance(descriptor, property)

def test_professor_has_course_id():
    assert hasattr(Professor, "course_id")
    descriptor = None
    for klass in Professor.__mro__:
        if "course_id" in klass.__dict__:
            descriptor = klass.__dict__["course_id"]
            break
    assert isinstance(descriptor, property)

def test_professor_has_professor_id():
    assert hasattr(Professor, "professor_id")
    descriptor = None
    for klass in Professor.__mro__:
        if "professor_id" in klass.__dict__:
            descriptor = klass.__dict__["professor_id"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(student)


def test_student_constructor_exists():
    assert callable(student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(student.__init__)
    params = list(sig.parameters.keys())
    assert "no_of_courses" in params, "Missing parameter 'no_of_courses'"
    assert "student_id" in params, "Missing parameter 'student_id'"
    assert "student_name" in params, "Missing parameter 'student_name'"

def test_student_has_no_of_courses():
    assert hasattr(student, "no_of_courses")
    descriptor = None
    for klass in student.__mro__:
        if "no_of_courses" in klass.__dict__:
            descriptor = klass.__dict__["no_of_courses"]
            break
    assert isinstance(descriptor, property)

def test_student_has_student_id():
    assert hasattr(student, "student_id")
    descriptor = None
    for klass in student.__mro__:
        if "student_id" in klass.__dict__:
            descriptor = klass.__dict__["student_id"]
            break
    assert isinstance(descriptor, property)

def test_student_has_student_name():
    assert hasattr(student, "student_name")
    descriptor = None
    for klass in student.__mro__:
        if "student_name" in klass.__dict__:
            descriptor = klass.__dict__["student_name"]
            break
    assert isinstance(descriptor, property)



def test_kiosk1_is_not_abstract():
    assert not inspect.isabstract(kiosk1)


def test_kiosk1_constructor_exists():
    assert callable(kiosk1.__init__)


def test_kiosk1_constructor_args():
    sig = inspect.signature(kiosk1.__init__)
    params = list(sig.parameters.keys())
    assert "check_in" in params, "Missing parameter 'check_in'"

def test_kiosk1_has_check_in():
    assert hasattr(kiosk1, "check_in")
    descriptor = None
    for klass in kiosk1.__mro__:
        if "check_in" in klass.__dict__:
            descriptor = klass.__dict__["check_in"]
            break
    assert isinstance(descriptor, property)



def test_individual_is_not_abstract():
    assert not inspect.isabstract(individual)


def test_individual_constructor_exists():
    assert callable(individual.__init__)


def test_individual_constructor_args():
    sig = inspect.signature(individual.__init__)
    params = list(sig.parameters.keys())
    assert "pass" in params, "Missing parameter 'pass'"

def test_individual_has_pass():
    assert hasattr(individual, "pass")
    descriptor = None
    for klass in individual.__mro__:
        if "pass" in klass.__dict__:
            descriptor = klass.__dict__["pass"]
            break
    assert isinstance(descriptor, property)



def test_groups_is_not_abstract():
    assert not inspect.isabstract(Groups)


def test_groups_constructor_exists():
    assert callable(Groups.__init__)


def test_groups_constructor_args():
    sig = inspect.signature(Groups.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"
    assert "id" in params, "Missing parameter 'id'"
    assert "passenger_amount" in params, "Missing parameter 'passenger_amount'"

def test_groups_has_names():
    assert hasattr(Groups, "names")
    descriptor = None
    for klass in Groups.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)

def test_groups_has_id():
    assert hasattr(Groups, "id")
    descriptor = None
    for klass in Groups.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_groups_has_passenger_amount():
    assert hasattr(Groups, "passenger_amount")
    descriptor = None
    for klass in Groups.__mro__:
        if "passenger_amount" in klass.__dict__:
            descriptor = klass.__dict__["passenger_amount"]
            break
    assert isinstance(descriptor, property)



def test_booking_clerk_is_not_abstract():
    assert not inspect.isabstract(booking_clerk)


def test_booking_clerk_constructor_exists():
    assert callable(booking_clerk.__init__)


def test_booking_clerk_constructor_args():
    sig = inspect.signature(booking_clerk.__init__)
    params = list(sig.parameters.keys())



def test_passenger_is_not_abstract():
    assert not inspect.isabstract(Passenger)


def test_passenger_constructor_exists():
    assert callable(Passenger.__init__)


def test_passenger_constructor_args():
    sig = inspect.signature(Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "check_in" in params, "Missing parameter 'check_in'"
    assert "id" in params, "Missing parameter 'id'"
    assert "baggage" in params, "Missing parameter 'baggage'"
    assert "pass" in params, "Missing parameter 'pass'"

def test_passenger_has_check_in():
    assert hasattr(Passenger, "check_in")
    descriptor = None
    for klass in Passenger.__mro__:
        if "check_in" in klass.__dict__:
            descriptor = klass.__dict__["check_in"]
            break
    assert isinstance(descriptor, property)

def test_passenger_has_id():
    assert hasattr(Passenger, "id")
    descriptor = None
    for klass in Passenger.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_passenger_has_baggage():
    assert hasattr(Passenger, "baggage")
    descriptor = None
    for klass in Passenger.__mro__:
        if "baggage" in klass.__dict__:
            descriptor = klass.__dict__["baggage"]
            break
    assert isinstance(descriptor, property)

def test_passenger_has_pass():
    assert hasattr(Passenger, "pass")
    descriptor = None
    for klass in Passenger.__mro__:
        if "pass" in klass.__dict__:
            descriptor = klass.__dict__["pass"]
            break
    assert isinstance(descriptor, property)



def test_teacher_is_not_abstract():
    assert not inspect.isabstract(teacher)


def test_teacher_constructor_exists():
    assert callable(teacher.__init__)


def test_teacher_constructor_args():
    sig = inspect.signature(teacher.__init__)
    params = list(sig.parameters.keys())



def test_parents_is_not_abstract():
    assert not inspect.isabstract(Parents)


def test_parents_constructor_exists():
    assert callable(Parents.__init__)


def test_parents_constructor_args():
    sig = inspect.signature(Parents.__init__)
    params = list(sig.parameters.keys())



def test_school_administrator_is_not_abstract():
    assert not inspect.isabstract(School_administrator)


def test_school_administrator_constructor_exists():
    assert callable(School_administrator.__init__)


def test_school_administrator_constructor_args():
    sig = inspect.signature(School_administrator.__init__)
    params = list(sig.parameters.keys())



def test_attendance_manager_is_not_abstract():
    assert not inspect.isabstract(attendance_manager)


def test_attendance_manager_constructor_exists():
    assert callable(attendance_manager.__init__)


def test_attendance_manager_constructor_args():
    sig = inspect.signature(attendance_manager.__init__)
    params = list(sig.parameters.keys())
    assert "Excuse_of_Absenties" in params, "Missing parameter 'Excuse_of_Absenties'"
    assert "student_names" in params, "Missing parameter 'student_names'"
    assert "identify_students" in params, "Missing parameter 'identify_students'"

def test_attendance_manager_has_Excuse_of_Absenties():
    assert hasattr(attendance_manager, "Excuse_of_Absenties")
    descriptor = None
    for klass in attendance_manager.__mro__:
        if "Excuse_of_Absenties" in klass.__dict__:
            descriptor = klass.__dict__["Excuse_of_Absenties"]
            break
    assert isinstance(descriptor, property)

def test_attendance_manager_has_student_names():
    assert hasattr(attendance_manager, "student_names")
    descriptor = None
    for klass in attendance_manager.__mro__:
        if "student_names" in klass.__dict__:
            descriptor = klass.__dict__["student_names"]
            break
    assert isinstance(descriptor, property)

def test_attendance_manager_has_identify_students():
    assert hasattr(attendance_manager, "identify_students")
    descriptor = None
    for klass in attendance_manager.__mro__:
        if "identify_students" in klass.__dict__:
            descriptor = klass.__dict__["identify_students"]
            break
    assert isinstance(descriptor, property)



def test_students_is_not_abstract():
    assert not inspect.isabstract(students)


def test_students_constructor_exists():
    assert callable(students.__init__)


def test_students_constructor_args():
    sig = inspect.signature(students.__init__)
    params = list(sig.parameters.keys())
    assert "student_id_" in params, "Missing parameter 'student_id_'"
    assert "student_name" in params, "Missing parameter 'student_name'"

def test_students_has_student_id_():
    assert hasattr(students, "student_id_")
    descriptor = None
    for klass in students.__mro__:
        if "student_id_" in klass.__dict__:
            descriptor = klass.__dict__["student_id_"]
            break
    assert isinstance(descriptor, property)

def test_students_has_student_name():
    assert hasattr(students, "student_name")
    descriptor = None
    for klass in students.__mro__:
        if "student_name" in klass.__dict__:
            descriptor = klass.__dict__["student_name"]
            break
    assert isinstance(descriptor, property)



def test_kiosk_is_not_abstract():
    assert not inspect.isabstract(kiosk)


def test_kiosk_constructor_exists():
    assert callable(kiosk.__init__)


def test_kiosk_constructor_args():
    sig = inspect.signature(kiosk.__init__)
    params = list(sig.parameters.keys())
    assert "saving" in params, "Missing parameter 'saving'"
    assert "discount" in params, "Missing parameter 'discount'"
    assert "newsletters" in params, "Missing parameter 'newsletters'"

def test_kiosk_has_saving():
    assert hasattr(kiosk, "saving")
    descriptor = None
    for klass in kiosk.__mro__:
        if "saving" in klass.__dict__:
            descriptor = klass.__dict__["saving"]
            break
    assert isinstance(descriptor, property)

def test_kiosk_has_discount():
    assert hasattr(kiosk, "discount")
    descriptor = None
    for klass in kiosk.__mro__:
        if "discount" in klass.__dict__:
            descriptor = klass.__dict__["discount"]
            break
    assert isinstance(descriptor, property)

def test_kiosk_has_newsletters():
    assert hasattr(kiosk, "newsletters")
    descriptor = None
    for klass in kiosk.__mro__:
        if "newsletters" in klass.__dict__:
            descriptor = klass.__dict__["newsletters"]
            break
    assert isinstance(descriptor, property)



def test_owner_is_not_abstract():
    assert not inspect.isabstract(Owner)


def test_owner_constructor_exists():
    assert callable(Owner.__init__)


def test_owner_constructor_args():
    sig = inspect.signature(Owner.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "items" in params, "Missing parameter 'items'"

def test_owner_has_email():
    assert hasattr(Owner, "email")
    descriptor = None
    for klass in Owner.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_owner_has_items():
    assert hasattr(Owner, "items")
    descriptor = None
    for klass in Owner.__mro__:
        if "items" in klass.__dict__:
            descriptor = klass.__dict__["items"]
            break
    assert isinstance(descriptor, property)



def test_compuer_is_not_abstract():
    assert not inspect.isabstract(compuer)


def test_compuer_constructor_exists():
    assert callable(compuer.__init__)


def test_compuer_constructor_args():
    sig = inspect.signature(compuer.__init__)
    params = list(sig.parameters.keys())



def test_customer_is_not_abstract():
    assert not inspect.isabstract(customer)


def test_customer_constructor_exists():
    assert callable(customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(customer.__init__)
    params = list(sig.parameters.keys())
    assert "customer_Id" in params, "Missing parameter 'customer_Id'"
    assert "customer_name" in params, "Missing parameter 'customer_name'"
    assert "_attr" in params, "Missing parameter '_attr'"

def test_customer_has_customer_Id():
    assert hasattr(customer, "customer_Id")
    descriptor = None
    for klass in customer.__mro__:
        if "customer_Id" in klass.__dict__:
            descriptor = klass.__dict__["customer_Id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customer_name():
    assert hasattr(customer, "customer_name")
    descriptor = None
    for klass in customer.__mro__:
        if "customer_name" in klass.__dict__:
            descriptor = klass.__dict__["customer_name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has__attr():
    assert hasattr(customer, "_attr")
    descriptor = None
    for klass in customer.__mro__:
        if "_attr" in klass.__dict__:
            descriptor = klass.__dict__["_attr"]
            break
    assert isinstance(descriptor, property)



def test_duties_manager_is_not_abstract():
    assert not inspect.isabstract(duties_manager)


def test_duties_manager_constructor_exists():
    assert callable(duties_manager.__init__)


def test_duties_manager_constructor_args():
    sig = inspect.signature(duties_manager.__init__)
    params = list(sig.parameters.keys())
    assert "make_attendence" in params, "Missing parameter 'make_attendence'"

def test_duties_manager_has_make_attendence():
    assert hasattr(duties_manager, "make_attendence")
    descriptor = None
    for klass in duties_manager.__mro__:
        if "make_attendence" in klass.__dict__:
            descriptor = klass.__dict__["make_attendence"]
            break
    assert isinstance(descriptor, property)



def test_pharmacy_is_not_abstract():
    assert not inspect.isabstract(pharmacy)


def test_pharmacy_constructor_exists():
    assert callable(pharmacy.__init__)


def test_pharmacy_constructor_args():
    sig = inspect.signature(pharmacy.__init__)
    params = list(sig.parameters.keys())
    assert "medicines" in params, "Missing parameter 'medicines'"
    assert "price" in params, "Missing parameter 'price'"

def test_pharmacy_has_medicines():
    assert hasattr(pharmacy, "medicines")
    descriptor = None
    for klass in pharmacy.__mro__:
        if "medicines" in klass.__dict__:
            descriptor = klass.__dict__["medicines"]
            break
    assert isinstance(descriptor, property)

def test_pharmacy_has_price():
    assert hasattr(pharmacy, "price")
    descriptor = None
    for klass in pharmacy.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(bank)


def test_bank_constructor_exists():
    assert callable(bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(bank.__init__)
    params = list(sig.parameters.keys())
    assert "bank_name" in params, "Missing parameter 'bank_name'"

def test_bank_has_bank_name():
    assert hasattr(bank, "bank_name")
    descriptor = None
    for klass in bank.__mro__:
        if "bank_name" in klass.__dict__:
            descriptor = klass.__dict__["bank_name"]
            break
    assert isinstance(descriptor, property)



def test_income_manager_is_not_abstract():
    assert not inspect.isabstract(income_manager)


def test_income_manager_constructor_exists():
    assert callable(income_manager.__init__)


def test_income_manager_constructor_args():
    sig = inspect.signature(income_manager.__init__)
    params = list(sig.parameters.keys())
    assert "manager_name" in params, "Missing parameter 'manager_name'"
    assert "manager_id" in params, "Missing parameter 'manager_id'"
    assert "duty_hours" in params, "Missing parameter 'duty_hours'"

def test_income_manager_has_manager_name():
    assert hasattr(income_manager, "manager_name")
    descriptor = None
    for klass in income_manager.__mro__:
        if "manager_name" in klass.__dict__:
            descriptor = klass.__dict__["manager_name"]
            break
    assert isinstance(descriptor, property)

def test_income_manager_has_manager_id():
    assert hasattr(income_manager, "manager_id")
    descriptor = None
    for klass in income_manager.__mro__:
        if "manager_id" in klass.__dict__:
            descriptor = klass.__dict__["manager_id"]
            break
    assert isinstance(descriptor, property)

def test_income_manager_has_duty_hours():
    assert hasattr(income_manager, "duty_hours")
    descriptor = None
    for klass in income_manager.__mro__:
        if "duty_hours" in klass.__dict__:
            descriptor = klass.__dict__["duty_hours"]
            break
    assert isinstance(descriptor, property)



def test_clinical_is_not_abstract():
    assert not inspect.isabstract(clinical)


def test_clinical_constructor_exists():
    assert callable(clinical.__init__)


def test_clinical_constructor_args():
    sig = inspect.signature(clinical.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "id" in params, "Missing parameter 'id'"

def test_clinical_has_name():
    assert hasattr(clinical, "name")
    descriptor = None
    for klass in clinical.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_clinical_has_salary():
    assert hasattr(clinical, "salary")
    descriptor = None
    for klass in clinical.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_clinical_has_id():
    assert hasattr(clinical, "id")
    descriptor = None
    for klass in clinical.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(doctor)


def test_doctor_constructor_exists():
    assert callable(doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(doctor.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"
    assert "doctor_id" in params, "Missing parameter 'doctor_id'"
    assert "doctor_name" in params, "Missing parameter 'doctor_name'"
    assert "attendance" in params, "Missing parameter 'attendance'"

def test_doctor_has_salary():
    assert hasattr(doctor, "salary")
    descriptor = None
    for klass in doctor.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_doctor_id():
    assert hasattr(doctor, "doctor_id")
    descriptor = None
    for klass in doctor.__mro__:
        if "doctor_id" in klass.__dict__:
            descriptor = klass.__dict__["doctor_id"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_doctor_name():
    assert hasattr(doctor, "doctor_name")
    descriptor = None
    for klass in doctor.__mro__:
        if "doctor_name" in klass.__dict__:
            descriptor = klass.__dict__["doctor_name"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_attendance():
    assert hasattr(doctor, "attendance")
    descriptor = None
    for klass in doctor.__mro__:
        if "attendance" in klass.__dict__:
            descriptor = klass.__dict__["attendance"]
            break
    assert isinstance(descriptor, property)



def test_int_interface_is_not_abstract():
    assert not inspect.isabstract(int_Interface)


def test_int_interface_constructor_exists():
    assert callable(int_Interface.__init__)


def test_int_interface_constructor_args():
    sig = inspect.signature(int_Interface.__init__)
    params = list(sig.parameters.keys())



def test_patient_is_not_abstract():
    assert not inspect.isabstract(patient)


def test_patient_constructor_exists():
    assert callable(patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(patient.__init__)
    params = list(sig.parameters.keys())
    assert "disease" in params, "Missing parameter 'disease'"
    assert "patient_id" in params, "Missing parameter 'patient_id'"
    assert "patient_name" in params, "Missing parameter 'patient_name'"

def test_patient_has_disease():
    assert hasattr(patient, "disease")
    descriptor = None
    for klass in patient.__mro__:
        if "disease" in klass.__dict__:
            descriptor = klass.__dict__["disease"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_patient_id():
    assert hasattr(patient, "patient_id")
    descriptor = None
    for klass in patient.__mro__:
        if "patient_id" in klass.__dict__:
            descriptor = klass.__dict__["patient_id"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_patient_name():
    assert hasattr(patient, "patient_name")
    descriptor = None
    for klass in patient.__mro__:
        if "patient_name" in klass.__dict__:
            descriptor = klass.__dict__["patient_name"]
            break
    assert isinstance(descriptor, property)

def test_bo_exists():
    # Check that the Enumeration exists
    assert bo is not None

def test_bo_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in bo]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in bo"


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
course_strategy = st.builds(
    course,
    course_name=
        safe_text,
    placed_on=
        safe_text,
    course_id=
        st.none(),
    teached_by=
        safe_text
)
Billing_system_strategy = st.builds(
    Billing_system,
    course_fees=
        st.none(),
    course_status=
        safe_text
)
Register_strategy = st.builds(
    Register,
    student_name=
        st.none(),
    professer_id=
        st.none(),
    course_id=
        safe_text,
    course_name=
        safe_text,
    student_id=
        st.none(),
    professor_name=
        st.none()
)
Professor_strategy = st.builds(
    Professor,
    professor_name=
        safe_text,
    course_name=
        safe_text,
    course_id=
        st.none(),
    professor_id=
        st.none()
)
student_strategy = st.builds(
    student,
    no_of_courses=
        st.none(),
    student_id=
        st.none(),
    student_name=
        safe_text
)
kiosk1_strategy = st.builds(
    kiosk1,
    check_in=
        st.none()
)
individual_strategy = st.builds(
    individual,
    pass=
        st.none()
)
Groups_strategy = st.builds(
    Groups,
    names=
        safe_text,
    id=
        st.none(),
    passenger_amount=
        st.none()
)
booking_clerk_strategy = st.builds(
    booking_clerk,
)
Passenger_strategy = st.builds(
    Passenger,
    check_in=
        st.booleans(),
    id=
        st.none(),
    baggage=
        st.none(),
    pass=
        safe_text
)
teacher_strategy = st.builds(
    teacher,
)
Parents_strategy = st.builds(
    Parents,
)
School_administrator_strategy = st.builds(
    School_administrator,
)
attendance_manager_strategy = st.builds(
    attendance_manager,
    Excuse_of_Absenties=
        safe_text,
    student_names=
        safe_text,
    identify_students=
        safe_text
)
students_strategy = st.builds(
    students,
    student_id_=
        st.none(),
    student_name=
        safe_text
)
kiosk_strategy = st.builds(
    kiosk,
    saving=
        st.none(),
    discount=
        st.none(),
    newsletters=
        safe_text
)
Owner_strategy = st.builds(
    Owner,
    email=
        safe_text,
    items=
        safe_text
)
compuer_strategy = st.builds(
    compuer,
)
customer_strategy = st.builds(
    customer,
    customer_Id=
        st.none(),
    customer_name=
        safe_text,
    _attr=
        safe_text
)
duties_manager_strategy = st.builds(
    duties_manager,
    make_attendence=
        st.booleans()
)
pharmacy_strategy = st.builds(
    pharmacy,
    medicines=
        safe_text,
    price=
        st.none()
)
bank_strategy = st.builds(
    bank,
    bank_name=
        safe_text
)
income_manager_strategy = st.builds(
    income_manager,
    manager_name=
        safe_text,
    manager_id=
        st.none(),
    duty_hours=
        st.none()
)
clinical_strategy = st.builds(
    clinical,
    name=
        safe_text,
    salary=
        st.none(),
    id=
        st.none()
)
doctor_strategy = st.builds(
    doctor,
    salary=
        st.none(),
    doctor_id=
        st.none(),
    doctor_name=
        safe_text,
    attendance=
        st.booleans()
)
int_Interface_strategy = st.builds(
    int_Interface,
)
patient_strategy = st.builds(
    patient,
    disease=
        safe_text,
    patient_id=
        st.none(),
    patient_name=
        safe_text
)

@given(instance=course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, course)



@given(instance=course_strategy)
def test_course_course_name_setter(instance):
    original = instance.course_name
    instance.course_name = original
    assert instance.course_name == original



@given(instance=course_strategy)
def test_course_placed_on_setter(instance):
    original = instance.placed_on
    instance.placed_on = original
    assert instance.placed_on == original



@given(instance=course_strategy)
def test_course_course_id_setter(instance):
    original = instance.course_id
    instance.course_id = original
    assert instance.course_id == original



@given(instance=course_strategy)
def test_course_teached_by_setter(instance):
    original = instance.teached_by
    instance.teached_by = original
    assert instance.teached_by == original

@given(instance=Billing_system_strategy)
@settings(max_examples=50)
def test_billing_system_instantiation(instance):
    assert isinstance(instance, Billing_system)



@given(instance=Billing_system_strategy)
def test_billing_system_course_fees_setter(instance):
    original = instance.course_fees
    instance.course_fees = original
    assert instance.course_fees == original



@given(instance=Billing_system_strategy)
def test_billing_system_course_status_setter(instance):
    original = instance.course_status
    instance.course_status = original
    assert instance.course_status == original

@given(instance=Register_strategy)
@settings(max_examples=50)
def test_register_instantiation(instance):
    assert isinstance(instance, Register)



@given(instance=Register_strategy)
def test_register_student_name_setter(instance):
    original = instance.student_name
    instance.student_name = original
    assert instance.student_name == original



@given(instance=Register_strategy)
def test_register_professer_id_setter(instance):
    original = instance.professer_id
    instance.professer_id = original
    assert instance.professer_id == original



@given(instance=Register_strategy)
def test_register_course_id_setter(instance):
    original = instance.course_id
    instance.course_id = original
    assert instance.course_id == original



@given(instance=Register_strategy)
def test_register_course_name_setter(instance):
    original = instance.course_name
    instance.course_name = original
    assert instance.course_name == original



@given(instance=Register_strategy)
def test_register_student_id_setter(instance):
    original = instance.student_id
    instance.student_id = original
    assert instance.student_id == original



@given(instance=Register_strategy)
def test_register_professor_name_setter(instance):
    original = instance.professor_name
    instance.professor_name = original
    assert instance.professor_name == original

@given(instance=Professor_strategy)
@settings(max_examples=50)
def test_professor_instantiation(instance):
    assert isinstance(instance, Professor)



@given(instance=Professor_strategy)
def test_professor_professor_name_setter(instance):
    original = instance.professor_name
    instance.professor_name = original
    assert instance.professor_name == original



@given(instance=Professor_strategy)
def test_professor_course_name_setter(instance):
    original = instance.course_name
    instance.course_name = original
    assert instance.course_name == original



@given(instance=Professor_strategy)
def test_professor_course_id_setter(instance):
    original = instance.course_id
    instance.course_id = original
    assert instance.course_id == original



@given(instance=Professor_strategy)
def test_professor_professor_id_setter(instance):
    original = instance.professor_id
    instance.professor_id = original
    assert instance.professor_id == original

@given(instance=student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, student)



@given(instance=student_strategy)
def test_student_no_of_courses_setter(instance):
    original = instance.no_of_courses
    instance.no_of_courses = original
    assert instance.no_of_courses == original



@given(instance=student_strategy)
def test_student_student_id_setter(instance):
    original = instance.student_id
    instance.student_id = original
    assert instance.student_id == original



@given(instance=student_strategy)
def test_student_student_name_setter(instance):
    original = instance.student_name
    instance.student_name = original
    assert instance.student_name == original

@given(instance=kiosk1_strategy)
@settings(max_examples=50)
def test_kiosk1_instantiation(instance):
    assert isinstance(instance, kiosk1)



@given(instance=kiosk1_strategy)
def test_kiosk1_check_in_setter(instance):
    original = instance.check_in
    instance.check_in = original
    assert instance.check_in == original

@given(instance=individual_strategy)
@settings(max_examples=50)
def test_individual_instantiation(instance):
    assert isinstance(instance, individual)



@given(instance=individual_strategy)
def test_individual_pass_setter(instance):
    original = instance.pass
    instance.pass = original
    assert instance.pass == original

@given(instance=Groups_strategy)
@settings(max_examples=50)
def test_groups_instantiation(instance):
    assert isinstance(instance, Groups)



@given(instance=Groups_strategy)
def test_groups_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original



@given(instance=Groups_strategy)
def test_groups_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Groups_strategy)
def test_groups_passenger_amount_setter(instance):
    original = instance.passenger_amount
    instance.passenger_amount = original
    assert instance.passenger_amount == original

@given(instance=booking_clerk_strategy)
@settings(max_examples=50)
def test_booking_clerk_instantiation(instance):
    assert isinstance(instance, booking_clerk)

@given(instance=Passenger_strategy)
@settings(max_examples=50)
def test_passenger_instantiation(instance):
    assert isinstance(instance, Passenger)



@given(instance=Passenger_strategy)
def test_passenger_check_in_setter(instance):
    original = instance.check_in
    instance.check_in = original
    assert instance.check_in == original



@given(instance=Passenger_strategy)
def test_passenger_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Passenger_strategy)
def test_passenger_baggage_setter(instance):
    original = instance.baggage
    instance.baggage = original
    assert instance.baggage == original



@given(instance=Passenger_strategy)
def test_passenger_pass_setter(instance):
    original = instance.pass
    instance.pass = original
    assert instance.pass == original

@given(instance=teacher_strategy)
@settings(max_examples=50)
def test_teacher_instantiation(instance):
    assert isinstance(instance, teacher)

@given(instance=Parents_strategy)
@settings(max_examples=50)
def test_parents_instantiation(instance):
    assert isinstance(instance, Parents)

@given(instance=School_administrator_strategy)
@settings(max_examples=50)
def test_school_administrator_instantiation(instance):
    assert isinstance(instance, School_administrator)

@given(instance=attendance_manager_strategy)
@settings(max_examples=50)
def test_attendance_manager_instantiation(instance):
    assert isinstance(instance, attendance_manager)



@given(instance=attendance_manager_strategy)
def test_attendance_manager_Excuse_of_Absenties_setter(instance):
    original = instance.Excuse_of_Absenties
    instance.Excuse_of_Absenties = original
    assert instance.Excuse_of_Absenties == original



@given(instance=attendance_manager_strategy)
def test_attendance_manager_student_names_setter(instance):
    original = instance.student_names
    instance.student_names = original
    assert instance.student_names == original



@given(instance=attendance_manager_strategy)
def test_attendance_manager_identify_students_setter(instance):
    original = instance.identify_students
    instance.identify_students = original
    assert instance.identify_students == original

@given(instance=students_strategy)
@settings(max_examples=50)
def test_students_instantiation(instance):
    assert isinstance(instance, students)



@given(instance=students_strategy)
def test_students_student_id__setter(instance):
    original = instance.student_id_
    instance.student_id_ = original
    assert instance.student_id_ == original



@given(instance=students_strategy)
def test_students_student_name_setter(instance):
    original = instance.student_name
    instance.student_name = original
    assert instance.student_name == original

@given(instance=kiosk_strategy)
@settings(max_examples=50)
def test_kiosk_instantiation(instance):
    assert isinstance(instance, kiosk)



@given(instance=kiosk_strategy)
def test_kiosk_saving_setter(instance):
    original = instance.saving
    instance.saving = original
    assert instance.saving == original



@given(instance=kiosk_strategy)
def test_kiosk_discount_setter(instance):
    original = instance.discount
    instance.discount = original
    assert instance.discount == original



@given(instance=kiosk_strategy)
def test_kiosk_newsletters_setter(instance):
    original = instance.newsletters
    instance.newsletters = original
    assert instance.newsletters == original

@given(instance=Owner_strategy)
@settings(max_examples=50)
def test_owner_instantiation(instance):
    assert isinstance(instance, Owner)



@given(instance=Owner_strategy)
def test_owner_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Owner_strategy)
def test_owner_items_setter(instance):
    original = instance.items
    instance.items = original
    assert instance.items == original

@given(instance=compuer_strategy)
@settings(max_examples=50)
def test_compuer_instantiation(instance):
    assert isinstance(instance, compuer)

@given(instance=customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, customer)



@given(instance=customer_strategy)
def test_customer_customer_Id_setter(instance):
    original = instance.customer_Id
    instance.customer_Id = original
    assert instance.customer_Id == original



@given(instance=customer_strategy)
def test_customer_customer_name_setter(instance):
    original = instance.customer_name
    instance.customer_name = original
    assert instance.customer_name == original



@given(instance=customer_strategy)
def test_customer__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original

@given(instance=duties_manager_strategy)
@settings(max_examples=50)
def test_duties_manager_instantiation(instance):
    assert isinstance(instance, duties_manager)



@given(instance=duties_manager_strategy)
def test_duties_manager_make_attendence_setter(instance):
    original = instance.make_attendence
    instance.make_attendence = original
    assert instance.make_attendence == original

@given(instance=pharmacy_strategy)
@settings(max_examples=50)
def test_pharmacy_instantiation(instance):
    assert isinstance(instance, pharmacy)



@given(instance=pharmacy_strategy)
def test_pharmacy_medicines_setter(instance):
    original = instance.medicines
    instance.medicines = original
    assert instance.medicines == original



@given(instance=pharmacy_strategy)
def test_pharmacy_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, bank)



@given(instance=bank_strategy)
def test_bank_bank_name_setter(instance):
    original = instance.bank_name
    instance.bank_name = original
    assert instance.bank_name == original

@given(instance=income_manager_strategy)
@settings(max_examples=50)
def test_income_manager_instantiation(instance):
    assert isinstance(instance, income_manager)



@given(instance=income_manager_strategy)
def test_income_manager_manager_name_setter(instance):
    original = instance.manager_name
    instance.manager_name = original
    assert instance.manager_name == original



@given(instance=income_manager_strategy)
def test_income_manager_manager_id_setter(instance):
    original = instance.manager_id
    instance.manager_id = original
    assert instance.manager_id == original



@given(instance=income_manager_strategy)
def test_income_manager_duty_hours_setter(instance):
    original = instance.duty_hours
    instance.duty_hours = original
    assert instance.duty_hours == original

@given(instance=clinical_strategy)
@settings(max_examples=50)
def test_clinical_instantiation(instance):
    assert isinstance(instance, clinical)



@given(instance=clinical_strategy)
def test_clinical_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=clinical_strategy)
def test_clinical_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=clinical_strategy)
def test_clinical_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, doctor)



@given(instance=doctor_strategy)
def test_doctor_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=doctor_strategy)
def test_doctor_doctor_id_setter(instance):
    original = instance.doctor_id
    instance.doctor_id = original
    assert instance.doctor_id == original



@given(instance=doctor_strategy)
def test_doctor_doctor_name_setter(instance):
    original = instance.doctor_name
    instance.doctor_name = original
    assert instance.doctor_name == original



@given(instance=doctor_strategy)
def test_doctor_attendance_setter(instance):
    original = instance.attendance
    instance.attendance = original
    assert instance.attendance == original

@given(instance=int_Interface_strategy)
@settings(max_examples=50)
def test_int_interface_instantiation(instance):
    assert isinstance(instance, int_Interface)

@given(instance=patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, patient)



@given(instance=patient_strategy)
def test_patient_disease_setter(instance):
    original = instance.disease
    instance.disease = original
    assert instance.disease == original



@given(instance=patient_strategy)
def test_patient_patient_id_setter(instance):
    original = instance.patient_id
    instance.patient_id = original
    assert instance.patient_id == original



@given(instance=patient_strategy)
def test_patient_patient_name_setter(instance):
    original = instance.patient_name
    instance.patient_name = original
    assert instance.patient_name == original
