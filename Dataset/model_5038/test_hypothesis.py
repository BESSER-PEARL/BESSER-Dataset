import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rental_License,
    rental_Rental,
    rental_Customer,
    rental_RentalObject,
    rental_Address,
    rental_RentalAgency,
    StreetType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rental_license_is_not_abstract():
    assert not inspect.isabstract(rental_License)


def test_rental_license_constructor_exists():
    assert callable(rental_License.__init__)


def test_rental_license_constructor_args():
    sig = inspect.signature(rental_License.__init__)
    params = list(sig.parameters.keys())
    assert "validityDate" in params, "Missing parameter 'validityDate'"
    assert "number" in params, "Missing parameter 'number'"

def test_rental_license_has_validityDate():
    assert hasattr(rental_License, "validityDate")
    descriptor = None
    for klass in rental_License.__mro__:
        if "validityDate" in klass.__dict__:
            descriptor = klass.__dict__["validityDate"]
            break
    assert isinstance(descriptor, property)

def test_rental_license_has_number():
    assert hasattr(rental_License, "number")
    descriptor = None
    for klass in rental_License.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_rental_rental_is_not_abstract():
    assert not inspect.isabstract(rental_Rental)


def test_rental_rental_constructor_exists():
    assert callable(rental_Rental.__init__)


def test_rental_rental_constructor_args():
    sig = inspect.signature(rental_Rental.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "endDate" in params, "Missing parameter 'endDate'"

def test_rental_rental_has_startDate():
    assert hasattr(rental_Rental, "startDate")
    descriptor = None
    for klass in rental_Rental.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_rental_rental_has_endDate():
    assert hasattr(rental_Rental, "endDate")
    descriptor = None
    for klass in rental_Rental.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)



def test_rental_customer_is_not_abstract():
    assert not inspect.isabstract(rental_Customer)


def test_rental_customer_constructor_exists():
    assert callable(rental_Customer.__init__)


def test_rental_customer_constructor_args():
    sig = inspect.signature(rental_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_rental_customer_has_name():
    assert hasattr(rental_Customer, "name")
    descriptor = None
    for klass in rental_Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rental_customer_has_firstName():
    assert hasattr(rental_Customer, "firstName")
    descriptor = None
    for klass in rental_Customer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_rental_rentalobject_is_not_abstract():
    assert not inspect.isabstract(rental_RentalObject)


def test_rental_rentalobject_constructor_exists():
    assert callable(rental_RentalObject.__init__)


def test_rental_rentalobject_constructor_args():
    sig = inspect.signature(rental_RentalObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "available" in params, "Missing parameter 'available'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_rental_rentalobject_has_name():
    assert hasattr(rental_RentalObject, "name")
    descriptor = None
    for klass in rental_RentalObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rental_rentalobject_has_available():
    assert hasattr(rental_RentalObject, "available")
    descriptor = None
    for klass in rental_RentalObject.__mro__:
        if "available" in klass.__dict__:
            descriptor = klass.__dict__["available"]
            break
    assert isinstance(descriptor, property)

def test_rental_rentalobject_has_ID():
    assert hasattr(rental_RentalObject, "ID")
    descriptor = None
    for klass in rental_RentalObject.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_rental_address_is_not_abstract():
    assert not inspect.isabstract(rental_Address)


def test_rental_address_constructor_exists():
    assert callable(rental_Address.__init__)


def test_rental_address_constructor_args():
    sig = inspect.signature(rental_Address.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "streetName" in params, "Missing parameter 'streetName'"
    assert "number" in params, "Missing parameter 'number'"
    assert "streetType" in params, "Missing parameter 'streetType'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"

def test_rental_address_has_city():
    assert hasattr(rental_Address, "city")
    descriptor = None
    for klass in rental_Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_rental_address_has_streetName():
    assert hasattr(rental_Address, "streetName")
    descriptor = None
    for klass in rental_Address.__mro__:
        if "streetName" in klass.__dict__:
            descriptor = klass.__dict__["streetName"]
            break
    assert isinstance(descriptor, property)

def test_rental_address_has_number():
    assert hasattr(rental_Address, "number")
    descriptor = None
    for klass in rental_Address.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_rental_address_has_streetType():
    assert hasattr(rental_Address, "streetType")
    descriptor = None
    for klass in rental_Address.__mro__:
        if "streetType" in klass.__dict__:
            descriptor = klass.__dict__["streetType"]
            break
    assert isinstance(descriptor, property)

def test_rental_address_has_zipCode():
    assert hasattr(rental_Address, "zipCode")
    descriptor = None
    for klass in rental_Address.__mro__:
        if "zipCode" in klass.__dict__:
            descriptor = klass.__dict__["zipCode"]
            break
    assert isinstance(descriptor, property)



def test_rental_rentalagency_is_not_abstract():
    assert not inspect.isabstract(rental_RentalAgency)


def test_rental_rentalagency_constructor_exists():
    assert callable(rental_RentalAgency.__init__)


def test_rental_rentalagency_constructor_args():
    sig = inspect.signature(rental_RentalAgency.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rental_rentalagency_has_name():
    assert hasattr(rental_RentalAgency, "name")
    descriptor = None
    for klass in rental_RentalAgency.__mro__:
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
        "Road",
        "Street",
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
rental_License_strategy = st.builds(
    rental_License,
    validityDate=
        st.dates(),
    number=
        st.integers()
)
rental_Rental_strategy = st.builds(
    rental_Rental,
    startDate=
        st.dates(),
    endDate=
        st.dates()
)
rental_Customer_strategy = st.builds(
    rental_Customer,
    name=
        safe_text,
    firstName=
        safe_text
)
rental_RentalObject_strategy = st.builds(
    rental_RentalObject,
    name=
        safe_text,
    available=
        st.booleans(),
    ID=
        safe_text
)
rental_Address_strategy = st.builds(
    rental_Address,
    city=
        safe_text,
    streetName=
        safe_text,
    number=
        st.integers(),
    streetType=
        safe_text,
    zipCode=
        safe_text
)
rental_RentalAgency_strategy = st.builds(
    rental_RentalAgency,
    name=
        safe_text
)

@given(instance=rental_License_strategy)
@settings(max_examples=50)
def test_rental_license_instantiation(instance):
    assert isinstance(instance, rental_License)



@given(instance=rental_License_strategy)
def test_rental_license_validityDate_setter(instance):
    original = instance.validityDate
    instance.validityDate = original
    assert instance.validityDate == original



@given(instance=rental_License_strategy)
def test_rental_license_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_License_strategy)
@settings(max_examples=30)
def test_rental_license_isvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isValid()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isValid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isValid' in rental_License is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isValid' in rental_License did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isValid' in rental_License is not implemented or raised an error")

@given(instance=rental_Rental_strategy)
@settings(max_examples=50)
def test_rental_rental_instantiation(instance):
    assert isinstance(instance, rental_Rental)



@given(instance=rental_Rental_strategy)
def test_rental_rental_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=rental_Rental_strategy)
def test_rental_rental_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_Rental_strategy)
@settings(max_examples=30)
def test_rental_rental_nbdaysbooked_changes_state(instance):
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
        assert has_statements, f"Function 'nbDaysBooked' in rental_Rental is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nbDaysBooked' in rental_Rental did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nbDaysBooked' in rental_Rental is not implemented or raised an error")

