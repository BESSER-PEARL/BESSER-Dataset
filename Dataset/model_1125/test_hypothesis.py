import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cjsidl::stateMachine,
    cjsidl::eventDef,
    cjsidl::transition,
    cjsidl::exit,
    cjsidl::entry,
    cjsidl::defaultState,
    cjsidl::state,
    cjsidl::startState,
    cjsidl::constDef,
    cjsidl::declaredConstSetRef,
    cjsidl::messageScopedRef,
    cjsidl::messageRef,
    cjsidl::messageDef,
    cjsidl::messages,
    cjsidl::scopedTypeId,
    cjsidl::typeReference,
    cjsidl::typeDef,
    cjsidl::declaredTypeSetRef,
    cjsidl::serviceDef,
    cjsidl::EObject,
    cjsidl::jaus,
    cjsidl::refAttr,
    cjsidl::protocolBehavior,
    cjsidl::internalEventSet,
    cjsidl::messageSet,
    cjsidl::declaredTypeSet,
    cjsidl::declaredConstSet,
    cjsidl::references,
    cjsidl::description,
    cjsidl::taggedItemDef,
    cjsidl::valueSpec,
    containerDef,
    cjsidl::formatEnumDef,
    cjsidl::valueRange,
    cjsidl::scaledRangeDef,
    cjsidl::subField,
    cjsidl::taggedUnitsEnum,
    cjsidl::valueSetDef,
    cjsidl::declaredEventDef,
    cjsidl::scopedType,
    cjsidl::scopedConstId,
    cjsidl::constReference,
    cjsidl::footerScopedRef,
    cjsidl::footerRef,
    cjsidl::bodyScopedRef,
    cjsidl::bodyRef,
    cjsidl::headerScopedRef,
    cjsidl::headerRef,
    cjsidl::containerRef,
    cjsidl::containerDef,
    cjsidl::footerDef,
    cjsidl::bodyDef,
    cjsidl::headerDef,
    cjsidl::varFormatField,
    cjsidl::varLenField,
    cjsidl::varLenString,
    cjsidl::fixedLenString,
    cjsidl::bitfieldDef,
    cjsidl::action,
    cjsidl::varField,
    cjsidl::fixedFieldDef,
    cjsidl::sequenceDef,
    cjsidl::variantDef,
    cjsidl::listDef,
    cjsidl::recordDef,
    cjsidl::arrayDef,
    cjsidl::simpleNumericType,
    cjsidl::simpleTransition,
    cjsidl::internalTransition,
    cjsidl::guardAction,
    cjsidl::guardParam,
    cjsidl::popTransition,
    cjsidl::pushTransition,
    cjsidl::nextState,
    cjsidl::sendActionList,
    cjsidl::actionList,
    cjsidl::defaultTransition,
    cjsidl::guard,
    cjsidl::scopedEventType,
    cjsidl::transParam,
    cjsidl::transParams,
    FIELD_FORMAT,
    UNIT,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cjsidl::statemachine_is_not_abstract():
    assert not inspect.isabstract(cjsidl::stateMachine)


def test_cjsidl::statemachine_constructor_exists():
    assert callable(cjsidl::stateMachine.__init__)


def test_cjsidl::statemachine_constructor_args():
    sig = inspect.signature(cjsidl::stateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::statemachine_has_name():
    assert hasattr(cjsidl::stateMachine, "name")
    descriptor = None
    for klass in cjsidl::stateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::statemachine_has_comment():
    assert hasattr(cjsidl::stateMachine, "comment")
    descriptor = None
    for klass in cjsidl::stateMachine.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::eventdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::eventDef)


def test_cjsidl::eventdef_constructor_exists():
    assert callable(cjsidl::eventDef.__init__)


