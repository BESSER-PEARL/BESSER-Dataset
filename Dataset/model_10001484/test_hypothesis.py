import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class4,
    vcx,
    Class,
    ccc,
    aaa,
    vvvv,
    cgv_Classqwe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class4_is_not_abstract():
    assert not inspect.isabstract(Class4)


def test_class4_constructor_exists():
    assert callable(Class4.__init__)


def test_class4_constructor_args():
    sig = inspect.signature(Class4.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_class4_has_attribute():
    assert hasattr(Class4, "attribute")
    descriptor = None
    for klass in Class4.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_vcx_is_not_abstract():
    assert not inspect.isabstract(vcx)


def test_vcx_constructor_exists():
    assert callable(vcx.__init__)


def test_vcx_constructor_args():
    sig = inspect.signature(vcx.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"

def test_vcx_has_attribute():
    assert hasattr(vcx, "attribute")
    descriptor = None
    for klass in vcx.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_vcx_has_attribute2():
    assert hasattr(vcx, "attribute2")
    descriptor = None
    for klass in vcx.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_ccc_is_not_abstract():
    assert not inspect.isabstract(ccc)


def test_ccc_constructor_exists():
    assert callable(ccc.__init__)


def test_ccc_constructor_args():
    sig = inspect.signature(ccc.__init__)
    params = list(sig.parameters.keys())
    assert "qwe" in params, "Missing parameter 'qwe'"

def test_ccc_has_qwe():
    assert hasattr(ccc, "qwe")
    descriptor = None
    for klass in ccc.__mro__:
        if "qwe" in klass.__dict__:
            descriptor = klass.__dict__["qwe"]
            break
    assert isinstance(descriptor, property)



def test_aaa_is_not_abstract():
    assert not inspect.isabstract(aaa)


def test_aaa_constructor_exists():
    assert callable(aaa.__init__)


def test_aaa_constructor_args():
    sig = inspect.signature(aaa.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "qwe" in params, "Missing parameter 'qwe'"

def test_aaa_has_attribute():
    assert hasattr(aaa, "attribute")
    descriptor = None
    for klass in aaa.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_aaa_has_qwe():
    assert hasattr(aaa, "qwe")
    descriptor = None
    for klass in aaa.__mro__:
        if "qwe" in klass.__dict__:
            descriptor = klass.__dict__["qwe"]
            break
    assert isinstance(descriptor, property)



def test_vvvv_is_not_abstract():
    assert not inspect.isabstract(vvvv)


def test_vvvv_constructor_exists():
    assert callable(vvvv.__init__)


def test_vvvv_constructor_args():
    sig = inspect.signature(vvvv.__init__)
    params = list(sig.parameters.keys())
    assert "zsxc" in params, "Missing parameter 'zsxc'"

def test_vvvv_has_zsxc():
    assert hasattr(vvvv, "zsxc")
    descriptor = None
    for klass in vvvv.__mro__:
        if "zsxc" in klass.__dict__:
            descriptor = klass.__dict__["zsxc"]
            break
    assert isinstance(descriptor, property)



def test_cgv_classqwe_is_not_abstract():
    assert not inspect.isabstract(cgv_Classqwe)


def test_cgv_classqwe_constructor_exists():
    assert callable(cgv_Classqwe.__init__)


def test_cgv_classqwe_constructor_args():
    sig = inspect.signature(cgv_Classqwe.__init__)
    params = list(sig.parameters.keys())
    assert "qw" in params, "Missing parameter 'qw'"

def test_cgv_classqwe_has_qw():
    assert hasattr(cgv_Classqwe, "qw")
    descriptor = None
    for klass in cgv_Classqwe.__mro__:
        if "qw" in klass.__dict__:
            descriptor = klass.__dict__["qw"]
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
Class4_strategy = st.builds(
    Class4,
    attribute=
        safe_text
)
vcx_strategy = st.builds(
    vcx,
    attribute=
        st.booleans(),
    attribute2=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
ccc_strategy = st.builds(
    ccc,
    qwe=
        safe_text
)
aaa_strategy = st.builds(
    aaa,
    attribute=
        st.booleans(),
    qwe=
        st.none()
)
vvvv_strategy = st.builds(
    vvvv,
    zsxc=
        st.integers()
)
cgv_Classqwe_strategy = st.builds(
    cgv_Classqwe,
    qw=
        st.none()
)

@given(instance=Class4_strategy)
@settings(max_examples=50)
def test_class4_instantiation(instance):
    assert isinstance(instance, Class4)



@given(instance=Class4_strategy)
def test_class4_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=vcx_strategy)
@settings(max_examples=50)
def test_vcx_instantiation(instance):
    assert isinstance(instance, vcx)



@given(instance=vcx_strategy)
def test_vcx_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=vcx_strategy)
def test_vcx_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=ccc_strategy)
@settings(max_examples=50)
def test_ccc_instantiation(instance):
    assert isinstance(instance, ccc)



@given(instance=ccc_strategy)
def test_ccc_qwe_setter(instance):
    original = instance.qwe
    instance.qwe = original
    assert instance.qwe == original

@given(instance=aaa_strategy)
@settings(max_examples=50)
def test_aaa_instantiation(instance):
    assert isinstance(instance, aaa)



@given(instance=aaa_strategy)
def test_aaa_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=aaa_strategy)
def test_aaa_qwe_setter(instance):
    original = instance.qwe
    instance.qwe = original
    assert instance.qwe == original

@given(instance=vvvv_strategy)
@settings(max_examples=50)
def test_vvvv_instantiation(instance):
    assert isinstance(instance, vvvv)



@given(instance=vvvv_strategy)
def test_vvvv_zsxc_setter(instance):
    original = instance.zsxc
    instance.zsxc = original
    assert instance.zsxc == original

@given(instance=cgv_Classqwe_strategy)
@settings(max_examples=50)
def test_cgv_classqwe_instantiation(instance):
    assert isinstance(instance, cgv_Classqwe)



@given(instance=cgv_Classqwe_strategy)
def test_cgv_classqwe_qw_setter(instance):
    original = instance.qw
    instance.qw = original
    assert instance.qw == original
