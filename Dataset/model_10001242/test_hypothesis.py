import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Logout_external,
    Login_external,
    Admin,
    FingerprintReader,
    Employee_Actor,
    Administrator_Actor,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Login,
    Attendance,
    Leave,
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



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserType" in params, "Missing parameter 'UserType'"

def test_admin_has_UserName():
    assert hasattr(Admin, "UserName")
    descriptor = None
    for klass in Admin.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Password():
    assert hasattr(Admin, "Password")
    descriptor = None
    for klass in Admin.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_UserType():
    assert hasattr(Admin, "UserType")
    descriptor = None
    for klass in Admin.__mro__:
        if "UserType" in klass.__dict__:
            descriptor = klass.__dict__["UserType"]
            break
    assert isinstance(descriptor, property)



def test_fingerprintreader_is_not_abstract():
    assert not inspect.isabstract(FingerprintReader)


def test_fingerprintreader_constructor_exists():
    assert callable(FingerprintReader.__init__)


def test_fingerprintreader_constructor_args():
    sig = inspect.signature(FingerprintReader.__init__)
    params = list(sig.parameters.keys())
    assert "Y__Cord" in params, "Missing parameter 'Y__Cord'"
    assert "MiniType" in params, "Missing parameter 'MiniType'"
    assert "miniType" in params, "Missing parameter 'miniType'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Angle" in params, "Missing parameter 'Angle'"
    assert "X_cord" in params, "Missing parameter 'X_cord'"

def test_fingerprintreader_has_Y__Cord():
    assert hasattr(FingerprintReader, "Y__Cord")
    descriptor = None
    for klass in FingerprintReader.__mro__:
        if "Y__Cord" in klass.__dict__:
            descriptor = klass.__dict__["Y__Cord"]
            break
    assert isinstance(descriptor, property)

def test_fingerprintreader_has_MiniType():
    assert hasattr(FingerprintReader, "MiniType")
    descriptor = None
    for klass in FingerprintReader.__mro__:
        if "MiniType" in klass.__dict__:
            descriptor = klass.__dict__["MiniType"]
            break
    assert isinstance(descriptor, property)

def test_fingerprintreader_has_miniType():
    assert hasattr(FingerprintReader, "miniType")
    descriptor = None
    for klass in FingerprintReader.__mro__:
        if "miniType" in klass.__dict__:
            descriptor = klass.__dict__["miniType"]
            break
    assert isinstance(descriptor, property)

def test_fingerprintreader_has_Emp_Id():
    assert hasattr(FingerprintReader, "Emp_Id")
    descriptor = None
    for klass in FingerprintReader.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)

def test_fingerprintreader_has_Angle():
    assert hasattr(FingerprintReader, "Angle")
    descriptor = None
    for klass in FingerprintReader.__mro__:
        if "Angle" in klass.__dict__:
            descriptor = klass.__dict__["Angle"]
            break
    assert isinstance(descriptor, property)

def test_fingerprintreader_has_X_cord():
    assert hasattr(FingerprintReader, "X_cord")
    descriptor = None
    for klass in FingerprintReader.__mro__:
        if "X_cord" in klass.__dict__:
            descriptor = klass.__dict__["X_cord"]
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



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Password1" in params, "Missing parameter 'Password1'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_login_has_UserName():
    assert hasattr(Login, "UserName")
    descriptor = None
    for klass in Login.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_login_has_Password1():
    assert hasattr(Login, "Password1")
    descriptor = None
    for klass in Login.__mro__:
        if "Password1" in klass.__dict__:
            descriptor = klass.__dict__["Password1"]
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
    assert "Emp_id" in params, "Missing parameter 'Emp_id'"
    assert "Attend_date" in params, "Missing parameter 'Attend_date'"
    assert "Leaving_Time" in params, "Missing parameter 'Leaving_Time'"
    assert "AttendTime" in params, "Missing parameter 'AttendTime'"

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

def test_attendance_has_AttendTime():
    assert hasattr(Attendance, "AttendTime")
    descriptor = None
    for klass in Attendance.__mro__:
        if "AttendTime" in klass.__dict__:
            descriptor = klass.__dict__["AttendTime"]
            break
    assert isinstance(descriptor, property)



