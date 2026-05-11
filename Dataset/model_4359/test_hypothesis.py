import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TrgResponse,
    jointPackage::CPL2SPL::TrgSuccessResponse,
    jointPackage::CPL2SPL::TrgErrorResponse,
    TrgVariablePlace,
    jointPackage::CPL2SPL::TrgPropertyCallPlace,
    jointPackage::CPL2SPL::TrgVariable,
    TrgSelectMember,
    jointPackage::CPL2SPL::TrgSelectCase,
    TrgMessageField,
    jointPackage::CPL2SPL::TrgHeadedMessageField,
    jointPackage::CPL2SPL::TrgReasonMessageField,
    TrgFunctionCall,
    TrgSelectDefault,
    TrgSelectCase,
    jointPackage::CPL2SPL::TrgSelectDefault,
    TrgConstant,
    jointPackage::CPL2SPL::TrgStringConstant,
    jointPackage::CPL2SPL::TrgBooleanConstant,
    jointPackage::CPL2SPL::TrgSequenceConstant,
    jointPackage::CPL2SPL::TrgResponseConstant,
    jointPackage::CPL2SPL::TrgIntegerConstant,
    jointPackage::CPL2SPL::TrgURIConstant,
    TrgNamedBranch,
    TrgWhenHeader,
    TrgVariable,
    TrgFunctionDeclaration,
    jointPackage::CPL2SPL::TrgLocalFunctionDeclaration,
    jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration,
    TrgPlace,
    jointPackage::CPL2SPL::TrgSIPHeaderPlace,
    jointPackage::CPL2SPL::TrgVariablePlace,
    TrgExpression,
    jointPackage::CPL2SPL::TrgOperatorExp,
    jointPackage::CPL2SPL::TrgForwardExp,
    jointPackage::CPL2SPL::TrgPlace,
    jointPackage::CPL2SPL::TrgReasonExp,
    jointPackage::CPL2SPL::TrgBODYExp,
    jointPackage::CPL2SPL::TrgConstantExp,
    jointPackage::CPL2SPL::TrgFunctionCallExp,
    jointPackage::CPL2SPL::TrgPopExp,
    jointPackage::CPL2SPL::TrgRequestURIExp,
    jointPackage::CPL2SPL::TrgBlockExp,
    jointPackage::CPL2SPL::TrgWithExp,
    TrgArgument,
    TrgMethodName,
    TrgMethod,
    jointPackage::CPL2SPL::TrgControlMethodName,
    jointPackage::CPL2SPL::TrgSIPMethodName,
    TrgVariableDeclaration,
    jointPackage::CPL2SPL::TrgWhenHeader,
    jointPackage::CPL2SPL::TrgArgument,
    TrgBranch,
    jointPackage::CPL2SPL::TrgDefaultBranch,
    jointPackage::CPL2SPL::TrgNamedBranch,
    TrgStatement,
    jointPackage::CPL2SPL::TrgForeachStat,
    jointPackage::CPL2SPL::TrgIfStat,
    jointPackage::CPL2SPL::TrgSetStat,
    jointPackage::CPL2SPL::TrgReturnStat,
    jointPackage::CPL2SPL::TrgBreakStat,
    jointPackage::CPL2SPL::TrgCompoundStat,
    jointPackage::CPL2SPL::TrgContinueStat,
    jointPackage::CPL2SPL::TrgDeclarationStat,
    jointPackage::CPL2SPL::TrgFunctionCallStat,
    jointPackage::CPL2SPL::TrgWhenStat,
    jointPackage::CPL2SPL::TrgSelectStat,
    jointPackage::CPL2SPL::TrgPushStat,
    TrgService,
    TrgLocatedElement,
    jointPackage::CPL2SPL::TrgResponse,
    jointPackage::CPL2SPL::TrgMessageField,
    jointPackage::CPL2SPL::TrgStatement,
    jointPackage::CPL2SPL::TrgDeclaration,
    jointPackage::CPL2SPL::TrgConstant,
    jointPackage::CPL2SPL::TrgExpression,
    jointPackage::CPL2SPL::TrgBranch,
    jointPackage::CPL2SPL::TrgFunctionCall,
    jointPackage::CPL2SPL::TrgMethodName,
    jointPackage::CPL2SPL::TrgSelectMember,
    jointPackage::CPL2SPL::TrgSession,
    jointPackage::CPL2SPL::TrgStructureProperty,
    jointPackage::CPL2SPL::TrgTypeExpression,
    jointPackage::CPL2SPL::TrgProgram,
    SrcAction,
    jointPackage::CPL2SPL::SrcSignallingAction,
    SrcOtherwise,
    SrcNotPresent,
    TrgSession,
    jointPackage::CPL2SPL::TrgDialog,
    jointPackage::CPL2SPL::TrgMethod,
    jointPackage::CPL2SPL::TrgRegistration,
    jointPackage::CPL2SPL::TrgEvent,
    TrgDeclaration,
    jointPackage::CPL2SPL::TrgVariableDeclaration,
    jointPackage::CPL2SPL::TrgStructureDeclaration,
    jointPackage::CPL2SPL::TrgFunctionDeclaration,
    jointPackage::CPL2SPL::TrgService,
    jointPackage::CPL2SPL::TrgLocatedElement,
    TrgErrorResponse,
    jointPackage::CPL2SPL::TrgGlobalErrorResponse,
    jointPackage::CPL2SPL::TrgServerErrorResponse,
    jointPackage::CPL2SPL::TrgRedirectionErrorResponse,
    jointPackage::CPL2SPL::TrgClientErrorResponse,
    TrgTypeExpression,
    jointPackage::CPL2SPL::TrgSequenceType,
    jointPackage::CPL2SPL::TrgDefinedType,
    jointPackage::CPL2SPL::TrgSimpleType,
    SrcNode,
    jointPackage::CPL2SPL::SrcSubCall,
    jointPackage::CPL2SPL::SrcSwitch,
    jointPackage::CPL2SPL::SrcAction,
    jointPackage::CPL2SPL::SrcElement,
    SrcDefault,
    SrcFailure,
    SrcRedirection,
    SrcNoAnswer,
    SrcBusy,
    SrcSignallingAction,
    jointPackage::CPL2SPL::SrcReject,
    jointPackage::CPL2SPL::SrcRedirect,
    jointPackage::CPL2SPL::SrcProxy,
    SrcSwitchedPriority,
    SrcNodeContainer,
    jointPackage::CPL2SPL::SrcNoAnswer,
    jointPackage::CPL2SPL::SrcIncoming,
    jointPackage::CPL2SPL::SrcOutgoing,
    jointPackage::CPL2SPL::SrcDefault,
    jointPackage::CPL2SPL::SrcSwitchedTime,
    jointPackage::CPL2SPL::SrcRedirection,
    jointPackage::CPL2SPL::SrcSwitchedString,
    jointPackage::CPL2SPL::SrcSwitchedAddress,
    jointPackage::CPL2SPL::SrcOtherwise,
    jointPackage::CPL2SPL::SrcFailure,
    jointPackage::CPL2SPL::SrcBusy,
    jointPackage::CPL2SPL::SrcNotPresent,
    jointPackage::CPL2SPL::SrcSwitchedPriority,
    jointPackage::CPL2SPL::SrcLocation,
    jointPackage::CPL2SPL::SrcSwitchedLanguage,
    jointPackage::CPL2SPL::SrcSubAction,
    SrcIncoming,
    SrcOutgoing,
    SrcSubAction,
    SrcElement,
    jointPackage::CPL2SPL::SrcNode,
    jointPackage::CPL2SPL::SrcCPL,
    jointPackage::CPL2SPL::SrcNodeContainer,
    jointPackage::CPL2SPL::SrcCPLModel,
    TrgServerErrorResponse,
    SrcReject,
    jointPackage::CPL2SPL::JointMM,
    SrcSwitchedTime,
    SrcSwitchedLanguage,
    SrcSwitchedString,
    SrcSwitchedAddress,
    SrcSwitch,
    jointPackage::CPL2SPL::SrcPrioritySwitch,
    jointPackage::CPL2SPL::SrcLanguageSwitch,
    jointPackage::CPL2SPL::SrcStringSwitch,
    jointPackage::CPL2SPL::SrcTimeSwitch,
    jointPackage::CPL2SPL::SrcAddressSwitch,
    SIPMethod,
    ServerErrorKind,
    ClientErrorKind,
    ControlMethod,
    Modifier,
    FunctionLocation,
    PrimitiveType,
    GlobalErrorKind,
    SuccessKind,
    SIPHeader,
    Direction,
    RedirectionErrorKind,
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



def test_jointpackage::cpl2spl::trgsuccessresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSuccessResponse)


def test_jointpackage::cpl2spl::trgsuccessresponse_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSuccessResponse.__init__)


def test_jointpackage::cpl2spl::trgsuccessresponse_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSuccessResponse.__init__)
    params = list(sig.parameters.keys())
    assert "successKind" in params, "Missing parameter 'successKind'"

def test_jointpackage::cpl2spl::trgsuccessresponse_has_successKind():
    assert hasattr(jointPackage::CPL2SPL::TrgSuccessResponse, "successKind")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgSuccessResponse.__mro__:
        if "successKind" in klass.__dict__:
            descriptor = klass.__dict__["successKind"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgerrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgErrorResponse)


def test_jointpackage::cpl2spl::trgerrorresponse_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgErrorResponse.__init__)


def test_jointpackage::cpl2spl::trgerrorresponse_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgErrorResponse.__init__)
    params = list(sig.parameters.keys())



def test_trgvariableplace_is_not_abstract():
    assert not inspect.isabstract(TrgVariablePlace)


def test_trgvariableplace_constructor_exists():
    assert callable(TrgVariablePlace.__init__)


def test_trgvariableplace_constructor_args():
    sig = inspect.signature(TrgVariablePlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgpropertycallplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgPropertyCallPlace)


def test_jointpackage::cpl2spl::trgpropertycallplace_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgPropertyCallPlace.__init__)


def test_jointpackage::cpl2spl::trgpropertycallplace_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgPropertyCallPlace.__init__)
    params = list(sig.parameters.keys())
    assert "propName" in params, "Missing parameter 'propName'"

def test_jointpackage::cpl2spl::trgpropertycallplace_has_propName():
    assert hasattr(jointPackage::CPL2SPL::TrgPropertyCallPlace, "propName")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgPropertyCallPlace.__mro__:
        if "propName" in klass.__dict__:
            descriptor = klass.__dict__["propName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgvariable_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgVariable)


def test_jointpackage::cpl2spl::trgvariable_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgVariable.__init__)


def test_jointpackage::cpl2spl::trgvariable_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgVariable.__init__)
    params = list(sig.parameters.keys())



def test_trgselectmember_is_not_abstract():
    assert not inspect.isabstract(TrgSelectMember)


def test_trgselectmember_constructor_exists():
    assert callable(TrgSelectMember.__init__)


def test_trgselectmember_constructor_args():
    sig = inspect.signature(TrgSelectMember.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgselectcase_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSelectCase)


def test_jointpackage::cpl2spl::trgselectcase_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSelectCase.__init__)


def test_jointpackage::cpl2spl::trgselectcase_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSelectCase.__init__)
    params = list(sig.parameters.keys())



def test_trgmessagefield_is_not_abstract():
    assert not inspect.isabstract(TrgMessageField)


def test_trgmessagefield_constructor_exists():
    assert callable(TrgMessageField.__init__)


def test_trgmessagefield_constructor_args():
    sig = inspect.signature(TrgMessageField.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgheadedmessagefield_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgHeadedMessageField)


def test_jointpackage::cpl2spl::trgheadedmessagefield_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgHeadedMessageField.__init__)


def test_jointpackage::cpl2spl::trgheadedmessagefield_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgHeadedMessageField.__init__)
    params = list(sig.parameters.keys())
    assert "headerId" in params, "Missing parameter 'headerId'"

def test_jointpackage::cpl2spl::trgheadedmessagefield_has_headerId():
    assert hasattr(jointPackage::CPL2SPL::TrgHeadedMessageField, "headerId")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgHeadedMessageField.__mro__:
        if "headerId" in klass.__dict__:
            descriptor = klass.__dict__["headerId"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgreasonmessagefield_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgReasonMessageField)


def test_jointpackage::cpl2spl::trgreasonmessagefield_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgReasonMessageField.__init__)


def test_jointpackage::cpl2spl::trgreasonmessagefield_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgReasonMessageField.__init__)
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



def test_jointpackage::cpl2spl::trgselectdefault_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSelectDefault)


def test_jointpackage::cpl2spl::trgselectdefault_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSelectDefault.__init__)


def test_jointpackage::cpl2spl::trgselectdefault_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSelectDefault.__init__)
    params = list(sig.parameters.keys())



def test_trgconstant_is_not_abstract():
    assert not inspect.isabstract(TrgConstant)


def test_trgconstant_constructor_exists():
    assert callable(TrgConstant.__init__)


def test_trgconstant_constructor_args():
    sig = inspect.signature(TrgConstant.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgstringconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgStringConstant)


def test_jointpackage::cpl2spl::trgstringconstant_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgStringConstant.__init__)


def test_jointpackage::cpl2spl::trgstringconstant_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgStringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage::cpl2spl::trgstringconstant_has_value():
    assert hasattr(jointPackage::CPL2SPL::TrgStringConstant, "value")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgStringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgbooleanconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgBooleanConstant)


def test_jointpackage::cpl2spl::trgbooleanconstant_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgBooleanConstant.__init__)


def test_jointpackage::cpl2spl::trgbooleanconstant_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgBooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage::cpl2spl::trgbooleanconstant_has_value():
    assert hasattr(jointPackage::CPL2SPL::TrgBooleanConstant, "value")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgBooleanConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgsequenceconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSequenceConstant)


def test_jointpackage::cpl2spl::trgsequenceconstant_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSequenceConstant.__init__)


def test_jointpackage::cpl2spl::trgsequenceconstant_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSequenceConstant.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgresponseconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgResponseConstant)