def test_cjsidl::eventdef_constructor_args():
    sig = inspect.signature(cjsidl::eventDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::eventdef_has_name():
    assert hasattr(cjsidl::eventDef, "name")
    descriptor = None
    for klass in cjsidl::eventDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::transition_is_not_abstract():
    assert not inspect.isabstract(cjsidl::transition)


def test_cjsidl::transition_constructor_exists():
    assert callable(cjsidl::transition.__init__)


def test_cjsidl::transition_constructor_args():
    sig = inspect.signature(cjsidl::transition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_cjsidl::transition_has_comment():
    assert hasattr(cjsidl::transition, "comment")
    descriptor = None
    for klass in cjsidl::transition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::transition_has_name():
    assert hasattr(cjsidl::transition, "name")
    descriptor = None
    for klass in cjsidl::transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::transition_has_type():
    assert hasattr(cjsidl::transition, "type")
    descriptor = None
    for klass in cjsidl::transition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::exit_is_not_abstract():
    assert not inspect.isabstract(cjsidl::exit)


def test_cjsidl::exit_constructor_exists():
    assert callable(cjsidl::exit.__init__)


def test_cjsidl::exit_constructor_args():
    sig = inspect.signature(cjsidl::exit.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::exit_has_comment():
    assert hasattr(cjsidl::exit, "comment")
    descriptor = None
    for klass in cjsidl::exit.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::entry_is_not_abstract():
    assert not inspect.isabstract(cjsidl::entry)


def test_cjsidl::entry_constructor_exists():
    assert callable(cjsidl::entry.__init__)


def test_cjsidl::entry_constructor_args():
    sig = inspect.signature(cjsidl::entry.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::entry_has_comment():
    assert hasattr(cjsidl::entry, "comment")
    descriptor = None
    for klass in cjsidl::entry.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::defaultstate_is_not_abstract():
    assert not inspect.isabstract(cjsidl::defaultState)


def test_cjsidl::defaultstate_constructor_exists():
    assert callable(cjsidl::defaultState.__init__)


def test_cjsidl::defaultstate_constructor_args():
    sig = inspect.signature(cjsidl::defaultState.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::defaultstate_has_comment():
    assert hasattr(cjsidl::defaultState, "comment")
    descriptor = None
    for klass in cjsidl::defaultState.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::state_is_not_abstract():
    assert not inspect.isabstract(cjsidl::state)


def test_cjsidl::state_constructor_exists():
    assert callable(cjsidl::state.__init__)


def test_cjsidl::state_constructor_args():
    sig = inspect.signature(cjsidl::state.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initial" in params, "Missing parameter 'initial'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::state_has_name():
    assert hasattr(cjsidl::state, "name")
    descriptor = None
    for klass in cjsidl::state.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::state_has_initial():
    assert hasattr(cjsidl::state, "initial")
    descriptor = None
    for klass in cjsidl::state.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::state_has_comment():
    assert hasattr(cjsidl::state, "comment")
    descriptor = None
    for klass in cjsidl::state.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::startstate_is_not_abstract():
    assert not inspect.isabstract(cjsidl::startState)


def test_cjsidl::startstate_constructor_exists():
    assert callable(cjsidl::startState.__init__)


def test_cjsidl::startstate_constructor_args():
    sig = inspect.signature(cjsidl::startState.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::startstate_has_comment():
    assert hasattr(cjsidl::startState, "comment")
    descriptor = None
    for klass in cjsidl::startState.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::constdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::constDef)


def test_cjsidl::constdef_constructor_exists():
    assert callable(cjsidl::constDef.__init__)


def test_cjsidl::constdef_constructor_args():
    sig = inspect.signature(cjsidl::constDef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "constValue" in params, "Missing parameter 'constValue'"
    assert "fieldUnits" in params, "Missing parameter 'fieldUnits'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::constdef_has_comment():
    assert hasattr(cjsidl::constDef, "comment")
    descriptor = None
    for klass in cjsidl::constDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::constdef_has_constValue():
    assert hasattr(cjsidl::constDef, "constValue")
    descriptor = None
    for klass in cjsidl::constDef.__mro__:
        if "constValue" in klass.__dict__:
            descriptor = klass.__dict__["constValue"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::constdef_has_fieldUnits():
    assert hasattr(cjsidl::constDef, "fieldUnits")
    descriptor = None
    for klass in cjsidl::constDef.__mro__:
        if "fieldUnits" in klass.__dict__:
            descriptor = klass.__dict__["fieldUnits"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::constdef_has_name():
    assert hasattr(cjsidl::constDef, "name")
    descriptor = None
    for klass in cjsidl::constDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::declaredconstsetref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::declaredConstSetRef)


def test_cjsidl::declaredconstsetref_constructor_exists():
    assert callable(cjsidl::declaredConstSetRef.__init__)


def test_cjsidl::declaredconstsetref_constructor_args():
    sig = inspect.signature(cjsidl::declaredConstSetRef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::declaredconstsetref_has_comment():
    assert hasattr(cjsidl::declaredConstSetRef, "comment")
    descriptor = None
    for klass in cjsidl::declaredConstSetRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::declaredconstsetref_has_name():
    assert hasattr(cjsidl::declaredConstSetRef, "name")
    descriptor = None
    for klass in cjsidl::declaredConstSetRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::messagescopedref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::messageScopedRef)


def test_cjsidl::messagescopedref_constructor_exists():
    assert callable(cjsidl::messageScopedRef.__init__)


def test_cjsidl::messagescopedref_constructor_args():
    sig = inspect.signature(cjsidl::messageScopedRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::messagescopedref_has_name():
    assert hasattr(cjsidl::messageScopedRef, "name")
    descriptor = None
    for klass in cjsidl::messageScopedRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::messagescopedref_has_comment():
    assert hasattr(cjsidl::messageScopedRef, "comment")
    descriptor = None
    for klass in cjsidl::messageScopedRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::messageref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::messageRef)


def test_cjsidl::messageref_constructor_exists():
    assert callable(cjsidl::messageRef.__init__)


def test_cjsidl::messageref_constructor_args():
    sig = inspect.signature(cjsidl::messageRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::messageref_has_name():
    assert hasattr(cjsidl::messageRef, "name")
    descriptor = None
    for klass in cjsidl::messageRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::messageref_has_comment():
    assert hasattr(cjsidl::messageRef, "comment")
    descriptor = None
    for klass in cjsidl::messageRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::messagedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::messageDef)


def test_cjsidl::messagedef_constructor_exists():
    assert callable(cjsidl::messageDef.__init__)


def test_cjsidl::messagedef_constructor_args():
    sig = inspect.signature(cjsidl::messageDef.__init__)
    params = list(sig.parameters.keys())
    assert "messageID" in params, "Missing parameter 'messageID'"
    assert "command" in params, "Missing parameter 'command'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::messagedef_has_messageID():
    assert hasattr(cjsidl::messageDef, "messageID")
    descriptor = None
    for klass in cjsidl::messageDef.__mro__:
        if "messageID" in klass.__dict__:
            descriptor = klass.__dict__["messageID"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::messagedef_has_command():
    assert hasattr(cjsidl::messageDef, "command")
    descriptor = None
    for klass in cjsidl::messageDef.__mro__:
        if "command" in klass.__dict__:
            descriptor = klass.__dict__["command"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::messagedef_has_name():
    assert hasattr(cjsidl::messageDef, "name")
    descriptor = None
    for klass in cjsidl::messageDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::messages_is_not_abstract():
    assert not inspect.isabstract(cjsidl::messages)


def test_cjsidl::messages_constructor_exists():
    assert callable(cjsidl::messages.__init__)


def test_cjsidl::messages_constructor_args():
    sig = inspect.signature(cjsidl::messages.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::scopedtypeid_is_not_abstract():
    assert not inspect.isabstract(cjsidl::scopedTypeId)


def test_cjsidl::scopedtypeid_constructor_exists():
    assert callable(cjsidl::scopedTypeId.__init__)


def test_cjsidl::scopedtypeid_constructor_args():
    sig = inspect.signature(cjsidl::scopedTypeId.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "scopedName" in params, "Missing parameter 'scopedName'"

def test_cjsidl::scopedtypeid_has_optional():
    assert hasattr(cjsidl::scopedTypeId, "optional")
    descriptor = None
    for klass in cjsidl::scopedTypeId.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::scopedtypeid_has_comment():
    assert hasattr(cjsidl::scopedTypeId, "comment")
    descriptor = None
    for klass in cjsidl::scopedTypeId.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::scopedtypeid_has_scopedName():
    assert hasattr(cjsidl::scopedTypeId, "scopedName")
    descriptor = None
    for klass in cjsidl::scopedTypeId.__mro__:
        if "scopedName" in klass.__dict__:
            descriptor = klass.__dict__["scopedName"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::typereference_is_not_abstract():
    assert not inspect.isabstract(cjsidl::typeReference)


def test_cjsidl::typereference_constructor_exists():
    assert callable(cjsidl::typeReference.__init__)


def test_cjsidl::typereference_constructor_args():
    sig = inspect.signature(cjsidl::typeReference.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_cjsidl::typereference_has_comment():
    assert hasattr(cjsidl::typeReference, "comment")
    descriptor = None
    for klass in cjsidl::typeReference.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::typereference_has_name():
    assert hasattr(cjsidl::typeReference, "name")
    descriptor = None
    for klass in cjsidl::typeReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::typereference_has_optional():
    assert hasattr(cjsidl::typeReference, "optional")
    descriptor = None
    for klass in cjsidl::typeReference.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::typedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::typeDef)


def test_cjsidl::typedef_constructor_exists():
    assert callable(cjsidl::typeDef.__init__)


def test_cjsidl::typedef_constructor_args():
    sig = inspect.signature(cjsidl::typeDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::declaredtypesetref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::declaredTypeSetRef)


def test_cjsidl::declaredtypesetref_constructor_exists():
    assert callable(cjsidl::declaredTypeSetRef.__init__)


def test_cjsidl::declaredtypesetref_constructor_args():
    sig = inspect.signature(cjsidl::declaredTypeSetRef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::declaredtypesetref_has_comment():
    assert hasattr(cjsidl::declaredTypeSetRef, "comment")
    descriptor = None
    for klass in cjsidl::declaredTypeSetRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::declaredtypesetref_has_name():
    assert hasattr(cjsidl::declaredTypeSetRef, "name")
    descriptor = None
    for klass in cjsidl::declaredTypeSetRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::servicedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::serviceDef)


def test_cjsidl::servicedef_constructor_exists():
    assert callable(cjsidl::serviceDef.__init__)


def test_cjsidl::servicedef_constructor_args():
    sig = inspect.signature(cjsidl::serviceDef.__init__)
    params = list(sig.parameters.keys())
    assert "serviceName" in params, "Missing parameter 'serviceName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "serviceVersion" in params, "Missing parameter 'serviceVersion'"
    assert "assumpt" in params, "Missing parameter 'assumpt'"

def test_cjsidl::servicedef_has_serviceName():
    assert hasattr(cjsidl::serviceDef, "serviceName")
    descriptor = None
    for klass in cjsidl::serviceDef.__mro__:
        if "serviceName" in klass.__dict__:
            descriptor = klass.__dict__["serviceName"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::servicedef_has_name():
    assert hasattr(cjsidl::serviceDef, "name")
    descriptor = None
    for klass in cjsidl::serviceDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::servicedef_has_serviceVersion():
    assert hasattr(cjsidl::serviceDef, "serviceVersion")
    descriptor = None
    for klass in cjsidl::serviceDef.__mro__:
        if "serviceVersion" in klass.__dict__:
            descriptor = klass.__dict__["serviceVersion"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::servicedef_has_assumpt():
    assert hasattr(cjsidl::serviceDef, "assumpt")
    descriptor = None
    for klass in cjsidl::serviceDef.__mro__:
        if "assumpt" in klass.__dict__:
            descriptor = klass.__dict__["assumpt"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::eobject_is_not_abstract():
    assert not inspect.isabstract(cjsidl::EObject)


def test_cjsidl::eobject_constructor_exists():
    assert callable(cjsidl::EObject.__init__)


def test_cjsidl::eobject_constructor_args():
    sig = inspect.signature(cjsidl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::jaus_is_not_abstract():
    assert not inspect.isabstract(cjsidl::jaus)


def test_cjsidl::jaus_constructor_exists():
    assert callable(cjsidl::jaus.__init__)


def test_cjsidl::jaus_constructor_args():
    sig = inspect.signature(cjsidl::jaus.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::refattr_is_not_abstract():
    assert not inspect.isabstract(cjsidl::refAttr)


def test_cjsidl::refattr_constructor_exists():
    assert callable(cjsidl::refAttr.__init__)


def test_cjsidl::refattr_constructor_args():
    sig = inspect.signature(cjsidl::refAttr.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::refattr_has_comment():
    assert hasattr(cjsidl::refAttr, "comment")
    descriptor = None
    for klass in cjsidl::refAttr.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::refattr_has_name():
    assert hasattr(cjsidl::refAttr, "name")
    descriptor = None
    for klass in cjsidl::refAttr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::protocolbehavior_is_not_abstract():
    assert not inspect.isabstract(cjsidl::protocolBehavior)


def test_cjsidl::protocolbehavior_constructor_exists():
    assert callable(cjsidl::protocolBehavior.__init__)


def test_cjsidl::protocolbehavior_constructor_args():
    sig = inspect.signature(cjsidl::protocolBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "stateless" in params, "Missing parameter 'stateless'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::protocolbehavior_has_stateless():
    assert hasattr(cjsidl::protocolBehavior, "stateless")
    descriptor = None
    for klass in cjsidl::protocolBehavior.__mro__:
        if "stateless" in klass.__dict__:
            descriptor = klass.__dict__["stateless"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::protocolbehavior_has_comment():
    assert hasattr(cjsidl::protocolBehavior, "comment")
    descriptor = None
    for klass in cjsidl::protocolBehavior.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::internaleventset_is_not_abstract():
    assert not inspect.isabstract(cjsidl::internalEventSet)


def test_cjsidl::internaleventset_constructor_exists():
    assert callable(cjsidl::internalEventSet.__init__)


def test_cjsidl::internaleventset_constructor_args():
    sig = inspect.signature(cjsidl::internalEventSet.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::internaleventset_has_comment():
    assert hasattr(cjsidl::internalEventSet, "comment")
    descriptor = None
    for klass in cjsidl::internalEventSet.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::messageset_is_not_abstract():
    assert not inspect.isabstract(cjsidl::messageSet)


def test_cjsidl::messageset_constructor_exists():
    assert callable(cjsidl::messageSet.__init__)


def test_cjsidl::messageset_constructor_args():
    sig = inspect.signature(cjsidl::messageSet.__init__)
    params = list(sig.parameters.keys())
    assert "outputComment" in params, "Missing parameter 'outputComment'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "inputComment" in params, "Missing parameter 'inputComment'"

def test_cjsidl::messageset_has_outputComment():
    assert hasattr(cjsidl::messageSet, "outputComment")
    descriptor = None
    for klass in cjsidl::messageSet.__mro__:
        if "outputComment" in klass.__dict__:
            descriptor = klass.__dict__["outputComment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::messageset_has_comment():
    assert hasattr(cjsidl::messageSet, "comment")
    descriptor = None
    for klass in cjsidl::messageSet.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::messageset_has_inputComment():
    assert hasattr(cjsidl::messageSet, "inputComment")
    descriptor = None
    for klass in cjsidl::messageSet.__mro__:
        if "inputComment" in klass.__dict__:
            descriptor = klass.__dict__["inputComment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::declaredtypeset_is_not_abstract():
    assert not inspect.isabstract(cjsidl::declaredTypeSet)


def test_cjsidl::declaredtypeset_constructor_exists():
    assert callable(cjsidl::declaredTypeSet.__init__)


def test_cjsidl::declaredtypeset_constructor_args():
    sig = inspect.signature(cjsidl::declaredTypeSet.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::declaredtypeset_has_typeName():
    assert hasattr(cjsidl::declaredTypeSet, "typeName")
    descriptor = None
    for klass in cjsidl::declaredTypeSet.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::declaredtypeset_has_version():
    assert hasattr(cjsidl::declaredTypeSet, "version")
    descriptor = None
    for klass in cjsidl::declaredTypeSet.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::declaredtypeset_has_name():
    assert hasattr(cjsidl::declaredTypeSet, "name")
    descriptor = None
    for klass in cjsidl::declaredTypeSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::declaredconstset_is_not_abstract():
    assert not inspect.isabstract(cjsidl::declaredConstSet)


def test_cjsidl::declaredconstset_constructor_exists():
    assert callable(cjsidl::declaredConstSet.__init__)


def test_cjsidl::declaredconstset_constructor_args():
    sig = inspect.signature(cjsidl::declaredConstSet.__init__)
    params = list(sig.parameters.keys())
    assert "constName" in params, "Missing parameter 'constName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "constSetVersion" in params, "Missing parameter 'constSetVersion'"

def test_cjsidl::declaredconstset_has_constName():
    assert hasattr(cjsidl::declaredConstSet, "constName")
    descriptor = None
    for klass in cjsidl::declaredConstSet.__mro__:
        if "constName" in klass.__dict__:
            descriptor = klass.__dict__["constName"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::declaredconstset_has_name():
    assert hasattr(cjsidl::declaredConstSet, "name")
    descriptor = None
    for klass in cjsidl::declaredConstSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::declaredconstset_has_constSetVersion():
    assert hasattr(cjsidl::declaredConstSet, "constSetVersion")
    descriptor = None
    for klass in cjsidl::declaredConstSet.__mro__:
        if "constSetVersion" in klass.__dict__:
            descriptor = klass.__dict__["constSetVersion"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::references_is_not_abstract():
    assert not inspect.isabstract(cjsidl::references)


def test_cjsidl::references_constructor_exists():
    assert callable(cjsidl::references.__init__)


def test_cjsidl::references_constructor_args():
    sig = inspect.signature(cjsidl::references.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::description_is_not_abstract():
    assert not inspect.isabstract(cjsidl::description)


def test_cjsidl::description_constructor_exists():
    assert callable(cjsidl::description.__init__)


def test_cjsidl::description_constructor_args():
    sig = inspect.signature(cjsidl::description.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_cjsidl::description_has_content():
    assert hasattr(cjsidl::description, "content")
    descriptor = None
    for klass in cjsidl::description.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::taggeditemdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::taggedItemDef)


def test_cjsidl::taggeditemdef_constructor_exists():
    assert callable(cjsidl::taggedItemDef.__init__)


def test_cjsidl::taggeditemdef_constructor_args():
    sig = inspect.signature(cjsidl::taggedItemDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::valuespec_is_not_abstract():
    assert not inspect.isabstract(cjsidl::valueSpec)


def test_cjsidl::valuespec_constructor_exists():
    assert callable(cjsidl::valueSpec.__init__)


def test_cjsidl::valuespec_constructor_args():
    sig = inspect.signature(cjsidl::valueSpec.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::valuespec_has_comment():
    assert hasattr(cjsidl::valueSpec, "comment")
    descriptor = None
    for klass in cjsidl::valueSpec.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::valuespec_has_value():
    assert hasattr(cjsidl::valueSpec, "value")
    descriptor = None
    for klass in cjsidl::valueSpec.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::valuespec_has_name():
    assert hasattr(cjsidl::valueSpec, "name")
    descriptor = None
    for klass in cjsidl::valueSpec.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_containerdef_is_not_abstract():
    assert not inspect.isabstract(containerDef)


def test_containerdef_constructor_exists():
    assert callable(containerDef.__init__)


def test_containerdef_constructor_args():
    sig = inspect.signature(containerDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::formatenumdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::formatEnumDef)


def test_cjsidl::formatenumdef_constructor_exists():
    assert callable(cjsidl::formatEnumDef.__init__)


def test_cjsidl::formatenumdef_constructor_args():
    sig = inspect.signature(cjsidl::formatEnumDef.__init__)
    params = list(sig.parameters.keys())
    assert "fieldFormat" in params, "Missing parameter 'fieldFormat'"
    assert "index" in params, "Missing parameter 'index'"
    assert "fieldFormatStr" in params, "Missing parameter 'fieldFormatStr'"

def test_cjsidl::formatenumdef_has_fieldFormat():
    assert hasattr(cjsidl::formatEnumDef, "fieldFormat")
    descriptor = None
    for klass in cjsidl::formatEnumDef.__mro__:
        if "fieldFormat" in klass.__dict__:
            descriptor = klass.__dict__["fieldFormat"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::formatenumdef_has_index():
    assert hasattr(cjsidl::formatEnumDef, "index")
    descriptor = None
    for klass in cjsidl::formatEnumDef.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::formatenumdef_has_fieldFormatStr():
    assert hasattr(cjsidl::formatEnumDef, "fieldFormatStr")
    descriptor = None
    for klass in cjsidl::formatEnumDef.__mro__:
        if "fieldFormatStr" in klass.__dict__:
            descriptor = klass.__dict__["fieldFormatStr"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::valuerange_is_not_abstract():
    assert not inspect.isabstract(cjsidl::valueRange)


def test_cjsidl::valuerange_constructor_exists():
    assert callable(cjsidl::valueRange.__init__)


def test_cjsidl::valuerange_constructor_args():
    sig = inspect.signature(cjsidl::valueRange.__init__)
    params = list(sig.parameters.keys())
    assert "upperLimit_type" in params, "Missing parameter 'upperLimit_type'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "lowerLim" in params, "Missing parameter 'lowerLim'"
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "lowerLimit_type" in params, "Missing parameter 'lowerLimit_type'"

def test_cjsidl::valuerange_has_upperLimit_type():
    assert hasattr(cjsidl::valueRange, "upperLimit_type")
    descriptor = None
    for klass in cjsidl::valueRange.__mro__:
        if "upperLimit_type" in klass.__dict__:
            descriptor = klass.__dict__["upperLimit_type"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::valuerange_has_comment():
    assert hasattr(cjsidl::valueRange, "comment")
    descriptor = None
    for klass in cjsidl::valueRange.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::valuerange_has_lowerLim():
    assert hasattr(cjsidl::valueRange, "lowerLim")
    descriptor = None
    for klass in cjsidl::valueRange.__mro__:
        if "lowerLim" in klass.__dict__:
            descriptor = klass.__dict__["lowerLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::valuerange_has_upperLim():
    assert hasattr(cjsidl::valueRange, "upperLim")
    descriptor = None
    for klass in cjsidl::valueRange.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::valuerange_has_lowerLimit_type():
    assert hasattr(cjsidl::valueRange, "lowerLimit_type")
    descriptor = None
    for klass in cjsidl::valueRange.__mro__:
        if "lowerLimit_type" in klass.__dict__:
            descriptor = klass.__dict__["lowerLimit_type"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::scaledrangedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::scaledRangeDef)


def test_cjsidl::scaledrangedef_constructor_exists():
    assert callable(cjsidl::scaledRangeDef.__init__)


def test_cjsidl::scaledrangedef_constructor_args():
    sig = inspect.signature(cjsidl::scaledRangeDef.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "interp" in params, "Missing parameter 'interp'"
    assert "lowerLim" in params, "Missing parameter 'lowerLim'"

def test_cjsidl::scaledrangedef_has_function():
    assert hasattr(cjsidl::scaledRangeDef, "function")
    descriptor = None
    for klass in cjsidl::scaledRangeDef.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::scaledrangedef_has_upperLim():
    assert hasattr(cjsidl::scaledRangeDef, "upperLim")
    descriptor = None
    for klass in cjsidl::scaledRangeDef.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::scaledrangedef_has_interp():
    assert hasattr(cjsidl::scaledRangeDef, "interp")
    descriptor = None
    for klass in cjsidl::scaledRangeDef.__mro__:
        if "interp" in klass.__dict__:
            descriptor = klass.__dict__["interp"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::scaledrangedef_has_lowerLim():
    assert hasattr(cjsidl::scaledRangeDef, "lowerLim")
    descriptor = None
    for klass in cjsidl::scaledRangeDef.__mro__:
        if "lowerLim" in klass.__dict__:
            descriptor = klass.__dict__["lowerLim"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::subfield_is_not_abstract():
    assert not inspect.isabstract(cjsidl::subField)


def test_cjsidl::subfield_constructor_exists():
    assert callable(cjsidl::subField.__init__)


def test_cjsidl::subfield_constructor_args():
    sig = inspect.signature(cjsidl::subField.__init__)
    params = list(sig.parameters.keys())
    assert "toIndex" in params, "Missing parameter 'toIndex'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "fromIndex" in params, "Missing parameter 'fromIndex'"

def test_cjsidl::subfield_has_toIndex():
    assert hasattr(cjsidl::subField, "toIndex")
    descriptor = None
    for klass in cjsidl::subField.__mro__:
        if "toIndex" in klass.__dict__:
            descriptor = klass.__dict__["toIndex"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::subfield_has_comment():
    assert hasattr(cjsidl::subField, "comment")
    descriptor = None
    for klass in cjsidl::subField.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::subfield_has_name():
    assert hasattr(cjsidl::subField, "name")
    descriptor = None
    for klass in cjsidl::subField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::subfield_has_fromIndex():
    assert hasattr(cjsidl::subField, "fromIndex")
    descriptor = None
    for klass in cjsidl::subField.__mro__:
        if "fromIndex" in klass.__dict__:
            descriptor = klass.__dict__["fromIndex"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::taggedunitsenum_is_not_abstract():
    assert not inspect.isabstract(cjsidl::taggedUnitsEnum)


def test_cjsidl::taggedunitsenum_constructor_exists():
    assert callable(cjsidl::taggedUnitsEnum.__init__)


def test_cjsidl::taggedunitsenum_constructor_args():
    sig = inspect.signature(cjsidl::taggedUnitsEnum.__init__)
    params = list(sig.parameters.keys())
    assert "fieldUnit" in params, "Missing parameter 'fieldUnit'"
    assert "name" in params, "Missing parameter 'name'"
    assert "const_tag" in params, "Missing parameter 'const_tag'"

def test_cjsidl::taggedunitsenum_has_fieldUnit():
    assert hasattr(cjsidl::taggedUnitsEnum, "fieldUnit")
    descriptor = None
    for klass in cjsidl::taggedUnitsEnum.__mro__:
        if "fieldUnit" in klass.__dict__:
            descriptor = klass.__dict__["fieldUnit"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::taggedunitsenum_has_name():
    assert hasattr(cjsidl::taggedUnitsEnum, "name")
    descriptor = None
    for klass in cjsidl::taggedUnitsEnum.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::taggedunitsenum_has_const_tag():
    assert hasattr(cjsidl::taggedUnitsEnum, "const_tag")
    descriptor = None
    for klass in cjsidl::taggedUnitsEnum.__mro__:
        if "const_tag" in klass.__dict__:
            descriptor = klass.__dict__["const_tag"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::valuesetdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::valueSetDef)


def test_cjsidl::valuesetdef_constructor_exists():
    assert callable(cjsidl::valueSetDef.__init__)


def test_cjsidl::valuesetdef_constructor_args():
    sig = inspect.signature(cjsidl::valueSetDef.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"

def test_cjsidl::valuesetdef_has_offset():
    assert hasattr(cjsidl::valueSetDef, "offset")
    descriptor = None
    for klass in cjsidl::valueSetDef.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::declaredeventdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::declaredEventDef)


def test_cjsidl::declaredeventdef_constructor_exists():
    assert callable(cjsidl::declaredEventDef.__init__)


def test_cjsidl::declaredeventdef_constructor_args():
    sig = inspect.signature(cjsidl::declaredEventDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::declaredeventdef_has_name():
    assert hasattr(cjsidl::declaredEventDef, "name")
    descriptor = None
    for klass in cjsidl::declaredEventDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::declaredeventdef_has_comment():
    assert hasattr(cjsidl::declaredEventDef, "comment")
    descriptor = None
    for klass in cjsidl::declaredEventDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::scopedtype_is_not_abstract():
    assert not inspect.isabstract(cjsidl::scopedType)


def test_cjsidl::scopedtype_constructor_exists():
    assert callable(cjsidl::scopedType.__init__)


def test_cjsidl::scopedtype_constructor_args():
    sig = inspect.signature(cjsidl::scopedType.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::scopedconstid_is_not_abstract():
    assert not inspect.isabstract(cjsidl::scopedConstId)


def test_cjsidl::scopedconstid_constructor_exists():
    assert callable(cjsidl::scopedConstId.__init__)


def test_cjsidl::scopedconstid_constructor_args():
    sig = inspect.signature(cjsidl::scopedConstId.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::constreference_is_not_abstract():
    assert not inspect.isabstract(cjsidl::constReference)


def test_cjsidl::constreference_constructor_exists():
    assert callable(cjsidl::constReference.__init__)


def test_cjsidl::constreference_constructor_args():
    sig = inspect.signature(cjsidl::constReference.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::constreference_has_comment():
    assert hasattr(cjsidl::constReference, "comment")
    descriptor = None
    for klass in cjsidl::constReference.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::footerscopedref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::footerScopedRef)


def test_cjsidl::footerscopedref_constructor_exists():
    assert callable(cjsidl::footerScopedRef.__init__)


def test_cjsidl::footerscopedref_constructor_args():
    sig = inspect.signature(cjsidl::footerScopedRef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::footerref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::footerRef)


def test_cjsidl::footerref_constructor_exists():
    assert callable(cjsidl::footerRef.__init__)


def test_cjsidl::footerref_constructor_args():
    sig = inspect.signature(cjsidl::footerRef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::footerref_has_comment():
    assert hasattr(cjsidl::footerRef, "comment")
    descriptor = None
    for klass in cjsidl::footerRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::footerref_has_name():
    assert hasattr(cjsidl::footerRef, "name")
    descriptor = None
    for klass in cjsidl::footerRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::bodyscopedref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::bodyScopedRef)


def test_cjsidl::bodyscopedref_constructor_exists():
    assert callable(cjsidl::bodyScopedRef.__init__)


def test_cjsidl::bodyscopedref_constructor_args():
    sig = inspect.signature(cjsidl::bodyScopedRef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::bodyref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::bodyRef)


def test_cjsidl::bodyref_constructor_exists():
    assert callable(cjsidl::bodyRef.__init__)


def test_cjsidl::bodyref_constructor_args():
    sig = inspect.signature(cjsidl::bodyRef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::bodyref_has_comment():
    assert hasattr(cjsidl::bodyRef, "comment")
    descriptor = None
    for klass in cjsidl::bodyRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::bodyref_has_name():
    assert hasattr(cjsidl::bodyRef, "name")
    descriptor = None
    for klass in cjsidl::bodyRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::headerscopedref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::headerScopedRef)


def test_cjsidl::headerscopedref_constructor_exists():
    assert callable(cjsidl::headerScopedRef.__init__)


def test_cjsidl::headerscopedref_constructor_args():
    sig = inspect.signature(cjsidl::headerScopedRef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::headerref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::headerRef)


def test_cjsidl::headerref_constructor_exists():
    assert callable(cjsidl::headerRef.__init__)


def test_cjsidl::headerref_constructor_args():
    sig = inspect.signature(cjsidl::headerRef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::headerref_has_comment():
    assert hasattr(cjsidl::headerRef, "comment")
    descriptor = None
    for klass in cjsidl::headerRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::headerref_has_name():
    assert hasattr(cjsidl::headerRef, "name")
    descriptor = None
    for klass in cjsidl::headerRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::containerref_is_not_abstract():
    assert not inspect.isabstract(cjsidl::containerRef)


def test_cjsidl::containerref_constructor_exists():
    assert callable(cjsidl::containerRef.__init__)


def test_cjsidl::containerref_constructor_args():
    sig = inspect.signature(cjsidl::containerRef.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::containerref_has_optional():
    assert hasattr(cjsidl::containerRef, "optional")
    descriptor = None
    for klass in cjsidl::containerRef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::containerref_has_name():
    assert hasattr(cjsidl::containerRef, "name")
    descriptor = None
    for klass in cjsidl::containerRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::containerref_has_comment():
    assert hasattr(cjsidl::containerRef, "comment")
    descriptor = None
    for klass in cjsidl::containerRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::containerdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::containerDef)


def test_cjsidl::containerdef_constructor_exists():
    assert callable(cjsidl::containerDef.__init__)


def test_cjsidl::containerdef_constructor_args():
    sig = inspect.signature(cjsidl::containerDef.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::containerdef_has_optional():
    assert hasattr(cjsidl::containerDef, "optional")
    descriptor = None
    for klass in cjsidl::containerDef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::containerdef_has_comment():
    assert hasattr(cjsidl::containerDef, "comment")
    descriptor = None
    for klass in cjsidl::containerDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::containerdef_has_name():
    assert hasattr(cjsidl::containerDef, "name")
    descriptor = None
    for klass in cjsidl::containerDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::footerdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::footerDef)


def test_cjsidl::footerdef_constructor_exists():
    assert callable(cjsidl::footerDef.__init__)


def test_cjsidl::footerdef_constructor_args():
    sig = inspect.signature(cjsidl::footerDef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::footerdef_has_comment():
    assert hasattr(cjsidl::footerDef, "comment")
    descriptor = None
    for klass in cjsidl::footerDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::footerdef_has_name():
    assert hasattr(cjsidl::footerDef, "name")
    descriptor = None
    for klass in cjsidl::footerDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::bodydef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::bodyDef)


def test_cjsidl::bodydef_constructor_exists():
    assert callable(cjsidl::bodyDef.__init__)


def test_cjsidl::bodydef_constructor_args():
    sig = inspect.signature(cjsidl::bodyDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::bodydef_has_name():
    assert hasattr(cjsidl::bodyDef, "name")
    descriptor = None
    for klass in cjsidl::bodyDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::bodydef_has_comment():
    assert hasattr(cjsidl::bodyDef, "comment")
    descriptor = None
    for klass in cjsidl::bodyDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::headerdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::headerDef)


def test_cjsidl::headerdef_constructor_exists():
    assert callable(cjsidl::headerDef.__init__)


def test_cjsidl::headerdef_constructor_args():
    sig = inspect.signature(cjsidl::headerDef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::headerdef_has_comment():
    assert hasattr(cjsidl::headerDef, "comment")
    descriptor = None
    for klass in cjsidl::headerDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::headerdef_has_name():
    assert hasattr(cjsidl::headerDef, "name")
    descriptor = None
    for klass in cjsidl::headerDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::varformatfield_is_not_abstract():
    assert not inspect.isabstract(cjsidl::varFormatField)


def test_cjsidl::varformatfield_constructor_exists():
    assert callable(cjsidl::varFormatField.__init__)


def test_cjsidl::varformatfield_constructor_args():
    sig = inspect.signature(cjsidl::varFormatField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "units" in params, "Missing parameter 'units'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "countComment" in params, "Missing parameter 'countComment'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::varformatfield_has_name():
    assert hasattr(cjsidl::varFormatField, "name")
    descriptor = None
    for klass in cjsidl::varFormatField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varformatfield_has_units():
    assert hasattr(cjsidl::varFormatField, "units")
    descriptor = None
    for klass in cjsidl::varFormatField.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varformatfield_has_optional():
    assert hasattr(cjsidl::varFormatField, "optional")
    descriptor = None
    for klass in cjsidl::varFormatField.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varformatfield_has_countComment():
    assert hasattr(cjsidl::varFormatField, "countComment")
    descriptor = None
    for klass in cjsidl::varFormatField.__mro__:
        if "countComment" in klass.__dict__:
            descriptor = klass.__dict__["countComment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varformatfield_has_comment():
    assert hasattr(cjsidl::varFormatField, "comment")
    descriptor = None
    for klass in cjsidl::varFormatField.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::varlenfield_is_not_abstract():
    assert not inspect.isabstract(cjsidl::varLenField)


def test_cjsidl::varlenfield_constructor_exists():
    assert callable(cjsidl::varLenField.__init__)


def test_cjsidl::varlenfield_constructor_args():
    sig = inspect.signature(cjsidl::varLenField.__init__)
    params = list(sig.parameters.keys())
    assert "countComment" in params, "Missing parameter 'countComment'"
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "fieldFormat" in params, "Missing parameter 'fieldFormat'"
    assert "lowerLim" in params, "Missing parameter 'lowerLim'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_cjsidl::varlenfield_has_countComment():
    assert hasattr(cjsidl::varLenField, "countComment")
    descriptor = None
    for klass in cjsidl::varLenField.__mro__:
        if "countComment" in klass.__dict__:
            descriptor = klass.__dict__["countComment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenfield_has_upperLim():
    assert hasattr(cjsidl::varLenField, "upperLim")
    descriptor = None
    for klass in cjsidl::varLenField.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenfield_has_comment():
    assert hasattr(cjsidl::varLenField, "comment")
    descriptor = None
    for klass in cjsidl::varLenField.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenfield_has_name():
    assert hasattr(cjsidl::varLenField, "name")
    descriptor = None
    for klass in cjsidl::varLenField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenfield_has_fieldFormat():
    assert hasattr(cjsidl::varLenField, "fieldFormat")
    descriptor = None
    for klass in cjsidl::varLenField.__mro__:
        if "fieldFormat" in klass.__dict__:
            descriptor = klass.__dict__["fieldFormat"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenfield_has_lowerLim():
    assert hasattr(cjsidl::varLenField, "lowerLim")
    descriptor = None
    for klass in cjsidl::varLenField.__mro__:
        if "lowerLim" in klass.__dict__:
            descriptor = klass.__dict__["lowerLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenfield_has_optional():
    assert hasattr(cjsidl::varLenField, "optional")
    descriptor = None
    for klass in cjsidl::varLenField.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::varlenstring_is_not_abstract():
    assert not inspect.isabstract(cjsidl::varLenString)


def test_cjsidl::varlenstring_constructor_exists():
    assert callable(cjsidl::varLenString.__init__)


def test_cjsidl::varlenstring_constructor_args():
    sig = inspect.signature(cjsidl::varLenString.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "lowerLim" in params, "Missing parameter 'lowerLim'"

def test_cjsidl::varlenstring_has_optional():
    assert hasattr(cjsidl::varLenString, "optional")
    descriptor = None
    for klass in cjsidl::varLenString.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenstring_has_upperLim():
    assert hasattr(cjsidl::varLenString, "upperLim")
    descriptor = None
    for klass in cjsidl::varLenString.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenstring_has_comment():
    assert hasattr(cjsidl::varLenString, "comment")
    descriptor = None
    for klass in cjsidl::varLenString.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenstring_has_name():
    assert hasattr(cjsidl::varLenString, "name")
    descriptor = None
    for klass in cjsidl::varLenString.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varlenstring_has_lowerLim():
    assert hasattr(cjsidl::varLenString, "lowerLim")
    descriptor = None
    for klass in cjsidl::varLenString.__mro__:
        if "lowerLim" in klass.__dict__:
            descriptor = klass.__dict__["lowerLim"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::fixedlenstring_is_not_abstract():
    assert not inspect.isabstract(cjsidl::fixedLenString)


def test_cjsidl::fixedlenstring_constructor_exists():
    assert callable(cjsidl::fixedLenString.__init__)


def test_cjsidl::fixedlenstring_constructor_args():
    sig = inspect.signature(cjsidl::fixedLenString.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "upperLim" in params, "Missing parameter 'upperLim'"

def test_cjsidl::fixedlenstring_has_name():
    assert hasattr(cjsidl::fixedLenString, "name")
    descriptor = None
    for klass in cjsidl::fixedLenString.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::fixedlenstring_has_comment():
    assert hasattr(cjsidl::fixedLenString, "comment")
    descriptor = None
    for klass in cjsidl::fixedLenString.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::fixedlenstring_has_optional():
    assert hasattr(cjsidl::fixedLenString, "optional")
    descriptor = None
    for klass in cjsidl::fixedLenString.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::fixedlenstring_has_upperLim():
    assert hasattr(cjsidl::fixedLenString, "upperLim")
    descriptor = None
    for klass in cjsidl::fixedLenString.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::bitfielddef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::bitfieldDef)


def test_cjsidl::bitfielddef_constructor_exists():
    assert callable(cjsidl::bitfieldDef.__init__)


def test_cjsidl::bitfielddef_constructor_args():
    sig = inspect.signature(cjsidl::bitfieldDef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_cjsidl::bitfielddef_has_type():
    assert hasattr(cjsidl::bitfieldDef, "type")
    descriptor = None
    for klass in cjsidl::bitfieldDef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::bitfielddef_has_comment():
    assert hasattr(cjsidl::bitfieldDef, "comment")
    descriptor = None
    for klass in cjsidl::bitfieldDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::bitfielddef_has_name():
    assert hasattr(cjsidl::bitfieldDef, "name")
    descriptor = None
    for klass in cjsidl::bitfieldDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::bitfielddef_has_optional():
    assert hasattr(cjsidl::bitfieldDef, "optional")
    descriptor = None
    for klass in cjsidl::bitfieldDef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::action_is_not_abstract():
    assert not inspect.isabstract(cjsidl::action)


def test_cjsidl::action_constructor_exists():
    assert callable(cjsidl::action.__init__)


def test_cjsidl::action_constructor_args():
    sig = inspect.signature(cjsidl::action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::action_has_name():
    assert hasattr(cjsidl::action, "name")
    descriptor = None
    for klass in cjsidl::action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::action_has_comment():
    assert hasattr(cjsidl::action, "comment")
    descriptor = None
    for klass in cjsidl::action.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::varfield_is_not_abstract():
    assert not inspect.isabstract(cjsidl::varField)


def test_cjsidl::varfield_constructor_exists():
    assert callable(cjsidl::varField.__init__)


def test_cjsidl::varfield_constructor_args():
    sig = inspect.signature(cjsidl::varField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_cjsidl::varfield_has_name():
    assert hasattr(cjsidl::varField, "name")
    descriptor = None
    for klass in cjsidl::varField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varfield_has_comment():
    assert hasattr(cjsidl::varField, "comment")
    descriptor = None
    for klass in cjsidl::varField.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::varfield_has_optional():
    assert hasattr(cjsidl::varField, "optional")
    descriptor = None
    for klass in cjsidl::varField.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::fixedfielddef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::fixedFieldDef)


def test_cjsidl::fixedfielddef_constructor_exists():
    assert callable(cjsidl::fixedFieldDef.__init__)


def test_cjsidl::fixedfielddef_constructor_args():
    sig = inspect.signature(cjsidl::fixedFieldDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "fieldUnit" in params, "Missing parameter 'fieldUnit'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::fixedfielddef_has_name():
    assert hasattr(cjsidl::fixedFieldDef, "name")
    descriptor = None
    for klass in cjsidl::fixedFieldDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::fixedfielddef_has_fieldUnit():
    assert hasattr(cjsidl::fixedFieldDef, "fieldUnit")
    descriptor = None
    for klass in cjsidl::fixedFieldDef.__mro__:
        if "fieldUnit" in klass.__dict__:
            descriptor = klass.__dict__["fieldUnit"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::fixedfielddef_has_optional():
    assert hasattr(cjsidl::fixedFieldDef, "optional")
    descriptor = None
    for klass in cjsidl::fixedFieldDef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::fixedfielddef_has_comment():
    assert hasattr(cjsidl::fixedFieldDef, "comment")
    descriptor = None
    for klass in cjsidl::fixedFieldDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::sequencedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::sequenceDef)


def test_cjsidl::sequencedef_constructor_exists():
    assert callable(cjsidl::sequenceDef.__init__)


def test_cjsidl::sequencedef_constructor_args():
    sig = inspect.signature(cjsidl::sequenceDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::variantdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::variantDef)


def test_cjsidl::variantdef_constructor_exists():
    assert callable(cjsidl::variantDef.__init__)


def test_cjsidl::variantdef_constructor_args():
    sig = inspect.signature(cjsidl::variantDef.__init__)
    params = list(sig.parameters.keys())
    assert "minCount" in params, "Missing parameter 'minCount'"
    assert "maxCount" in params, "Missing parameter 'maxCount'"
    assert "vtagComment" in params, "Missing parameter 'vtagComment'"

def test_cjsidl::variantdef_has_minCount():
    assert hasattr(cjsidl::variantDef, "minCount")
    descriptor = None
    for klass in cjsidl::variantDef.__mro__:
        if "minCount" in klass.__dict__:
            descriptor = klass.__dict__["minCount"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::variantdef_has_maxCount():
    assert hasattr(cjsidl::variantDef, "maxCount")
    descriptor = None
    for klass in cjsidl::variantDef.__mro__:
        if "maxCount" in klass.__dict__:
            descriptor = klass.__dict__["maxCount"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::variantdef_has_vtagComment():
    assert hasattr(cjsidl::variantDef, "vtagComment")
    descriptor = None
    for klass in cjsidl::variantDef.__mro__:
        if "vtagComment" in klass.__dict__:
            descriptor = klass.__dict__["vtagComment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::listdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::listDef)


def test_cjsidl::listdef_constructor_exists():
    assert callable(cjsidl::listDef.__init__)


def test_cjsidl::listdef_constructor_args():
    sig = inspect.signature(cjsidl::listDef.__init__)
    params = list(sig.parameters.keys())
    assert "minCount" in params, "Missing parameter 'minCount'"
    assert "countComment" in params, "Missing parameter 'countComment'"
    assert "maxCount" in params, "Missing parameter 'maxCount'"

def test_cjsidl::listdef_has_minCount():
    assert hasattr(cjsidl::listDef, "minCount")
    descriptor = None
    for klass in cjsidl::listDef.__mro__:
        if "minCount" in klass.__dict__:
            descriptor = klass.__dict__["minCount"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::listdef_has_countComment():
    assert hasattr(cjsidl::listDef, "countComment")
    descriptor = None
    for klass in cjsidl::listDef.__mro__:
        if "countComment" in klass.__dict__:
            descriptor = klass.__dict__["countComment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::listdef_has_maxCount():
    assert hasattr(cjsidl::listDef, "maxCount")
    descriptor = None
    for klass in cjsidl::listDef.__mro__:
        if "maxCount" in klass.__dict__:
            descriptor = klass.__dict__["maxCount"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::recorddef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::recordDef)


def test_cjsidl::recorddef_constructor_exists():
    assert callable(cjsidl::recordDef.__init__)


def test_cjsidl::recorddef_constructor_args():
    sig = inspect.signature(cjsidl::recordDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::arraydef_is_not_abstract():
    assert not inspect.isabstract(cjsidl::arrayDef)


def test_cjsidl::arraydef_constructor_exists():
    assert callable(cjsidl::arrayDef.__init__)


def test_cjsidl::arraydef_constructor_args():
    sig = inspect.signature(cjsidl::arrayDef.__init__)
    params = list(sig.parameters.keys())
    assert "arraySize" in params, "Missing parameter 'arraySize'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::arraydef_has_arraySize():
    assert hasattr(cjsidl::arrayDef, "arraySize")
    descriptor = None
    for klass in cjsidl::arrayDef.__mro__:
        if "arraySize" in klass.__dict__:
            descriptor = klass.__dict__["arraySize"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::arraydef_has_comment():
    assert hasattr(cjsidl::arrayDef, "comment")
    descriptor = None
    for klass in cjsidl::arrayDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::arraydef_has_optional():
    assert hasattr(cjsidl::arrayDef, "optional")
    descriptor = None
    for klass in cjsidl::arrayDef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::arraydef_has_name():
    assert hasattr(cjsidl::arrayDef, "name")
    descriptor = None
    for klass in cjsidl::arrayDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::simplenumerictype_is_not_abstract():
    assert not inspect.isabstract(cjsidl::simpleNumericType)


def test_cjsidl::simplenumerictype_constructor_exists():
    assert callable(cjsidl::simpleNumericType.__init__)


def test_cjsidl::simplenumerictype_constructor_args():
    sig = inspect.signature(cjsidl::simpleNumericType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cjsidl::simplenumerictype_has_type():
    assert hasattr(cjsidl::simpleNumericType, "type")
    descriptor = None
    for klass in cjsidl::simpleNumericType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::simpletransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl::simpleTransition)


def test_cjsidl::simpletransition_constructor_exists():
    assert callable(cjsidl::simpleTransition.__init__)


def test_cjsidl::simpletransition_constructor_args():
    sig = inspect.signature(cjsidl::simpleTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::simpletransition_has_comment():
    assert hasattr(cjsidl::simpleTransition, "comment")
    descriptor = None
    for klass in cjsidl::simpleTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::internaltransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl::internalTransition)


def test_cjsidl::internaltransition_constructor_exists():
    assert callable(cjsidl::internalTransition.__init__)


def test_cjsidl::internaltransition_constructor_args():
    sig = inspect.signature(cjsidl::internalTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::internaltransition_has_comment():
    assert hasattr(cjsidl::internalTransition, "comment")
    descriptor = None
    for klass in cjsidl::internalTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::guardaction_is_not_abstract():
    assert not inspect.isabstract(cjsidl::guardAction)


def test_cjsidl::guardaction_constructor_exists():
    assert callable(cjsidl::guardAction.__init__)


def test_cjsidl::guardaction_constructor_args():
    sig = inspect.signature(cjsidl::guardAction.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl::guardaction_has_not_():
    assert hasattr(cjsidl::guardAction, "not_")
    descriptor = None
    for klass in cjsidl::guardAction.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::guardaction_has_name():
    assert hasattr(cjsidl::guardAction, "name")
    descriptor = None
    for klass in cjsidl::guardAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::guardparam_is_not_abstract():
    assert not inspect.isabstract(cjsidl::guardParam)


def test_cjsidl::guardparam_constructor_exists():
    assert callable(cjsidl::guardParam.__init__)


def test_cjsidl::guardparam_constructor_args():
    sig = inspect.signature(cjsidl::guardParam.__init__)
    params = list(sig.parameters.keys())
    assert "guardConst" in params, "Missing parameter 'guardConst'"

def test_cjsidl::guardparam_has_guardConst():
    assert hasattr(cjsidl::guardParam, "guardConst")
    descriptor = None
    for klass in cjsidl::guardParam.__mro__:
        if "guardConst" in klass.__dict__:
            descriptor = klass.__dict__["guardConst"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::poptransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl::popTransition)


def test_cjsidl::poptransition_constructor_exists():
    assert callable(cjsidl::popTransition.__init__)


def test_cjsidl::poptransition_constructor_args():
    sig = inspect.signature(cjsidl::popTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::poptransition_has_comment():
    assert hasattr(cjsidl::popTransition, "comment")
    descriptor = None
    for klass in cjsidl::popTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::pushtransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl::pushTransition)


def test_cjsidl::pushtransition_constructor_exists():
    assert callable(cjsidl::pushTransition.__init__)


def test_cjsidl::pushtransition_constructor_args():
    sig = inspect.signature(cjsidl::pushTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::pushtransition_has_comment():
    assert hasattr(cjsidl::pushTransition, "comment")
    descriptor = None
    for klass in cjsidl::pushTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::nextstate_is_not_abstract():
    assert not inspect.isabstract(cjsidl::nextState)


def test_cjsidl::nextstate_constructor_exists():
    assert callable(cjsidl::nextState.__init__)


def test_cjsidl::nextstate_constructor_args():
    sig = inspect.signature(cjsidl::nextState.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::nextstate_has_comment():
    assert hasattr(cjsidl::nextState, "comment")
    descriptor = None
    for klass in cjsidl::nextState.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::sendactionlist_is_not_abstract():
    assert not inspect.isabstract(cjsidl::sendActionList)


def test_cjsidl::sendactionlist_constructor_exists():
    assert callable(cjsidl::sendActionList.__init__)


def test_cjsidl::sendactionlist_constructor_args():
    sig = inspect.signature(cjsidl::sendActionList.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::actionlist_is_not_abstract():
    assert not inspect.isabstract(cjsidl::actionList)


def test_cjsidl::actionlist_constructor_exists():
    assert callable(cjsidl::actionList.__init__)


def test_cjsidl::actionlist_constructor_args():
    sig = inspect.signature(cjsidl::actionList.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::defaulttransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl::defaultTransition)


def test_cjsidl::defaulttransition_constructor_exists():
    assert callable(cjsidl::defaultTransition.__init__)


def test_cjsidl::defaulttransition_constructor_args():
    sig = inspect.signature(cjsidl::defaultTransition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::defaulttransition_has_type():
    assert hasattr(cjsidl::defaultTransition, "type")
    descriptor = None
    for klass in cjsidl::defaultTransition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::defaulttransition_has_comment():
    assert hasattr(cjsidl::defaultTransition, "comment")
    descriptor = None
    for klass in cjsidl::defaultTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::guard_is_not_abstract():
    assert not inspect.isabstract(cjsidl::guard)


def test_cjsidl::guard_constructor_exists():
    assert callable(cjsidl::guard.__init__)


def test_cjsidl::guard_constructor_args():
    sig = inspect.signature(cjsidl::guard.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "logicalOperator" in params, "Missing parameter 'logicalOperator'"
    assert "equiv" in params, "Missing parameter 'equiv'"

def test_cjsidl::guard_has_comment():
    assert hasattr(cjsidl::guard, "comment")
    descriptor = None
    for klass in cjsidl::guard.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::guard_has_logicalOperator():
    assert hasattr(cjsidl::guard, "logicalOperator")
    descriptor = None
    for klass in cjsidl::guard.__mro__:
        if "logicalOperator" in klass.__dict__:
            descriptor = klass.__dict__["logicalOperator"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::guard_has_equiv():
    assert hasattr(cjsidl::guard, "equiv")
    descriptor = None
    for klass in cjsidl::guard.__mro__:
        if "equiv" in klass.__dict__:
            descriptor = klass.__dict__["equiv"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::scopedeventtype_is_not_abstract():
    assert not inspect.isabstract(cjsidl::scopedEventType)


def test_cjsidl::scopedeventtype_constructor_exists():
    assert callable(cjsidl::scopedEventType.__init__)


def test_cjsidl::scopedeventtype_constructor_args():
    sig = inspect.signature(cjsidl::scopedEventType.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl::transparam_is_not_abstract():
    assert not inspect.isabstract(cjsidl::transParam)


def test_cjsidl::transparam_constructor_exists():
    assert callable(cjsidl::transParam.__init__)


def test_cjsidl::transparam_constructor_args():
    sig = inspect.signature(cjsidl::transParam.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unsignedType" in params, "Missing parameter 'unsignedType'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl::transparam_has_name():
    assert hasattr(cjsidl::transParam, "name")
    descriptor = None
    for klass in cjsidl::transParam.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::transparam_has_unsignedType():
    assert hasattr(cjsidl::transParam, "unsignedType")
    descriptor = None
    for klass in cjsidl::transParam.__mro__:
        if "unsignedType" in klass.__dict__:
            descriptor = klass.__dict__["unsignedType"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl::transparam_has_comment():
    assert hasattr(cjsidl::transParam, "comment")
    descriptor = None
    for klass in cjsidl::transParam.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl::transparams_is_not_abstract():
    assert not inspect.isabstract(cjsidl::transParams)


def test_cjsidl::transparams_constructor_exists():
    assert callable(cjsidl::transParams.__init__)


def test_cjsidl::transparams_constructor_args():
    sig = inspect.signature(cjsidl::transParams.__init__)
    params = list(sig.parameters.keys())

def test_field_format_exists():
    # Check that the Enumeration exists
    assert FIELD_FORMAT is not None

def test_field_format_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FIELD_FORMAT]
    expected_literals = [
        "JPEG",
        "USER_DEFINED",
        "BMP",
        "WAV",
        "AU",
        "MPEG2",
        "MP4",
        "JAUS_MESSAGE",
        "RNC",
        "MP2",
        "XML",
        "XSD",
        "MJPEG",
        "MPEG1",
        "RNG",
        "MP3",
        "RAW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FIELD_FORMAT"

def test_unit_exists():
    # Check that the Enumeration exists
    assert UNIT is not None

def test_unit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UNIT]
    expected_literals = [
        "AMPPERSQRMETER",
        "AMP_PER_METER",
        "CELSIUS",
        "RADIAN",
        "KELVIN",
        "VOLT_PER_METER",
        "BEL",
        "HRZ",
        "RAD_PER_SEC",
        "RECIPROCAL_METER",
        "PASCAL_SEC",
        "TESLA",
        "NEWTON_METER",
        "HECTARE",
        "ROENTGEN",
        "METER_PER_SEC",
        "BARN",
        "LUMEN",
        "GRAY_PER_SEC",
        "SIEMENS",
        "COULOMB_PER_KG",
        "HENRY",
        "RAD_PER_SEC_SQR",
        "WATT",
        "ANGSROM",
        "JOULE",
        "ONE",
        "WEBER",
        "NMILE",
        "OHM",
        "STE_RAD",
        "FARAD_PER_METER",
        "LTR",
        "JOULE_PER_KELVIN",
        "CANDELA_PER_SQUARE_METER",
        "WATT_PER_SQR_METER_STERAD",
        "BAR",
        "NEWTON",
        "SEC",
        "JOULE_PER_MOLE_KELVIN",
        "CURIE",
        "COULOMB",
        "COULOMB_PER_SQR_METER",
        "CUBIC_METER",
        "METER",
        "DAY",
        "VOLT",
        "CANDELA",
        "RAD",
        "WATT_PER_SQR_METER",
        "BECQUEREL",
        "HENRY_PER_METER",
        "CUBICMETERPERKG",
        "MOLE_PER_CUBIC_METER",
        "LUX",
        "KG_PER_CUBIC_METER",
        "MOLE",
        "JOULES_PER_CUBIC_METER",
        "NEWTON_PER_METER",
        "SQR_METER",
        "COULOMB_PER_CUBIC_METER",
        "FARAD",
        "HOUR",
        "KATAL_PER_CUBIC_METER",
        "KATAL",
        "DEGREE",
        "MTON",
        "KNOT",
        "KG",
        "PASCAL",
        "NEPER",
        "SIEVERT",
        "MIN",
        "JOULE_PER_KG",
        "REM",
        "JOULE_PER_MOLE",
        "AMP",
        "ARE",
        "METER_PER_SEC_SQR",
        "WATT_PER_METER_KELVIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UNIT"


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
cjsidl::stateMachine_strategy = st.builds(
    cjsidl::stateMachine,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl::eventDef_strategy = st.builds(
    cjsidl::eventDef,
    name=
        safe_text
)
cjsidl::transition_strategy = st.builds(
    cjsidl::transition,
    comment=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
cjsidl::exit_strategy = st.builds(
    cjsidl::exit,
    comment=
        safe_text
)
cjsidl::entry_strategy = st.builds(
    cjsidl::entry,
    comment=
        safe_text
)
cjsidl::defaultState_strategy = st.builds(
    cjsidl::defaultState,
    comment=
        safe_text
)
cjsidl::state_strategy = st.builds(
    cjsidl::state,
    name=
        safe_text,
    initial=
        safe_text,
    comment=
        safe_text
)
cjsidl::startState_strategy = st.builds(
    cjsidl::startState,
    comment=
        safe_text
)
cjsidl::constDef_strategy = st.builds(
    cjsidl::constDef,
    comment=
        safe_text,
    constValue=
        safe_text,
    fieldUnits=
        safe_text,
    name=
        safe_text
)
cjsidl::declaredConstSetRef_strategy = st.builds(
    cjsidl::declaredConstSetRef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::messageScopedRef_strategy = st.builds(
    cjsidl::messageScopedRef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl::messageRef_strategy = st.builds(
    cjsidl::messageRef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl::messageDef_strategy = st.builds(
    cjsidl::messageDef,
    messageID=
        safe_text,
    command=
        safe_text,
    name=
        safe_text
)
cjsidl::messages_strategy = st.builds(
    cjsidl::messages,
)
cjsidl::scopedTypeId_strategy = st.builds(
    cjsidl::scopedTypeId,
    optional=
        safe_text,
    comment=
        safe_text,
    scopedName=
        safe_text
)
cjsidl::typeReference_strategy = st.builds(
    cjsidl::typeReference,
    comment=
        safe_text,
    name=
        safe_text,
    optional=
        safe_text
)
cjsidl::typeDef_strategy = st.builds(
    cjsidl::typeDef,
)
cjsidl::declaredTypeSetRef_strategy = st.builds(
    cjsidl::declaredTypeSetRef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::serviceDef_strategy = st.builds(
    cjsidl::serviceDef,
    serviceName=
        safe_text,
    name=
        safe_text,
    serviceVersion=
        safe_text,
    assumpt=
        safe_text
)
cjsidl::EObject_strategy = st.builds(
    cjsidl::EObject,
)
cjsidl::jaus_strategy = st.builds(
    cjsidl::jaus,
)
cjsidl::refAttr_strategy = st.builds(
    cjsidl::refAttr,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::protocolBehavior_strategy = st.builds(
    cjsidl::protocolBehavior,
    stateless=
        safe_text,
    comment=
        safe_text
)
cjsidl::internalEventSet_strategy = st.builds(
    cjsidl::internalEventSet,
    comment=
        safe_text
)
cjsidl::messageSet_strategy = st.builds(
    cjsidl::messageSet,
    outputComment=
        safe_text,
    comment=
        safe_text,
    inputComment=
        safe_text
)
cjsidl::declaredTypeSet_strategy = st.builds(
    cjsidl::declaredTypeSet,
    typeName=
        safe_text,
    version=
        safe_text,
    name=
        safe_text
)
cjsidl::declaredConstSet_strategy = st.builds(
    cjsidl::declaredConstSet,
    constName=
        safe_text,
    name=
        safe_text,
    constSetVersion=
        safe_text
)
cjsidl::references_strategy = st.builds(
    cjsidl::references,
)
cjsidl::description_strategy = st.builds(
    cjsidl::description,
    content=
        safe_text
)
cjsidl::taggedItemDef_strategy = st.builds(
    cjsidl::taggedItemDef,
)
cjsidl::valueSpec_strategy = st.builds(
    cjsidl::valueSpec,
    comment=
        safe_text,
    value=
        safe_text,
    name=
        safe_text
)
containerDef_strategy = st.builds(
    containerDef,
)
cjsidl::formatEnumDef_strategy = st.builds(
    cjsidl::formatEnumDef,
    fieldFormat=
        safe_text,
    index=
        safe_text,
    fieldFormatStr=
        safe_text
)
cjsidl::valueRange_strategy = st.builds(
    cjsidl::valueRange,
    upperLimit_type=
        safe_text,
    comment=
        safe_text,
    lowerLim=
        safe_text,
    upperLim=
        safe_text,
    lowerLimit_type=
        safe_text
)
cjsidl::scaledRangeDef_strategy = st.builds(
    cjsidl::scaledRangeDef,
    function=
        safe_text,
    upperLim=
        safe_text,
    interp=
        safe_text,
    lowerLim=
        safe_text
)
cjsidl::subField_strategy = st.builds(
    cjsidl::subField,
    toIndex=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text,
    fromIndex=
        safe_text
)
cjsidl::taggedUnitsEnum_strategy = st.builds(
    cjsidl::taggedUnitsEnum,
    fieldUnit=
        safe_text,
    name=
        safe_text,
    const_tag=
        safe_text
)
cjsidl::valueSetDef_strategy = st.builds(
    cjsidl::valueSetDef,
    offset=
        safe_text
)
cjsidl::declaredEventDef_strategy = st.builds(
    cjsidl::declaredEventDef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl::scopedType_strategy = st.builds(
    cjsidl::scopedType,
)
cjsidl::scopedConstId_strategy = st.builds(
    cjsidl::scopedConstId,
)
cjsidl::constReference_strategy = st.builds(
    cjsidl::constReference,
    comment=
        safe_text
)
cjsidl::footerScopedRef_strategy = st.builds(
    cjsidl::footerScopedRef,
)
cjsidl::footerRef_strategy = st.builds(
    cjsidl::footerRef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::bodyScopedRef_strategy = st.builds(
    cjsidl::bodyScopedRef,
)
cjsidl::bodyRef_strategy = st.builds(
    cjsidl::bodyRef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::headerScopedRef_strategy = st.builds(
    cjsidl::headerScopedRef,
)
cjsidl::headerRef_strategy = st.builds(
    cjsidl::headerRef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::containerRef_strategy = st.builds(
    cjsidl::containerRef,
    optional=
        safe_text,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl::containerDef_strategy = st.builds(
    cjsidl::containerDef,
    optional=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::footerDef_strategy = st.builds(
    cjsidl::footerDef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::bodyDef_strategy = st.builds(
    cjsidl::bodyDef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl::headerDef_strategy = st.builds(
    cjsidl::headerDef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl::varFormatField_strategy = st.builds(
    cjsidl::varFormatField,
    name=
        safe_text,
    units=
        safe_text,
    optional=
        safe_text,
    countComment=
        safe_text,
    comment=
        safe_text
)
cjsidl::varLenField_strategy = st.builds(
    cjsidl::varLenField,
    countComment=
        safe_text,
    upperLim=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text,
    fieldFormat=
        safe_text,
    lowerLim=
        safe_text,
    optional=
        safe_text
)
cjsidl::varLenString_strategy = st.builds(
    cjsidl::varLenString,
    optional=
        safe_text,
    upperLim=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text,
    lowerLim=
        safe_text
)
cjsidl::fixedLenString_strategy = st.builds(
    cjsidl::fixedLenString,
    name=
        safe_text,
    comment=
        safe_text,
    optional=
        safe_text,
    upperLim=
        safe_text
)
cjsidl::bitfieldDef_strategy = st.builds(
    cjsidl::bitfieldDef,
    type=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text,
    optional=
        safe_text
)
cjsidl::action_strategy = st.builds(
    cjsidl::action,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl::varField_strategy = st.builds(
    cjsidl::varField,
    name=
        safe_text,
    comment=
        safe_text,
    optional=
        safe_text
)
cjsidl::fixedFieldDef_strategy = st.builds(
    cjsidl::fixedFieldDef,
    name=
        safe_text,
    fieldUnit=
        safe_text,
    optional=
        safe_text,
    comment=
        safe_text
)
cjsidl::sequenceDef_strategy = st.builds(
    cjsidl::sequenceDef,
)
cjsidl::variantDef_strategy = st.builds(
    cjsidl::variantDef,
    minCount=
        safe_text,
    maxCount=
        safe_text,
    vtagComment=
        safe_text
)
cjsidl::listDef_strategy = st.builds(
    cjsidl::listDef,
    minCount=
        safe_text,
    countComment=
        safe_text,
    maxCount=
        safe_text
)
cjsidl::recordDef_strategy = st.builds(
    cjsidl::recordDef,
)
cjsidl::arrayDef_strategy = st.builds(
    cjsidl::arrayDef,
    arraySize=
        safe_text,
    comment=
        safe_text,
    optional=
        safe_text,
    name=
        safe_text
)
cjsidl::simpleNumericType_strategy = st.builds(
    cjsidl::simpleNumericType,
    type=
        safe_text
)
cjsidl::simpleTransition_strategy = st.builds(
    cjsidl::simpleTransition,
    comment=
        safe_text
)
cjsidl::internalTransition_strategy = st.builds(
    cjsidl::internalTransition,
    comment=
        safe_text
)
cjsidl::guardAction_strategy = st.builds(
    cjsidl::guardAction,
    not_=
        safe_text,
    name=
        safe_text
)
cjsidl::guardParam_strategy = st.builds(
    cjsidl::guardParam,
    guardConst=
        safe_text
)
cjsidl::popTransition_strategy = st.builds(
    cjsidl::popTransition,
    comment=
        safe_text
)
cjsidl::pushTransition_strategy = st.builds(
    cjsidl::pushTransition,
    comment=
        safe_text
)
cjsidl::nextState_strategy = st.builds(
    cjsidl::nextState,
    comment=
        safe_text
)
cjsidl::sendActionList_strategy = st.builds(
    cjsidl::sendActionList,
)
cjsidl::actionList_strategy = st.builds(
    cjsidl::actionList,
)
cjsidl::defaultTransition_strategy = st.builds(
    cjsidl::defaultTransition,
    type=
        safe_text,
    comment=
        safe_text
)
cjsidl::guard_strategy = st.builds(
    cjsidl::guard,
    comment=
        safe_text,
    logicalOperator=
        safe_text,
    equiv=
        safe_text
)
cjsidl::scopedEventType_strategy = st.builds(
    cjsidl::scopedEventType,
)
cjsidl::transParam_strategy = st.builds(
    cjsidl::transParam,
    name=
        safe_text,
    unsignedType=
        safe_text,
    comment=
        safe_text
)
cjsidl::transParams_strategy = st.builds(
    cjsidl::transParams,
)

@given(instance=cjsidl::stateMachine_strategy)
@settings(max_examples=50)
def test_cjsidl::statemachine_instantiation(instance):
    assert isinstance(instance, cjsidl::stateMachine)

@given(instance=cjsidl::stateMachine_strategy)
def test_cjsidl::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::stateMachine_strategy)
def test_cjsidl::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::stateMachine_strategy)
def test_cjsidl::statemachine_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::stateMachine_strategy)
def test_cjsidl::statemachine_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::eventDef_strategy)
@settings(max_examples=50)
def test_cjsidl::eventdef_instantiation(instance):
    assert isinstance(instance, cjsidl::eventDef)

@given(instance=cjsidl::eventDef_strategy)
def test_cjsidl::eventdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::eventDef_strategy)
def test_cjsidl::eventdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::transition_strategy)
@settings(max_examples=50)
def test_cjsidl::transition_instantiation(instance):
    assert isinstance(instance, cjsidl::transition)

@given(instance=cjsidl::transition_strategy)
def test_cjsidl::transition_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::transition_strategy)
def test_cjsidl::transition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::transition_strategy)
def test_cjsidl::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::transition_strategy)
def test_cjsidl::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::transition_strategy)
def test_cjsidl::transition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cjsidl::transition_strategy)
def test_cjsidl::transition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cjsidl::exit_strategy)
@settings(max_examples=50)
def test_cjsidl::exit_instantiation(instance):
    assert isinstance(instance, cjsidl::exit)

@given(instance=cjsidl::exit_strategy)
def test_cjsidl::exit_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::exit_strategy)
def test_cjsidl::exit_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::entry_strategy)
@settings(max_examples=50)
def test_cjsidl::entry_instantiation(instance):
    assert isinstance(instance, cjsidl::entry)

@given(instance=cjsidl::entry_strategy)
def test_cjsidl::entry_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::entry_strategy)
def test_cjsidl::entry_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::defaultState_strategy)
@settings(max_examples=50)
def test_cjsidl::defaultstate_instantiation(instance):
    assert isinstance(instance, cjsidl::defaultState)

@given(instance=cjsidl::defaultState_strategy)
def test_cjsidl::defaultstate_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::defaultState_strategy)
def test_cjsidl::defaultstate_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::state_strategy)
@settings(max_examples=50)
def test_cjsidl::state_instantiation(instance):
    assert isinstance(instance, cjsidl::state)

@given(instance=cjsidl::state_strategy)
def test_cjsidl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::state_strategy)
def test_cjsidl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::state_strategy)
def test_cjsidl::state_initial_type(instance):
    assert isinstance(instance.initial, str)


@given(instance=cjsidl::state_strategy)
def test_cjsidl::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=cjsidl::state_strategy)
def test_cjsidl::state_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::state_strategy)
def test_cjsidl::state_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::startState_strategy)
@settings(max_examples=50)
def test_cjsidl::startstate_instantiation(instance):
    assert isinstance(instance, cjsidl::startState)

@given(instance=cjsidl::startState_strategy)
def test_cjsidl::startstate_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::startState_strategy)
def test_cjsidl::startstate_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::constDef_strategy)
@settings(max_examples=50)
def test_cjsidl::constdef_instantiation(instance):
    assert isinstance(instance, cjsidl::constDef)

@given(instance=cjsidl::constDef_strategy)
def test_cjsidl::constdef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::constDef_strategy)
def test_cjsidl::constdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::constDef_strategy)
def test_cjsidl::constdef_constValue_type(instance):
    assert isinstance(instance.constValue, str)


@given(instance=cjsidl::constDef_strategy)
def test_cjsidl::constdef_constValue_setter(instance):
    original = instance.constValue
    instance.constValue = original
    assert instance.constValue == original

@given(instance=cjsidl::constDef_strategy)
def test_cjsidl::constdef_fieldUnits_type(instance):
    assert isinstance(instance.fieldUnits, str)


@given(instance=cjsidl::constDef_strategy)
def test_cjsidl::constdef_fieldUnits_setter(instance):
    original = instance.fieldUnits
    instance.fieldUnits = original
    assert instance.fieldUnits == original

@given(instance=cjsidl::constDef_strategy)
def test_cjsidl::constdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::constDef_strategy)
def test_cjsidl::constdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::declaredConstSetRef_strategy)
@settings(max_examples=50)
def test_cjsidl::declaredconstsetref_instantiation(instance):
    assert isinstance(instance, cjsidl::declaredConstSetRef)

@given(instance=cjsidl::declaredConstSetRef_strategy)
def test_cjsidl::declaredconstsetref_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::declaredConstSetRef_strategy)
def test_cjsidl::declaredconstsetref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::declaredConstSetRef_strategy)
def test_cjsidl::declaredconstsetref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::declaredConstSetRef_strategy)
def test_cjsidl::declaredconstsetref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::messageScopedRef_strategy)
@settings(max_examples=50)
def test_cjsidl::messagescopedref_instantiation(instance):
    assert isinstance(instance, cjsidl::messageScopedRef)

@given(instance=cjsidl::messageScopedRef_strategy)
def test_cjsidl::messagescopedref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::messageScopedRef_strategy)
def test_cjsidl::messagescopedref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::messageScopedRef_strategy)
def test_cjsidl::messagescopedref_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::messageScopedRef_strategy)
def test_cjsidl::messagescopedref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::messageRef_strategy)
@settings(max_examples=50)
def test_cjsidl::messageref_instantiation(instance):
    assert isinstance(instance, cjsidl::messageRef)

@given(instance=cjsidl::messageRef_strategy)
def test_cjsidl::messageref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::messageRef_strategy)
def test_cjsidl::messageref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::messageRef_strategy)
def test_cjsidl::messageref_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::messageRef_strategy)
def test_cjsidl::messageref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::messageDef_strategy)
@settings(max_examples=50)
def test_cjsidl::messagedef_instantiation(instance):
    assert isinstance(instance, cjsidl::messageDef)

@given(instance=cjsidl::messageDef_strategy)
def test_cjsidl::messagedef_messageID_type(instance):
    assert isinstance(instance.messageID, str)


@given(instance=cjsidl::messageDef_strategy)
def test_cjsidl::messagedef_messageID_setter(instance):
    original = instance.messageID
    instance.messageID = original
    assert instance.messageID == original

@given(instance=cjsidl::messageDef_strategy)
def test_cjsidl::messagedef_command_type(instance):
    assert isinstance(instance.command, str)


@given(instance=cjsidl::messageDef_strategy)
def test_cjsidl::messagedef_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original

@given(instance=cjsidl::messageDef_strategy)
def test_cjsidl::messagedef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::messageDef_strategy)
def test_cjsidl::messagedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::messages_strategy)
@settings(max_examples=50)
def test_cjsidl::messages_instantiation(instance):
    assert isinstance(instance, cjsidl::messages)

@given(instance=cjsidl::scopedTypeId_strategy)
@settings(max_examples=50)
def test_cjsidl::scopedtypeid_instantiation(instance):
    assert isinstance(instance, cjsidl::scopedTypeId)

@given(instance=cjsidl::scopedTypeId_strategy)
def test_cjsidl::scopedtypeid_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::scopedTypeId_strategy)
def test_cjsidl::scopedtypeid_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::scopedTypeId_strategy)
def test_cjsidl::scopedtypeid_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::scopedTypeId_strategy)
def test_cjsidl::scopedtypeid_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::scopedTypeId_strategy)
def test_cjsidl::scopedtypeid_scopedName_type(instance):
    assert isinstance(instance.scopedName, str)


@given(instance=cjsidl::scopedTypeId_strategy)
def test_cjsidl::scopedtypeid_scopedName_setter(instance):
    original = instance.scopedName
    instance.scopedName = original
    assert instance.scopedName == original

@given(instance=cjsidl::typeReference_strategy)
@settings(max_examples=50)
def test_cjsidl::typereference_instantiation(instance):
    assert isinstance(instance, cjsidl::typeReference)

@given(instance=cjsidl::typeReference_strategy)
def test_cjsidl::typereference_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::typeReference_strategy)
def test_cjsidl::typereference_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::typeReference_strategy)
def test_cjsidl::typereference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::typeReference_strategy)
def test_cjsidl::typereference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::typeReference_strategy)
def test_cjsidl::typereference_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::typeReference_strategy)
def test_cjsidl::typereference_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::typeDef_strategy)
@settings(max_examples=50)
def test_cjsidl::typedef_instantiation(instance):
    assert isinstance(instance, cjsidl::typeDef)

@given(instance=cjsidl::declaredTypeSetRef_strategy)
@settings(max_examples=50)
def test_cjsidl::declaredtypesetref_instantiation(instance):
    assert isinstance(instance, cjsidl::declaredTypeSetRef)

@given(instance=cjsidl::declaredTypeSetRef_strategy)
def test_cjsidl::declaredtypesetref_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::declaredTypeSetRef_strategy)
def test_cjsidl::declaredtypesetref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::declaredTypeSetRef_strategy)
def test_cjsidl::declaredtypesetref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::declaredTypeSetRef_strategy)
def test_cjsidl::declaredtypesetref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::serviceDef_strategy)
@settings(max_examples=50)
def test_cjsidl::servicedef_instantiation(instance):
    assert isinstance(instance, cjsidl::serviceDef)

@given(instance=cjsidl::serviceDef_strategy)
def test_cjsidl::servicedef_serviceName_type(instance):
    assert isinstance(instance.serviceName, str)


@given(instance=cjsidl::serviceDef_strategy)
def test_cjsidl::servicedef_serviceName_setter(instance):
    original = instance.serviceName
    instance.serviceName = original
    assert instance.serviceName == original

@given(instance=cjsidl::serviceDef_strategy)
def test_cjsidl::servicedef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::serviceDef_strategy)
def test_cjsidl::servicedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::serviceDef_strategy)
def test_cjsidl::servicedef_serviceVersion_type(instance):
    assert isinstance(instance.serviceVersion, str)


@given(instance=cjsidl::serviceDef_strategy)
def test_cjsidl::servicedef_serviceVersion_setter(instance):
    original = instance.serviceVersion
    instance.serviceVersion = original
    assert instance.serviceVersion == original

@given(instance=cjsidl::serviceDef_strategy)
def test_cjsidl::servicedef_assumpt_type(instance):
    assert isinstance(instance.assumpt, str)


@given(instance=cjsidl::serviceDef_strategy)
def test_cjsidl::servicedef_assumpt_setter(instance):
    original = instance.assumpt
    instance.assumpt = original
    assert instance.assumpt == original

@given(instance=cjsidl::EObject_strategy)
@settings(max_examples=50)
def test_cjsidl::eobject_instantiation(instance):
    assert isinstance(instance, cjsidl::EObject)

@given(instance=cjsidl::jaus_strategy)
@settings(max_examples=50)
def test_cjsidl::jaus_instantiation(instance):
    assert isinstance(instance, cjsidl::jaus)

@given(instance=cjsidl::refAttr_strategy)
@settings(max_examples=50)
def test_cjsidl::refattr_instantiation(instance):
    assert isinstance(instance, cjsidl::refAttr)

@given(instance=cjsidl::refAttr_strategy)
def test_cjsidl::refattr_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::refAttr_strategy)
def test_cjsidl::refattr_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::refAttr_strategy)
def test_cjsidl::refattr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::refAttr_strategy)
def test_cjsidl::refattr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::protocolBehavior_strategy)
@settings(max_examples=50)
def test_cjsidl::protocolbehavior_instantiation(instance):
    assert isinstance(instance, cjsidl::protocolBehavior)

@given(instance=cjsidl::protocolBehavior_strategy)
def test_cjsidl::protocolbehavior_stateless_type(instance):
    assert isinstance(instance.stateless, str)


@given(instance=cjsidl::protocolBehavior_strategy)
def test_cjsidl::protocolbehavior_stateless_setter(instance):
    original = instance.stateless
    instance.stateless = original
    assert instance.stateless == original

@given(instance=cjsidl::protocolBehavior_strategy)
def test_cjsidl::protocolbehavior_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::protocolBehavior_strategy)
def test_cjsidl::protocolbehavior_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::internalEventSet_strategy)
@settings(max_examples=50)
def test_cjsidl::internaleventset_instantiation(instance):
    assert isinstance(instance, cjsidl::internalEventSet)

@given(instance=cjsidl::internalEventSet_strategy)
def test_cjsidl::internaleventset_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::internalEventSet_strategy)
def test_cjsidl::internaleventset_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::messageSet_strategy)
@settings(max_examples=50)
def test_cjsidl::messageset_instantiation(instance):
    assert isinstance(instance, cjsidl::messageSet)

@given(instance=cjsidl::messageSet_strategy)
def test_cjsidl::messageset_outputComment_type(instance):
    assert isinstance(instance.outputComment, str)


@given(instance=cjsidl::messageSet_strategy)
def test_cjsidl::messageset_outputComment_setter(instance):
    original = instance.outputComment
    instance.outputComment = original
    assert instance.outputComment == original

@given(instance=cjsidl::messageSet_strategy)
def test_cjsidl::messageset_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::messageSet_strategy)
def test_cjsidl::messageset_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::messageSet_strategy)
def test_cjsidl::messageset_inputComment_type(instance):
    assert isinstance(instance.inputComment, str)


@given(instance=cjsidl::messageSet_strategy)
def test_cjsidl::messageset_inputComment_setter(instance):
    original = instance.inputComment
    instance.inputComment = original
    assert instance.inputComment == original

@given(instance=cjsidl::declaredTypeSet_strategy)
@settings(max_examples=50)
def test_cjsidl::declaredtypeset_instantiation(instance):
    assert isinstance(instance, cjsidl::declaredTypeSet)

@given(instance=cjsidl::declaredTypeSet_strategy)
def test_cjsidl::declaredtypeset_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=cjsidl::declaredTypeSet_strategy)
def test_cjsidl::declaredtypeset_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=cjsidl::declaredTypeSet_strategy)
def test_cjsidl::declaredtypeset_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=cjsidl::declaredTypeSet_strategy)
def test_cjsidl::declaredtypeset_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=cjsidl::declaredTypeSet_strategy)
def test_cjsidl::declaredtypeset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::declaredTypeSet_strategy)
def test_cjsidl::declaredtypeset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::declaredConstSet_strategy)
@settings(max_examples=50)
def test_cjsidl::declaredconstset_instantiation(instance):
    assert isinstance(instance, cjsidl::declaredConstSet)

@given(instance=cjsidl::declaredConstSet_strategy)
def test_cjsidl::declaredconstset_constName_type(instance):
    assert isinstance(instance.constName, str)


@given(instance=cjsidl::declaredConstSet_strategy)
def test_cjsidl::declaredconstset_constName_setter(instance):
    original = instance.constName
    instance.constName = original
    assert instance.constName == original

@given(instance=cjsidl::declaredConstSet_strategy)
def test_cjsidl::declaredconstset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::declaredConstSet_strategy)
def test_cjsidl::declaredconstset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::declaredConstSet_strategy)
def test_cjsidl::declaredconstset_constSetVersion_type(instance):
    assert isinstance(instance.constSetVersion, str)


@given(instance=cjsidl::declaredConstSet_strategy)
def test_cjsidl::declaredconstset_constSetVersion_setter(instance):
    original = instance.constSetVersion
    instance.constSetVersion = original
    assert instance.constSetVersion == original

@given(instance=cjsidl::references_strategy)
@settings(max_examples=50)
def test_cjsidl::references_instantiation(instance):
    assert isinstance(instance, cjsidl::references)

@given(instance=cjsidl::description_strategy)
@settings(max_examples=50)
def test_cjsidl::description_instantiation(instance):
    assert isinstance(instance, cjsidl::description)

@given(instance=cjsidl::description_strategy)
def test_cjsidl::description_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=cjsidl::description_strategy)
def test_cjsidl::description_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=cjsidl::taggedItemDef_strategy)
@settings(max_examples=50)
def test_cjsidl::taggeditemdef_instantiation(instance):
    assert isinstance(instance, cjsidl::taggedItemDef)

@given(instance=cjsidl::valueSpec_strategy)
@settings(max_examples=50)
def test_cjsidl::valuespec_instantiation(instance):
    assert isinstance(instance, cjsidl::valueSpec)

@given(instance=cjsidl::valueSpec_strategy)
def test_cjsidl::valuespec_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::valueSpec_strategy)
def test_cjsidl::valuespec_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::valueSpec_strategy)
def test_cjsidl::valuespec_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cjsidl::valueSpec_strategy)
def test_cjsidl::valuespec_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cjsidl::valueSpec_strategy)
def test_cjsidl::valuespec_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::valueSpec_strategy)
def test_cjsidl::valuespec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=containerDef_strategy)
@settings(max_examples=50)
def test_containerdef_instantiation(instance):
    assert isinstance(instance, containerDef)

@given(instance=cjsidl::formatEnumDef_strategy)
@settings(max_examples=50)
def test_cjsidl::formatenumdef_instantiation(instance):
    assert isinstance(instance, cjsidl::formatEnumDef)

@given(instance=cjsidl::formatEnumDef_strategy)
def test_cjsidl::formatenumdef_fieldFormat_type(instance):
    assert isinstance(instance.fieldFormat, str)


@given(instance=cjsidl::formatEnumDef_strategy)
def test_cjsidl::formatenumdef_fieldFormat_setter(instance):
    original = instance.fieldFormat
    instance.fieldFormat = original
    assert instance.fieldFormat == original

@given(instance=cjsidl::formatEnumDef_strategy)
def test_cjsidl::formatenumdef_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=cjsidl::formatEnumDef_strategy)
def test_cjsidl::formatenumdef_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=cjsidl::formatEnumDef_strategy)
def test_cjsidl::formatenumdef_fieldFormatStr_type(instance):
    assert isinstance(instance.fieldFormatStr, str)


@given(instance=cjsidl::formatEnumDef_strategy)
def test_cjsidl::formatenumdef_fieldFormatStr_setter(instance):
    original = instance.fieldFormatStr
    instance.fieldFormatStr = original
    assert instance.fieldFormatStr == original

@given(instance=cjsidl::valueRange_strategy)
@settings(max_examples=50)
def test_cjsidl::valuerange_instantiation(instance):
    assert isinstance(instance, cjsidl::valueRange)

@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_upperLimit_type_type(instance):
    assert isinstance(instance.upperLimit_type, str)


@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_upperLimit_type_setter(instance):
    original = instance.upperLimit_type
    instance.upperLimit_type = original
    assert instance.upperLimit_type == original

@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_lowerLim_type(instance):
    assert isinstance(instance.lowerLim, str)


@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_lowerLim_setter(instance):
    original = instance.lowerLim
    instance.lowerLim = original
    assert instance.lowerLim == original

@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_upperLim_type(instance):
    assert isinstance(instance.upperLim, str)


@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original

@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_lowerLimit_type_type(instance):
    assert isinstance(instance.lowerLimit_type, str)


@given(instance=cjsidl::valueRange_strategy)
def test_cjsidl::valuerange_lowerLimit_type_setter(instance):
    original = instance.lowerLimit_type
    instance.lowerLimit_type = original
    assert instance.lowerLimit_type == original

@given(instance=cjsidl::scaledRangeDef_strategy)
@settings(max_examples=50)
def test_cjsidl::scaledrangedef_instantiation(instance):
    assert isinstance(instance, cjsidl::scaledRangeDef)

@given(instance=cjsidl::scaledRangeDef_strategy)
def test_cjsidl::scaledrangedef_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=cjsidl::scaledRangeDef_strategy)
def test_cjsidl::scaledrangedef_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=cjsidl::scaledRangeDef_strategy)
def test_cjsidl::scaledrangedef_upperLim_type(instance):
    assert isinstance(instance.upperLim, str)


@given(instance=cjsidl::scaledRangeDef_strategy)
def test_cjsidl::scaledrangedef_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original

@given(instance=cjsidl::scaledRangeDef_strategy)
def test_cjsidl::scaledrangedef_interp_type(instance):
    assert isinstance(instance.interp, str)


@given(instance=cjsidl::scaledRangeDef_strategy)
def test_cjsidl::scaledrangedef_interp_setter(instance):
    original = instance.interp
    instance.interp = original
    assert instance.interp == original

@given(instance=cjsidl::scaledRangeDef_strategy)
def test_cjsidl::scaledrangedef_lowerLim_type(instance):
    assert isinstance(instance.lowerLim, str)


@given(instance=cjsidl::scaledRangeDef_strategy)
def test_cjsidl::scaledrangedef_lowerLim_setter(instance):
    original = instance.lowerLim
    instance.lowerLim = original
    assert instance.lowerLim == original

@given(instance=cjsidl::subField_strategy)
@settings(max_examples=50)
def test_cjsidl::subfield_instantiation(instance):
    assert isinstance(instance, cjsidl::subField)

@given(instance=cjsidl::subField_strategy)
def test_cjsidl::subfield_toIndex_type(instance):
    assert isinstance(instance.toIndex, str)


@given(instance=cjsidl::subField_strategy)
def test_cjsidl::subfield_toIndex_setter(instance):
    original = instance.toIndex
    instance.toIndex = original
    assert instance.toIndex == original

@given(instance=cjsidl::subField_strategy)
def test_cjsidl::subfield_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::subField_strategy)
def test_cjsidl::subfield_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::subField_strategy)
def test_cjsidl::subfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::subField_strategy)
def test_cjsidl::subfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::subField_strategy)
def test_cjsidl::subfield_fromIndex_type(instance):
    assert isinstance(instance.fromIndex, str)


