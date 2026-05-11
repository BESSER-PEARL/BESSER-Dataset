import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CarRental::Check,
    CarRental::ServiceDepot,
    CarRental::CarGroup,
    CarRental::Car,
    CarRental::Branch,
    CarRental::Rental,
    CarRental::Person,
    Person,
    CarRental::Employee,
    CarRental::Customer,
    CarGroupKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_carrental::check_is_not_abstract():
    assert not inspect.isabstract(CarRental::Check)


def test_carrental::check_constructor_exists():
    assert callable(CarRental::Check.__init__)


def test_carrental::check_constructor_args():
    sig = inspect.signature(CarRental::Check.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_carrental::check_has_description():
    assert hasattr(CarRental::Check, "description")
    descriptor = None
    for klass in CarRental::Check.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_carrental::servicedepot_is_not_abstract():
    assert not inspect.isabstract(CarRental::ServiceDepot)


def test_carrental::servicedepot_constructor_exists():
    assert callable(CarRental::ServiceDepot.__init__)


def test_carrental::servicedepot_constructor_args():
    sig = inspect.signature(CarRental::ServiceDepot.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_carrental::servicedepot_has_location():
    assert hasattr(CarRental::ServiceDepot, "location")
    descriptor = None
    for klass in CarRental::ServiceDepot.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_carrental::cargroup_is_not_abstract():
    assert not inspect.isabstract(CarRental::CarGroup)


def test_carrental::cargroup_constructor_exists():
    assert callable(CarRental::CarGroup.__init__)


def test_carrental::cargroup_constructor_args():
    sig = inspect.signature(CarRental::CarGroup.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_carrental::cargroup_has_kind():
    assert hasattr(CarRental::CarGroup, "kind")
    descriptor = None
    for klass in CarRental::CarGroup.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_carrental::car_is_not_abstract():
    assert not inspect.isabstract(CarRental::Car)


def test_carrental::car_constructor_exists():
    assert callable(CarRental::Car.__init__)


def test_carrental::car_constructor_args():
    sig = inspect.signature(CarRental::Car.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_carrental::car_has_id():
    assert hasattr(CarRental::Car, "id")
    descriptor = None
    for klass in CarRental::Car.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_carrental::branch_is_not_abstract():
    assert not inspect.isabstract(CarRental::Branch)


def test_carrental::branch_constructor_exists():
    assert callable(CarRental::Branch.__init__)


def test_carrental::branch_constructor_args():
    sig = inspect.signature(CarRental::Branch.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_carrental::branch_has_location():
    assert hasattr(CarRental::Branch, "location")
    descriptor = None
    for klass in CarRental::Branch.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_carrental::rental_is_not_abstract():
    assert not inspect.isabstract(CarRental::Rental)


def test_carrental::rental_constructor_exists():
    assert callable(CarRental::Rental.__init__)


def test_carrental::rental_constructor_args():
    sig = inspect.signature(CarRental::Rental.__init__)
    params = list(sig.parameters.keys())
    assert "untilDate" in params, "Missing parameter 'untilDate'"
    assert "framDate" in params, "Missing parameter 'framDate'"

def test_carrental::rental_has_untilDate():
    assert hasattr(CarRental::Rental, "untilDate")
    descriptor = None
    for klass in CarRental::Rental.__mro__:
        if "untilDate" in klass.__dict__:
            descriptor = klass.__dict__["untilDate"]
            break
    assert isinstance(descriptor, property)

def test_carrental::rental_has_framDate():
    assert hasattr(CarRental::Rental, "framDate")
    descriptor = None
    for klass in CarRental::Rental.__mro__:
        if "framDate" in klass.__dict__:
            descriptor = klass.__dict__["framDate"]
            break
    assert isinstance(descriptor, property)



def test_carrental::person_is_not_abstract():
    assert not inspect.isabstract(CarRental::Person)


def test_carrental::person_constructor_exists():
    assert callable(CarRental::Person.__init__)


def test_carrental::person_constructor_args():
    sig = inspect.signature(CarRental::Person.__init__)
    params = list(sig.parameters.keys())
    assert "isMarried" in params, "Missing parameter 'isMarried'"
    assert "age" in params, "Missing parameter 'age'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_carrental::person_has_isMarried():
    assert hasattr(CarRental::Person, "isMarried")
    descriptor = None
    for klass in CarRental::Person.__mro__:
        if "isMarried" in klass.__dict__:
            descriptor = klass.__dict__["isMarried"]
            break
    assert isinstance(descriptor, property)

def test_carrental::person_has_age():
    assert hasattr(CarRental::Person, "age")
    descriptor = None
    for klass in CarRental::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_carrental::person_has_firstname():
    assert hasattr(CarRental::Person, "firstname")
    descriptor = None
    for klass in CarRental::Person.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_carrental::person_has_lastname():
    assert hasattr(CarRental::Person, "lastname")
    descriptor = None
    for klass in CarRental::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_carrental::employee_is_not_abstract():
    assert not inspect.isabstract(CarRental::Employee)


def test_carrental::employee_constructor_exists():
    assert callable(CarRental::Employee.__init__)


def test_carrental::employee_constructor_args():
    sig = inspect.signature(CarRental::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"

def test_carrental::employee_has_salary():
    assert hasattr(CarRental::Employee, "salary")
    descriptor = None
    for klass in CarRental::Employee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_carrental::customer_is_not_abstract():
    assert not inspect.isabstract(CarRental::Customer)


def test_carrental::customer_constructor_exists():
    assert callable(CarRental::Customer.__init__)


def test_carrental::customer_constructor_args():
    sig = inspect.signature(CarRental::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_carrental::customer_has_address():
    assert hasattr(CarRental::Customer, "address")
    descriptor = None
    for klass in CarRental::Customer.__mro__:
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
        "intermediate",
        "luxury",
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
CarRental::Check_strategy = st.builds(
    CarRental::Check,
    description=
        safe_text
)
CarRental::ServiceDepot_strategy = st.builds(
    CarRental::ServiceDepot,
    location=
        safe_text
)
CarRental::CarGroup_strategy = st.builds(
    CarRental::CarGroup,
    kind=
        safe_text
)
CarRental::Car_strategy = st.builds(
    CarRental::Car,
    id=
        safe_text
)
CarRental::Branch_strategy = st.builds(
    CarRental::Branch,
    location=
        safe_text
)
CarRental::Rental_strategy = st.builds(
    CarRental::Rental,
    untilDate=
        safe_text,
    framDate=
        safe_text
)
CarRental::Person_strategy = st.builds(
    CarRental::Person,
    isMarried=
        st.booleans(),
    age=
        st.integers(),
    firstname=
        safe_text,
    lastname=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
CarRental::Employee_strategy = st.builds(
    CarRental::Employee,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CarRental::Customer_strategy = st.builds(
    CarRental::Customer,
    address=
        safe_text
)

@given(instance=CarRental::Check_strategy)
@settings(max_examples=50)
def test_carrental::check_instantiation(instance):
    assert isinstance(instance, CarRental::Check)

@given(instance=CarRental::Check_strategy)
def test_carrental::check_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=CarRental::Check_strategy)
def test_carrental::check_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=CarRental::ServiceDepot_strategy)
@settings(max_examples=50)
def test_carrental::servicedepot_instantiation(instance):
    assert isinstance(instance, CarRental::ServiceDepot)

@given(instance=CarRental::ServiceDepot_strategy)
def test_carrental::servicedepot_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=CarRental::ServiceDepot_strategy)
def test_carrental::servicedepot_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=CarRental::CarGroup_strategy)
@settings(max_examples=50)
def test_carrental::cargroup_instantiation(instance):
    assert isinstance(instance, CarRental::CarGroup)

@given(instance=CarRental::CarGroup_strategy)
def test_carrental::cargroup_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=CarRental::CarGroup_strategy)
def test_carrental::cargroup_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CarRental::Car_strategy)
@settings(max_examples=50)
def test_carrental::car_instantiation(instance):
    assert isinstance(instance, CarRental::Car)

@given(instance=CarRental::Car_strategy)
def test_carrental::car_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=CarRental::Car_strategy)
def test_carrental::car_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=CarRental::Branch_strategy)
@settings(max_examples=50)
def test_carrental::branch_instantiation(instance):
    assert isinstance(instance, CarRental::Branch)

@given(instance=CarRental::Branch_strategy)
def test_carrental::branch_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=CarRental::Branch_strategy)
def test_carrental::branch_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=CarRental::Rental_strategy)
@settings(max_examples=50)
def test_carrental::rental_instantiation(instance):
    assert isinstance(instance, CarRental::Rental)

