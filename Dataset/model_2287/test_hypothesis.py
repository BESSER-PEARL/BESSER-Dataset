import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gsml::GradingSystem,
    gsml::Grade,
    Task,
    gsml::TaskGroup,
    gsml::ConcreteTask,
    gsml::Task,
    gsml::GradingScheme,
    gsml::Grading,
    gsml::Course,
    MinRequirementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gsml::gradingsystem_is_not_abstract():
    assert not inspect.isabstract(gsml::GradingSystem)


def test_gsml::gradingsystem_constructor_exists():
    assert callable(gsml::GradingSystem.__init__)


def test_gsml::gradingsystem_constructor_args():
    sig = inspect.signature(gsml::GradingSystem.__init__)
    params = list(sig.parameters.keys())



def test_gsml::grade_is_not_abstract():
    assert not inspect.isabstract(gsml::Grade)


def test_gsml::grade_constructor_exists():
    assert callable(gsml::Grade.__init__)


def test_gsml::grade_constructor_args():
    sig = inspect.signature(gsml::Grade.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "RequiredPoints" in params, "Missing parameter 'RequiredPoints'"

def test_gsml::grade_has_Name():
    assert hasattr(gsml::Grade, "Name")
    descriptor = None
    for klass in gsml::Grade.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_gsml::grade_has_RequiredPoints():
    assert hasattr(gsml::Grade, "RequiredPoints")
    descriptor = None
    for klass in gsml::Grade.__mro__:
        if "RequiredPoints" in klass.__dict__:
            descriptor = klass.__dict__["RequiredPoints"]
            break
    assert isinstance(descriptor, property)



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_gsml::taskgroup_is_not_abstract():
    assert not inspect.isabstract(gsml::TaskGroup)


def test_gsml::taskgroup_constructor_exists():
    assert callable(gsml::TaskGroup.__init__)


def test_gsml::taskgroup_constructor_args():
    sig = inspect.signature(gsml::TaskGroup.__init__)
    params = list(sig.parameters.keys())



def test_gsml::concretetask_is_not_abstract():
    assert not inspect.isabstract(gsml::ConcreteTask)


def test_gsml::concretetask_constructor_exists():
    assert callable(gsml::ConcreteTask.__init__)


def test_gsml::concretetask_constructor_args():
    sig = inspect.signature(gsml::ConcreteTask.__init__)
    params = list(sig.parameters.keys())
    assert "MaxPoints" in params, "Missing parameter 'MaxPoints'"

def test_gsml::concretetask_has_MaxPoints():
    assert hasattr(gsml::ConcreteTask, "MaxPoints")
    descriptor = None
    for klass in gsml::ConcreteTask.__mro__:
        if "MaxPoints" in klass.__dict__:
            descriptor = klass.__dict__["MaxPoints"]
            break
    assert isinstance(descriptor, property)



def test_gsml::task_is_not_abstract():
    assert not inspect.isabstract(gsml::Task)


def test_gsml::task_constructor_exists():
    assert callable(gsml::Task.__init__)


def test_gsml::task_constructor_args():
    sig = inspect.signature(gsml::Task.__init__)
    params = list(sig.parameters.keys())
    assert "MinRequirement" in params, "Missing parameter 'MinRequirement'"
    assert "MinRequirementType" in params, "Missing parameter 'MinRequirementType'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_gsml::task_has_MinRequirement():
    assert hasattr(gsml::Task, "MinRequirement")
    descriptor = None
    for klass in gsml::Task.__mro__:
        if "MinRequirement" in klass.__dict__:
            descriptor = klass.__dict__["MinRequirement"]
            break
    assert isinstance(descriptor, property)

def test_gsml::task_has_MinRequirementType():
    assert hasattr(gsml::Task, "MinRequirementType")
    descriptor = None
    for klass in gsml::Task.__mro__:
        if "MinRequirementType" in klass.__dict__:
            descriptor = klass.__dict__["MinRequirementType"]
            break
    assert isinstance(descriptor, property)

def test_gsml::task_has_Name():
    assert hasattr(gsml::Task, "Name")
    descriptor = None
    for klass in gsml::Task.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_gsml::gradingscheme_is_not_abstract():
    assert not inspect.isabstract(gsml::GradingScheme)


def test_gsml::gradingscheme_constructor_exists():
    assert callable(gsml::GradingScheme.__init__)


def test_gsml::gradingscheme_constructor_args():
    sig = inspect.signature(gsml::GradingScheme.__init__)
    params = list(sig.parameters.keys())



def test_gsml::grading_is_not_abstract():
    assert not inspect.isabstract(gsml::Grading)


def test_gsml::grading_constructor_exists():
    assert callable(gsml::Grading.__init__)


def test_gsml::grading_constructor_args():
    sig = inspect.signature(gsml::Grading.__init__)
    params = list(sig.parameters.keys())
    assert "Semester" in params, "Missing parameter 'Semester'"

def test_gsml::grading_has_Semester():
    assert hasattr(gsml::Grading, "Semester")
    descriptor = None
    for klass in gsml::Grading.__mro__:
        if "Semester" in klass.__dict__:
            descriptor = klass.__dict__["Semester"]
            break
    assert isinstance(descriptor, property)



def test_gsml::course_is_not_abstract():
    assert not inspect.isabstract(gsml::Course)


def test_gsml::course_constructor_exists():
    assert callable(gsml::Course.__init__)


def test_gsml::course_constructor_args():
    sig = inspect.signature(gsml::Course.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_gsml::course_has_Name():
    assert hasattr(gsml::Course, "Name")
    descriptor = None
    for klass in gsml::Course.__mro__:
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
gsml::GradingSystem_strategy = st.builds(
    gsml::GradingSystem,
)
gsml::Grade_strategy = st.builds(
    gsml::Grade,
    Name=
        safe_text,
    RequiredPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Task_strategy = st.builds(
    Task,
)
gsml::TaskGroup_strategy = st.builds(
    gsml::TaskGroup,
)
gsml::ConcreteTask_strategy = st.builds(
    gsml::ConcreteTask,
    MaxPoints=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
gsml::Task_strategy = st.builds(
    gsml::Task,
    MinRequirement=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    MinRequirementType=
        safe_text,
    Name=
        safe_text
)
gsml::GradingScheme_strategy = st.builds(
    gsml::GradingScheme,
)
gsml::Grading_strategy = st.builds(
    gsml::Grading,
    Semester=
        safe_text
)
gsml::Course_strategy = st.builds(
    gsml::Course,
    Name=
        safe_text
)

@given(instance=gsml::GradingSystem_strategy)
@settings(max_examples=50)
def test_gsml::gradingsystem_instantiation(instance):
    assert isinstance(instance, gsml::GradingSystem)

@given(instance=gsml::Grade_strategy)
@settings(max_examples=50)
def test_gsml::grade_instantiation(instance):
    assert isinstance(instance, gsml::Grade)

@given(instance=gsml::Grade_strategy)
def test_gsml::grade_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=gsml::Grade_strategy)
def test_gsml::grade_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=gsml::Grade_strategy)
def test_gsml::grade_RequiredPoints_type(instance):
    assert isinstance(instance.RequiredPoints, float)


@given(instance=gsml::Grade_strategy)
def test_gsml::grade_RequiredPoints_setter(instance):
    original = instance.RequiredPoints
    instance.RequiredPoints = original
    assert instance.RequiredPoints == original

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=gsml::TaskGroup_strategy)
@settings(max_examples=50)
def test_gsml::taskgroup_instantiation(instance):
    assert isinstance(instance, gsml::TaskGroup)

@given(instance=gsml::ConcreteTask_strategy)
@settings(max_examples=50)
def test_gsml::concretetask_instantiation(instance):
    assert isinstance(instance, gsml::ConcreteTask)

@given(instance=gsml::ConcreteTask_strategy)
def test_gsml::concretetask_MaxPoints_type(instance):
    assert isinstance(instance.MaxPoints, float)


@given(instance=gsml::ConcreteTask_strategy)
def test_gsml::concretetask_MaxPoints_setter(instance):
    original = instance.MaxPoints
    instance.MaxPoints = original
    assert instance.MaxPoints == original

@given(instance=gsml::Task_strategy)
@settings(max_examples=50)
def test_gsml::task_instantiation(instance):
    assert isinstance(instance, gsml::Task)

@given(instance=gsml::Task_strategy)
def test_gsml::task_MinRequirement_type(instance):
    assert isinstance(instance.MinRequirement, float)


@given(instance=gsml::Task_strategy)
def test_gsml::task_MinRequirement_setter(instance):
    original = instance.MinRequirement
    instance.MinRequirement = original
    assert instance.MinRequirement == original

@given(instance=gsml::Task_strategy)
def test_gsml::task_MinRequirementType_type(instance):
    assert isinstance(instance.MinRequirementType, str)


@given(instance=gsml::Task_strategy)
def test_gsml::task_MinRequirementType_setter(instance):
    original = instance.MinRequirementType
    instance.MinRequirementType = original
    assert instance.MinRequirementType == original

@given(instance=gsml::Task_strategy)
def test_gsml::task_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=gsml::Task_strategy)
def test_gsml::task_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=gsml::GradingScheme_strategy)
@settings(max_examples=50)
def test_gsml::gradingscheme_instantiation(instance):
    assert isinstance(instance, gsml::GradingScheme)

@given(instance=gsml::Grading_strategy)
@settings(max_examples=50)
def test_gsml::grading_instantiation(instance):
    assert isinstance(instance, gsml::Grading)

@given(instance=gsml::Grading_strategy)
def test_gsml::grading_Semester_type(instance):
    assert isinstance(instance.Semester, str)


@given(instance=gsml::Grading_strategy)
def test_gsml::grading_Semester_setter(instance):
    original = instance.Semester
    instance.Semester = original
    assert instance.Semester == original

@given(instance=gsml::Course_strategy)
@settings(max_examples=50)
def test_gsml::course_instantiation(instance):
    assert isinstance(instance, gsml::Course)

@given(instance=gsml::Course_strategy)
def test_gsml::course_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=gsml::Course_strategy)
def test_gsml::course_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
