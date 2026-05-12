import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    releng_Promotion,
    Repository,
    releng_CompositeRepository,
    releng_Criterion,
    releng_Repository,
    releng_BuildJob,
    releng_Server,
    BuildType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_releng_promotion_is_not_abstract():
    assert not inspect.isabstract(releng_Promotion)


def test_releng_promotion_constructor_exists():
    assert callable(releng_Promotion.__init__)


def test_releng_promotion_constructor_args():
    sig = inspect.signature(releng_Promotion.__init__)
    params = list(sig.parameters.keys())
    assert "buildType" in params, "Missing parameter 'buildType'"

def test_releng_promotion_has_buildType():
    assert hasattr(releng_Promotion, "buildType")
    descriptor = None
    for klass in releng_Promotion.__mro__:
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



def test_releng_compositerepository_is_not_abstract():
    assert not inspect.isabstract(releng_CompositeRepository)


def test_releng_compositerepository_constructor_exists():
    assert callable(releng_CompositeRepository.__init__)


def test_releng_compositerepository_constructor_args():
    sig = inspect.signature(releng_CompositeRepository.__init__)
    params = list(sig.parameters.keys())



def test_releng_criterion_is_not_abstract():
    assert not inspect.isabstract(releng_Criterion)


def test_releng_criterion_constructor_exists():
    assert callable(releng_Criterion.__init__)


def test_releng_criterion_constructor_args():
    sig = inspect.signature(releng_Criterion.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_releng_criterion_has_description():
    assert hasattr(releng_Criterion, "description")
    descriptor = None
    for klass in releng_Criterion.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_releng_repository_is_not_abstract():
    assert not inspect.isabstract(releng_Repository)


def test_releng_repository_constructor_exists():
    assert callable(releng_Repository.__init__)


def test_releng_repository_constructor_args():
    sig = inspect.signature(releng_Repository.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_releng_repository_has_location():
    assert hasattr(releng_Repository, "location")
    descriptor = None
    for klass in releng_Repository.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_releng_buildjob_is_not_abstract():
    assert not inspect.isabstract(releng_BuildJob)


def test_releng_buildjob_constructor_exists():
    assert callable(releng_BuildJob.__init__)


def test_releng_buildjob_constructor_args():
    sig = inspect.signature(releng_BuildJob.__init__)
    params = list(sig.parameters.keys())
    assert "sourceBranch" in params, "Missing parameter 'sourceBranch'"
    assert "buckminsterComponent" in params, "Missing parameter 'buckminsterComponent'"
    assert "name" in params, "Missing parameter 'name'"
    assert "types" in params, "Missing parameter 'types'"

def test_releng_buildjob_has_sourceBranch():
    assert hasattr(releng_BuildJob, "sourceBranch")
    descriptor = None
    for klass in releng_BuildJob.__mro__:
        if "sourceBranch" in klass.__dict__:
            descriptor = klass.__dict__["sourceBranch"]
            break
    assert isinstance(descriptor, property)

def test_releng_buildjob_has_buckminsterComponent():
    assert hasattr(releng_BuildJob, "buckminsterComponent")
    descriptor = None
    for klass in releng_BuildJob.__mro__:
        if "buckminsterComponent" in klass.__dict__:
            descriptor = klass.__dict__["buckminsterComponent"]
            break
    assert isinstance(descriptor, property)

def test_releng_buildjob_has_name():
    assert hasattr(releng_BuildJob, "name")
    descriptor = None
    for klass in releng_BuildJob.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_releng_buildjob_has_types():
    assert hasattr(releng_BuildJob, "types")
    descriptor = None
    for klass in releng_BuildJob.__mro__:
        if "types" in klass.__dict__:
            descriptor = klass.__dict__["types"]
            break
    assert isinstance(descriptor, property)



def test_releng_server_is_not_abstract():
    assert not inspect.isabstract(releng_Server)


def test_releng_server_constructor_exists():
    assert callable(releng_Server.__init__)


def test_releng_server_constructor_args():
    sig = inspect.signature(releng_Server.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_releng_server_has_name():
    assert hasattr(releng_Server, "name")
    descriptor = None
    for klass in releng_Server.__mro__:
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
        "R",
        "I",
        "N",
        "S",
        "M",
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
releng_Promotion_strategy = st.builds(
    releng_Promotion,
    buildType=
        safe_text
)
Repository_strategy = st.builds(
    Repository,
)
releng_CompositeRepository_strategy = st.builds(
    releng_CompositeRepository,
)
releng_Criterion_strategy = st.builds(
    releng_Criterion,
    description=
        safe_text
)
releng_Repository_strategy = st.builds(
    releng_Repository,
    location=
        safe_text
)
releng_BuildJob_strategy = st.builds(
    releng_BuildJob,
    sourceBranch=
        safe_text,
    buckminsterComponent=
        safe_text,
    name=
        safe_text,
    types=
        safe_text
)
releng_Server_strategy = st.builds(
    releng_Server,
    name=
        safe_text
)

@given(instance=releng_Promotion_strategy)
@settings(max_examples=50)
def test_releng_promotion_instantiation(instance):
    assert isinstance(instance, releng_Promotion)



@given(instance=releng_Promotion_strategy)
def test_releng_promotion_buildType_setter(instance):
    original = instance.buildType
    instance.buildType = original
    assert instance.buildType == original

@given(instance=Repository_strategy)
@settings(max_examples=50)
def test_repository_instantiation(instance):
    assert isinstance(instance, Repository)

@given(instance=releng_CompositeRepository_strategy)
@settings(max_examples=50)
def test_releng_compositerepository_instantiation(instance):
    assert isinstance(instance, releng_CompositeRepository)

@given(instance=releng_Criterion_strategy)
@settings(max_examples=50)
def test_releng_criterion_instantiation(instance):
    assert isinstance(instance, releng_Criterion)



@given(instance=releng_Criterion_strategy)
def test_releng_criterion_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=releng_Repository_strategy)
@settings(max_examples=50)
def test_releng_repository_instantiation(instance):
    assert isinstance(instance, releng_Repository)



@given(instance=releng_Repository_strategy)
def test_releng_repository_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=releng_BuildJob_strategy)
@settings(max_examples=50)
def test_releng_buildjob_instantiation(instance):
    assert isinstance(instance, releng_BuildJob)



@given(instance=releng_BuildJob_strategy)
def test_releng_buildjob_sourceBranch_setter(instance):
    original = instance.sourceBranch
    instance.sourceBranch = original
    assert instance.sourceBranch == original



@given(instance=releng_BuildJob_strategy)
def test_releng_buildjob_buckminsterComponent_setter(instance):
    original = instance.buckminsterComponent
    instance.buckminsterComponent = original
    assert instance.buckminsterComponent == original



@given(instance=releng_BuildJob_strategy)
def test_releng_buildjob_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=releng_BuildJob_strategy)
def test_releng_buildjob_types_setter(instance):
    original = instance.types
    instance.types = original
    assert instance.types == original

@given(instance=releng_Server_strategy)
@settings(max_examples=50)
def test_releng_server_instantiation(instance):
    assert isinstance(instance, releng_Server)



@given(instance=releng_Server_strategy)
def test_releng_server_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
