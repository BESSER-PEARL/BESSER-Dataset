import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    Comment,
    Make::Makefile,
    Make::Dependency,
    Make::Comment,
    Rule,
    Make::ShellLine,
    Make::Macro,
    ShellLine,
    Dependency,
    Make::RuleDep,
    Make::FileDep,
    Make::Rule,
    Make::Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_make::makefile_is_not_abstract():
    assert not inspect.isabstract(Make::Makefile)


def test_make::makefile_constructor_exists():
    assert callable(Make::Makefile.__init__)


def test_make::makefile_constructor_args():
    sig = inspect.signature(Make::Makefile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_make::makefile_has_name():
    assert hasattr(Make::Makefile, "name")
    descriptor = None
    for klass in Make::Makefile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_make::dependency_is_not_abstract():
    assert not inspect.isabstract(Make::Dependency)


def test_make::dependency_constructor_exists():
    assert callable(Make::Dependency.__init__)


def test_make::dependency_constructor_args():
    sig = inspect.signature(Make::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_make::comment_is_not_abstract():
    assert not inspect.isabstract(Make::Comment)


def test_make::comment_constructor_exists():
    assert callable(Make::Comment.__init__)


def test_make::comment_constructor_args():
    sig = inspect.signature(Make::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_make::comment_has_text():
    assert hasattr(Make::Comment, "text")
    descriptor = None
    for klass in Make::Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_make::shellline_is_not_abstract():
    assert not inspect.isabstract(Make::ShellLine)


def test_make::shellline_constructor_exists():
    assert callable(Make::ShellLine.__init__)


def test_make::shellline_constructor_args():
    sig = inspect.signature(Make::ShellLine.__init__)
    params = list(sig.parameters.keys())
    assert "display" in params, "Missing parameter 'display'"
    assert "command" in params, "Missing parameter 'command'"

def test_make::shellline_has_display():
    assert hasattr(Make::ShellLine, "display")
    descriptor = None
    for klass in Make::ShellLine.__mro__:
        if "display" in klass.__dict__:
            descriptor = klass.__dict__["display"]
            break
    assert isinstance(descriptor, property)

def test_make::shellline_has_command():
    assert hasattr(Make::ShellLine, "command")
    descriptor = None
    for klass in Make::ShellLine.__mro__:
        if "command" in klass.__dict__:
            descriptor = klass.__dict__["command"]
            break
    assert isinstance(descriptor, property)



def test_make::macro_is_not_abstract():
    assert not inspect.isabstract(Make::Macro)


def test_make::macro_constructor_exists():
    assert callable(Make::Macro.__init__)


def test_make::macro_constructor_args():
    sig = inspect.signature(Make::Macro.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_make::macro_has_value():
    assert hasattr(Make::Macro, "value")
    descriptor = None
    for klass in Make::Macro.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_shellline_is_not_abstract():
    assert not inspect.isabstract(ShellLine)


def test_shellline_constructor_exists():
    assert callable(ShellLine.__init__)


def test_shellline_constructor_args():
    sig = inspect.signature(ShellLine.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_make::ruledep_is_not_abstract():
    assert not inspect.isabstract(Make::RuleDep)


def test_make::ruledep_constructor_exists():
    assert callable(Make::RuleDep.__init__)


def test_make::ruledep_constructor_args():
    sig = inspect.signature(Make::RuleDep.__init__)
    params = list(sig.parameters.keys())



def test_make::filedep_is_not_abstract():
    assert not inspect.isabstract(Make::FileDep)


def test_make::filedep_constructor_exists():
    assert callable(Make::FileDep.__init__)


def test_make::filedep_constructor_args():
    sig = inspect.signature(Make::FileDep.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_make::filedep_has_name():
    assert hasattr(Make::FileDep, "name")
    descriptor = None
    for klass in Make::FileDep.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_make::rule_is_not_abstract():
    assert not inspect.isabstract(Make::Rule)


def test_make::rule_constructor_exists():
    assert callable(Make::Rule.__init__)


def test_make::rule_constructor_args():
    sig = inspect.signature(Make::Rule.__init__)
    params = list(sig.parameters.keys())



def test_make::element_is_not_abstract():
    assert not inspect.isabstract(Make::Element)


def test_make::element_constructor_exists():
    assert callable(Make::Element.__init__)


def test_make::element_constructor_args():
    sig = inspect.signature(Make::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_make::element_has_name():
    assert hasattr(Make::Element, "name")
    descriptor = None
    for klass in Make::Element.__mro__:
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
Element_strategy = st.builds(
    Element,
)
Comment_strategy = st.builds(
    Comment,
)
Make::Makefile_strategy = st.builds(
    Make::Makefile,
    name=
        safe_text
)
Make::Dependency_strategy = st.builds(
    Make::Dependency,
)
Make::Comment_strategy = st.builds(
    Make::Comment,
    text=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
Make::ShellLine_strategy = st.builds(
    Make::ShellLine,
    display=
        safe_text,
    command=
        safe_text
)
Make::Macro_strategy = st.builds(
    Make::Macro,
    value=
        safe_text
)
ShellLine_strategy = st.builds(
    ShellLine,
)
Dependency_strategy = st.builds(
    Dependency,
)
Make::RuleDep_strategy = st.builds(
    Make::RuleDep,
)
Make::FileDep_strategy = st.builds(
    Make::FileDep,
    name=
        safe_text
)
Make::Rule_strategy = st.builds(
    Make::Rule,
)
Make::Element_strategy = st.builds(
    Make::Element,
    name=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Make::Makefile_strategy)
@settings(max_examples=50)
def test_make::makefile_instantiation(instance):
    assert isinstance(instance, Make::Makefile)

@given(instance=Make::Makefile_strategy)
def test_make::makefile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Make::Makefile_strategy)
def test_make::makefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Make::Dependency_strategy)
@settings(max_examples=50)
def test_make::dependency_instantiation(instance):
    assert isinstance(instance, Make::Dependency)

@given(instance=Make::Comment_strategy)
@settings(max_examples=50)
def test_make::comment_instantiation(instance):
    assert isinstance(instance, Make::Comment)

@given(instance=Make::Comment_strategy)
def test_make::comment_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=Make::Comment_strategy)
def test_make::comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=Make::ShellLine_strategy)
@settings(max_examples=50)
def test_make::shellline_instantiation(instance):
    assert isinstance(instance, Make::ShellLine)

@given(instance=Make::ShellLine_strategy)
def test_make::shellline_display_type(instance):
    assert isinstance(instance.display, str)


@given(instance=Make::ShellLine_strategy)
def test_make::shellline_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original

@given(instance=Make::ShellLine_strategy)
def test_make::shellline_command_type(instance):
    assert isinstance(instance.command, str)


@given(instance=Make::ShellLine_strategy)
def test_make::shellline_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original

@given(instance=Make::Macro_strategy)
@settings(max_examples=50)
def test_make::macro_instantiation(instance):
    assert isinstance(instance, Make::Macro)

@given(instance=Make::Macro_strategy)
def test_make::macro_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Make::Macro_strategy)
def test_make::macro_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ShellLine_strategy)
@settings(max_examples=50)
def test_shellline_instantiation(instance):
    assert isinstance(instance, ShellLine)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=Make::RuleDep_strategy)
@settings(max_examples=50)
def test_make::ruledep_instantiation(instance):
    assert isinstance(instance, Make::RuleDep)

@given(instance=Make::FileDep_strategy)
@settings(max_examples=50)
def test_make::filedep_instantiation(instance):
    assert isinstance(instance, Make::FileDep)

@given(instance=Make::FileDep_strategy)
def test_make::filedep_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Make::FileDep_strategy)
def test_make::filedep_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Make::Rule_strategy)
@settings(max_examples=50)
def test_make::rule_instantiation(instance):
    assert isinstance(instance, Make::Rule)

@given(instance=Make::Element_strategy)
@settings(max_examples=50)
def test_make::element_instantiation(instance):
    assert isinstance(instance, Make::Element)

@given(instance=Make::Element_strategy)
def test_make::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Make::Element_strategy)
def test_make::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