@given(instance=cjsidl::subField_strategy)
def test_cjsidl::subfield_fromIndex_setter(instance):
    original = instance.fromIndex
    instance.fromIndex = original
    assert instance.fromIndex == original

@given(instance=cjsidl::taggedUnitsEnum_strategy)
@settings(max_examples=50)
def test_cjsidl::taggedunitsenum_instantiation(instance):
    assert isinstance(instance, cjsidl::taggedUnitsEnum)

@given(instance=cjsidl::taggedUnitsEnum_strategy)
def test_cjsidl::taggedunitsenum_fieldUnit_type(instance):
    assert isinstance(instance.fieldUnit, str)


@given(instance=cjsidl::taggedUnitsEnum_strategy)
def test_cjsidl::taggedunitsenum_fieldUnit_setter(instance):
    original = instance.fieldUnit
    instance.fieldUnit = original
    assert instance.fieldUnit == original

@given(instance=cjsidl::taggedUnitsEnum_strategy)
def test_cjsidl::taggedunitsenum_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::taggedUnitsEnum_strategy)
def test_cjsidl::taggedunitsenum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::taggedUnitsEnum_strategy)
def test_cjsidl::taggedunitsenum_const_tag_type(instance):
    assert isinstance(instance.const_tag, str)


@given(instance=cjsidl::taggedUnitsEnum_strategy)
def test_cjsidl::taggedunitsenum_const_tag_setter(instance):
    original = instance.const_tag
    instance.const_tag = original
    assert instance.const_tag == original

