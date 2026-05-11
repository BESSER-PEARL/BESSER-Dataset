import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SubChild,
    Child4,
    package1::subpackage::SubChild2,
    package1::SubChild,
    RootInterface,
    package1::Child3,
    RootAbstractClass,
    package1::Child2,
    RootClass,
    package1::subpackage::Child5,
    package1::Child4,
    package1::subpackage::Child6,
    package1::SubChild3,
    package1::Child1,
    package1::RootInterface,
    package1::RootAbstractClass,
    package1::RootClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subchild_is_not_abstract():
    assert not inspect.isabstract(SubChild)


def test_subchild_constructor_exists():
    assert callable(SubChild.__init__)


def test_subchild_constructor_args():
    sig = inspect.signature(SubChild.__init__)
    params = list(sig.parameters.keys())



def test_child4_is_not_abstract():
    assert not inspect.isabstract(Child4)


def test_child4_constructor_exists():
    assert callable(Child4.__init__)


def test_child4_constructor_args():
    sig = inspect.signature(Child4.__init__)
    params = list(sig.parameters.keys())



def test_package1::subpackage::subchild2_is_not_abstract():
    assert not inspect.isabstract(package1::subpackage::SubChild2)


def test_package1::subpackage::subchild2_constructor_exists():
    assert callable(package1::subpackage::SubChild2.__init__)


def test_package1::subpackage::subchild2_constructor_args():
    sig = inspect.signature(package1::subpackage::SubChild2.__init__)
    params = list(sig.parameters.keys())



def test_package1::subchild_is_not_abstract():
    assert not inspect.isabstract(package1::SubChild)


def test_package1::subchild_constructor_exists():
    assert callable(package1::SubChild.__init__)


def test_package1::subchild_constructor_args():
    sig = inspect.signature(package1::SubChild.__init__)
    params = list(sig.parameters.keys())



def test_rootinterface_is_not_abstract():
    assert not inspect.isabstract(RootInterface)


def test_rootinterface_constructor_exists():
    assert callable(RootInterface.__init__)


def test_rootinterface_constructor_args():
    sig = inspect.signature(RootInterface.__init__)
    params = list(sig.parameters.keys())



def test_package1::child3_is_not_abstract():
    assert not inspect.isabstract(package1::Child3)


def test_package1::child3_constructor_exists():
    assert callable(package1::Child3.__init__)


def test_package1::child3_constructor_args():
    sig = inspect.signature(package1::Child3.__init__)
    params = list(sig.parameters.keys())



def test_rootabstractclass_is_not_abstract():
    assert not inspect.isabstract(RootAbstractClass)


def test_rootabstractclass_constructor_exists():
    assert callable(RootAbstractClass.__init__)


