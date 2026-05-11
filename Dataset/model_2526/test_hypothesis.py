import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    D3::B,
    B,
    D3,
    abcd::D3::B,
    D,
    abcd::D2,
    abcd::D3,
    abcd::D1,
    C,
    abcd::D3::B::C,
    abcd::C2,
    abcd::C1,
    NamedElt,
    abcd::Other,
    abcd::A,
    abcd::Model,
    abcd::NamedElt,
    A,
    abcd::D,
    abcd::B,
    abcd::C,
    StyleKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d3::b_is_not_abstract():
    assert not inspect.isabstract(D3::B)


def test_d3::b_constructor_exists():
    assert callable(D3::B.__init__)


def test_d3::b_constructor_args():
    sig = inspect.signature(D3::B.__init__)
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



def test_abcd::d3::b_is_not_abstract():
    assert not inspect.isabstract(abcd::D3::B)


def test_abcd::d3::b_constructor_exists():
    assert callable(abcd::D3::B.__init__)


def test_abcd::d3::b_constructor_args():
    sig = inspect.signature(abcd::D3::B.__init__)
    params = list(sig.parameters.keys())



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_abcd::d2_is_not_abstract():
    assert not inspect.isabstract(abcd::D2)


def test_abcd::d2_constructor_exists():
    assert callable(abcd::D2.__init__)


def test_abcd::d2_constructor_args():
    sig = inspect.signature(abcd::D2.__init__)
    params = list(sig.parameters.keys())
    assert "commonOfD" in params, "Missing parameter 'commonOfD'"

def test_abcd::d2_has_commonOfD():
    assert hasattr(abcd::D2, "commonOfD")
    descriptor = None
    for klass in abcd::D2.__mro__:
        if "commonOfD" in klass.__dict__:
            descriptor = klass.__dict__["commonOfD"]
            break
    assert isinstance(descriptor, property)



def test_abcd::d3_is_not_abstract():
    assert not inspect.isabstract(abcd::D3)


def test_abcd::d3_constructor_exists():
    assert callable(abcd::D3.__init__)


def test_abcd::d3_constructor_args():
    sig = inspect.signature(abcd::D3.__init__)
    params = list(sig.parameters.keys())
    assert "commonOfD" in params, "Missing parameter 'commonOfD'"

def test_abcd::d3_has_commonOfD():
    assert hasattr(abcd::D3, "commonOfD")
    descriptor = None
    for klass in abcd::D3.__mro__:
        if "commonOfD" in klass.__dict__:
            descriptor = klass.__dict__["commonOfD"]
            break
    assert isinstance(descriptor, property)



def test_abcd::d1_is_not_abstract():
    assert not inspect.isabstract(abcd::D1)


def test_abcd::d1_constructor_exists():
    assert callable(abcd::D1.__init__)


def test_abcd::d1_constructor_args():
    sig = inspect.signature(abcd::D1.__init__)
    params = list(sig.parameters.keys())
    assert "commonOfD" in params, "Missing parameter 'commonOfD'"

def test_abcd::d1_has_commonOfD():
    assert hasattr(abcd::D1, "commonOfD")
    descriptor = None
    for klass in abcd::D1.__mro__:
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



def test_abcd::d3::b::c_is_not_abstract():
    assert not inspect.isabstract(abcd::D3::B::C)


def test_abcd::d3::b::c_constructor_exists():
    assert callable(abcd::D3::B::C.__init__)


def test_abcd::d3::b::c_constructor_args():
    sig = inspect.signature(abcd::D3::B::C.__init__)
    params = list(sig.parameters.keys())



def test_abcd::c2_is_not_abstract():
    assert not inspect.isabstract(abcd::C2)


def test_abcd::c2_constructor_exists():
    assert callable(abcd::C2.__init__)


def test_abcd::c2_constructor_args():
    sig = inspect.signature(abcd::C2.__init__)
    params = list(sig.parameters.keys())
    assert "propOfC2" in params, "Missing parameter 'propOfC2'"

def test_abcd::c2_has_propOfC2():
    assert hasattr(abcd::C2, "propOfC2")
    descriptor = None
    for klass in abcd::C2.__mro__:
        if "propOfC2" in klass.__dict__:
            descriptor = klass.__dict__["propOfC2"]
            break
    assert isinstance(descriptor, property)



def test_abcd::c1_is_not_abstract():
    assert not inspect.isabstract(abcd::C1)


