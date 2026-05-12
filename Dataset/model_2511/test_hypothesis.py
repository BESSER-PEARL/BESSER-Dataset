import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rootPackage_aSubSubPackage_F,
    aSubSubPackage_F,
    rootPackage_aSubSubPackage_E,
    rootPackage_aSubPackage_D,
    rootPackage_AbstractA,
    rootPackage_B,
    rootPackage_C,
    AbstractA,
    rootPackage_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rootpackage_asubsubpackage_f_is_not_abstract():
    assert not inspect.isabstract(rootPackage_aSubSubPackage_F)


def test_rootpackage_asubsubpackage_f_constructor_exists():
    assert callable(rootPackage_aSubSubPackage_F.__init__)


def test_rootpackage_asubsubpackage_f_constructor_args():
    sig = inspect.signature(rootPackage_aSubSubPackage_F.__init__)
    params = list(sig.parameters.keys())



def test_asubsubpackage_f_is_not_abstract():
    assert not inspect.isabstract(aSubSubPackage_F)


def test_asubsubpackage_f_constructor_exists():
    assert callable(aSubSubPackage_F.__init__)


def test_asubsubpackage_f_constructor_args():
    sig = inspect.signature(aSubSubPackage_F.__init__)
    params = list(sig.parameters.keys())



def test_rootpackage_asubsubpackage_e_is_not_abstract():
    assert not inspect.isabstract(rootPackage_aSubSubPackage_E)


def test_rootpackage_asubsubpackage_e_constructor_exists():
    assert callable(rootPackage_aSubSubPackage_E.__init__)


def test_rootpackage_asubsubpackage_e_constructor_args():
    sig = inspect.signature(rootPackage_aSubSubPackage_E.__init__)
    params = list(sig.parameters.keys())



def test_rootpackage_asubpackage_d_is_not_abstract():
    assert not inspect.isabstract(rootPackage_aSubPackage_D)


def test_rootpackage_asubpackage_d_constructor_exists():
    assert callable(rootPackage_aSubPackage_D.__init__)


def test_rootpackage_asubpackage_d_constructor_args():
    sig = inspect.signature(rootPackage_aSubPackage_D.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"

def test_rootpackage_asubpackage_d_has_d():
    assert hasattr(rootPackage_aSubPackage_D, "d")
    descriptor = None
    for klass in rootPackage_aSubPackage_D.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)



def test_rootpackage_abstracta_is_not_abstract():
    assert not inspect.isabstract(rootPackage_AbstractA)


def test_rootpackage_abstracta_constructor_exists():
    assert callable(rootPackage_AbstractA.__init__)


def test_rootpackage_abstracta_constructor_args():
    sig = inspect.signature(rootPackage_AbstractA.__init__)
    params = list(sig.parameters.keys())



def test_rootpackage_b_is_not_abstract():
    assert not inspect.isabstract(rootPackage_B)


def test_rootpackage_b_constructor_exists():
    assert callable(rootPackage_B.__init__)


def test_rootpackage_b_constructor_args():
    sig = inspect.signature(rootPackage_B.__init__)
    params = list(sig.parameters.keys())
    assert "stuff" in params, "Missing parameter 'stuff'"
    assert "bint" in params, "Missing parameter 'bint'"

def test_rootpackage_b_has_stuff():
    assert hasattr(rootPackage_B, "stuff")
    descriptor = None
    for klass in rootPackage_B.__mro__:
        if "stuff" in klass.__dict__:
            descriptor = klass.__dict__["stuff"]
            break
    assert isinstance(descriptor, property)

def test_rootpackage_b_has_bint():
    assert hasattr(rootPackage_B, "bint")
    descriptor = None
    for klass in rootPackage_B.__mro__:
        if "bint" in klass.__dict__:
            descriptor = klass.__dict__["bint"]
            break
    assert isinstance(descriptor, property)



def test_rootpackage_c_is_not_abstract():
    assert not inspect.isabstract(rootPackage_C)


def test_rootpackage_c_constructor_exists():
    assert callable(rootPackage_C.__init__)


def test_rootpackage_c_constructor_args():
    sig = inspect.signature(rootPackage_C.__init__)
    params = list(sig.parameters.keys())
    assert "cstring" in params, "Missing parameter 'cstring'"

def test_rootpackage_c_has_cstring():
    assert hasattr(rootPackage_C, "cstring")
    descriptor = None
    for klass in rootPackage_C.__mro__:
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



