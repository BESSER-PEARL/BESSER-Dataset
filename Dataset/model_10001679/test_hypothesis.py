import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SavingAccount,
    CurrentAccount,
    ATMTransactions,
    ATM,
    Account,
    Customer,
    Bank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_savingaccount_is_not_abstract():
    assert not inspect.isabstract(SavingAccount)


def test_savingaccount_constructor_exists():
    assert callable(SavingAccount.__init__)


def test_savingaccount_constructor_args():
    sig = inspect.signature(SavingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "accountNo" in params, "Missing parameter 'accountNo'"

def test_savingaccount_has_balance():
    assert hasattr(SavingAccount, "balance")
    descriptor = None
    for klass in SavingAccount.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_savingaccount_has_accountNo():
    assert hasattr(SavingAccount, "accountNo")
    descriptor = None
    for klass in SavingAccount.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)



def test_currentaccount_is_not_abstract():
    assert not inspect.isabstract(CurrentAccount)


def test_currentaccount_constructor_exists():
    assert callable(CurrentAccount.__init__)


def test_currentaccount_constructor_args():
    sig = inspect.signature(CurrentAccount.__init__)
    params = list(sig.parameters.keys())
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_currentaccount_has_accountNo():
    assert hasattr(CurrentAccount, "accountNo")
    descriptor = None
    for klass in CurrentAccount.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)

def test_currentaccount_has_balance():
    assert hasattr(CurrentAccount, "balance")
    descriptor = None
    for klass in CurrentAccount.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_atmtransactions_is_not_abstract():
    assert not inspect.isabstract(ATMTransactions)


def test_atmtransactions_constructor_exists():
    assert callable(ATMTransactions.__init__)


def test_atmtransactions_constructor_args():
    sig = inspect.signature(ATMTransactions.__init__)
    params = list(sig.parameters.keys())
    assert "transactionid" in params, "Missing parameter 'transactionid'"
    assert "date" in params, "Missing parameter 'date'"
    assert "type" in params, "Missing parameter 'type'"
    assert "postBalance" in params, "Missing parameter 'postBalance'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_atmtransactions_has_transactionid():
    assert hasattr(ATMTransactions, "transactionid")
    descriptor = None
    for klass in ATMTransactions.__mro__:
        if "transactionid" in klass.__dict__:
            descriptor = klass.__dict__["transactionid"]
            break
    assert isinstance(descriptor, property)

def test_atmtransactions_has_date():
    assert hasattr(ATMTransactions, "date")
    descriptor = None
    for klass in ATMTransactions.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_atmtransactions_has_type():
    assert hasattr(ATMTransactions, "type")
    descriptor = None
    for klass in ATMTransactions.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_atmtransactions_has_postBalance():
    assert hasattr(ATMTransactions, "postBalance")
    descriptor = None
    for klass in ATMTransactions.__mro__:
        if "postBalance" in klass.__dict__:
            descriptor = klass.__dict__["postBalance"]
            break
    assert isinstance(descriptor, property)

def test_atmtransactions_has_amount():
    assert hasattr(ATMTransactions, "amount")
    descriptor = None
    for klass in ATMTransactions.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_atm_is_not_abstract():
    assert not inspect.isabstract(ATM)


def test_atm_constructor_exists():
    assert callable(ATM.__init__)


def test_atm_constructor_args():
    sig = inspect.signature(ATM.__init__)
    params = list(sig.parameters.keys())
    assert "managedBy" in params, "Missing parameter 'managedBy'"
    assert "location" in params, "Missing parameter 'location'"

def test_atm_has_managedBy():
    assert hasattr(ATM, "managedBy")
    descriptor = None
    for klass in ATM.__mro__:
        if "managedBy" in klass.__dict__:
            descriptor = klass.__dict__["managedBy"]
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
    assert "balance" in params, "Missing parameter 'balance'"
    assert "number" in params, "Missing parameter 'number'"