def test_jointpackage::cpl2spl::trgresponseconstant_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgResponseConstant.__init__)


def test_jointpackage::cpl2spl::trgresponseconstant_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgResponseConstant.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgintegerconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgIntegerConstant)


def test_jointpackage::cpl2spl::trgintegerconstant_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgIntegerConstant.__init__)


def test_jointpackage::cpl2spl::trgintegerconstant_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgIntegerConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage::cpl2spl::trgintegerconstant_has_value():
    assert hasattr(jointPackage::CPL2SPL::TrgIntegerConstant, "value")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgIntegerConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trguriconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgURIConstant)


def test_jointpackage::cpl2spl::trguriconstant_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgURIConstant.__init__)


def test_jointpackage::cpl2spl::trguriconstant_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgURIConstant.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_jointpackage::cpl2spl::trguriconstant_has_uri():
    assert hasattr(jointPackage::CPL2SPL::TrgURIConstant, "uri")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgURIConstant.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
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



def test_jointpackage::cpl2spl::trglocalfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgLocalFunctionDeclaration)


def test_jointpackage::cpl2spl::trglocalfunctiondeclaration_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgLocalFunctionDeclaration.__init__)


def test_jointpackage::cpl2spl::trglocalfunctiondeclaration_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgLocalFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgremotefunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration)


def test_jointpackage::cpl2spl::trgremotefunctiondeclaration_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration.__init__)


def test_jointpackage::cpl2spl::trgremotefunctiondeclaration_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionLocation" in params, "Missing parameter 'functionLocation'"

def test_jointpackage::cpl2spl::trgremotefunctiondeclaration_has_functionLocation():
    assert hasattr(jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration, "functionLocation")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration.__mro__:
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



def test_jointpackage::cpl2spl::trgsipheaderplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSIPHeaderPlace)


def test_jointpackage::cpl2spl::trgsipheaderplace_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSIPHeaderPlace.__init__)


def test_jointpackage::cpl2spl::trgsipheaderplace_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSIPHeaderPlace.__init__)
    params = list(sig.parameters.keys())
    assert "header" in params, "Missing parameter 'header'"

def test_jointpackage::cpl2spl::trgsipheaderplace_has_header():
    assert hasattr(jointPackage::CPL2SPL::TrgSIPHeaderPlace, "header")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgSIPHeaderPlace.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgvariableplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgVariablePlace)


def test_jointpackage::cpl2spl::trgvariableplace_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgVariablePlace.__init__)


def test_jointpackage::cpl2spl::trgvariableplace_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgVariablePlace.__init__)
    params = list(sig.parameters.keys())



def test_trgexpression_is_not_abstract():
    assert not inspect.isabstract(TrgExpression)


def test_trgexpression_constructor_exists():
    assert callable(TrgExpression.__init__)


def test_trgexpression_constructor_args():
    sig = inspect.signature(TrgExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgoperatorexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgOperatorExp)


def test_jointpackage::cpl2spl::trgoperatorexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgOperatorExp.__init__)


def test_jointpackage::cpl2spl::trgoperatorexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgOperatorExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_jointpackage::cpl2spl::trgoperatorexp_has_opName():
    assert hasattr(jointPackage::CPL2SPL::TrgOperatorExp, "opName")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgOperatorExp.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgforwardexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgForwardExp)


def test_jointpackage::cpl2spl::trgforwardexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgForwardExp.__init__)


def test_jointpackage::cpl2spl::trgforwardexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgForwardExp.__init__)
    params = list(sig.parameters.keys())
    assert "isParallel" in params, "Missing parameter 'isParallel'"

def test_jointpackage::cpl2spl::trgforwardexp_has_isParallel():
    assert hasattr(jointPackage::CPL2SPL::TrgForwardExp, "isParallel")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgForwardExp.__mro__:
        if "isParallel" in klass.__dict__:
            descriptor = klass.__dict__["isParallel"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgPlace)


def test_jointpackage::cpl2spl::trgplace_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgPlace.__init__)


def test_jointpackage::cpl2spl::trgplace_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgPlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgreasonexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgReasonExp)


def test_jointpackage::cpl2spl::trgreasonexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgReasonExp.__init__)


def test_jointpackage::cpl2spl::trgreasonexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgReasonExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgbodyexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgBODYExp)


def test_jointpackage::cpl2spl::trgbodyexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgBODYExp.__init__)


def test_jointpackage::cpl2spl::trgbodyexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgBODYExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgconstantexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgConstantExp)


def test_jointpackage::cpl2spl::trgconstantexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgConstantExp.__init__)


def test_jointpackage::cpl2spl::trgconstantexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgConstantExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgfunctioncallexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgFunctionCallExp)


def test_jointpackage::cpl2spl::trgfunctioncallexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgFunctionCallExp.__init__)


def test_jointpackage::cpl2spl::trgfunctioncallexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgFunctionCallExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgpopexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgPopExp)


def test_jointpackage::cpl2spl::trgpopexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgPopExp.__init__)


def test_jointpackage::cpl2spl::trgpopexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgPopExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgrequesturiexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgRequestURIExp)


def test_jointpackage::cpl2spl::trgrequesturiexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgRequestURIExp.__init__)


def test_jointpackage::cpl2spl::trgrequesturiexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgRequestURIExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgblockexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgBlockExp)


def test_jointpackage::cpl2spl::trgblockexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgBlockExp.__init__)


def test_jointpackage::cpl2spl::trgblockexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgBlockExp.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgwithexp_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgWithExp)


def test_jointpackage::cpl2spl::trgwithexp_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgWithExp.__init__)


def test_jointpackage::cpl2spl::trgwithexp_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgWithExp.__init__)
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



def test_jointpackage::cpl2spl::trgcontrolmethodname_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgControlMethodName)


def test_jointpackage::cpl2spl::trgcontrolmethodname_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgControlMethodName.__init__)


def test_jointpackage::cpl2spl::trgcontrolmethodname_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgControlMethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::cpl2spl::trgcontrolmethodname_has_name():
    assert hasattr(jointPackage::CPL2SPL::TrgControlMethodName, "name")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgControlMethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgsipmethodname_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSIPMethodName)


def test_jointpackage::cpl2spl::trgsipmethodname_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSIPMethodName.__init__)


def test_jointpackage::cpl2spl::trgsipmethodname_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSIPMethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::cpl2spl::trgsipmethodname_has_name():
    assert hasattr(jointPackage::CPL2SPL::TrgSIPMethodName, "name")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgSIPMethodName.__mro__:
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



def test_jointpackage::cpl2spl::trgwhenheader_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgWhenHeader)


def test_jointpackage::cpl2spl::trgwhenheader_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgWhenHeader.__init__)


def test_jointpackage::cpl2spl::trgwhenheader_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgWhenHeader.__init__)
    params = list(sig.parameters.keys())
    assert "headerId" in params, "Missing parameter 'headerId'"

def test_jointpackage::cpl2spl::trgwhenheader_has_headerId():
    assert hasattr(jointPackage::CPL2SPL::TrgWhenHeader, "headerId")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgWhenHeader.__mro__:
        if "headerId" in klass.__dict__:
            descriptor = klass.__dict__["headerId"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgargument_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgArgument)


def test_jointpackage::cpl2spl::trgargument_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgArgument.__init__)


def test_jointpackage::cpl2spl::trgargument_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgArgument.__init__)
    params = list(sig.parameters.keys())



def test_trgbranch_is_not_abstract():
    assert not inspect.isabstract(TrgBranch)


def test_trgbranch_constructor_exists():
    assert callable(TrgBranch.__init__)


def test_trgbranch_constructor_args():
    sig = inspect.signature(TrgBranch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgdefaultbranch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgDefaultBranch)


def test_jointpackage::cpl2spl::trgdefaultbranch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgDefaultBranch.__init__)


def test_jointpackage::cpl2spl::trgdefaultbranch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgDefaultBranch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgnamedbranch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgNamedBranch)


def test_jointpackage::cpl2spl::trgnamedbranch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgNamedBranch.__init__)


def test_jointpackage::cpl2spl::trgnamedbranch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgNamedBranch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::cpl2spl::trgnamedbranch_has_name():
    assert hasattr(jointPackage::CPL2SPL::TrgNamedBranch, "name")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgNamedBranch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trgstatement_is_not_abstract():
    assert not inspect.isabstract(TrgStatement)


def test_trgstatement_constructor_exists():
    assert callable(TrgStatement.__init__)


def test_trgstatement_constructor_args():
    sig = inspect.signature(TrgStatement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgforeachstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgForeachStat)


def test_jointpackage::cpl2spl::trgforeachstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgForeachStat.__init__)


def test_jointpackage::cpl2spl::trgforeachstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgForeachStat.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_jointpackage::cpl2spl::trgforeachstat_has_iteratorName():
    assert hasattr(jointPackage::CPL2SPL::TrgForeachStat, "iteratorName")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgForeachStat.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgifstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgIfStat)


def test_jointpackage::cpl2spl::trgifstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgIfStat.__init__)


def test_jointpackage::cpl2spl::trgifstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgIfStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgsetstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSetStat)


def test_jointpackage::cpl2spl::trgsetstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSetStat.__init__)


def test_jointpackage::cpl2spl::trgsetstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSetStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgreturnstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgReturnStat)


def test_jointpackage::cpl2spl::trgreturnstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgReturnStat.__init__)


def test_jointpackage::cpl2spl::trgreturnstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgReturnStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgbreakstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgBreakStat)


def test_jointpackage::cpl2spl::trgbreakstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgBreakStat.__init__)


def test_jointpackage::cpl2spl::trgbreakstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgBreakStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgcompoundstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgCompoundStat)


def test_jointpackage::cpl2spl::trgcompoundstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgCompoundStat.__init__)


def test_jointpackage::cpl2spl::trgcompoundstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgCompoundStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgcontinuestat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgContinueStat)


def test_jointpackage::cpl2spl::trgcontinuestat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgContinueStat.__init__)


def test_jointpackage::cpl2spl::trgcontinuestat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgContinueStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgdeclarationstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgDeclarationStat)


def test_jointpackage::cpl2spl::trgdeclarationstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgDeclarationStat.__init__)


def test_jointpackage::cpl2spl::trgdeclarationstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgDeclarationStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgfunctioncallstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgFunctionCallStat)


def test_jointpackage::cpl2spl::trgfunctioncallstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgFunctionCallStat.__init__)


def test_jointpackage::cpl2spl::trgfunctioncallstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgFunctionCallStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgwhenstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgWhenStat)


def test_jointpackage::cpl2spl::trgwhenstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgWhenStat.__init__)


def test_jointpackage::cpl2spl::trgwhenstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgWhenStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgselectstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSelectStat)


def test_jointpackage::cpl2spl::trgselectstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSelectStat.__init__)


def test_jointpackage::cpl2spl::trgselectstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSelectStat.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgpushstat_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgPushStat)


def test_jointpackage::cpl2spl::trgpushstat_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgPushStat.__init__)


def test_jointpackage::cpl2spl::trgpushstat_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgPushStat.__init__)
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



def test_jointpackage::cpl2spl::trgresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgResponse)


def test_jointpackage::cpl2spl::trgresponse_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgResponse.__init__)


def test_jointpackage::cpl2spl::trgresponse_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgResponse.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgmessagefield_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgMessageField)


def test_jointpackage::cpl2spl::trgmessagefield_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgMessageField.__init__)


def test_jointpackage::cpl2spl::trgmessagefield_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgMessageField.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgstatement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgStatement)


def test_jointpackage::cpl2spl::trgstatement_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgStatement.__init__)


def test_jointpackage::cpl2spl::trgstatement_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgStatement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgdeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgDeclaration)


def test_jointpackage::cpl2spl::trgdeclaration_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgDeclaration.__init__)


def test_jointpackage::cpl2spl::trgdeclaration_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::cpl2spl::trgdeclaration_has_name():
    assert hasattr(jointPackage::CPL2SPL::TrgDeclaration, "name")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgconstant_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgConstant)


def test_jointpackage::cpl2spl::trgconstant_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgConstant.__init__)


def test_jointpackage::cpl2spl::trgconstant_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgConstant.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgexpression_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgExpression)


def test_jointpackage::cpl2spl::trgexpression_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgExpression.__init__)


def test_jointpackage::cpl2spl::trgexpression_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgbranch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgBranch)


def test_jointpackage::cpl2spl::trgbranch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgBranch.__init__)


def test_jointpackage::cpl2spl::trgbranch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgBranch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgfunctioncall_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgFunctionCall)


def test_jointpackage::cpl2spl::trgfunctioncall_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgFunctionCall.__init__)


def test_jointpackage::cpl2spl::trgfunctioncall_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgFunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgmethodname_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgMethodName)


def test_jointpackage::cpl2spl::trgmethodname_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgMethodName.__init__)


def test_jointpackage::cpl2spl::trgmethodname_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgMethodName.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgselectmember_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSelectMember)


def test_jointpackage::cpl2spl::trgselectmember_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSelectMember.__init__)


def test_jointpackage::cpl2spl::trgselectmember_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSelectMember.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgsession_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSession)


def test_jointpackage::cpl2spl::trgsession_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSession.__init__)


def test_jointpackage::cpl2spl::trgsession_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSession.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgstructureproperty_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgStructureProperty)


def test_jointpackage::cpl2spl::trgstructureproperty_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgStructureProperty.__init__)


def test_jointpackage::cpl2spl::trgstructureproperty_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgStructureProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::cpl2spl::trgstructureproperty_has_name():
    assert hasattr(jointPackage::CPL2SPL::TrgStructureProperty, "name")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgStructureProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgtypeexpression_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgTypeExpression)


def test_jointpackage::cpl2spl::trgtypeexpression_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgTypeExpression.__init__)


def test_jointpackage::cpl2spl::trgtypeexpression_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgTypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgprogram_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgProgram)


