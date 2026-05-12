import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CertificatesOfDepositAccount,
    TransferTransaction,
    WithdrawTransaction,
    DepositTransaction,
    Login,
    SavingsAccount,
    CheckingAccount,
    Transaction,
    Account,
    Customer,
    TransactionType,
    AccountType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_certificatesofdepositaccount_is_not_abstract():
    assert not inspect.isabstract(CertificatesOfDepositAccount)


def test_certificatesofdepositaccount_constructor_exists():
    assert callable(CertificatesOfDepositAccount.__init__)


def test_certificatesofdepositaccount_constructor_args():
    sig = inspect.signature(CertificatesOfDepositAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "timePeriod" in params, "Missing parameter 'timePeriod'"

def test_certificatesofdepositaccount_has_interestRate():
    assert hasattr(CertificatesOfDepositAccount, "interestRate")
    descriptor = None
    for klass in CertificatesOfDepositAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_certificatesofdepositaccount_has_timePeriod():
    assert hasattr(CertificatesOfDepositAccount, "timePeriod")
    descriptor = None
    for klass in CertificatesOfDepositAccount.__mro__:
        if "timePeriod" in klass.__dict__:
            descriptor = klass.__dict__["timePeriod"]
            break
    assert isinstance(descriptor, property)



def test_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(TransferTransaction)


def test_transfertransaction_constructor_exists():
    assert callable(TransferTransaction.__init__)


def test_transfertransaction_constructor_args():
    sig = inspect.signature(TransferTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"

def test_transfertransaction_has_sourceAccount():
    assert hasattr(TransferTransaction, "sourceAccount")
    descriptor = None
    for klass in TransferTransaction.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
            break
    assert isinstance(descriptor, property)

def test_transfertransaction_has_targetAccount():
    assert hasattr(TransferTransaction, "targetAccount")
    descriptor = None
    for klass in TransferTransaction.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
            break
    assert isinstance(descriptor, property)



def test_withdrawtransaction_is_not_abstract():
    assert not inspect.isabstract(WithdrawTransaction)


def test_withdrawtransaction_constructor_exists():
    assert callable(WithdrawTransaction.__init__)


def test_withdrawtransaction_constructor_args():
    sig = inspect.signature(WithdrawTransaction.__init__)
    params = list(sig.parameters.keys())



def test_deposittransaction_is_not_abstract():
    assert not inspect.isabstract(DepositTransaction)


def test_deposittransaction_constructor_exists():
    assert callable(DepositTransaction.__init__)


def test_deposittransaction_constructor_args():
    sig = inspect.signature(DepositTransaction.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "securityQuestion" in params, "Missing parameter 'securityQuestion'"
    assert "securityAnswer" in params, "Missing parameter 'securityAnswer'"
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"
    assert "password" in params, "Missing parameter 'password'"

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
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

def test_login_has_lastLoginTime():
    assert hasattr(Login, "lastLoginTime")
    descriptor = None
    for klass in Login.__mro__:
        if "lastLoginTime" in klass.__dict__:
            descriptor = klass.__dict__["lastLoginTime"]
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



def test_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(SavingsAccount)


def test_savingsaccount_constructor_exists():
    assert callable(SavingsAccount.__init__)


def test_savingsaccount_constructor_args():
    sig = inspect.signature(SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_savingsaccount_has_interestRate():
    assert hasattr(SavingsAccount, "interestRate")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(CheckingAccount)


def test_checkingaccount_constructor_exists():
    assert callable(CheckingAccount.__init__)


def test_checkingaccount_constructor_args():
    sig = inspect.signature(CheckingAccount.__init__)
    params = list(sig.parameters.keys())



def test_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "type" in params, "Missing parameter 'type'"
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"

def test_transaction_has_id():
    assert hasattr(Transaction, "id")
    descriptor = None
    for klass in Transaction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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

def test_transaction_has_type():
    assert hasattr(Transaction, "type")
    descriptor = None
    for klass in Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_transactionTime():
    assert hasattr(Transaction, "transactionTime")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionTime" in klass.__dict__:
            descriptor = klass.__dict__["transactionTime"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "balance" in params, "Missing parameter 'balance'"
    assert "type" in params, "Missing parameter 'type'"

def test_account_has_accountNo():
    assert hasattr(Account, "accountNo")
    descriptor = None
    for klass in Account.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
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

def test_account_has_type():
    assert hasattr(Account, "type")
    descriptor = None
    for klass in Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"

def test_customer_has_dateOfBirth():
    assert hasattr(Customer, "dateOfBirth")
    descriptor = None
    for klass in Customer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
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

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_customer_has_phoneNumber():
    assert hasattr(Customer, "phoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
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

def test_accounttype_exists():
    # Check that the Enumeration exists
    assert AccountType is not None

def test_accounttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccountType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccountType"


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
CertificatesOfDepositAccount_strategy = st.builds(
    CertificatesOfDepositAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    timePeriod=
        st.integers()
)
TransferTransaction_strategy = st.builds(
    TransferTransaction,
    sourceAccount=
        st.none(),
    targetAccount=
        st.none()
)
WithdrawTransaction_strategy = st.builds(
    WithdrawTransaction,
)
DepositTransaction_strategy = st.builds(
    DepositTransaction,
)
Login_strategy = st.builds(
    Login,
    username=
        safe_text,
    securityQuestion=
        safe_text,
    securityAnswer=
        safe_text,
    lastLoginTime=
        st.dates(),
    password=
        safe_text
)
SavingsAccount_strategy = st.builds(
    SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CheckingAccount_strategy = st.builds(
    CheckingAccount,
)
Transaction_strategy = st.builds(
    Transaction,
    id=
        st.integers(),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none(),
    transactionTime=
        st.dates()
)
Account_strategy = st.builds(
    Account,
    accountNo=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none()
)
Customer_strategy = st.builds(
    Customer,
    dateOfBirth=
        st.dates(),
    address=
        safe_text,
    name=
        safe_text,
    emailAddress=
        safe_text,
    phoneNumber=
        safe_text
)

@given(instance=CertificatesOfDepositAccount_strategy)
@settings(max_examples=50)
def test_certificatesofdepositaccount_instantiation(instance):
    assert isinstance(instance, CertificatesOfDepositAccount)



@given(instance=CertificatesOfDepositAccount_strategy)
def test_certificatesofdepositaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=CertificatesOfDepositAccount_strategy)
def test_certificatesofdepositaccount_timePeriod_setter(instance):
    original = instance.timePeriod
    instance.timePeriod = original
    assert instance.timePeriod == original

@given(instance=TransferTransaction_strategy)
@settings(max_examples=50)
def test_transfertransaction_instantiation(instance):
    assert isinstance(instance, TransferTransaction)



@given(instance=TransferTransaction_strategy)
def test_transfertransaction_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original



@given(instance=TransferTransaction_strategy)
def test_transfertransaction_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original

@given(instance=WithdrawTransaction_strategy)
@settings(max_examples=50)
def test_withdrawtransaction_instantiation(instance):
    assert isinstance(instance, WithdrawTransaction)

@given(instance=DepositTransaction_strategy)
@settings(max_examples=50)
def test_deposittransaction_instantiation(instance):
    assert isinstance(instance, DepositTransaction)

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
def test_login_securityQuestion_setter(instance):
    original = instance.securityQuestion
    instance.securityQuestion = original
    assert instance.securityQuestion == original



@given(instance=Login_strategy)
def test_login_securityAnswer_setter(instance):
    original = instance.securityAnswer
    instance.securityAnswer = original
    assert instance.securityAnswer == original



@given(instance=Login_strategy)
def test_login_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=SavingsAccount_strategy)
@settings(max_examples=50)
def test_savingsaccount_instantiation(instance):
    assert isinstance(instance, SavingsAccount)



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=CheckingAccount_strategy)
@settings(max_examples=50)
def test_checkingaccount_instantiation(instance):
    assert isinstance(instance, CheckingAccount)

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



@given(instance=Transaction_strategy)
def test_transaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Transaction_strategy)
def test_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction_strategy)
def test_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Transaction_strategy)
def test_transaction_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=Account_strategy)
def test_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Account_strategy)
def test_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

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
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_customer_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original
