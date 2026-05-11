import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    courceList::Specialisation,
    courceList::StudyProgram,
    courceList::Student,
    courceList::CourceSpecification,
    courceList::StudyCourceRelation,
    courceList::Work,
    courceList::EvaluationForm,
    courceList::Exam,
    courceList::Professor,
    courceList::Cource,
    courceList::StudyGeneralization,
    courceList::Department,
    Semester,
    EducationLevel,
    Campus,
    EvaluationType,
    WorkForm,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_courcelist::specialisation_is_not_abstract():
    assert not inspect.isabstract(courceList::Specialisation)


def test_courcelist::specialisation_constructor_exists():
    assert callable(courceList::Specialisation.__init__)


def test_courcelist::specialisation_constructor_args():
    sig = inspect.signature(courceList::Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "startSemester" in params, "Missing parameter 'startSemester'"
    assert "name" in params, "Missing parameter 'name'"

def test_courcelist::specialisation_has_startSemester():
    assert hasattr(courceList::Specialisation, "startSemester")
    descriptor = None
    for klass in courceList::Specialisation.__mro__:
        if "startSemester" in klass.__dict__:
            descriptor = klass.__dict__["startSemester"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::specialisation_has_name():
    assert hasattr(courceList::Specialisation, "name")
    descriptor = None
    for klass in courceList::Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::studyprogram_is_not_abstract():
    assert not inspect.isabstract(courceList::StudyProgram)


def test_courcelist::studyprogram_constructor_exists():
    assert callable(courceList::StudyProgram.__init__)


def test_courcelist::studyprogram_constructor_args():
    sig = inspect.signature(courceList::StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_courcelist::studyprogram_has_year():
    assert hasattr(courceList::StudyProgram, "year")
    descriptor = None
    for klass in courceList::StudyProgram.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::student_is_not_abstract():
    assert not inspect.isabstract(courceList::Student)


def test_courcelist::student_constructor_exists():
    assert callable(courceList::Student.__init__)


def test_courcelist::student_constructor_args():
    sig = inspect.signature(courceList::Student.__init__)
    params = list(sig.parameters.keys())
    assert "nr" in params, "Missing parameter 'nr'"

def test_courcelist::student_has_nr():
    assert hasattr(courceList::Student, "nr")
    descriptor = None
    for klass in courceList::Student.__mro__:
        if "nr" in klass.__dict__:
            descriptor = klass.__dict__["nr"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::courcespecification_is_not_abstract():
    assert not inspect.isabstract(courceList::CourceSpecification)


def test_courcelist::courcespecification_constructor_exists():
    assert callable(courceList::CourceSpecification.__init__)


def test_courcelist::courcespecification_constructor_args():
    sig = inspect.signature(courceList::CourceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "language" in params, "Missing parameter 'language'"
    assert "name" in params, "Missing parameter 'name'"
    assert "semester" in params, "Missing parameter 'semester'"
    assert "specificationYear" in params, "Missing parameter 'specificationYear'"
    assert "version" in params, "Missing parameter 'version'"

def test_courcelist::courcespecification_has_credits():
    assert hasattr(courceList::CourceSpecification, "credits")
    descriptor = None
    for klass in courceList::CourceSpecification.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::courcespecification_has_language():
    assert hasattr(courceList::CourceSpecification, "language")
    descriptor = None
    for klass in courceList::CourceSpecification.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::courcespecification_has_name():
    assert hasattr(courceList::CourceSpecification, "name")
    descriptor = None
    for klass in courceList::CourceSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::courcespecification_has_semester():
    assert hasattr(courceList::CourceSpecification, "semester")
    descriptor = None
    for klass in courceList::CourceSpecification.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::courcespecification_has_specificationYear():
    assert hasattr(courceList::CourceSpecification, "specificationYear")
    descriptor = None
    for klass in courceList::CourceSpecification.__mro__:
        if "specificationYear" in klass.__dict__:
            descriptor = klass.__dict__["specificationYear"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::courcespecification_has_version():
    assert hasattr(courceList::CourceSpecification, "version")
    descriptor = None
    for klass in courceList::CourceSpecification.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::studycourcerelation_is_not_abstract():
    assert not inspect.isabstract(courceList::StudyCourceRelation)


def test_courcelist::studycourcerelation_constructor_exists():
    assert callable(courceList::StudyCourceRelation.__init__)


def test_courcelist::studycourcerelation_constructor_args():
    sig = inspect.signature(courceList::StudyCourceRelation.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "year" in params, "Missing parameter 'year'"

def test_courcelist::studycourcerelation_has_status():
    assert hasattr(courceList::StudyCourceRelation, "status")
    descriptor = None
    for klass in courceList::StudyCourceRelation.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::studycourcerelation_has_year():
    assert hasattr(courceList::StudyCourceRelation, "year")
    descriptor = None
    for klass in courceList::StudyCourceRelation.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::work_is_not_abstract():
    assert not inspect.isabstract(courceList::Work)


def test_courcelist::work_constructor_exists():
    assert callable(courceList::Work.__init__)


def test_courcelist::work_constructor_args():
    sig = inspect.signature(courceList::Work.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_courcelist::work_has_weight():
    assert hasattr(courceList::Work, "weight")
    descriptor = None
    for klass in courceList::Work.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::evaluationform_is_not_abstract():
    assert not inspect.isabstract(courceList::EvaluationForm)


def test_courcelist::evaluationform_constructor_exists():
    assert callable(courceList::EvaluationForm.__init__)


def test_courcelist::evaluationform_constructor_args():
    sig = inspect.signature(courceList::EvaluationForm.__init__)
    params = list(sig.parameters.keys())
    assert "evaluationType" in params, "Missing parameter 'evaluationType'"

def test_courcelist::evaluationform_has_evaluationType():
    assert hasattr(courceList::EvaluationForm, "evaluationType")
    descriptor = None
    for klass in courceList::EvaluationForm.__mro__:
        if "evaluationType" in klass.__dict__:
            descriptor = klass.__dict__["evaluationType"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::exam_is_not_abstract():
    assert not inspect.isabstract(courceList::Exam)


def test_courcelist::exam_constructor_exists():
    assert callable(courceList::Exam.__init__)


def test_courcelist::exam_constructor_args():
    sig = inspect.signature(courceList::Exam.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "lenght" in params, "Missing parameter 'lenght'"
    assert "date" in params, "Missing parameter 'date'"
    assert "form" in params, "Missing parameter 'form'"

def test_courcelist::exam_has_weight():
    assert hasattr(courceList::Exam, "weight")
    descriptor = None
    for klass in courceList::Exam.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::exam_has_lenght():
    assert hasattr(courceList::Exam, "lenght")
    descriptor = None
    for klass in courceList::Exam.__mro__:
        if "lenght" in klass.__dict__:
            descriptor = klass.__dict__["lenght"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::exam_has_date():
    assert hasattr(courceList::Exam, "date")
    descriptor = None
    for klass in courceList::Exam.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::exam_has_form():
    assert hasattr(courceList::Exam, "form")
    descriptor = None
    for klass in courceList::Exam.__mro__:
        if "form" in klass.__dict__:
            descriptor = klass.__dict__["form"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::professor_is_not_abstract():
    assert not inspect.isabstract(courceList::Professor)


def test_courcelist::professor_constructor_exists():
    assert callable(courceList::Professor.__init__)


def test_courcelist::professor_constructor_args():
    sig = inspect.signature(courceList::Professor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "title" in params, "Missing parameter 'title'"

def test_courcelist::professor_has_name():
    assert hasattr(courceList::Professor, "name")
    descriptor = None
    for klass in courceList::Professor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::professor_has_title():
    assert hasattr(courceList::Professor, "title")
    descriptor = None
    for klass in courceList::Professor.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::cource_is_not_abstract():
    assert not inspect.isabstract(courceList::Cource)


def test_courcelist::cource_constructor_exists():
    assert callable(courceList::Cource.__init__)


def test_courcelist::cource_constructor_args():
    sig = inspect.signature(courceList::Cource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "location" in params, "Missing parameter 'location'"
    assert "code" in params, "Missing parameter 'code'"

def test_courcelist::cource_has_name():
    assert hasattr(courceList::Cource, "name")
    descriptor = None
    for klass in courceList::Cource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::cource_has_location():
    assert hasattr(courceList::Cource, "location")
    descriptor = None
    for klass in courceList::Cource.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::cource_has_code():
    assert hasattr(courceList::Cource, "code")
    descriptor = None
    for klass in courceList::Cource.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::studygeneralization_is_not_abstract():
    assert not inspect.isabstract(courceList::StudyGeneralization)


def test_courcelist::studygeneralization_constructor_exists():
    assert callable(courceList::StudyGeneralization.__init__)


def test_courcelist::studygeneralization_constructor_args():
    sig = inspect.signature(courceList::StudyGeneralization.__init__)
    params = list(sig.parameters.keys())
    assert "educationLevel" in params, "Missing parameter 'educationLevel'"
    assert "abbreviation" in params, "Missing parameter 'abbreviation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "campus" in params, "Missing parameter 'campus'"
    assert "nrOfYears" in params, "Missing parameter 'nrOfYears'"

def test_courcelist::studygeneralization_has_educationLevel():
    assert hasattr(courceList::StudyGeneralization, "educationLevel")
    descriptor = None
    for klass in courceList::StudyGeneralization.__mro__:
        if "educationLevel" in klass.__dict__:
            descriptor = klass.__dict__["educationLevel"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::studygeneralization_has_abbreviation():
    assert hasattr(courceList::StudyGeneralization, "abbreviation")
    descriptor = None
    for klass in courceList::StudyGeneralization.__mro__:
        if "abbreviation" in klass.__dict__:
            descriptor = klass.__dict__["abbreviation"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::studygeneralization_has_name():
    assert hasattr(courceList::StudyGeneralization, "name")
    descriptor = None
    for klass in courceList::StudyGeneralization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::studygeneralization_has_campus():
    assert hasattr(courceList::StudyGeneralization, "campus")
    descriptor = None
    for klass in courceList::StudyGeneralization.__mro__:
        if "campus" in klass.__dict__:
            descriptor = klass.__dict__["campus"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::studygeneralization_has_nrOfYears():
    assert hasattr(courceList::StudyGeneralization, "nrOfYears")
    descriptor = None
    for klass in courceList::StudyGeneralization.__mro__:
        if "nrOfYears" in klass.__dict__:
            descriptor = klass.__dict__["nrOfYears"]
            break
    assert isinstance(descriptor, property)



def test_courcelist::department_is_not_abstract():
    assert not inspect.isabstract(courceList::Department)


def test_courcelist::department_constructor_exists():
    assert callable(courceList::Department.__init__)


def test_courcelist::department_constructor_args():
    sig = inspect.signature(courceList::Department.__init__)
    params = list(sig.parameters.keys())
    assert "abbreviation" in params, "Missing parameter 'abbreviation'"
    assert "name" in params, "Missing parameter 'name'"

def test_courcelist::department_has_abbreviation():
    assert hasattr(courceList::Department, "abbreviation")
    descriptor = None
    for klass in courceList::Department.__mro__:
        if "abbreviation" in klass.__dict__:
            descriptor = klass.__dict__["abbreviation"]
            break
    assert isinstance(descriptor, property)

def test_courcelist::department_has_name():
    assert hasattr(courceList::Department, "name")
    descriptor = None
    for klass in courceList::Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_semester_exists():
    # Check that the Enumeration exists
    assert Semester is not None

def test_semester_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Semester]
    expected_literals = [
        "spring",
        "autumn",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Semester"

def test_educationlevel_exists():
    # Check that the Enumeration exists
    assert EducationLevel is not None

def test_educationlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EducationLevel]
    expected_literals = [
        "oneYear",
        "master",
        "phd",
        "bachelor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EducationLevel"

def test_campus_exists():
    # Check that the Enumeration exists
    assert Campus is not None

def test_campus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Campus]
    expected_literals = [
        "Gjøvik",
        "Ålesund",
        "Web",
        "Trondheim",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Campus"

def test_evaluationtype_exists():
    # Check that the Enumeration exists
    assert EvaluationType is not None

def test_evaluationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EvaluationType]
    expected_literals = [
        "approved",
        "grade",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EvaluationType"

def test_workform_exists():
    # Check that the Enumeration exists
    assert WorkForm is not None

def test_workform_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkForm]
    expected_literals = [
        "home",
        "oral",
        "written",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkForm"


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
courceList::Specialisation_strategy = st.builds(
    courceList::Specialisation,
    startSemester=
        st.integers(),
    name=
        safe_text
)
courceList::StudyProgram_strategy = st.builds(
    courceList::StudyProgram,
    year=
        st.integers()
)
courceList::Student_strategy = st.builds(
    courceList::Student,
    nr=
        st.integers()
)
courceList::CourceSpecification_strategy = st.builds(
    courceList::CourceSpecification,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    language=
        safe_text,
    name=
        safe_text,
    semester=
        safe_text,
    specificationYear=
        st.integers(),
    version=
        safe_text
)
courceList::StudyCourceRelation_strategy = st.builds(
    courceList::StudyCourceRelation,
    status=
        safe_text,
    year=
        st.integers()
)
courceList::Work_strategy = st.builds(
    courceList::Work,
    weight=
        st.integers()
)
courceList::EvaluationForm_strategy = st.builds(
    courceList::EvaluationForm,
    evaluationType=
        safe_text
)
courceList::Exam_strategy = st.builds(
    courceList::Exam,
    weight=
        st.integers(),
    lenght=
        st.integers(),
    date=
        st.dates(),
    form=
        safe_text
)
courceList::Professor_strategy = st.builds(
    courceList::Professor,
    name=
        safe_text,
    title=
        safe_text
)
courceList::Cource_strategy = st.builds(
    courceList::Cource,
    name=
        safe_text,
    location=
        safe_text,
    code=
        safe_text
)
courceList::StudyGeneralization_strategy = st.builds(
    courceList::StudyGeneralization,
    educationLevel=
        safe_text,
    abbreviation=
        safe_text,
    name=
        safe_text,
    campus=
        safe_text,
    nrOfYears=
        st.integers()
)
courceList::Department_strategy = st.builds(
    courceList::Department,
    abbreviation=
        safe_text,
    name=
        safe_text
)

@given(instance=courceList::Specialisation_strategy)
@settings(max_examples=50)
def test_courcelist::specialisation_instantiation(instance):
    assert isinstance(instance, courceList::Specialisation)

@given(instance=courceList::Specialisation_strategy)
def test_courcelist::specialisation_startSemester_type(instance):
    assert isinstance(instance.startSemester, int)


@given(instance=courceList::Specialisation_strategy)
def test_courcelist::specialisation_startSemester_setter(instance):
    original = instance.startSemester
    instance.startSemester = original
    assert instance.startSemester == original

@given(instance=courceList::Specialisation_strategy)
def test_courcelist::specialisation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=courceList::Specialisation_strategy)
def test_courcelist::specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList::StudyProgram_strategy)
@settings(max_examples=50)
def test_courcelist::studyprogram_instantiation(instance):
    assert isinstance(instance, courceList::StudyProgram)

@given(instance=courceList::StudyProgram_strategy)
def test_courcelist::studyprogram_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=courceList::StudyProgram_strategy)
def test_courcelist::studyprogram_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=courceList::Student_strategy)
@settings(max_examples=50)
def test_courcelist::student_instantiation(instance):
    assert isinstance(instance, courceList::Student)

@given(instance=courceList::Student_strategy)
def test_courcelist::student_nr_type(instance):
    assert isinstance(instance.nr, int)


@given(instance=courceList::Student_strategy)
def test_courcelist::student_nr_setter(instance):
    original = instance.nr
    instance.nr = original
    assert instance.nr == original

@given(instance=courceList::CourceSpecification_strategy)
@settings(max_examples=50)
def test_courcelist::courcespecification_instantiation(instance):
    assert isinstance(instance, courceList::CourceSpecification)

@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_credits_type(instance):
    assert isinstance(instance.credits, float)


@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original

@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_semester_type(instance):
    assert isinstance(instance.semester, str)


@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_specificationYear_type(instance):
    assert isinstance(instance.specificationYear, int)


@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_specificationYear_setter(instance):
    original = instance.specificationYear
    instance.specificationYear = original
    assert instance.specificationYear == original

@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=courceList::CourceSpecification_strategy)
def test_courcelist::courcespecification_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=courceList::StudyCourceRelation_strategy)
@settings(max_examples=50)
def test_courcelist::studycourcerelation_instantiation(instance):
    assert isinstance(instance, courceList::StudyCourceRelation)

@given(instance=courceList::StudyCourceRelation_strategy)
def test_courcelist::studycourcerelation_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=courceList::StudyCourceRelation_strategy)
def test_courcelist::studycourcerelation_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=courceList::StudyCourceRelation_strategy)
def test_courcelist::studycourcerelation_year_type(instance):
    assert isinstance(instance.year, int)


@given(instance=courceList::StudyCourceRelation_strategy)
def test_courcelist::studycourcerelation_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=courceList::Work_strategy)
@settings(max_examples=50)
def test_courcelist::work_instantiation(instance):
    assert isinstance(instance, courceList::Work)

@given(instance=courceList::Work_strategy)
def test_courcelist::work_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=courceList::Work_strategy)
def test_courcelist::work_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=courceList::EvaluationForm_strategy)
@settings(max_examples=50)
def test_courcelist::evaluationform_instantiation(instance):
    assert isinstance(instance, courceList::EvaluationForm)

@given(instance=courceList::EvaluationForm_strategy)
def test_courcelist::evaluationform_evaluationType_type(instance):
    assert isinstance(instance.evaluationType, str)


@given(instance=courceList::EvaluationForm_strategy)
def test_courcelist::evaluationform_evaluationType_setter(instance):
    original = instance.evaluationType
    instance.evaluationType = original
    assert instance.evaluationType == original

@given(instance=courceList::Exam_strategy)
@settings(max_examples=50)
def test_courcelist::exam_instantiation(instance):
    assert isinstance(instance, courceList::Exam)

@given(instance=courceList::Exam_strategy)
def test_courcelist::exam_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=courceList::Exam_strategy)
def test_courcelist::exam_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=courceList::Exam_strategy)
def test_courcelist::exam_lenght_type(instance):
    assert isinstance(instance.lenght, int)


@given(instance=courceList::Exam_strategy)
def test_courcelist::exam_lenght_setter(instance):
    original = instance.lenght
    instance.lenght = original
    assert instance.lenght == original

@given(instance=courceList::Exam_strategy)
def test_courcelist::exam_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=courceList::Exam_strategy)
def test_courcelist::exam_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=courceList::Exam_strategy)
def test_courcelist::exam_form_type(instance):
    assert isinstance(instance.form, str)


@given(instance=courceList::Exam_strategy)
def test_courcelist::exam_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original

@given(instance=courceList::Professor_strategy)
@settings(max_examples=50)
def test_courcelist::professor_instantiation(instance):
    assert isinstance(instance, courceList::Professor)

@given(instance=courceList::Professor_strategy)
def test_courcelist::professor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=courceList::Professor_strategy)
def test_courcelist::professor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList::Professor_strategy)
def test_courcelist::professor_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=courceList::Professor_strategy)
def test_courcelist::professor_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=courceList::Cource_strategy)
@settings(max_examples=50)
def test_courcelist::cource_instantiation(instance):
    assert isinstance(instance, courceList::Cource)

