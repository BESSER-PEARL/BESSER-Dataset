import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Savings_Account,
    Current_Account,
    ATM__Transactions,
    ATM,
    Account,
    Customer,
    BANK,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_savings_account_is_not_abstract():
    assert not inspect.isabstract(Savings_Account)


def test_savings_account_constructor_exists():
    assert callable(Savings_Account.__init__)


def test_savings_account_constructor_args():
    sig = inspect.signature(Savings_Account.__init__)
    params = list(sig.parameters.keys())
    assert "AccountNumber" in params, "Missing parameter 'AccountNumber'"
    assert "Balance" in params, "Missing parameter 'Balance'"

def test_savings_account_has_AccountNumber():
    assert hasattr(Savings_Account, "AccountNumber")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "AccountNumber" in klass.__dict__:
            descriptor = klass.__dict__["AccountNumber"]
            break
    assert isinstance(descriptor, property)

def test_savings_account_has_Balance():
    assert hasattr(Savings_Account, "Balance")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "Balance" in klass.__dict__:
            descriptor = klass.__dict__["Balance"]
            break
    assert isinstance(descriptor, property)



def test_current_account_is_not_abstract():
    assert not inspect.isabstract(Current_Account)


def test_current_account_constructor_exists():
    assert callable(Current_Account.__init__)


def test_current_account_constructor_args():
    sig = inspect.signature(Current_Account.__init__)
    params = list(sig.parameters.keys())
    assert "Balance" in params, "Missing parameter 'Balance'"
    assert "AccountNumber" in params, "Missing parameter 'AccountNumber'"

def test_current_account_has_Balance():
    assert hasattr(Current_Account, "Balance")
    descriptor = None
    for klass in Current_Account.__mro__:
        if "Balance" in klass.__dict__:
            descriptor = klass.__dict__["Balance"]
            break
    assert isinstance(descriptor, property)

def test_current_account_has_AccountNumber():
    assert hasattr(Current_Account, "AccountNumber")
    descriptor = None
    for klass in Current_Account.__mro__:
        if "AccountNumber" in klass.__dict__:
            descriptor = klass.__dict__["AccountNumber"]
            break
    assert isinstance(descriptor, property)



def test_atm__transactions_is_not_abstract():
    assert not inspect.isabstract(ATM__Transactions)


def test_atm__transactions_constructor_exists():
    assert callable(ATM__Transactions.__init__)


def test_atm__transactions_constructor_args():
    sig = inspect.signature(ATM__Transactions.__init__)
    params = list(sig.parameters.keys())
    assert "Transaction_amount" in params, "Missing parameter 'Transaction_amount'"
    assert "Remaining_balance" in params, "Missing parameter 'Remaining_balance'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Transaction_id" in params, "Missing parameter 'Transaction_id'"

def test_atm__transactions_has_Transaction_amount():
    assert hasattr(ATM__Transactions, "Transaction_amount")
    descriptor = None
    for klass in ATM__Transactions.__mro__:
        if "Transaction_amount" in klass.__dict__:
            descriptor = klass.__dict__["Transaction_amount"]
            break
    assert isinstance(descriptor, property)

def test_atm__transactions_has_Remaining_balance():
    assert hasattr(ATM__Transactions, "Remaining_balance")
    descriptor = None
    for klass in ATM__Transactions.__mro__:
        if "Remaining_balance" in klass.__dict__:
            descriptor = klass.__dict__["Remaining_balance"]
            break
    assert isinstance(descriptor, property)

def test_atm__transactions_has_Type():
    assert hasattr(ATM__Transactions, "Type")
    descriptor = None
    for klass in ATM__Transactions.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_atm__transactions_has_Transaction_id():
    assert hasattr(ATM__Transactions, "Transaction_id")
    descriptor = None
    for klass in ATM__Transactions.__mro__:
        if "Transaction_id" in klass.__dict__:
            descriptor = klass.__dict__["Transaction_id"]
            break
    assert isinstance(descriptor, property)



def test_atm_is_not_abstract():
    assert not inspect.isabstract(ATM)


def test_atm_constructor_exists():
    assert callable(ATM.__init__)


