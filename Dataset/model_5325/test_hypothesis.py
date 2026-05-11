import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    subPackage::Foo,
    subsub::Bar,
    myPackage::subsub::Baz,
    myPackage::subsub::Bar,
    MyClass,
    myPackage::subPackage::Foo,
    myPackage::AThirdClass,
    myPackage::MyOtherClass,
    myPackage::MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subpackage::foo_is_not_abstract():
    assert not inspect.isabstract(subPackage::Foo)


def test_subpackage::foo_constructor_exists():
    assert callable(subPackage::Foo.__init__)


def test_subpackage::foo_constructor_args():
    sig = inspect.signature(subPackage::Foo.__init__)
    params = list(sig.parameters.keys())



def test_subsub::bar_is_not_abstract():
    assert not inspect.isabstract(subsub::Bar)


def test_subsub::bar_constructor_exists():
    assert callable(subsub::Bar.__init__)


def test_subsub::bar_constructor_args():
    sig = inspect.signature(subsub::Bar.__init__)
    params = list(sig.parameters.keys())



def test_mypackage::subsub::baz_is_not_abstract():
    assert not inspect.isabstract(myPackage::subsub::Baz)


def test_mypackage::subsub::baz_constructor_exists():
    assert callable(myPackage::subsub::Baz.__init__)


def test_mypackage::subsub::baz_constructor_args():
    sig = inspect.signature(myPackage::subsub::Baz.__init__)
    params = list(sig.parameters.keys())



def test_mypackage::subsub::bar_is_not_abstract():
    assert not inspect.isabstract(myPackage::subsub::Bar)


def test_mypackage::subsub::bar_constructor_exists():
    assert callable(myPackage::subsub::Bar.__init__)


def test_mypackage::subsub::bar_constructor_args():
    sig = inspect.signature(myPackage::subsub::Bar.__init__)
    params = list(sig.parameters.keys())
    assert "s" in params, "Missing parameter 's'"

def test_mypackage::subsub::bar_has_s():
    assert hasattr(myPackage::subsub::Bar, "s")
    descriptor = None
    for klass in myPackage::subsub::Bar.__mro__:
        if "s" in klass.__dict__:
            descriptor = klass.__dict__["s"]
            break
    assert isinstance(descriptor, property)



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_mypackage::subpackage::foo_is_not_abstract():
    assert not inspect.isabstract(myPackage::subPackage::Foo)


def test_mypackage::subpackage::foo_constructor_exists():
    assert callable(myPackage::subPackage::Foo.__init__)


def test_mypackage::subpackage::foo_constructor_args():
    sig = inspect.signature(myPackage::subPackage::Foo.__init__)
    params = list(sig.parameters.keys())



def test_mypackage::athirdclass_is_not_abstract():
    assert not inspect.isabstract(myPackage::AThirdClass)


def test_mypackage::athirdclass_constructor_exists():
    assert callable(myPackage::AThirdClass.__init__)


def test_mypackage::athirdclass_constructor_args():
    sig = inspect.signature(myPackage::AThirdClass.__init__)
    params = list(sig.parameters.keys())
    assert "thirdAttribute" in params, "Missing parameter 'thirdAttribute'"

def test_mypackage::athirdclass_has_thirdAttribute():
    assert hasattr(myPackage::AThirdClass, "thirdAttribute")
    descriptor = None
    for klass in myPackage::AThirdClass.__mro__:
        if "thirdAttribute" in klass.__dict__:
            descriptor = klass.__dict__["thirdAttribute"]
            break
    assert isinstance(descriptor, property)



def test_mypackage::myotherclass_is_not_abstract():
    assert not inspect.isabstract(myPackage::MyOtherClass)


def test_mypackage::myotherclass_constructor_exists():
    assert callable(myPackage::MyOtherClass.__init__)


def test_mypackage::myotherclass_constructor_args():
    sig = inspect.signature(myPackage::MyOtherClass.__init__)
    params = list(sig.parameters.keys())
    assert "otherAttribute" in params, "Missing parameter 'otherAttribute'"

def test_mypackage::myotherclass_has_otherAttribute():
    assert hasattr(myPackage::MyOtherClass, "otherAttribute")
    descriptor = None
    for klass in myPackage::MyOtherClass.__mro__:
        if "otherAttribute" in klass.__dict__:
            descriptor = klass.__dict__["otherAttribute"]
            break
    assert isinstance(descriptor, property)



def test_mypackage::myclass_is_not_abstract():
    assert not inspect.isabstract(myPackage::MyClass)


def test_mypackage::myclass_constructor_exists():
    assert callable(myPackage::MyClass.__init__)


