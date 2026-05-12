import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Logout_external,
    Login_external,
    Manager2,
    Customer1,
    Manager1,
    Order,
    Manager,
    Customer,
    Employee1,
    Admin1,
    Users1,
    Admin,
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Users,
    Leave,
    Salary,
    Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logout_external_is_not_abstract():
    assert not inspect.isabstract(Logout_external)


def test_logout_external_constructor_exists():
    assert callable(Logout_external.__init__)


def test_logout_external_constructor_args():
    sig = inspect.signature(Logout_external.__init__)
    params = list(sig.parameters.keys())



def test_login_external_is_not_abstract():
    assert not inspect.isabstract(Login_external)


def test_login_external_constructor_exists():
    assert callable(Login_external.__init__)


def test_login_external_constructor_args():
    sig = inspect.signature(Login_external.__init__)
    params = list(sig.parameters.keys())



def test_manager2_is_not_abstract():
    assert not inspect.isabstract(Manager2)


def test_manager2_constructor_exists():
    assert callable(Manager2.__init__)


def test_manager2_constructor_args():
    sig = inspect.signature(Manager2.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"

def test_manager2_has_id():
    assert hasattr(Manager2, "id")
    descriptor = None
    for klass in Manager2.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_manager2_has_password():
    assert hasattr(Manager2, "password")
    descriptor = None
    for klass in Manager2.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_manager2_has_name():
    assert hasattr(Manager2, "name")
    descriptor = None
    for klass in Manager2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customer1_is_not_abstract():
    assert not inspect.isabstract(Customer1)


def test_customer1_constructor_exists():
    assert callable(Customer1.__init__)


def test_customer1_constructor_args():
    sig = inspect.signature(Customer1.__init__)
    params = list(sig.parameters.keys())
    assert "S" in params, "Missing parameter 'S'"
    assert "Customer_Name" in params, "Missing parameter 'Customer_Name'"

def test_customer1_has_S():
    assert hasattr(Customer1, "S")
    descriptor = None
    for klass in Customer1.__mro__:
        if "S" in klass.__dict__:
            descriptor = klass.__dict__["S"]
            break
    assert isinstance(descriptor, property)

def test_customer1_has_Customer_Name():
    assert hasattr(Customer1, "Customer_Name")
    descriptor = None
    for klass in Customer1.__mro__:
        if "Customer_Name" in klass.__dict__:
            descriptor = klass.__dict__["Customer_Name"]
            break
    assert isinstance(descriptor, property)



def test_manager1_is_not_abstract():
    assert not inspect.isabstract(Manager1)


def test_manager1_constructor_exists():
    assert callable(Manager1.__init__)


def test_manager1_constructor_args():
    sig = inspect.signature(Manager1.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Manager_id" in params, "Missing parameter 'Manager_id'"

def test_manager1_has_Name():
    assert hasattr(Manager1, "Name")
    descriptor = None
    for klass in Manager1.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_manager1_has_Password():
    assert hasattr(Manager1, "Password")
    descriptor = None
    for klass in Manager1.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_manager1_has_Manager_id():
    assert hasattr(Manager1, "Manager_id")
    descriptor = None
    for klass in Manager1.__mro__:
        if "Manager_id" in klass.__dict__:
            descriptor = klass.__dict__["Manager_id"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_order_has_id():
    assert hasattr(Order, "id")
    descriptor = None
    for klass in Order.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_order_has_name():
    assert hasattr(Order, "name")
    descriptor = None
    for klass in Order.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_manager_has_password():
    assert hasattr(Manager, "password")
    descriptor = None
    for klass in Manager.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_UserName():
    assert hasattr(Manager, "UserName")
    descriptor = None
    for klass in Manager.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "password" in params, "Missing parameter 'password'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "postal_code" in params, "Missing parameter 'postal_code'"
    assert "address" in params, "Missing parameter 'address'"

def test_customer_has_country():
    assert hasattr(Customer, "country")
    descriptor = None
    for klass in Customer.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_password():
    assert hasattr(Customer, "password")
    descriptor = None
    for klass in Customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_UserName():
    assert hasattr(Customer, "UserName")
    descriptor = None
    for klass in Customer.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_postal_code():
    assert hasattr(Customer, "postal_code")
    descriptor = None
    for klass in Customer.__mro__:
        if "postal_code" in klass.__dict__:
            descriptor = klass.__dict__["postal_code"]
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



def test_employee1_is_not_abstract():
    assert not inspect.isabstract(Employee1)


def test_employee1_constructor_exists():
    assert callable(Employee1.__init__)


def test_employee1_constructor_args():
    sig = inspect.signature(Employee1.__init__)
    params = list(sig.parameters.keys())
    assert "contact_no" in params, "Missing parameter 'contact_no'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Emp_Dep" in params, "Missing parameter 'Emp_Dep'"
    assert "password" in params, "Missing parameter 'password'"
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Salary" in params, "Missing parameter 'Salary'"

def test_employee1_has_contact_no():
    assert hasattr(Employee1, "contact_no")
    descriptor = None
    for klass in Employee1.__mro__:
        if "contact_no" in klass.__dict__:
            descriptor = klass.__dict__["contact_no"]
            break
    assert isinstance(descriptor, property)

def test_employee1_has_name():
    assert hasattr(Employee1, "name")
    descriptor = None
    for klass in Employee1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_employee1_has_Email():
    assert hasattr(Employee1, "Email")
    descriptor = None
    for klass in Employee1.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_employee1_has_Emp_Dep():
    assert hasattr(Employee1, "Emp_Dep")
    descriptor = None
    for klass in Employee1.__mro__:
        if "Emp_Dep" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Dep"]
            break
    assert isinstance(descriptor, property)

def test_employee1_has_password():
    assert hasattr(Employee1, "password")
    descriptor = None
    for klass in Employee1.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_employee1_has_Emp_Address():
    assert hasattr(Employee1, "Emp_Address")
    descriptor = None
    for klass in Employee1.__mro__:
        if "Emp_Address" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Address"]
            break
    assert isinstance(descriptor, property)

def test_employee1_has_attribute():
    assert hasattr(Employee1, "attribute")
    descriptor = None
    for klass in Employee1.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_employee1_has_UserName():
    assert hasattr(Employee1, "UserName")
    descriptor = None
    for klass in Employee1.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_employee1_has_Salary():
    assert hasattr(Employee1, "Salary")
    descriptor = None
    for klass in Employee1.__mro__:
        if "Salary" in klass.__dict__:
            descriptor = klass.__dict__["Salary"]
            break
    assert isinstance(descriptor, property)



def test_admin1_is_not_abstract():
    assert not inspect.isabstract(Admin1)


def test_admin1_constructor_exists():
    assert callable(Admin1.__init__)


def test_admin1_constructor_args():
    sig = inspect.signature(Admin1.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_admin1_has_password():
    assert hasattr(Admin1, "password")
    descriptor = None
    for klass in Admin1.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin1_has_UserName():
    assert hasattr(Admin1, "UserName")
    descriptor = None
    for klass in Admin1.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)



def test_users1_is_not_abstract():
    assert not inspect.isabstract(Users1)


def test_users1_constructor_exists():
    assert callable(Users1.__init__)


def test_users1_constructor_args():
    sig = inspect.signature(Users1.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"

def test_users1_has_id():
    assert hasattr(Users1, "id")
    descriptor = None
    for klass in Users1.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_users1_has_password():
    assert hasattr(Users1, "password")
    descriptor = None
    for klass in Users1.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_admin_has_Password():
    assert hasattr(Admin, "Password")
    descriptor = None
    for klass in Admin.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_UserName():
    assert hasattr(Admin, "UserName")
    descriptor = None
    for klass in Admin.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)



def test_employee_actor_is_not_abstract():
    assert not inspect.isabstract(Employee_Actor)


def test_employee_actor_constructor_exists():
    assert callable(Employee_Actor.__init__)


def test_employee_actor_constructor_args():
    sig = inspect.signature(Employee_Actor.__init__)
    params = list(sig.parameters.keys())



def test_administrator_actor_is_not_abstract():
    assert not inspect.isabstract(Administrator_Actor)


def test_administrator_actor_constructor_exists():
    assert callable(Administrator_Actor.__init__)


def test_administrator_actor_constructor_args():
    sig = inspect.signature(Administrator_Actor.__init__)
    params = list(sig.parameters.keys())



def test_salary_management_usecase_is_not_abstract():
    assert not inspect.isabstract(Salary_Management_UseCase)


def test_salary_management_usecase_constructor_exists():
    assert callable(Salary_Management_UseCase.__init__)


def test_salary_management_usecase_constructor_args():
    sig = inspect.signature(Salary_Management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_authentication_usecase_is_not_abstract():
    assert not inspect.isabstract(Authentication_UseCase)


def test_authentication_usecase_constructor_exists():
    assert callable(Authentication_UseCase.__init__)


def test_authentication_usecase_constructor_args():
    sig = inspect.signature(Authentication_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_employee_management_system_component_is_not_abstract():
    assert not inspect.isabstract(Employee_Management_System_Component)


def test_employee_management_system_component_constructor_exists():
    assert callable(Employee_Management_System_Component.__init__)


def test_employee_management_system_component_constructor_args():
    sig = inspect.signature(Employee_Management_System_Component.__init__)
    params = list(sig.parameters.keys())



def test_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_users_constructor_exists():
    assert callable(Users.__init__)


def test_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_users_has_Password():
    assert hasattr(Users, "Password")
    descriptor = None
    for klass in Users.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_users_has_UserName():
    assert hasattr(Users, "UserName")
    descriptor = None
    for klass in Users.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)



def test_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "Leave_Title" in params, "Missing parameter 'Leave_Title'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Leave_EndDate" in params, "Missing parameter 'Leave_EndDate'"
    assert "Leave_detail" in params, "Missing parameter 'Leave_detail'"
    assert "Leave_Status" in params, "Missing parameter 'Leave_Status'"
    assert "leave_id" in params, "Missing parameter 'leave_id'"

def test_leave_has_Leave_Title():
    assert hasattr(Leave, "Leave_Title")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_Title" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Title"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_Emp_Id():
    assert hasattr(Leave, "Emp_Id")
    descriptor = None
    for klass in Leave.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_Leave_EndDate():
    assert hasattr(Leave, "Leave_EndDate")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_EndDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_EndDate"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_Leave_detail():
    assert hasattr(Leave, "Leave_detail")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_detail" in klass.__dict__:
            descriptor = klass.__dict__["Leave_detail"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_Leave_Status():
    assert hasattr(Leave, "Leave_Status")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_Status" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Status"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_leave_id():
    assert hasattr(Leave, "leave_id")
    descriptor = None
    for klass in Leave.__mro__:
        if "leave_id" in klass.__dict__:
            descriptor = klass.__dict__["leave_id"]
            break
    assert isinstance(descriptor, property)



def test_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "Sly_Basic" in params, "Missing parameter 'Sly_Basic'"
    assert "Sly_Decrement" in params, "Missing parameter 'Sly_Decrement'"
    assert "Sly_Increment" in params, "Missing parameter 'Sly_Increment'"
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "Sly_Netgross" in params, "Missing parameter 'Sly_Netgross'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"

def test_salary_has_Sly_Basic():
    assert hasattr(Salary, "Sly_Basic")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Basic" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Basic"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Sly_Decrement():
    assert hasattr(Salary, "Sly_Decrement")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Decrement" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Decrement"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Sly_Increment():
    assert hasattr(Salary, "Sly_Increment")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Increment" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Increment"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_OverTime():
    assert hasattr(Salary, "OverTime")
    descriptor = None
    for klass in Salary.__mro__:
        if "OverTime" in klass.__dict__:
            descriptor = klass.__dict__["OverTime"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Sly_Netgross():
    assert hasattr(Salary, "Sly_Netgross")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Netgross" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Netgross"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Emp_Id():
    assert hasattr(Salary, "Emp_Id")
    descriptor = None
    for klass in Salary.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Salary" in params, "Missing parameter 'Emp_Salary'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"
    assert "Emp_Email" in params, "Missing parameter 'Emp_Email'"
    assert "Emp_ContactNo" in params, "Missing parameter 'Emp_ContactNo'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"

def test_employee_has_Emp_Salary():
    assert hasattr(Employee, "Emp_Salary")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Salary" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Salary"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Password():
    assert hasattr(Employee, "Password")
    descriptor = None
    for klass in Employee.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Name():
    assert hasattr(Employee, "Emp_Name")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Name" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Name"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Address():
    assert hasattr(Employee, "Emp_Address")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Address" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Address"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Email():
    assert hasattr(Employee, "Emp_Email")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Email" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Email"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_ContactNo():
    assert hasattr(Employee, "Emp_ContactNo")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["Emp_ContactNo"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Id():
    assert hasattr(Employee, "Emp_Id")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Department():
    assert hasattr(Employee, "Emp_Department")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Department" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Department"]
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
Logout_external_strategy = st.builds(
    Logout_external,
)
Login_external_strategy = st.builds(
    Login_external,
)
Manager2_strategy = st.builds(
    Manager2,
    id=
        st.integers(),
    password=
        safe_text,
    name=
        safe_text
)
Customer1_strategy = st.builds(
    Customer1,
    S=
        safe_text,
    Customer_Name=
        safe_text
)
Manager1_strategy = st.builds(
    Manager1,
    Name=
        safe_text,
    Password=
        safe_text,
    Manager_id=
        st.integers()
)
Order_strategy = st.builds(
    Order,
    id=
        st.integers(),
    name=
        safe_text
)
Manager_strategy = st.builds(
    Manager,
    password=
        safe_text,
    UserName=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    country=
        safe_text,
    password=
        safe_text,
    UserName=
        safe_text,
    postal_code=
        st.integers(),
    address=
        safe_text
)
Employee1_strategy = st.builds(
    Employee1,
    contact_no=
        st.integers(),
    name=
        safe_text,
    Email=
        safe_text,
    Emp_Dep=
        safe_text,
    password=
        safe_text,
    Emp_Address=
        safe_text,
    attribute=
        safe_text,
    UserName=
        safe_text,
    Salary=
        st.integers()
)
Admin1_strategy = st.builds(
    Admin1,
    password=
        safe_text,
    UserName=
        safe_text
)
Users1_strategy = st.builds(
    Users1,
    id=
        safe_text,
    password=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    Password=
        safe_text,
    UserName=
        safe_text
)
Employee_Actor_strategy = st.builds(
    Employee_Actor,
)
Administrator_Actor_strategy = st.builds(
    Administrator_Actor,
)
Salary_Management_UseCase_strategy = st.builds(
    Salary_Management_UseCase,
)
Authentication_UseCase_strategy = st.builds(
    Authentication_UseCase,
)
Employee_Management_System_Component_strategy = st.builds(
    Employee_Management_System_Component,
)
Users_strategy = st.builds(
    Users,
    Password=
        safe_text,
    UserName=
        safe_text
)
Leave_strategy = st.builds(
    Leave,
    Leave_Title=
        safe_text,
    Emp_Id=
        st.integers(),
    Leave_EndDate=
        st.dates(),
    Leave_detail=
        safe_text,
    Leave_Status=
        safe_text,
    leave_id=
        st.integers()
)
Salary_strategy = st.builds(
    Salary,
    Sly_Basic=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Decrement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Increment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    OverTime=
        safe_text,
    Sly_Netgross=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_Id=
        st.integers()
)
Employee_strategy = st.builds(
    Employee,
    Emp_Salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Password=
        safe_text,
    Emp_Name=
        safe_text,
    Emp_Address=
        safe_text,
    Emp_Email=
        safe_text,
    Emp_ContactNo=
        safe_text,
    Emp_Id=
        st.integers(),
    Emp_Department=
        safe_text
)

@given(instance=Logout_external_strategy)
@settings(max_examples=50)
def test_logout_external_instantiation(instance):
    assert isinstance(instance, Logout_external)

@given(instance=Login_external_strategy)
@settings(max_examples=50)
def test_login_external_instantiation(instance):
    assert isinstance(instance, Login_external)

@given(instance=Manager2_strategy)
@settings(max_examples=50)
def test_manager2_instantiation(instance):
    assert isinstance(instance, Manager2)



@given(instance=Manager2_strategy)
def test_manager2_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Manager2_strategy)
def test_manager2_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Manager2_strategy)
def test_manager2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Customer1_strategy)
@settings(max_examples=50)
def test_customer1_instantiation(instance):
    assert isinstance(instance, Customer1)



@given(instance=Customer1_strategy)
def test_customer1_S_setter(instance):
    original = instance.S
    instance.S = original
    assert instance.S == original



@given(instance=Customer1_strategy)
def test_customer1_Customer_Name_setter(instance):
    original = instance.Customer_Name
    instance.Customer_Name = original
    assert instance.Customer_Name == original

@given(instance=Manager1_strategy)
@settings(max_examples=50)
def test_manager1_instantiation(instance):
    assert isinstance(instance, Manager1)



@given(instance=Manager1_strategy)
def test_manager1_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Manager1_strategy)
def test_manager1_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Manager1_strategy)
def test_manager1_Manager_id_setter(instance):
    original = instance.Manager_id
    instance.Manager_id = original
    assert instance.Manager_id == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Order_strategy)
