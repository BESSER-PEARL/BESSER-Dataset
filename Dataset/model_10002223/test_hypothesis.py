import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Work_days,
    Salary,
    DaysAttended,
    Employee,
    Login,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_work_days_is_not_abstract():
    assert not inspect.isabstract(Work_days)


def test_work_days_constructor_exists():
    assert callable(Work_days.__init__)


def test_work_days_constructor_args():
    sig = inspect.signature(Work_days.__init__)
    params = list(sig.parameters.keys())
    assert "_No__of_working_days_" in params, "Missing parameter '_No__of_working_days_'"
    assert "Days_Attended" in params, "Missing parameter 'Days_Attended'"

def test_work_days_has__No__of_working_days_():
    assert hasattr(Work_days, "_No__of_working_days_")
    descriptor = None
    for klass in Work_days.__mro__:
        if "_No__of_working_days_" in klass.__dict__:
            descriptor = klass.__dict__["_No__of_working_days_"]
            break
    assert isinstance(descriptor, property)

def test_work_days_has_Days_Attended():
    assert hasattr(Work_days, "Days_Attended")
    descriptor = None
    for klass in Work_days.__mro__:
        if "Days_Attended" in klass.__dict__:
            descriptor = klass.__dict__["Days_Attended"]
            break
    assert isinstance(descriptor, property)



def test_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "Days_attended" in params, "Missing parameter 'Days_attended'"
    assert "Net_Salary" in params, "Missing parameter 'Net_Salary'"
    assert "Bonus__" in params, "Missing parameter 'Bonus__'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"

def test_salary_has_Days_attended():
    assert hasattr(Salary, "Days_attended")
    descriptor = None
    for klass in Salary.__mro__:
        if "Days_attended" in klass.__dict__:
            descriptor = klass.__dict__["Days_attended"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Net_Salary():
    assert hasattr(Salary, "Net_Salary")
    descriptor = None
    for klass in Salary.__mro__:
        if "Net_Salary" in klass.__dict__:
            descriptor = klass.__dict__["Net_Salary"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Bonus__():
    assert hasattr(Salary, "Bonus__")
    descriptor = None
    for klass in Salary.__mro__:
        if "Bonus__" in klass.__dict__:
            descriptor = klass.__dict__["Bonus__"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Emp_Id():
    assert hasattr(Salary, "Emp_Id")
    descriptor = None
    for klass in Salary.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)



def test_daysattended_is_not_abstract():
    assert not inspect.isabstract(DaysAttended)


def test_daysattended_constructor_exists():
    assert callable(DaysAttended.__init__)


def test_daysattended_constructor_args():
    sig = inspect.signature(DaysAttended.__init__)
    params = list(sig.parameters.keys())
    assert "Additional_hours__" in params, "Missing parameter 'Additional_hours__'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_BasicSalary" in params, "Missing parameter 'Emp_BasicSalary'"

def test_daysattended_has_Additional_hours__():
    assert hasattr(DaysAttended, "Additional_hours__")
    descriptor = None
    for klass in DaysAttended.__mro__:
        if "Additional_hours__" in klass.__dict__:
            descriptor = klass.__dict__["Additional_hours__"]
            break
    assert isinstance(descriptor, property)

def test_daysattended_has_Emp_Id():
    assert hasattr(DaysAttended, "Emp_Id")
    descriptor = None
    for klass in DaysAttended.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)

def test_daysattended_has_Emp_BasicSalary():
    assert hasattr(DaysAttended, "Emp_BasicSalary")
    descriptor = None
    for klass in DaysAttended.__mro__:
        if "Emp_BasicSalary" in klass.__dict__:
            descriptor = klass.__dict__["Emp_BasicSalary"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"
    assert "Emp_FName" in params, "Missing parameter 'Emp_FName'"

def test_employee_has_Emp_Id():
    assert hasattr(Employee, "Emp_Id")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Name():
    assert hasattr(Employee, "Emp_Name")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Name" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Name"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_FName():
    assert hasattr(Employee, "Emp_FName")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_FName" in klass.__dict__:
            descriptor = klass.__dict__["Emp_FName"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "User_Name" in params, "Missing parameter 'User_Name'"

def test_login_has_Password():
    assert hasattr(Login, "Password")
    descriptor = None
    for klass in Login.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_User_Name():
    assert hasattr(Login, "User_Name")
    descriptor = None
    for klass in Login.__mro__:
        if "User_Name" in klass.__dict__:
            descriptor = klass.__dict__["User_Name"]
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
Work_days_strategy = st.builds(
    Work_days,
    _No__of_working_days_=
        st.integers(),
    Days_Attended=
        st.integers()
)
Salary_strategy = st.builds(
    Salary,
    Days_attended=
        st.integers(),
    Net_Salary=
        safe_text,
    Bonus__=
        safe_text,
    Emp_Id=
        safe_text
)
DaysAttended_strategy = st.builds(
    DaysAttended,
    Additional_hours__=
        safe_text,
    Emp_Id=
        safe_text,
    Emp_BasicSalary=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    Emp_Id=
        safe_text,
    Emp_Name=
        safe_text,
    Emp_FName=
        safe_text
)
Login_strategy = st.builds(
    Login,
    Password=
        safe_text,
    User_Name=
        safe_text
)

@given(instance=Work_days_strategy)
@settings(max_examples=50)
def test_work_days_instantiation(instance):
    assert isinstance(instance, Work_days)



@given(instance=Work_days_strategy)
def test_work_days__No__of_working_days__setter(instance):
    original = instance._No__of_working_days_
    instance._No__of_working_days_ = original
    assert instance._No__of_working_days_ == original



@given(instance=Work_days_strategy)
def test_work_days_Days_Attended_setter(instance):
    original = instance.Days_Attended
    instance.Days_Attended = original
    assert instance.Days_Attended == original

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)



@given(instance=Salary_strategy)
def test_salary_Days_attended_setter(instance):
    original = instance.Days_attended
    instance.Days_attended = original
    assert instance.Days_attended == original



@given(instance=Salary_strategy)
def test_salary_Net_Salary_setter(instance):
    original = instance.Net_Salary
    instance.Net_Salary = original
    assert instance.Net_Salary == original



@given(instance=Salary_strategy)
def test_salary_Bonus___setter(instance):
    original = instance.Bonus__
    instance.Bonus__ = original
    assert instance.Bonus__ == original



@given(instance=Salary_strategy)
def test_salary_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original

@given(instance=DaysAttended_strategy)
@settings(max_examples=50)
def test_daysattended_instantiation(instance):
    assert isinstance(instance, DaysAttended)



@given(instance=DaysAttended_strategy)
def test_daysattended_Additional_hours___setter(instance):
    original = instance.Additional_hours__
    instance.Additional_hours__ = original
    assert instance.Additional_hours__ == original



@given(instance=DaysAttended_strategy)
def test_daysattended_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=DaysAttended_strategy)
def test_daysattended_Emp_BasicSalary_setter(instance):
    original = instance.Emp_BasicSalary
    instance.Emp_BasicSalary = original
    assert instance.Emp_BasicSalary == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Employee_strategy)
def test_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original



@given(instance=Employee_strategy)
def test_employee_Emp_FName_setter(instance):
    original = instance.Emp_FName
    instance.Emp_FName = original
    assert instance.Emp_FName == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Login_strategy)
def test_login_User_Name_setter(instance):
    original = instance.User_Name
    instance.User_Name = original
    assert instance.User_Name == original
