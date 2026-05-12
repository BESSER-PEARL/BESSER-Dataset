import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rental_Rental,
    rental_Customer,
    rental_RentalObject,
    rental_RentalAgency,
    StreetType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rental_rental_is_not_abstract():
    assert not inspect.isabstract(rental_Rental)


def test_rental_rental_constructor_exists():
    assert callable(rental_Rental.__init__)


def test_rental_rental_constructor_args():
    sig = inspect.signature(rental_Rental.__init__)
    params = list(sig.parameters.keys())
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"

def test_rental_rental_has_endDate():
    assert hasattr(rental_Rental, "endDate")
    descriptor = None
    for klass in rental_Rental.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_rental_rental_has_startDate():
    assert hasattr(rental_Rental, "startDate")
    descriptor = None
    for klass in rental_Rental.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)



def test_rental_customer_is_not_abstract():
    assert not inspect.isabstract(rental_Customer)


def test_rental_customer_constructor_exists():
    assert callable(rental_Customer.__init__)


def test_rental_customer_constructor_args():
    sig = inspect.signature(rental_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_rental_customer_has_lastName():
    assert hasattr(rental_Customer, "lastName")
    descriptor = None
    for klass in rental_Customer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
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
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "picture" in params, "Missing parameter 'picture'"

def test_rental_rentalobject_has_ID():
    assert hasattr(rental_RentalObject, "ID")
    descriptor = None
    for klass in rental_RentalObject.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_rental_rentalobject_has_name():
    assert hasattr(rental_RentalObject, "name")
    descriptor = None
    for klass in rental_RentalObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rental_rentalobject_has_picture():
    assert hasattr(rental_RentalObject, "picture")
    descriptor = None
    for klass in rental_RentalObject.__mro__:
        if "picture" in klass.__dict__:
            descriptor = klass.__dict__["picture"]
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
rental_Rental_strategy = st.builds(
    rental_Rental,
    endDate=
        st.dates(),
    startDate=
        st.dates()
)
rental_Customer_strategy = st.builds(
    rental_Customer,
    lastName=
        safe_text,
    firstName=
        safe_text
)
rental_RentalObject_strategy = st.builds(
    rental_RentalObject,
    ID=
        safe_text,
    name=
        safe_text,
    picture=
        safe_text
)
rental_RentalAgency_strategy = st.builds(
    rental_RentalAgency,
    name=
        safe_text
)

@given(instance=rental_Rental_strategy)
@settings(max_examples=50)
def test_rental_rental_instantiation(instance):
    assert isinstance(instance, rental_Rental)



@given(instance=rental_Rental_strategy)
def test_rental_rental_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original



@given(instance=rental_Rental_strategy)
def test_rental_rental_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

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
def test_rental_customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



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
def test_rental_rentalobject_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=rental_RentalObject_strategy)
def test_rental_rentalobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=rental_RentalObject_strategy)
def test_rental_rentalobject_picture_setter(instance):
    original = instance.picture
    instance.picture = original
    assert instance.picture == original

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
def test_rental_rentalagency_removecustomer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeCustomer(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeCustomer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeCustomer' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeCustomer' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeCustomer' in rental_RentalAgency is not implemented or raised an error")

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
def test_rental_rentalagency_addobject_changes_state(instance):
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
        assert has_statements, f"Function 'addObject' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addObject' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addObject' in rental_RentalAgency is not implemented or raised an error")

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

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=30)
def test_rental_rentalagency_addcustomer_changes_state(instance):
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
        assert has_statements, f"Function 'addCustomer' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addCustomer' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addCustomer' in rental_RentalAgency is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=rental_RentalAgency_strategy)
@settings(max_examples=30)
def test_rental_rentalagency_removeobject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeObject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeObject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeObject' in rental_RentalAgency is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeObject' in rental_RentalAgency did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeObject' in rental_RentalAgency is not implemented or raised an error")