def test_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "Leave_StartDate" in params, "Missing parameter 'Leave_StartDate'"
    assert "Leave_EndDate" in params, "Missing parameter 'Leave_EndDate'"
    assert "leave_id" in params, "Missing parameter 'leave_id'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Leave_detail" in params, "Missing parameter 'Leave_detail'"
    assert "Leave_NoOfDays" in params, "Missing parameter 'Leave_NoOfDays'"
    assert "Leave_Status" in params, "Missing parameter 'Leave_Status'"
    assert "Leave_Title" in params, "Missing parameter 'Leave_Title'"
    assert "Leave_ApplyDate" in params, "Missing parameter 'Leave_ApplyDate'"

def test_leave_has_Leave_StartDate():
    assert hasattr(Leave, "Leave_StartDate")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_StartDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_StartDate"]
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

def test_leave_has_leave_id():
    assert hasattr(Leave, "leave_id")
    descriptor = None
    for klass in Leave.__mro__:
        if "leave_id" in klass.__dict__:
            descriptor = klass.__dict__["leave_id"]
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

def test_leave_has_Leave_detail():
    assert hasattr(Leave, "Leave_detail")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_detail" in klass.__dict__:
            descriptor = klass.__dict__["Leave_detail"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_Leave_NoOfDays():
    assert hasattr(Leave, "Leave_NoOfDays")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_NoOfDays" in klass.__dict__:
            descriptor = klass.__dict__["Leave_NoOfDays"]
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

def test_leave_has_Leave_Title():
    assert hasattr(Leave, "Leave_Title")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_Title" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Title"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_Leave_ApplyDate():
    assert hasattr(Leave, "Leave_ApplyDate")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_ApplyDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_ApplyDate"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"
    assert "Emp_ContactNo" in params, "Missing parameter 'Emp_ContactNo'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_Email" in params, "Missing parameter 'Emp_Email'"
    assert "Emp_Position" in params, "Missing parameter 'Emp_Position'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Emp_NIC" in params, "Missing parameter 'Emp_NIC'"
    assert "Emp_Date_Of_Joint" in params, "Missing parameter 'Emp_Date_Of_Joint'"

def test_employee_has_Emp_Address():
    assert hasattr(Employee, "Emp_Address")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Address" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Address"]
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

def test_employee_has_Emp_Email():
    assert hasattr(Employee, "Emp_Email")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Email" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Email"]
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

def test_employee_has_Emp_Name():
    assert hasattr(Employee, "Emp_Name")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Name" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Name"]
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
Admin_strategy = st.builds(
    Admin,
    UserName=
        safe_text,
    Password=
        safe_text,
    UserType=
        safe_text
)
FingerprintReader_strategy = st.builds(
    FingerprintReader,
    Y__Cord=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    MiniType=
        st.none(),
    miniType=
        st.integers(),
    Emp_Id=
        st.integers(),
    Angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    X_cord=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Employee_Actor_strategy = st.builds(
    Employee_Actor,
)
Administrator_Actor_strategy = st.builds(
    Administrator_Actor,
)
Authentication_UseCase_strategy = st.builds(
    Authentication_UseCase,
)
Employee_Management_System_Component_strategy = st.builds(
    Employee_Management_System_Component,
)
Login_strategy = st.builds(
    Login,
    UserName=
        safe_text,
    Password1=
        safe_text,
    Password=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    Emp_id=
        safe_text,
    Attend_date=
        st.dates(),
    Leaving_Time=
        safe_text,
    AttendTime=
        safe_text
)
Leave_strategy = st.builds(
    Leave,
    Leave_StartDate=
        st.dates(),
    Leave_EndDate=
        st.dates(),
    leave_id=
        st.integers(),
    Emp_Id=
        st.integers(),
    Leave_detail=
        safe_text,
    Leave_NoOfDays=
        st.integers(),
    Leave_Status=
        safe_text,
    Leave_Title=
        safe_text,
    Leave_ApplyDate=
        st.dates()
)
Employee_strategy = st.builds(
    Employee,
    Emp_Address=
        safe_text,
    Emp_Department=
        safe_text,
    Emp_ContactNo=
        safe_text,
    Emp_Id=
        st.integers(),
    Emp_Email=
        safe_text,
    Emp_Position=
        safe_text,
    Emp_Name=
        safe_text,
    Emp_DOB=
        st.dates(),
    Emp_NIC=
        safe_text,
    Emp_Date_Of_Joint=
        st.dates()
)

@given(instance=Logout_external_strategy)
@settings(max_examples=50)
def test_logout_external_instantiation(instance):
    assert isinstance(instance, Logout_external)

@given(instance=Login_external_strategy)
@settings(max_examples=50)
def test_login_external_instantiation(instance):
    assert isinstance(instance, Login_external)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Admin_strategy)
