import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    e2_EClass0,
    e2_University,
    e2_Goal,
    e2_Group,
    e2_Assingnment,
    e2_AssignmentSubmission,
    e2_Person,
    e2_SubGoal,
    e2_LectureContent,
    e2_Lecture,
    e2_Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_e2_eclass0_is_not_abstract():
    assert not inspect.isabstract(e2_EClass0)


def test_e2_eclass0_constructor_exists():
    assert callable(e2_EClass0.__init__)


def test_e2_eclass0_constructor_args():
    sig = inspect.signature(e2_EClass0.__init__)
    params = list(sig.parameters.keys())



def test_e2_university_is_not_abstract():
    assert not inspect.isabstract(e2_University)


def test_e2_university_constructor_exists():
    assert callable(e2_University.__init__)


def test_e2_university_constructor_args():
    sig = inspect.signature(e2_University.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_e2_university_has_Name():
    assert hasattr(e2_University, "Name")
    descriptor = None
    for klass in e2_University.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_e2_goal_is_not_abstract():
    assert not inspect.isabstract(e2_Goal)


def test_e2_goal_constructor_exists():
    assert callable(e2_Goal.__init__)


def test_e2_goal_constructor_args():
    sig = inspect.signature(e2_Goal.__init__)
    params = list(sig.parameters.keys())
    assert "GoalText" in params, "Missing parameter 'GoalText'"
    assert "GoalID" in params, "Missing parameter 'GoalID'"

def test_e2_goal_has_GoalText():
    assert hasattr(e2_Goal, "GoalText")
    descriptor = None
    for klass in e2_Goal.__mro__:
        if "GoalText" in klass.__dict__:
            descriptor = klass.__dict__["GoalText"]
            break
    assert isinstance(descriptor, property)

def test_e2_goal_has_GoalID():
    assert hasattr(e2_Goal, "GoalID")
    descriptor = None
    for klass in e2_Goal.__mro__:
        if "GoalID" in klass.__dict__:
            descriptor = klass.__dict__["GoalID"]
            break
    assert isinstance(descriptor, property)



def test_e2_group_is_not_abstract():
    assert not inspect.isabstract(e2_Group)


def test_e2_group_constructor_exists():
    assert callable(e2_Group.__init__)


def test_e2_group_constructor_args():
    sig = inspect.signature(e2_Group.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_e2_group_has_Name():
    assert hasattr(e2_Group, "Name")
    descriptor = None
    for klass in e2_Group.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_e2_assingnment_is_not_abstract():
    assert not inspect.isabstract(e2_Assingnment)


def test_e2_assingnment_constructor_exists():
    assert callable(e2_Assingnment.__init__)


def test_e2_assingnment_constructor_args():
    sig = inspect.signature(e2_Assingnment.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Content" in params, "Missing parameter 'Content'"
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"
    assert "Title" in params, "Missing parameter 'Title'"
    assert "Deadline" in params, "Missing parameter 'Deadline'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"

def test_e2_assingnment_has_Type():
    assert hasattr(e2_Assingnment, "Type")
    descriptor = None
    for klass in e2_Assingnment.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_e2_assingnment_has_Content():
    assert hasattr(e2_Assingnment, "Content")
    descriptor = None
    for klass in e2_Assingnment.__mro__:
        if "Content" in klass.__dict__:
            descriptor = klass.__dict__["Content"]
            break
    assert isinstance(descriptor, property)

def test_e2_assingnment_has_isMandatory():
    assert hasattr(e2_Assingnment, "isMandatory")
    descriptor = None
    for klass in e2_Assingnment.__mro__:
        if "isMandatory" in klass.__dict__:
            descriptor = klass.__dict__["isMandatory"]
            break
    assert isinstance(descriptor, property)

def test_e2_assingnment_has_Title():
    assert hasattr(e2_Assingnment, "Title")
    descriptor = None
    for klass in e2_Assingnment.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_e2_assingnment_has_Deadline():
    assert hasattr(e2_Assingnment, "Deadline")
    descriptor = None
    for klass in e2_Assingnment.__mro__:
        if "Deadline" in klass.__dict__:
            descriptor = klass.__dict__["Deadline"]
            break
    assert isinstance(descriptor, property)

def test_e2_assingnment_has_StartDate():
    assert hasattr(e2_Assingnment, "StartDate")
    descriptor = None
    for klass in e2_Assingnment.__mro__:
        if "StartDate" in klass.__dict__:
            descriptor = klass.__dict__["StartDate"]
            break
    assert isinstance(descriptor, property)



def test_e2_assignmentsubmission_is_not_abstract():
    assert not inspect.isabstract(e2_AssignmentSubmission)


def test_e2_assignmentsubmission_constructor_exists():
    assert callable(e2_AssignmentSubmission.__init__)


def test_e2_assignmentsubmission_constructor_args():
    sig = inspect.signature(e2_AssignmentSubmission.__init__)
    params = list(sig.parameters.keys())
    assert "Comments" in params, "Missing parameter 'Comments'"
    assert "assessment" in params, "Missing parameter 'assessment'"

def test_e2_assignmentsubmission_has_Comments():
    assert hasattr(e2_AssignmentSubmission, "Comments")
    descriptor = None
    for klass in e2_AssignmentSubmission.__mro__:
        if "Comments" in klass.__dict__:
            descriptor = klass.__dict__["Comments"]
            break
    assert isinstance(descriptor, property)

def test_e2_assignmentsubmission_has_assessment():
    assert hasattr(e2_AssignmentSubmission, "assessment")
    descriptor = None
    for klass in e2_AssignmentSubmission.__mro__:
        if "assessment" in klass.__dict__:
            descriptor = klass.__dict__["assessment"]
            break
    assert isinstance(descriptor, property)



def test_e2_person_is_not_abstract():
    assert not inspect.isabstract(e2_Person)


def test_e2_person_constructor_exists():
    assert callable(e2_Person.__init__)


def test_e2_person_constructor_args():
    sig = inspect.signature(e2_Person.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_e2_person_has_Name():
    assert hasattr(e2_Person, "Name")
    descriptor = None
    for klass in e2_Person.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_e2_subgoal_is_not_abstract():
    assert not inspect.isabstract(e2_SubGoal)


def test_e2_subgoal_constructor_exists():
    assert callable(e2_SubGoal.__init__)


def test_e2_subgoal_constructor_args():
    sig = inspect.signature(e2_SubGoal.__init__)
    params = list(sig.parameters.keys())
    assert "GoalText" in params, "Missing parameter 'GoalText'"
    assert "GoalID" in params, "Missing parameter 'GoalID'"

def test_e2_subgoal_has_GoalText():
    assert hasattr(e2_SubGoal, "GoalText")
    descriptor = None
    for klass in e2_SubGoal.__mro__:
        if "GoalText" in klass.__dict__:
            descriptor = klass.__dict__["GoalText"]
            break
    assert isinstance(descriptor, property)

def test_e2_subgoal_has_GoalID():
    assert hasattr(e2_SubGoal, "GoalID")
    descriptor = None
    for klass in e2_SubGoal.__mro__:
        if "GoalID" in klass.__dict__:
            descriptor = klass.__dict__["GoalID"]
            break
    assert isinstance(descriptor, property)



def test_e2_lecturecontent_is_not_abstract():
    assert not inspect.isabstract(e2_LectureContent)


def test_e2_lecturecontent_constructor_exists():
    assert callable(e2_LectureContent.__init__)


def test_e2_lecturecontent_constructor_args():
    sig = inspect.signature(e2_LectureContent.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Material" in params, "Missing parameter 'Material'"

def test_e2_lecturecontent_has_Type():
    assert hasattr(e2_LectureContent, "Type")
    descriptor = None
    for klass in e2_LectureContent.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_e2_lecturecontent_has_Material():
    assert hasattr(e2_LectureContent, "Material")
    descriptor = None
    for klass in e2_LectureContent.__mro__:
        if "Material" in klass.__dict__:
            descriptor = klass.__dict__["Material"]
            break
    assert isinstance(descriptor, property)



def test_e2_lecture_is_not_abstract():
    assert not inspect.isabstract(e2_Lecture)


def test_e2_lecture_constructor_exists():
    assert callable(e2_Lecture.__init__)


def test_e2_lecture_constructor_args():
    sig = inspect.signature(e2_Lecture.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "length" in params, "Missing parameter 'length'"

def test_e2_lecture_has_Date():
    assert hasattr(e2_Lecture, "Date")
    descriptor = None
    for klass in e2_Lecture.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_e2_lecture_has_length():
    assert hasattr(e2_Lecture, "length")
    descriptor = None
    for klass in e2_Lecture.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_e2_course_is_not_abstract():
    assert not inspect.isabstract(e2_Course)


def test_e2_course_constructor_exists():
    assert callable(e2_Course.__init__)


def test_e2_course_constructor_args():
    sig = inspect.signature(e2_Course.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "credit" in params, "Missing parameter 'credit'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_e2_course_has_ID():
    assert hasattr(e2_Course, "ID")
    descriptor = None
    for klass in e2_Course.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_e2_course_has_credit():
    assert hasattr(e2_Course, "credit")
    descriptor = None
    for klass in e2_Course.__mro__:
        if "credit" in klass.__dict__:
            descriptor = klass.__dict__["credit"]
            break
    assert isinstance(descriptor, property)

def test_e2_course_has_Name():
    assert hasattr(e2_Course, "Name")
    descriptor = None
    for klass in e2_Course.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
e2_EClass0_strategy = st.builds(
    e2_EClass0,
)
e2_University_strategy = st.builds(
    e2_University,
    Name=
        safe_text
)
e2_Goal_strategy = st.builds(
    e2_Goal,
    GoalText=
        safe_text,
    GoalID=
        safe_text
)
e2_Group_strategy = st.builds(
    e2_Group,
    Name=
        safe_text
)
e2_Assingnment_strategy = st.builds(
    e2_Assingnment,
    Type=
        safe_text,
    Content=
        safe_text,
    isMandatory=
        st.booleans(),
    Title=
        safe_text,
    Deadline=
        st.dates(),
    StartDate=
        st.dates()
)
e2_AssignmentSubmission_strategy = st.builds(
    e2_AssignmentSubmission,
    Comments=
        safe_text,
    assessment=
        st.integers()
)
e2_Person_strategy = st.builds(
    e2_Person,
    Name=
        safe_text
)
e2_SubGoal_strategy = st.builds(
    e2_SubGoal,
    GoalText=
        safe_text,
    GoalID=
        safe_text
)
e2_LectureContent_strategy = st.builds(
    e2_LectureContent,
    Type=
        safe_text,
    Material=
        safe_text
)
e2_Lecture_strategy = st.builds(
    e2_Lecture,
    Date=
        st.dates(),
    length=
        st.integers()
)
e2_Course_strategy = st.builds(
    e2_Course,
    ID=
        safe_text,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Name=
        safe_text
)

@given(instance=e2_EClass0_strategy)
@settings(max_examples=50)
def test_e2_eclass0_instantiation(instance):
    assert isinstance(instance, e2_EClass0)

@given(instance=e2_University_strategy)
@settings(max_examples=50)
def test_e2_university_instantiation(instance):
    assert isinstance(instance, e2_University)



@given(instance=e2_University_strategy)
def test_e2_university_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=e2_Goal_strategy)
@settings(max_examples=50)
def test_e2_goal_instantiation(instance):
    assert isinstance(instance, e2_Goal)



@given(instance=e2_Goal_strategy)
def test_e2_goal_GoalText_setter(instance):
    original = instance.GoalText
    instance.GoalText = original
    assert instance.GoalText == original



@given(instance=e2_Goal_strategy)
def test_e2_goal_GoalID_setter(instance):
    original = instance.GoalID
    instance.GoalID = original
    assert instance.GoalID == original

@given(instance=e2_Group_strategy)
@settings(max_examples=50)
def test_e2_group_instantiation(instance):
    assert isinstance(instance, e2_Group)



@given(instance=e2_Group_strategy)
def test_e2_group_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=e2_Assingnment_strategy)
@settings(max_examples=50)
def test_e2_assingnment_instantiation(instance):
    assert isinstance(instance, e2_Assingnment)



@given(instance=e2_Assingnment_strategy)
def test_e2_assingnment_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=e2_Assingnment_strategy)
def test_e2_assingnment_Content_setter(instance):
    original = instance.Content
    instance.Content = original
    assert instance.Content == original



@given(instance=e2_Assingnment_strategy)
def test_e2_assingnment_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original



@given(instance=e2_Assingnment_strategy)
def test_e2_assingnment_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=e2_Assingnment_strategy)
def test_e2_assingnment_Deadline_setter(instance):
    original = instance.Deadline
    instance.Deadline = original
    assert instance.Deadline == original



@given(instance=e2_Assingnment_strategy)
def test_e2_assingnment_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original

@given(instance=e2_AssignmentSubmission_strategy)
@settings(max_examples=50)
def test_e2_assignmentsubmission_instantiation(instance):
    assert isinstance(instance, e2_AssignmentSubmission)



@given(instance=e2_AssignmentSubmission_strategy)
def test_e2_assignmentsubmission_Comments_setter(instance):
    original = instance.Comments
    instance.Comments = original
    assert instance.Comments == original



@given(instance=e2_AssignmentSubmission_strategy)
def test_e2_assignmentsubmission_assessment_setter(instance):
    original = instance.assessment
    instance.assessment = original
    assert instance.assessment == original

@given(instance=e2_Person_strategy)
@settings(max_examples=50)
def test_e2_person_instantiation(instance):
    assert isinstance(instance, e2_Person)



@given(instance=e2_Person_strategy)
def test_e2_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=e2_SubGoal_strategy)
@settings(max_examples=50)
def test_e2_subgoal_instantiation(instance):
    assert isinstance(instance, e2_SubGoal)



@given(instance=e2_SubGoal_strategy)
def test_e2_subgoal_GoalText_setter(instance):
    original = instance.GoalText
    instance.GoalText = original
    assert instance.GoalText == original



@given(instance=e2_SubGoal_strategy)
def test_e2_subgoal_GoalID_setter(instance):
    original = instance.GoalID
    instance.GoalID = original
    assert instance.GoalID == original

@given(instance=e2_LectureContent_strategy)
@settings(max_examples=50)
def test_e2_lecturecontent_instantiation(instance):
    assert isinstance(instance, e2_LectureContent)



@given(instance=e2_LectureContent_strategy)
def test_e2_lecturecontent_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=e2_LectureContent_strategy)
def test_e2_lecturecontent_Material_setter(instance):
    original = instance.Material
    instance.Material = original
    assert instance.Material == original

@given(instance=e2_Lecture_strategy)
@settings(max_examples=50)
def test_e2_lecture_instantiation(instance):
    assert isinstance(instance, e2_Lecture)



@given(instance=e2_Lecture_strategy)
def test_e2_lecture_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=e2_Lecture_strategy)
def test_e2_lecture_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=e2_Course_strategy)
@settings(max_examples=50)
def test_e2_course_instantiation(instance):
    assert isinstance(instance, e2_Course)



@given(instance=e2_Course_strategy)
def test_e2_course_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=e2_Course_strategy)
def test_e2_course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original



@given(instance=e2_Course_strategy)
def test_e2_course_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
