import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RentalObject,
    rental::Device,
    rental::Car,
    rental::License,
    rental::Rental,
    rental::Customer,
    rental::RentalObject,
    rental::Address,
    rental::RentalAgency,
    StreetType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rentalobject_is_not_abstract():
    assert not inspect.isabstract(RentalObject)


def test_rentalobject_constructor_exists():
    assert callable(RentalObject.__init__)


def test_rentalobject_constructor_args():
    sig = inspect.signature(RentalObject.__init__)
    params = list(sig.parameters.keys())



def test_rental::device_is_not_abstract():
    assert not inspect.isabstract(rental::Device)


def test_rental::device_constructor_exists():
    assert callable(rental::Device.__init__)


def test_rental::device_constructor_args():
    sig = inspect.signature(rental::Device.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "height" in params, "Missing parameter 'height'"
    assert "serialNumber" in params, "Missing parameter 'serialNumber'"
    assert "width" in params, "Missing parameter 'width'"

def test_rental::device_has_length():
    assert hasattr(rental::Device, "length")
    descriptor = None
    for klass in rental::Device.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_rental::device_has_height():
    assert hasattr(rental::Device, "height")
    descriptor = None
    for klass in rental::Device.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_rental::device_has_serialNumber():
    assert hasattr(rental::Device, "serialNumber")
    descriptor = None
    for klass in rental::Device.__mro__:
        if "serialNumber" in klass.__dict__:
            descriptor = klass.__dict__["serialNumber"]
            break
    assert isinstance(descriptor, property)

def test_rental::device_has_width():
    assert hasattr(rental::Device, "width")
    descriptor = None
    for klass in rental::Device.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_rental::car_is_not_abstract():
    assert not inspect.isabstract(rental::Car)


def test_rental::car_constructor_exists():
    assert callable(rental::Car.__init__)


def test_rental::car_constructor_args():
    sig = inspect.signature(rental::Car.__init__)
    params = list(sig.parameters.keys())
    assert "licensePlate" in params, "Missing parameter 'licensePlate'"

def test_rental::car_has_licensePlate():
    assert hasattr(rental::Car, "licensePlate")
    descriptor = None
    for klass in rental::Car.__mro__:
        if "licensePlate" in klass.__dict__:
            descriptor = klass.__dict__["licensePlate"]
            break
    assert isinstance(descriptor, property)



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



def test_rental::rentalobject_is_not_abstract():
    assert not inspect.isabstract(rental::RentalObject)


def test_rental::rentalobject_constructor_exists():
    assert callable(rental::RentalObject.__init__)


def test_rental::rentalobject_constructor_args():
    sig = inspect.signature(rental::RentalObject.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "available" in params, "Missing parameter 'available'"

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

def test_rental::rentalobject_has_available():
    assert hasattr(rental::RentalObject, "available")
    descriptor = None
    for klass in rental::RentalObject.__mro__:
        if "available" in klass.__dict__:
            descriptor = klass.__dict__["available"]
            break
    assert isinstance(descriptor, property)



def test_rental::address_is_not_abstract():
    assert not inspect.isabstract(rental::Address)


def test_rental::address_constructor_exists():
    assert callable(rental::Address.__init__)


def test_rental::address_constructor_args():
    sig = inspect.signature(rental::Address.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "streetName" in params, "Missing parameter 'streetName'"
    assert "streetType" in params, "Missing parameter 'streetType'"
    assert "city" in params, "Missing parameter 'city'"
    assert "zipCode" in params, "Missing parameter 'zipCode'"

def test_rental::address_has_number():
    assert hasattr(rental::Address, "number")
    descriptor = None
    for klass in rental::Address.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
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

def test_rental::address_has_streetType():
    assert hasattr(rental::Address, "streetType")
    descriptor = None
    for klass in rental::Address.__mro__:
        if "streetType" in klass.__dict__:
            descriptor = klass.__dict__["streetType"]
            break
    assert isinstance(descriptor, property)

def test_rental::address_has_city():
    assert hasattr(rental::Address, "city")
    descriptor = None
    for klass in rental::Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
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
RentalObject_strategy = st.builds(
    RentalObject,
)
rental::Device_strategy = st.builds(
    rental::Device,
    length=
        st.integers(),
    height=
        st.integers(),
    serialNumber=
        safe_text,
    width=
        st.integers()
)
rental::Car_strategy = st.builds(
    rental::Car,
    licensePlate=
        safe_text
)
rental::License_strategy = st.builds(
    rental::License,
    validityDate=
        st.dates(),
    number=
        st.integers()
)
rental::Rental_strategy = st.builds(
    rental::Rental,
    startDate=
        st.dates(),
    endDate=
        st.dates()
)
rental::Customer_strategy = st.builds(
    rental::Customer,
    lastName=
        safe_text,
    firstName=
        safe_text
)
rental::RentalObject_strategy = st.builds(
    rental::RentalObject,
    ID=
        safe_text,
    name=
        safe_text,
    available=
        st.booleans()
)
rental::Address_strategy = st.builds(
    rental::Address,
    number=
        st.integers(),
    streetName=
        safe_text,
    streetType=
        safe_text,
    city=
        safe_text,
    zipCode=
        safe_text
)
rental::RentalAgency_strategy = st.builds(
    rental::RentalAgency,
    name=
        safe_text
)

@given(instance=RentalObject_strategy)
@settings(max_examples=50)
def test_rentalobject_instantiation(instance):
    assert isinstance(instance, RentalObject)

@given(instance=rental::Device_strategy)
@settings(max_examples=50)
def test_rental::device_instantiation(instance):
    assert isinstance(instance, rental::Device)

@given(instance=rental::Device_strategy)
def test_rental::device_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=rental::Device_strategy)
def test_rental::device_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=rental::Device_strategy)
def test_rental::device_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=rental::Device_strategy)
def test_rental::device_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=rental::Device_strategy)
def test_rental::device_serialNumber_type(instance):
    assert isinstance(instance.serialNumber, str)


