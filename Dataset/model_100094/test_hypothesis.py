import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    releng::Promotion,
    Repository,
    releng::CompositeRepository,
    releng::Criterion,
    releng::Repository,
    releng::BuildJob,
    releng::Server,
    BuildType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_releng::promotion_is_not_abstract():
    assert not inspect.isabstract(releng::Promotion)


def test_releng::promotion_constructor_exists():
    assert callable(releng::Promotion.__init__)


def test_releng::promotion_constructor_args():
    sig = inspect.signature(releng::Promotion.__init__)
    params = list(sig.parameters.keys())
    assert "buildType" in params, "Missing parameter 'buildType'"

def test_releng::promotion_has_buildType():
    assert hasattr(releng::Promotion, "buildType")
    descriptor = None
    for klass in releng::Promotion.__mro__:
        if "buildType" in klass.__dict__:
            descriptor = klass.__dict__["buildType"]
            break
    assert isinstance(descriptor, property)



def test_repository_is_not_abstract():
    assert not inspect.isabstract(Repository)


def test_repository_constructor_exists():
    assert callable(Repository.__init__)


def test_repository_constructor_args():
    sig = inspect.signature(Repository.__init__)
    params = list(sig.parameters.keys())



def test_releng::compositerepository_is_not_abstract():
    assert not inspect.isabstract(releng::CompositeRepository)


def test_releng::compositerepository_constructor_exists():
    assert callable(releng::CompositeRepository.__init__)


def test_releng::compositerepository_constructor_args():
    sig = inspect.signature(releng::CompositeRepository.__init__)
    params = list(sig.parameters.keys())



def test_releng::criterion_is_not_abstract():
    assert not inspect.isabstract(releng::Criterion)


def test_releng::criterion_constructor_exists():
    assert callable(releng::Criterion.__init__)


