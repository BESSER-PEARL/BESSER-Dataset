import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    Comment,
    Make_Makefile,
    Make_Dependency,
    Make_Comment,
    Rule,
    Make_ShellLine,
    Make_Macro,
    ShellLine,
    Dependency,
    Make_FileDep,
    Make_RuleDep,
    Make_Rule,
    Make_Element,
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



def test_make_makefile_is_not_abstract():
    assert not inspect.isabstract(Make_Makefile)


def test_make_makefile_constructor_exists():
    assert callable(Make_Makefile.__init__)


def test_make_makefile_constructor_args():
    sig = inspect.signature(Make_Makefile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_make_makefile_has_name():
    assert hasattr(Make_Makefile, "name")
    descriptor = None
    for klass in Make_Makefile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_make_dependency_is_not_abstract():
    assert not inspect.isabstract(Make_Dependency)


def test_make_dependency_constructor_exists():
    assert callable(Make_Dependency.__init__)


def test_make_dependency_constructor_args():
    sig = inspect.signature(Make_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_make_comment_is_not_abstract():
    assert not inspect.isabstract(Make_Comment)


def test_make_comment_constructor_exists():
    assert callable(Make_Comment.__init__)


def test_make_comment_constructor_args():
    sig = inspect.signature(Make_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_make_comment_has_text():
    assert hasattr(Make_Comment, "text")
    descriptor = None
    for klass in Make_Comment.__mro__:
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



def test_make_shellline_is_not_abstract():
    assert not inspect.isabstract(Make_ShellLine)


def test_make_shellline_constructor_exists():
    assert callable(Make_ShellLine.__init__)


def test_make_shellline_constructor_args():
    sig = inspect.signature(Make_ShellLine.__init__)
    params = list(sig.parameters.keys())
    assert "display" in params, "Missing parameter 'display'"
    assert "command" in params, "Missing parameter 'command'"

def test_make_shellline_has_display():
    assert hasattr(Make_ShellLine, "display")
    descriptor = None
    for klass in Make_ShellLine.__mro__:
        if "display" in klass.__dict__:
            descriptor = klass.__dict__["display"]
            break
    assert isinstance(descriptor, property)

def test_make_shellline_has_command():
    assert hasattr(Make_ShellLine, "command")
    descriptor = None
    for klass in Make_ShellLine.__mro__:
        if "command" in klass.__dict__:
            descriptor = klass.__dict__["command"]
            break
    assert isinstance(descriptor, property)



def test_make_macro_is_not_abstract():
    assert not inspect.isabstract(Make_Macro)


def test_make_macro_constructor_exists():
    assert callable(Make_Macro.__init__)


def test_make_macro_constructor_args():
    sig = inspect.signature(Make_Macro.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_make_macro_has_value():
    assert hasattr(Make_Macro, "value")
    descriptor = None
    for klass in Make_Macro.__mro__:
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



def test_make_filedep_is_not_abstract():
    assert not inspect.isabstract(Make_FileDep)


def test_make_filedep_constructor_exists():
    assert callable(Make_FileDep.__init__)


def test_make_filedep_constructor_args():
    sig = inspect.signature(Make_FileDep.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_make_filedep_has_name():
    assert hasattr(Make_FileDep, "name")
    descriptor = None
    for klass in Make_FileDep.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_make_ruledep_is_not_abstract():
    assert not inspect.isabstract(Make_RuleDep)


def test_make_ruledep_constructor_exists():
    assert callable(Make_RuleDep.__init__)


def test_make_ruledep_constructor_args():
    sig = inspect.signature(Make_RuleDep.__init__)
    params = list(sig.parameters.keys())



def test_make_rule_is_not_abstract():
    assert not inspect.isabstract(Make_Rule)


def test_make_rule_constructor_exists():
    assert callable(Make_Rule.__init__)


def test_make_rule_constructor_args():
    sig = inspect.signature(Make_Rule.__init__)
    params = list(sig.parameters.keys())



def test_make_element_is_not_abstract():
    assert not inspect.isabstract(Make_Element)


def test_make_element_constructor_exists():
    assert callable(Make_Element.__init__)


def test_make_element_constructor_args():
    sig = inspect.signature(Make_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_make_element_has_name():
    assert hasattr(Make_Element, "name")
    descriptor = None
    for klass in Make_Element.__mro__:
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
Make_Makefile_strategy = st.builds(
    Make_Makefile,
    name=
        safe_text
)
Make_Dependency_strategy = st.builds(
    Make_Dependency,
)
Make_Comment_strategy = st.builds(
    Make_Comment,
    text=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
Make_ShellLine_strategy = st.builds(
    Make_ShellLine,
    display=
        safe_text,
    command=
        safe_text
)
Make_Macro_strategy = st.builds(
    Make_Macro,
    value=
        safe_text
)
ShellLine_strategy = st.builds(
    ShellLine,
)
Dependency_strategy = st.builds(
    Dependency,
)
Make_FileDep_strategy = st.builds(
    Make_FileDep,
    name=
        safe_text
)
Make_RuleDep_strategy = st.builds(
    Make_RuleDep,
)
Make_Rule_strategy = st.builds(
    Make_Rule,
)
Make_Element_strategy = st.builds(
    Make_Element,
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

@given(instance=Make_Makefile_strategy)
@settings(max_examples=50)
def test_make_makefile_instantiation(instance):
    assert isinstance(instance, Make_Makefile)



@given(instance=Make_Makefile_strategy)
def test_make_makefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Make_Dependency_strategy)
@settings(max_examples=50)
def test_make_dependency_instantiation(instance):
    assert isinstance(instance, Make_Dependency)

@given(instance=Make_Comment_strategy)
@settings(max_examples=50)
def test_make_comment_instantiation(instance):
    assert isinstance(instance, Make_Comment)



@given(instance=Make_Comment_strategy)
def test_make_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=Make_ShellLine_strategy)
@settings(max_examples=50)
def test_make_shellline_instantiation(instance):
    assert isinstance(instance, Make_ShellLine)



@given(instance=Make_ShellLine_strategy)
def test_make_shellline_display_setter(instance):
    original = instance.display
    instance.display = original
    assert instance.display == original



@given(instance=Make_ShellLine_strategy)
def test_make_shellline_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original

@given(instance=Make_Macro_strategy)
@settings(max_examples=50)
def test_make_macro_instantiation(instance):
    assert isinstance(instance, Make_Macro)



@given(instance=Make_Macro_strategy)
def test_make_macro_value_setter(instance):
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

@given(instance=Make_FileDep_strategy)
@settings(max_examples=50)
def test_make_filedep_instantiation(instance):
    assert isinstance(instance, Make_FileDep)



@given(instance=Make_FileDep_strategy)
def test_make_filedep_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Make_RuleDep_strategy)
@settings(max_examples=50)
def test_make_ruledep_instantiation(instance):
    assert isinstance(instance, Make_RuleDep)

@given(instance=Make_Rule_strategy)
@settings(max_examples=50)
def test_make_rule_instantiation(instance):
    assert isinstance(instance, Make_Rule)

@given(instance=Make_Element_strategy)
@settings(max_examples=50)
def test_make_element_instantiation(instance):
    assert isinstance(instance, Make_Element)



@given(instance=Make_Element_strategy)
def test_make_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
