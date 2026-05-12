import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    G,
    F,
    E,
    B2,
    A3,
    A2,
    B,
    A,
    Y,
    R,
    Z,
    C2,
    C3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_g_is_not_abstract():
    assert not inspect.isabstract(G)


def test_g_constructor_exists():
    assert callable(G.__init__)


def test_g_constructor_args():
    sig = inspect.signature(G.__init__)
    params = list(sig.parameters.keys())



def test_f_is_not_abstract():
    assert not inspect.isabstract(F)


def test_f_constructor_exists():
    assert callable(F.__init__)


def test_f_constructor_args():
    sig = inspect.signature(F.__init__)
    params = list(sig.parameters.keys())
    assert "attF" in params, "Missing parameter 'attF'"

def test_f_has_attF():
    assert hasattr(F, "attF")
    descriptor = None
    for klass in F.__mro__:
        if "attF" in klass.__dict__:
            descriptor = klass.__dict__["attF"]
            break
    assert isinstance(descriptor, property)



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())
    assert "attE" in params, "Missing parameter 'attE'"

def test_e_has_attE():
    assert hasattr(E, "attE")
    descriptor = None
    for klass in E.__mro__:
        if "attE" in klass.__dict__:
            descriptor = klass.__dict__["attE"]
            break
    assert isinstance(descriptor, property)



def test_b2_is_not_abstract():
    assert not inspect.isabstract(B2)


def test_b2_constructor_exists():
    assert callable(B2.__init__)


def test_b2_constructor_args():
    sig = inspect.signature(B2.__init__)
    params = list(sig.parameters.keys())



def test_a3_is_not_abstract():
    assert not inspect.isabstract(A3)


def test_a3_constructor_exists():
    assert callable(A3.__init__)


def test_a3_constructor_args():
    sig = inspect.signature(A3.__init__)
    params = list(sig.parameters.keys())



def test_a2_is_not_abstract():
    assert not inspect.isabstract(A2)


def test_a2_constructor_exists():
    assert callable(A2.__init__)


def test_a2_constructor_args():
    sig = inspect.signature(A2.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"
    assert "b" in params, "Missing parameter 'b'"

def test_a_has_d():
    assert hasattr(A, "d")
    descriptor = None
    for klass in A.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_a_has_b():
    assert hasattr(A, "b")
    descriptor = None
    for klass in A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())
    assert "attY" in params, "Missing parameter 'attY'"

def test_y_has_attY():
    assert hasattr(Y, "attY")
    descriptor = None
    for klass in Y.__mro__:
        if "attY" in klass.__dict__:
            descriptor = klass.__dict__["attY"]
            break
    assert isinstance(descriptor, property)



def test_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_r_constructor_exists():
    assert callable(R.__init__)


def test_r_constructor_args():
    sig = inspect.signature(R.__init__)
    params = list(sig.parameters.keys())



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_c3_constructor_exists():
    assert callable(C3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
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
G_strategy = st.builds(
    G,
)
F_strategy = st.builds(
    F,
    attF=
        safe_text
)
E_strategy = st.builds(
    E,
    attE=
        safe_text
)
B2_strategy = st.builds(
    B2,
)
A3_strategy = st.builds(
    A3,
)
A2_strategy = st.builds(
    A2,
)
B_strategy = st.builds(
    B,
)
A_strategy = st.builds(
    A,
    d=
        st.integers(),
    b=
        st.booleans()
)
Y_strategy = st.builds(
    Y,
    attY=
        safe_text
)
R_strategy = st.builds(
    R,
)
Z_strategy = st.builds(
    Z,
)
C2_strategy = st.builds(
    C2,
)
C3_strategy = st.builds(
    C3,
)

@given(instance=G_strategy)
@settings(max_examples=50)
def test_g_instantiation(instance):
    assert isinstance(instance, G)

@given(instance=F_strategy)
@settings(max_examples=50)
def test_f_instantiation(instance):
    assert isinstance(instance, F)



@given(instance=F_strategy)
def test_f_attF_setter(instance):
    original = instance.attF
    instance.attF = original
    assert instance.attF == original

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)



@given(instance=E_strategy)
def test_e_attE_setter(instance):
    original = instance.attE
    instance.attE = original
    assert instance.attE == original

@given(instance=B2_strategy)
@settings(max_examples=50)
def test_b2_instantiation(instance):
    assert isinstance(instance, B2)

@given(instance=A3_strategy)
@settings(max_examples=50)
def test_a3_instantiation(instance):
    assert isinstance(instance, A3)

@given(instance=A2_strategy)
@settings(max_examples=50)
def test_a2_instantiation(instance):
    assert isinstance(instance, A2)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=A_strategy)
def test_a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)



@given(instance=Y_strategy)
def test_y_attY_setter(instance):
    original = instance.attY
    instance.attY = original
    assert instance.attY == original

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)
