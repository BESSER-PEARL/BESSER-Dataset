import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    exo6_Triangle,
    exo6_Point,
    exo6_Polygone,
    model2_R,
    model2_B,
    model2_Y,
    model2_A,
    model2_Z,
    model2_C,
    model2_C2,
    model2_C1,
    C,
    B,
    A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_exo6_triangle_is_not_abstract():
    assert not inspect.isabstract(exo6_Triangle)


def test_exo6_triangle_constructor_exists():
    assert callable(exo6_Triangle.__init__)


def test_exo6_triangle_constructor_args():
    sig = inspect.signature(exo6_Triangle.__init__)
    params = list(sig.parameters.keys())



def test_exo6_point_is_not_abstract():
    assert not inspect.isabstract(exo6_Point)


def test_exo6_point_constructor_exists():
    assert callable(exo6_Point.__init__)


def test_exo6_point_constructor_args():
    sig = inspect.signature(exo6_Point.__init__)
    params = list(sig.parameters.keys())
    assert "ordonnee" in params, "Missing parameter 'ordonnee'"
    assert "abcisse" in params, "Missing parameter 'abcisse'"

def test_exo6_point_has_ordonnee():
    assert hasattr(exo6_Point, "ordonnee")
    descriptor = None
    for klass in exo6_Point.__mro__:
        if "ordonnee" in klass.__dict__:
            descriptor = klass.__dict__["ordonnee"]
            break
    assert isinstance(descriptor, property)

def test_exo6_point_has_abcisse():
    assert hasattr(exo6_Point, "abcisse")
    descriptor = None
    for klass in exo6_Point.__mro__:
        if "abcisse" in klass.__dict__:
            descriptor = klass.__dict__["abcisse"]
            break
    assert isinstance(descriptor, property)



def test_exo6_polygone_is_not_abstract():
    assert not inspect.isabstract(exo6_Polygone)


def test_exo6_polygone_constructor_exists():
    assert callable(exo6_Polygone.__init__)


def test_exo6_polygone_constructor_args():
    sig = inspect.signature(exo6_Polygone.__init__)
    params = list(sig.parameters.keys())
    assert "sommets" in params, "Missing parameter 'sommets'"

def test_exo6_polygone_has_sommets():
    assert hasattr(exo6_Polygone, "sommets")
    descriptor = None
    for klass in exo6_Polygone.__mro__:
        if "sommets" in klass.__dict__:
            descriptor = klass.__dict__["sommets"]
            break
    assert isinstance(descriptor, property)



def test_model2_r_is_not_abstract():
    assert not inspect.isabstract(model2_R)


def test_model2_r_constructor_exists():
    assert callable(model2_R.__init__)


def test_model2_r_constructor_args():
    sig = inspect.signature(model2_R.__init__)
    params = list(sig.parameters.keys())



def test_model2_b_is_not_abstract():
    assert not inspect.isabstract(model2_B)


def test_model2_b_constructor_exists():
    assert callable(model2_B.__init__)


def test_model2_b_constructor_args():
    sig = inspect.signature(model2_B.__init__)
    params = list(sig.parameters.keys())
    assert "attB" in params, "Missing parameter 'attB'"

def test_model2_b_has_attB():
    assert hasattr(model2_B, "attB")
    descriptor = None
    for klass in model2_B.__mro__:
        if "attB" in klass.__dict__:
            descriptor = klass.__dict__["attB"]
            break
    assert isinstance(descriptor, property)



def test_model2_y_is_not_abstract():
    assert not inspect.isabstract(model2_Y)


def test_model2_y_constructor_exists():
    assert callable(model2_Y.__init__)


def test_model2_y_constructor_args():
    sig = inspect.signature(model2_Y.__init__)
    params = list(sig.parameters.keys())
    assert "attY" in params, "Missing parameter 'attY'"

def test_model2_y_has_attY():
    assert hasattr(model2_Y, "attY")
    descriptor = None
    for klass in model2_Y.__mro__:
        if "attY" in klass.__dict__:
            descriptor = klass.__dict__["attY"]
            break
    assert isinstance(descriptor, property)



def test_model2_a_is_not_abstract():
    assert not inspect.isabstract(model2_A)


def test_model2_a_constructor_exists():
    assert callable(model2_A.__init__)


def test_model2_a_constructor_args():
    sig = inspect.signature(model2_A.__init__)
    params = list(sig.parameters.keys())
    assert "attA" in params, "Missing parameter 'attA'"

def test_model2_a_has_attA():
    assert hasattr(model2_A, "attA")
    descriptor = None
    for klass in model2_A.__mro__:
        if "attA" in klass.__dict__:
            descriptor = klass.__dict__["attA"]
            break
    assert isinstance(descriptor, property)



def test_model2_z_is_not_abstract():
    assert not inspect.isabstract(model2_Z)


def test_model2_z_constructor_exists():
    assert callable(model2_Z.__init__)


def test_model2_z_constructor_args():
    sig = inspect.signature(model2_Z.__init__)
    params = list(sig.parameters.keys())



def test_model2_c_is_not_abstract():
    assert not inspect.isabstract(model2_C)


def test_model2_c_constructor_exists():
    assert callable(model2_C.__init__)


def test_model2_c_constructor_args():
    sig = inspect.signature(model2_C.__init__)
    params = list(sig.parameters.keys())
    assert "attC2" in params, "Missing parameter 'attC2'"
    assert "attC1" in params, "Missing parameter 'attC1'"