def test_admin_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Admin_strategy)
def test_admin_UserType_setter(instance):
    original = instance.UserType
    instance.UserType = original
    assert instance.UserType == original

@given(instance=FingerprintReader_strategy)
@settings(max_examples=50)
def test_fingerprintreader_instantiation(instance):
    assert isinstance(instance, FingerprintReader)



@given(instance=FingerprintReader_strategy)
def test_fingerprintreader_Y__Cord_setter(instance):
    original = instance.Y__Cord
    instance.Y__Cord = original
    assert instance.Y__Cord == original



@given(instance=FingerprintReader_strategy)
def test_fingerprintreader_MiniType_setter(instance):
    original = instance.MiniType
    instance.MiniType = original
    assert instance.MiniType == original



@given(instance=FingerprintReader_strategy)
def test_fingerprintreader_miniType_setter(instance):
    original = instance.miniType
    instance.miniType = original
    assert instance.miniType == original



@given(instance=FingerprintReader_strategy)
def test_fingerprintreader_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=FingerprintReader_strategy)
def test_fingerprintreader_Angle_setter(instance):
    original = instance.Angle
    instance.Angle = original
    assert instance.Angle == original



@given(instance=FingerprintReader_strategy)
def test_fingerprintreader_X_cord_setter(instance):
    original = instance.X_cord
    instance.X_cord = original
    assert instance.X_cord == original

@given(instance=Employee_Actor_strategy)
@settings(max_examples=50)
def test_employee_actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)

@given(instance=Administrator_Actor_strategy)
@settings(max_examples=50)
def test_administrator_actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)

@given(instance=Authentication_UseCase_strategy)
@settings(max_examples=50)
def test_authentication_usecase_instantiation(instance):
    assert isinstance(instance, Authentication_UseCase)

@given(instance=Employee_Management_System_Component_strategy)
@settings(max_examples=50)
def test_employee_management_system_component_instantiation(instance):
    assert isinstance(instance, Employee_Management_System_Component)

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
def test_login_Password1_setter(instance):
    original = instance.Password1
    instance.Password1 = original
    assert instance.Password1 == original



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



@given(instance=Attendance_strategy)
def test_attendance_AttendTime_setter(instance):
    original = instance.AttendTime
    instance.AttendTime = original
    assert instance.AttendTime == original

@given(instance=Leave_strategy)
@settings(max_examples=50)
def test_leave_instantiation(instance):
    assert isinstance(instance, Leave)



@given(instance=Leave_strategy)
def test_leave_Leave_StartDate_setter(instance):
    original = instance.Leave_StartDate
    instance.Leave_StartDate = original
    assert instance.Leave_StartDate == original



@given(instance=Leave_strategy)
def test_leave_Leave_EndDate_setter(instance):
    original = instance.Leave_EndDate
    instance.Leave_EndDate = original
    assert instance.Leave_EndDate == original



@given(instance=Leave_strategy)
def test_leave_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original



@given(instance=Leave_strategy)
def test_leave_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Leave_strategy)
def test_leave_Leave_detail_setter(instance):
    original = instance.Leave_detail
    instance.Leave_detail = original
    assert instance.Leave_detail == original



@given(instance=Leave_strategy)
def test_leave_Leave_NoOfDays_setter(instance):
    original = instance.Leave_NoOfDays
    instance.Leave_NoOfDays = original
    assert instance.Leave_NoOfDays == original



@given(instance=Leave_strategy)
def test_leave_Leave_Status_setter(instance):
    original = instance.Leave_Status
    instance.Leave_Status = original
    assert instance.Leave_Status == original



@given(instance=Leave_strategy)
def test_leave_Leave_Title_setter(instance):
    original = instance.Leave_Title
    instance.Leave_Title = original
    assert instance.Leave_Title == original



@given(instance=Leave_strategy)
def test_leave_Leave_ApplyDate_setter(instance):
    original = instance.Leave_ApplyDate
    instance.Leave_ApplyDate = original
    assert instance.Leave_ApplyDate == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original



@given(instance=Employee_strategy)
def test_employee_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original



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
def test_employee_Emp_Email_setter(instance):
    original = instance.Emp_Email
    instance.Emp_Email = original
    assert instance.Emp_Email == original



@given(instance=Employee_strategy)
def test_employee_Emp_Position_setter(instance):
    original = instance.Emp_Position
    instance.Emp_Position = original
    assert instance.Emp_Position == original



@given(instance=Employee_strategy)
def test_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original



@given(instance=Employee_strategy)
def test_employee_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



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
