import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Logout_external,
    Login_external,
    Tuning_Staff,
    Driving_Staff,
    Administrator,
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Login,
    Attendance,
    Leave_Status,
    Staff,
    Salary,
    Manager,
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



def test_tuning_staff_is_not_abstract():
    assert not inspect.isabstract(Tuning_Staff)


def test_tuning_staff_constructor_exists():
    assert callable(Tuning_Staff.__init__)


def test_tuning_staff_constructor_args():
    sig = inspect.signature(Tuning_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"

def test_tuning_staff_has_Address():
    assert hasattr(Tuning_Staff, "Address")
    descriptor = None
    for klass in Tuning_Staff.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_tuning_staff_has_UserName():
    assert hasattr(Tuning_Staff, "UserName")
    descriptor = None
    for klass in Tuning_Staff.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_tuning_staff_has_Authendication_Mood():
    assert hasattr(Tuning_Staff, "Authendication_Mood")
    descriptor = None
    for klass in Tuning_Staff.__mro__:
        if "Authendication_Mood" in klass.__dict__:
            descriptor = klass.__dict__["Authendication_Mood"]
            break
    assert isinstance(descriptor, property)



def test_driving_staff_is_not_abstract():
    assert not inspect.isabstract(Driving_Staff)


def test_driving_staff_constructor_exists():
    assert callable(Driving_Staff.__init__)


def test_driving_staff_constructor_args():
    sig = inspect.signature(Driving_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"
    assert "PilotName" in params, "Missing parameter 'PilotName'"
    assert "Pilot_ContactNo" in params, "Missing parameter 'Pilot_ContactNo'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_driving_staff_has_Authendication_Mood():
    assert hasattr(Driving_Staff, "Authendication_Mood")
    descriptor = None
    for klass in Driving_Staff.__mro__:
        if "Authendication_Mood" in klass.__dict__:
            descriptor = klass.__dict__["Authendication_Mood"]
            break
    assert isinstance(descriptor, property)

def test_driving_staff_has_PilotName():
    assert hasattr(Driving_Staff, "PilotName")
    descriptor = None
    for klass in Driving_Staff.__mro__:
        if "PilotName" in klass.__dict__:
            descriptor = klass.__dict__["PilotName"]
            break
    assert isinstance(descriptor, property)

def test_driving_staff_has_Pilot_ContactNo():
    assert hasattr(Driving_Staff, "Pilot_ContactNo")
    descriptor = None
    for klass in Driving_Staff.__mro__:
        if "Pilot_ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["Pilot_ContactNo"]
            break
    assert isinstance(descriptor, property)

def test_driving_staff_has_Password():
    assert hasattr(Driving_Staff, "Password")
    descriptor = None
    for klass in Driving_Staff.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"
    assert "Emp_Position" in params, "Missing parameter 'Emp_Position'"
    assert "Admin_Id" in params, "Missing parameter 'Admin_Id'"
    assert "Admin_Name" in params, "Missing parameter 'Admin_Name'"
    assert "Admin_NIC" in params, "Missing parameter 'Admin_NIC'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Admin_Email" in params, "Missing parameter 'Admin_Email'"
    assert "Emp_Date_Of_Joint" in params, "Missing parameter 'Emp_Date_Of_Joint'"
    assert "Admin_ContactNo" in params, "Missing parameter 'Admin_ContactNo'"

def test_administrator_has_Emp_Department():
    assert hasattr(Administrator, "Emp_Department")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Emp_Department" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Department"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Emp_Position():
    assert hasattr(Administrator, "Emp_Position")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Emp_Position" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Position"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Admin_Id():
    assert hasattr(Administrator, "Admin_Id")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Admin_Id" in klass.__dict__:
            descriptor = klass.__dict__["Admin_Id"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Admin_Name():
    assert hasattr(Administrator, "Admin_Name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Admin_Name" in klass.__dict__:
            descriptor = klass.__dict__["Admin_Name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Admin_NIC():
    assert hasattr(Administrator, "Admin_NIC")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Admin_NIC" in klass.__dict__:
            descriptor = klass.__dict__["Admin_NIC"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Emp_DOB():
    assert hasattr(Administrator, "Emp_DOB")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Emp_DOB" in klass.__dict__:
            descriptor = klass.__dict__["Emp_DOB"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Admin_Email():
    assert hasattr(Administrator, "Admin_Email")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Admin_Email" in klass.__dict__:
            descriptor = klass.__dict__["Admin_Email"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Emp_Date_Of_Joint():
    assert hasattr(Administrator, "Emp_Date_Of_Joint")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Emp_Date_Of_Joint" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Date_Of_Joint"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Admin_ContactNo():
    assert hasattr(Administrator, "Admin_ContactNo")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Admin_ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["Admin_ContactNo"]
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



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_login_has_Password():
    assert hasattr(Login, "Password")
    descriptor = None
    for klass in Login.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_UserName():
    assert hasattr(Login, "UserName")
    descriptor = None
    for klass in Login.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
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
    assert "Leaving_Time" in params, "Missing parameter 'Leaving_Time'"
    assert "AttendTime" in params, "Missing parameter 'AttendTime'"
    assert "Attend_date" in params, "Missing parameter 'Attend_date'"

def test_attendance_has_Emp_id():
    assert hasattr(Attendance, "Emp_id")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Emp_id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_id"]
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

def test_attendance_has_Attend_date():
    assert hasattr(Attendance, "Attend_date")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Attend_date" in klass.__dict__:
            descriptor = klass.__dict__["Attend_date"]
            break
    assert isinstance(descriptor, property)



def test_leave_status_is_not_abstract():
    assert not inspect.isabstract(Leave_Status)


def test_leave_status_constructor_exists():
    assert callable(Leave_Status.__init__)


def test_leave_status_constructor_args():
    sig = inspect.signature(Leave_Status.__init__)
    params = list(sig.parameters.keys())
    assert "Leave_Status" in params, "Missing parameter 'Leave_Status'"
    assert "Leave_detail" in params, "Missing parameter 'Leave_detail'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Leave_ApplyDate" in params, "Missing parameter 'Leave_ApplyDate'"
    assert "Leave_NoOfDays" in params, "Missing parameter 'Leave_NoOfDays'"
    assert "leave_id" in params, "Missing parameter 'leave_id'"
    assert "Leave_EndDate" in params, "Missing parameter 'Leave_EndDate'"
    assert "Leave_Title" in params, "Missing parameter 'Leave_Title'"
    assert "Leave_StartDate" in params, "Missing parameter 'Leave_StartDate'"

def test_leave_status_has_Leave_Status():
    assert hasattr(Leave_Status, "Leave_Status")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "Leave_Status" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Status"]
            break
    assert isinstance(descriptor, property)

def test_leave_status_has_Leave_detail():
    assert hasattr(Leave_Status, "Leave_detail")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "Leave_detail" in klass.__dict__:
            descriptor = klass.__dict__["Leave_detail"]
            break
    assert isinstance(descriptor, property)

def test_leave_status_has_Emp_Id():
    assert hasattr(Leave_Status, "Emp_Id")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "Emp_Id" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Id"]
            break
    assert isinstance(descriptor, property)

def test_leave_status_has_Leave_ApplyDate():
    assert hasattr(Leave_Status, "Leave_ApplyDate")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "Leave_ApplyDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_ApplyDate"]
            break
    assert isinstance(descriptor, property)

def test_leave_status_has_Leave_NoOfDays():
    assert hasattr(Leave_Status, "Leave_NoOfDays")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "Leave_NoOfDays" in klass.__dict__:
            descriptor = klass.__dict__["Leave_NoOfDays"]
            break
    assert isinstance(descriptor, property)

def test_leave_status_has_leave_id():
    assert hasattr(Leave_Status, "leave_id")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "leave_id" in klass.__dict__:
            descriptor = klass.__dict__["leave_id"]
            break
    assert isinstance(descriptor, property)

def test_leave_status_has_Leave_EndDate():
    assert hasattr(Leave_Status, "Leave_EndDate")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "Leave_EndDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_EndDate"]
            break
    assert isinstance(descriptor, property)

def test_leave_status_has_Leave_Title():
    assert hasattr(Leave_Status, "Leave_Title")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "Leave_Title" in klass.__dict__:
            descriptor = klass.__dict__["Leave_Title"]
            break
    assert isinstance(descriptor, property)

def test_leave_status_has_Leave_StartDate():
    assert hasattr(Leave_Status, "Leave_StartDate")
    descriptor = None
    for klass in Leave_Status.__mro__:
        if "Leave_StartDate" in klass.__dict__:
            descriptor = klass.__dict__["Leave_StartDate"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_staff_has_Password():
    assert hasattr(Staff, "Password")
    descriptor = None
    for klass in Staff.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Authendication_Mood():
    assert hasattr(Staff, "Authendication_Mood")
    descriptor = None
    for klass in Staff.__mro__:
        if "Authendication_Mood" in klass.__dict__:
            descriptor = klass.__dict__["Authendication_Mood"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_UserName():
    assert hasattr(Staff, "UserName")
    descriptor = None
    for klass in Staff.__mro__:
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
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "Sly_Decrement" in params, "Missing parameter 'Sly_Decrement'"
    assert "Sly_Basic" in params, "Missing parameter 'Sly_Basic'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Sly_Netgross" in params, "Missing parameter 'Sly_Netgross'"
    assert "Sly_Increment" in params, "Missing parameter 'Sly_Increment'"

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

def test_salary_has_Sly_Increment():
    assert hasattr(Salary, "Sly_Increment")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Increment" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Increment"]
            break
    assert isinstance(descriptor, property)



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "Emp_NIC" in params, "Missing parameter 'Emp_NIC'"
    assert "Mng_Email" in params, "Missing parameter 'Mng_Email'"
    assert "Mng_Salary" in params, "Missing parameter 'Mng_Salary'"
    assert "Emp_Date_Of_Joint" in params, "Missing parameter 'Emp_Date_Of_Joint'"
    assert "Emp_Position" in params, "Missing parameter 'Emp_Position'"
    assert "Emp_DOB" in params, "Missing parameter 'Emp_DOB'"
    assert "Mng_Name" in params, "Missing parameter 'Mng_Name'"
    assert "Mng_ContactNo" in params, "Missing parameter 'Mng_ContactNo'"
    assert "Mng_Id" in params, "Missing parameter 'Mng_Id'"
    assert "Emp_Department" in params, "Missing parameter 'Emp_Department'"
    assert "Emp_Address" in params, "Missing parameter 'Emp_Address'"

def test_manager_has_Emp_NIC():
    assert hasattr(Manager, "Emp_NIC")
    descriptor = None
    for klass in Manager.__mro__:
        if "Emp_NIC" in klass.__dict__:
            descriptor = klass.__dict__["Emp_NIC"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Mng_Email():
    assert hasattr(Manager, "Mng_Email")
    descriptor = None
    for klass in Manager.__mro__:
        if "Mng_Email" in klass.__dict__:
            descriptor = klass.__dict__["Mng_Email"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Mng_Salary():
    assert hasattr(Manager, "Mng_Salary")
    descriptor = None
    for klass in Manager.__mro__:
        if "Mng_Salary" in klass.__dict__:
            descriptor = klass.__dict__["Mng_Salary"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Emp_Date_Of_Joint():
    assert hasattr(Manager, "Emp_Date_Of_Joint")
    descriptor = None
    for klass in Manager.__mro__:
        if "Emp_Date_Of_Joint" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Date_Of_Joint"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Emp_Position():
    assert hasattr(Manager, "Emp_Position")
    descriptor = None
    for klass in Manager.__mro__:
        if "Emp_Position" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Position"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Emp_DOB():
    assert hasattr(Manager, "Emp_DOB")
    descriptor = None
    for klass in Manager.__mro__:
        if "Emp_DOB" in klass.__dict__:
            descriptor = klass.__dict__["Emp_DOB"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Mng_Name():
    assert hasattr(Manager, "Mng_Name")
    descriptor = None
    for klass in Manager.__mro__:
        if "Mng_Name" in klass.__dict__:
            descriptor = klass.__dict__["Mng_Name"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Mng_ContactNo():
    assert hasattr(Manager, "Mng_ContactNo")
    descriptor = None
    for klass in Manager.__mro__:
        if "Mng_ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["Mng_ContactNo"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Mng_Id():
    assert hasattr(Manager, "Mng_Id")
    descriptor = None
    for klass in Manager.__mro__:
        if "Mng_Id" in klass.__dict__:
            descriptor = klass.__dict__["Mng_Id"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Emp_Department():
    assert hasattr(Manager, "Emp_Department")
    descriptor = None
    for klass in Manager.__mro__:
        if "Emp_Department" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Department"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Emp_Address():
    assert hasattr(Manager, "Emp_Address")
    descriptor = None
    for klass in Manager.__mro__:
        if "Emp_Address" in klass.__dict__:
            descriptor = klass.__dict__["Emp_Address"]
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
Tuning_Staff_strategy = st.builds(
    Tuning_Staff,
    Address=
        safe_text,
    UserName=
        safe_text,
    Authendication_Mood=
        safe_text
)
Driving_Staff_strategy = st.builds(
    Driving_Staff,
    Authendication_Mood=
        safe_text,
    PilotName=
        safe_text,
    Pilot_ContactNo=
        safe_text,
    Password=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    Emp_Department=
        safe_text,
    Emp_Position=
        safe_text,
    Admin_Id=
        st.integers(),
    Admin_Name=
        safe_text,
    Admin_NIC=
        safe_text,
    Emp_DOB=
        st.dates(),
    Admin_Email=
        safe_text,
    Emp_Date_Of_Joint=
        st.dates(),
    Admin_ContactNo=
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
Login_strategy = st.builds(
    Login,
    Password=
        safe_text,
    UserName=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    Emp_id=
        safe_text,
    Leaving_Time=
        safe_text,
    AttendTime=
        safe_text,
    Attend_date=
        st.dates()
)
Leave_Status_strategy = st.builds(
    Leave_Status,
    Leave_Status=
        safe_text,
    Leave_detail=
        safe_text,
    Emp_Id=
        st.integers(),
    Leave_ApplyDate=
        st.dates(),
    Leave_NoOfDays=
        st.integers(),
    leave_id=
        st.integers(),
    Leave_EndDate=
        st.dates(),
    Leave_Title=
        safe_text,
    Leave_StartDate=
        st.dates()
)
Staff_strategy = st.builds(
    Staff,
    Password=
        safe_text,
    Authendication_Mood=
        safe_text,
    UserName=
        safe_text
)
Salary_strategy = st.builds(
    Salary,
    OverTime=
        safe_text,
    Sly_Decrement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Basic=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_Id=
        st.integers(),
    Sly_Netgross=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Increment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Manager_strategy = st.builds(
    Manager,
    Emp_NIC=
        safe_text,
    Mng_Email=
        safe_text,
    Mng_Salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_Date_Of_Joint=
        st.dates(),
    Emp_Position=
        safe_text,
    Emp_DOB=
        st.dates(),
    Mng_Name=
        safe_text,
    Mng_ContactNo=
        safe_text,
    Mng_Id=
        st.integers(),
    Emp_Department=
        safe_text,
    Emp_Address=
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

@given(instance=Tuning_Staff_strategy)
@settings(max_examples=50)
def test_tuning_staff_instantiation(instance):
    assert isinstance(instance, Tuning_Staff)



@given(instance=Tuning_Staff_strategy)
def test_tuning_staff_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Tuning_Staff_strategy)
def test_tuning_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Tuning_Staff_strategy)
def test_tuning_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original

@given(instance=Driving_Staff_strategy)
@settings(max_examples=50)
def test_driving_staff_instantiation(instance):
    assert isinstance(instance, Driving_Staff)



@given(instance=Driving_Staff_strategy)
def test_driving_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original



@given(instance=Driving_Staff_strategy)
def test_driving_staff_PilotName_setter(instance):
    original = instance.PilotName
    instance.PilotName = original
    assert instance.PilotName == original



@given(instance=Driving_Staff_strategy)
def test_driving_staff_Pilot_ContactNo_setter(instance):
    original = instance.Pilot_ContactNo
    instance.Pilot_ContactNo = original
    assert instance.Pilot_ContactNo == original



@given(instance=Driving_Staff_strategy)
def test_driving_staff_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original



@given(instance=Administrator_strategy)
def test_administrator_Emp_Position_setter(instance):
    original = instance.Emp_Position
    instance.Emp_Position = original
    assert instance.Emp_Position == original



@given(instance=Administrator_strategy)
def test_administrator_Admin_Id_setter(instance):
    original = instance.Admin_Id
    instance.Admin_Id = original
    assert instance.Admin_Id == original



@given(instance=Administrator_strategy)
def test_administrator_Admin_Name_setter(instance):
    original = instance.Admin_Name
    instance.Admin_Name = original
    assert instance.Admin_Name == original



@given(instance=Administrator_strategy)
def test_administrator_Admin_NIC_setter(instance):
    original = instance.Admin_NIC
    instance.Admin_NIC = original
    assert instance.Admin_NIC == original



@given(instance=Administrator_strategy)
def test_administrator_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



@given(instance=Administrator_strategy)
def test_administrator_Admin_Email_setter(instance):
    original = instance.Admin_Email
    instance.Admin_Email = original
    assert instance.Admin_Email == original



@given(instance=Administrator_strategy)
def test_administrator_Emp_Date_Of_Joint_setter(instance):
    original = instance.Emp_Date_Of_Joint
    instance.Emp_Date_Of_Joint = original
    assert instance.Emp_Date_Of_Joint == original



@given(instance=Administrator_strategy)
def test_administrator_Admin_ContactNo_setter(instance):
    original = instance.Admin_ContactNo
    instance.Admin_ContactNo = original
    assert instance.Admin_ContactNo == original

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
def test_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Login_strategy)
def test_login_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

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
def test_attendance_Leaving_Time_setter(instance):
    original = instance.Leaving_Time
    instance.Leaving_Time = original
    assert instance.Leaving_Time == original



@given(instance=Attendance_strategy)
def test_attendance_AttendTime_setter(instance):
    original = instance.AttendTime
    instance.AttendTime = original
    assert instance.AttendTime == original



@given(instance=Attendance_strategy)
def test_attendance_Attend_date_setter(instance):
    original = instance.Attend_date
    instance.Attend_date = original
    assert instance.Attend_date == original

@given(instance=Leave_Status_strategy)
@settings(max_examples=50)
def test_leave_status_instantiation(instance):
    assert isinstance(instance, Leave_Status)



@given(instance=Leave_Status_strategy)
def test_leave_status_Leave_Status_setter(instance):
    original = instance.Leave_Status
    instance.Leave_Status = original
    assert instance.Leave_Status == original



@given(instance=Leave_Status_strategy)
def test_leave_status_Leave_detail_setter(instance):
    original = instance.Leave_detail
    instance.Leave_detail = original
    assert instance.Leave_detail == original



@given(instance=Leave_Status_strategy)
def test_leave_status_Emp_Id_setter(instance):
    original = instance.Emp_Id
    instance.Emp_Id = original
    assert instance.Emp_Id == original



@given(instance=Leave_Status_strategy)
def test_leave_status_Leave_ApplyDate_setter(instance):
    original = instance.Leave_ApplyDate
    instance.Leave_ApplyDate = original
    assert instance.Leave_ApplyDate == original



@given(instance=Leave_Status_strategy)
def test_leave_status_Leave_NoOfDays_setter(instance):
    original = instance.Leave_NoOfDays
    instance.Leave_NoOfDays = original
    assert instance.Leave_NoOfDays == original



@given(instance=Leave_Status_strategy)
def test_leave_status_leave_id_setter(instance):
    original = instance.leave_id
    instance.leave_id = original
    assert instance.leave_id == original



@given(instance=Leave_Status_strategy)
def test_leave_status_Leave_EndDate_setter(instance):
    original = instance.Leave_EndDate
    instance.Leave_EndDate = original
    assert instance.Leave_EndDate == original



@given(instance=Leave_Status_strategy)
def test_leave_status_Leave_Title_setter(instance):
    original = instance.Leave_Title
    instance.Leave_Title = original
    assert instance.Leave_Title == original



@given(instance=Leave_Status_strategy)
def test_leave_status_Leave_StartDate_setter(instance):
    original = instance.Leave_StartDate
    instance.Leave_StartDate = original
    assert instance.Leave_StartDate == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Staff_strategy)
def test_staff_Authendication_Mood_setter(instance):
    original = instance.Authendication_Mood
    instance.Authendication_Mood = original
    assert instance.Authendication_Mood == original



@given(instance=Staff_strategy)
def test_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Salary_strategy)
@settings(max_examples=50)
def test_salary_instantiation(instance):
    assert isinstance(instance, Salary)



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
def test_salary_Sly_Increment_setter(instance):
    original = instance.Sly_Increment
    instance.Sly_Increment = original
    assert instance.Sly_Increment == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_Emp_NIC_setter(instance):
    original = instance.Emp_NIC
    instance.Emp_NIC = original
    assert instance.Emp_NIC == original



@given(instance=Manager_strategy)
def test_manager_Mng_Email_setter(instance):
    original = instance.Mng_Email
    instance.Mng_Email = original
    assert instance.Mng_Email == original



@given(instance=Manager_strategy)
def test_manager_Mng_Salary_setter(instance):
    original = instance.Mng_Salary
    instance.Mng_Salary = original
    assert instance.Mng_Salary == original



@given(instance=Manager_strategy)
def test_manager_Emp_Date_Of_Joint_setter(instance):
    original = instance.Emp_Date_Of_Joint
    instance.Emp_Date_Of_Joint = original
    assert instance.Emp_Date_Of_Joint == original



@given(instance=Manager_strategy)
def test_manager_Emp_Position_setter(instance):
    original = instance.Emp_Position
    instance.Emp_Position = original
    assert instance.Emp_Position == original



@given(instance=Manager_strategy)
def test_manager_Emp_DOB_setter(instance):
    original = instance.Emp_DOB
    instance.Emp_DOB = original
    assert instance.Emp_DOB == original



@given(instance=Manager_strategy)
def test_manager_Mng_Name_setter(instance):
    original = instance.Mng_Name
    instance.Mng_Name = original
    assert instance.Mng_Name == original



@given(instance=Manager_strategy)
def test_manager_Mng_ContactNo_setter(instance):
    original = instance.Mng_ContactNo
    instance.Mng_ContactNo = original
    assert instance.Mng_ContactNo == original



@given(instance=Manager_strategy)
def test_manager_Mng_Id_setter(instance):
    original = instance.Mng_Id
    instance.Mng_Id = original
    assert instance.Mng_Id == original



@given(instance=Manager_strategy)
def test_manager_Emp_Department_setter(instance):
    original = instance.Emp_Department
    instance.Emp_Department = original
    assert instance.Emp_Department == original



@given(instance=Manager_strategy)
def test_manager_Emp_Address_setter(instance):
    original = instance.Emp_Address
    instance.Emp_Address = original
    assert instance.Emp_Address == original
