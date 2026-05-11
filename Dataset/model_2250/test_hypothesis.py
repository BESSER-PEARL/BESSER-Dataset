import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    e2::University,
    e2::Lecture,
    e2::Group,
    e2::Course,
    e2::Assingnment,
    e2::AssignmentSubmission,
    e2::Person,
    e2::LectureContent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_e2::university_is_not_abstract():
    assert not inspect.isabstract(e2::University)


def test_e2::university_constructor_exists():
    assert callable(e2::University.__init__)


def test_e2::university_constructor_args():
    sig = inspect.signature(e2::University.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_e2::university_has_Name():
    assert hasattr(e2::University, "Name")
    descriptor = None
    for klass in e2::University.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_e2::lecture_is_not_abstract():
    assert not inspect.isabstract(e2::Lecture)


def test_e2::lecture_constructor_exists():
    assert callable(e2::Lecture.__init__)


def test_e2::lecture_constructor_args():
    sig = inspect.signature(e2::Lecture.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Length" in params, "Missing parameter 'Length'"

def test_e2::lecture_has_Date():
    assert hasattr(e2::Lecture, "Date")
    descriptor = None
    for klass in e2::Lecture.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_e2::lecture_has_Length():
    assert hasattr(e2::Lecture, "Length")
    descriptor = None
    for klass in e2::Lecture.__mro__:
        if "Length" in klass.__dict__:
            descriptor = klass.__dict__["Length"]
            break
    assert isinstance(descriptor, property)



def test_e2::group_is_not_abstract():
    assert not inspect.isabstract(e2::Group)


def test_e2::group_constructor_exists():
    assert callable(e2::Group.__init__)


def test_e2::group_constructor_args():
    sig = inspect.signature(e2::Group.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_e2::group_has_Name():
    assert hasattr(e2::Group, "Name")
    descriptor = None
    for klass in e2::Group.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_e2::course_is_not_abstract():
    assert not inspect.isabstract(e2::Course)


def test_e2::course_constructor_exists():
    assert callable(e2::Course.__init__)


def test_e2::course_constructor_args():
    sig = inspect.signature(e2::Course.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Credit" in params, "Missing parameter 'Credit'"

def test_e2::course_has_Name():
    assert hasattr(e2::Course, "Name")
    descriptor = None
    for klass in e2::Course.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_e2::course_has_ID():
    assert hasattr(e2::Course, "ID")
    descriptor = None
    for klass in e2::Course.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_e2::course_has_Credit():
    assert hasattr(e2::Course, "Credit")
    descriptor = None
    for klass in e2::Course.__mro__:
        if "Credit" in klass.__dict__:
            descriptor = klass.__dict__["Credit"]
            break
    assert isinstance(descriptor, property)



def test_e2::assingnment_is_not_abstract():
    assert not inspect.isabstract(e2::Assingnment)


def test_e2::assingnment_constructor_exists():
    assert callable(e2::Assingnment.__init__)


def test_e2::assingnment_constructor_args():
    sig = inspect.signature(e2::Assingnment.__init__)
    params = list(sig.parameters.keys())
    assert "Title" in params, "Missing parameter 'Title'"
    assert "Content" in params, "Missing parameter 'Content'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"
    assert "Deadline" in params, "Missing parameter 'Deadline'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_e2::assingnment_has_Title():
    assert hasattr(e2::Assingnment, "Title")
    descriptor = None
    for klass in e2::Assingnment.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_e2::assingnment_has_Content():
    assert hasattr(e2::Assingnment, "Content")
    descriptor = None
    for klass in e2::Assingnment.__mro__:
        if "Content" in klass.__dict__:
            descriptor = klass.__dict__["Content"]
            break
    assert isinstance(descriptor, property)

def test_e2::assingnment_has_isMandatory():
    assert hasattr(e2::Assingnment, "isMandatory")
    descriptor = None
    for klass in e2::Assingnment.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_e2::assingnment_has_StartDate():
    assert hasattr(e2::Assingnment, "StartDate")
    descriptor = None
    for klass in e2::Assingnment.__mro__:
        if "StartDate" in klass.__dict__:
            descriptor = klass.__dict__["StartDate"]
            break
    assert isinstance(descriptor, property)

def test_e2::assingnment_has_Deadline():
    assert hasattr(e2::Assingnment, "Deadline")
    descriptor = None
    for klass in e2::Assingnment.__mro__:
        if "Deadline" in klass.__dict__:
            descriptor = klass.__dict__["Deadline"]
            break
    assert isinstance(descriptor, property)

def test_e2::assingnment_has_Type():
    assert hasattr(e2::Assingnment, "Type")
    descriptor = None
    for klass in e2::Assingnment.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_e2::assignmentsubmission_is_not_abstract():
    assert not inspect.isabstract(e2::AssignmentSubmission)


def test_e2::assignmentsubmission_constructor_exists():
    assert callable(e2::AssignmentSubmission.__init__)


def test_e2::assignmentsubmission_constructor_args():
    sig = inspect.signature(e2::AssignmentSubmission.__init__)
    params = list(sig.parameters.keys())
    assert "Assessment" in params, "Missing parameter 'Assessment'"
    assert "Comments" in params, "Missing parameter 'Comments'"

def test_e2::assignmentsubmission_has_Assessment():
    assert hasattr(e2::AssignmentSubmission, "Assessment")
    descriptor = None
    for klass in e2::AssignmentSubmission.__mro__:
        if "Assessment" in klass.__dict__:
            descriptor = klass.__dict__["Assessment"]
            break
    assert isinstance(descriptor, property)

def test_e2::assignmentsubmission_has_Comments():
    assert hasattr(e2::AssignmentSubmission, "Comments")
    descriptor = None
    for klass in e2::AssignmentSubmission.__mro__:
        if "Comments" in klass.__dict__:
            descriptor = klass.__dict__["Comments"]
            break
    assert isinstance(descriptor, property)



def test_e2::person_is_not_abstract():
    assert not inspect.isabstract(e2::Person)


def test_e2::person_constructor_exists():
    assert callable(e2::Person.__init__)


def test_e2::person_constructor_args():
    sig = inspect.signature(e2::Person.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_e2::person_has_Name():
    assert hasattr(e2::Person, "Name")
    descriptor = None
    for klass in e2::Person.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_e2::lecturecontent_is_not_abstract():
    assert not inspect.isabstract(e2::LectureContent)


def test_e2::lecturecontent_constructor_exists():
    assert callable(e2::LectureContent.__init__)


def test_e2::lecturecontent_constructor_args():
    sig = inspect.signature(e2::LectureContent.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Material" in params, "Missing parameter 'Material'"

def test_e2::lecturecontent_has_Type():
    assert hasattr(e2::LectureContent, "Type")
    descriptor = None
    for klass in e2::LectureContent.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_e2::lecturecontent_has_Material():
    assert hasattr(e2::LectureContent, "Material")
    descriptor = None
    for klass in e2::LectureContent.__mro__:
        if "Material" in klass.__dict__:
            descriptor = klass.__dict__["Material"]
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
e2::University_strategy = st.builds(
    e2::University,
    Name=
        safe_text
)
e2::Lecture_strategy = st.builds(
    e2::Lecture,
    Date=
        st.dates(),
    Length=
        st.integers()
)
e2::Group_strategy = st.builds(
    e2::Group,
    Name=
        safe_text
)
e2::Course_strategy = st.builds(
    e2::Course,
    Name=
        safe_text,
    ID=
        safe_text,
    Credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
e2::Assingnment_strategy = st.builds(
    e2::Assingnment,
    Title=
        safe_text,
    Content=
        safe_text,
    isMandatory=
        st.booleans(),
    StartDate=
        st.dates(),
    Deadline=
        st.dates(),
    Type=
        safe_text
)
e2::AssignmentSubmission_strategy = st.builds(
    e2::AssignmentSubmission,
    Assessment=
        st.integers(),
    Comments=
        safe_text
)
e2::Person_strategy = st.builds(
    e2::Person,
    Name=
        safe_text
)
e2::LectureContent_strategy = st.builds(
    e2::LectureContent,
    Type=
        safe_text,
    Material=
        safe_text
)

@given(instance=e2::University_strategy)
@settings(max_examples=50)
def test_e2::university_instantiation(instance):
    assert isinstance(instance, e2::University)

@given(instance=e2::University_strategy)
def test_e2::university_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=e2::University_strategy)
def test_e2::university_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=e2::Lecture_strategy)
@settings(max_examples=50)
def test_e2::lecture_instantiation(instance):
    assert isinstance(instance, e2::Lecture)

@given(instance=e2::Lecture_strategy)
def test_e2::lecture_Date_type(instance):
    assert isinstance(instance.Date, date)


@given(instance=e2::Lecture_strategy)
def test_e2::lecture_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=e2::Lecture_strategy)
def test_e2::lecture_Length_type(instance):
    assert isinstance(instance.Length, int)


@given(instance=e2::Lecture_strategy)
def test_e2::lecture_Length_setter(instance):
    original = instance.Length
    instance.Length = original
    assert instance.Length == original

@given(instance=e2::Group_strategy)
@settings(max_examples=50)
def test_e2::group_instantiation(instance):
    assert isinstance(instance, e2::Group)

@given(instance=e2::Group_strategy)
def test_e2::group_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=e2::Group_strategy)
def test_e2::group_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=e2::Course_strategy)
@settings(max_examples=50)
def test_e2::course_instantiation(instance):
    assert isinstance(instance, e2::Course)

@given(instance=e2::Course_strategy)
def test_e2::course_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=e2::Course_strategy)
def test_e2::course_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=e2::Course_strategy)
def test_e2::course_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=e2::Course_strategy)
def test_e2::course_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=e2::Course_strategy)
def test_e2::course_Credit_type(instance):
    assert isinstance(instance.Credit, float)


