import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    gsml_GradingSystem,
    gsml_Grade,
    Task,
    gsml_TaskGroup,
    gsml_ConcreteTask,
    gsml_Task,
    gsml_GradingScheme,
    gsml_Grading,
    gsml_Course,
    MinRequirementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gsml_gradingsystem_is_not_abstract():
    assert not inspect.isabstract(gsml_GradingSystem)


def test_gsml_gradingsystem_constructor_exists():
    assert callable(gsml_GradingSystem.__init__)


def test_gsml_gradingsystem_constructor_args():
    sig = inspect.signature(gsml_GradingSystem.__init__)
    params = list(sig.parameters.keys())



def test_gsml_grade_is_not_abstract():
    assert not inspect.isabstract(gsml_Grade)


def test_gsml_grade_constructor_exists():
    assert callable(gsml_Grade.__init__)


def test_gsml_grade_constructor_args():
    sig = inspect.signature(gsml_Grade.__init__)
    params = list(sig.parameters.keys())
    assert "RequiredPoints" in params, "Missing parameter 'RequiredPoints'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_gsml_grade_has_RequiredPoints():
    assert hasattr(gsml_Grade, "RequiredPoints")
    descriptor = None
    for klass in gsml_Grade.__mro__:
        if "RequiredPoints" in klass.__dict__:
            descriptor = klass.__dict__["RequiredPoints"]
            break
    assert isinstance(descriptor, property)

def test_gsml_grade_has_Name():
    assert hasattr(gsml_Grade, "Name")
    descriptor = None
    for klass in gsml_Grade.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_gsml_taskgroup_is_not_abstract():
    assert not inspect.isabstract(gsml_TaskGroup)


def test_gsml_taskgroup_constructor_exists():
    assert callable(gsml_TaskGroup.__init__)


def test_gsml_taskgroup_constructor_args():
    sig = inspect.signature(gsml_TaskGroup.__init__)
    params = list(sig.parameters.keys())



def test_gsml_concretetask_is_not_abstract():
    assert not inspect.isabstract(gsml_ConcreteTask)


def test_gsml_concretetask_constructor_exists():
    assert callable(gsml_ConcreteTask.__init__)


def test_gsml_concretetask_constructor_args():
    sig = inspect.signature(gsml_ConcreteTask.__init__)
    params = list(sig.parameters.keys())
    assert "MaxPoints" in params, "Missing parameter 'MaxPoints'"

def test_gsml_concretetask_has_MaxPoints():
    assert hasattr(gsml_ConcreteTask, "MaxPoints")
    descriptor = None
    for klass in gsml_ConcreteTask.__mro__:
        if "MaxPoints" in klass.__dict__:
            descriptor = klass.__dict__["MaxPoints"]
            break
    assert isinstance(descriptor, property)



def test_gsml_task_is_not_abstract():
    assert not inspect.isabstract(gsml_Task)


def test_gsml_task_constructor_exists():
    assert callable(gsml_Task.__init__)


