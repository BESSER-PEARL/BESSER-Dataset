import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyClass37,
    MyClass36,
    MyClass35,
    MyClass34,
    MyClass33,
    MyClass32,
    MyClass6,
    MyClass5,
    MyClass4,
    MyClass3,
    MyClass2,
    sfbsdf,
    MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myclass37_is_not_abstract():
    assert not inspect.isabstract(MyClass37)


def test_myclass37_constructor_exists():
    assert callable(MyClass37.__init__)


def test_myclass37_constructor_args():
    sig = inspect.signature(MyClass37.__init__)
    params = list(sig.parameters.keys())



def test_myclass36_is_not_abstract():
    assert not inspect.isabstract(MyClass36)


def test_myclass36_constructor_exists():
    assert callable(MyClass36.__init__)


def test_myclass36_constructor_args():
    sig = inspect.signature(MyClass36.__init__)
    params = list(sig.parameters.keys())



def test_myclass35_is_not_abstract():
    assert not inspect.isabstract(MyClass35)


def test_myclass35_constructor_exists():
    assert callable(MyClass35.__init__)


def test_myclass35_constructor_args():
    sig = inspect.signature(MyClass35.__init__)
    params = list(sig.parameters.keys())



def test_myclass34_is_not_abstract():
    assert not inspect.isabstract(MyClass34)


def test_myclass34_constructor_exists():
    assert callable(MyClass34.__init__)


def test_myclass34_constructor_args():
    sig = inspect.signature(MyClass34.__init__)
    params = list(sig.parameters.keys())



def test_myclass33_is_not_abstract():
    assert not inspect.isabstract(MyClass33)


def test_myclass33_constructor_exists():
    assert callable(MyClass33.__init__)


def test_myclass33_constructor_args():
    sig = inspect.signature(MyClass33.__init__)
    params = list(sig.parameters.keys())



def test_myclass32_is_not_abstract():
    assert not inspect.isabstract(MyClass32)


def test_myclass32_constructor_exists():
    assert callable(MyClass32.__init__)


def test_myclass32_constructor_args():
    sig = inspect.signature(MyClass32.__init__)
    params = list(sig.parameters.keys())



def test_myclass6_is_not_abstract():
    assert not inspect.isabstract(MyClass6)


def test_myclass6_constructor_exists():
    assert callable(MyClass6.__init__)


def test_myclass6_constructor_args():
    sig = inspect.signature(MyClass6.__init__)
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



def test_sfbsdf_is_not_abstract():
    assert not inspect.isabstract(sfbsdf)


def test_sfbsdf_constructor_exists():
    assert callable(sfbsdf.__init__)


def test_sfbsdf_constructor_args():
    sig = inspect.signature(sfbsdf.__init__)
    params = list(sig.parameters.keys())



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "TenCoSo" in params, "Missing parameter 'TenCoSo'"

def test_myclass_has_attribute():
    assert hasattr(MyClass, "attribute")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_attribute2():
    assert hasattr(MyClass, "attribute2")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_attribute3():
    assert hasattr(MyClass, "attribute3")
    descriptor = None
    for klass in MyClass.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_myclass_has_TenCoSo():
    assert hasattr(MyClass, "TenCoSo")
    descriptor = None
    for klass in MyClass.__mro__:
        if "TenCoSo" in klass.__dict__:
            descriptor = klass.__dict__["TenCoSo"]
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
MyClass37_strategy = st.builds(
    MyClass37,
)
MyClass36_strategy = st.builds(
    MyClass36,
)
MyClass35_strategy = st.builds(
    MyClass35,
)
MyClass34_strategy = st.builds(
    MyClass34,
)
MyClass33_strategy = st.builds(
    MyClass33,
)
MyClass32_strategy = st.builds(
    MyClass32,
)
MyClass6_strategy = st.builds(
    MyClass6,
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
sfbsdf_strategy = st.builds(
    sfbsdf,
)
MyClass_strategy = st.builds(
    MyClass,
    attribute=
        safe_text,
    attribute2=
        safe_text,
    attribute3=
        safe_text,
    TenCoSo=
        safe_text
)

@given(instance=MyClass37_strategy)
@settings(max_examples=50)
def test_myclass37_instantiation(instance):
    assert isinstance(instance, MyClass37)

@given(instance=MyClass36_strategy)
@settings(max_examples=50)
def test_myclass36_instantiation(instance):
    assert isinstance(instance, MyClass36)

@given(instance=MyClass35_strategy)
@settings(max_examples=50)
def test_myclass35_instantiation(instance):
    assert isinstance(instance, MyClass35)

@given(instance=MyClass34_strategy)
@settings(max_examples=50)
def test_myclass34_instantiation(instance):
    assert isinstance(instance, MyClass34)

@given(instance=MyClass33_strategy)
@settings(max_examples=50)
def test_myclass33_instantiation(instance):
    assert isinstance(instance, MyClass33)

@given(instance=MyClass32_strategy)
@settings(max_examples=50)
def test_myclass32_instantiation(instance):
    assert isinstance(instance, MyClass32)

@given(instance=MyClass6_strategy)
@settings(max_examples=50)
def test_myclass6_instantiation(instance):
    assert isinstance(instance, MyClass6)

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

@given(instance=sfbsdf_strategy)
@settings(max_examples=50)
def test_sfbsdf_instantiation(instance):
    assert isinstance(instance, sfbsdf)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)



@given(instance=MyClass_strategy)
def test_myclass_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=MyClass_strategy)
def test_myclass_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=MyClass_strategy)
def test_myclass_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=MyClass_strategy)
def test_myclass_TenCoSo_setter(instance):
    original = instance.TenCoSo
    instance.TenCoSo = original
    assert instance.TenCoSo == original
