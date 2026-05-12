import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scxml_ScxmlTransitionType,
    scxml_ScxmlStateType,
    scxml_ScxmlSendType,
    scxml_ScxmlScxmlType,
    scxml_ScxmlScriptType,
    scxml_ScxmlLogType,
    scxml_ScxmlInvokeType,
    scxml_ScxmlInitialType,
    scxml_ScxmlIfType,
    scxml_ScxmlHistoryType,
    scxml_ScxmlRaiseType,
    scxml_ScxmlParamType,
    scxml_ScxmlParallelType,
    scxml_ScxmlOnexitType,
    scxml_ScxmlOnentryType,
    scxml_ScxmlDonedataType,
    scxml_ScxmlDatamodelType,
    scxml_ScxmlDataType,
    scxml_ScxmlContentType,
    scxml_ScxmlCancelType,
    scxml_ScxmlForeachType,
    scxml_ScxmlFinalizeType,
    scxml_ScxmlFinalType,
    scxml_ScxmlElseifType,
    scxml_ScxmlElseType,
    scxml_ScxmlAssignType,
    scxml_EStringToStringMapEntry,
    scxml_DocumentRoot,
    AssignTypeDatatype,
    ExmodeDatatype,
    HistoryTypeDatatype,
    BindingDatatype,
    BooleanDatatype,
    TransitionTypeDatatype,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scxml_scxmltransitiontype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlTransitionType)


def test_scxml_scxmltransitiontype_constructor_exists():
    assert callable(scxml_ScxmlTransitionType.__init__)


