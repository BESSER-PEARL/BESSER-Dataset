import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Employee,
    Account,
    BankingSystem_Saving,
    BankingSystem_Chequing,
    BankingSystem_Financial_Representative,
    BankingSystem_Loan,
    BankingSystem_Account,
    BankingSystem_Employee,
    BankingSystem_Customer,
    BankingSystem_Branch,
    BankingSystem_Bank,
    CustomerType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())



def test_bankingsystem_saving_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Saving)


def test_bankingsystem_saving_constructor_exists():
    assert callable(BankingSystem_Saving.__init__)


def test_bankingsystem_saving_constructor_args():
    sig = inspect.signature(BankingSystem_Saving.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_bankingsystem_saving_has_interestRate():
    assert hasattr(BankingSystem_Saving, "interestRate")
    descriptor = None
    for klass in BankingSystem_Saving.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem_chequing_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Chequing)


def test_bankingsystem_chequing_constructor_exists():
    assert callable(BankingSystem_Chequing.__init__)


def test_bankingsystem_chequing_constructor_args():
    sig = inspect.signature(BankingSystem_Chequing.__init__)
    params = list(sig.parameters.keys())



def test_bankingsystem_financial_representative_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Financial_Representative)


def test_bankingsystem_financial_representative_constructor_exists():
    assert callable(BankingSystem_Financial_Representative.__init__)


def test_bankingsystem_financial_representative_constructor_args():
    sig = inspect.signature(BankingSystem_Financial_Representative.__init__)
    params = list(sig.parameters.keys())



def test_bankingsystem_loan_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Loan)


def test_bankingsystem_loan_constructor_exists():
    assert callable(BankingSystem_Loan.__init__)


