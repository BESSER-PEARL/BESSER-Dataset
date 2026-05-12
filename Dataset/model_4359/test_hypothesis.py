import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TrgResponse,
    jointPackage_CPL2SPL_TrgErrorResponse,
    jointPackage_CPL2SPL_TrgSuccessResponse,
    TrgVariablePlace,
    jointPackage_CPL2SPL_TrgPropertyCallPlace,
    jointPackage_CPL2SPL_TrgVariable,
    TrgSelectMember,
    jointPackage_CPL2SPL_TrgSelectCase,
    TrgMessageField,
    jointPackage_CPL2SPL_TrgHeadedMessageField,
    jointPackage_CPL2SPL_TrgReasonMessageField,
    TrgFunctionCall,
    TrgSelectDefault,
    TrgSelectCase,
    jointPackage_CPL2SPL_TrgSelectDefault,
    TrgConstant,
    jointPackage_CPL2SPL_TrgSequenceConstant,
    jointPackage_CPL2SPL_TrgStringConstant,
    jointPackage_CPL2SPL_TrgResponseConstant,
    jointPackage_CPL2SPL_TrgIntegerConstant,
    jointPackage_CPL2SPL_TrgURIConstant,
    jointPackage_CPL2SPL_TrgBooleanConstant,
    TrgNamedBranch,
    TrgWhenHeader,
    TrgVariable,
    TrgFunctionDeclaration,
    jointPackage_CPL2SPL_TrgLocalFunctionDeclaration,
    jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration,
    TrgPlace,
    jointPackage_CPL2SPL_TrgSIPHeaderPlace,
    jointPackage_CPL2SPL_TrgVariablePlace,
    TrgExpression,
    jointPackage_CPL2SPL_TrgPlace,
    jointPackage_CPL2SPL_TrgBlockExp,
    jointPackage_CPL2SPL_TrgOperatorExp,
    jointPackage_CPL2SPL_TrgPopExp,
    jointPackage_CPL2SPL_TrgBODYExp,
    jointPackage_CPL2SPL_TrgReasonExp,
    jointPackage_CPL2SPL_TrgForwardExp,
    jointPackage_CPL2SPL_TrgWithExp,
    jointPackage_CPL2SPL_TrgFunctionCallExp,
    jointPackage_CPL2SPL_TrgConstantExp,
    jointPackage_CPL2SPL_TrgRequestURIExp,
    TrgArgument,
    TrgMethodName,
    TrgMethod,
    jointPackage_CPL2SPL_TrgControlMethodName,
    jointPackage_CPL2SPL_TrgSIPMethodName,
    TrgVariableDeclaration,
    jointPackage_CPL2SPL_TrgWhenHeader,
    jointPackage_CPL2SPL_TrgArgument,
    TrgBranch,
    jointPackage_CPL2SPL_TrgNamedBranch,
    jointPackage_CPL2SPL_TrgDefaultBranch,
    TrgStatement,
    jointPackage_CPL2SPL_TrgReturnStat,
    jointPackage_CPL2SPL_TrgSelectStat,
    jointPackage_CPL2SPL_TrgFunctionCallStat,
    jointPackage_CPL2SPL_TrgDeclarationStat,
    jointPackage_CPL2SPL_TrgPushStat,
    jointPackage_CPL2SPL_TrgBreakStat,
    jointPackage_CPL2SPL_TrgWhenStat,
    jointPackage_CPL2SPL_TrgSetStat,
    jointPackage_CPL2SPL_TrgForeachStat,
    jointPackage_CPL2SPL_TrgContinueStat,
    jointPackage_CPL2SPL_TrgIfStat,
    jointPackage_CPL2SPL_TrgCompoundStat,
    TrgService,
    TrgLocatedElement,
    jointPackage_CPL2SPL_TrgResponse,
    jointPackage_CPL2SPL_TrgSelectMember,
    jointPackage_CPL2SPL_TrgConstant,
    jointPackage_CPL2SPL_TrgExpression,
    jointPackage_CPL2SPL_TrgSession,
    jointPackage_CPL2SPL_TrgStructureProperty,
    jointPackage_CPL2SPL_TrgTypeExpression,
    jointPackage_CPL2SPL_TrgStatement,
    jointPackage_CPL2SPL_TrgMessageField,
    jointPackage_CPL2SPL_TrgMethodName,
    jointPackage_CPL2SPL_TrgBranch,
    jointPackage_CPL2SPL_TrgFunctionCall,
    jointPackage_CPL2SPL_TrgDeclaration,
    jointPackage_CPL2SPL_TrgProgram,
    SrcAction,
    jointPackage_CPL2SPL_SrcSignallingAction,
    SrcOtherwise,
    SrcNotPresent,
    TrgSession,
    jointPackage_CPL2SPL_TrgEvent,
    jointPackage_CPL2SPL_TrgRegistration,
    jointPackage_CPL2SPL_TrgMethod,
    jointPackage_CPL2SPL_TrgDialog,
    TrgDeclaration,
    jointPackage_CPL2SPL_TrgVariableDeclaration,
    jointPackage_CPL2SPL_TrgStructureDeclaration,
    jointPackage_CPL2SPL_TrgFunctionDeclaration,
    jointPackage_CPL2SPL_TrgService,
    jointPackage_CPL2SPL_TrgLocatedElement,
    TrgErrorResponse,
    jointPackage_CPL2SPL_TrgRedirectionErrorResponse,
    jointPackage_CPL2SPL_TrgGlobalErrorResponse,
    jointPackage_CPL2SPL_TrgServerErrorResponse,
    jointPackage_CPL2SPL_TrgClientErrorResponse,
    TrgTypeExpression,
    jointPackage_CPL2SPL_TrgDefinedType,
    jointPackage_CPL2SPL_TrgSimpleType,
    jointPackage_CPL2SPL_TrgSequenceType,
    SrcNode,
    jointPackage_CPL2SPL_SrcAction,
    jointPackage_CPL2SPL_SrcSwitch,
    jointPackage_CPL2SPL_SrcSubCall,
    jointPackage_CPL2SPL_SrcElement,
    SrcDefault,
    SrcFailure,
    SrcRedirection,
    SrcNoAnswer,
    SrcBusy,
    SrcSignallingAction,
    jointPackage_CPL2SPL_SrcReject,
    jointPackage_CPL2SPL_SrcRedirect,
    jointPackage_CPL2SPL_SrcProxy,
    SrcSwitchedPriority,
    SrcNodeContainer,
    jointPackage_CPL2SPL_SrcBusy,
    jointPackage_CPL2SPL_SrcOtherwise,
    jointPackage_CPL2SPL_SrcSwitchedLanguage,
    jointPackage_CPL2SPL_SrcSwitchedAddress,
    jointPackage_CPL2SPL_SrcIncoming,
    jointPackage_CPL2SPL_SrcFailure,
    jointPackage_CPL2SPL_SrcNoAnswer,
    jointPackage_CPL2SPL_SrcSwitchedTime,
    jointPackage_CPL2SPL_SrcSwitchedString,
    jointPackage_CPL2SPL_SrcRedirection,
    jointPackage_CPL2SPL_SrcNotPresent,
    jointPackage_CPL2SPL_SrcOutgoing,
    jointPackage_CPL2SPL_SrcDefault,
    jointPackage_CPL2SPL_SrcSwitchedPriority,
    jointPackage_CPL2SPL_SrcLocation,
    jointPackage_CPL2SPL_SrcSubAction,
    SrcIncoming,
    SrcOutgoing,
    SrcSubAction,
    SrcElement,
    jointPackage_CPL2SPL_SrcCPL,
    jointPackage_CPL2SPL_SrcNode,
    jointPackage_CPL2SPL_SrcNodeContainer,
    jointPackage_CPL2SPL_SrcCPLModel,
    TrgServerErrorResponse,
    SrcReject,
    jointPackage_CPL2SPL_JointMM,
    SrcSwitchedTime,
    SrcSwitchedLanguage,
    SrcSwitchedString,
    SrcSwitchedAddress,
    SrcSwitch,
    jointPackage_CPL2SPL_SrcLanguageSwitch,
    jointPackage_CPL2SPL_SrcTimeSwitch,
    jointPackage_CPL2SPL_SrcStringSwitch,
    jointPackage_CPL2SPL_SrcPrioritySwitch,
    jointPackage_CPL2SPL_SrcAddressSwitch,
    PrimitiveType,
    Direction,
    ClientErrorKind,
    GlobalErrorKind,
    Modifier,
    FunctionLocation,
    RedirectionErrorKind,
    SuccessKind,
    SIPHeader,
    ControlMethod,
    ServerErrorKind,
    SIPMethod,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trgresponse_is_not_abstract():
    assert not inspect.isabstract(TrgResponse)


def test_trgresponse_constructor_exists():
    assert callable(TrgResponse.__init__)


def test_trgresponse_constructor_args():
    sig = inspect.signature(TrgResponse.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgerrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgErrorResponse)


def test_jointpackage_cpl2spl_trgerrorresponse_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgErrorResponse.__init__)


def test_jointpackage_cpl2spl_trgerrorresponse_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgErrorResponse.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgsuccessresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSuccessResponse)


def test_jointpackage_cpl2spl_trgsuccessresponse_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSuccessResponse.__init__)


def test_jointpackage_cpl2spl_trgsuccessresponse_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSuccessResponse.__init__)
    params = list(sig.parameters.keys())
    assert "successKind" in params, "Missing parameter 'successKind'"

def test_jointpackage_cpl2spl_trgsuccessresponse_has_successKind():
    assert hasattr(jointPackage_CPL2SPL_TrgSuccessResponse, "successKind")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgSuccessResponse.__mro__:
        if "successKind" in klass.__dict__:
            descriptor = klass.__dict__["successKind"]
            break
    assert isinstance(descriptor, property)



def test_trgvariableplace_is_not_abstract():
    assert not inspect.isabstract(TrgVariablePlace)


def test_trgvariableplace_constructor_exists():
    assert callable(TrgVariablePlace.__init__)


def test_trgvariableplace_constructor_args():
    sig = inspect.signature(TrgVariablePlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgpropertycallplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgPropertyCallPlace)


def test_jointpackage_cpl2spl_trgpropertycallplace_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgPropertyCallPlace.__init__)


def test_jointpackage_cpl2spl_trgpropertycallplace_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgPropertyCallPlace.__init__)
    params = list(sig.parameters.keys())
    assert "propName" in params, "Missing parameter 'propName'"

def test_jointpackage_cpl2spl_trgpropertycallplace_has_propName():
    assert hasattr(jointPackage_CPL2SPL_TrgPropertyCallPlace, "propName")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgPropertyCallPlace.__mro__:
        if "propName" in klass.__dict__:
            descriptor = klass.__dict__["propName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgvariable_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgVariable)


def test_jointpackage_cpl2spl_trgvariable_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgVariable.__init__)


def test_jointpackage_cpl2spl_trgvariable_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgVariable.__init__)
    params = list(sig.parameters.keys())



def test_trgselectmember_is_not_abstract():
    assert not inspect.isabstract(TrgSelectMember)


def test_trgselectmember_constructor_exists():
    assert callable(TrgSelectMember.__init__)


def test_trgselectmember_constructor_args():
    sig = inspect.signature(TrgSelectMember.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgselectcase_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSelectCase)


def test_jointpackage_cpl2spl_trgselectcase_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSelectCase.__init__)


def test_jointpackage_cpl2spl_trgselectcase_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSelectCase.__init__)
    params = list(sig.parameters.keys())



def test_trgmessagefield_is_not_abstract():
    assert not inspect.isabstract(TrgMessageField)


def test_trgmessagefield_constructor_exists():
    assert callable(TrgMessageField.__init__)


def test_trgmessagefield_constructor_args():
    sig = inspect.signature(TrgMessageField.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgheadedmessagefield_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgHeadedMessageField)


def test_jointpackage_cpl2spl_trgheadedmessagefield_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgHeadedMessageField.__init__)


def test_jointpackage_cpl2spl_trgheadedmessagefield_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgHeadedMessageField.__init__)
    params = list(sig.parameters.keys())
    assert "headerId" in params, "Missing parameter 'headerId'"

def test_jointpackage_cpl2spl_trgheadedmessagefield_has_headerId():
    assert hasattr(jointPackage_CPL2SPL_TrgHeadedMessageField, "headerId")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgHeadedMessageField.__mro__:
        if "headerId" in klass.__dict__:
            descriptor = klass.__dict__["headerId"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgreasonmessagefield_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgReasonMessageField)


def test_jointpackage_cpl2spl_trgreasonmessagefield_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgReasonMessageField.__init__)


def test_jointpackage_cpl2spl_trgreasonmessagefield_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgReasonMessageField.__init__)
    params = list(sig.parameters.keys())



def test_trgfunctioncall_is_not_abstract():
    assert not inspect.isabstract(TrgFunctionCall)


def test_trgfunctioncall_constructor_exists():
    assert callable(TrgFunctionCall.__init__)


def test_trgfunctioncall_constructor_args():
    sig = inspect.signature(TrgFunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_trgselectdefault_is_not_abstract():
    assert not inspect.isabstract(TrgSelectDefault)


def test_trgselectdefault_constructor_exists():
    assert callable(TrgSelectDefault.__init__)


def test_trgselectdefault_constructor_args():
    sig = inspect.signature(TrgSelectDefault.__init__)
    params = list(sig.parameters.keys())



def test_trgselectcase_is_not_abstract():
    assert not inspect.isabstract(TrgSelectCase)


def test_trgselectcase_constructor_exists():
    assert callable(TrgSelectCase.__init__)


def test_trgselectcase_constructor_args():
    sig = inspect.signature(TrgSelectCase.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgselectdefault_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSelectDefault)


def test_jointpackage_cpl2spl_trgselectdefault_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSelectDefault.__init__)


def test_jointpackage_cpl2spl_trgselectdefault_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSelectDefault.__init__)
    params = list(sig.parameters.keys())



def test_trgconstant_is_not_abstract():
    assert not inspect.isabstract(TrgConstant)


def test_trgconstant_constructor_exists():
    assert callable(TrgConstant.__init__)


def test_trgconstant_constructor_args():
    sig = inspect.signature(TrgConstant.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgsequenceconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSequenceConstant)


def test_jointpackage_cpl2spl_trgsequenceconstant_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSequenceConstant.__init__)


def test_jointpackage_cpl2spl_trgsequenceconstant_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSequenceConstant.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgstringconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgStringConstant)


def test_jointpackage_cpl2spl_trgstringconstant_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgStringConstant.__init__)


def test_jointpackage_cpl2spl_trgstringconstant_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgStringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage_cpl2spl_trgstringconstant_has_value():
    assert hasattr(jointPackage_CPL2SPL_TrgStringConstant, "value")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgStringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgresponseconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgResponseConstant)


def test_jointpackage_cpl2spl_trgresponseconstant_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgResponseConstant.__init__)


def test_jointpackage_cpl2spl_trgresponseconstant_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgResponseConstant.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgintegerconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgIntegerConstant)


def test_jointpackage_cpl2spl_trgintegerconstant_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgIntegerConstant.__init__)


