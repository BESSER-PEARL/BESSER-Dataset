import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Setting,
    Transaction,
    Manager,
    Employee,
    User,
    Customer,
    Current_Account,
    Saving_Account,
    Account,
    Branch,
    Bank,
    TransactionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_setting_is_not_abstract():
    assert not inspect.isabstract(Setting)


def test_setting_constructor_exists():
    assert callable(Setting.__init__)


def test_setting_constructor_args():
    sig = inspect.signature(Setting.__init__)
    params = list(sig.parameters.keys())



def test_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "date" in params, "Missing parameter 'date'"
    assert "currentBalance" in params, "Missing parameter 'currentBalance'"
    assert "Acc_num" in params, "Missing parameter 'Acc_num'"
    assert "TranId" in params, "Missing parameter 'TranId'"
    assert "status" in params, "Missing parameter 'status'"
    assert "prevBalance" in params, "Missing parameter 'prevBalance'"
    assert "type" in params, "Missing parameter 'type'"

def test_transaction_has_amount():
    assert hasattr(Transaction, "amount")
    descriptor = None
    for klass in Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_date():
    assert hasattr(Transaction, "date")
    descriptor = None
    for klass in Transaction.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_currentBalance():
    assert hasattr(Transaction, "currentBalance")
    descriptor = None
    for klass in Transaction.__mro__:
        if "currentBalance" in klass.__dict__:
            descriptor = klass.__dict__["currentBalance"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_Acc_num():
    assert hasattr(Transaction, "Acc_num")
    descriptor = None
    for klass in Transaction.__mro__:
        if "Acc_num" in klass.__dict__:
            descriptor = klass.__dict__["Acc_num"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_TranId():
    assert hasattr(Transaction, "TranId")
    descriptor = None
    for klass in Transaction.__mro__:
        if "TranId" in klass.__dict__:
            descriptor = klass.__dict__["TranId"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_status():
    assert hasattr(Transaction, "status")
    descriptor = None
    for klass in Transaction.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_transaction_has_prevBalance():
    assert hasattr(Transaction, "prevBalance")
    descriptor = None
    for klass in Transaction.__mro__:
        if "prevBalance" in klass.__dict__:
            descriptor = klass.__dict__["prevBalance"]
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



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Mid" in params, "Missing parameter 'Mid'"
    assert "Eid" in params, "Missing parameter 'Eid'"

def test_employee_has_Mid():
    assert hasattr(Employee, "Mid")
    descriptor = None
    for klass in Employee.__mro__:
        if "Mid" in klass.__dict__:
            descriptor = klass.__dict__["Mid"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Eid():
    assert hasattr(Employee, "Eid")
    descriptor = None
    for klass in Employee.__mro__:
        if "Eid" in klass.__dict__:
            descriptor = klass.__dict__["Eid"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "family" in params, "Missing parameter 'family'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_user_has_family():
    assert hasattr(User, "family")
    descriptor = None
    for klass in User.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
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

def test_user_has_userName():
    assert hasattr(User, "userName")
    descriptor = None
    for klass in User.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_user_has_uid():
    assert hasattr(User, "uid")
    descriptor = None
    for klass in User.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_user_has_name():
    assert hasattr(User, "name")
    descriptor = None
    for klass in User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Cust_id" in params, "Missing parameter 'Cust_id'"
    assert "phone" in params, "Missing parameter 'phone'"

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

def test_customer_has_Cust_id():
    assert hasattr(Customer, "Cust_id")
    descriptor = None
    for klass in Customer.__mro__:
        if "Cust_id" in klass.__dict__:
            descriptor = klass.__dict__["Cust_id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_phone():
    assert hasattr(Customer, "phone")
    descriptor = None
    for klass in Customer.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)



def test_current_account_is_not_abstract():
    assert not inspect.isabstract(Current_Account)


def test_current_account_constructor_exists():
    assert callable(Current_Account.__init__)


def test_current_account_constructor_args():
    sig = inspect.signature(Current_Account.__init__)
    params = list(sig.parameters.keys())



def test_saving_account_is_not_abstract():
    assert not inspect.isabstract(Saving_Account)


def test_saving_account_constructor_exists():
    assert callable(Saving_Account.__init__)


def test_saving_account_constructor_args():
    sig = inspect.signature(Saving_Account.__init__)
    params = list(sig.parameters.keys())
    assert "interest_Rate" in params, "Missing parameter 'interest_Rate'"

def test_saving_account_has_interest_Rate():
    assert hasattr(Saving_Account, "interest_Rate")
    descriptor = None
    for klass in Saving_Account.__mro__:
        if "interest_Rate" in klass.__dict__:
            descriptor = klass.__dict__["interest_Rate"]
            break
    assert isinstance(descriptor, property)



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "date_Of_Opening" in params, "Missing parameter 'date_Of_Opening'"
    assert "Balance" in params, "Missing parameter 'Balance'"
    assert "min_Balance" in params, "Missing parameter 'min_Balance'"
    assert "Acc_no" in params, "Missing parameter 'Acc_no'"

def test_account_has_date_Of_Opening():
    assert hasattr(Account, "date_Of_Opening")
    descriptor = None
    for klass in Account.__mro__:
        if "date_Of_Opening" in klass.__dict__:
            descriptor = klass.__dict__["date_Of_Opening"]
            break
    assert isinstance(descriptor, property)

def test_account_has_Balance():
    assert hasattr(Account, "Balance")
    descriptor = None
    for klass in Account.__mro__:
        if "Balance" in klass.__dict__:
            descriptor = klass.__dict__["Balance"]
            break
    assert isinstance(descriptor, property)

def test_account_has_min_Balance():
    assert hasattr(Account, "min_Balance")
    descriptor = None
    for klass in Account.__mro__:
        if "min_Balance" in klass.__dict__:
            descriptor = klass.__dict__["min_Balance"]
            break
    assert isinstance(descriptor, property)

def test_account_has_Acc_no():
    assert hasattr(Account, "Acc_no")
    descriptor = None
    for klass in Account.__mro__:
        if "Acc_no" in klass.__dict__:
            descriptor = klass.__dict__["Acc_no"]
            break
    assert isinstance(descriptor, property)



def test_branch_is_not_abstract():
    assert not inspect.isabstract(Branch)


def test_branch_constructor_exists():
    assert callable(Branch.__init__)


def test_branch_constructor_args():
    sig = inspect.signature(Branch.__init__)
    params = list(sig.parameters.keys())
    assert "Branch_code" in params, "Missing parameter 'Branch_code'"
    assert "City" in params, "Missing parameter 'City'"

def test_branch_has_Branch_code():
    assert hasattr(Branch, "Branch_code")
    descriptor = None
    for klass in Branch.__mro__:
        if "Branch_code" in klass.__dict__:
            descriptor = klass.__dict__["Branch_code"]
            break
    assert isinstance(descriptor, property)

def test_branch_has_City():
    assert hasattr(Branch, "City")
    descriptor = None
    for klass in Branch.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Code" in params, "Missing parameter 'Code'"

def test_bank_has_Name():
    assert hasattr(Bank, "Name")
    descriptor = None
    for klass in Bank.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_Code():
    assert hasattr(Bank, "Code")
    descriptor = None
    for klass in Bank.__mro__:
        if "Code" in klass.__dict__:
            descriptor = klass.__dict__["Code"]
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
Setting_strategy = st.builds(
    Setting,
)
Transaction_strategy = st.builds(
    Transaction,
    amount=
        st.integers(),
    date=
        safe_text,
    currentBalance=
        st.integers(),
    Acc_num=
        st.integers(),
    TranId=
        st.integers(),
    status=
        safe_text,
    prevBalance=
        st.integers(),
    type=
        st.none()
)
Manager_strategy = st.builds(
    Manager,
)
Employee_strategy = st.builds(
    Employee,
    Mid=
        st.integers(),
    Eid=
        st.integers()
)
User_strategy = st.builds(
    User,
    family=
        safe_text,
    password=
        safe_text,
    userName=
        safe_text,
    uid=
        st.integers(),
    name=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    address=
        safe_text,
    name=
        safe_text,
    Cust_id=
        safe_text,
    phone=
        safe_text
)
Current_Account_strategy = st.builds(
    Current_Account,
)
Saving_Account_strategy = st.builds(
    Saving_Account,
    interest_Rate=
        st.integers()
)
Account_strategy = st.builds(
    Account,
    date_Of_Opening=
        safe_text,
    Balance=
        st.integers(),
    min_Balance=
        st.integers(),
    Acc_no=
        st.integers()
)
Branch_strategy = st.builds(
    Branch,
    Branch_code=
        safe_text,
    City=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    Name=
        safe_text,
    Code=
        safe_text
)

@given(instance=Setting_strategy)
@settings(max_examples=50)
def test_setting_instantiation(instance):
    assert isinstance(instance, Setting)

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



@given(instance=Transaction_strategy)
def test_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction_strategy)
def test_transaction_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Transaction_strategy)
def test_transaction_currentBalance_setter(instance):
    original = instance.currentBalance
    instance.currentBalance = original
    assert instance.currentBalance == original



@given(instance=Transaction_strategy)
def test_transaction_Acc_num_setter(instance):
    original = instance.Acc_num
    instance.Acc_num = original
    assert instance.Acc_num == original



@given(instance=Transaction_strategy)
def test_transaction_TranId_setter(instance):
    original = instance.TranId
    instance.TranId = original
    assert instance.TranId == original



@given(instance=Transaction_strategy)
def test_transaction_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Transaction_strategy)
def test_transaction_prevBalance_setter(instance):
    original = instance.prevBalance
    instance.prevBalance = original
    assert instance.prevBalance == original



@given(instance=Transaction_strategy)
def test_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Mid_setter(instance):
    original = instance.Mid
    instance.Mid = original
    assert instance.Mid == original



@given(instance=Employee_strategy)
def test_employee_Eid_setter(instance):
    original = instance.Eid
    instance.Eid = original
    assert instance.Eid == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=User_strategy)
def test_user_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=User_strategy)
def test_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



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
def test_customer_Cust_id_setter(instance):
    original = instance.Cust_id
    instance.Cust_id = original
    assert instance.Cust_id == original



