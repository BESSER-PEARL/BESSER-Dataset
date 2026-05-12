import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Indevidual,
    Business,
    Permanent,
    Contractor,
    Temporary,
    CheckingAccount,
    SavingsAccount,
    Customer,
    Employee,
    BMS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_indevidual_is_not_abstract():
    assert not inspect.isabstract(Indevidual)


def test_indevidual_constructor_exists():
    assert callable(Indevidual.__init__)


def test_indevidual_constructor_args():
    sig = inspect.signature(Indevidual.__init__)
    params = list(sig.parameters.keys())



def test_business_is_not_abstract():
    assert not inspect.isabstract(Business)


def test_business_constructor_exists():
    assert callable(Business.__init__)


def test_business_constructor_args():
    sig = inspect.signature(Business.__init__)
    params = list(sig.parameters.keys())



def test_permanent_is_not_abstract():
    assert not inspect.isabstract(Permanent)


def test_permanent_constructor_exists():
    assert callable(Permanent.__init__)


def test_permanent_constructor_args():
    sig = inspect.signature(Permanent.__init__)
    params = list(sig.parameters.keys())



def test_contractor_is_not_abstract():
    assert not inspect.isabstract(Contractor)


def test_contractor_constructor_exists():
    assert callable(Contractor.__init__)


def test_contractor_constructor_args():
    sig = inspect.signature(Contractor.__init__)
    params = list(sig.parameters.keys())



def test_temporary_is_not_abstract():
    assert not inspect.isabstract(Temporary)


def test_temporary_constructor_exists():
    assert callable(Temporary.__init__)


def test_temporary_constructor_args():
    sig = inspect.signature(Temporary.__init__)
    params = list(sig.parameters.keys())



def test_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(CheckingAccount)


def test_checkingaccount_constructor_exists():
    assert callable(CheckingAccount.__init__)


