import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Login_external,
    Logout_external,
    _10_7_1992,
    _10000,
    Employee,
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    T,
    Login,
    Attendance,
    L__Leave,
    Admin,
    Salary,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_login_external_is_not_abstract():
    assert not inspect.isabstract(Login_external)


def test_login_external_constructor_exists():
    assert callable(Login_external.__init__)


def test_login_external_constructor_args():
    sig = inspect.signature(Login_external.__init__)
    params = list(sig.parameters.keys())



def test_logout_external_is_not_abstract():
    assert not inspect.isabstract(Logout_external)


def test_logout_external_constructor_exists():
    assert callable(Logout_external.__init__)


def test_logout_external_constructor_args():
    sig = inspect.signature(Logout_external.__init__)
    params = list(sig.parameters.keys())



def test__10_7_1992_is_not_abstract():
    assert not inspect.isabstract(_10_7_1992)


def test__10_7_1992_constructor_exists():
    assert callable(_10_7_1992.__init__)


def test__10_7_1992_constructor_args():
    sig = inspect.signature(_10_7_1992.__init__)
    params = list(sig.parameters.keys())



def test__10000_is_not_abstract():
    assert not inspect.isabstract(_10000)


def test__10000_constructor_exists():
    assert callable(_10000.__init__)


def test__10000_constructor_args():
    sig = inspect.signature(_10000.__init__)
    params = list(sig.parameters.keys())



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_NIC" in params, "Missing parameter 'Emp_NIC'"
    assert "Emp_Date_Of_Joint" in params, "Missing parameter 'Emp_Date_Of_Joint'"
    assert "Emp_Email" in params, "Missing parameter 'Emp_Email'"
    assert "Emp_Salary" in params, "Missing parameter 'Emp_Salary'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Emp_ContactNo" in params, "Missing parameter 'Emp_ContactNo'"
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"
    assert "Emp_Position" in params, "Missing parameter 'Emp_Position'"

def test_employee_has_Emp_Id():
    assert hasattr(Employee, "Emp_Id")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_NIC():
    assert hasattr(Employee, "Emp_NIC")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_NIC" in klass.__dict__:
            descriptor = klass.__dict__["Emp_NIC"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Date_Of_Joint():
    assert hasattr(Employee, "Emp_Date_Of_Joint")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Date_Of_Joint" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Date_Of_Joint"]
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

def test_employee_has_Emp_Salary():
    assert hasattr(Employee, "Emp_Salary")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Salary" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Salary"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_DOB():
    assert hasattr(Employee, "Emp_DOB")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_DOB" in klass.__dict__:
            descriptor = klass.__dict__["Emp_DOB"]
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

def test_employee_has_Emp_Address():
    assert hasattr(Employee, "Emp_Address")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Address" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Address"]
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

def test_employee_has_Emp_Department():
    assert hasattr(Employee, "Emp_Department")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Department" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Department"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Emp_Position():
    assert hasattr(Employee, "Emp_Position")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Position" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Position"]
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



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_login_has_UserName():
    assert hasattr(Login, "UserName")
    descriptor = None
    for klass in Login.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_login_has_Password():
    assert hasattr(Login, "Password")
    descriptor = None
    for klass in Login.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "AttendTime" in params, "Missing parameter 'AttendTime'"
    assert "Emp_id" in params, "Missing parameter 'Emp_id'"
    assert "Attend_date" in params, "Missing parameter 'Attend_date'"
    assert "Leaving_Time" in params, "Missing parameter 'Leaving_Time'"

