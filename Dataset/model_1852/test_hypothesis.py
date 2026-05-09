import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    message::Translation,
    message::Message,
    message::Language,
    Categorized,
    message::MessageLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_message::translation_is_not_abstract():
    assert not inspect.isabstract(message::Translation)


def test_message::translation_constructor_exists():
    assert callable(message::Translation.__init__)


def test_message::translation_constructor_args():
    sig = inspect.signature(message::Translation.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "translation" in params, "Missing parameter 'translation'"

def test_message::translation_has_uid():
    assert hasattr(message::Translation, "uid")
    descriptor = None
    for klass in message::Translation.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_message::translation_has_translation():
    assert hasattr(message::Translation, "translation")
    descriptor = None
    for klass in message::Translation.__mro__:
        if "translation" in klass.__dict__:
            descriptor = klass.__dict__["translation"]
            break
    assert isinstance(descriptor, property)



def test_message::message_is_not_abstract():
    assert not inspect.isabstract(message::Message)


def test_message::message_constructor_exists():
    assert callable(message::Message.__init__)


def test_message::message_constructor_args():
    sig = inspect.signature(message::Message.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_message::message_has_uid():
    assert hasattr(message::Message, "uid")
    descriptor = None
    for klass in message::Message.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_message::message_has_name():
    assert hasattr(message::Message, "name")
    descriptor = None
    for klass in message::Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_message::language_is_not_abstract():
    assert not inspect.isabstract(message::Language)


def test_message::language_constructor_exists():
    assert callable(message::Language.__init__)


def test_message::language_constructor_args():
    sig = inspect.signature(message::Language.__init__)
    params = list(sig.parameters.keys())
    assert "defaultLang" in params, "Missing parameter 'defaultLang'"
    assert "code" in params, "Missing parameter 'code'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "lang" in params, "Missing parameter 'lang'"

def test_message::language_has_defaultLang():
    assert hasattr(message::Language, "defaultLang")
    descriptor = None
    for klass in message::Language.__mro__:
        if "defaultLang" in klass.__dict__:
            descriptor = klass.__dict__["defaultLang"]
            break
    assert isinstance(descriptor, property)

def test_message::language_has_code():
    assert hasattr(message::Language, "code")
    descriptor = None
    for klass in message::Language.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_message::language_has_uid():
    assert hasattr(message::Language, "uid")
    descriptor = None
    for klass in message::Language.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_message::language_has_lang():
    assert hasattr(message::Language, "lang")
    descriptor = None
    for klass in message::Language.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)



def test_categorized_is_not_abstract():
    assert not inspect.isabstract(Categorized)


def test_categorized_constructor_exists():
    assert callable(Categorized.__init__)


def test_categorized_constructor_args():
    sig = inspect.signature(Categorized.__init__)
    params = list(sig.parameters.keys())



def test_message::messagelibrary_is_not_abstract():
    assert not inspect.isabstract(message::MessageLibrary)


def test_message::messagelibrary_constructor_exists():
    assert callable(message::MessageLibrary.__init__)


def test_message::messagelibrary_constructor_args():
    sig = inspect.signature(message::MessageLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"

def test_message::messagelibrary_has_uid():
    assert hasattr(message::MessageLibrary, "uid")
    descriptor = None
    for klass in message::MessageLibrary.__mro__:
        if "uid" in klass.__dict__:
            descriptor = klass.__dict__["uid"]
            break
    assert isinstance(descriptor, property)

def test_message::messagelibrary_has_name():
    assert hasattr(message::MessageLibrary, "name")
    descriptor = None
    for klass in message::MessageLibrary.__mro__:
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
message::Translation_strategy = st.builds(
    message::Translation,
    uid=
        safe_text,
    translation=
        safe_text
)
message::Message_strategy = st.builds(
    message::Message,
    uid=
        safe_text,
    name=
        safe_text
)
message::Language_strategy = st.builds(
    message::Language,
    defaultLang=
        st.booleans(),
    code=
        safe_text,
    uid=
        safe_text,
    lang=
        safe_text
)
Categorized_strategy = st.builds(
    Categorized,
)
message::MessageLibrary_strategy = st.builds(
    message::MessageLibrary,
    uid=
        safe_text,
    name=
        safe_text
)

@given(instance=message::Translation_strategy)
@settings(max_examples=50)
def test_message::translation_instantiation(instance):
    assert isinstance(instance, message::Translation)

@given(instance=message::Translation_strategy)
def test_message::translation_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=message::Translation_strategy)
def test_message::translation_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=message::Translation_strategy)
def test_message::translation_translation_type(instance):
    assert isinstance(instance.translation, str)


@given(instance=message::Translation_strategy)
def test_message::translation_translation_setter(instance):
    original = instance.translation
    instance.translation = original
    assert instance.translation == original

@given(instance=message::Message_strategy)
@settings(max_examples=50)
def test_message::message_instantiation(instance):
    assert isinstance(instance, message::Message)

@given(instance=message::Message_strategy)
def test_message::message_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=message::Message_strategy)
def test_message::message_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=message::Message_strategy)
def test_message::message_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=message::Message_strategy)
def test_message::message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=message::Language_strategy)
@settings(max_examples=50)
def test_message::language_instantiation(instance):
    assert isinstance(instance, message::Language)

@given(instance=message::Language_strategy)
def test_message::language_defaultLang_type(instance):
    assert isinstance(instance.defaultLang, bool)


@given(instance=message::Language_strategy)
def test_message::language_defaultLang_setter(instance):
    original = instance.defaultLang
    instance.defaultLang = original
    assert instance.defaultLang == original

@given(instance=message::Language_strategy)
def test_message::language_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=message::Language_strategy)
def test_message::language_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=message::Language_strategy)
def test_message::language_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=message::Language_strategy)
def test_message::language_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=message::Language_strategy)
def test_message::language_lang_type(instance):
    assert isinstance(instance.lang, str)


@given(instance=message::Language_strategy)
def test_message::language_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=Categorized_strategy)
@settings(max_examples=50)
def test_categorized_instantiation(instance):
    assert isinstance(instance, Categorized)

@given(instance=message::MessageLibrary_strategy)
@settings(max_examples=50)
def test_message::messagelibrary_instantiation(instance):
    assert isinstance(instance, message::MessageLibrary)

@given(instance=message::MessageLibrary_strategy)
def test_message::messagelibrary_uid_type(instance):
    assert isinstance(instance.uid, str)


@given(instance=message::MessageLibrary_strategy)
def test_message::messagelibrary_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original

@given(instance=message::MessageLibrary_strategy)
def test_message::messagelibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=message::MessageLibrary_strategy)
def test_message::messagelibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