def test_jointpackage::cpl2spl::trgprogram_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgProgram.__init__)


def test_jointpackage::cpl2spl::trgprogram_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgProgram.__init__)
    params = list(sig.parameters.keys())



def test_srcaction_is_not_abstract():
    assert not inspect.isabstract(SrcAction)


def test_srcaction_constructor_exists():
    assert callable(SrcAction.__init__)


def test_srcaction_constructor_args():
    sig = inspect.signature(SrcAction.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcsignallingaction_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSignallingAction)


def test_jointpackage::cpl2spl::srcsignallingaction_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSignallingAction.__init__)


def test_jointpackage::cpl2spl::srcsignallingaction_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSignallingAction.__init__)
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



def test_jointpackage::cpl2spl::trgdialog_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgDialog)


def test_jointpackage::cpl2spl::trgdialog_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgDialog.__init__)


def test_jointpackage::cpl2spl::trgdialog_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgDialog.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgmethod_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgMethod)


def test_jointpackage::cpl2spl::trgmethod_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgMethod.__init__)


def test_jointpackage::cpl2spl::trgmethod_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgMethod.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_jointpackage::cpl2spl::trgmethod_has_direction():
    assert hasattr(jointPackage::CPL2SPL::TrgMethod, "direction")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgMethod.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgregistration_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgRegistration)


def test_jointpackage::cpl2spl::trgregistration_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgRegistration.__init__)


def test_jointpackage::cpl2spl::trgregistration_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgRegistration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgevent_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgEvent)


def test_jointpackage::cpl2spl::trgevent_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgEvent.__init__)


def test_jointpackage::cpl2spl::trgevent_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgEvent.__init__)
    params = list(sig.parameters.keys())
    assert "eventId" in params, "Missing parameter 'eventId'"

def test_jointpackage::cpl2spl::trgevent_has_eventId():
    assert hasattr(jointPackage::CPL2SPL::TrgEvent, "eventId")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgEvent.__mro__:
        if "eventId" in klass.__dict__:
            descriptor = klass.__dict__["eventId"]
            break
    assert isinstance(descriptor, property)



def test_trgdeclaration_is_not_abstract():
    assert not inspect.isabstract(TrgDeclaration)


def test_trgdeclaration_constructor_exists():
    assert callable(TrgDeclaration.__init__)


def test_trgdeclaration_constructor_args():
    sig = inspect.signature(TrgDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgVariableDeclaration)


def test_jointpackage::cpl2spl::trgvariabledeclaration_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgVariableDeclaration.__init__)


def test_jointpackage::cpl2spl::trgvariabledeclaration_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgstructuredeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgStructureDeclaration)


def test_jointpackage::cpl2spl::trgstructuredeclaration_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgStructureDeclaration.__init__)


def test_jointpackage::cpl2spl::trgstructuredeclaration_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgStructureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgFunctionDeclaration)


def test_jointpackage::cpl2spl::trgfunctiondeclaration_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgFunctionDeclaration.__init__)


def test_jointpackage::cpl2spl::trgfunctiondeclaration_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgservice_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgService)


def test_jointpackage::cpl2spl::trgservice_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgService.__init__)


def test_jointpackage::cpl2spl::trgservice_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgService.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::cpl2spl::trgservice_has_name():
    assert hasattr(jointPackage::CPL2SPL::TrgService, "name")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgService.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgLocatedElement)


def test_jointpackage::cpl2spl::trglocatedelement_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgLocatedElement.__init__)


def test_jointpackage::cpl2spl::trglocatedelement_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_jointpackage::cpl2spl::trglocatedelement_has_commentsAfter():
    assert hasattr(jointPackage::CPL2SPL::TrgLocatedElement, "commentsAfter")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgLocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::trglocatedelement_has_location():
    assert hasattr(jointPackage::CPL2SPL::TrgLocatedElement, "location")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgLocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::trglocatedelement_has_commentsBefore():
    assert hasattr(jointPackage::CPL2SPL::TrgLocatedElement, "commentsBefore")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgLocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)



def test_trgerrorresponse_is_not_abstract():
    assert not inspect.isabstract(TrgErrorResponse)


def test_trgerrorresponse_constructor_exists():
    assert callable(TrgErrorResponse.__init__)


def test_trgerrorresponse_constructor_args():
    sig = inspect.signature(TrgErrorResponse.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::trgglobalerrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgGlobalErrorResponse)


def test_jointpackage::cpl2spl::trgglobalerrorresponse_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgGlobalErrorResponse.__init__)


def test_jointpackage::cpl2spl::trgglobalerrorresponse_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgGlobalErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_jointpackage::cpl2spl::trgglobalerrorresponse_has_errorKind():
    assert hasattr(jointPackage::CPL2SPL::TrgGlobalErrorResponse, "errorKind")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgGlobalErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgservererrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgServerErrorResponse)


def test_jointpackage::cpl2spl::trgservererrorresponse_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgServerErrorResponse.__init__)


def test_jointpackage::cpl2spl::trgservererrorresponse_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgServerErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_jointpackage::cpl2spl::trgservererrorresponse_has_errorKind():
    assert hasattr(jointPackage::CPL2SPL::TrgServerErrorResponse, "errorKind")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgServerErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgredirectionerrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgRedirectionErrorResponse)


def test_jointpackage::cpl2spl::trgredirectionerrorresponse_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgRedirectionErrorResponse.__init__)


def test_jointpackage::cpl2spl::trgredirectionerrorresponse_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgRedirectionErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_jointpackage::cpl2spl::trgredirectionerrorresponse_has_errorKind():
    assert hasattr(jointPackage::CPL2SPL::TrgRedirectionErrorResponse, "errorKind")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgRedirectionErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgclienterrorresponse_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgClientErrorResponse)


def test_jointpackage::cpl2spl::trgclienterrorresponse_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgClientErrorResponse.__init__)


def test_jointpackage::cpl2spl::trgclienterrorresponse_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgClientErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_jointpackage::cpl2spl::trgclienterrorresponse_has_errorKind():
    assert hasattr(jointPackage::CPL2SPL::TrgClientErrorResponse, "errorKind")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgClientErrorResponse.__mro__:
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



def test_jointpackage::cpl2spl::trgsequencetype_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSequenceType)


def test_jointpackage::cpl2spl::trgsequencetype_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSequenceType.__init__)


def test_jointpackage::cpl2spl::trgsequencetype_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "type" in params, "Missing parameter 'type'"

def test_jointpackage::cpl2spl::trgsequencetype_has_size():
    assert hasattr(jointPackage::CPL2SPL::TrgSequenceType, "size")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgSequenceType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::trgsequencetype_has_modifier():
    assert hasattr(jointPackage::CPL2SPL::TrgSequenceType, "modifier")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgSequenceType.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::trgsequencetype_has_type():
    assert hasattr(jointPackage::CPL2SPL::TrgSequenceType, "type")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgSequenceType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgdefinedtype_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgDefinedType)


def test_jointpackage::cpl2spl::trgdefinedtype_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgDefinedType.__init__)


def test_jointpackage::cpl2spl::trgdefinedtype_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_jointpackage::cpl2spl::trgdefinedtype_has_typeName():
    assert hasattr(jointPackage::CPL2SPL::TrgDefinedType, "typeName")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgDefinedType.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::trgsimpletype_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::TrgSimpleType)


def test_jointpackage::cpl2spl::trgsimpletype_constructor_exists():
    assert callable(jointPackage::CPL2SPL::TrgSimpleType.__init__)


def test_jointpackage::cpl2spl::trgsimpletype_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::TrgSimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jointpackage::cpl2spl::trgsimpletype_has_type():
    assert hasattr(jointPackage::CPL2SPL::TrgSimpleType, "type")
    descriptor = None
    for klass in jointPackage::CPL2SPL::TrgSimpleType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_srcnode_is_not_abstract():
    assert not inspect.isabstract(SrcNode)


def test_srcnode_constructor_exists():
    assert callable(SrcNode.__init__)


def test_srcnode_constructor_args():
    sig = inspect.signature(SrcNode.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcsubcall_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSubCall)


def test_jointpackage::cpl2spl::srcsubcall_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSubCall.__init__)


def test_jointpackage::cpl2spl::srcsubcall_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSubCall.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_jointpackage::cpl2spl::srcsubcall_has_ref():
    assert hasattr(jointPackage::CPL2SPL::SrcSubCall, "ref")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSubCall.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSwitch)


def test_jointpackage::cpl2spl::srcswitch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSwitch.__init__)


def test_jointpackage::cpl2spl::srcswitch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSwitch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcaction_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcAction)


def test_jointpackage::cpl2spl::srcaction_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcAction.__init__)


def test_jointpackage::cpl2spl::srcaction_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcAction.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcElement)


def test_jointpackage::cpl2spl::srcelement_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcElement.__init__)


def test_jointpackage::cpl2spl::srcelement_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcElement.__init__)
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



def test_jointpackage::cpl2spl::srcreject_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcReject)


def test_jointpackage::cpl2spl::srcreject_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcReject.__init__)


def test_jointpackage::cpl2spl::srcreject_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcReject.__init__)
    params = list(sig.parameters.keys())
    assert "reason" in params, "Missing parameter 'reason'"
    assert "status" in params, "Missing parameter 'status'"

def test_jointpackage::cpl2spl::srcreject_has_reason():
    assert hasattr(jointPackage::CPL2SPL::SrcReject, "reason")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcReject.__mro__:
        if "reason" in klass.__dict__:
            descriptor = klass.__dict__["reason"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcreject_has_status():
    assert hasattr(jointPackage::CPL2SPL::SrcReject, "status")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcReject.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcredirect_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcRedirect)


def test_jointpackage::cpl2spl::srcredirect_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcRedirect.__init__)


def test_jointpackage::cpl2spl::srcredirect_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcRedirect.__init__)
    params = list(sig.parameters.keys())
    assert "permanent" in params, "Missing parameter 'permanent'"

def test_jointpackage::cpl2spl::srcredirect_has_permanent():
    assert hasattr(jointPackage::CPL2SPL::SrcRedirect, "permanent")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcRedirect.__mro__:
        if "permanent" in klass.__dict__:
            descriptor = klass.__dict__["permanent"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcproxy_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcProxy)


def test_jointpackage::cpl2spl::srcproxy_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcProxy.__init__)


def test_jointpackage::cpl2spl::srcproxy_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcProxy.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"
    assert "recurse" in params, "Missing parameter 'recurse'"
    assert "ordering" in params, "Missing parameter 'ordering'"

def test_jointpackage::cpl2spl::srcproxy_has_timeout():
    assert hasattr(jointPackage::CPL2SPL::SrcProxy, "timeout")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcProxy.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcproxy_has_recurse():
    assert hasattr(jointPackage::CPL2SPL::SrcProxy, "recurse")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcProxy.__mro__:
        if "recurse" in klass.__dict__:
            descriptor = klass.__dict__["recurse"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcproxy_has_ordering():
    assert hasattr(jointPackage::CPL2SPL::SrcProxy, "ordering")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcProxy.__mro__:
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



def test_jointpackage::cpl2spl::srcnoanswer_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcNoAnswer)


def test_jointpackage::cpl2spl::srcnoanswer_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcNoAnswer.__init__)


def test_jointpackage::cpl2spl::srcnoanswer_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcNoAnswer.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcincoming_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcIncoming)


def test_jointpackage::cpl2spl::srcincoming_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcIncoming.__init__)


def test_jointpackage::cpl2spl::srcincoming_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcIncoming.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcoutgoing_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcOutgoing)


def test_jointpackage::cpl2spl::srcoutgoing_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcOutgoing.__init__)


def test_jointpackage::cpl2spl::srcoutgoing_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcOutgoing.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcdefault_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcDefault)


def test_jointpackage::cpl2spl::srcdefault_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcDefault.__init__)


def test_jointpackage::cpl2spl::srcdefault_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcDefault.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcswitchedtime_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSwitchedTime)


def test_jointpackage::cpl2spl::srcswitchedtime_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSwitchedTime.__init__)


def test_jointpackage::cpl2spl::srcswitchedtime_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSwitchedTime.__init__)
    params = list(sig.parameters.keys())
    assert "byWeekNo" in params, "Missing parameter 'byWeekNo'"
    assert "dtend" in params, "Missing parameter 'dtend'"
    assert "until" in params, "Missing parameter 'until'"
    assert "freq" in params, "Missing parameter 'freq'"
    assert "byDay" in params, "Missing parameter 'byDay'"
    assert "bySetPos" in params, "Missing parameter 'bySetPos'"
    assert "dtstart" in params, "Missing parameter 'dtstart'"
    assert "byMonth" in params, "Missing parameter 'byMonth'"
    assert "count" in params, "Missing parameter 'count'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "byMinute" in params, "Missing parameter 'byMinute'"
    assert "byMonthDay" in params, "Missing parameter 'byMonthDay'"
    assert "byYearDay" in params, "Missing parameter 'byYearDay'"
    assert "bySecond" in params, "Missing parameter 'bySecond'"
    assert "byHour" in params, "Missing parameter 'byHour'"
    assert "wkst" in params, "Missing parameter 'wkst'"
    assert "interval" in params, "Missing parameter 'interval'"