def test_gsml_task_constructor_args():
    sig = inspect.signature(gsml_Task.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "MinRequirementType" in params, "Missing parameter 'MinRequirementType'"
    assert "MinRequirement" in params, "Missing parameter 'MinRequirement'"

def test_gsml_task_has_Name():
    assert hasattr(gsml_Task, "Name")
    descriptor = None
    for klass in gsml_Task.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_gsml_task_has_MinRequirementType():
    assert hasattr(gsml_Task, "MinRequirementType")
    descriptor = None
    for klass in gsml_Task.__mro__:
        if "MinRequirementType" in klass.__dict__:
            descriptor = klass.__dict__["MinRequirementType"]
            break
    assert isinstance(descriptor, property)

def test_gsml_task_has_MinRequirement():
    assert hasattr(gsml_Task, "MinRequirement")
    descriptor = None
    for klass in gsml_Task.__mro__:
        if "MinRequirement" in klass.__dict__:
            descriptor = klass.__dict__["MinRequirement"]
            break
    assert isinstance(descriptor, property)



def test_gsml_gradingscheme_is_not_abstract():
    assert not inspect.isabstract(gsml_GradingScheme)


def test_gsml_gradingscheme_constructor_exists():
    assert callable(gsml_GradingScheme.__init__)


def test_gsml_gradingscheme_constructor_args():
    sig = inspect.signature(gsml_GradingScheme.__init__)
    params = list(sig.parameters.keys())



def test_gsml_grading_is_not_abstract():
    assert not inspect.isabstract(gsml_Grading)


def test_gsml_grading_constructor_exists():
    assert callable(gsml_Grading.__init__)


def test_gsml_grading_constructor_args():
    sig = inspect.signature(gsml_Grading.__init__)
    params = list(sig.parameters.keys())
    assert "Semester" in params, "Missing parameter 'Semester'"

def test_gsml_grading_has_Semester():
    assert hasattr(gsml_Grading, "Semester")
    descriptor = None
    for klass in gsml_Grading.__mro__:
        if "Semester" in klass.__dict__:
            descriptor = klass.__dict__["Semester"]
            break
    assert isinstance(descriptor, property)



def test_gsml_course_is_not_abstract():
    assert not inspect.isabstract(gsml_Course)


def test_gsml_course_constructor_exists():
    assert callable(gsml_Course.__init__)


def test_gsml_course_constructor_args():
    sig = inspect.signature(gsml_Course.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_gsml_course_has_Name():
    assert hasattr(gsml_Course, "Name")
    descriptor = None
    for klass in gsml_Course.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_minrequirementtype_exists():
    # Check that the Enumeration exists
    assert MinRequirementType is not None

def test_minrequirementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MinRequirementType]
    expected_literals = [
        "Relative",
        "Absolute",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MinRequirementType"


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
gsml_GradingSystem_strategy = st.builds(
    gsml_GradingSystem,
)
gsml_Grade_strategy = st.builds(
    gsml_Grade,
    RequiredPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Name=
        safe_text
)
Task_strategy = st.builds(
    Task,
)
gsml_TaskGroup_strategy = st.builds(
    gsml_TaskGroup,
)
gsml_ConcreteTask_strategy = st.builds(
    gsml_ConcreteTask,
    MaxPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
gsml_Task_strategy = st.builds(
    gsml_Task,
    Name=
        safe_text,
    MinRequirementType=
        safe_text,
    MinRequirement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
gsml_GradingScheme_strategy = st.builds(
    gsml_GradingScheme,
)
gsml_Grading_strategy = st.builds(
    gsml_Grading,
    Semester=
        safe_text
)
gsml_Course_strategy = st.builds(
    gsml_Course,
    Name=
        safe_text
)

@given(instance=gsml_GradingSystem_strategy)
@settings(max_examples=50)
def test_gsml_gradingsystem_instantiation(instance):
    assert isinstance(instance, gsml_GradingSystem)

@given(instance=gsml_Grade_strategy)
@settings(max_examples=50)
def test_gsml_grade_instantiation(instance):
    assert isinstance(instance, gsml_Grade)



@given(instance=gsml_Grade_strategy)
def test_gsml_grade_RequiredPoints_setter(instance):
    original = instance.RequiredPoints
    instance.RequiredPoints = original
    assert instance.RequiredPoints == original



@given(instance=gsml_Grade_strategy)
def test_gsml_grade_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=gsml_TaskGroup_strategy)
@settings(max_examples=50)
def test_gsml_taskgroup_instantiation(instance):
    assert isinstance(instance, gsml_TaskGroup)

@given(instance=gsml_ConcreteTask_strategy)
@settings(max_examples=50)
def test_gsml_concretetask_instantiation(instance):
    assert isinstance(instance, gsml_ConcreteTask)



@given(instance=gsml_ConcreteTask_strategy)
def test_gsml_concretetask_MaxPoints_setter(instance):
    original = instance.MaxPoints
    instance.MaxPoints = original
    assert instance.MaxPoints == original

@given(instance=gsml_Task_strategy)
@settings(max_examples=50)
def test_gsml_task_instantiation(instance):
    assert isinstance(instance, gsml_Task)



@given(instance=gsml_Task_strategy)
def test_gsml_task_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=gsml_Task_strategy)
def test_gsml_task_MinRequirementType_setter(instance):
    original = instance.MinRequirementType
    instance.MinRequirementType = original
    assert instance.MinRequirementType == original



@given(instance=gsml_Task_strategy)
def test_gsml_task_MinRequirement_setter(instance):
    original = instance.MinRequirement
    instance.MinRequirement = original
    assert instance.MinRequirement == original

@given(instance=gsml_GradingScheme_strategy)
@settings(max_examples=50)
def test_gsml_gradingscheme_instantiation(instance):
    assert isinstance(instance, gsml_GradingScheme)

@given(instance=gsml_Grading_strategy)
@settings(max_examples=50)
def test_gsml_grading_instantiation(instance):
    assert isinstance(instance, gsml_Grading)



@given(instance=gsml_Grading_strategy)
def test_gsml_grading_Semester_setter(instance):
    original = instance.Semester
    instance.Semester = original
    assert instance.Semester == original

@given(instance=gsml_Course_strategy)
@settings(max_examples=50)
def test_gsml_course_instantiation(instance):
    assert isinstance(instance, gsml_Course)



@given(instance=gsml_Course_strategy)
def test_gsml_course_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
