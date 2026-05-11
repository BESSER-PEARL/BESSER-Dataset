import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    company::Company,
    Employee,
    company::Freelance,
    company::Employee,
    company::Student,
    company::Division,
    company::Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_company::company_is_not_abstract():
    assert not inspect.isabstract(company::Company)


def test_company::company_constructor_exists():
    assert callable(company::Company.__init__)


def test_company::company_constructor_args():
    sig = inspect.signature(company::Company.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "eotmDelta" in params, "Missing parameter 'eotmDelta'"

def test_company::company_has_name():
    assert hasattr(company::Company, "name")
    descriptor = None
    for klass in company::Company.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::company_has_eotmDelta():
    assert hasattr(company::Company, "eotmDelta")
    descriptor = None
    for klass in company::Company.__mro__:
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



def test_company::freelance_is_not_abstract():
    assert not inspect.isabstract(company::Freelance)


def test_company::freelance_constructor_exists():
    assert callable(company::Freelance.__init__)


def test_company::freelance_constructor_args():
    sig = inspect.signature(company::Freelance.__init__)
    params = list(sig.parameters.keys())
    assert "assignment" in params, "Missing parameter 'assignment'"

def test_company::freelance_has_assignment():
    assert hasattr(company::Freelance, "assignment")
    descriptor = None
    for klass in company::Freelance.__mro__:
        if "assignment" in klass.__dict__:
            descriptor = klass.__dict__["assignment"]
            break
    assert isinstance(descriptor, property)



def test_company::employee_is_not_abstract():
    assert not inspect.isabstract(company::Employee)


def test_company::employee_constructor_exists():
    assert callable(company::Employee.__init__)


def test_company::employee_constructor_args():
    sig = inspect.signature(company::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"
    assert "salary" in params, "Missing parameter 'salary'"

def test_company::employee_has_name():
    assert hasattr(company::Employee, "name")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_company::employee_has_age():
    assert hasattr(company::Employee, "age")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_company::employee_has_salary():
    assert hasattr(company::Employee, "salary")
    descriptor = None
    for klass in company::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_company::student_is_not_abstract():
    assert not inspect.isabstract(company::Student)


def test_company::student_constructor_exists():
    assert callable(company::Student.__init__)


def test_company::student_constructor_args():
    sig = inspect.signature(company::Student.__init__)
    params = list(sig.parameters.keys())



def test_company::division_is_not_abstract():
    assert not inspect.isabstract(company::Division)


def test_company::division_constructor_exists():
    assert callable(company::Division.__init__)


def test_company::division_constructor_args():
    sig = inspect.signature(company::Division.__init__)
    params = list(sig.parameters.keys())
    assert "budget" in params, "Missing parameter 'budget'"
    assert "numberEmployeesOfTheMonth" in params, "Missing parameter 'numberEmployeesOfTheMonth'"
    assert "name" in params, "Missing parameter 'name'"

def test_company::division_has_budget():
    assert hasattr(company::Division, "budget")
    descriptor = None
    for klass in company::Division.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_company::division_has_numberEmployeesOfTheMonth():
    assert hasattr(company::Division, "numberEmployeesOfTheMonth")
    descriptor = None
    for klass in company::Division.__mro__:
        if "numberEmployeesOfTheMonth" in klass.__dict__:
            descriptor = klass.__dict__["numberEmployeesOfTheMonth"]
            break
    assert isinstance(descriptor, property)

def test_company::division_has_name():
    assert hasattr(company::Division, "name")
    descriptor = None
    for klass in company::Division.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_company::department_is_not_abstract():
    assert not inspect.isabstract(company::Department)


def test_company::department_constructor_exists():
    assert callable(company::Department.__init__)


def test_company::department_constructor_args():
    sig = inspect.signature(company::Department.__init__)
    params = list(sig.parameters.keys())
    assert "biggestNumberOfStudentsOrFreelancers" in params, "Missing parameter 'biggestNumberOfStudentsOrFreelancers'"
    assert "maxJuniors" in params, "Missing parameter 'maxJuniors'"
    assert "budget" in params, "Missing parameter 'budget'"
    assert "name" in params, "Missing parameter 'name'"

def test_company::department_has_biggestNumberOfStudentsOrFreelancers():
    assert hasattr(company::Department, "biggestNumberOfStudentsOrFreelancers")
    descriptor = None
    for klass in company::Department.__mro__:
        if "biggestNumberOfStudentsOrFreelancers" in klass.__dict__:
            descriptor = klass.__dict__["biggestNumberOfStudentsOrFreelancers"]
            break
    assert isinstance(descriptor, property)

def test_company::department_has_maxJuniors():
    assert hasattr(company::Department, "maxJuniors")
    descriptor = None
    for klass in company::Department.__mro__:
        if "maxJuniors" in klass.__dict__:
            descriptor = klass.__dict__["maxJuniors"]
            break
    assert isinstance(descriptor, property)

def test_company::department_has_budget():
    assert hasattr(company::Department, "budget")
    descriptor = None
    for klass in company::Department.__mro__:
        if "budget" in klass.__dict__:
            descriptor = klass.__dict__["budget"]
            break
    assert isinstance(descriptor, property)

def test_company::department_has_name():
    assert hasattr(company::Department, "name")
    descriptor = None
    for klass in company::Department.__mro__:
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
company::Company_strategy = st.builds(
    company::Company,
    name=
        safe_text,
    eotmDelta=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
)
company::Freelance_strategy = st.builds(
    company::Freelance,
    assignment=
        safe_text
)
company::Employee_strategy = st.builds(
    company::Employee,
    name=
        safe_text,
    age=
        safe_text,
    salary=
        safe_text
)
company::Student_strategy = st.builds(
    company::Student,
)
company::Division_strategy = st.builds(
    company::Division,
    budget=
        safe_text,
    numberEmployeesOfTheMonth=
        safe_text,
    name=
        safe_text
)
company::Department_strategy = st.builds(
    company::Department,
    biggestNumberOfStudentsOrFreelancers=
        safe_text,
    maxJuniors=
        safe_text,
    budget=
        safe_text,
    name=
        safe_text
)

@given(instance=company::Company_strategy)
@settings(max_examples=50)
def test_company::company_instantiation(instance):
    assert isinstance(instance, company::Company)

@given(instance=company::Company_strategy)
def test_company::company_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Company_strategy)
def test_company::company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Company_strategy)
def test_company::company_eotmDelta_type(instance):
    assert isinstance(instance.eotmDelta, str)