def test_bankingsystem_loan_constructor_args():
    sig = inspect.signature(BankingSystem_Loan.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "loanNumber" in params, "Missing parameter 'loanNumber'"

def test_bankingsystem_loan_has_interestRate():
    assert hasattr(BankingSystem_Loan, "interestRate")
    descriptor = None
    for klass in BankingSystem_Loan.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_loan_has_amount():
    assert hasattr(BankingSystem_Loan, "amount")
    descriptor = None
    for klass in BankingSystem_Loan.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_loan_has_duration():
    assert hasattr(BankingSystem_Loan, "duration")
    descriptor = None
    for klass in BankingSystem_Loan.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_loan_has_loanNumber():
    assert hasattr(BankingSystem_Loan, "loanNumber")
    descriptor = None
    for klass in BankingSystem_Loan.__mro__:
        if "loanNumber" in klass.__dict__:
            descriptor = klass.__dict__["loanNumber"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem_account_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Account)


def test_bankingsystem_account_constructor_exists():
    assert callable(BankingSystem_Account.__init__)


def test_bankingsystem_account_constructor_args():
    sig = inspect.signature(BankingSystem_Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"

def test_bankingsystem_account_has_balance():
    assert hasattr(BankingSystem_Account, "balance")
    descriptor = None
    for klass in BankingSystem_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_account_has_accountNumber():
    assert hasattr(BankingSystem_Account, "accountNumber")
    descriptor = None
    for klass in BankingSystem_Account.__mro__:
        if "accountNumber" in klass.__dict__:
            descriptor = klass.__dict__["accountNumber"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem_employee_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Employee)


def test_bankingsystem_employee_constructor_exists():
    assert callable(BankingSystem_Employee.__init__)


def test_bankingsystem_employee_constructor_args():
    sig = inspect.signature(BankingSystem_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "ephoneNumber" in params, "Missing parameter 'ephoneNumber'"
    assert "eage" in params, "Missing parameter 'eage'"
    assert "eaddress" in params, "Missing parameter 'eaddress'"
    assert "eid" in params, "Missing parameter 'eid'"
    assert "ename" in params, "Missing parameter 'ename'"
    assert "isCustomer" in params, "Missing parameter 'isCustomer'"

def test_bankingsystem_employee_has_ephoneNumber():
    assert hasattr(BankingSystem_Employee, "ephoneNumber")
    descriptor = None
    for klass in BankingSystem_Employee.__mro__:
        if "ephoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["ephoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_employee_has_eage():
    assert hasattr(BankingSystem_Employee, "eage")
    descriptor = None
    for klass in BankingSystem_Employee.__mro__:
        if "eage" in klass.__dict__:
            descriptor = klass.__dict__["eage"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_employee_has_eaddress():
    assert hasattr(BankingSystem_Employee, "eaddress")
    descriptor = None
    for klass in BankingSystem_Employee.__mro__:
        if "eaddress" in klass.__dict__:
            descriptor = klass.__dict__["eaddress"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_employee_has_eid():
    assert hasattr(BankingSystem_Employee, "eid")
    descriptor = None
    for klass in BankingSystem_Employee.__mro__:
        if "eid" in klass.__dict__:
            descriptor = klass.__dict__["eid"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_employee_has_ename():
    assert hasattr(BankingSystem_Employee, "ename")
    descriptor = None
    for klass in BankingSystem_Employee.__mro__:
        if "ename" in klass.__dict__:
            descriptor = klass.__dict__["ename"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_employee_has_isCustomer():
    assert hasattr(BankingSystem_Employee, "isCustomer")
    descriptor = None
    for klass in BankingSystem_Employee.__mro__:
        if "isCustomer" in klass.__dict__:
            descriptor = klass.__dict__["isCustomer"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem_customer_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Customer)


def test_bankingsystem_customer_constructor_exists():
    assert callable(BankingSystem_Customer.__init__)


def test_bankingsystem_customer_constructor_args():
    sig = inspect.signature(BankingSystem_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "customerType" in params, "Missing parameter 'customerType'"
    assert "address" in params, "Missing parameter 'address'"
    assert "age" in params, "Missing parameter 'age'"

def test_bankingsystem_customer_has_phoneNumber():
    assert hasattr(BankingSystem_Customer, "phoneNumber")
    descriptor = None
    for klass in BankingSystem_Customer.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_customer_has_name():
    assert hasattr(BankingSystem_Customer, "name")
    descriptor = None
    for klass in BankingSystem_Customer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_customer_has_customerType():
    assert hasattr(BankingSystem_Customer, "customerType")
    descriptor = None
    for klass in BankingSystem_Customer.__mro__:
        if "customerType" in klass.__dict__:
            descriptor = klass.__dict__["customerType"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_customer_has_address():
    assert hasattr(BankingSystem_Customer, "address")
    descriptor = None
    for klass in BankingSystem_Customer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_customer_has_age():
    assert hasattr(BankingSystem_Customer, "age")
    descriptor = None
    for klass in BankingSystem_Customer.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem_branch_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Branch)


def test_bankingsystem_branch_constructor_exists():
    assert callable(BankingSystem_Branch.__init__)


def test_bankingsystem_branch_constructor_args():
    sig = inspect.signature(BankingSystem_Branch.__init__)
    params = list(sig.parameters.keys())
    assert "branchId" in params, "Missing parameter 'branchId'"
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"

def test_bankingsystem_branch_has_branchId():
    assert hasattr(BankingSystem_Branch, "branchId")
    descriptor = None
    for klass in BankingSystem_Branch.__mro__:
        if "branchId" in klass.__dict__:
            descriptor = klass.__dict__["branchId"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_branch_has_location():
    assert hasattr(BankingSystem_Branch, "location")
    descriptor = None
    for klass in BankingSystem_Branch.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_branch_has_name():
    assert hasattr(BankingSystem_Branch, "name")
    descriptor = None
    for klass in BankingSystem_Branch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_branch_has_phoneNumber():
    assert hasattr(BankingSystem_Branch, "phoneNumber")
    descriptor = None
    for klass in BankingSystem_Branch.__mro__:
        if "phoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["phoneNumber"]
            break
    assert isinstance(descriptor, property)



def test_bankingsystem_bank_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Bank)


def test_bankingsystem_bank_constructor_exists():
    assert callable(BankingSystem_Bank.__init__)


def test_bankingsystem_bank_constructor_args():
    sig = inspect.signature(BankingSystem_Bank.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "bankId" in params, "Missing parameter 'bankId'"
    assert "description" in params, "Missing parameter 'description'"

def test_bankingsystem_bank_has_name():
    assert hasattr(BankingSystem_Bank, "name")
    descriptor = None
    for klass in BankingSystem_Bank.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_bank_has_bankId():
    assert hasattr(BankingSystem_Bank, "bankId")
    descriptor = None
    for klass in BankingSystem_Bank.__mro__:
        if "bankId" in klass.__dict__:
            descriptor = klass.__dict__["bankId"]
            break
    assert isinstance(descriptor, property)

def test_bankingsystem_bank_has_description():
    assert hasattr(BankingSystem_Bank, "description")
    descriptor = None
    for klass in BankingSystem_Bank.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_customertype_exists():
    # Check that the Enumeration exists
    assert CustomerType is not None

def test_customertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CustomerType]
    expected_literals = [
        "Youth",
        "Adult",
        "Senior",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CustomerType"


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
Employee_strategy = st.builds(
    Employee,
)
Account_strategy = st.builds(
    Account,
)
BankingSystem_Saving_strategy = st.builds(
    BankingSystem_Saving,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BankingSystem_Chequing_strategy = st.builds(
    BankingSystem_Chequing,
)
BankingSystem_Financial_Representative_strategy = st.builds(
    BankingSystem_Financial_Representative,
)
BankingSystem_Loan_strategy = st.builds(
    BankingSystem_Loan,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    duration=
        st.integers(),
    loanNumber=
        safe_text
)
BankingSystem_Account_strategy = st.builds(
    BankingSystem_Account,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    accountNumber=
        safe_text
)
BankingSystem_Employee_strategy = st.builds(
    BankingSystem_Employee,
    ephoneNumber=
        safe_text,
    eage=
        st.integers(),
    eaddress=
        safe_text,
    eid=
        st.integers(),
    ename=
        safe_text,
    isCustomer=
        st.booleans()
)
BankingSystem_Customer_strategy = st.builds(
    BankingSystem_Customer,
    phoneNumber=
        safe_text,
    name=
        safe_text,
    customerType=
        safe_text,
    address=
        safe_text,
    age=
        st.integers()
)
BankingSystem_Branch_strategy = st.builds(
    BankingSystem_Branch,
    branchId=
        st.integers(),
    location=
        safe_text,
    name=
        safe_text,
    phoneNumber=
        safe_text
)
BankingSystem_Bank_strategy = st.builds(
    BankingSystem_Bank,
    name=
        safe_text,
    bankId=
        st.integers(),
    description=
        safe_text
)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)

@given(instance=BankingSystem_Saving_strategy)
@settings(max_examples=50)
def test_bankingsystem_saving_instantiation(instance):
    assert isinstance(instance, BankingSystem_Saving)



@given(instance=BankingSystem_Saving_strategy)
def test_bankingsystem_saving_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=BankingSystem_Chequing_strategy)
@settings(max_examples=50)
def test_bankingsystem_chequing_instantiation(instance):
    assert isinstance(instance, BankingSystem_Chequing)

@given(instance=BankingSystem_Financial_Representative_strategy)
@settings(max_examples=50)
def test_bankingsystem_financial_representative_instantiation(instance):
    assert isinstance(instance, BankingSystem_Financial_Representative)

@given(instance=BankingSystem_Loan_strategy)
@settings(max_examples=50)
def test_bankingsystem_loan_instantiation(instance):
    assert isinstance(instance, BankingSystem_Loan)



@given(instance=BankingSystem_Loan_strategy)
def test_bankingsystem_loan_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=BankingSystem_Loan_strategy)
def test_bankingsystem_loan_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=BankingSystem_Loan_strategy)
def test_bankingsystem_loan_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=BankingSystem_Loan_strategy)
def test_bankingsystem_loan_loanNumber_setter(instance):
    original = instance.loanNumber
    instance.loanNumber = original
    assert instance.loanNumber == original

@given(instance=BankingSystem_Account_strategy)
@settings(max_examples=50)
def test_bankingsystem_account_instantiation(instance):
    assert isinstance(instance, BankingSystem_Account)



@given(instance=BankingSystem_Account_strategy)
def test_bankingsystem_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=BankingSystem_Account_strategy)
def test_bankingsystem_account_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original

@given(instance=BankingSystem_Employee_strategy)
@settings(max_examples=50)
def test_bankingsystem_employee_instantiation(instance):
    assert isinstance(instance, BankingSystem_Employee)



@given(instance=BankingSystem_Employee_strategy)
def test_bankingsystem_employee_ephoneNumber_setter(instance):
    original = instance.ephoneNumber
    instance.ephoneNumber = original
    assert instance.ephoneNumber == original



@given(instance=BankingSystem_Employee_strategy)
def test_bankingsystem_employee_eage_setter(instance):
    original = instance.eage
    instance.eage = original
    assert instance.eage == original



@given(instance=BankingSystem_Employee_strategy)
def test_bankingsystem_employee_eaddress_setter(instance):
    original = instance.eaddress
    instance.eaddress = original
    assert instance.eaddress == original



@given(instance=BankingSystem_Employee_strategy)
def test_bankingsystem_employee_eid_setter(instance):
    original = instance.eid
    instance.eid = original
    assert instance.eid == original



@given(instance=BankingSystem_Employee_strategy)
def test_bankingsystem_employee_ename_setter(instance):
    original = instance.ename
    instance.ename = original
    assert instance.ename == original



@given(instance=BankingSystem_Employee_strategy)
def test_bankingsystem_employee_isCustomer_setter(instance):
    original = instance.isCustomer
    instance.isCustomer = original
    assert instance.isCustomer == original

@given(instance=BankingSystem_Customer_strategy)
@settings(max_examples=50)
def test_bankingsystem_customer_instantiation(instance):
    assert isinstance(instance, BankingSystem_Customer)



@given(instance=BankingSystem_Customer_strategy)
def test_bankingsystem_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=BankingSystem_Customer_strategy)
def test_bankingsystem_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BankingSystem_Customer_strategy)
def test_bankingsystem_customer_customerType_setter(instance):
    original = instance.customerType
    instance.customerType = original
    assert instance.customerType == original



@given(instance=BankingSystem_Customer_strategy)
def test_bankingsystem_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=BankingSystem_Customer_strategy)
def test_bankingsystem_customer_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=BankingSystem_Branch_strategy)
@settings(max_examples=50)
def test_bankingsystem_branch_instantiation(instance):
    assert isinstance(instance, BankingSystem_Branch)



@given(instance=BankingSystem_Branch_strategy)
def test_bankingsystem_branch_branchId_setter(instance):
    original = instance.branchId
    instance.branchId = original
    assert instance.branchId == original



@given(instance=BankingSystem_Branch_strategy)
def test_bankingsystem_branch_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=BankingSystem_Branch_strategy)
def test_bankingsystem_branch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BankingSystem_Branch_strategy)
def test_bankingsystem_branch_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original

@given(instance=BankingSystem_Bank_strategy)
@settings(max_examples=50)
def test_bankingsystem_bank_instantiation(instance):
    assert isinstance(instance, BankingSystem_Bank)



@given(instance=BankingSystem_Bank_strategy)
def test_bankingsystem_bank_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BankingSystem_Bank_strategy)
def test_bankingsystem_bank_bankId_setter(instance):
    original = instance.bankId
    instance.bankId = original
    assert instance.bankId == original



@given(instance=BankingSystem_Bank_strategy)
def test_bankingsystem_bank_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
