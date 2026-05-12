import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CheckBalance,
    Transfer_Money,
    Withdraw_Transaction,
    Savings_Account,
    Current_Account,
    ATM_Transaction,
    ATM_INFO,
    Account,
    Debit_Card,
    Customer,
    Bank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_checkbalance_is_not_abstract():
    assert not inspect.isabstract(CheckBalance)


def test_checkbalance_constructor_exists():
    assert callable(CheckBalance.__init__)


def test_checkbalance_constructor_args():
    sig = inspect.signature(CheckBalance.__init__)
    params = list(sig.parameters.keys())
    assert "Query" in params, "Missing parameter 'Query'"

def test_checkbalance_has_Query():
    assert hasattr(CheckBalance, "Query")
    descriptor = None
    for klass in CheckBalance.__mro__:
        if "Query" in klass.__dict__:
            descriptor = klass.__dict__["Query"]
            break
    assert isinstance(descriptor, property)



def test_transfer_money_is_not_abstract():
    assert not inspect.isabstract(Transfer_Money)


def test_transfer_money_constructor_exists():
    assert callable(Transfer_Money.__init__)


def test_transfer_money_constructor_args():
    sig = inspect.signature(Transfer_Money.__init__)
    params = list(sig.parameters.keys())
    assert "ACC_NO" in params, "Missing parameter 'ACC_NO'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_transfer_money_has_ACC_NO():
    assert hasattr(Transfer_Money, "ACC_NO")
    descriptor = None
    for klass in Transfer_Money.__mro__:
        if "ACC_NO" in klass.__dict__:
            descriptor = klass.__dict__["ACC_NO"]
            break
    assert isinstance(descriptor, property)

def test_transfer_money_has_amount():
    assert hasattr(Transfer_Money, "amount")
    descriptor = None
    for klass in Transfer_Money.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_withdraw_transaction_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Transaction)


def test_withdraw_transaction_constructor_exists():
    assert callable(Withdraw_Transaction.__init__)


