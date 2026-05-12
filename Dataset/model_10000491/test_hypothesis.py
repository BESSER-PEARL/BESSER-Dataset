import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Routing_Settings,
    Routing_Configuration_Settings,
    Custom_SalesForce_Object,
    Appraisal,
    Service_Channel,
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
    Routing_Model,
    transaction_TransactionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_routing_settings_is_not_abstract():
    assert not inspect.isabstract(Routing_Settings)


def test_routing_settings_constructor_exists():
    assert callable(Routing_Settings.__init__)


def test_routing_settings_constructor_args():
    sig = inspect.signature(Routing_Settings.__init__)
    params = list(sig.parameters.keys())
    assert "Push_Time_Out" in params, "Missing parameter 'Push_Time_Out'"
    assert "Routing_Model" in params, "Missing parameter 'Routing_Model'"
    assert "Routing_Priority" in params, "Missing parameter 'Routing_Priority'"

def test_routing_settings_has_Push_Time_Out():
    assert hasattr(Routing_Settings, "Push_Time_Out")
    descriptor = None
    for klass in Routing_Settings.__mro__:
        if "Push_Time_Out" in klass.__dict__:
            descriptor = klass.__dict__["Push_Time_Out"]
            break
    assert isinstance(descriptor, property)

def test_routing_settings_has_Routing_Model():
    assert hasattr(Routing_Settings, "Routing_Model")
    descriptor = None
    for klass in Routing_Settings.__mro__:
        if "Routing_Model" in klass.__dict__:
            descriptor = klass.__dict__["Routing_Model"]
            break
    assert isinstance(descriptor, property)

def test_routing_settings_has_Routing_Priority():
    assert hasattr(Routing_Settings, "Routing_Priority")
    descriptor = None
    for klass in Routing_Settings.__mro__:
        if "Routing_Priority" in klass.__dict__:
            descriptor = klass.__dict__["Routing_Priority"]
            break
    assert isinstance(descriptor, property)



def test_routing_configuration_settings_is_not_abstract():
    assert not inspect.isabstract(Routing_Configuration_Settings)


def test_routing_configuration_settings_constructor_exists():
    assert callable(Routing_Configuration_Settings.__init__)


