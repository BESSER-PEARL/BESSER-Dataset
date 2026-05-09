import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scxml::EStringToStringMapEntry,
    scxml::DocumentRoot,
    scxml::ScxmlTransitionType,
    scxml::ScxmlStateType,
    scxml::ScxmlScxmlType,
    scxml::ScxmlParamType,
    scxml::ScxmlScriptType,
    scxml::ScxmlSendType,
    scxml::ScxmlOnexecuteType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scxml::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(scxml::EStringToStringMapEntry)


def test_scxml::estringtostringmapentry_constructor_exists():
    assert callable(scxml::EStringToStringMapEntry.__init__)


def test_scxml::estringtostringmapentry_constructor_args():
    sig = inspect.signature(scxml::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_scxml::documentroot_is_not_abstract():
    assert not inspect.isabstract(scxml::DocumentRoot)


def test_scxml::documentroot_constructor_exists():
    assert callable(scxml::DocumentRoot.__init__)


def test_scxml::documentroot_constructor_args():
    sig = inspect.signature(scxml::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_scxml::documentroot_has_mixed():
    assert hasattr(scxml::DocumentRoot, "mixed")
    descriptor = None
    for klass in scxml::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmltransitiontype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlTransitionType)


def test_scxml::scxmltransitiontype_constructor_exists():
    assert callable(scxml::ScxmlTransitionType.__init__)


def test_scxml::scxmltransitiontype_constructor_args():
    sig = inspect.signature(scxml::ScxmlTransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "scxmlExecutablecontent" in params, "Missing parameter 'scxmlExecutablecontent'"
    assert "any" in params, "Missing parameter 'any'"
    assert "cond" in params, "Missing parameter 'cond'"
    assert "event" in params, "Missing parameter 'event'"

def test_scxml::scxmltransitiontype_has_target():
    assert hasattr(scxml::ScxmlTransitionType, "target")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmltransitiontype_has_scxmlExecutablecontent():
    assert hasattr(scxml::ScxmlTransitionType, "scxmlExecutablecontent")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "scxmlExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmltransitiontype_has_any():
    assert hasattr(scxml::ScxmlTransitionType, "any")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmltransitiontype_has_cond():
    assert hasattr(scxml::ScxmlTransitionType, "cond")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmltransitiontype_has_event():
    assert hasattr(scxml::ScxmlTransitionType, "event")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlstatetype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlStateType)


def test_scxml::scxmlstatetype_constructor_exists():
    assert callable(scxml::ScxmlStateType.__init__)


def test_scxml::scxmlstatetype_constructor_args():
    sig = inspect.signature(scxml::ScxmlStateType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_scxml::scxmlstatetype_has_id():
    assert hasattr(scxml::ScxmlStateType, "id")
    descriptor = None
    for klass in scxml::ScxmlStateType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlstatetype_has_initial():
    assert hasattr(scxml::ScxmlStateType, "initial")
    descriptor = None
    for klass in scxml::ScxmlStateType.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlscxmltype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlScxmlType)


def test_scxml::scxmlscxmltype_constructor_exists():
    assert callable(scxml::ScxmlScxmlType.__init__)


def test_scxml::scxmlscxmltype_constructor_args():
    sig = inspect.signature(scxml::ScxmlScxmlType.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"

def test_scxml::scxmlscxmltype_has_initial():
    assert hasattr(scxml::ScxmlScxmlType, "initial")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscxmltype_has_id():
    assert hasattr(scxml::ScxmlScxmlType, "id")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscxmltype_has_version():
    assert hasattr(scxml::ScxmlScxmlType, "version")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlparamtype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlParamType)


def test_scxml::scxmlparamtype_constructor_exists():
    assert callable(scxml::ScxmlParamType.__init__)


def test_scxml::scxmlparamtype_constructor_args():
    sig = inspect.signature(scxml::ScxmlParamType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"

def test_scxml::scxmlparamtype_has_any():
    assert hasattr(scxml::ScxmlParamType, "any")
    descriptor = None
    for klass in scxml::ScxmlParamType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparamtype_has_expr():
    assert hasattr(scxml::ScxmlParamType, "expr")
    descriptor = None
    for klass in scxml::ScxmlParamType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparamtype_has_anyAttribute():
    assert hasattr(scxml::ScxmlParamType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlParamType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparamtype_has_name():
    assert hasattr(scxml::ScxmlParamType, "name")
    descriptor = None
    for klass in scxml::ScxmlParamType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparamtype_has_scxmlExtraContent():
    assert hasattr(scxml::ScxmlParamType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml::ScxmlParamType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlscripttype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlScriptType)


def test_scxml::scxmlscripttype_constructor_exists():
    assert callable(scxml::ScxmlScriptType.__init__)


def test_scxml::scxmlscripttype_constructor_args():
    sig = inspect.signature(scxml::ScxmlScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "content" in params, "Missing parameter 'content'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "src" in params, "Missing parameter 'src'"

def test_scxml::scxmlscripttype_has_any():
    assert hasattr(scxml::ScxmlScriptType, "any")
    descriptor = None
    for klass in scxml::ScxmlScriptType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscripttype_has_content():
    assert hasattr(scxml::ScxmlScriptType, "content")
    descriptor = None
    for klass in scxml::ScxmlScriptType.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscripttype_has_scxmlExtraContent():
    assert hasattr(scxml::ScxmlScriptType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml::ScxmlScriptType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscripttype_has_mixed():
    assert hasattr(scxml::ScxmlScriptType, "mixed")
    descriptor = None
    for klass in scxml::ScxmlScriptType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscripttype_has_src():
    assert hasattr(scxml::ScxmlScriptType, "src")
    descriptor = None
    for klass in scxml::ScxmlScriptType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlsendtype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlSendType)


def test_scxml::scxmlsendtype_constructor_exists():
    assert callable(scxml::ScxmlSendType.__init__)


def test_scxml::scxmlsendtype_constructor_args():
    sig = inspect.signature(scxml::ScxmlSendType.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_scxml::scxmlsendtype_has_event():
    assert hasattr(scxml::ScxmlSendType, "event")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlonexecutetype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlOnexecuteType)


def test_scxml::scxmlonexecutetype_constructor_exists():
    assert callable(scxml::ScxmlOnexecuteType.__init__)


def test_scxml::scxmlonexecutetype_constructor_args():
    sig = inspect.signature(scxml::ScxmlOnexecuteType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlExecutablecontent" in params, "Missing parameter 'scxmlExecutablecontent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml::scxmlonexecutetype_has_any():
    assert hasattr(scxml::ScxmlOnexecuteType, "any")
    descriptor = None
    for klass in scxml::ScxmlOnexecuteType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlonexecutetype_has_scxmlExecutablecontent():
    assert hasattr(scxml::ScxmlOnexecuteType, "scxmlExecutablecontent")
    descriptor = None
    for klass in scxml::ScxmlOnexecuteType.__mro__:
        if "scxmlExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlonexecutetype_has_anyAttribute():
    assert hasattr(scxml::ScxmlOnexecuteType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlOnexecuteType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
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
scxml::EStringToStringMapEntry_strategy = st.builds(
    scxml::EStringToStringMapEntry,
)
scxml::DocumentRoot_strategy = st.builds(
    scxml::DocumentRoot,
    mixed=
        safe_text
)
scxml::ScxmlTransitionType_strategy = st.builds(
    scxml::ScxmlTransitionType,
    target=
        safe_text,
    scxmlExecutablecontent=
        safe_text,
    any=
        safe_text,
    cond=
        safe_text,
    event=
        safe_text
)
scxml::ScxmlStateType_strategy = st.builds(
    scxml::ScxmlStateType,
    id=
        safe_text,
    initial=
        safe_text
)
scxml::ScxmlScxmlType_strategy = st.builds(
    scxml::ScxmlScxmlType,
    initial=
        safe_text,
    id=
        safe_text,
    version=
        safe_text
)
scxml::ScxmlParamType_strategy = st.builds(
    scxml::ScxmlParamType,
    any=
        safe_text,
    expr=
        safe_text,
    anyAttribute=
        safe_text,
    name=
        safe_text,
    scxmlExtraContent=
        safe_text
)
scxml::ScxmlScriptType_strategy = st.builds(
    scxml::ScxmlScriptType,
    any=
        safe_text,
    content=
        safe_text,
    scxmlExtraContent=
        safe_text,
    mixed=
        safe_text,
    src=
        safe_text
)
scxml::ScxmlSendType_strategy = st.builds(
    scxml::ScxmlSendType,
    event=
        safe_text
)
scxml::ScxmlOnexecuteType_strategy = st.builds(
    scxml::ScxmlOnexecuteType,
    any=
        safe_text,
    scxmlExecutablecontent=
        safe_text,
    anyAttribute=
        safe_text
)

@given(instance=scxml::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_scxml::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, scxml::EStringToStringMapEntry)

@given(instance=scxml::DocumentRoot_strategy)
@settings(max_examples=50)
def test_scxml::documentroot_instantiation(instance):
    assert isinstance(instance, scxml::DocumentRoot)

@given(instance=scxml::DocumentRoot_strategy)
def test_scxml::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=scxml::DocumentRoot_strategy)
def test_scxml::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=scxml::ScxmlTransitionType_strategy)
@settings(max_examples=50)
def test_scxml::scxmltransitiontype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlTransitionType)

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_scxmlExecutablecontent_type(instance):
    assert isinstance(instance.scxmlExecutablecontent, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_scxmlExecutablecontent_setter(instance):
    original = instance.scxmlExecutablecontent
    instance.scxmlExecutablecontent = original
    assert instance.scxmlExecutablecontent == original

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_cond_type(instance):
    assert isinstance(instance.cond, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::ScxmlStateType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlstatetype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlStateType)

@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_initial_type(instance):
    assert isinstance(instance.initial, str)


@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=scxml::ScxmlScxmlType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlscxmltype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlScxmlType)

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_initial_type(instance):
    assert isinstance(instance.initial, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=scxml::ScxmlParamType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlparamtype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlParamType)

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_scxmlExtraContent_type(instance):
    assert isinstance(instance.scxmlExtraContent, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml::ScxmlScriptType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlscripttype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlScriptType)

@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_scxmlExtraContent_type(instance):
    assert isinstance(instance.scxmlExtraContent, str)


@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=scxml::ScxmlSendType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlsendtype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlSendType)

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::ScxmlOnexecuteType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlonexecutetype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlOnexecuteType)

@given(instance=scxml::ScxmlOnexecuteType_strategy)
def test_scxml::scxmlonexecutetype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlOnexecuteType_strategy)
def test_scxml::scxmlonexecutetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlOnexecuteType_strategy)
def test_scxml::scxmlonexecutetype_scxmlExecutablecontent_type(instance):
    assert isinstance(instance.scxmlExecutablecontent, str)


@given(instance=scxml::ScxmlOnexecuteType_strategy)
def test_scxml::scxmlonexecutetype_scxmlExecutablecontent_setter(instance):
    original = instance.scxmlExecutablecontent
    instance.scxmlExecutablecontent = original
    assert instance.scxmlExecutablecontent == original

@given(instance=scxml::ScxmlOnexecuteType_strategy)
def test_scxml::scxmlonexecutetype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlOnexecuteType_strategy)
def test_scxml::scxmlonexecutetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original