@given(instance=CarRental::Rental_strategy)
def test_carrental::rental_untilDate_type(instance):
    assert isinstance(instance.untilDate, str)


@given(instance=CarRental::Rental_strategy)
def test_carrental::rental_untilDate_setter(instance):
    original = instance.untilDate
    instance.untilDate = original
    assert instance.untilDate == original

@given(instance=CarRental::Rental_strategy)
def test_carrental::rental_framDate_type(instance):
    assert isinstance(instance.framDate, str)


@given(instance=CarRental::Rental_strategy)
def test_carrental::rental_framDate_setter(instance):
    original = instance.framDate
    instance.framDate = original
    assert instance.framDate == original

@given(instance=CarRental::Person_strategy)
@settings(max_examples=50)
def test_carrental::person_instantiation(instance):
    assert isinstance(instance, CarRental::Person)

@given(instance=CarRental::Person_strategy)
def test_carrental::person_isMarried_type(instance):
    assert isinstance(instance.isMarried, bool)


@given(instance=CarRental::Person_strategy)
def test_carrental::person_isMarried_setter(instance):
    original = instance.isMarried
    instance.isMarried = original
    assert instance.isMarried == original

@given(instance=CarRental::Person_strategy)
def test_carrental::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=CarRental::Person_strategy)
def test_carrental::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=CarRental::Person_strategy)
def test_carrental::person_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=CarRental::Person_strategy)
def test_carrental::person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=CarRental::Person_strategy)
def test_carrental::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=CarRental::Person_strategy)
def test_carrental::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=CarRental::Person_strategy)
@settings(max_examples=30)
def test_carrental::person_email_changes_state(instance):
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
        assert has_statements, f"Function 'email' in CarRental::Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'email' in CarRental::Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'email' in CarRental::Person is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=CarRental::Person_strategy)
