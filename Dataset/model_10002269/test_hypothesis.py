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
    assert "Balance" in params, "Missing parameter 'Balance'"
    assert "AccountNumber" in params, "Missing parameter 'AccountNumber'"

def test_savings_account_has_Balance():
    assert hasattr(Savings_Account, "Balance")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "Balance" in klass.__dict__:
            descriptor = klass.__dict__["Balance"]
            break
    assert isinstance(descriptor, property)

def test_savings_account_has_AccountNumber():
    assert hasattr(Savings_Account, "AccountNumber")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "AccountNumber" in klass.__dict__:
            descriptor = klass.__dict__["AccountNumber"]
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
    assert "Transaction_id" in params, "Missing parameter 'Transaction_id'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Post_balance" in params, "Missing parameter 'Post_balance'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_atm__transactions_has_Transaction_id():
    assert hasattr(ATM__Transactions, "Transaction_id")
    descriptor = None
    for klass in ATM__Transactions.__mro__:
        if "Transaction_id" in klass.__dict__:
            descriptor = klass.__dict__["Transaction_id"]
            break
    assert isinstance(descriptor, property)

def test_atm__transactions_has_Date():
    assert hasattr(ATM__Transactions, "Date")
    descriptor = None
    for klass in ATM__Transactions.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_atm__transactions_has_Post_balance():
    assert hasattr(ATM__Transactions, "Post_balance")
    descriptor = None
    for klass in ATM__Transactions.__mro__:
        if "Post_balance" in klass.__dict__:
            descriptor = klass.__dict__["Post_balance"]
            break
    assert isinstance(descriptor, property)

def test_atm__transactions_has_Amount():
    assert hasattr(ATM__Transactions, "Amount")
    descriptor = None
    for klass in ATM__Transactions.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
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



def test_atm_is_not_abstract():
    assert not inspect.isabstract(ATM)


def test_atm_constructor_exists():
    assert callable(ATM.__init__)


def test_atm_constructor_args():
    sig = inspect.signature(ATM.__init__)
    params = list(sig.parameters.keys())
    assert "ManagedBy" in params, "Missing parameter 'ManagedBy'"
    assert "location" in params, "Missing parameter 'location'"

def test_atm_has_ManagedBy():
    assert hasattr(ATM, "ManagedBy")
    descriptor = None
    for klass in ATM.__mro__:
        if "ManagedBy" in klass.__dict__:
            descriptor = klass.__dict__["ManagedBy"]
            break
    assert isinstance(descriptor, property)

def test_atm_has_location():
    assert hasattr(ATM, "location")
    descriptor = None
    for klass in ATM.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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
    assert "Name" in params, "Missing parameter 'Name'"
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "Card_num" in params, "Missing parameter 'Card_num'"
    assert "Pin" in params, "Missing parameter 'Pin'"

def test_customer_has_Name():
    assert hasattr(Customer, "Name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_DOB():
    assert hasattr(Customer, "DOB")
    descriptor = None
    for klass in Customer.__mro__:
        if "DOB" in klass.__dict__:
            descriptor = klass.__dict__["DOB"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Card_num():
    assert hasattr(Customer, "Card_num")
    descriptor = None
    for klass in Customer.__mro__:
        if "Card_num" in klass.__dict__:
            descriptor = klass.__dict__["Card_num"]
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



def test_bank_is_not_abstract():
    assert not inspect.isabstract(BANK)


def test_bank_constructor_exists():
    assert callable(BANK.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(BANK.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Code" in params, "Missing parameter 'Code'"

def test_bank_has_Address():
    assert hasattr(BANK, "Address")
    descriptor = None
    for klass in BANK.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_Code():
    assert hasattr(BANK, "Code")
    descriptor = None
    for klass in BANK.__mro__:
        if "Code" in klass.__dict__:
            descriptor = klass.__dict__["Code"]
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
    Balance=
        safe_text,
    AccountNumber=
        safe_text
)
Current_Account_strategy = st.builds(
    Current_Account,
    Balance=
        safe_text,
    AccountNumber=
        safe_text
)
ATM__Transactions_strategy = st.builds(
    ATM__Transactions,
    Transaction_id=
        safe_text,
    Date=
        safe_text,
    Post_balance=
        safe_text,
    Amount=
        safe_text,
    Type=
        safe_text
)
ATM_strategy = st.builds(
    ATM,
    ManagedBy=
        safe_text,
    location=
        safe_text
)
Account_strategy = st.builds(
    Account,
    Balance=
        safe_text,
    AccountNumber=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    Name=
        safe_text,
    DOB=
        safe_text,
    Card_num=
        st.integers(),
    Pin=
        st.integers()
)
BANK_strategy = st.builds(
    BANK,
    Address=
        safe_text,
    Code=
        safe_text
)

@given(instance=Savings_Account_strategy)
@settings(max_examples=50)
def test_savings_account_instantiation(instance):
    assert isinstance(instance, Savings_Account)



@given(instance=Savings_Account_strategy)
def test_savings_account_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original



@given(instance=Savings_Account_strategy)
def test_savings_account_AccountNumber_setter(instance):
    original = instance.AccountNumber
    instance.AccountNumber = original
    assert instance.AccountNumber == original

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
def test_atm__transactions_Transaction_id_setter(instance):
    original = instance.Transaction_id
    instance.Transaction_id = original
    assert instance.Transaction_id == original



@given(instance=ATM__Transactions_strategy)
def test_atm__transactions_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=ATM__Transactions_strategy)
def test_atm__transactions_Post_balance_setter(instance):
    original = instance.Post_balance
    instance.Post_balance = original
    assert instance.Post_balance == original



@given(instance=ATM__Transactions_strategy)
def test_atm__transactions_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=ATM__Transactions_strategy)
def test_atm__transactions_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=ATM_strategy)
@settings(max_examples=50)
def test_atm_instantiation(instance):
    assert isinstance(instance, ATM)



@given(instance=ATM_strategy)
def test_atm_ManagedBy_setter(instance):
    original = instance.ManagedBy
    instance.ManagedBy = original
    assert instance.ManagedBy == original



@given(instance=ATM_strategy)
def test_atm_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

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
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Customer_strategy)
def test_customer_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=Customer_strategy)
def test_customer_Card_num_setter(instance):
    original = instance.Card_num
    instance.Card_num = original
    assert instance.Card_num == original



@given(instance=Customer_strategy)
def test_customer_Pin_setter(instance):
    original = instance.Pin
    instance.Pin = original
    assert instance.Pin == original

@given(instance=BANK_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, BANK)



@given(instance=BANK_strategy)
def test_bank_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=BANK_strategy)
def test_bank_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original
