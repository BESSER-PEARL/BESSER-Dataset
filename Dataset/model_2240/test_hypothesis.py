import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::CourseAllocation,
    model::Semester,
    model::Role,
    model::Course,
    model::Person,
    model::Department,
    model::CourseInstance,
    SemesterKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::courseallocation_is_not_abstract():
    assert not inspect.isabstract(model::CourseAllocation)


def test_model::courseallocation_constructor_exists():
    assert callable(model::CourseAllocation.__init__)


def test_model::courseallocation_constructor_args():
    sig = inspect.signature(model::CourseAllocation.__init__)
    params = list(sig.parameters.keys())
    assert "factor" in params, "Missing parameter 'factor'"
    assert "explicitFactor" in params, "Missing parameter 'explicitFactor'"

def test_model::courseallocation_has_factor():
    assert hasattr(model::CourseAllocation, "factor")
    descriptor = None
    for klass in model::CourseAllocation.__mro__:
        if "factor" in klass.__dict__:
            descriptor = klass.__dict__["factor"]
            break
    assert isinstance(descriptor, property)

def test_model::courseallocation_has_explicitFactor():
    assert hasattr(model::CourseAllocation, "explicitFactor")
    descriptor = None
    for klass in model::CourseAllocation.__mro__:
        if "explicitFactor" in klass.__dict__:
            descriptor = klass.__dict__["explicitFactor"]
            break
    assert isinstance(descriptor, property)



def test_model::semester_is_not_abstract():
    assert not inspect.isabstract(model::Semester)


def test_model::semester_constructor_exists():
    assert callable(model::Semester.__init__)


def test_model::semester_constructor_args():
    sig = inspect.signature(model::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_model::semester_has_year():
    assert hasattr(model::Semester, "year")
    descriptor = None
    for klass in model::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_model::semester_has_kind():
    assert hasattr(model::Semester, "kind")
    descriptor = None
    for klass in model::Semester.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_model::role_is_not_abstract():
    assert not inspect.isabstract(model::Role)


def test_model::role_constructor_exists():
    assert callable(model::Role.__init__)


def test_model::role_constructor_args():
    sig = inspect.signature(model::Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "factor" in params, "Missing parameter 'factor'"

def test_model::role_has_name():
    assert hasattr(model::Role, "name")
    descriptor = None
    for klass in model::Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::role_has_factor():
    assert hasattr(model::Role, "factor")
    descriptor = None
    for klass in model::Role.__mro__:
        if "factor" in klass.__dict__:
            descriptor = klass.__dict__["factor"]
            break
    assert isinstance(descriptor, property)



def test_model::course_is_not_abstract():
    assert not inspect.isabstract(model::Course)


def test_model::course_constructor_exists():
    assert callable(model::Course.__init__)


def test_model::course_constructor_args():
    sig = inspect.signature(model::Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_model::course_has_name():
    assert hasattr(model::Course, "name")
    descriptor = None
    for klass in model::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::course_has_fullName():
    assert hasattr(model::Course, "fullName")
    descriptor = None
    for klass in model::Course.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_model::person_is_not_abstract():
    assert not inspect.isabstract(model::Person)


def test_model::person_constructor_exists():
    assert callable(model::Person.__init__)


def test_model::person_constructor_args():
    sig = inspect.signature(model::Person.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "faceUrl" in params, "Missing parameter 'faceUrl'"
    assert "name" in params, "Missing parameter 'name'"
    assert "employmentFactor" in params, "Missing parameter 'employmentFactor'"

def test_model::person_has_email():
    assert hasattr(model::Person, "email")
    descriptor = None
    for klass in model::Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_model::person_has_userName():
    assert hasattr(model::Person, "userName")
    descriptor = None
    for klass in model::Person.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_model::person_has_faceUrl():
    assert hasattr(model::Person, "faceUrl")
    descriptor = None
    for klass in model::Person.__mro__:
        if "faceUrl" in klass.__dict__:
            descriptor = klass.__dict__["faceUrl"]
            break
    assert isinstance(descriptor, property)

def test_model::person_has_name():
    assert hasattr(model::Person, "name")
    descriptor = None
    for klass in model::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::person_has_employmentFactor():
    assert hasattr(model::Person, "employmentFactor")
    descriptor = None
    for klass in model::Person.__mro__:
        if "employmentFactor" in klass.__dict__:
            descriptor = klass.__dict__["employmentFactor"]
            break
    assert isinstance(descriptor, property)



def test_model::department_is_not_abstract():
    assert not inspect.isabstract(model::Department)


def test_model::department_constructor_exists():
    assert callable(model::Department.__init__)


def test_model::department_constructor_args():
    sig = inspect.signature(model::Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::department_has_name():
    assert hasattr(model::Department, "name")
    descriptor = None
    for klass in model::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::courseinstance_is_not_abstract():
    assert not inspect.isabstract(model::CourseInstance)


def test_model::courseinstance_constructor_exists():
    assert callable(model::CourseInstance.__init__)


def test_model::courseinstance_constructor_args():
    sig = inspect.signature(model::CourseInstance.__init__)
    params = list(sig.parameters.keys())

def test_semesterkind_exists():
    # Check that the Enumeration exists
    assert SemesterKind is not None

def test_semesterkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterKind]
    expected_literals = [
        "SPRING",
        "AUTUMN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SemesterKind"


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
model::CourseAllocation_strategy = st.builds(
    model::CourseAllocation,
    factor=
        safe_text,
    explicitFactor=
        safe_text
)
model::Semester_strategy = st.builds(
    model::Semester,
    year=
        safe_text,
    kind=
        safe_text
)
model::Role_strategy = st.builds(
    model::Role,
    name=
        safe_text,
    factor=
        safe_text
)
model::Course_strategy = st.builds(
    model::Course,
    name=
        safe_text,
    fullName=
        safe_text
)
model::Person_strategy = st.builds(
    model::Person,
    email=
        safe_text,
    userName=
        safe_text,
    faceUrl=
        safe_text,
    name=
        safe_text,
    employmentFactor=
        safe_text
)
model::Department_strategy = st.builds(
    model::Department,
    name=
        safe_text
)
model::CourseInstance_strategy = st.builds(
    model::CourseInstance,
)

@given(instance=model::CourseAllocation_strategy)
@settings(max_examples=50)
def test_model::courseallocation_instantiation(instance):
    assert isinstance(instance, model::CourseAllocation)

@given(instance=model::CourseAllocation_strategy)
def test_model::courseallocation_factor_type(instance):
    assert isinstance(instance.factor, str)


@given(instance=model::CourseAllocation_strategy)
def test_model::courseallocation_factor_setter(instance):
    original = instance.factor
    instance.factor = original
    assert instance.factor == original

@given(instance=model::CourseAllocation_strategy)
def test_model::courseallocation_explicitFactor_type(instance):
    assert isinstance(instance.explicitFactor, str)


@given(instance=model::CourseAllocation_strategy)
def test_model::courseallocation_explicitFactor_setter(instance):
    original = instance.explicitFactor
    instance.explicitFactor = original
    assert instance.explicitFactor == original

@given(instance=model::Semester_strategy)
@settings(max_examples=50)
def test_model::semester_instantiation(instance):
    assert isinstance(instance, model::Semester)

@given(instance=model::Semester_strategy)
def test_model::semester_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=model::Semester_strategy)
def test_model::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=model::Semester_strategy)
def test_model::semester_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=model::Semester_strategy)
def test_model::semester_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=model::Role_strategy)
@settings(max_examples=50)
def test_model::role_instantiation(instance):
    assert isinstance(instance, model::Role)

@given(instance=model::Role_strategy)
def test_model::role_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Role_strategy)
def test_model::role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Role_strategy)
def test_model::role_factor_type(instance):
    assert isinstance(instance.factor, str)


