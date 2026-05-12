import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    gradingsystem_Grade,
    gradingsystem_GradingScheme,
    Task,
    gradingsystem_TaskGroup,
    gradingsystem_ConcreteTask,
    gradingsystem_MinRequirement,
    gradingsystem_Task,
    gradingsystem_Grading,
    gradingsystem_Course,
    gradingsystem_GradingSystem,
    MinRequirementsType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gradingsystem_grade_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_Grade)


def test_gradingsystem_grade_constructor_exists():
    assert callable(gradingsystem_Grade.__init__)


def test_gradingsystem_grade_constructor_args():
    sig = inspect.signature(gradingsystem_Grade.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "requiredPoints" in params, "Missing parameter 'requiredPoints'"

def test_gradingsystem_grade_has_name():
    assert hasattr(gradingsystem_Grade, "name")
    descriptor = None
    for klass in gradingsystem_Grade.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gradingsystem_grade_has_requiredPoints():
    assert hasattr(gradingsystem_Grade, "requiredPoints")
    descriptor = None
    for klass in gradingsystem_Grade.__mro__:
        if "requiredPoints" in klass.__dict__:
            descriptor = klass.__dict__["requiredPoints"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem_gradingscheme_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_GradingScheme)


def test_gradingsystem_gradingscheme_constructor_exists():
    assert callable(gradingsystem_GradingScheme.__init__)


def test_gradingsystem_gradingscheme_constructor_args():
    sig = inspect.signature(gradingsystem_GradingScheme.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_gradingsystem_taskgroup_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_TaskGroup)


def test_gradingsystem_taskgroup_constructor_exists():
    assert callable(gradingsystem_TaskGroup.__init__)


def test_gradingsystem_taskgroup_constructor_args():
    sig = inspect.signature(gradingsystem_TaskGroup.__init__)
    params = list(sig.parameters.keys())



def test_gradingsystem_concretetask_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_ConcreteTask)


def test_gradingsystem_concretetask_constructor_exists():
    assert callable(gradingsystem_ConcreteTask.__init__)


def test_gradingsystem_concretetask_constructor_args():
    sig = inspect.signature(gradingsystem_ConcreteTask.__init__)
    params = list(sig.parameters.keys())
    assert "maxPoints" in params, "Missing parameter 'maxPoints'"

def test_gradingsystem_concretetask_has_maxPoints():
    assert hasattr(gradingsystem_ConcreteTask, "maxPoints")
    descriptor = None
    for klass in gradingsystem_ConcreteTask.__mro__:
        if "maxPoints" in klass.__dict__:
            descriptor = klass.__dict__["maxPoints"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem_minrequirement_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_MinRequirement)


def test_gradingsystem_minrequirement_constructor_exists():
    assert callable(gradingsystem_MinRequirement.__init__)


def test_gradingsystem_minrequirement_constructor_args():
    sig = inspect.signature(gradingsystem_MinRequirement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_gradingsystem_minrequirement_has_type():
    assert hasattr(gradingsystem_MinRequirement, "type")
    descriptor = None
    for klass in gradingsystem_MinRequirement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gradingsystem_minrequirement_has_value():
    assert hasattr(gradingsystem_MinRequirement, "value")
    descriptor = None
    for klass in gradingsystem_MinRequirement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem_task_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_Task)


def test_gradingsystem_task_constructor_exists():
    assert callable(gradingsystem_Task.__init__)


def test_gradingsystem_task_constructor_args():
    sig = inspect.signature(gradingsystem_Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gradingsystem_task_has_name():
    assert hasattr(gradingsystem_Task, "name")
    descriptor = None
    for klass in gradingsystem_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem_grading_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_Grading)


def test_gradingsystem_grading_constructor_exists():
    assert callable(gradingsystem_Grading.__init__)


def test_gradingsystem_grading_constructor_args():
    sig = inspect.signature(gradingsystem_Grading.__init__)
    params = list(sig.parameters.keys())
    assert "semester" in params, "Missing parameter 'semester'"

def test_gradingsystem_grading_has_semester():
    assert hasattr(gradingsystem_Grading, "semester")
    descriptor = None
    for klass in gradingsystem_Grading.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem_course_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_Course)


def test_gradingsystem_course_constructor_exists():
    assert callable(gradingsystem_Course.__init__)