def test_releng::criterion_constructor_args():
    sig = inspect.signature(releng::Criterion.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_releng::criterion_has_description():
    assert hasattr(releng::Criterion, "description")
    descriptor = None
    for klass in releng::Criterion.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_releng::repository_is_not_abstract():
    assert not inspect.isabstract(releng::Repository)


def test_releng::repository_constructor_exists():
    assert callable(releng::Repository.__init__)


def test_releng::repository_constructor_args():
    sig = inspect.signature(releng::Repository.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_releng::repository_has_location():
    assert hasattr(releng::Repository, "location")
    descriptor = None
    for klass in releng::Repository.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_releng::buildjob_is_not_abstract():
    assert not inspect.isabstract(releng::BuildJob)


def test_releng::buildjob_constructor_exists():
    assert callable(releng::BuildJob.__init__)


def test_releng::buildjob_constructor_args():
    sig = inspect.signature(releng::BuildJob.__init__)
    params = list(sig.parameters.keys())
    assert "buckminsterComponent" in params, "Missing parameter 'buckminsterComponent'"
    assert "sourceBranch" in params, "Missing parameter 'sourceBranch'"
    assert "name" in params, "Missing parameter 'name'"
    assert "types" in params, "Missing parameter 'types'"

def test_releng::buildjob_has_buckminsterComponent():
    assert hasattr(releng::BuildJob, "buckminsterComponent")
    descriptor = None
    for klass in releng::BuildJob.__mro__:
        if "buckminsterComponent" in klass.__dict__:
            descriptor = klass.__dict__["buckminsterComponent"]
            break
    assert isinstance(descriptor, property)

def test_releng::buildjob_has_sourceBranch():
    assert hasattr(releng::BuildJob, "sourceBranch")
    descriptor = None
    for klass in releng::BuildJob.__mro__:
        if "sourceBranch" in klass.__dict__:
            descriptor = klass.__dict__["sourceBranch"]
            break
    assert isinstance(descriptor, property)

def test_releng::buildjob_has_name():
    assert hasattr(releng::BuildJob, "name")
    descriptor = None
    for klass in releng::BuildJob.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_releng::buildjob_has_types():
    assert hasattr(releng::BuildJob, "types")
    descriptor = None
    for klass in releng::BuildJob.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
            break
    assert isinstance(descriptor, property)



def test_releng::server_is_not_abstract():
    assert not inspect.isabstract(releng::Server)


def test_releng::server_constructor_exists():
    assert callable(releng::Server.__init__)


def test_releng::server_constructor_args():
    sig = inspect.signature(releng::Server.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_releng::server_has_name():
    assert hasattr(releng::Server, "name")
    descriptor = None
    for klass in releng::Server.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_buildtype_exists():
    # Check that the Enumeration exists
    assert BuildType is not None

def test_buildtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuildType]
    expected_literals = [
        "N",
        "M",
        "I",
        "S",
        "R",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuildType"


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
releng::Promotion_strategy = st.builds(
    releng::Promotion,
    buildType=
        safe_text
)
Repository_strategy = st.builds(
    Repository,
)
releng::CompositeRepository_strategy = st.builds(
    releng::CompositeRepository,
)
releng::Criterion_strategy = st.builds(
    releng::Criterion,
    description=
        safe_text
)
releng::Repository_strategy = st.builds(
    releng::Repository,
    location=
        safe_text
)
releng::BuildJob_strategy = st.builds(
    releng::BuildJob,
    buckminsterComponent=
        safe_text,
    sourceBranch=
        safe_text,
    name=
        safe_text,
    types=
        safe_text
)
releng::Server_strategy = st.builds(
    releng::Server,
    name=
        safe_text
)

@given(instance=releng::Promotion_strategy)
@settings(max_examples=50)
def test_releng::promotion_instantiation(instance):
    assert isinstance(instance, releng::Promotion)

@given(instance=releng::Promotion_strategy)
def test_releng::promotion_buildType_type(instance):
    assert isinstance(instance.buildType, str)


@given(instance=releng::Promotion_strategy)
def test_releng::promotion_buildType_setter(instance):
    original = instance.buildType
    instance.buildType = original
    assert instance.buildType == original

@given(instance=Repository_strategy)
@settings(max_examples=50)
def test_repository_instantiation(instance):
    assert isinstance(instance, Repository)

@given(instance=releng::CompositeRepository_strategy)
@settings(max_examples=50)
def test_releng::compositerepository_instantiation(instance):
    assert isinstance(instance, releng::CompositeRepository)

@given(instance=releng::Criterion_strategy)
@settings(max_examples=50)
def test_releng::criterion_instantiation(instance):
    assert isinstance(instance, releng::Criterion)

@given(instance=releng::Criterion_strategy)
def test_releng::criterion_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=releng::Criterion_strategy)
def test_releng::criterion_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=releng::Repository_strategy)
@settings(max_examples=50)
def test_releng::repository_instantiation(instance):
    assert isinstance(instance, releng::Repository)

@given(instance=releng::Repository_strategy)
def test_releng::repository_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=releng::Repository_strategy)
def test_releng::repository_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=releng::BuildJob_strategy)
@settings(max_examples=50)
def test_releng::buildjob_instantiation(instance):
    assert isinstance(instance, releng::BuildJob)

@given(instance=releng::BuildJob_strategy)
def test_releng::buildjob_buckminsterComponent_type(instance):
    assert isinstance(instance.buckminsterComponent, str)


@given(instance=releng::BuildJob_strategy)
def test_releng::buildjob_buckminsterComponent_setter(instance):
    original = instance.buckminsterComponent
    instance.buckminsterComponent = original
    assert instance.buckminsterComponent == original

@given(instance=releng::BuildJob_strategy)
def test_releng::buildjob_sourceBranch_type(instance):
    assert isinstance(instance.sourceBranch, str)


@given(instance=releng::BuildJob_strategy)
def test_releng::buildjob_sourceBranch_setter(instance):
    original = instance.sourceBranch
    instance.sourceBranch = original
    assert instance.sourceBranch == original

@given(instance=releng::BuildJob_strategy)
def test_releng::buildjob_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=releng::BuildJob_strategy)
def test_releng::buildjob_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=releng::BuildJob_strategy)
def test_releng::buildjob_types_type(instance):
    assert isinstance(instance.types, str)


@given(instance=releng::BuildJob_strategy)
def test_releng::buildjob_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original

@given(instance=releng::Server_strategy)
@settings(max_examples=50)
def test_releng::server_instantiation(instance):
    assert isinstance(instance, releng::Server)

@given(instance=releng::Server_strategy)
def test_releng::server_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=releng::Server_strategy)
def test_releng::server_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
