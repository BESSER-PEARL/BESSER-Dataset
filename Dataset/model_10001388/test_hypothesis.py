import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Loan,
    payslip,
    Attendence,
    EmployeeRequest,
    Admin,
    Login,
    Salary,
    Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_loan_is_not_abstract():
    assert not inspect.isabstract(Loan)


def test_loan_constructor_exists():
    assert callable(Loan.__init__)


def test_loan_constructor_args():
    sig = inspect.signature(Loan.__init__)
    params = list(sig.parameters.keys())
    assert "loan_purpose" in params, "Missing parameter 'loan_purpose'"
    assert "emp_name" in params, "Missing parameter 'emp_name'"
    assert "loan_type" in params, "Missing parameter 'loan_type'"
    assert "loan_interst" in params, "Missing parameter 'loan_interst'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_loan_has_loan_purpose():
    assert hasattr(Loan, "loan_purpose")
    descriptor = None
    for klass in Loan.__mro__:
        if "loan_purpose" in klass.__dict__:
            descriptor = klass.__dict__["loan_purpose"]
            break
    assert isinstance(descriptor, property)

def test_loan_has_emp_name():
    assert hasattr(Loan, "emp_name")
    descriptor = None
    for klass in Loan.__mro__:
        if "emp_name" in klass.__dict__:
            descriptor = klass.__dict__["emp_name"]
            break
    assert isinstance(descriptor, property)

def test_loan_has_loan_type():
    assert hasattr(Loan, "loan_type")
    descriptor = None
    for klass in Loan.__mro__:
        if "loan_type" in klass.__dict__:
            descriptor = klass.__dict__["loan_type"]
            break
    assert isinstance(descriptor, property)

def test_loan_has_loan_interst():
    assert hasattr(Loan, "loan_interst")
    descriptor = None
    for klass in Loan.__mro__:
        if "loan_interst" in klass.__dict__:
            descriptor = klass.__dict__["loan_interst"]
            break
    assert isinstance(descriptor, property)

def test_loan_has_emp_id():
    assert hasattr(Loan, "emp_id")
    descriptor = None
    for klass in Loan.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
            break
    assert isinstance(descriptor, property)

def test_loan_has_amount():
    assert hasattr(Loan, "amount")
    descriptor = None
    for klass in Loan.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_payslip_is_not_abstract():
    assert not inspect.isabstract(payslip)


def test_payslip_constructor_exists():
    assert callable(payslip.__init__)


def test_payslip_constructor_args():
    sig = inspect.signature(payslip.__init__)
    params = list(sig.parameters.keys())
    assert "emp_name" in params, "Missing parameter 'emp_name'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"

def test_payslip_has_emp_name():
    assert hasattr(payslip, "emp_name")
    descriptor = None
    for klass in payslip.__mro__:
        if "emp_name" in klass.__dict__:
            descriptor = klass.__dict__["emp_name"]
            break
    assert isinstance(descriptor, property)

def test_payslip_has_emp_id():
    assert hasattr(payslip, "emp_id")
    descriptor = None
    for klass in payslip.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
            break
    assert isinstance(descriptor, property)



def test_attendence_is_not_abstract():
    assert not inspect.isabstract(Attendence)


def test_attendence_constructor_exists():
    assert callable(Attendence.__init__)


def test_attendence_constructor_args():
    sig = inspect.signature(Attendence.__init__)
    params = list(sig.parameters.keys())
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "Basic_salary" in params, "Missing parameter 'Basic_salary'"
    assert "emp_name" in params, "Missing parameter 'emp_name'"

def test_attendence_has_emp_id():
    assert hasattr(Attendence, "emp_id")
    descriptor = None
    for klass in Attendence.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
            break
    assert isinstance(descriptor, property)

def test_attendence_has_Basic_salary():
    assert hasattr(Attendence, "Basic_salary")
    descriptor = None
    for klass in Attendence.__mro__:
        if "Basic_salary" in klass.__dict__:
            descriptor = klass.__dict__["Basic_salary"]
            break
    assert isinstance(descriptor, property)

def test_attendence_has_emp_name():
    assert hasattr(Attendence, "emp_name")
    descriptor = None
    for klass in Attendence.__mro__:
        if "emp_name" in klass.__dict__:
            descriptor = klass.__dict__["emp_name"]
            break
    assert isinstance(descriptor, property)



def test_employeerequest_is_not_abstract():
    assert not inspect.isabstract(EmployeeRequest)


def test_employeerequest_constructor_exists():
    assert callable(EmployeeRequest.__init__)


