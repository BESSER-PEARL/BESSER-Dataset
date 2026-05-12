import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    subPackage_Foo,
    subsub_Bar,
    myPackage_subsub_Baz,
    myPackage_subsub_Bar,
    MyClass,
    myPackage_subPackage_Foo,
    myPackage_AThirdClass,
    myPackage_MyOtherClass,
    myPackage_MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subpackage_foo_is_not_abstract():
    assert not inspect.isabstract(subPackage_Foo)


def test_subpackage_foo_constructor_exists():
    assert callable(subPackage_Foo.__init__)


def test_subpackage_foo_constructor_args():
    sig = inspect.signature(subPackage_Foo.__init__)
    params = list(sig.parameters.keys())



def test_subsub_bar_is_not_abstract():
    assert not inspect.isabstract(subsub_Bar)


def test_subsub_bar_constructor_exists():
    assert callable(subsub_Bar.__init__)


def test_subsub_bar_constructor_args():
    sig = inspect.signature(subsub_Bar.__init__)
    params = list(sig.parameters.keys())



def test_mypackage_subsub_baz_is_not_abstract():
    assert not inspect.isabstract(myPackage_subsub_Baz)


def test_mypackage_subsub_baz_constructor_exists():
    assert callable(myPackage_subsub_Baz.__init__)


def test_mypackage_subsub_baz_constructor_args():
    sig = inspect.signature(myPackage_subsub_Baz.__init__)
    params = list(sig.parameters.keys())



def test_mypackage_subsub_bar_is_not_abstract():
    assert not inspect.isabstract(myPackage_subsub_Bar)


def test_mypackage_subsub_bar_constructor_exists():
    assert callable(myPackage_subsub_Bar.__init__)


def test_mypackage_subsub_bar_constructor_args():
    sig = inspect.signature(myPackage_subsub_Bar.__init__)
    params = list(sig.parameters.keys())
    assert "s" in params, "Missing parameter 's'"

def test_mypackage_subsub_bar_has_s():
    assert hasattr(myPackage_subsub_Bar, "s")
    descriptor = None
    for klass in myPackage_subsub_Bar.__mro__:
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



def test_mypackage_subpackage_foo_is_not_abstract():
    assert not inspect.isabstract(myPackage_subPackage_Foo)


def test_mypackage_subpackage_foo_constructor_exists():
    assert callable(myPackage_subPackage_Foo.__init__)


def test_mypackage_subpackage_foo_constructor_args():
    sig = inspect.signature(myPackage_subPackage_Foo.__init__)
    params = list(sig.parameters.keys())



def test_mypackage_athirdclass_is_not_abstract():
    assert not inspect.isabstract(myPackage_AThirdClass)


def test_mypackage_athirdclass_constructor_exists():
    assert callable(myPackage_AThirdClass.__init__)


def test_mypackage_athirdclass_constructor_args():
    sig = inspect.signature(myPackage_AThirdClass.__init__)
    params = list(sig.parameters.keys())
    assert "thirdAttribute" in params, "Missing parameter 'thirdAttribute'"

def test_mypackage_athirdclass_has_thirdAttribute():
    assert hasattr(myPackage_AThirdClass, "thirdAttribute")
    descriptor = None
    for klass in myPackage_AThirdClass.__mro__:
        if "thirdAttribute" in klass.__dict__:
            descriptor = klass.__dict__["thirdAttribute"]
            break
    assert isinstance(descriptor, property)



def test_mypackage_myotherclass_is_not_abstract():
    assert not inspect.isabstract(myPackage_MyOtherClass)


def test_mypackage_myotherclass_constructor_exists():
    assert callable(myPackage_MyOtherClass.__init__)


def test_mypackage_myotherclass_constructor_args():
    sig = inspect.signature(myPackage_MyOtherClass.__init__)
    params = list(sig.parameters.keys())
    assert "otherAttribute" in params, "Missing parameter 'otherAttribute'"

def test_mypackage_myotherclass_has_otherAttribute():
    assert hasattr(myPackage_MyOtherClass, "otherAttribute")
    descriptor = None
    for klass in myPackage_MyOtherClass.__mro__:
        if "otherAttribute" in klass.__dict__:
            descriptor = klass.__dict__["otherAttribute"]
            break
    assert isinstance(descriptor, property)