def test_order_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Manager_strategy)
def test_manager_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Customer_strategy)
def test_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Customer_strategy)
def test_customer_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Customer_strategy)
def test_customer_postal_code_setter(instance):
    original = instance.postal_code
    instance.postal_code = original
    assert instance.postal_code == original



@given(instance=Customer_strategy)
def test_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Employee1_strategy)
@settings(max_examples=50)
def test_employee1_instantiation(instance):
    assert isinstance(instance, Employee1)



@given(instance=Employee1_strategy)
def test_employee1_contact_no_setter(instance):
    original = instance.contact_no
    instance.contact_no = original
    assert instance.contact_no == original



@given(instance=Employee1_strategy)
def test_employee1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Employee1_strategy)
def test_employee1_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Employee1_strategy)
def test_employee1_Emp_Dep_setter(instance):
    original = instance.Emp_Dep
    instance.Emp_Dep = original
    assert instance.Emp_Dep == original



@given(instance=Employee1_strategy)
def test_employee1_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Employee1_strategy)
def test_employee1_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original



@given(instance=Employee1_strategy)
def test_employee1_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Employee1_strategy)
def test_employee1_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Employee1_strategy)
def test_employee1_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original

@given(instance=Admin1_strategy)
@settings(max_examples=50)
def test_admin1_instantiation(instance):
    assert isinstance(instance, Admin1)



