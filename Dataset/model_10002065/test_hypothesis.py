import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Exceptions,
    Report,
    Email,
    Exam,
    Course,
    T,
    User,
    ILogin_Interface,
    Department,
    Binary_File,
    Student,
    Instructor,
    Finance,
    str,
    Stuff,
    Person,
    Admin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exceptions_is_not_abstract():
    assert not inspect.isabstract(Exceptions)


def test_exceptions_constructor_exists():
    assert callable(Exceptions.__init__)


def test_exceptions_constructor_args():
    sig = inspect.signature(Exceptions.__init__)
    params = list(sig.parameters.keys())



def test_report_is_not_abstract():
    assert not inspect.isabstract(Report)


def test_report_constructor_exists():
    assert callable(Report.__init__)


def test_report_constructor_args():
    sig = inspect.signature(Report.__init__)
    params = list(sig.parameters.keys())



def test_email_is_not_abstract():
    assert not inspect.isabstract(Email)


def test_email_constructor_exists():
    assert callable(Email.__init__)


def test_email_constructor_args():
    sig = inspect.signature(Email.__init__)
    params = list(sig.parameters.keys())



def test_exam_is_not_abstract():
    assert not inspect.isabstract(Exam)


def test_exam_constructor_exists():
    assert callable(Exam.__init__)


def test_exam_constructor_args():
    sig = inspect.signature(Exam.__init__)
    params = list(sig.parameters.keys())
    assert "MaxGrade" in params, "Missing parameter 'MaxGrade'"
    assert "EName" in params, "Missing parameter 'EName'"
    assert "ETime" in params, "Missing parameter 'ETime'"

def test_exam_has_MaxGrade():
    assert hasattr(Exam, "MaxGrade")
    descriptor = None
    for klass in Exam.__mro__:
        if "MaxGrade" in klass.__dict__:
            descriptor = klass.__dict__["MaxGrade"]
            break
    assert isinstance(descriptor, property)

def test_exam_has_EName():
    assert hasattr(Exam, "EName")
    descriptor = None
    for klass in Exam.__mro__:
        if "EName" in klass.__dict__:
            descriptor = klass.__dict__["EName"]
            break
    assert isinstance(descriptor, property)

def test_exam_has_ETime():
    assert hasattr(Exam, "ETime")
    descriptor = None
    for klass in Exam.__mro__:
        if "ETime" in klass.__dict__:
            descriptor = klass.__dict__["ETime"]
            break
    assert isinstance(descriptor, property)



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "CName" in params, "Missing parameter 'CName'"
    assert "CInstructor" in params, "Missing parameter 'CInstructor'"
    assert "CPrice" in params, "Missing parameter 'CPrice'"
    assert "CCode" in params, "Missing parameter 'CCode'"

def test_course_has_CName():
    assert hasattr(Course, "CName")
    descriptor = None
    for klass in Course.__mro__:
        if "CName" in klass.__dict__:
            descriptor = klass.__dict__["CName"]
            break
    assert isinstance(descriptor, property)

def test_course_has_CInstructor():
    assert hasattr(Course, "CInstructor")
    descriptor = None
    for klass in Course.__mro__:
        if "CInstructor" in klass.__dict__:
            descriptor = klass.__dict__["CInstructor"]
            break
    assert isinstance(descriptor, property)

def test_course_has_CPrice():
    assert hasattr(Course, "CPrice")
    descriptor = None
    for klass in Course.__mro__:
        if "CPrice" in klass.__dict__:
            descriptor = klass.__dict__["CPrice"]
            break
    assert isinstance(descriptor, property)

def test_course_has_CCode():
    assert hasattr(Course, "CCode")
    descriptor = None
    for klass in Course.__mro__:
        if "CCode" in klass.__dict__:
            descriptor = klass.__dict__["CCode"]
            break
    assert isinstance(descriptor, property)



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Fname" in params, "Missing parameter 'Fname'"
    assert "Lname" in params, "Missing parameter 'Lname'"

