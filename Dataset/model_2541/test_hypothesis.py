import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_ClassA,
    test_Interface4,
    test_ClassF,
    ClassC,
    Itf2,
    Interface3,
    test_ClassE,
    test_Interface3,
    test_Itf2,
    test_Itf1,
    ClassB,
    Itf1,
    test_ClassD,
    test_ClassB,
    test_ClassC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_classa_is_not_abstract():
    assert not inspect.isabstract(test_ClassA)


def test_test_classa_constructor_exists():
    assert callable(test_ClassA.__init__)


def test_test_classa_constructor_args():
    sig = inspect.signature(test_ClassA.__init__)
    params = list(sig.parameters.keys())



def test_test_interface4_is_not_abstract():
    assert not inspect.isabstract(test_Interface4)


def test_test_interface4_constructor_exists():
    assert callable(test_Interface4.__init__)


def test_test_interface4_constructor_args():
    sig = inspect.signature(test_Interface4.__init__)
    params = list(sig.parameters.keys())



def test_test_classf_is_not_abstract():
    assert not inspect.isabstract(test_ClassF)


def test_test_classf_constructor_exists():
    assert callable(test_ClassF.__init__)


def test_test_classf_constructor_args():
    sig = inspect.signature(test_ClassF.__init__)
    params = list(sig.parameters.keys())



def test_classc_is_not_abstract():
    assert not inspect.isabstract(ClassC)


def test_classc_constructor_exists():
    assert callable(ClassC.__init__)


def test_classc_constructor_args():
    sig = inspect.signature(ClassC.__init__)
    params = list(sig.parameters.keys())



def test_itf2_is_not_abstract():
    assert not inspect.isabstract(Itf2)


def test_itf2_constructor_exists():
    assert callable(Itf2.__init__)


def test_itf2_constructor_args():
    sig = inspect.signature(Itf2.__init__)
    params = list(sig.parameters.keys())



def test_interface3_is_not_abstract():
    assert not inspect.isabstract(Interface3)


def test_interface3_constructor_exists():
    assert callable(Interface3.__init__)


def test_interface3_constructor_args():
    sig = inspect.signature(Interface3.__init__)
    params = list(sig.parameters.keys())



def test_test_classe_is_not_abstract():
    assert not inspect.isabstract(test_ClassE)


def test_test_classe_constructor_exists():
    assert callable(test_ClassE.__init__)


def test_test_classe_constructor_args():
    sig = inspect.signature(test_ClassE.__init__)
    params = list(sig.parameters.keys())



def test_test_interface3_is_not_abstract():
    assert not inspect.isabstract(test_Interface3)


def test_test_interface3_constructor_exists():
    assert callable(test_Interface3.__init__)


def test_test_interface3_constructor_args():
    sig = inspect.signature(test_Interface3.__init__)
    params = list(sig.parameters.keys())



def test_test_itf2_is_not_abstract():
    assert not inspect.isabstract(test_Itf2)


def test_test_itf2_constructor_exists():
    assert callable(test_Itf2.__init__)


def test_test_itf2_constructor_args():
    sig = inspect.signature(test_Itf2.__init__)
    params = list(sig.parameters.keys())



def test_test_itf1_is_not_abstract():
    assert not inspect.isabstract(test_Itf1)


def test_test_itf1_constructor_exists():
    assert callable(test_Itf1.__init__)


def test_test_itf1_constructor_args():
    sig = inspect.signature(test_Itf1.__init__)
    params = list(sig.parameters.keys())



def test_classb_is_not_abstract():
    assert not inspect.isabstract(ClassB)


def test_classb_constructor_exists():
    assert callable(ClassB.__init__)


def test_classb_constructor_args():
    sig = inspect.signature(ClassB.__init__)
    params = list(sig.parameters.keys())



def test_itf1_is_not_abstract():
    assert not inspect.isabstract(Itf1)


def test_itf1_constructor_exists():
    assert callable(Itf1.__init__)


def test_itf1_constructor_args():
    sig = inspect.signature(Itf1.__init__)
    params = list(sig.parameters.keys())



def test_test_classd_is_not_abstract():
    assert not inspect.isabstract(test_ClassD)


def test_test_classd_constructor_exists():
    assert callable(test_ClassD.__init__)


