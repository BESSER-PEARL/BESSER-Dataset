import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    D3_B,
    B,
    D3,
    abcd_D3_B,
    D,
    abcd_D3,
    abcd_D2,
    abcd_D1,
    C,
    abcd_D3_B_C,
    abcd_C2,
    abcd_C1,
    NamedElt,
    abcd_Other,
    abcd_A,
    abcd_Model,
    abcd_NamedElt,
    A,
    abcd_D,
    abcd_B,
    abcd_C,
    StyleKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d3_b_is_not_abstract():
    assert not inspect.isabstract(D3_B)


def test_d3_b_constructor_exists():
    assert callable(D3_B.__init__)


def test_d3_b_constructor_args():
    sig = inspect.signature(D3_B.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_d3_is_not_abstract():
    assert not inspect.isabstract(D3)


def test_d3_constructor_exists():
    assert callable(D3.__init__)


def test_d3_constructor_args():
    sig = inspect.signature(D3.__init__)
    params = list(sig.parameters.keys())



def test_abcd_d3_b_is_not_abstract():
    assert not inspect.isabstract(abcd_D3_B)


def test_abcd_d3_b_constructor_exists():
    assert callable(abcd_D3_B.__init__)


def test_abcd_d3_b_constructor_args():
    sig = inspect.signature(abcd_D3_B.__init__)
    params = list(sig.parameters.keys())



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_abcd_d3_is_not_abstract():
    assert not inspect.isabstract(abcd_D3)


def test_abcd_d3_constructor_exists():
    assert callable(abcd_D3.__init__)


def test_abcd_d3_constructor_args():
    sig = inspect.signature(abcd_D3.__init__)
    params = list(sig.parameters.keys())
    assert "commonOfD" in params, "Missing parameter 'commonOfD'"

def test_abcd_d3_has_commonOfD():
    assert hasattr(abcd_D3, "commonOfD")
    descriptor = None
    for klass in abcd_D3.__mro__:
        if "commonOfD" in klass.__dict__:
            descriptor = klass.__dict__["commonOfD"]
            break
    assert isinstance(descriptor, property)



def test_abcd_d2_is_not_abstract():
    assert not inspect.isabstract(abcd_D2)


def test_abcd_d2_constructor_exists():
    assert callable(abcd_D2.__init__)


def test_abcd_d2_constructor_args():
    sig = inspect.signature(abcd_D2.__init__)
    params = list(sig.parameters.keys())
    assert "commonOfD" in params, "Missing parameter 'commonOfD'"

def test_abcd_d2_has_commonOfD():
    assert hasattr(abcd_D2, "commonOfD")
    descriptor = None
    for klass in abcd_D2.__mro__:
        if "commonOfD" in klass.__dict__:
            descriptor = klass.__dict__["commonOfD"]
            break
    assert isinstance(descriptor, property)



def test_abcd_d1_is_not_abstract():
    assert not inspect.isabstract(abcd_D1)


def test_abcd_d1_constructor_exists():
    assert callable(abcd_D1.__init__)


def test_abcd_d1_constructor_args():
    sig = inspect.signature(abcd_D1.__init__)
    params = list(sig.parameters.keys())
    assert "commonOfD" in params, "Missing parameter 'commonOfD'"

def test_abcd_d1_has_commonOfD():
    assert hasattr(abcd_D1, "commonOfD")
    descriptor = None
    for klass in abcd_D1.__mro__:
        if "commonOfD" in klass.__dict__:
            descriptor = klass.__dict__["commonOfD"]
            break
    assert isinstance(descriptor, property)



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_abcd_d3_b_c_is_not_abstract():
    assert not inspect.isabstract(abcd_D3_B_C)


def test_abcd_d3_b_c_constructor_exists():
    assert callable(abcd_D3_B_C.__init__)


def test_abcd_d3_b_c_constructor_args():
    sig = inspect.signature(abcd_D3_B_C.__init__)
    params = list(sig.parameters.keys())



def test_abcd_c2_is_not_abstract():
    assert not inspect.isabstract(abcd_C2)


def test_abcd_c2_constructor_exists():
    assert callable(abcd_C2.__init__)


def test_abcd_c2_constructor_args():
    sig = inspect.signature(abcd_C2.__init__)
    params = list(sig.parameters.keys())
    assert "propOfC2" in params, "Missing parameter 'propOfC2'"

def test_abcd_c2_has_propOfC2():
    assert hasattr(abcd_C2, "propOfC2")
    descriptor = None
    for klass in abcd_C2.__mro__:
        if "propOfC2" in klass.__dict__:
            descriptor = klass.__dict__["propOfC2"]
            break
    assert isinstance(descriptor, property)



def test_abcd_c1_is_not_abstract():
    assert not inspect.isabstract(abcd_C1)


def test_abcd_c1_constructor_exists():
    assert callable(abcd_C1.__init__)


def test_abcd_c1_constructor_args():
    sig = inspect.signature(abcd_C1.__init__)
    params = list(sig.parameters.keys())
    assert "propOfC1" in params, "Missing parameter 'propOfC1'"

def test_abcd_c1_has_propOfC1():
    assert hasattr(abcd_C1, "propOfC1")
    descriptor = None
    for klass in abcd_C1.__mro__:
        if "propOfC1" in klass.__dict__:
            descriptor = klass.__dict__["propOfC1"]
            break
    assert isinstance(descriptor, property)



def test_namedelt_is_not_abstract():
    assert not inspect.isabstract(NamedElt)


def test_namedelt_constructor_exists():
    assert callable(NamedElt.__init__)


def test_namedelt_constructor_args():
    sig = inspect.signature(NamedElt.__init__)
    params = list(sig.parameters.keys())



def test_abcd_other_is_not_abstract():
    assert not inspect.isabstract(abcd_Other)


def test_abcd_other_constructor_exists():
    assert callable(abcd_Other.__init__)


def test_abcd_other_constructor_args():
    sig = inspect.signature(abcd_Other.__init__)
    params = list(sig.parameters.keys())



def test_abcd_a_is_not_abstract():
    assert not inspect.isabstract(abcd_A)


def test_abcd_a_constructor_exists():
    assert callable(abcd_A.__init__)


def test_abcd_a_constructor_args():
    sig = inspect.signature(abcd_A.__init__)
    params = list(sig.parameters.keys())
    assert "aBooleanAttr" in params, "Missing parameter 'aBooleanAttr'"
    assert "anIntegerAttr" in params, "Missing parameter 'anIntegerAttr'"

def test_abcd_a_has_aBooleanAttr():
    assert hasattr(abcd_A, "aBooleanAttr")
    descriptor = None
    for klass in abcd_A.__mro__:
        if "aBooleanAttr" in klass.__dict__:
            descriptor = klass.__dict__["aBooleanAttr"]
            break
    assert isinstance(descriptor, property)

def test_abcd_a_has_anIntegerAttr():
    assert hasattr(abcd_A, "anIntegerAttr")
    descriptor = None
    for klass in abcd_A.__mro__:
        if "anIntegerAttr" in klass.__dict__:
            descriptor = klass.__dict__["anIntegerAttr"]
            break
    assert isinstance(descriptor, property)



def test_abcd_model_is_not_abstract():
    assert not inspect.isabstract(abcd_Model)


def test_abcd_model_constructor_exists():
    assert callable(abcd_Model.__init__)


def test_abcd_model_constructor_args():
    sig = inspect.signature(abcd_Model.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"

def test_abcd_model_has_style():
    assert hasattr(abcd_Model, "style")
    descriptor = None
    for klass in abcd_Model.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_abcd_namedelt_is_not_abstract():
    assert not inspect.isabstract(abcd_NamedElt)


def test_abcd_namedelt_constructor_exists():
    assert callable(abcd_NamedElt.__init__)


def test_abcd_namedelt_constructor_args():
    sig = inspect.signature(abcd_NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abcd_namedelt_has_name():
    assert hasattr(abcd_NamedElt, "name")
    descriptor = None
    for klass in abcd_NamedElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_abcd_d_is_not_abstract():
    assert not inspect.isabstract(abcd_D)


def test_abcd_d_constructor_exists():
    assert callable(abcd_D.__init__)


def test_abcd_d_constructor_args():
    sig = inspect.signature(abcd_D.__init__)
    params = list(sig.parameters.keys())
    assert "propOfD" in params, "Missing parameter 'propOfD'"

def test_abcd_d_has_propOfD():
    assert hasattr(abcd_D, "propOfD")
    descriptor = None
    for klass in abcd_D.__mro__:
        if "propOfD" in klass.__dict__:
            descriptor = klass.__dict__["propOfD"]
            break
    assert isinstance(descriptor, property)



def test_abcd_b_is_not_abstract():
    assert not inspect.isabstract(abcd_B)


def test_abcd_b_constructor_exists():
    assert callable(abcd_B.__init__)


def test_abcd_b_constructor_args():
    sig = inspect.signature(abcd_B.__init__)
    params = list(sig.parameters.keys())
    assert "propOfB" in params, "Missing parameter 'propOfB'"

def test_abcd_b_has_propOfB():
    assert hasattr(abcd_B, "propOfB")
    descriptor = None
    for klass in abcd_B.__mro__:
        if "propOfB" in klass.__dict__:
            descriptor = klass.__dict__["propOfB"]
            break
    assert isinstance(descriptor, property)



def test_abcd_c_is_not_abstract():
    assert not inspect.isabstract(abcd_C)


def test_abcd_c_constructor_exists():
    assert callable(abcd_C.__init__)


def test_abcd_c_constructor_args():
    sig = inspect.signature(abcd_C.__init__)
    params = list(sig.parameters.keys())
    assert "propOfC" in params, "Missing parameter 'propOfC'"

def test_abcd_c_has_propOfC():
    assert hasattr(abcd_C, "propOfC")
    descriptor = None
    for klass in abcd_C.__mro__:
        if "propOfC" in klass.__dict__:
            descriptor = klass.__dict__["propOfC"]
            break
    assert isinstance(descriptor, property)

def test_stylekind_exists():
    # Check that the Enumeration exists
    assert StyleKind is not None

def test_stylekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StyleKind]
    expected_literals = [
        "Style1",
        "Style2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StyleKind"


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
D3_B_strategy = st.builds(
    D3_B,
)
B_strategy = st.builds(
    B,
)
D3_strategy = st.builds(
    D3,
)
abcd_D3_B_strategy = st.builds(
    abcd_D3_B,
)
D_strategy = st.builds(
    D,
)
abcd_D3_strategy = st.builds(
    abcd_D3,
    commonOfD=
        safe_text
)
abcd_D2_strategy = st.builds(
    abcd_D2,
    commonOfD=
        safe_text
)
abcd_D1_strategy = st.builds(
    abcd_D1,
    commonOfD=
        safe_text
)
C_strategy = st.builds(
    C,
)
abcd_D3_B_C_strategy = st.builds(
    abcd_D3_B_C,
)
abcd_C2_strategy = st.builds(
    abcd_C2,
    propOfC2=
        safe_text
)
abcd_C1_strategy = st.builds(
    abcd_C1,
    propOfC1=
        safe_text
)
NamedElt_strategy = st.builds(
    NamedElt,
)
abcd_Other_strategy = st.builds(
    abcd_Other,
)
abcd_A_strategy = st.builds(
    abcd_A,
    aBooleanAttr=
        safe_text,
    anIntegerAttr=
        st.integers()
)
abcd_Model_strategy = st.builds(
    abcd_Model,
    style=
        safe_text
)
abcd_NamedElt_strategy = st.builds(
    abcd_NamedElt,
    name=
        safe_text
)
A_strategy = st.builds(
    A,
)
abcd_D_strategy = st.builds(
    abcd_D,
    propOfD=
        safe_text
)
abcd_B_strategy = st.builds(
    abcd_B,
    propOfB=
        safe_text
)
abcd_C_strategy = st.builds(
    abcd_C,
    propOfC=
        safe_text
)

@given(instance=D3_B_strategy)
@settings(max_examples=50)
def test_d3_b_instantiation(instance):
    assert isinstance(instance, D3_B)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=D3_strategy)
@settings(max_examples=50)
def test_d3_instantiation(instance):
    assert isinstance(instance, D3)

@given(instance=abcd_D3_B_strategy)
@settings(max_examples=50)
def test_abcd_d3_b_instantiation(instance):
    assert isinstance(instance, abcd_D3_B)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=abcd_D3_strategy)
@settings(max_examples=50)
def test_abcd_d3_instantiation(instance):
    assert isinstance(instance, abcd_D3)



@given(instance=abcd_D3_strategy)
def test_abcd_d3_commonOfD_setter(instance):
    original = instance.commonOfD
    instance.commonOfD = original
    assert instance.commonOfD == original

@given(instance=abcd_D2_strategy)
@settings(max_examples=50)
def test_abcd_d2_instantiation(instance):
    assert isinstance(instance, abcd_D2)



@given(instance=abcd_D2_strategy)
def test_abcd_d2_commonOfD_setter(instance):
    original = instance.commonOfD
    instance.commonOfD = original
    assert instance.commonOfD == original

@given(instance=abcd_D1_strategy)
@settings(max_examples=50)
def test_abcd_d1_instantiation(instance):
    assert isinstance(instance, abcd_D1)



@given(instance=abcd_D1_strategy)
def test_abcd_d1_commonOfD_setter(instance):
    original = instance.commonOfD
    instance.commonOfD = original
    assert instance.commonOfD == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=abcd_D3_B_C_strategy)