def test_jointpackage_cpl2spl_trgintegerconstant_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgIntegerConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage_cpl2spl_trgintegerconstant_has_value():
    assert hasattr(jointPackage_CPL2SPL_TrgIntegerConstant, "value")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgIntegerConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trguriconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgURIConstant)


def test_jointpackage_cpl2spl_trguriconstant_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgURIConstant.__init__)


def test_jointpackage_cpl2spl_trguriconstant_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgURIConstant.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_jointpackage_cpl2spl_trguriconstant_has_uri():
    assert hasattr(jointPackage_CPL2SPL_TrgURIConstant, "uri")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgURIConstant.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgbooleanconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgBooleanConstant)


def test_jointpackage_cpl2spl_trgbooleanconstant_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgBooleanConstant.__init__)


def test_jointpackage_cpl2spl_trgbooleanconstant_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgBooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage_cpl2spl_trgbooleanconstant_has_value():
    assert hasattr(jointPackage_CPL2SPL_TrgBooleanConstant, "value")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgBooleanConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_trgnamedbranch_is_not_abstract():
    assert not inspect.isabstract(TrgNamedBranch)


def test_trgnamedbranch_constructor_exists():
    assert callable(TrgNamedBranch.__init__)


def test_trgnamedbranch_constructor_args():
    sig = inspect.signature(TrgNamedBranch.__init__)
    params = list(sig.parameters.keys())



def test_trgwhenheader_is_not_abstract():
    assert not inspect.isabstract(TrgWhenHeader)


def test_trgwhenheader_constructor_exists():
    assert callable(TrgWhenHeader.__init__)


def test_trgwhenheader_constructor_args():
    sig = inspect.signature(TrgWhenHeader.__init__)
    params = list(sig.parameters.keys())



def test_trgvariable_is_not_abstract():
    assert not inspect.isabstract(TrgVariable)


def test_trgvariable_constructor_exists():
    assert callable(TrgVariable.__init__)


def test_trgvariable_constructor_args():
    sig = inspect.signature(TrgVariable.__init__)
    params = list(sig.parameters.keys())



def test_trgfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(TrgFunctionDeclaration)


def test_trgfunctiondeclaration_constructor_exists():
    assert callable(TrgFunctionDeclaration.__init__)


def test_trgfunctiondeclaration_constructor_args():
    sig = inspect.signature(TrgFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trglocalfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgLocalFunctionDeclaration)


def test_jointpackage_cpl2spl_trglocalfunctiondeclaration_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgLocalFunctionDeclaration.__init__)


def test_jointpackage_cpl2spl_trglocalfunctiondeclaration_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgLocalFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgremotefunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration)


def test_jointpackage_cpl2spl_trgremotefunctiondeclaration_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration.__init__)


def test_jointpackage_cpl2spl_trgremotefunctiondeclaration_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionLocation" in params, "Missing parameter 'functionLocation'"

def test_jointpackage_cpl2spl_trgremotefunctiondeclaration_has_functionLocation():
    assert hasattr(jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration, "functionLocation")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration.__mro__:
        if "functionLocation" in klass.__dict__:
            descriptor = klass.__dict__["functionLocation"]
            break
    assert isinstance(descriptor, property)



def test_trgplace_is_not_abstract():
    assert not inspect.isabstract(TrgPlace)


def test_trgplace_constructor_exists():
    assert callable(TrgPlace.__init__)


def test_trgplace_constructor_args():
    sig = inspect.signature(TrgPlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgsipheaderplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSIPHeaderPlace)


def test_jointpackage_cpl2spl_trgsipheaderplace_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSIPHeaderPlace.__init__)


def test_jointpackage_cpl2spl_trgsipheaderplace_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSIPHeaderPlace.__init__)
    params = list(sig.parameters.keys())
    assert "header" in params, "Missing parameter 'header'"

def test_jointpackage_cpl2spl_trgsipheaderplace_has_header():
    assert hasattr(jointPackage_CPL2SPL_TrgSIPHeaderPlace, "header")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgSIPHeaderPlace.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgvariableplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgVariablePlace)


def test_jointpackage_cpl2spl_trgvariableplace_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgVariablePlace.__init__)


def test_jointpackage_cpl2spl_trgvariableplace_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgVariablePlace.__init__)
    params = list(sig.parameters.keys())



def test_trgexpression_is_not_abstract():
    assert not inspect.isabstract(TrgExpression)


def test_trgexpression_constructor_exists():
    assert callable(TrgExpression.__init__)


def test_trgexpression_constructor_args():
    sig = inspect.signature(TrgExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgPlace)


def test_jointpackage_cpl2spl_trgplace_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgPlace.__init__)


def test_jointpackage_cpl2spl_trgplace_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgPlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgblockexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgBlockExp)


def test_jointpackage_cpl2spl_trgblockexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgBlockExp.__init__)


def test_jointpackage_cpl2spl_trgblockexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgBlockExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgoperatorexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgOperatorExp)


def test_jointpackage_cpl2spl_trgoperatorexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgOperatorExp.__init__)


def test_jointpackage_cpl2spl_trgoperatorexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgOperatorExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_jointpackage_cpl2spl_trgoperatorexp_has_opName():
    assert hasattr(jointPackage_CPL2SPL_TrgOperatorExp, "opName")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgOperatorExp.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgpopexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgPopExp)


def test_jointpackage_cpl2spl_trgpopexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgPopExp.__init__)


def test_jointpackage_cpl2spl_trgpopexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgPopExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgbodyexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgBODYExp)


def test_jointpackage_cpl2spl_trgbodyexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgBODYExp.__init__)


def test_jointpackage_cpl2spl_trgbodyexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgBODYExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgreasonexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgReasonExp)


def test_jointpackage_cpl2spl_trgreasonexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgReasonExp.__init__)


def test_jointpackage_cpl2spl_trgreasonexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgReasonExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgforwardexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgForwardExp)


def test_jointpackage_cpl2spl_trgforwardexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgForwardExp.__init__)


def test_jointpackage_cpl2spl_trgforwardexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgForwardExp.__init__)
    params = list(sig.parameters.keys())
    assert "isParallel" in params, "Missing parameter 'isParallel'"

def test_jointpackage_cpl2spl_trgforwardexp_has_isParallel():
    assert hasattr(jointPackage_CPL2SPL_TrgForwardExp, "isParallel")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgForwardExp.__mro__:
        if "isParallel" in klass.__dict__:
            descriptor = klass.__dict__["isParallel"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgwithexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgWithExp)


def test_jointpackage_cpl2spl_trgwithexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgWithExp.__init__)


def test_jointpackage_cpl2spl_trgwithexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgWithExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgfunctioncallexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgFunctionCallExp)


def test_jointpackage_cpl2spl_trgfunctioncallexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgFunctionCallExp.__init__)


def test_jointpackage_cpl2spl_trgfunctioncallexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgFunctionCallExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgconstantexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgConstantExp)


def test_jointpackage_cpl2spl_trgconstantexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgConstantExp.__init__)


def test_jointpackage_cpl2spl_trgconstantexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgConstantExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgrequesturiexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgRequestURIExp)


def test_jointpackage_cpl2spl_trgrequesturiexp_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgRequestURIExp.__init__)


def test_jointpackage_cpl2spl_trgrequesturiexp_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgRequestURIExp.__init__)
    params = list(sig.parameters.keys())



def test_trgargument_is_not_abstract():
    assert not inspect.isabstract(TrgArgument)


def test_trgargument_constructor_exists():
    assert callable(TrgArgument.__init__)


def test_trgargument_constructor_args():
    sig = inspect.signature(TrgArgument.__init__)
    params = list(sig.parameters.keys())



def test_trgmethodname_is_not_abstract():
    assert not inspect.isabstract(TrgMethodName)


def test_trgmethodname_constructor_exists():
    assert callable(TrgMethodName.__init__)


def test_trgmethodname_constructor_args():
    sig = inspect.signature(TrgMethodName.__init__)
    params = list(sig.parameters.keys())



def test_trgmethod_is_not_abstract():
    assert not inspect.isabstract(TrgMethod)


def test_trgmethod_constructor_exists():
    assert callable(TrgMethod.__init__)


def test_trgmethod_constructor_args():
    sig = inspect.signature(TrgMethod.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgcontrolmethodname_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgControlMethodName)


def test_jointpackage_cpl2spl_trgcontrolmethodname_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgControlMethodName.__init__)


def test_jointpackage_cpl2spl_trgcontrolmethodname_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgControlMethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_cpl2spl_trgcontrolmethodname_has_name():
    assert hasattr(jointPackage_CPL2SPL_TrgControlMethodName, "name")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgControlMethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgsipmethodname_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSIPMethodName)


def test_jointpackage_cpl2spl_trgsipmethodname_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSIPMethodName.__init__)


def test_jointpackage_cpl2spl_trgsipmethodname_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSIPMethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_cpl2spl_trgsipmethodname_has_name():
    assert hasattr(jointPackage_CPL2SPL_TrgSIPMethodName, "name")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgSIPMethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trgvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(TrgVariableDeclaration)


def test_trgvariabledeclaration_constructor_exists():
    assert callable(TrgVariableDeclaration.__init__)


def test_trgvariabledeclaration_constructor_args():
    sig = inspect.signature(TrgVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgwhenheader_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgWhenHeader)


def test_jointpackage_cpl2spl_trgwhenheader_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgWhenHeader.__init__)


def test_jointpackage_cpl2spl_trgwhenheader_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgWhenHeader.__init__)
    params = list(sig.parameters.keys())
    assert "headerId" in params, "Missing parameter 'headerId'"

def test_jointpackage_cpl2spl_trgwhenheader_has_headerId():
    assert hasattr(jointPackage_CPL2SPL_TrgWhenHeader, "headerId")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgWhenHeader.__mro__:
        if "headerId" in klass.__dict__:
            descriptor = klass.__dict__["headerId"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgargument_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgArgument)


def test_jointpackage_cpl2spl_trgargument_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgArgument.__init__)


def test_jointpackage_cpl2spl_trgargument_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgArgument.__init__)
    params = list(sig.parameters.keys())



def test_trgbranch_is_not_abstract():
    assert not inspect.isabstract(TrgBranch)


def test_trgbranch_constructor_exists():
    assert callable(TrgBranch.__init__)


def test_trgbranch_constructor_args():
    sig = inspect.signature(TrgBranch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgnamedbranch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgNamedBranch)


def test_jointpackage_cpl2spl_trgnamedbranch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgNamedBranch.__init__)


def test_jointpackage_cpl2spl_trgnamedbranch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgNamedBranch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_cpl2spl_trgnamedbranch_has_name():
    assert hasattr(jointPackage_CPL2SPL_TrgNamedBranch, "name")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgNamedBranch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgdefaultbranch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgDefaultBranch)


def test_jointpackage_cpl2spl_trgdefaultbranch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgDefaultBranch.__init__)


def test_jointpackage_cpl2spl_trgdefaultbranch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgDefaultBranch.__init__)
    params = list(sig.parameters.keys())



def test_trgstatement_is_not_abstract():
    assert not inspect.isabstract(TrgStatement)


def test_trgstatement_constructor_exists():
    assert callable(TrgStatement.__init__)


def test_trgstatement_constructor_args():
    sig = inspect.signature(TrgStatement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgreturnstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgReturnStat)


def test_jointpackage_cpl2spl_trgreturnstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgReturnStat.__init__)


def test_jointpackage_cpl2spl_trgreturnstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgReturnStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgselectstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSelectStat)


def test_jointpackage_cpl2spl_trgselectstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSelectStat.__init__)


def test_jointpackage_cpl2spl_trgselectstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSelectStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgfunctioncallstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgFunctionCallStat)


def test_jointpackage_cpl2spl_trgfunctioncallstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgFunctionCallStat.__init__)


def test_jointpackage_cpl2spl_trgfunctioncallstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgFunctionCallStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgdeclarationstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgDeclarationStat)


def test_jointpackage_cpl2spl_trgdeclarationstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgDeclarationStat.__init__)


def test_jointpackage_cpl2spl_trgdeclarationstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgDeclarationStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgpushstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgPushStat)


def test_jointpackage_cpl2spl_trgpushstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgPushStat.__init__)


def test_jointpackage_cpl2spl_trgpushstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgPushStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgbreakstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgBreakStat)


def test_jointpackage_cpl2spl_trgbreakstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgBreakStat.__init__)


def test_jointpackage_cpl2spl_trgbreakstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgBreakStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgwhenstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgWhenStat)


def test_jointpackage_cpl2spl_trgwhenstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgWhenStat.__init__)


def test_jointpackage_cpl2spl_trgwhenstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgWhenStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgsetstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSetStat)


def test_jointpackage_cpl2spl_trgsetstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSetStat.__init__)


def test_jointpackage_cpl2spl_trgsetstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSetStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgforeachstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgForeachStat)


def test_jointpackage_cpl2spl_trgforeachstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgForeachStat.__init__)


def test_jointpackage_cpl2spl_trgforeachstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgForeachStat.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_jointpackage_cpl2spl_trgforeachstat_has_iteratorName():
    assert hasattr(jointPackage_CPL2SPL_TrgForeachStat, "iteratorName")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgForeachStat.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgcontinuestat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgContinueStat)


def test_jointpackage_cpl2spl_trgcontinuestat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgContinueStat.__init__)


def test_jointpackage_cpl2spl_trgcontinuestat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgContinueStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgifstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgIfStat)


def test_jointpackage_cpl2spl_trgifstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgIfStat.__init__)


def test_jointpackage_cpl2spl_trgifstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgIfStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgcompoundstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgCompoundStat)


def test_jointpackage_cpl2spl_trgcompoundstat_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgCompoundStat.__init__)


def test_jointpackage_cpl2spl_trgcompoundstat_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgCompoundStat.__init__)
    params = list(sig.parameters.keys())



def test_trgservice_is_not_abstract():
    assert not inspect.isabstract(TrgService)


def test_trgservice_constructor_exists():
    assert callable(TrgService.__init__)


def test_trgservice_constructor_args():
    sig = inspect.signature(TrgService.__init__)
    params = list(sig.parameters.keys())



def test_trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(TrgLocatedElement)


def test_trglocatedelement_constructor_exists():
    assert callable(TrgLocatedElement.__init__)


def test_trglocatedelement_constructor_args():
    sig = inspect.signature(TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgResponse)


def test_jointpackage_cpl2spl_trgresponse_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgResponse.__init__)


def test_jointpackage_cpl2spl_trgresponse_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgResponse.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgselectmember_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSelectMember)


def test_jointpackage_cpl2spl_trgselectmember_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSelectMember.__init__)


def test_jointpackage_cpl2spl_trgselectmember_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSelectMember.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgConstant)


def test_jointpackage_cpl2spl_trgconstant_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgConstant.__init__)


def test_jointpackage_cpl2spl_trgconstant_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgConstant.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgexpression_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgExpression)


def test_jointpackage_cpl2spl_trgexpression_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgExpression.__init__)


