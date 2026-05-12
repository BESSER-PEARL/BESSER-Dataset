import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CheckingAccount,
    SavingAccount,
    CoDTransaction,
    CheckTransaction,
    Transaction,
    Account,
    Customer,
    Bank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(CheckingAccount)


def test_checkingaccount_constructor_exists():
    assert callable(CheckingAccount.__init__)


def test_checkingaccount_constructor_args():
    sig = inspect.signature(CheckingAccount.__init__)
    params = list(sig.parameters.keys())



def test_savingaccount_is_not_abstract():
    assert not inspect.isabstract(SavingAccount)


def test_savingaccount_constructor_exists():
    assert callable(SavingAccount.__init__)


def test_savingaccount_constructor_args():
    sig = inspect.signature(SavingAccount.__init__)
    params = list(sig.parameters.keys())



def test_codtransaction_is_not_abstract():
    assert not inspect.isabstract(CoDTransaction)


def test_codtransaction_constructor_exists():
    assert callable(CoDTransaction.__init__)


def test_codtransaction_constructor_args():
    sig = inspect.signature(CoDTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_codtransaction_has_startDate():
    assert hasattr(CoDTransaction, "startDate")
    descriptor = None
    for klass in CoDTransaction.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_codtransaction_has_endDate():
    assert hasattr(CoDTransaction, "endDate")
    descriptor = None
    for klass in CoDTransaction.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_codtransaction_has_interestRate():
    assert hasattr(CoDTransaction, "interestRate")
    descriptor = None
    for klass in CoDTransaction.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_checktransaction_is_not_abstract():
    assert not inspect.isabstract(CheckTransaction)


def test_checktransaction_constructor_exists():
    assert callable(CheckTransaction.__init__)


def test_checktransaction_constructor_args():
    sig = inspect.signature(CheckTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "memo" in params, "Missing parameter 'memo'"

def test_checktransaction_has_memo():
    assert hasattr(CheckTransaction, "memo")
    descriptor = None
    for klass in CheckTransaction.__mro__:
        if "memo" in klass.__dict__:
            descriptor = klass.__dict__["memo"]
            break
    assert isinstance(descriptor, property)



def test_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "transactionDate" in params, "Missing parameter 'transactionDate'"
    assert "transactionAmount" in params, "Missing parameter 'transactionAmount'"
    assert "transactionType" in params, "Missing parameter 'transactionType'"
    assert "holder" in params, "Missing parameter 'holder'"

def test_transaction_has_transactionDate():
    assert hasattr(Transaction, "transactionDate")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionDate" in klass.__dict__:
            descriptor = klass.__dict__["transactionDate"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_transactionAmount():
    assert hasattr(Transaction, "transactionAmount")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionAmount" in klass.__dict__:
            descriptor = klass.__dict__["transactionAmount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_transactionType():
    assert hasattr(Transaction, "transactionType")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionType" in klass.__dict__:
            descriptor = klass.__dict__["transactionType"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_holder():
    assert hasattr(Transaction, "holder")
    descriptor = None
    for klass in Transaction.__mro__:
        if "holder" in klass.__dict__:
            descriptor = klass.__dict__["holder"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "accId" in params, "Missing parameter 'accId'"
    assert "accNumber" in params, "Missing parameter 'accNumber'"
    assert "openDate" in params, "Missing parameter 'openDate'"
    assert "MAX_HOLDERS" in params, "Missing parameter 'MAX_HOLDERS'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_account_has_accId():
    assert hasattr(Account, "accId")
    descriptor = None
    for klass in Account.__mro__:
        if "accId" in klass.__dict__:
            descriptor = klass.__dict__["accId"]
            break
    assert isinstance(descriptor, property)

def test_account_has_accNumber():
    assert hasattr(Account, "accNumber")
    descriptor = None
    for klass in Account.__mro__:
        if "accNumber" in klass.__dict__:
            descriptor = klass.__dict__["accNumber"]
            break
    assert isinstance(descriptor, property)

def test_account_has_openDate():
    assert hasattr(Account, "openDate")
    descriptor = None
    for klass in Account.__mro__:
        if "openDate" in klass.__dict__:
            descriptor = klass.__dict__["openDate"]
            break
    assert isinstance(descriptor, property)

def test_account_has_MAX_HOLDERS():
    assert hasattr(Account, "MAX_HOLDERS")
    descriptor = None
    for klass in Account.__mro__:
        if "MAX_HOLDERS" in klass.__dict__:
            descriptor = klass.__dict__["MAX_HOLDERS"]
            break
    assert isinstance(descriptor, property)

def test_account_has_balance():
    assert hasattr(Account, "balance")
    descriptor = None
    for klass in Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "taxId" in params, "Missing parameter 'taxId'"
    assert "name" in params, "Missing parameter 'name'"

def test_customer_has_taxId():
    assert hasattr(Customer, "taxId")
    descriptor = None
    for klass in Customer.__mro__:
        if "taxId" in klass.__dict__:
            descriptor = klass.__dict__["taxId"]
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
CheckingAccount_strategy = st.builds(
    CheckingAccount,
)
SavingAccount_strategy = st.builds(
    SavingAccount,
)
CoDTransaction_strategy = st.builds(
    CoDTransaction,
    startDate=
        safe_text,
    endDate=
        safe_text,
    interestRate=
        safe_text
)
CheckTransaction_strategy = st.builds(
    CheckTransaction,
    memo=
        safe_text
)
Transaction_strategy = st.builds(
    Transaction,
    transactionDate=
        safe_text,
    transactionAmount=
        safe_text,
    transactionType=
        safe_text,
    holder=
        st.none()
)
Account_strategy = st.builds(
    Account,
    accId=
        safe_text,
    accNumber=
        safe_text,
    openDate=
        safe_text,
    MAX_HOLDERS=
        safe_text,
    balance=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    taxId=
        safe_text,
    name=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
)

@given(instance=CheckingAccount_strategy)
@settings(max_examples=50)
def test_checkingaccount_instantiation(instance):
    assert isinstance(instance, CheckingAccount)

@given(instance=SavingAccount_strategy)
@settings(max_examples=50)
def test_savingaccount_instantiation(instance):
    assert isinstance(instance, SavingAccount)

@given(instance=CoDTransaction_strategy)
@settings(max_examples=50)
def test_codtransaction_instantiation(instance):
    assert isinstance(instance, CoDTransaction)



@given(instance=CoDTransaction_strategy)
def test_codtransaction_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=CoDTransaction_strategy)
def test_codtransaction_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original



@given(instance=CoDTransaction_strategy)
def test_codtransaction_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=CheckTransaction_strategy)
@settings(max_examples=50)
def test_checktransaction_instantiation(instance):
    assert isinstance(instance, CheckTransaction)



@given(instance=CheckTransaction_strategy)
def test_checktransaction_memo_setter(instance):
    original = instance.memo
    instance.memo = original
    assert instance.memo == original

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



@given(instance=Transaction_strategy)
def test_transaction_transactionDate_setter(instance):
    original = instance.transactionDate
    instance.transactionDate = original
    assert instance.transactionDate == original



@given(instance=Transaction_strategy)
def test_transaction_transactionAmount_setter(instance):
    original = instance.transactionAmount
    instance.transactionAmount = original
    assert instance.transactionAmount == original



@given(instance=Transaction_strategy)
def test_transaction_transactionType_setter(instance):
    original = instance.transactionType
    instance.transactionType = original
    assert instance.transactionType == original



@given(instance=Transaction_strategy)
def test_transaction_holder_setter(instance):
    original = instance.holder
    instance.holder = original
    assert instance.holder == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_accId_setter(instance):
    original = instance.accId
    instance.accId = original
    assert instance.accId == original



@given(instance=Account_strategy)
def test_account_accNumber_setter(instance):
    original = instance.accNumber
    instance.accNumber = original
    assert instance.accNumber == original



@given(instance=Account_strategy)
def test_account_openDate_setter(instance):
    original = instance.openDate
    instance.openDate = original
    assert instance.openDate == original



@given(instance=Account_strategy)
def test_account_MAX_HOLDERS_setter(instance):
    original = instance.MAX_HOLDERS
    instance.MAX_HOLDERS = original
    assert instance.MAX_HOLDERS == original



@given(instance=Account_strategy)
def test_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_taxId_setter(instance):
    original = instance.taxId
    instance.taxId = original
    assert instance.taxId == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)