@given(instance=e2::Course_strategy)
def test_e2::course_Credit_setter(instance):
    original = instance.Credit
    instance.Credit = original
    assert instance.Credit == original

@given(instance=e2::Assingnment_strategy)
@settings(max_examples=50)
def test_e2::assingnment_instantiation(instance):
    assert isinstance(instance, e2::Assingnment)

@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_Title_type(instance):
    assert isinstance(instance.Title, str)


@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original

@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_Content_type(instance):
    assert isinstance(instance.Content, str)


@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_Content_setter(instance):
    original = instance.Content
    instance.Content = original
    assert instance.Content == original

@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_isMandatory_type(instance):
    assert isinstance(instance.isMandatory, bool)


@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original

@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_StartDate_type(instance):
    assert isinstance(instance.StartDate, date)


@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original

@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_Deadline_type(instance):
    assert isinstance(instance.Deadline, date)


@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_Deadline_setter(instance):
    original = instance.Deadline
    instance.Deadline = original
    assert instance.Deadline == original

@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=e2::Assingnment_strategy)
def test_e2::assingnment_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=e2::AssignmentSubmission_strategy)
@settings(max_examples=50)
def test_e2::assignmentsubmission_instantiation(instance):
    assert isinstance(instance, e2::AssignmentSubmission)