def test_jointpackage_cpl2spl_trgexpression_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgsession_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSession)


def test_jointpackage_cpl2spl_trgsession_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSession.__init__)


def test_jointpackage_cpl2spl_trgsession_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSession.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgstructureproperty_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgStructureProperty)


def test_jointpackage_cpl2spl_trgstructureproperty_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgStructureProperty.__init__)


def test_jointpackage_cpl2spl_trgstructureproperty_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgStructureProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_cpl2spl_trgstructureproperty_has_name():
    assert hasattr(jointPackage_CPL2SPL_TrgStructureProperty, "name")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgStructureProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgtypeexpression_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgTypeExpression)


def test_jointpackage_cpl2spl_trgtypeexpression_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgTypeExpression.__init__)


def test_jointpackage_cpl2spl_trgtypeexpression_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgTypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgstatement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgStatement)


def test_jointpackage_cpl2spl_trgstatement_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgStatement.__init__)


def test_jointpackage_cpl2spl_trgstatement_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgStatement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgmessagefield_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgMessageField)


def test_jointpackage_cpl2spl_trgmessagefield_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgMessageField.__init__)


def test_jointpackage_cpl2spl_trgmessagefield_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgMessageField.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgmethodname_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgMethodName)


def test_jointpackage_cpl2spl_trgmethodname_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgMethodName.__init__)


def test_jointpackage_cpl2spl_trgmethodname_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgMethodName.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgbranch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgBranch)


def test_jointpackage_cpl2spl_trgbranch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgBranch.__init__)


def test_jointpackage_cpl2spl_trgbranch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgBranch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgfunctioncall_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgFunctionCall)


def test_jointpackage_cpl2spl_trgfunctioncall_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgFunctionCall.__init__)


def test_jointpackage_cpl2spl_trgfunctioncall_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgFunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgdeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgDeclaration)


def test_jointpackage_cpl2spl_trgdeclaration_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgDeclaration.__init__)


def test_jointpackage_cpl2spl_trgdeclaration_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_cpl2spl_trgdeclaration_has_name():
    assert hasattr(jointPackage_CPL2SPL_TrgDeclaration, "name")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgprogram_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgProgram)


def test_jointpackage_cpl2spl_trgprogram_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgProgram.__init__)


def test_jointpackage_cpl2spl_trgprogram_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgProgram.__init__)
    params = list(sig.parameters.keys())



def test_srcaction_is_not_abstract():
    assert not inspect.isabstract(SrcAction)


def test_srcaction_constructor_exists():
    assert callable(SrcAction.__init__)


def test_srcaction_constructor_args():
    sig = inspect.signature(SrcAction.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcsignallingaction_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSignallingAction)


def test_jointpackage_cpl2spl_srcsignallingaction_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSignallingAction.__init__)


def test_jointpackage_cpl2spl_srcsignallingaction_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSignallingAction.__init__)
    params = list(sig.parameters.keys())



def test_srcotherwise_is_not_abstract():
    assert not inspect.isabstract(SrcOtherwise)


def test_srcotherwise_constructor_exists():
    assert callable(SrcOtherwise.__init__)


def test_srcotherwise_constructor_args():
    sig = inspect.signature(SrcOtherwise.__init__)
    params = list(sig.parameters.keys())



def test_srcnotpresent_is_not_abstract():
    assert not inspect.isabstract(SrcNotPresent)


def test_srcnotpresent_constructor_exists():
    assert callable(SrcNotPresent.__init__)


def test_srcnotpresent_constructor_args():
    sig = inspect.signature(SrcNotPresent.__init__)
    params = list(sig.parameters.keys())



def test_trgsession_is_not_abstract():
    assert not inspect.isabstract(TrgSession)


def test_trgsession_constructor_exists():
    assert callable(TrgSession.__init__)


def test_trgsession_constructor_args():
    sig = inspect.signature(TrgSession.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgevent_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgEvent)


def test_jointpackage_cpl2spl_trgevent_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgEvent.__init__)


def test_jointpackage_cpl2spl_trgevent_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgEvent.__init__)
    params = list(sig.parameters.keys())
    assert "eventId" in params, "Missing parameter 'eventId'"

def test_jointpackage_cpl2spl_trgevent_has_eventId():
    assert hasattr(jointPackage_CPL2SPL_TrgEvent, "eventId")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgEvent.__mro__:
        if "eventId" in klass.__dict__:
            descriptor = klass.__dict__["eventId"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgregistration_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgRegistration)


def test_jointpackage_cpl2spl_trgregistration_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgRegistration.__init__)


def test_jointpackage_cpl2spl_trgregistration_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgRegistration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgmethod_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgMethod)


def test_jointpackage_cpl2spl_trgmethod_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgMethod.__init__)


def test_jointpackage_cpl2spl_trgmethod_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgMethod.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_jointpackage_cpl2spl_trgmethod_has_direction():
    assert hasattr(jointPackage_CPL2SPL_TrgMethod, "direction")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgMethod.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgdialog_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgDialog)


def test_jointpackage_cpl2spl_trgdialog_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgDialog.__init__)


def test_jointpackage_cpl2spl_trgdialog_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgDialog.__init__)
    params = list(sig.parameters.keys())



def test_trgdeclaration_is_not_abstract():
    assert not inspect.isabstract(TrgDeclaration)


def test_trgdeclaration_constructor_exists():
    assert callable(TrgDeclaration.__init__)


def test_trgdeclaration_constructor_args():
    sig = inspect.signature(TrgDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgVariableDeclaration)


def test_jointpackage_cpl2spl_trgvariabledeclaration_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgVariableDeclaration.__init__)


def test_jointpackage_cpl2spl_trgvariabledeclaration_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgstructuredeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgStructureDeclaration)


def test_jointpackage_cpl2spl_trgstructuredeclaration_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgStructureDeclaration.__init__)


def test_jointpackage_cpl2spl_trgstructuredeclaration_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgStructureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgFunctionDeclaration)


def test_jointpackage_cpl2spl_trgfunctiondeclaration_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgFunctionDeclaration.__init__)


def test_jointpackage_cpl2spl_trgfunctiondeclaration_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgservice_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgService)


def test_jointpackage_cpl2spl_trgservice_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgService.__init__)


def test_jointpackage_cpl2spl_trgservice_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgService.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_cpl2spl_trgservice_has_name():
    assert hasattr(jointPackage_CPL2SPL_TrgService, "name")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgService.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgLocatedElement)


def test_jointpackage_cpl2spl_trglocatedelement_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgLocatedElement.__init__)


def test_jointpackage_cpl2spl_trglocatedelement_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"

def test_jointpackage_cpl2spl_trglocatedelement_has_location():
    assert hasattr(jointPackage_CPL2SPL_TrgLocatedElement, "location")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgLocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_trglocatedelement_has_commentsBefore():
    assert hasattr(jointPackage_CPL2SPL_TrgLocatedElement, "commentsBefore")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgLocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_trglocatedelement_has_commentsAfter():
    assert hasattr(jointPackage_CPL2SPL_TrgLocatedElement, "commentsAfter")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgLocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)



def test_trgerrorresponse_is_not_abstract():
    assert not inspect.isabstract(TrgErrorResponse)


def test_trgerrorresponse_constructor_exists():
    assert callable(TrgErrorResponse.__init__)


def test_trgerrorresponse_constructor_args():
    sig = inspect.signature(TrgErrorResponse.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgredirectionerrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgRedirectionErrorResponse)


def test_jointpackage_cpl2spl_trgredirectionerrorresponse_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgRedirectionErrorResponse.__init__)


def test_jointpackage_cpl2spl_trgredirectionerrorresponse_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgRedirectionErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_jointpackage_cpl2spl_trgredirectionerrorresponse_has_errorKind():
    assert hasattr(jointPackage_CPL2SPL_TrgRedirectionErrorResponse, "errorKind")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgRedirectionErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgglobalerrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgGlobalErrorResponse)


def test_jointpackage_cpl2spl_trgglobalerrorresponse_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgGlobalErrorResponse.__init__)


def test_jointpackage_cpl2spl_trgglobalerrorresponse_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgGlobalErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_jointpackage_cpl2spl_trgglobalerrorresponse_has_errorKind():
    assert hasattr(jointPackage_CPL2SPL_TrgGlobalErrorResponse, "errorKind")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgGlobalErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgservererrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgServerErrorResponse)


def test_jointpackage_cpl2spl_trgservererrorresponse_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgServerErrorResponse.__init__)


def test_jointpackage_cpl2spl_trgservererrorresponse_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgServerErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_jointpackage_cpl2spl_trgservererrorresponse_has_errorKind():
    assert hasattr(jointPackage_CPL2SPL_TrgServerErrorResponse, "errorKind")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgServerErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgclienterrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgClientErrorResponse)


def test_jointpackage_cpl2spl_trgclienterrorresponse_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgClientErrorResponse.__init__)


def test_jointpackage_cpl2spl_trgclienterrorresponse_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgClientErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_jointpackage_cpl2spl_trgclienterrorresponse_has_errorKind():
    assert hasattr(jointPackage_CPL2SPL_TrgClientErrorResponse, "errorKind")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgClientErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_trgtypeexpression_is_not_abstract():
    assert not inspect.isabstract(TrgTypeExpression)


def test_trgtypeexpression_constructor_exists():
    assert callable(TrgTypeExpression.__init__)


def test_trgtypeexpression_constructor_args():
    sig = inspect.signature(TrgTypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_trgdefinedtype_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgDefinedType)


def test_jointpackage_cpl2spl_trgdefinedtype_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgDefinedType.__init__)


def test_jointpackage_cpl2spl_trgdefinedtype_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_jointpackage_cpl2spl_trgdefinedtype_has_typeName():
    assert hasattr(jointPackage_CPL2SPL_TrgDefinedType, "typeName")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgDefinedType.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgsimpletype_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSimpleType)


def test_jointpackage_cpl2spl_trgsimpletype_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSimpleType.__init__)


def test_jointpackage_cpl2spl_trgsimpletype_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jointpackage_cpl2spl_trgsimpletype_has_type():
    assert hasattr(jointPackage_CPL2SPL_TrgSimpleType, "type")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgSimpleType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_trgsequencetype_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_TrgSequenceType)


def test_jointpackage_cpl2spl_trgsequencetype_constructor_exists():
    assert callable(jointPackage_CPL2SPL_TrgSequenceType.__init__)


def test_jointpackage_cpl2spl_trgsequencetype_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_TrgSequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "type" in params, "Missing parameter 'type'"
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_jointpackage_cpl2spl_trgsequencetype_has_size():
    assert hasattr(jointPackage_CPL2SPL_TrgSequenceType, "size")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgSequenceType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_trgsequencetype_has_type():
    assert hasattr(jointPackage_CPL2SPL_TrgSequenceType, "type")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgSequenceType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_trgsequencetype_has_modifier():
    assert hasattr(jointPackage_CPL2SPL_TrgSequenceType, "modifier")
    descriptor = None
    for klass in jointPackage_CPL2SPL_TrgSequenceType.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_srcnode_is_not_abstract():
    assert not inspect.isabstract(SrcNode)


def test_srcnode_constructor_exists():
    assert callable(SrcNode.__init__)


def test_srcnode_constructor_args():
    sig = inspect.signature(SrcNode.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcaction_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcAction)


def test_jointpackage_cpl2spl_srcaction_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcAction.__init__)


def test_jointpackage_cpl2spl_srcaction_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcAction.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSwitch)


def test_jointpackage_cpl2spl_srcswitch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSwitch.__init__)


def test_jointpackage_cpl2spl_srcswitch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSwitch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcsubcall_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSubCall)


def test_jointpackage_cpl2spl_srcsubcall_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSubCall.__init__)


def test_jointpackage_cpl2spl_srcsubcall_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSubCall.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_jointpackage_cpl2spl_srcsubcall_has_ref():
    assert hasattr(jointPackage_CPL2SPL_SrcSubCall, "ref")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSubCall.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcElement)


def test_jointpackage_cpl2spl_srcelement_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcElement.__init__)


def test_jointpackage_cpl2spl_srcelement_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_srcdefault_is_not_abstract():
    assert not inspect.isabstract(SrcDefault)


def test_srcdefault_constructor_exists():
    assert callable(SrcDefault.__init__)


def test_srcdefault_constructor_args():
    sig = inspect.signature(SrcDefault.__init__)
    params = list(sig.parameters.keys())



def test_srcfailure_is_not_abstract():
    assert not inspect.isabstract(SrcFailure)


def test_srcfailure_constructor_exists():
    assert callable(SrcFailure.__init__)


def test_srcfailure_constructor_args():
    sig = inspect.signature(SrcFailure.__init__)
    params = list(sig.parameters.keys())



def test_srcredirection_is_not_abstract():
    assert not inspect.isabstract(SrcRedirection)


def test_srcredirection_constructor_exists():
    assert callable(SrcRedirection.__init__)


def test_srcredirection_constructor_args():
    sig = inspect.signature(SrcRedirection.__init__)
    params = list(sig.parameters.keys())



def test_srcnoanswer_is_not_abstract():
    assert not inspect.isabstract(SrcNoAnswer)


def test_srcnoanswer_constructor_exists():
    assert callable(SrcNoAnswer.__init__)


def test_srcnoanswer_constructor_args():
    sig = inspect.signature(SrcNoAnswer.__init__)
    params = list(sig.parameters.keys())



def test_srcbusy_is_not_abstract():
    assert not inspect.isabstract(SrcBusy)


def test_srcbusy_constructor_exists():
    assert callable(SrcBusy.__init__)


def test_srcbusy_constructor_args():
    sig = inspect.signature(SrcBusy.__init__)
    params = list(sig.parameters.keys())



def test_srcsignallingaction_is_not_abstract():
    assert not inspect.isabstract(SrcSignallingAction)


def test_srcsignallingaction_constructor_exists():
    assert callable(SrcSignallingAction.__init__)


def test_srcsignallingaction_constructor_args():
    sig = inspect.signature(SrcSignallingAction.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcreject_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcReject)


def test_jointpackage_cpl2spl_srcreject_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcReject.__init__)


def test_jointpackage_cpl2spl_srcreject_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcReject.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "reason" in params, "Missing parameter 'reason'"

def test_jointpackage_cpl2spl_srcreject_has_status():
    assert hasattr(jointPackage_CPL2SPL_SrcReject, "status")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcReject.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcreject_has_reason():
    assert hasattr(jointPackage_CPL2SPL_SrcReject, "reason")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcReject.__mro__:
        if "reason" in klass.__dict__:
            descriptor = klass.__dict__["reason"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcredirect_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcRedirect)


def test_jointpackage_cpl2spl_srcredirect_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcRedirect.__init__)


def test_jointpackage_cpl2spl_srcredirect_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcRedirect.__init__)
    params = list(sig.parameters.keys())
    assert "permanent" in params, "Missing parameter 'permanent'"

def test_jointpackage_cpl2spl_srcredirect_has_permanent():
    assert hasattr(jointPackage_CPL2SPL_SrcRedirect, "permanent")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcRedirect.__mro__:
        if "permanent" in klass.__dict__:
            descriptor = klass.__dict__["permanent"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcproxy_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcProxy)


