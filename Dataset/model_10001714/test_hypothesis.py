import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IcalculateExtraFee_Interface,
    savingAccount,
    checkingAccount,
    Transaction,
    Customer,
    Account,
    TransactionType,
    EnumAccountType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_icalculateextrafee_interface_is_not_abstract():
    assert not inspect.isabstract(IcalculateExtraFee_Interface)


def test_icalculateextrafee_interface_constructor_exists():
    assert callable(IcalculateExtraFee_Interface.__init__)


def test_icalculateextrafee_interface_constructor_args():
    sig = inspect.signature(IcalculateExtraFee_Interface.__init__)
    params = list(sig.parameters.keys())



def test_savingaccount_is_not_abstract():
    assert not inspect.isabstract(savingAccount)


def test_savingaccount_constructor_exists():
    assert callable(savingAccount.__init__)


def test_savingaccount_constructor_args():
    sig = inspect.signature(savingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "annualInterestRate" in params, "Missing parameter 'annualInterestRate'"
    assert "extraFee" in params, "Missing parameter 'extraFee'"
    assert "annualGain" in params, "Missing parameter 'annualGain'"

def test_savingaccount_has_annualInterestRate():
    assert hasattr(savingAccount, "annualInterestRate")
    descriptor = None
    for klass in savingAccount.__mro__:
        if "annualInterestRate" in klass.__dict__:
            descriptor = klass.__dict__["annualInterestRate"]
            break
    assert isinstance(descriptor, property)

def test_savingaccount_has_extraFee():
    assert hasattr(savingAccount, "extraFee")
    descriptor = None
    for klass in savingAccount.__mro__:
        if "extraFee" in klass.__dict__:
            descriptor = klass.__dict__["extraFee"]
            break
    assert isinstance(descriptor, property)

def test_savingaccount_has_annualGain():
    assert hasattr(savingAccount, "annualGain")
    descriptor = None
    for klass in savingAccount.__mro__:
        if "annualGain" in klass.__dict__:
            descriptor = klass.__dict__["annualGain"]
            break
    assert isinstance(descriptor, property)



def test_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(checkingAccount)


def test_checkingaccount_constructor_exists():
    assert callable(checkingAccount.__init__)


def test_checkingaccount_constructor_args():
    sig = inspect.signature(checkingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "noOfTransactions" in params, "Missing parameter 'noOfTransactions'"

def test_checkingaccount_has_accountNo():
    assert hasattr(checkingAccount, "accountNo")
    descriptor = None
    for klass in checkingAccount.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_noOfTransactions():
    assert hasattr(checkingAccount, "noOfTransactions")
    descriptor = None
    for klass in checkingAccount.__mro__:
        if "noOfTransactions" in klass.__dict__:
            descriptor = klass.__dict__["noOfTransactions"]
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
    assert "amount" in params, "Missing parameter 'amount'"
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "transactionType" in params, "Missing parameter 'transactionType'"
    assert "transactionId" in params, "Missing parameter 'transactionId'"
    assert "description" in params, "Missing parameter 'description'"

def test_transaction_has_transactionDate():
    assert hasattr(Transaction, "transactionDate")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionDate" in klass.__dict__:
            descriptor = klass.__dict__["transactionDate"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_amount():
    assert hasattr(Transaction, "amount")
    descriptor = None
    for klass in Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_accountNo():
    assert hasattr(Transaction, "accountNo")
    descriptor = None
    for klass in Transaction.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
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

def test_transaction_has_transactionId():
    assert hasattr(Transaction, "transactionId")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionId" in klass.__dict__:
            descriptor = klass.__dict__["transactionId"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_description():
    assert hasattr(Transaction, "description")
    descriptor = None
    for klass in Transaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "address" in params, "Missing parameter 'address'"
    assert "custId" in params, "Missing parameter 'custId'"

def test_customer_has_accountNo():
    assert hasattr(Customer, "accountNo")
    descriptor = None
    for klass in Customer.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_lastName():
    assert hasattr(Customer, "lastName")
    descriptor = None
    for klass in Customer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_firstName():
    assert hasattr(Customer, "firstName")
    descriptor = None
    for klass in Customer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_address():
    assert hasattr(Customer, "address")
    descriptor = None
    for klass in Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_custId():
    assert hasattr(Customer, "custId")
    descriptor = None
    for klass in Customer.__mro__:
        if "custId" in klass.__dict__:
            descriptor = klass.__dict__["custId"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "accountType" in params, "Missing parameter 'accountType'"
    assert "PIN" in params, "Missing parameter 'PIN'"
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "availableBalance" in params, "Missing parameter 'availableBalance'"
    assert "openedDate" in params, "Missing parameter 'openedDate'"

def test_account_has_accountType():
    assert hasattr(Account, "accountType")
    descriptor = None
    for klass in Account.__mro__:
        if "accountType" in klass.__dict__:
            descriptor = klass.__dict__["accountType"]
            break
    assert isinstance(descriptor, property)

def test_account_has_PIN():
    assert hasattr(Account, "PIN")
    descriptor = None
    for klass in Account.__mro__:
        if "PIN" in klass.__dict__:
            descriptor = klass.__dict__["PIN"]
            break
    assert isinstance(descriptor, property)

def test_account_has_accountNo():
    assert hasattr(Account, "accountNo")
    descriptor = None
    for klass in Account.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)

def test_account_has_availableBalance():
    assert hasattr(Account, "availableBalance")
    descriptor = None
    for klass in Account.__mro__:
        if "availableBalance" in klass.__dict__:
            descriptor = klass.__dict__["availableBalance"]
            break
    assert isinstance(descriptor, property)

def test_account_has_openedDate():
    assert hasattr(Account, "openedDate")
    descriptor = None
    for klass in Account.__mro__:
        if "openedDate" in klass.__dict__:
            descriptor = klass.__dict__["openedDate"]
            break
    assert isinstance(descriptor, property)

def test_transactiontype_exists():
    # Check that the Enumeration exists
    assert TransactionType is not None

def test_transactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransactionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransactionType"

def test_enumaccounttype_exists():
    # Check that the Enumeration exists
    assert EnumAccountType is not None

def test_enumaccounttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumAccountType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumAccountType"


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
IcalculateExtraFee_Interface_strategy = st.builds(
    IcalculateExtraFee_Interface,
)
savingAccount_strategy = st.builds(
    savingAccount,
    annualInterestRate=
        safe_text,
    extraFee=
        safe_text,
    annualGain=
        safe_text
)
checkingAccount_strategy = st.builds(
    checkingAccount,
    accountNo=
        st.integers(),
    noOfTransactions=
        st.integers()
)
Transaction_strategy = st.builds(
    Transaction,
    transactionDate=
        safe_text,
    amount=
        safe_text,
    accountNo=
        st.integers(),
    transactionType=
        st.none(),
    transactionId=
        st.integers(),
    description=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    accountNo=
        st.integers(),
    lastName=
        safe_text,
    firstName=
        safe_text,
    address=
        safe_text,
    custId=
        st.integers()
)
Account_strategy = st.builds(
    Account,
    accountType=
        st.none(),
    PIN=
        st.integers(),
    accountNo=
        st.integers(),
    availableBalance=
        safe_text,
    openedDate=
        safe_text
)

@given(instance=IcalculateExtraFee_Interface_strategy)
@settings(max_examples=50)
def test_icalculateextrafee_interface_instantiation(instance):
    assert isinstance(instance, IcalculateExtraFee_Interface)

@given(instance=savingAccount_strategy)
@settings(max_examples=50)
def test_savingaccount_instantiation(instance):
    assert isinstance(instance, savingAccount)



@given(instance=savingAccount_strategy)
def test_savingaccount_annualInterestRate_setter(instance):
    original = instance.annualInterestRate
    instance.annualInterestRate = original
    assert instance.annualInterestRate == original



@given(instance=savingAccount_strategy)
def test_savingaccount_extraFee_setter(instance):
    original = instance.extraFee
    instance.extraFee = original
    assert instance.extraFee == original



@given(instance=savingAccount_strategy)
def test_savingaccount_annualGain_setter(instance):
    original = instance.annualGain
    instance.annualGain = original
    assert instance.annualGain == original

@given(instance=checkingAccount_strategy)
@settings(max_examples=50)
def test_checkingaccount_instantiation(instance):
    assert isinstance(instance, checkingAccount)



@given(instance=checkingAccount_strategy)
def test_checkingaccount_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=checkingAccount_strategy)
def test_checkingaccount_noOfTransactions_setter(instance):
    original = instance.noOfTransactions
    instance.noOfTransactions = original
    assert instance.noOfTransactions == original

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
def test_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction_strategy)
def test_transaction_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=Transaction_strategy)
def test_transaction_transactionType_setter(instance):
    original = instance.transactionType
    instance.transactionType = original
    assert instance.transactionType == original



@given(instance=Transaction_strategy)
def test_transaction_transactionId_setter(instance):
    original = instance.transactionId
    instance.transactionId = original
    assert instance.transactionId == original



@given(instance=Transaction_strategy)
def test_transaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=Customer_strategy)
def test_customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=Customer_strategy)
def test_customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_custId_setter(instance):
    original = instance.custId
    instance.custId = original
    assert instance.custId == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_accountType_setter(instance):
    original = instance.accountType
    instance.accountType = original
    assert instance.accountType == original



@given(instance=Account_strategy)
def test_account_PIN_setter(instance):
    original = instance.PIN
    instance.PIN = original
    assert instance.PIN == original



@given(instance=Account_strategy)
def test_account_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=Account_strategy)
def test_account_availableBalance_setter(instance):
    original = instance.availableBalance
    instance.availableBalance = original
    assert instance.availableBalance == original



@given(instance=Account_strategy)
def test_account_openedDate_setter(instance):
    original = instance.openedDate
    instance.openedDate = original
    assert instance.openedDate == original