def test_rootpackage_a_is_not_abstract():
    assert not inspect.isabstract(rootPackage_A)


def test_rootpackage_a_constructor_exists():
    assert callable(rootPackage_A.__init__)


def test_rootpackage_a_constructor_args():
    sig = inspect.signature(rootPackage_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "a2" in params, "Missing parameter 'a2'"

def test_rootpackage_a_has_a():
    assert hasattr(rootPackage_A, "a")
    descriptor = None
    for klass in rootPackage_A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_rootpackage_a_has_a2():
    assert hasattr(rootPackage_A, "a2")
    descriptor = None
    for klass in rootPackage_A.__mro__:
        if "a2" in klass.__dict__:
            descriptor = klass.__dict__["a2"]
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
rootPackage_aSubSubPackage_F_strategy = st.builds(
    rootPackage_aSubSubPackage_F,
)
aSubSubPackage_F_strategy = st.builds(
    aSubSubPackage_F,
)
rootPackage_aSubSubPackage_E_strategy = st.builds(
    rootPackage_aSubSubPackage_E,
)
rootPackage_aSubPackage_D_strategy = st.builds(
    rootPackage_aSubPackage_D,
    d=
        st.integers()
)
rootPackage_AbstractA_strategy = st.builds(
    rootPackage_AbstractA,
)
rootPackage_B_strategy = st.builds(
    rootPackage_B,
    stuff=
        safe_text,
    bint=
        st.integers()
)
rootPackage_C_strategy = st.builds(
    rootPackage_C,
    cstring=
        safe_text
)
AbstractA_strategy = st.builds(
    AbstractA,
)
rootPackage_A_strategy = st.builds(
    rootPackage_A,
    a=
        st.integers(),
    a2=
        st.booleans()
)

@given(instance=rootPackage_aSubSubPackage_F_strategy)
@settings(max_examples=50)
def test_rootpackage_asubsubpackage_f_instantiation(instance):
    assert isinstance(instance, rootPackage_aSubSubPackage_F)

@given(instance=aSubSubPackage_F_strategy)
@settings(max_examples=50)
def test_asubsubpackage_f_instantiation(instance):
    assert isinstance(instance, aSubSubPackage_F)

@given(instance=rootPackage_aSubSubPackage_E_strategy)
@settings(max_examples=50)
def test_rootpackage_asubsubpackage_e_instantiation(instance):
    assert isinstance(instance, rootPackage_aSubSubPackage_E)

@given(instance=rootPackage_aSubPackage_D_strategy)
@settings(max_examples=50)
def test_rootpackage_asubpackage_d_instantiation(instance):
    assert isinstance(instance, rootPackage_aSubPackage_D)



@given(instance=rootPackage_aSubPackage_D_strategy)
def test_rootpackage_asubpackage_d_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=rootPackage_AbstractA_strategy)
@settings(max_examples=50)
def test_rootpackage_abstracta_instantiation(instance):
    assert isinstance(instance, rootPackage_AbstractA)

@given(instance=rootPackage_B_strategy)
@settings(max_examples=50)
def test_rootpackage_b_instantiation(instance):
    assert isinstance(instance, rootPackage_B)



@given(instance=rootPackage_B_strategy)
def test_rootpackage_b_stuff_setter(instance):
    original = instance.stuff
    instance.stuff = original
    assert instance.stuff == original



@given(instance=rootPackage_B_strategy)
def test_rootpackage_b_bint_setter(instance):
    original = instance.bint
    instance.bint = original
    assert instance.bint == original

@given(instance=rootPackage_C_strategy)
@settings(max_examples=50)
def test_rootpackage_c_instantiation(instance):
    assert isinstance(instance, rootPackage_C)



@given(instance=rootPackage_C_strategy)
def test_rootpackage_c_cstring_setter(instance):
    original = instance.cstring
    instance.cstring = original
    assert instance.cstring == original

@given(instance=AbstractA_strategy)
@settings(max_examples=50)
def test_abstracta_instantiation(instance):
    assert isinstance(instance, AbstractA)

@given(instance=rootPackage_A_strategy)
@settings(max_examples=50)
def test_rootpackage_a_instantiation(instance):
    assert isinstance(instance, rootPackage_A)



@given(instance=rootPackage_A_strategy)
def test_rootpackage_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=rootPackage_A_strategy)
def test_rootpackage_a_a2_setter(instance):
    original = instance.a2
    instance.a2 = original
    assert instance.a2 == original
