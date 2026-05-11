import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gradingsystem::Grade,
    gradingsystem::GradingScheme,
    Task,
    gradingsystem::TaskGroup,
    gradingsystem::ConcreteTask,
    gradingsystem::MinRequirement,
    gradingsystem::Task,
    gradingsystem::Grading,
    gradingsystem::Course,
    gradingsystem::GradingSystem,
    MinRequirementsType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gradingsystem::grade_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::Grade)


def test_gradingsystem::grade_constructor_exists():
    assert callable(gradingsystem::Grade.__init__)


def test_gradingsystem::grade_constructor_args():
    sig = inspect.signature(gradingsystem::Grade.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "requiredPoints" in params, "Missing parameter 'requiredPoints'"

def test_gradingsystem::grade_has_name():
    assert hasattr(gradingsystem::Grade, "name")
    descriptor = None
    for klass in gradingsystem::Grade.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gradingsystem::grade_has_requiredPoints():
    assert hasattr(gradingsystem::Grade, "requiredPoints")
    descriptor = None
    for klass in gradingsystem::Grade.__mro__:
        if "requiredPoints" in klass.__dict__:
            descriptor = klass.__dict__["requiredPoints"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem::gradingscheme_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::GradingScheme)


def test_gradingsystem::gradingscheme_constructor_exists():
    assert callable(gradingsystem::GradingScheme.__init__)


def test_gradingsystem::gradingscheme_constructor_args():
    sig = inspect.signature(gradingsystem::GradingScheme.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_gradingsystem::taskgroup_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::TaskGroup)


def test_gradingsystem::taskgroup_constructor_exists():
    assert callable(gradingsystem::TaskGroup.__init__)


def test_gradingsystem::taskgroup_constructor_args():
    sig = inspect.signature(gradingsystem::TaskGroup.__init__)
    params = list(sig.parameters.keys())



def test_gradingsystem::concretetask_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::ConcreteTask)


def test_gradingsystem::concretetask_constructor_exists():
    assert callable(gradingsystem::ConcreteTask.__init__)


def test_gradingsystem::concretetask_constructor_args():
    sig = inspect.signature(gradingsystem::ConcreteTask.__init__)
    params = list(sig.parameters.keys())
    assert "maxPoints" in params, "Missing parameter 'maxPoints'"

def test_gradingsystem::concretetask_has_maxPoints():
    assert hasattr(gradingsystem::ConcreteTask, "maxPoints")
    descriptor = None
    for klass in gradingsystem::ConcreteTask.__mro__:
        if "maxPoints" in klass.__dict__:
            descriptor = klass.__dict__["maxPoints"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem::minrequirement_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::MinRequirement)


def test_gradingsystem::minrequirement_constructor_exists():
    assert callable(gradingsystem::MinRequirement.__init__)


def test_gradingsystem::minrequirement_constructor_args():
    sig = inspect.signature(gradingsystem::MinRequirement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_gradingsystem::minrequirement_has_value():
    assert hasattr(gradingsystem::MinRequirement, "value")
    descriptor = None
    for klass in gradingsystem::MinRequirement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_gradingsystem::minrequirement_has_type():
    assert hasattr(gradingsystem::MinRequirement, "type")
    descriptor = None
    for klass in gradingsystem::MinRequirement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem::task_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::Task)


def test_gradingsystem::task_constructor_exists():
    assert callable(gradingsystem::Task.__init__)


def test_gradingsystem::task_constructor_args():
    sig = inspect.signature(gradingsystem::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gradingsystem::task_has_name():
    assert hasattr(gradingsystem::Task, "name")
    descriptor = None
    for klass in gradingsystem::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem::grading_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::Grading)


def test_gradingsystem::grading_constructor_exists():
    assert callable(gradingsystem::Grading.__init__)


def test_gradingsystem::grading_constructor_args():
    sig = inspect.signature(gradingsystem::Grading.__init__)
    params = list(sig.parameters.keys())
    assert "semester" in params, "Missing parameter 'semester'"

def test_gradingsystem::grading_has_semester():
    assert hasattr(gradingsystem::Grading, "semester")
    descriptor = None
    for klass in gradingsystem::Grading.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem::course_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::Course)


def test_gradingsystem::course_constructor_exists():
    assert callable(gradingsystem::Course.__init__)