def test_attendance_has_AttendTime():
    assert hasattr(Attendance, "AttendTime")
    descriptor = None
    for klass in Attendance.__mro__:
        if "AttendTime" in klass.__dict__:
            descriptor = klass.__dict__["AttendTime"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_Emp_id():
    assert hasattr(Attendance, "Emp_id")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Emp_id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_id"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_Attend_date():
    assert hasattr(Attendance, "Attend_date")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Attend_date" in klass.__dict__:
            descriptor = klass.__dict__["Attend_date"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_Leaving_Time():
    assert hasattr(Attendance, "Leaving_Time")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Leaving_Time" in klass.__dict__:
            descriptor = klass.__dict__["Leaving_Time"]
            break
    assert isinstance(descriptor, property)



def test_l__leave_is_not_abstract():
    assert not inspect.isabstract(L__Leave)


def test_l__leave_constructor_exists():
    assert callable(L__Leave.__init__)


def test_l__leave_constructor_args():
    sig = inspect.signature(L__Leave.__init__)
    params = list(sig.parameters.keys())
    assert "leave_id" in params, "Missing parameter 'leave_id'"
    assert "Leave_detail" in params, "Missing parameter 'Leave_detail'"
    assert "Leave_Status" in params, "Missing parameter 'Leave_Status'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Leave_ApplyDate" in params, "Missing parameter 'Leave_ApplyDate'"
    assert "Leave_EndDate" in params, "Missing parameter 'Leave_EndDate'"
    assert "Leave_NoOfDays" in params, "Missing parameter 'Leave_NoOfDays'"
    assert "Leave_StartDate" in params, "Missing parameter 'Leave_StartDate'"
    assert "Leave_Title" in params, "Missing parameter 'Leave_Title'"

def test_l__leave_has_leave_id():
    assert hasattr(L__Leave, "leave_id")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "leave_id" in klass.__dict__:
            descriptor = klass.__dict__["leave_id"]
            break
    assert isinstance(descriptor, property)

def test_l__leave_has_Leave_detail():
    assert hasattr(L__Leave, "Leave_detail")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "Leave_detail" in klass.__dict__:
            descriptor = klass.__dict__["Leave_detail"]
            break
    assert isinstance(descriptor, property)

def test_l__leave_has_Leave_Status():
    assert hasattr(L__Leave, "Leave_Status")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "Leave_Status" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Status"]
            break
    assert isinstance(descriptor, property)

def test_l__leave_has_Emp_Id():
    assert hasattr(L__Leave, "Emp_Id")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)

def test_l__leave_has_Leave_ApplyDate():
    assert hasattr(L__Leave, "Leave_ApplyDate")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "Leave_ApplyDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_ApplyDate"]
            break
    assert isinstance(descriptor, property)

def test_l__leave_has_Leave_EndDate():
    assert hasattr(L__Leave, "Leave_EndDate")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "Leave_EndDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_EndDate"]
            break
    assert isinstance(descriptor, property)

def test_l__leave_has_Leave_NoOfDays():
    assert hasattr(L__Leave, "Leave_NoOfDays")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "Leave_NoOfDays" in klass.__dict__:
            descriptor = klass.__dict__["Leave_NoOfDays"]
            break
    assert isinstance(descriptor, property)

def test_l__leave_has_Leave_StartDate():
    assert hasattr(L__Leave, "Leave_StartDate")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "Leave_StartDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_StartDate"]
            break
    assert isinstance(descriptor, property)

def test_l__leave_has_Leave_Title():
    assert hasattr(L__Leave, "Leave_Title")
    descriptor = None
    for klass in L__Leave.__mro__:
        if "Leave_Title" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Title"]
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
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_admin_has_Password():
    assert hasattr(Admin, "Password")
    descriptor = None
    for klass in Admin.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_attribute():
    assert hasattr(Admin, "attribute")
    descriptor = None
    for klass in Admin.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
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



def test_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "Sly_Increment" in params, "Missing parameter 'Sly_Increment'"
    assert "Sly_Basic" in params, "Missing parameter 'Sly_Basic'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Sly_Netgross" in params, "Missing parameter 'Sly_Netgross'"
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "Sly_Decrement" in params, "Missing parameter 'Sly_Decrement'"

def test_salary_has_Sly_Increment():
    assert hasattr(Salary, "Sly_Increment")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Increment" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Increment"]
            break
    assert isinstance(descriptor, property)

def test_salary_has_Sly_Basic():
    assert hasattr(Salary, "Sly_Basic")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Basic" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Basic"]
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

def test_salary_has_Sly_Netgross():
    assert hasattr(Salary, "Sly_Netgross")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Netgross" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Netgross"]
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

def test_salary_has_Sly_Decrement():
    assert hasattr(Salary, "Sly_Decrement")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Decrement" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Decrement"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "User_contact" in params, "Missing parameter 'User_contact'"
    assert "User_Email" in params, "Missing parameter 'User_Email'"
    assert "User_Name" in params, "Missing parameter 'User_Name'"
    assert "User_DOB" in params, "Missing parameter 'User_DOB'"
    assert "User_Id" in params, "Missing parameter 'User_Id'"
    assert "User_Address" in params, "Missing parameter 'User_Address'"

def test_user_has_User_contact():
    assert hasattr(User, "User_contact")
    descriptor = None
    for klass in User.__mro__:
        if "User_contact" in klass.__dict__:
            descriptor = klass.__dict__["User_contact"]
            break
    assert isinstance(descriptor, property)