@given(instance=rental::Device_strategy)
def test_rental::device_serialNumber_setter(instance):
    original = instance.serialNumber
    instance.serialNumber = original
    assert instance.serialNumber == original

@given(instance=rental::Device_strategy)
def test_rental::device_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=rental::Device_strategy)
def test_rental::device_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=rental::Car_strategy)
@settings(max_examples=50)
def test_rental::car_instantiation(instance):
    assert isinstance(instance, rental::Car)

@given(instance=rental::Car_strategy)
def test_rental::car_licensePlate_type(instance):
    assert isinstance(instance.licensePlate, str)


@given(instance=rental::Car_strategy)
def test_rental::car_licensePlate_setter(instance):
    original = instance.licensePlate
    instance.licensePlate = original
    assert instance.licensePlate == original

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

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::License_strategy)
@settings(max_examples=30)
def test_rental::license_isvalid_changes_state(instance):
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
        assert has_statements, f"Function 'isValid' in rental::License is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isValid' in rental::License did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isValid' in rental::License is not implemented or raised an error")

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

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental::Customer_strategy)
@settings(max_examples=30)
def test_rental::customer_addlicense_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addLicense(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addLicense).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addLicense' in rental::Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addLicense' in rental::Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addLicense' in rental::Customer is not implemented or raised an error")

@given(instance=rental::RentalObject_strategy)
@settings(max_examples=50)
def test_rental::rentalobject_instantiation(instance):
    assert isinstance(instance, rental::RentalObject)

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

@given(instance=rental::RentalObject_strategy)
def test_rental::rentalobject_available_type(instance):
    assert isinstance(instance.available, bool)


@given(instance=rental::RentalObject_strategy)
def test_rental::rentalobject_available_setter(instance):
    original = instance.available
    instance.available = original
    assert instance.available == original

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

@given(instance=rental::Address_strategy)
@settings(max_examples=50)
def test_rental::address_instantiation(instance):
    assert isinstance(instance, rental::Address)

@given(instance=rental::Address_strategy)
def test_rental::address_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=rental::Address_strategy)
def test_rental::address_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=rental::Address_strategy)
def test_rental::address_streetName_type(instance):
    assert isinstance(instance.streetName, str)


@given(instance=rental::Address_strategy)
def test_rental::address_streetName_setter(instance):
    original = instance.streetName
    instance.streetName = original
    assert instance.streetName == original

@given(instance=rental::Address_strategy)
def test_rental::address_streetType_type(instance):
    assert isinstance(instance.streetType, str)


@given(instance=rental::Address_strategy)
def test_rental::address_streetType_setter(instance):
    original = instance.streetType
    instance.streetType = original
    assert instance.streetType == original

@given(instance=rental::Address_strategy)
def test_rental::address_city_type(instance):
    assert isinstance(instance.city, str)


@given(instance=rental::Address_strategy)
def test_rental::address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=rental::Address_strategy)
def test_rental::address_zipCode_type(instance):
    assert isinstance(instance.zipCode, str)


@given(instance=rental::Address_strategy)
def test_rental::address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original

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
def test_rental::rentalagency_isavailable_changes_state(instance):
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
        assert has_statements, f"Function 'isAvailable' in rental::RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in rental::RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in rental::RentalAgency is not implemented or raised an error")
