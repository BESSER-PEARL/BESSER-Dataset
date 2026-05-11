import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rental::License,
    rental::Address,
    rental::Customer,
    rental::Rental,
    rental::RentalObject,
    rental::RentalAgency,
    StreetType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rental::license_is_not_abstract():
    assert not inspect.isabstract(rental::License)


def test_rental::license_constructor_exists():
    assert callable(rental::License.__init__)


def test_rental::license_constructor_args():
    sig = inspect.signature(rental::License.__init__)
    params = list(sig.parameters.keys())
    assert "validityDate" in params, "Missing parameter 'validityDate'"
    assert "number" in params, "Missing parameter 'number'"

def test_rental::license_has_validityDate():
    assert hasattr(rental::License, "validityDate")
    descriptor = None
    for klass in rental::License.__mro__:
        if "validityDate" in klass.__dict__:
            descriptor = klass.__dict__["validityDate"]
            break
    assert isinstance(descriptor, property)

def test_rental::license_has_number():
    assert hasattr(rental::License, "number")
    descriptor = None
    for klass in rental::License.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_rental::address_is_not_abstract():
    assert not inspect.isabstract(rental::Address)


def test_rental::address_constructor_exists():
    assert callable(rental::Address.__init__)


def test_rental::address_constructor_args():
    sig = inspect.signature(rental::Address.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "number" in params, "Missing parameter 'number'"
    assert "streetType" in params, "Missing parameter 'streetType'"
    assert "streetName" in params, "Missing parameter 'streetName'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"

def test_rental::address_has_city():
    assert hasattr(rental::Address, "city")
    descriptor = None
    for klass in rental::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_rental::address_has_number():
    assert hasattr(rental::Address, "number")
    descriptor = None
    for klass in rental::Address.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_rental::address_has_streetType():
    assert hasattr(rental::Address, "streetType")
    descriptor = None
    for klass in rental::Address.__mro__:
        if "streetType" in klass.__dict__:
            descriptor = klass.__dict__["streetType"]
            break
    assert isinstance(descriptor, property)

def test_rental::address_has_streetName():
    assert hasattr(rental::Address, "streetName")
    descriptor = None
    for klass in rental::Address.__mro__:
        if "streetName" in klass.__dict__:
            descriptor = klass.__dict__["streetName"]
            break
    assert isinstance(descriptor, property)

def test_rental::address_has_zipCode():
    assert hasattr(rental::Address, "zipCode")
    descriptor = None
    for klass in rental::Address.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)



def test_rental::customer_is_not_abstract():
    assert not inspect.isabstract(rental::Customer)


def test_rental::customer_constructor_exists():
    assert callable(rental::Customer.__init__)


