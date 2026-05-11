import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ntnustudies::StudyPlan,
    ntnustudies::Department,
    ntnustudies::ChosenSemester,
    ntnustudies::Semester,
    ntnustudies::Specialization,
    ntnustudies::Programme,
    ntnustudies::Course,
    semesterType,
    courseLevel,
    courseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ntnustudies::studyplan_is_not_abstract():
    assert not inspect.isabstract(ntnustudies::StudyPlan)


def test_ntnustudies::studyplan_constructor_exists():
    assert callable(ntnustudies::StudyPlan.__init__)


def test_ntnustudies::studyplan_constructor_args():
    sig = inspect.signature(ntnustudies::StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_ntnustudies::department_is_not_abstract():
    assert not inspect.isabstract(ntnustudies::Department)


def test_ntnustudies::department_constructor_exists():
    assert callable(ntnustudies::Department.__init__)


def test_ntnustudies::department_constructor_args():
    sig = inspect.signature(ntnustudies::Department.__init__)
    params = list(sig.parameters.keys())
    assert "shortName" in params, "Missing parameter 'shortName'"
    assert "name" in params, "Missing parameter 'name'"

def test_ntnustudies::department_has_shortName():
    assert hasattr(ntnustudies::Department, "shortName")
    descriptor = None
    for klass in ntnustudies::Department.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::department_has_name():
    assert hasattr(ntnustudies::Department, "name")
    descriptor = None
    for klass in ntnustudies::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ntnustudies::chosensemester_is_not_abstract():
    assert not inspect.isabstract(ntnustudies::ChosenSemester)


def test_ntnustudies::chosensemester_constructor_exists():
    assert callable(ntnustudies::ChosenSemester.__init__)


def test_ntnustudies::chosensemester_constructor_args():
    sig = inspect.signature(ntnustudies::ChosenSemester.__init__)
    params = list(sig.parameters.keys())



def test_ntnustudies::semester_is_not_abstract():
    assert not inspect.isabstract(ntnustudies::Semester)


def test_ntnustudies::semester_constructor_exists():
    assert callable(ntnustudies::Semester.__init__)


def test_ntnustudies::semester_constructor_args():
    sig = inspect.signature(ntnustudies::Semester.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "year" in params, "Missing parameter 'year'"

def test_ntnustudies::semester_has_type():
    assert hasattr(ntnustudies::Semester, "type")
    descriptor = None
    for klass in ntnustudies::Semester.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::semester_has_year():
    assert hasattr(ntnustudies::Semester, "year")
    descriptor = None
    for klass in ntnustudies::Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_ntnustudies::specialization_is_not_abstract():
    assert not inspect.isabstract(ntnustudies::Specialization)


def test_ntnustudies::specialization_constructor_exists():
    assert callable(ntnustudies::Specialization.__init__)


def test_ntnustudies::specialization_constructor_args():
    sig = inspect.signature(ntnustudies::Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "specializationChoicePointSemester" in params, "Missing parameter 'specializationChoicePointSemester'"
    assert "name" in params, "Missing parameter 'name'"

def test_ntnustudies::specialization_has_specializationChoicePointSemester():
    assert hasattr(ntnustudies::Specialization, "specializationChoicePointSemester")
    descriptor = None
    for klass in ntnustudies::Specialization.__mro__:
        if "specializationChoicePointSemester" in klass.__dict__:
            descriptor = klass.__dict__["specializationChoicePointSemester"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::specialization_has_name():
    assert hasattr(ntnustudies::Specialization, "name")
    descriptor = None
    for klass in ntnustudies::Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ntnustudies::programme_is_not_abstract():
    assert not inspect.isabstract(ntnustudies::Programme)


def test_ntnustudies::programme_constructor_exists():
    assert callable(ntnustudies::Programme.__init__)


def test_ntnustudies::programme_constructor_args():
    sig = inspect.signature(ntnustudies::Programme.__init__)
    params = list(sig.parameters.keys())
    assert "years" in params, "Missing parameter 'years'"
    assert "name" in params, "Missing parameter 'name'"

def test_ntnustudies::programme_has_years():
    assert hasattr(ntnustudies::Programme, "years")
    descriptor = None
    for klass in ntnustudies::Programme.__mro__:
        if "years" in klass.__dict__:
            descriptor = klass.__dict__["years"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::programme_has_name():
    assert hasattr(ntnustudies::Programme, "name")
    descriptor = None
    for klass in ntnustudies::Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ntnustudies::course_is_not_abstract():
    assert not inspect.isabstract(ntnustudies::Course)


def test_ntnustudies::course_constructor_exists():
    assert callable(ntnustudies::Course.__init__)


def test_ntnustudies::course_constructor_args():
    sig = inspect.signature(ntnustudies::Course.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "code" in params, "Missing parameter 'code'"
    assert "semesters" in params, "Missing parameter 'semesters'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "credtis" in params, "Missing parameter 'credtis'"

def test_ntnustudies::course_has_level():
    assert hasattr(ntnustudies::Course, "level")
    descriptor = None
    for klass in ntnustudies::Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::course_has_code():
    assert hasattr(ntnustudies::Course, "code")
    descriptor = None
    for klass in ntnustudies::Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::course_has_semesters():
    assert hasattr(ntnustudies::Course, "semesters")
    descriptor = None
    for klass in ntnustudies::Course.__mro__:
        if "semesters" in klass.__dict__:
            descriptor = klass.__dict__["semesters"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::course_has_name():
    assert hasattr(ntnustudies::Course, "name")
    descriptor = None
    for klass in ntnustudies::Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::course_has_type():
    assert hasattr(ntnustudies::Course, "type")
    descriptor = None
    for klass in ntnustudies::Course.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies::course_has_credtis():
    assert hasattr(ntnustudies::Course, "credtis")
    descriptor = None
    for klass in ntnustudies::Course.__mro__:
        if "credtis" in klass.__dict__:
            descriptor = klass.__dict__["credtis"]
            break
    assert isinstance(descriptor, property)

def test_semestertype_exists():
    # Check that the Enumeration exists
    assert semesterType is not None

def test_semestertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in semesterType]
    expected_literals = [
        "fall",
        "spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in semesterType"

def test_courselevel_exists():
    # Check that the Enumeration exists
    assert courseLevel is not None

def test_courselevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in courseLevel]
    expected_literals = [
        "medium",
        "high",
        "basic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in courseLevel"

def test_coursetype_exists():
    # Check that the Enumeration exists
    assert courseType is not None

def test_coursetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in courseType]
    expected_literals = [
        "elective",
        "mandatory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in courseType"


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
ntnustudies::StudyPlan_strategy = st.builds(
    ntnustudies::StudyPlan,
)
ntnustudies::Department_strategy = st.builds(
    ntnustudies::Department,
    shortName=
        safe_text,
    name=
        safe_text
)
ntnustudies::ChosenSemester_strategy = st.builds(
    ntnustudies::ChosenSemester,
)
ntnustudies::Semester_strategy = st.builds(
    ntnustudies::Semester,
    type=
        safe_text,
    year=
        st.integers()
)
ntnustudies::Specialization_strategy = st.builds(
    ntnustudies::Specialization,
    specializationChoicePointSemester=
        st.integers(),
    name=
        safe_text
)
ntnustudies::Programme_strategy = st.builds(
    ntnustudies::Programme,
    years=
        st.integers(),
    name=
        safe_text
)
ntnustudies::Course_strategy = st.builds(
    ntnustudies::Course,
    level=
        safe_text,
    code=
        safe_text,
    semesters=
        safe_text,
    name=
        safe_text,
    type=
        safe_text,
    credtis=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=ntnustudies::StudyPlan_strategy)
@settings(max_examples=50)
def test_ntnustudies::studyplan_instantiation(instance):
    assert isinstance(instance, ntnustudies::StudyPlan)

@given(instance=ntnustudies::Department_strategy)
@settings(max_examples=50)
def test_ntnustudies::department_instantiation(instance):
    assert isinstance(instance, ntnustudies::Department)

@given(instance=ntnustudies::Department_strategy)
def test_ntnustudies::department_shortName_type(instance):
    assert isinstance(instance.shortName, str)


@given(instance=ntnustudies::Department_strategy)
def test_ntnustudies::department_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=ntnustudies::Department_strategy)
def test_ntnustudies::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ntnustudies::Department_strategy)
def test_ntnustudies::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ntnustudies::ChosenSemester_strategy)
@settings(max_examples=50)
def test_ntnustudies::chosensemester_instantiation(instance):
    assert isinstance(instance, ntnustudies::ChosenSemester)

@given(instance=ntnustudies::Semester_strategy)
@settings(max_examples=50)
def test_ntnustudies::semester_instantiation(instance):
    assert isinstance(instance, ntnustudies::Semester)

@given(instance=ntnustudies::Semester_strategy)
def test_ntnustudies::semester_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ntnustudies::Semester_strategy)
def test_ntnustudies::semester_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ntnustudies::Semester_strategy)
def test_ntnustudies::semester_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=ntnustudies::Semester_strategy)
def test_ntnustudies::semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=ntnustudies::Specialization_strategy)
@settings(max_examples=50)
def test_ntnustudies::specialization_instantiation(instance):
    assert isinstance(instance, ntnustudies::Specialization)