def test_gradingsystem::course_constructor_args():
    sig = inspect.signature(gradingsystem::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gradingsystem::course_has_name():
    assert hasattr(gradingsystem::Course, "name")
    descriptor = None
    for klass in gradingsystem::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gradingsystem::gradingsystem_is_not_abstract():
    assert not inspect.isabstract(gradingsystem::GradingSystem)


def test_gradingsystem::gradingsystem_constructor_exists():
    assert callable(gradingsystem::GradingSystem.__init__)


def test_gradingsystem::gradingsystem_constructor_args():
    sig = inspect.signature(gradingsystem::GradingSystem.__init__)
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
gradingsystem::Grade_strategy = st.builds(
    gradingsystem::Grade,
    name=
        safe_text,
    requiredPoints=
        st.integers()
)
gradingsystem::GradingScheme_strategy = st.builds(
    gradingsystem::GradingScheme,
)
Task_strategy = st.builds(
    Task,
)
gradingsystem::TaskGroup_strategy = st.builds(
    gradingsystem::TaskGroup,
)
gradingsystem::ConcreteTask_strategy = st.builds(
    gradingsystem::ConcreteTask,
    maxPoints=
        st.integers()
)
gradingsystem::MinRequirement_strategy = st.builds(
    gradingsystem::MinRequirement,
    value=
        st.integers(),
    type=
        safe_text
)
gradingsystem::Task_strategy = st.builds(
    gradingsystem::Task,
    name=
        safe_text
)
gradingsystem::Grading_strategy = st.builds(
    gradingsystem::Grading,
    semester=
        safe_text
)
gradingsystem::Course_strategy = st.builds(
    gradingsystem::Course,
    name=
        safe_text
)
gradingsystem::GradingSystem_strategy = st.builds(
    gradingsystem::GradingSystem,
)

@given(instance=gradingsystem::Grade_strategy)
@settings(max_examples=50)
def test_gradingsystem::grade_instantiation(instance):
    assert isinstance(instance, gradingsystem::Grade)

@given(instance=gradingsystem::Grade_strategy)
def test_gradingsystem::grade_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gradingsystem::Grade_strategy)
def test_gradingsystem::grade_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gradingsystem::Grade_strategy)
def test_gradingsystem::grade_requiredPoints_type(instance):
    assert isinstance(instance.requiredPoints, int)


@given(instance=gradingsystem::Grade_strategy)
def test_gradingsystem::grade_requiredPoints_setter(instance):
    original = instance.requiredPoints
    instance.requiredPoints = original
    assert instance.requiredPoints == original

@given(instance=gradingsystem::GradingScheme_strategy)
@settings(max_examples=50)
def test_gradingsystem::gradingscheme_instantiation(instance):
    assert isinstance(instance, gradingsystem::GradingScheme)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=gradingsystem::TaskGroup_strategy)
@settings(max_examples=50)
def test_gradingsystem::taskgroup_instantiation(instance):
    assert isinstance(instance, gradingsystem::TaskGroup)

@given(instance=gradingsystem::ConcreteTask_strategy)
@settings(max_examples=50)
def test_gradingsystem::concretetask_instantiation(instance):
    assert isinstance(instance, gradingsystem::ConcreteTask)

@given(instance=gradingsystem::ConcreteTask_strategy)
def test_gradingsystem::concretetask_maxPoints_type(instance):
    assert isinstance(instance.maxPoints, int)


@given(instance=gradingsystem::ConcreteTask_strategy)
def test_gradingsystem::concretetask_maxPoints_setter(instance):
    original = instance.maxPoints
    instance.maxPoints = original
    assert instance.maxPoints == original

@given(instance=gradingsystem::MinRequirement_strategy)
@settings(max_examples=50)
def test_gradingsystem::minrequirement_instantiation(instance):
    assert isinstance(instance, gradingsystem::MinRequirement)

@given(instance=gradingsystem::MinRequirement_strategy)
def test_gradingsystem::minrequirement_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=gradingsystem::MinRequirement_strategy)
def test_gradingsystem::minrequirement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gradingsystem::MinRequirement_strategy)
def test_gradingsystem::minrequirement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=gradingsystem::MinRequirement_strategy)
def test_gradingsystem::minrequirement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=gradingsystem::Task_strategy)
@settings(max_examples=50)
def test_gradingsystem::task_instantiation(instance):
    assert isinstance(instance, gradingsystem::Task)

@given(instance=gradingsystem::Task_strategy)
def test_gradingsystem::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gradingsystem::Task_strategy)
def test_gradingsystem::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gradingsystem::Grading_strategy)
@settings(max_examples=50)
def test_gradingsystem::grading_instantiation(instance):
    assert isinstance(instance, gradingsystem::Grading)

@given(instance=gradingsystem::Grading_strategy)
def test_gradingsystem::grading_semester_type(instance):
    assert isinstance(instance.semester, str)


@given(instance=gradingsystem::Grading_strategy)
def test_gradingsystem::grading_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=gradingsystem::Course_strategy)
@settings(max_examples=50)
def test_gradingsystem::course_instantiation(instance):
    assert isinstance(instance, gradingsystem::Course)

@given(instance=gradingsystem::Course_strategy)
def test_gradingsystem::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gradingsystem::Course_strategy)
def test_gradingsystem::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gradingsystem::GradingSystem_strategy)
@settings(max_examples=50)
def test_gradingsystem::gradingsystem_instantiation(instance):
    assert isinstance(instance, gradingsystem::GradingSystem)