def test_withdraw_transaction_constructor_args():
    sig = inspect.signature(Withdraw_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_withdraw_transaction_has_amount():
    assert hasattr(Withdraw_Transaction, "amount")
    descriptor = None
    for klass in Withdraw_Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_savings_account_is_not_abstract():
    assert not inspect.isabstract(Savings_Account)


def test_savings_account_constructor_exists():
    assert callable(Savings_Account.__init__)


def test_savings_account_constructor_args():
    sig = inspect.signature(Savings_Account.__init__)
    params = list(sig.parameters.keys())
    assert "Acc_no" in params, "Missing parameter 'Acc_no'"
    assert "Balance" in params, "Missing parameter 'Balance'"

def test_savings_account_has_Acc_no():
    assert hasattr(Savings_Account, "Acc_no")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "Acc_no" in klass.__dict__:
            descriptor = klass.__dict__["Acc_no"]
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
    assert "Acc_no" in params, "Missing parameter 'Acc_no'"
    assert "Balance" in params, "Missing parameter 'Balance'"

def test_current_account_has_Acc_no():
    assert hasattr(Current_Account, "Acc_no")
    descriptor = None
    for klass in Current_Account.__mro__:
        if "Acc_no" in klass.__dict__:
            descriptor = klass.__dict__["Acc_no"]
            break
    assert isinstance(descriptor, property)

def test_current_account_has_Balance():
    assert hasattr(Current_Account, "Balance")
    descriptor = None
    for klass in Current_Account.__mro__:
        if "Balance" in klass.__dict__:
            descriptor = klass.__dict__["Balance"]
            break
    assert isinstance(descriptor, property)



def test_atm_transaction_is_not_abstract():
    assert not inspect.isabstract(ATM_Transaction)


def test_atm_transaction_constructor_exists():
    assert callable(ATM_Transaction.__init__)


def test_atm_transaction_constructor_args():
    sig = inspect.signature(ATM_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "TransactionId" in params, "Missing parameter 'TransactionId'"

def test_atm_transaction_has_Amount():
    assert hasattr(ATM_Transaction, "Amount")
    descriptor = None
    for klass in ATM_Transaction.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_atm_transaction_has_Date():
    assert hasattr(ATM_Transaction, "Date")
    descriptor = None
    for klass in ATM_Transaction.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_atm_transaction_has_TransactionId():
    assert hasattr(ATM_Transaction, "TransactionId")
    descriptor = None
    for klass in ATM_Transaction.__mro__:
        if "TransactionId" in klass.__dict__:
            descriptor = klass.__dict__["TransactionId"]
            break
    assert isinstance(descriptor, property)



def test_atm_info_is_not_abstract():
    assert not inspect.isabstract(ATM_INFO)


def test_atm_info_constructor_exists():
    assert callable(ATM_INFO.__init__)


def test_atm_info_constructor_args():
    sig = inspect.signature(ATM_INFO.__init__)
    params = list(sig.parameters.keys())
    assert "Location" in params, "Missing parameter 'Location'"

def test_atm_info_has_Location():
    assert hasattr(ATM_INFO, "Location")
    descriptor = None
    for klass in ATM_INFO.__mro__:
        if "Location" in klass.__dict__:
            descriptor = klass.__dict__["Location"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "BranchLocation" in params, "Missing parameter 'BranchLocation'"
    assert "Owned_by" in params, "Missing parameter 'Owned_by'"

def test_account_has_Type():
    assert hasattr(Account, "Type")
    descriptor = None
    for klass in Account.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_account_has_BranchLocation():
    assert hasattr(Account, "BranchLocation")
    descriptor = None
    for klass in Account.__mro__:
        if "BranchLocation" in klass.__dict__:
            descriptor = klass.__dict__["BranchLocation"]
            break
    assert isinstance(descriptor, property)

def test_account_has_Owned_by():
    assert hasattr(Account, "Owned_by")
    descriptor = None
    for klass in Account.__mro__:
        if "Owned_by" in klass.__dict__:
            descriptor = klass.__dict__["Owned_by"]
            break
    assert isinstance(descriptor, property)



def test_debit_card_is_not_abstract():
    assert not inspect.isabstract(Debit_Card)


def test_debit_card_constructor_exists():
    assert callable(Debit_Card.__init__)


def test_debit_card_constructor_args():
    sig = inspect.signature(Debit_Card.__init__)
    params = list(sig.parameters.keys())
    assert "Owned_By" in params, "Missing parameter 'Owned_By'"
    assert "Card_No" in params, "Missing parameter 'Card_No'"

def test_debit_card_has_Owned_By():
    assert hasattr(Debit_Card, "Owned_By")
    descriptor = None
    for klass in Debit_Card.__mro__:
        if "Owned_By" in klass.__dict__:
            descriptor = klass.__dict__["Owned_By"]
            break
    assert isinstance(descriptor, property)

def test_debit_card_has_Card_No():
    assert hasattr(Debit_Card, "Card_No")
    descriptor = None
    for klass in Debit_Card.__mro__:
        if "Card_No" in klass.__dict__:
            descriptor = klass.__dict__["Card_No"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_customer_has_Address():
    assert hasattr(Customer, "Address")
    descriptor = None
    for klass in Customer.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Id():
    assert hasattr(Customer, "Id")
    descriptor = None
    for klass in Customer.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
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
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "BankId" in params, "Missing parameter 'BankId'"

def test_bank_has_location():
    assert hasattr(Bank, "location")
    descriptor = None
    for klass in Bank.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_BankId():
    assert hasattr(Bank, "BankId")
    descriptor = None
    for klass in Bank.__mro__:
        if "BankId" in klass.__dict__:
            descriptor = klass.__dict__["BankId"]
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
CheckBalance_strategy = st.builds(
    CheckBalance,
    Query=
        safe_text
)
Transfer_Money_strategy = st.builds(
    Transfer_Money,
    ACC_NO=
        safe_text,
    amount=
        st.integers()
)
Withdraw_Transaction_strategy = st.builds(
    Withdraw_Transaction,
    amount=
        st.integers()
)
Savings_Account_strategy = st.builds(
    Savings_Account,
    Acc_no=
        safe_text,
    Balance=
        safe_text
)
Current_Account_strategy = st.builds(
    Current_Account,
    Acc_no=
        safe_text,
    Balance=
        safe_text
)
ATM_Transaction_strategy = st.builds(
    ATM_Transaction,
    Amount=
        st.integers(),
    Date=
        safe_text,
    TransactionId=
        safe_text
)
ATM_INFO_strategy = st.builds(
    ATM_INFO,
    Location=
        safe_text
)
Account_strategy = st.builds(
    Account,
    Type=
        safe_text,
    BranchLocation=
        safe_text,
    Owned_by=
        safe_text
)
Debit_Card_strategy = st.builds(
    Debit_Card,
    Owned_By=
        safe_text,
    Card_No=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    Address=
        safe_text,
    Id=
        safe_text,
    Name=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    location=
        safe_text,
    BankId=
        safe_text
)

@given(instance=CheckBalance_strategy)
@settings(max_examples=50)
def test_checkbalance_instantiation(instance):
    assert isinstance(instance, CheckBalance)



@given(instance=CheckBalance_strategy)
def test_checkbalance_Query_setter(instance):
    original = instance.Query
    instance.Query = original
    assert instance.Query == original

@given(instance=Transfer_Money_strategy)
@settings(max_examples=50)
def test_transfer_money_instantiation(instance):
    assert isinstance(instance, Transfer_Money)



@given(instance=Transfer_Money_strategy)
def test_transfer_money_ACC_NO_setter(instance):
    original = instance.ACC_NO
    instance.ACC_NO = original
    assert instance.ACC_NO == original



@given(instance=Transfer_Money_strategy)
def test_transfer_money_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Withdraw_Transaction_strategy)
@settings(max_examples=50)
def test_withdraw_transaction_instantiation(instance):
    assert isinstance(instance, Withdraw_Transaction)



@given(instance=Withdraw_Transaction_strategy)
def test_withdraw_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Savings_Account_strategy)
@settings(max_examples=50)
def test_savings_account_instantiation(instance):
    assert isinstance(instance, Savings_Account)



@given(instance=Savings_Account_strategy)
def test_savings_account_Acc_no_setter(instance):
    original = instance.Acc_no
    instance.Acc_no = original
    assert instance.Acc_no == original



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
def test_current_account_Acc_no_setter(instance):
    original = instance.Acc_no
    instance.Acc_no = original
    assert instance.Acc_no == original



@given(instance=Current_Account_strategy)
def test_current_account_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original

@given(instance=ATM_Transaction_strategy)
@settings(max_examples=50)
def test_atm_transaction_instantiation(instance):
    assert isinstance(instance, ATM_Transaction)



@given(instance=ATM_Transaction_strategy)
def test_atm_transaction_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=ATM_Transaction_strategy)
def test_atm_transaction_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=ATM_Transaction_strategy)
def test_atm_transaction_TransactionId_setter(instance):
    original = instance.TransactionId
    instance.TransactionId = original
    assert instance.TransactionId == original