@given(instance=cjsidl::valueSetDef_strategy)
@settings(max_examples=50)
def test_cjsidl::valuesetdef_instantiation(instance):
    assert isinstance(instance, cjsidl::valueSetDef)

@given(instance=cjsidl::valueSetDef_strategy)
def test_cjsidl::valuesetdef_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=cjsidl::valueSetDef_strategy)
def test_cjsidl::valuesetdef_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=cjsidl::declaredEventDef_strategy)
@settings(max_examples=50)
def test_cjsidl::declaredeventdef_instantiation(instance):
    assert isinstance(instance, cjsidl::declaredEventDef)

@given(instance=cjsidl::declaredEventDef_strategy)
def test_cjsidl::declaredeventdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::declaredEventDef_strategy)
def test_cjsidl::declaredeventdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::declaredEventDef_strategy)
def test_cjsidl::declaredeventdef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::declaredEventDef_strategy)
def test_cjsidl::declaredeventdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::scopedType_strategy)
@settings(max_examples=50)
def test_cjsidl::scopedtype_instantiation(instance):
    assert isinstance(instance, cjsidl::scopedType)

@given(instance=cjsidl::scopedConstId_strategy)
@settings(max_examples=50)
def test_cjsidl::scopedconstid_instantiation(instance):
    assert isinstance(instance, cjsidl::scopedConstId)

