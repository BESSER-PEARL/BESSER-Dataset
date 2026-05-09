import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Employee,
    Account,
    BankingSystem::Saving,
    BankingSystem::Chequing,
    BankingSystem::Financial::Representative,
    BankingSystem::Loan,
    BankingSystem::Account,
    BankingSystem::Employee,
    BankingSystem::Customer,
    BankingSystem::Branch,
    BankingSystem::Bank,
    CustomerType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())



def test_bankingsystem::saving_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Saving)


def test_bankingsystem::saving_constructor_exists():
    assert callable(BankingSystem::Saving.__init__)


def test_bankingsystem::saving_constructor_args():
    sig = inspect.signature(BankingSystem::Saving.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_bankingsystem::saving_has_interestRate():
    assert hasattr(BankingSystem::Saving, "interestRate")
    descriptor = None
    for klass in BankingSystem::Saving.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem::chequing_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Chequing)


def test_bankingsystem::chequing_constructor_exists():
    assert callable(BankingSystem::Chequing.__init__)


def test_bankingsystem::chequing_constructor_args():
    sig = inspect.signature(BankingSystem::Chequing.__init__)
    params = list(sig.parameters.keys())



def test_bankingsystem::financial::representative_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Financial::Representative)


def test_bankingsystem::financial::representative_constructor_exists():
    assert callable(BankingSystem::Financial::Representative.__init__)


def test_bankingsystem::financial::representative_constructor_args():
    sig = inspect.signature(BankingSystem::Financial::Representative.__init__)
    params = list(sig.parameters.keys())



def test_bankingsystem::loan_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Loan)


def test_bankingsystem::loan_constructor_exists():
    assert callable(BankingSystem::Loan.__init__)


