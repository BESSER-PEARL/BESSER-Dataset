import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Baz,
    yyh::Boul,
    yyh::Bouz,
    yyh::Foo,
    yyh::Rel,
    yyh::Bar,
    yyh::Alias,
    yyh::NamedElement,
    yyh::Output,
    NamedElement,
    yyh::Baz,
    yyh::Boz,
    yyh::Zing,
    yyh::Base,
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



def test_yyh::boul_is_not_abstract():
    assert not inspect.isabstract(yyh::Boul)


def test_yyh::boul_constructor_exists():
    assert callable(yyh::Boul.__init__)


def test_yyh::boul_constructor_args():
    sig = inspect.signature(yyh::Boul.__init__)
    params = list(sig.parameters.keys())
    assert "hi" in params, "Missing parameter 'hi'"

def test_yyh::boul_has_hi():
    assert hasattr(yyh::Boul, "hi")
    descriptor = None
    for klass in yyh::Boul.__mro__:
        if "hi" in klass.__dict__:
            descriptor = klass.__dict__["hi"]
            break
    assert isinstance(descriptor, property)



def test_yyh::bouz_is_not_abstract():
    assert not inspect.isabstract(yyh::Bouz)


def test_yyh::bouz_constructor_exists():
    assert callable(yyh::Bouz.__init__)


def test_yyh::bouz_constructor_args():
    sig = inspect.signature(yyh::Bouz.__init__)
    params = list(sig.parameters.keys())
    assert "bil" in params, "Missing parameter 'bil'"

def test_yyh::bouz_has_bil():
    assert hasattr(yyh::Bouz, "bil")
    descriptor = None
    for klass in yyh::Bouz.__mro__:
        if "bil" in klass.__dict__:
            descriptor = klass.__dict__["bil"]
            break
    assert isinstance(descriptor, property)



def test_yyh::foo_is_not_abstract():
    assert not inspect.isabstract(yyh::Foo)


def test_yyh::foo_constructor_exists():
    assert callable(yyh::Foo.__init__)


