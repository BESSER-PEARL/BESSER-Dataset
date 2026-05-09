import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Baz,
    yyk::Boul,
    yyk::Bouz,
    yyk::NamedElement,
    yyk::Output,
    yyk::Foo,
    NamedElement,
    yyk::Baz,
    yyk::Relation,
    yyk::Zing,
    yyk::Base,
    yyk::Rel,
    yyk::Bar,
    yyk::Alias,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_baz_is_not_abstract():
    assert not inspect.isabstract(Baz)


def test_baz_constructor_exists():
    assert callable(Baz.__init__)


def test_baz_constructor_args():
    sig = inspect.signature(Baz.__init__)
    params = list(sig.parameters.keys())



def test_yyk::boul_is_not_abstract():
    assert not inspect.isabstract(yyk::Boul)


def test_yyk::boul_constructor_exists():
    assert callable(yyk::Boul.__init__)


def test_yyk::boul_constructor_args():
    sig = inspect.signature(yyk::Boul.__init__)
    params = list(sig.parameters.keys())
    assert "hi" in params, "Missing parameter 'hi'"

def test_yyk::boul_has_hi():
    assert hasattr(yyk::Boul, "hi")
    descriptor = None
    for klass in yyk::Boul.__mro__:
        if "hi" in klass.__dict__:
            descriptor = klass.__dict__["hi"]
            break
    assert isinstance(descriptor, property)



def test_yyk::bouz_is_not_abstract():
    assert not inspect.isabstract(yyk::Bouz)


def test_yyk::bouz_constructor_exists():
    assert callable(yyk::Bouz.__init__)


def test_yyk::bouz_constructor_args():
    sig = inspect.signature(yyk::Bouz.__init__)
    params = list(sig.parameters.keys())
    assert "bil" in params, "Missing parameter 'bil'"

def test_yyk::bouz_has_bil():
    assert hasattr(yyk::Bouz, "bil")
    descriptor = None
    for klass in yyk::Bouz.__mro__:
        if "bil" in klass.__dict__:
            descriptor = klass.__dict__["bil"]
            break
    assert isinstance(descriptor, property)



def test_yyk::namedelement_is_not_abstract():
    assert not inspect.isabstract(yyk::NamedElement)


def test_yyk::namedelement_constructor_exists():
    assert callable(yyk::NamedElement.__init__)