@settings(max_examples=30)
def test_carrental::person_updateage_changes_state(instance):
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
        assert has_statements, f"Function 'updateAge' in CarRental::Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateAge' in CarRental::Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateAge' in CarRental::Person is not implemented or raised an error")

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=CarRental::Employee_strategy)
@settings(max_examples=50)
def test_carrental::employee_instantiation(instance):
    assert isinstance(instance, CarRental::Employee)

@given(instance=CarRental::Employee_strategy)
def test_carrental::employee_salary_type(instance):
    assert isinstance(instance.salary, float)


@given(instance=CarRental::Employee_strategy)
def test_carrental::employee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=CarRental::Employee_strategy)
@settings(max_examples=30)
def test_carrental::employee_raisesalary_changes_state(instance):
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
        assert has_statements, f"Function 'raiseSalary' in CarRental::Employee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'raiseSalary' in CarRental::Employee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'raiseSalary' in CarRental::Employee is not implemented or raised an error")

@given(instance=CarRental::Customer_strategy)
@settings(max_examples=50)
def test_carrental::customer_instantiation(instance):
    assert isinstance(instance, CarRental::Customer)

@given(instance=CarRental::Customer_strategy)
def test_carrental::customer_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=CarRental::Customer_strategy)
def test_carrental::customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
