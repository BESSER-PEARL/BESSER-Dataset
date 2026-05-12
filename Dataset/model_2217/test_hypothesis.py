import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ntnustudies_StudyPlan,
    ntnustudies_Department,
    ntnustudies_ChosenSemester,
    ntnustudies_Semester,
    ntnustudies_Specialization,
    ntnustudies_Programme,
    ntnustudies_Course,
    semesterType,
    courseLevel,
    courseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ntnustudies_studyplan_is_not_abstract():
    assert not inspect.isabstract(ntnustudies_StudyPlan)


def test_ntnustudies_studyplan_constructor_exists():
    assert callable(ntnustudies_StudyPlan.__init__)


def test_ntnustudies_studyplan_constructor_args():
    sig = inspect.signature(ntnustudies_StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_ntnustudies_department_is_not_abstract():
    assert not inspect.isabstract(ntnustudies_Department)


def test_ntnustudies_department_constructor_exists():
    assert callable(ntnustudies_Department.__init__)


def test_ntnustudies_department_constructor_args():
    sig = inspect.signature(ntnustudies_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shortName" in params, "Missing parameter 'shortName'"

def test_ntnustudies_department_has_name():
    assert hasattr(ntnustudies_Department, "name")
    descriptor = None
    for klass in ntnustudies_Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_department_has_shortName():
    assert hasattr(ntnustudies_Department, "shortName")
    descriptor = None
    for klass in ntnustudies_Department.__mro__:
        if "shortName" in klass.__dict__:
            descriptor = klass.__dict__["shortName"]
            break
    assert isinstance(descriptor, property)



def test_ntnustudies_chosensemester_is_not_abstract():
    assert not inspect.isabstract(ntnustudies_ChosenSemester)


def test_ntnustudies_chosensemester_constructor_exists():
    assert callable(ntnustudies_ChosenSemester.__init__)


def test_ntnustudies_chosensemester_constructor_args():
    sig = inspect.signature(ntnustudies_ChosenSemester.__init__)
    params = list(sig.parameters.keys())



def test_ntnustudies_semester_is_not_abstract():
    assert not inspect.isabstract(ntnustudies_Semester)


def test_ntnustudies_semester_constructor_exists():
    assert callable(ntnustudies_Semester.__init__)


def test_ntnustudies_semester_constructor_args():
    sig = inspect.signature(ntnustudies_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "type" in params, "Missing parameter 'type'"

def test_ntnustudies_semester_has_year():
    assert hasattr(ntnustudies_Semester, "year")
    descriptor = None
    for klass in ntnustudies_Semester.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_semester_has_type():
    assert hasattr(ntnustudies_Semester, "type")
    descriptor = None
    for klass in ntnustudies_Semester.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ntnustudies_specialization_is_not_abstract():
    assert not inspect.isabstract(ntnustudies_Specialization)


def test_ntnustudies_specialization_constructor_exists():
    assert callable(ntnustudies_Specialization.__init__)


def test_ntnustudies_specialization_constructor_args():
    sig = inspect.signature(ntnustudies_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "specializationChoicePointSemester" in params, "Missing parameter 'specializationChoicePointSemester'"

def test_ntnustudies_specialization_has_name():
    assert hasattr(ntnustudies_Specialization, "name")
    descriptor = None
    for klass in ntnustudies_Specialization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_specialization_has_specializationChoicePointSemester():
    assert hasattr(ntnustudies_Specialization, "specializationChoicePointSemester")
    descriptor = None
    for klass in ntnustudies_Specialization.__mro__:
        if "specializationChoicePointSemester" in klass.__dict__:
            descriptor = klass.__dict__["specializationChoicePointSemester"]
            break
    assert isinstance(descriptor, property)



def test_ntnustudies_programme_is_not_abstract():
    assert not inspect.isabstract(ntnustudies_Programme)


def test_ntnustudies_programme_constructor_exists():
    assert callable(ntnustudies_Programme.__init__)


def test_ntnustudies_programme_constructor_args():
    sig = inspect.signature(ntnustudies_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "years" in params, "Missing parameter 'years'"
    assert "name" in params, "Missing parameter 'name'"

def test_ntnustudies_programme_has_years():
    assert hasattr(ntnustudies_Programme, "years")
    descriptor = None
    for klass in ntnustudies_Programme.__mro__:
        if "years" in klass.__dict__:
            descriptor = klass.__dict__["years"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_programme_has_name():
    assert hasattr(ntnustudies_Programme, "name")
    descriptor = None
    for klass in ntnustudies_Programme.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ntnustudies_course_is_not_abstract():
    assert not inspect.isabstract(ntnustudies_Course)


def test_ntnustudies_course_constructor_exists():
    assert callable(ntnustudies_Course.__init__)


def test_ntnustudies_course_constructor_args():
    sig = inspect.signature(ntnustudies_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "semesters" in params, "Missing parameter 'semesters'"
    assert "credtis" in params, "Missing parameter 'credtis'"
    assert "type" in params, "Missing parameter 'type'"
    assert "level" in params, "Missing parameter 'level'"

def test_ntnustudies_course_has_code():
    assert hasattr(ntnustudies_Course, "code")
    descriptor = None
    for klass in ntnustudies_Course.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_course_has_name():
    assert hasattr(ntnustudies_Course, "name")
    descriptor = None
    for klass in ntnustudies_Course.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_course_has_semesters():
    assert hasattr(ntnustudies_Course, "semesters")
    descriptor = None
    for klass in ntnustudies_Course.__mro__:
        if "semesters" in klass.__dict__:
            descriptor = klass.__dict__["semesters"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_course_has_credtis():
    assert hasattr(ntnustudies_Course, "credtis")
    descriptor = None
    for klass in ntnustudies_Course.__mro__:
        if "credtis" in klass.__dict__:
            descriptor = klass.__dict__["credtis"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_course_has_type():
    assert hasattr(ntnustudies_Course, "type")
    descriptor = None
    for klass in ntnustudies_Course.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ntnustudies_course_has_level():
    assert hasattr(ntnustudies_Course, "level")
    descriptor = None
    for klass in ntnustudies_Course.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
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
        "high",
        "basic",
        "medium",
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
ntnustudies_StudyPlan_strategy = st.builds(
    ntnustudies_StudyPlan,
)
ntnustudies_Department_strategy = st.builds(
    ntnustudies_Department,
    name=
        safe_text,
    shortName=
        safe_text
)
ntnustudies_ChosenSemester_strategy = st.builds(
    ntnustudies_ChosenSemester,
)
ntnustudies_Semester_strategy = st.builds(
    ntnustudies_Semester,
    year=
        st.integers(),
    type=
        safe_text
)
ntnustudies_Specialization_strategy = st.builds(
    ntnustudies_Specialization,
    name=
        safe_text,
    specializationChoicePointSemester=
        st.integers()
)
ntnustudies_Programme_strategy = st.builds(
    ntnustudies_Programme,
    years=
        st.integers(),
    name=
        safe_text
)
ntnustudies_Course_strategy = st.builds(
    ntnustudies_Course,
    code=
        safe_text,
    name=
        safe_text,
    semesters=
        safe_text,
    credtis=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text,
    level=
        safe_text
)

@given(instance=ntnustudies_StudyPlan_strategy)
@settings(max_examples=50)
def test_ntnustudies_studyplan_instantiation(instance):
    assert isinstance(instance, ntnustudies_StudyPlan)

@given(instance=ntnustudies_Department_strategy)
@settings(max_examples=50)
def test_ntnustudies_department_instantiation(instance):
    assert isinstance(instance, ntnustudies_Department)



@given(instance=ntnustudies_Department_strategy)
def test_ntnustudies_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ntnustudies_Department_strategy)
def test_ntnustudies_department_shortName_setter(instance):
    original = instance.shortName
    instance.shortName = original
    assert instance.shortName == original

@given(instance=ntnustudies_ChosenSemester_strategy)
@settings(max_examples=50)
def test_ntnustudies_chosensemester_instantiation(instance):
    assert isinstance(instance, ntnustudies_ChosenSemester)

@given(instance=ntnustudies_Semester_strategy)
@settings(max_examples=50)
def test_ntnustudies_semester_instantiation(instance):
    assert isinstance(instance, ntnustudies_Semester)



@given(instance=ntnustudies_Semester_strategy)
def test_ntnustudies_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=ntnustudies_Semester_strategy)
def test_ntnustudies_semester_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ntnustudies_Specialization_strategy)
@settings(max_examples=50)
def test_ntnustudies_specialization_instantiation(instance):
    assert isinstance(instance, ntnustudies_Specialization)



@given(instance=ntnustudies_Specialization_strategy)
def test_ntnustudies_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ntnustudies_Specialization_strategy)
def test_ntnustudies_specialization_specializationChoicePointSemester_setter(instance):
    original = instance.specializationChoicePointSemester
    instance.specializationChoicePointSemester = original
    assert instance.specializationChoicePointSemester == original

@given(instance=ntnustudies_Programme_strategy)
@settings(max_examples=50)
def test_ntnustudies_programme_instantiation(instance):
    assert isinstance(instance, ntnustudies_Programme)



@given(instance=ntnustudies_Programme_strategy)
def test_ntnustudies_programme_years_setter(instance):
    original = instance.years
    instance.years = original
    assert instance.years == original



@given(instance=ntnustudies_Programme_strategy)
def test_ntnustudies_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ntnustudies_Course_strategy)
@settings(max_examples=50)
def test_ntnustudies_course_instantiation(instance):
    assert isinstance(instance, ntnustudies_Course)



@given(instance=ntnustudies_Course_strategy)
def test_ntnustudies_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=ntnustudies_Course_strategy)
def test_ntnustudies_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ntnustudies_Course_strategy)
def test_ntnustudies_course_semesters_setter(instance):
    original = instance.semesters
    instance.semesters = original
    assert instance.semesters == original



@given(instance=ntnustudies_Course_strategy)
def test_ntnustudies_course_credtis_setter(instance):
    original = instance.credtis
    instance.credtis = original
    assert instance.credtis == original



@given(instance=ntnustudies_Course_strategy)
def test_ntnustudies_course_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ntnustudies_Course_strategy)
def test_ntnustudies_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original
