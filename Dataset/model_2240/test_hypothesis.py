import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_CourseAllocation,
    model_Semester,
    model_Role,
    model_Course,
    model_Person,
    model_Department,
    model_CourseInstance,
    SemesterKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_courseallocation_is_not_abstract():
    assert not inspect.isabstract(model_CourseAllocation)


def test_model_courseallocation_constructor_exists():
    assert callable(model_CourseAllocation.__init__)


def test_model_courseallocation_constructor_args():
    sig = inspect.signature(model_CourseAllocation.__init__)
    params = list(sig.parameters.keys())
    assert "factor" in params, "Missing parameter 'factor'"
    assert "explicitFactor" in params, "Missing parameter 'explicitFactor'"

def test_model_courseallocation_has_factor():
    assert hasattr(model_CourseAllocation, "factor")
    descriptor = None
    for klass in model_CourseAllocation.__mro__:
        if "factor" in klass.__dict__:
            descriptor = klass.__dict__["factor"]
            break
    assert isinstance(descriptor, property)

def test_model_courseallocation_has_explicitFactor():
    assert hasattr(model_CourseAllocation, "explicitFactor")
    descriptor = None
    for klass in model_CourseAllocation.__mro__:
        if "explicitFactor" in klass.__dict__:
            descriptor = klass.__dict__["explicitFactor"]
            break
    assert isinstance(descriptor, property)



def test_model_semester_is_not_abstract():
    assert not inspect.isabstract(model_Semester)


def test_model_semester_constructor_exists():
    assert callable(model_Semester.__init__)


