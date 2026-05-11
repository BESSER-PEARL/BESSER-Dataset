import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classescstraces::Root,
    classescstraces::RootCS,
    classescstraces::RootCS2Root,
    classescstraces::Class,
    classescstraces::ClassCS,
    classescstraces::ClassCS2Class,
    classescstraces::Package,
    classescstraces::PackageCS,
    classescstraces::PackageCS2Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classescstraces::root_is_not_abstract():
    assert not inspect.isabstract(classescstraces::Root)


def test_classescstraces::root_constructor_exists():
    assert callable(classescstraces::Root.__init__)


def test_classescstraces::root_constructor_args():
    sig = inspect.signature(classescstraces::Root.__init__)
    params = list(sig.parameters.keys())



def test_classescstraces::rootcs_is_not_abstract():
    assert not inspect.isabstract(classescstraces::RootCS)


def test_classescstraces::rootcs_constructor_exists():
    assert callable(classescstraces::RootCS.__init__)


def test_classescstraces::rootcs_constructor_args():
    sig = inspect.signature(classescstraces::RootCS.__init__)
    params = list(sig.parameters.keys())



def test_classescstraces::rootcs2root_is_not_abstract():
    assert not inspect.isabstract(classescstraces::RootCS2Root)


def test_classescstraces::rootcs2root_constructor_exists():
    assert callable(classescstraces::RootCS2Root.__init__)


def test_classescstraces::rootcs2root_constructor_args():
    sig = inspect.signature(classescstraces::RootCS2Root.__init__)
    params = list(sig.parameters.keys())



def test_classescstraces::class_is_not_abstract():
    assert not inspect.isabstract(classescstraces::Class)


def test_classescstraces::class_constructor_exists():
    assert callable(classescstraces::Class.__init__)


def test_classescstraces::class_constructor_args():
    sig = inspect.signature(classescstraces::Class.__init__)
    params = list(sig.parameters.keys())



def test_classescstraces::classcs_is_not_abstract():
    assert not inspect.isabstract(classescstraces::ClassCS)


def test_classescstraces::classcs_constructor_exists():
    assert callable(classescstraces::ClassCS.__init__)


def test_classescstraces::classcs_constructor_args():
    sig = inspect.signature(classescstraces::ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_classescstraces::classcs2class_is_not_abstract():
    assert not inspect.isabstract(classescstraces::ClassCS2Class)


def test_classescstraces::classcs2class_constructor_exists():
    assert callable(classescstraces::ClassCS2Class.__init__)


def test_classescstraces::classcs2class_constructor_args():
    sig = inspect.signature(classescstraces::ClassCS2Class.__init__)
    params = list(sig.parameters.keys())



def test_classescstraces::package_is_not_abstract():
    assert not inspect.isabstract(classescstraces::Package)


def test_classescstraces::package_constructor_exists():
    assert callable(classescstraces::Package.__init__)


def test_classescstraces::package_constructor_args():
    sig = inspect.signature(classescstraces::Package.__init__)
    params = list(sig.parameters.keys())



def test_classescstraces::packagecs_is_not_abstract():
    assert not inspect.isabstract(classescstraces::PackageCS)


def test_classescstraces::packagecs_constructor_exists():
    assert callable(classescstraces::PackageCS.__init__)


def test_classescstraces::packagecs_constructor_args():
    sig = inspect.signature(classescstraces::PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_classescstraces::packagecs2package_is_not_abstract():
    assert not inspect.isabstract(classescstraces::PackageCS2Package)


def test_classescstraces::packagecs2package_constructor_exists():
    assert callable(classescstraces::PackageCS2Package.__init__)


def test_classescstraces::packagecs2package_constructor_args():
    sig = inspect.signature(classescstraces::PackageCS2Package.__init__)
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
classescstraces::Root_strategy = st.builds(
    classescstraces::Root,
)
classescstraces::RootCS_strategy = st.builds(
    classescstraces::RootCS,
)
classescstraces::RootCS2Root_strategy = st.builds(
    classescstraces::RootCS2Root,
)
classescstraces::Class_strategy = st.builds(
    classescstraces::Class,
)
classescstraces::ClassCS_strategy = st.builds(
    classescstraces::ClassCS,
)
classescstraces::ClassCS2Class_strategy = st.builds(
    classescstraces::ClassCS2Class,
)
classescstraces::Package_strategy = st.builds(
    classescstraces::Package,
)
classescstraces::PackageCS_strategy = st.builds(
    classescstraces::PackageCS,
)
classescstraces::PackageCS2Package_strategy = st.builds(
    classescstraces::PackageCS2Package,
)

@given(instance=classescstraces::Root_strategy)
@settings(max_examples=50)
def test_classescstraces::root_instantiation(instance):
    assert isinstance(instance, classescstraces::Root)

@given(instance=classescstraces::RootCS_strategy)
@settings(max_examples=50)
def test_classescstraces::rootcs_instantiation(instance):
    assert isinstance(instance, classescstraces::RootCS)

@given(instance=classescstraces::RootCS2Root_strategy)
@settings(max_examples=50)
def test_classescstraces::rootcs2root_instantiation(instance):
    assert isinstance(instance, classescstraces::RootCS2Root)

@given(instance=classescstraces::Class_strategy)
@settings(max_examples=50)
def test_classescstraces::class_instantiation(instance):
    assert isinstance(instance, classescstraces::Class)

@given(instance=classescstraces::ClassCS_strategy)
@settings(max_examples=50)
def test_classescstraces::classcs_instantiation(instance):
    assert isinstance(instance, classescstraces::ClassCS)

@given(instance=classescstraces::ClassCS2Class_strategy)
@settings(max_examples=50)
def test_classescstraces::classcs2class_instantiation(instance):
    assert isinstance(instance, classescstraces::ClassCS2Class)

@given(instance=classescstraces::Package_strategy)
@settings(max_examples=50)
def test_classescstraces::package_instantiation(instance):
    assert isinstance(instance, classescstraces::Package)

@given(instance=classescstraces::PackageCS_strategy)
@settings(max_examples=50)
def test_classescstraces::packagecs_instantiation(instance):
    assert isinstance(instance, classescstraces::PackageCS)

@given(instance=classescstraces::PackageCS2Package_strategy)
@settings(max_examples=50)
def test_classescstraces::packagecs2package_instantiation(instance):
    assert isinstance(instance, classescstraces::PackageCS2Package)