def test_user_has_email():
    assert hasattr(User, "email")
    descriptor = None
    for klass in User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Fname():
    assert hasattr(User, "Fname")
    descriptor = None
    for klass in User.__mro__:
        if "Fname" in klass.__dict__:
            descriptor = klass.__dict__["Fname"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Lname():
    assert hasattr(User, "Lname")
    descriptor = None
    for klass in User.__mro__:
        if "Lname" in klass.__dict__:
            descriptor = klass.__dict__["Lname"]
            break
    assert isinstance(descriptor, property)



def test_ilogin_interface_is_not_abstract():
    assert not inspect.isabstract(ILogin_Interface)


def test_ilogin_interface_constructor_exists():
    assert callable(ILogin_Interface.__init__)


def test_ilogin_interface_constructor_args():
    sig = inspect.signature(ILogin_Interface.__init__)
    params = list(sig.parameters.keys())



def test_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_department_constructor_exists():
    assert callable(Department.__init__)


def test_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "deptId" in params, "Missing parameter 'deptId'"
    assert "deptName" in params, "Missing parameter 'deptName'"

def test_department_has_deptId():
    assert hasattr(Department, "deptId")
    descriptor = None
    for klass in Department.__mro__:
        if "deptId" in klass.__dict__:
            descriptor = klass.__dict__["deptId"]
            break
    assert isinstance(descriptor, property)

def test_department_has_deptName():
    assert hasattr(Department, "deptName")
    descriptor = None
    for klass in Department.__mro__:
        if "deptName" in klass.__dict__:
            descriptor = klass.__dict__["deptName"]
            break
    assert isinstance(descriptor, property)



def test_binary_file_is_not_abstract():
    assert not inspect.isabstract(Binary_File)


def test_binary_file_constructor_exists():
    assert callable(Binary_File.__init__)


def test_binary_file_constructor_args():
    sig = inspect.signature(Binary_File.__init__)
    params = list(sig.parameters.keys())



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "SGender" in params, "Missing parameter 'SGender'"
    assert "SAge" in params, "Missing parameter 'SAge'"

def test_student_has_SGender():
    assert hasattr(Student, "SGender")
    descriptor = None
    for klass in Student.__mro__:
        if "SGender" in klass.__dict__:
            descriptor = klass.__dict__["SGender"]
            break
    assert isinstance(descriptor, property)

def test_student_has_SAge():
    assert hasattr(Student, "SAge")
    descriptor = None
    for klass in Student.__mro__:
        if "SAge" in klass.__dict__:
            descriptor = klass.__dict__["SAge"]
            break
    assert isinstance(descriptor, property)



def test_instructor_is_not_abstract():
    assert not inspect.isabstract(Instructor)


def test_instructor_constructor_exists():
    assert callable(Instructor.__init__)


def test_instructor_constructor_args():
    sig = inspect.signature(Instructor.__init__)
    params = list(sig.parameters.keys())



def test_finance_is_not_abstract():
    assert not inspect.isabstract(Finance)


def test_finance_constructor_exists():
    assert callable(Finance.__init__)


def test_finance_constructor_args():
    sig = inspect.signature(Finance.__init__)
    params = list(sig.parameters.keys())



def test_str_is_not_abstract():
    assert not inspect.isabstract(str)


def test_str_constructor_exists():
    assert callable(str.__init__)


def test_str_constructor_args():
    sig = inspect.signature(str.__init__)
    params = list(sig.parameters.keys())



def test_stuff_is_not_abstract():
    assert not inspect.isabstract(Stuff)


def test_stuff_constructor_exists():
    assert callable(Stuff.__init__)


def test_stuff_constructor_args():
    sig = inspect.signature(Stuff.__init__)
    params = list(sig.parameters.keys())
    assert "WorkHours" in params, "Missing parameter 'WorkHours'"
    assert "Salary" in params, "Missing parameter 'Salary'"

def test_stuff_has_WorkHours():
    assert hasattr(Stuff, "WorkHours")
    descriptor = None
    for klass in Stuff.__mro__:
        if "WorkHours" in klass.__dict__:
            descriptor = klass.__dict__["WorkHours"]
            break
    assert isinstance(descriptor, property)

def test_stuff_has_Salary():
    assert hasattr(Stuff, "Salary")
    descriptor = None
    for klass in Stuff.__mro__:
        if "Salary" in klass.__dict__:
            descriptor = klass.__dict__["Salary"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "PhoneNum" in params, "Missing parameter 'PhoneNum'"

def test_person_has_Id():
    assert hasattr(Person, "Id")
    descriptor = None
    for klass in Person.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_person_has_PhoneNum():
    assert hasattr(Person, "PhoneNum")
    descriptor = None
    for klass in Person.__mro__:
        if "PhoneNum" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNum"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
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
Exceptions_strategy = st.builds(
    Exceptions,
)
Report_strategy = st.builds(
    Report,
)
Email_strategy = st.builds(
    Email,
)
Exam_strategy = st.builds(
    Exam,
    MaxGrade=
        safe_text,
    EName=
        safe_text,
    ETime=
        safe_text
)
Course_strategy = st.builds(
    Course,
    CName=
        safe_text,
    CInstructor=
        safe_text,
    CPrice=
        safe_text,
    CCode=
        safe_text
)
T_strategy = st.builds(
    T,
)
User_strategy = st.builds(
    User,
    email=
        safe_text,
    Password=
        safe_text,
    Fname=
        safe_text,
    Lname=
        safe_text
)
ILogin_Interface_strategy = st.builds(
    ILogin_Interface,
)
Department_strategy = st.builds(
    Department,
    deptId=
        safe_text,
    deptName=
        safe_text
)
Binary_File_strategy = st.builds(
    Binary_File,
)
Student_strategy = st.builds(
    Student,
    SGender=
        safe_text,
    SAge=
        st.integers()
)
Instructor_strategy = st.builds(
    Instructor,
)
Finance_strategy = st.builds(
    Finance,
)
str_strategy = st.builds(
    str,
)
Stuff_strategy = st.builds(
    Stuff,
    WorkHours=
        safe_text,
    Salary=
        safe_text
)
Person_strategy = st.builds(
    Person,
    Id=
        safe_text,
    PhoneNum=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
)

@given(instance=Exceptions_strategy)
@settings(max_examples=50)
def test_exceptions_instantiation(instance):
    assert isinstance(instance, Exceptions)

@given(instance=Report_strategy)
@settings(max_examples=50)
def test_report_instantiation(instance):
    assert isinstance(instance, Report)

@given(instance=Email_strategy)
@settings(max_examples=50)
def test_email_instantiation(instance):
    assert isinstance(instance, Email)

@given(instance=Exam_strategy)
@settings(max_examples=50)
def test_exam_instantiation(instance):
    assert isinstance(instance, Exam)



@given(instance=Exam_strategy)
def test_exam_MaxGrade_setter(instance):
    original = instance.MaxGrade
    instance.MaxGrade = original
    assert instance.MaxGrade == original



@given(instance=Exam_strategy)
def test_exam_EName_setter(instance):
    original = instance.EName
    instance.EName = original
    assert instance.EName == original



@given(instance=Exam_strategy)
def test_exam_ETime_setter(instance):
    original = instance.ETime
    instance.ETime = original
    assert instance.ETime == original

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course_CName_setter(instance):
    original = instance.CName
    instance.CName = original
    assert instance.CName == original



@given(instance=Course_strategy)
def test_course_CInstructor_setter(instance):
    original = instance.CInstructor
    instance.CInstructor = original
    assert instance.CInstructor == original



@given(instance=Course_strategy)
def test_course_CPrice_setter(instance):
    original = instance.CPrice
    instance.CPrice = original
    assert instance.CPrice == original



@given(instance=Course_strategy)
def test_course_CCode_setter(instance):
    original = instance.CCode
    instance.CCode = original
    assert instance.CCode == original

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_user_Fname_setter(instance):
    original = instance.Fname
    instance.Fname = original
    assert instance.Fname == original



@given(instance=User_strategy)
def test_user_Lname_setter(instance):
    original = instance.Lname
    instance.Lname = original
    assert instance.Lname == original

@given(instance=ILogin_Interface_strategy)
@settings(max_examples=50)
def test_ilogin_interface_instantiation(instance):
    assert isinstance(instance, ILogin_Interface)

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_department_deptId_setter(instance):
    original = instance.deptId
    instance.deptId = original
    assert instance.deptId == original



@given(instance=Department_strategy)
def test_department_deptName_setter(instance):
    original = instance.deptName
    instance.deptName = original
    assert instance.deptName == original

@given(instance=Binary_File_strategy)
@settings(max_examples=50)
def test_binary_file_instantiation(instance):
    assert isinstance(instance, Binary_File)

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_SGender_setter(instance):
    original = instance.SGender
    instance.SGender = original
    assert instance.SGender == original



@given(instance=Student_strategy)
def test_student_SAge_setter(instance):
    original = instance.SAge
    instance.SAge = original
    assert instance.SAge == original

@given(instance=Instructor_strategy)
@settings(max_examples=50)
def test_instructor_instantiation(instance):
    assert isinstance(instance, Instructor)

@given(instance=Finance_strategy)
@settings(max_examples=50)
def test_finance_instantiation(instance):
    assert isinstance(instance, Finance)

@given(instance=str_strategy)
@settings(max_examples=50)
def test_str_instantiation(instance):
    assert isinstance(instance, str)

@given(instance=Stuff_strategy)
@settings(max_examples=50)
def test_stuff_instantiation(instance):
    assert isinstance(instance, Stuff)



@given(instance=Stuff_strategy)
def test_stuff_WorkHours_setter(instance):
    original = instance.WorkHours
    instance.WorkHours = original
    assert instance.WorkHours == original



@given(instance=Stuff_strategy)
def test_stuff_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Person_strategy)
def test_person_PhoneNum_setter(instance):
    original = instance.PhoneNum
    instance.PhoneNum = original
    assert instance.PhoneNum == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)
