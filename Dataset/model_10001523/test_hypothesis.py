import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Admin,
    Leave,
    Days_Attended,
    Salary,
    Employee,
    Login,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_admin_has_Email():
    assert hasattr(Admin, "Email")
    descriptor = None
    for klass in Admin.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Name():
    assert hasattr(Admin, "Name")
    descriptor = None
    for klass in Admin.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "Leave_NoOfDays" in params, "Missing parameter 'Leave_NoOfDays'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "Leave_Detail" in params, "Missing parameter 'Leave_Detail'"

def test_leave_has_Leave_NoOfDays():
    assert hasattr(Leave, "Leave_NoOfDays")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_NoOfDays" in klass.__dict__:
            descriptor = klass.__dict__["Leave_NoOfDays"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_attribute():
    assert hasattr(Leave, "attribute")
    descriptor = None
    for klass in Leave.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_Leave_Detail():
    assert hasattr(Leave, "Leave_Detail")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_Detail" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Detail"]
            break
    assert isinstance(descriptor, property)



def test_days_attended_is_not_abstract():
    assert not inspect.isabstract(Days_Attended)


def test_days_attended_constructor_exists():
    assert callable(Days_Attended.__init__)


def test_days_attended_constructor_args():
    sig = inspect.signature(Days_Attended.__init__)
    params = list(sig.parameters.keys())
    assert "Days_attended" in params, "Missing parameter 'Days_attended'"
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "EmployeeId" in params, "Missing parameter 'EmployeeId'"
    assert "EmployeeBasicSalary" in params, "Missing parameter 'EmployeeBasicSalary'"
    assert "Total_no__of_workingdays" in params, "Missing parameter 'Total_no__of_workingdays'"

def test_days_attended_has_Days_attended():
    assert hasattr(Days_Attended, "Days_attended")
    descriptor = None
    for klass in Days_Attended.__mro__:
        if "Days_attended" in klass.__dict__:
            descriptor = klass.__dict__["Days_attended"]
            break
    assert isinstance(descriptor, property)

def test_days_attended_has_OverTime():
    assert hasattr(Days_Attended, "OverTime")
    descriptor = None
    for klass in Days_Attended.__mro__:
        if "OverTime" in klass.__dict__:
            descriptor = klass.__dict__["OverTime"]
            break
    assert isinstance(descriptor, property)

def test_days_attended_has_EmployeeId():
    assert hasattr(Days_Attended, "EmployeeId")
    descriptor = None
    for klass in Days_Attended.__mro__:
        if "EmployeeId" in klass.__dict__:
            descriptor = klass.__dict__["EmployeeId"]
            break
    assert isinstance(descriptor, property)

def test_days_attended_has_EmployeeBasicSalary():
    assert hasattr(Days_Attended, "EmployeeBasicSalary")
    descriptor = None
    for klass in Days_Attended.__mro__:
        if "EmployeeBasicSalary" in klass.__dict__:
            descriptor = klass.__dict__["EmployeeBasicSalary"]
            break
    assert isinstance(descriptor, property)

def test_days_attended_has_Total_no__of_workingdays():
    assert hasattr(Days_Attended, "Total_no__of_workingdays")
    descriptor = None
    for klass in Days_Attended.__mro__:
        if "Total_no__of_workingdays" in klass.__dict__:
            descriptor = klass.__dict__["Total_no__of_workingdays"]
            break
    assert isinstance(descriptor, property)



def test_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "Bonus" in params, "Missing parameter 'Bonus'"
    assert "DaysAttended" in params, "Missing parameter 'DaysAttended'"
    assert "NetSalary" in params, "Missing parameter 'NetSalary'"
    assert "EmployeeID" in params, "Missing parameter 'EmployeeID'"

