import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scxml::ScxmlTransitionType,
    scxml::ScxmlStateType,
    scxml::ScxmlSendType,
    scxml::ScxmlScxmlType,
    scxml::ScxmlScriptType,
    scxml::ScxmlLogType,
    scxml::ScxmlInvokeType,
    scxml::ScxmlInitialType,
    scxml::ScxmlIfType,
    scxml::ScxmlHistoryType,
    scxml::ScxmlRaiseType,
    scxml::ScxmlParamType,
    scxml::ScxmlParallelType,
    scxml::ScxmlOnexitType,
    scxml::ScxmlOnentryType,
    scxml::ScxmlDonedataType,
    scxml::ScxmlDatamodelType,
    scxml::ScxmlDataType,
    scxml::ScxmlContentType,
    scxml::ScxmlCancelType,
    scxml::ScxmlForeachType,
    scxml::ScxmlFinalizeType,
    scxml::ScxmlFinalType,
    scxml::ScxmlElseifType,
    scxml::ScxmlElseType,
    scxml::ScxmlAssignType,
    scxml::EStringToStringMapEntry,
    scxml::DocumentRoot,
    BooleanDatatype,
    HistoryTypeDatatype,
    BindingDatatype,
    AssignTypeDatatype,
    TransitionTypeDatatype,
    ExmodeDatatype,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scxml::scxmltransitiontype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlTransitionType)


def test_scxml::scxmltransitiontype_constructor_exists():
    assert callable(scxml::ScxmlTransitionType.__init__)


