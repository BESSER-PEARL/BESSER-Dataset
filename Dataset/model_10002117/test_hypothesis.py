import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Add_notes,
    Show_all_grades,
    Home_page,
    Interface2_Interface,
    Interface1_Interface,
    Class,
    Interface_Interface,
    New_user,
    names,
    Login,
    Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_add_notes_is_not_abstract():
    assert not inspect.isabstract(Add_notes)


def test_add_notes_constructor_exists():
    assert callable(Add_notes.__init__)


def test_add_notes_constructor_args():
    sig = inspect.signature(Add_notes.__init__)
    params = list(sig.parameters.keys())
    assert "Course_Name" in params, "Missing parameter 'Course_Name'"
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "Notes_taken" in params, "Missing parameter 'Notes_taken'"

def test_add_notes_has_Course_Name():
    assert hasattr(Add_notes, "Course_Name")
    descriptor = None
    for klass in Add_notes.__mro__:
        if "Course_Name" in klass.__dict__:
            descriptor = klass.__dict__["Course_Name"]
            break
    assert isinstance(descriptor, property)

def test_add_notes_has_Student_ID():
    assert hasattr(Add_notes, "Student_ID")
    descriptor = None
    for klass in Add_notes.__mro__:
        if "Student_ID" in klass.__dict__:
            descriptor = klass.__dict__["Student_ID"]
            break
    assert isinstance(descriptor, property)

def test_add_notes_has_Notes_taken():
    assert hasattr(Add_notes, "Notes_taken")
    descriptor = None
    for klass in Add_notes.__mro__:
        if "Notes_taken" in klass.__dict__:
            descriptor = klass.__dict__["Notes_taken"]
            break
    assert isinstance(descriptor, property)



def test_show_all_grades_is_not_abstract():
    assert not inspect.isabstract(Show_all_grades)


def test_show_all_grades_constructor_exists():
    assert callable(Show_all_grades.__init__)


def test_show_all_grades_constructor_args():
    sig = inspect.signature(Show_all_grades.__init__)
    params = list(sig.parameters.keys())
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "First_Name" in params, "Missing parameter 'First_Name'"
    assert "Teacher" in params, "Missing parameter 'Teacher'"
    assert "Course_name" in params, "Missing parameter 'Course_name'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "Grade_earned" in params, "Missing parameter 'Grade_earned'"

def test_show_all_grades_has_Student_ID():
    assert hasattr(Show_all_grades, "Student_ID")
    descriptor = None
    for klass in Show_all_grades.__mro__:
        if "Student_ID" in klass.__dict__:
            descriptor = klass.__dict__["Student_ID"]
            break
    assert isinstance(descriptor, property)

def test_show_all_grades_has_First_Name():
    assert hasattr(Show_all_grades, "First_Name")
    descriptor = None
    for klass in Show_all_grades.__mro__:
        if "First_Name" in klass.__dict__:
            descriptor = klass.__dict__["First_Name"]
            break
    assert isinstance(descriptor, property)

def test_show_all_grades_has_Teacher():
    assert hasattr(Show_all_grades, "Teacher")
    descriptor = None
    for klass in Show_all_grades.__mro__:
        if "Teacher" in klass.__dict__:
            descriptor = klass.__dict__["Teacher"]
            break
    assert isinstance(descriptor, property)

def test_show_all_grades_has_Course_name():
    assert hasattr(Show_all_grades, "Course_name")
    descriptor = None
    for klass in Show_all_grades.__mro__:
        if "Course_name" in klass.__dict__:
            descriptor = klass.__dict__["Course_name"]
            break
    assert isinstance(descriptor, property)

def test_show_all_grades_has_Last_Name():
    assert hasattr(Show_all_grades, "Last_Name")
    descriptor = None
    for klass in Show_all_grades.__mro__:
        if "Last_Name" in klass.__dict__:
            descriptor = klass.__dict__["Last_Name"]
            break
    assert isinstance(descriptor, property)