@given(instance=e2::AssignmentSubmission_strategy)
def test_e2::assignmentsubmission_Assessment_type(instance):
    assert isinstance(instance.Assessment, int)


@given(instance=e2::AssignmentSubmission_strategy)
def test_e2::assignmentsubmission_Assessment_setter(instance):
    original = instance.Assessment
    instance.Assessment = original
    assert instance.Assessment == original

@given(instance=e2::AssignmentSubmission_strategy)
def test_e2::assignmentsubmission_Comments_type(instance):
    assert isinstance(instance.Comments, str)


@given(instance=e2::AssignmentSubmission_strategy)
def test_e2::assignmentsubmission_Comments_setter(instance):
    original = instance.Comments
    instance.Comments = original
    assert instance.Comments == original

@given(instance=e2::Person_strategy)
@settings(max_examples=50)
def test_e2::person_instantiation(instance):
    assert isinstance(instance, e2::Person)

@given(instance=e2::Person_strategy)
def test_e2::person_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=e2::Person_strategy)
def test_e2::person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=e2::LectureContent_strategy)
@settings(max_examples=50)
def test_e2::lecturecontent_instantiation(instance):
    assert isinstance(instance, e2::LectureContent)

@given(instance=e2::LectureContent_strategy)
def test_e2::lecturecontent_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=e2::LectureContent_strategy)
def test_e2::lecturecontent_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=e2::LectureContent_strategy)
def test_e2::lecturecontent_Material_type(instance):
    assert isinstance(instance.Material, str)


@given(instance=e2::LectureContent_strategy)
def test_e2::lecturecontent_Material_setter(instance):
    original = instance.Material
    instance.Material = original
    assert instance.Material == original
