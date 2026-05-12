import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    F,
    E,
    PACS,
    Mariage,
    Union,
    Personne,
    Class,
    R,
    Y,
    Z,
    C3,
    C2,
    C1,
    B1,
    A1,
    C,
    B,
    A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_pacs_is_not_abstract():
    assert not inspect.isabstract(PACS)


def test_pacs_constructor_exists():
    assert callable(PACS.__init__)


def test_pacs_constructor_args():
    sig = inspect.signature(PACS.__init__)
    params = list(sig.parameters.keys())



def test_mariage_is_not_abstract():
    assert not inspect.isabstract(Mariage)


def test_mariage_constructor_exists():
    assert callable(Mariage.__init__)


def test_mariage_constructor_args():
    sig = inspect.signature(Mariage.__init__)
    params = list(sig.parameters.keys())



def test_union_is_not_abstract():
    assert not inspect.isabstract(Union)


def test_union_constructor_exists():
    assert callable(Union.__init__)


def test_union_constructor_args():
    sig = inspect.signature(Union.__init__)
    params = list(sig.parameters.keys())
    assert "dateUnion" in params, "Missing parameter 'dateUnion'"

def test_union_has_dateUnion():
    assert hasattr(Union, "dateUnion")
    descriptor = None
    for klass in Union.__mro__:
        if "dateUnion" in klass.__dict__:
            descriptor = klass.__dict__["dateUnion"]
            break
    assert isinstance(descriptor, property)



def test_personne_is_not_abstract():
    assert not inspect.isabstract(Personne)


def test_personne_constructor_exists():
    assert callable(Personne.__init__)


def test_personne_constructor_args():
    sig = inspect.signature(Personne.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
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



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
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



def test_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_c1_constructor_exists():
    assert callable(C1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())
    assert "attC2" in params, "Missing parameter 'attC2'"
    assert "attC1" in params, "Missing parameter 'attC1'"

def test_c1_has_attC2():
    assert hasattr(C1, "attC2")
    descriptor = None
    for klass in C1.__mro__:
        if "attC2" in klass.__dict__:
            descriptor = klass.__dict__["attC2"]
            break
    assert isinstance(descriptor, property)

def test_c1_has_attC1():
    assert hasattr(C1, "attC1")
    descriptor = None
    for klass in C1.__mro__:
        if "attC1" in klass.__dict__:
            descriptor = klass.__dict__["attC1"]
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



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "attC2" in params, "Missing parameter 'attC2'"
    assert "attC1" in params, "Missing parameter 'attC1'"

def test_c_has_attC2():
    assert hasattr(C, "attC2")
    descriptor = None
    for klass in C.__mro__:
        if "attC2" in klass.__dict__:
            descriptor = klass.__dict__["attC2"]
            break
    assert isinstance(descriptor, property)

def test_c_has_attC1():
    assert hasattr(C, "attC1")
    descriptor = None
    for klass in C.__mro__:
        if "attC1" in klass.__dict__:
            descriptor = klass.__dict__["attC1"]
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
PACS_strategy = st.builds(
    PACS,
)
Mariage_strategy = st.builds(
    Mariage,
)
Union_strategy = st.builds(
    Union,
    dateUnion=
        safe_text
)
Personne_strategy = st.builds(
    Personne,
)
Class_strategy = st.builds(
    Class,
)
R_strategy = st.builds(
    R,
)
Y_strategy = st.builds(
    Y,
    attY=
        safe_text
)
Z_strategy = st.builds(
    Z,
)
C3_strategy = st.builds(
    C3,
)
C2_strategy = st.builds(
    C2,
)
C1_strategy = st.builds(
    C1,
    attC2=
        st.booleans(),
    attC1=
        st.integers()
)
B1_strategy = st.builds(
    B1,
    attB=
        st.integers()
)
A1_strategy = st.builds(
    A1,
    attA=
        safe_text
)
C_strategy = st.builds(
    C,
    attC2=
        st.booleans(),
    attC1=
        st.integers()
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

@given(instance=PACS_strategy)
@settings(max_examples=50)
def test_pacs_instantiation(instance):
    assert isinstance(instance, PACS)

@given(instance=Mariage_strategy)
@settings(max_examples=50)
def test_mariage_instantiation(instance):
    assert isinstance(instance, Mariage)

@given(instance=Union_strategy)
@settings(max_examples=50)
def test_union_instantiation(instance):
    assert isinstance(instance, Union)



@given(instance=Union_strategy)
def test_union_dateUnion_setter(instance):
    original = instance.dateUnion
    instance.dateUnion = original
    assert instance.dateUnion == original

@given(instance=Personne_strategy)
@settings(max_examples=50)
def test_personne_instantiation(instance):
    assert isinstance(instance, Personne)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

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

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=C3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, C3)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)



@given(instance=C1_strategy)
def test_c1_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original



@given(instance=C1_strategy)
def test_c1_attC1_setter(instance):
    original = instance.attC1
    instance.attC1 = original
    assert instance.attC1 == original

@given(instance=B1_strategy)
@settings(max_examples=50)
def test_b1_instantiation(instance):
    assert isinstance(instance, B1)



@given(instance=B1_strategy)
def test_b1_attB_setter(instance):
    original = instance.attB
    instance.attB = original
    assert instance.attB == original

@given(instance=A1_strategy)
@settings(max_examples=50)
def test_a1_instantiation(instance):
    assert isinstance(instance, A1)



@given(instance=A1_strategy)
def test_a1_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original



@given(instance=C_strategy)
def test_c_attC1_setter(instance):
    original = instance.attC1
    instance.attC1 = original
    assert instance.attC1 == original

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