def test_mypackage::myclass_constructor_args():
    sig = inspect.signature(myPackage::MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "myAttribute" in params, "Missing parameter 'myAttribute'"

def test_mypackage::myclass_has_myAttribute():
    assert hasattr(myPackage::MyClass, "myAttribute")
    descriptor = None
    for klass in myPackage::MyClass.__mro__:
        if "myAttribute" in klass.__dict__:
            descriptor = klass.__dict__["myAttribute"]
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
subPackage::Foo_strategy = st.builds(
    subPackage::Foo,
)
subsub::Bar_strategy = st.builds(
    subsub::Bar,
)
myPackage::subsub::Baz_strategy = st.builds(
    myPackage::subsub::Baz,
)
myPackage::subsub::Bar_strategy = st.builds(
    myPackage::subsub::Bar,
    s=
        safe_text
)
MyClass_strategy = st.builds(
    MyClass,
)
myPackage::subPackage::Foo_strategy = st.builds(
    myPackage::subPackage::Foo,
)
myPackage::AThirdClass_strategy = st.builds(
    myPackage::AThirdClass,
    thirdAttribute=
        safe_text
)
myPackage::MyOtherClass_strategy = st.builds(
    myPackage::MyOtherClass,
    otherAttribute=
        safe_text
)
myPackage::MyClass_strategy = st.builds(
    myPackage::MyClass,
    myAttribute=
        safe_text
)

@given(instance=subPackage::Foo_strategy)
@settings(max_examples=50)
def test_subpackage::foo_instantiation(instance):
    assert isinstance(instance, subPackage::Foo)

@given(instance=subsub::Bar_strategy)
@settings(max_examples=50)
def test_subsub::bar_instantiation(instance):
    assert isinstance(instance, subsub::Bar)

@given(instance=myPackage::subsub::Baz_strategy)
@settings(max_examples=50)
def test_mypackage::subsub::baz_instantiation(instance):
    assert isinstance(instance, myPackage::subsub::Baz)

@given(instance=myPackage::subsub::Bar_strategy)
@settings(max_examples=50)
def test_mypackage::subsub::bar_instantiation(instance):
    assert isinstance(instance, myPackage::subsub::Bar)

@given(instance=myPackage::subsub::Bar_strategy)
def test_mypackage::subsub::bar_s_type(instance):
    assert isinstance(instance.s, str)


@given(instance=myPackage::subsub::Bar_strategy)
def test_mypackage::subsub::bar_s_setter(instance):
    original = instance.s
    instance.s = original
    assert instance.s == original

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)

@given(instance=myPackage::subPackage::Foo_strategy)
@settings(max_examples=50)
def test_mypackage::subpackage::foo_instantiation(instance):
    assert isinstance(instance, myPackage::subPackage::Foo)

@given(instance=myPackage::AThirdClass_strategy)
@settings(max_examples=50)
def test_mypackage::athirdclass_instantiation(instance):
    assert isinstance(instance, myPackage::AThirdClass)

@given(instance=myPackage::AThirdClass_strategy)
def test_mypackage::athirdclass_thirdAttribute_type(instance):
    assert isinstance(instance.thirdAttribute, str)


@given(instance=myPackage::AThirdClass_strategy)
def test_mypackage::athirdclass_thirdAttribute_setter(instance):
    original = instance.thirdAttribute
    instance.thirdAttribute = original
    assert instance.thirdAttribute == original

@given(instance=myPackage::MyOtherClass_strategy)
@settings(max_examples=50)
def test_mypackage::myotherclass_instantiation(instance):
    assert isinstance(instance, myPackage::MyOtherClass)

@given(instance=myPackage::MyOtherClass_strategy)
def test_mypackage::myotherclass_otherAttribute_type(instance):
    assert isinstance(instance.otherAttribute, str)


@given(instance=myPackage::MyOtherClass_strategy)
def test_mypackage::myotherclass_otherAttribute_setter(instance):
    original = instance.otherAttribute
    instance.otherAttribute = original
    assert instance.otherAttribute == original

@given(instance=myPackage::MyClass_strategy)
@settings(max_examples=50)
def test_mypackage::myclass_instantiation(instance):
    assert isinstance(instance, myPackage::MyClass)

@given(instance=myPackage::MyClass_strategy)
def test_mypackage::myclass_myAttribute_type(instance):
    assert isinstance(instance.myAttribute, str)


@given(instance=myPackage::MyClass_strategy)
def test_mypackage::myclass_myAttribute_setter(instance):
    original = instance.myAttribute
    instance.myAttribute = original
    assert instance.myAttribute == original