def test_checkingaccount_constructor_args():
    sig = inspect.signature(CheckingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "Diposit" in params, "Missing parameter 'Diposit'"
    assert "AccountNo" in params, "Missing parameter 'AccountNo'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Cust_DOB" in params, "Missing parameter 'Cust_DOB'"
    assert "Withdraw" in params, "Missing parameter 'Withdraw'"
    assert "MobileNo" in params, "Missing parameter 'MobileNo'"
    assert "Cust_Name" in params, "Missing parameter 'Cust_Name'"
    assert "AccountType" in params, "Missing parameter 'AccountType'"
    assert "CustomerId" in params, "Missing parameter 'CustomerId'"

def test_checkingaccount_has_Diposit():
    assert hasattr(CheckingAccount, "Diposit")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "Diposit" in klass.__dict__:
            descriptor = klass.__dict__["Diposit"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_AccountNo():
    assert hasattr(CheckingAccount, "AccountNo")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "AccountNo" in klass.__dict__:
            descriptor = klass.__dict__["AccountNo"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_Amount():
    assert hasattr(CheckingAccount, "Amount")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_Cust_DOB():
    assert hasattr(CheckingAccount, "Cust_DOB")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "Cust_DOB" in klass.__dict__:
            descriptor = klass.__dict__["Cust_DOB"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_Withdraw():
    assert hasattr(CheckingAccount, "Withdraw")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "Withdraw" in klass.__dict__:
            descriptor = klass.__dict__["Withdraw"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_MobileNo():
    assert hasattr(CheckingAccount, "MobileNo")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "MobileNo" in klass.__dict__:
            descriptor = klass.__dict__["MobileNo"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_Cust_Name():
    assert hasattr(CheckingAccount, "Cust_Name")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "Cust_Name" in klass.__dict__:
            descriptor = klass.__dict__["Cust_Name"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_AccountType():
    assert hasattr(CheckingAccount, "AccountType")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "AccountType" in klass.__dict__:
            descriptor = klass.__dict__["AccountType"]
            break
    assert isinstance(descriptor, property)

def test_checkingaccount_has_CustomerId():
    assert hasattr(CheckingAccount, "CustomerId")
    descriptor = None
    for klass in CheckingAccount.__mro__:
        if "CustomerId" in klass.__dict__:
            descriptor = klass.__dict__["CustomerId"]
            break
    assert isinstance(descriptor, property)



def test_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(SavingsAccount)


def test_savingsaccount_constructor_exists():
    assert callable(SavingsAccount.__init__)


def test_savingsaccount_constructor_args():
    sig = inspect.signature(SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Cust_Name" in params, "Missing parameter 'Cust_Name'"
    assert "CustomerId" in params, "Missing parameter 'CustomerId'"
    assert "Diposit" in params, "Missing parameter 'Diposit'"
    assert "Cust_DOB" in params, "Missing parameter 'Cust_DOB'"
    assert "AccountType" in params, "Missing parameter 'AccountType'"
    assert "Withdraw" in params, "Missing parameter 'Withdraw'"
    assert "AccountNo" in params, "Missing parameter 'AccountNo'"
    assert "Mobile" in params, "Missing parameter 'Mobile'"

def test_savingsaccount_has_Amount():
    assert hasattr(SavingsAccount, "Amount")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_Cust_Name():
    assert hasattr(SavingsAccount, "Cust_Name")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "Cust_Name" in klass.__dict__:
            descriptor = klass.__dict__["Cust_Name"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_CustomerId():
    assert hasattr(SavingsAccount, "CustomerId")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "CustomerId" in klass.__dict__:
            descriptor = klass.__dict__["CustomerId"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_Diposit():
    assert hasattr(SavingsAccount, "Diposit")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "Diposit" in klass.__dict__:
            descriptor = klass.__dict__["Diposit"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_Cust_DOB():
    assert hasattr(SavingsAccount, "Cust_DOB")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "Cust_DOB" in klass.__dict__:
            descriptor = klass.__dict__["Cust_DOB"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_AccountType():
    assert hasattr(SavingsAccount, "AccountType")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "AccountType" in klass.__dict__:
            descriptor = klass.__dict__["AccountType"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_Withdraw():
    assert hasattr(SavingsAccount, "Withdraw")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "Withdraw" in klass.__dict__:
            descriptor = klass.__dict__["Withdraw"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_AccountNo():
    assert hasattr(SavingsAccount, "AccountNo")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "AccountNo" in klass.__dict__:
            descriptor = klass.__dict__["AccountNo"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_Mobile():
    assert hasattr(SavingsAccount, "Mobile")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "Mobile" in klass.__dict__:
            descriptor = klass.__dict__["Mobile"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "State" in params, "Missing parameter 'State'"
    assert "CustId" in params, "Missing parameter 'CustId'"
    assert "FName" in params, "Missing parameter 'FName'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Lname" in params, "Missing parameter 'Lname'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "Zipcode" in params, "Missing parameter 'Zipcode'"
    assert "Mobile" in params, "Missing parameter 'Mobile'"

def test_customer_has_DOB():
    assert hasattr(Customer, "DOB")
    descriptor = None
    for klass in Customer.__mro__:
        if "DOB" in klass.__dict__:
            descriptor = klass.__dict__["DOB"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_State():
    assert hasattr(Customer, "State")
    descriptor = None
    for klass in Customer.__mro__:
        if "State" in klass.__dict__:
            descriptor = klass.__dict__["State"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_CustId():
    assert hasattr(Customer, "CustId")
    descriptor = None
    for klass in Customer.__mro__:
        if "CustId" in klass.__dict__:
            descriptor = klass.__dict__["CustId"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_FName():
    assert hasattr(Customer, "FName")
    descriptor = None
    for klass in Customer.__mro__:
        if "FName" in klass.__dict__:
            descriptor = klass.__dict__["FName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Address():
    assert hasattr(Customer, "Address")
    descriptor = None
    for klass in Customer.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Lname():
    assert hasattr(Customer, "Lname")
    descriptor = None
    for klass in Customer.__mro__:
        if "Lname" in klass.__dict__:
            descriptor = klass.__dict__["Lname"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Gender():
    assert hasattr(Customer, "Gender")
    descriptor = None
    for klass in Customer.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_attribute():
    assert hasattr(Customer, "attribute")
    descriptor = None
    for klass in Customer.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Zipcode():
    assert hasattr(Customer, "Zipcode")
    descriptor = None
    for klass in Customer.__mro__:
        if "Zipcode" in klass.__dict__:
            descriptor = klass.__dict__["Zipcode"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Mobile():
    assert hasattr(Customer, "Mobile")
    descriptor = None
    for klass in Customer.__mro__:
        if "Mobile" in klass.__dict__:
            descriptor = klass.__dict__["Mobile"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "EmpId" in params, "Missing parameter 'EmpId'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "City" in params, "Missing parameter 'City'"
    assert "EmpType" in params, "Missing parameter 'EmpType'"
    assert "Zipcode" in params, "Missing parameter 'Zipcode'"
    assert "EmpLName" in params, "Missing parameter 'EmpLName'"
    assert "State" in params, "Missing parameter 'State'"
    assert "Department" in params, "Missing parameter 'Department'"
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "EmpFName" in params, "Missing parameter 'EmpFName'"

def test_employee_has_EmpId():
    assert hasattr(Employee, "EmpId")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmpId" in klass.__dict__:
            descriptor = klass.__dict__["EmpId"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Gender():
    assert hasattr(Employee, "Gender")
    descriptor = None
    for klass in Employee.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_City():
    assert hasattr(Employee, "City")
    descriptor = None
    for klass in Employee.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmpType():
    assert hasattr(Employee, "EmpType")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmpType" in klass.__dict__:
            descriptor = klass.__dict__["EmpType"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Zipcode():
    assert hasattr(Employee, "Zipcode")
    descriptor = None
    for klass in Employee.__mro__:
        if "Zipcode" in klass.__dict__:
            descriptor = klass.__dict__["Zipcode"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmpLName():
    assert hasattr(Employee, "EmpLName")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmpLName" in klass.__dict__:
            descriptor = klass.__dict__["EmpLName"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_State():
    assert hasattr(Employee, "State")
    descriptor = None
    for klass in Employee.__mro__:
        if "State" in klass.__dict__:
            descriptor = klass.__dict__["State"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Department():
    assert hasattr(Employee, "Department")
    descriptor = None
    for klass in Employee.__mro__:
        if "Department" in klass.__dict__:
            descriptor = klass.__dict__["Department"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_DOB():
    assert hasattr(Employee, "DOB")
    descriptor = None
    for klass in Employee.__mro__:
        if "DOB" in klass.__dict__:
            descriptor = klass.__dict__["DOB"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Address():
    assert hasattr(Employee, "Address")
    descriptor = None
    for klass in Employee.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmpFName():
    assert hasattr(Employee, "EmpFName")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmpFName" in klass.__dict__:
            descriptor = klass.__dict__["EmpFName"]
            break
    assert isinstance(descriptor, property)



def test_bms_is_not_abstract():
    assert not inspect.isabstract(BMS)


def test_bms_constructor_exists():
    assert callable(BMS.__init__)


def test_bms_constructor_args():
    sig = inspect.signature(BMS.__init__)
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
Indevidual_strategy = st.builds(
    Indevidual,
)
Business_strategy = st.builds(
    Business,
)
Permanent_strategy = st.builds(
    Permanent,
)
Contractor_strategy = st.builds(
    Contractor,
)
Temporary_strategy = st.builds(
    Temporary,
)
CheckingAccount_strategy = st.builds(
    CheckingAccount,
    Diposit=
        safe_text,
    AccountNo=
        st.integers(),
    Amount=
        safe_text,
    Cust_DOB=
        safe_text,
    Withdraw=
        safe_text,
    MobileNo=
        st.integers(),
    Cust_Name=
        safe_text,
    AccountType=
        safe_text,
    CustomerId=
        st.integers()
)
SavingsAccount_strategy = st.builds(
    SavingsAccount,
    Amount=
        safe_text,
    Cust_Name=
        safe_text,
    CustomerId=
        st.integers(),
    Diposit=
        safe_text,
    Cust_DOB=
        safe_text,
    AccountType=
        safe_text,
    Withdraw=
        safe_text,
    AccountNo=
        st.integers(),
    Mobile=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    DOB=
        safe_text,
    State=
        safe_text,
    CustId=
        st.integers(),
    FName=
        safe_text,
    Address=
        safe_text,
    Lname=
        safe_text,
    Gender=
        safe_text,
    attribute=
        safe_text,
    Zipcode=
        st.integers(),
    Mobile=
        st.integers()
)
Employee_strategy = st.builds(
    Employee,
    EmpId=
        st.integers(),
    Gender=
        safe_text,
    City=
        safe_text,
    EmpType=
        safe_text,
    Zipcode=
        safe_text,
    EmpLName=
        safe_text,
    State=
        safe_text,
    Department=
        safe_text,
    DOB=
        safe_text,
    Address=
        safe_text,
    EmpFName=
        safe_text
)
BMS_strategy = st.builds(
    BMS,
)

@given(instance=Indevidual_strategy)
@settings(max_examples=50)
def test_indevidual_instantiation(instance):
    assert isinstance(instance, Indevidual)

@given(instance=Business_strategy)
@settings(max_examples=50)
def test_business_instantiation(instance):
    assert isinstance(instance, Business)

@given(instance=Permanent_strategy)
@settings(max_examples=50)
def test_permanent_instantiation(instance):
    assert isinstance(instance, Permanent)

@given(instance=Contractor_strategy)
@settings(max_examples=50)
def test_contractor_instantiation(instance):
    assert isinstance(instance, Contractor)

@given(instance=Temporary_strategy)
@settings(max_examples=50)
def test_temporary_instantiation(instance):
    assert isinstance(instance, Temporary)

@given(instance=CheckingAccount_strategy)
@settings(max_examples=50)
def test_checkingaccount_instantiation(instance):
    assert isinstance(instance, CheckingAccount)



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_Diposit_setter(instance):
    original = instance.Diposit
    instance.Diposit = original
    assert instance.Diposit == original



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_AccountNo_setter(instance):
    original = instance.AccountNo
    instance.AccountNo = original
    assert instance.AccountNo == original



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_Cust_DOB_setter(instance):
    original = instance.Cust_DOB
    instance.Cust_DOB = original
    assert instance.Cust_DOB == original



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_Withdraw_setter(instance):
    original = instance.Withdraw
    instance.Withdraw = original
    assert instance.Withdraw == original



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_MobileNo_setter(instance):
    original = instance.MobileNo
    instance.MobileNo = original
    assert instance.MobileNo == original



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_Cust_Name_setter(instance):
    original = instance.Cust_Name
    instance.Cust_Name = original
    assert instance.Cust_Name == original



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_AccountType_setter(instance):
    original = instance.AccountType
    instance.AccountType = original
    assert instance.AccountType == original



@given(instance=CheckingAccount_strategy)
def test_checkingaccount_CustomerId_setter(instance):
    original = instance.CustomerId
    instance.CustomerId = original
    assert instance.CustomerId == original

@given(instance=SavingsAccount_strategy)
@settings(max_examples=50)
def test_savingsaccount_instantiation(instance):
    assert isinstance(instance, SavingsAccount)



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_Cust_Name_setter(instance):
    original = instance.Cust_Name
    instance.Cust_Name = original
    assert instance.Cust_Name == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_CustomerId_setter(instance):
    original = instance.CustomerId
    instance.CustomerId = original
    assert instance.CustomerId == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_Diposit_setter(instance):
    original = instance.Diposit
    instance.Diposit = original
    assert instance.Diposit == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_Cust_DOB_setter(instance):
    original = instance.Cust_DOB
    instance.Cust_DOB = original
    assert instance.Cust_DOB == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_AccountType_setter(instance):
    original = instance.AccountType
    instance.AccountType = original
    assert instance.AccountType == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_Withdraw_setter(instance):
    original = instance.Withdraw
    instance.Withdraw = original
    assert instance.Withdraw == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_AccountNo_setter(instance):
    original = instance.AccountNo
    instance.AccountNo = original
    assert instance.AccountNo == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_Mobile_setter(instance):
    original = instance.Mobile
    instance.Mobile = original
    assert instance.Mobile == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=Customer_strategy)
def test_customer_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original



@given(instance=Customer_strategy)
def test_customer_CustId_setter(instance):
    original = instance.CustId
    instance.CustId = original
    assert instance.CustId == original



@given(instance=Customer_strategy)
def test_customer_FName_setter(instance):
    original = instance.FName
    instance.FName = original
    assert instance.FName == original



@given(instance=Customer_strategy)
def test_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_customer_Lname_setter(instance):
    original = instance.Lname
    instance.Lname = original
    assert instance.Lname == original



@given(instance=Customer_strategy)
def test_customer_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Customer_strategy)
def test_customer_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Customer_strategy)
def test_customer_Zipcode_setter(instance):
    original = instance.Zipcode
    instance.Zipcode = original
    assert instance.Zipcode == original



@given(instance=Customer_strategy)
def test_customer_Mobile_setter(instance):
    original = instance.Mobile
    instance.Mobile = original
    assert instance.Mobile == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_EmpId_setter(instance):
    original = instance.EmpId
    instance.EmpId = original
    assert instance.EmpId == original



@given(instance=Employee_strategy)
def test_employee_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Employee_strategy)
def test_employee_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=Employee_strategy)
def test_employee_EmpType_setter(instance):
    original = instance.EmpType
    instance.EmpType = original
    assert instance.EmpType == original



@given(instance=Employee_strategy)
def test_employee_Zipcode_setter(instance):
    original = instance.Zipcode
    instance.Zipcode = original
    assert instance.Zipcode == original



@given(instance=Employee_strategy)
def test_employee_EmpLName_setter(instance):
    original = instance.EmpLName
    instance.EmpLName = original
    assert instance.EmpLName == original



@given(instance=Employee_strategy)
def test_employee_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original



@given(instance=Employee_strategy)
def test_employee_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original



@given(instance=Employee_strategy)
def test_employee_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=Employee_strategy)
def test_employee_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Employee_strategy)
def test_employee_EmpFName_setter(instance):
    original = instance.EmpFName
    instance.EmpFName = original
    assert instance.EmpFName == original

@given(instance=BMS_strategy)
@settings(max_examples=50)
def test_bms_instantiation(instance):
    assert isinstance(instance, BMS)