def test_mypackage_myclass_is_not_abstract():
    assert not inspect.isabstract(myPackage_MyClass)


def test_mypackage_myclass_constructor_exists():
    assert callable(myPackage_MyClass.__init__)


def test_mypackage_myclass_constructor_args():
    sig = inspect.signature(myPackage_MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "myAttribute" in params, "Missing parameter 'myAttribute'"

def test_mypackage_myclass_has_myAttribute():
    assert hasattr(myPackage_MyClass, "myAttribute")
    descriptor = None
    for klass in myPackage_MyClass.__mro__:
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
subPackage_Foo_strategy = st.builds(
    subPackage_Foo,
)
subsub_Bar_strategy = st.builds(
    subsub_Bar,
)
myPackage_subsub_Baz_strategy = st.builds(
    myPackage_subsub_Baz,
)
myPackage_subsub_Bar_strategy = st.builds(
    myPackage_subsub_Bar,
    s=
        safe_text
)
MyClass_strategy = st.builds(
    MyClass,
)
myPackage_subPackage_Foo_strategy = st.builds(
    myPackage_subPackage_Foo,
)
myPackage_AThirdClass_strategy = st.builds(
    myPackage_AThirdClass,
    thirdAttribute=
        safe_text
)
myPackage_MyOtherClass_strategy = st.builds(
    myPackage_MyOtherClass,
    otherAttribute=
        safe_text
)
myPackage_MyClass_strategy = st.builds(
    myPackage_MyClass,
    myAttribute=
        safe_text
)

@given(instance=subPackage_Foo_strategy)
@settings(max_examples=50)
def test_subpackage_foo_instantiation(instance):
    assert isinstance(instance, subPackage_Foo)

@given(instance=subsub_Bar_strategy)
@settings(max_examples=50)
def test_subsub_bar_instantiation(instance):
    assert isinstance(instance, subsub_Bar)

@given(instance=myPackage_subsub_Baz_strategy)
@settings(max_examples=50)
def test_mypackage_subsub_baz_instantiation(instance):
    assert isinstance(instance, myPackage_subsub_Baz)

@given(instance=myPackage_subsub_Bar_strategy)
@settings(max_examples=50)
def test_mypackage_subsub_bar_instantiation(instance):
    assert isinstance(instance, myPackage_subsub_Bar)



@given(instance=myPackage_subsub_Bar_strategy)
def test_mypackage_subsub_bar_s_setter(instance):
    original = instance.s
    instance.s = original
    assert instance.s == original

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)

@given(instance=myPackage_subPackage_Foo_strategy)
@settings(max_examples=50)
def test_mypackage_subpackage_foo_instantiation(instance):
    assert isinstance(instance, myPackage_subPackage_Foo)

@given(instance=myPackage_AThirdClass_strategy)
@settings(max_examples=50)
def test_mypackage_athirdclass_instantiation(instance):
    assert isinstance(instance, myPackage_AThirdClass)



@given(instance=myPackage_AThirdClass_strategy)
def test_mypackage_athirdclass_thirdAttribute_setter(instance):
    original = instance.thirdAttribute
    instance.thirdAttribute = original
    assert instance.thirdAttribute == original

@given(instance=myPackage_MyOtherClass_strategy)
@settings(max_examples=50)
def test_mypackage_myotherclass_instantiation(instance):
    assert isinstance(instance, myPackage_MyOtherClass)



@given(instance=myPackage_MyOtherClass_strategy)
def test_mypackage_myotherclass_otherAttribute_setter(instance):
    original = instance.otherAttribute
    instance.otherAttribute = original
    assert instance.otherAttribute == original

@given(instance=myPackage_MyClass_strategy)
@settings(max_examples=50)
def test_mypackage_myclass_instantiation(instance):
    assert isinstance(instance, myPackage_MyClass)



@given(instance=myPackage_MyClass_strategy)
def test_mypackage_myclass_myAttribute_setter(instance):
    original = instance.myAttribute
    instance.myAttribute = original
    assert instance.myAttribute == original
