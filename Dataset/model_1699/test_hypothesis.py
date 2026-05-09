import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Baz,
    yyg::Boul,
    yyg::Bouz,
    yyg::Rel,
    yyg::Bar,
    yyg::Alias,
    yyg::NamedElement,
    yyg::Output,
    yyg::Foo,
    NamedElement,
    yyg::Boz,
    yyg::Zing,
    yyg::Baz,
    yyg::Base,
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



def test_yyg::boul_is_not_abstract():
    assert not inspect.isabstract(yyg::Boul)


def test_yyg::boul_constructor_exists():
    assert callable(yyg::Boul.__init__)


def test_yyg::boul_constructor_args():
    sig = inspect.signature(yyg::Boul.__init__)
    params = list(sig.parameters.keys())
    assert "hi" in params, "Missing parameter 'hi'"

def test_yyg::boul_has_hi():
    assert hasattr(yyg::Boul, "hi")
    descriptor = None
    for klass in yyg::Boul.__mro__:
        if "hi" in klass.__dict__:
            descriptor = klass.__dict__["hi"]
            break
    assert isinstance(descriptor, property)



def test_yyg::bouz_is_not_abstract():
    assert not inspect.isabstract(yyg::Bouz)


def test_yyg::bouz_constructor_exists():
    assert callable(yyg::Bouz.__init__)


def test_yyg::bouz_constructor_args():
    sig = inspect.signature(yyg::Bouz.__init__)
    params = list(sig.parameters.keys())
    assert "bil" in params, "Missing parameter 'bil'"

def test_yyg::bouz_has_bil():
    assert hasattr(yyg::Bouz, "bil")
    descriptor = None
    for klass in yyg::Bouz.__mro__:
        if "bil" in klass.__dict__:
            descriptor = klass.__dict__["bil"]
            break
    assert isinstance(descriptor, property)



def test_yyg::rel_is_not_abstract():
    assert not inspect.isabstract(yyg::Rel)


def test_yyg::rel_constructor_exists():
    assert callable(yyg::Rel.__init__)


