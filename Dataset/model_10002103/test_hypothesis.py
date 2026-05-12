import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    location,
    login,
    Attendance,
    Full_day,
    Haff_day,
    Leave,
    Employee,
    Admin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_location_is_not_abstract():
    assert not inspect.isabstract(location)


def test_location_constructor_exists():
    assert callable(location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(location.__init__)
    params = list(sig.parameters.keys())
    assert "Longitude" in params, "Missing parameter 'Longitude'"
    assert "Latitude" in params, "Missing parameter 'Latitude'"

def test_location_has_Longitude():
    assert hasattr(location, "Longitude")
    descriptor = None
    for klass in location.__mro__:
        if "Longitude" in klass.__dict__:
            descriptor = klass.__dict__["Longitude"]
            break
    assert isinstance(descriptor, property)

def test_location_has_Latitude():
    assert hasattr(location, "Latitude")
    descriptor = None
    for klass in location.__mro__:
        if "Latitude" in klass.__dict__:
            descriptor = klass.__dict__["Latitude"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(login)


def test_login_constructor_exists():
    assert callable(login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(login.__init__)
    params = list(sig.parameters.keys())
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"
    assert "login_id" in params, "Missing parameter 'login_id'"
    assert "loginpassword" in params, "Missing parameter 'loginpassword'"
    assert "loginUsername" in params, "Missing parameter 'loginUsername'"

def test_login_has_loginStatus():
    assert hasattr(login, "loginStatus")
    descriptor = None
    for klass in login.__mro__:
        if "loginStatus" in klass.__dict__:
            descriptor = klass.__dict__["loginStatus"]
            break
    assert isinstance(descriptor, property)

def test_login_has_login_id():
    assert hasattr(login, "login_id")
    descriptor = None
    for klass in login.__mro__:
        if "login_id" in klass.__dict__:
            descriptor = klass.__dict__["login_id"]
            break
    assert isinstance(descriptor, property)

def test_login_has_loginpassword():
    assert hasattr(login, "loginpassword")
    descriptor = None
    for klass in login.__mro__:
        if "loginpassword" in klass.__dict__:
            descriptor = klass.__dict__["loginpassword"]
            break
    assert isinstance(descriptor, property)

def test_login_has_loginUsername():
    assert hasattr(login, "loginUsername")
    descriptor = None
    for klass in login.__mro__:
        if "loginUsername" in klass.__dict__:
            descriptor = klass.__dict__["loginUsername"]
            break
    assert isinstance(descriptor, property)



def test_attendance_is_not_abstract():
    assert not inspect.isabstract(Attendance)


def test_attendance_constructor_exists():
    assert callable(Attendance.__init__)


def test_attendance_constructor_args():
    sig = inspect.signature(Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "atten_date" in params, "Missing parameter 'atten_date'"
    assert "atten_id" in params, "Missing parameter 'atten_id'"
    assert "atten_time" in params, "Missing parameter 'atten_time'"
    assert "atten_type" in params, "Missing parameter 'atten_type'"
    assert "atten_emp_id" in params, "Missing parameter 'atten_emp_id'"

def test_attendance_has_atten_date():
    assert hasattr(Attendance, "atten_date")
    descriptor = None
    for klass in Attendance.__mro__:
        if "atten_date" in klass.__dict__:
            descriptor = klass.__dict__["atten_date"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_atten_id():
    assert hasattr(Attendance, "atten_id")
    descriptor = None
    for klass in Attendance.__mro__:
        if "atten_id" in klass.__dict__:
            descriptor = klass.__dict__["atten_id"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_atten_time():
    assert hasattr(Attendance, "atten_time")
    descriptor = None
    for klass in Attendance.__mro__:
        if "atten_time" in klass.__dict__:
            descriptor = klass.__dict__["atten_time"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_atten_type():
    assert hasattr(Attendance, "atten_type")
    descriptor = None
    for klass in Attendance.__mro__:
        if "atten_type" in klass.__dict__:
            descriptor = klass.__dict__["atten_type"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_atten_emp_id():
    assert hasattr(Attendance, "atten_emp_id")
    descriptor = None
    for klass in Attendance.__mro__:
        if "atten_emp_id" in klass.__dict__:
            descriptor = klass.__dict__["atten_emp_id"]
            break
    assert isinstance(descriptor, property)



def test_full_day_is_not_abstract():
    assert not inspect.isabstract(Full_day)


def test_full_day_constructor_exists():
    assert callable(Full_day.__init__)


def test_full_day_constructor_args():
    sig = inspect.signature(Full_day.__init__)
    params = list(sig.parameters.keys())
    assert "end_date" in params, "Missing parameter 'end_date'"
    assert "start_date" in params, "Missing parameter 'start_date'"

def test_full_day_has_end_date():
    assert hasattr(Full_day, "end_date")
    descriptor = None
    for klass in Full_day.__mro__:
        if "end_date" in klass.__dict__:
            descriptor = klass.__dict__["end_date"]
            break
    assert isinstance(descriptor, property)

def test_full_day_has_start_date():
    assert hasattr(Full_day, "start_date")
    descriptor = None
    for klass in Full_day.__mro__:
        if "start_date" in klass.__dict__:
            descriptor = klass.__dict__["start_date"]
            break
    assert isinstance(descriptor, property)



def test_haff_day_is_not_abstract():
    assert not inspect.isabstract(Haff_day)


def test_haff_day_constructor_exists():
    assert callable(Haff_day.__init__)


def test_haff_day_constructor_args():
    sig = inspect.signature(Haff_day.__init__)
    params = list(sig.parameters.keys())
    assert "start_date" in params, "Missing parameter 'start_date'"

def test_haff_day_has_start_date():
    assert hasattr(Haff_day, "start_date")
    descriptor = None
    for klass in Haff_day.__mro__:
        if "start_date" in klass.__dict__:
            descriptor = klass.__dict__["start_date"]
            break
    assert isinstance(descriptor, property)



def test_leave_is_not_abstract():
    assert not inspect.isabstract(Leave)


def test_leave_constructor_exists():
    assert callable(Leave.__init__)


def test_leave_constructor_args():
    sig = inspect.signature(Leave.__init__)
    params = list(sig.parameters.keys())
    assert "l_description" in params, "Missing parameter 'l_description'"
    assert "l_id" in params, "Missing parameter 'l_id'"
    assert "l_type" in params, "Missing parameter 'l_type'"
    assert "l_emp_id" in params, "Missing parameter 'l_emp_id'"

def test_leave_has_l_description():
    assert hasattr(Leave, "l_description")
    descriptor = None
    for klass in Leave.__mro__:
        if "l_description" in klass.__dict__:
            descriptor = klass.__dict__["l_description"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_l_id():
    assert hasattr(Leave, "l_id")
    descriptor = None
    for klass in Leave.__mro__:
        if "l_id" in klass.__dict__:
            descriptor = klass.__dict__["l_id"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_l_type():
    assert hasattr(Leave, "l_type")
    descriptor = None
    for klass in Leave.__mro__:
        if "l_type" in klass.__dict__:
            descriptor = klass.__dict__["l_type"]
            break
    assert isinstance(descriptor, property)

def test_leave_has_l_emp_id():
    assert hasattr(Leave, "l_emp_id")
    descriptor = None
    for klass in Leave.__mro__:
        if "l_emp_id" in klass.__dict__:
            descriptor = klass.__dict__["l_emp_id"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "email_id" in params, "Missing parameter 'email_id'"
    assert "address" in params, "Missing parameter 'address'"
    assert "e_id" in params, "Missing parameter 'e_id'"
    assert "phone_no" in params, "Missing parameter 'phone_no'"
    assert "office_address" in params, "Missing parameter 'office_address'"
    assert "paasword" in params, "Missing parameter 'paasword'"

def test_employee_has_name():
    assert hasattr(Employee, "name")
    descriptor = None
    for klass in Employee.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_email_id():
    assert hasattr(Employee, "email_id")
    descriptor = None
    for klass in Employee.__mro__:
        if "email_id" in klass.__dict__:
            descriptor = klass.__dict__["email_id"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_address():
    assert hasattr(Employee, "address")
    descriptor = None
    for klass in Employee.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_e_id():
    assert hasattr(Employee, "e_id")
    descriptor = None
    for klass in Employee.__mro__:
        if "e_id" in klass.__dict__:
            descriptor = klass.__dict__["e_id"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_phone_no():
    assert hasattr(Employee, "phone_no")
    descriptor = None
    for klass in Employee.__mro__:
        if "phone_no" in klass.__dict__:
            descriptor = klass.__dict__["phone_no"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_office_address():
    assert hasattr(Employee, "office_address")
    descriptor = None
    for klass in Employee.__mro__:
        if "office_address" in klass.__dict__:
            descriptor = klass.__dict__["office_address"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_paasword():
    assert hasattr(Employee, "paasword")
    descriptor = None
    for klass in Employee.__mro__:
        if "paasword" in klass.__dict__:
            descriptor = klass.__dict__["paasword"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"

def test_admin_has_username():
    assert hasattr(Admin, "username")
    descriptor = None
    for klass in Admin.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
location_strategy = st.builds(
    location,
    Longitude=
        st.integers(),
    Latitude=
        st.integers()
)
login_strategy = st.builds(
    login,
    loginStatus=
        safe_text,
    login_id=
        st.integers(),
    loginpassword=
        safe_text,
    loginUsername=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    atten_date=
        safe_text,
    atten_id=
        st.integers(),
    atten_time=
        st.integers(),
    atten_type=
        safe_text,
    atten_emp_id=
        st.integers()
)
Full_day_strategy = st.builds(
    Full_day,
    end_date=
        st.integers(),
    start_date=
        st.integers()
)
Haff_day_strategy = st.builds(
    Haff_day,
    start_date=
        st.integers()
)
Leave_strategy = st.builds(
    Leave,
    l_description=
        safe_text,
    l_id=
        st.integers(),
    l_type=
        safe_text,
    l_emp_id=
        st.integers()
)
Employee_strategy = st.builds(
    Employee,
    name=
        safe_text,
    email_id=
        safe_text,
    address=
        safe_text,
    e_id=
        st.integers(),
    phone_no=
        st.integers(),
    office_address=
        safe_text,
    paasword=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    username=
        safe_text,
    password=
        safe_text
)

@given(instance=location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, location)



@given(instance=location_strategy)
def test_location_Longitude_setter(instance):
    original = instance.Longitude
    instance.Longitude = original
    assert instance.Longitude == original



@given(instance=location_strategy)
def test_location_Latitude_setter(instance):
    original = instance.Latitude
    instance.Latitude = original
    assert instance.Latitude == original

@given(instance=login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, login)



@given(instance=login_strategy)
def test_login_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original



@given(instance=login_strategy)
def test_login_login_id_setter(instance):
    original = instance.login_id
    instance.login_id = original
    assert instance.login_id == original



@given(instance=login_strategy)
def test_login_loginpassword_setter(instance):
    original = instance.loginpassword
    instance.loginpassword = original
    assert instance.loginpassword == original



@given(instance=login_strategy)
def test_login_loginUsername_setter(instance):
    original = instance.loginUsername
    instance.loginUsername = original
    assert instance.loginUsername == original

@given(instance=Attendance_strategy)
@settings(max_examples=50)
def test_attendance_instantiation(instance):
    assert isinstance(instance, Attendance)



@given(instance=Attendance_strategy)
def test_attendance_atten_date_setter(instance):
    original = instance.atten_date
    instance.atten_date = original
    assert instance.atten_date == original



@given(instance=Attendance_strategy)
def test_attendance_atten_id_setter(instance):
    original = instance.atten_id
    instance.atten_id = original
    assert instance.atten_id == original



@given(instance=Attendance_strategy)
def test_attendance_atten_time_setter(instance):
    original = instance.atten_time
    instance.atten_time = original
    assert instance.atten_time == original



@given(instance=Attendance_strategy)
def test_attendance_atten_type_setter(instance):
    original = instance.atten_type
    instance.atten_type = original
    assert instance.atten_type == original



@given(instance=Attendance_strategy)
def test_attendance_atten_emp_id_setter(instance):
    original = instance.atten_emp_id
    instance.atten_emp_id = original
    assert instance.atten_emp_id == original

@given(instance=Full_day_strategy)
@settings(max_examples=50)
def test_full_day_instantiation(instance):
    assert isinstance(instance, Full_day)



@given(instance=Full_day_strategy)
def test_full_day_end_date_setter(instance):
    original = instance.end_date
    instance.end_date = original
    assert instance.end_date == original



@given(instance=Full_day_strategy)
def test_full_day_start_date_setter(instance):
    original = instance.start_date
    instance.start_date = original
    assert instance.start_date == original

@given(instance=Haff_day_strategy)
@settings(max_examples=50)
def test_haff_day_instantiation(instance):
    assert isinstance(instance, Haff_day)



@given(instance=Haff_day_strategy)
def test_haff_day_start_date_setter(instance):
    original = instance.start_date
    instance.start_date = original
    assert instance.start_date == original

@given(instance=Leave_strategy)
@settings(max_examples=50)
def test_leave_instantiation(instance):
    assert isinstance(instance, Leave)



@given(instance=Leave_strategy)
def test_leave_l_description_setter(instance):
    original = instance.l_description
    instance.l_description = original
    assert instance.l_description == original



@given(instance=Leave_strategy)
def test_leave_l_id_setter(instance):
    original = instance.l_id
    instance.l_id = original
    assert instance.l_id == original



@given(instance=Leave_strategy)
def test_leave_l_type_setter(instance):
    original = instance.l_type
    instance.l_type = original
    assert instance.l_type == original



@given(instance=Leave_strategy)
def test_leave_l_emp_id_setter(instance):
    original = instance.l_emp_id
    instance.l_emp_id = original
    assert instance.l_emp_id == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Employee_strategy)
def test_employee_email_id_setter(instance):
    original = instance.email_id
    instance.email_id = original
    assert instance.email_id == original



@given(instance=Employee_strategy)
def test_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Employee_strategy)
def test_employee_e_id_setter(instance):
    original = instance.e_id
    instance.e_id = original
    assert instance.e_id == original



@given(instance=Employee_strategy)
def test_employee_phone_no_setter(instance):
    original = instance.phone_no
    instance.phone_no = original
    assert instance.phone_no == original



@given(instance=Employee_strategy)
def test_employee_office_address_setter(instance):
    original = instance.office_address
    instance.office_address = original
    assert instance.office_address == original



@given(instance=Employee_strategy)
def test_employee_paasword_setter(instance):
    original = instance.paasword
    instance.paasword = original
    assert instance.paasword == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
