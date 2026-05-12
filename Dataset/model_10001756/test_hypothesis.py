import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyInterface3_Interface,
    MyClass15,
    MyClass14,
    MyClass13,
    MyClass12,
    MyClass11,
    MyClass10,
    MyClass9,
    MyClass8,
    MyClass7,
    MyInterface2_Interface,
    MyClass6,
    MyInterface_Interface,
    MyClass5,
    MyClass4,
    MyClass3,
    MyClass2,
    MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myinterface3_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface3_Interface)


def test_myinterface3_interface_constructor_exists():
    assert callable(MyInterface3_Interface.__init__)


def test_myinterface3_interface_constructor_args():
    sig = inspect.signature(MyInterface3_Interface.__init__)
    params = list(sig.parameters.keys())



def test_myclass15_is_not_abstract():
    assert not inspect.isabstract(MyClass15)


def test_myclass15_constructor_exists():
    assert callable(MyClass15.__init__)


def test_myclass15_constructor_args():
    sig = inspect.signature(MyClass15.__init__)
    params = list(sig.parameters.keys())



def test_myclass14_is_not_abstract():
    assert not inspect.isabstract(MyClass14)


def test_myclass14_constructor_exists():
    assert callable(MyClass14.__init__)


def test_myclass14_constructor_args():
    sig = inspect.signature(MyClass14.__init__)
    params = list(sig.parameters.keys())



def test_myclass13_is_not_abstract():
    assert not inspect.isabstract(MyClass13)


def test_myclass13_constructor_exists():
    assert callable(MyClass13.__init__)


def test_myclass13_constructor_args():
    sig = inspect.signature(MyClass13.__init__)
    params = list(sig.parameters.keys())



def test_myclass12_is_not_abstract():
    assert not inspect.isabstract(MyClass12)


def test_myclass12_constructor_exists():
    assert callable(MyClass12.__init__)


def test_myclass12_constructor_args():
    sig = inspect.signature(MyClass12.__init__)
    params = list(sig.parameters.keys())



def test_myclass11_is_not_abstract():
    assert not inspect.isabstract(MyClass11)


def test_myclass11_constructor_exists():
    assert callable(MyClass11.__init__)


def test_myclass11_constructor_args():
    sig = inspect.signature(MyClass11.__init__)
    params = list(sig.parameters.keys())



def test_myclass10_is_not_abstract():
    assert not inspect.isabstract(MyClass10)


def test_myclass10_constructor_exists():
    assert callable(MyClass10.__init__)


def test_myclass10_constructor_args():
    sig = inspect.signature(MyClass10.__init__)
    params = list(sig.parameters.keys())



def test_myclass9_is_not_abstract():
    assert not inspect.isabstract(MyClass9)


def test_myclass9_constructor_exists():
    assert callable(MyClass9.__init__)


def test_myclass9_constructor_args():
    sig = inspect.signature(MyClass9.__init__)
    params = list(sig.parameters.keys())



def test_myclass8_is_not_abstract():
    assert not inspect.isabstract(MyClass8)


def test_myclass8_constructor_exists():
    assert callable(MyClass8.__init__)


def test_myclass8_constructor_args():
    sig = inspect.signature(MyClass8.__init__)
    params = list(sig.parameters.keys())



def test_myclass7_is_not_abstract():
    assert not inspect.isabstract(MyClass7)


def test_myclass7_constructor_exists():
    assert callable(MyClass7.__init__)


def test_myclass7_constructor_args():
    sig = inspect.signature(MyClass7.__init__)
    params = list(sig.parameters.keys())



def test_myinterface2_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface2_Interface)


def test_myinterface2_interface_constructor_exists():
    assert callable(MyInterface2_Interface.__init__)


def test_myinterface2_interface_constructor_args():
    sig = inspect.signature(MyInterface2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_myclass6_is_not_abstract():
    assert not inspect.isabstract(MyClass6)


def test_myclass6_constructor_exists():
    assert callable(MyClass6.__init__)


def test_myclass6_constructor_args():
    sig = inspect.signature(MyClass6.__init__)
    params = list(sig.parameters.keys())



def test_myinterface_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface_Interface)


def test_myinterface_interface_constructor_exists():
    assert callable(MyInterface_Interface.__init__)