def test_user_has_User_Email():
    assert hasattr(User, "User_Email")
    descriptor = None
    for klass in User.__mro__:
        if "User_Email" in klass.__dict__:
            descriptor = klass.__dict__["User_Email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_User_Name():
    assert hasattr(User, "User_Name")
    descriptor = None
    for klass in User.__mro__:
        if "User_Name" in klass.__dict__:
            descriptor = klass.__dict__["User_Name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_User_DOB():
    assert hasattr(User, "User_DOB")
    descriptor = None
    for klass in User.__mro__:
        if "User_DOB" in klass.__dict__:
            descriptor = klass.__dict__["User_DOB"]
            break
    assert isinstance(descriptor, property)

def test_user_has_User_Id():
    assert hasattr(User, "User_Id")
    descriptor = None
    for klass in User.__mro__:
        if "User_Id" in klass.__dict__:
            descriptor = klass.__dict__["User_Id"]
            break
    assert isinstance(descriptor, property)

def test_user_has_User_Address():
    assert hasattr(User, "User_Address")
    descriptor = None
    for klass in User.__mro__:
        if "User_Address" in klass.__dict__:
            descriptor = klass.__dict__["User_Address"]
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
Login_external_strategy = st.builds(
    Login_external,
)
Logout_external_strategy = st.builds(
    Logout_external,
)
_10_7_1992_strategy = st.builds(
    _10_7_1992,
)
_10000_strategy = st.builds(
    _10000,
)
Employee_strategy = st.builds(
    Employee,
    Emp_Id=
        safe_text,
    Emp_NIC=
        safe_text,
    Emp_Date_Of_Joint=
        safe_text,
    Emp_Email=
        safe_text,
    Emp_Salary=
        safe_text,
    Emp_DOB=
        st.none(),
    Emp_ContactNo=
        safe_text,
    Emp_Address=
        safe_text,
    Emp_Name=
        safe_text,
    Emp_Department=
        safe_text,
    Emp_Position=
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
T_strategy = st.builds(
    T,
)
Login_strategy = st.builds(
    Login,
    UserName=
        safe_text,
    Password=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    AttendTime=
        safe_text,
    Emp_id=
        safe_text,
    Attend_date=
        safe_text,
    Leaving_Time=
        safe_text
)
L__Leave_strategy = st.builds(
    L__Leave,
    leave_id=
        safe_text,
    Leave_detail=
        safe_text,
    Leave_Status=
        safe_text,
    Emp_Id=
        safe_text,
    Leave_ApplyDate=
        safe_text,
    Leave_EndDate=
        safe_text,
    Leave_NoOfDays=
        safe_text,
    Leave_StartDate=
        safe_text,
    Leave_Title=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    Password=
        safe_text,
    attribute=
        safe_text,
    UserName=
        safe_text
)
Salary_strategy = st.builds(
    Salary,
    Sly_Increment=
        st.none(),
    Sly_Basic=
        safe_text,
    Emp_Id=
        safe_text,
    Sly_Netgross=
        safe_text,
    OverTime=
        safe_text,
    Sly_Decrement=
        safe_text
)
User_strategy = st.builds(
    User,
    User_contact=
        safe_text,
    User_Email=
        safe_text,
    User_Name=
        safe_text,
    User_DOB=
        safe_text,
    User_Id=
        safe_text,
    User_Address=
        safe_text
)

@given(instance=Login_external_strategy)
@settings(max_examples=50)
def test_login_external_instantiation(instance):
    assert isinstance(instance, Login_external)

@given(instance=Logout_external_strategy)
@settings(max_examples=50)
def test_logout_external_instantiation(instance):
    assert isinstance(instance, Logout_external)

@given(instance=_10_7_1992_strategy)
@settings(max_examples=50)
def test__10_7_1992_instantiation(instance):
    assert isinstance(instance, _10_7_1992)

@given(instance=_10000_strategy)
@settings(max_examples=50)
def test__10000_instantiation(instance):
    assert isinstance(instance, _10000)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Employee_strategy)
def test_employee_Emp_NIC_setter(instance):
    original = instance.Emp_NIC
    instance.Emp_NIC = original
    assert instance.Emp_NIC == original



@given(instance=Employee_strategy)
def test_employee_Emp_Date_Of_Joint_setter(instance):
    original = instance.Emp_Date_Of_Joint
    instance.Emp_Date_Of_Joint = original
    assert instance.Emp_Date_Of_Joint == original



@given(instance=Employee_strategy)
def test_employee_Emp_Email_setter(instance):
    original = instance.Emp_Email
    instance.Emp_Email = original
    assert instance.Emp_Email == original



@given(instance=Employee_strategy)
def test_employee_Emp_Salary_setter(instance):
    original = instance.Emp_Salary
    instance.Emp_Salary = original
    assert instance.Emp_Salary == original



@given(instance=Employee_strategy)
def test_employee_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



@given(instance=Employee_strategy)
def test_employee_Emp_ContactNo_setter(instance):
    original = instance.Emp_ContactNo
    instance.Emp_ContactNo = original
    assert instance.Emp_ContactNo == original



@given(instance=Employee_strategy)
def test_employee_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original



@given(instance=Employee_strategy)
def test_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original



@given(instance=Employee_strategy)
def test_employee_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original



@given(instance=Employee_strategy)
def test_employee_Emp_Position_setter(instance):
    original = instance.Emp_Position
    instance.Emp_Position = original
    assert instance.Emp_Position == original

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

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Login_strategy)
def test_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Attendance_strategy)
@settings(max_examples=50)
def test_attendance_instantiation(instance):
    assert isinstance(instance, Attendance)



