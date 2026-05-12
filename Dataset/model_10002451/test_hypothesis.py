import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Logout_external,
    Login_external,
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Login,
    Attendance,
    Leave,
    Authenticate_staff,
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
    assert "Date" in params, "Missing parameter 'Date'"
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "Emp_id" in params, "Missing parameter 'Emp_id'"

def test_attendance_has_Date():
    assert hasattr(Attendance, "Date")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_endTime():
    assert hasattr(Attendance, "endTime")
    descriptor = None
    for klass in Attendance.__mro__:
        if "endTime" in klass.__dict__:
            descriptor = klass.__dict__["endTime"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_startTime():
    assert hasattr(Attendance, "startTime")
    descriptor = None
    for klass in Attendance.__mro__:
        if "startTime" in klass.__dict__:
            descriptor = klass.__dict__["startTime"]
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



def test_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "leave_id" in params, "Missing parameter 'leave_id'"
    assert "Leave_Status" in params, "Missing parameter 'Leave_Status'"
    assert "Leave_StartDate" in params, "Missing parameter 'Leave_StartDate'"
    assert "Leave_ApplyDate" in params, "Missing parameter 'Leave_ApplyDate'"
    assert "Leave_Type" in params, "Missing parameter 'Leave_Type'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Leave_Title" in params, "Missing parameter 'Leave_Title'"
    assert "Leave_EndDate" in params, "Missing parameter 'Leave_EndDate'"
    assert "Leave_NoOfDays" in params, "Missing parameter 'Leave_NoOfDays'"

def test_leave_has_leave_id():
    assert hasattr(Leave, "leave_id")
    descriptor = None
    for klass in Leave.__mro__:
        if "leave_id" in klass.__dict__:
            descriptor = klass.__dict__["leave_id"]
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

def test_leave_has_Leave_StartDate():
    assert hasattr(Leave, "Leave_StartDate")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_StartDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_StartDate"]
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

def test_leave_has_Leave_Type():
    assert hasattr(Leave, "Leave_Type")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_Type" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Type"]
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

def test_leave_has_Leave_Title():
    assert hasattr(Leave, "Leave_Title")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_Title" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Title"]
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

def test_leave_has_Leave_NoOfDays():
    assert hasattr(Leave, "Leave_NoOfDays")
    descriptor = None
    for klass in Leave.__mro__:
        if "Leave_NoOfDays" in klass.__dict__:
            descriptor = klass.__dict__["Leave_NoOfDays"]
            break
    assert isinstance(descriptor, property)



def test_authenticate_staff_is_not_abstract():
    assert not inspect.isabstract(Authenticate_staff)


def test_authenticate_staff_constructor_exists():
    assert callable(Authenticate_staff.__init__)


def test_authenticate_staff_constructor_args():
    sig = inspect.signature(Authenticate_staff.__init__)
    params = list(sig.parameters.keys())
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_authenticate_staff_has_Authendication_Mood():
    assert hasattr(Authenticate_staff, "Authendication_Mood")
    descriptor = None
    for klass in Authenticate_staff.__mro__:
        if "Authendication_Mood" in klass.__dict__:
            descriptor = klass.__dict__["Authendication_Mood"]
            break
    assert isinstance(descriptor, property)

def test_authenticate_staff_has_Password():
    assert hasattr(Authenticate_staff, "Password")
    descriptor = None
    for klass in Authenticate_staff.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_authenticate_staff_has_UserName():
    assert hasattr(Authenticate_staff, "UserName")
    descriptor = None
    for klass in Authenticate_staff.__mro__:
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
    assert "Sly_Decrement" in params, "Missing parameter 'Sly_Decrement'"
    assert "Sly_Increment" in params, "Missing parameter 'Sly_Increment'"
    assert "Sly_Basic" in params, "Missing parameter 'Sly_Basic'"
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Sly_Netgross" in params, "Missing parameter 'Sly_Netgross'"

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

def test_salary_has_Sly_Basic():
    assert hasattr(Salary, "Sly_Basic")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Basic" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Basic"]
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



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Designation" in params, "Missing parameter 'Emp_Designation'"
    assert "Emp_Name" in params, "Missing parameter 'Emp_Name'"
    assert "Emp_Salary" in params, "Missing parameter 'Emp_Salary'"
    assert "Emp_ContactNo" in params, "Missing parameter 'Emp_ContactNo'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Emp_Email" in params, "Missing parameter 'Emp_Email'"

def test_employee_has_Emp_Designation():
    assert hasattr(Employee, "Emp_Designation")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Designation" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Designation"]
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

def test_employee_has_Emp_Salary():
    assert hasattr(Employee, "Emp_Salary")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_Salary" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Salary"]
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

