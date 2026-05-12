import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    account_Account,
    account_CheckingAccount,
    account_CertificatesOfDepositAccount,
    account_SavingsAccount,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
    transaction_DepositTransaction,
    transaction_Transaction,
    Login,
    Customer,
    account_AccountType,
    transaction_TransactionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_account_account_is_not_abstract():
    assert not inspect.isabstract(account_Account)


def test_account_account_constructor_exists():
    assert callable(account_Account.__init__)


def test_account_account_constructor_args():
    sig = inspect.signature(account_Account.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_account_account_has_type():
    assert hasattr(account_Account, "type")
    descriptor = None
    for klass in account_Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_accountNo():
    assert hasattr(account_Account, "accountNo")
    descriptor = None
    for klass in account_Account.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_balance():
    assert hasattr(account_Account, "balance")
    descriptor = None
    for klass in account_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_account_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(account_CheckingAccount)


def test_account_checkingaccount_constructor_exists():
    assert callable(account_CheckingAccount.__init__)


def test_account_checkingaccount_constructor_args():
    sig = inspect.signature(account_CheckingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_account_checkingaccount_has_name():
    assert hasattr(account_CheckingAccount, "name")
    descriptor = None
    for klass in account_CheckingAccount.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_account_certificatesofdepositaccount_is_not_abstract():
    assert not inspect.isabstract(account_CertificatesOfDepositAccount)


def test_account_certificatesofdepositaccount_constructor_exists():
    assert callable(account_CertificatesOfDepositAccount.__init__)


def test_account_certificatesofdepositaccount_constructor_args():
    sig = inspect.signature(account_CertificatesOfDepositAccount.__init__)
    params = list(sig.parameters.keys())
    assert "timePeriod" in params, "Missing parameter 'timePeriod'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_account_certificatesofdepositaccount_has_timePeriod():
    assert hasattr(account_CertificatesOfDepositAccount, "timePeriod")
    descriptor = None
    for klass in account_CertificatesOfDepositAccount.__mro__:
        if "timePeriod" in klass.__dict__:
            descriptor = klass.__dict__["timePeriod"]
            break
    assert isinstance(descriptor, property)

def test_account_certificatesofdepositaccount_has_interestRate():
    assert hasattr(account_CertificatesOfDepositAccount, "interestRate")
    descriptor = None
    for klass in account_CertificatesOfDepositAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_account_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(account_SavingsAccount)


def test_account_savingsaccount_constructor_exists():
    assert callable(account_SavingsAccount.__init__)


def test_account_savingsaccount_constructor_args():
    sig = inspect.signature(account_SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_account_savingsaccount_has_interestRate():
    assert hasattr(account_SavingsAccount, "interestRate")
    descriptor = None
    for klass in account_SavingsAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_transaction_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_TransferTransaction)


def test_transaction_transfertransaction_constructor_exists():
    assert callable(transaction_TransferTransaction.__init__)


def test_transaction_transfertransaction_constructor_args():
    sig = inspect.signature(transaction_TransferTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"

def test_transaction_transfertransaction_has_targetAccount():
    assert hasattr(transaction_TransferTransaction, "targetAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transfertransaction_has_sourceAccount():
    assert hasattr(transaction_TransferTransaction, "sourceAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
            break
    assert isinstance(descriptor, property)



def test_transaction_withdrawtransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_WithdrawTransaction)


def test_transaction_withdrawtransaction_constructor_exists():
    assert callable(transaction_WithdrawTransaction.__init__)


def test_transaction_withdrawtransaction_constructor_args():
    sig = inspect.signature(transaction_WithdrawTransaction.__init__)
    params = list(sig.parameters.keys())



def test_transaction_deposittransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_DepositTransaction)


def test_transaction_deposittransaction_constructor_exists():
    assert callable(transaction_DepositTransaction.__init__)


def test_transaction_deposittransaction_constructor_args():
    sig = inspect.signature(transaction_DepositTransaction.__init__)
    params = list(sig.parameters.keys())



def test_transaction_transaction_is_not_abstract():
    assert not inspect.isabstract(transaction_Transaction)


def test_transaction_transaction_constructor_exists():
    assert callable(transaction_Transaction.__init__)


def test_transaction_transaction_constructor_args():
    sig = inspect.signature(transaction_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"
    assert "type" in params, "Missing parameter 'type'"

def test_transaction_transaction_has_id():
    assert hasattr(transaction_Transaction, "id")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_amount():
    assert hasattr(transaction_Transaction, "amount")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_transactionTime():
    assert hasattr(transaction_Transaction, "transactionTime")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionTime" in klass.__dict__:
            descriptor = klass.__dict__["transactionTime"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_type():
    assert hasattr(transaction_Transaction, "type")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"
    assert "securityQuestion" in params, "Missing parameter 'securityQuestion'"
    assert "securityAnswer" in params, "Missing parameter 'securityAnswer'"

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_lastLoginTime():
    assert hasattr(Login, "lastLoginTime")
    descriptor = None
    for klass in Login.__mro__:
        if "lastLoginTime" in klass.__dict__:
            descriptor = klass.__dict__["lastLoginTime"]
            break
    assert isinstance(descriptor, property)

def test_login_has_securityQuestion():
    assert hasattr(Login, "securityQuestion")
    descriptor = None
    for klass in Login.__mro__:
        if "securityQuestion" in klass.__dict__:
            descriptor = klass.__dict__["securityQuestion"]
            break
    assert isinstance(descriptor, property)

def test_login_has_securityAnswer():
    assert hasattr(Login, "securityAnswer")
    descriptor = None
    for klass in Login.__mro__:
        if "securityAnswer" in klass.__dict__:
            descriptor = klass.__dict__["securityAnswer"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "address" in params, "Missing parameter 'address'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"

def test_customer_has_dateOfBirth():
    assert hasattr(Customer, "dateOfBirth")
    descriptor = None
    for klass in Customer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
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

def test_customer_has_phoneNumber():
    assert hasattr(Customer, "phoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
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

def test_customer_has_emailAddress():
    assert hasattr(Customer, "emailAddress")
    descriptor = None
    for klass in Customer.__mro__:
        if "emailAddress" in klass.__dict__:
            descriptor = klass.__dict__["emailAddress"]
            break
    assert isinstance(descriptor, property)

def test_account_accounttype_exists():
    # Check that the Enumeration exists
    assert account_AccountType is not None

def test_account_accounttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in account_AccountType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in account_AccountType"

def test_transaction_transactiontype_exists():
    # Check that the Enumeration exists
    assert transaction_TransactionType is not None

def test_transaction_transactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in transaction_TransactionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in transaction_TransactionType"


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
account_Account_strategy = st.builds(
    account_Account,
    type=
        st.none(),
    accountNo=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
account_CheckingAccount_strategy = st.builds(
    account_CheckingAccount,
    name=
        safe_text
)
account_CertificatesOfDepositAccount_strategy = st.builds(
    account_CertificatesOfDepositAccount,
    timePeriod=
        st.integers(),
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_TransferTransaction_strategy = st.builds(
    transaction_TransferTransaction,
    targetAccount=
        st.none(),
    sourceAccount=
        st.none()
)
transaction_WithdrawTransaction_strategy = st.builds(
    transaction_WithdrawTransaction,
)
transaction_DepositTransaction_strategy = st.builds(
    transaction_DepositTransaction,
)
transaction_Transaction_strategy = st.builds(
    transaction_Transaction,
    id=
        st.integers(),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    transactionTime=
        st.dates(),
    type=
        st.none()
)
Login_strategy = st.builds(
    Login,
    username=
        safe_text,
    password=
        safe_text,
    lastLoginTime=
        st.dates(),
    securityQuestion=
        safe_text,
    securityAnswer=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    dateOfBirth=
        st.dates(),
    name=
        safe_text,
    phoneNumber=
        safe_text,
    address=
        safe_text,
    emailAddress=
        safe_text
)

@given(instance=account_Account_strategy)
@settings(max_examples=50)
def test_account_account_instantiation(instance):
    assert isinstance(instance, account_Account)



@given(instance=account_Account_strategy)
def test_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=account_Account_strategy)
def test_account_account_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=account_Account_strategy)
def test_account_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=account_CheckingAccount_strategy)
@settings(max_examples=50)
def test_account_checkingaccount_instantiation(instance):
    assert isinstance(instance, account_CheckingAccount)



@given(instance=account_CheckingAccount_strategy)
def test_account_checkingaccount_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=account_CertificatesOfDepositAccount_strategy)
@settings(max_examples=50)
def test_account_certificatesofdepositaccount_instantiation(instance):
    assert isinstance(instance, account_CertificatesOfDepositAccount)



@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_account_certificatesofdepositaccount_timePeriod_setter(instance):
    original = instance.timePeriod
    instance.timePeriod = original
    assert instance.timePeriod == original



@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_account_certificatesofdepositaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=account_SavingsAccount_strategy)
@settings(max_examples=50)
def test_account_savingsaccount_instantiation(instance):
    assert isinstance(instance, account_SavingsAccount)



@given(instance=account_SavingsAccount_strategy)
def test_account_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=transaction_TransferTransaction_strategy)
@settings(max_examples=50)
def test_transaction_transfertransaction_instantiation(instance):
    assert isinstance(instance, transaction_TransferTransaction)



@given(instance=transaction_TransferTransaction_strategy)
def test_transaction_transfertransaction_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original



@given(instance=transaction_TransferTransaction_strategy)
def test_transaction_transfertransaction_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original

@given(instance=transaction_WithdrawTransaction_strategy)
@settings(max_examples=50)
def test_transaction_withdrawtransaction_instantiation(instance):
    assert isinstance(instance, transaction_WithdrawTransaction)

@given(instance=transaction_DepositTransaction_strategy)
@settings(max_examples=50)
def test_transaction_deposittransaction_instantiation(instance):
    assert isinstance(instance, transaction_DepositTransaction)

@given(instance=transaction_Transaction_strategy)
@settings(max_examples=50)
def test_transaction_transaction_instantiation(instance):
    assert isinstance(instance, transaction_Transaction)



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original



@given(instance=Login_strategy)
def test_login_securityQuestion_setter(instance):
    original = instance.securityQuestion
    instance.securityQuestion = original
    assert instance.securityQuestion == original



@given(instance=Login_strategy)
def test_login_securityAnswer_setter(instance):
    original = instance.securityAnswer
    instance.securityAnswer = original
    assert instance.securityAnswer == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original