@given(instance=cjsidl::constReference_strategy)
@settings(max_examples=50)
def test_cjsidl::constreference_instantiation(instance):
    assert isinstance(instance, cjsidl::constReference)

@given(instance=cjsidl::constReference_strategy)
def test_cjsidl::constreference_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::constReference_strategy)
def test_cjsidl::constreference_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::footerScopedRef_strategy)
@settings(max_examples=50)
def test_cjsidl::footerscopedref_instantiation(instance):
    assert isinstance(instance, cjsidl::footerScopedRef)

@given(instance=cjsidl::footerRef_strategy)
@settings(max_examples=50)
def test_cjsidl::footerref_instantiation(instance):
    assert isinstance(instance, cjsidl::footerRef)

@given(instance=cjsidl::footerRef_strategy)
def test_cjsidl::footerref_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::footerRef_strategy)
def test_cjsidl::footerref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::footerRef_strategy)
def test_cjsidl::footerref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::footerRef_strategy)
def test_cjsidl::footerref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::bodyScopedRef_strategy)
@settings(max_examples=50)
def test_cjsidl::bodyscopedref_instantiation(instance):
    assert isinstance(instance, cjsidl::bodyScopedRef)

@given(instance=cjsidl::bodyRef_strategy)
@settings(max_examples=50)
def test_cjsidl::bodyref_instantiation(instance):
    assert isinstance(instance, cjsidl::bodyRef)

