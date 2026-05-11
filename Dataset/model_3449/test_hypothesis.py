import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fopramodel::Auxiliary,
    fopramodel::ResearchGroup,
    Person,
    fopramodel::Professor,
    fopramodel::Student,
    fopramodel::Associate,
    fopramodel::ExternalAdvisor,
    fopramodel::Person,
    fopramodel::FoPraManagementSystem,
    fopramodel::FoPra,
    Status,
    Course,
    AuxiliaryKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fopramodel::auxiliary_is_not_abstract():
    assert not inspect.isabstract(fopramodel::Auxiliary)


def test_fopramodel::auxiliary_constructor_exists():
    assert callable(fopramodel::Auxiliary.__init__)


def test_fopramodel::auxiliary_constructor_args():
    sig = inspect.signature(fopramodel::Auxiliary.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "description" in params, "Missing parameter 'description'"

def test_fopramodel::auxiliary_has_kind():
    assert hasattr(fopramodel::Auxiliary, "kind")
    descriptor = None
    for klass in fopramodel::Auxiliary.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel::auxiliary_has_description():
    assert hasattr(fopramodel::Auxiliary, "description")
    descriptor = None
    for klass in fopramodel::Auxiliary.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_fopramodel::researchgroup_is_not_abstract():
    assert not inspect.isabstract(fopramodel::ResearchGroup)


def test_fopramodel::researchgroup_constructor_exists():
    assert callable(fopramodel::ResearchGroup.__init__)


def test_fopramodel::researchgroup_constructor_args():
    sig = inspect.signature(fopramodel::ResearchGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fopramodel::researchgroup_has_name():
    assert hasattr(fopramodel::ResearchGroup, "name")
    descriptor = None
    for klass in fopramodel::ResearchGroup.__mro__:
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



def test_fopramodel::professor_is_not_abstract():
    assert not inspect.isabstract(fopramodel::Professor)


def test_fopramodel::professor_constructor_exists():
    assert callable(fopramodel::Professor.__init__)


def test_fopramodel::professor_constructor_args():
    sig = inspect.signature(fopramodel::Professor.__init__)
    params = list(sig.parameters.keys())



def test_fopramodel::student_is_not_abstract():
    assert not inspect.isabstract(fopramodel::Student)


def test_fopramodel::student_constructor_exists():
    assert callable(fopramodel::Student.__init__)


def test_fopramodel::student_constructor_args():
    sig = inspect.signature(fopramodel::Student.__init__)
    params = list(sig.parameters.keys())
    assert "course" in params, "Missing parameter 'course'"
    assert "matrikel" in params, "Missing parameter 'matrikel'"

def test_fopramodel::student_has_course():
    assert hasattr(fopramodel::Student, "course")
    descriptor = None
    for klass in fopramodel::Student.__mro__:
        if "course" in klass.__dict__:
            descriptor = klass.__dict__["course"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel::student_has_matrikel():
    assert hasattr(fopramodel::Student, "matrikel")
    descriptor = None
    for klass in fopramodel::Student.__mro__:
        if "matrikel" in klass.__dict__:
            descriptor = klass.__dict__["matrikel"]
            break
    assert isinstance(descriptor, property)



def test_fopramodel::associate_is_not_abstract():
    assert not inspect.isabstract(fopramodel::Associate)


def test_fopramodel::associate_constructor_exists():
    assert callable(fopramodel::Associate.__init__)


def test_fopramodel::associate_constructor_args():
    sig = inspect.signature(fopramodel::Associate.__init__)
    params = list(sig.parameters.keys())



def test_fopramodel::externaladvisor_is_not_abstract():
    assert not inspect.isabstract(fopramodel::ExternalAdvisor)


def test_fopramodel::externaladvisor_constructor_exists():
    assert callable(fopramodel::ExternalAdvisor.__init__)


def test_fopramodel::externaladvisor_constructor_args():
    sig = inspect.signature(fopramodel::ExternalAdvisor.__init__)
    params = list(sig.parameters.keys())
    assert "information" in params, "Missing parameter 'information'"

def test_fopramodel::externaladvisor_has_information():
    assert hasattr(fopramodel::ExternalAdvisor, "information")
    descriptor = None
    for klass in fopramodel::ExternalAdvisor.__mro__:
        if "information" in klass.__dict__:
            descriptor = klass.__dict__["information"]
            break
    assert isinstance(descriptor, property)



def test_fopramodel::person_is_not_abstract():
    assert not inspect.isabstract(fopramodel::Person)


def test_fopramodel::person_constructor_exists():
    assert callable(fopramodel::Person.__init__)


def test_fopramodel::person_constructor_args():
    sig = inspect.signature(fopramodel::Person.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "forename" in params, "Missing parameter 'forename'"

def test_fopramodel::person_has_lastname():
    assert hasattr(fopramodel::Person, "lastname")
    descriptor = None
    for klass in fopramodel::Person.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel::person_has_forename():
    assert hasattr(fopramodel::Person, "forename")
    descriptor = None
    for klass in fopramodel::Person.__mro__:
        if "forename" in klass.__dict__:
            descriptor = klass.__dict__["forename"]
            break
    assert isinstance(descriptor, property)



def test_fopramodel::fopramanagementsystem_is_not_abstract():
    assert not inspect.isabstract(fopramodel::FoPraManagementSystem)


def test_fopramodel::fopramanagementsystem_constructor_exists():
    assert callable(fopramodel::FoPraManagementSystem.__init__)


def test_fopramodel::fopramanagementsystem_constructor_args():
    sig = inspect.signature(fopramodel::FoPraManagementSystem.__init__)
    params = list(sig.parameters.keys())



def test_fopramodel::fopra_is_not_abstract():
    assert not inspect.isabstract(fopramodel::FoPra)


def test_fopramodel::fopra_constructor_exists():
    assert callable(fopramodel::FoPra.__init__)


def test_fopramodel::fopra_constructor_args():
    sig = inspect.signature(fopramodel::FoPra.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "maxNumberOfStudents" in params, "Missing parameter 'maxNumberOfStudents'"
    assert "description" in params, "Missing parameter 'description'"
    assert "start" in params, "Missing parameter 'start'"
    assert "status" in params, "Missing parameter 'status'"
    assert "title" in params, "Missing parameter 'title'"

def test_fopramodel::fopra_has_end():
    assert hasattr(fopramodel::FoPra, "end")
    descriptor = None
    for klass in fopramodel::FoPra.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel::fopra_has_maxNumberOfStudents():
    assert hasattr(fopramodel::FoPra, "maxNumberOfStudents")
    descriptor = None
    for klass in fopramodel::FoPra.__mro__:
        if "maxNumberOfStudents" in klass.__dict__:
            descriptor = klass.__dict__["maxNumberOfStudents"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel::fopra_has_description():
    assert hasattr(fopramodel::FoPra, "description")
    descriptor = None
    for klass in fopramodel::FoPra.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel::fopra_has_start():
    assert hasattr(fopramodel::FoPra, "start")
    descriptor = None
    for klass in fopramodel::FoPra.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel::fopra_has_status():
    assert hasattr(fopramodel::FoPra, "status")
    descriptor = None
    for klass in fopramodel::FoPra.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_fopramodel::fopra_has_title():
    assert hasattr(fopramodel::FoPra, "title")
    descriptor = None
    for klass in fopramodel::FoPra.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_status_exists():
    # Check that the Enumeration exists
    assert Status is not None

def test_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Status]
    expected_literals = [
        "pending",
        "completed",
        "inprocess",
        "cancelled",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Status"

def test_course_exists():
    # Check that the Enumeration exists
    assert Course is not None

def test_course_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Course]
    expected_literals = [
        "InfoMinorSubject",
        "InfoBSc",
        "InfoPostGraduate",
        "InfoMSc",
        "InfoDiplom",
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
        "Tool",
        "Method",
        "ProgrammingLanguage",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuxiliaryKind"


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
fopramodel::Auxiliary_strategy = st.builds(
    fopramodel::Auxiliary,
    kind=
        safe_text,
    description=
        safe_text
)
fopramodel::ResearchGroup_strategy = st.builds(
    fopramodel::ResearchGroup,
    name=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
fopramodel::Professor_strategy = st.builds(
    fopramodel::Professor,
)
fopramodel::Student_strategy = st.builds(
    fopramodel::Student,
    course=
        safe_text,
    matrikel=
        safe_text
)
fopramodel::Associate_strategy = st.builds(
    fopramodel::Associate,
)
fopramodel::ExternalAdvisor_strategy = st.builds(
    fopramodel::ExternalAdvisor,
    information=
        safe_text
)
fopramodel::Person_strategy = st.builds(
    fopramodel::Person,
    lastname=
        safe_text,
    forename=
        safe_text
)
fopramodel::FoPraManagementSystem_strategy = st.builds(
    fopramodel::FoPraManagementSystem,
)
fopramodel::FoPra_strategy = st.builds(
    fopramodel::FoPra,
    end=
        st.dates(),
    maxNumberOfStudents=
        st.integers(),
    description=
        safe_text,
    start=
        st.dates(),
    status=
        safe_text,
    title=
        safe_text
)

@given(instance=fopramodel::Auxiliary_strategy)
@settings(max_examples=50)
def test_fopramodel::auxiliary_instantiation(instance):
    assert isinstance(instance, fopramodel::Auxiliary)

@given(instance=fopramodel::Auxiliary_strategy)
def test_fopramodel::auxiliary_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=fopramodel::Auxiliary_strategy)
def test_fopramodel::auxiliary_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=fopramodel::Auxiliary_strategy)
def test_fopramodel::auxiliary_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fopramodel::Auxiliary_strategy)
def test_fopramodel::auxiliary_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fopramodel::ResearchGroup_strategy)
@settings(max_examples=50)
def test_fopramodel::researchgroup_instantiation(instance):
    assert isinstance(instance, fopramodel::ResearchGroup)

@given(instance=fopramodel::ResearchGroup_strategy)
def test_fopramodel::researchgroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fopramodel::ResearchGroup_strategy)
def test_fopramodel::researchgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=fopramodel::Professor_strategy)
@settings(max_examples=50)
def test_fopramodel::professor_instantiation(instance):
    assert isinstance(instance, fopramodel::Professor)

@given(instance=fopramodel::Student_strategy)
@settings(max_examples=50)
def test_fopramodel::student_instantiation(instance):
    assert isinstance(instance, fopramodel::Student)

@given(instance=fopramodel::Student_strategy)
def test_fopramodel::student_course_type(instance):
    assert isinstance(instance.course, str)


@given(instance=fopramodel::Student_strategy)
def test_fopramodel::student_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original

@given(instance=fopramodel::Student_strategy)
def test_fopramodel::student_matrikel_type(instance):
    assert isinstance(instance.matrikel, str)


@given(instance=fopramodel::Student_strategy)
def test_fopramodel::student_matrikel_setter(instance):
    original = instance.matrikel
    instance.matrikel = original
    assert instance.matrikel == original

@given(instance=fopramodel::Associate_strategy)
@settings(max_examples=50)
def test_fopramodel::associate_instantiation(instance):
    assert isinstance(instance, fopramodel::Associate)

@given(instance=fopramodel::ExternalAdvisor_strategy)
@settings(max_examples=50)
def test_fopramodel::externaladvisor_instantiation(instance):
    assert isinstance(instance, fopramodel::ExternalAdvisor)

@given(instance=fopramodel::ExternalAdvisor_strategy)
def test_fopramodel::externaladvisor_information_type(instance):
    assert isinstance(instance.information, str)


@given(instance=fopramodel::ExternalAdvisor_strategy)
def test_fopramodel::externaladvisor_information_setter(instance):
    original = instance.information
    instance.information = original
    assert instance.information == original

@given(instance=fopramodel::Person_strategy)
@settings(max_examples=50)
def test_fopramodel::person_instantiation(instance):
    assert isinstance(instance, fopramodel::Person)

@given(instance=fopramodel::Person_strategy)
def test_fopramodel::person_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=fopramodel::Person_strategy)
def test_fopramodel::person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=fopramodel::Person_strategy)
def test_fopramodel::person_forename_type(instance):
    assert isinstance(instance.forename, str)


@given(instance=fopramodel::Person_strategy)
def test_fopramodel::person_forename_setter(instance):
    original = instance.forename
    instance.forename = original
    assert instance.forename == original

@given(instance=fopramodel::FoPraManagementSystem_strategy)
@settings(max_examples=50)
def test_fopramodel::fopramanagementsystem_instantiation(instance):
    assert isinstance(instance, fopramodel::FoPraManagementSystem)

@given(instance=fopramodel::FoPra_strategy)
@settings(max_examples=50)
def test_fopramodel::fopra_instantiation(instance):
    assert isinstance(instance, fopramodel::FoPra)

@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_end_type(instance):
    assert isinstance(instance.end, date)


@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_maxNumberOfStudents_type(instance):
    assert isinstance(instance.maxNumberOfStudents, int)


@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_maxNumberOfStudents_setter(instance):
    original = instance.maxNumberOfStudents
    instance.maxNumberOfStudents = original
    assert instance.maxNumberOfStudents == original

@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_start_type(instance):
    assert isinstance(instance.start, date)


@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=fopramodel::FoPra_strategy)
def test_fopramodel::fopra_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original
