import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genmymodelreverse_java_util_Date,
    genmymodelreverse_C2,
    genmymodelreverse_C1,
    genmymodelreverse_java_util_HashMap,
    genmymodelreverse_org_springframework_ui_Model_Interface,
    TestAccountChain,
    model_Withdrawal,
    model_Transaction,
    model_SavingsAccount,
    model_OpenAccount,
    model_MakePayment,
    model_Loan,
    model_Deposit,
    model_Customer,
    model_CreditAccount,
    model_CloseAccount,
    model_CheckingAccount,
    model_Bank,
    model_AccountHandler,
    model_AccountChain_Interface,
    model_AccountAction,
    model_Account,
    data_CustomerProfileRepository,
    OnlineBanking_AppConfig,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genmymodelreverse_java_util_date_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_Date)


def test_genmymodelreverse_java_util_date_constructor_exists():
    assert callable(genmymodelreverse_java_util_Date.__init__)


def test_genmymodelreverse_java_util_date_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_Date.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c2_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C2)


def test_genmymodelreverse_c2_constructor_exists():
    assert callable(genmymodelreverse_C2.__init__)


def test_genmymodelreverse_c2_constructor_args():
    sig = inspect.signature(genmymodelreverse_C2.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c1_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C1)


def test_genmymodelreverse_c1_constructor_exists():
    assert callable(genmymodelreverse_C1.__init__)


def test_genmymodelreverse_c1_constructor_args():
    sig = inspect.signature(genmymodelreverse_C1.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_util_hashmap_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_HashMap)


def test_genmymodelreverse_java_util_hashmap_constructor_exists():
    assert callable(genmymodelreverse_java_util_HashMap.__init__)


def test_genmymodelreverse_java_util_hashmap_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_HashMap.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_org_springframework_ui_model_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_org_springframework_ui_Model_Interface)


def test_genmymodelreverse_org_springframework_ui_model_interface_constructor_exists():
    assert callable(genmymodelreverse_org_springframework_ui_Model_Interface.__init__)


def test_genmymodelreverse_org_springframework_ui_model_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_org_springframework_ui_Model_Interface.__init__)
    params = list(sig.parameters.keys())



def test_testaccountchain_is_not_abstract():
    assert not inspect.isabstract(TestAccountChain)


def test_testaccountchain_constructor_exists():
    assert callable(TestAccountChain.__init__)


def test_testaccountchain_constructor_args():
    sig = inspect.signature(TestAccountChain.__init__)
    params = list(sig.parameters.keys())



def test_model_withdrawal_is_not_abstract():
    assert not inspect.isabstract(model_Withdrawal)


def test_model_withdrawal_constructor_exists():
    assert callable(model_Withdrawal.__init__)


def test_model_withdrawal_constructor_args():
    sig = inspect.signature(model_Withdrawal.__init__)
    params = list(sig.parameters.keys())



def test_model_transaction_is_not_abstract():
    assert not inspect.isabstract(model_Transaction)


def test_model_transaction_constructor_exists():
    assert callable(model_Transaction.__init__)