def test_yyg::rel_constructor_args():
    sig = inspect.signature(yyg::Rel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyg::rel_has_id():
    assert hasattr(yyg::Rel, "id")
    descriptor = None
    for klass in yyg::Rel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyg::bar_is_not_abstract():
    assert not inspect.isabstract(yyg::Bar)


def test_yyg::bar_constructor_exists():
    assert callable(yyg::Bar.__init__)


def test_yyg::bar_constructor_args():
    sig = inspect.signature(yyg::Bar.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyg::bar_has_id():
    assert hasattr(yyg::Bar, "id")
    descriptor = None
    for klass in yyg::Bar.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyg::alias_is_not_abstract():
    assert not inspect.isabstract(yyg::Alias)


def test_yyg::alias_constructor_exists():
    assert callable(yyg::Alias.__init__)


def test_yyg::alias_constructor_args():
    sig = inspect.signature(yyg::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyg::alias_has_id():
    assert hasattr(yyg::Alias, "id")
    descriptor = None
    for klass in yyg::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyg::namedelement_is_not_abstract():
    assert not inspect.isabstract(yyg::NamedElement)


def test_yyg::namedelement_constructor_exists():
    assert callable(yyg::NamedElement.__init__)


def test_yyg::namedelement_constructor_args():
    sig = inspect.signature(yyg::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yyg::namedelement_has_name():
    assert hasattr(yyg::NamedElement, "name")
    descriptor = None
    for klass in yyg::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_yyg::output_is_not_abstract():
    assert not inspect.isabstract(yyg::Output)


def test_yyg::output_constructor_exists():
    assert callable(yyg::Output.__init__)


def test_yyg::output_constructor_args():
    sig = inspect.signature(yyg::Output.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyg::output_has_id():
    assert hasattr(yyg::Output, "id")
    descriptor = None
    for klass in yyg::Output.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyg::foo_is_not_abstract():
    assert not inspect.isabstract(yyg::Foo)


def test_yyg::foo_constructor_exists():
    assert callable(yyg::Foo.__init__)


def test_yyg::foo_constructor_args():
    sig = inspect.signature(yyg::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyg::foo_has_id():
    assert hasattr(yyg::Foo, "id")
    descriptor = None
    for klass in yyg::Foo.__mro__:
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



def test_yyg::boz_is_not_abstract():
    assert not inspect.isabstract(yyg::Boz)


def test_yyg::boz_constructor_exists():
    assert callable(yyg::Boz.__init__)


def test_yyg::boz_constructor_args():
    sig = inspect.signature(yyg::Boz.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyg::boz_has_since():
    assert hasattr(yyg::Boz, "since")
    descriptor = None
    for klass in yyg::Boz.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyg::zing_is_not_abstract():
    assert not inspect.isabstract(yyg::Zing)


def test_yyg::zing_constructor_exists():
    assert callable(yyg::Zing.__init__)


def test_yyg::zing_constructor_args():
    sig = inspect.signature(yyg::Zing.__init__)
    params = list(sig.parameters.keys())



def test_yyg::baz_is_not_abstract():
    assert not inspect.isabstract(yyg::Baz)


def test_yyg::baz_constructor_exists():
    assert callable(yyg::Baz.__init__)


def test_yyg::baz_constructor_args():
    sig = inspect.signature(yyg::Baz.__init__)
    params = list(sig.parameters.keys())
    assert "zig" in params, "Missing parameter 'zig'"

def test_yyg::baz_has_zig():
    assert hasattr(yyg::Baz, "zig")
    descriptor = None
    for klass in yyg::Baz.__mro__:
        if "zig" in klass.__dict__:
            descriptor = klass.__dict__["zig"]
            break
    assert isinstance(descriptor, property)



def test_yyg::base_is_not_abstract():
    assert not inspect.isabstract(yyg::Base)


def test_yyg::base_constructor_exists():
    assert callable(yyg::Base.__init__)


def test_yyg::base_constructor_args():
    sig = inspect.signature(yyg::Base.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyg::base_has_id():
    assert hasattr(yyg::Base, "id")
    descriptor = None
    for klass in yyg::Base.__mro__:
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
yyg::Boul_strategy = st.builds(
    yyg::Boul,
    hi=
        safe_text
)
yyg::Bouz_strategy = st.builds(
    yyg::Bouz,
    bil=
        safe_text
)
yyg::Rel_strategy = st.builds(
    yyg::Rel,
    id=
        safe_text
)
yyg::Bar_strategy = st.builds(
    yyg::Bar,
    id=
        safe_text
)
yyg::Alias_strategy = st.builds(
    yyg::Alias,
    id=
        safe_text
)
yyg::NamedElement_strategy = st.builds(
    yyg::NamedElement,
    name=
        safe_text
)
yyg::Output_strategy = st.builds(
    yyg::Output,
    id=
        safe_text
)
yyg::Foo_strategy = st.builds(
    yyg::Foo,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yyg::Boz_strategy = st.builds(
    yyg::Boz,
    since=
        safe_text
)
yyg::Zing_strategy = st.builds(
    yyg::Zing,
)
yyg::Baz_strategy = st.builds(
    yyg::Baz,
    zig=
        safe_text
)
yyg::Base_strategy = st.builds(
    yyg::Base,
    id=
        st.integers()
)

@given(instance=Baz_strategy)
@settings(max_examples=50)
def test_baz_instantiation(instance):
    assert isinstance(instance, Baz)

@given(instance=yyg::Boul_strategy)
@settings(max_examples=50)
def test_yyg::boul_instantiation(instance):
    assert isinstance(instance, yyg::Boul)

@given(instance=yyg::Boul_strategy)
def test_yyg::boul_hi_type(instance):
    assert isinstance(instance.hi, str)


@given(instance=yyg::Boul_strategy)
def test_yyg::boul_hi_setter(instance):
    original = instance.hi
    instance.hi = original
    assert instance.hi == original

@given(instance=yyg::Bouz_strategy)
@settings(max_examples=50)
def test_yyg::bouz_instantiation(instance):
    assert isinstance(instance, yyg::Bouz)

@given(instance=yyg::Bouz_strategy)
def test_yyg::bouz_bil_type(instance):
    assert isinstance(instance.bil, str)


@given(instance=yyg::Bouz_strategy)
def test_yyg::bouz_bil_setter(instance):
    original = instance.bil
    instance.bil = original
    assert instance.bil == original

@given(instance=yyg::Rel_strategy)
@settings(max_examples=50)
def test_yyg::rel_instantiation(instance):
    assert isinstance(instance, yyg::Rel)

@given(instance=yyg::Rel_strategy)
def test_yyg::rel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyg::Rel_strategy)
def test_yyg::rel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyg::Bar_strategy)
@settings(max_examples=50)
def test_yyg::bar_instantiation(instance):
    assert isinstance(instance, yyg::Bar)

@given(instance=yyg::Bar_strategy)
def test_yyg::bar_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyg::Bar_strategy)
def test_yyg::bar_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyg::Alias_strategy)
@settings(max_examples=50)
def test_yyg::alias_instantiation(instance):
    assert isinstance(instance, yyg::Alias)

@given(instance=yyg::Alias_strategy)
def test_yyg::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyg::Alias_strategy)
def test_yyg::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyg::NamedElement_strategy)
@settings(max_examples=50)
def test_yyg::namedelement_instantiation(instance):
    assert isinstance(instance, yyg::NamedElement)

@given(instance=yyg::NamedElement_strategy)
def test_yyg::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yyg::NamedElement_strategy)
def test_yyg::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=yyg::Output_strategy)
@settings(max_examples=50)
def test_yyg::output_instantiation(instance):
    assert isinstance(instance, yyg::Output)

@given(instance=yyg::Output_strategy)
def test_yyg::output_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyg::Output_strategy)
def test_yyg::output_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyg::Foo_strategy)
@settings(max_examples=50)
def test_yyg::foo_instantiation(instance):
    assert isinstance(instance, yyg::Foo)

@given(instance=yyg::Foo_strategy)
def test_yyg::foo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyg::Foo_strategy)
def test_yyg::foo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yyg::Boz_strategy)
@settings(max_examples=50)
def test_yyg::boz_instantiation(instance):
    assert isinstance(instance, yyg::Boz)

@given(instance=yyg::Boz_strategy)
def test_yyg::boz_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yyg::Boz_strategy)
def test_yyg::boz_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyg::Zing_strategy)
@settings(max_examples=50)
def test_yyg::zing_instantiation(instance):
    assert isinstance(instance, yyg::Zing)

@given(instance=yyg::Baz_strategy)
@settings(max_examples=50)
def test_yyg::baz_instantiation(instance):
    assert isinstance(instance, yyg::Baz)

@given(instance=yyg::Baz_strategy)
def test_yyg::baz_zig_type(instance):
    assert isinstance(instance.zig, str)


@given(instance=yyg::Baz_strategy)
def test_yyg::baz_zig_setter(instance):
    original = instance.zig
    instance.zig = original
    assert instance.zig == original

@given(instance=yyg::Base_strategy)
@settings(max_examples=50)
def test_yyg::base_instantiation(instance):
    assert isinstance(instance, yyg::Base)

@given(instance=yyg::Base_strategy)
def test_yyg::base_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yyg::Base_strategy)
def test_yyg::base_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