def test_scxml_scxmltransitiontype_constructor_args():
    sig = inspect.signature(scxml_ScxmlTransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "target" in params, "Missing parameter 'target'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "type" in params, "Missing parameter 'type'"
    assert "cond" in params, "Missing parameter 'cond'"
    assert "event" in params, "Missing parameter 'event'"

def test_scxml_scxmltransitiontype_has_any():
    assert hasattr(scxml_ScxmlTransitionType, "any")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmltransitiontype_has_target():
    assert hasattr(scxml_ScxmlTransitionType, "target")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmltransitiontype_has_anyAttribute():
    assert hasattr(scxml_ScxmlTransitionType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmltransitiontype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml_ScxmlTransitionType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmltransitiontype_has_type():
    assert hasattr(scxml_ScxmlTransitionType, "type")
    descriptor = None
    for klass in scxml_ScxmlTransitionType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
    assert "initial1" in params, "Missing parameter 'initial1'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "id" in params, "Missing parameter 'id'"
    assert "scxmlStateMix" in params, "Missing parameter 'scxmlStateMix'"

def test_scxml_scxmlstatetype_has_initial1():
    assert hasattr(scxml_ScxmlStateType, "initial1")
    descriptor = None
    for klass in scxml_ScxmlStateType.__mro__:
        if "initial1" in klass.__dict__:
            descriptor = klass.__dict__["initial1"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlstatetype_has_anyAttribute():
    assert hasattr(scxml_ScxmlStateType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlStateType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlstatetype_has_any():
    assert hasattr(scxml_ScxmlStateType, "any")
    descriptor = None
    for klass in scxml_ScxmlStateType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
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

def test_scxml_scxmlstatetype_has_scxmlStateMix():
    assert hasattr(scxml_ScxmlStateType, "scxmlStateMix")
    descriptor = None
    for klass in scxml_ScxmlStateType.__mro__:
        if "scxmlStateMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlStateMix"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlsendtype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlSendType)


def test_scxml_scxmlsendtype_constructor_exists():
    assert callable(scxml_ScxmlSendType.__init__)


def test_scxml_scxmlsendtype_constructor_args():
    sig = inspect.signature(scxml_ScxmlSendType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "targetexpr" in params, "Missing parameter 'targetexpr'"
    assert "scxmlSendMix" in params, "Missing parameter 'scxmlSendMix'"
    assert "delayexpr" in params, "Missing parameter 'delayexpr'"
    assert "event" in params, "Missing parameter 'event'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "type" in params, "Missing parameter 'type'"
    assert "eventexpr" in params, "Missing parameter 'eventexpr'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "target" in params, "Missing parameter 'target'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "id" in params, "Missing parameter 'id'"

def test_scxml_scxmlsendtype_has_any():
    assert hasattr(scxml_ScxmlSendType, "any")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_idlocation():
    assert hasattr(scxml_ScxmlSendType, "idlocation")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "idlocation" in klass.__dict__:
            descriptor = klass.__dict__["idlocation"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_targetexpr():
    assert hasattr(scxml_ScxmlSendType, "targetexpr")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "targetexpr" in klass.__dict__:
            descriptor = klass.__dict__["targetexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_scxmlSendMix():
    assert hasattr(scxml_ScxmlSendType, "scxmlSendMix")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "scxmlSendMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlSendMix"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_delayexpr():
    assert hasattr(scxml_ScxmlSendType, "delayexpr")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "delayexpr" in klass.__dict__:
            descriptor = klass.__dict__["delayexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_event():
    assert hasattr(scxml_ScxmlSendType, "event")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_delay():
    assert hasattr(scxml_ScxmlSendType, "delay")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_namelist():
    assert hasattr(scxml_ScxmlSendType, "namelist")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "namelist" in klass.__dict__:
            descriptor = klass.__dict__["namelist"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_type():
    assert hasattr(scxml_ScxmlSendType, "type")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_eventexpr():
    assert hasattr(scxml_ScxmlSendType, "eventexpr")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "eventexpr" in klass.__dict__:
            descriptor = klass.__dict__["eventexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_typeexpr():
    assert hasattr(scxml_ScxmlSendType, "typeexpr")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_target():
    assert hasattr(scxml_ScxmlSendType, "target")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_anyAttribute():
    assert hasattr(scxml_ScxmlSendType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlsendtype_has_id():
    assert hasattr(scxml_ScxmlSendType, "id")
    descriptor = None
    for klass in scxml_ScxmlSendType.__mro__:
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
    assert "exmode" in params, "Missing parameter 'exmode'"
    assert "scxmlScxmlMix" in params, "Missing parameter 'scxmlScxmlMix'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "name" in params, "Missing parameter 'name'"
    assert "any" in params, "Missing parameter 'any'"
    assert "datamodel1" in params, "Missing parameter 'datamodel1'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "binding" in params, "Missing parameter 'binding'"
    assert "version" in params, "Missing parameter 'version'"

def test_scxml_scxmlscxmltype_has_exmode():
    assert hasattr(scxml_ScxmlScxmlType, "exmode")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "exmode" in klass.__dict__:
            descriptor = klass.__dict__["exmode"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscxmltype_has_scxmlScxmlMix():
    assert hasattr(scxml_ScxmlScxmlType, "scxmlScxmlMix")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "scxmlScxmlMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlScxmlMix"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscxmltype_has_anyAttribute():
    assert hasattr(scxml_ScxmlScxmlType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscxmltype_has_name():
    assert hasattr(scxml_ScxmlScxmlType, "name")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscxmltype_has_any():
    assert hasattr(scxml_ScxmlScxmlType, "any")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlscxmltype_has_datamodel1():
    assert hasattr(scxml_ScxmlScxmlType, "datamodel1")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "datamodel1" in klass.__dict__:
            descriptor = klass.__dict__["datamodel1"]
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

def test_scxml_scxmlscxmltype_has_binding():
    assert hasattr(scxml_ScxmlScxmlType, "binding")
    descriptor = None
    for klass in scxml_ScxmlScxmlType.__mro__:
        if "binding" in klass.__dict__:
            descriptor = klass.__dict__["binding"]
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



def test_scxml_scxmlscripttype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlScriptType)


def test_scxml_scxmlscripttype_constructor_exists():
    assert callable(scxml_ScxmlScriptType.__init__)


def test_scxml_scxmlscripttype_constructor_args():
    sig = inspect.signature(scxml_ScxmlScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml_scxmlscripttype_has_src():
    assert hasattr(scxml_ScxmlScriptType, "src")
    descriptor = None
    for klass in scxml_ScxmlScriptType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
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

def test_scxml_scxmlscripttype_has_anyAttribute():
    assert hasattr(scxml_ScxmlScriptType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlScriptType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
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

def test_scxml_scxmlscripttype_has_any():
    assert hasattr(scxml_ScxmlScriptType, "any")
    descriptor = None
    for klass in scxml_ScxmlScriptType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmllogtype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlLogType)


def test_scxml_scxmllogtype_constructor_exists():
    assert callable(scxml_ScxmlLogType.__init__)


def test_scxml_scxmllogtype_constructor_args():
    sig = inspect.signature(scxml_ScxmlLogType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "label" in params, "Missing parameter 'label'"
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"

def test_scxml_scxmllogtype_has_anyAttribute():
    assert hasattr(scxml_ScxmlLogType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlLogType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmllogtype_has_expr():
    assert hasattr(scxml_ScxmlLogType, "expr")
    descriptor = None
    for klass in scxml_ScxmlLogType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmllogtype_has_label():
    assert hasattr(scxml_ScxmlLogType, "label")
    descriptor = None
    for klass in scxml_ScxmlLogType.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmllogtype_has_any():
    assert hasattr(scxml_ScxmlLogType, "any")
    descriptor = None
    for klass in scxml_ScxmlLogType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmllogtype_has_scxmlExtraContent():
    assert hasattr(scxml_ScxmlLogType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml_ScxmlLogType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlinvoketype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlInvokeType)


def test_scxml_scxmlinvoketype_constructor_exists():
    assert callable(scxml_ScxmlInvokeType.__init__)


def test_scxml_scxmlinvoketype_constructor_args():
    sig = inspect.signature(scxml_ScxmlInvokeType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlInvokeMix" in params, "Missing parameter 'scxmlInvokeMix'"
    assert "autoforward" in params, "Missing parameter 'autoforward'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "srcexpr" in params, "Missing parameter 'srcexpr'"
    assert "src" in params, "Missing parameter 'src'"
    assert "id" in params, "Missing parameter 'id'"

def test_scxml_scxmlinvoketype_has_any():
    assert hasattr(scxml_ScxmlInvokeType, "any")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_scxmlInvokeMix():
    assert hasattr(scxml_ScxmlInvokeType, "scxmlInvokeMix")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "scxmlInvokeMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlInvokeMix"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_autoforward():
    assert hasattr(scxml_ScxmlInvokeType, "autoforward")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "autoforward" in klass.__dict__:
            descriptor = klass.__dict__["autoforward"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_typeexpr():
    assert hasattr(scxml_ScxmlInvokeType, "typeexpr")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_type():
    assert hasattr(scxml_ScxmlInvokeType, "type")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_anyAttribute():
    assert hasattr(scxml_ScxmlInvokeType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_idlocation():
    assert hasattr(scxml_ScxmlInvokeType, "idlocation")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "idlocation" in klass.__dict__:
            descriptor = klass.__dict__["idlocation"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_namelist():
    assert hasattr(scxml_ScxmlInvokeType, "namelist")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "namelist" in klass.__dict__:
            descriptor = klass.__dict__["namelist"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_srcexpr():
    assert hasattr(scxml_ScxmlInvokeType, "srcexpr")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "srcexpr" in klass.__dict__:
            descriptor = klass.__dict__["srcexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_src():
    assert hasattr(scxml_ScxmlInvokeType, "src")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinvoketype_has_id():
    assert hasattr(scxml_ScxmlInvokeType, "id")
    descriptor = None
    for klass in scxml_ScxmlInvokeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlinitialtype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlInitialType)


def test_scxml_scxmlinitialtype_constructor_exists():
    assert callable(scxml_ScxmlInitialType.__init__)


def test_scxml_scxmlinitialtype_constructor_args():
    sig = inspect.signature(scxml_ScxmlInitialType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlExtraContent1" in params, "Missing parameter 'scxmlExtraContent1'"
    assert "any1" in params, "Missing parameter 'any1'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml_scxmlinitialtype_has_any():
    assert hasattr(scxml_ScxmlInitialType, "any")
    descriptor = None
    for klass in scxml_ScxmlInitialType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinitialtype_has_scxmlExtraContent1():
    assert hasattr(scxml_ScxmlInitialType, "scxmlExtraContent1")
    descriptor = None
    for klass in scxml_ScxmlInitialType.__mro__:
        if "scxmlExtraContent1" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent1"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinitialtype_has_any1():
    assert hasattr(scxml_ScxmlInitialType, "any1")
    descriptor = None
    for klass in scxml_ScxmlInitialType.__mro__:
        if "any1" in klass.__dict__:
            descriptor = klass.__dict__["any1"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinitialtype_has_scxmlExtraContent():
    assert hasattr(scxml_ScxmlInitialType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml_ScxmlInitialType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlinitialtype_has_anyAttribute():
    assert hasattr(scxml_ScxmlInitialType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlInitialType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmliftype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlIfType)


def test_scxml_scxmliftype_constructor_exists():
    assert callable(scxml_ScxmlIfType.__init__)


def test_scxml_scxmliftype_constructor_args():
    sig = inspect.signature(scxml_ScxmlIfType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "cond" in params, "Missing parameter 'cond'"
    assert "any2" in params, "Missing parameter 'any2'"
    assert "scxmlCoreExecutablecontent1" in params, "Missing parameter 'scxmlCoreExecutablecontent1'"
    assert "scxmlCoreExecutablecontent2" in params, "Missing parameter 'scxmlCoreExecutablecontent2'"
    assert "any1" in params, "Missing parameter 'any1'"
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"

def test_scxml_scxmliftype_has_anyAttribute():
    assert hasattr(scxml_ScxmlIfType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlIfType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmliftype_has_cond():
    assert hasattr(scxml_ScxmlIfType, "cond")
    descriptor = None
    for klass in scxml_ScxmlIfType.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmliftype_has_any2():
    assert hasattr(scxml_ScxmlIfType, "any2")
    descriptor = None
    for klass in scxml_ScxmlIfType.__mro__:
        if "any2" in klass.__dict__:
            descriptor = klass.__dict__["any2"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmliftype_has_scxmlCoreExecutablecontent1():
    assert hasattr(scxml_ScxmlIfType, "scxmlCoreExecutablecontent1")
    descriptor = None
    for klass in scxml_ScxmlIfType.__mro__:
        if "scxmlCoreExecutablecontent1" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent1"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmliftype_has_scxmlCoreExecutablecontent2():
    assert hasattr(scxml_ScxmlIfType, "scxmlCoreExecutablecontent2")
    descriptor = None
    for klass in scxml_ScxmlIfType.__mro__:
        if "scxmlCoreExecutablecontent2" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent2"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmliftype_has_any1():
    assert hasattr(scxml_ScxmlIfType, "any1")
    descriptor = None
    for klass in scxml_ScxmlIfType.__mro__:
        if "any1" in klass.__dict__:
            descriptor = klass.__dict__["any1"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmliftype_has_any():
    assert hasattr(scxml_ScxmlIfType, "any")
    descriptor = None
    for klass in scxml_ScxmlIfType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmliftype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml_ScxmlIfType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml_ScxmlIfType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlhistorytype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlHistoryType)


def test_scxml_scxmlhistorytype_constructor_exists():
    assert callable(scxml_ScxmlHistoryType.__init__)


def test_scxml_scxmlhistorytype_constructor_args():
    sig = inspect.signature(scxml_ScxmlHistoryType.__init__)
    params = list(sig.parameters.keys())
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any1" in params, "Missing parameter 'any1'"
    assert "any" in params, "Missing parameter 'any'"
    assert "type" in params, "Missing parameter 'type'"
    assert "scxmlExtraContent1" in params, "Missing parameter 'scxmlExtraContent1'"
    assert "id" in params, "Missing parameter 'id'"

def test_scxml_scxmlhistorytype_has_scxmlExtraContent():
    assert hasattr(scxml_ScxmlHistoryType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml_ScxmlHistoryType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlhistorytype_has_anyAttribute():
    assert hasattr(scxml_ScxmlHistoryType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlHistoryType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlhistorytype_has_any1():
    assert hasattr(scxml_ScxmlHistoryType, "any1")
    descriptor = None
    for klass in scxml_ScxmlHistoryType.__mro__:
        if "any1" in klass.__dict__:
            descriptor = klass.__dict__["any1"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlhistorytype_has_any():
    assert hasattr(scxml_ScxmlHistoryType, "any")
    descriptor = None
    for klass in scxml_ScxmlHistoryType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlhistorytype_has_type():
    assert hasattr(scxml_ScxmlHistoryType, "type")
    descriptor = None
    for klass in scxml_ScxmlHistoryType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlhistorytype_has_scxmlExtraContent1():
    assert hasattr(scxml_ScxmlHistoryType, "scxmlExtraContent1")
    descriptor = None
    for klass in scxml_ScxmlHistoryType.__mro__:
        if "scxmlExtraContent1" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent1"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlhistorytype_has_id():
    assert hasattr(scxml_ScxmlHistoryType, "id")
    descriptor = None
    for klass in scxml_ScxmlHistoryType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlraisetype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlRaiseType)


def test_scxml_scxmlraisetype_constructor_exists():
    assert callable(scxml_ScxmlRaiseType.__init__)


def test_scxml_scxmlraisetype_constructor_args():
    sig = inspect.signature(scxml_ScxmlRaiseType.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml_scxmlraisetype_has_event():
    assert hasattr(scxml_ScxmlRaiseType, "event")
    descriptor = None
    for klass in scxml_ScxmlRaiseType.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlraisetype_has_anyAttribute():
    assert hasattr(scxml_ScxmlRaiseType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlRaiseType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlparamtype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlParamType)


def test_scxml_scxmlparamtype_constructor_exists():
    assert callable(scxml_ScxmlParamType.__init__)


def test_scxml_scxmlparamtype_constructor_args():
    sig = inspect.signature(scxml_ScxmlParamType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml_scxmlparamtype_has_any():
    assert hasattr(scxml_ScxmlParamType, "any")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
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

def test_scxml_scxmlparamtype_has_location():
    assert hasattr(scxml_ScxmlParamType, "location")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlparamtype_has_name():
    assert hasattr(scxml_ScxmlParamType, "name")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_scxml_scxmlparamtype_has_anyAttribute():
    assert hasattr(scxml_ScxmlParamType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlParamType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlparalleltype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlParallelType)


def test_scxml_scxmlparalleltype_constructor_exists():
    assert callable(scxml_ScxmlParallelType.__init__)


def test_scxml_scxmlparalleltype_constructor_args():
    sig = inspect.signature(scxml_ScxmlParallelType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlParallelMix" in params, "Missing parameter 'scxmlParallelMix'"
    assert "id" in params, "Missing parameter 'id'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml_scxmlparalleltype_has_anyAttribute():
    assert hasattr(scxml_ScxmlParallelType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlParallelType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlparalleltype_has_scxmlParallelMix():
    assert hasattr(scxml_ScxmlParallelType, "scxmlParallelMix")
    descriptor = None
    for klass in scxml_ScxmlParallelType.__mro__:
        if "scxmlParallelMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlParallelMix"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlparalleltype_has_id():
    assert hasattr(scxml_ScxmlParallelType, "id")
    descriptor = None
    for klass in scxml_ScxmlParallelType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlparalleltype_has_any():
    assert hasattr(scxml_ScxmlParallelType, "any")
    descriptor = None
    for klass in scxml_ScxmlParallelType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlonexittype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlOnexitType)


def test_scxml_scxmlonexittype_constructor_exists():
    assert callable(scxml_ScxmlOnexitType.__init__)


def test_scxml_scxmlonexittype_constructor_args():
    sig = inspect.signature(scxml_ScxmlOnexitType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml_scxmlonexittype_has_any():
    assert hasattr(scxml_ScxmlOnexitType, "any")
    descriptor = None
    for klass in scxml_ScxmlOnexitType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlonexittype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml_ScxmlOnexitType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml_ScxmlOnexitType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlonexittype_has_anyAttribute():
    assert hasattr(scxml_ScxmlOnexitType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlOnexitType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlonentrytype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlOnentryType)


def test_scxml_scxmlonentrytype_constructor_exists():
    assert callable(scxml_ScxmlOnentryType.__init__)


def test_scxml_scxmlonentrytype_constructor_args():
    sig = inspect.signature(scxml_ScxmlOnentryType.__init__)
    params = list(sig.parameters.keys())
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml_scxmlonentrytype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml_ScxmlOnentryType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml_ScxmlOnentryType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlonentrytype_has_anyAttribute():
    assert hasattr(scxml_ScxmlOnentryType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlOnentryType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlonentrytype_has_any():
    assert hasattr(scxml_ScxmlOnentryType, "any")
    descriptor = None
    for klass in scxml_ScxmlOnentryType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmldonedatatype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlDonedataType)


def test_scxml_scxmldonedatatype_constructor_exists():
    assert callable(scxml_ScxmlDonedataType.__init__)


def test_scxml_scxmldonedatatype_constructor_args():
    sig = inspect.signature(scxml_ScxmlDonedataType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml_scxmldonedatatype_has_anyAttribute():
    assert hasattr(scxml_ScxmlDonedataType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlDonedataType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmldatamodeltype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlDatamodelType)


def test_scxml_scxmldatamodeltype_constructor_exists():
    assert callable(scxml_ScxmlDatamodelType.__init__)


def test_scxml_scxmldatamodeltype_constructor_args():
    sig = inspect.signature(scxml_ScxmlDatamodelType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml_scxmldatamodeltype_has_anyAttribute():
    assert hasattr(scxml_ScxmlDatamodelType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlDatamodelType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmldatamodeltype_has_scxmlExtraContent():
    assert hasattr(scxml_ScxmlDatamodelType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml_ScxmlDatamodelType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmldatamodeltype_has_any():
    assert hasattr(scxml_ScxmlDatamodelType, "any")
    descriptor = None
    for klass in scxml_ScxmlDatamodelType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmldatatype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlDataType)


def test_scxml_scxmldatatype_constructor_exists():
    assert callable(scxml_ScxmlDataType.__init__)


def test_scxml_scxmldatatype_constructor_args():
    sig = inspect.signature(scxml_ScxmlDataType.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "id" in params, "Missing parameter 'id'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_scxml_scxmldatatype_has_src():
    assert hasattr(scxml_ScxmlDataType, "src")
    descriptor = None
    for klass in scxml_ScxmlDataType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmldatatype_has_id():
    assert hasattr(scxml_ScxmlDataType, "id")
    descriptor = None
    for klass in scxml_ScxmlDataType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmldatatype_has_any():
    assert hasattr(scxml_ScxmlDataType, "any")
    descriptor = None
    for klass in scxml_ScxmlDataType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmldatatype_has_anyAttribute():
    assert hasattr(scxml_ScxmlDataType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlDataType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmldatatype_has_expr():
    assert hasattr(scxml_ScxmlDataType, "expr")
    descriptor = None
    for klass in scxml_ScxmlDataType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmldatatype_has_mixed():
    assert hasattr(scxml_ScxmlDataType, "mixed")
    descriptor = None
    for klass in scxml_ScxmlDataType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlcontenttype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlContentType)


def test_scxml_scxmlcontenttype_constructor_exists():
    assert callable(scxml_ScxmlContentType.__init__)


def test_scxml_scxmlcontenttype_constructor_args():
    sig = inspect.signature(scxml_ScxmlContentType.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml_scxmlcontenttype_has_expr():
    assert hasattr(scxml_ScxmlContentType, "expr")
    descriptor = None
    for klass in scxml_ScxmlContentType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlcontenttype_has_any():
    assert hasattr(scxml_ScxmlContentType, "any")
    descriptor = None
    for klass in scxml_ScxmlContentType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlcontenttype_has_mixed():
    assert hasattr(scxml_ScxmlContentType, "mixed")
    descriptor = None
    for klass in scxml_ScxmlContentType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlcontenttype_has_anyAttribute():
    assert hasattr(scxml_ScxmlContentType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlContentType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlcanceltype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlCancelType)


def test_scxml_scxmlcanceltype_constructor_exists():
    assert callable(scxml_ScxmlCancelType.__init__)


def test_scxml_scxmlcanceltype_constructor_args():
    sig = inspect.signature(scxml_ScxmlCancelType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "sendid" in params, "Missing parameter 'sendid'"
    assert "sendidexpr" in params, "Missing parameter 'sendidexpr'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml_scxmlcanceltype_has_anyAttribute():
    assert hasattr(scxml_ScxmlCancelType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlCancelType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlcanceltype_has_scxmlExtraContent():
    assert hasattr(scxml_ScxmlCancelType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml_ScxmlCancelType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlcanceltype_has_sendid():
    assert hasattr(scxml_ScxmlCancelType, "sendid")
    descriptor = None
    for klass in scxml_ScxmlCancelType.__mro__:
        if "sendid" in klass.__dict__:
            descriptor = klass.__dict__["sendid"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlcanceltype_has_sendidexpr():
    assert hasattr(scxml_ScxmlCancelType, "sendidexpr")
    descriptor = None
    for klass in scxml_ScxmlCancelType.__mro__:
        if "sendidexpr" in klass.__dict__:
            descriptor = klass.__dict__["sendidexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlcanceltype_has_any():
    assert hasattr(scxml_ScxmlCancelType, "any")
    descriptor = None
    for klass in scxml_ScxmlCancelType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlforeachtype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlForeachType)


def test_scxml_scxmlforeachtype_constructor_exists():
    assert callable(scxml_ScxmlForeachType.__init__)


def test_scxml_scxmlforeachtype_constructor_args():
    sig = inspect.signature(scxml_ScxmlForeachType.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "any" in params, "Missing parameter 'any'"
    assert "array" in params, "Missing parameter 'array'"
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "item" in params, "Missing parameter 'item'"

def test_scxml_scxmlforeachtype_has_index():
    assert hasattr(scxml_ScxmlForeachType, "index")
    descriptor = None
    for klass in scxml_ScxmlForeachType.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlforeachtype_has_any():
    assert hasattr(scxml_ScxmlForeachType, "any")
    descriptor = None
    for klass in scxml_ScxmlForeachType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlforeachtype_has_array():
    assert hasattr(scxml_ScxmlForeachType, "array")
    descriptor = None
    for klass in scxml_ScxmlForeachType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlforeachtype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml_ScxmlForeachType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml_ScxmlForeachType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlforeachtype_has_anyAttribute():
    assert hasattr(scxml_ScxmlForeachType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlForeachType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlforeachtype_has_item():
    assert hasattr(scxml_ScxmlForeachType, "item")
    descriptor = None
    for klass in scxml_ScxmlForeachType.__mro__:
        if "item" in klass.__dict__:
            descriptor = klass.__dict__["item"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlfinalizetype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlFinalizeType)


def test_scxml_scxmlfinalizetype_constructor_exists():
    assert callable(scxml_ScxmlFinalizeType.__init__)


def test_scxml_scxmlfinalizetype_constructor_args():
    sig = inspect.signature(scxml_ScxmlFinalizeType.__init__)
    params = list(sig.parameters.keys())
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml_scxmlfinalizetype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml_ScxmlFinalizeType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml_ScxmlFinalizeType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlfinalizetype_has_anyAttribute():
    assert hasattr(scxml_ScxmlFinalizeType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlFinalizeType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlfinalizetype_has_any():
    assert hasattr(scxml_ScxmlFinalizeType, "any")
    descriptor = None
    for klass in scxml_ScxmlFinalizeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlfinaltype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlFinalType)


def test_scxml_scxmlfinaltype_constructor_exists():
    assert callable(scxml_ScxmlFinalType.__init__)


def test_scxml_scxmlfinaltype_constructor_args():
    sig = inspect.signature(scxml_ScxmlFinalType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "id" in params, "Missing parameter 'id'"
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlFinalMix" in params, "Missing parameter 'scxmlFinalMix'"

def test_scxml_scxmlfinaltype_has_anyAttribute():
    assert hasattr(scxml_ScxmlFinalType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlFinalType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlfinaltype_has_id():
    assert hasattr(scxml_ScxmlFinalType, "id")
    descriptor = None
    for klass in scxml_ScxmlFinalType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlfinaltype_has_any():
    assert hasattr(scxml_ScxmlFinalType, "any")
    descriptor = None
    for klass in scxml_ScxmlFinalType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlfinaltype_has_scxmlFinalMix():
    assert hasattr(scxml_ScxmlFinalType, "scxmlFinalMix")
    descriptor = None
    for klass in scxml_ScxmlFinalType.__mro__:
        if "scxmlFinalMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlFinalMix"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlelseiftype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlElseifType)


def test_scxml_scxmlelseiftype_constructor_exists():
    assert callable(scxml_ScxmlElseifType.__init__)


def test_scxml_scxmlelseiftype_constructor_args():
    sig = inspect.signature(scxml_ScxmlElseifType.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml_scxmlelseiftype_has_cond():
    assert hasattr(scxml_ScxmlElseifType, "cond")
    descriptor = None
    for klass in scxml_ScxmlElseifType.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlelseiftype_has_anyAttribute():
    assert hasattr(scxml_ScxmlElseifType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlElseifType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlelsetype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlElseType)


def test_scxml_scxmlelsetype_constructor_exists():
    assert callable(scxml_ScxmlElseType.__init__)


def test_scxml_scxmlelsetype_constructor_args():
    sig = inspect.signature(scxml_ScxmlElseType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml_scxmlelsetype_has_anyAttribute():
    assert hasattr(scxml_ScxmlElseType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlElseType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml_scxmlassigntype_is_not_abstract():
    assert not inspect.isabstract(scxml_ScxmlAssignType)


def test_scxml_scxmlassigntype_constructor_exists():
    assert callable(scxml_ScxmlAssignType.__init__)


def test_scxml_scxmlassigntype_constructor_args():
    sig = inspect.signature(scxml_ScxmlAssignType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "location" in params, "Missing parameter 'location'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "attr" in params, "Missing parameter 'attr'"
    assert "any" in params, "Missing parameter 'any'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_scxml_scxmlassigntype_has_anyAttribute():
    assert hasattr(scxml_ScxmlAssignType, "anyAttribute")
    descriptor = None
    for klass in scxml_ScxmlAssignType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlassigntype_has_location():
    assert hasattr(scxml_ScxmlAssignType, "location")
    descriptor = None
    for klass in scxml_ScxmlAssignType.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlassigntype_has_expr():
    assert hasattr(scxml_ScxmlAssignType, "expr")
    descriptor = None
    for klass in scxml_ScxmlAssignType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlassigntype_has_attr():
    assert hasattr(scxml_ScxmlAssignType, "attr")
    descriptor = None
    for klass in scxml_ScxmlAssignType.__mro__:
        if "attr" in klass.__dict__:
            descriptor = klass.__dict__["attr"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlassigntype_has_any():
    assert hasattr(scxml_ScxmlAssignType, "any")
    descriptor = None
    for klass in scxml_ScxmlAssignType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlassigntype_has_type():
    assert hasattr(scxml_ScxmlAssignType, "type")
    descriptor = None
    for klass in scxml_ScxmlAssignType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml_scxmlassigntype_has_mixed():
    assert hasattr(scxml_ScxmlAssignType, "mixed")
    descriptor = None
    for klass in scxml_ScxmlAssignType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



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

def test_assigntypedatatype_exists():
    # Check that the Enumeration exists
    assert AssignTypeDatatype is not None

def test_assigntypedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignTypeDatatype]
    expected_literals = [
        "replacechildren",
        "replace",
        "delete",
        "addattribute",
        "lastchild",
        "firstchild",
        "previoussibling",
        "nextsibling",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignTypeDatatype"

def test_exmodedatatype_exists():
    # Check that the Enumeration exists
    assert ExmodeDatatype is not None

def test_exmodedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExmodeDatatype]
    expected_literals = [
        "strict",
        "lax",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExmodeDatatype"

def test_historytypedatatype_exists():
    # Check that the Enumeration exists
    assert HistoryTypeDatatype is not None

def test_historytypedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HistoryTypeDatatype]
    expected_literals = [
        "deep",
        "shallow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HistoryTypeDatatype"

def test_bindingdatatype_exists():
    # Check that the Enumeration exists
    assert BindingDatatype is not None

def test_bindingdatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BindingDatatype]
    expected_literals = [
        "late",
        "early",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BindingDatatype"

def test_booleandatatype_exists():
    # Check that the Enumeration exists
    assert BooleanDatatype is not None

def test_booleandatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanDatatype]
    expected_literals = [
        "true",
        "false",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanDatatype"

def test_transitiontypedatatype_exists():
    # Check that the Enumeration exists
    assert TransitionTypeDatatype is not None

def test_transitiontypedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionTypeDatatype]
    expected_literals = [
        "internal",
        "external",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionTypeDatatype"


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
scxml_ScxmlTransitionType_strategy = st.builds(
    scxml_ScxmlTransitionType,
    any=
        safe_text,
    target=
        safe_text,
    anyAttribute=
        safe_text,
    scxmlCoreExecutablecontent=
        safe_text,
    type=
        safe_text,
    cond=
        safe_text,
    event=
        safe_text
)
scxml_ScxmlStateType_strategy = st.builds(
    scxml_ScxmlStateType,
    initial1=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    id=
        safe_text,
    scxmlStateMix=
        safe_text
)
scxml_ScxmlSendType_strategy = st.builds(
    scxml_ScxmlSendType,
    any=
        safe_text,
    idlocation=
        safe_text,
    targetexpr=
        safe_text,
    scxmlSendMix=
        safe_text,
    delayexpr=
        safe_text,
    event=
        safe_text,
    delay=
        safe_text,
    namelist=
        safe_text,
    type=
        safe_text,
    eventexpr=
        safe_text,
    typeexpr=
        safe_text,
    target=
        safe_text,
    anyAttribute=
        safe_text,
    id=
        safe_text
)
scxml_ScxmlScxmlType_strategy = st.builds(
    scxml_ScxmlScxmlType,
    exmode=
        safe_text,
    scxmlScxmlMix=
        safe_text,
    anyAttribute=
        safe_text,
    name=
        safe_text,
    any=
        safe_text,
    datamodel1=
        safe_text,
    initial=
        safe_text,
    binding=
        safe_text,
    version=
        safe_text
)
scxml_ScxmlScriptType_strategy = st.builds(
    scxml_ScxmlScriptType,
    src=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text,
    scxmlExtraContent=
        safe_text,
    any=
        safe_text
)
scxml_ScxmlLogType_strategy = st.builds(
    scxml_ScxmlLogType,
    anyAttribute=
        safe_text,
    expr=
        safe_text,
    label=
        safe_text,
    any=
        safe_text,
    scxmlExtraContent=
        safe_text
)
scxml_ScxmlInvokeType_strategy = st.builds(
    scxml_ScxmlInvokeType,
    any=
        safe_text,
    scxmlInvokeMix=
        safe_text,
    autoforward=
        safe_text,
    typeexpr=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text,
    idlocation=
        safe_text,
    namelist=
        safe_text,
    srcexpr=
        safe_text,
    src=
        safe_text,
    id=
        safe_text
)
scxml_ScxmlInitialType_strategy = st.builds(
    scxml_ScxmlInitialType,
    any=
        safe_text,
    scxmlExtraContent1=
        safe_text,
    any1=
        safe_text,
    scxmlExtraContent=
        safe_text,
    anyAttribute=
        safe_text
)
scxml_ScxmlIfType_strategy = st.builds(
    scxml_ScxmlIfType,
    anyAttribute=
        safe_text,
    cond=
        safe_text,
    any2=
        safe_text,
    scxmlCoreExecutablecontent1=
        safe_text,
    scxmlCoreExecutablecontent2=
        safe_text,
    any1=
        safe_text,
    any=
        safe_text,
    scxmlCoreExecutablecontent=
        safe_text
)
scxml_ScxmlHistoryType_strategy = st.builds(
    scxml_ScxmlHistoryType,
    scxmlExtraContent=
        safe_text,
    anyAttribute=
        safe_text,
    any1=
        safe_text,
    any=
        safe_text,
    type=
        safe_text,
    scxmlExtraContent1=
        safe_text,
    id=
        safe_text
)
scxml_ScxmlRaiseType_strategy = st.builds(
    scxml_ScxmlRaiseType,
    event=
        safe_text,
    anyAttribute=
        safe_text
)
scxml_ScxmlParamType_strategy = st.builds(
    scxml_ScxmlParamType,
    any=
        safe_text,
    expr=
        safe_text,
    location=
        safe_text,
    name=
        safe_text,
    scxmlExtraContent=
        safe_text,
    anyAttribute=
        safe_text
)
scxml_ScxmlParallelType_strategy = st.builds(
    scxml_ScxmlParallelType,
    anyAttribute=
        safe_text,
    scxmlParallelMix=
        safe_text,
    id=
        safe_text,
    any=
        safe_text
)
scxml_ScxmlOnexitType_strategy = st.builds(
    scxml_ScxmlOnexitType,
    any=
        safe_text,
    scxmlCoreExecutablecontent=
        safe_text,
    anyAttribute=
        safe_text
)
scxml_ScxmlOnentryType_strategy = st.builds(
    scxml_ScxmlOnentryType,
    scxmlCoreExecutablecontent=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
scxml_ScxmlDonedataType_strategy = st.builds(
    scxml_ScxmlDonedataType,
    anyAttribute=
        safe_text
)
scxml_ScxmlDatamodelType_strategy = st.builds(
    scxml_ScxmlDatamodelType,
    anyAttribute=
        safe_text,
    scxmlExtraContent=
        safe_text,
    any=
        safe_text
)
scxml_ScxmlDataType_strategy = st.builds(
    scxml_ScxmlDataType,
    src=
        safe_text,
    id=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    expr=
        safe_text,
    mixed=
        safe_text
)
scxml_ScxmlContentType_strategy = st.builds(
    scxml_ScxmlContentType,
    expr=
        safe_text,
    any=
        safe_text,
    mixed=
        safe_text,
    anyAttribute=
        safe_text
)
scxml_ScxmlCancelType_strategy = st.builds(
    scxml_ScxmlCancelType,
    anyAttribute=
        safe_text,
    scxmlExtraContent=
        safe_text,
    sendid=
        safe_text,
    sendidexpr=
        safe_text,
    any=
        safe_text
)
scxml_ScxmlForeachType_strategy = st.builds(
    scxml_ScxmlForeachType,
    index=
        safe_text,
    any=
        safe_text,
    array=
        safe_text,
    scxmlCoreExecutablecontent=
        safe_text,
    anyAttribute=
        safe_text,
    item=
        safe_text
)
scxml_ScxmlFinalizeType_strategy = st.builds(
    scxml_ScxmlFinalizeType,
    scxmlCoreExecutablecontent=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
scxml_ScxmlFinalType_strategy = st.builds(
    scxml_ScxmlFinalType,
    anyAttribute=
        safe_text,
    id=
        safe_text,
    any=
        safe_text,
    scxmlFinalMix=
        safe_text
)
scxml_ScxmlElseifType_strategy = st.builds(
    scxml_ScxmlElseifType,
    cond=
        safe_text,
    anyAttribute=
        safe_text
)
scxml_ScxmlElseType_strategy = st.builds(
    scxml_ScxmlElseType,
    anyAttribute=
        safe_text
)
scxml_ScxmlAssignType_strategy = st.builds(
    scxml_ScxmlAssignType,
    anyAttribute=
        safe_text,
    location=
        safe_text,
    expr=
        safe_text,
    attr=
        safe_text,
    any=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text
)
scxml_EStringToStringMapEntry_strategy = st.builds(
    scxml_EStringToStringMapEntry,
)
scxml_DocumentRoot_strategy = st.builds(
    scxml_DocumentRoot,
    mixed=
        safe_text
)

@given(instance=scxml_ScxmlTransitionType_strategy)
@settings(max_examples=50)
def test_scxml_scxmltransitiontype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlTransitionType)



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_ScxmlTransitionType_strategy)
def test_scxml_scxmltransitiontype_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original



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
def test_scxml_scxmlstatetype_initial1_setter(instance):
    original = instance.initial1
    instance.initial1 = original
    assert instance.initial1 == original



@given(instance=scxml_ScxmlStateType_strategy)
def test_scxml_scxmlstatetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlStateType_strategy)
def test_scxml_scxmlstatetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlStateType_strategy)
def test_scxml_scxmlstatetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_ScxmlStateType_strategy)
def test_scxml_scxmlstatetype_scxmlStateMix_setter(instance):
    original = instance.scxmlStateMix
    instance.scxmlStateMix = original
    assert instance.scxmlStateMix == original

@given(instance=scxml_ScxmlSendType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlsendtype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlSendType)



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_targetexpr_setter(instance):
    original = instance.targetexpr
    instance.targetexpr = original
    assert instance.targetexpr == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_scxmlSendMix_setter(instance):
    original = instance.scxmlSendMix
    instance.scxmlSendMix = original
    assert instance.scxmlSendMix == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_delayexpr_setter(instance):
    original = instance.delayexpr
    instance.delayexpr = original
    assert instance.delayexpr == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_eventexpr_setter(instance):
    original = instance.eventexpr
    instance.eventexpr = original
    assert instance.eventexpr == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlSendType_strategy)
def test_scxml_scxmlsendtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml_ScxmlScxmlType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlscxmltype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlScxmlType)



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_exmode_setter(instance):
    original = instance.exmode
    instance.exmode = original
    assert instance.exmode == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_scxmlScxmlMix_setter(instance):
    original = instance.scxmlScxmlMix
    instance.scxmlScxmlMix = original
    assert instance.scxmlScxmlMix == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_datamodel1_setter(instance):
    original = instance.datamodel1
    instance.datamodel1 = original
    assert instance.datamodel1 == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original



@given(instance=scxml_ScxmlScxmlType_strategy)
def test_scxml_scxmlscxmltype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=scxml_ScxmlScriptType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlscripttype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlScriptType)



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original



@given(instance=scxml_ScxmlScriptType_strategy)
def test_scxml_scxmlscripttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml_ScxmlLogType_strategy)
@settings(max_examples=50)
def test_scxml_scxmllogtype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlLogType)



@given(instance=scxml_ScxmlLogType_strategy)
def test_scxml_scxmllogtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlLogType_strategy)
def test_scxml_scxmllogtype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_ScxmlLogType_strategy)
def test_scxml_scxmllogtype_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=scxml_ScxmlLogType_strategy)
def test_scxml_scxmllogtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlLogType_strategy)
def test_scxml_scxmllogtype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml_ScxmlInvokeType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlinvoketype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlInvokeType)



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_scxmlInvokeMix_setter(instance):
    original = instance.scxmlInvokeMix
    instance.scxmlInvokeMix = original
    assert instance.scxmlInvokeMix == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_autoforward_setter(instance):
    original = instance.autoforward
    instance.autoforward = original
    assert instance.autoforward == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_srcexpr_setter(instance):
    original = instance.srcexpr
    instance.srcexpr = original
    assert instance.srcexpr == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=scxml_ScxmlInvokeType_strategy)
def test_scxml_scxmlinvoketype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml_ScxmlInitialType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlinitialtype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlInitialType)



@given(instance=scxml_ScxmlInitialType_strategy)
def test_scxml_scxmlinitialtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlInitialType_strategy)
def test_scxml_scxmlinitialtype_scxmlExtraContent1_setter(instance):
    original = instance.scxmlExtraContent1
    instance.scxmlExtraContent1 = original
    assert instance.scxmlExtraContent1 == original



@given(instance=scxml_ScxmlInitialType_strategy)
def test_scxml_scxmlinitialtype_any1_setter(instance):
    original = instance.any1
    instance.any1 = original
    assert instance.any1 == original



@given(instance=scxml_ScxmlInitialType_strategy)
def test_scxml_scxmlinitialtype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original



@given(instance=scxml_ScxmlInitialType_strategy)
def test_scxml_scxmlinitialtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml_ScxmlIfType_strategy)
@settings(max_examples=50)
def test_scxml_scxmliftype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlIfType)



@given(instance=scxml_ScxmlIfType_strategy)
def test_scxml_scxmliftype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlIfType_strategy)
def test_scxml_scxmliftype_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original



@given(instance=scxml_ScxmlIfType_strategy)
def test_scxml_scxmliftype_any2_setter(instance):
    original = instance.any2
    instance.any2 = original
    assert instance.any2 == original



@given(instance=scxml_ScxmlIfType_strategy)
def test_scxml_scxmliftype_scxmlCoreExecutablecontent1_setter(instance):
    original = instance.scxmlCoreExecutablecontent1
    instance.scxmlCoreExecutablecontent1 = original
    assert instance.scxmlCoreExecutablecontent1 == original



@given(instance=scxml_ScxmlIfType_strategy)
def test_scxml_scxmliftype_scxmlCoreExecutablecontent2_setter(instance):
    original = instance.scxmlCoreExecutablecontent2
    instance.scxmlCoreExecutablecontent2 = original
    assert instance.scxmlCoreExecutablecontent2 == original



@given(instance=scxml_ScxmlIfType_strategy)
def test_scxml_scxmliftype_any1_setter(instance):
    original = instance.any1
    instance.any1 = original
    assert instance.any1 == original



@given(instance=scxml_ScxmlIfType_strategy)
def test_scxml_scxmliftype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlIfType_strategy)
def test_scxml_scxmliftype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original

@given(instance=scxml_ScxmlHistoryType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlhistorytype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlHistoryType)



@given(instance=scxml_ScxmlHistoryType_strategy)
def test_scxml_scxmlhistorytype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original



@given(instance=scxml_ScxmlHistoryType_strategy)
def test_scxml_scxmlhistorytype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlHistoryType_strategy)
def test_scxml_scxmlhistorytype_any1_setter(instance):
    original = instance.any1
    instance.any1 = original
    assert instance.any1 == original



@given(instance=scxml_ScxmlHistoryType_strategy)
def test_scxml_scxmlhistorytype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlHistoryType_strategy)
def test_scxml_scxmlhistorytype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_ScxmlHistoryType_strategy)
def test_scxml_scxmlhistorytype_scxmlExtraContent1_setter(instance):
    original = instance.scxmlExtraContent1
    instance.scxmlExtraContent1 = original
    assert instance.scxmlExtraContent1 == original



@given(instance=scxml_ScxmlHistoryType_strategy)
def test_scxml_scxmlhistorytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml_ScxmlRaiseType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlraisetype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlRaiseType)



@given(instance=scxml_ScxmlRaiseType_strategy)
def test_scxml_scxmlraisetype_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=scxml_ScxmlRaiseType_strategy)
def test_scxml_scxmlraisetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml_ScxmlParamType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlparamtype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlParamType)



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original



@given(instance=scxml_ScxmlParamType_strategy)
def test_scxml_scxmlparamtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml_ScxmlParallelType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlparalleltype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlParallelType)



@given(instance=scxml_ScxmlParallelType_strategy)
def test_scxml_scxmlparalleltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlParallelType_strategy)
def test_scxml_scxmlparalleltype_scxmlParallelMix_setter(instance):
    original = instance.scxmlParallelMix
    instance.scxmlParallelMix = original
    assert instance.scxmlParallelMix == original



@given(instance=scxml_ScxmlParallelType_strategy)
def test_scxml_scxmlparalleltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_ScxmlParallelType_strategy)
def test_scxml_scxmlparalleltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml_ScxmlOnexitType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlonexittype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlOnexitType)



@given(instance=scxml_ScxmlOnexitType_strategy)
def test_scxml_scxmlonexittype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlOnexitType_strategy)
def test_scxml_scxmlonexittype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original



@given(instance=scxml_ScxmlOnexitType_strategy)
def test_scxml_scxmlonexittype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml_ScxmlOnentryType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlonentrytype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlOnentryType)



@given(instance=scxml_ScxmlOnentryType_strategy)
def test_scxml_scxmlonentrytype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original



@given(instance=scxml_ScxmlOnentryType_strategy)
def test_scxml_scxmlonentrytype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlOnentryType_strategy)
def test_scxml_scxmlonentrytype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml_ScxmlDonedataType_strategy)
@settings(max_examples=50)
def test_scxml_scxmldonedatatype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlDonedataType)



@given(instance=scxml_ScxmlDonedataType_strategy)
def test_scxml_scxmldonedatatype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml_ScxmlDatamodelType_strategy)
@settings(max_examples=50)
def test_scxml_scxmldatamodeltype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlDatamodelType)



@given(instance=scxml_ScxmlDatamodelType_strategy)
def test_scxml_scxmldatamodeltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlDatamodelType_strategy)
def test_scxml_scxmldatamodeltype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original



@given(instance=scxml_ScxmlDatamodelType_strategy)
def test_scxml_scxmldatamodeltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml_ScxmlDataType_strategy)
@settings(max_examples=50)
def test_scxml_scxmldatatype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlDataType)



@given(instance=scxml_ScxmlDataType_strategy)
def test_scxml_scxmldatatype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=scxml_ScxmlDataType_strategy)
def test_scxml_scxmldatatype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_ScxmlDataType_strategy)
def test_scxml_scxmldatatype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlDataType_strategy)
def test_scxml_scxmldatatype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlDataType_strategy)
def test_scxml_scxmldatatype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_ScxmlDataType_strategy)
def test_scxml_scxmldatatype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=scxml_ScxmlContentType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlcontenttype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlContentType)



@given(instance=scxml_ScxmlContentType_strategy)
def test_scxml_scxmlcontenttype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_ScxmlContentType_strategy)
def test_scxml_scxmlcontenttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlContentType_strategy)
def test_scxml_scxmlcontenttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=scxml_ScxmlContentType_strategy)
def test_scxml_scxmlcontenttype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml_ScxmlCancelType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlcanceltype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlCancelType)