@given(instance=model::Role_strategy)
def test_model::role_factor_setter(instance):
    original = instance.factor
    instance.factor = original
    assert instance.factor == original

@given(instance=model::Course_strategy)
@settings(max_examples=50)
def test_model::course_instantiation(instance):
    assert isinstance(instance, model::Course)

@given(instance=model::Course_strategy)
def test_model::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Course_strategy)
def test_model::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Course_strategy)
def test_model::course_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=model::Course_strategy)
def test_model::course_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=model::Person_strategy)
@settings(max_examples=50)
def test_model::person_instantiation(instance):
    assert isinstance(instance, model::Person)

@given(instance=model::Person_strategy)
def test_model::person_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=model::Person_strategy)
def test_model::person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=model::Person_strategy)
def test_model::person_userName_type(instance):
    assert isinstance(instance.userName, str)


@given(instance=model::Person_strategy)
def test_model::person_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original

@given(instance=model::Person_strategy)
def test_model::person_faceUrl_type(instance):
    assert isinstance(instance.faceUrl, str)


@given(instance=model::Person_strategy)
def test_model::person_faceUrl_setter(instance):
    original = instance.faceUrl
    instance.faceUrl = original
    assert instance.faceUrl == original

@given(instance=model::Person_strategy)
def test_model::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Person_strategy)
def test_model::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Person_strategy)
def test_model::person_employmentFactor_type(instance):
    assert isinstance(instance.employmentFactor, str)


@given(instance=model::Person_strategy)
def test_model::person_employmentFactor_setter(instance):
    original = instance.employmentFactor
    instance.employmentFactor = original
    assert instance.employmentFactor == original

@given(instance=model::Department_strategy)
@settings(max_examples=50)
def test_model::department_instantiation(instance):
    assert isinstance(instance, model::Department)

@given(instance=model::Department_strategy)
def test_model::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Department_strategy)
def test_model::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::CourseInstance_strategy)
@settings(max_examples=50)
def test_model::courseinstance_instantiation(instance):
    assert isinstance(instance, model::CourseInstance)