def test_jointpackage_cpl2spl_srcproxy_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcProxy.__init__)


def test_jointpackage_cpl2spl_srcproxy_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcProxy.__init__)
    params = list(sig.parameters.keys())
    assert "recurse" in params, "Missing parameter 'recurse'"
    assert "timeout" in params, "Missing parameter 'timeout'"
    assert "ordering" in params, "Missing parameter 'ordering'"

def test_jointpackage_cpl2spl_srcproxy_has_recurse():
    assert hasattr(jointPackage_CPL2SPL_SrcProxy, "recurse")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcProxy.__mro__:
        if "recurse" in klass.__dict__:
            descriptor = klass.__dict__["recurse"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcproxy_has_timeout():
    assert hasattr(jointPackage_CPL2SPL_SrcProxy, "timeout")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcProxy.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcproxy_has_ordering():
    assert hasattr(jointPackage_CPL2SPL_SrcProxy, "ordering")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcProxy.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)



def test_srcswitchedpriority_is_not_abstract():
    assert not inspect.isabstract(SrcSwitchedPriority)


def test_srcswitchedpriority_constructor_exists():
    assert callable(SrcSwitchedPriority.__init__)


def test_srcswitchedpriority_constructor_args():
    sig = inspect.signature(SrcSwitchedPriority.__init__)
    params = list(sig.parameters.keys())



def test_srcnodecontainer_is_not_abstract():
    assert not inspect.isabstract(SrcNodeContainer)


def test_srcnodecontainer_constructor_exists():
    assert callable(SrcNodeContainer.__init__)


def test_srcnodecontainer_constructor_args():
    sig = inspect.signature(SrcNodeContainer.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcbusy_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcBusy)


def test_jointpackage_cpl2spl_srcbusy_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcBusy.__init__)


def test_jointpackage_cpl2spl_srcbusy_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcBusy.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcotherwise_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcOtherwise)


def test_jointpackage_cpl2spl_srcotherwise_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcOtherwise.__init__)


def test_jointpackage_cpl2spl_srcotherwise_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcOtherwise.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcswitchedlanguage_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSwitchedLanguage)


def test_jointpackage_cpl2spl_srcswitchedlanguage_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSwitchedLanguage.__init__)


def test_jointpackage_cpl2spl_srcswitchedlanguage_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSwitchedLanguage.__init__)
    params = list(sig.parameters.keys())
    assert "matches" in params, "Missing parameter 'matches'"

def test_jointpackage_cpl2spl_srcswitchedlanguage_has_matches():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedLanguage, "matches")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedLanguage.__mro__:
        if "matches" in klass.__dict__:
            descriptor = klass.__dict__["matches"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcswitchedaddress_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSwitchedAddress)


def test_jointpackage_cpl2spl_srcswitchedaddress_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSwitchedAddress.__init__)


def test_jointpackage_cpl2spl_srcswitchedaddress_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSwitchedAddress.__init__)
    params = list(sig.parameters.keys())
    assert "is_" in params, "Missing parameter 'is_'"
    assert "contains" in params, "Missing parameter 'contains'"
    assert "subDomainOf" in params, "Missing parameter 'subDomainOf'"

def test_jointpackage_cpl2spl_srcswitchedaddress_has_is_():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedAddress, "is_")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedAddress.__mro__:
        if "is_" in klass.__dict__:
            descriptor = klass.__dict__["is_"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedaddress_has_contains():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedAddress, "contains")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedAddress.__mro__:
        if "contains" in klass.__dict__:
            descriptor = klass.__dict__["contains"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedaddress_has_subDomainOf():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedAddress, "subDomainOf")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedAddress.__mro__:
        if "subDomainOf" in klass.__dict__:
            descriptor = klass.__dict__["subDomainOf"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcincoming_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcIncoming)


def test_jointpackage_cpl2spl_srcincoming_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcIncoming.__init__)


def test_jointpackage_cpl2spl_srcincoming_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcIncoming.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcfailure_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcFailure)


def test_jointpackage_cpl2spl_srcfailure_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcFailure.__init__)


def test_jointpackage_cpl2spl_srcfailure_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcFailure.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcnoanswer_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcNoAnswer)


def test_jointpackage_cpl2spl_srcnoanswer_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcNoAnswer.__init__)


def test_jointpackage_cpl2spl_srcnoanswer_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcNoAnswer.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcswitchedtime_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSwitchedTime)


def test_jointpackage_cpl2spl_srcswitchedtime_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSwitchedTime.__init__)


def test_jointpackage_cpl2spl_srcswitchedtime_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSwitchedTime.__init__)
    params = list(sig.parameters.keys())
    assert "dtend" in params, "Missing parameter 'dtend'"
    assert "freq" in params, "Missing parameter 'freq'"
    assert "byHour" in params, "Missing parameter 'byHour'"
    assert "interval" in params, "Missing parameter 'interval'"
    assert "byDay" in params, "Missing parameter 'byDay'"
    assert "bySetPos" in params, "Missing parameter 'bySetPos'"
    assert "dtstart" in params, "Missing parameter 'dtstart'"
    assert "byMinute" in params, "Missing parameter 'byMinute'"
    assert "byWeekNo" in params, "Missing parameter 'byWeekNo'"
    assert "byMonth" in params, "Missing parameter 'byMonth'"
    assert "bySecond" in params, "Missing parameter 'bySecond'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "byMonthDay" in params, "Missing parameter 'byMonthDay'"
    assert "until" in params, "Missing parameter 'until'"
    assert "wkst" in params, "Missing parameter 'wkst'"
    assert "count" in params, "Missing parameter 'count'"
    assert "byYearDay" in params, "Missing parameter 'byYearDay'"

def test_jointpackage_cpl2spl_srcswitchedtime_has_dtend():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "dtend")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "dtend" in klass.__dict__:
            descriptor = klass.__dict__["dtend"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_freq():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "freq")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "freq" in klass.__dict__:
            descriptor = klass.__dict__["freq"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_byHour():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "byHour")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "byHour" in klass.__dict__:
            descriptor = klass.__dict__["byHour"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_interval():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "interval")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "interval" in klass.__dict__:
            descriptor = klass.__dict__["interval"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_byDay():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "byDay")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "byDay" in klass.__dict__:
            descriptor = klass.__dict__["byDay"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_bySetPos():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "bySetPos")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "bySetPos" in klass.__dict__:
            descriptor = klass.__dict__["bySetPos"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_dtstart():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "dtstart")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "dtstart" in klass.__dict__:
            descriptor = klass.__dict__["dtstart"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_byMinute():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "byMinute")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "byMinute" in klass.__dict__:
            descriptor = klass.__dict__["byMinute"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_byWeekNo():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "byWeekNo")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "byWeekNo" in klass.__dict__:
            descriptor = klass.__dict__["byWeekNo"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_byMonth():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "byMonth")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "byMonth" in klass.__dict__:
            descriptor = klass.__dict__["byMonth"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_bySecond():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "bySecond")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "bySecond" in klass.__dict__:
            descriptor = klass.__dict__["bySecond"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_duration():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "duration")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_byMonthDay():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "byMonthDay")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "byMonthDay" in klass.__dict__:
            descriptor = klass.__dict__["byMonthDay"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_until():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "until")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "until" in klass.__dict__:
            descriptor = klass.__dict__["until"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_wkst():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "wkst")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "wkst" in klass.__dict__:
            descriptor = klass.__dict__["wkst"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_count():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "count")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedtime_has_byYearDay():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedTime, "byYearDay")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedTime.__mro__:
        if "byYearDay" in klass.__dict__:
            descriptor = klass.__dict__["byYearDay"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcswitchedstring_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSwitchedString)


def test_jointpackage_cpl2spl_srcswitchedstring_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSwitchedString.__init__)


def test_jointpackage_cpl2spl_srcswitchedstring_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSwitchedString.__init__)
    params = list(sig.parameters.keys())
    assert "is_" in params, "Missing parameter 'is_'"
    assert "contains" in params, "Missing parameter 'contains'"

def test_jointpackage_cpl2spl_srcswitchedstring_has_is_():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedString, "is_")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedString.__mro__:
        if "is_" in klass.__dict__:
            descriptor = klass.__dict__["is_"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedstring_has_contains():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedString, "contains")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedString.__mro__:
        if "contains" in klass.__dict__:
            descriptor = klass.__dict__["contains"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcredirection_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcRedirection)


def test_jointpackage_cpl2spl_srcredirection_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcRedirection.__init__)


def test_jointpackage_cpl2spl_srcredirection_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcRedirection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcnotpresent_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcNotPresent)


def test_jointpackage_cpl2spl_srcnotpresent_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcNotPresent.__init__)


def test_jointpackage_cpl2spl_srcnotpresent_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcNotPresent.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcoutgoing_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcOutgoing)


def test_jointpackage_cpl2spl_srcoutgoing_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcOutgoing.__init__)


def test_jointpackage_cpl2spl_srcoutgoing_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcOutgoing.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcdefault_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcDefault)


def test_jointpackage_cpl2spl_srcdefault_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcDefault.__init__)


def test_jointpackage_cpl2spl_srcdefault_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcDefault.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcswitchedpriority_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSwitchedPriority)


def test_jointpackage_cpl2spl_srcswitchedpriority_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSwitchedPriority.__init__)


def test_jointpackage_cpl2spl_srcswitchedpriority_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSwitchedPriority.__init__)
    params = list(sig.parameters.keys())
    assert "equal" in params, "Missing parameter 'equal'"
    assert "greater" in params, "Missing parameter 'greater'"
    assert "less" in params, "Missing parameter 'less'"

def test_jointpackage_cpl2spl_srcswitchedpriority_has_equal():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedPriority, "equal")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedPriority.__mro__:
        if "equal" in klass.__dict__:
            descriptor = klass.__dict__["equal"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedpriority_has_greater():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedPriority, "greater")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedPriority.__mro__:
        if "greater" in klass.__dict__:
            descriptor = klass.__dict__["greater"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcswitchedpriority_has_less():
    assert hasattr(jointPackage_CPL2SPL_SrcSwitchedPriority, "less")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSwitchedPriority.__mro__:
        if "less" in klass.__dict__:
            descriptor = klass.__dict__["less"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srclocation_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcLocation)


def test_jointpackage_cpl2spl_srclocation_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcLocation.__init__)


def test_jointpackage_cpl2spl_srclocation_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcLocation.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "clear" in params, "Missing parameter 'clear'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_jointpackage_cpl2spl_srclocation_has_url():
    assert hasattr(jointPackage_CPL2SPL_SrcLocation, "url")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcLocation.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srclocation_has_clear():
    assert hasattr(jointPackage_CPL2SPL_SrcLocation, "clear")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcLocation.__mro__:
        if "clear" in klass.__dict__:
            descriptor = klass.__dict__["clear"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srclocation_has_priority():
    assert hasattr(jointPackage_CPL2SPL_SrcLocation, "priority")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcLocation.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcsubaction_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcSubAction)


def test_jointpackage_cpl2spl_srcsubaction_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcSubAction.__init__)


def test_jointpackage_cpl2spl_srcsubaction_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcSubAction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_jointpackage_cpl2spl_srcsubaction_has_id():
    assert hasattr(jointPackage_CPL2SPL_SrcSubAction, "id")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcSubAction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_srcincoming_is_not_abstract():
    assert not inspect.isabstract(SrcIncoming)


def test_srcincoming_constructor_exists():
    assert callable(SrcIncoming.__init__)


def test_srcincoming_constructor_args():
    sig = inspect.signature(SrcIncoming.__init__)
    params = list(sig.parameters.keys())



def test_srcoutgoing_is_not_abstract():
    assert not inspect.isabstract(SrcOutgoing)


def test_srcoutgoing_constructor_exists():
    assert callable(SrcOutgoing.__init__)


def test_srcoutgoing_constructor_args():
    sig = inspect.signature(SrcOutgoing.__init__)
    params = list(sig.parameters.keys())



def test_srcsubaction_is_not_abstract():
    assert not inspect.isabstract(SrcSubAction)


def test_srcsubaction_constructor_exists():
    assert callable(SrcSubAction.__init__)


def test_srcsubaction_constructor_args():
    sig = inspect.signature(SrcSubAction.__init__)
    params = list(sig.parameters.keys())



def test_srcelement_is_not_abstract():
    assert not inspect.isabstract(SrcElement)


def test_srcelement_constructor_exists():
    assert callable(SrcElement.__init__)


def test_srcelement_constructor_args():
    sig = inspect.signature(SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srccpl_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcCPL)


def test_jointpackage_cpl2spl_srccpl_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcCPL.__init__)


def test_jointpackage_cpl2spl_srccpl_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcCPL.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcnode_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcNode)


def test_jointpackage_cpl2spl_srcnode_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcNode.__init__)


def test_jointpackage_cpl2spl_srcnode_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcNode.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcnodecontainer_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcNodeContainer)


def test_jointpackage_cpl2spl_srcnodecontainer_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcNodeContainer.__init__)


def test_jointpackage_cpl2spl_srcnodecontainer_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcNodeContainer.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srccplmodel_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcCPLModel)


def test_jointpackage_cpl2spl_srccplmodel_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcCPLModel.__init__)


def test_jointpackage_cpl2spl_srccplmodel_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcCPLModel.__init__)
    params = list(sig.parameters.keys())



def test_trgservererrorresponse_is_not_abstract():
    assert not inspect.isabstract(TrgServerErrorResponse)


def test_trgservererrorresponse_constructor_exists():
    assert callable(TrgServerErrorResponse.__init__)


def test_trgservererrorresponse_constructor_args():
    sig = inspect.signature(TrgServerErrorResponse.__init__)
    params = list(sig.parameters.keys())



def test_srcreject_is_not_abstract():
    assert not inspect.isabstract(SrcReject)


def test_srcreject_constructor_exists():
    assert callable(SrcReject.__init__)


def test_srcreject_constructor_args():
    sig = inspect.signature(SrcReject.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_JointMM)


def test_jointpackage_cpl2spl_jointmm_constructor_exists():
    assert callable(jointPackage_CPL2SPL_JointMM.__init__)


def test_jointpackage_cpl2spl_jointmm_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_JointMM.__init__)
    params = list(sig.parameters.keys())



def test_srcswitchedtime_is_not_abstract():
    assert not inspect.isabstract(SrcSwitchedTime)


def test_srcswitchedtime_constructor_exists():
    assert callable(SrcSwitchedTime.__init__)


def test_srcswitchedtime_constructor_args():
    sig = inspect.signature(SrcSwitchedTime.__init__)
    params = list(sig.parameters.keys())



def test_srcswitchedlanguage_is_not_abstract():
    assert not inspect.isabstract(SrcSwitchedLanguage)


def test_srcswitchedlanguage_constructor_exists():
    assert callable(SrcSwitchedLanguage.__init__)


def test_srcswitchedlanguage_constructor_args():
    sig = inspect.signature(SrcSwitchedLanguage.__init__)
    params = list(sig.parameters.keys())



def test_srcswitchedstring_is_not_abstract():
    assert not inspect.isabstract(SrcSwitchedString)


