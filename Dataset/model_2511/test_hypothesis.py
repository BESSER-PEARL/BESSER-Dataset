import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rootPackage::aSubSubPackage::F,
    aSubSubPackage::F,
    rootPackage::aSubSubPackage::E,
    rootPackage::aSubPackage::D,
    rootPackage::AbstractA,
    rootPackage::B,
    rootPackage::C,
    AbstractA,
    rootPackage::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rootpackage::asubsubpackage::f_is_not_abstract():
    assert not inspect.isabstract(rootPackage::aSubSubPackage::F)


def test_rootpackage::asubsubpackage::f_constructor_exists():
    assert callable(rootPackage::aSubSubPackage::F.__init__)


def test_rootpackage::asubsubpackage::f_constructor_args():
    sig = inspect.signature(rootPackage::aSubSubPackage::F.__init__)
    params = list(sig.parameters.keys())



def test_asubsubpackage::f_is_not_abstract():
    assert not inspect.isabstract(aSubSubPackage::F)


def test_asubsubpackage::f_constructor_exists():
    assert callable(aSubSubPackage::F.__init__)


def test_asubsubpackage::f_constructor_args():
    sig = inspect.signature(aSubSubPackage::F.__init__)
    params = list(sig.parameters.keys())



def test_rootpackage::asubsubpackage::e_is_not_abstract():
    assert not inspect.isabstract(rootPackage::aSubSubPackage::E)


def test_rootpackage::asubsubpackage::e_constructor_exists():
    assert callable(rootPackage::aSubSubPackage::E.__init__)


def test_rootpackage::asubsubpackage::e_constructor_args():
    sig = inspect.signature(rootPackage::aSubSubPackage::E.__init__)
    params = list(sig.parameters.keys())



def test_rootpackage::asubpackage::d_is_not_abstract():
    assert not inspect.isabstract(rootPackage::aSubPackage::D)


def test_rootpackage::asubpackage::d_constructor_exists():
    assert callable(rootPackage::aSubPackage::D.__init__)


def test_rootpackage::asubpackage::d_constructor_args():
    sig = inspect.signature(rootPackage::aSubPackage::D.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"

def test_rootpackage::asubpackage::d_has_d():
    assert hasattr(rootPackage::aSubPackage::D, "d")
    descriptor = None
    for klass in rootPackage::aSubPackage::D.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)



def test_rootpackage::abstracta_is_not_abstract():
    assert not inspect.isabstract(rootPackage::AbstractA)


def test_rootpackage::abstracta_constructor_exists():
    assert callable(rootPackage::AbstractA.__init__)


def test_rootpackage::abstracta_constructor_args():
    sig = inspect.signature(rootPackage::AbstractA.__init__)
    params = list(sig.parameters.keys())



def test_rootpackage::b_is_not_abstract():
    assert not inspect.isabstract(rootPackage::B)


def test_rootpackage::b_constructor_exists():
    assert callable(rootPackage::B.__init__)


def test_rootpackage::b_constructor_args():
    sig = inspect.signature(rootPackage::B.__init__)
    params = list(sig.parameters.keys())
    assert "bint" in params, "Missing parameter 'bint'"
    assert "stuff" in params, "Missing parameter 'stuff'"

def test_rootpackage::b_has_bint():
    assert hasattr(rootPackage::B, "bint")
    descriptor = None
    for klass in rootPackage::B.__mro__:
        if "bint" in klass.__dict__:
            descriptor = klass.__dict__["bint"]
            break
    assert isinstance(descriptor, property)

def test_rootpackage::b_has_stuff():
    assert hasattr(rootPackage::B, "stuff")
    descriptor = None
    for klass in rootPackage::B.__mro__:
        if "stuff" in klass.__dict__:
            descriptor = klass.__dict__["stuff"]
            break
    assert isinstance(descriptor, property)



def test_rootpackage::c_is_not_abstract():
    assert not inspect.isabstract(rootPackage::C)


def test_rootpackage::c_constructor_exists():
    assert callable(rootPackage::C.__init__)


def test_rootpackage::c_constructor_args():
    sig = inspect.signature(rootPackage::C.__init__)
    params = list(sig.parameters.keys())
    assert "cstring" in params, "Missing parameter 'cstring'"

def test_rootpackage::c_has_cstring():
    assert hasattr(rootPackage::C, "cstring")
    descriptor = None
    for klass in rootPackage::C.__mro__:
        if "cstring" in klass.__dict__:
            descriptor = klass.__dict__["cstring"]
            break
    assert isinstance(descriptor, property)



def test_abstracta_is_not_abstract():
    assert not inspect.isabstract(AbstractA)


def test_abstracta_constructor_exists():
    assert callable(AbstractA.__init__)


def test_abstracta_constructor_args():
    sig = inspect.signature(AbstractA.__init__)
    params = list(sig.parameters.keys())



def test_rootpackage::a_is_not_abstract():
    assert not inspect.isabstract(rootPackage::A)


def test_rootpackage::a_constructor_exists():
    assert callable(rootPackage::A.__init__)


