import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MyClass4,
    MyClass3,
    MyClass2,
    MyClass,
    UseCase_UseCase,
    Actor_Actor,
    T1,
    ClassB,
    T,
    ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_t1_is_not_abstract():
    assert not inspect.isabstract(T1)


def test_t1_constructor_exists():
    assert callable(T1.__init__)


def test_t1_constructor_args():
    sig = inspect.signature(T1.__init__)
    params = list(sig.parameters.keys())



def test_classb_is_not_abstract():
    assert not inspect.isabstract(ClassB)


def test_classb_constructor_exists():
    assert callable(ClassB.__init__)


def test_classb_constructor_args():
    sig = inspect.signature(ClassB.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_classa_is_not_abstract():
    assert not inspect.isabstract(ClassA)


def test_classa_constructor_exists():
    assert callable(ClassA.__init__)


def test_classa_constructor_args():
    sig = inspect.signature(ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "flag" in params, "Missing parameter 'flag'"

def test_classa_has_flag():
    assert hasattr(ClassA, "flag")
    descriptor = None
    for klass in ClassA.__mro__:
        if "flag" in klass.__dict__:
            descriptor = klass.__dict__["flag"]
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
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
T1_strategy = st.builds(
    T1,
)
ClassB_strategy = st.builds(
    ClassB,
)
T_strategy = st.builds(
    T,
)
ClassA_strategy = st.builds(
    ClassA,
    flag=
        st.booleans()
)

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

@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=50)
def test_usecase_usecase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=T1_strategy)
@settings(max_examples=50)
def test_t1_instantiation(instance):
    assert isinstance(instance, T1)

@given(instance=ClassB_strategy)
@settings(max_examples=50)
def test_classb_instantiation(instance):
    assert isinstance(instance, ClassB)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=ClassA_strategy)
@settings(max_examples=50)
def test_classa_instantiation(instance):
    assert isinstance(instance, ClassA)



@given(instance=ClassA_strategy)
def test_classa_flag_setter(instance):
    original = instance.flag
    instance.flag = original
    assert instance.flag == original