def test_jointpackage::cpl2spl::srcswitchedtime_has_byWeekNo():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "byWeekNo")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "byWeekNo" in klass.__dict__:
            descriptor = klass.__dict__["byWeekNo"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_dtend():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "dtend")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "dtend" in klass.__dict__:
            descriptor = klass.__dict__["dtend"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_until():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "until")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "until" in klass.__dict__:
            descriptor = klass.__dict__["until"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_freq():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "freq")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "freq" in klass.__dict__:
            descriptor = klass.__dict__["freq"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_byDay():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "byDay")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "byDay" in klass.__dict__:
            descriptor = klass.__dict__["byDay"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_bySetPos():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "bySetPos")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "bySetPos" in klass.__dict__:
            descriptor = klass.__dict__["bySetPos"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_dtstart():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "dtstart")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "dtstart" in klass.__dict__:
            descriptor = klass.__dict__["dtstart"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_byMonth():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "byMonth")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "byMonth" in klass.__dict__:
            descriptor = klass.__dict__["byMonth"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_count():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "count")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_duration():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "duration")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_byMinute():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "byMinute")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "byMinute" in klass.__dict__:
            descriptor = klass.__dict__["byMinute"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_byMonthDay():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "byMonthDay")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "byMonthDay" in klass.__dict__:
            descriptor = klass.__dict__["byMonthDay"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_byYearDay():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "byYearDay")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "byYearDay" in klass.__dict__:
            descriptor = klass.__dict__["byYearDay"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_bySecond():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "bySecond")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "bySecond" in klass.__dict__:
            descriptor = klass.__dict__["bySecond"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_byHour():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "byHour")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "byHour" in klass.__dict__:
            descriptor = klass.__dict__["byHour"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_wkst():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "wkst")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "wkst" in klass.__dict__:
            descriptor = klass.__dict__["wkst"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedtime_has_interval():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedTime, "interval")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedTime.__mro__:
        if "interval" in klass.__dict__:
            descriptor = klass.__dict__["interval"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcredirection_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcRedirection)


def test_jointpackage::cpl2spl::srcredirection_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcRedirection.__init__)


def test_jointpackage::cpl2spl::srcredirection_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcRedirection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcswitchedstring_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSwitchedString)


def test_jointpackage::cpl2spl::srcswitchedstring_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSwitchedString.__init__)


def test_jointpackage::cpl2spl::srcswitchedstring_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSwitchedString.__init__)
    params = list(sig.parameters.keys())
    assert "is_" in params, "Missing parameter 'is_'"
    assert "contains" in params, "Missing parameter 'contains'"

def test_jointpackage::cpl2spl::srcswitchedstring_has_is_():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedString, "is_")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedString.__mro__:
        if "is_" in klass.__dict__:
            descriptor = klass.__dict__["is_"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedstring_has_contains():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedString, "contains")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedString.__mro__:
        if "contains" in klass.__dict__:
            descriptor = klass.__dict__["contains"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcswitchedaddress_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSwitchedAddress)


def test_jointpackage::cpl2spl::srcswitchedaddress_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSwitchedAddress.__init__)


def test_jointpackage::cpl2spl::srcswitchedaddress_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSwitchedAddress.__init__)
    params = list(sig.parameters.keys())
    assert "is_" in params, "Missing parameter 'is_'"
    assert "subDomainOf" in params, "Missing parameter 'subDomainOf'"
    assert "contains" in params, "Missing parameter 'contains'"

def test_jointpackage::cpl2spl::srcswitchedaddress_has_is_():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedAddress, "is_")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedAddress.__mro__:
        if "is_" in klass.__dict__:
            descriptor = klass.__dict__["is_"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedaddress_has_subDomainOf():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedAddress, "subDomainOf")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedAddress.__mro__:
        if "subDomainOf" in klass.__dict__:
            descriptor = klass.__dict__["subDomainOf"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedaddress_has_contains():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedAddress, "contains")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedAddress.__mro__:
        if "contains" in klass.__dict__:
            descriptor = klass.__dict__["contains"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcotherwise_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcOtherwise)


def test_jointpackage::cpl2spl::srcotherwise_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcOtherwise.__init__)


def test_jointpackage::cpl2spl::srcotherwise_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcOtherwise.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcfailure_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcFailure)


def test_jointpackage::cpl2spl::srcfailure_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcFailure.__init__)


def test_jointpackage::cpl2spl::srcfailure_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcFailure.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcbusy_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcBusy)


def test_jointpackage::cpl2spl::srcbusy_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcBusy.__init__)


def test_jointpackage::cpl2spl::srcbusy_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcBusy.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcnotpresent_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcNotPresent)


def test_jointpackage::cpl2spl::srcnotpresent_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcNotPresent.__init__)


def test_jointpackage::cpl2spl::srcnotpresent_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcNotPresent.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcswitchedpriority_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSwitchedPriority)


def test_jointpackage::cpl2spl::srcswitchedpriority_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSwitchedPriority.__init__)


def test_jointpackage::cpl2spl::srcswitchedpriority_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSwitchedPriority.__init__)
    params = list(sig.parameters.keys())
    assert "less" in params, "Missing parameter 'less'"
    assert "greater" in params, "Missing parameter 'greater'"
    assert "equal" in params, "Missing parameter 'equal'"

def test_jointpackage::cpl2spl::srcswitchedpriority_has_less():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedPriority, "less")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedPriority.__mro__:
        if "less" in klass.__dict__:
            descriptor = klass.__dict__["less"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedpriority_has_greater():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedPriority, "greater")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedPriority.__mro__:
        if "greater" in klass.__dict__:
            descriptor = klass.__dict__["greater"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcswitchedpriority_has_equal():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedPriority, "equal")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedPriority.__mro__:
        if "equal" in klass.__dict__:
            descriptor = klass.__dict__["equal"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srclocation_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcLocation)


def test_jointpackage::cpl2spl::srclocation_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcLocation.__init__)


def test_jointpackage::cpl2spl::srclocation_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcLocation.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "clear" in params, "Missing parameter 'clear'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_jointpackage::cpl2spl::srclocation_has_url():
    assert hasattr(jointPackage::CPL2SPL::SrcLocation, "url")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcLocation.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srclocation_has_clear():
    assert hasattr(jointPackage::CPL2SPL::SrcLocation, "clear")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcLocation.__mro__:
        if "clear" in klass.__dict__:
            descriptor = klass.__dict__["clear"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srclocation_has_priority():
    assert hasattr(jointPackage::CPL2SPL::SrcLocation, "priority")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcLocation.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcswitchedlanguage_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSwitchedLanguage)


def test_jointpackage::cpl2spl::srcswitchedlanguage_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSwitchedLanguage.__init__)


def test_jointpackage::cpl2spl::srcswitchedlanguage_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSwitchedLanguage.__init__)
    params = list(sig.parameters.keys())
    assert "matches" in params, "Missing parameter 'matches'"

def test_jointpackage::cpl2spl::srcswitchedlanguage_has_matches():
    assert hasattr(jointPackage::CPL2SPL::SrcSwitchedLanguage, "matches")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSwitchedLanguage.__mro__:
        if "matches" in klass.__dict__:
            descriptor = klass.__dict__["matches"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcsubaction_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcSubAction)


def test_jointpackage::cpl2spl::srcsubaction_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcSubAction.__init__)


def test_jointpackage::cpl2spl::srcsubaction_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcSubAction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_jointpackage::cpl2spl::srcsubaction_has_id():
    assert hasattr(jointPackage::CPL2SPL::SrcSubAction, "id")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcSubAction.__mro__:
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



def test_jointpackage::cpl2spl::srcnode_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcNode)


def test_jointpackage::cpl2spl::srcnode_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcNode.__init__)


def test_jointpackage::cpl2spl::srcnode_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcNode.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srccpl_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcCPL)


def test_jointpackage::cpl2spl::srccpl_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcCPL.__init__)


def test_jointpackage::cpl2spl::srccpl_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcCPL.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcnodecontainer_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcNodeContainer)


def test_jointpackage::cpl2spl::srcnodecontainer_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcNodeContainer.__init__)


def test_jointpackage::cpl2spl::srcnodecontainer_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcNodeContainer.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srccplmodel_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcCPLModel)


def test_jointpackage::cpl2spl::srccplmodel_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcCPLModel.__init__)


def test_jointpackage::cpl2spl::srccplmodel_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcCPLModel.__init__)
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



def test_jointpackage::cpl2spl::jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::JointMM)


def test_jointpackage::cpl2spl::jointmm_constructor_exists():
    assert callable(jointPackage::CPL2SPL::JointMM.__init__)


def test_jointpackage::cpl2spl::jointmm_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::JointMM.__init__)
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



def test_jointpackage::cpl2spl::srcpriorityswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcPrioritySwitch)


def test_jointpackage::cpl2spl::srcpriorityswitch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcPrioritySwitch.__init__)


def test_jointpackage::cpl2spl::srcpriorityswitch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcPrioritySwitch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srclanguageswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcLanguageSwitch)


def test_jointpackage::cpl2spl::srclanguageswitch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcLanguageSwitch.__init__)


def test_jointpackage::cpl2spl::srclanguageswitch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcLanguageSwitch.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::cpl2spl::srcstringswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcStringSwitch)


def test_jointpackage::cpl2spl::srcstringswitch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcStringSwitch.__init__)


def test_jointpackage::cpl2spl::srcstringswitch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcStringSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_jointpackage::cpl2spl::srcstringswitch_has_field():
    assert hasattr(jointPackage::CPL2SPL::SrcStringSwitch, "field")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcStringSwitch.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srctimeswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcTimeSwitch)


def test_jointpackage::cpl2spl::srctimeswitch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcTimeSwitch.__init__)


def test_jointpackage::cpl2spl::srctimeswitch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcTimeSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "tzurl" in params, "Missing parameter 'tzurl'"
    assert "tzid" in params, "Missing parameter 'tzid'"