def test_yyh::foo_constructor_args():
    sig = inspect.signature(yyh::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyh::foo_has_id():
    assert hasattr(yyh::Foo, "id")
    descriptor = None
    for klass in yyh::Foo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyh::rel_is_not_abstract():
    assert not inspect.isabstract(yyh::Rel)


def test_yyh::rel_constructor_exists():
    assert callable(yyh::Rel.__init__)


def test_yyh::rel_constructor_args():
    sig = inspect.signature(yyh::Rel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyh::rel_has_id():
    assert hasattr(yyh::Rel, "id")
    descriptor = None
    for klass in yyh::Rel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyh::bar_is_not_abstract():
    assert not inspect.isabstract(yyh::Bar)


def test_yyh::bar_constructor_exists():
    assert callable(yyh::Bar.__init__)


def test_yyh::bar_constructor_args():
    sig = inspect.signature(yyh::Bar.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyh::bar_has_id():
    assert hasattr(yyh::Bar, "id")
    descriptor = None
    for klass in yyh::Bar.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyh::alias_is_not_abstract():
    assert not inspect.isabstract(yyh::Alias)


def test_yyh::alias_constructor_exists():
    assert callable(yyh::Alias.__init__)


def test_yyh::alias_constructor_args():
    sig = inspect.signature(yyh::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyh::alias_has_id():
    assert hasattr(yyh::Alias, "id")
    descriptor = None
    for klass in yyh::Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyh::namedelement_is_not_abstract():
    assert not inspect.isabstract(yyh::NamedElement)


def test_yyh::namedelement_constructor_exists():
    assert callable(yyh::NamedElement.__init__)


def test_yyh::namedelement_constructor_args():
    sig = inspect.signature(yyh::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yyh::namedelement_has_name():
    assert hasattr(yyh::NamedElement, "name")
    descriptor = None
    for klass in yyh::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_yyh::output_is_not_abstract():
    assert not inspect.isabstract(yyh::Output)


def test_yyh::output_constructor_exists():
    assert callable(yyh::Output.__init__)


def test_yyh::output_constructor_args():
    sig = inspect.signature(yyh::Output.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyh::output_has_id():
    assert hasattr(yyh::Output, "id")
    descriptor = None
    for klass in yyh::Output.__mro__:
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



def test_yyh::baz_is_not_abstract():
    assert not inspect.isabstract(yyh::Baz)


def test_yyh::baz_constructor_exists():
    assert callable(yyh::Baz.__init__)


def test_yyh::baz_constructor_args():
    sig = inspect.signature(yyh::Baz.__init__)
    params = list(sig.parameters.keys())
    assert "zig" in params, "Missing parameter 'zig'"

def test_yyh::baz_has_zig():
    assert hasattr(yyh::Baz, "zig")
    descriptor = None
    for klass in yyh::Baz.__mro__:
        if "zig" in klass.__dict__:
            descriptor = klass.__dict__["zig"]
            break
    assert isinstance(descriptor, property)



def test_yyh::boz_is_not_abstract():
    assert not inspect.isabstract(yyh::Boz)


def test_yyh::boz_constructor_exists():
    assert callable(yyh::Boz.__init__)


def test_yyh::boz_constructor_args():
    sig = inspect.signature(yyh::Boz.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyh::boz_has_since():
    assert hasattr(yyh::Boz, "since")
    descriptor = None
    for klass in yyh::Boz.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyh::zing_is_not_abstract():
    assert not inspect.isabstract(yyh::Zing)


def test_yyh::zing_constructor_exists():
    assert callable(yyh::Zing.__init__)


def test_yyh::zing_constructor_args():
    sig = inspect.signature(yyh::Zing.__init__)
    params = list(sig.parameters.keys())



def test_yyh::base_is_not_abstract():
    assert not inspect.isabstract(yyh::Base)


def test_yyh::base_constructor_exists():
    assert callable(yyh::Base.__init__)


def test_yyh::base_constructor_args():
    sig = inspect.signature(yyh::Base.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyh::base_has_id():
    assert hasattr(yyh::Base, "id")
    descriptor = None
    for klass in yyh::Base.__mro__:
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
yyh::Boul_strategy = st.builds(
    yyh::Boul,
    hi=
        safe_text
)
yyh::Bouz_strategy = st.builds(
    yyh::Bouz,
    bil=
        safe_text
)
yyh::Foo_strategy = st.builds(
    yyh::Foo,
    id=
        safe_text
)
yyh::Rel_strategy = st.builds(
    yyh::Rel,
    id=
        safe_text
)
yyh::Bar_strategy = st.builds(
    yyh::Bar,
    id=
        safe_text
)
yyh::Alias_strategy = st.builds(
    yyh::Alias,
    id=
        safe_text
)
yyh::NamedElement_strategy = st.builds(
    yyh::NamedElement,
    name=
        safe_text
)
yyh::Output_strategy = st.builds(
    yyh::Output,
    id=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yyh::Baz_strategy = st.builds(
    yyh::Baz,
    zig=
        safe_text
)
yyh::Boz_strategy = st.builds(
    yyh::Boz,
    since=
        safe_text
)
yyh::Zing_strategy = st.builds(
    yyh::Zing,
)
yyh::Base_strategy = st.builds(
    yyh::Base,
    id=
        st.integers()
)

@given(instance=Baz_strategy)
@settings(max_examples=50)
def test_baz_instantiation(instance):
    assert isinstance(instance, Baz)

@given(instance=yyh::Boul_strategy)
@settings(max_examples=50)
def test_yyh::boul_instantiation(instance):
    assert isinstance(instance, yyh::Boul)

@given(instance=yyh::Boul_strategy)
def test_yyh::boul_hi_type(instance):
    assert isinstance(instance.hi, str)


@given(instance=yyh::Boul_strategy)
def test_yyh::boul_hi_setter(instance):
    original = instance.hi
    instance.hi = original
    assert instance.hi == original

@given(instance=yyh::Bouz_strategy)
@settings(max_examples=50)
def test_yyh::bouz_instantiation(instance):
    assert isinstance(instance, yyh::Bouz)

@given(instance=yyh::Bouz_strategy)
def test_yyh::bouz_bil_type(instance):
    assert isinstance(instance.bil, str)


@given(instance=yyh::Bouz_strategy)
def test_yyh::bouz_bil_setter(instance):
    original = instance.bil
    instance.bil = original
    assert instance.bil == original

@given(instance=yyh::Foo_strategy)
@settings(max_examples=50)
def test_yyh::foo_instantiation(instance):
    assert isinstance(instance, yyh::Foo)

@given(instance=yyh::Foo_strategy)
def test_yyh::foo_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyh::Foo_strategy)
def test_yyh::foo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyh::Rel_strategy)
@settings(max_examples=50)
def test_yyh::rel_instantiation(instance):
    assert isinstance(instance, yyh::Rel)

@given(instance=yyh::Rel_strategy)
def test_yyh::rel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyh::Rel_strategy)
def test_yyh::rel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyh::Bar_strategy)
@settings(max_examples=50)
def test_yyh::bar_instantiation(instance):
    assert isinstance(instance, yyh::Bar)

@given(instance=yyh::Bar_strategy)
def test_yyh::bar_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyh::Bar_strategy)
def test_yyh::bar_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyh::Alias_strategy)
@settings(max_examples=50)
def test_yyh::alias_instantiation(instance):
    assert isinstance(instance, yyh::Alias)

@given(instance=yyh::Alias_strategy)
def test_yyh::alias_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyh::Alias_strategy)
def test_yyh::alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyh::NamedElement_strategy)
@settings(max_examples=50)
def test_yyh::namedelement_instantiation(instance):
    assert isinstance(instance, yyh::NamedElement)

@given(instance=yyh::NamedElement_strategy)
def test_yyh::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yyh::NamedElement_strategy)
def test_yyh::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=yyh::Output_strategy)
@settings(max_examples=50)
def test_yyh::output_instantiation(instance):
    assert isinstance(instance, yyh::Output)

@given(instance=yyh::Output_strategy)
def test_yyh::output_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=yyh::Output_strategy)
def test_yyh::output_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yyh::Baz_strategy)
@settings(max_examples=50)
def test_yyh::baz_instantiation(instance):
    assert isinstance(instance, yyh::Baz)

@given(instance=yyh::Baz_strategy)
def test_yyh::baz_zig_type(instance):
    assert isinstance(instance.zig, str)


@given(instance=yyh::Baz_strategy)
def test_yyh::baz_zig_setter(instance):
    original = instance.zig
    instance.zig = original
    assert instance.zig == original

@given(instance=yyh::Boz_strategy)
@settings(max_examples=50)
def test_yyh::boz_instantiation(instance):
    assert isinstance(instance, yyh::Boz)

@given(instance=yyh::Boz_strategy)
def test_yyh::boz_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=yyh::Boz_strategy)
def test_yyh::boz_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyh::Zing_strategy)
@settings(max_examples=50)
def test_yyh::zing_instantiation(instance):
    assert isinstance(instance, yyh::Zing)

@given(instance=yyh::Base_strategy)
@settings(max_examples=50)
def test_yyh::base_instantiation(instance):
    assert isinstance(instance, yyh::Base)

@given(instance=yyh::Base_strategy)
def test_yyh::base_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=yyh::Base_strategy)
def test_yyh::base_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
