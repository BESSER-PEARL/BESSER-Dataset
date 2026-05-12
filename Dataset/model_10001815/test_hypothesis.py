import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    C2,
    C11,
    C1,
    B1,
    Z,
    A1,
    R,
    Y,
    C,
    B,
    A,
    RESERVATION,
    CHAUFFEUR,
    PERMIS,
    PERSONNEL,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_c11_is_not_abstract():
    assert not inspect.isabstract(C11)


def test_c11_constructor_exists():
    assert callable(C11.__init__)


def test_c11_constructor_args():
    sig = inspect.signature(C11.__init__)
    params = list(sig.parameters.keys())



def test_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_c1_constructor_exists():
    assert callable(C1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())
    assert "attC1" in params, "Missing parameter 'attC1'"
    assert "attC2" in params, "Missing parameter 'attC2'"

def test_c1_has_attC1():
    assert hasattr(C1, "attC1")
    descriptor = None
    for klass in C1.__mro__:
        if "attC1" in klass.__dict__:
            descriptor = klass.__dict__["attC1"]
            break
    assert isinstance(descriptor, property)

def test_c1_has_attC2():
    assert hasattr(C1, "attC2")
    descriptor = None
    for klass in C1.__mro__:
        if "attC2" in klass.__dict__:
            descriptor = klass.__dict__["attC2"]
            break
    assert isinstance(descriptor, property)



def test_b1_is_not_abstract():
    assert not inspect.isabstract(B1)


def test_b1_constructor_exists():
    assert callable(B1.__init__)


def test_b1_constructor_args():
    sig = inspect.signature(B1.__init__)
    params = list(sig.parameters.keys())
    assert "attB" in params, "Missing parameter 'attB'"

def test_b1_has_attB():
    assert hasattr(B1, "attB")
    descriptor = None
    for klass in B1.__mro__:
        if "attB" in klass.__dict__:
            descriptor = klass.__dict__["attB"]
            break
    assert isinstance(descriptor, property)



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_a1_is_not_abstract():
    assert not inspect.isabstract(A1)


def test_a1_constructor_exists():
    assert callable(A1.__init__)


def test_a1_constructor_args():
    sig = inspect.signature(A1.__init__)
    params = list(sig.parameters.keys())
    assert "attA" in params, "Missing parameter 'attA'"

def test_a1_has_attA():
    assert hasattr(A1, "attA")
    descriptor = None
    for klass in A1.__mro__:
        if "attA" in klass.__dict__:
            descriptor = klass.__dict__["attA"]
            break
    assert isinstance(descriptor, property)



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



def test_reservation_is_not_abstract():
    assert not inspect.isabstract(RESERVATION)


def test_reservation_constructor_exists():
    assert callable(RESERVATION.__init__)


def test_reservation_constructor_args():
    sig = inspect.signature(RESERVATION.__init__)
    params = list(sig.parameters.keys())



def test_chauffeur_is_not_abstract():
    assert not inspect.isabstract(CHAUFFEUR)


def test_chauffeur_constructor_exists():
    assert callable(CHAUFFEUR.__init__)


def test_chauffeur_constructor_args():
    sig = inspect.signature(CHAUFFEUR.__init__)
    params = list(sig.parameters.keys())
    assert "nomPersonnel" in params, "Missing parameter 'nomPersonnel'"
    assert "prenomPersonnel" in params, "Missing parameter 'prenomPersonnel'"

def test_chauffeur_has_nomPersonnel():
    assert hasattr(CHAUFFEUR, "nomPersonnel")
    descriptor = None
    for klass in CHAUFFEUR.__mro__:
        if "nomPersonnel" in klass.__dict__:
            descriptor = klass.__dict__["nomPersonnel"]
            break
    assert isinstance(descriptor, property)

def test_chauffeur_has_prenomPersonnel():
    assert hasattr(CHAUFFEUR, "prenomPersonnel")
    descriptor = None
    for klass in CHAUFFEUR.__mro__:
        if "prenomPersonnel" in klass.__dict__:
            descriptor = klass.__dict__["prenomPersonnel"]
            break
    assert isinstance(descriptor, property)



def test_permis_is_not_abstract():
    assert not inspect.isabstract(PERMIS)


def test_permis_constructor_exists():
    assert callable(PERMIS.__init__)


def test_permis_constructor_args():
    sig = inspect.signature(PERMIS.__init__)
    params = list(sig.parameters.keys())
    assert "libPermis" in params, "Missing parameter 'libPermis'"

def test_permis_has_libPermis():
    assert hasattr(PERMIS, "libPermis")
    descriptor = None
    for klass in PERMIS.__mro__:
        if "libPermis" in klass.__dict__:
            descriptor = klass.__dict__["libPermis"]
            break
    assert isinstance(descriptor, property)



def test_personnel_is_not_abstract():
    assert not inspect.isabstract(PERSONNEL)


def test_personnel_constructor_exists():
    assert callable(PERSONNEL.__init__)


