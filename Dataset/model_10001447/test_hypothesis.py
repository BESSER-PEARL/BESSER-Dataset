import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Escale,
    Vol,
    A_roport,
    Ville,
    tp2BMOexe3_A3,
    tp2BMOexe3_A2,
    tp2BMOexe3_A,
    tp2BMOexe3_B2,
    tp2BMOexe3_B,
    C3,
    C2,
    Z,
    R,
    Y,
    C,
    B,
    A,
    Client,
    Passagers,
    R_servation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_escale_is_not_abstract():
    assert not inspect.isabstract(Escale)


def test_escale_constructor_exists():
    assert callable(Escale.__init__)


def test_escale_constructor_args():
    sig = inspect.signature(Escale.__init__)
    params = list(sig.parameters.keys())



def test_vol_is_not_abstract():
    assert not inspect.isabstract(Vol)


def test_vol_constructor_exists():
    assert callable(Vol.__init__)


def test_vol_constructor_args():
    sig = inspect.signature(Vol.__init__)
    params = list(sig.parameters.keys())



def test_a_roport_is_not_abstract():
    assert not inspect.isabstract(A_roport)


def test_a_roport_constructor_exists():
    assert callable(A_roport.__init__)


def test_a_roport_constructor_args():
    sig = inspect.signature(A_roport.__init__)
    params = list(sig.parameters.keys())



def test_ville_is_not_abstract():
    assert not inspect.isabstract(Ville)


def test_ville_constructor_exists():
    assert callable(Ville.__init__)


def test_ville_constructor_args():
    sig = inspect.signature(Ville.__init__)
    params = list(sig.parameters.keys())



def test_tp2bmoexe3_a3_is_not_abstract():
    assert not inspect.isabstract(tp2BMOexe3_A3)


def test_tp2bmoexe3_a3_constructor_exists():
    assert callable(tp2BMOexe3_A3.__init__)


def test_tp2bmoexe3_a3_constructor_args():
    sig = inspect.signature(tp2BMOexe3_A3.__init__)
    params = list(sig.parameters.keys())



def test_tp2bmoexe3_a2_is_not_abstract():
    assert not inspect.isabstract(tp2BMOexe3_A2)


def test_tp2bmoexe3_a2_constructor_exists():
    assert callable(tp2BMOexe3_A2.__init__)


def test_tp2bmoexe3_a2_constructor_args():
    sig = inspect.signature(tp2BMOexe3_A2.__init__)
    params = list(sig.parameters.keys())



def test_tp2bmoexe3_a_is_not_abstract():
    assert not inspect.isabstract(tp2BMOexe3_A)


def test_tp2bmoexe3_a_constructor_exists():
    assert callable(tp2BMOexe3_A.__init__)


