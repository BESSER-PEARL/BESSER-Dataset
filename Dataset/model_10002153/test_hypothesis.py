import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Loan_Account,
    Savings_Account,
    CurrentAccount,
    ATM_s,
    AccountHolder,
    BankEmployee,
    Accounts,
    Bank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_loan_account_is_not_abstract():
    assert not inspect.isabstract(Loan_Account)


def test_loan_account_constructor_exists():
    assert callable(Loan_Account.__init__)


def test_loan_account_constructor_args():
    sig = inspect.signature(Loan_Account.__init__)
    params = list(sig.parameters.keys())
    assert "Loan_No" in params, "Missing parameter 'Loan_No'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "HolderName" in params, "Missing parameter 'HolderName'"
    assert "Acc_No" in params, "Missing parameter 'Acc_No'"

def test_loan_account_has_Loan_No():
    assert hasattr(Loan_Account, "Loan_No")
    descriptor = None
    for klass in Loan_Account.__mro__:
        if "Loan_No" in klass.__dict__:
            descriptor = klass.__dict__["Loan_No"]
            break
    assert isinstance(descriptor, property)

def test_loan_account_has_Type():
    assert hasattr(Loan_Account, "Type")
    descriptor = None
    for klass in Loan_Account.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_loan_account_has_HolderName():
    assert hasattr(Loan_Account, "HolderName")
    descriptor = None
    for klass in Loan_Account.__mro__:
        if "HolderName" in klass.__dict__:
            descriptor = klass.__dict__["HolderName"]
            break
    assert isinstance(descriptor, property)

def test_loan_account_has_Acc_No():
    assert hasattr(Loan_Account, "Acc_No")
    descriptor = None
    for klass in Loan_Account.__mro__:
        if "Acc_No" in klass.__dict__:
            descriptor = klass.__dict__["Acc_No"]
            break
    assert isinstance(descriptor, property)



def test_savings_account_is_not_abstract():
    assert not inspect.isabstract(Savings_Account)


def test_savings_account_constructor_exists():
    assert callable(Savings_Account.__init__)


def test_savings_account_constructor_args():
    sig = inspect.signature(Savings_Account.__init__)
    params = list(sig.parameters.keys())
    assert "PIn" in params, "Missing parameter 'PIn'"
    assert "Holder_Name" in params, "Missing parameter 'Holder_Name'"
    assert "AccNo" in params, "Missing parameter 'AccNo'"

def test_savings_account_has_PIn():
    assert hasattr(Savings_Account, "PIn")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "PIn" in klass.__dict__:
            descriptor = klass.__dict__["PIn"]
            break
    assert isinstance(descriptor, property)

def test_savings_account_has_Holder_Name():
    assert hasattr(Savings_Account, "Holder_Name")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "Holder_Name" in klass.__dict__:
            descriptor = klass.__dict__["Holder_Name"]
            break
    assert isinstance(descriptor, property)

def test_savings_account_has_AccNo():
    assert hasattr(Savings_Account, "AccNo")
    descriptor = None
    for klass in Savings_Account.__mro__:
        if "AccNo" in klass.__dict__:
            descriptor = klass.__dict__["AccNo"]
            break
    assert isinstance(descriptor, property)



def test_currentaccount_is_not_abstract():
    assert not inspect.isabstract(CurrentAccount)


def test_currentaccount_constructor_exists():
    assert callable(CurrentAccount.__init__)


def test_currentaccount_constructor_args():
    sig = inspect.signature(CurrentAccount.__init__)
    params = list(sig.parameters.keys())
    assert "HolderName" in params, "Missing parameter 'HolderName'"
    assert "AccNo" in params, "Missing parameter 'AccNo'"
    assert "PIn" in params, "Missing parameter 'PIn'"

def test_currentaccount_has_HolderName():
    assert hasattr(CurrentAccount, "HolderName")
    descriptor = None
    for klass in CurrentAccount.__mro__:
        if "HolderName" in klass.__dict__:
            descriptor = klass.__dict__["HolderName"]
            break
    assert isinstance(descriptor, property)