@given(instance=scxml_ScxmlCancelType_strategy)
def test_scxml_scxmlcanceltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlCancelType_strategy)
def test_scxml_scxmlcanceltype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original



@given(instance=scxml_ScxmlCancelType_strategy)
def test_scxml_scxmlcanceltype_sendid_setter(instance):
    original = instance.sendid
    instance.sendid = original
    assert instance.sendid == original



@given(instance=scxml_ScxmlCancelType_strategy)
def test_scxml_scxmlcanceltype_sendidexpr_setter(instance):
    original = instance.sendidexpr
    instance.sendidexpr = original
    assert instance.sendidexpr == original



@given(instance=scxml_ScxmlCancelType_strategy)
def test_scxml_scxmlcanceltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml_ScxmlForeachType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlforeachtype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlForeachType)



@given(instance=scxml_ScxmlForeachType_strategy)
def test_scxml_scxmlforeachtype_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=scxml_ScxmlForeachType_strategy)
def test_scxml_scxmlforeachtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlForeachType_strategy)
def test_scxml_scxmlforeachtype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original



@given(instance=scxml_ScxmlForeachType_strategy)
def test_scxml_scxmlforeachtype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original



@given(instance=scxml_ScxmlForeachType_strategy)
def test_scxml_scxmlforeachtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlForeachType_strategy)
def test_scxml_scxmlforeachtype_item_setter(instance):
    original = instance.item
    instance.item = original
    assert instance.item == original