def test_tp2bmoexe3_a_constructor_args():
    sig = inspect.signature(tp2BMOexe3_A.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"
    assert "d" in params, "Missing parameter 'd'"
    assert "b" in params, "Missing parameter 'b'"

def test_tp2bmoexe3_a_has_c():
    assert hasattr(tp2BMOexe3_A, "c")
    descriptor = None
    for klass in tp2BMOexe3_A.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_tp2bmoexe3_a_has_d():
    assert hasattr(tp2BMOexe3_A, "d")
    descriptor = None
    for klass in tp2BMOexe3_A.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_tp2bmoexe3_a_has_b():
    assert hasattr(tp2BMOexe3_A, "b")
    descriptor = None
    for klass in tp2BMOexe3_A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_tp2bmoexe3_b2_is_not_abstract():
    assert not inspect.isabstract(tp2BMOexe3_B2)


def test_tp2bmoexe3_b2_constructor_exists():
    assert callable(tp2BMOexe3_B2.__init__)


def test_tp2bmoexe3_b2_constructor_args():
    sig = inspect.signature(tp2BMOexe3_B2.__init__)
    params = list(sig.parameters.keys())



def test_tp2bmoexe3_b_is_not_abstract():
    assert not inspect.isabstract(tp2BMOexe3_B)


def test_tp2bmoexe3_b_constructor_exists():
    assert callable(tp2BMOexe3_B.__init__)


def test_tp2bmoexe3_b_constructor_args():
    sig = inspect.signature(tp2BMOexe3_B.__init__)
    params = list(sig.parameters.keys())



def test_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_c3_constructor_exists():
    assert callable(C3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
    params = list(sig.parameters.keys())



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_r_constructor_exists():
    assert callable(R.__init__)


def test_r_constructor_args():
    sig = inspect.signature(R.__init__)
    params = list(sig.parameters.keys())



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



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "attC1" in params, "Missing parameter 'attC1'"
    assert "attC2" in params, "Missing parameter 'attC2'"

def test_c_has_attC1():
    assert hasattr(C, "attC1")
    descriptor = None
    for klass in C.__mro__:
        if "attC1" in klass.__dict__:
            descriptor = klass.__dict__["attC1"]
            break
    assert isinstance(descriptor, property)

def test_c_has_attC2():
    assert hasattr(C, "attC2")
    descriptor = None
    for klass in C.__mro__:
        if "attC2" in klass.__dict__:
            descriptor = klass.__dict__["attC2"]
            break
    assert isinstance(descriptor, property)



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())
    assert "attB" in params, "Missing parameter 'attB'"

def test_b_has_attB():
    assert hasattr(B, "attB")
    descriptor = None
    for klass in B.__mro__:
        if "attB" in klass.__dict__:
            descriptor = klass.__dict__["attB"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "attA" in params, "Missing parameter 'attA'"

def test_a_has_attA():
    assert hasattr(A, "attA")
    descriptor = None
    for klass in A.__mro__:
        if "attA" in klass.__dict__:
            descriptor = klass.__dict__["attA"]
            break
    assert isinstance(descriptor, property)



def test_client_is_not_abstract():
    assert not inspect.isabstract(Client)


def test_client_constructor_exists():
    assert callable(Client.__init__)


def test_client_constructor_args():
    sig = inspect.signature(Client.__init__)
    params = list(sig.parameters.keys())



def test_passagers_is_not_abstract():
    assert not inspect.isabstract(Passagers)


def test_passagers_constructor_exists():
    assert callable(Passagers.__init__)


def test_passagers_constructor_args():
    sig = inspect.signature(Passagers.__init__)
    params = list(sig.parameters.keys())



def test_r_servation_is_not_abstract():
    assert not inspect.isabstract(R_servation)


def test_r_servation_constructor_exists():
    assert callable(R_servation.__init__)


def test_r_servation_constructor_args():
    sig = inspect.signature(R_servation.__init__)
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
Escale_strategy = st.builds(
    Escale,
)
Vol_strategy = st.builds(
    Vol,
)
A_roport_strategy = st.builds(
    A_roport,
)
Ville_strategy = st.builds(
    Ville,
)
tp2BMOexe3_A3_strategy = st.builds(
    tp2BMOexe3_A3,
)
tp2BMOexe3_A2_strategy = st.builds(
    tp2BMOexe3_A2,
)
tp2BMOexe3_A_strategy = st.builds(
    tp2BMOexe3_A,
    c=
        st.none(),
    d=
        st.integers(),
    b=
        st.booleans()
)
tp2BMOexe3_B2_strategy = st.builds(
    tp2BMOexe3_B2,
)
tp2BMOexe3_B_strategy = st.builds(
    tp2BMOexe3_B,
)
C3_strategy = st.builds(
    C3,
)
C2_strategy = st.builds(
    C2,
)
Z_strategy = st.builds(
    Z,
)
R_strategy = st.builds(
    R,
)
Y_strategy = st.builds(
    Y,
    attY=
        safe_text
)
C_strategy = st.builds(
    C,
    attC1=
        st.integers(),
    attC2=
        st.booleans()
)
B_strategy = st.builds(
    B,
    attB=
        st.integers()
)
A_strategy = st.builds(
    A,
    attA=
        safe_text
)
Client_strategy = st.builds(
    Client,
)
Passagers_strategy = st.builds(
    Passagers,
)
R_servation_strategy = st.builds(
    R_servation,
)

@given(instance=Escale_strategy)
@settings(max_examples=50)
def test_escale_instantiation(instance):
    assert isinstance(instance, Escale)

@given(instance=Vol_strategy)
@settings(max_examples=50)
def test_vol_instantiation(instance):
    assert isinstance(instance, Vol)

@given(instance=A_roport_strategy)
@settings(max_examples=50)
def test_a_roport_instantiation(instance):
    assert isinstance(instance, A_roport)

@given(instance=Ville_strategy)
@settings(max_examples=50)
def test_ville_instantiation(instance):
    assert isinstance(instance, Ville)

@given(instance=tp2BMOexe3_A3_strategy)
@settings(max_examples=50)
def test_tp2bmoexe3_a3_instantiation(instance):
    assert isinstance(instance, tp2BMOexe3_A3)

@given(instance=tp2BMOexe3_A2_strategy)
@settings(max_examples=50)
def test_tp2bmoexe3_a2_instantiation(instance):
    assert isinstance(instance, tp2BMOexe3_A2)

@given(instance=tp2BMOexe3_A_strategy)
@settings(max_examples=50)
def test_tp2bmoexe3_a_instantiation(instance):
    assert isinstance(instance, tp2BMOexe3_A)



@given(instance=tp2BMOexe3_A_strategy)
def test_tp2bmoexe3_a_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=tp2BMOexe3_A_strategy)
def test_tp2bmoexe3_a_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=tp2BMOexe3_A_strategy)
def test_tp2bmoexe3_a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=tp2BMOexe3_B2_strategy)
@settings(max_examples=50)
def test_tp2bmoexe3_b2_instantiation(instance):
    assert isinstance(instance, tp2BMOexe3_B2)

@given(instance=tp2BMOexe3_B_strategy)
@settings(max_examples=50)
def test_tp2bmoexe3_b_instantiation(instance):
    assert isinstance(instance, tp2BMOexe3_B)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)



@given(instance=Y_strategy)
def test_y_attY_setter(instance):
    original = instance.attY
    instance.attY = original
    assert instance.attY == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_attC1_setter(instance):
    original = instance.attC1
    instance.attC1 = original
    assert instance.attC1 == original



@given(instance=C_strategy)
def test_c_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)



@given(instance=B_strategy)
def test_b_attB_setter(instance):
    original = instance.attB
    instance.attB = original
    assert instance.attB == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original

@given(instance=Client_strategy)
@settings(max_examples=50)
def test_client_instantiation(instance):
    assert isinstance(instance, Client)

@given(instance=Passagers_strategy)
@settings(max_examples=50)
def test_passagers_instantiation(instance):
    assert isinstance(instance, Passagers)

@given(instance=R_servation_strategy)
@settings(max_examples=50)
def test_r_servation_instantiation(instance):
    assert isinstance(instance, R_servation)
