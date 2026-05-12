import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    delete_employee_external,
    update_salary_external,
    Pay_Salary_external,
    update_leaves_external,
    Request_a_leave_external,
    change_password_external,
    manage_leave_requests_external,
    Update_Employee_external,
    Salary_reports_external,
    View_list_of_all_employees_external,
    logout_external,
    login_external,
    Add_Employee_external,
    Edit_profile_external,
    Class,
    Employee_Actor,
    _Component,
    Actor_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_delete_employee_external_is_not_abstract():
    assert not inspect.isabstract(delete_employee_external)


def test_delete_employee_external_constructor_exists():
    assert callable(delete_employee_external.__init__)


def test_delete_employee_external_constructor_args():
    sig = inspect.signature(delete_employee_external.__init__)
    params = list(sig.parameters.keys())



def test_update_salary_external_is_not_abstract():
    assert not inspect.isabstract(update_salary_external)


def test_update_salary_external_constructor_exists():
    assert callable(update_salary_external.__init__)


def test_update_salary_external_constructor_args():
    sig = inspect.signature(update_salary_external.__init__)
    params = list(sig.parameters.keys())



def test_pay_salary_external_is_not_abstract():
    assert not inspect.isabstract(Pay_Salary_external)


def test_pay_salary_external_constructor_exists():
    assert callable(Pay_Salary_external.__init__)


def test_pay_salary_external_constructor_args():
    sig = inspect.signature(Pay_Salary_external.__init__)
    params = list(sig.parameters.keys())



def test_update_leaves_external_is_not_abstract():
    assert not inspect.isabstract(update_leaves_external)


def test_update_leaves_external_constructor_exists():
    assert callable(update_leaves_external.__init__)


def test_update_leaves_external_constructor_args():
    sig = inspect.signature(update_leaves_external.__init__)
    params = list(sig.parameters.keys())



def test_request_a_leave_external_is_not_abstract():
    assert not inspect.isabstract(Request_a_leave_external)


def test_request_a_leave_external_constructor_exists():
    assert callable(Request_a_leave_external.__init__)


def test_request_a_leave_external_constructor_args():
    sig = inspect.signature(Request_a_leave_external.__init__)
    params = list(sig.parameters.keys())



def test_change_password_external_is_not_abstract():
    assert not inspect.isabstract(change_password_external)


def test_change_password_external_constructor_exists():
    assert callable(change_password_external.__init__)


def test_change_password_external_constructor_args():
    sig = inspect.signature(change_password_external.__init__)
    params = list(sig.parameters.keys())



def test_manage_leave_requests_external_is_not_abstract():
    assert not inspect.isabstract(manage_leave_requests_external)


def test_manage_leave_requests_external_constructor_exists():
    assert callable(manage_leave_requests_external.__init__)


def test_manage_leave_requests_external_constructor_args():
    sig = inspect.signature(manage_leave_requests_external.__init__)
    params = list(sig.parameters.keys())



def test_update_employee_external_is_not_abstract():
    assert not inspect.isabstract(Update_Employee_external)


def test_update_employee_external_constructor_exists():
    assert callable(Update_Employee_external.__init__)


def test_update_employee_external_constructor_args():
    sig = inspect.signature(Update_Employee_external.__init__)
    params = list(sig.parameters.keys())



def test_salary_reports_external_is_not_abstract():
    assert not inspect.isabstract(Salary_reports_external)


def test_salary_reports_external_constructor_exists():
    assert callable(Salary_reports_external.__init__)


def test_salary_reports_external_constructor_args():
    sig = inspect.signature(Salary_reports_external.__init__)
    params = list(sig.parameters.keys())



def test_view_list_of_all_employees_external_is_not_abstract():
    assert not inspect.isabstract(View_list_of_all_employees_external)


def test_view_list_of_all_employees_external_constructor_exists():
    assert callable(View_list_of_all_employees_external.__init__)


def test_view_list_of_all_employees_external_constructor_args():
    sig = inspect.signature(View_list_of_all_employees_external.__init__)
    params = list(sig.parameters.keys())



def test_logout_external_is_not_abstract():
    assert not inspect.isabstract(logout_external)


def test_logout_external_constructor_exists():
    assert callable(logout_external.__init__)


def test_logout_external_constructor_args():
    sig = inspect.signature(logout_external.__init__)
    params = list(sig.parameters.keys())



def test_login_external_is_not_abstract():
    assert not inspect.isabstract(login_external)


def test_login_external_constructor_exists():
    assert callable(login_external.__init__)


def test_login_external_constructor_args():
    sig = inspect.signature(login_external.__init__)
    params = list(sig.parameters.keys())



def test_add_employee_external_is_not_abstract():
    assert not inspect.isabstract(Add_Employee_external)


def test_add_employee_external_constructor_exists():
    assert callable(Add_Employee_external.__init__)


def test_add_employee_external_constructor_args():
    sig = inspect.signature(Add_Employee_external.__init__)
    params = list(sig.parameters.keys())



