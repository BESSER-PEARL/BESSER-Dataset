import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pltest::TestPackageableElement,
    pltest::Numbers,
    GrandChildD,
    pltest::WhatEver,
    pltest::Circle,
    pltest::Red,
    TestClassifier,
    pltest::TestInterface,
    pltest::TestClass,
    TestPackageableElement,
    pltest::TestClassifier,
    pltest::TestPackage,
    pltest::Interface,
    Base,
    pltest::Common,
    pltest::Base,
    Child2,
    pltest::GrandGrandChildF,
    pltest::GrandChild2,
    pltest::Child3,
    Child1,
    pltest::GrandGrandChildE,
    Child3,
    pltest::GrandChildD,
    pltest::GrandChild,
    Interface,
    Common,
    pltest::Child2,
    pltest::Child1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pltest::testpackageableelement_is_not_abstract():
    assert not inspect.isabstract(pltest::TestPackageableElement)


def test_pltest::testpackageableelement_constructor_exists():
    assert callable(pltest::TestPackageableElement.__init__)


def test_pltest::testpackageableelement_constructor_args():
    sig = inspect.signature(pltest::TestPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_pltest::numbers_is_not_abstract():
    assert not inspect.isabstract(pltest::Numbers)


def test_pltest::numbers_constructor_exists():
    assert callable(pltest::Numbers.__init__)


def test_pltest::numbers_constructor_args():
    sig = inspect.signature(pltest::Numbers.__init__)
    params = list(sig.parameters.keys())
    assert "bigInt" in params, "Missing parameter 'bigInt'"
    assert "double" in params, "Missing parameter 'double'"
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"
    assert "int" in params, "Missing parameter 'int'"
    assert "long" in params, "Missing parameter 'long'"
    assert "float" in params, "Missing parameter 'float'"

def test_pltest::numbers_has_bigInt():
    assert hasattr(pltest::Numbers, "bigInt")
    descriptor = None
    for klass in pltest::Numbers.__mro__:
        if "bigInt" in klass.__dict__:
            descriptor = klass.__dict__["bigInt"]
            break
    assert isinstance(descriptor, property)

def test_pltest::numbers_has_double():
    assert hasattr(pltest::Numbers, "double")
    descriptor = None
    for klass in pltest::Numbers.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)

def test_pltest::numbers_has_bigDecimal():
    assert hasattr(pltest::Numbers, "bigDecimal")
    descriptor = None
    for klass in pltest::Numbers.__mro__:
        if "bigDecimal" in klass.__dict__:
            descriptor = klass.__dict__["bigDecimal"]
            break
    assert isinstance(descriptor, property)

def test_pltest::numbers_has_int():
    assert hasattr(pltest::Numbers, "int")
    descriptor = None
    for klass in pltest::Numbers.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_pltest::numbers_has_long():
    assert hasattr(pltest::Numbers, "long")
    descriptor = None
    for klass in pltest::Numbers.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)

def test_pltest::numbers_has_float():
    assert hasattr(pltest::Numbers, "float")
    descriptor = None
    for klass in pltest::Numbers.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)



def test_grandchildd_is_not_abstract():
    assert not inspect.isabstract(GrandChildD)


def test_grandchildd_constructor_exists():
    assert callable(GrandChildD.__init__)


def test_grandchildd_constructor_args():
    sig = inspect.signature(GrandChildD.__init__)
    params = list(sig.parameters.keys())



def test_pltest::whatever_is_not_abstract():
    assert not inspect.isabstract(pltest::WhatEver)


def test_pltest::whatever_constructor_exists():
    assert callable(pltest::WhatEver.__init__)


def test_pltest::whatever_constructor_args():
    sig = inspect.signature(pltest::WhatEver.__init__)
    params = list(sig.parameters.keys())



def test_pltest::circle_is_not_abstract():
    assert not inspect.isabstract(pltest::Circle)


def test_pltest::circle_constructor_exists():
    assert callable(pltest::Circle.__init__)


def test_pltest::circle_constructor_args():
    sig = inspect.signature(pltest::Circle.__init__)
    params = list(sig.parameters.keys())
    assert "circumference" in params, "Missing parameter 'circumference'"
    assert "diameter" in params, "Missing parameter 'diameter'"
    assert "area" in params, "Missing parameter 'area'"

def test_pltest::circle_has_circumference():
    assert hasattr(pltest::Circle, "circumference")
    descriptor = None
    for klass in pltest::Circle.__mro__:
        if "circumference" in klass.__dict__:
            descriptor = klass.__dict__["circumference"]
            break
    assert isinstance(descriptor, property)