@given(instance=scxml_ScxmlFinalizeType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlfinalizetype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlFinalizeType)



@given(instance=scxml_ScxmlFinalizeType_strategy)
def test_scxml_scxmlfinalizetype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original



@given(instance=scxml_ScxmlFinalizeType_strategy)
def test_scxml_scxmlfinalizetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlFinalizeType_strategy)
def test_scxml_scxmlfinalizetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml_ScxmlFinalType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlfinaltype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlFinalType)



@given(instance=scxml_ScxmlFinalType_strategy)
def test_scxml_scxmlfinaltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlFinalType_strategy)
def test_scxml_scxmlfinaltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_ScxmlFinalType_strategy)
def test_scxml_scxmlfinaltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlFinalType_strategy)
def test_scxml_scxmlfinaltype_scxmlFinalMix_setter(instance):
    original = instance.scxmlFinalMix
    instance.scxmlFinalMix = original
    assert instance.scxmlFinalMix == original

@given(instance=scxml_ScxmlElseifType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlelseiftype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlElseifType)



@given(instance=scxml_ScxmlElseifType_strategy)
def test_scxml_scxmlelseiftype_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original



@given(instance=scxml_ScxmlElseifType_strategy)
def test_scxml_scxmlelseiftype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml_ScxmlElseType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlelsetype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlElseType)



@given(instance=scxml_ScxmlElseType_strategy)
def test_scxml_scxmlelsetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml_ScxmlAssignType_strategy)
@settings(max_examples=50)
def test_scxml_scxmlassigntype_instantiation(instance):
    assert isinstance(instance, scxml_ScxmlAssignType)



@given(instance=scxml_ScxmlAssignType_strategy)
def test_scxml_scxmlassigntype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original



@given(instance=scxml_ScxmlAssignType_strategy)
def test_scxml_scxmlassigntype_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=scxml_ScxmlAssignType_strategy)
def test_scxml_scxmlassigntype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_ScxmlAssignType_strategy)
def test_scxml_scxmlassigntype_attr_setter(instance):
    original = instance.attr
    instance.attr = original
    assert instance.attr == original



@given(instance=scxml_ScxmlAssignType_strategy)
def test_scxml_scxmlassigntype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=scxml_ScxmlAssignType_strategy)
def test_scxml_scxmlassigntype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_ScxmlAssignType_strategy)
def test_scxml_scxmlassigntype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

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