def test_personnel_constructor_args():
    sig = inspect.signature(PERSONNEL.__init__)
    params = list(sig.parameters.keys())
    assert "unPrivate" in params, "Missing parameter 'unPrivate'"
    assert "prenomPersonnel" in params, "Missing parameter 'prenomPersonnel'"
    assert "nomPersonnel" in params, "Missing parameter 'nomPersonnel'"

def test_personnel_has_unPrivate():
    assert hasattr(PERSONNEL, "unPrivate")
    descriptor = None
    for klass in PERSONNEL.__mro__:
        if "unPrivate" in klass.__dict__:
            descriptor = klass.__dict__["unPrivate"]
            break
    assert isinstance(descriptor, property)

def test_personnel_has_prenomPersonnel():
    assert hasattr(PERSONNEL, "prenomPersonnel")
    descriptor = None
    for klass in PERSONNEL.__mro__:
        if "prenomPersonnel" in klass.__dict__:
            descriptor = klass.__dict__["prenomPersonnel"]
            break
    assert isinstance(descriptor, property)

def test_personnel_has_nomPersonnel():
    assert hasattr(PERSONNEL, "nomPersonnel")
    descriptor = None
    for klass in PERSONNEL.__mro__:
        if "nomPersonnel" in klass.__dict__:
            descriptor = klass.__dict__["nomPersonnel"]
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
C2_strategy = st.builds(
    C2,
)
C11_strategy = st.builds(
    C11,
)
C1_strategy = st.builds(
    C1,
    attC1=
        st.integers(),
    attC2=
        st.booleans()
)
B1_strategy = st.builds(
    B1,
    attB=
        st.integers()
)
Z_strategy = st.builds(
    Z,
)
A1_strategy = st.builds(
    A1,
    attA=
        safe_text
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
RESERVATION_strategy = st.builds(
    RESERVATION,
)
CHAUFFEUR_strategy = st.builds(
    CHAUFFEUR,
    nomPersonnel=
        safe_text,
    prenomPersonnel=
        safe_text
)
PERMIS_strategy = st.builds(
    PERMIS,
    libPermis=
        safe_text
)
PERSONNEL_strategy = st.builds(
    PERSONNEL,
    unPrivate=
        st.booleans(),
    prenomPersonnel=
        safe_text,
    nomPersonnel=
        safe_text
)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=C11_strategy)
@settings(max_examples=50)
def test_c11_instantiation(instance):
    assert isinstance(instance, C11)

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)



@given(instance=C1_strategy)
def test_c1_attC1_setter(instance):
    original = instance.attC1
    instance.attC1 = original
    assert instance.attC1 == original



@given(instance=C1_strategy)
def test_c1_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original

@given(instance=B1_strategy)
@settings(max_examples=50)
def test_b1_instantiation(instance):
    assert isinstance(instance, B1)



@given(instance=B1_strategy)
def test_b1_attB_setter(instance):
    original = instance.attB
    instance.attB = original
    assert instance.attB == original

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=A1_strategy)
@settings(max_examples=50)
def test_a1_instantiation(instance):
    assert isinstance(instance, A1)



@given(instance=A1_strategy)
def test_a1_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original

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

@given(instance=RESERVATION_strategy)
@settings(max_examples=50)
def test_reservation_instantiation(instance):
    assert isinstance(instance, RESERVATION)

@given(instance=CHAUFFEUR_strategy)
@settings(max_examples=50)
def test_chauffeur_instantiation(instance):
    assert isinstance(instance, CHAUFFEUR)



@given(instance=CHAUFFEUR_strategy)
def test_chauffeur_nomPersonnel_setter(instance):
    original = instance.nomPersonnel
    instance.nomPersonnel = original
    assert instance.nomPersonnel == original



@given(instance=CHAUFFEUR_strategy)
def test_chauffeur_prenomPersonnel_setter(instance):
    original = instance.prenomPersonnel
    instance.prenomPersonnel = original
    assert instance.prenomPersonnel == original

@given(instance=PERMIS_strategy)
@settings(max_examples=50)
def test_permis_instantiation(instance):
    assert isinstance(instance, PERMIS)



@given(instance=PERMIS_strategy)
def test_permis_libPermis_setter(instance):
    original = instance.libPermis
    instance.libPermis = original
    assert instance.libPermis == original

@given(instance=PERSONNEL_strategy)
@settings(max_examples=50)
def test_personnel_instantiation(instance):
    assert isinstance(instance, PERSONNEL)



@given(instance=PERSONNEL_strategy)
def test_personnel_unPrivate_setter(instance):
    original = instance.unPrivate
    instance.unPrivate = original
    assert instance.unPrivate == original



@given(instance=PERSONNEL_strategy)
def test_personnel_prenomPersonnel_setter(instance):
    original = instance.prenomPersonnel
    instance.prenomPersonnel = original
    assert instance.prenomPersonnel == original



@given(instance=PERSONNEL_strategy)
def test_personnel_nomPersonnel_setter(instance):
    original = instance.nomPersonnel
    instance.nomPersonnel = original
    assert instance.nomPersonnel == original
