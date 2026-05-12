import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    techStaff_DeveloperTest,
    techStaff_DatabaseAdminTest,
    techStaff_Developer,
    techStaff_DatabaseAdmin,
    Staff_Employee,
    Management_ManagerTest,
    Management_DirectorTest,
    Management_Manager,
    Management_Director,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_techstaff_developertest_is_not_abstract():
    assert not inspect.isabstract(techStaff_DeveloperTest)


def test_techstaff_developertest_constructor_exists():
    assert callable(techStaff_DeveloperTest.__init__)


def test_techstaff_developertest_constructor_args():
    sig = inspect.signature(techStaff_DeveloperTest.__init__)
    params = list(sig.parameters.keys())



def test_techstaff_databaseadmintest_is_not_abstract():
    assert not inspect.isabstract(techStaff_DatabaseAdminTest)


def test_techstaff_databaseadmintest_constructor_exists():
    assert callable(techStaff_DatabaseAdminTest.__init__)


def test_techstaff_databaseadmintest_constructor_args():
    sig = inspect.signature(techStaff_DatabaseAdminTest.__init__)
    params = list(sig.parameters.keys())



def test_techstaff_developer_is_not_abstract():
    assert not inspect.isabstract(techStaff_Developer)


def test_techstaff_developer_constructor_exists():
    assert callable(techStaff_Developer.__init__)


def test_techstaff_developer_constructor_args():
    sig = inspect.signature(techStaff_Developer.__init__)
    params = list(sig.parameters.keys())



def test_techstaff_databaseadmin_is_not_abstract():
    assert not inspect.isabstract(techStaff_DatabaseAdmin)


def test_techstaff_databaseadmin_constructor_exists():
    assert callable(techStaff_DatabaseAdmin.__init__)


def test_techstaff_databaseadmin_constructor_args():
    sig = inspect.signature(techStaff_DatabaseAdmin.__init__)
    params = list(sig.parameters.keys())



def test_staff_employee_is_not_abstract():
    assert not inspect.isabstract(Staff_Employee)


def test_staff_employee_constructor_exists():
    assert callable(Staff_Employee.__init__)


def test_staff_employee_constructor_args():
    sig = inspect.signature(Staff_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "nationalInsurance" in params, "Missing parameter 'nationalInsurance'"
    assert "salary" in params, "Missing parameter 'salary'"
    assert "name" in params, "Missing parameter 'name'"

def test_staff_employee_has_nationalInsurance():
    assert hasattr(Staff_Employee, "nationalInsurance")
    descriptor = None
    for klass in Staff_Employee.__mro__:
        if "nationalInsurance" in klass.__dict__:
            descriptor = klass.__dict__["nationalInsurance"]
            break
    assert isinstance(descriptor, property)

def test_staff_employee_has_salary():
    assert hasattr(Staff_Employee, "salary")
    descriptor = None
    for klass in Staff_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)

def test_staff_employee_has_name():
    assert hasattr(Staff_Employee, "name")
    descriptor = None
    for klass in Staff_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_management_managertest_is_not_abstract():
    assert not inspect.isabstract(Management_ManagerTest)


def test_management_managertest_constructor_exists():
    assert callable(Management_ManagerTest.__init__)


def test_management_managertest_constructor_args():
    sig = inspect.signature(Management_ManagerTest.__init__)
    params = list(sig.parameters.keys())



def test_management_directortest_is_not_abstract():
    assert not inspect.isabstract(Management_DirectorTest)


def test_management_directortest_constructor_exists():
    assert callable(Management_DirectorTest.__init__)


def test_management_directortest_constructor_args():
    sig = inspect.signature(Management_DirectorTest.__init__)
    params = list(sig.parameters.keys())



def test_management_manager_is_not_abstract():
    assert not inspect.isabstract(Management_Manager)


def test_management_manager_constructor_exists():
    assert callable(Management_Manager.__init__)