def test_jointpackage::cpl2spl::srctimeswitch_has_tzurl():
    assert hasattr(jointPackage::CPL2SPL::SrcTimeSwitch, "tzurl")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcTimeSwitch.__mro__:
        if "tzurl" in klass.__dict__:
            descriptor = klass.__dict__["tzurl"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srctimeswitch_has_tzid():
    assert hasattr(jointPackage::CPL2SPL::SrcTimeSwitch, "tzid")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcTimeSwitch.__mro__:
        if "tzid" in klass.__dict__:
            descriptor = klass.__dict__["tzid"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::cpl2spl::srcaddressswitch_is_not_abstract():
    assert not inspect.isabstract(jointPackage::CPL2SPL::SrcAddressSwitch)


def test_jointpackage::cpl2spl::srcaddressswitch_constructor_exists():
    assert callable(jointPackage::CPL2SPL::SrcAddressSwitch.__init__)


def test_jointpackage::cpl2spl::srcaddressswitch_constructor_args():
    sig = inspect.signature(jointPackage::CPL2SPL::SrcAddressSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "subField" in params, "Missing parameter 'subField'"
    assert "field" in params, "Missing parameter 'field'"

def test_jointpackage::cpl2spl::srcaddressswitch_has_subField():
    assert hasattr(jointPackage::CPL2SPL::SrcAddressSwitch, "subField")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcAddressSwitch.__mro__:
        if "subField" in klass.__dict__:
            descriptor = klass.__dict__["subField"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::cpl2spl::srcaddressswitch_has_field():
    assert hasattr(jointPackage::CPL2SPL::SrcAddressSwitch, "field")
    descriptor = None
    for klass in jointPackage::CPL2SPL::SrcAddressSwitch.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_sipmethod_exists():
    # Check that the Enumeration exists
    assert SIPMethod is not None

def test_sipmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIPMethod]
    expected_literals = [
        "CANCEL",
        "INVITE",
        "SUBSCRIBE",
        "OPTIONS",
        "REGISTER",
        "REINVITE",
        "REREGISTER",
        "ACK",
        "REACK",
        "NOTIFY",
        "RESUBSCRIBE",
        "BYE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIPMethod"

def test_servererrorkind_exists():
    # Check that the Enumeration exists
    assert ServerErrorKind is not None

def test_servererrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServerErrorKind]
    expected_literals = [
        "SERVER_INTERNAL_ERROR",
        "VERSION_NOT_SUPPORTED",
        "NOT_IMPLEMENTED",
        "BAD_GATEWAY",
        "MESSAGE_TOO_LARGE",
        "SERVICE_UNAVAILABLE",
        "SERVER_TIMEOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServerErrorKind"

def test_clienterrorkind_exists():
    # Check that the Enumeration exists
    assert ClientErrorKind is not None

def test_clienterrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClientErrorKind]
    expected_literals = [
        "REQUEST_ENTITY_TOO_LARGE",
        "REQUEST_TIMEOUT",
        "INTERVAL_TOO_BRIEF",
        "REQUEST_TERMINATED",
        "NOT_ACCEPTABLE_HERE",
        "FORBIDDEN",
        "CALL_OR_TRANSACTION_DOES_NOT_EXIST",
        "NOT_FOUND",
        "NOT_ACCEPTABLE",
        "BAD_REQUEST",
        "UNDECIPHERABLE",
        "BAD_EXTENSION",
        "PROXY_AUTHENTICATION_REQUIRED",
        "LOOP_DETECTED",
        "EXTENSION_REQUIRED",
        "TEMPORARILY_UNAVAILABLE",
        "METHOD_NOT_ALLOWED",
        "ADDRESS_INCOMPLETE",
        "AMBIGUOUS",
        "BUSY_HERE",
        "TOO_MANY_HOPS",
        "REQUEST_PENDING",
        "UNAUTHORIZED",
        "REQUESTURI_TOO_LONG",
        "PAYMENT_REQUIRED",
        "UNSUPPORTED_MEDIA_TYPE",
        "GONE",
        "UNSUPPORTED_URI_SCHEME",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClientErrorKind"

def test_controlmethod_exists():
    # Check that the Enumeration exists
    assert ControlMethod is not None

def test_controlmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ControlMethod]
    expected_literals = [
        "uninvite",
        "unregister",
        "undeploy",
        "unsubscribe",
        "deploy",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ControlMethod"

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

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "uri",
        "string",
        "void",
        "time",
        "bool",
        "int",
        "response",
        "request",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"

def test_globalerrorkind_exists():
    # Check that the Enumeration exists
    assert GlobalErrorKind is not None

def test_globalerrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GlobalErrorKind]
    expected_literals = [
        "BUSY_EVERYWHERE",
        "NOT_ACCEPTABLE",
        "DOES_NOT_EXIST_ANYWHERE",
        "DECLINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GlobalErrorKind"

def test_successkind_exists():
    # Check that the Enumeration exists
    assert SuccessKind is not None

def test_successkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SuccessKind]
    expected_literals = [
        "OK",
        "ACCEPTED",
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
        "MAX_FORWARDS",
        "VIA",
        "EVENT",
        "TO",
        "CONTACT",
        "SUBSCRIPTION_STATE",
        "CALL_ID",
        "CSEQ",
        "FROM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIPHeader"

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

def test_redirectionerrorkind_exists():
    # Check that the Enumeration exists
    assert RedirectionErrorKind is not None

def test_redirectionerrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RedirectionErrorKind]
    expected_literals = [
        "ALTERNATIVE_SERVICE",
        "MOVED_TEMPORARILY",
        "USE_PROXY",
        "MULTIPLE_CHOICES",
        "MOVED_PERMANENTLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RedirectionErrorKind"


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
jointPackage::CPL2SPL::TrgSuccessResponse_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSuccessResponse,
    successKind=
        safe_text
)
jointPackage::CPL2SPL::TrgErrorResponse_strategy = st.builds(
    jointPackage::CPL2SPL::TrgErrorResponse,
)
TrgVariablePlace_strategy = st.builds(
    TrgVariablePlace,
)
jointPackage::CPL2SPL::TrgPropertyCallPlace_strategy = st.builds(
    jointPackage::CPL2SPL::TrgPropertyCallPlace,
    propName=
        safe_text
)
jointPackage::CPL2SPL::TrgVariable_strategy = st.builds(
    jointPackage::CPL2SPL::TrgVariable,
)
TrgSelectMember_strategy = st.builds(
    TrgSelectMember,
)
jointPackage::CPL2SPL::TrgSelectCase_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSelectCase,
)
TrgMessageField_strategy = st.builds(
    TrgMessageField,
)
jointPackage::CPL2SPL::TrgHeadedMessageField_strategy = st.builds(
    jointPackage::CPL2SPL::TrgHeadedMessageField,
    headerId=
        safe_text
)
jointPackage::CPL2SPL::TrgReasonMessageField_strategy = st.builds(
    jointPackage::CPL2SPL::TrgReasonMessageField,
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
jointPackage::CPL2SPL::TrgSelectDefault_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSelectDefault,
)
TrgConstant_strategy = st.builds(
    TrgConstant,
)
jointPackage::CPL2SPL::TrgStringConstant_strategy = st.builds(
    jointPackage::CPL2SPL::TrgStringConstant,
    value=
        safe_text
)
jointPackage::CPL2SPL::TrgBooleanConstant_strategy = st.builds(
    jointPackage::CPL2SPL::TrgBooleanConstant,
    value=
        st.booleans()
)
jointPackage::CPL2SPL::TrgSequenceConstant_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSequenceConstant,
)
jointPackage::CPL2SPL::TrgResponseConstant_strategy = st.builds(
    jointPackage::CPL2SPL::TrgResponseConstant,
)
jointPackage::CPL2SPL::TrgIntegerConstant_strategy = st.builds(
    jointPackage::CPL2SPL::TrgIntegerConstant,
    value=
        st.integers()
)
jointPackage::CPL2SPL::TrgURIConstant_strategy = st.builds(
    jointPackage::CPL2SPL::TrgURIConstant,
    uri=
        safe_text
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
jointPackage::CPL2SPL::TrgLocalFunctionDeclaration_strategy = st.builds(
    jointPackage::CPL2SPL::TrgLocalFunctionDeclaration,
)
jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration_strategy = st.builds(
    jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration,
    functionLocation=
        safe_text
)
TrgPlace_strategy = st.builds(
    TrgPlace,
)
jointPackage::CPL2SPL::TrgSIPHeaderPlace_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSIPHeaderPlace,
    header=
        safe_text
)
jointPackage::CPL2SPL::TrgVariablePlace_strategy = st.builds(
    jointPackage::CPL2SPL::TrgVariablePlace,
)
TrgExpression_strategy = st.builds(
    TrgExpression,
)
jointPackage::CPL2SPL::TrgOperatorExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgOperatorExp,
    opName=
        safe_text
)
jointPackage::CPL2SPL::TrgForwardExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgForwardExp,
    isParallel=
        st.booleans()
)
jointPackage::CPL2SPL::TrgPlace_strategy = st.builds(
    jointPackage::CPL2SPL::TrgPlace,
)
jointPackage::CPL2SPL::TrgReasonExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgReasonExp,
)
jointPackage::CPL2SPL::TrgBODYExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgBODYExp,
)
jointPackage::CPL2SPL::TrgConstantExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgConstantExp,
)
jointPackage::CPL2SPL::TrgFunctionCallExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgFunctionCallExp,
)
jointPackage::CPL2SPL::TrgPopExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgPopExp,
)
jointPackage::CPL2SPL::TrgRequestURIExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgRequestURIExp,
)
jointPackage::CPL2SPL::TrgBlockExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgBlockExp,
)
jointPackage::CPL2SPL::TrgWithExp_strategy = st.builds(
    jointPackage::CPL2SPL::TrgWithExp,
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
jointPackage::CPL2SPL::TrgControlMethodName_strategy = st.builds(
    jointPackage::CPL2SPL::TrgControlMethodName,
    name=
        safe_text
)
jointPackage::CPL2SPL::TrgSIPMethodName_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSIPMethodName,
    name=
        safe_text
)
TrgVariableDeclaration_strategy = st.builds(
    TrgVariableDeclaration,
)
jointPackage::CPL2SPL::TrgWhenHeader_strategy = st.builds(
    jointPackage::CPL2SPL::TrgWhenHeader,
    headerId=
        safe_text
)
jointPackage::CPL2SPL::TrgArgument_strategy = st.builds(
    jointPackage::CPL2SPL::TrgArgument,
)
TrgBranch_strategy = st.builds(
    TrgBranch,
)
jointPackage::CPL2SPL::TrgDefaultBranch_strategy = st.builds(
    jointPackage::CPL2SPL::TrgDefaultBranch,
)
jointPackage::CPL2SPL::TrgNamedBranch_strategy = st.builds(
    jointPackage::CPL2SPL::TrgNamedBranch,
    name=
        safe_text
)
TrgStatement_strategy = st.builds(
    TrgStatement,
)
jointPackage::CPL2SPL::TrgForeachStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgForeachStat,
    iteratorName=
        safe_text
)
jointPackage::CPL2SPL::TrgIfStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgIfStat,
)
jointPackage::CPL2SPL::TrgSetStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSetStat,
)
jointPackage::CPL2SPL::TrgReturnStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgReturnStat,
)
jointPackage::CPL2SPL::TrgBreakStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgBreakStat,
)
jointPackage::CPL2SPL::TrgCompoundStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgCompoundStat,
)
jointPackage::CPL2SPL::TrgContinueStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgContinueStat,
)
jointPackage::CPL2SPL::TrgDeclarationStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgDeclarationStat,
)
jointPackage::CPL2SPL::TrgFunctionCallStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgFunctionCallStat,
)
jointPackage::CPL2SPL::TrgWhenStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgWhenStat,
)
jointPackage::CPL2SPL::TrgSelectStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSelectStat,
)
jointPackage::CPL2SPL::TrgPushStat_strategy = st.builds(
    jointPackage::CPL2SPL::TrgPushStat,
)
TrgService_strategy = st.builds(
    TrgService,
)
TrgLocatedElement_strategy = st.builds(
    TrgLocatedElement,
)
jointPackage::CPL2SPL::TrgResponse_strategy = st.builds(
    jointPackage::CPL2SPL::TrgResponse,
)
jointPackage::CPL2SPL::TrgMessageField_strategy = st.builds(
    jointPackage::CPL2SPL::TrgMessageField,
)
jointPackage::CPL2SPL::TrgStatement_strategy = st.builds(
    jointPackage::CPL2SPL::TrgStatement,
)
jointPackage::CPL2SPL::TrgDeclaration_strategy = st.builds(
    jointPackage::CPL2SPL::TrgDeclaration,
    name=
        safe_text
)
jointPackage::CPL2SPL::TrgConstant_strategy = st.builds(
    jointPackage::CPL2SPL::TrgConstant,
)
jointPackage::CPL2SPL::TrgExpression_strategy = st.builds(
    jointPackage::CPL2SPL::TrgExpression,
)
jointPackage::CPL2SPL::TrgBranch_strategy = st.builds(
    jointPackage::CPL2SPL::TrgBranch,
)
jointPackage::CPL2SPL::TrgFunctionCall_strategy = st.builds(
    jointPackage::CPL2SPL::TrgFunctionCall,
)
jointPackage::CPL2SPL::TrgMethodName_strategy = st.builds(
    jointPackage::CPL2SPL::TrgMethodName,
)
jointPackage::CPL2SPL::TrgSelectMember_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSelectMember,
)
jointPackage::CPL2SPL::TrgSession_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSession,
)
jointPackage::CPL2SPL::TrgStructureProperty_strategy = st.builds(
    jointPackage::CPL2SPL::TrgStructureProperty,
    name=
        safe_text
)
jointPackage::CPL2SPL::TrgTypeExpression_strategy = st.builds(
    jointPackage::CPL2SPL::TrgTypeExpression,
)
jointPackage::CPL2SPL::TrgProgram_strategy = st.builds(
    jointPackage::CPL2SPL::TrgProgram,
)
SrcAction_strategy = st.builds(
    SrcAction,
)
jointPackage::CPL2SPL::SrcSignallingAction_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSignallingAction,
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
jointPackage::CPL2SPL::TrgDialog_strategy = st.builds(
    jointPackage::CPL2SPL::TrgDialog,
)
jointPackage::CPL2SPL::TrgMethod_strategy = st.builds(
    jointPackage::CPL2SPL::TrgMethod,
    direction=
        safe_text
)
jointPackage::CPL2SPL::TrgRegistration_strategy = st.builds(
    jointPackage::CPL2SPL::TrgRegistration,
)
jointPackage::CPL2SPL::TrgEvent_strategy = st.builds(
    jointPackage::CPL2SPL::TrgEvent,
    eventId=
        safe_text
)
TrgDeclaration_strategy = st.builds(
    TrgDeclaration,
)
jointPackage::CPL2SPL::TrgVariableDeclaration_strategy = st.builds(
    jointPackage::CPL2SPL::TrgVariableDeclaration,
)
jointPackage::CPL2SPL::TrgStructureDeclaration_strategy = st.builds(
    jointPackage::CPL2SPL::TrgStructureDeclaration,
)
jointPackage::CPL2SPL::TrgFunctionDeclaration_strategy = st.builds(
    jointPackage::CPL2SPL::TrgFunctionDeclaration,
)
jointPackage::CPL2SPL::TrgService_strategy = st.builds(
    jointPackage::CPL2SPL::TrgService,
    name=
        safe_text
)
jointPackage::CPL2SPL::TrgLocatedElement_strategy = st.builds(
    jointPackage::CPL2SPL::TrgLocatedElement,
    commentsAfter=
        safe_text,
    location=
        safe_text,
    commentsBefore=
        safe_text
)
TrgErrorResponse_strategy = st.builds(
    TrgErrorResponse,
)
jointPackage::CPL2SPL::TrgGlobalErrorResponse_strategy = st.builds(
    jointPackage::CPL2SPL::TrgGlobalErrorResponse,
    errorKind=
        safe_text
)
jointPackage::CPL2SPL::TrgServerErrorResponse_strategy = st.builds(
    jointPackage::CPL2SPL::TrgServerErrorResponse,
    errorKind=
        safe_text
)
jointPackage::CPL2SPL::TrgRedirectionErrorResponse_strategy = st.builds(
    jointPackage::CPL2SPL::TrgRedirectionErrorResponse,
    errorKind=
        safe_text
)
jointPackage::CPL2SPL::TrgClientErrorResponse_strategy = st.builds(
    jointPackage::CPL2SPL::TrgClientErrorResponse,
    errorKind=
        safe_text
)
TrgTypeExpression_strategy = st.builds(
    TrgTypeExpression,
)
jointPackage::CPL2SPL::TrgSequenceType_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSequenceType,
    size=
        st.integers(),
    modifier=
        safe_text,
    type=
        safe_text
)
jointPackage::CPL2SPL::TrgDefinedType_strategy = st.builds(
    jointPackage::CPL2SPL::TrgDefinedType,
    typeName=
        safe_text
)
jointPackage::CPL2SPL::TrgSimpleType_strategy = st.builds(
    jointPackage::CPL2SPL::TrgSimpleType,
    type=
        safe_text
)
SrcNode_strategy = st.builds(
    SrcNode,
)
jointPackage::CPL2SPL::SrcSubCall_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSubCall,
    ref=
        safe_text
)
jointPackage::CPL2SPL::SrcSwitch_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSwitch,
)
jointPackage::CPL2SPL::SrcAction_strategy = st.builds(
    jointPackage::CPL2SPL::SrcAction,
)
jointPackage::CPL2SPL::SrcElement_strategy = st.builds(
    jointPackage::CPL2SPL::SrcElement,
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
jointPackage::CPL2SPL::SrcReject_strategy = st.builds(
    jointPackage::CPL2SPL::SrcReject,
    reason=
        safe_text,
    status=
        safe_text
)
jointPackage::CPL2SPL::SrcRedirect_strategy = st.builds(
    jointPackage::CPL2SPL::SrcRedirect,
    permanent=
        safe_text
)
jointPackage::CPL2SPL::SrcProxy_strategy = st.builds(
    jointPackage::CPL2SPL::SrcProxy,
    timeout=
        safe_text,
    recurse=
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
jointPackage::CPL2SPL::SrcNoAnswer_strategy = st.builds(
    jointPackage::CPL2SPL::SrcNoAnswer,
)
jointPackage::CPL2SPL::SrcIncoming_strategy = st.builds(
    jointPackage::CPL2SPL::SrcIncoming,
)
jointPackage::CPL2SPL::SrcOutgoing_strategy = st.builds(
    jointPackage::CPL2SPL::SrcOutgoing,
)
jointPackage::CPL2SPL::SrcDefault_strategy = st.builds(
    jointPackage::CPL2SPL::SrcDefault,
)
jointPackage::CPL2SPL::SrcSwitchedTime_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSwitchedTime,
    byWeekNo=
        safe_text,
    dtend=
        safe_text,
    until=
        safe_text,
    freq=
        safe_text,
    byDay=
        safe_text,
    bySetPos=
        safe_text,
    dtstart=
        safe_text,
    byMonth=
        safe_text,
    count=
        safe_text,
    duration=
        safe_text,
    byMinute=
        safe_text,
    byMonthDay=
        safe_text,
    byYearDay=
        safe_text,
    bySecond=
        safe_text,
    byHour=
        safe_text,
    wkst=
        safe_text,
    interval=
        safe_text
)
jointPackage::CPL2SPL::SrcRedirection_strategy = st.builds(
    jointPackage::CPL2SPL::SrcRedirection,
)
jointPackage::CPL2SPL::SrcSwitchedString_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSwitchedString,
    is_=
        safe_text,
    contains=
        safe_text
)
jointPackage::CPL2SPL::SrcSwitchedAddress_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSwitchedAddress,
    is_=
        safe_text,
    subDomainOf=
        safe_text,
    contains=
        safe_text
)
jointPackage::CPL2SPL::SrcOtherwise_strategy = st.builds(
    jointPackage::CPL2SPL::SrcOtherwise,
)
jointPackage::CPL2SPL::SrcFailure_strategy = st.builds(
    jointPackage::CPL2SPL::SrcFailure,
)
jointPackage::CPL2SPL::SrcBusy_strategy = st.builds(
    jointPackage::CPL2SPL::SrcBusy,
)
jointPackage::CPL2SPL::SrcNotPresent_strategy = st.builds(
    jointPackage::CPL2SPL::SrcNotPresent,
)
jointPackage::CPL2SPL::SrcSwitchedPriority_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSwitchedPriority,
    less=
        safe_text,
    greater=
        safe_text,
    equal=
        safe_text
)
jointPackage::CPL2SPL::SrcLocation_strategy = st.builds(
    jointPackage::CPL2SPL::SrcLocation,
    url=
        safe_text,
    clear=
        safe_text,
    priority=
        safe_text
)
jointPackage::CPL2SPL::SrcSwitchedLanguage_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSwitchedLanguage,
    matches=
        safe_text
)
jointPackage::CPL2SPL::SrcSubAction_strategy = st.builds(
    jointPackage::CPL2SPL::SrcSubAction,
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
jointPackage::CPL2SPL::SrcNode_strategy = st.builds(
    jointPackage::CPL2SPL::SrcNode,
)
jointPackage::CPL2SPL::SrcCPL_strategy = st.builds(
    jointPackage::CPL2SPL::SrcCPL,
)
jointPackage::CPL2SPL::SrcNodeContainer_strategy = st.builds(
    jointPackage::CPL2SPL::SrcNodeContainer,
)
jointPackage::CPL2SPL::SrcCPLModel_strategy = st.builds(
    jointPackage::CPL2SPL::SrcCPLModel,
)
TrgServerErrorResponse_strategy = st.builds(
    TrgServerErrorResponse,
)
SrcReject_strategy = st.builds(
    SrcReject,
)
jointPackage::CPL2SPL::JointMM_strategy = st.builds(
    jointPackage::CPL2SPL::JointMM,
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
jointPackage::CPL2SPL::SrcPrioritySwitch_strategy = st.builds(
    jointPackage::CPL2SPL::SrcPrioritySwitch,
)
jointPackage::CPL2SPL::SrcLanguageSwitch_strategy = st.builds(
    jointPackage::CPL2SPL::SrcLanguageSwitch,
)
jointPackage::CPL2SPL::SrcStringSwitch_strategy = st.builds(
    jointPackage::CPL2SPL::SrcStringSwitch,
    field=
        safe_text
)
jointPackage::CPL2SPL::SrcTimeSwitch_strategy = st.builds(
    jointPackage::CPL2SPL::SrcTimeSwitch,
    tzurl=
        safe_text,
    tzid=
        safe_text
)
jointPackage::CPL2SPL::SrcAddressSwitch_strategy = st.builds(
    jointPackage::CPL2SPL::SrcAddressSwitch,
    subField=
        safe_text,
    field=
        safe_text
)

@given(instance=TrgResponse_strategy)
@settings(max_examples=50)
def test_trgresponse_instantiation(instance):
    assert isinstance(instance, TrgResponse)

@given(instance=jointPackage::CPL2SPL::TrgSuccessResponse_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgsuccessresponse_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSuccessResponse)

@given(instance=jointPackage::CPL2SPL::TrgSuccessResponse_strategy)
def test_jointpackage::cpl2spl::trgsuccessresponse_successKind_type(instance):
    assert isinstance(instance.successKind, str)


@given(instance=jointPackage::CPL2SPL::TrgSuccessResponse_strategy)
def test_jointpackage::cpl2spl::trgsuccessresponse_successKind_setter(instance):
    original = instance.successKind
    instance.successKind = original
    assert instance.successKind == original

@given(instance=jointPackage::CPL2SPL::TrgErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgerrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgErrorResponse)

@given(instance=TrgVariablePlace_strategy)
@settings(max_examples=50)
def test_trgvariableplace_instantiation(instance):
    assert isinstance(instance, TrgVariablePlace)

@given(instance=jointPackage::CPL2SPL::TrgPropertyCallPlace_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgpropertycallplace_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgPropertyCallPlace)

@given(instance=jointPackage::CPL2SPL::TrgPropertyCallPlace_strategy)
def test_jointpackage::cpl2spl::trgpropertycallplace_propName_type(instance):
    assert isinstance(instance.propName, str)


@given(instance=jointPackage::CPL2SPL::TrgPropertyCallPlace_strategy)
def test_jointpackage::cpl2spl::trgpropertycallplace_propName_setter(instance):
    original = instance.propName
    instance.propName = original
    assert instance.propName == original

@given(instance=jointPackage::CPL2SPL::TrgVariable_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgvariable_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgVariable)

@given(instance=TrgSelectMember_strategy)
@settings(max_examples=50)
def test_trgselectmember_instantiation(instance):
    assert isinstance(instance, TrgSelectMember)

@given(instance=jointPackage::CPL2SPL::TrgSelectCase_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgselectcase_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSelectCase)

@given(instance=TrgMessageField_strategy)
@settings(max_examples=50)
def test_trgmessagefield_instantiation(instance):
    assert isinstance(instance, TrgMessageField)

@given(instance=jointPackage::CPL2SPL::TrgHeadedMessageField_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgheadedmessagefield_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgHeadedMessageField)

@given(instance=jointPackage::CPL2SPL::TrgHeadedMessageField_strategy)
def test_jointpackage::cpl2spl::trgheadedmessagefield_headerId_type(instance):
    assert isinstance(instance.headerId, str)


@given(instance=jointPackage::CPL2SPL::TrgHeadedMessageField_strategy)
def test_jointpackage::cpl2spl::trgheadedmessagefield_headerId_setter(instance):
    original = instance.headerId
    instance.headerId = original
    assert instance.headerId == original

@given(instance=jointPackage::CPL2SPL::TrgReasonMessageField_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgreasonmessagefield_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgReasonMessageField)

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

@given(instance=jointPackage::CPL2SPL::TrgSelectDefault_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgselectdefault_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSelectDefault)

@given(instance=TrgConstant_strategy)
@settings(max_examples=50)
def test_trgconstant_instantiation(instance):
    assert isinstance(instance, TrgConstant)

@given(instance=jointPackage::CPL2SPL::TrgStringConstant_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgstringconstant_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgStringConstant)

@given(instance=jointPackage::CPL2SPL::TrgStringConstant_strategy)
def test_jointpackage::cpl2spl::trgstringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=jointPackage::CPL2SPL::TrgStringConstant_strategy)
def test_jointpackage::cpl2spl::trgstringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage::CPL2SPL::TrgBooleanConstant_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgbooleanconstant_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgBooleanConstant)