@settings(max_examples=50)
def test_abcd_d3_b_c_instantiation(instance):
    assert isinstance(instance, abcd_D3_B_C)

@given(instance=abcd_C2_strategy)
@settings(max_examples=50)
def test_abcd_c2_instantiation(instance):
    assert isinstance(instance, abcd_C2)



@given(instance=abcd_C2_strategy)
def test_abcd_c2_propOfC2_setter(instance):
    original = instance.propOfC2
    instance.propOfC2 = original
    assert instance.propOfC2 == original

@given(instance=abcd_C1_strategy)
@settings(max_examples=50)
def test_abcd_c1_instantiation(instance):
    assert isinstance(instance, abcd_C1)



@given(instance=abcd_C1_strategy)
def test_abcd_c1_propOfC1_setter(instance):
    original = instance.propOfC1
    instance.propOfC1 = original
    assert instance.propOfC1 == original

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=abcd_Other_strategy)
@settings(max_examples=50)
def test_abcd_other_instantiation(instance):
    assert isinstance(instance, abcd_Other)

@given(instance=abcd_A_strategy)
@settings(max_examples=50)
def test_abcd_a_instantiation(instance):
    assert isinstance(instance, abcd_A)



@given(instance=abcd_A_strategy)
def test_abcd_a_aBooleanAttr_setter(instance):
    original = instance.aBooleanAttr
    instance.aBooleanAttr = original
    assert instance.aBooleanAttr == original