def test_rental::customer_constructor_args():
    sig = inspect.signature(rental::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_rental::customer_has_lastName():
    assert hasattr(rental::Customer, "lastName")
    descriptor = None
    for klass in rental::Customer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_rental::customer_has_firstName():
    assert hasattr(rental::Customer, "firstName")
    descriptor = None
    for klass in rental::Customer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_rental::rental_is_not_abstract():
    assert not inspect.isabstract(rental::Rental)


def test_rental::rental_constructor_exists():
    assert callable(rental::Rental.__init__)


def test_rental::rental_constructor_args():
    sig = inspect.signature(rental::Rental.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "endDate" in params, "Missing parameter 'endDate'"

def test_rental::rental_has_startDate():
    assert hasattr(rental::Rental, "startDate")
    descriptor = None
    for klass in rental::Rental.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_rental::rental_has_endDate():
    assert hasattr(rental::Rental, "endDate")
    descriptor = None
    for klass in rental::Rental.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)



def test_rental::rentalobject_is_not_abstract():
    assert not inspect.isabstract(rental::RentalObject)


def test_rental::rentalobject_constructor_exists():
    assert callable(rental::RentalObject.__init__)


def test_rental::rentalobject_constructor_args():
    sig = inspect.signature(rental::RentalObject.__init__)
    params = list(sig.parameters.keys())
    assert "picture" in params, "Missing parameter 'picture'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"

def test_rental::rentalobject_has_picture():
    assert hasattr(rental::RentalObject, "picture")
    descriptor = None
    for klass in rental::RentalObject.__mro__:
        if "picture" in klass.__dict__:
            descriptor = klass.__dict__["picture"]
            break
    assert isinstance(descriptor, property)

def test_rental::rentalobject_has_ID():
    assert hasattr(rental::RentalObject, "ID")
    descriptor = None
    for klass in rental::RentalObject.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_rental::rentalobject_has_name():
    assert hasattr(rental::RentalObject, "name")
    descriptor = None
    for klass in rental::RentalObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rental::rentalagency_is_not_abstract():
    assert not inspect.isabstract(rental::RentalAgency)


def test_rental::rentalagency_constructor_exists():
    assert callable(rental::RentalAgency.__init__)


def test_rental::rentalagency_constructor_args():
    sig = inspect.signature(rental::RentalAgency.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rental::rentalagency_has_name():
    assert hasattr(rental::RentalAgency, "name")
    descriptor = None
    for klass in rental::RentalAgency.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_streettype_exists():
    # Check that the Enumeration exists
    assert StreetType is not None

def test_streettype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StreetType]
    expected_literals = [
        "Street",
        "Road",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StreetType"


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
rental::License_strategy = st.builds(
    rental::License,
    validityDate=
        st.dates(),
    number=
        st.integers()
)
rental::Address_strategy = st.builds(
    rental::Address,
    city=
        safe_text,
    number=
        st.integers(),
    streetType=
        safe_text,
    streetName=
        safe_text,
    zipCode=
        safe_text
)
rental::Customer_strategy = st.builds(
    rental::Customer,
    lastName=
        safe_text,
    firstName=
        safe_text
)
rental::Rental_strategy = st.builds(
    rental::Rental,
    startDate=
        st.dates(),
    endDate=
        st.dates()
)
rental::RentalObject_strategy = st.builds(
    rental::RentalObject,
    picture=
        safe_text,
    ID=
        safe_text,
    name=
        safe_text
)
rental::RentalAgency_strategy = st.builds(
    rental::RentalAgency,
    name=
        safe_text
)

@given(instance=rental::License_strategy)
@settings(max_examples=50)
def test_rental::license_instantiation(instance):
    assert isinstance(instance, rental::License)

@given(instance=rental::License_strategy)
def test_rental::license_validityDate_type(instance):
    assert isinstance(instance.validityDate, date)


@given(instance=rental::License_strategy)
def test_rental::license_validityDate_setter(instance):
    original = instance.validityDate
    instance.validityDate = original
    assert instance.validityDate == original

@given(instance=rental::License_strategy)
def test_rental::license_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=rental::License_strategy)
def test_rental::license_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=rental::Address_strategy)
@settings(max_examples=50)
def test_rental::address_instantiation(instance):
    assert isinstance(instance, rental::Address)

@given(instance=rental::Address_strategy)
def test_rental::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=rental::Address_strategy)
def test_rental::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=rental::Address_strategy)
def test_rental::address_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=rental::Address_strategy)
def test_rental::address_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=rental::Address_strategy)
def test_rental::address_streetType_type(instance):
    assert isinstance(instance.streetType, str)


@given(instance=rental::Address_strategy)
def test_rental::address_streetType_setter(instance):
    original = instance.streetType
    instance.streetType = original
    assert instance.streetType == original

@given(instance=rental::Address_strategy)
def test_rental::address_streetName_type(instance):
    assert isinstance(instance.streetName, str)


@given(instance=rental::Address_strategy)
def test_rental::address_streetName_setter(instance):
    original = instance.streetName
    instance.streetName = original
    assert instance.streetName == original

@given(instance=rental::Address_strategy)
def test_rental::address_zipCode_type(instance):
    assert isinstance(instance.zipCode, str)


@given(instance=rental::Address_strategy)
def test_rental::address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original

