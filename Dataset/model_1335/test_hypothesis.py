import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    classescs_RootCS,
    classescs_PathNameCS,
    NamedElementCS,
    classescs_ClassCS,
    classescs_PathElementCS,
    classescs_PackageCS,
    classescs_NamedElementCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classescs_rootcs_is_not_abstract():
    assert not inspect.isabstract(classescs_RootCS)


def test_classescs_rootcs_constructor_exists():
    assert callable(classescs_RootCS.__init__)


def test_classescs_rootcs_constructor_args():
    sig = inspect.signature(classescs_RootCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(classescs_PathNameCS)


def test_classescs_pathnamecs_constructor_exists():
    assert callable(classescs_PathNameCS.__init__)


def test_classescs_pathnamecs_constructor_args():
    sig = inspect.signature(classescs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_classcs_is_not_abstract():
    assert not inspect.isabstract(classescs_ClassCS)


def test_classescs_classcs_constructor_exists():
    assert callable(classescs_ClassCS.__init__)


def test_classescs_classcs_constructor_args():
    sig = inspect.signature(classescs_ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs_PathElementCS)


def test_classescs_pathelementcs_constructor_exists():
    assert callable(classescs_PathElementCS.__init__)


def test_classescs_pathelementcs_constructor_args():
    sig = inspect.signature(classescs_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_packagecs_is_not_abstract():
    assert not inspect.isabstract(classescs_PackageCS)


def test_classescs_packagecs_constructor_exists():
    assert callable(classescs_PackageCS.__init__)


def test_classescs_packagecs_constructor_args():
    sig = inspect.signature(classescs_PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_classescs_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs_NamedElementCS)


def test_classescs_namedelementcs_constructor_exists():
    assert callable(classescs_NamedElementCS.__init__)


def test_classescs_namedelementcs_constructor_args():
    sig = inspect.signature(classescs_NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classescs_namedelementcs_has_name():
    assert hasattr(classescs_NamedElementCS, "name")
    descriptor = None
    for klass in classescs_NamedElementCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
classescs_RootCS_strategy = st.builds(
    classescs_RootCS,
)
classescs_PathNameCS_strategy = st.builds(
    classescs_PathNameCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
classescs_ClassCS_strategy = st.builds(
    classescs_ClassCS,
)
classescs_PathElementCS_strategy = st.builds(
    classescs_PathElementCS,
)
classescs_PackageCS_strategy = st.builds(
    classescs_PackageCS,
)
classescs_NamedElementCS_strategy = st.builds(
    classescs_NamedElementCS,
    name=
        safe_text
)

@given(instance=classescs_RootCS_strategy)
@settings(max_examples=50)
def test_classescs_rootcs_instantiation(instance):
    assert isinstance(instance, classescs_RootCS)

@given(instance=classescs_PathNameCS_strategy)
@settings(max_examples=50)
def test_classescs_pathnamecs_instantiation(instance):
    assert isinstance(instance, classescs_PathNameCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=classescs_ClassCS_strategy)
@settings(max_examples=50)
def test_classescs_classcs_instantiation(instance):
    assert isinstance(instance, classescs_ClassCS)

@given(instance=classescs_PathElementCS_strategy)
@settings(max_examples=50)
def test_classescs_pathelementcs_instantiation(instance):
    assert isinstance(instance, classescs_PathElementCS)

@given(instance=classescs_PackageCS_strategy)
@settings(max_examples=50)
def test_classescs_packagecs_instantiation(instance):
    assert isinstance(instance, classescs_PackageCS)

@given(instance=classescs_NamedElementCS_strategy)
@settings(max_examples=50)
def test_classescs_namedelementcs_instantiation(instance):
    assert isinstance(instance, classescs_NamedElementCS)



@given(instance=classescs_NamedElementCS_strategy)
def test_classescs_namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