def test_pltest::circle_has_diameter():
    assert hasattr(pltest::Circle, "diameter")
    descriptor = None
    for klass in pltest::Circle.__mro__:
        if "diameter" in klass.__dict__:
            descriptor = klass.__dict__["diameter"]
            break
    assert isinstance(descriptor, property)

def test_pltest::circle_has_area():
    assert hasattr(pltest::Circle, "area")
    descriptor = None
    for klass in pltest::Circle.__mro__:
        if "area" in klass.__dict__:
            descriptor = klass.__dict__["area"]
            break
    assert isinstance(descriptor, property)



def test_pltest::red_is_not_abstract():
    assert not inspect.isabstract(pltest::Red)


def test_pltest::red_constructor_exists():
    assert callable(pltest::Red.__init__)


def test_pltest::red_constructor_args():
    sig = inspect.signature(pltest::Red.__init__)
    params = list(sig.parameters.keys())
    assert "redness" in params, "Missing parameter 'redness'"

def test_pltest::red_has_redness():
    assert hasattr(pltest::Red, "redness")
    descriptor = None
    for klass in pltest::Red.__mro__:
        if "redness" in klass.__dict__:
            descriptor = klass.__dict__["redness"]
            break
    assert isinstance(descriptor, property)



def test_testclassifier_is_not_abstract():
    assert not inspect.isabstract(TestClassifier)


def test_testclassifier_constructor_exists():
    assert callable(TestClassifier.__init__)


def test_testclassifier_constructor_args():
    sig = inspect.signature(TestClassifier.__init__)
    params = list(sig.parameters.keys())



def test_pltest::testinterface_is_not_abstract():
    assert not inspect.isabstract(pltest::TestInterface)


def test_pltest::testinterface_constructor_exists():
    assert callable(pltest::TestInterface.__init__)


def test_pltest::testinterface_constructor_args():
    sig = inspect.signature(pltest::TestInterface.__init__)
    params = list(sig.parameters.keys())



def test_pltest::testclass_is_not_abstract():
    assert not inspect.isabstract(pltest::TestClass)


def test_pltest::testclass_constructor_exists():
    assert callable(pltest::TestClass.__init__)