@given(instance=Attendance_strategy)
def test_attendance_AttendTime_setter(instance):
    original = instance.AttendTime
    instance.AttendTime = original
    assert instance.AttendTime == original



@given(instance=Attendance_strategy)
def test_attendance_Emp_id_setter(instance):
    original = instance.Emp_id
    instance.Emp_id = original
    assert instance.Emp_id == original



@given(instance=Attendance_strategy)
def test_attendance_Attend_date_setter(instance):
    original = instance.Attend_date
    instance.Attend_date = original
    assert instance.Attend_date == original



@given(instance=Attendance_strategy)
def test_attendance_Leaving_Time_setter(instance):
    original = instance.Leaving_Time
    instance.Leaving_Time = original
    assert instance.Leaving_Time == original

@given(instance=L__Leave_strategy)
@settings(max_examples=50)
def test_l__leave_instantiation(instance):
    assert isinstance(instance, L__Leave)



@given(instance=L__Leave_strategy)
def test_l__leave_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original



@given(instance=L__Leave_strategy)
def test_l__leave_Leave_detail_setter(instance):
    original = instance.Leave_detail
    instance.Leave_detail = original
    assert instance.Leave_detail == original



@given(instance=L__Leave_strategy)
def test_l__leave_Leave_Status_setter(instance):
    original = instance.Leave_Status
    instance.Leave_Status = original
    assert instance.Leave_Status == original



@given(instance=L__Leave_strategy)
def test_l__leave_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=L__Leave_strategy)
def test_l__leave_Leave_ApplyDate_setter(instance):
    original = instance.Leave_ApplyDate
    instance.Leave_ApplyDate = original
    assert instance.Leave_ApplyDate == original



@given(instance=L__Leave_strategy)
def test_l__leave_Leave_EndDate_setter(instance):
    original = instance.Leave_EndDate
    instance.Leave_EndDate = original
    assert instance.Leave_EndDate == original



@given(instance=L__Leave_strategy)
def test_l__leave_Leave_NoOfDays_setter(instance):
    original = instance.Leave_NoOfDays
    instance.Leave_NoOfDays = original
    assert instance.Leave_NoOfDays == original



@given(instance=L__Leave_strategy)
def test_l__leave_Leave_StartDate_setter(instance):
    original = instance.Leave_StartDate
    instance.Leave_StartDate = original
    assert instance.Leave_StartDate == original



@given(instance=L__Leave_strategy)
def test_l__leave_Leave_Title_setter(instance):
    original = instance.Leave_Title
    instance.Leave_Title = original
    assert instance.Leave_Title == original

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
def test_admin_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Admin_strategy)
def test_admin_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)



@given(instance=Salary_strategy)
def test_salary_Sly_Increment_setter(instance):
    original = instance.Sly_Increment
    instance.Sly_Increment = original
    assert instance.Sly_Increment == original



@given(instance=Salary_strategy)
def test_salary_Sly_Basic_setter(instance):
    original = instance.Sly_Basic
    instance.Sly_Basic = original
    assert instance.Sly_Basic == original



@given(instance=Salary_strategy)
def test_salary_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Salary_strategy)
def test_salary_Sly_Netgross_setter(instance):
    original = instance.Sly_Netgross
    instance.Sly_Netgross = original
    assert instance.Sly_Netgross == original



@given(instance=Salary_strategy)
def test_salary_OverTime_setter(instance):
    original = instance.OverTime
    instance.OverTime = original
    assert instance.OverTime == original



@given(instance=Salary_strategy)
def test_salary_Sly_Decrement_setter(instance):
    original = instance.Sly_Decrement
    instance.Sly_Decrement = original
    assert instance.Sly_Decrement == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_User_contact_setter(instance):
    original = instance.User_contact
    instance.User_contact = original
    assert instance.User_contact == original



@given(instance=User_strategy)
def test_user_User_Email_setter(instance):
    original = instance.User_Email
    instance.User_Email = original
    assert instance.User_Email == original



@given(instance=User_strategy)
def test_user_User_Name_setter(instance):
    original = instance.User_Name
    instance.User_Name = original
    assert instance.User_Name == original



@given(instance=User_strategy)
def test_user_User_DOB_setter(instance):
    original = instance.User_DOB
    instance.User_DOB = original
    assert instance.User_DOB == original



@given(instance=User_strategy)
def test_user_User_Id_setter(instance):
    original = instance.User_Id
    instance.User_Id = original
    assert instance.User_Id == original



@given(instance=User_strategy)
def test_user_User_Address_setter(instance):
    original = instance.User_Address
    instance.User_Address = original
    assert instance.User_Address == original
