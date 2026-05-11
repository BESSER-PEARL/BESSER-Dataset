import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Triangles::AbstractClass,
    AbstractClass,
    Triangles::C::Class,
    Triangles::B::Class,
    Triangles::E::Class,
    Triangles::D::Class,
    Triangles::A::Class,
    Triangles::Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_triangles::abstractclass_is_not_abstract():
    assert not inspect.isabstract(Triangles::AbstractClass)


def test_triangles::abstractclass_constructor_exists():
    assert callable(Triangles::AbstractClass.__init__)


def test_triangles::abstractclass_constructor_args():
    sig = inspect.signature(Triangles::AbstractClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "flag" in params, "Missing parameter 'flag'"
    assert "id" in params, "Missing parameter 'id'"

def test_triangles::abstractclass_has_name():
    assert hasattr(Triangles::AbstractClass, "name")
    descriptor = None
    for klass in Triangles::AbstractClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_triangles::abstractclass_has_flag():
    assert hasattr(Triangles::AbstractClass, "flag")
    descriptor = None
    for klass in Triangles::AbstractClass.__mro__:
        if "flag" in klass.__dict__:
            descriptor = klass.__dict__["flag"]
            break
    assert isinstance(descriptor, property)

def test_triangles::abstractclass_has_id():
    assert hasattr(Triangles::AbstractClass, "id")
    descriptor = None
    for klass in Triangles::AbstractClass.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_abstractclass_is_not_abstract():
    assert not inspect.isabstract(AbstractClass)


def test_abstractclass_constructor_exists():
    assert callable(AbstractClass.__init__)


def test_abstractclass_constructor_args():
    sig = inspect.signature(AbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_triangles::c::class_is_not_abstract():
    assert not inspect.isabstract(Triangles::C::Class)


def test_triangles::c::class_constructor_exists():
    assert callable(Triangles::C::Class.__init__)


def test_triangles::c::class_constructor_args():
    sig = inspect.signature(Triangles::C::Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles::b::class_is_not_abstract():
    assert not inspect.isabstract(Triangles::B::Class)


def test_triangles::b::class_constructor_exists():
    assert callable(Triangles::B::Class.__init__)


def test_triangles::b::class_constructor_args():
    sig = inspect.signature(Triangles::B::Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles::e::class_is_not_abstract():
    assert not inspect.isabstract(Triangles::E::Class)


def test_triangles::e::class_constructor_exists():
    assert callable(Triangles::E::Class.__init__)


def test_triangles::e::class_constructor_args():
    sig = inspect.signature(Triangles::E::Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles::d::class_is_not_abstract():
    assert not inspect.isabstract(Triangles::D::Class)


def test_triangles::d::class_constructor_exists():
    assert callable(Triangles::D::Class.__init__)


def test_triangles::d::class_constructor_args():
    sig = inspect.signature(Triangles::D::Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles::a::class_is_not_abstract():
    assert not inspect.isabstract(Triangles::A::Class)


def test_triangles::a::class_constructor_exists():
    assert callable(Triangles::A::Class.__init__)


def test_triangles::a::class_constructor_args():
    sig = inspect.signature(Triangles::A::Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles::container_is_not_abstract():
    assert not inspect.isabstract(Triangles::Container)


def test_triangles::container_constructor_exists():
    assert callable(Triangles::Container.__init__)


def test_triangles::container_constructor_args():
    sig = inspect.signature(Triangles::Container.__init__)
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
Triangles::AbstractClass_strategy = st.builds(
    Triangles::AbstractClass,
    name=
        safe_text,
    flag=
        st.booleans(),
    id=
        st.integers()
)
AbstractClass_strategy = st.builds(
    AbstractClass,
)
Triangles::C::Class_strategy = st.builds(
    Triangles::C::Class,
)
Triangles::B::Class_strategy = st.builds(
    Triangles::B::Class,
)
Triangles::E::Class_strategy = st.builds(
    Triangles::E::Class,
)
Triangles::D::Class_strategy = st.builds(
    Triangles::D::Class,
)
Triangles::A::Class_strategy = st.builds(
    Triangles::A::Class,
)
Triangles::Container_strategy = st.builds(
    Triangles::Container,
)

@given(instance=Triangles::AbstractClass_strategy)
@settings(max_examples=50)
def test_triangles::abstractclass_instantiation(instance):
    assert isinstance(instance, Triangles::AbstractClass)

@given(instance=Triangles::AbstractClass_strategy)
def test_triangles::abstractclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Triangles::AbstractClass_strategy)
def test_triangles::abstractclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Triangles::AbstractClass_strategy)
def test_triangles::abstractclass_flag_type(instance):
    assert isinstance(instance.flag, bool)


@given(instance=Triangles::AbstractClass_strategy)
def test_triangles::abstractclass_flag_setter(instance):
    original = instance.flag
    instance.flag = original
    assert instance.flag == original

@given(instance=Triangles::AbstractClass_strategy)
def test_triangles::abstractclass_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=Triangles::AbstractClass_strategy)
def test_triangles::abstractclass_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AbstractClass_strategy)
@settings(max_examples=50)
def test_abstractclass_instantiation(instance):
    assert isinstance(instance, AbstractClass)

@given(instance=Triangles::C::Class_strategy)
@settings(max_examples=50)
def test_triangles::c::class_instantiation(instance):
    assert isinstance(instance, Triangles::C::Class)

@given(instance=Triangles::B::Class_strategy)
@settings(max_examples=50)
def test_triangles::b::class_instantiation(instance):
    assert isinstance(instance, Triangles::B::Class)

@given(instance=Triangles::E::Class_strategy)
@settings(max_examples=50)
def test_triangles::e::class_instantiation(instance):
    assert isinstance(instance, Triangles::E::Class)

@given(instance=Triangles::D::Class_strategy)
@settings(max_examples=50)
def test_triangles::d::class_instantiation(instance):
    assert isinstance(instance, Triangles::D::Class)

@given(instance=Triangles::A::Class_strategy)
@settings(max_examples=50)
def test_triangles::a::class_instantiation(instance):
    assert isinstance(instance, Triangles::A::Class)

@given(instance=Triangles::Container_strategy)
@settings(max_examples=50)
def test_triangles::container_instantiation(instance):
    assert isinstance(instance, Triangles::Container)
