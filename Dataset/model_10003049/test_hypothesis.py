import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    account_Account,
    account_SavingsAccount,
    transaction_Payee,
    transaction_ExternalAccount,
    transaction_PaybillsTransaction,
    transaction_TransferTransaction,
    transaction_DepositTransaction,
    transaction_Transaction,
    User,
    Profile,
    UserGroup,
    transaction_TransactionType,
    account_AccountType,
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
    assert "balance" in params, "Missing parameter 'balance'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "type" in params, "Missing parameter 'type'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"

def test_account_account_has_balance():
    assert hasattr(account_Account, "balance")
    descriptor = None
    for klass in account_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_pin():
    assert hasattr(account_Account, "pin")
    descriptor = None
    for klass in account_Account.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_type():
    assert hasattr(account_Account, "type")
    descriptor = None
    for klass in account_Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_userID():
    assert hasattr(account_Account, "userID")
    descriptor = None
    for klass in account_Account.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_account_account_has_accountNum():
    assert hasattr(account_Account, "accountNum")
    descriptor = None
    for klass in account_Account.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
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



def test_transaction_payee_is_not_abstract():
    assert not inspect.isabstract(transaction_Payee)


def test_transaction_payee_constructor_exists():
    assert callable(transaction_Payee.__init__)


def test_transaction_payee_constructor_args():
    sig = inspect.signature(transaction_Payee.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "address1" in params, "Missing parameter 'address1'"
    assert "address2" in params, "Missing parameter 'address2'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "city" in params, "Missing parameter 'city'"
    assert "state" in params, "Missing parameter 'state'"
    assert "phoneNum" in params, "Missing parameter 'phoneNum'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"

def test_transaction_payee_has_country():
    assert hasattr(transaction_Payee, "country")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_accountNum():
    assert hasattr(transaction_Payee, "accountNum")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_address1():
    assert hasattr(transaction_Payee, "address1")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "address1" in klass.__dict__:
            descriptor = klass.__dict__["address1"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_address2():
    assert hasattr(transaction_Payee, "address2")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "address2" in klass.__dict__:
            descriptor = klass.__dict__["address2"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_zipcode():
    assert hasattr(transaction_Payee, "zipcode")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "zipcode" in klass.__dict__:
            descriptor = klass.__dict__["zipcode"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_city():
    assert hasattr(transaction_Payee, "city")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_state():
    assert hasattr(transaction_Payee, "state")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_phoneNum():
    assert hasattr(transaction_Payee, "phoneNum")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "phoneNum" in klass.__dict__:
            descriptor = klass.__dict__["phoneNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_email():
    assert hasattr(transaction_Payee, "email")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_transaction_payee_has_name():
    assert hasattr(transaction_Payee, "name")
    descriptor = None
    for klass in transaction_Payee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transaction_externalaccount_is_not_abstract():
    assert not inspect.isabstract(transaction_ExternalAccount)


def test_transaction_externalaccount_constructor_exists():
    assert callable(transaction_ExternalAccount.__init__)


def test_transaction_externalaccount_constructor_args():
    sig = inspect.signature(transaction_ExternalAccount.__init__)
    params = list(sig.parameters.keys())
    assert "routingNum" in params, "Missing parameter 'routingNum'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "associatedAccount" in params, "Missing parameter 'associatedAccount'"

def test_transaction_externalaccount_has_routingNum():
    assert hasattr(transaction_ExternalAccount, "routingNum")
    descriptor = None
    for klass in transaction_ExternalAccount.__mro__:
        if "routingNum" in klass.__dict__:
            descriptor = klass.__dict__["routingNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_externalaccount_has_accountNum():
    assert hasattr(transaction_ExternalAccount, "accountNum")
    descriptor = None
    for klass in transaction_ExternalAccount.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)

def test_transaction_externalaccount_has_associatedAccount():
    assert hasattr(transaction_ExternalAccount, "associatedAccount")
    descriptor = None
    for klass in transaction_ExternalAccount.__mro__:
        if "associatedAccount" in klass.__dict__:
            descriptor = klass.__dict__["associatedAccount"]
            break
    assert isinstance(descriptor, property)



def test_transaction_paybillstransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_PaybillsTransaction)


def test_transaction_paybillstransaction_constructor_exists():
    assert callable(transaction_PaybillsTransaction.__init__)


def test_transaction_paybillstransaction_constructor_args():
    sig = inspect.signature(transaction_PaybillsTransaction.__init__)
    params = list(sig.parameters.keys())



def test_transaction_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_TransferTransaction)


def test_transaction_transfertransaction_constructor_exists():
    assert callable(transaction_TransferTransaction.__init__)


def test_transaction_transfertransaction_constructor_args():
    sig = inspect.signature(transaction_TransferTransaction.__init__)
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
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "type" in params, "Missing parameter 'type'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "time" in params, "Missing parameter 'time'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "description" in params, "Missing parameter 'description'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"

def test_transaction_transaction_has_sourceAccountNum():
    assert hasattr(transaction_Transaction, "sourceAccountNum")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
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

def test_transaction_transaction_has_transactionID():
    assert hasattr(transaction_Transaction, "transactionID")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_time():
    assert hasattr(transaction_Transaction, "time")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
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

def test_transaction_transaction_has_description():
    assert hasattr(transaction_Transaction, "description")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_comment():
    assert hasattr(transaction_Transaction, "comment")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_destinationAccountNum():
    assert hasattr(transaction_Transaction, "destinationAccountNum")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"
    assert "userRole" in params, "Missing parameter 'userRole'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "username" in params, "Missing parameter 'username'"

def test_user_has_lastLoginTime():
    assert hasattr(User, "lastLoginTime")
    descriptor = None
    for klass in User.__mro__:
        if "lastLoginTime" in klass.__dict__:
            descriptor = klass.__dict__["lastLoginTime"]
            break
    assert isinstance(descriptor, property)

def test_user_has_userRole():
    assert hasattr(User, "userRole")
    descriptor = None
    for klass in User.__mro__:
        if "userRole" in klass.__dict__:
            descriptor = klass.__dict__["userRole"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_userID():
    assert hasattr(User, "userID")
    descriptor = None
    for klass in User.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_username():
    assert hasattr(User, "username")
    descriptor = None
    for klass in User.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "IDType" in params, "Missing parameter 'IDType'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "IDNum" in params, "Missing parameter 'IDNum'"
    assert "email" in params, "Missing parameter 'email'"
    assert "address1" in params, "Missing parameter 'address1'"
    assert "state" in params, "Missing parameter 'state'"
    assert "city" in params, "Missing parameter 'city'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "country" in params, "Missing parameter 'country'"
    assert "address2" in params, "Missing parameter 'address2'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_profile_has_IDType():
    assert hasattr(Profile, "IDType")
    descriptor = None
    for klass in Profile.__mro__:
        if "IDType" in klass.__dict__:
            descriptor = klass.__dict__["IDType"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_firstname():
    assert hasattr(Profile, "firstname")
    descriptor = None
    for klass in Profile.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_zipcode():
    assert hasattr(Profile, "zipcode")
    descriptor = None
    for klass in Profile.__mro__:
        if "zipcode" in klass.__dict__:
            descriptor = klass.__dict__["zipcode"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_IDNum():
    assert hasattr(Profile, "IDNum")
    descriptor = None
    for klass in Profile.__mro__:
        if "IDNum" in klass.__dict__:
            descriptor = klass.__dict__["IDNum"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_email():
    assert hasattr(Profile, "email")
    descriptor = None
    for klass in Profile.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_address1():
    assert hasattr(Profile, "address1")
    descriptor = None
    for klass in Profile.__mro__:
        if "address1" in klass.__dict__:
            descriptor = klass.__dict__["address1"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_state():
    assert hasattr(Profile, "state")
    descriptor = None
    for klass in Profile.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_city():
    assert hasattr(Profile, "city")
    descriptor = None
    for klass in Profile.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_dateOfBirth():
    assert hasattr(Profile, "dateOfBirth")
    descriptor = None
    for klass in Profile.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_country():
    assert hasattr(Profile, "country")
    descriptor = None
    for klass in Profile.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_address2():
    assert hasattr(Profile, "address2")
    descriptor = None
    for klass in Profile.__mro__:
        if "address2" in klass.__dict__:
            descriptor = klass.__dict__["address2"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_userID():
    assert hasattr(Profile, "userID")
    descriptor = None
    for klass in Profile.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_phoneNumber():
    assert hasattr(Profile, "phoneNumber")
    descriptor = None
    for klass in Profile.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_profile_has_lastname():
    assert hasattr(Profile, "lastname")
    descriptor = None
    for klass in Profile.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_usergroup_exists():
    # Check that the Enumeration exists
    assert UserGroup is not None

def test_usergroup_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UserGroup]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UserGroup"

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
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    pin=
        safe_text,
    type=
        st.none(),
    userID=
        safe_text,
    accountNum=
        safe_text
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_Payee_strategy = st.builds(
    transaction_Payee,
    country=
        safe_text,
    accountNum=
        safe_text,
    address1=
        safe_text,
    address2=
        safe_text,
    zipcode=
        safe_text,
    city=
        safe_text,
    state=
        safe_text,
    phoneNum=
        safe_text,
    email=
        safe_text,
    name=
        safe_text
)
transaction_ExternalAccount_strategy = st.builds(
    transaction_ExternalAccount,
    routingNum=
        safe_text,
    accountNum=
        safe_text,
    associatedAccount=
        safe_text
)
transaction_PaybillsTransaction_strategy = st.builds(
    transaction_PaybillsTransaction,
)
transaction_TransferTransaction_strategy = st.builds(
    transaction_TransferTransaction,
)
transaction_DepositTransaction_strategy = st.builds(
    transaction_DepositTransaction,
)
transaction_Transaction_strategy = st.builds(
    transaction_Transaction,
    sourceAccountNum=
        safe_text,
    type=
        st.none(),
    transactionID=
        safe_text,
    time=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    description=
        safe_text,
    comment=
        safe_text,
    destinationAccountNum=
        safe_text
)
User_strategy = st.builds(
    User,
    lastLoginTime=
        safe_text,
    userRole=
        safe_text,
    password=
        safe_text,
    userID=
        safe_text,
    username=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    IDType=
        st.integers(),
    firstname=
        safe_text,
    zipcode=
        safe_text,
    IDNum=
        safe_text,
    email=
        safe_text,
    address1=
        safe_text,
    state=
        safe_text,
    city=
        safe_text,
    dateOfBirth=
        st.dates(),
    country=
        safe_text,
    address2=
        safe_text,
    userID=
        safe_text,
    phoneNumber=
        safe_text,
    lastname=
        safe_text
)

@given(instance=account_Account_strategy)
@settings(max_examples=50)
def test_account_account_instantiation(instance):
    assert isinstance(instance, account_Account)



@given(instance=account_Account_strategy)
def test_account_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=account_Account_strategy)
def test_account_account_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=account_Account_strategy)
def test_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=account_Account_strategy)
def test_account_account_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=account_Account_strategy)
def test_account_account_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original

@given(instance=account_SavingsAccount_strategy)
@settings(max_examples=50)
def test_account_savingsaccount_instantiation(instance):
    assert isinstance(instance, account_SavingsAccount)



@given(instance=account_SavingsAccount_strategy)
def test_account_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=transaction_Payee_strategy)
@settings(max_examples=50)
def test_transaction_payee_instantiation(instance):
    assert isinstance(instance, transaction_Payee)



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_address1_setter(instance):
    original = instance.address1
    instance.address1 = original
    assert instance.address1 == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_address2_setter(instance):
    original = instance.address2
    instance.address2 = original
    assert instance.address2 == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_phoneNum_setter(instance):
    original = instance.phoneNum
    instance.phoneNum = original
    assert instance.phoneNum == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=transaction_Payee_strategy)
def test_transaction_payee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=transaction_ExternalAccount_strategy)
@settings(max_examples=50)
def test_transaction_externalaccount_instantiation(instance):
    assert isinstance(instance, transaction_ExternalAccount)



@given(instance=transaction_ExternalAccount_strategy)
def test_transaction_externalaccount_routingNum_setter(instance):
    original = instance.routingNum
    instance.routingNum = original
    assert instance.routingNum == original



@given(instance=transaction_ExternalAccount_strategy)
def test_transaction_externalaccount_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=transaction_ExternalAccount_strategy)
def test_transaction_externalaccount_associatedAccount_setter(instance):
    original = instance.associatedAccount
    instance.associatedAccount = original
    assert instance.associatedAccount == original

