import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    Login,
    Attendance,
    Mission,
    Authenticate_staff,
    Salary,
    staff_member,
    Logout_external,
    Login_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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
    assert "AttendTime" in params, "Missing parameter 'AttendTime'"
    assert "Leaving_Time" in params, "Missing parameter 'Leaving_Time'"
    assert "Emp_id" in params, "Missing parameter 'Emp_id'"
    assert "Attend_date" in params, "Missing parameter 'Attend_date'"

def test_attendance_has_AttendTime():
    assert hasattr(Attendance, "AttendTime")
    descriptor = None
    for klass in Attendance.__mro__:
        if "AttendTime" in klass.__dict__:
            descriptor = klass.__dict__["AttendTime"]
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



def test_mission_is_not_abstract():
    assert not inspect.isabstract(Mission)


def test_mission_constructor_exists():
    assert callable(Mission.__init__)


def test_mission_constructor_args():
    sig = inspect.signature(Mission.__init__)
    params = list(sig.parameters.keys())
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"
    assert "mission_id" in params, "Missing parameter 'mission_id'"
    assert "mission_StartDate" in params, "Missing parameter 'mission_StartDate'"
    assert "mission_NoOfDays" in params, "Missing parameter 'mission_NoOfDays'"
    assert "mission_detail" in params, "Missing parameter 'mission_detail'"
    assert "mission_Status" in params, "Missing parameter 'mission_Status'"
    assert "mission_Title" in params, "Missing parameter 'mission_Title'"
    assert "mission_EndDate" in params, "Missing parameter 'mission_EndDate'"

def test_mission_has_staff_Id():
    assert hasattr(Mission, "staff_Id")
    descriptor = None
    for klass in Mission.__mro__:
        if "staff_Id" in klass.__dict__:
            descriptor = klass.__dict__["staff_Id"]
            break
    assert isinstance(descriptor, property)

def test_mission_has_mission_id():
    assert hasattr(Mission, "mission_id")
    descriptor = None
    for klass in Mission.__mro__:
        if "mission_id" in klass.__dict__:
            descriptor = klass.__dict__["mission_id"]
            break
    assert isinstance(descriptor, property)

def test_mission_has_mission_StartDate():
    assert hasattr(Mission, "mission_StartDate")
    descriptor = None
    for klass in Mission.__mro__:
        if "mission_StartDate" in klass.__dict__:
            descriptor = klass.__dict__["mission_StartDate"]
            break
    assert isinstance(descriptor, property)

def test_mission_has_mission_NoOfDays():
    assert hasattr(Mission, "mission_NoOfDays")
    descriptor = None
    for klass in Mission.__mro__:
        if "mission_NoOfDays" in klass.__dict__:
            descriptor = klass.__dict__["mission_NoOfDays"]
            break
    assert isinstance(descriptor, property)

def test_mission_has_mission_detail():
    assert hasattr(Mission, "mission_detail")
    descriptor = None
    for klass in Mission.__mro__:
        if "mission_detail" in klass.__dict__:
            descriptor = klass.__dict__["mission_detail"]
            break
    assert isinstance(descriptor, property)

def test_mission_has_mission_Status():
    assert hasattr(Mission, "mission_Status")
    descriptor = None
    for klass in Mission.__mro__:
        if "mission_Status" in klass.__dict__:
            descriptor = klass.__dict__["mission_Status"]
            break
    assert isinstance(descriptor, property)

def test_mission_has_mission_Title():
    assert hasattr(Mission, "mission_Title")
    descriptor = None
    for klass in Mission.__mro__:
        if "mission_Title" in klass.__dict__:
            descriptor = klass.__dict__["mission_Title"]
            break
    assert isinstance(descriptor, property)

def test_mission_has_mission_EndDate():
    assert hasattr(Mission, "mission_EndDate")
    descriptor = None
    for klass in Mission.__mro__:
        if "mission_EndDate" in klass.__dict__:
            descriptor = klass.__dict__["mission_EndDate"]
            break
    assert isinstance(descriptor, property)



def test_authenticate_staff_is_not_abstract():
    assert not inspect.isabstract(Authenticate_staff)


def test_authenticate_staff_constructor_exists():
    assert callable(Authenticate_staff.__init__)


def test_authenticate_staff_constructor_args():
    sig = inspect.signature(Authenticate_staff.__init__)
    params = list(sig.parameters.keys())
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Authendication_Mood" in params, "Missing parameter 'Authendication_Mood'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_authenticate_staff_has_UserName():
    assert hasattr(Authenticate_staff, "UserName")
    descriptor = None
    for klass in Authenticate_staff.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

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



def test_salary_is_not_abstract():
    assert not inspect.isabstract(Salary)


def test_salary_constructor_exists():
    assert callable(Salary.__init__)