def test_atm_constructor_args():
    sig = inspect.signature(ATM.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "ManagedBy" in params, "Missing parameter 'ManagedBy'"

def test_atm_has_location():
    assert hasattr(ATM, "location")
    descriptor = None
    for klass in ATM.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_atm_has_ManagedBy():
    assert hasattr(ATM, "ManagedBy")
    descriptor = None
    for klass in ATM.__mro__:
        if "ManagedBy" in klass.__dict__:
            descriptor = klass.__dict__["ManagedBy"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "Balance" in params, "Missing parameter 'Balance'"
    assert "AccountNumber" in params, "Missing parameter 'AccountNumber'"

def test_account_has_Balance():
    assert hasattr(Account, "Balance")
    descriptor = None
    for klass in Account.__mro__:
        if "Balance" in klass.__dict__:
            descriptor = klass.__dict__["Balance"]
            break
    assert isinstance(descriptor, property)

def test_account_has_AccountNumber():
    assert hasattr(Account, "AccountNumber")
    descriptor = None
    for klass in Account.__mro__:
        if "AccountNumber" in klass.__dict__:
            descriptor = klass.__dict__["AccountNumber"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Card_number" in params, "Missing parameter 'Card_number'"
    assert "Pin" in params, "Missing parameter 'Pin'"
    assert "Date_of_birth" in params, "Missing parameter 'Date_of_birth'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_customer_has_Card_number():
    assert hasattr(Customer, "Card_number")
    descriptor = None
    for klass in Customer.__mro__:
        if "Card_number" in klass.__dict__:
            descriptor = klass.__dict__["Card_number"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Pin():
    assert hasattr(Customer, "Pin")
    descriptor = None
    for klass in Customer.__mro__:
        if "Pin" in klass.__dict__:
            descriptor = klass.__dict__["Pin"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Date_of_birth():
    assert hasattr(Customer, "Date_of_birth")
    descriptor = None
    for klass in Customer.__mro__:
        if "Date_of_birth" in klass.__dict__:
            descriptor = klass.__dict__["Date_of_birth"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Name():
    assert hasattr(Customer, "Name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(BANK)


def test_bank_constructor_exists():
    assert callable(BANK.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(BANK.__init__)
    params = list(sig.parameters.keys())
    assert "Code" in params, "Missing parameter 'Code'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_bank_has_Code():
    assert hasattr(BANK, "Code")
    descriptor = None
    for klass in BANK.__mro__:
        if "Code" in klass.__dict__:
            descriptor = klass.__dict__["Code"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_Address():
    assert hasattr(BANK, "Address")
    descriptor = None
    for klass in BANK.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
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
Savings_Account_strategy = st.builds(
    Savings_Account,
    AccountNumber=
        st.integers(),
    Balance=
        st.integers()
)
Current_Account_strategy = st.builds(
    Current_Account,
    Balance=
        st.integers(),
    AccountNumber=
        st.integers()
)
ATM__Transactions_strategy = st.builds(
    ATM__Transactions,
    Transaction_amount=
        st.integers(),
    Remaining_balance=
        st.integers(),
    Type=
        safe_text,
    Transaction_id=
        safe_text
)
ATM_strategy = st.builds(
    ATM,
    location=
        safe_text,
    ManagedBy=
        safe_text
)
Account_strategy = st.builds(
    Account,
    Balance=
        st.integers(),
    AccountNumber=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    Card_number=
        st.integers(),
    Pin=
        st.integers(),
    Date_of_birth=
        safe_text,
    Name=
        safe_text
)
BANK_strategy = st.builds(
    BANK,
    Code=
        safe_text,
    Address=
        safe_text
)

@given(instance=Savings_Account_strategy)
@settings(max_examples=50)
def test_savings_account_instantiation(instance):
    assert isinstance(instance, Savings_Account)



@given(instance=Savings_Account_strategy)
def test_savings_account_AccountNumber_setter(instance):
    original = instance.AccountNumber
    instance.AccountNumber = original
    assert instance.AccountNumber == original



@given(instance=Savings_Account_strategy)
def test_savings_account_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original

@given(instance=Current_Account_strategy)
@settings(max_examples=50)
def test_current_account_instantiation(instance):
    assert isinstance(instance, Current_Account)



@given(instance=Current_Account_strategy)
def test_current_account_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original



@given(instance=Current_Account_strategy)
def test_current_account_AccountNumber_setter(instance):
    original = instance.AccountNumber
    instance.AccountNumber = original
    assert instance.AccountNumber == original

@given(instance=ATM__Transactions_strategy)
@settings(max_examples=50)
def test_atm__transactions_instantiation(instance):
    assert isinstance(instance, ATM__Transactions)



@given(instance=ATM__Transactions_strategy)
def test_atm__transactions_Transaction_amount_setter(instance):
    original = instance.Transaction_amount
    instance.Transaction_amount = original
    assert instance.Transaction_amount == original



@given(instance=ATM__Transactions_strategy)
def test_atm__transactions_Remaining_balance_setter(instance):
    original = instance.Remaining_balance
    instance.Remaining_balance = original
    assert instance.Remaining_balance == original



@given(instance=ATM__Transactions_strategy)
def test_atm__transactions_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=ATM__Transactions_strategy)
def test_atm__transactions_Transaction_id_setter(instance):
    original = instance.Transaction_id
    instance.Transaction_id = original
    assert instance.Transaction_id == original

@given(instance=ATM_strategy)
@settings(max_examples=50)
def test_atm_instantiation(instance):
    assert isinstance(instance, ATM)



@given(instance=ATM_strategy)
def test_atm_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=ATM_strategy)
def test_atm_ManagedBy_setter(instance):
    original = instance.ManagedBy
    instance.ManagedBy = original
    assert instance.ManagedBy == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original



@given(instance=Account_strategy)
def test_account_AccountNumber_setter(instance):
    original = instance.AccountNumber
    instance.AccountNumber = original
    assert instance.AccountNumber == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_Card_number_setter(instance):
    original = instance.Card_number
    instance.Card_number = original
    assert instance.Card_number == original



@given(instance=Customer_strategy)
def test_customer_Pin_setter(instance):
    original = instance.Pin
    instance.Pin = original
    assert instance.Pin == original



@given(instance=Customer_strategy)
def test_customer_Date_of_birth_setter(instance):
    original = instance.Date_of_birth
    instance.Date_of_birth = original
    assert instance.Date_of_birth == original



@given(instance=Customer_strategy)
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=BANK_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, BANK)



@given(instance=BANK_strategy)
def test_bank_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original



@given(instance=BANK_strategy)
def test_bank_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original