@given(instance=transaction_PaybillsTransaction_strategy)
@settings(max_examples=50)
def test_transaction_paybillstransaction_instantiation(instance):
    assert isinstance(instance, transaction_PaybillsTransaction)

@given(instance=transaction_TransferTransaction_strategy)
@settings(max_examples=50)
def test_transaction_transfertransaction_instantiation(instance):
    assert isinstance(instance, transaction_TransferTransaction)

@given(instance=transaction_DepositTransaction_strategy)
@settings(max_examples=50)
def test_transaction_deposittransaction_instantiation(instance):
    assert isinstance(instance, transaction_DepositTransaction)

@given(instance=transaction_Transaction_strategy)
@settings(max_examples=50)
def test_transaction_transaction_instantiation(instance):
    assert isinstance(instance, transaction_Transaction)



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original



@given(instance=User_strategy)
def test_user_userRole_setter(instance):
    original = instance.userRole
    instance.userRole = original
    assert instance.userRole == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=User_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)



@given(instance=Profile_strategy)
def test_profile_IDType_setter(instance):
    original = instance.IDType
    instance.IDType = original
    assert instance.IDType == original



@given(instance=Profile_strategy)
def test_profile_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Profile_strategy)
def test_profile_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original



@given(instance=Profile_strategy)
def test_profile_IDNum_setter(instance):
    original = instance.IDNum
    instance.IDNum = original
    assert instance.IDNum == original



@given(instance=Profile_strategy)
def test_profile_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Profile_strategy)
def test_profile_address1_setter(instance):
    original = instance.address1
    instance.address1 = original
    assert instance.address1 == original



@given(instance=Profile_strategy)
def test_profile_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Profile_strategy)
def test_profile_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Profile_strategy)
def test_profile_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Profile_strategy)
def test_profile_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Profile_strategy)
def test_profile_address2_setter(instance):
    original = instance.address2
    instance.address2 = original
    assert instance.address2 == original



@given(instance=Profile_strategy)
def test_profile_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Profile_strategy)
def test_profile_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Profile_strategy)
def test_profile_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original
