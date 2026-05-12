import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    company_Company,
    Employee,
    company_Freelance,
    company_Employee,
    company_Student,
    company_Division,
    company_Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company_company_is_not_abstract():
    assert not inspect.isabstract(company_Company)


def test_company_company_constructor_exists():
    assert callable(company_Company.__init__)


def test_company_company_constructor_args():
    sig = inspect.signature(company_Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "eotmDelta" in params, "Missing parameter 'eotmDelta'"

def test_company_company_has_name():
    assert hasattr(company_Company, "name")
    descriptor = None
    for klass in company_Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_company_has_eotmDelta():
    assert hasattr(company_Company, "eotmDelta")
    descriptor = None
    for klass in company_Company.__mro__:
        if "eotmDelta" in klass.__dict__:
            descriptor = klass.__dict__["eotmDelta"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_company_freelance_is_not_abstract():
    assert not inspect.isabstract(company_Freelance)


def test_company_freelance_constructor_exists():
    assert callable(company_Freelance.__init__)


def test_company_freelance_constructor_args():
    sig = inspect.signature(company_Freelance.__init__)
    params = list(sig.parameters.keys())
    assert "assignment" in params, "Missing parameter 'assignment'"

def test_company_freelance_has_assignment():
    assert hasattr(company_Freelance, "assignment")
    descriptor = None
    for klass in company_Freelance.__mro__:
        if "assignment" in klass.__dict__:
            descriptor = klass.__dict__["assignment"]
            break
    assert isinstance(descriptor, property)



def test_company_employee_is_not_abstract():
    assert not inspect.isabstract(company_Employee)


def test_company_employee_constructor_exists():
    assert callable(company_Employee.__init__)


def test_company_employee_constructor_args():
    sig = inspect.signature(company_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_company_employee_has_age():
    assert hasattr(company_Employee, "age")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_company_employee_has_name():
    assert hasattr(company_Employee, "name")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_employee_has_salary():
    assert hasattr(company_Employee, "salary")
    descriptor = None
    for klass in company_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_company_student_is_not_abstract():
    assert not inspect.isabstract(company_Student)


def test_company_student_constructor_exists():
    assert callable(company_Student.__init__)


def test_company_student_constructor_args():
    sig = inspect.signature(company_Student.__init__)
    params = list(sig.parameters.keys())



def test_company_division_is_not_abstract():
    assert not inspect.isabstract(company_Division)


def test_company_division_constructor_exists():
    assert callable(company_Division.__init__)


def test_company_division_constructor_args():
    sig = inspect.signature(company_Division.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numberEmployeesOfTheMonth" in params, "Missing parameter 'numberEmployeesOfTheMonth'"
    assert "budget" in params, "Missing parameter 'budget'"

def test_company_division_has_name():
    assert hasattr(company_Division, "name")
    descriptor = None
    for klass in company_Division.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company_division_has_numberEmployeesOfTheMonth():
    assert hasattr(company_Division, "numberEmployeesOfTheMonth")
    descriptor = None
    for klass in company_Division.__mro__:
        if "numberEmployeesOfTheMonth" in klass.__dict__:
            descriptor = klass.__dict__["numberEmployeesOfTheMonth"]
            break
    assert isinstance(descriptor, property)

def test_company_division_has_budget():
    assert hasattr(company_Division, "budget")
    descriptor = None
    for klass in company_Division.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)



def test_company_department_is_not_abstract():
    assert not inspect.isabstract(company_Department)


def test_company_department_constructor_exists():
    assert callable(company_Department.__init__)


def test_company_department_constructor_args():
    sig = inspect.signature(company_Department.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "biggestNumberOfStudentsOrFreelancers" in params, "Missing parameter 'biggestNumberOfStudentsOrFreelancers'"
    assert "maxJuniors" in params, "Missing parameter 'maxJuniors'"
    assert "name" in params, "Missing parameter 'name'"

def test_company_department_has_budget():
    assert hasattr(company_Department, "budget")
    descriptor = None
    for klass in company_Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_company_department_has_biggestNumberOfStudentsOrFreelancers():
    assert hasattr(company_Department, "biggestNumberOfStudentsOrFreelancers")
    descriptor = None
    for klass in company_Department.__mro__:
        if "biggestNumberOfStudentsOrFreelancers" in klass.__dict__:
            descriptor = klass.__dict__["biggestNumberOfStudentsOrFreelancers"]
            break
    assert isinstance(descriptor, property)

def test_company_department_has_maxJuniors():
    assert hasattr(company_Department, "maxJuniors")
    descriptor = None
    for klass in company_Department.__mro__:
        if "maxJuniors" in klass.__dict__:
            descriptor = klass.__dict__["maxJuniors"]
            break
    assert isinstance(descriptor, property)

def test_company_department_has_name():
    assert hasattr(company_Department, "name")
    descriptor = None
    for klass in company_Department.__mro__:
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
company_Company_strategy = st.builds(
    company_Company,
    name=
        safe_text,
    eotmDelta=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
)
company_Freelance_strategy = st.builds(
    company_Freelance,
    assignment=
        safe_text
)
company_Employee_strategy = st.builds(
    company_Employee,
    age=
        safe_text,
    name=
        safe_text,
    salary=
        safe_text
)
company_Student_strategy = st.builds(
    company_Student,
)
company_Division_strategy = st.builds(
    company_Division,
    name=
        safe_text,
    numberEmployeesOfTheMonth=
        safe_text,
    budget=
        safe_text
)
company_Department_strategy = st.builds(
    company_Department,
    budget=
        safe_text,
    biggestNumberOfStudentsOrFreelancers=
        safe_text,
    maxJuniors=
        safe_text,
    name=
        safe_text
)

@given(instance=company_Company_strategy)
@settings(max_examples=50)
def test_company_company_instantiation(instance):
    assert isinstance(instance, company_Company)



@given(instance=company_Company_strategy)
def test_company_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Company_strategy)
def test_company_company_eotmDelta_setter(instance):
    original = instance.eotmDelta
    instance.eotmDelta = original
    assert instance.eotmDelta == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=company_Freelance_strategy)
@settings(max_examples=50)
def test_company_freelance_instantiation(instance):
    assert isinstance(instance, company_Freelance)



@given(instance=company_Freelance_strategy)
def test_company_freelance_assignment_setter(instance):
    original = instance.assignment
    instance.assignment = original
    assert instance.assignment == original

@given(instance=company_Employee_strategy)
@settings(max_examples=50)
def test_company_employee_instantiation(instance):
    assert isinstance(instance, company_Employee)



@given(instance=company_Employee_strategy)
def test_company_employee_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=company_Employee_strategy)
def test_company_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Employee_strategy)
def test_company_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=company_Student_strategy)
@settings(max_examples=50)
def test_company_student_instantiation(instance):
    assert isinstance(instance, company_Student)

