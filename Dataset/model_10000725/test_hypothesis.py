import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Database,
    Attendance,
    Monitor,
    Login,
    Faculty,
    Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_database_constructor_exists():
    assert callable(Database.__init__)


def test_database_constructor_args():
    sig = inspect.signature(Database.__init__)
    params = list(sig.parameters.keys())
    assert "Attendance" in params, "Missing parameter 'Attendance'"
    assert "Category" in params, "Missing parameter 'Category'"

def test_database_has_Attendance():
    assert hasattr(Database, "Attendance")
    descriptor = None
    for klass in Database.__mro__:
        if "Attendance" in klass.__dict__:
            descriptor = klass.__dict__["Attendance"]
            break
    assert isinstance(descriptor, property)

def test_database_has_Category():
    assert hasattr(Database, "Category")
    descriptor = None
    for klass in Database.__mro__:
        if "Category" in klass.__dict__:
            descriptor = klass.__dict__["Category"]
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
    assert "ID" in params, "Missing parameter 'ID'"

def test_attendance_has_Date():
    assert hasattr(Attendance, "Date")
    descriptor = None
    for klass in Attendance.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_attendance_has_ID():
    assert hasattr(Attendance, "ID")
    descriptor = None
    for klass in Attendance.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_monitor_is_not_abstract():
    assert not inspect.isabstract(Monitor)


def test_monitor_constructor_exists():
    assert callable(Monitor.__init__)


def test_monitor_constructor_args():
    sig = inspect.signature(Monitor.__init__)
    params = list(sig.parameters.keys())
    assert "Location" in params, "Missing parameter 'Location'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_monitor_has_Location():
    assert hasattr(Monitor, "Location")
    descriptor = None
    for klass in Monitor.__mro__:
        if "Location" in klass.__dict__:
            descriptor = klass.__dict__["Location"]
            break
    assert isinstance(descriptor, property)

def test_monitor_has_Time():
    assert hasattr(Monitor, "Time")
    descriptor = None
    for klass in Monitor.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_monitor_has_Date():
    assert hasattr(Monitor, "Date")
    descriptor = None
    for klass in Monitor.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "login" in params, "Missing parameter 'login'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_login_has_login():
    assert hasattr(Login, "login")
    descriptor = None
    for klass in Login.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_login_has_Username():
    assert hasattr(Login, "Username")
    descriptor = None
    for klass in Login.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
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



def test_faculty_is_not_abstract():
    assert not inspect.isabstract(Faculty)


def test_faculty_constructor_exists():
    assert callable(Faculty.__init__)


def test_faculty_constructor_args():
    sig = inspect.signature(Faculty.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_faculty_has_Username():
    assert hasattr(Faculty, "Username")
    descriptor = None
    for klass in Faculty.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_faculty_has_ID():
    assert hasattr(Faculty, "ID")
    descriptor = None
    for klass in Faculty.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_faculty_has_Password():
    assert hasattr(Faculty, "Password")
    descriptor = None
    for klass in Faculty.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "First_Name" in params, "Missing parameter 'First_Name'"

def test_student_has_Last_Name():
    assert hasattr(Student, "Last_Name")
    descriptor = None
    for klass in Student.__mro__:
        if "Last_Name" in klass.__dict__:
            descriptor = klass.__dict__["Last_Name"]
            break
    assert isinstance(descriptor, property)

def test_student_has_Username():
    assert hasattr(Student, "Username")
    descriptor = None
    for klass in Student.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_student_has_Password():
    assert hasattr(Student, "Password")
    descriptor = None
    for klass in Student.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_student_has_ID():
    assert hasattr(Student, "ID")
    descriptor = None
    for klass in Student.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_student_has_First_Name():
    assert hasattr(Student, "First_Name")
    descriptor = None
    for klass in Student.__mro__:
        if "First_Name" in klass.__dict__:
            descriptor = klass.__dict__["First_Name"]
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
Database_strategy = st.builds(
    Database,
    Attendance=
        safe_text,
    Category=
        safe_text
)
Attendance_strategy = st.builds(
    Attendance,
    Date=
        safe_text,
    ID=
        safe_text
)
Monitor_strategy = st.builds(
    Monitor,
    Location=
        safe_text,
    Time=
        st.integers(),
    Date=
        st.dates()
)
Login_strategy = st.builds(
    Login,
    login=
        st.none(),
    Username=
        safe_text,
    Password=
        safe_text
)
Faculty_strategy = st.builds(
    Faculty,
    Username=
        safe_text,
    ID=
        safe_text,
    Password=
        safe_text
)
Student_strategy = st.builds(
    Student,
    Last_Name=
        safe_text,
    Username=
        safe_text,
    Password=
        safe_text,
    ID=
        safe_text,
    First_Name=
        safe_text
)

@given(instance=Database_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, Database)



@given(instance=Database_strategy)
def test_database_Attendance_setter(instance):
    original = instance.Attendance
    instance.Attendance = original
    assert instance.Attendance == original



@given(instance=Database_strategy)
def test_database_Category_setter(instance):
    original = instance.Category
    instance.Category = original
    assert instance.Category == original

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
def test_attendance_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Monitor_strategy)
@settings(max_examples=50)
def test_monitor_instantiation(instance):
    assert isinstance(instance, Monitor)



@given(instance=Monitor_strategy)
def test_monitor_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original



@given(instance=Monitor_strategy)
def test_monitor_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Monitor_strategy)
def test_monitor_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=Login_strategy)
def test_login_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Login_strategy)
def test_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Faculty_strategy)
@settings(max_examples=50)
def test_faculty_instantiation(instance):
    assert isinstance(instance, Faculty)



@given(instance=Faculty_strategy)
def test_faculty_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Faculty_strategy)
def test_faculty_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Faculty_strategy)
def test_faculty_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=Student_strategy)
def test_student_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Student_strategy)
def test_student_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Student_strategy)
def test_student_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Student_strategy)
def test_student_First_Name_setter(instance):
    original = instance.First_Name
    instance.First_Name = original
    assert instance.First_Name == original
