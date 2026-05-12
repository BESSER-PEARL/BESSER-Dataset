import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scxml_EStringToStringMapEntry,
    scxml_DocumentRoot,
    scxml_ScxmlTransitionType,
    scxml_ScxmlStateType,
    scxml_ScxmlScxmlType,
    scxml_ScxmlParamType,
    scxml_ScxmlScriptType,
    scxml_ScxmlSendType,
    scxml_ScxmlOnexecuteType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scxml_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(scxml_EStringToStringMapEntry)


def test_scxml_estringtostringmapentry_constructor_exists():
    assert callable(scxml_EStringToStringMapEntry.__init__)


def test_scxml_estringtostringmapentry_constructor_args():
    sig = inspect.signature(scxml_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_scxml_documentroot_is_not_abstract():
    assert not inspect.isabstract(scxml_DocumentRoot)


def test_scxml_documentroot_constructor_exists():
    assert callable(scxml_DocumentRoot.__init__)


def test_scxml_documentroot_constructor_args():
    sig = inspect.signature(scxml_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_scxml_documentroot_has_mixed():
    assert hasattr(scxml_DocumentRoot, "mixed")
    descriptor = None
    for klass in scxml_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmltransitiontype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlTransitionType)


def test_scxml_scxmltransitiontype_constructor_exists():
    assert callable(scxml_ScxmlTransitionType.__init__)


def test_scxml_scxmltransitiontype_constructor_args():
    sig = inspect.signature(scxml_ScxmlTransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "cond" in params, "Missing parameter 'cond'"
    assert "scxmlExecutablecontent" in params, "Missing parameter 'scxmlExecutablecontent'"
    assert "any" in params, "Missing parameter 'any'"
    assert "event" in params, "Missing parameter 'event'"

def test_scxml_scxmltransitiontype_has_target():
    assert hasattr(scxml_ScxmlTransitionType, "target")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmltransitiontype_has_cond():
    assert hasattr(scxml_ScxmlTransitionType, "cond")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmltransitiontype_has_scxmlExecutablecontent():
    assert hasattr(scxml_ScxmlTransitionType, "scxmlExecutablecontent")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "scxmlExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmltransitiontype_has_any():
    assert hasattr(scxml_ScxmlTransitionType, "any")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmltransitiontype_has_event():
    assert hasattr(scxml_ScxmlTransitionType, "event")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlstatetype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlStateType)


def test_scxml_scxmlstatetype_constructor_exists():
    assert callable(scxml_ScxmlStateType.__init__)


def test_scxml_scxmlstatetype_constructor_args():
    sig = inspect.signature(scxml_ScxmlStateType.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "id" in params, "Missing parameter 'id'"

def test_scxml_scxmlstatetype_has_initial():
    assert hasattr(scxml_ScxmlStateType, "initial")
    descriptor = None
    for klass in scxml_ScxmlStateType.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlstatetype_has_id():
    assert hasattr(scxml_ScxmlStateType, "id")
    descriptor = None
    for klass in scxml_ScxmlStateType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlscxmltype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlScxmlType)


def test_scxml_scxmlscxmltype_constructor_exists():
    assert callable(scxml_ScxmlScxmlType.__init__)


def test_scxml_scxmlscxmltype_constructor_args():
    sig = inspect.signature(scxml_ScxmlScxmlType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "version" in params, "Missing parameter 'version'"

def test_scxml_scxmlscxmltype_has_id():
    assert hasattr(scxml_ScxmlScxmlType, "id")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscxmltype_has_initial():
    assert hasattr(scxml_ScxmlScxmlType, "initial")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscxmltype_has_version():
    assert hasattr(scxml_ScxmlScxmlType, "version")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlparamtype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlParamType)


def test_scxml_scxmlparamtype_constructor_exists():
    assert callable(scxml_ScxmlParamType.__init__)


def test_scxml_scxmlparamtype_constructor_args():
    sig = inspect.signature(scxml_ScxmlParamType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"

def test_scxml_scxmlparamtype_has_name():
    assert hasattr(scxml_ScxmlParamType, "name")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlparamtype_has_anyAttribute():
    assert hasattr(scxml_ScxmlParamType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlparamtype_has_expr():
    assert hasattr(scxml_ScxmlParamType, "expr")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlparamtype_has_any():
    assert hasattr(scxml_ScxmlParamType, "any")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlparamtype_has_scxmlExtraContent():
    assert hasattr(scxml_ScxmlParamType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlscripttype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlScriptType)


def test_scxml_scxmlscripttype_constructor_exists():
    assert callable(scxml_ScxmlScriptType.__init__)


def test_scxml_scxmlscripttype_constructor_args():
    sig = inspect.signature(scxml_ScxmlScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "content" in params, "Missing parameter 'content'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "src" in params, "Missing parameter 'src'"

def test_scxml_scxmlscripttype_has_any():
    assert hasattr(scxml_ScxmlScriptType, "any")
    descriptor = None
    for klass in scxml_ScxmlScriptType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscripttype_has_scxmlExtraContent():
    assert hasattr(scxml_ScxmlScriptType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml_ScxmlScriptType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscripttype_has_content():
    assert hasattr(scxml_ScxmlScriptType, "content")
    descriptor = None
    for klass in scxml_ScxmlScriptType.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscripttype_has_mixed():
    assert hasattr(scxml_ScxmlScriptType, "mixed")
    descriptor = None
    for klass in scxml_ScxmlScriptType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscripttype_has_src():
    assert hasattr(scxml_ScxmlScriptType, "src")
    descriptor = None
    for klass in scxml_ScxmlScriptType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlsendtype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlSendType)


def test_scxml_scxmlsendtype_constructor_exists():
    assert callable(scxml_ScxmlSendType.__init__)


def test_scxml_scxmlsendtype_constructor_args():
    sig = inspect.signature(scxml_ScxmlSendType.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_scxml_scxmlsendtype_has_event():
    assert hasattr(scxml_ScxmlSendType, "event")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlonexecutetype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlOnexecuteType)


def test_scxml_scxmlonexecutetype_constructor_exists():
    assert callable(scxml_ScxmlOnexecuteType.__init__)


def test_scxml_scxmlonexecutetype_constructor_args():
    sig = inspect.signature(scxml_ScxmlOnexecuteType.__init__)
    params = list(sig.parameters.keys())
    assert "scxmlExecutablecontent" in params, "Missing parameter 'scxmlExecutablecontent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml_scxmlonexecutetype_has_scxmlExecutablecontent():
    assert hasattr(scxml_ScxmlOnexecuteType, "scxmlExecutablecontent")
    descriptor = None
    for klass in scxml_ScxmlOnexecuteType.__mro__:
        if "scxmlExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlonexecutetype_has_anyAttribute():
    assert hasattr(scxml_ScxmlOnexecuteType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlOnexecuteType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlonexecutetype_has_any():
    assert hasattr(scxml_ScxmlOnexecuteType, "any")
    descriptor = None
    for klass in scxml_ScxmlOnexecuteType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
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
scxml_EStringToStringMapEntry_strategy = st.builds(
    scxml_EStringToStringMapEntry,
)
scxml_DocumentRoot_strategy = st.builds(
    scxml_DocumentRoot,
    mixed=
        safe_text
)
scxml_ScxmlTransitionType_strategy = st.builds(
    scxml_ScxmlTransitionType,
    target=
        safe_text,
    cond=
        safe_text,
    scxmlExecutablecontent=
        safe_text,
    any=
        safe_text,
    event=
        safe_text
)
scxml_ScxmlStateType_strategy = st.builds(
    scxml_ScxmlStateType,
    initial=
        safe_text,
    id=
        safe_text
)
scxml_ScxmlScxmlType_strategy = st.builds(
    scxml_ScxmlScxmlType,
    id=
        safe_text,
    initial=
        safe_text,
    version=
        safe_text
)
scxml_ScxmlParamType_strategy = st.builds(
    scxml_ScxmlParamType,
    name=
        safe_text,
    anyAttribute=
        safe_text,
    expr=
        safe_text,
    any=
        safe_text,
    scxmlExtraContent=
        safe_text
)
scxml_ScxmlScriptType_strategy = st.builds(
    scxml_ScxmlScriptType,
    any=
        safe_text,
    scxmlExtraContent=
        safe_text,
    content=
        safe_text,
    mixed=
        safe_text,
    src=
        safe_text
)
scxml_ScxmlSendType_strategy = st.builds(
    scxml_ScxmlSendType,
    event=
        safe_text
)
scxml_ScxmlOnexecuteType_strategy = st.builds(
    scxml_ScxmlOnexecuteType,
    scxmlExecutablecontent=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)

@given(instance=scxml_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_scxml_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, scxml_EStringToStringMapEntry)

@given(instance=scxml_DocumentRoot_strategy)
@settings(max_examples=50)
def test_scxml_documentroot_instantiation(instance):
    assert isinstance(instance, scxml_DocumentRoot)



@given(instance=scxml_DocumentRoot_strategy)
def test_scxml_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=scxml_ScxmlTransitionType_strategy)
@settings(max_examples=50)
def test_scxml_scxmltransitiontype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlTransitionType)



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_scxmlExecutablecontent_setter(instance):
    original = instance.scxmlExecutablecontent
    instance.scxmlExecutablecontent = original
    assert instance.scxmlExecutablecontent == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml_ScxmlStateType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlstatetype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlStateType)



@given(instance=scxml_ScxmlStateType_strategy)
def test_scxml_scxmlstatetype_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=scxml_ScxmlStateType_strategy)
def test_scxml_scxmlstatetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml_ScxmlScxmlType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlscxmltype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlScxmlType)



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=scxml_ScxmlParamType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlparamtype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlParamType)



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml_ScxmlScriptType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlscripttype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlScriptType)



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=scxml_ScxmlSendType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlsendtype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlSendType)



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml_ScxmlOnexecuteType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlonexecutetype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlOnexecuteType)



@given(instance=scxml_ScxmlOnexecuteType_strategy)
def test_scxml_scxmlonexecutetype_scxmlExecutablecontent_setter(instance):
    original = instance.scxmlExecutablecontent
    instance.scxmlExecutablecontent = original
    assert instance.scxmlExecutablecontent == original



@given(instance=scxml_ScxmlOnexecuteType_strategy)
def test_scxml_scxmlonexecutetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlOnexecuteType_strategy)
def test_scxml_scxmlonexecutetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original