@given(instance=ntnustudies::Specialization_strategy)
def test_ntnustudies::specialization_specializationChoicePointSemester_type(instance):
    assert isinstance(instance.specializationChoicePointSemester, int)


@given(instance=ntnustudies::Specialization_strategy)
def test_ntnustudies::specialization_specializationChoicePointSemester_setter(instance):
    original = instance.specializationChoicePointSemester
    instance.specializationChoicePointSemester = original
    assert instance.specializationChoicePointSemester == original

@given(instance=ntnustudies::Specialization_strategy)
def test_ntnustudies::specialization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ntnustudies::Specialization_strategy)
def test_ntnustudies::specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ntnustudies::Programme_strategy)
@settings(max_examples=50)
def test_ntnustudies::programme_instantiation(instance):
    assert isinstance(instance, ntnustudies::Programme)

@given(instance=ntnustudies::Programme_strategy)
def test_ntnustudies::programme_years_type(instance):
    assert isinstance(instance.years, int)


@given(instance=ntnustudies::Programme_strategy)
def test_ntnustudies::programme_years_setter(instance):
    original = instance.years
    instance.years = original
    assert instance.years == original

@given(instance=ntnustudies::Programme_strategy)
def test_ntnustudies::programme_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ntnustudies::Programme_strategy)
def test_ntnustudies::programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ntnustudies::Course_strategy)
@settings(max_examples=50)
def test_ntnustudies::course_instantiation(instance):
    assert isinstance(instance, ntnustudies::Course)

@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_semesters_type(instance):
    assert isinstance(instance.semesters, str)


@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_semesters_setter(instance):
    original = instance.semesters
    instance.semesters = original
    assert instance.semesters == original

@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_credtis_type(instance):
    assert isinstance(instance.credtis, float)


@given(instance=ntnustudies::Course_strategy)
def test_ntnustudies::course_credtis_setter(instance):
    original = instance.credtis
    instance.credtis = original
    assert instance.credtis == original