def test_edit_profile_external_is_not_abstract():
    assert not inspect.isabstract(Edit_profile_external)


def test_edit_profile_external_constructor_exists():
    assert callable(Edit_profile_external.__init__)


def test_edit_profile_external_constructor_args():
    sig = inspect.signature(Edit_profile_external.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_employee_actor_is_not_abstract():
    assert not inspect.isabstract(Employee_Actor)


def test_employee_actor_constructor_exists():
    assert callable(Employee_Actor.__init__)


def test_employee_actor_constructor_args():
    sig = inspect.signature(Employee_Actor.__init__)
    params = list(sig.parameters.keys())



def test__component_is_not_abstract():
    assert not inspect.isabstract(_Component)


def test__component_constructor_exists():
    assert callable(_Component.__init__)


def test__component_constructor_args():
    sig = inspect.signature(_Component.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
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
delete_employee_external_strategy = st.builds(
    delete_employee_external,
)
update_salary_external_strategy = st.builds(
    update_salary_external,
)
Pay_Salary_external_strategy = st.builds(
    Pay_Salary_external,
)
update_leaves_external_strategy = st.builds(
    update_leaves_external,
)
Request_a_leave_external_strategy = st.builds(
    Request_a_leave_external,
)
change_password_external_strategy = st.builds(
    change_password_external,
)
manage_leave_requests_external_strategy = st.builds(
    manage_leave_requests_external,
)
Update_Employee_external_strategy = st.builds(
    Update_Employee_external,
)
Salary_reports_external_strategy = st.builds(
    Salary_reports_external,
)
View_list_of_all_employees_external_strategy = st.builds(
    View_list_of_all_employees_external,
)
logout_external_strategy = st.builds(
    logout_external,
)
login_external_strategy = st.builds(
    login_external,
)
Add_Employee_external_strategy = st.builds(
    Add_Employee_external,
)
Edit_profile_external_strategy = st.builds(
    Edit_profile_external,
)
Class_strategy = st.builds(
    Class,
)
Employee_Actor_strategy = st.builds(
    Employee_Actor,
)
_Component_strategy = st.builds(
    _Component,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)

@given(instance=delete_employee_external_strategy)
@settings(max_examples=50)
def test_delete_employee_external_instantiation(instance):
    assert isinstance(instance, delete_employee_external)

@given(instance=update_salary_external_strategy)
@settings(max_examples=50)
def test_update_salary_external_instantiation(instance):
    assert isinstance(instance, update_salary_external)

@given(instance=Pay_Salary_external_strategy)
@settings(max_examples=50)
def test_pay_salary_external_instantiation(instance):
    assert isinstance(instance, Pay_Salary_external)

@given(instance=update_leaves_external_strategy)
@settings(max_examples=50)
def test_update_leaves_external_instantiation(instance):
    assert isinstance(instance, update_leaves_external)

@given(instance=Request_a_leave_external_strategy)
@settings(max_examples=50)
def test_request_a_leave_external_instantiation(instance):
    assert isinstance(instance, Request_a_leave_external)

@given(instance=change_password_external_strategy)
@settings(max_examples=50)
def test_change_password_external_instantiation(instance):
    assert isinstance(instance, change_password_external)

@given(instance=manage_leave_requests_external_strategy)
@settings(max_examples=50)
def test_manage_leave_requests_external_instantiation(instance):
    assert isinstance(instance, manage_leave_requests_external)

@given(instance=Update_Employee_external_strategy)
@settings(max_examples=50)
def test_update_employee_external_instantiation(instance):
    assert isinstance(instance, Update_Employee_external)

@given(instance=Salary_reports_external_strategy)
@settings(max_examples=50)
def test_salary_reports_external_instantiation(instance):
    assert isinstance(instance, Salary_reports_external)

@given(instance=View_list_of_all_employees_external_strategy)
@settings(max_examples=50)
def test_view_list_of_all_employees_external_instantiation(instance):
    assert isinstance(instance, View_list_of_all_employees_external)

@given(instance=logout_external_strategy)
@settings(max_examples=50)
def test_logout_external_instantiation(instance):
    assert isinstance(instance, logout_external)

@given(instance=login_external_strategy)
@settings(max_examples=50)
def test_login_external_instantiation(instance):
    assert isinstance(instance, login_external)

@given(instance=Add_Employee_external_strategy)
@settings(max_examples=50)
def test_add_employee_external_instantiation(instance):
    assert isinstance(instance, Add_Employee_external)

@given(instance=Edit_profile_external_strategy)
@settings(max_examples=50)
def test_edit_profile_external_instantiation(instance):
    assert isinstance(instance, Edit_profile_external)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Employee_Actor_strategy)
@settings(max_examples=50)
def test_employee_actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)

@given(instance=_Component_strategy)
@settings(max_examples=50)
def test__component_instantiation(instance):
    assert isinstance(instance, _Component)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)