def test_show_all_grades_has_Grade_earned():
    assert hasattr(Show_all_grades, "Grade_earned")
    descriptor = None
    for klass in Show_all_grades.__mro__:
        if "Grade_earned" in klass.__dict__:
            descriptor = klass.__dict__["Grade_earned"]
            break
    assert isinstance(descriptor, property)



def test_home_page_is_not_abstract():
    assert not inspect.isabstract(Home_page)


def test_home_page_constructor_exists():
    assert callable(Home_page.__init__)


def test_home_page_constructor_args():
    sig = inspect.signature(Home_page.__init__)
    params = list(sig.parameters.keys())



def test_interface2_interface_is_not_abstract():
    assert not inspect.isabstract(Interface2_Interface)


def test_interface2_interface_constructor_exists():
    assert callable(Interface2_Interface.__init__)


def test_interface2_interface_constructor_args():
    sig = inspect.signature(Interface2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_interface1_interface_is_not_abstract():
    assert not inspect.isabstract(Interface1_Interface)


def test_interface1_interface_constructor_exists():
    assert callable(Interface1_Interface.__init__)


def test_interface1_interface_constructor_args():
    sig = inspect.signature(Interface1_Interface.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_new_user_is_not_abstract():
    assert not inspect.isabstract(New_user)


def test_new_user_constructor_exists():
    assert callable(New_user.__init__)


def test_new_user_constructor_args():
    sig = inspect.signature(New_user.__init__)
    params = list(sig.parameters.keys())
    assert "First_name" in params, "Missing parameter 'First_name'"
    assert "Contact_No" in params, "Missing parameter 'Contact_No'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "Major" in params, "Missing parameter 'Major'"
    assert "Student_ID1" in params, "Missing parameter 'Student_ID1'"

def test_new_user_has_First_name():
    assert hasattr(New_user, "First_name")
    descriptor = None
    for klass in New_user.__mro__:
        if "First_name" in klass.__dict__:
            descriptor = klass.__dict__["First_name"]
            break
    assert isinstance(descriptor, property)

def test_new_user_has_Contact_No():
    assert hasattr(New_user, "Contact_No")
    descriptor = None
    for klass in New_user.__mro__:
        if "Contact_No" in klass.__dict__:
            descriptor = klass.__dict__["Contact_No"]
            break
    assert isinstance(descriptor, property)

def test_new_user_has_Last_Name():
    assert hasattr(New_user, "Last_Name")
    descriptor = None
    for klass in New_user.__mro__:
        if "Last_Name" in klass.__dict__:
            descriptor = klass.__dict__["Last_Name"]
            break
    assert isinstance(descriptor, property)

def test_new_user_has_Student_ID():
    assert hasattr(New_user, "Student_ID")
    descriptor = None
    for klass in New_user.__mro__:
        if "Student_ID" in klass.__dict__:
            descriptor = klass.__dict__["Student_ID"]
            break
    assert isinstance(descriptor, property)

def test_new_user_has_Major():
    assert hasattr(New_user, "Major")
    descriptor = None
    for klass in New_user.__mro__:
        if "Major" in klass.__dict__:
            descriptor = klass.__dict__["Major"]
            break
    assert isinstance(descriptor, property)

def test_new_user_has_Student_ID1():
    assert hasattr(New_user, "Student_ID1")
    descriptor = None
    for klass in New_user.__mro__:
        if "Student_ID1" in klass.__dict__:
            descriptor = klass.__dict__["Student_ID1"]
            break
    assert isinstance(descriptor, property)



def test_names_is_not_abstract():
    assert not inspect.isabstract(names)


def test_names_constructor_exists():
    assert callable(names.__init__)


def test_names_constructor_args():
    sig = inspect.signature(names.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_login_has_Email():
    assert hasattr(Login, "Email")
    descriptor = None
    for klass in Login.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_login_has_Student_ID():
    assert hasattr(Login, "Student_ID")
    descriptor = None
    for klass in Login.__mro__:
        if "Student_ID" in klass.__dict__:
            descriptor = klass.__dict__["Student_ID"]
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



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "Room" in params, "Missing parameter 'Room'"
    assert "Course_Index" in params, "Missing parameter 'Course_Index'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "Teacher" in params, "Missing parameter 'Teacher'"
    assert "Day" in params, "Missing parameter 'Day'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Grade_earned" in params, "Missing parameter 'Grade_earned'"
    assert "Course_name" in params, "Missing parameter 'Course_name'"

def test_course_has_Room():
    assert hasattr(Course, "Room")
    descriptor = None
    for klass in Course.__mro__:
        if "Room" in klass.__dict__:
            descriptor = klass.__dict__["Room"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Course_Index():
    assert hasattr(Course, "Course_Index")
    descriptor = None
    for klass in Course.__mro__:
        if "Course_Index" in klass.__dict__:
            descriptor = klass.__dict__["Course_Index"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Status():
    assert hasattr(Course, "Status")
    descriptor = None
    for klass in Course.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Student_ID():
    assert hasattr(Course, "Student_ID")
    descriptor = None
    for klass in Course.__mro__:
        if "Student_ID" in klass.__dict__:
            descriptor = klass.__dict__["Student_ID"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Teacher():
    assert hasattr(Course, "Teacher")
    descriptor = None
    for klass in Course.__mro__:
        if "Teacher" in klass.__dict__:
            descriptor = klass.__dict__["Teacher"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Day():
    assert hasattr(Course, "Day")
    descriptor = None
    for klass in Course.__mro__:
        if "Day" in klass.__dict__:
            descriptor = klass.__dict__["Day"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Time():
    assert hasattr(Course, "Time")
    descriptor = None
    for klass in Course.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Grade_earned():
    assert hasattr(Course, "Grade_earned")
    descriptor = None
    for klass in Course.__mro__:
        if "Grade_earned" in klass.__dict__:
            descriptor = klass.__dict__["Grade_earned"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Course_name():
    assert hasattr(Course, "Course_name")
    descriptor = None
    for klass in Course.__mro__:
        if "Course_name" in klass.__dict__:
            descriptor = klass.__dict__["Course_name"]
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
Add_notes_strategy = st.builds(
    Add_notes,
    Course_Name=
        safe_text,
    Student_ID=
        st.integers(),
    Notes_taken=
        safe_text
)
Show_all_grades_strategy = st.builds(
    Show_all_grades,
    Student_ID=
        st.integers(),
    First_Name=
        safe_text,
    Teacher=
        safe_text,
    Course_name=
        safe_text,
    Last_Name=
        safe_text,
    Grade_earned=
        safe_text
)
Home_page_strategy = st.builds(
    Home_page,
)
Interface2_Interface_strategy = st.builds(
    Interface2_Interface,
)
Interface1_Interface_strategy = st.builds(
    Interface1_Interface,
)
Class_strategy = st.builds(
    Class,
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
New_user_strategy = st.builds(
    New_user,
    First_name=
        safe_text,
    Contact_No=
        st.integers(),
    Last_Name=
        safe_text,
    Student_ID=
        st.integers(),
    Major=
        safe_text,
    Student_ID1=
        st.integers()
)
names_strategy = st.builds(
    names,
)
Login_strategy = st.builds(
    Login,
    Email=
        safe_text,
    Student_ID=
        st.integers(),
    Password=
        safe_text
)
Course_strategy = st.builds(
    Course,
    Room=
        st.integers(),
    Course_Index=
        st.integers(),
    Status=
        safe_text,
    Student_ID=
        st.integers(),
    Teacher=
        safe_text,
    Day=
        safe_text,
    Time=
        safe_text,
    Grade_earned=
        safe_text,
    Course_name=
        safe_text
)

@given(instance=Add_notes_strategy)
@settings(max_examples=50)
def test_add_notes_instantiation(instance):
    assert isinstance(instance, Add_notes)



@given(instance=Add_notes_strategy)
def test_add_notes_Course_Name_setter(instance):
    original = instance.Course_Name
    instance.Course_Name = original
    assert instance.Course_Name == original



@given(instance=Add_notes_strategy)
def test_add_notes_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=Add_notes_strategy)
def test_add_notes_Notes_taken_setter(instance):
    original = instance.Notes_taken
    instance.Notes_taken = original
    assert instance.Notes_taken == original

@given(instance=Show_all_grades_strategy)
@settings(max_examples=50)
def test_show_all_grades_instantiation(instance):
    assert isinstance(instance, Show_all_grades)



@given(instance=Show_all_grades_strategy)
def test_show_all_grades_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=Show_all_grades_strategy)
def test_show_all_grades_First_Name_setter(instance):
    original = instance.First_Name
    instance.First_Name = original
    assert instance.First_Name == original



@given(instance=Show_all_grades_strategy)
def test_show_all_grades_Teacher_setter(instance):
    original = instance.Teacher
    instance.Teacher = original
    assert instance.Teacher == original



@given(instance=Show_all_grades_strategy)
def test_show_all_grades_Course_name_setter(instance):
    original = instance.Course_name
    instance.Course_name = original
    assert instance.Course_name == original



@given(instance=Show_all_grades_strategy)
def test_show_all_grades_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=Show_all_grades_strategy)
def test_show_all_grades_Grade_earned_setter(instance):
    original = instance.Grade_earned
    instance.Grade_earned = original
    assert instance.Grade_earned == original

@given(instance=Home_page_strategy)
@settings(max_examples=50)
def test_home_page_instantiation(instance):
    assert isinstance(instance, Home_page)

@given(instance=Interface2_Interface_strategy)
@settings(max_examples=50)
def test_interface2_interface_instantiation(instance):
    assert isinstance(instance, Interface2_Interface)

@given(instance=Interface1_Interface_strategy)
@settings(max_examples=50)
def test_interface1_interface_instantiation(instance):
    assert isinstance(instance, Interface1_Interface)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)

@given(instance=New_user_strategy)
@settings(max_examples=50)
def test_new_user_instantiation(instance):
    assert isinstance(instance, New_user)



@given(instance=New_user_strategy)
def test_new_user_First_name_setter(instance):
    original = instance.First_name
    instance.First_name = original
    assert instance.First_name == original



@given(instance=New_user_strategy)
def test_new_user_Contact_No_setter(instance):
    original = instance.Contact_No
    instance.Contact_No = original
    assert instance.Contact_No == original



@given(instance=New_user_strategy)
def test_new_user_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=New_user_strategy)
def test_new_user_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=New_user_strategy)
def test_new_user_Major_setter(instance):
    original = instance.Major
    instance.Major = original
    assert instance.Major == original



@given(instance=New_user_strategy)
def test_new_user_Student_ID1_setter(instance):
    original = instance.Student_ID1
    instance.Student_ID1 = original
    assert instance.Student_ID1 == original

@given(instance=names_strategy)
@settings(max_examples=50)
def test_names_instantiation(instance):
    assert isinstance(instance, names)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Login_strategy)
def test_login_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=Login_strategy)
def test_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course_Room_setter(instance):
    original = instance.Room
    instance.Room = original
    assert instance.Room == original



@given(instance=Course_strategy)
def test_course_Course_Index_setter(instance):
    original = instance.Course_Index
    instance.Course_Index = original
    assert instance.Course_Index == original



@given(instance=Course_strategy)
def test_course_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Course_strategy)
def test_course_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=Course_strategy)
def test_course_Teacher_setter(instance):
    original = instance.Teacher
    instance.Teacher = original
    assert instance.Teacher == original



@given(instance=Course_strategy)
def test_course_Day_setter(instance):
    original = instance.Day
    instance.Day = original
    assert instance.Day == original



@given(instance=Course_strategy)
def test_course_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Course_strategy)
def test_course_Grade_earned_setter(instance):
    original = instance.Grade_earned
    instance.Grade_earned = original
    assert instance.Grade_earned == original



@given(instance=Course_strategy)
def test_course_Course_name_setter(instance):
    original = instance.Course_name
    instance.Course_name = original
    assert instance.Course_name == original