def test_scxml::scxmltransitiontype_constructor_args():
    sig = inspect.signature(scxml::ScxmlTransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"
    assert "event" in params, "Missing parameter 'event'"
    assert "target" in params, "Missing parameter 'target'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "type" in params, "Missing parameter 'type'"

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

def test_scxml::scxmltransitiontype_has_target():
    assert hasattr(scxml::ScxmlTransitionType, "target")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
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

def test_scxml::scxmltransitiontype_has_anyAttribute():
    assert hasattr(scxml::ScxmlTransitionType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmltransitiontype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml::ScxmlTransitionType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmltransitiontype_has_type():
    assert hasattr(scxml::ScxmlTransitionType, "type")
    descriptor = None
    for klass in scxml::ScxmlTransitionType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlstatetype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlStateType)


def test_scxml::scxmlstatetype_constructor_exists():
    assert callable(scxml::ScxmlStateType.__init__)


def test_scxml::scxmlstatetype_constructor_args():
    sig = inspect.signature(scxml::ScxmlStateType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlStateMix" in params, "Missing parameter 'scxmlStateMix'"
    assert "id" in params, "Missing parameter 'id'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "initial1" in params, "Missing parameter 'initial1'"

def test_scxml::scxmlstatetype_has_any():
    assert hasattr(scxml::ScxmlStateType, "any")
    descriptor = None
    for klass in scxml::ScxmlStateType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlstatetype_has_scxmlStateMix():
    assert hasattr(scxml::ScxmlStateType, "scxmlStateMix")
    descriptor = None
    for klass in scxml::ScxmlStateType.__mro__:
        if "scxmlStateMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlStateMix"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlstatetype_has_id():
    assert hasattr(scxml::ScxmlStateType, "id")
    descriptor = None
    for klass in scxml::ScxmlStateType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlstatetype_has_anyAttribute():
    assert hasattr(scxml::ScxmlStateType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlStateType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlstatetype_has_initial1():
    assert hasattr(scxml::ScxmlStateType, "initial1")
    descriptor = None
    for klass in scxml::ScxmlStateType.__mro__:
        if "initial1" in klass.__dict__:
            descriptor = klass.__dict__["initial1"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlsendtype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlSendType)


def test_scxml::scxmlsendtype_constructor_exists():
    assert callable(scxml::ScxmlSendType.__init__)


def test_scxml::scxmlsendtype_constructor_args():
    sig = inspect.signature(scxml::ScxmlSendType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "any" in params, "Missing parameter 'any'"
    assert "delayexpr" in params, "Missing parameter 'delayexpr'"
    assert "targetexpr" in params, "Missing parameter 'targetexpr'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "target" in params, "Missing parameter 'target'"
    assert "event" in params, "Missing parameter 'event'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "scxmlSendMix" in params, "Missing parameter 'scxmlSendMix'"
    assert "eventexpr" in params, "Missing parameter 'eventexpr'"

def test_scxml::scxmlsendtype_has_id():
    assert hasattr(scxml::ScxmlSendType, "id")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_type():
    assert hasattr(scxml::ScxmlSendType, "type")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_any():
    assert hasattr(scxml::ScxmlSendType, "any")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_delayexpr():
    assert hasattr(scxml::ScxmlSendType, "delayexpr")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "delayexpr" in klass.__dict__:
            descriptor = klass.__dict__["delayexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_targetexpr():
    assert hasattr(scxml::ScxmlSendType, "targetexpr")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "targetexpr" in klass.__dict__:
            descriptor = klass.__dict__["targetexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_delay():
    assert hasattr(scxml::ScxmlSendType, "delay")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "delay" in klass.__dict__:
            descriptor = klass.__dict__["delay"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_anyAttribute():
    assert hasattr(scxml::ScxmlSendType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_target():
    assert hasattr(scxml::ScxmlSendType, "target")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_event():
    assert hasattr(scxml::ScxmlSendType, "event")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_idlocation():
    assert hasattr(scxml::ScxmlSendType, "idlocation")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "idlocation" in klass.__dict__:
            descriptor = klass.__dict__["idlocation"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_typeexpr():
    assert hasattr(scxml::ScxmlSendType, "typeexpr")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_namelist():
    assert hasattr(scxml::ScxmlSendType, "namelist")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "namelist" in klass.__dict__:
            descriptor = klass.__dict__["namelist"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_scxmlSendMix():
    assert hasattr(scxml::ScxmlSendType, "scxmlSendMix")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "scxmlSendMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlSendMix"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlsendtype_has_eventexpr():
    assert hasattr(scxml::ScxmlSendType, "eventexpr")
    descriptor = None
    for klass in scxml::ScxmlSendType.__mro__:
        if "eventexpr" in klass.__dict__:
            descriptor = klass.__dict__["eventexpr"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlscxmltype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlScxmlType)


def test_scxml::scxmlscxmltype_constructor_exists():
    assert callable(scxml::ScxmlScxmlType.__init__)


def test_scxml::scxmlscxmltype_constructor_args():
    sig = inspect.signature(scxml::ScxmlScxmlType.__init__)
    params = list(sig.parameters.keys())
    assert "exmode" in params, "Missing parameter 'exmode'"
    assert "binding" in params, "Missing parameter 'binding'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlScxmlMix" in params, "Missing parameter 'scxmlScxmlMix'"
    assert "version" in params, "Missing parameter 'version'"
    assert "datamodel1" in params, "Missing parameter 'datamodel1'"
    assert "name" in params, "Missing parameter 'name'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml::scxmlscxmltype_has_exmode():
    assert hasattr(scxml::ScxmlScxmlType, "exmode")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "exmode" in klass.__dict__:
            descriptor = klass.__dict__["exmode"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscxmltype_has_binding():
    assert hasattr(scxml::ScxmlScxmlType, "binding")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "binding" in klass.__dict__:
            descriptor = klass.__dict__["binding"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscxmltype_has_initial():
    assert hasattr(scxml::ScxmlScxmlType, "initial")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscxmltype_has_any():
    assert hasattr(scxml::ScxmlScxmlType, "any")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscxmltype_has_scxmlScxmlMix():
    assert hasattr(scxml::ScxmlScxmlType, "scxmlScxmlMix")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "scxmlScxmlMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlScxmlMix"]
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

def test_scxml::scxmlscxmltype_has_datamodel1():
    assert hasattr(scxml::ScxmlScxmlType, "datamodel1")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "datamodel1" in klass.__dict__:
            descriptor = klass.__dict__["datamodel1"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscxmltype_has_name():
    assert hasattr(scxml::ScxmlScxmlType, "name")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscxmltype_has_anyAttribute():
    assert hasattr(scxml::ScxmlScxmlType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlScxmlType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlscripttype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlScriptType)


def test_scxml::scxmlscripttype_constructor_exists():
    assert callable(scxml::ScxmlScriptType.__init__)


def test_scxml::scxmlscripttype_constructor_args():
    sig = inspect.signature(scxml::ScxmlScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "src" in params, "Missing parameter 'src'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml::scxmlscripttype_has_anyAttribute():
    assert hasattr(scxml::ScxmlScriptType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlScriptType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
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

def test_scxml::scxmlscripttype_has_scxmlExtraContent():
    assert hasattr(scxml::ScxmlScriptType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml::ScxmlScriptType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlscripttype_has_any():
    assert hasattr(scxml::ScxmlScriptType, "any")
    descriptor = None
    for klass in scxml::ScxmlScriptType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmllogtype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlLogType)


def test_scxml::scxmllogtype_constructor_exists():
    assert callable(scxml::ScxmlLogType.__init__)


def test_scxml::scxmllogtype_constructor_args():
    sig = inspect.signature(scxml::ScxmlLogType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "label" in params, "Missing parameter 'label'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"

def test_scxml::scxmllogtype_has_any():
    assert hasattr(scxml::ScxmlLogType, "any")
    descriptor = None
    for klass in scxml::ScxmlLogType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmllogtype_has_expr():
    assert hasattr(scxml::ScxmlLogType, "expr")
    descriptor = None
    for klass in scxml::ScxmlLogType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmllogtype_has_anyAttribute():
    assert hasattr(scxml::ScxmlLogType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlLogType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmllogtype_has_label():
    assert hasattr(scxml::ScxmlLogType, "label")
    descriptor = None
    for klass in scxml::ScxmlLogType.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmllogtype_has_scxmlExtraContent():
    assert hasattr(scxml::ScxmlLogType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml::ScxmlLogType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlinvoketype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlInvokeType)


def test_scxml::scxmlinvoketype_constructor_exists():
    assert callable(scxml::ScxmlInvokeType.__init__)


def test_scxml::scxmlinvoketype_constructor_args():
    sig = inspect.signature(scxml::ScxmlInvokeType.__init__)
    params = list(sig.parameters.keys())
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "srcexpr" in params, "Missing parameter 'srcexpr'"
    assert "id" in params, "Missing parameter 'id'"
    assert "autoforward" in params, "Missing parameter 'autoforward'"
    assert "scxmlInvokeMix" in params, "Missing parameter 'scxmlInvokeMix'"
    assert "type" in params, "Missing parameter 'type'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "any" in params, "Missing parameter 'any'"
    assert "src" in params, "Missing parameter 'src'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"

def test_scxml::scxmlinvoketype_has_typeexpr():
    assert hasattr(scxml::ScxmlInvokeType, "typeexpr")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "typeexpr" in klass.__dict__:
            descriptor = klass.__dict__["typeexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_srcexpr():
    assert hasattr(scxml::ScxmlInvokeType, "srcexpr")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "srcexpr" in klass.__dict__:
            descriptor = klass.__dict__["srcexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_id():
    assert hasattr(scxml::ScxmlInvokeType, "id")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_autoforward():
    assert hasattr(scxml::ScxmlInvokeType, "autoforward")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "autoforward" in klass.__dict__:
            descriptor = klass.__dict__["autoforward"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_scxmlInvokeMix():
    assert hasattr(scxml::ScxmlInvokeType, "scxmlInvokeMix")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "scxmlInvokeMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlInvokeMix"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_type():
    assert hasattr(scxml::ScxmlInvokeType, "type")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_namelist():
    assert hasattr(scxml::ScxmlInvokeType, "namelist")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "namelist" in klass.__dict__:
            descriptor = klass.__dict__["namelist"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_any():
    assert hasattr(scxml::ScxmlInvokeType, "any")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_src():
    assert hasattr(scxml::ScxmlInvokeType, "src")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_anyAttribute():
    assert hasattr(scxml::ScxmlInvokeType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinvoketype_has_idlocation():
    assert hasattr(scxml::ScxmlInvokeType, "idlocation")
    descriptor = None
    for klass in scxml::ScxmlInvokeType.__mro__:
        if "idlocation" in klass.__dict__:
            descriptor = klass.__dict__["idlocation"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlinitialtype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlInitialType)


def test_scxml::scxmlinitialtype_constructor_exists():
    assert callable(scxml::ScxmlInitialType.__init__)


def test_scxml::scxmlinitialtype_constructor_args():
    sig = inspect.signature(scxml::ScxmlInitialType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlExtraContent1" in params, "Missing parameter 'scxmlExtraContent1'"
    assert "any1" in params, "Missing parameter 'any1'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"

def test_scxml::scxmlinitialtype_has_any():
    assert hasattr(scxml::ScxmlInitialType, "any")
    descriptor = None
    for klass in scxml::ScxmlInitialType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinitialtype_has_scxmlExtraContent1():
    assert hasattr(scxml::ScxmlInitialType, "scxmlExtraContent1")
    descriptor = None
    for klass in scxml::ScxmlInitialType.__mro__:
        if "scxmlExtraContent1" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent1"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinitialtype_has_any1():
    assert hasattr(scxml::ScxmlInitialType, "any1")
    descriptor = None
    for klass in scxml::ScxmlInitialType.__mro__:
        if "any1" in klass.__dict__:
            descriptor = klass.__dict__["any1"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinitialtype_has_anyAttribute():
    assert hasattr(scxml::ScxmlInitialType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlInitialType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlinitialtype_has_scxmlExtraContent():
    assert hasattr(scxml::ScxmlInitialType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml::ScxmlInitialType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmliftype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlIfType)


def test_scxml::scxmliftype_constructor_exists():
    assert callable(scxml::ScxmlIfType.__init__)


def test_scxml::scxmliftype_constructor_args():
    sig = inspect.signature(scxml::ScxmlIfType.__init__)
    params = list(sig.parameters.keys())
    assert "any1" in params, "Missing parameter 'any1'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlCoreExecutablecontent1" in params, "Missing parameter 'scxmlCoreExecutablecontent1'"
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "any2" in params, "Missing parameter 'any2'"
    assert "cond" in params, "Missing parameter 'cond'"
    assert "scxmlCoreExecutablecontent2" in params, "Missing parameter 'scxmlCoreExecutablecontent2'"

def test_scxml::scxmliftype_has_any1():
    assert hasattr(scxml::ScxmlIfType, "any1")
    descriptor = None
    for klass in scxml::ScxmlIfType.__mro__:
        if "any1" in klass.__dict__:
            descriptor = klass.__dict__["any1"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmliftype_has_any():
    assert hasattr(scxml::ScxmlIfType, "any")
    descriptor = None
    for klass in scxml::ScxmlIfType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmliftype_has_anyAttribute():
    assert hasattr(scxml::ScxmlIfType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlIfType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmliftype_has_scxmlCoreExecutablecontent1():
    assert hasattr(scxml::ScxmlIfType, "scxmlCoreExecutablecontent1")
    descriptor = None
    for klass in scxml::ScxmlIfType.__mro__:
        if "scxmlCoreExecutablecontent1" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent1"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmliftype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml::ScxmlIfType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml::ScxmlIfType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmliftype_has_any2():
    assert hasattr(scxml::ScxmlIfType, "any2")
    descriptor = None
    for klass in scxml::ScxmlIfType.__mro__:
        if "any2" in klass.__dict__:
            descriptor = klass.__dict__["any2"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmliftype_has_cond():
    assert hasattr(scxml::ScxmlIfType, "cond")
    descriptor = None
    for klass in scxml::ScxmlIfType.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmliftype_has_scxmlCoreExecutablecontent2():
    assert hasattr(scxml::ScxmlIfType, "scxmlCoreExecutablecontent2")
    descriptor = None
    for klass in scxml::ScxmlIfType.__mro__:
        if "scxmlCoreExecutablecontent2" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent2"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlhistorytype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlHistoryType)


def test_scxml::scxmlhistorytype_constructor_exists():
    assert callable(scxml::ScxmlHistoryType.__init__)


def test_scxml::scxmlhistorytype_constructor_args():
    sig = inspect.signature(scxml::ScxmlHistoryType.__init__)
    params = list(sig.parameters.keys())
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "any1" in params, "Missing parameter 'any1'"
    assert "any" in params, "Missing parameter 'any'"
    assert "id" in params, "Missing parameter 'id'"
    assert "scxmlExtraContent1" in params, "Missing parameter 'scxmlExtraContent1'"
    assert "type" in params, "Missing parameter 'type'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml::scxmlhistorytype_has_scxmlExtraContent():
    assert hasattr(scxml::ScxmlHistoryType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml::ScxmlHistoryType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlhistorytype_has_any1():
    assert hasattr(scxml::ScxmlHistoryType, "any1")
    descriptor = None
    for klass in scxml::ScxmlHistoryType.__mro__:
        if "any1" in klass.__dict__:
            descriptor = klass.__dict__["any1"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlhistorytype_has_any():
    assert hasattr(scxml::ScxmlHistoryType, "any")
    descriptor = None
    for klass in scxml::ScxmlHistoryType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlhistorytype_has_id():
    assert hasattr(scxml::ScxmlHistoryType, "id")
    descriptor = None
    for klass in scxml::ScxmlHistoryType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlhistorytype_has_scxmlExtraContent1():
    assert hasattr(scxml::ScxmlHistoryType, "scxmlExtraContent1")
    descriptor = None
    for klass in scxml::ScxmlHistoryType.__mro__:
        if "scxmlExtraContent1" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent1"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlhistorytype_has_type():
    assert hasattr(scxml::ScxmlHistoryType, "type")
    descriptor = None
    for klass in scxml::ScxmlHistoryType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlhistorytype_has_anyAttribute():
    assert hasattr(scxml::ScxmlHistoryType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlHistoryType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlraisetype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlRaiseType)


def test_scxml::scxmlraisetype_constructor_exists():
    assert callable(scxml::ScxmlRaiseType.__init__)


def test_scxml::scxmlraisetype_constructor_args():
    sig = inspect.signature(scxml::ScxmlRaiseType.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml::scxmlraisetype_has_event():
    assert hasattr(scxml::ScxmlRaiseType, "event")
    descriptor = None
    for klass in scxml::ScxmlRaiseType.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlraisetype_has_anyAttribute():
    assert hasattr(scxml::ScxmlRaiseType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlRaiseType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlparamtype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlParamType)


def test_scxml::scxmlparamtype_constructor_exists():
    assert callable(scxml::ScxmlParamType.__init__)


def test_scxml::scxmlparamtype_constructor_args():
    sig = inspect.signature(scxml::ScxmlParamType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "location" in params, "Missing parameter 'location'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "name" in params, "Missing parameter 'name'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"

def test_scxml::scxmlparamtype_has_anyAttribute():
    assert hasattr(scxml::ScxmlParamType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlParamType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparamtype_has_any():
    assert hasattr(scxml::ScxmlParamType, "any")
    descriptor = None
    for klass in scxml::ScxmlParamType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparamtype_has_location():
    assert hasattr(scxml::ScxmlParamType, "location")
    descriptor = None
    for klass in scxml::ScxmlParamType.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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



def test_scxml::scxmlparalleltype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlParallelType)


def test_scxml::scxmlparalleltype_constructor_exists():
    assert callable(scxml::ScxmlParallelType.__init__)


def test_scxml::scxmlparalleltype_constructor_args():
    sig = inspect.signature(scxml::ScxmlParallelType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlParallelMix" in params, "Missing parameter 'scxmlParallelMix'"
    assert "id" in params, "Missing parameter 'id'"

def test_scxml::scxmlparalleltype_has_anyAttribute():
    assert hasattr(scxml::ScxmlParallelType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlParallelType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparalleltype_has_any():
    assert hasattr(scxml::ScxmlParallelType, "any")
    descriptor = None
    for klass in scxml::ScxmlParallelType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparalleltype_has_scxmlParallelMix():
    assert hasattr(scxml::ScxmlParallelType, "scxmlParallelMix")
    descriptor = None
    for klass in scxml::ScxmlParallelType.__mro__:
        if "scxmlParallelMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlParallelMix"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlparalleltype_has_id():
    assert hasattr(scxml::ScxmlParallelType, "id")
    descriptor = None
    for klass in scxml::ScxmlParallelType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlonexittype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlOnexitType)


def test_scxml::scxmlonexittype_constructor_exists():
    assert callable(scxml::ScxmlOnexitType.__init__)


def test_scxml::scxmlonexittype_constructor_args():
    sig = inspect.signature(scxml::ScxmlOnexitType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"

def test_scxml::scxmlonexittype_has_anyAttribute():
    assert hasattr(scxml::ScxmlOnexitType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlOnexitType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlonexittype_has_any():
    assert hasattr(scxml::ScxmlOnexitType, "any")
    descriptor = None
    for klass in scxml::ScxmlOnexitType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlonexittype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml::ScxmlOnexitType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml::ScxmlOnexitType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlonentrytype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlOnentryType)


def test_scxml::scxmlonentrytype_constructor_exists():
    assert callable(scxml::ScxmlOnentryType.__init__)


def test_scxml::scxmlonentrytype_constructor_args():
    sig = inspect.signature(scxml::ScxmlOnentryType.__init__)
    params = list(sig.parameters.keys())
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml::scxmlonentrytype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml::ScxmlOnentryType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml::ScxmlOnentryType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlonentrytype_has_anyAttribute():
    assert hasattr(scxml::ScxmlOnentryType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlOnentryType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlonentrytype_has_any():
    assert hasattr(scxml::ScxmlOnentryType, "any")
    descriptor = None
    for klass in scxml::ScxmlOnentryType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmldonedatatype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlDonedataType)


def test_scxml::scxmldonedatatype_constructor_exists():
    assert callable(scxml::ScxmlDonedataType.__init__)


def test_scxml::scxmldonedatatype_constructor_args():
    sig = inspect.signature(scxml::ScxmlDonedataType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml::scxmldonedatatype_has_anyAttribute():
    assert hasattr(scxml::ScxmlDonedataType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlDonedataType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmldatamodeltype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlDatamodelType)


def test_scxml::scxmldatamodeltype_constructor_exists():
    assert callable(scxml::ScxmlDatamodelType.__init__)


def test_scxml::scxmldatamodeltype_constructor_args():
    sig = inspect.signature(scxml::ScxmlDatamodelType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "any" in params, "Missing parameter 'any'"

def test_scxml::scxmldatamodeltype_has_anyAttribute():
    assert hasattr(scxml::ScxmlDatamodelType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlDatamodelType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmldatamodeltype_has_scxmlExtraContent():
    assert hasattr(scxml::ScxmlDatamodelType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml::ScxmlDatamodelType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmldatamodeltype_has_any():
    assert hasattr(scxml::ScxmlDatamodelType, "any")
    descriptor = None
    for klass in scxml::ScxmlDatamodelType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmldatatype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlDataType)


def test_scxml::scxmldatatype_constructor_exists():
    assert callable(scxml::ScxmlDataType.__init__)


def test_scxml::scxmldatatype_constructor_args():
    sig = inspect.signature(scxml::ScxmlDataType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "id" in params, "Missing parameter 'id'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "src" in params, "Missing parameter 'src'"

def test_scxml::scxmldatatype_has_any():
    assert hasattr(scxml::ScxmlDataType, "any")
    descriptor = None
    for klass in scxml::ScxmlDataType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmldatatype_has_id():
    assert hasattr(scxml::ScxmlDataType, "id")
    descriptor = None
    for klass in scxml::ScxmlDataType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmldatatype_has_anyAttribute():
    assert hasattr(scxml::ScxmlDataType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlDataType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmldatatype_has_mixed():
    assert hasattr(scxml::ScxmlDataType, "mixed")
    descriptor = None
    for klass in scxml::ScxmlDataType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmldatatype_has_expr():
    assert hasattr(scxml::ScxmlDataType, "expr")
    descriptor = None
    for klass in scxml::ScxmlDataType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmldatatype_has_src():
    assert hasattr(scxml::ScxmlDataType, "src")
    descriptor = None
    for klass in scxml::ScxmlDataType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlcontenttype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlContentType)


def test_scxml::scxmlcontenttype_constructor_exists():
    assert callable(scxml::ScxmlContentType.__init__)


def test_scxml::scxmlcontenttype_constructor_args():
    sig = inspect.signature(scxml::ScxmlContentType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "expr" in params, "Missing parameter 'expr'"

def test_scxml::scxmlcontenttype_has_mixed():
    assert hasattr(scxml::ScxmlContentType, "mixed")
    descriptor = None
    for klass in scxml::ScxmlContentType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlcontenttype_has_any():
    assert hasattr(scxml::ScxmlContentType, "any")
    descriptor = None
    for klass in scxml::ScxmlContentType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlcontenttype_has_anyAttribute():
    assert hasattr(scxml::ScxmlContentType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlContentType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlcontenttype_has_expr():
    assert hasattr(scxml::ScxmlContentType, "expr")
    descriptor = None
    for klass in scxml::ScxmlContentType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlcanceltype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlCancelType)


def test_scxml::scxmlcanceltype_constructor_exists():
    assert callable(scxml::ScxmlCancelType.__init__)


def test_scxml::scxmlcanceltype_constructor_args():
    sig = inspect.signature(scxml::ScxmlCancelType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "sendidexpr" in params, "Missing parameter 'sendidexpr'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlExtraContent" in params, "Missing parameter 'scxmlExtraContent'"
    assert "sendid" in params, "Missing parameter 'sendid'"

def test_scxml::scxmlcanceltype_has_any():
    assert hasattr(scxml::ScxmlCancelType, "any")
    descriptor = None
    for klass in scxml::ScxmlCancelType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlcanceltype_has_sendidexpr():
    assert hasattr(scxml::ScxmlCancelType, "sendidexpr")
    descriptor = None
    for klass in scxml::ScxmlCancelType.__mro__:
        if "sendidexpr" in klass.__dict__:
            descriptor = klass.__dict__["sendidexpr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlcanceltype_has_anyAttribute():
    assert hasattr(scxml::ScxmlCancelType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlCancelType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlcanceltype_has_scxmlExtraContent():
    assert hasattr(scxml::ScxmlCancelType, "scxmlExtraContent")
    descriptor = None
    for klass in scxml::ScxmlCancelType.__mro__:
        if "scxmlExtraContent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlExtraContent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlcanceltype_has_sendid():
    assert hasattr(scxml::ScxmlCancelType, "sendid")
    descriptor = None
    for klass in scxml::ScxmlCancelType.__mro__:
        if "sendid" in klass.__dict__:
            descriptor = klass.__dict__["sendid"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlforeachtype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlForeachType)


def test_scxml::scxmlforeachtype_constructor_exists():
    assert callable(scxml::ScxmlForeachType.__init__)


def test_scxml::scxmlforeachtype_constructor_args():
    sig = inspect.signature(scxml::ScxmlForeachType.__init__)
    params = list(sig.parameters.keys())
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "item" in params, "Missing parameter 'item'"
    assert "any" in params, "Missing parameter 'any'"
    assert "index" in params, "Missing parameter 'index'"
    assert "array" in params, "Missing parameter 'array'"

def test_scxml::scxmlforeachtype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml::ScxmlForeachType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml::ScxmlForeachType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlforeachtype_has_anyAttribute():
    assert hasattr(scxml::ScxmlForeachType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlForeachType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlforeachtype_has_item():
    assert hasattr(scxml::ScxmlForeachType, "item")
    descriptor = None
    for klass in scxml::ScxmlForeachType.__mro__:
        if "item" in klass.__dict__:
            descriptor = klass.__dict__["item"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlforeachtype_has_any():
    assert hasattr(scxml::ScxmlForeachType, "any")
    descriptor = None
    for klass in scxml::ScxmlForeachType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlforeachtype_has_index():
    assert hasattr(scxml::ScxmlForeachType, "index")
    descriptor = None
    for klass in scxml::ScxmlForeachType.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlforeachtype_has_array():
    assert hasattr(scxml::ScxmlForeachType, "array")
    descriptor = None
    for klass in scxml::ScxmlForeachType.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlfinalizetype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlFinalizeType)


def test_scxml::scxmlfinalizetype_constructor_exists():
    assert callable(scxml::ScxmlFinalizeType.__init__)


def test_scxml::scxmlfinalizetype_constructor_args():
    sig = inspect.signature(scxml::ScxmlFinalizeType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "scxmlCoreExecutablecontent" in params, "Missing parameter 'scxmlCoreExecutablecontent'"

def test_scxml::scxmlfinalizetype_has_any():
    assert hasattr(scxml::ScxmlFinalizeType, "any")
    descriptor = None
    for klass in scxml::ScxmlFinalizeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlfinalizetype_has_anyAttribute():
    assert hasattr(scxml::ScxmlFinalizeType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlFinalizeType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlfinalizetype_has_scxmlCoreExecutablecontent():
    assert hasattr(scxml::ScxmlFinalizeType, "scxmlCoreExecutablecontent")
    descriptor = None
    for klass in scxml::ScxmlFinalizeType.__mro__:
        if "scxmlCoreExecutablecontent" in klass.__dict__:
            descriptor = klass.__dict__["scxmlCoreExecutablecontent"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlfinaltype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlFinalType)


def test_scxml::scxmlfinaltype_constructor_exists():
    assert callable(scxml::ScxmlFinalType.__init__)


def test_scxml::scxmlfinaltype_constructor_args():
    sig = inspect.signature(scxml::ScxmlFinalType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "id" in params, "Missing parameter 'id'"
    assert "scxmlFinalMix" in params, "Missing parameter 'scxmlFinalMix'"

def test_scxml::scxmlfinaltype_has_any():
    assert hasattr(scxml::ScxmlFinalType, "any")
    descriptor = None
    for klass in scxml::ScxmlFinalType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlfinaltype_has_anyAttribute():
    assert hasattr(scxml::ScxmlFinalType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlFinalType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlfinaltype_has_id():
    assert hasattr(scxml::ScxmlFinalType, "id")
    descriptor = None
    for klass in scxml::ScxmlFinalType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlfinaltype_has_scxmlFinalMix():
    assert hasattr(scxml::ScxmlFinalType, "scxmlFinalMix")
    descriptor = None
    for klass in scxml::ScxmlFinalType.__mro__:
        if "scxmlFinalMix" in klass.__dict__:
            descriptor = klass.__dict__["scxmlFinalMix"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlelseiftype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlElseifType)


def test_scxml::scxmlelseiftype_constructor_exists():
    assert callable(scxml::ScxmlElseifType.__init__)


def test_scxml::scxmlelseiftype_constructor_args():
    sig = inspect.signature(scxml::ScxmlElseifType.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml::scxmlelseiftype_has_cond():
    assert hasattr(scxml::ScxmlElseifType, "cond")
    descriptor = None
    for klass in scxml::ScxmlElseifType.__mro__:
        if "cond" in klass.__dict__:
            descriptor = klass.__dict__["cond"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlelseiftype_has_anyAttribute():
    assert hasattr(scxml::ScxmlElseifType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlElseifType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlelsetype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlElseType)


def test_scxml::scxmlelsetype_constructor_exists():
    assert callable(scxml::ScxmlElseType.__init__)


def test_scxml::scxmlelsetype_constructor_args():
    sig = inspect.signature(scxml::ScxmlElseType.__init__)
    params = list(sig.parameters.keys())
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"

def test_scxml::scxmlelsetype_has_anyAttribute():
    assert hasattr(scxml::ScxmlElseType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlElseType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)



def test_scxml::scxmlassigntype_is_not_abstract():
    assert not inspect.isabstract(scxml::ScxmlAssignType)


def test_scxml::scxmlassigntype_constructor_exists():
    assert callable(scxml::ScxmlAssignType.__init__)


def test_scxml::scxmlassigntype_constructor_args():
    sig = inspect.signature(scxml::ScxmlAssignType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "attr" in params, "Missing parameter 'attr'"
    assert "location" in params, "Missing parameter 'location'"
    assert "any" in params, "Missing parameter 'any'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "anyAttribute" in params, "Missing parameter 'anyAttribute'"
    assert "type" in params, "Missing parameter 'type'"

def test_scxml::scxmlassigntype_has_mixed():
    assert hasattr(scxml::ScxmlAssignType, "mixed")
    descriptor = None
    for klass in scxml::ScxmlAssignType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlassigntype_has_attr():
    assert hasattr(scxml::ScxmlAssignType, "attr")
    descriptor = None
    for klass in scxml::ScxmlAssignType.__mro__:
        if "attr" in klass.__dict__:
            descriptor = klass.__dict__["attr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlassigntype_has_location():
    assert hasattr(scxml::ScxmlAssignType, "location")
    descriptor = None
    for klass in scxml::ScxmlAssignType.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlassigntype_has_any():
    assert hasattr(scxml::ScxmlAssignType, "any")
    descriptor = None
    for klass in scxml::ScxmlAssignType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlassigntype_has_expr():
    assert hasattr(scxml::ScxmlAssignType, "expr")
    descriptor = None
    for klass in scxml::ScxmlAssignType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlassigntype_has_anyAttribute():
    assert hasattr(scxml::ScxmlAssignType, "anyAttribute")
    descriptor = None
    for klass in scxml::ScxmlAssignType.__mro__:
        if "anyAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anyAttribute"]
            break
    assert isinstance(descriptor, property)

def test_scxml::scxmlassigntype_has_type():
    assert hasattr(scxml::ScxmlAssignType, "type")
    descriptor = None
    for klass in scxml::ScxmlAssignType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



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

def test_historytypedatatype_exists():
    # Check that the Enumeration exists
    assert HistoryTypeDatatype is not None

def test_historytypedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HistoryTypeDatatype]
    expected_literals = [
        "shallow",
        "deep",
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
        "early",
        "late",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BindingDatatype"

def test_assigntypedatatype_exists():
    # Check that the Enumeration exists
    assert AssignTypeDatatype is not None

def test_assigntypedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignTypeDatatype]
    expected_literals = [
        "previoussibling",
        "nextsibling",
        "lastchild",
        "replace",
        "delete",
        "firstchild",
        "addattribute",
        "replacechildren",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignTypeDatatype"

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

def test_exmodedatatype_exists():
    # Check that the Enumeration exists
    assert ExmodeDatatype is not None

def test_exmodedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExmodeDatatype]
    expected_literals = [
        "lax",
        "strict",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExmodeDatatype"


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
scxml::ScxmlTransitionType_strategy = st.builds(
    scxml::ScxmlTransitionType,
    cond=
        safe_text,
    event=
        safe_text,
    target=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    scxmlCoreExecutablecontent=
        safe_text,
    type=
        safe_text
)
scxml::ScxmlStateType_strategy = st.builds(
    scxml::ScxmlStateType,
    any=
        safe_text,
    scxmlStateMix=
        safe_text,
    id=
        safe_text,
    anyAttribute=
        safe_text,
    initial1=
        safe_text
)
scxml::ScxmlSendType_strategy = st.builds(
    scxml::ScxmlSendType,
    id=
        safe_text,
    type=
        safe_text,
    any=
        safe_text,
    delayexpr=
        safe_text,
    targetexpr=
        safe_text,
    delay=
        safe_text,
    anyAttribute=
        safe_text,
    target=
        safe_text,
    event=
        safe_text,
    idlocation=
        safe_text,
    typeexpr=
        safe_text,
    namelist=
        safe_text,
    scxmlSendMix=
        safe_text,
    eventexpr=
        safe_text
)
scxml::ScxmlScxmlType_strategy = st.builds(
    scxml::ScxmlScxmlType,
    exmode=
        safe_text,
    binding=
        safe_text,
    initial=
        safe_text,
    any=
        safe_text,
    scxmlScxmlMix=
        safe_text,
    version=
        safe_text,
    datamodel1=
        safe_text,
    name=
        safe_text,
    anyAttribute=
        safe_text
)
scxml::ScxmlScriptType_strategy = st.builds(
    scxml::ScxmlScriptType,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    src=
        safe_text,
    scxmlExtraContent=
        safe_text,
    any=
        safe_text
)
scxml::ScxmlLogType_strategy = st.builds(
    scxml::ScxmlLogType,
    any=
        safe_text,
    expr=
        safe_text,
    anyAttribute=
        safe_text,
    label=
        safe_text,
    scxmlExtraContent=
        safe_text
)
scxml::ScxmlInvokeType_strategy = st.builds(
    scxml::ScxmlInvokeType,
    typeexpr=
        safe_text,
    srcexpr=
        safe_text,
    id=
        safe_text,
    autoforward=
        safe_text,
    scxmlInvokeMix=
        safe_text,
    type=
        safe_text,
    namelist=
        safe_text,
    any=
        safe_text,
    src=
        safe_text,
    anyAttribute=
        safe_text,
    idlocation=
        safe_text
)
scxml::ScxmlInitialType_strategy = st.builds(
    scxml::ScxmlInitialType,
    any=
        safe_text,
    scxmlExtraContent1=
        safe_text,
    any1=
        safe_text,
    anyAttribute=
        safe_text,
    scxmlExtraContent=
        safe_text
)
scxml::ScxmlIfType_strategy = st.builds(
    scxml::ScxmlIfType,
    any1=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    scxmlCoreExecutablecontent1=
        safe_text,
    scxmlCoreExecutablecontent=
        safe_text,
    any2=
        safe_text,
    cond=
        safe_text,
    scxmlCoreExecutablecontent2=
        safe_text
)
scxml::ScxmlHistoryType_strategy = st.builds(
    scxml::ScxmlHistoryType,
    scxmlExtraContent=
        safe_text,
    any1=
        safe_text,
    any=
        safe_text,
    id=
        safe_text,
    scxmlExtraContent1=
        safe_text,
    type=
        safe_text,
    anyAttribute=
        safe_text
)
scxml::ScxmlRaiseType_strategy = st.builds(
    scxml::ScxmlRaiseType,
    event=
        safe_text,
    anyAttribute=
        safe_text
)
scxml::ScxmlParamType_strategy = st.builds(
    scxml::ScxmlParamType,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    location=
        safe_text,
    expr=
        safe_text,
    name=
        safe_text,
    scxmlExtraContent=
        safe_text
)
scxml::ScxmlParallelType_strategy = st.builds(
    scxml::ScxmlParallelType,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    scxmlParallelMix=
        safe_text,
    id=
        safe_text
)
scxml::ScxmlOnexitType_strategy = st.builds(
    scxml::ScxmlOnexitType,
    anyAttribute=
        safe_text,
    any=
        safe_text,
    scxmlCoreExecutablecontent=
        safe_text
)
scxml::ScxmlOnentryType_strategy = st.builds(
    scxml::ScxmlOnentryType,
    scxmlCoreExecutablecontent=
        safe_text,
    anyAttribute=
        safe_text,
    any=
        safe_text
)
scxml::ScxmlDonedataType_strategy = st.builds(
    scxml::ScxmlDonedataType,
    anyAttribute=
        safe_text
)
scxml::ScxmlDatamodelType_strategy = st.builds(
    scxml::ScxmlDatamodelType,
    anyAttribute=
        safe_text,
    scxmlExtraContent=
        safe_text,
    any=
        safe_text
)
scxml::ScxmlDataType_strategy = st.builds(
    scxml::ScxmlDataType,
    any=
        safe_text,
    id=
        safe_text,
    anyAttribute=
        safe_text,
    mixed=
        safe_text,
    expr=
        safe_text,
    src=
        safe_text
)
scxml::ScxmlContentType_strategy = st.builds(
    scxml::ScxmlContentType,
    mixed=
        safe_text,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    expr=
        safe_text
)
scxml::ScxmlCancelType_strategy = st.builds(
    scxml::ScxmlCancelType,
    any=
        safe_text,
    sendidexpr=
        safe_text,
    anyAttribute=
        safe_text,
    scxmlExtraContent=
        safe_text,
    sendid=
        safe_text
)
scxml::ScxmlForeachType_strategy = st.builds(
    scxml::ScxmlForeachType,
    scxmlCoreExecutablecontent=
        safe_text,
    anyAttribute=
        safe_text,
    item=
        safe_text,
    any=
        safe_text,
    index=
        safe_text,
    array=
        safe_text
)
scxml::ScxmlFinalizeType_strategy = st.builds(
    scxml::ScxmlFinalizeType,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    scxmlCoreExecutablecontent=
        safe_text
)
scxml::ScxmlFinalType_strategy = st.builds(
    scxml::ScxmlFinalType,
    any=
        safe_text,
    anyAttribute=
        safe_text,
    id=
        safe_text,
    scxmlFinalMix=
        safe_text
)
scxml::ScxmlElseifType_strategy = st.builds(
    scxml::ScxmlElseifType,
    cond=
        safe_text,
    anyAttribute=
        safe_text
)
scxml::ScxmlElseType_strategy = st.builds(
    scxml::ScxmlElseType,
    anyAttribute=
        safe_text
)
scxml::ScxmlAssignType_strategy = st.builds(
    scxml::ScxmlAssignType,
    mixed=
        safe_text,
    attr=
        safe_text,
    location=
        safe_text,
    any=
        safe_text,
    expr=
        safe_text,
    anyAttribute=
        safe_text,
    type=
        safe_text
)
scxml::EStringToStringMapEntry_strategy = st.builds(
    scxml::EStringToStringMapEntry,
)
scxml::DocumentRoot_strategy = st.builds(
    scxml::DocumentRoot,
    mixed=
        safe_text
)

@given(instance=scxml::ScxmlTransitionType_strategy)
@settings(max_examples=50)
def test_scxml::scxmltransitiontype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlTransitionType)

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

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_scxmlCoreExecutablecontent_type(instance):
    assert isinstance(instance.scxmlCoreExecutablecontent, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original

@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::ScxmlTransitionType_strategy)
def test_scxml::scxmltransitiontype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::ScxmlStateType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlstatetype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlStateType)

@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_scxmlStateMix_type(instance):
    assert isinstance(instance.scxmlStateMix, str)


@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_scxmlStateMix_setter(instance):
    original = instance.scxmlStateMix
    instance.scxmlStateMix = original
    assert instance.scxmlStateMix == original

@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_initial1_type(instance):
    assert isinstance(instance.initial1, str)


@given(instance=scxml::ScxmlStateType_strategy)
def test_scxml::scxmlstatetype_initial1_setter(instance):
    original = instance.initial1
    instance.initial1 = original
    assert instance.initial1 == original

@given(instance=scxml::ScxmlSendType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlsendtype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlSendType)

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_delayexpr_type(instance):
    assert isinstance(instance.delayexpr, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_delayexpr_setter(instance):
    original = instance.delayexpr
    instance.delayexpr = original
    assert instance.delayexpr == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_targetexpr_type(instance):
    assert isinstance(instance.targetexpr, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_targetexpr_setter(instance):
    original = instance.targetexpr
    instance.targetexpr = original
    assert instance.targetexpr == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_delay_type(instance):
    assert isinstance(instance.delay, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_idlocation_type(instance):
    assert isinstance(instance.idlocation, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_typeexpr_type(instance):
    assert isinstance(instance.typeexpr, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_namelist_type(instance):
    assert isinstance(instance.namelist, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_scxmlSendMix_type(instance):
    assert isinstance(instance.scxmlSendMix, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_scxmlSendMix_setter(instance):
    original = instance.scxmlSendMix
    instance.scxmlSendMix = original
    assert instance.scxmlSendMix == original

@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_eventexpr_type(instance):
    assert isinstance(instance.eventexpr, str)


@given(instance=scxml::ScxmlSendType_strategy)
def test_scxml::scxmlsendtype_eventexpr_setter(instance):
    original = instance.eventexpr
    instance.eventexpr = original
    assert instance.eventexpr == original

@given(instance=scxml::ScxmlScxmlType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlscxmltype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlScxmlType)

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_exmode_type(instance):
    assert isinstance(instance.exmode, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_exmode_setter(instance):
    original = instance.exmode
    instance.exmode = original
    assert instance.exmode == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_binding_type(instance):
    assert isinstance(instance.binding, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_initial_type(instance):
    assert isinstance(instance.initial, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_scxmlScxmlMix_type(instance):
    assert isinstance(instance.scxmlScxmlMix, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_scxmlScxmlMix_setter(instance):
    original = instance.scxmlScxmlMix
    instance.scxmlScxmlMix = original
    assert instance.scxmlScxmlMix == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_datamodel1_type(instance):
    assert isinstance(instance.datamodel1, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_datamodel1_setter(instance):
    original = instance.datamodel1
    instance.datamodel1 = original
    assert instance.datamodel1 == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlScxmlType_strategy)
def test_scxml::scxmlscxmltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlScriptType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlscripttype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlScriptType)

@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

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

@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_scxmlExtraContent_type(instance):
    assert isinstance(instance.scxmlExtraContent, str)


@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlScriptType_strategy)
def test_scxml::scxmlscripttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlLogType_strategy)
@settings(max_examples=50)
def test_scxml::scxmllogtype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlLogType)

@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_scxmlExtraContent_type(instance):
    assert isinstance(instance.scxmlExtraContent, str)


@given(instance=scxml::ScxmlLogType_strategy)
def test_scxml::scxmllogtype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml::ScxmlInvokeType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlinvoketype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlInvokeType)

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_typeexpr_type(instance):
    assert isinstance(instance.typeexpr, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_srcexpr_type(instance):
    assert isinstance(instance.srcexpr, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_srcexpr_setter(instance):
    original = instance.srcexpr
    instance.srcexpr = original
    assert instance.srcexpr == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_autoforward_type(instance):
    assert isinstance(instance.autoforward, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_autoforward_setter(instance):
    original = instance.autoforward
    instance.autoforward = original
    assert instance.autoforward == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_scxmlInvokeMix_type(instance):
    assert isinstance(instance.scxmlInvokeMix, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_scxmlInvokeMix_setter(instance):
    original = instance.scxmlInvokeMix
    instance.scxmlInvokeMix = original
    assert instance.scxmlInvokeMix == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_namelist_type(instance):
    assert isinstance(instance.namelist, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_idlocation_type(instance):
    assert isinstance(instance.idlocation, str)


@given(instance=scxml::ScxmlInvokeType_strategy)
def test_scxml::scxmlinvoketype_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original

@given(instance=scxml::ScxmlInitialType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlinitialtype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlInitialType)

@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_scxmlExtraContent1_type(instance):
    assert isinstance(instance.scxmlExtraContent1, str)


@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_scxmlExtraContent1_setter(instance):
    original = instance.scxmlExtraContent1
    instance.scxmlExtraContent1 = original
    assert instance.scxmlExtraContent1 == original

@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_any1_type(instance):
    assert isinstance(instance.any1, str)


@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_any1_setter(instance):
    original = instance.any1
    instance.any1 = original
    assert instance.any1 == original

@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_scxmlExtraContent_type(instance):
    assert isinstance(instance.scxmlExtraContent, str)


@given(instance=scxml::ScxmlInitialType_strategy)
def test_scxml::scxmlinitialtype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml::ScxmlIfType_strategy)
@settings(max_examples=50)
def test_scxml::scxmliftype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlIfType)

@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_any1_type(instance):
    assert isinstance(instance.any1, str)


@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_any1_setter(instance):
    original = instance.any1
    instance.any1 = original
    assert instance.any1 == original

@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_scxmlCoreExecutablecontent1_type(instance):
    assert isinstance(instance.scxmlCoreExecutablecontent1, str)


@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_scxmlCoreExecutablecontent1_setter(instance):
    original = instance.scxmlCoreExecutablecontent1
    instance.scxmlCoreExecutablecontent1 = original
    assert instance.scxmlCoreExecutablecontent1 == original

@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_scxmlCoreExecutablecontent_type(instance):
    assert isinstance(instance.scxmlCoreExecutablecontent, str)


@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original

@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_any2_type(instance):
    assert isinstance(instance.any2, str)


@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_any2_setter(instance):
    original = instance.any2
    instance.any2 = original
    assert instance.any2 == original

@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_cond_type(instance):
    assert isinstance(instance.cond, str)


@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_scxmlCoreExecutablecontent2_type(instance):
    assert isinstance(instance.scxmlCoreExecutablecontent2, str)


@given(instance=scxml::ScxmlIfType_strategy)
def test_scxml::scxmliftype_scxmlCoreExecutablecontent2_setter(instance):
    original = instance.scxmlCoreExecutablecontent2
    instance.scxmlCoreExecutablecontent2 = original
    assert instance.scxmlCoreExecutablecontent2 == original

@given(instance=scxml::ScxmlHistoryType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlhistorytype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlHistoryType)

@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_scxmlExtraContent_type(instance):
    assert isinstance(instance.scxmlExtraContent, str)


@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_any1_type(instance):
    assert isinstance(instance.any1, str)


@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_any1_setter(instance):
    original = instance.any1
    instance.any1 = original
    assert instance.any1 == original

@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_scxmlExtraContent1_type(instance):
    assert isinstance(instance.scxmlExtraContent1, str)


@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_scxmlExtraContent1_setter(instance):
    original = instance.scxmlExtraContent1
    instance.scxmlExtraContent1 = original
    assert instance.scxmlExtraContent1 == original

@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlHistoryType_strategy)
def test_scxml::scxmlhistorytype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlRaiseType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlraisetype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlRaiseType)

@given(instance=scxml::ScxmlRaiseType_strategy)
def test_scxml::scxmlraisetype_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=scxml::ScxmlRaiseType_strategy)
def test_scxml::scxmlraisetype_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=scxml::ScxmlRaiseType_strategy)
def test_scxml::scxmlraisetype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlRaiseType_strategy)
def test_scxml::scxmlraisetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlParamType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlparamtype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlParamType)

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::ScxmlParamType_strategy)
def test_scxml::scxmlparamtype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

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

@given(instance=scxml::ScxmlParallelType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlparalleltype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlParallelType)

@given(instance=scxml::ScxmlParallelType_strategy)
def test_scxml::scxmlparalleltype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlParallelType_strategy)
def test_scxml::scxmlparalleltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlParallelType_strategy)
def test_scxml::scxmlparalleltype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlParallelType_strategy)
def test_scxml::scxmlparalleltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlParallelType_strategy)
def test_scxml::scxmlparalleltype_scxmlParallelMix_type(instance):
    assert isinstance(instance.scxmlParallelMix, str)


@given(instance=scxml::ScxmlParallelType_strategy)
def test_scxml::scxmlparalleltype_scxmlParallelMix_setter(instance):
    original = instance.scxmlParallelMix
    instance.scxmlParallelMix = original
    assert instance.scxmlParallelMix == original

@given(instance=scxml::ScxmlParallelType_strategy)
def test_scxml::scxmlparalleltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlParallelType_strategy)
def test_scxml::scxmlparalleltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlOnexitType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlonexittype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlOnexitType)

@given(instance=scxml::ScxmlOnexitType_strategy)
def test_scxml::scxmlonexittype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlOnexitType_strategy)
def test_scxml::scxmlonexittype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlOnexitType_strategy)
def test_scxml::scxmlonexittype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlOnexitType_strategy)
def test_scxml::scxmlonexittype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlOnexitType_strategy)
def test_scxml::scxmlonexittype_scxmlCoreExecutablecontent_type(instance):
    assert isinstance(instance.scxmlCoreExecutablecontent, str)


@given(instance=scxml::ScxmlOnexitType_strategy)
def test_scxml::scxmlonexittype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original

@given(instance=scxml::ScxmlOnentryType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlonentrytype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlOnentryType)

@given(instance=scxml::ScxmlOnentryType_strategy)
def test_scxml::scxmlonentrytype_scxmlCoreExecutablecontent_type(instance):
    assert isinstance(instance.scxmlCoreExecutablecontent, str)


@given(instance=scxml::ScxmlOnentryType_strategy)
def test_scxml::scxmlonentrytype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original

@given(instance=scxml::ScxmlOnentryType_strategy)
def test_scxml::scxmlonentrytype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlOnentryType_strategy)
def test_scxml::scxmlonentrytype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlOnentryType_strategy)
def test_scxml::scxmlonentrytype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlOnentryType_strategy)
def test_scxml::scxmlonentrytype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlDonedataType_strategy)
@settings(max_examples=50)
def test_scxml::scxmldonedatatype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlDonedataType)

@given(instance=scxml::ScxmlDonedataType_strategy)
def test_scxml::scxmldonedatatype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlDonedataType_strategy)
def test_scxml::scxmldonedatatype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlDatamodelType_strategy)
@settings(max_examples=50)
def test_scxml::scxmldatamodeltype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlDatamodelType)

@given(instance=scxml::ScxmlDatamodelType_strategy)
def test_scxml::scxmldatamodeltype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlDatamodelType_strategy)
def test_scxml::scxmldatamodeltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlDatamodelType_strategy)
def test_scxml::scxmldatamodeltype_scxmlExtraContent_type(instance):
    assert isinstance(instance.scxmlExtraContent, str)


@given(instance=scxml::ScxmlDatamodelType_strategy)
def test_scxml::scxmldatamodeltype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml::ScxmlDatamodelType_strategy)
def test_scxml::scxmldatamodeltype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlDatamodelType_strategy)
def test_scxml::scxmldatamodeltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlDataType_strategy)
@settings(max_examples=50)
def test_scxml::scxmldatatype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlDataType)

@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=scxml::ScxmlDataType_strategy)
def test_scxml::scxmldatatype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=scxml::ScxmlContentType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlcontenttype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlContentType)

@given(instance=scxml::ScxmlContentType_strategy)
def test_scxml::scxmlcontenttype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=scxml::ScxmlContentType_strategy)
def test_scxml::scxmlcontenttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=scxml::ScxmlContentType_strategy)
def test_scxml::scxmlcontenttype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlContentType_strategy)
def test_scxml::scxmlcontenttype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlContentType_strategy)
def test_scxml::scxmlcontenttype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlContentType_strategy)
def test_scxml::scxmlcontenttype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlContentType_strategy)
def test_scxml::scxmlcontenttype_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::ScxmlContentType_strategy)
def test_scxml::scxmlcontenttype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::ScxmlCancelType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlcanceltype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlCancelType)

@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_sendidexpr_type(instance):
    assert isinstance(instance.sendidexpr, str)


@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_sendidexpr_setter(instance):
    original = instance.sendidexpr
    instance.sendidexpr = original
    assert instance.sendidexpr == original

@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_scxmlExtraContent_type(instance):
    assert isinstance(instance.scxmlExtraContent, str)


@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_scxmlExtraContent_setter(instance):
    original = instance.scxmlExtraContent
    instance.scxmlExtraContent = original
    assert instance.scxmlExtraContent == original

@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_sendid_type(instance):
    assert isinstance(instance.sendid, str)


@given(instance=scxml::ScxmlCancelType_strategy)
def test_scxml::scxmlcanceltype_sendid_setter(instance):
    original = instance.sendid
    instance.sendid = original
    assert instance.sendid == original

@given(instance=scxml::ScxmlForeachType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlforeachtype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlForeachType)

@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_scxmlCoreExecutablecontent_type(instance):
    assert isinstance(instance.scxmlCoreExecutablecontent, str)


@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original

@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_item_type(instance):
    assert isinstance(instance.item, str)


@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_item_setter(instance):
    original = instance.item
    instance.item = original
    assert instance.item == original

@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_array_type(instance):
    assert isinstance(instance.array, str)


@given(instance=scxml::ScxmlForeachType_strategy)
def test_scxml::scxmlforeachtype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=scxml::ScxmlFinalizeType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlfinalizetype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlFinalizeType)

@given(instance=scxml::ScxmlFinalizeType_strategy)
def test_scxml::scxmlfinalizetype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlFinalizeType_strategy)
def test_scxml::scxmlfinalizetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlFinalizeType_strategy)
def test_scxml::scxmlfinalizetype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlFinalizeType_strategy)
def test_scxml::scxmlfinalizetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlFinalizeType_strategy)
def test_scxml::scxmlfinalizetype_scxmlCoreExecutablecontent_type(instance):
    assert isinstance(instance.scxmlCoreExecutablecontent, str)


@given(instance=scxml::ScxmlFinalizeType_strategy)
def test_scxml::scxmlfinalizetype_scxmlCoreExecutablecontent_setter(instance):
    original = instance.scxmlCoreExecutablecontent
    instance.scxmlCoreExecutablecontent = original
    assert instance.scxmlCoreExecutablecontent == original

@given(instance=scxml::ScxmlFinalType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlfinaltype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlFinalType)

@given(instance=scxml::ScxmlFinalType_strategy)
def test_scxml::scxmlfinaltype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlFinalType_strategy)
def test_scxml::scxmlfinaltype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlFinalType_strategy)
def test_scxml::scxmlfinaltype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlFinalType_strategy)
def test_scxml::scxmlfinaltype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlFinalType_strategy)
def test_scxml::scxmlfinaltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=scxml::ScxmlFinalType_strategy)
def test_scxml::scxmlfinaltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=scxml::ScxmlFinalType_strategy)
def test_scxml::scxmlfinaltype_scxmlFinalMix_type(instance):
    assert isinstance(instance.scxmlFinalMix, str)


@given(instance=scxml::ScxmlFinalType_strategy)
def test_scxml::scxmlfinaltype_scxmlFinalMix_setter(instance):
    original = instance.scxmlFinalMix
    instance.scxmlFinalMix = original
    assert instance.scxmlFinalMix == original

@given(instance=scxml::ScxmlElseifType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlelseiftype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlElseifType)

@given(instance=scxml::ScxmlElseifType_strategy)
def test_scxml::scxmlelseiftype_cond_type(instance):
    assert isinstance(instance.cond, str)


@given(instance=scxml::ScxmlElseifType_strategy)
def test_scxml::scxmlelseiftype_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original

@given(instance=scxml::ScxmlElseifType_strategy)
def test_scxml::scxmlelseiftype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlElseifType_strategy)
def test_scxml::scxmlelseiftype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlElseType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlelsetype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlElseType)

@given(instance=scxml::ScxmlElseType_strategy)
def test_scxml::scxmlelsetype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlElseType_strategy)
def test_scxml::scxmlelsetype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlAssignType_strategy)
@settings(max_examples=50)
def test_scxml::scxmlassigntype_instantiation(instance):
    assert isinstance(instance, scxml::ScxmlAssignType)

@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_attr_type(instance):
    assert isinstance(instance.attr, str)


@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_attr_setter(instance):
    original = instance.attr
    instance.attr = original
    assert instance.attr == original

@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_anyAttribute_type(instance):
    assert isinstance(instance.anyAttribute, str)


@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_anyAttribute_setter(instance):
    original = instance.anyAttribute
    instance.anyAttribute = original
    assert instance.anyAttribute == original

@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=scxml::ScxmlAssignType_strategy)
def test_scxml::scxmlassigntype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

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
