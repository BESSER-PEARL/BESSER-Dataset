import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    generictest::SuperReffedClass,
    SuperReffedClass,
    generictest::NonGenericSuperclass,
    generictest::TypeArgForRef,
    generictest::GenRef,
    generictest::TypeArgReferencedOnlyExternally,
    generictest::NextGenSuperClass,
    GenericSuperClassBound,
    generictest::TypeArgForGenericSuperClass,
    generictest::GenericSuperClassBound,
    generictest::GenericSuperClass,
    generictest::ReffedClass,
    generictest::Door,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_generictest::superreffedclass_is_not_abstract():
    assert not inspect.isabstract(generictest::SuperReffedClass)


def test_generictest::superreffedclass_constructor_exists():
    assert callable(generictest::SuperReffedClass.__init__)


def test_generictest::superreffedclass_constructor_args():
    sig = inspect.signature(generictest::SuperReffedClass.__init__)
    params = list(sig.parameters.keys())



def test_superreffedclass_is_not_abstract():
    assert not inspect.isabstract(SuperReffedClass)


def test_superreffedclass_constructor_exists():
    assert callable(SuperReffedClass.__init__)


def test_superreffedclass_constructor_args():
    sig = inspect.signature(SuperReffedClass.__init__)
    params = list(sig.parameters.keys())



def test_generictest::nongenericsuperclass_is_not_abstract():
    assert not inspect.isabstract(generictest::NonGenericSuperclass)


def test_generictest::nongenericsuperclass_constructor_exists():
    assert callable(generictest::NonGenericSuperclass.__init__)


def test_generictest::nongenericsuperclass_constructor_args():
    sig = inspect.signature(generictest::NonGenericSuperclass.__init__)
    params = list(sig.parameters.keys())



def test_generictest::typeargforref_is_not_abstract():
    assert not inspect.isabstract(generictest::TypeArgForRef)


def test_generictest::typeargforref_constructor_exists():
    assert callable(generictest::TypeArgForRef.__init__)


def test_generictest::typeargforref_constructor_args():
    sig = inspect.signature(generictest::TypeArgForRef.__init__)
    params = list(sig.parameters.keys())



def test_generictest::genref_is_not_abstract():
    assert not inspect.isabstract(generictest::GenRef)


def test_generictest::genref_constructor_exists():
    assert callable(generictest::GenRef.__init__)


def test_generictest::genref_constructor_args():
    sig = inspect.signature(generictest::GenRef.__init__)
    params = list(sig.parameters.keys())



def test_generictest::typeargreferencedonlyexternally_is_not_abstract():
    assert not inspect.isabstract(generictest::TypeArgReferencedOnlyExternally)


def test_generictest::typeargreferencedonlyexternally_constructor_exists():
    assert callable(generictest::TypeArgReferencedOnlyExternally.__init__)


def test_generictest::typeargreferencedonlyexternally_constructor_args():
    sig = inspect.signature(generictest::TypeArgReferencedOnlyExternally.__init__)
    params = list(sig.parameters.keys())



def test_generictest::nextgensuperclass_is_not_abstract():
    assert not inspect.isabstract(generictest::NextGenSuperClass)


def test_generictest::nextgensuperclass_constructor_exists():
    assert callable(generictest::NextGenSuperClass.__init__)


