import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    generictest_SuperReffedClass,
    SuperReffedClass,
    generictest_NonGenericSuperclass,
    generictest_TypeArgForRef,
    generictest_GenRef,
    generictest_TypeArgReferencedOnlyExternally,
    generictest_NextGenSuperClass,
    GenericSuperClassBound,
    generictest_TypeArgForGenericSuperClass,
    generictest_GenericSuperClassBound,
    generictest_GenericSuperClass,
    generictest_ReffedClass,
    generictest_Door,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_generictest_superreffedclass_is_not_abstract():
    assert not inspect.isabstract(generictest_SuperReffedClass)


def test_generictest_superreffedclass_constructor_exists():
    assert callable(generictest_SuperReffedClass.__init__)


def test_generictest_superreffedclass_constructor_args():
    sig = inspect.signature(generictest_SuperReffedClass.__init__)
    params = list(sig.parameters.keys())



def test_superreffedclass_is_not_abstract():
    assert not inspect.isabstract(SuperReffedClass)


def test_superreffedclass_constructor_exists():
    assert callable(SuperReffedClass.__init__)


def test_superreffedclass_constructor_args():
    sig = inspect.signature(SuperReffedClass.__init__)
    params = list(sig.parameters.keys())



def test_generictest_nongenericsuperclass_is_not_abstract():
    assert not inspect.isabstract(generictest_NonGenericSuperclass)


def test_generictest_nongenericsuperclass_constructor_exists():
    assert callable(generictest_NonGenericSuperclass.__init__)


def test_generictest_nongenericsuperclass_constructor_args():
    sig = inspect.signature(generictest_NonGenericSuperclass.__init__)
    params = list(sig.parameters.keys())



def test_generictest_typeargforref_is_not_abstract():
    assert not inspect.isabstract(generictest_TypeArgForRef)


def test_generictest_typeargforref_constructor_exists():
    assert callable(generictest_TypeArgForRef.__init__)


def test_generictest_typeargforref_constructor_args():
    sig = inspect.signature(generictest_TypeArgForRef.__init__)
    params = list(sig.parameters.keys())



def test_generictest_genref_is_not_abstract():
    assert not inspect.isabstract(generictest_GenRef)


def test_generictest_genref_constructor_exists():
    assert callable(generictest_GenRef.__init__)


def test_generictest_genref_constructor_args():
    sig = inspect.signature(generictest_GenRef.__init__)
    params = list(sig.parameters.keys())



def test_generictest_typeargreferencedonlyexternally_is_not_abstract():
    assert not inspect.isabstract(generictest_TypeArgReferencedOnlyExternally)


def test_generictest_typeargreferencedonlyexternally_constructor_exists():
    assert callable(generictest_TypeArgReferencedOnlyExternally.__init__)


def test_generictest_typeargreferencedonlyexternally_constructor_args():
    sig = inspect.signature(generictest_TypeArgReferencedOnlyExternally.__init__)
    params = list(sig.parameters.keys())



def test_generictest_nextgensuperclass_is_not_abstract():
    assert not inspect.isabstract(generictest_NextGenSuperClass)


def test_generictest_nextgensuperclass_constructor_exists():
    assert callable(generictest_NextGenSuperClass.__init__)


