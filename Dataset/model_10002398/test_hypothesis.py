import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mypackage_FileManager,
    mypackage_Exam,
    mypackage_Course,
    mypackage_Admin,
    mypackage_Tutor,
    mypackage_studentAffairsEmp,
    mypackage_Student,
    mypackage_Staff,
    mypackage_Perosn,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mypackage_filemanager_is_not_abstract():
    assert not inspect.isabstract(mypackage_FileManager)


def test_mypackage_filemanager_constructor_exists():
    assert callable(mypackage_FileManager.__init__)


def test_mypackage_filemanager_constructor_args():
    sig = inspect.signature(mypackage_FileManager.__init__)
    params = list(sig.parameters.keys())



def test_mypackage_exam_is_not_abstract():
    assert not inspect.isabstract(mypackage_Exam)


def test_mypackage_exam_constructor_exists():
    assert callable(mypackage_Exam.__init__)


def test_mypackage_exam_constructor_args():
    sig = inspect.signature(mypackage_Exam.__init__)
    params = list(sig.parameters.keys())
    assert "ExamsFileName" in params, "Missing parameter 'ExamsFileName'"
    assert "EId" in params, "Missing parameter 'EId'"
    assert "EName" in params, "Missing parameter 'EName'"
    assert "MaxGrade" in params, "Missing parameter 'MaxGrade'"