@given(instance=courceList::Cource_strategy)
def test_courcelist::cource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=courceList::Cource_strategy)
def test_courcelist::cource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList::Cource_strategy)
def test_courcelist::cource_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=courceList::Cource_strategy)
def test_courcelist::cource_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=courceList::Cource_strategy)
def test_courcelist::cource_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=courceList::Cource_strategy)
def test_courcelist::cource_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=courceList::StudyGeneralization_strategy)
@settings(max_examples=50)
def test_courcelist::studygeneralization_instantiation(instance):
    assert isinstance(instance, courceList::StudyGeneralization)

@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_educationLevel_type(instance):
    assert isinstance(instance.educationLevel, str)


@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_educationLevel_setter(instance):
    original = instance.educationLevel
    instance.educationLevel = original
    assert instance.educationLevel == original

@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_abbreviation_type(instance):
    assert isinstance(instance.abbreviation, str)


@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_abbreviation_setter(instance):
    original = instance.abbreviation
    instance.abbreviation = original
    assert instance.abbreviation == original

@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_campus_type(instance):
    assert isinstance(instance.campus, str)


@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_campus_setter(instance):
    original = instance.campus
    instance.campus = original
    assert instance.campus == original

@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_nrOfYears_type(instance):
    assert isinstance(instance.nrOfYears, int)


@given(instance=courceList::StudyGeneralization_strategy)
def test_courcelist::studygeneralization_nrOfYears_setter(instance):
    original = instance.nrOfYears
    instance.nrOfYears = original
    assert instance.nrOfYears == original

@given(instance=courceList::Department_strategy)
@settings(max_examples=50)
def test_courcelist::department_instantiation(instance):
    assert isinstance(instance, courceList::Department)

@given(instance=courceList::Department_strategy)
def test_courcelist::department_abbreviation_type(instance):
    assert isinstance(instance.abbreviation, str)


@given(instance=courceList::Department_strategy)
def test_courcelist::department_abbreviation_setter(instance):
    original = instance.abbreviation
    instance.abbreviation = original
    assert instance.abbreviation == original

@given(instance=courceList::Department_strategy)
def test_courcelist::department_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=courceList::Department_strategy)
def test_courcelist::department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