def test_gradingsystem_course_constructor_args():
    sig = inspect.signature(gradingsystem_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gradingsystem_course_has_name():
    assert hasattr(gradingsystem_Course, "name")
    descriptor = None
    for klass in gradingsystem_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem_gradingsystem_is_not_abstract():
    assert not inspect.isabstract(gradingsystem_GradingSystem)


def test_gradingsystem_gradingsystem_constructor_exists():
    assert callable(gradingsystem_GradingSystem.__init__)


def test_gradingsystem_gradingsystem_constructor_args():
    sig = inspect.signature(gradingsystem_GradingSystem.__init__)
    params = list(sig.parameters.keys())

def test_minrequirementstype_exists():
    # Check that the Enumeration exists
    assert MinRequirementsType is not None

def test_minrequirementstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MinRequirementsType]
    expected_literals = [
        "Percentage",
        "Absolute",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MinRequirementsType"


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
gradingsystem_Grade_strategy = st.builds(
    gradingsystem_Grade,
    name=
        safe_text,
    requiredPoints=
        st.integers()
)
gradingsystem_GradingScheme_strategy = st.builds(
    gradingsystem_GradingScheme,
)
Task_strategy = st.builds(
    Task,
)
gradingsystem_TaskGroup_strategy = st.builds(
    gradingsystem_TaskGroup,
)
gradingsystem_ConcreteTask_strategy = st.builds(
    gradingsystem_ConcreteTask,
    maxPoints=
        st.integers()
)
gradingsystem_MinRequirement_strategy = st.builds(
    gradingsystem_MinRequirement,
    type=
        safe_text,
    value=
        st.integers()
)
gradingsystem_Task_strategy = st.builds(
    gradingsystem_Task,
    name=
        safe_text
)
gradingsystem_Grading_strategy = st.builds(
    gradingsystem_Grading,
    semester=
        safe_text
)
gradingsystem_Course_strategy = st.builds(
    gradingsystem_Course,
    name=
        safe_text
)
gradingsystem_GradingSystem_strategy = st.builds(
    gradingsystem_GradingSystem,
)

@given(instance=gradingsystem_Grade_strategy)
@settings(max_examples=50)
def test_gradingsystem_grade_instantiation(instance):
    assert isinstance(instance, gradingsystem_Grade)



@given(instance=gradingsystem_Grade_strategy)
def test_gradingsystem_grade_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gradingsystem_Grade_strategy)
def test_gradingsystem_grade_requiredPoints_setter(instance):
    original = instance.requiredPoints
    instance.requiredPoints = original
    assert instance.requiredPoints == original

@given(instance=gradingsystem_GradingScheme_strategy)
@settings(max_examples=50)
def test_gradingsystem_gradingscheme_instantiation(instance):
    assert isinstance(instance, gradingsystem_GradingScheme)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=gradingsystem_TaskGroup_strategy)
@settings(max_examples=50)
def test_gradingsystem_taskgroup_instantiation(instance):
    assert isinstance(instance, gradingsystem_TaskGroup)

@given(instance=gradingsystem_ConcreteTask_strategy)
@settings(max_examples=50)
def test_gradingsystem_concretetask_instantiation(instance):
    assert isinstance(instance, gradingsystem_ConcreteTask)



@given(instance=gradingsystem_ConcreteTask_strategy)
def test_gradingsystem_concretetask_maxPoints_setter(instance):
    original = instance.maxPoints
    instance.maxPoints = original
    assert instance.maxPoints == original

@given(instance=gradingsystem_MinRequirement_strategy)
@settings(max_examples=50)
def test_gradingsystem_minrequirement_instantiation(instance):
    assert isinstance(instance, gradingsystem_MinRequirement)



@given(instance=gradingsystem_MinRequirement_strategy)
def test_gradingsystem_minrequirement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=gradingsystem_MinRequirement_strategy)
def test_gradingsystem_minrequirement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gradingsystem_Task_strategy)
@settings(max_examples=50)
def test_gradingsystem_task_instantiation(instance):
    assert isinstance(instance, gradingsystem_Task)



@given(instance=gradingsystem_Task_strategy)
def test_gradingsystem_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gradingsystem_Grading_strategy)
@settings(max_examples=50)
def test_gradingsystem_grading_instantiation(instance):
    assert isinstance(instance, gradingsystem_Grading)



@given(instance=gradingsystem_Grading_strategy)
def test_gradingsystem_grading_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=gradingsystem_Course_strategy)
@settings(max_examples=50)
def test_gradingsystem_course_instantiation(instance):
    assert isinstance(instance, gradingsystem_Course)



@given(instance=gradingsystem_Course_strategy)
def test_gradingsystem_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gradingsystem_GradingSystem_strategy)
@settings(max_examples=50)
def test_gradingsystem_gradingsystem_instantiation(instance):
    assert isinstance(instance, gradingsystem_GradingSystem)
