import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Trapezoidal,
    Triangular,
    Linear,
    Left_Shoulder,
    Membership_Function,
    Right_Shoulder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trapezoidal_is_not_abstract():
    assert not inspect.isabstract(Trapezoidal)


def test_trapezoidal_constructor_exists():
    assert callable(Trapezoidal.__init__)


def test_trapezoidal_constructor_args():
    sig = inspect.signature(Trapezoidal.__init__)
    params = list(sig.parameters.keys())
    assert "E" in params, "Missing parameter 'E'"
    assert "D" in params, "Missing parameter 'D'"

def test_trapezoidal_has_E():
    assert hasattr(Trapezoidal, "E")
    descriptor = None
    for klass in Trapezoidal.__mro__:
        if "E" in klass.__dict__:
            descriptor = klass.__dict__["E"]
            break
    assert isinstance(descriptor, property)

def test_trapezoidal_has_D():
    assert hasattr(Trapezoidal, "D")
    descriptor = None
    for klass in Trapezoidal.__mro__:
        if "D" in klass.__dict__:
            descriptor = klass.__dict__["D"]
            break
    assert isinstance(descriptor, property)



def test_triangular_is_not_abstract():
    assert not inspect.isabstract(Triangular)


def test_triangular_constructor_exists():
    assert callable(Triangular.__init__)


def test_triangular_constructor_args():
    sig = inspect.signature(Triangular.__init__)
    params = list(sig.parameters.keys())
    assert "C" in params, "Missing parameter 'C'"

def test_triangular_has_C():
    assert hasattr(Triangular, "C")
    descriptor = None
    for klass in Triangular.__mro__:
        if "C" in klass.__dict__:
            descriptor = klass.__dict__["C"]
            break
    assert isinstance(descriptor, property)



def test_linear_is_not_abstract():
    assert not inspect.isabstract(Linear)


def test_linear_constructor_exists():
    assert callable(Linear.__init__)


def test_linear_constructor_args():
    sig = inspect.signature(Linear.__init__)
    params = list(sig.parameters.keys())



def test_left_shoulder_is_not_abstract():
    assert not inspect.isabstract(Left_Shoulder)


def test_left_shoulder_constructor_exists():
    assert callable(Left_Shoulder.__init__)


def test_left_shoulder_constructor_args():
    sig = inspect.signature(Left_Shoulder.__init__)
    params = list(sig.parameters.keys())



def test_membership_function_is_not_abstract():
    assert not inspect.isabstract(Membership_Function)


def test_membership_function_constructor_exists():
    assert callable(Membership_Function.__init__)


def test_membership_function_constructor_args():
    sig = inspect.signature(Membership_Function.__init__)
    params = list(sig.parameters.keys())
    assert "A" in params, "Missing parameter 'A'"
    assert "HasUID" in params, "Missing parameter 'HasUID'"
    assert "B" in params, "Missing parameter 'B'"
    assert "HasName" in params, "Missing parameter 'HasName'"

def test_membership_function_has_A():
    assert hasattr(Membership_Function, "A")
    descriptor = None
    for klass in Membership_Function.__mro__:
        if "A" in klass.__dict__:
            descriptor = klass.__dict__["A"]
            break
    assert isinstance(descriptor, property)

def test_membership_function_has_HasUID():
    assert hasattr(Membership_Function, "HasUID")
    descriptor = None
    for klass in Membership_Function.__mro__:
        if "HasUID" in klass.__dict__:
            descriptor = klass.__dict__["HasUID"]
            break
    assert isinstance(descriptor, property)

def test_membership_function_has_B():
    assert hasattr(Membership_Function, "B")
    descriptor = None
    for klass in Membership_Function.__mro__:
        if "B" in klass.__dict__:
            descriptor = klass.__dict__["B"]
            break
    assert isinstance(descriptor, property)

def test_membership_function_has_HasName():
    assert hasattr(Membership_Function, "HasName")
    descriptor = None
    for klass in Membership_Function.__mro__:
        if "HasName" in klass.__dict__:
            descriptor = klass.__dict__["HasName"]
            break
    assert isinstance(descriptor, property)



def test_right_shoulder_is_not_abstract():
    assert not inspect.isabstract(Right_Shoulder)


def test_right_shoulder_constructor_exists():
    assert callable(Right_Shoulder.__init__)


def test_right_shoulder_constructor_args():
    sig = inspect.signature(Right_Shoulder.__init__)
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
Trapezoidal_strategy = st.builds(
    Trapezoidal,
    E=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    D=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Triangular_strategy = st.builds(
    Triangular,
    C=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Linear_strategy = st.builds(
    Linear,
)
Left_Shoulder_strategy = st.builds(
    Left_Shoulder,
)
Membership_Function_strategy = st.builds(
    Membership_Function,
    A=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    HasUID=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    B=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    HasName=
        safe_text
)
Right_Shoulder_strategy = st.builds(
    Right_Shoulder,
)

@given(instance=Trapezoidal_strategy)
@settings(max_examples=50)
def test_trapezoidal_instantiation(instance):
    assert isinstance(instance, Trapezoidal)



@given(instance=Trapezoidal_strategy)
def test_trapezoidal_E_setter(instance):
    original = instance.E
    instance.E = original
    assert instance.E == original



@given(instance=Trapezoidal_strategy)
def test_trapezoidal_D_setter(instance):
    original = instance.D
    instance.D = original
    assert instance.D == original

@given(instance=Triangular_strategy)
@settings(max_examples=50)
def test_triangular_instantiation(instance):
    assert isinstance(instance, Triangular)



@given(instance=Triangular_strategy)
def test_triangular_C_setter(instance):
    original = instance.C
    instance.C = original
    assert instance.C == original

@given(instance=Linear_strategy)
@settings(max_examples=50)
def test_linear_instantiation(instance):
    assert isinstance(instance, Linear)

@given(instance=Left_Shoulder_strategy)
@settings(max_examples=50)
def test_left_shoulder_instantiation(instance):
    assert isinstance(instance, Left_Shoulder)

@given(instance=Membership_Function_strategy)
@settings(max_examples=50)
def test_membership_function_instantiation(instance):
    assert isinstance(instance, Membership_Function)



@given(instance=Membership_Function_strategy)
def test_membership_function_A_setter(instance):
    original = instance.A
    instance.A = original
    assert instance.A == original



@given(instance=Membership_Function_strategy)
def test_membership_function_HasUID_setter(instance):
    original = instance.HasUID
    instance.HasUID = original
    assert instance.HasUID == original



@given(instance=Membership_Function_strategy)
def test_membership_function_B_setter(instance):
    original = instance.B
    instance.B = original
    assert instance.B == original



@given(instance=Membership_Function_strategy)
def test_membership_function_HasName_setter(instance):
    original = instance.HasName
    instance.HasName = original
    assert instance.HasName == original

@given(instance=Right_Shoulder_strategy)
@settings(max_examples=50)
def test_right_shoulder_instantiation(instance):
    assert isinstance(instance, Right_Shoulder)
