import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Payment,
    shop_ElectronicPayment,
    shop_CashPayment,
    shop_ChequePayment,
    shop_Valuable,
    shop_Person,
    Valuable,
    shop_Payment,
    shop_BankOperation,
    shop_AccountBook,
    shop_Sale,
    shop_Shop,
    Person,
    shop_Customer,
    shop_Employee,
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



def test_shop_electronicpayment_is_not_abstract():
    assert not inspect.isabstract(shop_ElectronicPayment)


def test_shop_electronicpayment_constructor_exists():
    assert callable(shop_ElectronicPayment.__init__)


def test_shop_electronicpayment_constructor_args():
    sig = inspect.signature(shop_ElectronicPayment.__init__)
    params = list(sig.parameters.keys())



def test_shop_cashpayment_is_not_abstract():
    assert not inspect.isabstract(shop_CashPayment)


def test_shop_cashpayment_constructor_exists():
    assert callable(shop_CashPayment.__init__)


def test_shop_cashpayment_constructor_args():
    sig = inspect.signature(shop_CashPayment.__init__)
    params = list(sig.parameters.keys())



def test_shop_chequepayment_is_not_abstract():
    assert not inspect.isabstract(shop_ChequePayment)


def test_shop_chequepayment_constructor_exists():
    assert callable(shop_ChequePayment.__init__)


def test_shop_chequepayment_constructor_args():
    sig = inspect.signature(shop_ChequePayment.__init__)
    params = list(sig.parameters.keys())
    assert "depositDate" in params, "Missing parameter 'depositDate'"
    assert "deposited" in params, "Missing parameter 'deposited'"

def test_shop_chequepayment_has_depositDate():
    assert hasattr(shop_ChequePayment, "depositDate")
    descriptor = None
    for klass in shop_ChequePayment.__mro__:
        if "depositDate" in klass.__dict__:
            descriptor = klass.__dict__["depositDate"]
            break
    assert isinstance(descriptor, property)

def test_shop_chequepayment_has_deposited():
    assert hasattr(shop_ChequePayment, "deposited")
    descriptor = None
    for klass in shop_ChequePayment.__mro__:
        if "deposited" in klass.__dict__:
            descriptor = klass.__dict__["deposited"]
            break
    assert isinstance(descriptor, property)



def test_shop_valuable_is_not_abstract():
    assert not inspect.isabstract(shop_Valuable)


def test_shop_valuable_constructor_exists():
    assert callable(shop_Valuable.__init__)