def test_model_transaction_constructor_args():
    sig = inspect.signature(model_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "ammount" in params, "Missing parameter 'ammount'"
    assert "date" in params, "Missing parameter 'date'"

def test_model_transaction_has_ammount():
    assert hasattr(model_Transaction, "ammount")
    descriptor = None
    for klass in model_Transaction.__mro__:
        if "ammount" in klass.__dict__:
            descriptor = klass.__dict__["ammount"]
            break
    assert isinstance(descriptor, property)

def test_model_transaction_has_date():
    assert hasattr(model_Transaction, "date")
    descriptor = None
    for klass in model_Transaction.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_model_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(model_SavingsAccount)


def test_model_savingsaccount_constructor_exists():
    assert callable(model_SavingsAccount.__init__)


def test_model_savingsaccount_constructor_args():
    sig = inspect.signature(model_SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_model_savingsaccount_has_type():
    assert hasattr(model_SavingsAccount, "type")
    descriptor = None
    for klass in model_SavingsAccount.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model_savingsaccount_has_interestRate():
    assert hasattr(model_SavingsAccount, "interestRate")
    descriptor = None
    for klass in model_SavingsAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_model_openaccount_is_not_abstract():
    assert not inspect.isabstract(model_OpenAccount)


def test_model_openaccount_constructor_exists():
    assert callable(model_OpenAccount.__init__)


def test_model_openaccount_constructor_args():
    sig = inspect.signature(model_OpenAccount.__init__)
    params = list(sig.parameters.keys())



def test_model_makepayment_is_not_abstract():
    assert not inspect.isabstract(model_MakePayment)


def test_model_makepayment_constructor_exists():
    assert callable(model_MakePayment.__init__)


def test_model_makepayment_constructor_args():
    sig = inspect.signature(model_MakePayment.__init__)
    params = list(sig.parameters.keys())



def test_model_loan_is_not_abstract():
    assert not inspect.isabstract(model_Loan)


def test_model_loan_constructor_exists():
    assert callable(model_Loan.__init__)


def test_model_loan_constructor_args():
    sig = inspect.signature(model_Loan.__init__)
    params = list(sig.parameters.keys())
    assert "minPayment" in params, "Missing parameter 'minPayment'"
    assert "type" in params, "Missing parameter 'type'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "paymentDueDate" in params, "Missing parameter 'paymentDueDate'"

def test_model_loan_has_minPayment():
    assert hasattr(model_Loan, "minPayment")
    descriptor = None
    for klass in model_Loan.__mro__:
        if "minPayment" in klass.__dict__:
            descriptor = klass.__dict__["minPayment"]
            break
    assert isinstance(descriptor, property)

def test_model_loan_has_type():
    assert hasattr(model_Loan, "type")
    descriptor = None
    for klass in model_Loan.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model_loan_has_interestRate():
    assert hasattr(model_Loan, "interestRate")
    descriptor = None
    for klass in model_Loan.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_model_loan_has_paymentDueDate():
    assert hasattr(model_Loan, "paymentDueDate")
    descriptor = None
    for klass in model_Loan.__mro__:
        if "paymentDueDate" in klass.__dict__:
            descriptor = klass.__dict__["paymentDueDate"]
            break
    assert isinstance(descriptor, property)



def test_model_deposit_is_not_abstract():
    assert not inspect.isabstract(model_Deposit)


def test_model_deposit_constructor_exists():
    assert callable(model_Deposit.__init__)


def test_model_deposit_constructor_args():
    sig = inspect.signature(model_Deposit.__init__)
    params = list(sig.parameters.keys())



def test_model_customer_is_not_abstract():
    assert not inspect.isabstract(model_Customer)


def test_model_customer_constructor_exists():
    assert callable(model_Customer.__init__)


def test_model_customer_constructor_args():
    sig = inspect.signature(model_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "password" in params, "Missing parameter 'password'"
    assert "dob" in params, "Missing parameter 'dob'"
    assert "name" in params, "Missing parameter 'name'"
    assert "username" in params, "Missing parameter 'username'"
    assert "accounts" in params, "Missing parameter 'accounts'"
    assert "id" in params, "Missing parameter 'id'"

def test_model_customer_has_address():
    assert hasattr(model_Customer, "address")
    descriptor = None
    for klass in model_Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_model_customer_has_password():
    assert hasattr(model_Customer, "password")
    descriptor = None
    for klass in model_Customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_model_customer_has_dob():
    assert hasattr(model_Customer, "dob")
    descriptor = None
    for klass in model_Customer.__mro__:
        if "dob" in klass.__dict__:
            descriptor = klass.__dict__["dob"]
            break
    assert isinstance(descriptor, property)

def test_model_customer_has_name():
    assert hasattr(model_Customer, "name")
    descriptor = None
    for klass in model_Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_customer_has_username():
    assert hasattr(model_Customer, "username")
    descriptor = None
    for klass in model_Customer.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_model_customer_has_accounts():
    assert hasattr(model_Customer, "accounts")
    descriptor = None
    for klass in model_Customer.__mro__:
        if "accounts" in klass.__dict__:
            descriptor = klass.__dict__["accounts"]
            break
    assert isinstance(descriptor, property)

def test_model_customer_has_id():
    assert hasattr(model_Customer, "id")
    descriptor = None
    for klass in model_Customer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model_creditaccount_is_not_abstract():
    assert not inspect.isabstract(model_CreditAccount)


def test_model_creditaccount_constructor_exists():
    assert callable(model_CreditAccount.__init__)


def test_model_creditaccount_constructor_args():
    sig = inspect.signature(model_CreditAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "paymentDueDate" in params, "Missing parameter 'paymentDueDate'"
    assert "type" in params, "Missing parameter 'type'"
    assert "minPayment" in params, "Missing parameter 'minPayment'"

def test_model_creditaccount_has_interestRate():
    assert hasattr(model_CreditAccount, "interestRate")
    descriptor = None
    for klass in model_CreditAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_model_creditaccount_has_paymentDueDate():
    assert hasattr(model_CreditAccount, "paymentDueDate")
    descriptor = None
    for klass in model_CreditAccount.__mro__:
        if "paymentDueDate" in klass.__dict__:
            descriptor = klass.__dict__["paymentDueDate"]
            break
    assert isinstance(descriptor, property)

def test_model_creditaccount_has_type():
    assert hasattr(model_CreditAccount, "type")
    descriptor = None
    for klass in model_CreditAccount.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model_creditaccount_has_minPayment():
    assert hasattr(model_CreditAccount, "minPayment")
    descriptor = None
    for klass in model_CreditAccount.__mro__:
        if "minPayment" in klass.__dict__:
            descriptor = klass.__dict__["minPayment"]
            break
    assert isinstance(descriptor, property)



def test_model_closeaccount_is_not_abstract():
    assert not inspect.isabstract(model_CloseAccount)


def test_model_closeaccount_constructor_exists():
    assert callable(model_CloseAccount.__init__)


def test_model_closeaccount_constructor_args():
    sig = inspect.signature(model_CloseAccount.__init__)
    params = list(sig.parameters.keys())



def test_model_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(model_CheckingAccount)


def test_model_checkingaccount_constructor_exists():
    assert callable(model_CheckingAccount.__init__)


def test_model_checkingaccount_constructor_args():
    sig = inspect.signature(model_CheckingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "type" in params, "Missing parameter 'type'"

def test_model_checkingaccount_has_interestRate():
    assert hasattr(model_CheckingAccount, "interestRate")
    descriptor = None
    for klass in model_CheckingAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_model_checkingaccount_has_type():
    assert hasattr(model_CheckingAccount, "type")
    descriptor = None
    for klass in model_CheckingAccount.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model_bank_is_not_abstract():
    assert not inspect.isabstract(model_Bank)


def test_model_bank_constructor_exists():
    assert callable(model_Bank.__init__)


def test_model_bank_constructor_args():
    sig = inspect.signature(model_Bank.__init__)
    params = list(sig.parameters.keys())
    assert "customerMap" in params, "Missing parameter 'customerMap'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_model_bank_has_customerMap():
    assert hasattr(model_Bank, "customerMap")
    descriptor = None
    for klass in model_Bank.__mro__:
        if "customerMap" in klass.__dict__:
            descriptor = klass.__dict__["customerMap"]
            break
    assert isinstance(descriptor, property)

def test_model_bank_has_name():
    assert hasattr(model_Bank, "name")
    descriptor = None
    for klass in model_Bank.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_bank_has_address():
    assert hasattr(model_Bank, "address")
    descriptor = None
    for klass in model_Bank.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_model_accounthandler_is_not_abstract():
    assert not inspect.isabstract(model_AccountHandler)


def test_model_accounthandler_constructor_exists():
    assert callable(model_AccountHandler.__init__)


def test_model_accounthandler_constructor_args():
    sig = inspect.signature(model_AccountHandler.__init__)
    params = list(sig.parameters.keys())



def test_model_accountchain_interface_is_not_abstract():
    assert not inspect.isabstract(model_AccountChain_Interface)


def test_model_accountchain_interface_constructor_exists():
    assert callable(model_AccountChain_Interface.__init__)


def test_model_accountchain_interface_constructor_args():
    sig = inspect.signature(model_AccountChain_Interface.__init__)
    params = list(sig.parameters.keys())



def test_model_accountaction_is_not_abstract():
    assert not inspect.isabstract(model_AccountAction)


def test_model_accountaction_constructor_exists():
    assert callable(model_AccountAction.__init__)


def test_model_accountaction_constructor_args():
    sig = inspect.signature(model_AccountAction.__init__)
    params = list(sig.parameters.keys())
    assert "success" in params, "Missing parameter 'success'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "action" in params, "Missing parameter 'action'"

def test_model_accountaction_has_success():
    assert hasattr(model_AccountAction, "success")
    descriptor = None
    for klass in model_AccountAction.__mro__:
        if "success" in klass.__dict__:
            descriptor = klass.__dict__["success"]
            break
    assert isinstance(descriptor, property)

def test_model_accountaction_has_amount():
    assert hasattr(model_AccountAction, "amount")
    descriptor = None
    for klass in model_AccountAction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_model_accountaction_has_action():
    assert hasattr(model_AccountAction, "action")
    descriptor = None
    for klass in model_AccountAction.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_model_account_is_not_abstract():
    assert not inspect.isabstract(model_Account)


def test_model_account_constructor_exists():
    assert callable(model_Account.__init__)


def test_model_account_constructor_args():
    sig = inspect.signature(model_Account.__init__)
    params = list(sig.parameters.keys())
    assert "customerId" in params, "Missing parameter 'customerId'"
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"
    assert "balance" in params, "Missing parameter 'balance'"
    assert "type" in params, "Missing parameter 'type'"

def test_model_account_has_customerId():
    assert hasattr(model_Account, "customerId")
    descriptor = None
    for klass in model_Account.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)

def test_model_account_has_accountNumber():
    assert hasattr(model_Account, "accountNumber")
    descriptor = None
    for klass in model_Account.__mro__:
        if "accountNumber" in klass.__dict__:
            descriptor = klass.__dict__["accountNumber"]
            break
    assert isinstance(descriptor, property)

def test_model_account_has_balance():
    assert hasattr(model_Account, "balance")
    descriptor = None
    for klass in model_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_model_account_has_type():
    assert hasattr(model_Account, "type")
    descriptor = None
    for klass in model_Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_data_customerprofilerepository_is_not_abstract():
    assert not inspect.isabstract(data_CustomerProfileRepository)


def test_data_customerprofilerepository_constructor_exists():
    assert callable(data_CustomerProfileRepository.__init__)


def test_data_customerprofilerepository_constructor_args():
    sig = inspect.signature(data_CustomerProfileRepository.__init__)
    params = list(sig.parameters.keys())
    assert "customerProfiles" in params, "Missing parameter 'customerProfiles'"
    assert "numAccounts" in params, "Missing parameter 'numAccounts'"

def test_data_customerprofilerepository_has_customerProfiles():
    assert hasattr(data_CustomerProfileRepository, "customerProfiles")
    descriptor = None
    for klass in data_CustomerProfileRepository.__mro__:
        if "customerProfiles" in klass.__dict__:
            descriptor = klass.__dict__["customerProfiles"]
            break
    assert isinstance(descriptor, property)

def test_data_customerprofilerepository_has_numAccounts():
    assert hasattr(data_CustomerProfileRepository, "numAccounts")
    descriptor = None
    for klass in data_CustomerProfileRepository.__mro__:
        if "numAccounts" in klass.__dict__:
            descriptor = klass.__dict__["numAccounts"]
            break
    assert isinstance(descriptor, property)



def test_onlinebanking_appconfig_is_not_abstract():
    assert not inspect.isabstract(OnlineBanking_AppConfig)


def test_onlinebanking_appconfig_constructor_exists():
    assert callable(OnlineBanking_AppConfig.__init__)


def test_onlinebanking_appconfig_constructor_args():
    sig = inspect.signature(OnlineBanking_AppConfig.__init__)
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
genmymodelreverse_java_util_Date_strategy = st.builds(
    genmymodelreverse_java_util_Date,
)
genmymodelreverse_C2_strategy = st.builds(
    genmymodelreverse_C2,
)
genmymodelreverse_C1_strategy = st.builds(
    genmymodelreverse_C1,
)
genmymodelreverse_java_util_HashMap_strategy = st.builds(
    genmymodelreverse_java_util_HashMap,
)
genmymodelreverse_org_springframework_ui_Model_Interface_strategy = st.builds(
    genmymodelreverse_org_springframework_ui_Model_Interface,
)
TestAccountChain_strategy = st.builds(
    TestAccountChain,
)
model_Withdrawal_strategy = st.builds(
    model_Withdrawal,
)
model_Transaction_strategy = st.builds(
    model_Transaction,
    ammount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    date=
        st.none()
)
model_SavingsAccount_strategy = st.builds(
    model_SavingsAccount,
    type=
        safe_text,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_OpenAccount_strategy = st.builds(
    model_OpenAccount,
)
model_MakePayment_strategy = st.builds(
    model_MakePayment,
)
model_Loan_strategy = st.builds(
    model_Loan,
    minPayment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    paymentDueDate=
        safe_text
)
model_Deposit_strategy = st.builds(
    model_Deposit,
)
model_Customer_strategy = st.builds(
    model_Customer,
    address=
        safe_text,
    password=
        safe_text,
    dob=
        safe_text,
    name=
        safe_text,
    username=
        safe_text,
    accounts=
        safe_text,
    id=
        st.integers()
)
model_CreditAccount_strategy = st.builds(
    model_CreditAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    paymentDueDate=
        safe_text,
    type=
        safe_text,
    minPayment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_CloseAccount_strategy = st.builds(
    model_CloseAccount,
)
model_CheckingAccount_strategy = st.builds(
    model_CheckingAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text
)
model_Bank_strategy = st.builds(
    model_Bank,
    customerMap=
        safe_text,
    name=
        safe_text,
    address=
        safe_text
)
model_AccountHandler_strategy = st.builds(
    model_AccountHandler,
)
model_AccountChain_Interface_strategy = st.builds(
    model_AccountChain_Interface,
)
model_AccountAction_strategy = st.builds(
    model_AccountAction,
    success=
        st.booleans(),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    action=
        safe_text
)
model_Account_strategy = st.builds(
    model_Account,
    customerId=
        st.integers(),
    accountNumber=
        st.integers(),
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text
)
data_CustomerProfileRepository_strategy = st.builds(
    data_CustomerProfileRepository,
    customerProfiles=
        safe_text,
    numAccounts=
        st.integers()
)
OnlineBanking_AppConfig_strategy = st.builds(
    OnlineBanking_AppConfig,
)

@given(instance=genmymodelreverse_java_util_Date_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_util_date_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Date)

@given(instance=genmymodelreverse_C2_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c2_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C2)

@given(instance=genmymodelreverse_C1_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c1_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C1)

@given(instance=genmymodelreverse_java_util_HashMap_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_util_hashmap_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_HashMap)

@given(instance=genmymodelreverse_org_springframework_ui_Model_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_org_springframework_ui_model_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_org_springframework_ui_Model_Interface)

@given(instance=TestAccountChain_strategy)
@settings(max_examples=50)
def test_testaccountchain_instantiation(instance):
    assert isinstance(instance, TestAccountChain)

@given(instance=model_Withdrawal_strategy)
@settings(max_examples=50)
def test_model_withdrawal_instantiation(instance):
    assert isinstance(instance, model_Withdrawal)

@given(instance=model_Transaction_strategy)
@settings(max_examples=50)
def test_model_transaction_instantiation(instance):
    assert isinstance(instance, model_Transaction)



@given(instance=model_Transaction_strategy)
def test_model_transaction_ammount_setter(instance):
    original = instance.ammount
    instance.ammount = original
    assert instance.ammount == original



@given(instance=model_Transaction_strategy)
def test_model_transaction_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=model_SavingsAccount_strategy)
@settings(max_examples=50)
def test_model_savingsaccount_instantiation(instance):
    assert isinstance(instance, model_SavingsAccount)



@given(instance=model_SavingsAccount_strategy)
def test_model_savingsaccount_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_SavingsAccount_strategy)
def test_model_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=model_OpenAccount_strategy)
@settings(max_examples=50)
def test_model_openaccount_instantiation(instance):
    assert isinstance(instance, model_OpenAccount)

@given(instance=model_MakePayment_strategy)
@settings(max_examples=50)
def test_model_makepayment_instantiation(instance):
    assert isinstance(instance, model_MakePayment)

@given(instance=model_Loan_strategy)
@settings(max_examples=50)
def test_model_loan_instantiation(instance):
    assert isinstance(instance, model_Loan)



@given(instance=model_Loan_strategy)
def test_model_loan_minPayment_setter(instance):
    original = instance.minPayment
    instance.minPayment = original
    assert instance.minPayment == original



@given(instance=model_Loan_strategy)
def test_model_loan_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_Loan_strategy)
def test_model_loan_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=model_Loan_strategy)
def test_model_loan_paymentDueDate_setter(instance):
    original = instance.paymentDueDate
    instance.paymentDueDate = original
    assert instance.paymentDueDate == original

@given(instance=model_Deposit_strategy)
@settings(max_examples=50)
def test_model_deposit_instantiation(instance):
    assert isinstance(instance, model_Deposit)

@given(instance=model_Customer_strategy)
@settings(max_examples=50)
def test_model_customer_instantiation(instance):
    assert isinstance(instance, model_Customer)



@given(instance=model_Customer_strategy)
def test_model_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=model_Customer_strategy)
def test_model_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=model_Customer_strategy)
def test_model_customer_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original