def test_bankingsystem::loan_constructor_args():
    sig = inspect.signature(BankingSystem::Loan.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "loanNumber" in params, "Missing parameter 'loanNumber'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_bankingsystem::loan_has_amount():
    assert hasattr(BankingSystem::Loan, "amount")
    descriptor = None
    for klass in BankingSystem::Loan.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::loan_has_duration():
    assert hasattr(BankingSystem::Loan, "duration")
    descriptor = None
    for klass in BankingSystem::Loan.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::loan_has_loanNumber():
    assert hasattr(BankingSystem::Loan, "loanNumber")
    descriptor = None
    for klass in BankingSystem::Loan.__mro__:
        if "loanNumber" in klass.__dict__:
            descriptor = klass.__dict__["loanNumber"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::loan_has_interestRate():
    assert hasattr(BankingSystem::Loan, "interestRate")
    descriptor = None
    for klass in BankingSystem::Loan.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem::account_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Account)


def test_bankingsystem::account_constructor_exists():
    assert callable(BankingSystem::Account.__init__)


def test_bankingsystem::account_constructor_args():
    sig = inspect.signature(BankingSystem::Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"

def test_bankingsystem::account_has_balance():
    assert hasattr(BankingSystem::Account, "balance")
    descriptor = None
    for klass in BankingSystem::Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::account_has_accountNumber():
    assert hasattr(BankingSystem::Account, "accountNumber")
    descriptor = None
    for klass in BankingSystem::Account.__mro__:
        if "accountNumber" in klass.__dict__:
            descriptor = klass.__dict__["accountNumber"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem::employee_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Employee)


def test_bankingsystem::employee_constructor_exists():
    assert callable(BankingSystem::Employee.__init__)


def test_bankingsystem::employee_constructor_args():
    sig = inspect.signature(BankingSystem::Employee.__init__)
    params = list(sig.parameters.keys())
    assert "eaddress" in params, "Missing parameter 'eaddress'"
    assert "ephoneNumber" in params, "Missing parameter 'ephoneNumber'"
    assert "eid" in params, "Missing parameter 'eid'"
    assert "ename" in params, "Missing parameter 'ename'"
    assert "isCustomer" in params, "Missing parameter 'isCustomer'"
    assert "eage" in params, "Missing parameter 'eage'"

def test_bankingsystem::employee_has_eaddress():
    assert hasattr(BankingSystem::Employee, "eaddress")
    descriptor = None
    for klass in BankingSystem::Employee.__mro__:
        if "eaddress" in klass.__dict__:
            descriptor = klass.__dict__["eaddress"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::employee_has_ephoneNumber():
    assert hasattr(BankingSystem::Employee, "ephoneNumber")
    descriptor = None
    for klass in BankingSystem::Employee.__mro__:
        if "ephoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["ephoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::employee_has_eid():
    assert hasattr(BankingSystem::Employee, "eid")
    descriptor = None
    for klass in BankingSystem::Employee.__mro__:
        if "eid" in klass.__dict__:
            descriptor = klass.__dict__["eid"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::employee_has_ename():
    assert hasattr(BankingSystem::Employee, "ename")
    descriptor = None
    for klass in BankingSystem::Employee.__mro__:
        if "ename" in klass.__dict__:
            descriptor = klass.__dict__["ename"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::employee_has_isCustomer():
    assert hasattr(BankingSystem::Employee, "isCustomer")
    descriptor = None
    for klass in BankingSystem::Employee.__mro__:
        if "isCustomer" in klass.__dict__:
            descriptor = klass.__dict__["isCustomer"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::employee_has_eage():
    assert hasattr(BankingSystem::Employee, "eage")
    descriptor = None
    for klass in BankingSystem::Employee.__mro__:
        if "eage" in klass.__dict__:
            descriptor = klass.__dict__["eage"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem::customer_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Customer)


def test_bankingsystem::customer_constructor_exists():
    assert callable(BankingSystem::Customer.__init__)


def test_bankingsystem::customer_constructor_args():
    sig = inspect.signature(BankingSystem::Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "customerType" in params, "Missing parameter 'customerType'"
    assert "address" in params, "Missing parameter 'address'"
    assert "age" in params, "Missing parameter 'age'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"

def test_bankingsystem::customer_has_name():
    assert hasattr(BankingSystem::Customer, "name")
    descriptor = None
    for klass in BankingSystem::Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::customer_has_customerType():
    assert hasattr(BankingSystem::Customer, "customerType")
    descriptor = None
    for klass in BankingSystem::Customer.__mro__:
        if "customerType" in klass.__dict__:
            descriptor = klass.__dict__["customerType"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::customer_has_address():
    assert hasattr(BankingSystem::Customer, "address")
    descriptor = None
    for klass in BankingSystem::Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::customer_has_age():
    assert hasattr(BankingSystem::Customer, "age")
    descriptor = None
    for klass in BankingSystem::Customer.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::customer_has_phoneNumber():
    assert hasattr(BankingSystem::Customer, "phoneNumber")
    descriptor = None
    for klass in BankingSystem::Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem::branch_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Branch)


def test_bankingsystem::branch_constructor_exists():
    assert callable(BankingSystem::Branch.__init__)


def test_bankingsystem::branch_constructor_args():
    sig = inspect.signature(BankingSystem::Branch.__init__)
    params = list(sig.parameters.keys())
    assert "branchId" in params, "Missing parameter 'branchId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "location" in params, "Missing parameter 'location'"

def test_bankingsystem::branch_has_branchId():
    assert hasattr(BankingSystem::Branch, "branchId")
    descriptor = None
    for klass in BankingSystem::Branch.__mro__:
        if "branchId" in klass.__dict__:
            descriptor = klass.__dict__["branchId"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::branch_has_name():
    assert hasattr(BankingSystem::Branch, "name")
    descriptor = None
    for klass in BankingSystem::Branch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::branch_has_phoneNumber():
    assert hasattr(BankingSystem::Branch, "phoneNumber")
    descriptor = None
    for klass in BankingSystem::Branch.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::branch_has_location():
    assert hasattr(BankingSystem::Branch, "location")
    descriptor = None
    for klass in BankingSystem::Branch.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem::bank_is_not_abstract():
    assert not inspect.isabstract(BankingSystem::Bank)


def test_bankingsystem::bank_constructor_exists():
    assert callable(BankingSystem::Bank.__init__)


def test_bankingsystem::bank_constructor_args():
    sig = inspect.signature(BankingSystem::Bank.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "bankId" in params, "Missing parameter 'bankId'"
    assert "description" in params, "Missing parameter 'description'"

def test_bankingsystem::bank_has_name():
    assert hasattr(BankingSystem::Bank, "name")
    descriptor = None
    for klass in BankingSystem::Bank.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::bank_has_bankId():
    assert hasattr(BankingSystem::Bank, "bankId")
    descriptor = None
    for klass in BankingSystem::Bank.__mro__:
        if "bankId" in klass.__dict__:
            descriptor = klass.__dict__["bankId"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem::bank_has_description():
    assert hasattr(BankingSystem::Bank, "description")
    descriptor = None
    for klass in BankingSystem::Bank.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_customertype_exists():
    # Check that the Enumeration exists
    assert CustomerType is not None

def test_customertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CustomerType]
    expected_literals = [
        "Senior",
        "Youth",
        "Adult",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CustomerType"


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
Employee_strategy = st.builds(
    Employee,
)
Account_strategy = st.builds(
    Account,
)
BankingSystem::Saving_strategy = st.builds(
    BankingSystem::Saving,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BankingSystem::Chequing_strategy = st.builds(
    BankingSystem::Chequing,
)
BankingSystem::Financial::Representative_strategy = st.builds(
    BankingSystem::Financial::Representative,
)
BankingSystem::Loan_strategy = st.builds(
    BankingSystem::Loan,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    duration=
        st.integers(),
    loanNumber=
        safe_text,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BankingSystem::Account_strategy = st.builds(
    BankingSystem::Account,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    accountNumber=
        safe_text
)
BankingSystem::Employee_strategy = st.builds(
    BankingSystem::Employee,
    eaddress=
        safe_text,
    ephoneNumber=
        safe_text,
    eid=
        st.integers(),
    ename=
        safe_text,
    isCustomer=
        st.booleans(),
    eage=
        st.integers()
)
BankingSystem::Customer_strategy = st.builds(
    BankingSystem::Customer,
    name=
        safe_text,
    customerType=
        safe_text,
    address=
        safe_text,
    age=
        st.integers(),
    phoneNumber=
        safe_text
)
BankingSystem::Branch_strategy = st.builds(
    BankingSystem::Branch,
    branchId=
        st.integers(),
    name=
        safe_text,
    phoneNumber=
        safe_text,
    location=
        safe_text
)
BankingSystem::Bank_strategy = st.builds(
    BankingSystem::Bank,
    name=
        safe_text,
    bankId=
        st.integers(),
    description=
        safe_text
)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)

@given(instance=BankingSystem::Saving_strategy)
@settings(max_examples=50)
def test_bankingsystem::saving_instantiation(instance):
    assert isinstance(instance, BankingSystem::Saving)

@given(instance=BankingSystem::Saving_strategy)
def test_bankingsystem::saving_interestRate_type(instance):
    assert isinstance(instance.interestRate, float)


@given(instance=BankingSystem::Saving_strategy)
def test_bankingsystem::saving_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=BankingSystem::Chequing_strategy)
@settings(max_examples=50)
def test_bankingsystem::chequing_instantiation(instance):
    assert isinstance(instance, BankingSystem::Chequing)

@given(instance=BankingSystem::Financial::Representative_strategy)
@settings(max_examples=50)
def test_bankingsystem::financial::representative_instantiation(instance):
    assert isinstance(instance, BankingSystem::Financial::Representative)

@given(instance=BankingSystem::Loan_strategy)
@settings(max_examples=50)
def test_bankingsystem::loan_instantiation(instance):
    assert isinstance(instance, BankingSystem::Loan)

@given(instance=BankingSystem::Loan_strategy)
def test_bankingsystem::loan_amount_type(instance):
    assert isinstance(instance.amount, float)


@given(instance=BankingSystem::Loan_strategy)
def test_bankingsystem::loan_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=BankingSystem::Loan_strategy)
def test_bankingsystem::loan_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=BankingSystem::Loan_strategy)
def test_bankingsystem::loan_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=BankingSystem::Loan_strategy)
def test_bankingsystem::loan_loanNumber_type(instance):
    assert isinstance(instance.loanNumber, str)


@given(instance=BankingSystem::Loan_strategy)
def test_bankingsystem::loan_loanNumber_setter(instance):
    original = instance.loanNumber
    instance.loanNumber = original
    assert instance.loanNumber == original

@given(instance=BankingSystem::Loan_strategy)
def test_bankingsystem::loan_interestRate_type(instance):
    assert isinstance(instance.interestRate, float)


@given(instance=BankingSystem::Loan_strategy)
def test_bankingsystem::loan_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=BankingSystem::Account_strategy)
@settings(max_examples=50)
def test_bankingsystem::account_instantiation(instance):
    assert isinstance(instance, BankingSystem::Account)

@given(instance=BankingSystem::Account_strategy)
def test_bankingsystem::account_balance_type(instance):
    assert isinstance(instance.balance, float)


@given(instance=BankingSystem::Account_strategy)
def test_bankingsystem::account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=BankingSystem::Account_strategy)
def test_bankingsystem::account_accountNumber_type(instance):
    assert isinstance(instance.accountNumber, str)


@given(instance=BankingSystem::Account_strategy)
def test_bankingsystem::account_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original

@given(instance=BankingSystem::Employee_strategy)
@settings(max_examples=50)
def test_bankingsystem::employee_instantiation(instance):
    assert isinstance(instance, BankingSystem::Employee)

@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_eaddress_type(instance):
    assert isinstance(instance.eaddress, str)


@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_eaddress_setter(instance):
    original = instance.eaddress
    instance.eaddress = original
    assert instance.eaddress == original

@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_ephoneNumber_type(instance):
    assert isinstance(instance.ephoneNumber, str)


@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_ephoneNumber_setter(instance):
    original = instance.ephoneNumber
    instance.ephoneNumber = original
    assert instance.ephoneNumber == original

@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_eid_type(instance):
    assert isinstance(instance.eid, int)


@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_eid_setter(instance):
    original = instance.eid
    instance.eid = original
    assert instance.eid == original

@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_ename_type(instance):
    assert isinstance(instance.ename, str)


@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_ename_setter(instance):
    original = instance.ename
    instance.ename = original
    assert instance.ename == original

@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_isCustomer_type(instance):
    assert isinstance(instance.isCustomer, bool)


@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_isCustomer_setter(instance):
    original = instance.isCustomer
    instance.isCustomer = original
    assert instance.isCustomer == original

@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_eage_type(instance):
    assert isinstance(instance.eage, int)


@given(instance=BankingSystem::Employee_strategy)
def test_bankingsystem::employee_eage_setter(instance):
    original = instance.eage
    instance.eage = original
    assert instance.eage == original

@given(instance=BankingSystem::Customer_strategy)
@settings(max_examples=50)
def test_bankingsystem::customer_instantiation(instance):
    assert isinstance(instance, BankingSystem::Customer)

@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_customerType_type(instance):
    assert isinstance(instance.customerType, str)


@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_customerType_setter(instance):
    original = instance.customerType
    instance.customerType = original
    assert instance.customerType == original

@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_phoneNumber_type(instance):
    assert isinstance(instance.phoneNumber, str)


@given(instance=BankingSystem::Customer_strategy)
def test_bankingsystem::customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original

@given(instance=BankingSystem::Branch_strategy)
@settings(max_examples=50)
def test_bankingsystem::branch_instantiation(instance):
    assert isinstance(instance, BankingSystem::Branch)

@given(instance=BankingSystem::Branch_strategy)
def test_bankingsystem::branch_branchId_type(instance):
    assert isinstance(instance.branchId, int)


@given(instance=BankingSystem::Branch_strategy)
def test_bankingsystem::branch_branchId_setter(instance):
    original = instance.branchId
    instance.branchId = original
    assert instance.branchId == original

@given(instance=BankingSystem::Branch_strategy)
def test_bankingsystem::branch_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BankingSystem::Branch_strategy)
def test_bankingsystem::branch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BankingSystem::Branch_strategy)
def test_bankingsystem::branch_phoneNumber_type(instance):
    assert isinstance(instance.phoneNumber, str)


@given(instance=BankingSystem::Branch_strategy)
def test_bankingsystem::branch_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original

@given(instance=BankingSystem::Branch_strategy)
def test_bankingsystem::branch_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=BankingSystem::Branch_strategy)
def test_bankingsystem::branch_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=BankingSystem::Bank_strategy)
@settings(max_examples=50)
def test_bankingsystem::bank_instantiation(instance):
    assert isinstance(instance, BankingSystem::Bank)

@given(instance=BankingSystem::Bank_strategy)
def test_bankingsystem::bank_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BankingSystem::Bank_strategy)
def test_bankingsystem::bank_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BankingSystem::Bank_strategy)
def test_bankingsystem::bank_bankId_type(instance):
    assert isinstance(instance.bankId, int)


@given(instance=BankingSystem::Bank_strategy)
def test_bankingsystem::bank_bankId_setter(instance):
    original = instance.bankId
    instance.bankId = original
    assert instance.bankId == original

@given(instance=BankingSystem::Bank_strategy)
def test_bankingsystem::bank_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=BankingSystem::Bank_strategy)
def test_bankingsystem::bank_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
