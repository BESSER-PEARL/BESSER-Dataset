import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fopramodel_Auxiliary,
    fopramodel_ResearchGroup,
    Person,
    fopramodel_ExternalAdvisor,
    fopramodel_Associate,
    fopramodel_Student,
    fopramodel_Professor,
    fopramodel_Person,
    fopramodel_FoPraManagementSystem,
    fopramodel_FoPra,
    Course,
    AuxiliaryKind,
    Status,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fopramodel_auxiliary_is_not_abstract():
    assert not inspect.isabstract(fopramodel_Auxiliary)


def test_fopramodel_auxiliary_constructor_exists():
    assert callable(fopramodel_Auxiliary.__init__)


def test_fopramodel_auxiliary_constructor_args():
    sig = inspect.signature(fopramodel_Auxiliary.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_fopramodel_auxiliary_has_description():
    assert hasattr(fopramodel_Auxiliary, "description")
    descriptor = None
    for klass in fopramodel_Auxiliary.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel_auxiliary_has_kind():
    assert hasattr(fopramodel_Auxiliary, "kind")
    descriptor = None
    for klass in fopramodel_Auxiliary.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_fopramodel_researchgroup_is_not_abstract():
    assert not inspect.isabstract(fopramodel_ResearchGroup)


def test_fopramodel_researchgroup_constructor_exists():
    assert callable(fopramodel_ResearchGroup.__init__)


def test_fopramodel_researchgroup_constructor_args():
    sig = inspect.signature(fopramodel_ResearchGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fopramodel_researchgroup_has_name():
    assert hasattr(fopramodel_ResearchGroup, "name")
    descriptor = None
    for klass in fopramodel_ResearchGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_fopramodel_externaladvisor_is_not_abstract():
    assert not inspect.isabstract(fopramodel_ExternalAdvisor)


def test_fopramodel_externaladvisor_constructor_exists():
    assert callable(fopramodel_ExternalAdvisor.__init__)


def test_fopramodel_externaladvisor_constructor_args():
    sig = inspect.signature(fopramodel_ExternalAdvisor.__init__)
    params = list(sig.parameters.keys())
    assert "information" in params, "Missing parameter 'information'"

def test_fopramodel_externaladvisor_has_information():
    assert hasattr(fopramodel_ExternalAdvisor, "information")
    descriptor = None
    for klass in fopramodel_ExternalAdvisor.__mro__:
        if "information" in klass.__dict__:
            descriptor = klass.__dict__["information"]
            break
    assert isinstance(descriptor, property)



def test_fopramodel_associate_is_not_abstract():
    assert not inspect.isabstract(fopramodel_Associate)


def test_fopramodel_associate_constructor_exists():
    assert callable(fopramodel_Associate.__init__)


def test_fopramodel_associate_constructor_args():
    sig = inspect.signature(fopramodel_Associate.__init__)
    params = list(sig.parameters.keys())



def test_fopramodel_student_is_not_abstract():
    assert not inspect.isabstract(fopramodel_Student)


def test_fopramodel_student_constructor_exists():
    assert callable(fopramodel_Student.__init__)


def test_fopramodel_student_constructor_args():
    sig = inspect.signature(fopramodel_Student.__init__)
    params = list(sig.parameters.keys())
    assert "matrikel" in params, "Missing parameter 'matrikel'"
    assert "course" in params, "Missing parameter 'course'"

def test_fopramodel_student_has_matrikel():
    assert hasattr(fopramodel_Student, "matrikel")
    descriptor = None
    for klass in fopramodel_Student.__mro__:
        if "matrikel" in klass.__dict__:
            descriptor = klass.__dict__["matrikel"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel_student_has_course():
    assert hasattr(fopramodel_Student, "course")
    descriptor = None
    for klass in fopramodel_Student.__mro__:
        if "course" in klass.__dict__:
            descriptor = klass.__dict__["course"]
            break
    assert isinstance(descriptor, property)



def test_fopramodel_professor_is_not_abstract():
    assert not inspect.isabstract(fopramodel_Professor)


def test_fopramodel_professor_constructor_exists():
    assert callable(fopramodel_Professor.__init__)


def test_fopramodel_professor_constructor_args():
    sig = inspect.signature(fopramodel_Professor.__init__)
    params = list(sig.parameters.keys())



def test_fopramodel_person_is_not_abstract():
    assert not inspect.isabstract(fopramodel_Person)


def test_fopramodel_person_constructor_exists():
    assert callable(fopramodel_Person.__init__)


def test_fopramodel_person_constructor_args():
    sig = inspect.signature(fopramodel_Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "forename" in params, "Missing parameter 'forename'"

def test_fopramodel_person_has_lastname():
    assert hasattr(fopramodel_Person, "lastname")
    descriptor = None
    for klass in fopramodel_Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel_person_has_forename():
    assert hasattr(fopramodel_Person, "forename")
    descriptor = None
    for klass in fopramodel_Person.__mro__:
        if "forename" in klass.__dict__:
            descriptor = klass.__dict__["forename"]
            break
    assert isinstance(descriptor, property)



def test_fopramodel_fopramanagementsystem_is_not_abstract():
    assert not inspect.isabstract(fopramodel_FoPraManagementSystem)


def test_fopramodel_fopramanagementsystem_constructor_exists():
    assert callable(fopramodel_FoPraManagementSystem.__init__)


def test_fopramodel_fopramanagementsystem_constructor_args():
    sig = inspect.signature(fopramodel_FoPraManagementSystem.__init__)
    params = list(sig.parameters.keys())



def test_fopramodel_fopra_is_not_abstract():
    assert not inspect.isabstract(fopramodel_FoPra)


def test_fopramodel_fopra_constructor_exists():
    assert callable(fopramodel_FoPra.__init__)


def test_fopramodel_fopra_constructor_args():
    sig = inspect.signature(fopramodel_FoPra.__init__)
    params = list(sig.parameters.keys())
    assert "maxNumberOfStudents" in params, "Missing parameter 'maxNumberOfStudents'"
    assert "status" in params, "Missing parameter 'status'"
    assert "description" in params, "Missing parameter 'description'"
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"
    assert "title" in params, "Missing parameter 'title'"

def test_fopramodel_fopra_has_maxNumberOfStudents():
    assert hasattr(fopramodel_FoPra, "maxNumberOfStudents")
    descriptor = None
    for klass in fopramodel_FoPra.__mro__:
        if "maxNumberOfStudents" in klass.__dict__:
            descriptor = klass.__dict__["maxNumberOfStudents"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel_fopra_has_status():
    assert hasattr(fopramodel_FoPra, "status")
    descriptor = None
    for klass in fopramodel_FoPra.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel_fopra_has_description():
    assert hasattr(fopramodel_FoPra, "description")
    descriptor = None
    for klass in fopramodel_FoPra.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel_fopra_has_start():
    assert hasattr(fopramodel_FoPra, "start")
    descriptor = None
    for klass in fopramodel_FoPra.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel_fopra_has_end():
    assert hasattr(fopramodel_FoPra, "end")
    descriptor = None
    for klass in fopramodel_FoPra.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel_fopra_has_title():
    assert hasattr(fopramodel_FoPra, "title")
    descriptor = None
    for klass in fopramodel_FoPra.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_course_exists():
    # Check that the Enumeration exists
    assert Course is not None

def test_course_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Course]
    expected_literals = [
        "InfoDiplom",
        "InfoMSc",
        "InfoMinorSubject",
        "InfoBSc",
        "InfoPostGraduate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Course"

def test_auxiliarykind_exists():
    # Check that the Enumeration exists
    assert AuxiliaryKind is not None

def test_auxiliarykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuxiliaryKind]
    expected_literals = [
        "ProgrammingLanguage",
        "Tool",
        "Method",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuxiliaryKind"

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "inprocess",
        "cancelled",
        "pending",
        "completed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"


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
fopramodel_Auxiliary_strategy = st.builds(
    fopramodel_Auxiliary,
    description=
        safe_text,
    kind=
        safe_text
)
fopramodel_ResearchGroup_strategy = st.builds(
    fopramodel_ResearchGroup,
    name=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
fopramodel_ExternalAdvisor_strategy = st.builds(
    fopramodel_ExternalAdvisor,
    information=
        safe_text
)
fopramodel_Associate_strategy = st.builds(
    fopramodel_Associate,
)
fopramodel_Student_strategy = st.builds(
    fopramodel_Student,
    matrikel=
        safe_text,
    course=
        safe_text
)
fopramodel_Professor_strategy = st.builds(
    fopramodel_Professor,
)
fopramodel_Person_strategy = st.builds(
    fopramodel_Person,
    lastname=
        safe_text,
    forename=
        safe_text
)
fopramodel_FoPraManagementSystem_strategy = st.builds(
    fopramodel_FoPraManagementSystem,
)
fopramodel_FoPra_strategy = st.builds(
    fopramodel_FoPra,
    maxNumberOfStudents=
        st.integers(),
    status=
        safe_text,
    description=
        safe_text,
    start=
        st.dates(),
    end=
        st.dates(),
    title=
        safe_text
)

@given(instance=fopramodel_Auxiliary_strategy)
@settings(max_examples=50)
def test_fopramodel_auxiliary_instantiation(instance):
    assert isinstance(instance, fopramodel_Auxiliary)



@given(instance=fopramodel_Auxiliary_strategy)
def test_fopramodel_auxiliary_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fopramodel_Auxiliary_strategy)
def test_fopramodel_auxiliary_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=fopramodel_ResearchGroup_strategy)
@settings(max_examples=50)
def test_fopramodel_researchgroup_instantiation(instance):
    assert isinstance(instance, fopramodel_ResearchGroup)



@given(instance=fopramodel_ResearchGroup_strategy)
def test_fopramodel_researchgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=fopramodel_ExternalAdvisor_strategy)
@settings(max_examples=50)
def test_fopramodel_externaladvisor_instantiation(instance):
    assert isinstance(instance, fopramodel_ExternalAdvisor)



@given(instance=fopramodel_ExternalAdvisor_strategy)
def test_fopramodel_externaladvisor_information_setter(instance):
    original = instance.information
    instance.information = original
    assert instance.information == original

@given(instance=fopramodel_Associate_strategy)
@settings(max_examples=50)
def test_fopramodel_associate_instantiation(instance):
    assert isinstance(instance, fopramodel_Associate)

@given(instance=fopramodel_Student_strategy)
@settings(max_examples=50)
def test_fopramodel_student_instantiation(instance):
    assert isinstance(instance, fopramodel_Student)



@given(instance=fopramodel_Student_strategy)
def test_fopramodel_student_matrikel_setter(instance):
    original = instance.matrikel
    instance.matrikel = original
    assert instance.matrikel == original



@given(instance=fopramodel_Student_strategy)
def test_fopramodel_student_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original

@given(instance=fopramodel_Professor_strategy)
@settings(max_examples=50)
def test_fopramodel_professor_instantiation(instance):
    assert isinstance(instance, fopramodel_Professor)

@given(instance=fopramodel_Person_strategy)
@settings(max_examples=50)
def test_fopramodel_person_instantiation(instance):
    assert isinstance(instance, fopramodel_Person)



@given(instance=fopramodel_Person_strategy)
def test_fopramodel_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=fopramodel_Person_strategy)
def test_fopramodel_person_forename_setter(instance):
    original = instance.forename
    instance.forename = original
    assert instance.forename == original

@given(instance=fopramodel_FoPraManagementSystem_strategy)
@settings(max_examples=50)
def test_fopramodel_fopramanagementsystem_instantiation(instance):
    assert isinstance(instance, fopramodel_FoPraManagementSystem)

@given(instance=fopramodel_FoPra_strategy)
@settings(max_examples=50)
def test_fopramodel_fopra_instantiation(instance):
    assert isinstance(instance, fopramodel_FoPra)



@given(instance=fopramodel_FoPra_strategy)
def test_fopramodel_fopra_maxNumberOfStudents_setter(instance):
    original = instance.maxNumberOfStudents
    instance.maxNumberOfStudents = original
    assert instance.maxNumberOfStudents == original



@given(instance=fopramodel_FoPra_strategy)
def test_fopramodel_fopra_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=fopramodel_FoPra_strategy)
def test_fopramodel_fopra_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fopramodel_FoPra_strategy)
def test_fopramodel_fopra_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=fopramodel_FoPra_strategy)
def test_fopramodel_fopra_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=fopramodel_FoPra_strategy)
def test_fopramodel_fopra_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