@given(instance=Admin1_strategy)
def test_admin1_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin1_strategy)
def test_admin1_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Users1_strategy)
@settings(max_examples=50)
def test_users1_instantiation(instance):
    assert isinstance(instance, Users1)



@given(instance=Users1_strategy)
def test_users1_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Users1_strategy)
def test_users1_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Admin_strategy)
def test_admin_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Employee_Actor_strategy)
@settings(max_examples=50)
def test_employee_actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)

@given(instance=Administrator_Actor_strategy)
@settings(max_examples=50)
def test_administrator_actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)

@given(instance=Salary_Management_UseCase_strategy)
@settings(max_examples=50)
def test_salary_management_usecase_instantiation(instance):
    assert isinstance(instance, Salary_Management_UseCase)

@given(instance=Authentication_UseCase_strategy)
@settings(max_examples=50)
def test_authentication_usecase_instantiation(instance):
    assert isinstance(instance, Authentication_UseCase)

@given(instance=Employee_Management_System_Component_strategy)
@settings(max_examples=50)
def test_employee_management_system_component_instantiation(instance):
    assert isinstance(instance, Employee_Management_System_Component)

@given(instance=Users_strategy)
@settings(max_examples=50)
def test_users_instantiation(instance):
    assert isinstance(instance, Users)