def test_test_classd_constructor_args():
    sig = inspect.signature(test_ClassD.__init__)
    params = list(sig.parameters.keys())



def test_test_classb_is_not_abstract():
    assert not inspect.isabstract(test_ClassB)


def test_test_classb_constructor_exists():
    assert callable(test_ClassB.__init__)


def test_test_classb_constructor_args():
    sig = inspect.signature(test_ClassB.__init__)
    params = list(sig.parameters.keys())



def test_test_classc_is_not_abstract():
    assert not inspect.isabstract(test_ClassC)


def test_test_classc_constructor_exists():
    assert callable(test_ClassC.__init__)


def test_test_classc_constructor_args():
    sig = inspect.signature(test_ClassC.__init__)
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
test_ClassA_strategy = st.builds(
    test_ClassA,
)
test_Interface4_strategy = st.builds(
    test_Interface4,
)
test_ClassF_strategy = st.builds(
    test_ClassF,
)
ClassC_strategy = st.builds(
    ClassC,
)
Itf2_strategy = st.builds(
    Itf2,
)
Interface3_strategy = st.builds(
    Interface3,
)
test_ClassE_strategy = st.builds(
    test_ClassE,
)
test_Interface3_strategy = st.builds(
    test_Interface3,
)
test_Itf2_strategy = st.builds(
    test_Itf2,
)
test_Itf1_strategy = st.builds(
    test_Itf1,
)
ClassB_strategy = st.builds(
    ClassB,
)
Itf1_strategy = st.builds(
    Itf1,
)
test_ClassD_strategy = st.builds(
    test_ClassD,
)
test_ClassB_strategy = st.builds(
    test_ClassB,
)
test_ClassC_strategy = st.builds(
    test_ClassC,
)

@given(instance=test_ClassA_strategy)
@settings(max_examples=50)
def test_test_classa_instantiation(instance):
    assert isinstance(instance, test_ClassA)

@given(instance=test_Interface4_strategy)
@settings(max_examples=50)
def test_test_interface4_instantiation(instance):
    assert isinstance(instance, test_Interface4)

@given(instance=test_ClassF_strategy)
@settings(max_examples=50)
def test_test_classf_instantiation(instance):
    assert isinstance(instance, test_ClassF)

@given(instance=ClassC_strategy)
@settings(max_examples=50)
def test_classc_instantiation(instance):
    assert isinstance(instance, ClassC)

@given(instance=Itf2_strategy)
@settings(max_examples=50)
def test_itf2_instantiation(instance):
    assert isinstance(instance, Itf2)

@given(instance=Interface3_strategy)
@settings(max_examples=50)
def test_interface3_instantiation(instance):
    assert isinstance(instance, Interface3)

@given(instance=test_ClassE_strategy)
@settings(max_examples=50)
def test_test_classe_instantiation(instance):
    assert isinstance(instance, test_ClassE)

@given(instance=test_Interface3_strategy)
@settings(max_examples=50)
def test_test_interface3_instantiation(instance):
    assert isinstance(instance, test_Interface3)

@given(instance=test_Itf2_strategy)
@settings(max_examples=50)
def test_test_itf2_instantiation(instance):
    assert isinstance(instance, test_Itf2)

@given(instance=test_Itf1_strategy)
@settings(max_examples=50)
def test_test_itf1_instantiation(instance):
    assert isinstance(instance, test_Itf1)

@given(instance=ClassB_strategy)
@settings(max_examples=50)
def test_classb_instantiation(instance):
    assert isinstance(instance, ClassB)

@given(instance=Itf1_strategy)
@settings(max_examples=50)
def test_itf1_instantiation(instance):
    assert isinstance(instance, Itf1)

@given(instance=test_ClassD_strategy)
@settings(max_examples=50)
def test_test_classd_instantiation(instance):
    assert isinstance(instance, test_ClassD)

@given(instance=test_ClassB_strategy)
@settings(max_examples=50)
def test_test_classb_instantiation(instance):
    assert isinstance(instance, test_ClassB)

@given(instance=test_ClassC_strategy)
@settings(max_examples=50)
def test_test_classc_instantiation(instance):
    assert isinstance(instance, test_ClassC)