@given(instance=model_Customer_strategy)
def test_model_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Customer_strategy)
def test_model_customer_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=model_Customer_strategy)
def test_model_customer_accounts_setter(instance):
    original = instance.accounts
    instance.accounts = original
    assert instance.accounts == original



@given(instance=model_Customer_strategy)
def test_model_customer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model_CreditAccount_strategy)
@settings(max_examples=50)
def test_model_creditaccount_instantiation(instance):
    assert isinstance(instance, model_CreditAccount)



@given(instance=model_CreditAccount_strategy)
def test_model_creditaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=model_CreditAccount_strategy)
def test_model_creditaccount_paymentDueDate_setter(instance):
    original = instance.paymentDueDate
    instance.paymentDueDate = original
    assert instance.paymentDueDate == original



@given(instance=model_CreditAccount_strategy)
def test_model_creditaccount_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_CreditAccount_strategy)
def test_model_creditaccount_minPayment_setter(instance):
    original = instance.minPayment
    instance.minPayment = original
    assert instance.minPayment == original

@given(instance=model_CloseAccount_strategy)
@settings(max_examples=50)
def test_model_closeaccount_instantiation(instance):
    assert isinstance(instance, model_CloseAccount)

@given(instance=model_CheckingAccount_strategy)
@settings(max_examples=50)
def test_model_checkingaccount_instantiation(instance):
    assert isinstance(instance, model_CheckingAccount)