def test_mypackage_exam_has_ExamsFileName():
    assert hasattr(mypackage_Exam, "ExamsFileName")
    descriptor = None
    for klass in mypackage_Exam.__mro__:
        if "ExamsFileName" in klass.__dict__:
            descriptor = klass.__dict__["ExamsFileName"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_exam_has_EId():
    assert hasattr(mypackage_Exam, "EId")
    descriptor = None
    for klass in mypackage_Exam.__mro__:
        if "EId" in klass.__dict__:
            descriptor = klass.__dict__["EId"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_exam_has_EName():
    assert hasattr(mypackage_Exam, "EName")
    descriptor = None
    for klass in mypackage_Exam.__mro__:
        if "EName" in klass.__dict__:
            descriptor = klass.__dict__["EName"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_exam_has_MaxGrade():
    assert hasattr(mypackage_Exam, "MaxGrade")
    descriptor = None
    for klass in mypackage_Exam.__mro__:
        if "MaxGrade" in klass.__dict__:
            descriptor = klass.__dict__["MaxGrade"]
            break
    assert isinstance(descriptor, property)



def test_mypackage_course_is_not_abstract():
    assert not inspect.isabstract(mypackage_Course)


def test_mypackage_course_constructor_exists():
    assert callable(mypackage_Course.__init__)


def test_mypackage_course_constructor_args():
    sig = inspect.signature(mypackage_Course.__init__)
    params = list(sig.parameters.keys())
    assert "CName" in params, "Missing parameter 'CName'"
    assert "CreditHours" in params, "Missing parameter 'CreditHours'"
    assert "CId" in params, "Missing parameter 'CId'"
    assert "CourseFileName" in params, "Missing parameter 'CourseFileName'"

def test_mypackage_course_has_CName():
    assert hasattr(mypackage_Course, "CName")
    descriptor = None
    for klass in mypackage_Course.__mro__:
        if "CName" in klass.__dict__:
            descriptor = klass.__dict__["CName"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_course_has_CreditHours():
    assert hasattr(mypackage_Course, "CreditHours")
    descriptor = None
    for klass in mypackage_Course.__mro__:
        if "CreditHours" in klass.__dict__:
            descriptor = klass.__dict__["CreditHours"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_course_has_CId():
    assert hasattr(mypackage_Course, "CId")
    descriptor = None
    for klass in mypackage_Course.__mro__:
        if "CId" in klass.__dict__:
            descriptor = klass.__dict__["CId"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_course_has_CourseFileName():
    assert hasattr(mypackage_Course, "CourseFileName")
    descriptor = None
    for klass in mypackage_Course.__mro__:
        if "CourseFileName" in klass.__dict__:
            descriptor = klass.__dict__["CourseFileName"]
            break
    assert isinstance(descriptor, property)



def test_mypackage_admin_is_not_abstract():
    assert not inspect.isabstract(mypackage_Admin)


def test_mypackage_admin_constructor_exists():
    assert callable(mypackage_Admin.__init__)


def test_mypackage_admin_constructor_args():
    sig = inspect.signature(mypackage_Admin.__init__)
    params = list(sig.parameters.keys())



def test_mypackage_tutor_is_not_abstract():
    assert not inspect.isabstract(mypackage_Tutor)


def test_mypackage_tutor_constructor_exists():
    assert callable(mypackage_Tutor.__init__)


def test_mypackage_tutor_constructor_args():
    sig = inspect.signature(mypackage_Tutor.__init__)
    params = list(sig.parameters.keys())
    assert "TutorFileName" in params, "Missing parameter 'TutorFileName'"
    assert "academicalHours" in params, "Missing parameter 'academicalHours'"

def test_mypackage_tutor_has_TutorFileName():
    assert hasattr(mypackage_Tutor, "TutorFileName")
    descriptor = None
    for klass in mypackage_Tutor.__mro__:
        if "TutorFileName" in klass.__dict__:
            descriptor = klass.__dict__["TutorFileName"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_tutor_has_academicalHours():
    assert hasattr(mypackage_Tutor, "academicalHours")
    descriptor = None
    for klass in mypackage_Tutor.__mro__:
        if "academicalHours" in klass.__dict__:
            descriptor = klass.__dict__["academicalHours"]
            break
    assert isinstance(descriptor, property)



def test_mypackage_studentaffairsemp_is_not_abstract():
    assert not inspect.isabstract(mypackage_studentAffairsEmp)


def test_mypackage_studentaffairsemp_constructor_exists():
    assert callable(mypackage_studentAffairsEmp.__init__)


def test_mypackage_studentaffairsemp_constructor_args():
    sig = inspect.signature(mypackage_studentAffairsEmp.__init__)
    params = list(sig.parameters.keys())
    assert "EmpFileName" in params, "Missing parameter 'EmpFileName'"

def test_mypackage_studentaffairsemp_has_EmpFileName():
    assert hasattr(mypackage_studentAffairsEmp, "EmpFileName")
    descriptor = None
    for klass in mypackage_studentAffairsEmp.__mro__:
        if "EmpFileName" in klass.__dict__:
            descriptor = klass.__dict__["EmpFileName"]
            break
    assert isinstance(descriptor, property)



def test_mypackage_student_is_not_abstract():
    assert not inspect.isabstract(mypackage_Student)


def test_mypackage_student_constructor_exists():
    assert callable(mypackage_Student.__init__)


def test_mypackage_student_constructor_args():
    sig = inspect.signature(mypackage_Student.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"
    assert "level" in params, "Missing parameter 'level'"
    assert "studentFileName" in params, "Missing parameter 'studentFileName'"

def test_mypackage_student_has_grade():
    assert hasattr(mypackage_Student, "grade")
    descriptor = None
    for klass in mypackage_Student.__mro__:
        if "grade" in klass.__dict__:
            descriptor = klass.__dict__["grade"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_student_has_level():
    assert hasattr(mypackage_Student, "level")
    descriptor = None
    for klass in mypackage_Student.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_student_has_studentFileName():
    assert hasattr(mypackage_Student, "studentFileName")
    descriptor = None
    for klass in mypackage_Student.__mro__:
        if "studentFileName" in klass.__dict__:
            descriptor = klass.__dict__["studentFileName"]
            break
    assert isinstance(descriptor, property)



def test_mypackage_staff_is_not_abstract():
    assert not inspect.isabstract(mypackage_Staff)


def test_mypackage_staff_constructor_exists():
    assert callable(mypackage_Staff.__init__)


def test_mypackage_staff_constructor_args():
    sig = inspect.signature(mypackage_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"

def test_mypackage_staff_has_salary():
    assert hasattr(mypackage_Staff, "salary")
    descriptor = None
    for klass in mypackage_Staff.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_mypackage_perosn_is_not_abstract():
    assert not inspect.isabstract(mypackage_Perosn)


def test_mypackage_perosn_constructor_exists():
    assert callable(mypackage_Perosn.__init__)


def test_mypackage_perosn_constructor_args():
    sig = inspect.signature(mypackage_Perosn.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"
    assert "age" in params, "Missing parameter 'age'"
    assert "id" in params, "Missing parameter 'id'"
    assert "fName" in params, "Missing parameter 'fName'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_mypackage_perosn_has_lname():
    assert hasattr(mypackage_Perosn, "lname")
    descriptor = None
    for klass in mypackage_Perosn.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_perosn_has_age():
    assert hasattr(mypackage_Perosn, "age")
    descriptor = None
    for klass in mypackage_Perosn.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_perosn_has_id():
    assert hasattr(mypackage_Perosn, "id")
    descriptor = None
    for klass in mypackage_Perosn.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_perosn_has_fName():
    assert hasattr(mypackage_Perosn, "fName")
    descriptor = None
    for klass in mypackage_Perosn.__mro__:
        if "fName" in klass.__dict__:
            descriptor = klass.__dict__["fName"]
            break
    assert isinstance(descriptor, property)

def test_mypackage_perosn_has_UserName():
    assert hasattr(mypackage_Perosn, "UserName")
    descriptor = None
    for klass in mypackage_Perosn.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
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
mypackage_FileManager_strategy = st.builds(
    mypackage_FileManager,
)
mypackage_Exam_strategy = st.builds(
    mypackage_Exam,
    ExamsFileName=
        safe_text,
    EId=
        safe_text,
    EName=
        safe_text,
    MaxGrade=
        safe_text
)
mypackage_Course_strategy = st.builds(
    mypackage_Course,
    CName=
        safe_text,
    CreditHours=
        st.integers(),
    CId=
        safe_text,
    CourseFileName=
        safe_text
)
mypackage_Admin_strategy = st.builds(
    mypackage_Admin,
)
mypackage_Tutor_strategy = st.builds(
    mypackage_Tutor,
    TutorFileName=
        safe_text,
    academicalHours=
        safe_text
)
mypackage_studentAffairsEmp_strategy = st.builds(
    mypackage_studentAffairsEmp,
    EmpFileName=
        safe_text
)
mypackage_Student_strategy = st.builds(
    mypackage_Student,
    grade=
        safe_text,
    level=
        st.integers(),
    studentFileName=
        safe_text
)
mypackage_Staff_strategy = st.builds(
    mypackage_Staff,
    salary=
        safe_text
)
mypackage_Perosn_strategy = st.builds(
    mypackage_Perosn,
    lname=
        safe_text,
    age=
        st.integers(),
    id=
        st.integers(),
    fName=
        safe_text,
    UserName=
        safe_text
)

@given(instance=mypackage_FileManager_strategy)
@settings(max_examples=50)
def test_mypackage_filemanager_instantiation(instance):
    assert isinstance(instance, mypackage_FileManager)

@given(instance=mypackage_Exam_strategy)
@settings(max_examples=50)
def test_mypackage_exam_instantiation(instance):
    assert isinstance(instance, mypackage_Exam)



@given(instance=mypackage_Exam_strategy)
def test_mypackage_exam_ExamsFileName_setter(instance):
    original = instance.ExamsFileName
    instance.ExamsFileName = original
    assert instance.ExamsFileName == original



@given(instance=mypackage_Exam_strategy)
def test_mypackage_exam_EId_setter(instance):
    original = instance.EId
    instance.EId = original
    assert instance.EId == original



@given(instance=mypackage_Exam_strategy)
def test_mypackage_exam_EName_setter(instance):
    original = instance.EName
    instance.EName = original
    assert instance.EName == original



@given(instance=mypackage_Exam_strategy)
def test_mypackage_exam_MaxGrade_setter(instance):
    original = instance.MaxGrade
    instance.MaxGrade = original
    assert instance.MaxGrade == original

@given(instance=mypackage_Course_strategy)
@settings(max_examples=50)
def test_mypackage_course_instantiation(instance):
    assert isinstance(instance, mypackage_Course)



@given(instance=mypackage_Course_strategy)
def test_mypackage_course_CName_setter(instance):
    original = instance.CName
    instance.CName = original
    assert instance.CName == original



@given(instance=mypackage_Course_strategy)
def test_mypackage_course_CreditHours_setter(instance):
    original = instance.CreditHours
    instance.CreditHours = original
    assert instance.CreditHours == original



@given(instance=mypackage_Course_strategy)
def test_mypackage_course_CId_setter(instance):
    original = instance.CId
    instance.CId = original
    assert instance.CId == original



@given(instance=mypackage_Course_strategy)
def test_mypackage_course_CourseFileName_setter(instance):
    original = instance.CourseFileName
    instance.CourseFileName = original
    assert instance.CourseFileName == original

@given(instance=mypackage_Admin_strategy)
@settings(max_examples=50)
def test_mypackage_admin_instantiation(instance):
    assert isinstance(instance, mypackage_Admin)

@given(instance=mypackage_Tutor_strategy)
@settings(max_examples=50)
def test_mypackage_tutor_instantiation(instance):
    assert isinstance(instance, mypackage_Tutor)



@given(instance=mypackage_Tutor_strategy)
def test_mypackage_tutor_TutorFileName_setter(instance):
    original = instance.TutorFileName
    instance.TutorFileName = original
    assert instance.TutorFileName == original



@given(instance=mypackage_Tutor_strategy)
def test_mypackage_tutor_academicalHours_setter(instance):
    original = instance.academicalHours
    instance.academicalHours = original
    assert instance.academicalHours == original

@given(instance=mypackage_studentAffairsEmp_strategy)
@settings(max_examples=50)
def test_mypackage_studentaffairsemp_instantiation(instance):
    assert isinstance(instance, mypackage_studentAffairsEmp)



@given(instance=mypackage_studentAffairsEmp_strategy)
def test_mypackage_studentaffairsemp_EmpFileName_setter(instance):
    original = instance.EmpFileName
    instance.EmpFileName = original
    assert instance.EmpFileName == original

@given(instance=mypackage_Student_strategy)
@settings(max_examples=50)
def test_mypackage_student_instantiation(instance):
    assert isinstance(instance, mypackage_Student)



@given(instance=mypackage_Student_strategy)
def test_mypackage_student_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original



@given(instance=mypackage_Student_strategy)
def test_mypackage_student_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=mypackage_Student_strategy)
def test_mypackage_student_studentFileName_setter(instance):
    original = instance.studentFileName
    instance.studentFileName = original
    assert instance.studentFileName == original

@given(instance=mypackage_Staff_strategy)
@settings(max_examples=50)
def test_mypackage_staff_instantiation(instance):
    assert isinstance(instance, mypackage_Staff)



@given(instance=mypackage_Staff_strategy)
def test_mypackage_staff_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=mypackage_Perosn_strategy)
@settings(max_examples=50)
def test_mypackage_perosn_instantiation(instance):
    assert isinstance(instance, mypackage_Perosn)



@given(instance=mypackage_Perosn_strategy)
def test_mypackage_perosn_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=mypackage_Perosn_strategy)
def test_mypackage_perosn_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=mypackage_Perosn_strategy)
def test_mypackage_perosn_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=mypackage_Perosn_strategy)
def test_mypackage_perosn_fName_setter(instance):
    original = instance.fName
    instance.fName = original
    assert instance.fName == original



@given(instance=mypackage_Perosn_strategy)
def test_mypackage_perosn_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original