@given(instance=cjsidl::bodyRef_strategy)
def test_cjsidl::bodyref_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::bodyRef_strategy)
def test_cjsidl::bodyref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::bodyRef_strategy)
def test_cjsidl::bodyref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::bodyRef_strategy)
def test_cjsidl::bodyref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::headerScopedRef_strategy)
@settings(max_examples=50)
def test_cjsidl::headerscopedref_instantiation(instance):
    assert isinstance(instance, cjsidl::headerScopedRef)

@given(instance=cjsidl::headerRef_strategy)
@settings(max_examples=50)
def test_cjsidl::headerref_instantiation(instance):
    assert isinstance(instance, cjsidl::headerRef)

@given(instance=cjsidl::headerRef_strategy)
def test_cjsidl::headerref_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::headerRef_strategy)
def test_cjsidl::headerref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::headerRef_strategy)
def test_cjsidl::headerref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::headerRef_strategy)
def test_cjsidl::headerref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::containerRef_strategy)
@settings(max_examples=50)
def test_cjsidl::containerref_instantiation(instance):
    assert isinstance(instance, cjsidl::containerRef)

@given(instance=cjsidl::containerRef_strategy)
def test_cjsidl::containerref_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::containerRef_strategy)
def test_cjsidl::containerref_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::containerRef_strategy)
def test_cjsidl::containerref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::containerRef_strategy)
def test_cjsidl::containerref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::containerRef_strategy)
def test_cjsidl::containerref_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::containerRef_strategy)
def test_cjsidl::containerref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::containerDef_strategy)
@settings(max_examples=50)
def test_cjsidl::containerdef_instantiation(instance):
    assert isinstance(instance, cjsidl::containerDef)