def test_account_has_balance():
    assert hasattr(Account, "balance")
    descriptor = None
    for klass in Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_account_has_number():
    assert hasattr(Account, "number")
    descriptor = None
    for klass in Account.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "cardno" in params, "Missing parameter 'cardno'"
    assert "dob" in params, "Missing parameter 'dob'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_cardno():
    assert hasattr(Customer, "cardno")
    descriptor = None
    for klass in Customer.__mro__:
        if "cardno" in klass.__dict__:
            descriptor = klass.__dict__["cardno"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_dob():
    assert hasattr(Customer, "dob")
    descriptor = None
    for klass in Customer.__mro__:
        if "dob" in klass.__dict__:
            descriptor = klass.__dict__["dob"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_pin():
    assert hasattr(Customer, "pin")
    descriptor = None
    for klass in Customer.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "code" in params, "Missing parameter 'code'"

def test_bank_has_address():
    assert hasattr(Bank, "address")
    descriptor = None
    for klass in Bank.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_code():
    assert hasattr(Bank, "code")
    descriptor = None
    for klass in Bank.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
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
SavingAccount_strategy = st.builds(
    SavingAccount,
    balance=
        st.integers(),
    accountNo=
        st.integers()
)
CurrentAccount_strategy = st.builds(
    CurrentAccount,
    accountNo=
        st.integers(),
    balance=
        st.integers()
)
ATMTransactions_strategy = st.builds(
    ATMTransactions,
    transactionid=
        st.integers(),
    date=
        safe_text,
    type=
        safe_text,
    postBalance=
        st.integers(),
    amount=
        st.integers()
)
ATM_strategy = st.builds(
    ATM,
    managedBy=
        safe_text,
    location=
        safe_text
)
Account_strategy = st.builds(
    Account,
    balance=
        st.integers(),
    number=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    address=
        safe_text,
    cardno=
        st.integers(),
    dob=
        safe_text,
    pin=
        st.integers(),
    name=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    address=
        safe_text,
    code=
        st.integers()
)

@given(instance=SavingAccount_strategy)
@settings(max_examples=50)
def test_savingaccount_instantiation(instance):
    assert isinstance(instance, SavingAccount)



@given(instance=SavingAccount_strategy)
def test_savingaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=SavingAccount_strategy)
def test_savingaccount_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original

@given(instance=CurrentAccount_strategy)
@settings(max_examples=50)
def test_currentaccount_instantiation(instance):
    assert isinstance(instance, CurrentAccount)



@given(instance=CurrentAccount_strategy)
def test_currentaccount_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=CurrentAccount_strategy)
def test_currentaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=ATMTransactions_strategy)
@settings(max_examples=50)
def test_atmtransactions_instantiation(instance):
    assert isinstance(instance, ATMTransactions)



@given(instance=ATMTransactions_strategy)
def test_atmtransactions_transactionid_setter(instance):
    original = instance.transactionid
    instance.transactionid = original
    assert instance.transactionid == original



@given(instance=ATMTransactions_strategy)
def test_atmtransactions_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=ATMTransactions_strategy)
def test_atmtransactions_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ATMTransactions_strategy)
def test_atmtransactions_postBalance_setter(instance):
    original = instance.postBalance
    instance.postBalance = original
    assert instance.postBalance == original



@given(instance=ATMTransactions_strategy)
def test_atmtransactions_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=ATM_strategy)
@settings(max_examples=50)
def test_atm_instantiation(instance):
    assert isinstance(instance, ATM)



@given(instance=ATM_strategy)
def test_atm_managedBy_setter(instance):
    original = instance.managedBy
    instance.managedBy = original
    assert instance.managedBy == original



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
def test_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Account_strategy)
def test_account_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_cardno_setter(instance):
    original = instance.cardno
    instance.cardno = original
    assert instance.cardno == original



@given(instance=Customer_strategy)
def test_customer_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original



@given(instance=Customer_strategy)
def test_customer_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Bank_strategy)
def test_bank_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original