def test_salary_constructor_args():
    sig = inspect.signature(Salary.__init__)
    params = list(sig.parameters.keys())
    assert "OverTime" in params, "Missing parameter 'OverTime'"
    assert "Sly_Basic" in params, "Missing parameter 'Sly_Basic'"
    assert "Emp_Id" in params, "Missing parameter 'Emp_Id'"
    assert "Sly_Decrement" in params, "Missing parameter 'Sly_Decrement'"
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

def test_salary_has_Sly_Decrement():
    assert hasattr(Salary, "Sly_Decrement")
    descriptor = None
    for klass in Salary.__mro__:
        if "Sly_Decrement" in klass.__dict__:
            descriptor = klass.__dict__["Sly_Decrement"]
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



def test_staff_member_is_not_abstract():
    assert not inspect.isabstract(staff_member)


def test_staff_member_constructor_exists():
    assert callable(staff_member.__init__)


def test_staff_member_constructor_args():
    sig = inspect.signature(staff_member.__init__)
    params = list(sig.parameters.keys())
    assert "staff_Address" in params, "Missing parameter 'staff_Address'"
    assert "staff_NIC" in params, "Missing parameter 'staff_NIC'"
    assert "staff_Email" in params, "Missing parameter 'staff_Email'"
    assert "staff_Salary" in params, "Missing parameter 'staff_Salary'"
    assert "staff_Name" in params, "Missing parameter 'staff_Name'"
    assert "staff_ContactNo" in params, "Missing parameter 'staff_ContactNo'"
    assert "staff_Department" in params, "Missing parameter 'staff_Department'"
    assert "staff_Date_Of_Joint" in params, "Missing parameter 'staff_Date_Of_Joint'"
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"
    assert "staff_DOB" in params, "Missing parameter 'staff_DOB'"
    assert "staff_Position" in params, "Missing parameter 'staff_Position'"