@given(instance=cjsidl::containerDef_strategy)
def test_cjsidl::containerdef_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::containerDef_strategy)
def test_cjsidl::containerdef_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::containerDef_strategy)
def test_cjsidl::containerdef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::containerDef_strategy)
def test_cjsidl::containerdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::containerDef_strategy)
def test_cjsidl::containerdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::containerDef_strategy)
def test_cjsidl::containerdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::footerDef_strategy)
@settings(max_examples=50)
def test_cjsidl::footerdef_instantiation(instance):
    assert isinstance(instance, cjsidl::footerDef)

@given(instance=cjsidl::footerDef_strategy)
def test_cjsidl::footerdef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::footerDef_strategy)
def test_cjsidl::footerdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::footerDef_strategy)
def test_cjsidl::footerdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::footerDef_strategy)
def test_cjsidl::footerdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::bodyDef_strategy)
@settings(max_examples=50)
def test_cjsidl::bodydef_instantiation(instance):
    assert isinstance(instance, cjsidl::bodyDef)

@given(instance=cjsidl::bodyDef_strategy)
def test_cjsidl::bodydef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::bodyDef_strategy)
def test_cjsidl::bodydef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::bodyDef_strategy)
def test_cjsidl::bodydef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::bodyDef_strategy)
def test_cjsidl::bodydef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::headerDef_strategy)
@settings(max_examples=50)
def test_cjsidl::headerdef_instantiation(instance):
    assert isinstance(instance, cjsidl::headerDef)

@given(instance=cjsidl::headerDef_strategy)
def test_cjsidl::headerdef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::headerDef_strategy)
def test_cjsidl::headerdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::headerDef_strategy)
def test_cjsidl::headerdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::headerDef_strategy)
def test_cjsidl::headerdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::varFormatField_strategy)
@settings(max_examples=50)
def test_cjsidl::varformatfield_instantiation(instance):
    assert isinstance(instance, cjsidl::varFormatField)

@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_units_type(instance):
    assert isinstance(instance.units, str)


@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original

@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_countComment_type(instance):
    assert isinstance(instance.countComment, str)


@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_countComment_setter(instance):
    original = instance.countComment
    instance.countComment = original
    assert instance.countComment == original

@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::varFormatField_strategy)
def test_cjsidl::varformatfield_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::varLenField_strategy)
@settings(max_examples=50)
def test_cjsidl::varlenfield_instantiation(instance):
    assert isinstance(instance, cjsidl::varLenField)

@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_countComment_type(instance):
    assert isinstance(instance.countComment, str)


@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_countComment_setter(instance):
    original = instance.countComment
    instance.countComment = original
    assert instance.countComment == original

@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_upperLim_type(instance):
    assert isinstance(instance.upperLim, str)


@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original

@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_fieldFormat_type(instance):
    assert isinstance(instance.fieldFormat, str)


@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_fieldFormat_setter(instance):
    original = instance.fieldFormat
    instance.fieldFormat = original
    assert instance.fieldFormat == original

@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_lowerLim_type(instance):
    assert isinstance(instance.lowerLim, str)


