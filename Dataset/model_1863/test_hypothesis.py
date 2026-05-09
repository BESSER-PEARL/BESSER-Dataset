import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    beans::NamedElement,
    NamedElement,
    beans::BeanProperty,
    beans::Bean,
    beans::BeanLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_beans::namedelement_is_not_abstract():
    assert not inspect.isabstract(beans::NamedElement)


def test_beans::namedelement_constructor_exists():
    assert callable(beans::NamedElement.__init__)


def test_beans::namedelement_constructor_args():
    sig = inspect.signature(beans::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_beans::namedelement_has_name():
    assert hasattr(beans::NamedElement, "name")
    descriptor = None
    for klass in beans::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_beans::beanproperty_is_not_abstract():
    assert not inspect.isabstract(beans::BeanProperty)


def test_beans::beanproperty_constructor_exists():
    assert callable(beans::BeanProperty.__init__)


def test_beans::beanproperty_constructor_args():
    sig = inspect.signature(beans::BeanProperty.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "changeable" in params, "Missing parameter 'changeable'"

def test_beans::beanproperty_has_typeName():
    assert hasattr(beans::BeanProperty, "typeName")
    descriptor = None
    for klass in beans::BeanProperty.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_beans::beanproperty_has_changeable():
    assert hasattr(beans::BeanProperty, "changeable")
    descriptor = None
    for klass in beans::BeanProperty.__mro__:
        if "changeable" in klass.__dict__:
            descriptor = klass.__dict__["changeable"]
            break
    assert isinstance(descriptor, property)



def test_beans::bean_is_not_abstract():
    assert not inspect.isabstract(beans::Bean)


def test_beans::bean_constructor_exists():
    assert callable(beans::Bean.__init__)


def test_beans::bean_constructor_args():
    sig = inspect.signature(beans::Bean.__init__)
    params = list(sig.parameters.keys())



def test_beans::beanlibrary_is_not_abstract():
    assert not inspect.isabstract(beans::BeanLibrary)


def test_beans::beanlibrary_constructor_exists():
    assert callable(beans::BeanLibrary.__init__)


def test_beans::beanlibrary_constructor_args():
    sig = inspect.signature(beans::BeanLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "packageName" in params, "Missing parameter 'packageName'"

def test_beans::beanlibrary_has_packageName():
    assert hasattr(beans::BeanLibrary, "packageName")
    descriptor = None
    for klass in beans::BeanLibrary.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
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
beans::NamedElement_strategy = st.builds(
    beans::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
beans::BeanProperty_strategy = st.builds(
    beans::BeanProperty,
    typeName=
        safe_text,
    changeable=
        st.booleans()
)
beans::Bean_strategy = st.builds(
    beans::Bean,
)
beans::BeanLibrary_strategy = st.builds(
    beans::BeanLibrary,
    packageName=
        safe_text
)

@given(instance=beans::NamedElement_strategy)
@settings(max_examples=50)
def test_beans::namedelement_instantiation(instance):
    assert isinstance(instance, beans::NamedElement)

@given(instance=beans::NamedElement_strategy)
def test_beans::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=beans::NamedElement_strategy)
def test_beans::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=beans::BeanProperty_strategy)
@settings(max_examples=50)
def test_beans::beanproperty_instantiation(instance):
    assert isinstance(instance, beans::BeanProperty)

@given(instance=beans::BeanProperty_strategy)
def test_beans::beanproperty_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=beans::BeanProperty_strategy)
def test_beans::beanproperty_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=beans::BeanProperty_strategy)
def test_beans::beanproperty_changeable_type(instance):
    assert isinstance(instance.changeable, bool)


@given(instance=beans::BeanProperty_strategy)
def test_beans::beanproperty_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original

@given(instance=beans::Bean_strategy)
@settings(max_examples=50)
def test_beans::bean_instantiation(instance):
    assert isinstance(instance, beans::Bean)

@given(instance=beans::BeanLibrary_strategy)
@settings(max_examples=50)
def test_beans::beanlibrary_instantiation(instance):
    assert isinstance(instance, beans::BeanLibrary)

@given(instance=beans::BeanLibrary_strategy)
def test_beans::beanlibrary_packageName_type(instance):
    assert isinstance(instance.packageName, str)


@given(instance=beans::BeanLibrary_strategy)
def test_beans::beanlibrary_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original