def test_management_manager_constructor_args():
    sig = inspect.signature(Management_Manager.__init__)
    params = list(sig.parameters.keys())
    assert "deptName" in params, "Missing parameter 'deptName'"

def test_management_manager_has_deptName():
    assert hasattr(Management_Manager, "deptName")
    descriptor = None
    for klass in Management_Manager.__mro__:
        if "deptName" in klass.__dict__:
            descriptor = klass.__dict__["deptName"]
            break
    assert isinstance(descriptor, property)



def test_management_director_is_not_abstract():
    assert not inspect.isabstract(Management_Director)


def test_management_director_constructor_exists():
    assert callable(Management_Director.__init__)


def test_management_director_constructor_args():
    sig = inspect.signature(Management_Director.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"

def test_management_director_has_budget():
    assert hasattr(Management_Director, "budget")
    descriptor = None
    for klass in Management_Director.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
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
techStaff_DeveloperTest_strategy = st.builds(
    techStaff_DeveloperTest,
)
techStaff_DatabaseAdminTest_strategy = st.builds(
    techStaff_DatabaseAdminTest,
)
techStaff_Developer_strategy = st.builds(
    techStaff_Developer,
)
techStaff_DatabaseAdmin_strategy = st.builds(
    techStaff_DatabaseAdmin,
)
Staff_Employee_strategy = st.builds(
    Staff_Employee,
    nationalInsurance=
        safe_text,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
Management_ManagerTest_strategy = st.builds(
    Management_ManagerTest,
)
Management_DirectorTest_strategy = st.builds(
    Management_DirectorTest,
)
Management_Manager_strategy = st.builds(
    Management_Manager,
    deptName=
        safe_text
)
Management_Director_strategy = st.builds(
    Management_Director,
    budget=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=techStaff_DeveloperTest_strategy)
@settings(max_examples=50)
def test_techstaff_developertest_instantiation(instance):
    assert isinstance(instance, techStaff_DeveloperTest)

@given(instance=techStaff_DatabaseAdminTest_strategy)
@settings(max_examples=50)
def test_techstaff_databaseadmintest_instantiation(instance):
    assert isinstance(instance, techStaff_DatabaseAdminTest)

@given(instance=techStaff_Developer_strategy)
@settings(max_examples=50)
def test_techstaff_developer_instantiation(instance):
    assert isinstance(instance, techStaff_Developer)

@given(instance=techStaff_DatabaseAdmin_strategy)
@settings(max_examples=50)
def test_techstaff_databaseadmin_instantiation(instance):
    assert isinstance(instance, techStaff_DatabaseAdmin)

@given(instance=Staff_Employee_strategy)
@settings(max_examples=50)
def test_staff_employee_instantiation(instance):
    assert isinstance(instance, Staff_Employee)



@given(instance=Staff_Employee_strategy)
def test_staff_employee_nationalInsurance_setter(instance):
    original = instance.nationalInsurance
    instance.nationalInsurance = original
    assert instance.nationalInsurance == original



@given(instance=Staff_Employee_strategy)
def test_staff_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original



@given(instance=Staff_Employee_strategy)
def test_staff_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Management_ManagerTest_strategy)
@settings(max_examples=50)
def test_management_managertest_instantiation(instance):
    assert isinstance(instance, Management_ManagerTest)

@given(instance=Management_DirectorTest_strategy)
@settings(max_examples=50)
def test_management_directortest_instantiation(instance):
    assert isinstance(instance, Management_DirectorTest)

@given(instance=Management_Manager_strategy)
@settings(max_examples=50)
def test_management_manager_instantiation(instance):
    assert isinstance(instance, Management_Manager)



@given(instance=Management_Manager_strategy)
def test_management_manager_deptName_setter(instance):
    original = instance.deptName
    instance.deptName = original
    assert instance.deptName == original

@given(instance=Management_Director_strategy)
@settings(max_examples=50)
def test_management_director_instantiation(instance):
    assert isinstance(instance, Management_Director)



@given(instance=Management_Director_strategy)
def test_management_director_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original