def test_currentaccount_has_AccNo():
    assert hasattr(CurrentAccount, "AccNo")
    descriptor = None
    for klass in CurrentAccount.__mro__:
        if "AccNo" in klass.__dict__:
            descriptor = klass.__dict__["AccNo"]
            break
    assert isinstance(descriptor, property)

def test_currentaccount_has_PIn():
    assert hasattr(CurrentAccount, "PIn")
    descriptor = None
    for klass in CurrentAccount.__mro__:
        if "PIn" in klass.__dict__:
            descriptor = klass.__dict__["PIn"]
            break
    assert isinstance(descriptor, property)



def test_atm_s_is_not_abstract():
    assert not inspect.isabstract(ATM_s)


def test_atm_s_constructor_exists():
    assert callable(ATM_s.__init__)


def test_atm_s_constructor_args():
    sig = inspect.signature(ATM_s.__init__)
    params = list(sig.parameters.keys())
    assert "PIN" in params, "Missing parameter 'PIN'"
    assert "Withdrawn" in params, "Missing parameter 'Withdrawn'"
    assert "OperatorName" in params, "Missing parameter 'OperatorName'"

def test_atm_s_has_PIN():
    assert hasattr(ATM_s, "PIN")
    descriptor = None
    for klass in ATM_s.__mro__:
        if "PIN" in klass.__dict__:
            descriptor = klass.__dict__["PIN"]
            break
    assert isinstance(descriptor, property)

def test_atm_s_has_Withdrawn():
    assert hasattr(ATM_s, "Withdrawn")
    descriptor = None
    for klass in ATM_s.__mro__:
        if "Withdrawn" in klass.__dict__:
            descriptor = klass.__dict__["Withdrawn"]
            break
    assert isinstance(descriptor, property)

def test_atm_s_has_OperatorName():
    assert hasattr(ATM_s, "OperatorName")
    descriptor = None
    for klass in ATM_s.__mro__:
        if "OperatorName" in klass.__dict__:
            descriptor = klass.__dict__["OperatorName"]
            break
    assert isinstance(descriptor, property)



def test_accountholder_is_not_abstract():
    assert not inspect.isabstract(AccountHolder)


def test_accountholder_constructor_exists():
    assert callable(AccountHolder.__init__)