@given(instance=Customer_strategy)
def test_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=Current_Account_strategy)
@settings(max_examples=50)
def test_current_account_instantiation(instance):
    assert isinstance(instance, Current_Account)

@given(instance=Saving_Account_strategy)
@settings(max_examples=50)
def test_saving_account_instantiation(instance):
    assert isinstance(instance, Saving_Account)



@given(instance=Saving_Account_strategy)
def test_saving_account_interest_Rate_setter(instance):
    original = instance.interest_Rate
    instance.interest_Rate = original
    assert instance.interest_Rate == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_date_Of_Opening_setter(instance):
    original = instance.date_Of_Opening
    instance.date_Of_Opening = original
    assert instance.date_Of_Opening == original



@given(instance=Account_strategy)
def test_account_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original



@given(instance=Account_strategy)
def test_account_min_Balance_setter(instance):
    original = instance.min_Balance
    instance.min_Balance = original
    assert instance.min_Balance == original



@given(instance=Account_strategy)
def test_account_Acc_no_setter(instance):
    original = instance.Acc_no
    instance.Acc_no = original
    assert instance.Acc_no == original

@given(instance=Branch_strategy)
@settings(max_examples=50)
def test_branch_instantiation(instance):
    assert isinstance(instance, Branch)



@given(instance=Branch_strategy)
def test_branch_Branch_code_setter(instance):
    original = instance.Branch_code
    instance.Branch_code = original
    assert instance.Branch_code == original



@given(instance=Branch_strategy)
def test_branch_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Bank_strategy)
def test_bank_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original