@given(instance=ATM_INFO_strategy)
@settings(max_examples=50)
def test_atm_info_instantiation(instance):
    assert isinstance(instance, ATM_INFO)



@given(instance=ATM_INFO_strategy)
def test_atm_info_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Account_strategy)
def test_account_BranchLocation_setter(instance):
    original = instance.BranchLocation
    instance.BranchLocation = original
    assert instance.BranchLocation == original



@given(instance=Account_strategy)
def test_account_Owned_by_setter(instance):
    original = instance.Owned_by
    instance.Owned_by = original
    assert instance.Owned_by == original

@given(instance=Debit_Card_strategy)
@settings(max_examples=50)
def test_debit_card_instantiation(instance):
    assert isinstance(instance, Debit_Card)



@given(instance=Debit_Card_strategy)
def test_debit_card_Owned_By_setter(instance):
    original = instance.Owned_By
    instance.Owned_By = original
    assert instance.Owned_By == original



@given(instance=Debit_Card_strategy)
def test_debit_card_Card_No_setter(instance):
    original = instance.Card_No
    instance.Card_No = original
    assert instance.Card_No == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_customer_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Customer_strategy)
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Bank_strategy)
def test_bank_BankId_setter(instance):
    original = instance.BankId
    instance.BankId = original
    assert instance.BankId == original