def test_rootpackage::a_constructor_args():
    sig = inspect.signature(rootPackage::A.__init__)
    params = list(sig.parameters.keys())
    assert "a2" in params, "Missing parameter 'a2'"
    assert "a" in params, "Missing parameter 'a'"

def test_rootpackage::a_has_a2():
    assert hasattr(rootPackage::A, "a2")
    descriptor = None
    for klass in rootPackage::A.__mro__:
        if "a2" in klass.__dict__:
            descriptor = klass.__dict__["a2"]
            break
    assert isinstance(descriptor, property)

def test_rootpackage::a_has_a():
    assert hasattr(rootPackage::A, "a")
    descriptor = None
    for klass in rootPackage::A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
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
rootPackage::aSubSubPackage::F_strategy = st.builds(
    rootPackage::aSubSubPackage::F,
)
aSubSubPackage::F_strategy = st.builds(
    aSubSubPackage::F,
)
rootPackage::aSubSubPackage::E_strategy = st.builds(
    rootPackage::aSubSubPackage::E,
)
rootPackage::aSubPackage::D_strategy = st.builds(
    rootPackage::aSubPackage::D,
    d=
        st.integers()
)
rootPackage::AbstractA_strategy = st.builds(
    rootPackage::AbstractA,
)
rootPackage::B_strategy = st.builds(
    rootPackage::B,
    bint=
        st.integers(),
    stuff=
        safe_text
)
rootPackage::C_strategy = st.builds(
    rootPackage::C,
    cstring=
        safe_text
)
AbstractA_strategy = st.builds(
    AbstractA,
)
rootPackage::A_strategy = st.builds(
    rootPackage::A,
    a2=
        st.booleans(),
    a=
        st.integers()
)

@given(instance=rootPackage::aSubSubPackage::F_strategy)
@settings(max_examples=50)
def test_rootpackage::asubsubpackage::f_instantiation(instance):
    assert isinstance(instance, rootPackage::aSubSubPackage::F)

@given(instance=aSubSubPackage::F_strategy)
@settings(max_examples=50)
def test_asubsubpackage::f_instantiation(instance):
    assert isinstance(instance, aSubSubPackage::F)

@given(instance=rootPackage::aSubSubPackage::E_strategy)
@settings(max_examples=50)
def test_rootpackage::asubsubpackage::e_instantiation(instance):
    assert isinstance(instance, rootPackage::aSubSubPackage::E)

@given(instance=rootPackage::aSubPackage::D_strategy)
@settings(max_examples=50)
def test_rootpackage::asubpackage::d_instantiation(instance):
    assert isinstance(instance, rootPackage::aSubPackage::D)

@given(instance=rootPackage::aSubPackage::D_strategy)
def test_rootpackage::asubpackage::d_d_type(instance):
    assert isinstance(instance.d, int)


@given(instance=rootPackage::aSubPackage::D_strategy)
def test_rootpackage::asubpackage::d_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=rootPackage::AbstractA_strategy)
@settings(max_examples=50)
def test_rootpackage::abstracta_instantiation(instance):
    assert isinstance(instance, rootPackage::AbstractA)

@given(instance=rootPackage::B_strategy)
@settings(max_examples=50)
def test_rootpackage::b_instantiation(instance):
    assert isinstance(instance, rootPackage::B)

@given(instance=rootPackage::B_strategy)
def test_rootpackage::b_bint_type(instance):
    assert isinstance(instance.bint, int)


@given(instance=rootPackage::B_strategy)
def test_rootpackage::b_bint_setter(instance):
    original = instance.bint
    instance.bint = original
    assert instance.bint == original

@given(instance=rootPackage::B_strategy)
def test_rootpackage::b_stuff_type(instance):
    assert isinstance(instance.stuff, str)


@given(instance=rootPackage::B_strategy)
def test_rootpackage::b_stuff_setter(instance):
    original = instance.stuff
    instance.stuff = original
    assert instance.stuff == original

@given(instance=rootPackage::C_strategy)
@settings(max_examples=50)
def test_rootpackage::c_instantiation(instance):
    assert isinstance(instance, rootPackage::C)

@given(instance=rootPackage::C_strategy)
def test_rootpackage::c_cstring_type(instance):
    assert isinstance(instance.cstring, str)


@given(instance=rootPackage::C_strategy)
def test_rootpackage::c_cstring_setter(instance):
    original = instance.cstring
    instance.cstring = original
    assert instance.cstring == original

@given(instance=AbstractA_strategy)
@settings(max_examples=50)
def test_abstracta_instantiation(instance):
    assert isinstance(instance, AbstractA)

@given(instance=rootPackage::A_strategy)
@settings(max_examples=50)
def test_rootpackage::a_instantiation(instance):
    assert isinstance(instance, rootPackage::A)

@given(instance=rootPackage::A_strategy)
def test_rootpackage::a_a2_type(instance):
    assert isinstance(instance.a2, bool)


@given(instance=rootPackage::A_strategy)
def test_rootpackage::a_a2_setter(instance):
    original = instance.a2
    instance.a2 = original
    assert instance.a2 == original

@given(instance=rootPackage::A_strategy)
def test_rootpackage::a_a_type(instance):
    assert isinstance(instance.a, int)


@given(instance=rootPackage::A_strategy)
def test_rootpackage::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