def test_employeerequest_constructor_args():
    sig = inspect.signature(EmployeeRequest.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "adminEmail" in params, "Missing parameter 'adminEmail'"

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_adminEmail():
    assert hasattr(Admin, "adminEmail")
    descriptor = None
    for klass in Admin.__mro__:
        if "adminEmail" in klass.__dict__:
            descriptor = klass.__dict__["adminEmail"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "emp_id" in params, "Missing parameter 'emp_id'"
    assert "basic_salary" in params, "Missing parameter 'basic_salary'"
    assert "emp_name" in params, "Missing parameter 'emp_name'"

def test_salary_has_emp_id():
    assert hasattr(Salary, "emp_id")
    descriptor = None
    for klass in Salary.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_basic_salary():
    assert hasattr(Salary, "basic_salary")
    descriptor = None
    for klass in Salary.__mro__:
        if "basic_salary" in klass.__dict__:
            descriptor = klass.__dict__["basic_salary"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_emp_name():
    assert hasattr(Salary, "emp_name")
    descriptor = None
    for klass in Salary.__mro__:
        if "emp_name" in klass.__dict__:
            descriptor = klass.__dict__["emp_name"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "emp_email" in params, "Missing parameter 'emp_email'"
    assert "emp_name" in params, "Missing parameter 'emp_name'"
    assert "emp_id" in params, "Missing parameter 'emp_id'"

def test_employee_has_emp_email():
    assert hasattr(Employee, "emp_email")
    descriptor = None
    for klass in Employee.__mro__:
        if "emp_email" in klass.__dict__:
            descriptor = klass.__dict__["emp_email"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_emp_name():
    assert hasattr(Employee, "emp_name")
    descriptor = None
    for klass in Employee.__mro__:
        if "emp_name" in klass.__dict__:
            descriptor = klass.__dict__["emp_name"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_emp_id():
    assert hasattr(Employee, "emp_id")
    descriptor = None
    for klass in Employee.__mro__:
        if "emp_id" in klass.__dict__:
            descriptor = klass.__dict__["emp_id"]
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
Loan_strategy = st.builds(
    Loan,
    loan_purpose=
        safe_text,
    emp_name=
        safe_text,
    loan_type=
        safe_text,
    loan_interst=
        st.integers(),
    emp_id=
        st.integers(),
    amount=
        safe_text
)
payslip_strategy = st.builds(
    payslip,
    emp_name=
        safe_text,
    emp_id=
        st.integers()
)
Attendence_strategy = st.builds(
    Attendence,
    emp_id=
        st.integers(),
    Basic_salary=
        st.integers(),
    emp_name=
        safe_text
)
EmployeeRequest_strategy = st.builds(
    EmployeeRequest,
)
Admin_strategy = st.builds(
    Admin,
    password=
        st.integers(),
    adminEmail=
        safe_text
)
Login_strategy = st.builds(
    Login,
    username=
        safe_text,
    password=
        st.integers()
)
Salary_strategy = st.builds(
    Salary,
    emp_id=
        st.integers(),
    basic_salary=
        safe_text,
    emp_name=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    emp_email=
        safe_text,
    emp_name=
        safe_text,
    emp_id=
        st.integers()
)

@given(instance=Loan_strategy)
@settings(max_examples=50)
def test_loan_instantiation(instance):
    assert isinstance(instance, Loan)



@given(instance=Loan_strategy)
def test_loan_loan_purpose_setter(instance):
    original = instance.loan_purpose
    instance.loan_purpose = original
    assert instance.loan_purpose == original



@given(instance=Loan_strategy)
def test_loan_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original



@given(instance=Loan_strategy)
def test_loan_loan_type_setter(instance):
    original = instance.loan_type
    instance.loan_type = original
    assert instance.loan_type == original



@given(instance=Loan_strategy)
def test_loan_loan_interst_setter(instance):
    original = instance.loan_interst
    instance.loan_interst = original
    assert instance.loan_interst == original



@given(instance=Loan_strategy)
def test_loan_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Loan_strategy)
def test_loan_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=payslip_strategy)
@settings(max_examples=50)
def test_payslip_instantiation(instance):
    assert isinstance(instance, payslip)



@given(instance=payslip_strategy)
def test_payslip_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original



@given(instance=payslip_strategy)
def test_payslip_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original

@given(instance=Attendence_strategy)
@settings(max_examples=50)
def test_attendence_instantiation(instance):
    assert isinstance(instance, Attendence)



@given(instance=Attendence_strategy)
def test_attendence_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Attendence_strategy)
def test_attendence_Basic_salary_setter(instance):
    original = instance.Basic_salary
    instance.Basic_salary = original
    assert instance.Basic_salary == original



@given(instance=Attendence_strategy)
def test_attendence_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original

@given(instance=EmployeeRequest_strategy)
@settings(max_examples=50)
def test_employeerequest_instantiation(instance):
    assert isinstance(instance, EmployeeRequest)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_admin_adminEmail_setter(instance):
    original = instance.adminEmail
    instance.adminEmail = original
    assert instance.adminEmail == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)



@given(instance=Salary_strategy)
def test_salary_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original



@given(instance=Salary_strategy)
def test_salary_basic_salary_setter(instance):
    original = instance.basic_salary
    instance.basic_salary = original
    assert instance.basic_salary == original



@given(instance=Salary_strategy)
def test_salary_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_emp_email_setter(instance):
    original = instance.emp_email
    instance.emp_email = original
    assert instance.emp_email == original



@given(instance=Employee_strategy)
def test_employee_emp_name_setter(instance):
    original = instance.emp_name
    instance.emp_name = original
    assert instance.emp_name == original



@given(instance=Employee_strategy)
def test_employee_emp_id_setter(instance):
    original = instance.emp_id
    instance.emp_id = original
    assert instance.emp_id == original