@given(instance=Users_strategy)
def test_users_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Users_strategy)
def test_users_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Leave_strategy)
@settings(max_examples=50)
def test_leave_instantiation(instance):
    assert isinstance(instance, Leave)



@given(instance=Leave_strategy)
def test_leave_Leave_Title_setter(instance):
    original = instance.Leave_Title
    instance.Leave_Title = original
    assert instance.Leave_Title == original



@given(instance=Leave_strategy)
def test_leave_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Leave_strategy)
def test_leave_Leave_EndDate_setter(instance):
    original = instance.Leave_EndDate
    instance.Leave_EndDate = original
    assert instance.Leave_EndDate == original



@given(instance=Leave_strategy)
def test_leave_Leave_detail_setter(instance):
    original = instance.Leave_detail
    instance.Leave_detail = original
    assert instance.Leave_detail == original



@given(instance=Leave_strategy)
def test_leave_Leave_Status_setter(instance):
    original = instance.Leave_Status
    instance.Leave_Status = original
    assert instance.Leave_Status == original



@given(instance=Leave_strategy)
def test_leave_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)



@given(instance=Salary_strategy)
def test_salary_Sly_Basic_setter(instance):
    original = instance.Sly_Basic
    instance.Sly_Basic = original
    assert instance.Sly_Basic == original