@given(instance=model_CheckingAccount_strategy)
def test_model_checkingaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=model_CheckingAccount_strategy)
def test_model_checkingaccount_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model_Bank_strategy)
@settings(max_examples=50)
def test_model_bank_instantiation(instance):
    assert isinstance(instance, model_Bank)



@given(instance=model_Bank_strategy)
def test_model_bank_customerMap_setter(instance):
    original = instance.customerMap
    instance.customerMap = original
    assert instance.customerMap == original



@given(instance=model_Bank_strategy)
def test_model_bank_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Bank_strategy)
def test_model_bank_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=model_AccountHandler_strategy)
@settings(max_examples=50)
def test_model_accounthandler_instantiation(instance):
    assert isinstance(instance, model_AccountHandler)

@given(instance=model_AccountChain_Interface_strategy)
@settings(max_examples=50)
def test_model_accountchain_interface_instantiation(instance):
    assert isinstance(instance, model_AccountChain_Interface)

@given(instance=model_AccountAction_strategy)
@settings(max_examples=50)
def test_model_accountaction_instantiation(instance):
    assert isinstance(instance, model_AccountAction)



@given(instance=model_AccountAction_strategy)
def test_model_accountaction_success_setter(instance):
    original = instance.success
    instance.success = original
    assert instance.success == original