@given(instance=jointPackage::CPL2SPL::TrgBooleanConstant_strategy)
def test_jointpackage::cpl2spl::trgbooleanconstant_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=jointPackage::CPL2SPL::TrgBooleanConstant_strategy)
def test_jointpackage::cpl2spl::trgbooleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage::CPL2SPL::TrgSequenceConstant_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgsequenceconstant_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSequenceConstant)

@given(instance=jointPackage::CPL2SPL::TrgResponseConstant_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgresponseconstant_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgResponseConstant)

@given(instance=jointPackage::CPL2SPL::TrgIntegerConstant_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgintegerconstant_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgIntegerConstant)

@given(instance=jointPackage::CPL2SPL::TrgIntegerConstant_strategy)
def test_jointpackage::cpl2spl::trgintegerconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=jointPackage::CPL2SPL::TrgIntegerConstant_strategy)
def test_jointpackage::cpl2spl::trgintegerconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage::CPL2SPL::TrgURIConstant_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trguriconstant_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgURIConstant)

@given(instance=jointPackage::CPL2SPL::TrgURIConstant_strategy)
def test_jointpackage::cpl2spl::trguriconstant_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=jointPackage::CPL2SPL::TrgURIConstant_strategy)
def test_jointpackage::cpl2spl::trguriconstant_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

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

@given(instance=jointPackage::CPL2SPL::TrgLocalFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trglocalfunctiondeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgLocalFunctionDeclaration)

@given(instance=jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgremotefunctiondeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration)

@given(instance=jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration_strategy)
def test_jointpackage::cpl2spl::trgremotefunctiondeclaration_functionLocation_type(instance):
    assert isinstance(instance.functionLocation, str)


@given(instance=jointPackage::CPL2SPL::TrgRemoteFunctionDeclaration_strategy)
def test_jointpackage::cpl2spl::trgremotefunctiondeclaration_functionLocation_setter(instance):
    original = instance.functionLocation
    instance.functionLocation = original
    assert instance.functionLocation == original

@given(instance=TrgPlace_strategy)
@settings(max_examples=50)
def test_trgplace_instantiation(instance):
    assert isinstance(instance, TrgPlace)

@given(instance=jointPackage::CPL2SPL::TrgSIPHeaderPlace_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgsipheaderplace_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSIPHeaderPlace)

@given(instance=jointPackage::CPL2SPL::TrgSIPHeaderPlace_strategy)
def test_jointpackage::cpl2spl::trgsipheaderplace_header_type(instance):
    assert isinstance(instance.header, str)


@given(instance=jointPackage::CPL2SPL::TrgSIPHeaderPlace_strategy)
def test_jointpackage::cpl2spl::trgsipheaderplace_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original

@given(instance=jointPackage::CPL2SPL::TrgVariablePlace_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgvariableplace_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgVariablePlace)

@given(instance=TrgExpression_strategy)
@settings(max_examples=50)
def test_trgexpression_instantiation(instance):
    assert isinstance(instance, TrgExpression)

@given(instance=jointPackage::CPL2SPL::TrgOperatorExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgoperatorexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgOperatorExp)

@given(instance=jointPackage::CPL2SPL::TrgOperatorExp_strategy)
def test_jointpackage::cpl2spl::trgoperatorexp_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=jointPackage::CPL2SPL::TrgOperatorExp_strategy)
def test_jointpackage::cpl2spl::trgoperatorexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=jointPackage::CPL2SPL::TrgForwardExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgforwardexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgForwardExp)

@given(instance=jointPackage::CPL2SPL::TrgForwardExp_strategy)
def test_jointpackage::cpl2spl::trgforwardexp_isParallel_type(instance):
    assert isinstance(instance.isParallel, bool)


@given(instance=jointPackage::CPL2SPL::TrgForwardExp_strategy)
def test_jointpackage::cpl2spl::trgforwardexp_isParallel_setter(instance):
    original = instance.isParallel
    instance.isParallel = original
    assert instance.isParallel == original

@given(instance=jointPackage::CPL2SPL::TrgPlace_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgplace_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgPlace)

@given(instance=jointPackage::CPL2SPL::TrgReasonExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgreasonexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgReasonExp)

@given(instance=jointPackage::CPL2SPL::TrgBODYExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgbodyexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgBODYExp)

@given(instance=jointPackage::CPL2SPL::TrgConstantExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgconstantexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgConstantExp)

@given(instance=jointPackage::CPL2SPL::TrgFunctionCallExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgfunctioncallexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgFunctionCallExp)

@given(instance=jointPackage::CPL2SPL::TrgPopExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgpopexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgPopExp)

@given(instance=jointPackage::CPL2SPL::TrgRequestURIExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgrequesturiexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgRequestURIExp)

@given(instance=jointPackage::CPL2SPL::TrgBlockExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgblockexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgBlockExp)

@given(instance=jointPackage::CPL2SPL::TrgWithExp_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgwithexp_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgWithExp)

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

@given(instance=jointPackage::CPL2SPL::TrgControlMethodName_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgcontrolmethodname_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgControlMethodName)

@given(instance=jointPackage::CPL2SPL::TrgControlMethodName_strategy)
def test_jointpackage::cpl2spl::trgcontrolmethodname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::CPL2SPL::TrgControlMethodName_strategy)
def test_jointpackage::cpl2spl::trgcontrolmethodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::CPL2SPL::TrgSIPMethodName_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgsipmethodname_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSIPMethodName)

@given(instance=jointPackage::CPL2SPL::TrgSIPMethodName_strategy)
def test_jointpackage::cpl2spl::trgsipmethodname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::CPL2SPL::TrgSIPMethodName_strategy)
def test_jointpackage::cpl2spl::trgsipmethodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TrgVariableDeclaration_strategy)
@settings(max_examples=50)
def test_trgvariabledeclaration_instantiation(instance):
    assert isinstance(instance, TrgVariableDeclaration)