def test_yyk::namedelement_constructor_args():
    sig = inspect.signature(yyk::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yyk::namedelement_has_name():
    assert hasattr(yyk::NamedElement, "name")
    descriptor = None
    for klass in yyk::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_yyk::output_is_not_abstract():
    assert not inspect.isabstract(yyk::Output)


def test_yyk::output_constructor_exists():
    assert callable(yyk::Output.__init__)


def test_yyk::output_constructor_args():
    sig = inspect.signature(yyk::Output.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyk::output_has_id():
    assert hasattr(yyk::Output, "id")
    descriptor = None
    for klass in yyk::Output.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyk::foo_is_not_abstract():
    assert not inspect.isabstract(yyk::Foo)


def test_yyk::foo_constructor_exists():
    assert callable(yyk::Foo.__init__)


def test_yyk::foo_constructor_args():
    sig = inspect.signature(yyk::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyk::foo_has_id():
    assert hasattr(yyk::Foo, "id")
    descriptor = None
    for klass in yyk::Foo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_yyk::baz_is_not_abstract():
    assert not inspect.isabstract(yyk::Baz)


def test_yyk::baz_constructor_exists():
    assert callable(yyk::Baz.__init__)


def test_yyk::baz_constructor_args():
    sig = inspect.signature(yyk::Baz.__init__)
    params = list(sig.parameters.keys())
    assert "zig" in params, "Missing parameter 'zig'"

def test_yyk::baz_has_zig():
    assert hasattr(yyk::Baz, "zig")
    descriptor = None
    for klass in yyk::Baz.__mro__:
        if "zig" in klass.__dict__:
            descriptor = klass.__dict__["zig"]
            break
    assert isinstance(descriptor, property)



def test_yyk::relation_is_not_abstract():
    assert not inspect.isabstract(yyk::Relation)


def test_yyk::relation_constructor_exists():
    assert callable(yyk::Relation.__init__)


def test_yyk::relation_constructor_args():
    sig = inspect.signature(yyk::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyk::relation_has_since():
    assert hasattr(yyk::Relation, "since")
    descriptor = None
    for klass in yyk::Relation.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyk::zing_is_not_abstract():
    assert not inspect.isabstract(yyk::Zing)


def test_yyk::zing_constructor_exists():
    assert callable(yyk::Zing.__init__)


def test_yyk::zing_constructor_args():
    sig = inspect.signature(yyk::Zing.__init__)
    params = list(sig.parameters.keys())



def test_yyk::base_is_not_abstract():
    assert not inspect.isabstract(yyk::Base)


def test_yyk::base_constructor_exists():
    assert callable(yyk::Base.__init__)


def test_yyk::base_constructor_args():
    sig = inspect.signature(yyk::Base.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyk::base_has_id():
    assert hasattr(yyk::Base, "id")
    descriptor = None
    for klass in yyk::Base.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyk::rel_is_not_abstract():
    assert not inspect.isabstract(yyk::Rel)


def test_yyk::rel_constructor_exists():
    assert callable(yyk::Rel.__init__)


def test_yyk::rel_constructor_args():
    sig = inspect.signature(yyk::Rel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyk::rel_has_id():
    assert hasattr(yyk::Rel, "id")
    descriptor = None
    for klass in yyk::Rel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyk::bar_is_not_abstract():
    assert not inspect.isabstract(yyk::Bar)


def test_yyk::bar_constructor_exists():
    assert callable(yyk::Bar.__init__)


def test_yyk::bar_constructor_args():
    sig = inspect.signature(yyk::Bar.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyk::bar_has_id():
    assert hasattr(yyk::Bar, "id")
    descriptor = None
    for klass in yyk::Bar.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyk::alias_is_not_abstract():
    assert not inspect.isabstract(yyk::Alias)


def test_yyk::alias_constructor_exists():
    assert callable(yyk::Alias.__init__)


def test_yyk::alias_constructor_args():
    sig = inspect.signature(yyk::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyk::alias_has_id():
    assert hasattr(yyk::Alias, "id")
    descriptor = None
    for klass in yyk::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
Baz_strategy = st.builds(
    Baz,
)
yyk::Boul_strategy = st.builds(
    yyk::Boul,
    hi=
        safe_text
)
yyk::Bouz_strategy = st.builds(
    yyk::Bouz,
    bil=
        safe_text
)
yyk::NamedElement_strategy = st.builds(
    yyk::NamedElement,
    name=
        safe_text
)
yyk::Output_strategy = st.builds(
    yyk::Output,
    id=
        safe_text
)
yyk::Foo_strategy = st.builds(
    yyk::Foo,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yyk::Baz_strategy = st.builds(
    yyk::Baz,
    zig=
        safe_text
)
yyk::Relation_strategy = st.builds(
    yyk::Relation,
    since=
        safe_text
)
yyk::Zing_strategy = st.builds(
    yyk::Zing,
)
yyk::Base_strategy = st.builds(
    yyk::Base,
    id=
        st.integers()
)
yyk::Rel_strategy = st.builds(
    yyk::Rel,
    id=
        safe_text
)
yyk::Bar_strategy = st.builds(
    yyk::Bar,
    id=
        safe_text
)
yyk::Alias_strategy = st.builds(
    yyk::Alias,
    id=
        safe_text
)

@given(instance=Baz_strategy)
@settings(max_examples=50)
def test_baz_instantiation(instance):
    assert isinstance(instance, Baz)

@given(instance=yyk::Boul_strategy)
@settings(max_examples=50)
def test_yyk::boul_instantiation(instance):
    assert isinstance(instance, yyk::Boul)

@given(instance=yyk::Boul_strategy)
def test_yyk::boul_hi_type(instance):
    assert isinstance(instance.hi, str)


@given(instance=yyk::Boul_strategy)
def test_yyk::boul_hi_setter(instance):
    original = instance.hi
    instance.hi = original
    assert instance.hi == original

@given(instance=yyk::Bouz_strategy)
@settings(max_examples=50)
def test_yyk::bouz_instantiation(instance):
    assert isinstance(instance, yyk::Bouz)

@given(instance=yyk::Bouz_strategy)
def test_yyk::bouz_bil_type(instance):
    assert isinstance(instance.bil, str)


@given(instance=yyk::Bouz_strategy)
def test_yyk::bouz_bil_setter(instance):
    original = instance.bil
    instance.bil = original
    assert instance.bil == original

@given(instance=yyk::NamedElement_strategy)
@settings(max_examples=50)
def test_yyk::namedelement_instantiation(instance):
    assert isinstance(instance, yyk::NamedElement)

@given(instance=yyk::NamedElement_strategy)
def test_yyk::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yyk::NamedElement_strategy)
def test_yyk::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=yyk::Output_strategy)
@settings(max_examples=50)
def test_yyk::output_instantiation(instance):
    assert isinstance(instance, yyk::Output)

@given(instance=yyk::Output_strategy)
def test_yyk::output_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyk::Output_strategy)
def test_yyk::output_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyk::Foo_strategy)
@settings(max_examples=50)
def test_yyk::foo_instantiation(instance):
    assert isinstance(instance, yyk::Foo)

@given(instance=yyk::Foo_strategy)
def test_yyk::foo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyk::Foo_strategy)
def test_yyk::foo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yyk::Baz_strategy)
@settings(max_examples=50)
def test_yyk::baz_instantiation(instance):
    assert isinstance(instance, yyk::Baz)

@given(instance=yyk::Baz_strategy)
def test_yyk::baz_zig_type(instance):
    assert isinstance(instance.zig, str)


@given(instance=yyk::Baz_strategy)
def test_yyk::baz_zig_setter(instance):
    original = instance.zig
    instance.zig = original
    assert instance.zig == original

@given(instance=yyk::Relation_strategy)
@settings(max_examples=50)
def test_yyk::relation_instantiation(instance):
    assert isinstance(instance, yyk::Relation)

@given(instance=yyk::Relation_strategy)
def test_yyk::relation_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yyk::Relation_strategy)
def test_yyk::relation_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyk::Zing_strategy)
@settings(max_examples=50)
def test_yyk::zing_instantiation(instance):
    assert isinstance(instance, yyk::Zing)

@given(instance=yyk::Base_strategy)
@settings(max_examples=50)
def test_yyk::base_instantiation(instance):
    assert isinstance(instance, yyk::Base)

@given(instance=yyk::Base_strategy)
def test_yyk::base_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yyk::Base_strategy)
def test_yyk::base_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyk::Rel_strategy)
@settings(max_examples=50)
def test_yyk::rel_instantiation(instance):
    assert isinstance(instance, yyk::Rel)

@given(instance=yyk::Rel_strategy)
def test_yyk::rel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyk::Rel_strategy)
def test_yyk::rel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyk::Bar_strategy)
@settings(max_examples=50)
def test_yyk::bar_instantiation(instance):
    assert isinstance(instance, yyk::Bar)

@given(instance=yyk::Bar_strategy)
def test_yyk::bar_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyk::Bar_strategy)
def test_yyk::bar_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyk::Alias_strategy)
@settings(max_examples=50)
def test_yyk::alias_instantiation(instance):
    assert isinstance(instance, yyk::Alias)

@given(instance=yyk::Alias_strategy)
def test_yyk::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyk::Alias_strategy)
def test_yyk::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