@given(instance=Salary_strategy)
def test_salary_Sly_Decrement_setter(instance):
    original = instance.Sly_Decrement
    instance.Sly_Decrement = original
    assert instance.Sly_Decrement == original



@given(instance=Salary_strategy)
def test_salary_Sly_Increment_setter(instance):
    original = instance.Sly_Increment
    instance.Sly_Increment = original
    assert instance.Sly_Increment == original



@given(instance=Salary_strategy)
def test_salary_OverTime_setter(instance):
    original = instance.OverTime
    instance.OverTime = original
    assert instance.OverTime == original



@given(instance=Salary_strategy)
def test_salary_Sly_Netgross_setter(instance):
    original = instance.Sly_Netgross
    instance.Sly_Netgross = original
    assert instance.Sly_Netgross == original



@given(instance=Salary_strategy)
def test_salary_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Emp_Salary_setter(instance):
    original = instance.Emp_Salary
    instance.Emp_Salary = original
    assert instance.Emp_Salary == original



@given(instance=Employee_strategy)
def test_employee_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Employee_strategy)
def test_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original



@given(instance=Employee_strategy)
def test_employee_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original



@given(instance=Employee_strategy)
def test_employee_Emp_Email_setter(instance):
    original = instance.Emp_Email
    instance.Emp_Email = original
    assert instance.Emp_Email == original



@given(instance=Employee_strategy)
def test_employee_Emp_ContactNo_setter(instance):
    original = instance.Emp_ContactNo
    instance.Emp_ContactNo = original
    assert instance.Emp_ContactNo == original



@given(instance=Employee_strategy)
def test_employee_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Employee_strategy)
def test_employee_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original