@given(instance=jointPackage::CPL2SPL::TrgWhenHeader_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgwhenheader_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgWhenHeader)

@given(instance=jointPackage::CPL2SPL::TrgWhenHeader_strategy)
def test_jointpackage::cpl2spl::trgwhenheader_headerId_type(instance):
    assert isinstance(instance.headerId, str)


@given(instance=jointPackage::CPL2SPL::TrgWhenHeader_strategy)
def test_jointpackage::cpl2spl::trgwhenheader_headerId_setter(instance):
    original = instance.headerId
    instance.headerId = original
    assert instance.headerId == original

@given(instance=jointPackage::CPL2SPL::TrgArgument_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgargument_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgArgument)

@given(instance=TrgBranch_strategy)
@settings(max_examples=50)
def test_trgbranch_instantiation(instance):
    assert isinstance(instance, TrgBranch)

@given(instance=jointPackage::CPL2SPL::TrgDefaultBranch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgdefaultbranch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgDefaultBranch)

@given(instance=jointPackage::CPL2SPL::TrgNamedBranch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgnamedbranch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgNamedBranch)

@given(instance=jointPackage::CPL2SPL::TrgNamedBranch_strategy)
def test_jointpackage::cpl2spl::trgnamedbranch_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::CPL2SPL::TrgNamedBranch_strategy)
def test_jointpackage::cpl2spl::trgnamedbranch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TrgStatement_strategy)
@settings(max_examples=50)
def test_trgstatement_instantiation(instance):
    assert isinstance(instance, TrgStatement)

@given(instance=jointPackage::CPL2SPL::TrgForeachStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgforeachstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgForeachStat)

@given(instance=jointPackage::CPL2SPL::TrgForeachStat_strategy)
def test_jointpackage::cpl2spl::trgforeachstat_iteratorName_type(instance):
    assert isinstance(instance.iteratorName, str)


@given(instance=jointPackage::CPL2SPL::TrgForeachStat_strategy)
def test_jointpackage::cpl2spl::trgforeachstat_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=jointPackage::CPL2SPL::TrgIfStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgifstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgIfStat)

@given(instance=jointPackage::CPL2SPL::TrgSetStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgsetstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSetStat)

@given(instance=jointPackage::CPL2SPL::TrgReturnStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgreturnstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgReturnStat)

@given(instance=jointPackage::CPL2SPL::TrgBreakStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgbreakstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgBreakStat)

@given(instance=jointPackage::CPL2SPL::TrgCompoundStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgcompoundstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgCompoundStat)

@given(instance=jointPackage::CPL2SPL::TrgContinueStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgcontinuestat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgContinueStat)

@given(instance=jointPackage::CPL2SPL::TrgDeclarationStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgdeclarationstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgDeclarationStat)

@given(instance=jointPackage::CPL2SPL::TrgFunctionCallStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgfunctioncallstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgFunctionCallStat)

@given(instance=jointPackage::CPL2SPL::TrgWhenStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgwhenstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgWhenStat)

@given(instance=jointPackage::CPL2SPL::TrgSelectStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgselectstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSelectStat)

@given(instance=jointPackage::CPL2SPL::TrgPushStat_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgpushstat_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgPushStat)

@given(instance=TrgService_strategy)
@settings(max_examples=50)
def test_trgservice_instantiation(instance):
    assert isinstance(instance, TrgService)

@given(instance=TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_trglocatedelement_instantiation(instance):
    assert isinstance(instance, TrgLocatedElement)

@given(instance=jointPackage::CPL2SPL::TrgResponse_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgresponse_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgResponse)

@given(instance=jointPackage::CPL2SPL::TrgMessageField_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgmessagefield_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgMessageField)

@given(instance=jointPackage::CPL2SPL::TrgStatement_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgstatement_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgStatement)

@given(instance=jointPackage::CPL2SPL::TrgDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgdeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgDeclaration)

@given(instance=jointPackage::CPL2SPL::TrgDeclaration_strategy)
def test_jointpackage::cpl2spl::trgdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::CPL2SPL::TrgDeclaration_strategy)
def test_jointpackage::cpl2spl::trgdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::CPL2SPL::TrgConstant_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgconstant_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgConstant)

@given(instance=jointPackage::CPL2SPL::TrgExpression_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgexpression_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgExpression)

@given(instance=jointPackage::CPL2SPL::TrgBranch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgbranch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgBranch)

@given(instance=jointPackage::CPL2SPL::TrgFunctionCall_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgfunctioncall_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgFunctionCall)

@given(instance=jointPackage::CPL2SPL::TrgMethodName_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgmethodname_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgMethodName)

@given(instance=jointPackage::CPL2SPL::TrgSelectMember_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgselectmember_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSelectMember)

@given(instance=jointPackage::CPL2SPL::TrgSession_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgsession_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSession)

@given(instance=jointPackage::CPL2SPL::TrgStructureProperty_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgstructureproperty_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgStructureProperty)

@given(instance=jointPackage::CPL2SPL::TrgStructureProperty_strategy)
def test_jointpackage::cpl2spl::trgstructureproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::CPL2SPL::TrgStructureProperty_strategy)
def test_jointpackage::cpl2spl::trgstructureproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::CPL2SPL::TrgTypeExpression_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgtypeexpression_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgTypeExpression)

@given(instance=jointPackage::CPL2SPL::TrgProgram_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgprogram_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgProgram)

@given(instance=SrcAction_strategy)
@settings(max_examples=50)
def test_srcaction_instantiation(instance):
    assert isinstance(instance, SrcAction)

@given(instance=jointPackage::CPL2SPL::SrcSignallingAction_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcsignallingaction_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSignallingAction)

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

@given(instance=jointPackage::CPL2SPL::TrgDialog_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgdialog_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgDialog)

@given(instance=jointPackage::CPL2SPL::TrgMethod_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgmethod_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgMethod)

@given(instance=jointPackage::CPL2SPL::TrgMethod_strategy)
def test_jointpackage::cpl2spl::trgmethod_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=jointPackage::CPL2SPL::TrgMethod_strategy)
def test_jointpackage::cpl2spl::trgmethod_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=jointPackage::CPL2SPL::TrgRegistration_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgregistration_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgRegistration)

@given(instance=jointPackage::CPL2SPL::TrgEvent_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgevent_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgEvent)

@given(instance=jointPackage::CPL2SPL::TrgEvent_strategy)
def test_jointpackage::cpl2spl::trgevent_eventId_type(instance):
    assert isinstance(instance.eventId, str)


@given(instance=jointPackage::CPL2SPL::TrgEvent_strategy)
def test_jointpackage::cpl2spl::trgevent_eventId_setter(instance):
    original = instance.eventId
    instance.eventId = original
    assert instance.eventId == original

@given(instance=TrgDeclaration_strategy)
@settings(max_examples=50)
def test_trgdeclaration_instantiation(instance):
    assert isinstance(instance, TrgDeclaration)

@given(instance=jointPackage::CPL2SPL::TrgVariableDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgvariabledeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgVariableDeclaration)

@given(instance=jointPackage::CPL2SPL::TrgStructureDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgstructuredeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgStructureDeclaration)

@given(instance=jointPackage::CPL2SPL::TrgFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgfunctiondeclaration_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgFunctionDeclaration)

@given(instance=jointPackage::CPL2SPL::TrgService_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgservice_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgService)

@given(instance=jointPackage::CPL2SPL::TrgService_strategy)
def test_jointpackage::cpl2spl::trgservice_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::CPL2SPL::TrgService_strategy)
def test_jointpackage::cpl2spl::trgservice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::CPL2SPL::TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trglocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgLocatedElement)

@given(instance=jointPackage::CPL2SPL::TrgLocatedElement_strategy)
def test_jointpackage::cpl2spl::trglocatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=jointPackage::CPL2SPL::TrgLocatedElement_strategy)
def test_jointpackage::cpl2spl::trglocatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=jointPackage::CPL2SPL::TrgLocatedElement_strategy)
def test_jointpackage::cpl2spl::trglocatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=jointPackage::CPL2SPL::TrgLocatedElement_strategy)
def test_jointpackage::cpl2spl::trglocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=jointPackage::CPL2SPL::TrgLocatedElement_strategy)
def test_jointpackage::cpl2spl::trglocatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=jointPackage::CPL2SPL::TrgLocatedElement_strategy)
def test_jointpackage::cpl2spl::trglocatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=TrgErrorResponse_strategy)
@settings(max_examples=50)
def test_trgerrorresponse_instantiation(instance):
    assert isinstance(instance, TrgErrorResponse)

@given(instance=jointPackage::CPL2SPL::TrgGlobalErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgglobalerrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgGlobalErrorResponse)

@given(instance=jointPackage::CPL2SPL::TrgGlobalErrorResponse_strategy)
def test_jointpackage::cpl2spl::trgglobalerrorresponse_errorKind_type(instance):
    assert isinstance(instance.errorKind, str)


@given(instance=jointPackage::CPL2SPL::TrgGlobalErrorResponse_strategy)
def test_jointpackage::cpl2spl::trgglobalerrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=jointPackage::CPL2SPL::TrgServerErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgservererrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgServerErrorResponse)

@given(instance=jointPackage::CPL2SPL::TrgServerErrorResponse_strategy)
def test_jointpackage::cpl2spl::trgservererrorresponse_errorKind_type(instance):
    assert isinstance(instance.errorKind, str)


@given(instance=jointPackage::CPL2SPL::TrgServerErrorResponse_strategy)
def test_jointpackage::cpl2spl::trgservererrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=jointPackage::CPL2SPL::TrgRedirectionErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgredirectionerrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgRedirectionErrorResponse)

@given(instance=jointPackage::CPL2SPL::TrgRedirectionErrorResponse_strategy)
def test_jointpackage::cpl2spl::trgredirectionerrorresponse_errorKind_type(instance):
    assert isinstance(instance.errorKind, str)


@given(instance=jointPackage::CPL2SPL::TrgRedirectionErrorResponse_strategy)
def test_jointpackage::cpl2spl::trgredirectionerrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=jointPackage::CPL2SPL::TrgClientErrorResponse_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgclienterrorresponse_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgClientErrorResponse)

@given(instance=jointPackage::CPL2SPL::TrgClientErrorResponse_strategy)
def test_jointpackage::cpl2spl::trgclienterrorresponse_errorKind_type(instance):
    assert isinstance(instance.errorKind, str)


@given(instance=jointPackage::CPL2SPL::TrgClientErrorResponse_strategy)
def test_jointpackage::cpl2spl::trgclienterrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=TrgTypeExpression_strategy)
@settings(max_examples=50)
def test_trgtypeexpression_instantiation(instance):
    assert isinstance(instance, TrgTypeExpression)

@given(instance=jointPackage::CPL2SPL::TrgSequenceType_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgsequencetype_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSequenceType)

@given(instance=jointPackage::CPL2SPL::TrgSequenceType_strategy)
def test_jointpackage::cpl2spl::trgsequencetype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=jointPackage::CPL2SPL::TrgSequenceType_strategy)
def test_jointpackage::cpl2spl::trgsequencetype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=jointPackage::CPL2SPL::TrgSequenceType_strategy)
def test_jointpackage::cpl2spl::trgsequencetype_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=jointPackage::CPL2SPL::TrgSequenceType_strategy)
def test_jointpackage::cpl2spl::trgsequencetype_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=jointPackage::CPL2SPL::TrgSequenceType_strategy)
def test_jointpackage::cpl2spl::trgsequencetype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=jointPackage::CPL2SPL::TrgSequenceType_strategy)
def test_jointpackage::cpl2spl::trgsequencetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jointPackage::CPL2SPL::TrgDefinedType_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgdefinedtype_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgDefinedType)

@given(instance=jointPackage::CPL2SPL::TrgDefinedType_strategy)
def test_jointpackage::cpl2spl::trgdefinedtype_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=jointPackage::CPL2SPL::TrgDefinedType_strategy)
def test_jointpackage::cpl2spl::trgdefinedtype_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=jointPackage::CPL2SPL::TrgSimpleType_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::trgsimpletype_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::TrgSimpleType)

@given(instance=jointPackage::CPL2SPL::TrgSimpleType_strategy)
def test_jointpackage::cpl2spl::trgsimpletype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=jointPackage::CPL2SPL::TrgSimpleType_strategy)
def test_jointpackage::cpl2spl::trgsimpletype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SrcNode_strategy)
@settings(max_examples=50)
def test_srcnode_instantiation(instance):
    assert isinstance(instance, SrcNode)

@given(instance=jointPackage::CPL2SPL::SrcSubCall_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcsubcall_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSubCall)

@given(instance=jointPackage::CPL2SPL::SrcSubCall_strategy)
def test_jointpackage::cpl2spl::srcsubcall_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=jointPackage::CPL2SPL::SrcSubCall_strategy)
def test_jointpackage::cpl2spl::srcsubcall_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=jointPackage::CPL2SPL::SrcSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcswitch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSwitch)

@given(instance=jointPackage::CPL2SPL::SrcAction_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcaction_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcAction)

@given(instance=jointPackage::CPL2SPL::SrcElement_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcelement_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcElement)

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

@given(instance=jointPackage::CPL2SPL::SrcReject_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcreject_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcReject)

@given(instance=jointPackage::CPL2SPL::SrcReject_strategy)
def test_jointpackage::cpl2spl::srcreject_reason_type(instance):
    assert isinstance(instance.reason, str)


@given(instance=jointPackage::CPL2SPL::SrcReject_strategy)
def test_jointpackage::cpl2spl::srcreject_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original

@given(instance=jointPackage::CPL2SPL::SrcReject_strategy)
def test_jointpackage::cpl2spl::srcreject_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=jointPackage::CPL2SPL::SrcReject_strategy)
def test_jointpackage::cpl2spl::srcreject_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=jointPackage::CPL2SPL::SrcRedirect_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcredirect_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcRedirect)

@given(instance=jointPackage::CPL2SPL::SrcRedirect_strategy)
def test_jointpackage::cpl2spl::srcredirect_permanent_type(instance):
    assert isinstance(instance.permanent, str)