def test_srcswitchedstring_constructor_exists():
    assert callable(SrcSwitchedString.__init__)


def test_srcswitchedstring_constructor_args():
    sig = inspect.signature(SrcSwitchedString.__init__)
    params = list(sig.parameters.keys())



def test_srcswitchedaddress_is_not_abstract():
    assert not inspect.isabstract(SrcSwitchedAddress)


def test_srcswitchedaddress_constructor_exists():
    assert callable(SrcSwitchedAddress.__init__)


def test_srcswitchedaddress_constructor_args():
    sig = inspect.signature(SrcSwitchedAddress.__init__)
    params = list(sig.parameters.keys())



def test_srcswitch_is_not_abstract():
    assert not inspect.isabstract(SrcSwitch)


def test_srcswitch_constructor_exists():
    assert callable(SrcSwitch.__init__)


def test_srcswitch_constructor_args():
    sig = inspect.signature(SrcSwitch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srclanguageswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcLanguageSwitch)


def test_jointpackage_cpl2spl_srclanguageswitch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcLanguageSwitch.__init__)


def test_jointpackage_cpl2spl_srclanguageswitch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcLanguageSwitch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srctimeswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcTimeSwitch)


def test_jointpackage_cpl2spl_srctimeswitch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcTimeSwitch.__init__)


def test_jointpackage_cpl2spl_srctimeswitch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcTimeSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "tzid" in params, "Missing parameter 'tzid'"
    assert "tzurl" in params, "Missing parameter 'tzurl'"

def test_jointpackage_cpl2spl_srctimeswitch_has_tzid():
    assert hasattr(jointPackage_CPL2SPL_SrcTimeSwitch, "tzid")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcTimeSwitch.__mro__:
        if "tzid" in klass.__dict__:
            descriptor = klass.__dict__["tzid"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srctimeswitch_has_tzurl():
    assert hasattr(jointPackage_CPL2SPL_SrcTimeSwitch, "tzurl")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcTimeSwitch.__mro__:
        if "tzurl" in klass.__dict__:
            descriptor = klass.__dict__["tzurl"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcstringswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcStringSwitch)


def test_jointpackage_cpl2spl_srcstringswitch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcStringSwitch.__init__)


def test_jointpackage_cpl2spl_srcstringswitch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcStringSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_jointpackage_cpl2spl_srcstringswitch_has_field():
    assert hasattr(jointPackage_CPL2SPL_SrcStringSwitch, "field")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcStringSwitch.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_cpl2spl_srcpriorityswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcPrioritySwitch)


def test_jointpackage_cpl2spl_srcpriorityswitch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcPrioritySwitch.__init__)


def test_jointpackage_cpl2spl_srcpriorityswitch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcPrioritySwitch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_cpl2spl_srcaddressswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage_CPL2SPL_SrcAddressSwitch)


def test_jointpackage_cpl2spl_srcaddressswitch_constructor_exists():
    assert callable(jointPackage_CPL2SPL_SrcAddressSwitch.__init__)