def test_generictest::nextgensuperclass_constructor_args():
    sig = inspect.signature(generictest::NextGenSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_genericsuperclassbound_is_not_abstract():
    assert not inspect.isabstract(GenericSuperClassBound)


def test_genericsuperclassbound_constructor_exists():
    assert callable(GenericSuperClassBound.__init__)


def test_genericsuperclassbound_constructor_args():
    sig = inspect.signature(GenericSuperClassBound.__init__)
    params = list(sig.parameters.keys())



def test_generictest::typeargforgenericsuperclass_is_not_abstract():
    assert not inspect.isabstract(generictest::TypeArgForGenericSuperClass)


def test_generictest::typeargforgenericsuperclass_constructor_exists():
    assert callable(generictest::TypeArgForGenericSuperClass.__init__)


def test_generictest::typeargforgenericsuperclass_constructor_args():
    sig = inspect.signature(generictest::TypeArgForGenericSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_generictest::genericsuperclassbound_is_not_abstract():
    assert not inspect.isabstract(generictest::GenericSuperClassBound)


def test_generictest::genericsuperclassbound_constructor_exists():
    assert callable(generictest::GenericSuperClassBound.__init__)


def test_generictest::genericsuperclassbound_constructor_args():
    sig = inspect.signature(generictest::GenericSuperClassBound.__init__)
    params = list(sig.parameters.keys())



def test_generictest::genericsuperclass_is_not_abstract():
    assert not inspect.isabstract(generictest::GenericSuperClass)


def test_generictest::genericsuperclass_constructor_exists():
    assert callable(generictest::GenericSuperClass.__init__)


def test_generictest::genericsuperclass_constructor_args():
    sig = inspect.signature(generictest::GenericSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_generictest::reffedclass_is_not_abstract():
    assert not inspect.isabstract(generictest::ReffedClass)


def test_generictest::reffedclass_constructor_exists():
    assert callable(generictest::ReffedClass.__init__)


def test_generictest::reffedclass_constructor_args():
    sig = inspect.signature(generictest::ReffedClass.__init__)
    params = list(sig.parameters.keys())



def test_generictest::door_is_not_abstract():
    assert not inspect.isabstract(generictest::Door)


def test_generictest::door_constructor_exists():
    assert callable(generictest::Door.__init__)


def test_generictest::door_constructor_args():
    sig = inspect.signature(generictest::Door.__init__)
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
generictest::SuperReffedClass_strategy = st.builds(
    generictest::SuperReffedClass,
)
SuperReffedClass_strategy = st.builds(
    SuperReffedClass,
)
generictest::NonGenericSuperclass_strategy = st.builds(
    generictest::NonGenericSuperclass,
)
generictest::TypeArgForRef_strategy = st.builds(
    generictest::TypeArgForRef,
)
generictest::GenRef_strategy = st.builds(
    generictest::GenRef,
)
generictest::TypeArgReferencedOnlyExternally_strategy = st.builds(
    generictest::TypeArgReferencedOnlyExternally,
)
generictest::NextGenSuperClass_strategy = st.builds(
    generictest::NextGenSuperClass,
)
GenericSuperClassBound_strategy = st.builds(
    GenericSuperClassBound,
)
generictest::TypeArgForGenericSuperClass_strategy = st.builds(
    generictest::TypeArgForGenericSuperClass,
)
generictest::GenericSuperClassBound_strategy = st.builds(
    generictest::GenericSuperClassBound,
)
generictest::GenericSuperClass_strategy = st.builds(
    generictest::GenericSuperClass,
)
generictest::ReffedClass_strategy = st.builds(
    generictest::ReffedClass,
)
generictest::Door_strategy = st.builds(
    generictest::Door,
)

@given(instance=generictest::SuperReffedClass_strategy)
@settings(max_examples=50)
def test_generictest::superreffedclass_instantiation(instance):
    assert isinstance(instance, generictest::SuperReffedClass)

@given(instance=SuperReffedClass_strategy)
@settings(max_examples=50)
def test_superreffedclass_instantiation(instance):
    assert isinstance(instance, SuperReffedClass)

@given(instance=generictest::NonGenericSuperclass_strategy)
@settings(max_examples=50)
def test_generictest::nongenericsuperclass_instantiation(instance):
    assert isinstance(instance, generictest::NonGenericSuperclass)

@given(instance=generictest::TypeArgForRef_strategy)
@settings(max_examples=50)
def test_generictest::typeargforref_instantiation(instance):
    assert isinstance(instance, generictest::TypeArgForRef)

@given(instance=generictest::GenRef_strategy)
@settings(max_examples=50)
def test_generictest::genref_instantiation(instance):
    assert isinstance(instance, generictest::GenRef)

@given(instance=generictest::TypeArgReferencedOnlyExternally_strategy)
@settings(max_examples=50)
def test_generictest::typeargreferencedonlyexternally_instantiation(instance):
    assert isinstance(instance, generictest::TypeArgReferencedOnlyExternally)

@given(instance=generictest::NextGenSuperClass_strategy)
@settings(max_examples=50)
def test_generictest::nextgensuperclass_instantiation(instance):
    assert isinstance(instance, generictest::NextGenSuperClass)

@given(instance=GenericSuperClassBound_strategy)
@settings(max_examples=50)
def test_genericsuperclassbound_instantiation(instance):
    assert isinstance(instance, GenericSuperClassBound)

@given(instance=generictest::TypeArgForGenericSuperClass_strategy)
@settings(max_examples=50)
def test_generictest::typeargforgenericsuperclass_instantiation(instance):
    assert isinstance(instance, generictest::TypeArgForGenericSuperClass)

@given(instance=generictest::GenericSuperClassBound_strategy)
@settings(max_examples=50)
def test_generictest::genericsuperclassbound_instantiation(instance):
    assert isinstance(instance, generictest::GenericSuperClassBound)

@given(instance=generictest::GenericSuperClass_strategy)
@settings(max_examples=50)
def test_generictest::genericsuperclass_instantiation(instance):
    assert isinstance(instance, generictest::GenericSuperClass)

@given(instance=generictest::ReffedClass_strategy)
@settings(max_examples=50)
def test_generictest::reffedclass_instantiation(instance):
    assert isinstance(instance, generictest::ReffedClass)

@given(instance=generictest::Door_strategy)
@settings(max_examples=50)
def test_generictest::door_instantiation(instance):
    assert isinstance(instance, generictest::Door)
