import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CarRental_Check,
    CarRental_ServiceDepot,
    CarRental_CarGroup,
    CarRental_Car,
    CarRental_Branch,
    CarRental_Rental,
    CarRental_Person,
    Person,
    CarRental_Employee,
    CarRental_Customer,
    CarGroupKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_carrental_check_is_not_abstract():
    assert not inspect.isabstract(CarRental_Check)


def test_carrental_check_constructor_exists():
    assert callable(CarRental_Check.__init__)


def test_carrental_check_constructor_args():
    sig = inspect.signature(CarRental_Check.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_carrental_check_has_description():
    assert hasattr(CarRental_Check, "description")
    descriptor = None
    for klass in CarRental_Check.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_carrental_servicedepot_is_not_abstract():
    assert not inspect.isabstract(CarRental_ServiceDepot)


def test_carrental_servicedepot_constructor_exists():
    assert callable(CarRental_ServiceDepot.__init__)


def test_carrental_servicedepot_constructor_args():
    sig = inspect.signature(CarRental_ServiceDepot.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_carrental_servicedepot_has_location():
    assert hasattr(CarRental_ServiceDepot, "location")
    descriptor = None
    for klass in CarRental_ServiceDepot.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_carrental_cargroup_is_not_abstract():
    assert not inspect.isabstract(CarRental_CarGroup)


def test_carrental_cargroup_constructor_exists():
    assert callable(CarRental_CarGroup.__init__)


def test_carrental_cargroup_constructor_args():
    sig = inspect.signature(CarRental_CarGroup.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_carrental_cargroup_has_kind():
    assert hasattr(CarRental_CarGroup, "kind")
    descriptor = None
    for klass in CarRental_CarGroup.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_carrental_car_is_not_abstract():
    assert not inspect.isabstract(CarRental_Car)


def test_carrental_car_constructor_exists():
    assert callable(CarRental_Car.__init__)


def test_carrental_car_constructor_args():
    sig = inspect.signature(CarRental_Car.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_carrental_car_has_id():
    assert hasattr(CarRental_Car, "id")
    descriptor = None
    for klass in CarRental_Car.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_carrental_branch_is_not_abstract():
    assert not inspect.isabstract(CarRental_Branch)


def test_carrental_branch_constructor_exists():
    assert callable(CarRental_Branch.__init__)


def test_carrental_branch_constructor_args():
    sig = inspect.signature(CarRental_Branch.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_carrental_branch_has_location():
    assert hasattr(CarRental_Branch, "location")
    descriptor = None
    for klass in CarRental_Branch.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_carrental_rental_is_not_abstract():
    assert not inspect.isabstract(CarRental_Rental)


def test_carrental_rental_constructor_exists():
    assert callable(CarRental_Rental.__init__)


def test_carrental_rental_constructor_args():
    sig = inspect.signature(CarRental_Rental.__init__)
    params = list(sig.parameters.keys())
    assert "untilDate" in params, "Missing parameter 'untilDate'"
    assert "framDate" in params, "Missing parameter 'framDate'"

def test_carrental_rental_has_untilDate():
    assert hasattr(CarRental_Rental, "untilDate")
    descriptor = None
    for klass in CarRental_Rental.__mro__:
        if "untilDate" in klass.__dict__:
            descriptor = klass.__dict__["untilDate"]
            break
    assert isinstance(descriptor, property)

def test_carrental_rental_has_framDate():
    assert hasattr(CarRental_Rental, "framDate")
    descriptor = None
    for klass in CarRental_Rental.__mro__:
        if "framDate" in klass.__dict__:
            descriptor = klass.__dict__["framDate"]
            break
    assert isinstance(descriptor, property)



def test_carrental_person_is_not_abstract():
    assert not inspect.isabstract(CarRental_Person)


def test_carrental_person_constructor_exists():
    assert callable(CarRental_Person.__init__)


def test_carrental_person_constructor_args():
    sig = inspect.signature(CarRental_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "isMarried" in params, "Missing parameter 'isMarried'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "age" in params, "Missing parameter 'age'"

def test_carrental_person_has_firstname():
    assert hasattr(CarRental_Person, "firstname")
    descriptor = None
    for klass in CarRental_Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_carrental_person_has_isMarried():
    assert hasattr(CarRental_Person, "isMarried")
    descriptor = None
    for klass in CarRental_Person.__mro__:
        if "isMarried" in klass.__dict__:
            descriptor = klass.__dict__["isMarried"]
            break
    assert isinstance(descriptor, property)

def test_carrental_person_has_lastname():
    assert hasattr(CarRental_Person, "lastname")
    descriptor = None
    for klass in CarRental_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_carrental_person_has_age():
    assert hasattr(CarRental_Person, "age")
    descriptor = None
    for klass in CarRental_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_carrental_employee_is_not_abstract():
    assert not inspect.isabstract(CarRental_Employee)


def test_carrental_employee_constructor_exists():
    assert callable(CarRental_Employee.__init__)


def test_carrental_employee_constructor_args():
    sig = inspect.signature(CarRental_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"

def test_carrental_employee_has_salary():
    assert hasattr(CarRental_Employee, "salary")
    descriptor = None
    for klass in CarRental_Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_carrental_customer_is_not_abstract():
    assert not inspect.isabstract(CarRental_Customer)


def test_carrental_customer_constructor_exists():
    assert callable(CarRental_Customer.__init__)


def test_carrental_customer_constructor_args():
    sig = inspect.signature(CarRental_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_carrental_customer_has_address():
    assert hasattr(CarRental_Customer, "address")
    descriptor = None
    for klass in CarRental_Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_cargroupkind_exists():
    # Check that the Enumeration exists
    assert CarGroupKind is not None

def test_cargroupkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CarGroupKind]
    expected_literals = [
        "compact",
        "luxury",
        "intermediate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CarGroupKind"


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
CarRental_Check_strategy = st.builds(
    CarRental_Check,
    description=
        safe_text
)
CarRental_ServiceDepot_strategy = st.builds(
    CarRental_ServiceDepot,
    location=
        safe_text
)
CarRental_CarGroup_strategy = st.builds(
    CarRental_CarGroup,
    kind=
        safe_text
)
CarRental_Car_strategy = st.builds(
    CarRental_Car,
    id=
        safe_text
)
CarRental_Branch_strategy = st.builds(
    CarRental_Branch,
    location=
        safe_text
)
CarRental_Rental_strategy = st.builds(
    CarRental_Rental,
    untilDate=
        safe_text,
    framDate=
        safe_text
)
CarRental_Person_strategy = st.builds(
    CarRental_Person,
    firstname=
        safe_text,
    isMarried=
        st.booleans(),
    lastname=
        safe_text,
    age=
        st.integers()
)
Person_strategy = st.builds(
    Person,
)
CarRental_Employee_strategy = st.builds(
    CarRental_Employee,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CarRental_Customer_strategy = st.builds(
    CarRental_Customer,
    address=
        safe_text
)

@given(instance=CarRental_Check_strategy)
@settings(max_examples=50)
def test_carrental_check_instantiation(instance):
    assert isinstance(instance, CarRental_Check)



@given(instance=CarRental_Check_strategy)
def test_carrental_check_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=CarRental_ServiceDepot_strategy)
@settings(max_examples=50)
def test_carrental_servicedepot_instantiation(instance):
    assert isinstance(instance, CarRental_ServiceDepot)



@given(instance=CarRental_ServiceDepot_strategy)
def test_carrental_servicedepot_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=CarRental_CarGroup_strategy)
@settings(max_examples=50)
def test_carrental_cargroup_instantiation(instance):
    assert isinstance(instance, CarRental_CarGroup)



@given(instance=CarRental_CarGroup_strategy)
def test_carrental_cargroup_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CarRental_Car_strategy)
@settings(max_examples=50)
def test_carrental_car_instantiation(instance):
    assert isinstance(instance, CarRental_Car)



@given(instance=CarRental_Car_strategy)
def test_carrental_car_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=CarRental_Branch_strategy)
@settings(max_examples=50)
def test_carrental_branch_instantiation(instance):
    assert isinstance(instance, CarRental_Branch)



@given(instance=CarRental_Branch_strategy)
def test_carrental_branch_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=CarRental_Rental_strategy)
@settings(max_examples=50)
def test_carrental_rental_instantiation(instance):
    assert isinstance(instance, CarRental_Rental)



@given(instance=CarRental_Rental_strategy)
def test_carrental_rental_untilDate_setter(instance):
    original = instance.untilDate
    instance.untilDate = original
    assert instance.untilDate == original



@given(instance=CarRental_Rental_strategy)
def test_carrental_rental_framDate_setter(instance):
    original = instance.framDate
    instance.framDate = original
    assert instance.framDate == original

@given(instance=CarRental_Person_strategy)
@settings(max_examples=50)
def test_carrental_person_instantiation(instance):
    assert isinstance(instance, CarRental_Person)



@given(instance=CarRental_Person_strategy)
def test_carrental_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=CarRental_Person_strategy)
def test_carrental_person_isMarried_setter(instance):
    original = instance.isMarried
    instance.isMarried = original
    assert instance.isMarried == original



@given(instance=CarRental_Person_strategy)
def test_carrental_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=CarRental_Person_strategy)
def test_carrental_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=CarRental_Person_strategy)
@settings(max_examples=30)
def test_carrental_person_updateage_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateAge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateAge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateAge' in CarRental_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateAge' in CarRental_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateAge' in CarRental_Person is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=CarRental_Person_strategy)
@settings(max_examples=30)
def test_carrental_person_email_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.email()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.email).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'email' in CarRental_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'email' in CarRental_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'email' in CarRental_Person is not implemented or raised an error")

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=CarRental_Employee_strategy)
@settings(max_examples=50)
def test_carrental_employee_instantiation(instance):
    assert isinstance(instance, CarRental_Employee)



@given(instance=CarRental_Employee_strategy)
def test_carrental_employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=CarRental_Employee_strategy)
@settings(max_examples=30)
def test_carrental_employee_raisesalary_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.raiseSalary(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.raiseSalary).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'raiseSalary' in CarRental_Employee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'raiseSalary' in CarRental_Employee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'raiseSalary' in CarRental_Employee is not implemented or raised an error")

@given(instance=CarRental_Customer_strategy)
@settings(max_examples=50)
def test_carrental_customer_instantiation(instance):
    assert isinstance(instance, CarRental_Customer)



@given(instance=CarRental_Customer_strategy)
def test_carrental_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