def test_jointpackage_cpl2spl_srcaddressswitch_constructor_args():
    sig = inspect.signature(jointPackage_CPL2SPL_SrcAddressSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "subField" in params, "Missing parameter 'subField'"
    assert "field" in params, "Missing parameter 'field'"

def test_jointpackage_cpl2spl_srcaddressswitch_has_subField():
    assert hasattr(jointPackage_CPL2SPL_SrcAddressSwitch, "subField")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcAddressSwitch.__mro__:
        if "subField" in klass.__dict__:
            descriptor = klass.__dict__["subField"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_cpl2spl_srcaddressswitch_has_field():
    assert hasattr(jointPackage_CPL2SPL_SrcAddressSwitch, "field")
    descriptor = None
    for klass in jointPackage_CPL2SPL_SrcAddressSwitch.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "request",
        "void",
        "time",
        "uri",
        "int",
        "response",
        "bool",
        "string",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "inout",
        "out",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_clienterrorkind_exists():
    # Check that the Enumeration exists
    assert ClientErrorKind is not None

def test_clienterrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClientErrorKind]
    expected_literals = [
        "TEMPORARILY_UNAVAILABLE",
        "UNAUTHORIZED",
        "ADDRESS_INCOMPLETE",
        "AMBIGUOUS",
        "LOOP_DETECTED",
        "UNDECIPHERABLE",
        "REQUEST_PENDING",
        "GONE",
        "NOT_FOUND",
        "NOT_ACCEPTABLE_HERE",
        "UNSUPPORTED_MEDIA_TYPE",
        "BAD_REQUEST",
        "REQUEST_TERMINATED",
        "FORBIDDEN",
        "METHOD_NOT_ALLOWED",
        "TOO_MANY_HOPS",
        "UNSUPPORTED_URI_SCHEME",
        "EXTENSION_REQUIRED",
        "INTERVAL_TOO_BRIEF",
        "NOT_ACCEPTABLE",
        "PAYMENT_REQUIRED",
        "CALL_OR_TRANSACTION_DOES_NOT_EXIST",
        "REQUESTURI_TOO_LONG",
        "REQUEST_TIMEOUT",
        "BAD_EXTENSION",
        "BUSY_HERE",
        "REQUEST_ENTITY_TOO_LARGE",
        "PROXY_AUTHENTICATION_REQUIRED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClientErrorKind"

def test_globalerrorkind_exists():
    # Check that the Enumeration exists
    assert GlobalErrorKind is not None

def test_globalerrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GlobalErrorKind]
    expected_literals = [
        "NOT_ACCEPTABLE",
        "DOES_NOT_EXIST_ANYWHERE",
        "DECLINE",
        "BUSY_EVERYWHERE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GlobalErrorKind"

def test_modifier_exists():
    # Check that the Enumeration exists
    assert Modifier is not None

def test_modifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Modifier]
    expected_literals = [
        "LIFO",
        "FIFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Modifier"

def test_functionlocation_exists():
    # Check that the Enumeration exists
    assert FunctionLocation is not None

def test_functionlocation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionLocation]
    expected_literals = [
        "local",
        "remote",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionLocation"

def test_redirectionerrorkind_exists():
    # Check that the Enumeration exists
    assert RedirectionErrorKind is not None

def test_redirectionerrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RedirectionErrorKind]
    expected_literals = [
        "USE_PROXY",
        "ALTERNATIVE_SERVICE",
        "MOVED_PERMANENTLY",
        "MOVED_TEMPORARILY",
        "MULTIPLE_CHOICES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RedirectionErrorKind"

def test_successkind_exists():
    # Check that the Enumeration exists
    assert SuccessKind is not None

def test_successkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuccessKind]
    expected_literals = [
        "ACCEPTED",
        "OK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SuccessKind"

def test_sipheader_exists():
    # Check that the Enumeration exists
    assert SIPHeader is not None

def test_sipheader_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIPHeader]
    expected_literals = [
        "VIA",
        "SUBSCRIPTION_STATE",
        "CALL_ID",
        "FROM",
        "CSEQ",
        "EVENT",
        "MAX_FORWARDS",
        "CONTACT",
        "TO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIPHeader"

def test_controlmethod_exists():
    # Check that the Enumeration exists
    assert ControlMethod is not None

def test_controlmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ControlMethod]
    expected_literals = [
        "unsubscribe",
        "deploy",
        "uninvite",
        "undeploy",
        "unregister",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ControlMethod"

def test_servererrorkind_exists():
    # Check that the Enumeration exists
    assert ServerErrorKind is not None

def test_servererrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServerErrorKind]
    expected_literals = [
        "VERSION_NOT_SUPPORTED",
        "NOT_IMPLEMENTED",
        "SERVICE_UNAVAILABLE",
        "SERVER_TIMEOUT",
        "SERVER_INTERNAL_ERROR",
        "MESSAGE_TOO_LARGE",
        "BAD_GATEWAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServerErrorKind"

def test_sipmethod_exists():
    # Check that the Enumeration exists
    assert SIPMethod is not None

def test_sipmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIPMethod]
    expected_literals = [
        "INVITE",
        "SUBSCRIBE",
        "NOTIFY",
        "OPTIONS",
        "BYE",
        "REREGISTER",
        "ACK",
        "REACK",
        "REINVITE",
        "CANCEL",
        "RESUBSCRIBE",
        "REGISTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIPMethod"


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
TrgResponse_strategy = st.builds(
    TrgResponse,
)
jointPackage_CPL2SPL_TrgErrorResponse_strategy = st.builds(
    jointPackage_CPL2SPL_TrgErrorResponse,
)
jointPackage_CPL2SPL_TrgSuccessResponse_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSuccessResponse,
    successKind=
        safe_text
)
TrgVariablePlace_strategy = st.builds(
    TrgVariablePlace,
)
jointPackage_CPL2SPL_TrgPropertyCallPlace_strategy = st.builds(
    jointPackage_CPL2SPL_TrgPropertyCallPlace,
    propName=
        safe_text
)
jointPackage_CPL2SPL_TrgVariable_strategy = st.builds(
    jointPackage_CPL2SPL_TrgVariable,
)
TrgSelectMember_strategy = st.builds(
    TrgSelectMember,
)
jointPackage_CPL2SPL_TrgSelectCase_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSelectCase,
)
TrgMessageField_strategy = st.builds(
    TrgMessageField,
)
jointPackage_CPL2SPL_TrgHeadedMessageField_strategy = st.builds(
    jointPackage_CPL2SPL_TrgHeadedMessageField,
    headerId=
        safe_text
)
jointPackage_CPL2SPL_TrgReasonMessageField_strategy = st.builds(
    jointPackage_CPL2SPL_TrgReasonMessageField,
)
TrgFunctionCall_strategy = st.builds(
    TrgFunctionCall,
)
TrgSelectDefault_strategy = st.builds(
    TrgSelectDefault,
)
TrgSelectCase_strategy = st.builds(
    TrgSelectCase,
)
jointPackage_CPL2SPL_TrgSelectDefault_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSelectDefault,
)
TrgConstant_strategy = st.builds(
    TrgConstant,
)
jointPackage_CPL2SPL_TrgSequenceConstant_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSequenceConstant,
)
jointPackage_CPL2SPL_TrgStringConstant_strategy = st.builds(
    jointPackage_CPL2SPL_TrgStringConstant,
    value=
        safe_text
)
jointPackage_CPL2SPL_TrgResponseConstant_strategy = st.builds(
    jointPackage_CPL2SPL_TrgResponseConstant,
)
jointPackage_CPL2SPL_TrgIntegerConstant_strategy = st.builds(
    jointPackage_CPL2SPL_TrgIntegerConstant,
    value=
        st.integers()
)
jointPackage_CPL2SPL_TrgURIConstant_strategy = st.builds(
    jointPackage_CPL2SPL_TrgURIConstant,
    uri=
        safe_text
)
jointPackage_CPL2SPL_TrgBooleanConstant_strategy = st.builds(
    jointPackage_CPL2SPL_TrgBooleanConstant,
    value=
        st.booleans()
)
TrgNamedBranch_strategy = st.builds(
    TrgNamedBranch,
)
TrgWhenHeader_strategy = st.builds(
    TrgWhenHeader,
)
TrgVariable_strategy = st.builds(
    TrgVariable,
)
TrgFunctionDeclaration_strategy = st.builds(
    TrgFunctionDeclaration,
)
jointPackage_CPL2SPL_TrgLocalFunctionDeclaration_strategy = st.builds(
    jointPackage_CPL2SPL_TrgLocalFunctionDeclaration,
)
jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration_strategy = st.builds(
    jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration,
    functionLocation=
        safe_text
)
TrgPlace_strategy = st.builds(
    TrgPlace,
)
jointPackage_CPL2SPL_TrgSIPHeaderPlace_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSIPHeaderPlace,
    header=
        safe_text
)
jointPackage_CPL2SPL_TrgVariablePlace_strategy = st.builds(
    jointPackage_CPL2SPL_TrgVariablePlace,
)
TrgExpression_strategy = st.builds(
    TrgExpression,
)
jointPackage_CPL2SPL_TrgPlace_strategy = st.builds(
    jointPackage_CPL2SPL_TrgPlace,
)
jointPackage_CPL2SPL_TrgBlockExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgBlockExp,
)
jointPackage_CPL2SPL_TrgOperatorExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgOperatorExp,
    opName=
        safe_text
)
jointPackage_CPL2SPL_TrgPopExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgPopExp,
)
jointPackage_CPL2SPL_TrgBODYExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgBODYExp,
)
jointPackage_CPL2SPL_TrgReasonExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgReasonExp,
)
jointPackage_CPL2SPL_TrgForwardExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgForwardExp,
    isParallel=
        st.booleans()
)
jointPackage_CPL2SPL_TrgWithExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgWithExp,
)
jointPackage_CPL2SPL_TrgFunctionCallExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgFunctionCallExp,
)
jointPackage_CPL2SPL_TrgConstantExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgConstantExp,
)
jointPackage_CPL2SPL_TrgRequestURIExp_strategy = st.builds(
    jointPackage_CPL2SPL_TrgRequestURIExp,
)
TrgArgument_strategy = st.builds(
    TrgArgument,
)
TrgMethodName_strategy = st.builds(
    TrgMethodName,
)
TrgMethod_strategy = st.builds(
    TrgMethod,
)
jointPackage_CPL2SPL_TrgControlMethodName_strategy = st.builds(
    jointPackage_CPL2SPL_TrgControlMethodName,
    name=
        safe_text
)
jointPackage_CPL2SPL_TrgSIPMethodName_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSIPMethodName,
    name=
        safe_text
)
TrgVariableDeclaration_strategy = st.builds(
    TrgVariableDeclaration,
)
jointPackage_CPL2SPL_TrgWhenHeader_strategy = st.builds(
    jointPackage_CPL2SPL_TrgWhenHeader,
    headerId=
        safe_text
)
jointPackage_CPL2SPL_TrgArgument_strategy = st.builds(
    jointPackage_CPL2SPL_TrgArgument,
)
TrgBranch_strategy = st.builds(
    TrgBranch,
)
jointPackage_CPL2SPL_TrgNamedBranch_strategy = st.builds(
    jointPackage_CPL2SPL_TrgNamedBranch,
    name=
        safe_text
)
jointPackage_CPL2SPL_TrgDefaultBranch_strategy = st.builds(
    jointPackage_CPL2SPL_TrgDefaultBranch,
)
TrgStatement_strategy = st.builds(
    TrgStatement,
)
jointPackage_CPL2SPL_TrgReturnStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgReturnStat,
)
jointPackage_CPL2SPL_TrgSelectStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSelectStat,
)
jointPackage_CPL2SPL_TrgFunctionCallStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgFunctionCallStat,
)
jointPackage_CPL2SPL_TrgDeclarationStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgDeclarationStat,
)
jointPackage_CPL2SPL_TrgPushStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgPushStat,
)
jointPackage_CPL2SPL_TrgBreakStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgBreakStat,
)
jointPackage_CPL2SPL_TrgWhenStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgWhenStat,
)
jointPackage_CPL2SPL_TrgSetStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSetStat,
)
jointPackage_CPL2SPL_TrgForeachStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgForeachStat,
    iteratorName=
        safe_text
)
jointPackage_CPL2SPL_TrgContinueStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgContinueStat,
)
jointPackage_CPL2SPL_TrgIfStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgIfStat,
)
jointPackage_CPL2SPL_TrgCompoundStat_strategy = st.builds(
    jointPackage_CPL2SPL_TrgCompoundStat,
)
TrgService_strategy = st.builds(
    TrgService,
)
TrgLocatedElement_strategy = st.builds(
    TrgLocatedElement,
)
jointPackage_CPL2SPL_TrgResponse_strategy = st.builds(
    jointPackage_CPL2SPL_TrgResponse,
)
jointPackage_CPL2SPL_TrgSelectMember_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSelectMember,
)
jointPackage_CPL2SPL_TrgConstant_strategy = st.builds(
    jointPackage_CPL2SPL_TrgConstant,
)
jointPackage_CPL2SPL_TrgExpression_strategy = st.builds(
    jointPackage_CPL2SPL_TrgExpression,
)
jointPackage_CPL2SPL_TrgSession_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSession,
)
jointPackage_CPL2SPL_TrgStructureProperty_strategy = st.builds(
    jointPackage_CPL2SPL_TrgStructureProperty,
    name=
        safe_text
)
jointPackage_CPL2SPL_TrgTypeExpression_strategy = st.builds(
    jointPackage_CPL2SPL_TrgTypeExpression,
)
jointPackage_CPL2SPL_TrgStatement_strategy = st.builds(
    jointPackage_CPL2SPL_TrgStatement,
)
jointPackage_CPL2SPL_TrgMessageField_strategy = st.builds(
    jointPackage_CPL2SPL_TrgMessageField,
)
jointPackage_CPL2SPL_TrgMethodName_strategy = st.builds(
    jointPackage_CPL2SPL_TrgMethodName,
)
jointPackage_CPL2SPL_TrgBranch_strategy = st.builds(
    jointPackage_CPL2SPL_TrgBranch,
)
jointPackage_CPL2SPL_TrgFunctionCall_strategy = st.builds(
    jointPackage_CPL2SPL_TrgFunctionCall,
)
jointPackage_CPL2SPL_TrgDeclaration_strategy = st.builds(
    jointPackage_CPL2SPL_TrgDeclaration,
    name=
        safe_text
)
jointPackage_CPL2SPL_TrgProgram_strategy = st.builds(
    jointPackage_CPL2SPL_TrgProgram,
)
SrcAction_strategy = st.builds(
    SrcAction,
)
jointPackage_CPL2SPL_SrcSignallingAction_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSignallingAction,
)
SrcOtherwise_strategy = st.builds(
    SrcOtherwise,
)
SrcNotPresent_strategy = st.builds(
    SrcNotPresent,
)
TrgSession_strategy = st.builds(
    TrgSession,
)
jointPackage_CPL2SPL_TrgEvent_strategy = st.builds(
    jointPackage_CPL2SPL_TrgEvent,
    eventId=
        safe_text
)
jointPackage_CPL2SPL_TrgRegistration_strategy = st.builds(
    jointPackage_CPL2SPL_TrgRegistration,
)
jointPackage_CPL2SPL_TrgMethod_strategy = st.builds(
    jointPackage_CPL2SPL_TrgMethod,
    direction=
        safe_text
)
jointPackage_CPL2SPL_TrgDialog_strategy = st.builds(
    jointPackage_CPL2SPL_TrgDialog,
)
TrgDeclaration_strategy = st.builds(
    TrgDeclaration,
)
jointPackage_CPL2SPL_TrgVariableDeclaration_strategy = st.builds(
    jointPackage_CPL2SPL_TrgVariableDeclaration,
)
jointPackage_CPL2SPL_TrgStructureDeclaration_strategy = st.builds(
    jointPackage_CPL2SPL_TrgStructureDeclaration,
)
jointPackage_CPL2SPL_TrgFunctionDeclaration_strategy = st.builds(
    jointPackage_CPL2SPL_TrgFunctionDeclaration,
)
jointPackage_CPL2SPL_TrgService_strategy = st.builds(
    jointPackage_CPL2SPL_TrgService,
    name=
        safe_text
)
jointPackage_CPL2SPL_TrgLocatedElement_strategy = st.builds(
    jointPackage_CPL2SPL_TrgLocatedElement,
    location=
        safe_text,
    commentsBefore=
        safe_text,
    commentsAfter=
        safe_text
)
TrgErrorResponse_strategy = st.builds(
    TrgErrorResponse,
)
jointPackage_CPL2SPL_TrgRedirectionErrorResponse_strategy = st.builds(
    jointPackage_CPL2SPL_TrgRedirectionErrorResponse,
    errorKind=
        safe_text
)
jointPackage_CPL2SPL_TrgGlobalErrorResponse_strategy = st.builds(
    jointPackage_CPL2SPL_TrgGlobalErrorResponse,
    errorKind=
        safe_text
)
jointPackage_CPL2SPL_TrgServerErrorResponse_strategy = st.builds(
    jointPackage_CPL2SPL_TrgServerErrorResponse,
    errorKind=
        safe_text
)
jointPackage_CPL2SPL_TrgClientErrorResponse_strategy = st.builds(
    jointPackage_CPL2SPL_TrgClientErrorResponse,
    errorKind=
        safe_text
)
TrgTypeExpression_strategy = st.builds(
    TrgTypeExpression,
)
jointPackage_CPL2SPL_TrgDefinedType_strategy = st.builds(
    jointPackage_CPL2SPL_TrgDefinedType,
    typeName=
        safe_text
)
jointPackage_CPL2SPL_TrgSimpleType_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSimpleType,
    type=
        safe_text
)
jointPackage_CPL2SPL_TrgSequenceType_strategy = st.builds(
    jointPackage_CPL2SPL_TrgSequenceType,
    size=
        st.integers(),
    type=
        safe_text,
    modifier=
        safe_text
)
SrcNode_strategy = st.builds(
    SrcNode,
)
jointPackage_CPL2SPL_SrcAction_strategy = st.builds(
    jointPackage_CPL2SPL_SrcAction,
)
jointPackage_CPL2SPL_SrcSwitch_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSwitch,
)
jointPackage_CPL2SPL_SrcSubCall_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSubCall,
    ref=
        safe_text
)
jointPackage_CPL2SPL_SrcElement_strategy = st.builds(
    jointPackage_CPL2SPL_SrcElement,
)
SrcDefault_strategy = st.builds(
    SrcDefault,
)
SrcFailure_strategy = st.builds(
    SrcFailure,
)
SrcRedirection_strategy = st.builds(
    SrcRedirection,
)
SrcNoAnswer_strategy = st.builds(
    SrcNoAnswer,
)
SrcBusy_strategy = st.builds(
    SrcBusy,
)
SrcSignallingAction_strategy = st.builds(
    SrcSignallingAction,
)
jointPackage_CPL2SPL_SrcReject_strategy = st.builds(
    jointPackage_CPL2SPL_SrcReject,
    status=
        safe_text,
    reason=
        safe_text
)
jointPackage_CPL2SPL_SrcRedirect_strategy = st.builds(
    jointPackage_CPL2SPL_SrcRedirect,
    permanent=
        safe_text
)
jointPackage_CPL2SPL_SrcProxy_strategy = st.builds(
    jointPackage_CPL2SPL_SrcProxy,
    recurse=
        safe_text,
    timeout=
        safe_text,
    ordering=
        safe_text
)
SrcSwitchedPriority_strategy = st.builds(
    SrcSwitchedPriority,
)
SrcNodeContainer_strategy = st.builds(
    SrcNodeContainer,
)
jointPackage_CPL2SPL_SrcBusy_strategy = st.builds(
    jointPackage_CPL2SPL_SrcBusy,
)
jointPackage_CPL2SPL_SrcOtherwise_strategy = st.builds(
    jointPackage_CPL2SPL_SrcOtherwise,
)
jointPackage_CPL2SPL_SrcSwitchedLanguage_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSwitchedLanguage,
    matches=
        safe_text
)
jointPackage_CPL2SPL_SrcSwitchedAddress_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSwitchedAddress,
    is_=
        safe_text,
    contains=
        safe_text,
    subDomainOf=
        safe_text
)
jointPackage_CPL2SPL_SrcIncoming_strategy = st.builds(
    jointPackage_CPL2SPL_SrcIncoming,
)
jointPackage_CPL2SPL_SrcFailure_strategy = st.builds(
    jointPackage_CPL2SPL_SrcFailure,
)
jointPackage_CPL2SPL_SrcNoAnswer_strategy = st.builds(
    jointPackage_CPL2SPL_SrcNoAnswer,
)
jointPackage_CPL2SPL_SrcSwitchedTime_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSwitchedTime,
    dtend=
        safe_text,
    freq=
        safe_text,
    byHour=
        safe_text,
    interval=
        safe_text,
    byDay=
        safe_text,
    bySetPos=
        safe_text,
    dtstart=
        safe_text,
    byMinute=
        safe_text,
    byWeekNo=
        safe_text,
    byMonth=
        safe_text,
    bySecond=
        safe_text,
    duration=
        safe_text,
    byMonthDay=
        safe_text,
    until=
        safe_text,
    wkst=
        safe_text,
    count=
        safe_text,
    byYearDay=
        safe_text
)
jointPackage_CPL2SPL_SrcSwitchedString_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSwitchedString,
    is_=
        safe_text,
    contains=
        safe_text
)
jointPackage_CPL2SPL_SrcRedirection_strategy = st.builds(
    jointPackage_CPL2SPL_SrcRedirection,
)
jointPackage_CPL2SPL_SrcNotPresent_strategy = st.builds(
    jointPackage_CPL2SPL_SrcNotPresent,
)
jointPackage_CPL2SPL_SrcOutgoing_strategy = st.builds(
    jointPackage_CPL2SPL_SrcOutgoing,
)
jointPackage_CPL2SPL_SrcDefault_strategy = st.builds(
    jointPackage_CPL2SPL_SrcDefault,
)
jointPackage_CPL2SPL_SrcSwitchedPriority_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSwitchedPriority,
    equal=
        safe_text,
    greater=
        safe_text,
    less=
        safe_text
)
jointPackage_CPL2SPL_SrcLocation_strategy = st.builds(
    jointPackage_CPL2SPL_SrcLocation,
    url=
        safe_text,
    clear=
        safe_text,
    priority=
        safe_text
)
jointPackage_CPL2SPL_SrcSubAction_strategy = st.builds(
    jointPackage_CPL2SPL_SrcSubAction,
    id=
        safe_text
)
SrcIncoming_strategy = st.builds(
    SrcIncoming,
)
SrcOutgoing_strategy = st.builds(
    SrcOutgoing,
)
SrcSubAction_strategy = st.builds(
    SrcSubAction,
)
SrcElement_strategy = st.builds(
    SrcElement,
)
jointPackage_CPL2SPL_SrcCPL_strategy = st.builds(
    jointPackage_CPL2SPL_SrcCPL,
)
jointPackage_CPL2SPL_SrcNode_strategy = st.builds(
    jointPackage_CPL2SPL_SrcNode,
)
jointPackage_CPL2SPL_SrcNodeContainer_strategy = st.builds(
    jointPackage_CPL2SPL_SrcNodeContainer,
)
jointPackage_CPL2SPL_SrcCPLModel_strategy = st.builds(
    jointPackage_CPL2SPL_SrcCPLModel,
)
TrgServerErrorResponse_strategy = st.builds(
    TrgServerErrorResponse,
)
SrcReject_strategy = st.builds(
    SrcReject,
)
jointPackage_CPL2SPL_JointMM_strategy = st.builds(
    jointPackage_CPL2SPL_JointMM,
)
SrcSwitchedTime_strategy = st.builds(
    SrcSwitchedTime,
)
SrcSwitchedLanguage_strategy = st.builds(
    SrcSwitchedLanguage,
)
SrcSwitchedString_strategy = st.builds(
    SrcSwitchedString,
)
SrcSwitchedAddress_strategy = st.builds(
    SrcSwitchedAddress,
)
SrcSwitch_strategy = st.builds(
    SrcSwitch,
)
jointPackage_CPL2SPL_SrcLanguageSwitch_strategy = st.builds(
    jointPackage_CPL2SPL_SrcLanguageSwitch,
)
jointPackage_CPL2SPL_SrcTimeSwitch_strategy = st.builds(
    jointPackage_CPL2SPL_SrcTimeSwitch,
    tzid=
        safe_text,
    tzurl=
        safe_text
)
jointPackage_CPL2SPL_SrcStringSwitch_strategy = st.builds(
    jointPackage_CPL2SPL_SrcStringSwitch,
    field=
        safe_text
)
jointPackage_CPL2SPL_SrcPrioritySwitch_strategy = st.builds(
    jointPackage_CPL2SPL_SrcPrioritySwitch,
)
jointPackage_CPL2SPL_SrcAddressSwitch_strategy = st.builds(
    jointPackage_CPL2SPL_SrcAddressSwitch,
    subField=
        safe_text,
    field=
        safe_text
)

@given(instance=TrgResponse_strategy)
@settings(max_examples=50)
def test_trgresponse_instantiation(instance):
    assert isinstance(instance, TrgResponse)

@given(instance=jointPackage_CPL2SPL_TrgErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgerrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgErrorResponse)

@given(instance=jointPackage_CPL2SPL_TrgSuccessResponse_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgsuccessresponse_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSuccessResponse)



@given(instance=jointPackage_CPL2SPL_TrgSuccessResponse_strategy)
def test_jointpackage_cpl2spl_trgsuccessresponse_successKind_setter(instance):
    original = instance.successKind
    instance.successKind = original
    assert instance.successKind == original

@given(instance=TrgVariablePlace_strategy)
@settings(max_examples=50)
def test_trgvariableplace_instantiation(instance):
    assert isinstance(instance, TrgVariablePlace)

@given(instance=jointPackage_CPL2SPL_TrgPropertyCallPlace_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgpropertycallplace_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgPropertyCallPlace)



@given(instance=jointPackage_CPL2SPL_TrgPropertyCallPlace_strategy)
def test_jointpackage_cpl2spl_trgpropertycallplace_propName_setter(instance):
    original = instance.propName
    instance.propName = original
    assert instance.propName == original

@given(instance=jointPackage_CPL2SPL_TrgVariable_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgvariable_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgVariable)

@given(instance=TrgSelectMember_strategy)
@settings(max_examples=50)
def test_trgselectmember_instantiation(instance):
    assert isinstance(instance, TrgSelectMember)

@given(instance=jointPackage_CPL2SPL_TrgSelectCase_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgselectcase_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSelectCase)

@given(instance=TrgMessageField_strategy)
@settings(max_examples=50)
def test_trgmessagefield_instantiation(instance):
    assert isinstance(instance, TrgMessageField)

@given(instance=jointPackage_CPL2SPL_TrgHeadedMessageField_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgheadedmessagefield_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgHeadedMessageField)