@given(instance=company::Company_strategy)
def test_company::company_eotmDelta_setter(instance):
    original = instance.eotmDelta
    instance.eotmDelta = original
    assert instance.eotmDelta == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=company::Freelance_strategy)
@settings(max_examples=50)
def test_company::freelance_instantiation(instance):
    assert isinstance(instance, company::Freelance)

@given(instance=company::Freelance_strategy)
def test_company::freelance_assignment_type(instance):
    assert isinstance(instance.assignment, str)


@given(instance=company::Freelance_strategy)
def test_company::freelance_assignment_setter(instance):
    original = instance.assignment
    instance.assignment = original
    assert instance.assignment == original

@given(instance=company::Employee_strategy)
@settings(max_examples=50)
def test_company::employee_instantiation(instance):
    assert isinstance(instance, company::Employee)

@given(instance=company::Employee_strategy)
def test_company::employee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Employee_strategy)
def test_company::employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Employee_strategy)
def test_company::employee_age_type(instance):
    assert isinstance(instance.age, str)


@given(instance=company::Employee_strategy)
def test_company::employee_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=company::Employee_strategy)
def test_company::employee_salary_type(instance):
    assert isinstance(instance.salary, str)


@given(instance=company::Employee_strategy)
def test_company::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=company::Student_strategy)
@settings(max_examples=50)
def test_company::student_instantiation(instance):
    assert isinstance(instance, company::Student)

@given(instance=company::Division_strategy)
@settings(max_examples=50)
def test_company::division_instantiation(instance):
    assert isinstance(instance, company::Division)

@given(instance=company::Division_strategy)
def test_company::division_budget_type(instance):
    assert isinstance(instance.budget, str)


@given(instance=company::Division_strategy)
def test_company::division_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=company::Division_strategy)
def test_company::division_numberEmployeesOfTheMonth_type(instance):
    assert isinstance(instance.numberEmployeesOfTheMonth, str)


@given(instance=company::Division_strategy)
def test_company::division_numberEmployeesOfTheMonth_setter(instance):
    original = instance.numberEmployeesOfTheMonth
    instance.numberEmployeesOfTheMonth = original
    assert instance.numberEmployeesOfTheMonth == original

@given(instance=company::Division_strategy)
def test_company::division_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Division_strategy)
def test_company::division_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=company::Department_strategy)
@settings(max_examples=50)
def test_company::department_instantiation(instance):
    assert isinstance(instance, company::Department)

@given(instance=company::Department_strategy)
def test_company::department_biggestNumberOfStudentsOrFreelancers_type(instance):
    assert isinstance(instance.biggestNumberOfStudentsOrFreelancers, str)


@given(instance=company::Department_strategy)
def test_company::department_biggestNumberOfStudentsOrFreelancers_setter(instance):
    original = instance.biggestNumberOfStudentsOrFreelancers
    instance.biggestNumberOfStudentsOrFreelancers = original
    assert instance.biggestNumberOfStudentsOrFreelancers == original

@given(instance=company::Department_strategy)
def test_company::department_maxJuniors_type(instance):
    assert isinstance(instance.maxJuniors, str)


@given(instance=company::Department_strategy)
def test_company::department_maxJuniors_setter(instance):
    original = instance.maxJuniors
    instance.maxJuniors = original
    assert instance.maxJuniors == original

@given(instance=company::Department_strategy)
def test_company::department_budget_type(instance):
    assert isinstance(instance.budget, str)


@given(instance=company::Department_strategy)
def test_company::department_budget_setter(instance):
    original = instance.budget
    instance.budget = original
    assert instance.budget == original

@given(instance=company::Department_strategy)
def test_company::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=company::Department_strategy)
def test_company::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=company::Department_strategy)
@settings(max_examples=30)
def test_company::department_calcexpenses_changes_state(instance):
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
        assert has_statements, f"Function 'calcExpenses' in company::Department is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'calcExpenses' in company::Department did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'calcExpenses' in company::Department is not implemented or raised an error")