def test_abcd::c1_constructor_exists():
    assert callable(abcd::C1.__init__)


def test_abcd::c1_constructor_args():
    sig = inspect.signature(abcd::C1.__init__)
    params = list(sig.parameters.keys())
    assert "propOfC1" in params, "Missing parameter 'propOfC1'"

def test_abcd::c1_has_propOfC1():
    assert hasattr(abcd::C1, "propOfC1")
    descriptor = None
    for klass in abcd::C1.__mro__:
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



def test_abcd::other_is_not_abstract():
    assert not inspect.isabstract(abcd::Other)


def test_abcd::other_constructor_exists():
    assert callable(abcd::Other.__init__)


def test_abcd::other_constructor_args():
    sig = inspect.signature(abcd::Other.__init__)
    params = list(sig.parameters.keys())



def test_abcd::a_is_not_abstract():
    assert not inspect.isabstract(abcd::A)


def test_abcd::a_constructor_exists():
    assert callable(abcd::A.__init__)


def test_abcd::a_constructor_args():
    sig = inspect.signature(abcd::A.__init__)
    params = list(sig.parameters.keys())
    assert "anIntegerAttr" in params, "Missing parameter 'anIntegerAttr'"
    assert "aBooleanAttr" in params, "Missing parameter 'aBooleanAttr'"

def test_abcd::a_has_anIntegerAttr():
    assert hasattr(abcd::A, "anIntegerAttr")
    descriptor = None
    for klass in abcd::A.__mro__:
        if "anIntegerAttr" in klass.__dict__:
            descriptor = klass.__dict__["anIntegerAttr"]
            break
    assert isinstance(descriptor, property)

def test_abcd::a_has_aBooleanAttr():
    assert hasattr(abcd::A, "aBooleanAttr")
    descriptor = None
    for klass in abcd::A.__mro__:
        if "aBooleanAttr" in klass.__dict__:
            descriptor = klass.__dict__["aBooleanAttr"]
            break
    assert isinstance(descriptor, property)



def test_abcd::model_is_not_abstract():
    assert not inspect.isabstract(abcd::Model)


def test_abcd::model_constructor_exists():
    assert callable(abcd::Model.__init__)