@given(instance=jointPackage_CPL2SPL_TrgHeadedMessageField_strategy)
def test_jointpackage_cpl2spl_trgheadedmessagefield_headerId_setter(instance):
    original = instance.headerId
    instance.headerId = original
    assert instance.headerId == original

@given(instance=jointPackage_CPL2SPL_TrgReasonMessageField_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgreasonmessagefield_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgReasonMessageField)

@given(instance=TrgFunctionCall_strategy)
@settings(max_examples=50)
def test_trgfunctioncall_instantiation(instance):
    assert isinstance(instance, TrgFunctionCall)

@given(instance=TrgSelectDefault_strategy)
@settings(max_examples=50)
def test_trgselectdefault_instantiation(instance):
    assert isinstance(instance, TrgSelectDefault)

@given(instance=TrgSelectCase_strategy)
@settings(max_examples=50)
def test_trgselectcase_instantiation(instance):
    assert isinstance(instance, TrgSelectCase)

@given(instance=jointPackage_CPL2SPL_TrgSelectDefault_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgselectdefault_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSelectDefault)

@given(instance=TrgConstant_strategy)
@settings(max_examples=50)
def test_trgconstant_instantiation(instance):
    assert isinstance(instance, TrgConstant)

@given(instance=jointPackage_CPL2SPL_TrgSequenceConstant_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgsequenceconstant_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSequenceConstant)

@given(instance=jointPackage_CPL2SPL_TrgStringConstant_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgstringconstant_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgStringConstant)



@given(instance=jointPackage_CPL2SPL_TrgStringConstant_strategy)
def test_jointpackage_cpl2spl_trgstringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage_CPL2SPL_TrgResponseConstant_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgresponseconstant_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgResponseConstant)

@given(instance=jointPackage_CPL2SPL_TrgIntegerConstant_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgintegerconstant_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgIntegerConstant)



@given(instance=jointPackage_CPL2SPL_TrgIntegerConstant_strategy)
def test_jointpackage_cpl2spl_trgintegerconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage_CPL2SPL_TrgURIConstant_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trguriconstant_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgURIConstant)



@given(instance=jointPackage_CPL2SPL_TrgURIConstant_strategy)
def test_jointpackage_cpl2spl_trguriconstant_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=jointPackage_CPL2SPL_TrgBooleanConstant_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgbooleanconstant_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgBooleanConstant)



@given(instance=jointPackage_CPL2SPL_TrgBooleanConstant_strategy)
def test_jointpackage_cpl2spl_trgbooleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TrgNamedBranch_strategy)
@settings(max_examples=50)
def test_trgnamedbranch_instantiation(instance):
    assert isinstance(instance, TrgNamedBranch)

@given(instance=TrgWhenHeader_strategy)
@settings(max_examples=50)
def test_trgwhenheader_instantiation(instance):
    assert isinstance(instance, TrgWhenHeader)

@given(instance=TrgVariable_strategy)
@settings(max_examples=50)
def test_trgvariable_instantiation(instance):
    assert isinstance(instance, TrgVariable)

@given(instance=TrgFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_trgfunctiondeclaration_instantiation(instance):
    assert isinstance(instance, TrgFunctionDeclaration)

@given(instance=jointPackage_CPL2SPL_TrgLocalFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trglocalfunctiondeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgLocalFunctionDeclaration)

@given(instance=jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgremotefunctiondeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration)



@given(instance=jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration_strategy)
def test_jointpackage_cpl2spl_trgremotefunctiondeclaration_functionLocation_setter(instance):
    original = instance.functionLocation
    instance.functionLocation = original
    assert instance.functionLocation == original

@given(instance=TrgPlace_strategy)
@settings(max_examples=50)
def test_trgplace_instantiation(instance):
    assert isinstance(instance, TrgPlace)

@given(instance=jointPackage_CPL2SPL_TrgSIPHeaderPlace_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgsipheaderplace_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSIPHeaderPlace)



@given(instance=jointPackage_CPL2SPL_TrgSIPHeaderPlace_strategy)
def test_jointpackage_cpl2spl_trgsipheaderplace_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original

@given(instance=jointPackage_CPL2SPL_TrgVariablePlace_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgvariableplace_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgVariablePlace)

@given(instance=TrgExpression_strategy)
@settings(max_examples=50)
def test_trgexpression_instantiation(instance):
    assert isinstance(instance, TrgExpression)

@given(instance=jointPackage_CPL2SPL_TrgPlace_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgplace_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgPlace)

@given(instance=jointPackage_CPL2SPL_TrgBlockExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgblockexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgBlockExp)

@given(instance=jointPackage_CPL2SPL_TrgOperatorExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgoperatorexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgOperatorExp)



@given(instance=jointPackage_CPL2SPL_TrgOperatorExp_strategy)
def test_jointpackage_cpl2spl_trgoperatorexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=jointPackage_CPL2SPL_TrgPopExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgpopexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgPopExp)

@given(instance=jointPackage_CPL2SPL_TrgBODYExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgbodyexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgBODYExp)

@given(instance=jointPackage_CPL2SPL_TrgReasonExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgreasonexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgReasonExp)

@given(instance=jointPackage_CPL2SPL_TrgForwardExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgforwardexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgForwardExp)



@given(instance=jointPackage_CPL2SPL_TrgForwardExp_strategy)
def test_jointpackage_cpl2spl_trgforwardexp_isParallel_setter(instance):
    original = instance.isParallel
    instance.isParallel = original
    assert instance.isParallel == original

@given(instance=jointPackage_CPL2SPL_TrgWithExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgwithexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgWithExp)

@given(instance=jointPackage_CPL2SPL_TrgFunctionCallExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgfunctioncallexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgFunctionCallExp)

@given(instance=jointPackage_CPL2SPL_TrgConstantExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgconstantexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgConstantExp)

@given(instance=jointPackage_CPL2SPL_TrgRequestURIExp_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgrequesturiexp_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgRequestURIExp)

@given(instance=TrgArgument_strategy)
@settings(max_examples=50)
def test_trgargument_instantiation(instance):
    assert isinstance(instance, TrgArgument)

@given(instance=TrgMethodName_strategy)
@settings(max_examples=50)
def test_trgmethodname_instantiation(instance):
    assert isinstance(instance, TrgMethodName)

@given(instance=TrgMethod_strategy)
@settings(max_examples=50)
def test_trgmethod_instantiation(instance):
    assert isinstance(instance, TrgMethod)

@given(instance=jointPackage_CPL2SPL_TrgControlMethodName_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgcontrolmethodname_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgControlMethodName)



@given(instance=jointPackage_CPL2SPL_TrgControlMethodName_strategy)
def test_jointpackage_cpl2spl_trgcontrolmethodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_CPL2SPL_TrgSIPMethodName_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgsipmethodname_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSIPMethodName)



@given(instance=jointPackage_CPL2SPL_TrgSIPMethodName_strategy)
def test_jointpackage_cpl2spl_trgsipmethodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TrgVariableDeclaration_strategy)
@settings(max_examples=50)
def test_trgvariabledeclaration_instantiation(instance):
    assert isinstance(instance, TrgVariableDeclaration)

@given(instance=jointPackage_CPL2SPL_TrgWhenHeader_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgwhenheader_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgWhenHeader)



@given(instance=jointPackage_CPL2SPL_TrgWhenHeader_strategy)
def test_jointpackage_cpl2spl_trgwhenheader_headerId_setter(instance):
    original = instance.headerId
    instance.headerId = original
    assert instance.headerId == original

@given(instance=jointPackage_CPL2SPL_TrgArgument_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgargument_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgArgument)

@given(instance=TrgBranch_strategy)
@settings(max_examples=50)
def test_trgbranch_instantiation(instance):
    assert isinstance(instance, TrgBranch)

@given(instance=jointPackage_CPL2SPL_TrgNamedBranch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgnamedbranch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgNamedBranch)



@given(instance=jointPackage_CPL2SPL_TrgNamedBranch_strategy)
def test_jointpackage_cpl2spl_trgnamedbranch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_CPL2SPL_TrgDefaultBranch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgdefaultbranch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgDefaultBranch)

@given(instance=TrgStatement_strategy)
@settings(max_examples=50)
def test_trgstatement_instantiation(instance):
    assert isinstance(instance, TrgStatement)

@given(instance=jointPackage_CPL2SPL_TrgReturnStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgreturnstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgReturnStat)

@given(instance=jointPackage_CPL2SPL_TrgSelectStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgselectstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSelectStat)

@given(instance=jointPackage_CPL2SPL_TrgFunctionCallStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgfunctioncallstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgFunctionCallStat)

@given(instance=jointPackage_CPL2SPL_TrgDeclarationStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgdeclarationstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgDeclarationStat)

@given(instance=jointPackage_CPL2SPL_TrgPushStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgpushstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgPushStat)

@given(instance=jointPackage_CPL2SPL_TrgBreakStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgbreakstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgBreakStat)

@given(instance=jointPackage_CPL2SPL_TrgWhenStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgwhenstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgWhenStat)

@given(instance=jointPackage_CPL2SPL_TrgSetStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgsetstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSetStat)

@given(instance=jointPackage_CPL2SPL_TrgForeachStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgforeachstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgForeachStat)



@given(instance=jointPackage_CPL2SPL_TrgForeachStat_strategy)
def test_jointpackage_cpl2spl_trgforeachstat_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=jointPackage_CPL2SPL_TrgContinueStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgcontinuestat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgContinueStat)

@given(instance=jointPackage_CPL2SPL_TrgIfStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgifstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgIfStat)

@given(instance=jointPackage_CPL2SPL_TrgCompoundStat_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgcompoundstat_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgCompoundStat)

@given(instance=TrgService_strategy)
@settings(max_examples=50)
def test_trgservice_instantiation(instance):
    assert isinstance(instance, TrgService)

@given(instance=TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_trglocatedelement_instantiation(instance):
    assert isinstance(instance, TrgLocatedElement)

@given(instance=jointPackage_CPL2SPL_TrgResponse_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgresponse_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgResponse)

@given(instance=jointPackage_CPL2SPL_TrgSelectMember_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgselectmember_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSelectMember)

@given(instance=jointPackage_CPL2SPL_TrgConstant_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgconstant_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgConstant)

@given(instance=jointPackage_CPL2SPL_TrgExpression_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgexpression_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgExpression)

@given(instance=jointPackage_CPL2SPL_TrgSession_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgsession_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSession)

@given(instance=jointPackage_CPL2SPL_TrgStructureProperty_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgstructureproperty_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgStructureProperty)



@given(instance=jointPackage_CPL2SPL_TrgStructureProperty_strategy)
def test_jointpackage_cpl2spl_trgstructureproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_CPL2SPL_TrgTypeExpression_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgtypeexpression_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgTypeExpression)

@given(instance=jointPackage_CPL2SPL_TrgStatement_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgstatement_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgStatement)

@given(instance=jointPackage_CPL2SPL_TrgMessageField_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgmessagefield_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgMessageField)

@given(instance=jointPackage_CPL2SPL_TrgMethodName_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgmethodname_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgMethodName)

@given(instance=jointPackage_CPL2SPL_TrgBranch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgbranch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgBranch)

@given(instance=jointPackage_CPL2SPL_TrgFunctionCall_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgfunctioncall_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgFunctionCall)

@given(instance=jointPackage_CPL2SPL_TrgDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgdeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgDeclaration)



@given(instance=jointPackage_CPL2SPL_TrgDeclaration_strategy)
def test_jointpackage_cpl2spl_trgdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_CPL2SPL_TrgProgram_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgprogram_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgProgram)

@given(instance=SrcAction_strategy)
@settings(max_examples=50)
def test_srcaction_instantiation(instance):
    assert isinstance(instance, SrcAction)

@given(instance=jointPackage_CPL2SPL_SrcSignallingAction_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcsignallingaction_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSignallingAction)

@given(instance=SrcOtherwise_strategy)
@settings(max_examples=50)
def test_srcotherwise_instantiation(instance):
    assert isinstance(instance, SrcOtherwise)

@given(instance=SrcNotPresent_strategy)
@settings(max_examples=50)
def test_srcnotpresent_instantiation(instance):
    assert isinstance(instance, SrcNotPresent)

@given(instance=TrgSession_strategy)
@settings(max_examples=50)
def test_trgsession_instantiation(instance):
    assert isinstance(instance, TrgSession)

@given(instance=jointPackage_CPL2SPL_TrgEvent_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgevent_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgEvent)



@given(instance=jointPackage_CPL2SPL_TrgEvent_strategy)
def test_jointpackage_cpl2spl_trgevent_eventId_setter(instance):
    original = instance.eventId
    instance.eventId = original
    assert instance.eventId == original

@given(instance=jointPackage_CPL2SPL_TrgRegistration_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgregistration_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgRegistration)

@given(instance=jointPackage_CPL2SPL_TrgMethod_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgmethod_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgMethod)



@given(instance=jointPackage_CPL2SPL_TrgMethod_strategy)
def test_jointpackage_cpl2spl_trgmethod_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=jointPackage_CPL2SPL_TrgDialog_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgdialog_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgDialog)

@given(instance=TrgDeclaration_strategy)
@settings(max_examples=50)
def test_trgdeclaration_instantiation(instance):
    assert isinstance(instance, TrgDeclaration)

@given(instance=jointPackage_CPL2SPL_TrgVariableDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgvariabledeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgVariableDeclaration)

@given(instance=jointPackage_CPL2SPL_TrgStructureDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgstructuredeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgStructureDeclaration)

@given(instance=jointPackage_CPL2SPL_TrgFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgfunctiondeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgFunctionDeclaration)

@given(instance=jointPackage_CPL2SPL_TrgService_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgservice_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgService)



@given(instance=jointPackage_CPL2SPL_TrgService_strategy)
def test_jointpackage_cpl2spl_trgservice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_CPL2SPL_TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trglocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgLocatedElement)



@given(instance=jointPackage_CPL2SPL_TrgLocatedElement_strategy)
def test_jointpackage_cpl2spl_trglocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=jointPackage_CPL2SPL_TrgLocatedElement_strategy)
def test_jointpackage_cpl2spl_trglocatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=jointPackage_CPL2SPL_TrgLocatedElement_strategy)
def test_jointpackage_cpl2spl_trglocatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=TrgErrorResponse_strategy)
@settings(max_examples=50)
def test_trgerrorresponse_instantiation(instance):
    assert isinstance(instance, TrgErrorResponse)

@given(instance=jointPackage_CPL2SPL_TrgRedirectionErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgredirectionerrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgRedirectionErrorResponse)



@given(instance=jointPackage_CPL2SPL_TrgRedirectionErrorResponse_strategy)
def test_jointpackage_cpl2spl_trgredirectionerrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=jointPackage_CPL2SPL_TrgGlobalErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgglobalerrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgGlobalErrorResponse)



@given(instance=jointPackage_CPL2SPL_TrgGlobalErrorResponse_strategy)
def test_jointpackage_cpl2spl_trgglobalerrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=jointPackage_CPL2SPL_TrgServerErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgservererrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgServerErrorResponse)