def test_myinterface_interface_constructor_args():
    sig = inspect.signature(MyInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_myclass5_is_not_abstract():
    assert not inspect.isabstract(MyClass5)


def test_myclass5_constructor_exists():
    assert callable(MyClass5.__init__)


def test_myclass5_constructor_args():
    sig = inspect.signature(MyClass5.__init__)
    params = list(sig.parameters.keys())



def test_myclass4_is_not_abstract():
    assert not inspect.isabstract(MyClass4)


def test_myclass4_constructor_exists():
    assert callable(MyClass4.__init__)


def test_myclass4_constructor_args():
    sig = inspect.signature(MyClass4.__init__)
    params = list(sig.parameters.keys())



def test_myclass3_is_not_abstract():
    assert not inspect.isabstract(MyClass3)


def test_myclass3_constructor_exists():
    assert callable(MyClass3.__init__)


def test_myclass3_constructor_args():
    sig = inspect.signature(MyClass3.__init__)
    params = list(sig.parameters.keys())



def test_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "asdasda__" in params, "Missing parameter 'asdasda__'"

def test_myclass_has_asdasda__():
    assert hasattr(MyClass, "asdasda__")
    descriptor = None
    for klass in MyClass.__mro__:
        if "asdasda__" in klass.__dict__:
            descriptor = klass.__dict__["asdasda__"]
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
MyInterface3_Interface_strategy = st.builds(
    MyInterface3_Interface,
)
MyClass15_strategy = st.builds(
    MyClass15,
)
MyClass14_strategy = st.builds(
    MyClass14,
)
MyClass13_strategy = st.builds(
    MyClass13,
)
MyClass12_strategy = st.builds(
    MyClass12,
)
MyClass11_strategy = st.builds(
    MyClass11,
)
MyClass10_strategy = st.builds(
    MyClass10,
)
MyClass9_strategy = st.builds(
    MyClass9,
)
MyClass8_strategy = st.builds(
    MyClass8,
)
MyClass7_strategy = st.builds(
    MyClass7,
)
MyInterface2_Interface_strategy = st.builds(
    MyInterface2_Interface,
)
MyClass6_strategy = st.builds(
    MyClass6,
)
MyInterface_Interface_strategy = st.builds(
    MyInterface_Interface,
)
MyClass5_strategy = st.builds(
    MyClass5,
)
MyClass4_strategy = st.builds(
    MyClass4,
)
MyClass3_strategy = st.builds(
    MyClass3,
)
MyClass2_strategy = st.builds(
    MyClass2,
)
MyClass_strategy = st.builds(
    MyClass,
    asdasda__=
        safe_text
)

@given(instance=MyInterface3_Interface_strategy)
@settings(max_examples=50)
def test_myinterface3_interface_instantiation(instance):
    assert isinstance(instance, MyInterface3_Interface)

@given(instance=MyClass15_strategy)
@settings(max_examples=50)
def test_myclass15_instantiation(instance):
    assert isinstance(instance, MyClass15)

@given(instance=MyClass14_strategy)
@settings(max_examples=50)
def test_myclass14_instantiation(instance):
    assert isinstance(instance, MyClass14)

@given(instance=MyClass13_strategy)
@settings(max_examples=50)
def test_myclass13_instantiation(instance):
    assert isinstance(instance, MyClass13)

@given(instance=MyClass12_strategy)
@settings(max_examples=50)
def test_myclass12_instantiation(instance):
    assert isinstance(instance, MyClass12)

@given(instance=MyClass11_strategy)
@settings(max_examples=50)
def test_myclass11_instantiation(instance):
    assert isinstance(instance, MyClass11)

@given(instance=MyClass10_strategy)
@settings(max_examples=50)
def test_myclass10_instantiation(instance):
    assert isinstance(instance, MyClass10)

@given(instance=MyClass9_strategy)
@settings(max_examples=50)
def test_myclass9_instantiation(instance):
    assert isinstance(instance, MyClass9)

@given(instance=MyClass8_strategy)
@settings(max_examples=50)
def test_myclass8_instantiation(instance):
    assert isinstance(instance, MyClass8)

@given(instance=MyClass7_strategy)
@settings(max_examples=50)
def test_myclass7_instantiation(instance):
    assert isinstance(instance, MyClass7)

@given(instance=MyInterface2_Interface_strategy)
@settings(max_examples=50)
def test_myinterface2_interface_instantiation(instance):
    assert isinstance(instance, MyInterface2_Interface)

@given(instance=MyClass6_strategy)
@settings(max_examples=50)
def test_myclass6_instantiation(instance):
    assert isinstance(instance, MyClass6)

@given(instance=MyInterface_Interface_strategy)
@settings(max_examples=50)
def test_myinterface_interface_instantiation(instance):
    assert isinstance(instance, MyInterface_Interface)

@given(instance=MyClass5_strategy)
@settings(max_examples=50)
def test_myclass5_instantiation(instance):
    assert isinstance(instance, MyClass5)

@given(instance=MyClass4_strategy)
@settings(max_examples=50)
def test_myclass4_instantiation(instance):
    assert isinstance(instance, MyClass4)

@given(instance=MyClass3_strategy)
@settings(max_examples=50)
def test_myclass3_instantiation(instance):
    assert isinstance(instance, MyClass3)

@given(instance=MyClass2_strategy)
@settings(max_examples=50)
def test_myclass2_instantiation(instance):
    assert isinstance(instance, MyClass2)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)



@given(instance=MyClass_strategy)
def test_myclass_asdasda___setter(instance):
    original = instance.asdasda__
    instance.asdasda__ = original
    assert instance.asdasda__ == original
