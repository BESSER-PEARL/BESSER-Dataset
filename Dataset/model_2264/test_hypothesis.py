import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mteach_Topic,
    mteach_Course,
    mteach_Professor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mteach_topic_is_not_abstract():
    assert not inspect.isabstract(mteach_Topic)


def test_mteach_topic_constructor_exists():
    assert callable(mteach_Topic.__init__)


def test_mteach_topic_constructor_args():
    sig = inspect.signature(mteach_Topic.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_mteach_topic_has_title():
    assert hasattr(mteach_Topic, "title")
    descriptor = None
    for klass in mteach_Topic.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_mteach_course_is_not_abstract():
    assert not inspect.isabstract(mteach_Course)


def test_mteach_course_constructor_exists():
    assert callable(mteach_Course.__init__)


def test_mteach_course_constructor_args():
    sig = inspect.signature(mteach_Course.__init__)
    params = list(sig.parameters.keys())
    assert "coefficient" in params, "Missing parameter 'coefficient'"
    assert "name" in params, "Missing parameter 'name'"
    assert "time" in params, "Missing parameter 'time'"

def test_mteach_course_has_coefficient():
    assert hasattr(mteach_Course, "coefficient")
    descriptor = None
    for klass in mteach_Course.__mro__:
        if "coefficient" in klass.__dict__:
            descriptor = klass.__dict__["coefficient"]
            break
    assert isinstance(descriptor, property)

def test_mteach_course_has_name():
    assert hasattr(mteach_Course, "name")
    descriptor = None
    for klass in mteach_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mteach_course_has_time():
    assert hasattr(mteach_Course, "time")
    descriptor = None
    for klass in mteach_Course.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_mteach_professor_is_not_abstract():
    assert not inspect.isabstract(mteach_Professor)


def test_mteach_professor_constructor_exists():
    assert callable(mteach_Professor.__init__)


def test_mteach_professor_constructor_args():
    sig = inspect.signature(mteach_Professor.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_mteach_professor_has_lastName():
    assert hasattr(mteach_Professor, "lastName")
    descriptor = None
    for klass in mteach_Professor.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_mteach_professor_has_firstName():
    assert hasattr(mteach_Professor, "firstName")
    descriptor = None
    for klass in mteach_Professor.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
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
mteach_Topic_strategy = st.builds(
    mteach_Topic,
    title=
        safe_text
)
mteach_Course_strategy = st.builds(
    mteach_Course,
    coefficient=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    time=
        st.integers()
)
mteach_Professor_strategy = st.builds(
    mteach_Professor,
    lastName=
        safe_text,
    firstName=
        safe_text
)

@given(instance=mteach_Topic_strategy)
@settings(max_examples=50)
def test_mteach_topic_instantiation(instance):
    assert isinstance(instance, mteach_Topic)



@given(instance=mteach_Topic_strategy)
def test_mteach_topic_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mteach_Course_strategy)
@settings(max_examples=50)
def test_mteach_course_instantiation(instance):
    assert isinstance(instance, mteach_Course)



@given(instance=mteach_Course_strategy)
def test_mteach_course_coefficient_setter(instance):
    original = instance.coefficient
    instance.coefficient = original
    assert instance.coefficient == original



@given(instance=mteach_Course_strategy)
def test_mteach_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mteach_Course_strategy)
def test_mteach_course_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=mteach_Professor_strategy)
@settings(max_examples=50)
def test_mteach_professor_instantiation(instance):
    assert isinstance(instance, mteach_Professor)



@given(instance=mteach_Professor_strategy)
def test_mteach_professor_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=mteach_Professor_strategy)
def test_mteach_professor_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
