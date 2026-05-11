import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::ClassA,
    test::Interface4,
    test::ClassF,
    ClassC,
    Itf2,
    Interface3,
    test::ClassE,
    test::Interface3,
    test::Itf2,
    test::Itf1,
    ClassB,
    Itf1,
    test::ClassD,
    test::ClassB,
    test::ClassC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::classa_is_not_abstract():
    assert not inspect.isabstract(test::ClassA)


def test_test::classa_constructor_exists():
    assert callable(test::ClassA.__init__)


def test_test::classa_constructor_args():
    sig = inspect.signature(test::ClassA.__init__)
    params = list(sig.parameters.keys())



def test_test::interface4_is_not_abstract():
    assert not inspect.isabstract(test::Interface4)


def test_test::interface4_constructor_exists():
    assert callable(test::Interface4.__init__)


def test_test::interface4_constructor_args():
    sig = inspect.signature(test::Interface4.__init__)
    params = list(sig.parameters.keys())



def test_test::classf_is_not_abstract():
    assert not inspect.isabstract(test::ClassF)


def test_test::classf_constructor_exists():
    assert callable(test::ClassF.__init__)


def test_test::classf_constructor_args():
    sig = inspect.signature(test::ClassF.__init__)
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



def test_test::classe_is_not_abstract():
    assert not inspect.isabstract(test::ClassE)


def test_test::classe_constructor_exists():
    assert callable(test::ClassE.__init__)


def test_test::classe_constructor_args():
    sig = inspect.signature(test::ClassE.__init__)
    params = list(sig.parameters.keys())



def test_test::interface3_is_not_abstract():
    assert not inspect.isabstract(test::Interface3)


def test_test::interface3_constructor_exists():
    assert callable(test::Interface3.__init__)


def test_test::interface3_constructor_args():
    sig = inspect.signature(test::Interface3.__init__)
    params = list(sig.parameters.keys())



def test_test::itf2_is_not_abstract():
    assert not inspect.isabstract(test::Itf2)


def test_test::itf2_constructor_exists():
    assert callable(test::Itf2.__init__)


def test_test::itf2_constructor_args():
    sig = inspect.signature(test::Itf2.__init__)
    params = list(sig.parameters.keys())



def test_test::itf1_is_not_abstract():
    assert not inspect.isabstract(test::Itf1)


def test_test::itf1_constructor_exists():
    assert callable(test::Itf1.__init__)


def test_test::itf1_constructor_args():
    sig = inspect.signature(test::Itf1.__init__)
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



def test_test::classd_is_not_abstract():
    assert not inspect.isabstract(test::ClassD)


def test_test::classd_constructor_exists():
    assert callable(test::ClassD.__init__)


def test_test::classd_constructor_args():
    sig = inspect.signature(test::ClassD.__init__)
    params = list(sig.parameters.keys())



def test_test::classb_is_not_abstract():
    assert not inspect.isabstract(test::ClassB)


def test_test::classb_constructor_exists():
    assert callable(test::ClassB.__init__)


def test_test::classb_constructor_args():
    sig = inspect.signature(test::ClassB.__init__)
    params = list(sig.parameters.keys())



def test_test::classc_is_not_abstract():
    assert not inspect.isabstract(test::ClassC)


def test_test::classc_constructor_exists():
    assert callable(test::ClassC.__init__)


def test_test::classc_constructor_args():
    sig = inspect.signature(test::ClassC.__init__)
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
test::ClassA_strategy = st.builds(
    test::ClassA,
)
test::Interface4_strategy = st.builds(
    test::Interface4,
)
test::ClassF_strategy = st.builds(
    test::ClassF,
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
test::ClassE_strategy = st.builds(
    test::ClassE,
)
test::Interface3_strategy = st.builds(
    test::Interface3,
)
test::Itf2_strategy = st.builds(
    test::Itf2,
)
test::Itf1_strategy = st.builds(
    test::Itf1,
)
ClassB_strategy = st.builds(
    ClassB,
)
Itf1_strategy = st.builds(
    Itf1,
)
test::ClassD_strategy = st.builds(
    test::ClassD,
)
test::ClassB_strategy = st.builds(
    test::ClassB,
)
test::ClassC_strategy = st.builds(
    test::ClassC,
)

@given(instance=test::ClassA_strategy)
@settings(max_examples=50)
def test_test::classa_instantiation(instance):
    assert isinstance(instance, test::ClassA)

@given(instance=test::Interface4_strategy)
@settings(max_examples=50)
def test_test::interface4_instantiation(instance):
    assert isinstance(instance, test::Interface4)

@given(instance=test::ClassF_strategy)
@settings(max_examples=50)
def test_test::classf_instantiation(instance):
    assert isinstance(instance, test::ClassF)

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

@given(instance=test::ClassE_strategy)
@settings(max_examples=50)
def test_test::classe_instantiation(instance):
    assert isinstance(instance, test::ClassE)

@given(instance=test::Interface3_strategy)
@settings(max_examples=50)
def test_test::interface3_instantiation(instance):
    assert isinstance(instance, test::Interface3)

@given(instance=test::Itf2_strategy)
@settings(max_examples=50)
def test_test::itf2_instantiation(instance):
    assert isinstance(instance, test::Itf2)

@given(instance=test::Itf1_strategy)
@settings(max_examples=50)
def test_test::itf1_instantiation(instance):
    assert isinstance(instance, test::Itf1)

@given(instance=ClassB_strategy)
@settings(max_examples=50)
def test_classb_instantiation(instance):
    assert isinstance(instance, ClassB)

@given(instance=Itf1_strategy)
@settings(max_examples=50)
def test_itf1_instantiation(instance):
    assert isinstance(instance, Itf1)

@given(instance=test::ClassD_strategy)
@settings(max_examples=50)
def test_test::classd_instantiation(instance):
    assert isinstance(instance, test::ClassD)

@given(instance=test::ClassB_strategy)
@settings(max_examples=50)
def test_test::classb_instantiation(instance):
    assert isinstance(instance, test::ClassB)

@given(instance=test::ClassC_strategy)
@settings(max_examples=50)
def test_test::classc_instantiation(instance):
    assert isinstance(instance, test::ClassC)
