import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    school_store,
    school_NewEClass7,
    school_SchoolYear,
    school_Room,
    school_ClassLevel,
    school_Teacher,
    school_Student,
    school_ClassGroup,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_school_store_is_not_abstract():
    assert not inspect.isabstract(school_store)


def test_school_store_constructor_exists():
    assert callable(school_store.__init__)


def test_school_store_constructor_args():
    sig = inspect.signature(school_store.__init__)
    params = list(sig.parameters.keys())
    assert "lastIn" in params, "Missing parameter 'lastIn'"

def test_school_store_has_lastIn():
    assert hasattr(school_store, "lastIn")
    descriptor = None
    for klass in school_store.__mro__:
        if "lastIn" in klass.__dict__:
            descriptor = klass.__dict__["lastIn"]
            break
    assert isinstance(descriptor, property)



def test_school_neweclass7_is_not_abstract():
    assert not inspect.isabstract(school_NewEClass7)


def test_school_neweclass7_constructor_exists():
    assert callable(school_NewEClass7.__init__)


def test_school_neweclass7_constructor_args():
    sig = inspect.signature(school_NewEClass7.__init__)
    params = list(sig.parameters.keys())



def test_school_schoolyear_is_not_abstract():
    assert not inspect.isabstract(school_SchoolYear)


def test_school_schoolyear_constructor_exists():
    assert callable(school_SchoolYear.__init__)


def test_school_schoolyear_constructor_args():
    sig = inspect.signature(school_SchoolYear.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_school_schoolyear_has_year():
    assert hasattr(school_SchoolYear, "year")
    descriptor = None
    for klass in school_SchoolYear.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_school_room_is_not_abstract():
    assert not inspect.isabstract(school_Room)


def test_school_room_constructor_exists():
    assert callable(school_Room.__init__)


def test_school_room_constructor_args():
    sig = inspect.signature(school_Room.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_school_room_has_location():
    assert hasattr(school_Room, "location")
    descriptor = None
    for klass in school_Room.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_school_classlevel_is_not_abstract():
    assert not inspect.isabstract(school_ClassLevel)


def test_school_classlevel_constructor_exists():
    assert callable(school_ClassLevel.__init__)


def test_school_classlevel_constructor_args():
    sig = inspect.signature(school_ClassLevel.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_school_classlevel_has_level():
    assert hasattr(school_ClassLevel, "level")
    descriptor = None
    for klass in school_ClassLevel.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_school_teacher_is_not_abstract():
    assert not inspect.isabstract(school_Teacher)


def test_school_teacher_constructor_exists():
    assert callable(school_Teacher.__init__)


def test_school_teacher_constructor_args():
    sig = inspect.signature(school_Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_teacher_has_name():
    assert hasattr(school_Teacher, "name")
    descriptor = None
    for klass in school_Teacher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_student_is_not_abstract():
    assert not inspect.isabstract(school_Student)


def test_school_student_constructor_exists():
    assert callable(school_Student.__init__)


def test_school_student_constructor_args():
    sig = inspect.signature(school_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_student_has_name():
    assert hasattr(school_Student, "name")
    descriptor = None
    for klass in school_Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_school_classgroup_is_not_abstract():
    assert not inspect.isabstract(school_ClassGroup)


def test_school_classgroup_constructor_exists():
    assert callable(school_ClassGroup.__init__)


def test_school_classgroup_constructor_args():
    sig = inspect.signature(school_ClassGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_school_classgroup_has_name():
    assert hasattr(school_ClassGroup, "name")
    descriptor = None
    for klass in school_ClassGroup.__mro__:
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
school_store_strategy = st.builds(
    school_store,
    lastIn=
        safe_text
)
school_NewEClass7_strategy = st.builds(
    school_NewEClass7,
)
school_SchoolYear_strategy = st.builds(
    school_SchoolYear,
    year=
        st.dates()
)
school_Room_strategy = st.builds(
    school_Room,
    location=
        safe_text
)
school_ClassLevel_strategy = st.builds(
    school_ClassLevel,
    level=
        st.integers()
)
school_Teacher_strategy = st.builds(
    school_Teacher,
    name=
        safe_text
)
school_Student_strategy = st.builds(
    school_Student,
    name=
        safe_text
)
school_ClassGroup_strategy = st.builds(
    school_ClassGroup,
    name=
        safe_text
)

@given(instance=school_store_strategy)
@settings(max_examples=50)
def test_school_store_instantiation(instance):
    assert isinstance(instance, school_store)



@given(instance=school_store_strategy)
def test_school_store_lastIn_setter(instance):
    original = instance.lastIn
    instance.lastIn = original
    assert instance.lastIn == original

@given(instance=school_NewEClass7_strategy)
@settings(max_examples=50)
def test_school_neweclass7_instantiation(instance):
    assert isinstance(instance, school_NewEClass7)

@given(instance=school_SchoolYear_strategy)
@settings(max_examples=50)
def test_school_schoolyear_instantiation(instance):
    assert isinstance(instance, school_SchoolYear)



@given(instance=school_SchoolYear_strategy)
def test_school_schoolyear_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=school_Room_strategy)
@settings(max_examples=50)
def test_school_room_instantiation(instance):
    assert isinstance(instance, school_Room)



@given(instance=school_Room_strategy)
def test_school_room_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=school_Room_strategy)
@settings(max_examples=30)
def test_school_room_affectteacher_changes_state(instance):
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
        assert has_statements, f"Function 'AffectTeacher' in school_Room is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AffectTeacher' in school_Room did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AffectTeacher' in school_Room is not implemented or raised an error")

@given(instance=school_ClassLevel_strategy)
@settings(max_examples=50)
def test_school_classlevel_instantiation(instance):
    assert isinstance(instance, school_ClassLevel)



@given(instance=school_ClassLevel_strategy)
def test_school_classlevel_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=school_Teacher_strategy)
@settings(max_examples=50)
def test_school_teacher_instantiation(instance):
    assert isinstance(instance, school_Teacher)



@given(instance=school_Teacher_strategy)
def test_school_teacher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_Student_strategy)
@settings(max_examples=50)
def test_school_student_instantiation(instance):
    assert isinstance(instance, school_Student)



@given(instance=school_Student_strategy)
def test_school_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=school_ClassGroup_strategy)
@settings(max_examples=50)
def test_school_classgroup_instantiation(instance):
    assert isinstance(instance, school_ClassGroup)



@given(instance=school_ClassGroup_strategy)
def test_school_classgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