def test_pltest::testclass_constructor_args():
    sig = inspect.signature(pltest::TestClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackageableelement_is_not_abstract():
    assert not inspect.isabstract(TestPackageableElement)


def test_testpackageableelement_constructor_exists():
    assert callable(TestPackageableElement.__init__)


def test_testpackageableelement_constructor_args():
    sig = inspect.signature(TestPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_pltest::testclassifier_is_not_abstract():
    assert not inspect.isabstract(pltest::TestClassifier)


def test_pltest::testclassifier_constructor_exists():
    assert callable(pltest::TestClassifier.__init__)


def test_pltest::testclassifier_constructor_args():
    sig = inspect.signature(pltest::TestClassifier.__init__)
    params = list(sig.parameters.keys())



def test_pltest::testpackage_is_not_abstract():
    assert not inspect.isabstract(pltest::TestPackage)


def test_pltest::testpackage_constructor_exists():
    assert callable(pltest::TestPackage.__init__)


def test_pltest::testpackage_constructor_args():
    sig = inspect.signature(pltest::TestPackage.__init__)
    params = list(sig.parameters.keys())



def test_pltest::interface_is_not_abstract():
    assert not inspect.isabstract(pltest::Interface)


def test_pltest::interface_constructor_exists():
    assert callable(pltest::Interface.__init__)


def test_pltest::interface_constructor_args():
    sig = inspect.signature(pltest::Interface.__init__)
    params = list(sig.parameters.keys())



def test_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_base_constructor_exists():
    assert callable(Base.__init__)


def test_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())



def test_pltest::common_is_not_abstract():
    assert not inspect.isabstract(pltest::Common)


def test_pltest::common_constructor_exists():
    assert callable(pltest::Common.__init__)


def test_pltest::common_constructor_args():
    sig = inspect.signature(pltest::Common.__init__)
    params = list(sig.parameters.keys())



def test_pltest::base_is_not_abstract():
    assert not inspect.isabstract(pltest::Base)


def test_pltest::base_constructor_exists():
    assert callable(pltest::Base.__init__)


def test_pltest::base_constructor_args():
    sig = inspect.signature(pltest::Base.__init__)
    params = list(sig.parameters.keys())



def test_child2_is_not_abstract():
    assert not inspect.isabstract(Child2)


def test_child2_constructor_exists():
    assert callable(Child2.__init__)


def test_child2_constructor_args():
    sig = inspect.signature(Child2.__init__)
    params = list(sig.parameters.keys())



def test_pltest::grandgrandchildf_is_not_abstract():
    assert not inspect.isabstract(pltest::GrandGrandChildF)


def test_pltest::grandgrandchildf_constructor_exists():
    assert callable(pltest::GrandGrandChildF.__init__)


def test_pltest::grandgrandchildf_constructor_args():
    sig = inspect.signature(pltest::GrandGrandChildF.__init__)
    params = list(sig.parameters.keys())



def test_pltest::grandchild2_is_not_abstract():
    assert not inspect.isabstract(pltest::GrandChild2)


def test_pltest::grandchild2_constructor_exists():
    assert callable(pltest::GrandChild2.__init__)


def test_pltest::grandchild2_constructor_args():
    sig = inspect.signature(pltest::GrandChild2.__init__)
    params = list(sig.parameters.keys())



def test_pltest::child3_is_not_abstract():
    assert not inspect.isabstract(pltest::Child3)


def test_pltest::child3_constructor_exists():
    assert callable(pltest::Child3.__init__)


def test_pltest::child3_constructor_args():
    sig = inspect.signature(pltest::Child3.__init__)
    params = list(sig.parameters.keys())



def test_child1_is_not_abstract():
    assert not inspect.isabstract(Child1)


def test_child1_constructor_exists():
    assert callable(Child1.__init__)


def test_child1_constructor_args():
    sig = inspect.signature(Child1.__init__)
    params = list(sig.parameters.keys())



def test_pltest::grandgrandchilde_is_not_abstract():
    assert not inspect.isabstract(pltest::GrandGrandChildE)


def test_pltest::grandgrandchilde_constructor_exists():
    assert callable(pltest::GrandGrandChildE.__init__)


def test_pltest::grandgrandchilde_constructor_args():
    sig = inspect.signature(pltest::GrandGrandChildE.__init__)
    params = list(sig.parameters.keys())



def test_child3_is_not_abstract():
    assert not inspect.isabstract(Child3)


def test_child3_constructor_exists():
    assert callable(Child3.__init__)


def test_child3_constructor_args():
    sig = inspect.signature(Child3.__init__)
    params = list(sig.parameters.keys())



def test_pltest::grandchildd_is_not_abstract():
    assert not inspect.isabstract(pltest::GrandChildD)


def test_pltest::grandchildd_constructor_exists():
    assert callable(pltest::GrandChildD.__init__)


def test_pltest::grandchildd_constructor_args():
    sig = inspect.signature(pltest::GrandChildD.__init__)
    params = list(sig.parameters.keys())



def test_pltest::grandchild_is_not_abstract():
    assert not inspect.isabstract(pltest::GrandChild)


def test_pltest::grandchild_constructor_exists():
    assert callable(pltest::GrandChild.__init__)


def test_pltest::grandchild_constructor_args():
    sig = inspect.signature(pltest::GrandChild.__init__)
    params = list(sig.parameters.keys())



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_common_is_not_abstract():
    assert not inspect.isabstract(Common)


def test_common_constructor_exists():
    assert callable(Common.__init__)


def test_common_constructor_args():
    sig = inspect.signature(Common.__init__)
    params = list(sig.parameters.keys())



def test_pltest::child2_is_not_abstract():
    assert not inspect.isabstract(pltest::Child2)


def test_pltest::child2_constructor_exists():
    assert callable(pltest::Child2.__init__)


def test_pltest::child2_constructor_args():
    sig = inspect.signature(pltest::Child2.__init__)
    params = list(sig.parameters.keys())



def test_pltest::child1_is_not_abstract():
    assert not inspect.isabstract(pltest::Child1)


def test_pltest::child1_constructor_exists():
    assert callable(pltest::Child1.__init__)


def test_pltest::child1_constructor_args():
    sig = inspect.signature(pltest::Child1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pltest::child1_has_name():
    assert hasattr(pltest::Child1, "name")
    descriptor = None
    for klass in pltest::Child1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
pltest::TestPackageableElement_strategy = st.builds(
    pltest::TestPackageableElement,
)
pltest::Numbers_strategy = st.builds(
    pltest::Numbers,
    bigInt=
        safe_text,
    double=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    bigDecimal=
        safe_text,
    int=
        st.integers(),
    long=
        safe_text,
    float=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
GrandChildD_strategy = st.builds(
    GrandChildD,
)
pltest::WhatEver_strategy = st.builds(
    pltest::WhatEver,
)
pltest::Circle_strategy = st.builds(
    pltest::Circle,
    circumference=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    diameter=
        safe_text,
    area=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
pltest::Red_strategy = st.builds(
    pltest::Red,
    redness=
        st.integers()
)
TestClassifier_strategy = st.builds(
    TestClassifier,
)
pltest::TestInterface_strategy = st.builds(
    pltest::TestInterface,
)
pltest::TestClass_strategy = st.builds(
    pltest::TestClass,
)
TestPackageableElement_strategy = st.builds(
    TestPackageableElement,
)
pltest::TestClassifier_strategy = st.builds(
    pltest::TestClassifier,
)
pltest::TestPackage_strategy = st.builds(
    pltest::TestPackage,
)
pltest::Interface_strategy = st.builds(
    pltest::Interface,
)
Base_strategy = st.builds(
    Base,
)
pltest::Common_strategy = st.builds(
    pltest::Common,
)
pltest::Base_strategy = st.builds(
    pltest::Base,
)
Child2_strategy = st.builds(
    Child2,
)
pltest::GrandGrandChildF_strategy = st.builds(
    pltest::GrandGrandChildF,
)
pltest::GrandChild2_strategy = st.builds(
    pltest::GrandChild2,
)
pltest::Child3_strategy = st.builds(
    pltest::Child3,
)
Child1_strategy = st.builds(
    Child1,
)
pltest::GrandGrandChildE_strategy = st.builds(
    pltest::GrandGrandChildE,
)
Child3_strategy = st.builds(
    Child3,
)
pltest::GrandChildD_strategy = st.builds(
    pltest::GrandChildD,
)
pltest::GrandChild_strategy = st.builds(
    pltest::GrandChild,
)
Interface_strategy = st.builds(
    Interface,
)
Common_strategy = st.builds(
    Common,
)
pltest::Child2_strategy = st.builds(
    pltest::Child2,
)
pltest::Child1_strategy = st.builds(
    pltest::Child1,
    name=
        safe_text
)

@given(instance=pltest::TestPackageableElement_strategy)
@settings(max_examples=50)
def test_pltest::testpackageableelement_instantiation(instance):
    assert isinstance(instance, pltest::TestPackageableElement)

@given(instance=pltest::Numbers_strategy)
@settings(max_examples=50)
def test_pltest::numbers_instantiation(instance):
    assert isinstance(instance, pltest::Numbers)

@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_bigInt_type(instance):
    assert isinstance(instance.bigInt, str)


@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_bigInt_setter(instance):
    original = instance.bigInt
    instance.bigInt = original
    assert instance.bigInt == original

@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_double_type(instance):
    assert isinstance(instance.double, float)


@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original

@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_bigDecimal_type(instance):
    assert isinstance(instance.bigDecimal, str)


@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original

@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_int_type(instance):
    assert isinstance(instance.int, int)


@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_long_type(instance):
    assert isinstance(instance.long, str)


@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original

@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_float_type(instance):
    assert isinstance(instance.float, float)


@given(instance=pltest::Numbers_strategy)
def test_pltest::numbers_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original

@given(instance=GrandChildD_strategy)
@settings(max_examples=50)
def test_grandchildd_instantiation(instance):
    assert isinstance(instance, GrandChildD)

@given(instance=pltest::WhatEver_strategy)
@settings(max_examples=50)
def test_pltest::whatever_instantiation(instance):
    assert isinstance(instance, pltest::WhatEver)

@given(instance=pltest::Circle_strategy)
@settings(max_examples=50)
def test_pltest::circle_instantiation(instance):
    assert isinstance(instance, pltest::Circle)

@given(instance=pltest::Circle_strategy)
def test_pltest::circle_circumference_type(instance):
    assert isinstance(instance.circumference, float)


@given(instance=pltest::Circle_strategy)
def test_pltest::circle_circumference_setter(instance):
    original = instance.circumference
    instance.circumference = original
    assert instance.circumference == original

@given(instance=pltest::Circle_strategy)
def test_pltest::circle_diameter_type(instance):
    assert isinstance(instance.diameter, str)


@given(instance=pltest::Circle_strategy)
def test_pltest::circle_diameter_setter(instance):
    original = instance.diameter
    instance.diameter = original
    assert instance.diameter == original

@given(instance=pltest::Circle_strategy)
def test_pltest::circle_area_type(instance):
    assert isinstance(instance.area, float)


@given(instance=pltest::Circle_strategy)
def test_pltest::circle_area_setter(instance):
    original = instance.area
    instance.area = original
    assert instance.area == original

@given(instance=pltest::Red_strategy)
@settings(max_examples=50)
def test_pltest::red_instantiation(instance):
    assert isinstance(instance, pltest::Red)

@given(instance=pltest::Red_strategy)
def test_pltest::red_redness_type(instance):
    assert isinstance(instance.redness, int)


@given(instance=pltest::Red_strategy)
def test_pltest::red_redness_setter(instance):
    original = instance.redness
    instance.redness = original
    assert instance.redness == original

@given(instance=TestClassifier_strategy)
@settings(max_examples=50)
def test_testclassifier_instantiation(instance):
    assert isinstance(instance, TestClassifier)

@given(instance=pltest::TestInterface_strategy)
@settings(max_examples=50)
def test_pltest::testinterface_instantiation(instance):
    assert isinstance(instance, pltest::TestInterface)

@given(instance=pltest::TestClass_strategy)
@settings(max_examples=50)
def test_pltest::testclass_instantiation(instance):
    assert isinstance(instance, pltest::TestClass)

@given(instance=TestPackageableElement_strategy)
@settings(max_examples=50)
def test_testpackageableelement_instantiation(instance):
    assert isinstance(instance, TestPackageableElement)

@given(instance=pltest::TestClassifier_strategy)
@settings(max_examples=50)
def test_pltest::testclassifier_instantiation(instance):
    assert isinstance(instance, pltest::TestClassifier)

@given(instance=pltest::TestPackage_strategy)
@settings(max_examples=50)
def test_pltest::testpackage_instantiation(instance):
    assert isinstance(instance, pltest::TestPackage)

@given(instance=pltest::Interface_strategy)
@settings(max_examples=50)
def test_pltest::interface_instantiation(instance):
    assert isinstance(instance, pltest::Interface)

@given(instance=Base_strategy)
@settings(max_examples=50)
def test_base_instantiation(instance):
    assert isinstance(instance, Base)

@given(instance=pltest::Common_strategy)
@settings(max_examples=50)
def test_pltest::common_instantiation(instance):
    assert isinstance(instance, pltest::Common)

@given(instance=pltest::Base_strategy)
@settings(max_examples=50)
def test_pltest::base_instantiation(instance):
    assert isinstance(instance, pltest::Base)

@given(instance=Child2_strategy)
@settings(max_examples=50)
def test_child2_instantiation(instance):
    assert isinstance(instance, Child2)

@given(instance=pltest::GrandGrandChildF_strategy)
@settings(max_examples=50)
def test_pltest::grandgrandchildf_instantiation(instance):
    assert isinstance(instance, pltest::GrandGrandChildF)

@given(instance=pltest::GrandChild2_strategy)
@settings(max_examples=50)
def test_pltest::grandchild2_instantiation(instance):
    assert isinstance(instance, pltest::GrandChild2)

@given(instance=pltest::Child3_strategy)
@settings(max_examples=50)
def test_pltest::child3_instantiation(instance):
    assert isinstance(instance, pltest::Child3)

@given(instance=Child1_strategy)
@settings(max_examples=50)
def test_child1_instantiation(instance):
    assert isinstance(instance, Child1)

@given(instance=pltest::GrandGrandChildE_strategy)
@settings(max_examples=50)
def test_pltest::grandgrandchilde_instantiation(instance):
    assert isinstance(instance, pltest::GrandGrandChildE)

@given(instance=Child3_strategy)
@settings(max_examples=50)
def test_child3_instantiation(instance):
    assert isinstance(instance, Child3)

@given(instance=pltest::GrandChildD_strategy)
@settings(max_examples=50)
def test_pltest::grandchildd_instantiation(instance):
    assert isinstance(instance, pltest::GrandChildD)

@given(instance=pltest::GrandChild_strategy)
@settings(max_examples=50)
def test_pltest::grandchild_instantiation(instance):
    assert isinstance(instance, pltest::GrandChild)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=Common_strategy)
@settings(max_examples=50)
def test_common_instantiation(instance):
    assert isinstance(instance, Common)

@given(instance=pltest::Child2_strategy)
@settings(max_examples=50)
def test_pltest::child2_instantiation(instance):
    assert isinstance(instance, pltest::Child2)

@given(instance=pltest::Child1_strategy)
@settings(max_examples=50)
def test_pltest::child1_instantiation(instance):
    assert isinstance(instance, pltest::Child1)

@given(instance=pltest::Child1_strategy)
def test_pltest::child1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pltest::Child1_strategy)
def test_pltest::child1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