@given(instance=jointPackage::CPL2SPL::SrcRedirect_strategy)
def test_jointpackage::cpl2spl::srcredirect_permanent_setter(instance):
    original = instance.permanent
    instance.permanent = original
    assert instance.permanent == original

@given(instance=jointPackage::CPL2SPL::SrcProxy_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcproxy_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcProxy)

@given(instance=jointPackage::CPL2SPL::SrcProxy_strategy)
def test_jointpackage::cpl2spl::srcproxy_timeout_type(instance):
    assert isinstance(instance.timeout, str)


@given(instance=jointPackage::CPL2SPL::SrcProxy_strategy)
def test_jointpackage::cpl2spl::srcproxy_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=jointPackage::CPL2SPL::SrcProxy_strategy)
def test_jointpackage::cpl2spl::srcproxy_recurse_type(instance):
    assert isinstance(instance.recurse, str)


@given(instance=jointPackage::CPL2SPL::SrcProxy_strategy)
def test_jointpackage::cpl2spl::srcproxy_recurse_setter(instance):
    original = instance.recurse
    instance.recurse = original
    assert instance.recurse == original

@given(instance=jointPackage::CPL2SPL::SrcProxy_strategy)
def test_jointpackage::cpl2spl::srcproxy_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=jointPackage::CPL2SPL::SrcProxy_strategy)
def test_jointpackage::cpl2spl::srcproxy_ordering_setter(instance):
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

@given(instance=jointPackage::CPL2SPL::SrcNoAnswer_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcnoanswer_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcNoAnswer)

@given(instance=jointPackage::CPL2SPL::SrcIncoming_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcincoming_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcIncoming)

@given(instance=jointPackage::CPL2SPL::SrcOutgoing_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcoutgoing_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcOutgoing)

@given(instance=jointPackage::CPL2SPL::SrcDefault_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcdefault_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcDefault)

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcswitchedtime_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSwitchedTime)

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byWeekNo_type(instance):
    assert isinstance(instance.byWeekNo, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byWeekNo_setter(instance):
    original = instance.byWeekNo
    instance.byWeekNo = original
    assert instance.byWeekNo == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_dtend_type(instance):
    assert isinstance(instance.dtend, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_dtend_setter(instance):
    original = instance.dtend
    instance.dtend = original
    assert instance.dtend == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_until_type(instance):
    assert isinstance(instance.until, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_until_setter(instance):
    original = instance.until
    instance.until = original
    assert instance.until == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_freq_type(instance):
    assert isinstance(instance.freq, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_freq_setter(instance):
    original = instance.freq
    instance.freq = original
    assert instance.freq == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byDay_type(instance):
    assert isinstance(instance.byDay, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byDay_setter(instance):
    original = instance.byDay
    instance.byDay = original
    assert instance.byDay == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_bySetPos_type(instance):
    assert isinstance(instance.bySetPos, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_bySetPos_setter(instance):
    original = instance.bySetPos
    instance.bySetPos = original
    assert instance.bySetPos == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_dtstart_type(instance):
    assert isinstance(instance.dtstart, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_dtstart_setter(instance):
    original = instance.dtstart
    instance.dtstart = original
    assert instance.dtstart == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byMonth_type(instance):
    assert isinstance(instance.byMonth, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byMonth_setter(instance):
    original = instance.byMonth
    instance.byMonth = original
    assert instance.byMonth == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_count_type(instance):
    assert isinstance(instance.count, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byMinute_type(instance):
    assert isinstance(instance.byMinute, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byMinute_setter(instance):
    original = instance.byMinute
    instance.byMinute = original
    assert instance.byMinute == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byMonthDay_type(instance):
    assert isinstance(instance.byMonthDay, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byMonthDay_setter(instance):
    original = instance.byMonthDay
    instance.byMonthDay = original
    assert instance.byMonthDay == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byYearDay_type(instance):
    assert isinstance(instance.byYearDay, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byYearDay_setter(instance):
    original = instance.byYearDay
    instance.byYearDay = original
    assert instance.byYearDay == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_bySecond_type(instance):
    assert isinstance(instance.bySecond, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_bySecond_setter(instance):
    original = instance.bySecond
    instance.bySecond = original
    assert instance.bySecond == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byHour_type(instance):
    assert isinstance(instance.byHour, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_byHour_setter(instance):
    original = instance.byHour
    instance.byHour = original
    assert instance.byHour == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_wkst_type(instance):
    assert isinstance(instance.wkst, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_wkst_setter(instance):
    original = instance.wkst
    instance.wkst = original
    assert instance.wkst == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_interval_type(instance):
    assert isinstance(instance.interval, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedTime_strategy)
def test_jointpackage::cpl2spl::srcswitchedtime_interval_setter(instance):
    original = instance.interval
    instance.interval = original
    assert instance.interval == original

@given(instance=jointPackage::CPL2SPL::SrcRedirection_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcredirection_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcRedirection)

@given(instance=jointPackage::CPL2SPL::SrcSwitchedString_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcswitchedstring_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSwitchedString)

@given(instance=jointPackage::CPL2SPL::SrcSwitchedString_strategy)
def test_jointpackage::cpl2spl::srcswitchedstring_is__type(instance):
    assert isinstance(instance.is_, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedString_strategy)
def test_jointpackage::cpl2spl::srcswitchedstring_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedString_strategy)
def test_jointpackage::cpl2spl::srcswitchedstring_contains_type(instance):
    assert isinstance(instance.contains, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedString_strategy)
def test_jointpackage::cpl2spl::srcswitchedstring_contains_setter(instance):
    original = instance.contains
    instance.contains = original
    assert instance.contains == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedAddress_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcswitchedaddress_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSwitchedAddress)

@given(instance=jointPackage::CPL2SPL::SrcSwitchedAddress_strategy)
def test_jointpackage::cpl2spl::srcswitchedaddress_is__type(instance):
    assert isinstance(instance.is_, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedAddress_strategy)
def test_jointpackage::cpl2spl::srcswitchedaddress_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedAddress_strategy)
def test_jointpackage::cpl2spl::srcswitchedaddress_subDomainOf_type(instance):
    assert isinstance(instance.subDomainOf, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedAddress_strategy)
def test_jointpackage::cpl2spl::srcswitchedaddress_subDomainOf_setter(instance):
    original = instance.subDomainOf
    instance.subDomainOf = original
    assert instance.subDomainOf == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedAddress_strategy)
def test_jointpackage::cpl2spl::srcswitchedaddress_contains_type(instance):
    assert isinstance(instance.contains, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedAddress_strategy)
def test_jointpackage::cpl2spl::srcswitchedaddress_contains_setter(instance):
    original = instance.contains
    instance.contains = original
    assert instance.contains == original

@given(instance=jointPackage::CPL2SPL::SrcOtherwise_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcotherwise_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcOtherwise)

@given(instance=jointPackage::CPL2SPL::SrcFailure_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcfailure_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcFailure)

@given(instance=jointPackage::CPL2SPL::SrcBusy_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcbusy_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcBusy)

@given(instance=jointPackage::CPL2SPL::SrcNotPresent_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcnotpresent_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcNotPresent)

@given(instance=jointPackage::CPL2SPL::SrcSwitchedPriority_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcswitchedpriority_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSwitchedPriority)

@given(instance=jointPackage::CPL2SPL::SrcSwitchedPriority_strategy)
def test_jointpackage::cpl2spl::srcswitchedpriority_less_type(instance):
    assert isinstance(instance.less, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedPriority_strategy)
def test_jointpackage::cpl2spl::srcswitchedpriority_less_setter(instance):
    original = instance.less
    instance.less = original
    assert instance.less == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedPriority_strategy)
def test_jointpackage::cpl2spl::srcswitchedpriority_greater_type(instance):
    assert isinstance(instance.greater, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedPriority_strategy)
def test_jointpackage::cpl2spl::srcswitchedpriority_greater_setter(instance):
    original = instance.greater
    instance.greater = original
    assert instance.greater == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedPriority_strategy)
def test_jointpackage::cpl2spl::srcswitchedpriority_equal_type(instance):
    assert isinstance(instance.equal, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedPriority_strategy)
def test_jointpackage::cpl2spl::srcswitchedpriority_equal_setter(instance):
    original = instance.equal
    instance.equal = original
    assert instance.equal == original

@given(instance=jointPackage::CPL2SPL::SrcLocation_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srclocation_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcLocation)

@given(instance=jointPackage::CPL2SPL::SrcLocation_strategy)
def test_jointpackage::cpl2spl::srclocation_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=jointPackage::CPL2SPL::SrcLocation_strategy)
def test_jointpackage::cpl2spl::srclocation_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=jointPackage::CPL2SPL::SrcLocation_strategy)
def test_jointpackage::cpl2spl::srclocation_clear_type(instance):
    assert isinstance(instance.clear, str)


@given(instance=jointPackage::CPL2SPL::SrcLocation_strategy)
def test_jointpackage::cpl2spl::srclocation_clear_setter(instance):
    original = instance.clear
    instance.clear = original
    assert instance.clear == original

@given(instance=jointPackage::CPL2SPL::SrcLocation_strategy)
def test_jointpackage::cpl2spl::srclocation_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=jointPackage::CPL2SPL::SrcLocation_strategy)
def test_jointpackage::cpl2spl::srclocation_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=jointPackage::CPL2SPL::SrcSwitchedLanguage_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcswitchedlanguage_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSwitchedLanguage)

@given(instance=jointPackage::CPL2SPL::SrcSwitchedLanguage_strategy)
def test_jointpackage::cpl2spl::srcswitchedlanguage_matches_type(instance):
    assert isinstance(instance.matches, str)


@given(instance=jointPackage::CPL2SPL::SrcSwitchedLanguage_strategy)
def test_jointpackage::cpl2spl::srcswitchedlanguage_matches_setter(instance):
    original = instance.matches
    instance.matches = original
    assert instance.matches == original

@given(instance=jointPackage::CPL2SPL::SrcSubAction_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcsubaction_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcSubAction)

@given(instance=jointPackage::CPL2SPL::SrcSubAction_strategy)
def test_jointpackage::cpl2spl::srcsubaction_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=jointPackage::CPL2SPL::SrcSubAction_strategy)
def test_jointpackage::cpl2spl::srcsubaction_id_setter(instance):
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

@given(instance=jointPackage::CPL2SPL::SrcNode_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcnode_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcNode)

@given(instance=jointPackage::CPL2SPL::SrcCPL_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srccpl_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcCPL)

@given(instance=jointPackage::CPL2SPL::SrcNodeContainer_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcnodecontainer_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcNodeContainer)

@given(instance=jointPackage::CPL2SPL::SrcCPLModel_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srccplmodel_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcCPLModel)

@given(instance=TrgServerErrorResponse_strategy)
@settings(max_examples=50)
def test_trgservererrorresponse_instantiation(instance):
    assert isinstance(instance, TrgServerErrorResponse)

@given(instance=SrcReject_strategy)
@settings(max_examples=50)
def test_srcreject_instantiation(instance):
    assert isinstance(instance, SrcReject)

@given(instance=jointPackage::CPL2SPL::JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::JointMM)

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

@given(instance=jointPackage::CPL2SPL::SrcPrioritySwitch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcpriorityswitch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcPrioritySwitch)

@given(instance=jointPackage::CPL2SPL::SrcLanguageSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srclanguageswitch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcLanguageSwitch)

@given(instance=jointPackage::CPL2SPL::SrcStringSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcstringswitch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcStringSwitch)

@given(instance=jointPackage::CPL2SPL::SrcStringSwitch_strategy)
def test_jointpackage::cpl2spl::srcstringswitch_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=jointPackage::CPL2SPL::SrcStringSwitch_strategy)
def test_jointpackage::cpl2spl::srcstringswitch_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=jointPackage::CPL2SPL::SrcTimeSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srctimeswitch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcTimeSwitch)

@given(instance=jointPackage::CPL2SPL::SrcTimeSwitch_strategy)
def test_jointpackage::cpl2spl::srctimeswitch_tzurl_type(instance):
    assert isinstance(instance.tzurl, str)


@given(instance=jointPackage::CPL2SPL::SrcTimeSwitch_strategy)
def test_jointpackage::cpl2spl::srctimeswitch_tzurl_setter(instance):
    original = instance.tzurl
    instance.tzurl = original
    assert instance.tzurl == original

@given(instance=jointPackage::CPL2SPL::SrcTimeSwitch_strategy)
def test_jointpackage::cpl2spl::srctimeswitch_tzid_type(instance):
    assert isinstance(instance.tzid, str)


@given(instance=jointPackage::CPL2SPL::SrcTimeSwitch_strategy)
def test_jointpackage::cpl2spl::srctimeswitch_tzid_setter(instance):
    original = instance.tzid
    instance.tzid = original
    assert instance.tzid == original

@given(instance=jointPackage::CPL2SPL::SrcAddressSwitch_strategy)
@settings(max_examples=50)
def test_jointpackage::cpl2spl::srcaddressswitch_instantiation(instance):
    assert isinstance(instance, jointPackage::CPL2SPL::SrcAddressSwitch)

@given(instance=jointPackage::CPL2SPL::SrcAddressSwitch_strategy)
def test_jointpackage::cpl2spl::srcaddressswitch_subField_type(instance):
    assert isinstance(instance.subField, str)


@given(instance=jointPackage::CPL2SPL::SrcAddressSwitch_strategy)
def test_jointpackage::cpl2spl::srcaddressswitch_subField_setter(instance):
    original = instance.subField
    instance.subField = original
    assert instance.subField == original

@given(instance=jointPackage::CPL2SPL::SrcAddressSwitch_strategy)
def test_jointpackage::cpl2spl::srcaddressswitch_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=jointPackage::CPL2SPL::SrcAddressSwitch_strategy)
def test_jointpackage::cpl2spl::srcaddressswitch_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original