@given(instance=jointPackage_CPL2SPL_TrgServerErrorResponse_strategy)
def test_jointpackage_cpl2spl_trgservererrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=jointPackage_CPL2SPL_TrgClientErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgclienterrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgClientErrorResponse)



@given(instance=jointPackage_CPL2SPL_TrgClientErrorResponse_strategy)
def test_jointpackage_cpl2spl_trgclienterrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=TrgTypeExpression_strategy)
@settings(max_examples=50)
def test_trgtypeexpression_instantiation(instance):
    assert isinstance(instance, TrgTypeExpression)

@given(instance=jointPackage_CPL2SPL_TrgDefinedType_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgdefinedtype_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgDefinedType)



@given(instance=jointPackage_CPL2SPL_TrgDefinedType_strategy)
def test_jointpackage_cpl2spl_trgdefinedtype_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=jointPackage_CPL2SPL_TrgSimpleType_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgsimpletype_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSimpleType)



@given(instance=jointPackage_CPL2SPL_TrgSimpleType_strategy)
def test_jointpackage_cpl2spl_trgsimpletype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jointPackage_CPL2SPL_TrgSequenceType_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_trgsequencetype_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_TrgSequenceType)



@given(instance=jointPackage_CPL2SPL_TrgSequenceType_strategy)
def test_jointpackage_cpl2spl_trgsequencetype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=jointPackage_CPL2SPL_TrgSequenceType_strategy)
def test_jointpackage_cpl2spl_trgsequencetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=jointPackage_CPL2SPL_TrgSequenceType_strategy)
def test_jointpackage_cpl2spl_trgsequencetype_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=SrcNode_strategy)
@settings(max_examples=50)
def test_srcnode_instantiation(instance):
    assert isinstance(instance, SrcNode)

@given(instance=jointPackage_CPL2SPL_SrcAction_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcaction_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcAction)

@given(instance=jointPackage_CPL2SPL_SrcSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcswitch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSwitch)

@given(instance=jointPackage_CPL2SPL_SrcSubCall_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcsubcall_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSubCall)



@given(instance=jointPackage_CPL2SPL_SrcSubCall_strategy)
def test_jointpackage_cpl2spl_srcsubcall_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=jointPackage_CPL2SPL_SrcElement_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcelement_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcElement)

@given(instance=SrcDefault_strategy)
@settings(max_examples=50)
def test_srcdefault_instantiation(instance):
    assert isinstance(instance, SrcDefault)

@given(instance=SrcFailure_strategy)
@settings(max_examples=50)
def test_srcfailure_instantiation(instance):
    assert isinstance(instance, SrcFailure)

@given(instance=SrcRedirection_strategy)
@settings(max_examples=50)
def test_srcredirection_instantiation(instance):
    assert isinstance(instance, SrcRedirection)

@given(instance=SrcNoAnswer_strategy)
@settings(max_examples=50)
def test_srcnoanswer_instantiation(instance):
    assert isinstance(instance, SrcNoAnswer)

@given(instance=SrcBusy_strategy)
@settings(max_examples=50)
def test_srcbusy_instantiation(instance):
    assert isinstance(instance, SrcBusy)

@given(instance=SrcSignallingAction_strategy)
@settings(max_examples=50)
def test_srcsignallingaction_instantiation(instance):
    assert isinstance(instance, SrcSignallingAction)

@given(instance=jointPackage_CPL2SPL_SrcReject_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcreject_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcReject)



@given(instance=jointPackage_CPL2SPL_SrcReject_strategy)
def test_jointpackage_cpl2spl_srcreject_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=jointPackage_CPL2SPL_SrcReject_strategy)
def test_jointpackage_cpl2spl_srcreject_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original

@given(instance=jointPackage_CPL2SPL_SrcRedirect_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcredirect_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcRedirect)



@given(instance=jointPackage_CPL2SPL_SrcRedirect_strategy)
def test_jointpackage_cpl2spl_srcredirect_permanent_setter(instance):
    original = instance.permanent
    instance.permanent = original
    assert instance.permanent == original

@given(instance=jointPackage_CPL2SPL_SrcProxy_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcproxy_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcProxy)



@given(instance=jointPackage_CPL2SPL_SrcProxy_strategy)
def test_jointpackage_cpl2spl_srcproxy_recurse_setter(instance):
    original = instance.recurse
    instance.recurse = original
    assert instance.recurse == original



@given(instance=jointPackage_CPL2SPL_SrcProxy_strategy)
def test_jointpackage_cpl2spl_srcproxy_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original



@given(instance=jointPackage_CPL2SPL_SrcProxy_strategy)
def test_jointpackage_cpl2spl_srcproxy_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=SrcSwitchedPriority_strategy)
@settings(max_examples=50)
def test_srcswitchedpriority_instantiation(instance):
    assert isinstance(instance, SrcSwitchedPriority)

@given(instance=SrcNodeContainer_strategy)
@settings(max_examples=50)
def test_srcnodecontainer_instantiation(instance):
    assert isinstance(instance, SrcNodeContainer)

@given(instance=jointPackage_CPL2SPL_SrcBusy_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcbusy_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcBusy)

@given(instance=jointPackage_CPL2SPL_SrcOtherwise_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcotherwise_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcOtherwise)

@given(instance=jointPackage_CPL2SPL_SrcSwitchedLanguage_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcswitchedlanguage_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSwitchedLanguage)



@given(instance=jointPackage_CPL2SPL_SrcSwitchedLanguage_strategy)
def test_jointpackage_cpl2spl_srcswitchedlanguage_matches_setter(instance):
    original = instance.matches
    instance.matches = original
    assert instance.matches == original

@given(instance=jointPackage_CPL2SPL_SrcSwitchedAddress_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcswitchedaddress_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSwitchedAddress)



@given(instance=jointPackage_CPL2SPL_SrcSwitchedAddress_strategy)
def test_jointpackage_cpl2spl_srcswitchedaddress_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedAddress_strategy)
def test_jointpackage_cpl2spl_srcswitchedaddress_contains_setter(instance):
    original = instance.contains
    instance.contains = original
    assert instance.contains == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedAddress_strategy)
def test_jointpackage_cpl2spl_srcswitchedaddress_subDomainOf_setter(instance):
    original = instance.subDomainOf
    instance.subDomainOf = original
    assert instance.subDomainOf == original

@given(instance=jointPackage_CPL2SPL_SrcIncoming_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcincoming_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcIncoming)

@given(instance=jointPackage_CPL2SPL_SrcFailure_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcfailure_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcFailure)

@given(instance=jointPackage_CPL2SPL_SrcNoAnswer_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcnoanswer_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcNoAnswer)

@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcswitchedtime_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSwitchedTime)



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_dtend_setter(instance):
    original = instance.dtend
    instance.dtend = original
    assert instance.dtend == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_freq_setter(instance):
    original = instance.freq
    instance.freq = original
    assert instance.freq == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_byHour_setter(instance):
    original = instance.byHour
    instance.byHour = original
    assert instance.byHour == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_interval_setter(instance):
    original = instance.interval
    instance.interval = original
    assert instance.interval == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_byDay_setter(instance):
    original = instance.byDay
    instance.byDay = original
    assert instance.byDay == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_bySetPos_setter(instance):
    original = instance.bySetPos
    instance.bySetPos = original
    assert instance.bySetPos == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_dtstart_setter(instance):
    original = instance.dtstart
    instance.dtstart = original
    assert instance.dtstart == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_byMinute_setter(instance):
    original = instance.byMinute
    instance.byMinute = original
    assert instance.byMinute == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_byWeekNo_setter(instance):
    original = instance.byWeekNo
    instance.byWeekNo = original
    assert instance.byWeekNo == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_byMonth_setter(instance):
    original = instance.byMonth
    instance.byMonth = original
    assert instance.byMonth == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_bySecond_setter(instance):
    original = instance.bySecond
    instance.bySecond = original
    assert instance.bySecond == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_byMonthDay_setter(instance):
    original = instance.byMonthDay
    instance.byMonthDay = original
    assert instance.byMonthDay == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_until_setter(instance):
    original = instance.until
    instance.until = original
    assert instance.until == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_wkst_setter(instance):
    original = instance.wkst
    instance.wkst = original
    assert instance.wkst == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedTime_strategy)
def test_jointpackage_cpl2spl_srcswitchedtime_byYearDay_setter(instance):
    original = instance.byYearDay
    instance.byYearDay = original
    assert instance.byYearDay == original

@given(instance=jointPackage_CPL2SPL_SrcSwitchedString_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcswitchedstring_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSwitchedString)



@given(instance=jointPackage_CPL2SPL_SrcSwitchedString_strategy)
def test_jointpackage_cpl2spl_srcswitchedstring_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedString_strategy)
def test_jointpackage_cpl2spl_srcswitchedstring_contains_setter(instance):
    original = instance.contains
    instance.contains = original
    assert instance.contains == original

@given(instance=jointPackage_CPL2SPL_SrcRedirection_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcredirection_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcRedirection)

@given(instance=jointPackage_CPL2SPL_SrcNotPresent_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcnotpresent_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcNotPresent)

@given(instance=jointPackage_CPL2SPL_SrcOutgoing_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcoutgoing_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcOutgoing)

@given(instance=jointPackage_CPL2SPL_SrcDefault_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcdefault_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcDefault)

@given(instance=jointPackage_CPL2SPL_SrcSwitchedPriority_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcswitchedpriority_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSwitchedPriority)



@given(instance=jointPackage_CPL2SPL_SrcSwitchedPriority_strategy)
def test_jointpackage_cpl2spl_srcswitchedpriority_equal_setter(instance):
    original = instance.equal
    instance.equal = original
    assert instance.equal == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedPriority_strategy)
def test_jointpackage_cpl2spl_srcswitchedpriority_greater_setter(instance):
    original = instance.greater
    instance.greater = original
    assert instance.greater == original



@given(instance=jointPackage_CPL2SPL_SrcSwitchedPriority_strategy)
def test_jointpackage_cpl2spl_srcswitchedpriority_less_setter(instance):
    original = instance.less
    instance.less = original
    assert instance.less == original

@given(instance=jointPackage_CPL2SPL_SrcLocation_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srclocation_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcLocation)



@given(instance=jointPackage_CPL2SPL_SrcLocation_strategy)
def test_jointpackage_cpl2spl_srclocation_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=jointPackage_CPL2SPL_SrcLocation_strategy)
def test_jointpackage_cpl2spl_srclocation_clear_setter(instance):
    original = instance.clear
    instance.clear = original
    assert instance.clear == original



@given(instance=jointPackage_CPL2SPL_SrcLocation_strategy)
def test_jointpackage_cpl2spl_srclocation_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=jointPackage_CPL2SPL_SrcSubAction_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcsubaction_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcSubAction)



@given(instance=jointPackage_CPL2SPL_SrcSubAction_strategy)
def test_jointpackage_cpl2spl_srcsubaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SrcIncoming_strategy)
@settings(max_examples=50)
def test_srcincoming_instantiation(instance):
    assert isinstance(instance, SrcIncoming)

@given(instance=SrcOutgoing_strategy)
@settings(max_examples=50)
def test_srcoutgoing_instantiation(instance):
    assert isinstance(instance, SrcOutgoing)

@given(instance=SrcSubAction_strategy)
@settings(max_examples=50)
def test_srcsubaction_instantiation(instance):
    assert isinstance(instance, SrcSubAction)

@given(instance=SrcElement_strategy)
@settings(max_examples=50)
def test_srcelement_instantiation(instance):
    assert isinstance(instance, SrcElement)

@given(instance=jointPackage_CPL2SPL_SrcCPL_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srccpl_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcCPL)

@given(instance=jointPackage_CPL2SPL_SrcNode_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcnode_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcNode)

@given(instance=jointPackage_CPL2SPL_SrcNodeContainer_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcnodecontainer_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcNodeContainer)

@given(instance=jointPackage_CPL2SPL_SrcCPLModel_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srccplmodel_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcCPLModel)

@given(instance=TrgServerErrorResponse_strategy)
@settings(max_examples=50)
def test_trgservererrorresponse_instantiation(instance):
    assert isinstance(instance, TrgServerErrorResponse)

@given(instance=SrcReject_strategy)
@settings(max_examples=50)
def test_srcreject_instantiation(instance):
    assert isinstance(instance, SrcReject)

@given(instance=jointPackage_CPL2SPL_JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_JointMM)

@given(instance=SrcSwitchedTime_strategy)
@settings(max_examples=50)
def test_srcswitchedtime_instantiation(instance):
    assert isinstance(instance, SrcSwitchedTime)

@given(instance=SrcSwitchedLanguage_strategy)
@settings(max_examples=50)
def test_srcswitchedlanguage_instantiation(instance):
    assert isinstance(instance, SrcSwitchedLanguage)

@given(instance=SrcSwitchedString_strategy)
@settings(max_examples=50)
def test_srcswitchedstring_instantiation(instance):
    assert isinstance(instance, SrcSwitchedString)

@given(instance=SrcSwitchedAddress_strategy)
@settings(max_examples=50)
def test_srcswitchedaddress_instantiation(instance):
    assert isinstance(instance, SrcSwitchedAddress)

@given(instance=SrcSwitch_strategy)
@settings(max_examples=50)
def test_srcswitch_instantiation(instance):
    assert isinstance(instance, SrcSwitch)

@given(instance=jointPackage_CPL2SPL_SrcLanguageSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srclanguageswitch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcLanguageSwitch)

@given(instance=jointPackage_CPL2SPL_SrcTimeSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srctimeswitch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcTimeSwitch)



@given(instance=jointPackage_CPL2SPL_SrcTimeSwitch_strategy)
def test_jointpackage_cpl2spl_srctimeswitch_tzid_setter(instance):
    original = instance.tzid
    instance.tzid = original
    assert instance.tzid == original



@given(instance=jointPackage_CPL2SPL_SrcTimeSwitch_strategy)
def test_jointpackage_cpl2spl_srctimeswitch_tzurl_setter(instance):
    original = instance.tzurl
    instance.tzurl = original
    assert instance.tzurl == original

@given(instance=jointPackage_CPL2SPL_SrcStringSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcstringswitch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcStringSwitch)



@given(instance=jointPackage_CPL2SPL_SrcStringSwitch_strategy)
def test_jointpackage_cpl2spl_srcstringswitch_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=jointPackage_CPL2SPL_SrcPrioritySwitch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcpriorityswitch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcPrioritySwitch)

@given(instance=jointPackage_CPL2SPL_SrcAddressSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage_cpl2spl_srcaddressswitch_instantiation(instance):
    assert isinstance(instance, jointPackage_CPL2SPL_SrcAddressSwitch)



@given(instance=jointPackage_CPL2SPL_SrcAddressSwitch_strategy)
def test_jointpackage_cpl2spl_srcaddressswitch_subField_setter(instance):
    original = instance.subField
    instance.subField = original
    assert instance.subField == original



@given(instance=jointPackage_CPL2SPL_SrcAddressSwitch_strategy)
def test_jointpackage_cpl2spl_srcaddressswitch_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original
