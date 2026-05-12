import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Student,
    Person,
    Insturctor,
    Finance,
    ILogin_Interface,
    FileBinary,
    Email,
    Exam,
    Course,
    Admin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentfname" in params, "Missing parameter 'studentfname'"
    assert "s_age" in params, "Missing parameter 's_age'"
    assert "grade" in params, "Missing parameter 'grade'"

def test_student_has_studentfname():
    assert hasattr(Student, "studentfname")
    descriptor = None
    for klass in Student.__mro__:
        if "studentfname" in klass.__dict__:
            descriptor = klass.__dict__["studentfname"]
            break
    assert isinstance(descriptor, property)

def test_student_has_s_age():
    assert hasattr(Student, "s_age")
    descriptor = None
    for klass in Student.__mro__:
        if "s_age" in klass.__dict__:
            descriptor = klass.__dict__["s_age"]
            break
    assert isinstance(descriptor, property)

def test_student_has_grade():
    assert hasattr(Student, "grade")
    descriptor = None
    for klass in Student.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "PersonFName" in params, "Missing parameter 'PersonFName'"
    assert "phNum" in params, "Missing parameter 'phNum'"
    assert "id" in params, "Missing parameter 'id'"

def test_person_has_PersonFName():
    assert hasattr(Person, "PersonFName")
    descriptor = None
    for klass in Person.__mro__:
        if "PersonFName" in klass.__dict__:
            descriptor = klass.__dict__["PersonFName"]
            break
    assert isinstance(descriptor, property)

def test_person_has_phNum():
    assert hasattr(Person, "phNum")
    descriptor = None
    for klass in Person.__mro__:
        if "phNum" in klass.__dict__:
            descriptor = klass.__dict__["phNum"]
            break
    assert isinstance(descriptor, property)

def test_person_has_id():
    assert hasattr(Person, "id")
    descriptor = None
    for klass in Person.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_insturctor_is_not_abstract():
    assert not inspect.isabstract(Insturctor)


def test_insturctor_constructor_exists():
    assert callable(Insturctor.__init__)


def test_insturctor_constructor_args():
    sig = inspect.signature(Insturctor.__init__)
    params = list(sig.parameters.keys())
    assert "INfilename" in params, "Missing parameter 'INfilename'"

def test_insturctor_has_INfilename():
    assert hasattr(Insturctor, "INfilename")
    descriptor = None
    for klass in Insturctor.__mro__:
        if "INfilename" in klass.__dict__:
            descriptor = klass.__dict__["INfilename"]
            break
    assert isinstance(descriptor, property)



def test_finance_is_not_abstract():
    assert not inspect.isabstract(Finance)


def test_finance_constructor_exists():
    assert callable(Finance.__init__)


def test_finance_constructor_args():
    sig = inspect.signature(Finance.__init__)
    params = list(sig.parameters.keys())
    assert "coast" in params, "Missing parameter 'coast'"
    assert "Cname" in params, "Missing parameter 'Cname'"

def test_finance_has_coast():
    assert hasattr(Finance, "coast")
    descriptor = None
    for klass in Finance.__mro__:
        if "coast" in klass.__dict__:
            descriptor = klass.__dict__["coast"]
            break
    assert isinstance(descriptor, property)

def test_finance_has_Cname():
    assert hasattr(Finance, "Cname")
    descriptor = None
    for klass in Finance.__mro__:
        if "Cname" in klass.__dict__:
            descriptor = klass.__dict__["Cname"]
            break
    assert isinstance(descriptor, property)



def test_ilogin_interface_is_not_abstract():
    assert not inspect.isabstract(ILogin_Interface)


def test_ilogin_interface_constructor_exists():
    assert callable(ILogin_Interface.__init__)


def test_ilogin_interface_constructor_args():
    sig = inspect.signature(ILogin_Interface.__init__)
    params = list(sig.parameters.keys())



def test_filebinary_is_not_abstract():
    assert not inspect.isabstract(FileBinary)


def test_filebinary_constructor_exists():
    assert callable(FileBinary.__init__)


def test_filebinary_constructor_args():
    sig = inspect.signature(FileBinary.__init__)
    params = list(sig.parameters.keys())



def test_email_is_not_abstract():
    assert not inspect.isabstract(Email)


def test_email_constructor_exists():
    assert callable(Email.__init__)