def test_shop_valuable_constructor_args():
    sig = inspect.signature(shop_Valuable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "date" in params, "Missing parameter 'date'"

def test_shop_valuable_has_value():
    assert hasattr(shop_Valuable, "value")
    descriptor = None
    for klass in shop_Valuable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_shop_valuable_has_date():
    assert hasattr(shop_Valuable, "date")
    descriptor = None
    for klass in shop_Valuable.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_shop_person_is_not_abstract():
    assert not inspect.isabstract(shop_Person)


def test_shop_person_constructor_exists():
    assert callable(shop_Person.__init__)


def test_shop_person_constructor_args():
    sig = inspect.signature(shop_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "address" in params, "Missing parameter 'address'"
    assert "emails" in params, "Missing parameter 'emails'"
    assert "phoneNumbers" in params, "Missing parameter 'phoneNumbers'"

def test_shop_person_has_firstName():
    assert hasattr(shop_Person, "firstName")
    descriptor = None
    for klass in shop_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_shop_person_has_birthDate():
    assert hasattr(shop_Person, "birthDate")
    descriptor = None
    for klass in shop_Person.__mro__:
        if "birthDate" in klass.__dict__:
            descriptor = klass.__dict__["birthDate"]
            break
    assert isinstance(descriptor, property)

def test_shop_person_has_lastName():
    assert hasattr(shop_Person, "lastName")
    descriptor = None
    for klass in shop_Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_shop_person_has_address():
    assert hasattr(shop_Person, "address")
    descriptor = None
    for klass in shop_Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_shop_person_has_emails():
    assert hasattr(shop_Person, "emails")
    descriptor = None
    for klass in shop_Person.__mro__:
        if "emails" in klass.__dict__:
            descriptor = klass.__dict__["emails"]
            break
    assert isinstance(descriptor, property)

def test_shop_person_has_phoneNumbers():
    assert hasattr(shop_Person, "phoneNumbers")
    descriptor = None
    for klass in shop_Person.__mro__:
        if "phoneNumbers" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumbers"]
            break
    assert isinstance(descriptor, property)



def test_valuable_is_not_abstract():
    assert not inspect.isabstract(Valuable)


def test_valuable_constructor_exists():
    assert callable(Valuable.__init__)


def test_valuable_constructor_args():
    sig = inspect.signature(Valuable.__init__)
    params = list(sig.parameters.keys())



def test_shop_payment_is_not_abstract():
    assert not inspect.isabstract(shop_Payment)


def test_shop_payment_constructor_exists():
    assert callable(shop_Payment.__init__)


def test_shop_payment_constructor_args():
    sig = inspect.signature(shop_Payment.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_shop_payment_has_type():
    assert hasattr(shop_Payment, "type")
    descriptor = None
    for klass in shop_Payment.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_shop_bankoperation_is_not_abstract():
    assert not inspect.isabstract(shop_BankOperation)


def test_shop_bankoperation_constructor_exists():
    assert callable(shop_BankOperation.__init__)


def test_shop_bankoperation_constructor_args():
    sig = inspect.signature(shop_BankOperation.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_shop_bankoperation_has_description():
    assert hasattr(shop_BankOperation, "description")
    descriptor = None
    for klass in shop_BankOperation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_shop_accountbook_is_not_abstract():
    assert not inspect.isabstract(shop_AccountBook)


def test_shop_accountbook_constructor_exists():
    assert callable(shop_AccountBook.__init__)


def test_shop_accountbook_constructor_args():
    sig = inspect.signature(shop_AccountBook.__init__)
    params = list(sig.parameters.keys())
    assert "cashFlow" in params, "Missing parameter 'cashFlow'"

def test_shop_accountbook_has_cashFlow():
    assert hasattr(shop_AccountBook, "cashFlow")
    descriptor = None
    for klass in shop_AccountBook.__mro__:
        if "cashFlow" in klass.__dict__:
            descriptor = klass.__dict__["cashFlow"]
            break
    assert isinstance(descriptor, property)



def test_shop_sale_is_not_abstract():
    assert not inspect.isabstract(shop_Sale)


def test_shop_sale_constructor_exists():
    assert callable(shop_Sale.__init__)


def test_shop_sale_constructor_args():
    sig = inspect.signature(shop_Sale.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_shop_sale_has_description():
    assert hasattr(shop_Sale, "description")
    descriptor = None
    for klass in shop_Sale.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_shop_shop_is_not_abstract():
    assert not inspect.isabstract(shop_Shop)


def test_shop_shop_constructor_exists():
    assert callable(shop_Shop.__init__)


def test_shop_shop_constructor_args():
    sig = inspect.signature(shop_Shop.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_shop_customer_is_not_abstract():
    assert not inspect.isabstract(shop_Customer)


def test_shop_customer_constructor_exists():
    assert callable(shop_Customer.__init__)


def test_shop_customer_constructor_args():
    sig = inspect.signature(shop_Customer.__init__)
    params = list(sig.parameters.keys())



def test_shop_employee_is_not_abstract():
    assert not inspect.isabstract(shop_Employee)


def test_shop_employee_constructor_exists():
    assert callable(shop_Employee.__init__)


def test_shop_employee_constructor_args():
    sig = inspect.signature(shop_Employee.__init__)
    params = list(sig.parameters.keys())

def test_paymenttype_exists():
    # Check that the Enumeration exists
    assert PaymentType is not None

def test_paymenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PaymentType]
    expected_literals = [
        "CASH",
        "ELECTRONIC",
        "CHEQUE",
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
shop_ElectronicPayment_strategy = st.builds(
    shop_ElectronicPayment,
)
shop_CashPayment_strategy = st.builds(
    shop_CashPayment,
)
shop_ChequePayment_strategy = st.builds(
    shop_ChequePayment,
    depositDate=
        st.dates(),
    deposited=
        st.booleans()
)
shop_Valuable_strategy = st.builds(
    shop_Valuable,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    date=
        st.dates()
)
shop_Person_strategy = st.builds(
    shop_Person,
    firstName=
        safe_text,
    birthDate=
        st.dates(),
    lastName=
        safe_text,
    address=
        safe_text,
    emails=
        safe_text,
    phoneNumbers=
        safe_text
)
Valuable_strategy = st.builds(
    Valuable,
)
shop_Payment_strategy = st.builds(
    shop_Payment,
    type=
        safe_text
)
shop_BankOperation_strategy = st.builds(
    shop_BankOperation,
    description=
        safe_text
)
shop_AccountBook_strategy = st.builds(
    shop_AccountBook,
    cashFlow=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
shop_Sale_strategy = st.builds(
    shop_Sale,
    description=
        safe_text
)
shop_Shop_strategy = st.builds(
    shop_Shop,
)
Person_strategy = st.builds(
    Person,
)
shop_Customer_strategy = st.builds(
    shop_Customer,
)
shop_Employee_strategy = st.builds(
    shop_Employee,
)

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)

@given(instance=shop_ElectronicPayment_strategy)
@settings(max_examples=50)
def test_shop_electronicpayment_instantiation(instance):
    assert isinstance(instance, shop_ElectronicPayment)

@given(instance=shop_CashPayment_strategy)
@settings(max_examples=50)
def test_shop_cashpayment_instantiation(instance):
    assert isinstance(instance, shop_CashPayment)

@given(instance=shop_ChequePayment_strategy)
@settings(max_examples=50)
def test_shop_chequepayment_instantiation(instance):
    assert isinstance(instance, shop_ChequePayment)



@given(instance=shop_ChequePayment_strategy)
def test_shop_chequepayment_depositDate_setter(instance):
    original = instance.depositDate
    instance.depositDate = original
    assert instance.depositDate == original



@given(instance=shop_ChequePayment_strategy)
def test_shop_chequepayment_deposited_setter(instance):
    original = instance.deposited
    instance.deposited = original
    assert instance.deposited == original

@given(instance=shop_Valuable_strategy)
@settings(max_examples=50)
def test_shop_valuable_instantiation(instance):
    assert isinstance(instance, shop_Valuable)



@given(instance=shop_Valuable_strategy)
def test_shop_valuable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=shop_Valuable_strategy)
def test_shop_valuable_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=shop_Person_strategy)
@settings(max_examples=50)
def test_shop_person_instantiation(instance):
    assert isinstance(instance, shop_Person)



@given(instance=shop_Person_strategy)
def test_shop_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=shop_Person_strategy)
def test_shop_person_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=shop_Person_strategy)
def test_shop_person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=shop_Person_strategy)
def test_shop_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=shop_Person_strategy)
def test_shop_person_emails_setter(instance):
    original = instance.emails
    instance.emails = original
    assert instance.emails == original