@given(instance=abcd_A_strategy)
def test_abcd_a_anIntegerAttr_setter(instance):
    original = instance.anIntegerAttr
    instance.anIntegerAttr = original
    assert instance.anIntegerAttr == original

@given(instance=abcd_Model_strategy)
@settings(max_examples=50)
def test_abcd_model_instantiation(instance):
    assert isinstance(instance, abcd_Model)



@given(instance=abcd_Model_strategy)
def test_abcd_model_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=abcd_NamedElt_strategy)
@settings(max_examples=50)
def test_abcd_namedelt_instantiation(instance):
    assert isinstance(instance, abcd_NamedElt)



@given(instance=abcd_NamedElt_strategy)
def test_abcd_namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=abcd_D_strategy)
@settings(max_examples=50)
def test_abcd_d_instantiation(instance):
    assert isinstance(instance, abcd_D)



@given(instance=abcd_D_strategy)
def test_abcd_d_propOfD_setter(instance):
    original = instance.propOfD
    instance.propOfD = original
    assert instance.propOfD == original

@given(instance=abcd_B_strategy)
@settings(max_examples=50)
def test_abcd_b_instantiation(instance):
    assert isinstance(instance, abcd_B)



@given(instance=abcd_B_strategy)
def test_abcd_b_propOfB_setter(instance):
    original = instance.propOfB
    instance.propOfB = original
    assert instance.propOfB == original

@given(instance=abcd_C_strategy)
@settings(max_examples=50)
def test_abcd_c_instantiation(instance):
    assert isinstance(instance, abcd_C)



@given(instance=abcd_C_strategy)
def test_abcd_c_propOfC_setter(instance):
    original = instance.propOfC
    instance.propOfC = original
    assert instance.propOfC == original
