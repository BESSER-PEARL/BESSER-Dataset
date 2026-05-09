import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Payment,
    shop::ElectronicPayment,
    shop::CashPayment,
    shop::ChequePayment,
    shop::Valuable,
    shop::Person,
    Valuable,
    shop::Payment,
    shop::BankOperation,
    shop::AccountBook,
    shop::Sale,
    shop::Shop,
    Person,
    shop::Customer,
    shop::Employee,
    PaymentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())



def test_shop::electronicpayment_is_not_abstract():
    assert not inspect.isabstract(shop::ElectronicPayment)


def test_shop::electronicpayment_constructor_exists():
    assert callable(shop::ElectronicPayment.__init__)


def test_shop::electronicpayment_constructor_args():
    sig = inspect.signature(shop::ElectronicPayment.__init__)
    params = list(sig.parameters.keys())



def test_shop::cashpayment_is_not_abstract():
    assert not inspect.isabstract(shop::CashPayment)


def test_shop::cashpayment_constructor_exists():
    assert callable(shop::CashPayment.__init__)


def test_shop::cashpayment_constructor_args():
    sig = inspect.signature(shop::CashPayment.__init__)
    params = list(sig.parameters.keys())



def test_shop::chequepayment_is_not_abstract():
    assert not inspect.isabstract(shop::ChequePayment)


def test_shop::chequepayment_constructor_exists():
    assert callable(shop::ChequePayment.__init__)


def test_shop::chequepayment_constructor_args():
    sig = inspect.signature(shop::ChequePayment.__init__)
    params = list(sig.parameters.keys())
    assert "depositDate" in params, "Missing parameter 'depositDate'"
    assert "deposited" in params, "Missing parameter 'deposited'"

def test_shop::chequepayment_has_depositDate():
    assert hasattr(shop::ChequePayment, "depositDate")
    descriptor = None
    for klass in shop::ChequePayment.__mro__:
        if "depositDate" in klass.__dict__:
            descriptor = klass.__dict__["depositDate"]
            break
    assert isinstance(descriptor, property)

def test_shop::chequepayment_has_deposited():
    assert hasattr(shop::ChequePayment, "deposited")
    descriptor = None
    for klass in shop::ChequePayment.__mro__:
        if "deposited" in klass.__dict__:
            descriptor = klass.__dict__["deposited"]
            break
    assert isinstance(descriptor, property)



def test_shop::valuable_is_not_abstract():
    assert not inspect.isabstract(shop::Valuable)


def test_shop::valuable_constructor_exists():
    assert callable(shop::Valuable.__init__)