def test_accountholder_constructor_args():
    sig = inspect.signature(AccountHolder.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "AccNo" in params, "Missing parameter 'AccNo'"

def test_accountholder_has_Name():
    assert hasattr(AccountHolder, "Name")
    descriptor = None
    for klass in AccountHolder.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_accountholder_has_Address():
    assert hasattr(AccountHolder, "Address")
    descriptor = None
    for klass in AccountHolder.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_accountholder_has_AccNo():
    assert hasattr(AccountHolder, "AccNo")
    descriptor = None
    for klass in AccountHolder.__mro__:
        if "AccNo" in klass.__dict__:
            descriptor = klass.__dict__["AccNo"]
            break
    assert isinstance(descriptor, property)



def test_bankemployee_is_not_abstract():
    assert not inspect.isabstract(BankEmployee)


def test_bankemployee_constructor_exists():
    assert callable(BankEmployee.__init__)


def test_bankemployee_constructor_args():
    sig = inspect.signature(BankEmployee.__init__)
    params = list(sig.parameters.keys())
    assert "EmpAdd" in params, "Missing parameter 'EmpAdd'"
    assert "EmployeeID" in params, "Missing parameter 'EmployeeID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Salary" in params, "Missing parameter 'Salary'"

def test_bankemployee_has_EmpAdd():
    assert hasattr(BankEmployee, "EmpAdd")
    descriptor = None
    for klass in BankEmployee.__mro__:
        if "EmpAdd" in klass.__dict__:
            descriptor = klass.__dict__["EmpAdd"]
            break
    assert isinstance(descriptor, property)

def test_bankemployee_has_EmployeeID():
    assert hasattr(BankEmployee, "EmployeeID")
    descriptor = None
    for klass in BankEmployee.__mro__:
        if "EmployeeID" in klass.__dict__:
            descriptor = klass.__dict__["EmployeeID"]
            break
    assert isinstance(descriptor, property)

def test_bankemployee_has_Name():
    assert hasattr(BankEmployee, "Name")
    descriptor = None
    for klass in BankEmployee.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_bankemployee_has_Salary():
    assert hasattr(BankEmployee, "Salary")
    descriptor = None
    for klass in BankEmployee.__mro__:
        if "Salary" in klass.__dict__:
            descriptor = klass.__dict__["Salary"]
            break
    assert isinstance(descriptor, property)



def test_accounts_is_not_abstract():
    assert not inspect.isabstract(Accounts)


def test_accounts_constructor_exists():
    assert callable(Accounts.__init__)


def test_accounts_constructor_args():
    sig = inspect.signature(Accounts.__init__)
    params = list(sig.parameters.keys())
    assert "AccountNo" in params, "Missing parameter 'AccountNo'"
    assert "branchCode" in params, "Missing parameter 'branchCode'"

def test_accounts_has_AccountNo():
    assert hasattr(Accounts, "AccountNo")
    descriptor = None
    for klass in Accounts.__mro__:
        if "AccountNo" in klass.__dict__:
            descriptor = klass.__dict__["AccountNo"]
            break
    assert isinstance(descriptor, property)

def test_accounts_has_branchCode():
    assert hasattr(Accounts, "branchCode")
    descriptor = None
    for klass in Accounts.__mro__:
        if "branchCode" in klass.__dict__:
            descriptor = klass.__dict__["branchCode"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "locality" in params, "Missing parameter 'locality'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Name_string" in params, "Missing parameter 'Name_string'"

def test_bank_has_locality():
    assert hasattr(Bank, "locality")
    descriptor = None
    for klass in Bank.__mro__:
        if "locality" in klass.__dict__:
            descriptor = klass.__dict__["locality"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_ID():
    assert hasattr(Bank, "ID")
    descriptor = None
    for klass in Bank.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_Name():
    assert hasattr(Bank, "Name")
    descriptor = None
    for klass in Bank.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_Name_string():
    assert hasattr(Bank, "Name_string")
    descriptor = None
    for klass in Bank.__mro__:
        if "Name_string" in klass.__dict__:
            descriptor = klass.__dict__["Name_string"]
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
Loan_Account_strategy = st.builds(
    Loan_Account,
    Loan_No=
        st.integers(),
    Type=
        safe_text,
    HolderName=
        safe_text,
    Acc_No=
        st.integers()
)
Savings_Account_strategy = st.builds(
    Savings_Account,
    PIn=
        st.none(),
    Holder_Name=
        safe_text,
    AccNo=
        st.integers()
)
CurrentAccount_strategy = st.builds(
    CurrentAccount,
    HolderName=
        safe_text,
    AccNo=
        st.integers(),
    PIn=
        st.integers()
)
ATM_s_strategy = st.builds(
    ATM_s,
    PIN=
        st.integers(),
    Withdrawn=
        st.integers(),
    OperatorName=
        safe_text
)
AccountHolder_strategy = st.builds(
    AccountHolder,
    Name=
        safe_text,
    Address=
        safe_text,
    AccNo=
        st.integers()
)
BankEmployee_strategy = st.builds(
    BankEmployee,
    EmpAdd=
        safe_text,
    EmployeeID=
        st.integers(),
    Name=
        safe_text,
    Salary=
        st.integers()
)
Accounts_strategy = st.builds(
    Accounts,
    AccountNo=
        st.integers(),
    branchCode=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    locality=
        safe_text,
    ID=
        st.integers(),
    Name=
        safe_text,
    Name_string=
        safe_text
)

@given(instance=Loan_Account_strategy)
@settings(max_examples=50)
def test_loan_account_instantiation(instance):
    assert isinstance(instance, Loan_Account)



@given(instance=Loan_Account_strategy)
def test_loan_account_Loan_No_setter(instance):
    original = instance.Loan_No
    instance.Loan_No = original
    assert instance.Loan_No == original



@given(instance=Loan_Account_strategy)
def test_loan_account_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Loan_Account_strategy)
def test_loan_account_HolderName_setter(instance):
    original = instance.HolderName
    instance.HolderName = original
    assert instance.HolderName == original



@given(instance=Loan_Account_strategy)
def test_loan_account_Acc_No_setter(instance):
    original = instance.Acc_No
    instance.Acc_No = original
    assert instance.Acc_No == original

@given(instance=Savings_Account_strategy)
@settings(max_examples=50)
def test_savings_account_instantiation(instance):
    assert isinstance(instance, Savings_Account)



@given(instance=Savings_Account_strategy)
def test_savings_account_PIn_setter(instance):
    original = instance.PIn
    instance.PIn = original
    assert instance.PIn == original



@given(instance=Savings_Account_strategy)
def test_savings_account_Holder_Name_setter(instance):
    original = instance.Holder_Name
    instance.Holder_Name = original
    assert instance.Holder_Name == original



@given(instance=Savings_Account_strategy)
def test_savings_account_AccNo_setter(instance):
    original = instance.AccNo
    instance.AccNo = original
    assert instance.AccNo == original

@given(instance=CurrentAccount_strategy)
@settings(max_examples=50)
def test_currentaccount_instantiation(instance):
    assert isinstance(instance, CurrentAccount)



@given(instance=CurrentAccount_strategy)
def test_currentaccount_HolderName_setter(instance):
    original = instance.HolderName
    instance.HolderName = original
    assert instance.HolderName == original



@given(instance=CurrentAccount_strategy)
def test_currentaccount_AccNo_setter(instance):
    original = instance.AccNo
    instance.AccNo = original
    assert instance.AccNo == original



@given(instance=CurrentAccount_strategy)
def test_currentaccount_PIn_setter(instance):
    original = instance.PIn
    instance.PIn = original
    assert instance.PIn == original

@given(instance=ATM_s_strategy)
@settings(max_examples=50)
def test_atm_s_instantiation(instance):
    assert isinstance(instance, ATM_s)



@given(instance=ATM_s_strategy)
def test_atm_s_PIN_setter(instance):
    original = instance.PIN
    instance.PIN = original
    assert instance.PIN == original



@given(instance=ATM_s_strategy)
def test_atm_s_Withdrawn_setter(instance):
    original = instance.Withdrawn
    instance.Withdrawn = original
    assert instance.Withdrawn == original



@given(instance=ATM_s_strategy)
def test_atm_s_OperatorName_setter(instance):
    original = instance.OperatorName
    instance.OperatorName = original
    assert instance.OperatorName == original

@given(instance=AccountHolder_strategy)
@settings(max_examples=50)
def test_accountholder_instantiation(instance):
    assert isinstance(instance, AccountHolder)



@given(instance=AccountHolder_strategy)
def test_accountholder_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=AccountHolder_strategy)
def test_accountholder_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=AccountHolder_strategy)
def test_accountholder_AccNo_setter(instance):
    original = instance.AccNo
    instance.AccNo = original
    assert instance.AccNo == original

