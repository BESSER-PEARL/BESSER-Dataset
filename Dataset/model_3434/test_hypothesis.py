import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    school::store,
    school::NewEClass7,
    school::SchoolYear,
    school::Room,
    school::ClassLevel,
    school::Teacher,
    school::Student,
    school::ClassGroup,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school::store_is_not_abstract():
    assert not inspect.isabstract(school::store)


def test_school::store_constructor_exists():
    assert callable(school::store.__init__)


def test_school::store_constructor_args():
    sig = inspect.signature(school::store.__init__)
    params = list(sig.parameters.keys())
    assert "lastIn" in params, "Missing parameter 'lastIn'"

def test_school::store_has_lastIn():
    assert hasattr(school::store, "lastIn")
    descriptor = None
    for klass in school::store.__mro__:
        if "lastIn" in klass.__dict__:
            descriptor = klass.__dict__["lastIn"]
            break
    assert isinstance(descriptor, property)



def test_school::neweclass7_is_not_abstract():
    assert not inspect.isabstract(school::NewEClass7)


def test_school::neweclass7_constructor_exists():
    assert callable(school::NewEClass7.__init__)


def test_school::neweclass7_constructor_args():
    sig = inspect.signature(school::NewEClass7.__init__)
    params = list(sig.parameters.keys())



def test_school::schoolyear_is_not_abstract():
    assert not inspect.isabstract(school::SchoolYear)


def test_school::schoolyear_constructor_exists():
    assert callable(school::SchoolYear.__init__)


def test_school::schoolyear_constructor_args():
    sig = inspect.signature(school::SchoolYear.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_school::schoolyear_has_year():
    assert hasattr(school::SchoolYear, "year")
    descriptor = None
    for klass in school::SchoolYear.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_school::room_is_not_abstract():
    assert not inspect.isabstract(school::Room)


def test_school::room_constructor_exists():
    assert callable(school::Room.__init__)


def test_school::room_constructor_args():
    sig = inspect.signature(school::Room.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_school::room_has_location():
    assert hasattr(school::Room, "location")
    descriptor = None
    for klass in school::Room.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_school::classlevel_is_not_abstract():
    assert not inspect.isabstract(school::ClassLevel)


def test_school::classlevel_constructor_exists():
    assert callable(school::ClassLevel.__init__)


def test_school::classlevel_constructor_args():
    sig = inspect.signature(school::ClassLevel.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_school::classlevel_has_level():
    assert hasattr(school::ClassLevel, "level")
    descriptor = None
    for klass in school::ClassLevel.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_school::teacher_is_not_abstract():
    assert not inspect.isabstract(school::Teacher)


def test_school::teacher_constructor_exists():
    assert callable(school::Teacher.__init__)


def test_school::teacher_constructor_args():
    sig = inspect.signature(school::Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::teacher_has_name():
    assert hasattr(school::Teacher, "name")
    descriptor = None
    for klass in school::Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::student_is_not_abstract():
    assert not inspect.isabstract(school::Student)


def test_school::student_constructor_exists():
    assert callable(school::Student.__init__)


def test_school::student_constructor_args():
    sig = inspect.signature(school::Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::student_has_name():
    assert hasattr(school::Student, "name")
    descriptor = None
    for klass in school::Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school::classgroup_is_not_abstract():
    assert not inspect.isabstract(school::ClassGroup)


def test_school::classgroup_constructor_exists():
    assert callable(school::ClassGroup.__init__)


def test_school::classgroup_constructor_args():
    sig = inspect.signature(school::ClassGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school::classgroup_has_name():
    assert hasattr(school::ClassGroup, "name")
    descriptor = None
    for klass in school::ClassGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
school::store_strategy = st.builds(
    school::store,
    lastIn=
        safe_text
)
school::NewEClass7_strategy = st.builds(
    school::NewEClass7,
)
school::SchoolYear_strategy = st.builds(
    school::SchoolYear,
    year=
        st.dates()
)
school::Room_strategy = st.builds(
    school::Room,
    location=
        safe_text
)
school::ClassLevel_strategy = st.builds(
    school::ClassLevel,
    level=
        st.integers()
)
school::Teacher_strategy = st.builds(
    school::Teacher,
    name=
        safe_text
)
school::Student_strategy = st.builds(
    school::Student,
    name=
        safe_text
)
school::ClassGroup_strategy = st.builds(
    school::ClassGroup,
    name=
        safe_text
)

@given(instance=school::store_strategy)
@settings(max_examples=50)
def test_school::store_instantiation(instance):
    assert isinstance(instance, school::store)

@given(instance=school::store_strategy)
def test_school::store_lastIn_type(instance):
    assert isinstance(instance.lastIn, str)


@given(instance=school::store_strategy)
def test_school::store_lastIn_setter(instance):
    original = instance.lastIn
    instance.lastIn = original
    assert instance.lastIn == original

@given(instance=school::NewEClass7_strategy)
@settings(max_examples=50)
def test_school::neweclass7_instantiation(instance):
    assert isinstance(instance, school::NewEClass7)

@given(instance=school::SchoolYear_strategy)
@settings(max_examples=50)
def test_school::schoolyear_instantiation(instance):
    assert isinstance(instance, school::SchoolYear)

@given(instance=school::SchoolYear_strategy)
def test_school::schoolyear_year_type(instance):
    assert isinstance(instance.year, date)


@given(instance=school::SchoolYear_strategy)
def test_school::schoolyear_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=school::Room_strategy)
@settings(max_examples=50)
def test_school::room_instantiation(instance):
    assert isinstance(instance, school::Room)

@given(instance=school::Room_strategy)
def test_school::room_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=school::Room_strategy)
def test_school::room_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=school::Room_strategy)
@settings(max_examples=30)
def test_school::room_affectteacher_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AffectTeacher(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AffectTeacher).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AffectTeacher' in school::Room is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AffectTeacher' in school::Room did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AffectTeacher' in school::Room is not implemented or raised an error")

@given(instance=school::ClassLevel_strategy)
@settings(max_examples=50)
def test_school::classlevel_instantiation(instance):
    assert isinstance(instance, school::ClassLevel)

@given(instance=school::ClassLevel_strategy)
def test_school::classlevel_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=school::ClassLevel_strategy)
def test_school::classlevel_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=school::Teacher_strategy)
@settings(max_examples=50)
def test_school::teacher_instantiation(instance):
    assert isinstance(instance, school::Teacher)

@given(instance=school::Teacher_strategy)
def test_school::teacher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Teacher_strategy)
def test_school::teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::Student_strategy)
@settings(max_examples=50)
def test_school::student_instantiation(instance):
    assert isinstance(instance, school::Student)

@given(instance=school::Student_strategy)
def test_school::student_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::Student_strategy)
def test_school::student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school::ClassGroup_strategy)
@settings(max_examples=50)
def test_school::classgroup_instantiation(instance):
    assert isinstance(instance, school::ClassGroup)

@given(instance=school::ClassGroup_strategy)
def test_school::classgroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=school::ClassGroup_strategy)
def test_school::classgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