def test_rootabstractclass_constructor_args():
    sig = inspect.signature(RootAbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_package1::child2_is_not_abstract():
    assert not inspect.isabstract(package1::Child2)


def test_package1::child2_constructor_exists():
    assert callable(package1::Child2.__init__)


def test_package1::child2_constructor_args():
    sig = inspect.signature(package1::Child2.__init__)
    params = list(sig.parameters.keys())



def test_rootclass_is_not_abstract():
    assert not inspect.isabstract(RootClass)


def test_rootclass_constructor_exists():
    assert callable(RootClass.__init__)


def test_rootclass_constructor_args():
    sig = inspect.signature(RootClass.__init__)
    params = list(sig.parameters.keys())



def test_package1::subpackage::child5_is_not_abstract():
    assert not inspect.isabstract(package1::subpackage::Child5)


def test_package1::subpackage::child5_constructor_exists():
    assert callable(package1::subpackage::Child5.__init__)


def test_package1::subpackage::child5_constructor_args():
    sig = inspect.signature(package1::subpackage::Child5.__init__)
    params = list(sig.parameters.keys())



def test_package1::child4_is_not_abstract():
    assert not inspect.isabstract(package1::Child4)


def test_package1::child4_constructor_exists():
    assert callable(package1::Child4.__init__)


def test_package1::child4_constructor_args():
    sig = inspect.signature(package1::Child4.__init__)
    params = list(sig.parameters.keys())



def test_package1::subpackage::child6_is_not_abstract():
    assert not inspect.isabstract(package1::subpackage::Child6)


def test_package1::subpackage::child6_constructor_exists():
    assert callable(package1::subpackage::Child6.__init__)


def test_package1::subpackage::child6_constructor_args():
    sig = inspect.signature(package1::subpackage::Child6.__init__)
    params = list(sig.parameters.keys())



def test_package1::subchild3_is_not_abstract():
    assert not inspect.isabstract(package1::SubChild3)


def test_package1::subchild3_constructor_exists():
    assert callable(package1::SubChild3.__init__)


def test_package1::subchild3_constructor_args():
    sig = inspect.signature(package1::SubChild3.__init__)
    params = list(sig.parameters.keys())



def test_package1::child1_is_not_abstract():
    assert not inspect.isabstract(package1::Child1)


def test_package1::child1_constructor_exists():
    assert callable(package1::Child1.__init__)


def test_package1::child1_constructor_args():
    sig = inspect.signature(package1::Child1.__init__)
    params = list(sig.parameters.keys())



def test_package1::rootinterface_is_not_abstract():
    assert not inspect.isabstract(package1::RootInterface)


def test_package1::rootinterface_constructor_exists():
    assert callable(package1::RootInterface.__init__)


def test_package1::rootinterface_constructor_args():
    sig = inspect.signature(package1::RootInterface.__init__)
    params = list(sig.parameters.keys())



def test_package1::rootabstractclass_is_not_abstract():
    assert not inspect.isabstract(package1::RootAbstractClass)


def test_package1::rootabstractclass_constructor_exists():
    assert callable(package1::RootAbstractClass.__init__)


def test_package1::rootabstractclass_constructor_args():
    sig = inspect.signature(package1::RootAbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_package1::rootclass_is_not_abstract():
    assert not inspect.isabstract(package1::RootClass)


def test_package1::rootclass_constructor_exists():
    assert callable(package1::RootClass.__init__)


def test_package1::rootclass_constructor_args():
    sig = inspect.signature(package1::RootClass.__init__)
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
SubChild_strategy = st.builds(
    SubChild,
)
Child4_strategy = st.builds(
    Child4,
)
package1::subpackage::SubChild2_strategy = st.builds(
    package1::subpackage::SubChild2,
)
package1::SubChild_strategy = st.builds(
    package1::SubChild,
)
RootInterface_strategy = st.builds(
    RootInterface,
)
package1::Child3_strategy = st.builds(
    package1::Child3,
)
RootAbstractClass_strategy = st.builds(
    RootAbstractClass,
)
package1::Child2_strategy = st.builds(
    package1::Child2,
)
RootClass_strategy = st.builds(
    RootClass,
)
package1::subpackage::Child5_strategy = st.builds(
    package1::subpackage::Child5,
)
package1::Child4_strategy = st.builds(
    package1::Child4,
)
package1::subpackage::Child6_strategy = st.builds(
    package1::subpackage::Child6,
)
package1::SubChild3_strategy = st.builds(
    package1::SubChild3,
)
package1::Child1_strategy = st.builds(
    package1::Child1,
)
package1::RootInterface_strategy = st.builds(
    package1::RootInterface,
)
package1::RootAbstractClass_strategy = st.builds(
    package1::RootAbstractClass,
)
package1::RootClass_strategy = st.builds(
    package1::RootClass,
)

@given(instance=SubChild_strategy)
@settings(max_examples=50)
def test_subchild_instantiation(instance):
    assert isinstance(instance, SubChild)

@given(instance=Child4_strategy)
@settings(max_examples=50)
def test_child4_instantiation(instance):
    assert isinstance(instance, Child4)

@given(instance=package1::subpackage::SubChild2_strategy)
@settings(max_examples=50)
def test_package1::subpackage::subchild2_instantiation(instance):
    assert isinstance(instance, package1::subpackage::SubChild2)

@given(instance=package1::SubChild_strategy)
@settings(max_examples=50)
def test_package1::subchild_instantiation(instance):
    assert isinstance(instance, package1::SubChild)

@given(instance=RootInterface_strategy)
@settings(max_examples=50)
def test_rootinterface_instantiation(instance):
    assert isinstance(instance, RootInterface)

@given(instance=package1::Child3_strategy)
@settings(max_examples=50)
def test_package1::child3_instantiation(instance):
    assert isinstance(instance, package1::Child3)

@given(instance=RootAbstractClass_strategy)
@settings(max_examples=50)
def test_rootabstractclass_instantiation(instance):
    assert isinstance(instance, RootAbstractClass)

@given(instance=package1::Child2_strategy)
@settings(max_examples=50)
def test_package1::child2_instantiation(instance):
    assert isinstance(instance, package1::Child2)

@given(instance=RootClass_strategy)
@settings(max_examples=50)
def test_rootclass_instantiation(instance):
    assert isinstance(instance, RootClass)

@given(instance=package1::subpackage::Child5_strategy)
@settings(max_examples=50)
def test_package1::subpackage::child5_instantiation(instance):
    assert isinstance(instance, package1::subpackage::Child5)

@given(instance=package1::Child4_strategy)
@settings(max_examples=50)
def test_package1::child4_instantiation(instance):
    assert isinstance(instance, package1::Child4)

@given(instance=package1::subpackage::Child6_strategy)
@settings(max_examples=50)
def test_package1::subpackage::child6_instantiation(instance):
    assert isinstance(instance, package1::subpackage::Child6)

@given(instance=package1::SubChild3_strategy)
@settings(max_examples=50)
def test_package1::subchild3_instantiation(instance):
    assert isinstance(instance, package1::SubChild3)

@given(instance=package1::Child1_strategy)
@settings(max_examples=50)
def test_package1::child1_instantiation(instance):
    assert isinstance(instance, package1::Child1)

@given(instance=package1::RootInterface_strategy)
@settings(max_examples=50)
def test_package1::rootinterface_instantiation(instance):
    assert isinstance(instance, package1::RootInterface)

@given(instance=package1::RootAbstractClass_strategy)
@settings(max_examples=50)
def test_package1::rootabstractclass_instantiation(instance):
    assert isinstance(instance, package1::RootAbstractClass)

@given(instance=package1::RootClass_strategy)
@settings(max_examples=50)
def test_package1::rootclass_instantiation(instance):
    assert isinstance(instance, package1::RootClass)