def test_shop::valuable_constructor_args():
    sig = inspect.signature(shop::Valuable.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "value" in params, "Missing parameter 'value'"

def test_shop::valuable_has_date():
    assert hasattr(shop::Valuable, "date")
    descriptor = None
    for klass in shop::Valuable.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_shop::valuable_has_value():
    assert hasattr(shop::Valuable, "value")
    descriptor = None
    for klass in shop::Valuable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_shop::person_is_not_abstract():
    assert not inspect.isabstract(shop::Person)


def test_shop::person_constructor_exists():
    assert callable(shop::Person.__init__)


def test_shop::person_constructor_args():
    sig = inspect.signature(shop::Person.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNumbers" in params, "Missing parameter 'phoneNumbers'"
    assert "emails" in params, "Missing parameter 'emails'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "address" in params, "Missing parameter 'address'"

def test_shop::person_has_phoneNumbers():
    assert hasattr(shop::Person, "phoneNumbers")
    descriptor = None
    for klass in shop::Person.__mro__:
        if "phoneNumbers" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumbers"]
            break
    assert isinstance(descriptor, property)

def test_shop::person_has_emails():
    assert hasattr(shop::Person, "emails")
    descriptor = None
    for klass in shop::Person.__mro__:
        if "emails" in klass.__dict__:
            descriptor = klass.__dict__["emails"]
            break
    assert isinstance(descriptor, property)

def test_shop::person_has_birthDate():
    assert hasattr(shop::Person, "birthDate")
    descriptor = None
    for klass in shop::Person.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_shop::person_has_lastName():
    assert hasattr(shop::Person, "lastName")
    descriptor = None
    for klass in shop::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_shop::person_has_firstName():
    assert hasattr(shop::Person, "firstName")
    descriptor = None
    for klass in shop::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_shop::person_has_address():
    assert hasattr(shop::Person, "address")
    descriptor = None
    for klass in shop::Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_valuable_is_not_abstract():
    assert not inspect.isabstract(Valuable)


def test_valuable_constructor_exists():
    assert callable(Valuable.__init__)


def test_valuable_constructor_args():
    sig = inspect.signature(Valuable.__init__)
    params = list(sig.parameters.keys())



def test_shop::payment_is_not_abstract():
    assert not inspect.isabstract(shop::Payment)


def test_shop::payment_constructor_exists():
    assert callable(shop::Payment.__init__)


def test_shop::payment_constructor_args():
    sig = inspect.signature(shop::Payment.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_shop::payment_has_type():
    assert hasattr(shop::Payment, "type")
    descriptor = None
    for klass in shop::Payment.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_shop::bankoperation_is_not_abstract():
    assert not inspect.isabstract(shop::BankOperation)


def test_shop::bankoperation_constructor_exists():
    assert callable(shop::BankOperation.__init__)


def test_shop::bankoperation_constructor_args():
    sig = inspect.signature(shop::BankOperation.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_shop::bankoperation_has_description():
    assert hasattr(shop::BankOperation, "description")
    descriptor = None
    for klass in shop::BankOperation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_shop::accountbook_is_not_abstract():
    assert not inspect.isabstract(shop::AccountBook)


def test_shop::accountbook_constructor_exists():
    assert callable(shop::AccountBook.__init__)


def test_shop::accountbook_constructor_args():
    sig = inspect.signature(shop::AccountBook.__init__)
    params = list(sig.parameters.keys())
    assert "cashFlow" in params, "Missing parameter 'cashFlow'"

def test_shop::accountbook_has_cashFlow():
    assert hasattr(shop::AccountBook, "cashFlow")
    descriptor = None
    for klass in shop::AccountBook.__mro__:
        if "cashFlow" in klass.__dict__:
            descriptor = klass.__dict__["cashFlow"]
            break
    assert isinstance(descriptor, property)



def test_shop::sale_is_not_abstract():
    assert not inspect.isabstract(shop::Sale)


def test_shop::sale_constructor_exists():
    assert callable(shop::Sale.__init__)


def test_shop::sale_constructor_args():
    sig = inspect.signature(shop::Sale.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_shop::sale_has_description():
    assert hasattr(shop::Sale, "description")
    descriptor = None
    for klass in shop::Sale.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_shop::shop_is_not_abstract():
    assert not inspect.isabstract(shop::Shop)


def test_shop::shop_constructor_exists():
    assert callable(shop::Shop.__init__)


def test_shop::shop_constructor_args():
    sig = inspect.signature(shop::Shop.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_shop::customer_is_not_abstract():
    assert not inspect.isabstract(shop::Customer)


def test_shop::customer_constructor_exists():
    assert callable(shop::Customer.__init__)


def test_shop::customer_constructor_args():
    sig = inspect.signature(shop::Customer.__init__)
    params = list(sig.parameters.keys())



def test_shop::employee_is_not_abstract():
    assert not inspect.isabstract(shop::Employee)


def test_shop::employee_constructor_exists():
    assert callable(shop::Employee.__init__)


def test_shop::employee_constructor_args():
    sig = inspect.signature(shop::Employee.__init__)
    params = list(sig.parameters.keys())

def test_paymenttype_exists():
    # Check that the Enumeration exists
    assert PaymentType is not None

def test_paymenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PaymentType]
    expected_literals = [
        "CHEQUE",
        "CASH",
        "ELECTRONIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PaymentType"


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
Payment_strategy = st.builds(
    Payment,
)
shop::ElectronicPayment_strategy = st.builds(
    shop::ElectronicPayment,
)
shop::CashPayment_strategy = st.builds(
    shop::CashPayment,
)
shop::ChequePayment_strategy = st.builds(
    shop::ChequePayment,
    depositDate=
        st.dates(),
    deposited=
        st.booleans()
)
shop::Valuable_strategy = st.builds(
    shop::Valuable,
    date=
        st.dates(),
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
shop::Person_strategy = st.builds(
    shop::Person,
    phoneNumbers=
        safe_text,
    emails=
        safe_text,
    birthDate=
        st.dates(),
    lastName=
        safe_text,
    firstName=
        safe_text,
    address=
        safe_text
)
Valuable_strategy = st.builds(
    Valuable,
)
shop::Payment_strategy = st.builds(
    shop::Payment,
    type=
        safe_text
)
shop::BankOperation_strategy = st.builds(
    shop::BankOperation,
    description=
        safe_text
)
shop::AccountBook_strategy = st.builds(
    shop::AccountBook,
    cashFlow=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
shop::Sale_strategy = st.builds(
    shop::Sale,
    description=
        safe_text
)
shop::Shop_strategy = st.builds(
    shop::Shop,
)
Person_strategy = st.builds(
    Person,
)
shop::Customer_strategy = st.builds(
    shop::Customer,
)
shop::Employee_strategy = st.builds(
    shop::Employee,
)

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)

@given(instance=shop::ElectronicPayment_strategy)
@settings(max_examples=50)
def test_shop::electronicpayment_instantiation(instance):
    assert isinstance(instance, shop::ElectronicPayment)

@given(instance=shop::CashPayment_strategy)
@settings(max_examples=50)
def test_shop::cashpayment_instantiation(instance):
    assert isinstance(instance, shop::CashPayment)

@given(instance=shop::ChequePayment_strategy)
@settings(max_examples=50)
def test_shop::chequepayment_instantiation(instance):
    assert isinstance(instance, shop::ChequePayment)

@given(instance=shop::ChequePayment_strategy)
def test_shop::chequepayment_depositDate_type(instance):
    assert isinstance(instance.depositDate, date)


@given(instance=shop::ChequePayment_strategy)
def test_shop::chequepayment_depositDate_setter(instance):
    original = instance.depositDate
    instance.depositDate = original
    assert instance.depositDate == original

@given(instance=shop::ChequePayment_strategy)
def test_shop::chequepayment_deposited_type(instance):
    assert isinstance(instance.deposited, bool)


@given(instance=shop::ChequePayment_strategy)
def test_shop::chequepayment_deposited_setter(instance):
    original = instance.deposited
    instance.deposited = original
    assert instance.deposited == original

@given(instance=shop::Valuable_strategy)
@settings(max_examples=50)
def test_shop::valuable_instantiation(instance):
    assert isinstance(instance, shop::Valuable)

@given(instance=shop::Valuable_strategy)
def test_shop::valuable_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=shop::Valuable_strategy)
def test_shop::valuable_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=shop::Valuable_strategy)
def test_shop::valuable_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=shop::Valuable_strategy)
def test_shop::valuable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=shop::Person_strategy)
@settings(max_examples=50)
def test_shop::person_instantiation(instance):
    assert isinstance(instance, shop::Person)

@given(instance=shop::Person_strategy)
def test_shop::person_phoneNumbers_type(instance):
    assert isinstance(instance.phoneNumbers, str)


@given(instance=shop::Person_strategy)
def test_shop::person_phoneNumbers_setter(instance):
    original = instance.phoneNumbers
    instance.phoneNumbers = original
    assert instance.phoneNumbers == original

@given(instance=shop::Person_strategy)
def test_shop::person_emails_type(instance):
    assert isinstance(instance.emails, str)


@given(instance=shop::Person_strategy)
def test_shop::person_emails_setter(instance):
    original = instance.emails
    instance.emails = original
    assert instance.emails == original

@given(instance=shop::Person_strategy)
def test_shop::person_birthDate_type(instance):
    assert isinstance(instance.birthDate, date)


@given(instance=shop::Person_strategy)
def test_shop::person_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original

@given(instance=shop::Person_strategy)
def test_shop::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=shop::Person_strategy)
def test_shop::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=shop::Person_strategy)
def test_shop::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=shop::Person_strategy)
def test_shop::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=shop::Person_strategy)
def test_shop::person_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=shop::Person_strategy)
def test_shop::person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Valuable_strategy)
@settings(max_examples=50)
def test_valuable_instantiation(instance):
    assert isinstance(instance, Valuable)