@given(instance=BankEmployee_strategy)
@settings(max_examples=50)
def test_bankemployee_instantiation(instance):
    assert isinstance(instance, BankEmployee)



@given(instance=BankEmployee_strategy)
def test_bankemployee_EmpAdd_setter(instance):
    original = instance.EmpAdd
    instance.EmpAdd = original
    assert instance.EmpAdd == original



@given(instance=BankEmployee_strategy)
def test_bankemployee_EmployeeID_setter(instance):
    original = instance.EmployeeID
    instance.EmployeeID = original
    assert instance.EmployeeID == original



@given(instance=BankEmployee_strategy)
def test_bankemployee_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=BankEmployee_strategy)
def test_bankemployee_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original

@given(instance=Accounts_strategy)
@settings(max_examples=50)
def test_accounts_instantiation(instance):
    assert isinstance(instance, Accounts)



@given(instance=Accounts_strategy)
def test_accounts_AccountNo_setter(instance):
    original = instance.AccountNo
    instance.AccountNo = original
    assert instance.AccountNo == original



@given(instance=Accounts_strategy)
def test_accounts_branchCode_setter(instance):
    original = instance.branchCode
    instance.branchCode = original
    assert instance.branchCode == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_locality_setter(instance):
    original = instance.locality
    instance.locality = original
    assert instance.locality == original



@given(instance=Bank_strategy)
def test_bank_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Bank_strategy)
def test_bank_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Bank_strategy)
def test_bank_Name_string_setter(instance):
    original = instance.Name_string
    instance.Name_string = original
    assert instance.Name_string == original