def test_routing_configuration_settings_constructor_args():
    sig = inspect.signature(Routing_Configuration_Settings.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Overflow_Assignee" in params, "Missing parameter 'Overflow_Assignee'"

def test_routing_configuration_settings_has_Name():
    assert hasattr(Routing_Configuration_Settings, "Name")
    descriptor = None
    for klass in Routing_Configuration_Settings.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_routing_configuration_settings_has_Overflow_Assignee():
    assert hasattr(Routing_Configuration_Settings, "Overflow_Assignee")
    descriptor = None
    for klass in Routing_Configuration_Settings.__mro__:
        if "Overflow_Assignee" in klass.__dict__:
            descriptor = klass.__dict__["Overflow_Assignee"]
            break
    assert isinstance(descriptor, property)



def test_custom_salesforce_object_is_not_abstract():
    assert not inspect.isabstract(Custom_SalesForce_Object)


def test_custom_salesforce_object_constructor_exists():
    assert callable(Custom_SalesForce_Object.__init__)


def test_custom_salesforce_object_constructor_args():
    sig = inspect.signature(Custom_SalesForce_Object.__init__)
    params = list(sig.parameters.keys())
    assert "Owner" in params, "Missing parameter 'Owner'"

def test_custom_salesforce_object_has_Owner():
    assert hasattr(Custom_SalesForce_Object, "Owner")
    descriptor = None
    for klass in Custom_SalesForce_Object.__mro__:
        if "Owner" in klass.__dict__:
            descriptor = klass.__dict__["Owner"]
            break
    assert isinstance(descriptor, property)



def test_appraisal_is_not_abstract():
    assert not inspect.isabstract(Appraisal)


def test_appraisal_constructor_exists():
    assert callable(Appraisal.__init__)


def test_appraisal_constructor_args():
    sig = inspect.signature(Appraisal.__init__)
    params = list(sig.parameters.keys())
    assert "Col1" in params, "Missing parameter 'Col1'"
    assert "Col2" in params, "Missing parameter 'Col2'"

def test_appraisal_has_Col1():
    assert hasattr(Appraisal, "Col1")
    descriptor = None
    for klass in Appraisal.__mro__:
        if "Col1" in klass.__dict__:
            descriptor = klass.__dict__["Col1"]
            break
    assert isinstance(descriptor, property)

def test_appraisal_has_Col2():
    assert hasattr(Appraisal, "Col2")
    descriptor = None
    for klass in Appraisal.__mro__:
        if "Col2" in klass.__dict__:
            descriptor = klass.__dict__["Col2"]
            break
    assert isinstance(descriptor, property)



def test_service_channel_is_not_abstract():
    assert not inspect.isabstract(Service_Channel)


def test_service_channel_constructor_exists():
    assert callable(Service_Channel.__init__)


def test_service_channel_constructor_args():
    sig = inspect.signature(Service_Channel.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_service_channel_has_Name():
    assert hasattr(Service_Channel, "Name")
    descriptor = None
    for klass in Service_Channel.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_account_account_is_not_abstract():
    assert not inspect.isabstract(account_Account)


def test_account_account_constructor_exists():
    assert callable(account_Account.__init__)


def test_account_account_constructor_args():
    sig = inspect.signature(account_Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "type" in params, "Missing parameter 'type'"
    assert "accountNo" in params, "Missing parameter 'accountNo'"

def test_account_account_has_balance():
    assert hasattr(account_Account, "balance")
    descriptor = None
    for klass in account_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
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

def test_account_account_has_accountNo():
    assert hasattr(account_Account, "accountNo")
    descriptor = None
    for klass in account_Account.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
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
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "timePeriod" in params, "Missing parameter 'timePeriod'"

def test_account_certificatesofdepositaccount_has_interestRate():
    assert hasattr(account_CertificatesOfDepositAccount, "interestRate")
    descriptor = None
    for klass in account_CertificatesOfDepositAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_account_certificatesofdepositaccount_has_timePeriod():
    assert hasattr(account_CertificatesOfDepositAccount, "timePeriod")
    descriptor = None
    for klass in account_CertificatesOfDepositAccount.__mro__:
        if "timePeriod" in klass.__dict__:
            descriptor = klass.__dict__["timePeriod"]
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
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"

def test_transaction_transfertransaction_has_sourceAccount():
    assert hasattr(transaction_TransferTransaction, "sourceAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transfertransaction_has_targetAccount():
    assert hasattr(transaction_TransferTransaction, "targetAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
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
    assert "amount" in params, "Missing parameter 'amount'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"

def test_transaction_transaction_has_amount():
    assert hasattr(transaction_Transaction, "amount")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_transaction_has_id():
    assert hasattr(transaction_Transaction, "id")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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

def test_transaction_transaction_has_transactionTime():
    assert hasattr(transaction_Transaction, "transactionTime")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionTime" in klass.__dict__:
            descriptor = klass.__dict__["transactionTime"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "securityAnswer" in params, "Missing parameter 'securityAnswer'"
    assert "username" in params, "Missing parameter 'username'"
    assert "securityQuestion" in params, "Missing parameter 'securityQuestion'"
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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

def test_login_has_lastLoginTime():
    assert hasattr(Login, "lastLoginTime")
    descriptor = None
    for klass in Login.__mro__:
        if "lastLoginTime" in klass.__dict__:
            descriptor = klass.__dict__["lastLoginTime"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"

def test_customer_has_name():
    assert hasattr(Customer, "name")
    descriptor = None
    for klass in Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_customer_has_phoneNumber():
    assert hasattr(Customer, "phoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_dateOfBirth():
    assert hasattr(Customer, "dateOfBirth")
    descriptor = None
    for klass in Customer.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
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

def test_routing_model_exists():
    # Check that the Enumeration exists
    assert Routing_Model is not None

def test_routing_model_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Routing_Model]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Routing_Model"

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
Routing_Settings_strategy = st.builds(
    Routing_Settings,
    Push_Time_Out=
        safe_text,
    Routing_Model=
        st.none(),
    Routing_Priority=
        st.integers()
)
Routing_Configuration_Settings_strategy = st.builds(
    Routing_Configuration_Settings,
    Name=
        safe_text,
    Overflow_Assignee=
        safe_text
)
Custom_SalesForce_Object_strategy = st.builds(
    Custom_SalesForce_Object,
    Owner=
        safe_text
)
Appraisal_strategy = st.builds(
    Appraisal,
    Col1=
        safe_text,
    Col2=
        safe_text
)
Service_Channel_strategy = st.builds(
    Service_Channel,
    Name=
        safe_text
)
account_Account_strategy = st.builds(
    account_Account,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none(),
    accountNo=
        safe_text
)
account_CheckingAccount_strategy = st.builds(
    account_CheckingAccount,
    name=
        safe_text
)
account_CertificatesOfDepositAccount_strategy = st.builds(
    account_CertificatesOfDepositAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    timePeriod=
        st.integers()
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_TransferTransaction_strategy = st.builds(
    transaction_TransferTransaction,
    sourceAccount=
        st.none(),
    targetAccount=
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
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    id=
        st.integers(),
    type=
        st.none(),
    transactionTime=
        st.dates()
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    securityAnswer=
        safe_text,
    username=
        safe_text,
    securityQuestion=
        safe_text,
    lastLoginTime=
        st.dates()
)
Customer_strategy = st.builds(
    Customer,
    name=
        safe_text,
    address=
        safe_text,
    emailAddress=
        safe_text,
    phoneNumber=
        safe_text,
    dateOfBirth=
        st.dates()
)

@given(instance=Routing_Settings_strategy)
@settings(max_examples=50)
def test_routing_settings_instantiation(instance):
    assert isinstance(instance, Routing_Settings)



@given(instance=Routing_Settings_strategy)
def test_routing_settings_Push_Time_Out_setter(instance):
    original = instance.Push_Time_Out
    instance.Push_Time_Out = original
    assert instance.Push_Time_Out == original



@given(instance=Routing_Settings_strategy)
def test_routing_settings_Routing_Model_setter(instance):
    original = instance.Routing_Model
    instance.Routing_Model = original
    assert instance.Routing_Model == original



@given(instance=Routing_Settings_strategy)
def test_routing_settings_Routing_Priority_setter(instance):
    original = instance.Routing_Priority
    instance.Routing_Priority = original
    assert instance.Routing_Priority == original

@given(instance=Routing_Configuration_Settings_strategy)
@settings(max_examples=50)
def test_routing_configuration_settings_instantiation(instance):
    assert isinstance(instance, Routing_Configuration_Settings)



@given(instance=Routing_Configuration_Settings_strategy)
def test_routing_configuration_settings_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Routing_Configuration_Settings_strategy)
def test_routing_configuration_settings_Overflow_Assignee_setter(instance):
    original = instance.Overflow_Assignee
    instance.Overflow_Assignee = original
    assert instance.Overflow_Assignee == original

@given(instance=Custom_SalesForce_Object_strategy)
@settings(max_examples=50)
def test_custom_salesforce_object_instantiation(instance):
    assert isinstance(instance, Custom_SalesForce_Object)



@given(instance=Custom_SalesForce_Object_strategy)
def test_custom_salesforce_object_Owner_setter(instance):
    original = instance.Owner
    instance.Owner = original
    assert instance.Owner == original

@given(instance=Appraisal_strategy)
@settings(max_examples=50)
def test_appraisal_instantiation(instance):
    assert isinstance(instance, Appraisal)



@given(instance=Appraisal_strategy)
def test_appraisal_Col1_setter(instance):
    original = instance.Col1
    instance.Col1 = original
    assert instance.Col1 == original



@given(instance=Appraisal_strategy)
def test_appraisal_Col2_setter(instance):
    original = instance.Col2
    instance.Col2 = original
    assert instance.Col2 == original

@given(instance=Service_Channel_strategy)
@settings(max_examples=50)
def test_service_channel_instantiation(instance):
    assert isinstance(instance, Service_Channel)



@given(instance=Service_Channel_strategy)
def test_service_channel_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

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
def test_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=account_Account_strategy)
def test_account_account_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original

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
def test_account_certificatesofdepositaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_account_certificatesofdepositaccount_timePeriod_setter(instance):
    original = instance.timePeriod
    instance.timePeriod = original
    assert instance.timePeriod == original

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
def test_transaction_transfertransaction_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original



@given(instance=transaction_TransferTransaction_strategy)
def test_transaction_transfertransaction_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original

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
def test_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=transaction_Transaction_strategy)
def test_transaction_transaction_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_securityAnswer_setter(instance):
    original = instance.securityAnswer
    instance.securityAnswer = original
    assert instance.securityAnswer == original



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
def test_login_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



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



@given(instance=Customer_strategy)
def test_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer_strategy)
def test_customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original