def test_staff_member_has_staff_Address():
    assert hasattr(staff_member, "staff_Address")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_Address" in klass.__dict__:
            descriptor = klass.__dict__["staff_Address"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_NIC():
    assert hasattr(staff_member, "staff_NIC")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_NIC" in klass.__dict__:
            descriptor = klass.__dict__["staff_NIC"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_Email():
    assert hasattr(staff_member, "staff_Email")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_Email" in klass.__dict__:
            descriptor = klass.__dict__["staff_Email"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_Salary():
    assert hasattr(staff_member, "staff_Salary")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_Salary" in klass.__dict__:
            descriptor = klass.__dict__["staff_Salary"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_Name():
    assert hasattr(staff_member, "staff_Name")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_Name" in klass.__dict__:
            descriptor = klass.__dict__["staff_Name"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_ContactNo():
    assert hasattr(staff_member, "staff_ContactNo")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["staff_ContactNo"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_Department():
    assert hasattr(staff_member, "staff_Department")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_Department" in klass.__dict__:
            descriptor = klass.__dict__["staff_Department"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_Date_Of_Joint():
    assert hasattr(staff_member, "staff_Date_Of_Joint")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_Date_Of_Joint" in klass.__dict__:
            descriptor = klass.__dict__["staff_Date_Of_Joint"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_Id():
    assert hasattr(staff_member, "staff_Id")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_Id" in klass.__dict__:
            descriptor = klass.__dict__["staff_Id"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_DOB():
    assert hasattr(staff_member, "staff_DOB")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_DOB" in klass.__dict__:
            descriptor = klass.__dict__["staff_DOB"]
            break
    assert isinstance(descriptor, property)

def test_staff_member_has_staff_Position():
    assert hasattr(staff_member, "staff_Position")
    descriptor = None
    for klass in staff_member.__mro__:
        if "staff_Position" in klass.__dict__:
            descriptor = klass.__dict__["staff_Position"]
            break
    assert isinstance(descriptor, property)



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
    AttendTime=
        safe_text,
    Leaving_Time=
        safe_text,
    Emp_id=
        safe_text,
    Attend_date=
        st.dates()
)
Mission_strategy = st.builds(
    Mission,
    staff_Id=
        st.integers(),
    mission_id=
        st.integers(),
    mission_StartDate=
        st.dates(),
    mission_NoOfDays=
        st.integers(),
    mission_detail=
        safe_text,
    mission_Status=
        safe_text,
    mission_Title=
        safe_text,
    mission_EndDate=
        st.dates()
)
Authenticate_staff_strategy = st.builds(
    Authenticate_staff,
    UserName=
        safe_text,
    Authendication_Mood=
        safe_text,
    Password=
        safe_text
)
Salary_strategy = st.builds(
    Salary,
    OverTime=
        safe_text,
    Sly_Basic=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emp_Id=
        st.integers(),
    Sly_Decrement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Netgross=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Sly_Increment=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
staff_member_strategy = st.builds(
    staff_member,
    staff_Address=
        safe_text,
    staff_NIC=
        safe_text,
    staff_Email=
        safe_text,
    staff_Salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    staff_Name=
        safe_text,
    staff_ContactNo=
        safe_text,
    staff_Department=
        safe_text,
    staff_Date_Of_Joint=
        st.dates(),
    staff_Id=
        st.integers(),
    staff_DOB=
        st.dates(),
    staff_Position=
        safe_text
)
Logout_external_strategy = st.builds(
    Logout_external,
)
Login_external_strategy = st.builds(
    Login_external,
)

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
def test_attendance_AttendTime_setter(instance):
    original = instance.AttendTime
    instance.AttendTime = original
    assert instance.AttendTime == original



@given(instance=Attendance_strategy)
def test_attendance_Leaving_Time_setter(instance):
    original = instance.Leaving_Time
    instance.Leaving_Time = original
    assert instance.Leaving_Time == original



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

@given(instance=Mission_strategy)
@settings(max_examples=50)
def test_mission_instantiation(instance):
    assert isinstance(instance, Mission)



@given(instance=Mission_strategy)
def test_mission_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original



@given(instance=Mission_strategy)
def test_mission_mission_id_setter(instance):
    original = instance.mission_id
    instance.mission_id = original
    assert instance.mission_id == original



@given(instance=Mission_strategy)
def test_mission_mission_StartDate_setter(instance):
    original = instance.mission_StartDate
    instance.mission_StartDate = original
    assert instance.mission_StartDate == original



@given(instance=Mission_strategy)
def test_mission_mission_NoOfDays_setter(instance):
    original = instance.mission_NoOfDays
    instance.mission_NoOfDays = original
    assert instance.mission_NoOfDays == original



@given(instance=Mission_strategy)
def test_mission_mission_detail_setter(instance):
    original = instance.mission_detail
    instance.mission_detail = original
    assert instance.mission_detail == original



@given(instance=Mission_strategy)
def test_mission_mission_Status_setter(instance):
    original = instance.mission_Status
    instance.mission_Status = original
    assert instance.mission_Status == original



@given(instance=Mission_strategy)
def test_mission_mission_Title_setter(instance):
    original = instance.mission_Title
    instance.mission_Title = original
    assert instance.mission_Title == original



@given(instance=Mission_strategy)
def test_mission_mission_EndDate_setter(instance):
    original = instance.mission_EndDate
    instance.mission_EndDate = original
    assert instance.mission_EndDate == original

@given(instance=Authenticate_staff_strategy)
@settings(max_examples=50)
def test_authenticate_staff_instantiation(instance):
    assert isinstance(instance, Authenticate_staff)



@given(instance=Authenticate_staff_strategy)
def test_authenticate_staff_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



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
def test_salary_Sly_Decrement_setter(instance):
    original = instance.Sly_Decrement
    instance.Sly_Decrement = original
    assert instance.Sly_Decrement == original



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

@given(instance=staff_member_strategy)
@settings(max_examples=50)
def test_staff_member_instantiation(instance):
    assert isinstance(instance, staff_member)



@given(instance=staff_member_strategy)
def test_staff_member_staff_Address_setter(instance):
    original = instance.staff_Address
    instance.staff_Address = original
    assert instance.staff_Address == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_NIC_setter(instance):
    original = instance.staff_NIC
    instance.staff_NIC = original
    assert instance.staff_NIC == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_Email_setter(instance):
    original = instance.staff_Email
    instance.staff_Email = original
    assert instance.staff_Email == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_Salary_setter(instance):
    original = instance.staff_Salary
    instance.staff_Salary = original
    assert instance.staff_Salary == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_Name_setter(instance):
    original = instance.staff_Name
    instance.staff_Name = original
    assert instance.staff_Name == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_ContactNo_setter(instance):
    original = instance.staff_ContactNo
    instance.staff_ContactNo = original
    assert instance.staff_ContactNo == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_Department_setter(instance):
    original = instance.staff_Department
    instance.staff_Department = original
    assert instance.staff_Department == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_Date_Of_Joint_setter(instance):
    original = instance.staff_Date_Of_Joint
    instance.staff_Date_Of_Joint = original
    assert instance.staff_Date_Of_Joint == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_DOB_setter(instance):
    original = instance.staff_DOB
    instance.staff_DOB = original
    assert instance.staff_DOB == original



@given(instance=staff_member_strategy)
def test_staff_member_staff_Position_setter(instance):
    original = instance.staff_Position
    instance.staff_Position = original
    assert instance.staff_Position == original

@given(instance=Logout_external_strategy)
@settings(max_examples=50)
def test_logout_external_instantiation(instance):
    assert isinstance(instance, Logout_external)

@given(instance=Login_external_strategy)
@settings(max_examples=50)
def test_login_external_instantiation(instance):
    assert isinstance(instance, Login_external)