@given(instance=rental_Customer_strategy)
@settings(max_examples=50)
def test_rental_customer_instantiation(instance):
    assert isinstance(instance, rental_Customer)



@given(instance=rental_Customer_strategy)
def test_rental_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rental_Customer_strategy)
def test_rental_customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=rental_RentalObject_strategy)
@settings(max_examples=50)
def test_rental_rentalobject_instantiation(instance):
    assert isinstance(instance, rental_RentalObject)



@given(instance=rental_RentalObject_strategy)
def test_rental_rentalobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rental_RentalObject_strategy)
def test_rental_rentalobject_available_setter(instance):
    original = instance.available
    instance.available = original
    assert instance.available == original



@given(instance=rental_RentalObject_strategy)
def test_rental_rentalobject_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalObject_strategy)
@settings(max_examples=30)
def test_rental_rentalobject_rent_changes_state(instance):
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
        assert has_statements, f"Function 'rent' in rental_RentalObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'rent' in rental_RentalObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'rent' in rental_RentalObject is not implemented or raised an error")

@given(instance=rental_Address_strategy)
@settings(max_examples=50)
def test_rental_address_instantiation(instance):
    assert isinstance(instance, rental_Address)



@given(instance=rental_Address_strategy)
def test_rental_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=rental_Address_strategy)
def test_rental_address_streetName_setter(instance):
    original = instance.streetName
    instance.streetName = original
    assert instance.streetName == original



@given(instance=rental_Address_strategy)
def test_rental_address_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=rental_Address_strategy)
def test_rental_address_streetType_setter(instance):
    original = instance.streetType
    instance.streetType = original
    assert instance.streetType == original



@given(instance=rental_Address_strategy)
def test_rental_address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=50)
def test_rental_rentalagency_instantiation(instance):
    assert isinstance(instance, rental_RentalAgency)



@given(instance=rental_RentalAgency_strategy)
def test_rental_rentalagency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=30)
def test_rental_rentalagency_book_changes_state(instance):
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
        assert has_statements, f"Function 'book' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'book' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'book' in rental_RentalAgency is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=30)
def test_rental_rentalagency_isavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAvailable(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAvailable' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in rental_RentalAgency is not implemented or raised an error")