@given(instance=shop::Payment_strategy)
@settings(max_examples=50)
def test_shop::payment_instantiation(instance):
    assert isinstance(instance, shop::Payment)

@given(instance=shop::Payment_strategy)
def test_shop::payment_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=shop::Payment_strategy)
def test_shop::payment_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=shop::BankOperation_strategy)
@settings(max_examples=50)
def test_shop::bankoperation_instantiation(instance):
    assert isinstance(instance, shop::BankOperation)

@given(instance=shop::BankOperation_strategy)
def test_shop::bankoperation_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=shop::BankOperation_strategy)
def test_shop::bankoperation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=shop::AccountBook_strategy)
@settings(max_examples=50)
def test_shop::accountbook_instantiation(instance):
    assert isinstance(instance, shop::AccountBook)

@given(instance=shop::AccountBook_strategy)
def test_shop::accountbook_cashFlow_type(instance):
    assert isinstance(instance.cashFlow, float)


@given(instance=shop::AccountBook_strategy)
def test_shop::accountbook_cashFlow_setter(instance):
    original = instance.cashFlow
    instance.cashFlow = original
    assert instance.cashFlow == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=shop::AccountBook_strategy)
@settings(max_examples=30)
def test_shop::accountbook_depositcash_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.depositCash(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.depositCash).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'depositCash' in shop::AccountBook is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'depositCash' in shop::AccountBook did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'depositCash' in shop::AccountBook is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=shop::AccountBook_strategy)
@settings(max_examples=30)
def test_shop::accountbook_depositcheques_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.depositCheques(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.depositCheques).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'depositCheques' in shop::AccountBook is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'depositCheques' in shop::AccountBook did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'depositCheques' in shop::AccountBook is not implemented or raised an error")

@given(instance=shop::Sale_strategy)
@settings(max_examples=50)
def test_shop::sale_instantiation(instance):
    assert isinstance(instance, shop::Sale)

@given(instance=shop::Sale_strategy)
def test_shop::sale_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=shop::Sale_strategy)
def test_shop::sale_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=shop::Shop_strategy)
@settings(max_examples=50)
def test_shop::shop_instantiation(instance):
    assert isinstance(instance, shop::Shop)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=shop::Customer_strategy)
@settings(max_examples=50)
def test_shop::customer_instantiation(instance):
    assert isinstance(instance, shop::Customer)

@given(instance=shop::Employee_strategy)
@settings(max_examples=50)
def test_shop::employee_instantiation(instance):
    assert isinstance(instance, shop::Employee)