def test_employee_has_Emp_DOB():
    assert hasattr(Employee, "Emp_DOB")
    descriptor = None
    for klass in Employee.__mro__:
        if "Emp_DOB" in klass.__dict__:
            descriptor = klass.__dict__["Emp_DOB"]
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
Login_strategy = st.builds(
    Login,
    UserName=
        safe_text,
    Password=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    Date=
        st.dates(),
    endTime=
        safe_text,
    startTime=
        safe_text,
    Emp_id=
        safe_text
)
Leave_strategy = st.builds(
    Leave,
    leave_id=
        st.integers(),
    Leave_Status=
        safe_text,
    Leave_StartDate=
        st.dates(),
    Leave_ApplyDate=
        st.dates(),
    Leave_Type=
        safe_text,
    Emp_Id=
        st.integers(),
    Leave_Title=
        safe_text,
    Leave_EndDate=
        st.dates(),
    Leave_NoOfDays=
        st.integers()
)
Authenticate_staff_strategy = st.builds(
    Authenticate_staff,
    Authendication_Mood=
        safe_text,
    Password=
        safe_text,
    UserName=
        safe_text
)
Salary_strategy = st.builds(
    Salary,
    Sly_Decrement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Increment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Basic=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    OverTime=
        safe_text,
    Emp_Id=
        st.integers(),
    Sly_Netgross=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Employee_strategy = st.builds(
    Employee,
    Emp_Designation=
        safe_text,
    Emp_Name=
        safe_text,
    Emp_Salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_ContactNo=
        safe_text,
    Emp_DOB=
        st.dates(),
    Emp_Id=
        st.integers(),
    Emp_Email=
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
def test_attendance_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Attendance_strategy)
def test_attendance_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=Attendance_strategy)
def test_attendance_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original



@given(instance=Attendance_strategy)
def test_attendance_Emp_id_setter(instance):
    original = instance.Emp_id
    instance.Emp_id = original
    assert instance.Emp_id == original

@given(instance=Leave_strategy)
@settings(max_examples=50)
def test_leave_instantiation(instance):
    assert isinstance(instance, Leave)



@given(instance=Leave_strategy)
def test_leave_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original



@given(instance=Leave_strategy)
def test_leave_Leave_Status_setter(instance):
    original = instance.Leave_Status
    instance.Leave_Status = original
    assert instance.Leave_Status == original



@given(instance=Leave_strategy)
def test_leave_Leave_StartDate_setter(instance):
    original = instance.Leave_StartDate
    instance.Leave_StartDate = original
    assert instance.Leave_StartDate == original



@given(instance=Leave_strategy)
def test_leave_Leave_ApplyDate_setter(instance):
    original = instance.Leave_ApplyDate
    instance.Leave_ApplyDate = original
    assert instance.Leave_ApplyDate == original



@given(instance=Leave_strategy)
def test_leave_Leave_Type_setter(instance):
    original = instance.Leave_Type
    instance.Leave_Type = original
    assert instance.Leave_Type == original



@given(instance=Leave_strategy)
def test_leave_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Leave_strategy)
def test_leave_Leave_Title_setter(instance):
    original = instance.Leave_Title
    instance.Leave_Title = original
    assert instance.Leave_Title == original



@given(instance=Leave_strategy)
def test_leave_Leave_EndDate_setter(instance):
    original = instance.Leave_EndDate
    instance.Leave_EndDate = original
    assert instance.Leave_EndDate == original



@given(instance=Leave_strategy)
def test_leave_Leave_NoOfDays_setter(instance):
    original = instance.Leave_NoOfDays
    instance.Leave_NoOfDays = original
    assert instance.Leave_NoOfDays == original

@given(instance=Authenticate_staff_strategy)
@settings(max_examples=50)
def test_authenticate_staff_instantiation(instance):
    assert isinstance(instance, Authenticate_staff)



@given(instance=Authenticate_staff_strategy)
def test_authenticate_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original



@given(instance=Authenticate_staff_strategy)
def test_authenticate_staff_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Authenticate_staff_strategy)
def test_authenticate_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)



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
def test_salary_Sly_Basic_setter(instance):
    original = instance.Sly_Basic
    instance.Sly_Basic = original
    assert instance.Sly_Basic == original



@given(instance=Salary_strategy)
def test_salary_OverTime_setter(instance):
    original = instance.OverTime
    instance.OverTime = original
    assert instance.OverTime == original



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

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Emp_Designation_setter(instance):
    original = instance.Emp_Designation
    instance.Emp_Designation = original
    assert instance.Emp_Designation == original



@given(instance=Employee_strategy)
def test_employee_Emp_Name_setter(instance):
    original = instance.Emp_Name
    instance.Emp_Name = original
    assert instance.Emp_Name == original



@given(instance=Employee_strategy)
def test_employee_Emp_Salary_setter(instance):
    original = instance.Emp_Salary
    instance.Emp_Salary = original
    assert instance.Emp_Salary == original



@given(instance=Employee_strategy)
def test_employee_Emp_ContactNo_setter(instance):
    original = instance.Emp_ContactNo
    instance.Emp_ContactNo = original
    assert instance.Emp_ContactNo == original



@given(instance=Employee_strategy)
def test_employee_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



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