def test_salary_has_Bonus():
    assert hasattr(Salary, "Bonus")
    descriptor = None
    for klass in Salary.__mro__:
        if "Bonus" in klass.__dict__:
            descriptor = klass.__dict__["Bonus"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_DaysAttended():
    assert hasattr(Salary, "DaysAttended")
    descriptor = None
    for klass in Salary.__mro__:
        if "DaysAttended" in klass.__dict__:
            descriptor = klass.__dict__["DaysAttended"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_NetSalary():
    assert hasattr(Salary, "NetSalary")
    descriptor = None
    for klass in Salary.__mro__:
        if "NetSalary" in klass.__dict__:
            descriptor = klass.__dict__["NetSalary"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_EmployeeID():
    assert hasattr(Salary, "EmployeeID")
    descriptor = None
    for klass in Salary.__mro__:
        if "EmployeeID" in klass.__dict__:
            descriptor = klass.__dict__["EmployeeID"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "EmployeeId" in params, "Missing parameter 'EmployeeId'"
    assert "EmployeeEmail" in params, "Missing parameter 'EmployeeEmail'"
    assert "EmplyeeName" in params, "Missing parameter 'EmplyeeName'"
    assert "EmployeePhoneNumber" in params, "Missing parameter 'EmployeePhoneNumber'"

def test_employee_has_EmployeeId():
    assert hasattr(Employee, "EmployeeId")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmployeeId" in klass.__dict__:
            descriptor = klass.__dict__["EmployeeId"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmployeeEmail():
    assert hasattr(Employee, "EmployeeEmail")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmployeeEmail" in klass.__dict__:
            descriptor = klass.__dict__["EmployeeEmail"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmplyeeName():
    assert hasattr(Employee, "EmplyeeName")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmplyeeName" in klass.__dict__:
            descriptor = klass.__dict__["EmplyeeName"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmployeePhoneNumber():
    assert hasattr(Employee, "EmployeePhoneNumber")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmployeePhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["EmployeePhoneNumber"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_login_has_Username():
    assert hasattr(Login, "Username")
    descriptor = None
    for klass in Login.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_login_has_Password():
    assert hasattr(Login, "Password")
    descriptor = None
    for klass in Login.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
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
Admin_strategy = st.builds(
    Admin,
    Email=
        safe_text,
    Name=
        safe_text
)
Leave_strategy = st.builds(
    Leave,
    Leave_NoOfDays=
        st.integers(),
    attribute=
        safe_text,
    Leave_Detail=
        safe_text
)
Days_Attended_strategy = st.builds(
    Days_Attended,
    Days_attended=
        st.integers(),
    OverTime=
        st.integers(),
    EmployeeId=
        safe_text,
    EmployeeBasicSalary=
        st.integers(),
    Total_no__of_workingdays=
        st.integers()
)
Salary_strategy = st.builds(
    Salary,
    Bonus=
        st.integers(),
    DaysAttended=
        st.integers(),
    NetSalary=
        st.integers(),
    EmployeeID=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    EmployeeId=
        safe_text,
    EmployeeEmail=
        safe_text,
    EmplyeeName=
        safe_text,
    EmployeePhoneNumber=
        st.integers()
)
Login_strategy = st.builds(
    Login,
    Username=
        safe_text,
    Password=
        safe_text
)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Admin_strategy)
def test_admin_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Leave_strategy)
@settings(max_examples=50)
def test_leave_instantiation(instance):
    assert isinstance(instance, Leave)



@given(instance=Leave_strategy)
def test_leave_Leave_NoOfDays_setter(instance):
    original = instance.Leave_NoOfDays
    instance.Leave_NoOfDays = original
    assert instance.Leave_NoOfDays == original



@given(instance=Leave_strategy)
def test_leave_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Leave_strategy)
def test_leave_Leave_Detail_setter(instance):
    original = instance.Leave_Detail
    instance.Leave_Detail = original
    assert instance.Leave_Detail == original

@given(instance=Days_Attended_strategy)
@settings(max_examples=50)
def test_days_attended_instantiation(instance):
    assert isinstance(instance, Days_Attended)



@given(instance=Days_Attended_strategy)
def test_days_attended_Days_attended_setter(instance):
    original = instance.Days_attended
    instance.Days_attended = original
    assert instance.Days_attended == original



@given(instance=Days_Attended_strategy)
def test_days_attended_OverTime_setter(instance):
    original = instance.OverTime
    instance.OverTime = original
    assert instance.OverTime == original



@given(instance=Days_Attended_strategy)
def test_days_attended_EmployeeId_setter(instance):
    original = instance.EmployeeId
    instance.EmployeeId = original
    assert instance.EmployeeId == original



@given(instance=Days_Attended_strategy)
def test_days_attended_EmployeeBasicSalary_setter(instance):
    original = instance.EmployeeBasicSalary
    instance.EmployeeBasicSalary = original
    assert instance.EmployeeBasicSalary == original



@given(instance=Days_Attended_strategy)
def test_days_attended_Total_no__of_workingdays_setter(instance):
    original = instance.Total_no__of_workingdays
    instance.Total_no__of_workingdays = original
    assert instance.Total_no__of_workingdays == original

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)



@given(instance=Salary_strategy)
def test_salary_Bonus_setter(instance):
    original = instance.Bonus
    instance.Bonus = original
    assert instance.Bonus == original



@given(instance=Salary_strategy)
def test_salary_DaysAttended_setter(instance):
    original = instance.DaysAttended
    instance.DaysAttended = original
    assert instance.DaysAttended == original



@given(instance=Salary_strategy)
def test_salary_NetSalary_setter(instance):
    original = instance.NetSalary
    instance.NetSalary = original
    assert instance.NetSalary == original



@given(instance=Salary_strategy)
def test_salary_EmployeeID_setter(instance):
    original = instance.EmployeeID
    instance.EmployeeID = original
    assert instance.EmployeeID == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_EmployeeId_setter(instance):
    original = instance.EmployeeId
    instance.EmployeeId = original
    assert instance.EmployeeId == original



@given(instance=Employee_strategy)
def test_employee_EmployeeEmail_setter(instance):
    original = instance.EmployeeEmail
    instance.EmployeeEmail = original
    assert instance.EmployeeEmail == original



@given(instance=Employee_strategy)
def test_employee_EmplyeeName_setter(instance):
    original = instance.EmplyeeName
    instance.EmplyeeName = original
    assert instance.EmplyeeName == original



@given(instance=Employee_strategy)
def test_employee_EmployeePhoneNumber_setter(instance):
    original = instance.EmployeePhoneNumber
    instance.EmployeePhoneNumber = original
    assert instance.EmployeePhoneNumber == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Login_strategy)
def test_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original