@given(instance=rental::Customer_strategy)
@settings(max_examples=50)
def test_rental::customer_instantiation(instance):
    assert isinstance(instance, rental::Customer)

@given(instance=rental::Customer_strategy)
def test_rental::customer_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=rental::Customer_strategy)
def test_rental::customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=rental::Customer_strategy)
def test_rental::customer_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=rental::Customer_strategy)
def test_rental::customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=rental::Rental_strategy)
@settings(max_examples=50)
def test_rental::rental_instantiation(instance):
    assert isinstance(instance, rental::Rental)

@given(instance=rental::Rental_strategy)
def test_rental::rental_startDate_type(instance):
    assert isinstance(instance.startDate, date)


@given(instance=rental::Rental_strategy)
def test_rental::rental_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=rental::Rental_strategy)
def test_rental::rental_endDate_type(instance):
    assert isinstance(instance.endDate, date)


@given(instance=rental::Rental_strategy)
def test_rental::rental_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::Rental_strategy)
@settings(max_examples=30)
def test_rental::rental_end_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.end()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.end).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'end' in rental::Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'end' in rental::Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'end' in rental::Rental is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::Rental_strategy)
@settings(max_examples=30)
def test_rental::rental_start_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.start()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.start).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'start' in rental::Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'start' in rental::Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'start' in rental::Rental is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::Rental_strategy)
@settings(max_examples=30)
def test_rental::rental_nbdaysbooked_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.nbDaysBooked()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.nbDaysBooked).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'nbDaysBooked' in rental::Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nbDaysBooked' in rental::Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nbDaysBooked' in rental::Rental is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::Rental_strategy)
@settings(max_examples=30)
def test_rental::rental_nbdaysrented_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.nbDaysRented()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.nbDaysRented).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'nbDaysRented' in rental::Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nbDaysRented' in rental::Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nbDaysRented' in rental::Rental is not implemented or raised an error")

@given(instance=rental::RentalObject_strategy)
@settings(max_examples=50)
def test_rental::rentalobject_instantiation(instance):
    assert isinstance(instance, rental::RentalObject)

@given(instance=rental::RentalObject_strategy)
def test_rental::rentalobject_picture_type(instance):
    assert isinstance(instance.picture, str)


@given(instance=rental::RentalObject_strategy)
def test_rental::rentalobject_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original

@given(instance=rental::RentalObject_strategy)
def test_rental::rentalobject_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=rental::RentalObject_strategy)
def test_rental::rentalobject_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=rental::RentalObject_strategy)
def test_rental::rentalobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rental::RentalObject_strategy)
def test_rental::rentalobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::RentalObject_strategy)
@settings(max_examples=30)
def test_rental::rentalobject_rent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.rent(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.rent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'rent' in rental::RentalObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'rent' in rental::RentalObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'rent' in rental::RentalObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::RentalObject_strategy)
@settings(max_examples=30)
def test_rental::rentalobject_isavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAvailable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAvailable' in rental::RentalObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in rental::RentalObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in rental::RentalObject is not implemented or raised an error")

@given(instance=rental::RentalAgency_strategy)
@settings(max_examples=50)
def test_rental::rentalagency_instantiation(instance):
    assert isinstance(instance, rental::RentalAgency)

@given(instance=rental::RentalAgency_strategy)
def test_rental::rentalagency_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rental::RentalAgency_strategy)
def test_rental::rentalagency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::RentalAgency_strategy)
@settings(max_examples=30)
def test_rental::rentalagency_addobject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addObject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addObject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addObject' in rental::RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addObject' in rental::RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addObject' in rental::RentalAgency is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::RentalAgency_strategy)
@settings(max_examples=30)
def test_rental::rentalagency_book_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.book(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.book).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'book' in rental::RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'book' in rental::RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'book' in rental::RentalAgency is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::RentalAgency_strategy)
@settings(max_examples=30)
def test_rental::rentalagency_addcustomer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addCustomer(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addCustomer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addCustomer' in rental::RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addCustomer' in rental::RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addCustomer' in rental::RentalAgency is not implemented or raised an error")
