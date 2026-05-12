import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    courceList_Specialisation,
    courceList_StudyProgram,
    courceList_Student,
    courceList_CourceSpecification,
    courceList_StudyCourceRelation,
    courceList_Work,
    courceList_EvaluationForm,
    courceList_Exam,
    courceList_Professor,
    courceList_Cource,
    courceList_StudyGeneralization,
    courceList_Department,
    Semester,
    EvaluationType,
    EducationLevel,
    Campus,
    WorkForm,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_courcelist_specialisation_is_not_abstract():
    assert not inspect.isabstract(courceList_Specialisation)


def test_courcelist_specialisation_constructor_exists():
    assert callable(courceList_Specialisation.__init__)


def test_courcelist_specialisation_constructor_args():
    sig = inspect.signature(courceList_Specialisation.__init__)
    params = list(sig.parameters.keys())
    assert "startSemester" in params, "Missing parameter 'startSemester'"
    assert "name" in params, "Missing parameter 'name'"

def test_courcelist_specialisation_has_startSemester():
    assert hasattr(courceList_Specialisation, "startSemester")
    descriptor = None
    for klass in courceList_Specialisation.__mro__:
        if "startSemester" in klass.__dict__:
            descriptor = klass.__dict__["startSemester"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_specialisation_has_name():
    assert hasattr(courceList_Specialisation, "name")
    descriptor = None
    for klass in courceList_Specialisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_studyprogram_is_not_abstract():
    assert not inspect.isabstract(courceList_StudyProgram)


def test_courcelist_studyprogram_constructor_exists():
    assert callable(courceList_StudyProgram.__init__)


def test_courcelist_studyprogram_constructor_args():
    sig = inspect.signature(courceList_StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_courcelist_studyprogram_has_year():
    assert hasattr(courceList_StudyProgram, "year")
    descriptor = None
    for klass in courceList_StudyProgram.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_student_is_not_abstract():
    assert not inspect.isabstract(courceList_Student)


def test_courcelist_student_constructor_exists():
    assert callable(courceList_Student.__init__)


def test_courcelist_student_constructor_args():
    sig = inspect.signature(courceList_Student.__init__)
    params = list(sig.parameters.keys())
    assert "nr" in params, "Missing parameter 'nr'"

def test_courcelist_student_has_nr():
    assert hasattr(courceList_Student, "nr")
    descriptor = None
    for klass in courceList_Student.__mro__:
        if "nr" in klass.__dict__:
            descriptor = klass.__dict__["nr"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_courcespecification_is_not_abstract():
    assert not inspect.isabstract(courceList_CourceSpecification)


def test_courcelist_courcespecification_constructor_exists():
    assert callable(courceList_CourceSpecification.__init__)


def test_courcelist_courcespecification_constructor_args():
    sig = inspect.signature(courceList_CourceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "specificationYear" in params, "Missing parameter 'specificationYear'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "language" in params, "Missing parameter 'language'"
    assert "semester" in params, "Missing parameter 'semester'"
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_courcelist_courcespecification_has_specificationYear():
    assert hasattr(courceList_CourceSpecification, "specificationYear")
    descriptor = None
    for klass in courceList_CourceSpecification.__mro__:
        if "specificationYear" in klass.__dict__:
            descriptor = klass.__dict__["specificationYear"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_courcespecification_has_credits():
    assert hasattr(courceList_CourceSpecification, "credits")
    descriptor = None
    for klass in courceList_CourceSpecification.__mro__:
        if "credits" in klass.__dict__:
            descriptor = klass.__dict__["credits"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_courcespecification_has_language():
    assert hasattr(courceList_CourceSpecification, "language")
    descriptor = None
    for klass in courceList_CourceSpecification.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_courcespecification_has_semester():
    assert hasattr(courceList_CourceSpecification, "semester")
    descriptor = None
    for klass in courceList_CourceSpecification.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_courcespecification_has_version():
    assert hasattr(courceList_CourceSpecification, "version")
    descriptor = None
    for klass in courceList_CourceSpecification.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_courcespecification_has_name():
    assert hasattr(courceList_CourceSpecification, "name")
    descriptor = None
    for klass in courceList_CourceSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_studycourcerelation_is_not_abstract():
    assert not inspect.isabstract(courceList_StudyCourceRelation)


def test_courcelist_studycourcerelation_constructor_exists():
    assert callable(courceList_StudyCourceRelation.__init__)


def test_courcelist_studycourcerelation_constructor_args():
    sig = inspect.signature(courceList_StudyCourceRelation.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "year" in params, "Missing parameter 'year'"

def test_courcelist_studycourcerelation_has_status():
    assert hasattr(courceList_StudyCourceRelation, "status")
    descriptor = None
    for klass in courceList_StudyCourceRelation.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_studycourcerelation_has_year():
    assert hasattr(courceList_StudyCourceRelation, "year")
    descriptor = None
    for klass in courceList_StudyCourceRelation.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_work_is_not_abstract():
    assert not inspect.isabstract(courceList_Work)


def test_courcelist_work_constructor_exists():
    assert callable(courceList_Work.__init__)


def test_courcelist_work_constructor_args():
    sig = inspect.signature(courceList_Work.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_courcelist_work_has_weight():
    assert hasattr(courceList_Work, "weight")
    descriptor = None
    for klass in courceList_Work.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_evaluationform_is_not_abstract():
    assert not inspect.isabstract(courceList_EvaluationForm)


def test_courcelist_evaluationform_constructor_exists():
    assert callable(courceList_EvaluationForm.__init__)


def test_courcelist_evaluationform_constructor_args():
    sig = inspect.signature(courceList_EvaluationForm.__init__)
    params = list(sig.parameters.keys())
    assert "evaluationType" in params, "Missing parameter 'evaluationType'"

def test_courcelist_evaluationform_has_evaluationType():
    assert hasattr(courceList_EvaluationForm, "evaluationType")
    descriptor = None
    for klass in courceList_EvaluationForm.__mro__:
        if "evaluationType" in klass.__dict__:
            descriptor = klass.__dict__["evaluationType"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_exam_is_not_abstract():
    assert not inspect.isabstract(courceList_Exam)


def test_courcelist_exam_constructor_exists():
    assert callable(courceList_Exam.__init__)


def test_courcelist_exam_constructor_args():
    sig = inspect.signature(courceList_Exam.__init__)
    params = list(sig.parameters.keys())
    assert "form" in params, "Missing parameter 'form'"
    assert "lenght" in params, "Missing parameter 'lenght'"
    assert "date" in params, "Missing parameter 'date'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_courcelist_exam_has_form():
    assert hasattr(courceList_Exam, "form")
    descriptor = None
    for klass in courceList_Exam.__mro__:
        if "form" in klass.__dict__:
            descriptor = klass.__dict__["form"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_exam_has_lenght():
    assert hasattr(courceList_Exam, "lenght")
    descriptor = None
    for klass in courceList_Exam.__mro__:
        if "lenght" in klass.__dict__:
            descriptor = klass.__dict__["lenght"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_exam_has_date():
    assert hasattr(courceList_Exam, "date")
    descriptor = None
    for klass in courceList_Exam.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_exam_has_weight():
    assert hasattr(courceList_Exam, "weight")
    descriptor = None
    for klass in courceList_Exam.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_professor_is_not_abstract():
    assert not inspect.isabstract(courceList_Professor)


def test_courcelist_professor_constructor_exists():
    assert callable(courceList_Professor.__init__)


def test_courcelist_professor_constructor_args():
    sig = inspect.signature(courceList_Professor.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"

def test_courcelist_professor_has_title():
    assert hasattr(courceList_Professor, "title")
    descriptor = None
    for klass in courceList_Professor.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_professor_has_name():
    assert hasattr(courceList_Professor, "name")
    descriptor = None
    for klass in courceList_Professor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_cource_is_not_abstract():
    assert not inspect.isabstract(courceList_Cource)


def test_courcelist_cource_constructor_exists():
    assert callable(courceList_Cource.__init__)


def test_courcelist_cource_constructor_args():
    sig = inspect.signature(courceList_Cource.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"

def test_courcelist_cource_has_code():
    assert hasattr(courceList_Cource, "code")
    descriptor = None
    for klass in courceList_Cource.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_cource_has_location():
    assert hasattr(courceList_Cource, "location")
    descriptor = None
    for klass in courceList_Cource.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_cource_has_name():
    assert hasattr(courceList_Cource, "name")
    descriptor = None
    for klass in courceList_Cource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_studygeneralization_is_not_abstract():
    assert not inspect.isabstract(courceList_StudyGeneralization)


def test_courcelist_studygeneralization_constructor_exists():
    assert callable(courceList_StudyGeneralization.__init__)


def test_courcelist_studygeneralization_constructor_args():
    sig = inspect.signature(courceList_StudyGeneralization.__init__)
    params = list(sig.parameters.keys())
    assert "abbreviation" in params, "Missing parameter 'abbreviation'"
    assert "campus" in params, "Missing parameter 'campus'"
    assert "educationLevel" in params, "Missing parameter 'educationLevel'"
    assert "nrOfYears" in params, "Missing parameter 'nrOfYears'"
    assert "name" in params, "Missing parameter 'name'"

def test_courcelist_studygeneralization_has_abbreviation():
    assert hasattr(courceList_StudyGeneralization, "abbreviation")
    descriptor = None
    for klass in courceList_StudyGeneralization.__mro__:
        if "abbreviation" in klass.__dict__:
            descriptor = klass.__dict__["abbreviation"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_studygeneralization_has_campus():
    assert hasattr(courceList_StudyGeneralization, "campus")
    descriptor = None
    for klass in courceList_StudyGeneralization.__mro__:
        if "campus" in klass.__dict__:
            descriptor = klass.__dict__["campus"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_studygeneralization_has_educationLevel():
    assert hasattr(courceList_StudyGeneralization, "educationLevel")
    descriptor = None
    for klass in courceList_StudyGeneralization.__mro__:
        if "educationLevel" in klass.__dict__:
            descriptor = klass.__dict__["educationLevel"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_studygeneralization_has_nrOfYears():
    assert hasattr(courceList_StudyGeneralization, "nrOfYears")
    descriptor = None
    for klass in courceList_StudyGeneralization.__mro__:
        if "nrOfYears" in klass.__dict__:
            descriptor = klass.__dict__["nrOfYears"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_studygeneralization_has_name():
    assert hasattr(courceList_StudyGeneralization, "name")
    descriptor = None
    for klass in courceList_StudyGeneralization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_courcelist_department_is_not_abstract():
    assert not inspect.isabstract(courceList_Department)


def test_courcelist_department_constructor_exists():
    assert callable(courceList_Department.__init__)


def test_courcelist_department_constructor_args():
    sig = inspect.signature(courceList_Department.__init__)
    params = list(sig.parameters.keys())
    assert "abbreviation" in params, "Missing parameter 'abbreviation'"
    assert "name" in params, "Missing parameter 'name'"

def test_courcelist_department_has_abbreviation():
    assert hasattr(courceList_Department, "abbreviation")
    descriptor = None
    for klass in courceList_Department.__mro__:
        if "abbreviation" in klass.__dict__:
            descriptor = klass.__dict__["abbreviation"]
            break
    assert isinstance(descriptor, property)

def test_courcelist_department_has_name():
    assert hasattr(courceList_Department, "name")
    descriptor = None
    for klass in courceList_Department.__mro__:
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

def test_educationlevel_exists():
    # Check that the Enumeration exists
    assert EducationLevel is not None

def test_educationlevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EducationLevel]
    expected_literals = [
        "oneYear",
        "master",
        "bachelor",
        "phd",
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
        "Trondheim",
        "Web",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Campus"

def test_workform_exists():
    # Check that the Enumeration exists
    assert WorkForm is not None

def test_workform_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkForm]
    expected_literals = [
        "oral",
        "home",
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
courceList_Specialisation_strategy = st.builds(
    courceList_Specialisation,
    startSemester=
        st.integers(),
    name=
        safe_text
)
courceList_StudyProgram_strategy = st.builds(
    courceList_StudyProgram,
    year=
        st.integers()
)
courceList_Student_strategy = st.builds(
    courceList_Student,
    nr=
        st.integers()
)
courceList_CourceSpecification_strategy = st.builds(
    courceList_CourceSpecification,
    specificationYear=
        st.integers(),
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    language=
        safe_text,
    semester=
        safe_text,
    version=
        safe_text,
    name=
        safe_text
)
courceList_StudyCourceRelation_strategy = st.builds(
    courceList_StudyCourceRelation,
    status=
        safe_text,
    year=
        st.integers()
)
courceList_Work_strategy = st.builds(
    courceList_Work,
    weight=
        st.integers()
)
courceList_EvaluationForm_strategy = st.builds(
    courceList_EvaluationForm,
    evaluationType=
        safe_text
)
courceList_Exam_strategy = st.builds(
    courceList_Exam,
    form=
        safe_text,
    lenght=
        st.integers(),
    date=
        st.dates(),
    weight=
        st.integers()
)
courceList_Professor_strategy = st.builds(
    courceList_Professor,
    title=
        safe_text,
    name=
        safe_text
)
courceList_Cource_strategy = st.builds(
    courceList_Cource,
    code=
        safe_text,
    location=
        safe_text,
    name=
        safe_text
)
courceList_StudyGeneralization_strategy = st.builds(
    courceList_StudyGeneralization,
    abbreviation=
        safe_text,
    campus=
        safe_text,
    educationLevel=
        safe_text,
    nrOfYears=
        st.integers(),
    name=
        safe_text
)
courceList_Department_strategy = st.builds(
    courceList_Department,
    abbreviation=
        safe_text,
    name=
        safe_text
)

@given(instance=courceList_Specialisation_strategy)
@settings(max_examples=50)
def test_courcelist_specialisation_instantiation(instance):
    assert isinstance(instance, courceList_Specialisation)



@given(instance=courceList_Specialisation_strategy)
def test_courcelist_specialisation_startSemester_setter(instance):
    original = instance.startSemester
    instance.startSemester = original
    assert instance.startSemester == original



@given(instance=courceList_Specialisation_strategy)
def test_courcelist_specialisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList_StudyProgram_strategy)
@settings(max_examples=50)
def test_courcelist_studyprogram_instantiation(instance):
    assert isinstance(instance, courceList_StudyProgram)



@given(instance=courceList_StudyProgram_strategy)
def test_courcelist_studyprogram_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=courceList_Student_strategy)
@settings(max_examples=50)
def test_courcelist_student_instantiation(instance):
    assert isinstance(instance, courceList_Student)



@given(instance=courceList_Student_strategy)
def test_courcelist_student_nr_setter(instance):
    original = instance.nr
    instance.nr = original
    assert instance.nr == original

@given(instance=courceList_CourceSpecification_strategy)
@settings(max_examples=50)
def test_courcelist_courcespecification_instantiation(instance):
    assert isinstance(instance, courceList_CourceSpecification)



@given(instance=courceList_CourceSpecification_strategy)
def test_courcelist_courcespecification_specificationYear_setter(instance):
    original = instance.specificationYear
    instance.specificationYear = original
    assert instance.specificationYear == original



@given(instance=courceList_CourceSpecification_strategy)
def test_courcelist_courcespecification_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=courceList_CourceSpecification_strategy)
def test_courcelist_courcespecification_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=courceList_CourceSpecification_strategy)
def test_courcelist_courcespecification_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original



@given(instance=courceList_CourceSpecification_strategy)
def test_courcelist_courcespecification_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=courceList_CourceSpecification_strategy)
def test_courcelist_courcespecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList_StudyCourceRelation_strategy)
@settings(max_examples=50)
def test_courcelist_studycourcerelation_instantiation(instance):
    assert isinstance(instance, courceList_StudyCourceRelation)



@given(instance=courceList_StudyCourceRelation_strategy)
def test_courcelist_studycourcerelation_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=courceList_StudyCourceRelation_strategy)
def test_courcelist_studycourcerelation_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=courceList_Work_strategy)
@settings(max_examples=50)
def test_courcelist_work_instantiation(instance):
    assert isinstance(instance, courceList_Work)



@given(instance=courceList_Work_strategy)
def test_courcelist_work_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=courceList_EvaluationForm_strategy)
@settings(max_examples=50)
def test_courcelist_evaluationform_instantiation(instance):
    assert isinstance(instance, courceList_EvaluationForm)



@given(instance=courceList_EvaluationForm_strategy)
def test_courcelist_evaluationform_evaluationType_setter(instance):
    original = instance.evaluationType
    instance.evaluationType = original
    assert instance.evaluationType == original

@given(instance=courceList_Exam_strategy)
@settings(max_examples=50)
def test_courcelist_exam_instantiation(instance):
    assert isinstance(instance, courceList_Exam)



@given(instance=courceList_Exam_strategy)
def test_courcelist_exam_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original



@given(instance=courceList_Exam_strategy)
def test_courcelist_exam_lenght_setter(instance):
    original = instance.lenght
    instance.lenght = original
    assert instance.lenght == original



@given(instance=courceList_Exam_strategy)
def test_courcelist_exam_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=courceList_Exam_strategy)
def test_courcelist_exam_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=courceList_Professor_strategy)
@settings(max_examples=50)
def test_courcelist_professor_instantiation(instance):
    assert isinstance(instance, courceList_Professor)



@given(instance=courceList_Professor_strategy)
def test_courcelist_professor_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=courceList_Professor_strategy)
def test_courcelist_professor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList_Cource_strategy)
@settings(max_examples=50)
def test_courcelist_cource_instantiation(instance):
    assert isinstance(instance, courceList_Cource)



@given(instance=courceList_Cource_strategy)
def test_courcelist_cource_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=courceList_Cource_strategy)
def test_courcelist_cource_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=courceList_Cource_strategy)
def test_courcelist_cource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList_StudyGeneralization_strategy)
@settings(max_examples=50)
def test_courcelist_studygeneralization_instantiation(instance):
    assert isinstance(instance, courceList_StudyGeneralization)



@given(instance=courceList_StudyGeneralization_strategy)
def test_courcelist_studygeneralization_abbreviation_setter(instance):
    original = instance.abbreviation
    instance.abbreviation = original
    assert instance.abbreviation == original



@given(instance=courceList_StudyGeneralization_strategy)
def test_courcelist_studygeneralization_campus_setter(instance):
    original = instance.campus
    instance.campus = original
    assert instance.campus == original



@given(instance=courceList_StudyGeneralization_strategy)
def test_courcelist_studygeneralization_educationLevel_setter(instance):
    original = instance.educationLevel
    instance.educationLevel = original
    assert instance.educationLevel == original



@given(instance=courceList_StudyGeneralization_strategy)
def test_courcelist_studygeneralization_nrOfYears_setter(instance):
    original = instance.nrOfYears
    instance.nrOfYears = original
    assert instance.nrOfYears == original



@given(instance=courceList_StudyGeneralization_strategy)
def test_courcelist_studygeneralization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=courceList_Department_strategy)
@settings(max_examples=50)
def test_courcelist_department_instantiation(instance):
    assert isinstance(instance, courceList_Department)



@given(instance=courceList_Department_strategy)
def test_courcelist_department_abbreviation_setter(instance):
    original = instance.abbreviation
    instance.abbreviation = original
    assert instance.abbreviation == original



@given(instance=courceList_Department_strategy)
def test_courcelist_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