def test_model_semester_constructor_args():
    sig = inspect.signature(model_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_model_semester_has_year():
    assert hasattr(model_Semester, "year")
    descriptor = None
    for klass in model_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_model_semester_has_kind():
    assert hasattr(model_Semester, "kind")
    descriptor = None
    for klass in model_Semester.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_model_role_is_not_abstract():
    assert not inspect.isabstract(model_Role)


def test_model_role_constructor_exists():
    assert callable(model_Role.__init__)


def test_model_role_constructor_args():
    sig = inspect.signature(model_Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "factor" in params, "Missing parameter 'factor'"

def test_model_role_has_name():
    assert hasattr(model_Role, "name")
    descriptor = None
    for klass in model_Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_role_has_factor():
    assert hasattr(model_Role, "factor")
    descriptor = None
    for klass in model_Role.__mro__:
        if "factor" in klass.__dict__:
            descriptor = klass.__dict__["factor"]
            break
    assert isinstance(descriptor, property)



def test_model_course_is_not_abstract():
    assert not inspect.isabstract(model_Course)


def test_model_course_constructor_exists():
    assert callable(model_Course.__init__)


def test_model_course_constructor_args():
    sig = inspect.signature(model_Course.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_course_has_fullName():
    assert hasattr(model_Course, "fullName")
    descriptor = None
    for klass in model_Course.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)

def test_model_course_has_name():
    assert hasattr(model_Course, "name")
    descriptor = None
    for klass in model_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_person_is_not_abstract():
    assert not inspect.isabstract(model_Person)


def test_model_person_constructor_exists():
    assert callable(model_Person.__init__)


def test_model_person_constructor_args():
    sig = inspect.signature(model_Person.__init__)
    params = list(sig.parameters.keys())
    assert "faceUrl" in params, "Missing parameter 'faceUrl'"
    assert "name" in params, "Missing parameter 'name'"
    assert "employmentFactor" in params, "Missing parameter 'employmentFactor'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "email" in params, "Missing parameter 'email'"

def test_model_person_has_faceUrl():
    assert hasattr(model_Person, "faceUrl")
    descriptor = None
    for klass in model_Person.__mro__:
        if "faceUrl" in klass.__dict__:
            descriptor = klass.__dict__["faceUrl"]
            break
    assert isinstance(descriptor, property)

def test_model_person_has_name():
    assert hasattr(model_Person, "name")
    descriptor = None
    for klass in model_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_person_has_employmentFactor():
    assert hasattr(model_Person, "employmentFactor")
    descriptor = None
    for klass in model_Person.__mro__:
        if "employmentFactor" in klass.__dict__:
            descriptor = klass.__dict__["employmentFactor"]
            break
    assert isinstance(descriptor, property)

def test_model_person_has_userName():
    assert hasattr(model_Person, "userName")
    descriptor = None
    for klass in model_Person.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_model_person_has_email():
    assert hasattr(model_Person, "email")
    descriptor = None
    for klass in model_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_model_department_is_not_abstract():
    assert not inspect.isabstract(model_Department)


def test_model_department_constructor_exists():
    assert callable(model_Department.__init__)


def test_model_department_constructor_args():
    sig = inspect.signature(model_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_department_has_name():
    assert hasattr(model_Department, "name")
    descriptor = None
    for klass in model_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_courseinstance_is_not_abstract():
    assert not inspect.isabstract(model_CourseInstance)


def test_model_courseinstance_constructor_exists():
    assert callable(model_CourseInstance.__init__)


def test_model_courseinstance_constructor_args():
    sig = inspect.signature(model_CourseInstance.__init__)
    params = list(sig.parameters.keys())

def test_semesterkind_exists():
    # Check that the Enumeration exists
    assert SemesterKind is not None

def test_semesterkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SemesterKind]
    expected_literals = [
        "AUTUMN",
        "SPRING",
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
model_CourseAllocation_strategy = st.builds(
    model_CourseAllocation,
    factor=
        safe_text,
    explicitFactor=
        safe_text
)
model_Semester_strategy = st.builds(
    model_Semester,
    year=
        safe_text,
    kind=
        safe_text
)
model_Role_strategy = st.builds(
    model_Role,
    name=
        safe_text,
    factor=
        safe_text
)
model_Course_strategy = st.builds(
    model_Course,
    fullName=
        safe_text,
    name=
        safe_text
)
model_Person_strategy = st.builds(
    model_Person,
    faceUrl=
        safe_text,
    name=
        safe_text,
    employmentFactor=
        safe_text,
    userName=
        safe_text,
    email=
        safe_text
)
model_Department_strategy = st.builds(
    model_Department,
    name=
        safe_text
)
model_CourseInstance_strategy = st.builds(
    model_CourseInstance,
)

@given(instance=model_CourseAllocation_strategy)
@settings(max_examples=50)
def test_model_courseallocation_instantiation(instance):
    assert isinstance(instance, model_CourseAllocation)



@given(instance=model_CourseAllocation_strategy)
def test_model_courseallocation_factor_setter(instance):
    original = instance.factor
    instance.factor = original
    assert instance.factor == original



@given(instance=model_CourseAllocation_strategy)
def test_model_courseallocation_explicitFactor_setter(instance):
    original = instance.explicitFactor
    instance.explicitFactor = original
    assert instance.explicitFactor == original

@given(instance=model_Semester_strategy)
@settings(max_examples=50)
def test_model_semester_instantiation(instance):
    assert isinstance(instance, model_Semester)



@given(instance=model_Semester_strategy)
def test_model_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=model_Semester_strategy)
def test_model_semester_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=model_Role_strategy)
@settings(max_examples=50)
def test_model_role_instantiation(instance):
    assert isinstance(instance, model_Role)



@given(instance=model_Role_strategy)
def test_model_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Role_strategy)
def test_model_role_factor_setter(instance):
    original = instance.factor
    instance.factor = original
    assert instance.factor == original

@given(instance=model_Course_strategy)
@settings(max_examples=50)
def test_model_course_instantiation(instance):
    assert isinstance(instance, model_Course)



@given(instance=model_Course_strategy)
def test_model_course_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original



@given(instance=model_Course_strategy)
def test_model_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_Person_strategy)
@settings(max_examples=50)
def test_model_person_instantiation(instance):
    assert isinstance(instance, model_Person)



@given(instance=model_Person_strategy)
def test_model_person_faceUrl_setter(instance):
    original = instance.faceUrl
    instance.faceUrl = original
    assert instance.faceUrl == original



@given(instance=model_Person_strategy)
def test_model_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Person_strategy)
def test_model_person_employmentFactor_setter(instance):
    original = instance.employmentFactor
    instance.employmentFactor = original
    assert instance.employmentFactor == original



@given(instance=model_Person_strategy)
def test_model_person_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=model_Person_strategy)
def test_model_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=model_Department_strategy)
@settings(max_examples=50)
def test_model_department_instantiation(instance):
    assert isinstance(instance, model_Department)



@given(instance=model_Department_strategy)
def test_model_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_CourseInstance_strategy)
@settings(max_examples=50)
def test_model_courseinstance_instantiation(instance):
    assert isinstance(instance, model_CourseInstance)
