import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    conf::Person,
    conf::RevisionNote,
    conf::Chapter,
    conf::Evaluation,
    Person,
    conf::Publication,
    conf::Researcher,
    conf::Contribution,
    conf::SteeringComitee,
    conf::ProgramComitee,
    conf::Location,
    conf::Session,
    conf::RevisionProcess,
    conf::Conference,
    conf::Admin,
    conf::System,
    conf::Laboratory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_conf::person_is_not_abstract():
    assert not inspect.isabstract(conf::Person)


def test_conf::person_constructor_exists():
    assert callable(conf::Person.__init__)


def test_conf::person_constructor_args():
    sig = inspect.signature(conf::Person.__init__)
    params = list(sig.parameters.keys())



def test_conf::revisionnote_is_not_abstract():
    assert not inspect.isabstract(conf::RevisionNote)


def test_conf::revisionnote_constructor_exists():
    assert callable(conf::RevisionNote.__init__)


def test_conf::revisionnote_constructor_args():
    sig = inspect.signature(conf::RevisionNote.__init__)
    params = list(sig.parameters.keys())



def test_conf::chapter_is_not_abstract():
    assert not inspect.isabstract(conf::Chapter)


def test_conf::chapter_constructor_exists():
    assert callable(conf::Chapter.__init__)


def test_conf::chapter_constructor_args():
    sig = inspect.signature(conf::Chapter.__init__)
    params = list(sig.parameters.keys())



def test_conf::evaluation_is_not_abstract():
    assert not inspect.isabstract(conf::Evaluation)


def test_conf::evaluation_constructor_exists():
    assert callable(conf::Evaluation.__init__)