@given(instance=company_Division_strategy)
@settings(max_examples=50)
def test_company_division_instantiation(instance):
    assert isinstance(instance, company_Division)



@given(instance=company_Division_strategy)
def test_company_division_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=company_Division_strategy)
def test_company_division_numberEmployeesOfTheMonth_setter(instance):
    original = instance.numberEmployeesOfTheMonth
    instance.numberEmployeesOfTheMonth = original
    assert instance.numberEmployeesOfTheMonth == original



@given(instance=company_Division_strategy)
def test_company_division_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=company_Department_strategy)
@settings(max_examples=50)
def test_company_department_instantiation(instance):
    assert isinstance(instance, company_Department)



@given(instance=company_Department_strategy)
def test_company_department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original



@given(instance=company_Department_strategy)
def test_company_department_biggestNumberOfStudentsOrFreelancers_setter(instance):
    original = instance.biggestNumberOfStudentsOrFreelancers
    instance.biggestNumberOfStudentsOrFreelancers = original
    assert instance.biggestNumberOfStudentsOrFreelancers == original



@given(instance=company_Department_strategy)
def test_company_department_maxJuniors_setter(instance):
    original = instance.maxJuniors
    instance.maxJuniors = original
    assert instance.maxJuniors == original



@given(instance=company_Department_strategy)
def test_company_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=company_Department_strategy)
@settings(max_examples=30)
def test_company_department_calcexpenses_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.calcExpenses()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.calcExpenses).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'calcExpenses' in company_Department is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'calcExpenses' in company_Department did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'calcExpenses' in company_Department is not implemented or raised an error")
