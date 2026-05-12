import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Awards,
    Backup,
    Employer,
    Normal_User,
    Supervisor,
    Admin,
    User,
    Half_Day,
    Casual_Leave,
    Sick_Leave,
    Temporary,
    Permanant,
    Attendance,
    Leave,
    Expenses,
    Salary,
    Employee,
    Login,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_awards_is_not_abstract():
    assert not inspect.isabstract(Awards)


def test_awards_constructor_exists():
    assert callable(Awards.__init__)


def test_awards_constructor_args():
    sig = inspect.signature(Awards.__init__)
    params = list(sig.parameters.keys())



def test_backup_is_not_abstract():
    assert not inspect.isabstract(Backup)


def test_backup_constructor_exists():
    assert callable(Backup.__init__)


def test_backup_constructor_args():
    sig = inspect.signature(Backup.__init__)
    params = list(sig.parameters.keys())



def test_employer_is_not_abstract():
    assert not inspect.isabstract(Employer)


def test_employer_constructor_exists():
    assert callable(Employer.__init__)


def test_employer_constructor_args():
    sig = inspect.signature(Employer.__init__)
    params = list(sig.parameters.keys())



def test_normal_user_is_not_abstract():
    assert not inspect.isabstract(Normal_User)


def test_normal_user_constructor_exists():
    assert callable(Normal_User.__init__)


def test_normal_user_constructor_args():
    sig = inspect.signature(Normal_User.__init__)
    params = list(sig.parameters.keys())



def test_supervisor_is_not_abstract():
    assert not inspect.isabstract(Supervisor)


def test_supervisor_constructor_exists():
    assert callable(Supervisor.__init__)


def test_supervisor_constructor_args():
    sig = inspect.signature(Supervisor.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())



def test_half_day_is_not_abstract():
    assert not inspect.isabstract(Half_Day)


def test_half_day_constructor_exists():
    assert callable(Half_Day.__init__)


def test_half_day_constructor_args():
    sig = inspect.signature(Half_Day.__init__)
    params = list(sig.parameters.keys())



def test_casual_leave_is_not_abstract():
    assert not inspect.isabstract(Casual_Leave)


def test_casual_leave_constructor_exists():
    assert callable(Casual_Leave.__init__)


def test_casual_leave_constructor_args():
    sig = inspect.signature(Casual_Leave.__init__)
    params = list(sig.parameters.keys())



def test_sick_leave_is_not_abstract():
    assert not inspect.isabstract(Sick_Leave)


def test_sick_leave_constructor_exists():
    assert callable(Sick_Leave.__init__)


def test_sick_leave_constructor_args():
    sig = inspect.signature(Sick_Leave.__init__)
    params = list(sig.parameters.keys())



def test_temporary_is_not_abstract():
    assert not inspect.isabstract(Temporary)


def test_temporary_constructor_exists():
    assert callable(Temporary.__init__)


def test_temporary_constructor_args():
    sig = inspect.signature(Temporary.__init__)
    params = list(sig.parameters.keys())



def test_permanant_is_not_abstract():
    assert not inspect.isabstract(Permanant)


def test_permanant_constructor_exists():
    assert callable(Permanant.__init__)


def test_permanant_constructor_args():
    sig = inspect.signature(Permanant.__init__)
    params = list(sig.parameters.keys())



def test_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())



def test_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())



def test_expenses_is_not_abstract():
    assert not inspect.isabstract(Expenses)


def test_expenses_constructor_exists():
    assert callable(Expenses.__init__)


def test_expenses_constructor_args():
    sig = inspect.signature(Expenses.__init__)
    params = list(sig.parameters.keys())



def test_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())


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
Awards_strategy = st.builds(
    Awards,
)
Backup_strategy = st.builds(
    Backup,
)
Employer_strategy = st.builds(
    Employer,
)
Normal_User_strategy = st.builds(
    Normal_User,
)
Supervisor_strategy = st.builds(
    Supervisor,
)
Admin_strategy = st.builds(
    Admin,
)
User_strategy = st.builds(
    User,
)
Half_Day_strategy = st.builds(
    Half_Day,
)
Casual_Leave_strategy = st.builds(
    Casual_Leave,
)
Sick_Leave_strategy = st.builds(
    Sick_Leave,
)
Temporary_strategy = st.builds(
    Temporary,
)
Permanant_strategy = st.builds(
    Permanant,
)
Attendance_strategy = st.builds(
    Attendance,
)
Leave_strategy = st.builds(
    Leave,
)
Expenses_strategy = st.builds(
    Expenses,
)
Salary_strategy = st.builds(
    Salary,
)
Employee_strategy = st.builds(
    Employee,
)
Login_strategy = st.builds(
    Login,
)

@given(instance=Awards_strategy)
@settings(max_examples=50)
def test_awards_instantiation(instance):
    assert isinstance(instance, Awards)

@given(instance=Backup_strategy)
@settings(max_examples=50)
def test_backup_instantiation(instance):
    assert isinstance(instance, Backup)

@given(instance=Employer_strategy)
@settings(max_examples=50)
def test_employer_instantiation(instance):
    assert isinstance(instance, Employer)

@given(instance=Normal_User_strategy)
@settings(max_examples=50)
def test_normal_user_instantiation(instance):
    assert isinstance(instance, Normal_User)

@given(instance=Supervisor_strategy)
@settings(max_examples=50)
def test_supervisor_instantiation(instance):
    assert isinstance(instance, Supervisor)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)

@given(instance=Half_Day_strategy)
@settings(max_examples=50)
def test_half_day_instantiation(instance):
    assert isinstance(instance, Half_Day)

@given(instance=Casual_Leave_strategy)
@settings(max_examples=50)
def test_casual_leave_instantiation(instance):
    assert isinstance(instance, Casual_Leave)

@given(instance=Sick_Leave_strategy)
@settings(max_examples=50)
def test_sick_leave_instantiation(instance):
    assert isinstance(instance, Sick_Leave)

@given(instance=Temporary_strategy)
@settings(max_examples=50)
def test_temporary_instantiation(instance):
    assert isinstance(instance, Temporary)

@given(instance=Permanant_strategy)
@settings(max_examples=50)
def test_permanant_instantiation(instance):
    assert isinstance(instance, Permanant)

@given(instance=Attendance_strategy)
@settings(max_examples=50)
def test_attendance_instantiation(instance):
    assert isinstance(instance, Attendance)

@given(instance=Leave_strategy)
@settings(max_examples=50)
def test_leave_instantiation(instance):
    assert isinstance(instance, Leave)

@given(instance=Expenses_strategy)
@settings(max_examples=50)
def test_expenses_instantiation(instance):
    assert isinstance(instance, Expenses)

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)