def test_email_constructor_args():
    sig = inspect.signature(Email.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"

def test_email_has_Email():
    assert hasattr(Email, "Email")
    descriptor = None
    for klass in Email.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_exam_is_not_abstract():
    assert not inspect.isabstract(Exam)


def test_exam_constructor_exists():
    assert callable(Exam.__init__)


def test_exam_constructor_args():
    sig = inspect.signature(Exam.__init__)
    params = list(sig.parameters.keys())
    assert "EName" in params, "Missing parameter 'EName'"
    assert "EID" in params, "Missing parameter 'EID'"
    assert "MaxGrade" in params, "Missing parameter 'MaxGrade'"
    assert "Exam_File_Name" in params, "Missing parameter 'Exam_File_Name'"
    assert "ETIME" in params, "Missing parameter 'ETIME'"

def test_exam_has_EName():
    assert hasattr(Exam, "EName")
    descriptor = None
    for klass in Exam.__mro__:
        if "EName" in klass.__dict__:
            descriptor = klass.__dict__["EName"]
            break
    assert isinstance(descriptor, property)

def test_exam_has_EID():
    assert hasattr(Exam, "EID")
    descriptor = None
    for klass in Exam.__mro__:
        if "EID" in klass.__dict__:
            descriptor = klass.__dict__["EID"]
            break
    assert isinstance(descriptor, property)

def test_exam_has_MaxGrade():
    assert hasattr(Exam, "MaxGrade")
    descriptor = None
    for klass in Exam.__mro__:
        if "MaxGrade" in klass.__dict__:
            descriptor = klass.__dict__["MaxGrade"]
            break
    assert isinstance(descriptor, property)

def test_exam_has_Exam_File_Name():
    assert hasattr(Exam, "Exam_File_Name")
    descriptor = None
    for klass in Exam.__mro__:
        if "Exam_File_Name" in klass.__dict__:
            descriptor = klass.__dict__["Exam_File_Name"]
            break
    assert isinstance(descriptor, property)

def test_exam_has_ETIME():
    assert hasattr(Exam, "ETIME")
    descriptor = None
    for klass in Exam.__mro__:
        if "ETIME" in klass.__dict__:
            descriptor = klass.__dict__["ETIME"]
            break
    assert isinstance(descriptor, property)



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "CTutor" in params, "Missing parameter 'CTutor'"
    assert "Course_File_Name" in params, "Missing parameter 'Course_File_Name'"
    assert "Course_REG" in params, "Missing parameter 'Course_REG'"
    assert "Cprice" in params, "Missing parameter 'Cprice'"
    assert "Cname" in params, "Missing parameter 'Cname'"
    assert "Cid" in params, "Missing parameter 'Cid'"

def test_course_has_CTutor():
    assert hasattr(Course, "CTutor")
    descriptor = None
    for klass in Course.__mro__:
        if "CTutor" in klass.__dict__:
            descriptor = klass.__dict__["CTutor"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Course_File_Name():
    assert hasattr(Course, "Course_File_Name")
    descriptor = None
    for klass in Course.__mro__:
        if "Course_File_Name" in klass.__dict__:
            descriptor = klass.__dict__["Course_File_Name"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Course_REG():
    assert hasattr(Course, "Course_REG")
    descriptor = None
    for klass in Course.__mro__:
        if "Course_REG" in klass.__dict__:
            descriptor = klass.__dict__["Course_REG"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Cprice():
    assert hasattr(Course, "Cprice")
    descriptor = None
    for klass in Course.__mro__:
        if "Cprice" in klass.__dict__:
            descriptor = klass.__dict__["Cprice"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Cname():
    assert hasattr(Course, "Cname")
    descriptor = None
    for klass in Course.__mro__:
        if "Cname" in klass.__dict__:
            descriptor = klass.__dict__["Cname"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Cid():
    assert hasattr(Course, "Cid")
    descriptor = None
    for klass in Course.__mro__:
        if "Cid" in klass.__dict__:
            descriptor = klass.__dict__["Cid"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "AdminFileName" in params, "Missing parameter 'AdminFileName'"

def test_admin_has_AdminFileName():
    assert hasattr(Admin, "AdminFileName")
    descriptor = None
    for klass in Admin.__mro__:
        if "AdminFileName" in klass.__dict__:
            descriptor = klass.__dict__["AdminFileName"]
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
Student_strategy = st.builds(
    Student,
    studentfname=
        safe_text,
    s_age=
        st.integers(),
    grade=
        safe_text
)
Person_strategy = st.builds(
    Person,
    PersonFName=
        safe_text,
    phNum=
        safe_text,
    id=
        safe_text
)
Insturctor_strategy = st.builds(
    Insturctor,
    INfilename=
        safe_text
)
Finance_strategy = st.builds(
    Finance,
    coast=
        safe_text,
    Cname=
        safe_text
)
ILogin_Interface_strategy = st.builds(
    ILogin_Interface,
)
FileBinary_strategy = st.builds(
    FileBinary,
)
Email_strategy = st.builds(
    Email,
    Email=
        safe_text
)
Exam_strategy = st.builds(
    Exam,
    EName=
        safe_text,
    EID=
        safe_text,
    MaxGrade=
        safe_text,
    Exam_File_Name=
        safe_text,
    ETIME=
        safe_text
)
Course_strategy = st.builds(
    Course,
    CTutor=
        safe_text,
    Course_File_Name=
        safe_text,
    Course_REG=
        safe_text,
    Cprice=
        safe_text,
    Cname=
        safe_text,
    Cid=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    AdminFileName=
        safe_text
)

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_studentfname_setter(instance):
    original = instance.studentfname
    instance.studentfname = original
    assert instance.studentfname == original



@given(instance=Student_strategy)
def test_student_s_age_setter(instance):
    original = instance.s_age
    instance.s_age = original
    assert instance.s_age == original



@given(instance=Student_strategy)
def test_student_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_PersonFName_setter(instance):
    original = instance.PersonFName
    instance.PersonFName = original
    assert instance.PersonFName == original



@given(instance=Person_strategy)
def test_person_phNum_setter(instance):
    original = instance.phNum
    instance.phNum = original
    assert instance.phNum == original



@given(instance=Person_strategy)
def test_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Insturctor_strategy)
@settings(max_examples=50)
def test_insturctor_instantiation(instance):
    assert isinstance(instance, Insturctor)



@given(instance=Insturctor_strategy)
def test_insturctor_INfilename_setter(instance):
    original = instance.INfilename
    instance.INfilename = original
    assert instance.INfilename == original

@given(instance=Finance_strategy)
@settings(max_examples=50)
def test_finance_instantiation(instance):
    assert isinstance(instance, Finance)



@given(instance=Finance_strategy)
def test_finance_coast_setter(instance):
    original = instance.coast
    instance.coast = original
    assert instance.coast == original



@given(instance=Finance_strategy)
def test_finance_Cname_setter(instance):
    original = instance.Cname
    instance.Cname = original
    assert instance.Cname == original

@given(instance=ILogin_Interface_strategy)
@settings(max_examples=50)
def test_ilogin_interface_instantiation(instance):
    assert isinstance(instance, ILogin_Interface)

@given(instance=FileBinary_strategy)
@settings(max_examples=50)
def test_filebinary_instantiation(instance):
    assert isinstance(instance, FileBinary)

@given(instance=Email_strategy)
@settings(max_examples=50)
def test_email_instantiation(instance):
    assert isinstance(instance, Email)



@given(instance=Email_strategy)
def test_email_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Exam_strategy)
@settings(max_examples=50)
def test_exam_instantiation(instance):
    assert isinstance(instance, Exam)



@given(instance=Exam_strategy)
def test_exam_EName_setter(instance):
    original = instance.EName
    instance.EName = original
    assert instance.EName == original



@given(instance=Exam_strategy)
def test_exam_EID_setter(instance):
    original = instance.EID
    instance.EID = original
    assert instance.EID == original



@given(instance=Exam_strategy)
def test_exam_MaxGrade_setter(instance):
    original = instance.MaxGrade
    instance.MaxGrade = original
    assert instance.MaxGrade == original



@given(instance=Exam_strategy)
def test_exam_Exam_File_Name_setter(instance):
    original = instance.Exam_File_Name
    instance.Exam_File_Name = original
    assert instance.Exam_File_Name == original



@given(instance=Exam_strategy)
def test_exam_ETIME_setter(instance):
    original = instance.ETIME
    instance.ETIME = original
    assert instance.ETIME == original

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course_CTutor_setter(instance):
    original = instance.CTutor
    instance.CTutor = original
    assert instance.CTutor == original



@given(instance=Course_strategy)
def test_course_Course_File_Name_setter(instance):
    original = instance.Course_File_Name
    instance.Course_File_Name = original
    assert instance.Course_File_Name == original



@given(instance=Course_strategy)
def test_course_Course_REG_setter(instance):
    original = instance.Course_REG
    instance.Course_REG = original
    assert instance.Course_REG == original



@given(instance=Course_strategy)
def test_course_Cprice_setter(instance):
    original = instance.Cprice
    instance.Cprice = original
    assert instance.Cprice == original



@given(instance=Course_strategy)
def test_course_Cname_setter(instance):
    original = instance.Cname
    instance.Cname = original
    assert instance.Cname == original



@given(instance=Course_strategy)
def test_course_Cid_setter(instance):
    original = instance.Cid
    instance.Cid = original
    assert instance.Cid == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_AdminFileName_setter(instance):
    original = instance.AdminFileName
    instance.AdminFileName = original
    assert instance.AdminFileName == original