def test_generictest_nextgensuperclass_constructor_args():
    sig = inspect.signature(generictest_NextGenSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_genericsuperclassbound_is_not_abstract():
    assert not inspect.isabstract(GenericSuperClassBound)


def test_genericsuperclassbound_constructor_exists():
    assert callable(GenericSuperClassBound.__init__)


def test_genericsuperclassbound_constructor_args():
    sig = inspect.signature(GenericSuperClassBound.__init__)
    params = list(sig.parameters.keys())



def test_generictest_typeargforgenericsuperclass_is_not_abstract():
    assert not inspect.isabstract(generictest_TypeArgForGenericSuperClass)


def test_generictest_typeargforgenericsuperclass_constructor_exists():
    assert callable(generictest_TypeArgForGenericSuperClass.__init__)


def test_generictest_typeargforgenericsuperclass_constructor_args():
    sig = inspect.signature(generictest_TypeArgForGenericSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_generictest_genericsuperclassbound_is_not_abstract():
    assert not inspect.isabstract(generictest_GenericSuperClassBound)


def test_generictest_genericsuperclassbound_constructor_exists():
    assert callable(generictest_GenericSuperClassBound.__init__)


def test_generictest_genericsuperclassbound_constructor_args():
    sig = inspect.signature(generictest_GenericSuperClassBound.__init__)
    params = list(sig.parameters.keys())



def test_generictest_genericsuperclass_is_not_abstract():
    assert not inspect.isabstract(generictest_GenericSuperClass)


def test_generictest_genericsuperclass_constructor_exists():
    assert callable(generictest_GenericSuperClass.__init__)


def test_generictest_genericsuperclass_constructor_args():
    sig = inspect.signature(generictest_GenericSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_generictest_reffedclass_is_not_abstract():
    assert not inspect.isabstract(generictest_ReffedClass)


def test_generictest_reffedclass_constructor_exists():
    assert callable(generictest_ReffedClass.__init__)


def test_generictest_reffedclass_constructor_args():
    sig = inspect.signature(generictest_ReffedClass.__init__)
    params = list(sig.parameters.keys())



def test_generictest_door_is_not_abstract():
    assert not inspect.isabstract(generictest_Door)


def test_generictest_door_constructor_exists():
    assert callable(generictest_Door.__init__)


def test_generictest_door_constructor_args():
    sig = inspect.signature(generictest_Door.__init__)
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
generictest_SuperReffedClass_strategy = st.builds(
    generictest_SuperReffedClass,
)
SuperReffedClass_strategy = st.builds(
    SuperReffedClass,
)
generictest_NonGenericSuperclass_strategy = st.builds(
    generictest_NonGenericSuperclass,
)
generictest_TypeArgForRef_strategy = st.builds(
    generictest_TypeArgForRef,
)
generictest_GenRef_strategy = st.builds(
    generictest_GenRef,
)
generictest_TypeArgReferencedOnlyExternally_strategy = st.builds(
    generictest_TypeArgReferencedOnlyExternally,
)
generictest_NextGenSuperClass_strategy = st.builds(
    generictest_NextGenSuperClass,
)
GenericSuperClassBound_strategy = st.builds(
    GenericSuperClassBound,
)
generictest_TypeArgForGenericSuperClass_strategy = st.builds(
    generictest_TypeArgForGenericSuperClass,
)
generictest_GenericSuperClassBound_strategy = st.builds(
    generictest_GenericSuperClassBound,
)
generictest_GenericSuperClass_strategy = st.builds(
    generictest_GenericSuperClass,
)
generictest_ReffedClass_strategy = st.builds(
    generictest_ReffedClass,
)
generictest_Door_strategy = st.builds(
    generictest_Door,
)

@given(instance=generictest_SuperReffedClass_strategy)
@settings(max_examples=50)
def test_generictest_superreffedclass_instantiation(instance):
    assert isinstance(instance, generictest_SuperReffedClass)

@given(instance=SuperReffedClass_strategy)
@settings(max_examples=50)
def test_superreffedclass_instantiation(instance):
    assert isinstance(instance, SuperReffedClass)

@given(instance=generictest_NonGenericSuperclass_strategy)
@settings(max_examples=50)
def test_generictest_nongenericsuperclass_instantiation(instance):
    assert isinstance(instance, generictest_NonGenericSuperclass)

@given(instance=generictest_TypeArgForRef_strategy)
@settings(max_examples=50)
def test_generictest_typeargforref_instantiation(instance):
    assert isinstance(instance, generictest_TypeArgForRef)

@given(instance=generictest_GenRef_strategy)
@settings(max_examples=50)
def test_generictest_genref_instantiation(instance):
    assert isinstance(instance, generictest_GenRef)

@given(instance=generictest_TypeArgReferencedOnlyExternally_strategy)
@settings(max_examples=50)
def test_generictest_typeargreferencedonlyexternally_instantiation(instance):
    assert isinstance(instance, generictest_TypeArgReferencedOnlyExternally)

@given(instance=generictest_NextGenSuperClass_strategy)
@settings(max_examples=50)
def test_generictest_nextgensuperclass_instantiation(instance):
    assert isinstance(instance, generictest_NextGenSuperClass)

@given(instance=GenericSuperClassBound_strategy)
@settings(max_examples=50)
def test_genericsuperclassbound_instantiation(instance):
    assert isinstance(instance, GenericSuperClassBound)

@given(instance=generictest_TypeArgForGenericSuperClass_strategy)
@settings(max_examples=50)
def test_generictest_typeargforgenericsuperclass_instantiation(instance):
    assert isinstance(instance, generictest_TypeArgForGenericSuperClass)

@given(instance=generictest_GenericSuperClassBound_strategy)
@settings(max_examples=50)
def test_generictest_genericsuperclassbound_instantiation(instance):
    assert isinstance(instance, generictest_GenericSuperClassBound)

@given(instance=generictest_GenericSuperClass_strategy)
@settings(max_examples=50)
def test_generictest_genericsuperclass_instantiation(instance):
    assert isinstance(instance, generictest_GenericSuperClass)

@given(instance=generictest_ReffedClass_strategy)
@settings(max_examples=50)
def test_generictest_reffedclass_instantiation(instance):
    assert isinstance(instance, generictest_ReffedClass)

@given(instance=generictest_Door_strategy)
@settings(max_examples=50)
def test_generictest_door_instantiation(instance):
    assert isinstance(instance, generictest_Door)