def test_conf::evaluation_constructor_args():
    sig = inspect.signature(conf::Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_conf::publication_is_not_abstract():
    assert not inspect.isabstract(conf::Publication)


def test_conf::publication_constructor_exists():
    assert callable(conf::Publication.__init__)


def test_conf::publication_constructor_args():
    sig = inspect.signature(conf::Publication.__init__)
    params = list(sig.parameters.keys())



def test_conf::researcher_is_not_abstract():
    assert not inspect.isabstract(conf::Researcher)


def test_conf::researcher_constructor_exists():
    assert callable(conf::Researcher.__init__)


def test_conf::researcher_constructor_args():
    sig = inspect.signature(conf::Researcher.__init__)
    params = list(sig.parameters.keys())



def test_conf::contribution_is_not_abstract():
    assert not inspect.isabstract(conf::Contribution)


def test_conf::contribution_constructor_exists():
    assert callable(conf::Contribution.__init__)


def test_conf::contribution_constructor_args():
    sig = inspect.signature(conf::Contribution.__init__)
    params = list(sig.parameters.keys())



def test_conf::steeringcomitee_is_not_abstract():
    assert not inspect.isabstract(conf::SteeringComitee)


def test_conf::steeringcomitee_constructor_exists():
    assert callable(conf::SteeringComitee.__init__)


def test_conf::steeringcomitee_constructor_args():
    sig = inspect.signature(conf::SteeringComitee.__init__)
    params = list(sig.parameters.keys())



def test_conf::programcomitee_is_not_abstract():
    assert not inspect.isabstract(conf::ProgramComitee)


def test_conf::programcomitee_constructor_exists():
    assert callable(conf::ProgramComitee.__init__)


def test_conf::programcomitee_constructor_args():
    sig = inspect.signature(conf::ProgramComitee.__init__)
    params = list(sig.parameters.keys())



def test_conf::location_is_not_abstract():
    assert not inspect.isabstract(conf::Location)


def test_conf::location_constructor_exists():
    assert callable(conf::Location.__init__)


def test_conf::location_constructor_args():
    sig = inspect.signature(conf::Location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_conf::location_has_name():
    assert hasattr(conf::Location, "name")
    descriptor = None
    for klass in conf::Location.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conf::session_is_not_abstract():
    assert not inspect.isabstract(conf::Session)


def test_conf::session_constructor_exists():
    assert callable(conf::Session.__init__)


def test_conf::session_constructor_args():
    sig = inspect.signature(conf::Session.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_conf::session_has_year():
    assert hasattr(conf::Session, "year")
    descriptor = None
    for klass in conf::Session.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_conf::revisionprocess_is_not_abstract():
    assert not inspect.isabstract(conf::RevisionProcess)


def test_conf::revisionprocess_constructor_exists():
    assert callable(conf::RevisionProcess.__init__)


def test_conf::revisionprocess_constructor_args():
    sig = inspect.signature(conf::RevisionProcess.__init__)
    params = list(sig.parameters.keys())



def test_conf::conference_is_not_abstract():
    assert not inspect.isabstract(conf::Conference)


def test_conf::conference_constructor_exists():
    assert callable(conf::Conference.__init__)


def test_conf::conference_constructor_args():
    sig = inspect.signature(conf::Conference.__init__)
    params = list(sig.parameters.keys())



def test_conf::admin_is_not_abstract():
    assert not inspect.isabstract(conf::Admin)


def test_conf::admin_constructor_exists():
    assert callable(conf::Admin.__init__)


def test_conf::admin_constructor_args():
    sig = inspect.signature(conf::Admin.__init__)
    params = list(sig.parameters.keys())



def test_conf::system_is_not_abstract():
    assert not inspect.isabstract(conf::System)


def test_conf::system_constructor_exists():
    assert callable(conf::System.__init__)


def test_conf::system_constructor_args():
    sig = inspect.signature(conf::System.__init__)
    params = list(sig.parameters.keys())



def test_conf::laboratory_is_not_abstract():
    assert not inspect.isabstract(conf::Laboratory)


def test_conf::laboratory_constructor_exists():
    assert callable(conf::Laboratory.__init__)


def test_conf::laboratory_constructor_args():
    sig = inspect.signature(conf::Laboratory.__init__)
    params = list(sig.parameters.keys())


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
conf::Person_strategy = st.builds(
    conf::Person,
)
conf::RevisionNote_strategy = st.builds(
    conf::RevisionNote,
)
conf::Chapter_strategy = st.builds(
    conf::Chapter,
)
conf::Evaluation_strategy = st.builds(
    conf::Evaluation,
)
Person_strategy = st.builds(
    Person,
)
conf::Publication_strategy = st.builds(
    conf::Publication,
)
conf::Researcher_strategy = st.builds(
    conf::Researcher,
)
conf::Contribution_strategy = st.builds(
    conf::Contribution,
)
conf::SteeringComitee_strategy = st.builds(
    conf::SteeringComitee,
)
conf::ProgramComitee_strategy = st.builds(
    conf::ProgramComitee,
)
conf::Location_strategy = st.builds(
    conf::Location,
    name=
        safe_text
)
conf::Session_strategy = st.builds(
    conf::Session,
    year=
        safe_text
)
conf::RevisionProcess_strategy = st.builds(
    conf::RevisionProcess,
)
conf::Conference_strategy = st.builds(
    conf::Conference,
)
conf::Admin_strategy = st.builds(
    conf::Admin,
)
conf::System_strategy = st.builds(
    conf::System,
)
conf::Laboratory_strategy = st.builds(
    conf::Laboratory,
)

@given(instance=conf::Person_strategy)
@settings(max_examples=50)
def test_conf::person_instantiation(instance):
    assert isinstance(instance, conf::Person)

@given(instance=conf::RevisionNote_strategy)
@settings(max_examples=50)
def test_conf::revisionnote_instantiation(instance):
    assert isinstance(instance, conf::RevisionNote)

@given(instance=conf::Chapter_strategy)
@settings(max_examples=50)
def test_conf::chapter_instantiation(instance):
    assert isinstance(instance, conf::Chapter)

@given(instance=conf::Evaluation_strategy)
@settings(max_examples=50)
def test_conf::evaluation_instantiation(instance):
    assert isinstance(instance, conf::Evaluation)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=conf::Publication_strategy)
@settings(max_examples=50)
def test_conf::publication_instantiation(instance):
    assert isinstance(instance, conf::Publication)

@given(instance=conf::Researcher_strategy)
@settings(max_examples=50)
def test_conf::researcher_instantiation(instance):
    assert isinstance(instance, conf::Researcher)

@given(instance=conf::Contribution_strategy)
@settings(max_examples=50)
def test_conf::contribution_instantiation(instance):
    assert isinstance(instance, conf::Contribution)

@given(instance=conf::SteeringComitee_strategy)
@settings(max_examples=50)
def test_conf::steeringcomitee_instantiation(instance):
    assert isinstance(instance, conf::SteeringComitee)

@given(instance=conf::ProgramComitee_strategy)
@settings(max_examples=50)
def test_conf::programcomitee_instantiation(instance):
    assert isinstance(instance, conf::ProgramComitee)

@given(instance=conf::Location_strategy)
@settings(max_examples=50)
def test_conf::location_instantiation(instance):
    assert isinstance(instance, conf::Location)

@given(instance=conf::Location_strategy)
def test_conf::location_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=conf::Location_strategy)
def test_conf::location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=conf::Session_strategy)
@settings(max_examples=50)
def test_conf::session_instantiation(instance):
    assert isinstance(instance, conf::Session)

@given(instance=conf::Session_strategy)
def test_conf::session_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=conf::Session_strategy)
def test_conf::session_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=conf::RevisionProcess_strategy)
@settings(max_examples=50)
def test_conf::revisionprocess_instantiation(instance):
    assert isinstance(instance, conf::RevisionProcess)

@given(instance=conf::Conference_strategy)
@settings(max_examples=50)
def test_conf::conference_instantiation(instance):
    assert isinstance(instance, conf::Conference)

@given(instance=conf::Admin_strategy)
@settings(max_examples=50)
def test_conf::admin_instantiation(instance):
    assert isinstance(instance, conf::Admin)

@given(instance=conf::System_strategy)
@settings(max_examples=50)
def test_conf::system_instantiation(instance):
    assert isinstance(instance, conf::System)

@given(instance=conf::Laboratory_strategy)
@settings(max_examples=50)
def test_conf::laboratory_instantiation(instance):
    assert isinstance(instance, conf::Laboratory)