def test_abcd::model_constructor_args():
    sig = inspect.signature(abcd::Model.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"

def test_abcd::model_has_style():
    assert hasattr(abcd::Model, "style")
    descriptor = None
    for klass in abcd::Model.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_abcd::namedelt_is_not_abstract():
    assert not inspect.isabstract(abcd::NamedElt)


def test_abcd::namedelt_constructor_exists():
    assert callable(abcd::NamedElt.__init__)


def test_abcd::namedelt_constructor_args():
    sig = inspect.signature(abcd::NamedElt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abcd::namedelt_has_name():
    assert hasattr(abcd::NamedElt, "name")
    descriptor = None
    for klass in abcd::NamedElt.__mro__:
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



def test_abcd::d_is_not_abstract():
    assert not inspect.isabstract(abcd::D)


def test_abcd::d_constructor_exists():
    assert callable(abcd::D.__init__)


def test_abcd::d_constructor_args():
    sig = inspect.signature(abcd::D.__init__)
    params = list(sig.parameters.keys())
    assert "propOfD" in params, "Missing parameter 'propOfD'"

def test_abcd::d_has_propOfD():
    assert hasattr(abcd::D, "propOfD")
    descriptor = None
    for klass in abcd::D.__mro__:
        if "propOfD" in klass.__dict__:
            descriptor = klass.__dict__["propOfD"]
            break
    assert isinstance(descriptor, property)



def test_abcd::b_is_not_abstract():
    assert not inspect.isabstract(abcd::B)


def test_abcd::b_constructor_exists():
    assert callable(abcd::B.__init__)


def test_abcd::b_constructor_args():
    sig = inspect.signature(abcd::B.__init__)
    params = list(sig.parameters.keys())
    assert "propOfB" in params, "Missing parameter 'propOfB'"

def test_abcd::b_has_propOfB():
    assert hasattr(abcd::B, "propOfB")
    descriptor = None
    for klass in abcd::B.__mro__:
        if "propOfB" in klass.__dict__:
            descriptor = klass.__dict__["propOfB"]
            break
    assert isinstance(descriptor, property)



def test_abcd::c_is_not_abstract():
    assert not inspect.isabstract(abcd::C)


def test_abcd::c_constructor_exists():
    assert callable(abcd::C.__init__)


def test_abcd::c_constructor_args():
    sig = inspect.signature(abcd::C.__init__)
    params = list(sig.parameters.keys())
    assert "propOfC" in params, "Missing parameter 'propOfC'"

def test_abcd::c_has_propOfC():
    assert hasattr(abcd::C, "propOfC")
    descriptor = None
    for klass in abcd::C.__mro__:
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
D3::B_strategy = st.builds(
    D3::B,
)
B_strategy = st.builds(
    B,
)
D3_strategy = st.builds(
    D3,
)
abcd::D3::B_strategy = st.builds(
    abcd::D3::B,
)
D_strategy = st.builds(
    D,
)
abcd::D2_strategy = st.builds(
    abcd::D2,
    commonOfD=
        safe_text
)
abcd::D3_strategy = st.builds(
    abcd::D3,
    commonOfD=
        safe_text
)
abcd::D1_strategy = st.builds(
    abcd::D1,
    commonOfD=
        safe_text
)
C_strategy = st.builds(
    C,
)
abcd::D3::B::C_strategy = st.builds(
    abcd::D3::B::C,
)
abcd::C2_strategy = st.builds(
    abcd::C2,
    propOfC2=
        safe_text
)
abcd::C1_strategy = st.builds(
    abcd::C1,
    propOfC1=
        safe_text
)
NamedElt_strategy = st.builds(
    NamedElt,
)
abcd::Other_strategy = st.builds(
    abcd::Other,
)
abcd::A_strategy = st.builds(
    abcd::A,
    anIntegerAttr=
        st.integers(),
    aBooleanAttr=
        safe_text
)
abcd::Model_strategy = st.builds(
    abcd::Model,
    style=
        safe_text
)
abcd::NamedElt_strategy = st.builds(
    abcd::NamedElt,
    name=
        safe_text
)
A_strategy = st.builds(
    A,
)
abcd::D_strategy = st.builds(
    abcd::D,
    propOfD=
        safe_text
)
abcd::B_strategy = st.builds(
    abcd::B,
    propOfB=
        safe_text
)
abcd::C_strategy = st.builds(
    abcd::C,
    propOfC=
        safe_text
)

@given(instance=D3::B_strategy)
@settings(max_examples=50)
def test_d3::b_instantiation(instance):
    assert isinstance(instance, D3::B)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=D3_strategy)
@settings(max_examples=50)
def test_d3_instantiation(instance):
    assert isinstance(instance, D3)

@given(instance=abcd::D3::B_strategy)
@settings(max_examples=50)
def test_abcd::d3::b_instantiation(instance):
    assert isinstance(instance, abcd::D3::B)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=abcd::D2_strategy)
@settings(max_examples=50)
def test_abcd::d2_instantiation(instance):
    assert isinstance(instance, abcd::D2)

@given(instance=abcd::D2_strategy)
def test_abcd::d2_commonOfD_type(instance):
    assert isinstance(instance.commonOfD, str)


@given(instance=abcd::D2_strategy)
def test_abcd::d2_commonOfD_setter(instance):
    original = instance.commonOfD
    instance.commonOfD = original
    assert instance.commonOfD == original

@given(instance=abcd::D3_strategy)
@settings(max_examples=50)
def test_abcd::d3_instantiation(instance):
    assert isinstance(instance, abcd::D3)

@given(instance=abcd::D3_strategy)
def test_abcd::d3_commonOfD_type(instance):
    assert isinstance(instance.commonOfD, str)


@given(instance=abcd::D3_strategy)
def test_abcd::d3_commonOfD_setter(instance):
    original = instance.commonOfD
    instance.commonOfD = original
    assert instance.commonOfD == original

@given(instance=abcd::D1_strategy)
@settings(max_examples=50)
def test_abcd::d1_instantiation(instance):
    assert isinstance(instance, abcd::D1)

@given(instance=abcd::D1_strategy)
def test_abcd::d1_commonOfD_type(instance):
    assert isinstance(instance.commonOfD, str)


@given(instance=abcd::D1_strategy)
def test_abcd::d1_commonOfD_setter(instance):
    original = instance.commonOfD
    instance.commonOfD = original
    assert instance.commonOfD == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=abcd::D3::B::C_strategy)
@settings(max_examples=50)
def test_abcd::d3::b::c_instantiation(instance):
    assert isinstance(instance, abcd::D3::B::C)