@given(instance=shop_Person_strategy)
def test_shop_person_phoneNumbers_setter(instance):
    original = instance.phoneNumbers
    instance.phoneNumbers = original
    assert instance.phoneNumbers == original

@given(instance=Valuable_strategy)
@settings(max_examples=50)
def test_valuable_instantiation(instance):
    assert isinstance(instance, Valuable)

@given(instance=shop_Payment_strategy)
@settings(max_examples=50)
def test_shop_payment_instantiation(instance):
    assert isinstance(instance, shop_Payment)



@given(instance=shop_Payment_strategy)
def test_shop_payment_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=shop_BankOperation_strategy)
@settings(max_examples=50)
def test_shop_bankoperation_instantiation(instance):
    assert isinstance(instance, shop_BankOperation)



@given(instance=shop_BankOperation_strategy)
def test_shop_bankoperation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=shop_AccountBook_strategy)
@settings(max_examples=50)
def test_shop_accountbook_instantiation(instance):
    assert isinstance(instance, shop_AccountBook)



@given(instance=shop_AccountBook_strategy)
def test_shop_accountbook_cashFlow_setter(instance):
    original = instance.cashFlow
    instance.cashFlow = original
    assert instance.cashFlow == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=shop_AccountBook_strategy)
@settings(max_examples=30)
def test_shop_accountbook_depositcash_changes_state(instance):
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
        assert has_statements, f"Function 'depositCash' in shop_AccountBook is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'depositCash' in shop_AccountBook did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'depositCash' in shop_AccountBook is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=shop_AccountBook_strategy)
@settings(max_examples=30)
def test_shop_accountbook_depositcheques_changes_state(instance):
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
        assert has_statements, f"Function 'depositCheques' in shop_AccountBook is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'depositCheques' in shop_AccountBook did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'depositCheques' in shop_AccountBook is not implemented or raised an error")

@given(instance=shop_Sale_strategy)
@settings(max_examples=50)
def test_shop_sale_instantiation(instance):
    assert isinstance(instance, shop_Sale)



@given(instance=shop_Sale_strategy)
def test_shop_sale_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=shop_Shop_strategy)
@settings(max_examples=50)
def test_shop_shop_instantiation(instance):
    assert isinstance(instance, shop_Shop)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=shop_Customer_strategy)
@settings(max_examples=50)
def test_shop_customer_instantiation(instance):
    assert isinstance(instance, shop_Customer)

@given(instance=shop_Employee_strategy)
@settings(max_examples=50)
def test_shop_employee_instantiation(instance):
    assert isinstance(instance, shop_Employee)
