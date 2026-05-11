import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mteach::Topic,
    mteach::Course,
    mteach::Professor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mteach::topic_is_not_abstract():
    assert not inspect.isabstract(mteach::Topic)


def test_mteach::topic_constructor_exists():
    assert callable(mteach::Topic.__init__)


def test_mteach::topic_constructor_args():
    sig = inspect.signature(mteach::Topic.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_mteach::topic_has_title():
    assert hasattr(mteach::Topic, "title")
    descriptor = None
    for klass in mteach::Topic.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_mteach::course_is_not_abstract():
    assert not inspect.isabstract(mteach::Course)


def test_mteach::course_constructor_exists():
    assert callable(mteach::Course.__init__)


def test_mteach::course_constructor_args():
    sig = inspect.signature(mteach::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "time" in params, "Missing parameter 'time'"
    assert "coefficient" in params, "Missing parameter 'coefficient'"

def test_mteach::course_has_name():
    assert hasattr(mteach::Course, "name")
    descriptor = None
    for klass in mteach::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mteach::course_has_time():
    assert hasattr(mteach::Course, "time")
    descriptor = None
    for klass in mteach::Course.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_mteach::course_has_coefficient():
    assert hasattr(mteach::Course, "coefficient")
    descriptor = None
    for klass in mteach::Course.__mro__:
        if "coefficient" in klass.__dict__:
            descriptor = klass.__dict__["coefficient"]
            break
    assert isinstance(descriptor, property)



def test_mteach::professor_is_not_abstract():
    assert not inspect.isabstract(mteach::Professor)


def test_mteach::professor_constructor_exists():
    assert callable(mteach::Professor.__init__)


def test_mteach::professor_constructor_args():
    sig = inspect.signature(mteach::Professor.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_mteach::professor_has_firstName():
    assert hasattr(mteach::Professor, "firstName")
    descriptor = None
    for klass in mteach::Professor.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_mteach::professor_has_lastName():
    assert hasattr(mteach::Professor, "lastName")
    descriptor = None
    for klass in mteach::Professor.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
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
mteach::Topic_strategy = st.builds(
    mteach::Topic,
    title=
        safe_text
)
mteach::Course_strategy = st.builds(
    mteach::Course,
    name=
        safe_text,
    time=
        st.integers(),
    coefficient=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mteach::Professor_strategy = st.builds(
    mteach::Professor,
    firstName=
        safe_text,
    lastName=
        safe_text
)

@given(instance=mteach::Topic_strategy)
@settings(max_examples=50)
def test_mteach::topic_instantiation(instance):
    assert isinstance(instance, mteach::Topic)

@given(instance=mteach::Topic_strategy)
def test_mteach::topic_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mteach::Topic_strategy)
def test_mteach::topic_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=mteach::Course_strategy)
@settings(max_examples=50)
def test_mteach::course_instantiation(instance):
    assert isinstance(instance, mteach::Course)

@given(instance=mteach::Course_strategy)
def test_mteach::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mteach::Course_strategy)
def test_mteach::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mteach::Course_strategy)
def test_mteach::course_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=mteach::Course_strategy)
def test_mteach::course_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=mteach::Course_strategy)
def test_mteach::course_coefficient_type(instance):
    assert isinstance(instance.coefficient, float)


@given(instance=mteach::Course_strategy)
def test_mteach::course_coefficient_setter(instance):
    original = instance.coefficient
    instance.coefficient = original
    assert instance.coefficient == original

@given(instance=mteach::Professor_strategy)
@settings(max_examples=50)
def test_mteach::professor_instantiation(instance):
    assert isinstance(instance, mteach::Professor)

@given(instance=mteach::Professor_strategy)
def test_mteach::professor_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=mteach::Professor_strategy)
def test_mteach::professor_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=mteach::Professor_strategy)
def test_mteach::professor_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=mteach::Professor_strategy)
def test_mteach::professor_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original