@given(instance=abcd::C2_strategy)
@settings(max_examples=50)
def test_abcd::c2_instantiation(instance):
    assert isinstance(instance, abcd::C2)

@given(instance=abcd::C2_strategy)
def test_abcd::c2_propOfC2_type(instance):
    assert isinstance(instance.propOfC2, str)


@given(instance=abcd::C2_strategy)
def test_abcd::c2_propOfC2_setter(instance):
    original = instance.propOfC2
    instance.propOfC2 = original
    assert instance.propOfC2 == original

@given(instance=abcd::C1_strategy)
@settings(max_examples=50)
def test_abcd::c1_instantiation(instance):
    assert isinstance(instance, abcd::C1)

@given(instance=abcd::C1_strategy)
def test_abcd::c1_propOfC1_type(instance):
    assert isinstance(instance.propOfC1, str)


@given(instance=abcd::C1_strategy)
def test_abcd::c1_propOfC1_setter(instance):
    original = instance.propOfC1
    instance.propOfC1 = original
    assert instance.propOfC1 == original

@given(instance=NamedElt_strategy)
@settings(max_examples=50)
def test_namedelt_instantiation(instance):
    assert isinstance(instance, NamedElt)

@given(instance=abcd::Other_strategy)
@settings(max_examples=50)
def test_abcd::other_instantiation(instance):
    assert isinstance(instance, abcd::Other)

@given(instance=abcd::A_strategy)
@settings(max_examples=50)
def test_abcd::a_instantiation(instance):
    assert isinstance(instance, abcd::A)

@given(instance=abcd::A_strategy)
def test_abcd::a_anIntegerAttr_type(instance):
    assert isinstance(instance.anIntegerAttr, int)


@given(instance=abcd::A_strategy)
def test_abcd::a_anIntegerAttr_setter(instance):
    original = instance.anIntegerAttr
    instance.anIntegerAttr = original
    assert instance.anIntegerAttr == original

@given(instance=abcd::A_strategy)
def test_abcd::a_aBooleanAttr_type(instance):
    assert isinstance(instance.aBooleanAttr, str)


@given(instance=abcd::A_strategy)
def test_abcd::a_aBooleanAttr_setter(instance):
    original = instance.aBooleanAttr
    instance.aBooleanAttr = original
    assert instance.aBooleanAttr == original

@given(instance=abcd::Model_strategy)
@settings(max_examples=50)
def test_abcd::model_instantiation(instance):
    assert isinstance(instance, abcd::Model)

@given(instance=abcd::Model_strategy)
def test_abcd::model_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=abcd::Model_strategy)
def test_abcd::model_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=abcd::NamedElt_strategy)
@settings(max_examples=50)
def test_abcd::namedelt_instantiation(instance):
    assert isinstance(instance, abcd::NamedElt)

@given(instance=abcd::NamedElt_strategy)
def test_abcd::namedelt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abcd::NamedElt_strategy)
def test_abcd::namedelt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=abcd::D_strategy)
@settings(max_examples=50)
def test_abcd::d_instantiation(instance):
    assert isinstance(instance, abcd::D)

@given(instance=abcd::D_strategy)
def test_abcd::d_propOfD_type(instance):
    assert isinstance(instance.propOfD, str)


@given(instance=abcd::D_strategy)
def test_abcd::d_propOfD_setter(instance):
    original = instance.propOfD
    instance.propOfD = original
    assert instance.propOfD == original

@given(instance=abcd::B_strategy)
@settings(max_examples=50)
def test_abcd::b_instantiation(instance):
    assert isinstance(instance, abcd::B)

@given(instance=abcd::B_strategy)
def test_abcd::b_propOfB_type(instance):
    assert isinstance(instance.propOfB, str)


@given(instance=abcd::B_strategy)
def test_abcd::b_propOfB_setter(instance):
    original = instance.propOfB
    instance.propOfB = original
    assert instance.propOfB == original

@given(instance=abcd::C_strategy)
@settings(max_examples=50)
def test_abcd::c_instantiation(instance):
    assert isinstance(instance, abcd::C)

@given(instance=abcd::C_strategy)
def test_abcd::c_propOfC_type(instance):
    assert isinstance(instance.propOfC, str)


@given(instance=abcd::C_strategy)
def test_abcd::c_propOfC_setter(instance):
    original = instance.propOfC
    instance.propOfC = original
    assert instance.propOfC == original