def test_model2_c_has_attC2():
    assert hasattr(model2_C, "attC2")
    descriptor = None
    for klass in model2_C.__mro__:
        if "attC2" in klass.__dict__:
            descriptor = klass.__dict__["attC2"]
            break
    assert isinstance(descriptor, property)

def test_model2_c_has_attC1():
    assert hasattr(model2_C, "attC1")
    descriptor = None
    for klass in model2_C.__mro__:
        if "attC1" in klass.__dict__:
            descriptor = klass.__dict__["attC1"]
            break
    assert isinstance(descriptor, property)



def test_model2_c2_is_not_abstract():
    assert not inspect.isabstract(model2_C2)


def test_model2_c2_constructor_exists():
    assert callable(model2_C2.__init__)


def test_model2_c2_constructor_args():
    sig = inspect.signature(model2_C2.__init__)
    params = list(sig.parameters.keys())



def test_model2_c1_is_not_abstract():
    assert not inspect.isabstract(model2_C1)


def test_model2_c1_constructor_exists():
    assert callable(model2_C1.__init__)


def test_model2_c1_constructor_args():
    sig = inspect.signature(model2_C1.__init__)
    params = list(sig.parameters.keys())



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
Class_strategy = st.builds(
    Class,
)
exo6_Triangle_strategy = st.builds(
    exo6_Triangle,
)
exo6_Point_strategy = st.builds(
    exo6_Point,
    ordonnee=
        st.none(),
    abcisse=
        st.none()
)
exo6_Polygone_strategy = st.builds(
    exo6_Polygone,
    sommets=
        st.none()
)
model2_R_strategy = st.builds(
    model2_R,
)
model2_B_strategy = st.builds(
    model2_B,
    attB=
        st.integers()
)
model2_Y_strategy = st.builds(
    model2_Y,
    attY=
        safe_text
)
model2_A_strategy = st.builds(
    model2_A,
    attA=
        safe_text
)
model2_Z_strategy = st.builds(
    model2_Z,
)
model2_C_strategy = st.builds(
    model2_C,
    attC2=
        st.booleans(),
    attC1=
        st.integers()
)
model2_C2_strategy = st.builds(
    model2_C2,
)
model2_C1_strategy = st.builds(
    model2_C1,
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

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=exo6_Triangle_strategy)
@settings(max_examples=50)
def test_exo6_triangle_instantiation(instance):
    assert isinstance(instance, exo6_Triangle)

@given(instance=exo6_Point_strategy)
@settings(max_examples=50)
def test_exo6_point_instantiation(instance):
    assert isinstance(instance, exo6_Point)



@given(instance=exo6_Point_strategy)
def test_exo6_point_ordonnee_setter(instance):
    original = instance.ordonnee
    instance.ordonnee = original
    assert instance.ordonnee == original



@given(instance=exo6_Point_strategy)
def test_exo6_point_abcisse_setter(instance):
    original = instance.abcisse
    instance.abcisse = original
    assert instance.abcisse == original

@given(instance=exo6_Polygone_strategy)
@settings(max_examples=50)
def test_exo6_polygone_instantiation(instance):
    assert isinstance(instance, exo6_Polygone)



@given(instance=exo6_Polygone_strategy)
def test_exo6_polygone_sommets_setter(instance):
    original = instance.sommets
    instance.sommets = original
    assert instance.sommets == original

@given(instance=model2_R_strategy)
@settings(max_examples=50)
def test_model2_r_instantiation(instance):
    assert isinstance(instance, model2_R)

@given(instance=model2_B_strategy)
@settings(max_examples=50)
def test_model2_b_instantiation(instance):
    assert isinstance(instance, model2_B)



@given(instance=model2_B_strategy)
def test_model2_b_attB_setter(instance):
    original = instance.attB
    instance.attB = original
    assert instance.attB == original

@given(instance=model2_Y_strategy)
@settings(max_examples=50)
def test_model2_y_instantiation(instance):
    assert isinstance(instance, model2_Y)



@given(instance=model2_Y_strategy)
def test_model2_y_attY_setter(instance):
    original = instance.attY
    instance.attY = original
    assert instance.attY == original

@given(instance=model2_A_strategy)
@settings(max_examples=50)
def test_model2_a_instantiation(instance):
    assert isinstance(instance, model2_A)



@given(instance=model2_A_strategy)
def test_model2_a_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original

@given(instance=model2_Z_strategy)
@settings(max_examples=50)
def test_model2_z_instantiation(instance):
    assert isinstance(instance, model2_Z)

@given(instance=model2_C_strategy)
@settings(max_examples=50)
def test_model2_c_instantiation(instance):
    assert isinstance(instance, model2_C)



@given(instance=model2_C_strategy)
def test_model2_c_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original



@given(instance=model2_C_strategy)
def test_model2_c_attC1_setter(instance):
    original = instance.attC1
    instance.attC1 = original
    assert instance.attC1 == original

@given(instance=model2_C2_strategy)
@settings(max_examples=50)
def test_model2_c2_instantiation(instance):
    assert isinstance(instance, model2_C2)

@given(instance=model2_C1_strategy)
@settings(max_examples=50)
def test_model2_c1_instantiation(instance):
    assert isinstance(instance, model2_C1)

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