@given(instance=model_AccountAction_strategy)
def test_model_accountaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=model_AccountAction_strategy)
def test_model_accountaction_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=model_Account_strategy)
@settings(max_examples=50)
def test_model_account_instantiation(instance):
    assert isinstance(instance, model_Account)



@given(instance=model_Account_strategy)
def test_model_account_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original



@given(instance=model_Account_strategy)
def test_model_account_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original



@given(instance=model_Account_strategy)
def test_model_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=model_Account_strategy)
def test_model_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=data_CustomerProfileRepository_strategy)
@settings(max_examples=50)
def test_data_customerprofilerepository_instantiation(instance):
    assert isinstance(instance, data_CustomerProfileRepository)



@given(instance=data_CustomerProfileRepository_strategy)
def test_data_customerprofilerepository_customerProfiles_setter(instance):
    original = instance.customerProfiles
    instance.customerProfiles = original
    assert instance.customerProfiles == original



@given(instance=data_CustomerProfileRepository_strategy)
def test_data_customerprofilerepository_numAccounts_setter(instance):
    original = instance.numAccounts
    instance.numAccounts = original
    assert instance.numAccounts == original

@given(instance=OnlineBanking_AppConfig_strategy)
@settings(max_examples=50)
def test_onlinebanking_appconfig_instantiation(instance):
    assert isinstance(instance, OnlineBanking_AppConfig)
