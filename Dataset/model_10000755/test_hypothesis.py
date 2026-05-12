import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyClass,
    ClassV,
    ClassU,
    ClassT,
    ClassS,
    ClassR,
    ClassQ,
    InterfaceO_Interface,
    ClassP,
    ClassN,
    ClassM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_classv_is_not_abstract():
    assert not inspect.isabstract(ClassV)


def test_classv_constructor_exists():
    assert callable(ClassV.__init__)


def test_classv_constructor_args():
    sig = inspect.signature(ClassV.__init__)
    params = list(sig.parameters.keys())



def test_classu_is_not_abstract():
    assert not inspect.isabstract(ClassU)


def test_classu_constructor_exists():
    assert callable(ClassU.__init__)


def test_classu_constructor_args():
    sig = inspect.signature(ClassU.__init__)
    params = list(sig.parameters.keys())



def test_classt_is_not_abstract():
    assert not inspect.isabstract(ClassT)


def test_classt_constructor_exists():
    assert callable(ClassT.__init__)


def test_classt_constructor_args():
    sig = inspect.signature(ClassT.__init__)
    params = list(sig.parameters.keys())



def test_classs_is_not_abstract():
    assert not inspect.isabstract(ClassS)


def test_classs_constructor_exists():
    assert callable(ClassS.__init__)


def test_classs_constructor_args():
    sig = inspect.signature(ClassS.__init__)
    params = list(sig.parameters.keys())



def test_classr_is_not_abstract():
    assert not inspect.isabstract(ClassR)


def test_classr_constructor_exists():
    assert callable(ClassR.__init__)


def test_classr_constructor_args():
    sig = inspect.signature(ClassR.__init__)
    params = list(sig.parameters.keys())



def test_classq_is_not_abstract():
    assert not inspect.isabstract(ClassQ)


def test_classq_constructor_exists():
    assert callable(ClassQ.__init__)


def test_classq_constructor_args():
    sig = inspect.signature(ClassQ.__init__)
    params = list(sig.parameters.keys())



def test_interfaceo_interface_is_not_abstract():
    assert not inspect.isabstract(InterfaceO_Interface)


def test_interfaceo_interface_constructor_exists():
    assert callable(InterfaceO_Interface.__init__)


def test_interfaceo_interface_constructor_args():
    sig = inspect.signature(InterfaceO_Interface.__init__)
    params = list(sig.parameters.keys())



def test_classp_is_not_abstract():
    assert not inspect.isabstract(ClassP)


def test_classp_constructor_exists():
    assert callable(ClassP.__init__)


def test_classp_constructor_args():
    sig = inspect.signature(ClassP.__init__)
    params = list(sig.parameters.keys())



def test_classn_is_not_abstract():
    assert not inspect.isabstract(ClassN)


def test_classn_constructor_exists():
    assert callable(ClassN.__init__)


def test_classn_constructor_args():
    sig = inspect.signature(ClassN.__init__)
    params = list(sig.parameters.keys())



def test_classm_is_not_abstract():
    assert not inspect.isabstract(ClassM)


def test_classm_constructor_exists():
    assert callable(ClassM.__init__)


def test_classm_constructor_args():
    sig = inspect.signature(ClassM.__init__)
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
MyClass_strategy = st.builds(
    MyClass,
)
ClassV_strategy = st.builds(
    ClassV,
)
ClassU_strategy = st.builds(
    ClassU,
)
ClassT_strategy = st.builds(
    ClassT,
)
ClassS_strategy = st.builds(
    ClassS,
)
ClassR_strategy = st.builds(
    ClassR,
)
ClassQ_strategy = st.builds(
    ClassQ,
)
InterfaceO_Interface_strategy = st.builds(
    InterfaceO_Interface,
)
ClassP_strategy = st.builds(
    ClassP,
)
ClassN_strategy = st.builds(
    ClassN,
)
ClassM_strategy = st.builds(
    ClassM,
)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)

@given(instance=ClassV_strategy)
@settings(max_examples=50)
def test_classv_instantiation(instance):
    assert isinstance(instance, ClassV)

@given(instance=ClassU_strategy)
@settings(max_examples=50)
def test_classu_instantiation(instance):
    assert isinstance(instance, ClassU)

@given(instance=ClassT_strategy)
@settings(max_examples=50)
def test_classt_instantiation(instance):
    assert isinstance(instance, ClassT)

@given(instance=ClassS_strategy)
@settings(max_examples=50)
def test_classs_instantiation(instance):
    assert isinstance(instance, ClassS)

@given(instance=ClassR_strategy)
@settings(max_examples=50)
def test_classr_instantiation(instance):
    assert isinstance(instance, ClassR)

@given(instance=ClassQ_strategy)
@settings(max_examples=50)
def test_classq_instantiation(instance):
    assert isinstance(instance, ClassQ)

@given(instance=InterfaceO_Interface_strategy)
@settings(max_examples=50)
def test_interfaceo_interface_instantiation(instance):
    assert isinstance(instance, InterfaceO_Interface)

@given(instance=ClassP_strategy)
@settings(max_examples=50)
def test_classp_instantiation(instance):
    assert isinstance(instance, ClassP)

@given(instance=ClassN_strategy)
@settings(max_examples=50)
def test_classn_instantiation(instance):
    assert isinstance(instance, ClassN)

@given(instance=ClassM_strategy)
@settings(max_examples=50)
def test_classm_instantiation(instance):
    assert isinstance(instance, ClassM)