@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_lowerLim_setter(instance):
    original = instance.lowerLim
    instance.lowerLim = original
    assert instance.lowerLim == original

@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::varLenField_strategy)
def test_cjsidl::varlenfield_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::varLenString_strategy)
@settings(max_examples=50)
def test_cjsidl::varlenstring_instantiation(instance):
    assert isinstance(instance, cjsidl::varLenString)

@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_upperLim_type(instance):
    assert isinstance(instance.upperLim, str)


@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original

@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_lowerLim_type(instance):
    assert isinstance(instance.lowerLim, str)


@given(instance=cjsidl::varLenString_strategy)
def test_cjsidl::varlenstring_lowerLim_setter(instance):
    original = instance.lowerLim
    instance.lowerLim = original
    assert instance.lowerLim == original

@given(instance=cjsidl::fixedLenString_strategy)
@settings(max_examples=50)
def test_cjsidl::fixedlenstring_instantiation(instance):
    assert isinstance(instance, cjsidl::fixedLenString)

@given(instance=cjsidl::fixedLenString_strategy)
def test_cjsidl::fixedlenstring_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::fixedLenString_strategy)
def test_cjsidl::fixedlenstring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::fixedLenString_strategy)
def test_cjsidl::fixedlenstring_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::fixedLenString_strategy)
def test_cjsidl::fixedlenstring_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::fixedLenString_strategy)
def test_cjsidl::fixedlenstring_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::fixedLenString_strategy)
def test_cjsidl::fixedlenstring_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::fixedLenString_strategy)
def test_cjsidl::fixedlenstring_upperLim_type(instance):
    assert isinstance(instance.upperLim, str)


@given(instance=cjsidl::fixedLenString_strategy)
def test_cjsidl::fixedlenstring_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original

@given(instance=cjsidl::bitfieldDef_strategy)
@settings(max_examples=50)
def test_cjsidl::bitfielddef_instantiation(instance):
    assert isinstance(instance, cjsidl::bitfieldDef)

@given(instance=cjsidl::bitfieldDef_strategy)
def test_cjsidl::bitfielddef_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cjsidl::bitfieldDef_strategy)
def test_cjsidl::bitfielddef_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cjsidl::bitfieldDef_strategy)
def test_cjsidl::bitfielddef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::bitfieldDef_strategy)
def test_cjsidl::bitfielddef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::bitfieldDef_strategy)
def test_cjsidl::bitfielddef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::bitfieldDef_strategy)
def test_cjsidl::bitfielddef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::bitfieldDef_strategy)
def test_cjsidl::bitfielddef_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::bitfieldDef_strategy)
def test_cjsidl::bitfielddef_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::action_strategy)
@settings(max_examples=50)
def test_cjsidl::action_instantiation(instance):
    assert isinstance(instance, cjsidl::action)

@given(instance=cjsidl::action_strategy)
def test_cjsidl::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::action_strategy)
def test_cjsidl::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::action_strategy)
def test_cjsidl::action_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::action_strategy)
def test_cjsidl::action_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::varField_strategy)
@settings(max_examples=50)
def test_cjsidl::varfield_instantiation(instance):
    assert isinstance(instance, cjsidl::varField)

@given(instance=cjsidl::varField_strategy)
def test_cjsidl::varfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::varField_strategy)
def test_cjsidl::varfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::varField_strategy)
def test_cjsidl::varfield_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::varField_strategy)
def test_cjsidl::varfield_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::varField_strategy)
def test_cjsidl::varfield_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::varField_strategy)
def test_cjsidl::varfield_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::fixedFieldDef_strategy)
@settings(max_examples=50)
def test_cjsidl::fixedfielddef_instantiation(instance):
    assert isinstance(instance, cjsidl::fixedFieldDef)

@given(instance=cjsidl::fixedFieldDef_strategy)
def test_cjsidl::fixedfielddef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::fixedFieldDef_strategy)
def test_cjsidl::fixedfielddef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::fixedFieldDef_strategy)
def test_cjsidl::fixedfielddef_fieldUnit_type(instance):
    assert isinstance(instance.fieldUnit, str)


@given(instance=cjsidl::fixedFieldDef_strategy)
def test_cjsidl::fixedfielddef_fieldUnit_setter(instance):
    original = instance.fieldUnit
    instance.fieldUnit = original
    assert instance.fieldUnit == original

@given(instance=cjsidl::fixedFieldDef_strategy)
def test_cjsidl::fixedfielddef_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::fixedFieldDef_strategy)
def test_cjsidl::fixedfielddef_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::fixedFieldDef_strategy)
def test_cjsidl::fixedfielddef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::fixedFieldDef_strategy)
def test_cjsidl::fixedfielddef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::sequenceDef_strategy)
@settings(max_examples=50)
def test_cjsidl::sequencedef_instantiation(instance):
    assert isinstance(instance, cjsidl::sequenceDef)

@given(instance=cjsidl::variantDef_strategy)
@settings(max_examples=50)
def test_cjsidl::variantdef_instantiation(instance):
    assert isinstance(instance, cjsidl::variantDef)

@given(instance=cjsidl::variantDef_strategy)
def test_cjsidl::variantdef_minCount_type(instance):
    assert isinstance(instance.minCount, str)


@given(instance=cjsidl::variantDef_strategy)
def test_cjsidl::variantdef_minCount_setter(instance):
    original = instance.minCount
    instance.minCount = original
    assert instance.minCount == original

@given(instance=cjsidl::variantDef_strategy)
def test_cjsidl::variantdef_maxCount_type(instance):
    assert isinstance(instance.maxCount, str)


@given(instance=cjsidl::variantDef_strategy)
def test_cjsidl::variantdef_maxCount_setter(instance):
    original = instance.maxCount
    instance.maxCount = original
    assert instance.maxCount == original

@given(instance=cjsidl::variantDef_strategy)
def test_cjsidl::variantdef_vtagComment_type(instance):
    assert isinstance(instance.vtagComment, str)


@given(instance=cjsidl::variantDef_strategy)
def test_cjsidl::variantdef_vtagComment_setter(instance):
    original = instance.vtagComment
    instance.vtagComment = original
    assert instance.vtagComment == original

@given(instance=cjsidl::listDef_strategy)
@settings(max_examples=50)
def test_cjsidl::listdef_instantiation(instance):
    assert isinstance(instance, cjsidl::listDef)

@given(instance=cjsidl::listDef_strategy)
def test_cjsidl::listdef_minCount_type(instance):
    assert isinstance(instance.minCount, str)


@given(instance=cjsidl::listDef_strategy)
def test_cjsidl::listdef_minCount_setter(instance):
    original = instance.minCount
    instance.minCount = original
    assert instance.minCount == original

@given(instance=cjsidl::listDef_strategy)
def test_cjsidl::listdef_countComment_type(instance):
    assert isinstance(instance.countComment, str)


@given(instance=cjsidl::listDef_strategy)
def test_cjsidl::listdef_countComment_setter(instance):
    original = instance.countComment
    instance.countComment = original
    assert instance.countComment == original

@given(instance=cjsidl::listDef_strategy)
def test_cjsidl::listdef_maxCount_type(instance):
    assert isinstance(instance.maxCount, str)


@given(instance=cjsidl::listDef_strategy)
def test_cjsidl::listdef_maxCount_setter(instance):
    original = instance.maxCount
    instance.maxCount = original
    assert instance.maxCount == original

@given(instance=cjsidl::recordDef_strategy)
@settings(max_examples=50)
def test_cjsidl::recorddef_instantiation(instance):
    assert isinstance(instance, cjsidl::recordDef)

@given(instance=cjsidl::arrayDef_strategy)
@settings(max_examples=50)
def test_cjsidl::arraydef_instantiation(instance):
    assert isinstance(instance, cjsidl::arrayDef)

@given(instance=cjsidl::arrayDef_strategy)
def test_cjsidl::arraydef_arraySize_type(instance):
    assert isinstance(instance.arraySize, str)


@given(instance=cjsidl::arrayDef_strategy)
def test_cjsidl::arraydef_arraySize_setter(instance):
    original = instance.arraySize
    instance.arraySize = original
    assert instance.arraySize == original

@given(instance=cjsidl::arrayDef_strategy)
def test_cjsidl::arraydef_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::arrayDef_strategy)
def test_cjsidl::arraydef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::arrayDef_strategy)
def test_cjsidl::arraydef_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=cjsidl::arrayDef_strategy)
def test_cjsidl::arraydef_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl::arrayDef_strategy)
def test_cjsidl::arraydef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::arrayDef_strategy)
def test_cjsidl::arraydef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::simpleNumericType_strategy)
@settings(max_examples=50)
def test_cjsidl::simplenumerictype_instantiation(instance):
    assert isinstance(instance, cjsidl::simpleNumericType)

@given(instance=cjsidl::simpleNumericType_strategy)
def test_cjsidl::simplenumerictype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cjsidl::simpleNumericType_strategy)
def test_cjsidl::simplenumerictype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cjsidl::simpleTransition_strategy)
@settings(max_examples=50)
def test_cjsidl::simpletransition_instantiation(instance):
    assert isinstance(instance, cjsidl::simpleTransition)

@given(instance=cjsidl::simpleTransition_strategy)
def test_cjsidl::simpletransition_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::simpleTransition_strategy)
def test_cjsidl::simpletransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::internalTransition_strategy)
@settings(max_examples=50)
def test_cjsidl::internaltransition_instantiation(instance):
    assert isinstance(instance, cjsidl::internalTransition)

@given(instance=cjsidl::internalTransition_strategy)
def test_cjsidl::internaltransition_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::internalTransition_strategy)
def test_cjsidl::internaltransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::guardAction_strategy)
@settings(max_examples=50)
def test_cjsidl::guardaction_instantiation(instance):
    assert isinstance(instance, cjsidl::guardAction)

@given(instance=cjsidl::guardAction_strategy)
def test_cjsidl::guardaction_not__type(instance):
    assert isinstance(instance.not_, str)


@given(instance=cjsidl::guardAction_strategy)
def test_cjsidl::guardaction_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=cjsidl::guardAction_strategy)
def test_cjsidl::guardaction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::guardAction_strategy)
def test_cjsidl::guardaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::guardParam_strategy)
@settings(max_examples=50)
def test_cjsidl::guardparam_instantiation(instance):
    assert isinstance(instance, cjsidl::guardParam)

@given(instance=cjsidl::guardParam_strategy)
def test_cjsidl::guardparam_guardConst_type(instance):
    assert isinstance(instance.guardConst, str)


@given(instance=cjsidl::guardParam_strategy)
def test_cjsidl::guardparam_guardConst_setter(instance):
    original = instance.guardConst
    instance.guardConst = original
    assert instance.guardConst == original

@given(instance=cjsidl::popTransition_strategy)
@settings(max_examples=50)
def test_cjsidl::poptransition_instantiation(instance):
    assert isinstance(instance, cjsidl::popTransition)

@given(instance=cjsidl::popTransition_strategy)
def test_cjsidl::poptransition_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::popTransition_strategy)
def test_cjsidl::poptransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::pushTransition_strategy)
@settings(max_examples=50)
def test_cjsidl::pushtransition_instantiation(instance):
    assert isinstance(instance, cjsidl::pushTransition)

@given(instance=cjsidl::pushTransition_strategy)
def test_cjsidl::pushtransition_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::pushTransition_strategy)
def test_cjsidl::pushtransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::nextState_strategy)
@settings(max_examples=50)
def test_cjsidl::nextstate_instantiation(instance):
    assert isinstance(instance, cjsidl::nextState)

@given(instance=cjsidl::nextState_strategy)
def test_cjsidl::nextstate_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::nextState_strategy)
def test_cjsidl::nextstate_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::sendActionList_strategy)
@settings(max_examples=50)
def test_cjsidl::sendactionlist_instantiation(instance):
    assert isinstance(instance, cjsidl::sendActionList)

@given(instance=cjsidl::actionList_strategy)
@settings(max_examples=50)
def test_cjsidl::actionlist_instantiation(instance):
    assert isinstance(instance, cjsidl::actionList)

@given(instance=cjsidl::defaultTransition_strategy)
@settings(max_examples=50)
def test_cjsidl::defaulttransition_instantiation(instance):
    assert isinstance(instance, cjsidl::defaultTransition)

@given(instance=cjsidl::defaultTransition_strategy)
def test_cjsidl::defaulttransition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cjsidl::defaultTransition_strategy)
def test_cjsidl::defaulttransition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cjsidl::defaultTransition_strategy)
def test_cjsidl::defaulttransition_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::defaultTransition_strategy)
def test_cjsidl::defaulttransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::guard_strategy)
@settings(max_examples=50)
def test_cjsidl::guard_instantiation(instance):
    assert isinstance(instance, cjsidl::guard)

@given(instance=cjsidl::guard_strategy)
def test_cjsidl::guard_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::guard_strategy)
def test_cjsidl::guard_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::guard_strategy)
def test_cjsidl::guard_logicalOperator_type(instance):
    assert isinstance(instance.logicalOperator, str)


@given(instance=cjsidl::guard_strategy)
def test_cjsidl::guard_logicalOperator_setter(instance):
    original = instance.logicalOperator
    instance.logicalOperator = original
    assert instance.logicalOperator == original

@given(instance=cjsidl::guard_strategy)
def test_cjsidl::guard_equiv_type(instance):
    assert isinstance(instance.equiv, str)


@given(instance=cjsidl::guard_strategy)
def test_cjsidl::guard_equiv_setter(instance):
    original = instance.equiv
    instance.equiv = original
    assert instance.equiv == original

@given(instance=cjsidl::scopedEventType_strategy)
@settings(max_examples=50)
def test_cjsidl::scopedeventtype_instantiation(instance):
    assert isinstance(instance, cjsidl::scopedEventType)

@given(instance=cjsidl::transParam_strategy)
@settings(max_examples=50)
def test_cjsidl::transparam_instantiation(instance):
    assert isinstance(instance, cjsidl::transParam)

@given(instance=cjsidl::transParam_strategy)
def test_cjsidl::transparam_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cjsidl::transParam_strategy)
def test_cjsidl::transparam_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl::transParam_strategy)
def test_cjsidl::transparam_unsignedType_type(instance):
    assert isinstance(instance.unsignedType, str)


@given(instance=cjsidl::transParam_strategy)
def test_cjsidl::transparam_unsignedType_setter(instance):
    original = instance.unsignedType
    instance.unsignedType = original
    assert instance.unsignedType == original

@given(instance=cjsidl::transParam_strategy)
def test_cjsidl::transparam_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cjsidl::transParam_strategy)
def test_cjsidl::transparam_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl::transParams_strategy)
@settings(max_examples=50)
def test_cjsidl::transparams_instantiation(instance):
    assert isinstance(instance, cjsidl::transParams)
