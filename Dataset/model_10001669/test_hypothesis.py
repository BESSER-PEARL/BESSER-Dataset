import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Vol,
    Aeroport,
    C,
    B,
    A,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_vol_is_not_abstract():
    assert not inspect.isabstract(Vol)


def test_vol_constructor_exists():
    assert callable(Vol.__init__)


def test_vol_constructor_args():
    sig = inspect.signature(Vol.__init__)
    params = list(sig.parameters.keys())
    assert "dateHeureArrivee" in params, "Missing parameter 'dateHeureArrivee'"
    assert "dateHeureDepart" in params, "Missing parameter 'dateHeureDepart'"
    assert "numeroVol" in params, "Missing parameter 'numeroVol'"
    assert "etatVol" in params, "Missing parameter 'etatVol'"

def test_vol_has_dateHeureArrivee():
    assert hasattr(Vol, "dateHeureArrivee")
    descriptor = None
    for klass in Vol.__mro__:
        if "dateHeureArrivee" in klass.__dict__:
            descriptor = klass.__dict__["dateHeureArrivee"]
            break
    assert isinstance(descriptor, property)

def test_vol_has_dateHeureDepart():
    assert hasattr(Vol, "dateHeureDepart")
    descriptor = None
    for klass in Vol.__mro__:
        if "dateHeureDepart" in klass.__dict__:
            descriptor = klass.__dict__["dateHeureDepart"]
            break
    assert isinstance(descriptor, property)

def test_vol_has_numeroVol():
    assert hasattr(Vol, "numeroVol")
    descriptor = None
    for klass in Vol.__mro__:
        if "numeroVol" in klass.__dict__:
            descriptor = klass.__dict__["numeroVol"]
            break
    assert isinstance(descriptor, property)

def test_vol_has_etatVol():
    assert hasattr(Vol, "etatVol")
    descriptor = None
    for klass in Vol.__mro__:
        if "etatVol" in klass.__dict__:
            descriptor = klass.__dict__["etatVol"]
            break
    assert isinstance(descriptor, property)



def test_aeroport_is_not_abstract():
    assert not inspect.isabstract(Aeroport)


def test_aeroport_constructor_exists():
    assert callable(Aeroport.__init__)


def test_aeroport_constructor_args():
    sig = inspect.signature(Aeroport.__init__)
    params = list(sig.parameters.keys())
    assert "altitude" in params, "Missing parameter 'altitude'"
    assert "nomAeroport" in params, "Missing parameter 'nomAeroport'"

def test_aeroport_has_altitude():
    assert hasattr(Aeroport, "altitude")
    descriptor = None
    for klass in Aeroport.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)

def test_aeroport_has_nomAeroport():
    assert hasattr(Aeroport, "nomAeroport")
    descriptor = None
    for klass in Aeroport.__mro__:
        if "nomAeroport" in klass.__dict__:
            descriptor = klass.__dict__["nomAeroport"]
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

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
Vol_strategy = st.builds(
    Vol,
    dateHeureArrivee=
        safe_text,
    dateHeureDepart=
        safe_text,
    numeroVol=
        safe_text,
    etatVol=
        st.none()
)
Aeroport_strategy = st.builds(
    Aeroport,
    altitude=
        st.integers(),
    nomAeroport=
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

@given(instance=Vol_strategy)
@settings(max_examples=50)
def test_vol_instantiation(instance):
    assert isinstance(instance, Vol)



@given(instance=Vol_strategy)
def test_vol_dateHeureArrivee_setter(instance):
    original = instance.dateHeureArrivee
    instance.dateHeureArrivee = original
    assert instance.dateHeureArrivee == original



@given(instance=Vol_strategy)
def test_vol_dateHeureDepart_setter(instance):
    original = instance.dateHeureDepart
    instance.dateHeureDepart = original
    assert instance.dateHeureDepart == original



@given(instance=Vol_strategy)
def test_vol_numeroVol_setter(instance):
    original = instance.numeroVol
    instance.numeroVol = original
    assert instance.numeroVol == original



@given(instance=Vol_strategy)
def test_vol_etatVol_setter(instance):
    original = instance.etatVol
    instance.etatVol = original
    assert instance.etatVol == original

@given(instance=Aeroport_strategy)
@settings(max_examples=50)
def test_aeroport_instantiation(instance):
    assert isinstance(instance, Aeroport)



@given(instance=Aeroport_strategy)
def test_aeroport_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original



@given(instance=Aeroport_strategy)
def test_aeroport_nomAeroport_setter(instance):
    original = instance.nomAeroport
    instance.nomAeroport = original
    assert instance.nomAeroport == original

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
