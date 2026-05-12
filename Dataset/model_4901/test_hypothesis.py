import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ErrorResponse,
    SPL_GlobalErrorResponse,
    SPL_ServerErrorResponse,
    SPL_RedirectionErrorResponse,
    SPL_ClientErrorResponse,
    Response,
    SPL_ErrorResponse,
    SPL_SuccessResponse,
    Constant,
    SPL_StringConstant,
    SPL_IntegerConstant,
    SPL_URIConstant,
    SPL_BooleanConstant,
    MessageField,
    SPL_HeadedMessageField,
    SPL_ReasonMessageField,
    VariablePlace,
    SPL_PropertyCallPlace,
    Place,
    SPL_VariablePlace,
    SPL_SIPHeaderPlace,
    SPL_ResponseConstant,
    SPL_SequenceConstant,
    Expression,
    SPL_BODYExp,
    SPL_OperatorExp,
    SPL_BlockExp,
    SPL_ForwardExp,
    SPL_ReasonExp,
    SPL_WithExp,
    SPL_ConstantExp,
    SPL_FunctionCallExp,
    SPL_PopExp,
    SPL_RequestURIExp,
    SelectMember,
    SPL_SelectDefault,
    SPL_SelectCase,
    SPL_Place,
    Statement,
    SPL_BreakStat,
    SPL_PushStat,
    SPL_ReturnStat,
    SPL_SetStat,
    SPL_ForeachStat,
    SPL_FunctionCallStat,
    SPL_IfStat,
    SPL_WhenStat,
    SPL_SelectStat,
    SPL_DeclarationStat,
    SPL_ContinueStat,
    SPL_CompoundStat,
    SPL_Variable,
    FunctionDeclaration,
    SPL_LocalFunctionDeclaration,
    SPL_RemoteFunctionDeclaration,
    Declaration,
    SPL_FunctionDeclaration,
    SPL_StructureDeclaration,
    SPL_VariableDeclaration,
    Branch,
    SPL_NamedBranch,
    SPL_DefaultBranch,
    MethodName,
    SPL_ControlMethodName,
    SPL_SIPMethodName,
    VariableDeclaration,
    SPL_WhenHeader,
    SPL_Argument,
    TypeExpression,
    SPL_DefinedType,
    SPL_SequenceType,
    SPL_SimpleType,
    Session,
    SPL_Dialog,
    SPL_Event,
    SPL_Method,
    SPL_Registration,
    LocatedElement,
    SPL_Declaration,
    SPL_Service,
    SPL_Constant,
    SPL_Statement,
    SPL_MessageField,
    SPL_Expression,
    SPL_StructureProperty,
    SPL_MethodName,
    SPL_Response,
    SPL_FunctionCall,
    SPL_SelectMember,
    SPL_Branch,
    SPL_Session,
    SPL_Program,
    SPL_TypeExpression,
    SPL_LocatedElement,
    ClientErrorKind,
    ControlMethod,
    ServerErrorKind,
    Direction,
    FunctionLocation,
    RedirectionErrorKind,
    PrimitiveType,
    GlobalErrorKind,
    Modifier,
    SuccessKind,
    SIPHeader,
    SIPMethod,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_errorresponse_is_not_abstract():
    assert not inspect.isabstract(ErrorResponse)


def test_errorresponse_constructor_exists():
    assert callable(ErrorResponse.__init__)


def test_errorresponse_constructor_args():
    sig = inspect.signature(ErrorResponse.__init__)
    params = list(sig.parameters.keys())



def test_spl_globalerrorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL_GlobalErrorResponse)


def test_spl_globalerrorresponse_constructor_exists():
    assert callable(SPL_GlobalErrorResponse.__init__)


def test_spl_globalerrorresponse_constructor_args():
    sig = inspect.signature(SPL_GlobalErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_spl_globalerrorresponse_has_errorKind():
    assert hasattr(SPL_GlobalErrorResponse, "errorKind")
    descriptor = None
    for klass in SPL_GlobalErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_spl_servererrorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL_ServerErrorResponse)


def test_spl_servererrorresponse_constructor_exists():
    assert callable(SPL_ServerErrorResponse.__init__)


def test_spl_servererrorresponse_constructor_args():
    sig = inspect.signature(SPL_ServerErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_spl_servererrorresponse_has_errorKind():
    assert hasattr(SPL_ServerErrorResponse, "errorKind")
    descriptor = None
    for klass in SPL_ServerErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_spl_redirectionerrorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL_RedirectionErrorResponse)


def test_spl_redirectionerrorresponse_constructor_exists():
    assert callable(SPL_RedirectionErrorResponse.__init__)


def test_spl_redirectionerrorresponse_constructor_args():
    sig = inspect.signature(SPL_RedirectionErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_spl_redirectionerrorresponse_has_errorKind():
    assert hasattr(SPL_RedirectionErrorResponse, "errorKind")
    descriptor = None
    for klass in SPL_RedirectionErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_spl_clienterrorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL_ClientErrorResponse)


def test_spl_clienterrorresponse_constructor_exists():
    assert callable(SPL_ClientErrorResponse.__init__)


def test_spl_clienterrorresponse_constructor_args():
    sig = inspect.signature(SPL_ClientErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_spl_clienterrorresponse_has_errorKind():
    assert hasattr(SPL_ClientErrorResponse, "errorKind")
    descriptor = None
    for klass in SPL_ClientErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_response_is_not_abstract():
    assert not inspect.isabstract(Response)


def test_response_constructor_exists():
    assert callable(Response.__init__)


def test_response_constructor_args():
    sig = inspect.signature(Response.__init__)
    params = list(sig.parameters.keys())



def test_spl_errorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL_ErrorResponse)


def test_spl_errorresponse_constructor_exists():
    assert callable(SPL_ErrorResponse.__init__)


def test_spl_errorresponse_constructor_args():
    sig = inspect.signature(SPL_ErrorResponse.__init__)
    params = list(sig.parameters.keys())



def test_spl_successresponse_is_not_abstract():
    assert not inspect.isabstract(SPL_SuccessResponse)


def test_spl_successresponse_constructor_exists():
    assert callable(SPL_SuccessResponse.__init__)


def test_spl_successresponse_constructor_args():
    sig = inspect.signature(SPL_SuccessResponse.__init__)
    params = list(sig.parameters.keys())
    assert "successKind" in params, "Missing parameter 'successKind'"

def test_spl_successresponse_has_successKind():
    assert hasattr(SPL_SuccessResponse, "successKind")
    descriptor = None
    for klass in SPL_SuccessResponse.__mro__:
        if "successKind" in klass.__dict__:
            descriptor = klass.__dict__["successKind"]
            break
    assert isinstance(descriptor, property)



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_spl_stringconstant_is_not_abstract():
    assert not inspect.isabstract(SPL_StringConstant)


def test_spl_stringconstant_constructor_exists():
    assert callable(SPL_StringConstant.__init__)


def test_spl_stringconstant_constructor_args():
    sig = inspect.signature(SPL_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spl_stringconstant_has_value():
    assert hasattr(SPL_StringConstant, "value")
    descriptor = None
    for klass in SPL_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spl_integerconstant_is_not_abstract():
    assert not inspect.isabstract(SPL_IntegerConstant)


def test_spl_integerconstant_constructor_exists():
    assert callable(SPL_IntegerConstant.__init__)


def test_spl_integerconstant_constructor_args():
    sig = inspect.signature(SPL_IntegerConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spl_integerconstant_has_value():
    assert hasattr(SPL_IntegerConstant, "value")
    descriptor = None
    for klass in SPL_IntegerConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spl_uriconstant_is_not_abstract():
    assert not inspect.isabstract(SPL_URIConstant)


def test_spl_uriconstant_constructor_exists():
    assert callable(SPL_URIConstant.__init__)


def test_spl_uriconstant_constructor_args():
    sig = inspect.signature(SPL_URIConstant.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_spl_uriconstant_has_uri():
    assert hasattr(SPL_URIConstant, "uri")
    descriptor = None
    for klass in SPL_URIConstant.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_spl_booleanconstant_is_not_abstract():
    assert not inspect.isabstract(SPL_BooleanConstant)


def test_spl_booleanconstant_constructor_exists():
    assert callable(SPL_BooleanConstant.__init__)


def test_spl_booleanconstant_constructor_args():
    sig = inspect.signature(SPL_BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spl_booleanconstant_has_value():
    assert hasattr(SPL_BooleanConstant, "value")
    descriptor = None
    for klass in SPL_BooleanConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_messagefield_is_not_abstract():
    assert not inspect.isabstract(MessageField)


def test_messagefield_constructor_exists():
    assert callable(MessageField.__init__)


def test_messagefield_constructor_args():
    sig = inspect.signature(MessageField.__init__)
    params = list(sig.parameters.keys())



def test_spl_headedmessagefield_is_not_abstract():
    assert not inspect.isabstract(SPL_HeadedMessageField)


def test_spl_headedmessagefield_constructor_exists():
    assert callable(SPL_HeadedMessageField.__init__)


def test_spl_headedmessagefield_constructor_args():
    sig = inspect.signature(SPL_HeadedMessageField.__init__)
    params = list(sig.parameters.keys())
    assert "headerId" in params, "Missing parameter 'headerId'"

def test_spl_headedmessagefield_has_headerId():
    assert hasattr(SPL_HeadedMessageField, "headerId")
    descriptor = None
    for klass in SPL_HeadedMessageField.__mro__:
        if "headerId" in klass.__dict__:
            descriptor = klass.__dict__["headerId"]
            break
    assert isinstance(descriptor, property)



def test_spl_reasonmessagefield_is_not_abstract():
    assert not inspect.isabstract(SPL_ReasonMessageField)


def test_spl_reasonmessagefield_constructor_exists():
    assert callable(SPL_ReasonMessageField.__init__)


def test_spl_reasonmessagefield_constructor_args():
    sig = inspect.signature(SPL_ReasonMessageField.__init__)
    params = list(sig.parameters.keys())



def test_variableplace_is_not_abstract():
    assert not inspect.isabstract(VariablePlace)


def test_variableplace_constructor_exists():
    assert callable(VariablePlace.__init__)


def test_variableplace_constructor_args():
    sig = inspect.signature(VariablePlace.__init__)
    params = list(sig.parameters.keys())



def test_spl_propertycallplace_is_not_abstract():
    assert not inspect.isabstract(SPL_PropertyCallPlace)


def test_spl_propertycallplace_constructor_exists():
    assert callable(SPL_PropertyCallPlace.__init__)


def test_spl_propertycallplace_constructor_args():
    sig = inspect.signature(SPL_PropertyCallPlace.__init__)
    params = list(sig.parameters.keys())
    assert "propName" in params, "Missing parameter 'propName'"

def test_spl_propertycallplace_has_propName():
    assert hasattr(SPL_PropertyCallPlace, "propName")
    descriptor = None
    for klass in SPL_PropertyCallPlace.__mro__:
        if "propName" in klass.__dict__:
            descriptor = klass.__dict__["propName"]
            break
    assert isinstance(descriptor, property)



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_spl_variableplace_is_not_abstract():
    assert not inspect.isabstract(SPL_VariablePlace)


def test_spl_variableplace_constructor_exists():
    assert callable(SPL_VariablePlace.__init__)


def test_spl_variableplace_constructor_args():
    sig = inspect.signature(SPL_VariablePlace.__init__)
    params = list(sig.parameters.keys())



def test_spl_sipheaderplace_is_not_abstract():
    assert not inspect.isabstract(SPL_SIPHeaderPlace)


def test_spl_sipheaderplace_constructor_exists():
    assert callable(SPL_SIPHeaderPlace.__init__)


def test_spl_sipheaderplace_constructor_args():
    sig = inspect.signature(SPL_SIPHeaderPlace.__init__)
    params = list(sig.parameters.keys())
    assert "header" in params, "Missing parameter 'header'"

def test_spl_sipheaderplace_has_header():
    assert hasattr(SPL_SIPHeaderPlace, "header")
    descriptor = None
    for klass in SPL_SIPHeaderPlace.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)



def test_spl_responseconstant_is_not_abstract():
    assert not inspect.isabstract(SPL_ResponseConstant)


def test_spl_responseconstant_constructor_exists():
    assert callable(SPL_ResponseConstant.__init__)


def test_spl_responseconstant_constructor_args():
    sig = inspect.signature(SPL_ResponseConstant.__init__)
    params = list(sig.parameters.keys())



def test_spl_sequenceconstant_is_not_abstract():
    assert not inspect.isabstract(SPL_SequenceConstant)


def test_spl_sequenceconstant_constructor_exists():
    assert callable(SPL_SequenceConstant.__init__)


def test_spl_sequenceconstant_constructor_args():
    sig = inspect.signature(SPL_SequenceConstant.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_spl_bodyexp_is_not_abstract():
    assert not inspect.isabstract(SPL_BODYExp)


def test_spl_bodyexp_constructor_exists():
    assert callable(SPL_BODYExp.__init__)


def test_spl_bodyexp_constructor_args():
    sig = inspect.signature(SPL_BODYExp.__init__)
    params = list(sig.parameters.keys())



def test_spl_operatorexp_is_not_abstract():
    assert not inspect.isabstract(SPL_OperatorExp)


def test_spl_operatorexp_constructor_exists():
    assert callable(SPL_OperatorExp.__init__)


def test_spl_operatorexp_constructor_args():
    sig = inspect.signature(SPL_OperatorExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_spl_operatorexp_has_opName():
    assert hasattr(SPL_OperatorExp, "opName")
    descriptor = None
    for klass in SPL_OperatorExp.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_spl_blockexp_is_not_abstract():
    assert not inspect.isabstract(SPL_BlockExp)


def test_spl_blockexp_constructor_exists():
    assert callable(SPL_BlockExp.__init__)


def test_spl_blockexp_constructor_args():
    sig = inspect.signature(SPL_BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_spl_forwardexp_is_not_abstract():
    assert not inspect.isabstract(SPL_ForwardExp)


def test_spl_forwardexp_constructor_exists():
    assert callable(SPL_ForwardExp.__init__)


def test_spl_forwardexp_constructor_args():
    sig = inspect.signature(SPL_ForwardExp.__init__)
    params = list(sig.parameters.keys())
    assert "isParallel" in params, "Missing parameter 'isParallel'"

def test_spl_forwardexp_has_isParallel():
    assert hasattr(SPL_ForwardExp, "isParallel")
    descriptor = None
    for klass in SPL_ForwardExp.__mro__:
        if "isParallel" in klass.__dict__:
            descriptor = klass.__dict__["isParallel"]
            break
    assert isinstance(descriptor, property)



def test_spl_reasonexp_is_not_abstract():
    assert not inspect.isabstract(SPL_ReasonExp)


def test_spl_reasonexp_constructor_exists():
    assert callable(SPL_ReasonExp.__init__)


def test_spl_reasonexp_constructor_args():
    sig = inspect.signature(SPL_ReasonExp.__init__)
    params = list(sig.parameters.keys())



def test_spl_withexp_is_not_abstract():
    assert not inspect.isabstract(SPL_WithExp)


def test_spl_withexp_constructor_exists():
    assert callable(SPL_WithExp.__init__)


def test_spl_withexp_constructor_args():
    sig = inspect.signature(SPL_WithExp.__init__)
    params = list(sig.parameters.keys())



def test_spl_constantexp_is_not_abstract():
    assert not inspect.isabstract(SPL_ConstantExp)


def test_spl_constantexp_constructor_exists():
    assert callable(SPL_ConstantExp.__init__)


def test_spl_constantexp_constructor_args():
    sig = inspect.signature(SPL_ConstantExp.__init__)
    params = list(sig.parameters.keys())



def test_spl_functioncallexp_is_not_abstract():
    assert not inspect.isabstract(SPL_FunctionCallExp)


def test_spl_functioncallexp_constructor_exists():
    assert callable(SPL_FunctionCallExp.__init__)


def test_spl_functioncallexp_constructor_args():
    sig = inspect.signature(SPL_FunctionCallExp.__init__)
    params = list(sig.parameters.keys())



def test_spl_popexp_is_not_abstract():
    assert not inspect.isabstract(SPL_PopExp)


def test_spl_popexp_constructor_exists():
    assert callable(SPL_PopExp.__init__)


def test_spl_popexp_constructor_args():
    sig = inspect.signature(SPL_PopExp.__init__)
    params = list(sig.parameters.keys())



def test_spl_requesturiexp_is_not_abstract():
    assert not inspect.isabstract(SPL_RequestURIExp)


def test_spl_requesturiexp_constructor_exists():
    assert callable(SPL_RequestURIExp.__init__)


def test_spl_requesturiexp_constructor_args():
    sig = inspect.signature(SPL_RequestURIExp.__init__)
    params = list(sig.parameters.keys())



def test_selectmember_is_not_abstract():
    assert not inspect.isabstract(SelectMember)


def test_selectmember_constructor_exists():
    assert callable(SelectMember.__init__)


def test_selectmember_constructor_args():
    sig = inspect.signature(SelectMember.__init__)
    params = list(sig.parameters.keys())



def test_spl_selectdefault_is_not_abstract():
    assert not inspect.isabstract(SPL_SelectDefault)


def test_spl_selectdefault_constructor_exists():
    assert callable(SPL_SelectDefault.__init__)


def test_spl_selectdefault_constructor_args():
    sig = inspect.signature(SPL_SelectDefault.__init__)
    params = list(sig.parameters.keys())



def test_spl_selectcase_is_not_abstract():
    assert not inspect.isabstract(SPL_SelectCase)


def test_spl_selectcase_constructor_exists():
    assert callable(SPL_SelectCase.__init__)


def test_spl_selectcase_constructor_args():
    sig = inspect.signature(SPL_SelectCase.__init__)
    params = list(sig.parameters.keys())



def test_spl_place_is_not_abstract():
    assert not inspect.isabstract(SPL_Place)


def test_spl_place_constructor_exists():
    assert callable(SPL_Place.__init__)


def test_spl_place_constructor_args():
    sig = inspect.signature(SPL_Place.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_spl_breakstat_is_not_abstract():
    assert not inspect.isabstract(SPL_BreakStat)


def test_spl_breakstat_constructor_exists():
    assert callable(SPL_BreakStat.__init__)


def test_spl_breakstat_constructor_args():
    sig = inspect.signature(SPL_BreakStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_pushstat_is_not_abstract():
    assert not inspect.isabstract(SPL_PushStat)


def test_spl_pushstat_constructor_exists():
    assert callable(SPL_PushStat.__init__)


def test_spl_pushstat_constructor_args():
    sig = inspect.signature(SPL_PushStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_returnstat_is_not_abstract():
    assert not inspect.isabstract(SPL_ReturnStat)


def test_spl_returnstat_constructor_exists():
    assert callable(SPL_ReturnStat.__init__)


def test_spl_returnstat_constructor_args():
    sig = inspect.signature(SPL_ReturnStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_setstat_is_not_abstract():
    assert not inspect.isabstract(SPL_SetStat)


def test_spl_setstat_constructor_exists():
    assert callable(SPL_SetStat.__init__)


def test_spl_setstat_constructor_args():
    sig = inspect.signature(SPL_SetStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_foreachstat_is_not_abstract():
    assert not inspect.isabstract(SPL_ForeachStat)


def test_spl_foreachstat_constructor_exists():
    assert callable(SPL_ForeachStat.__init__)


def test_spl_foreachstat_constructor_args():
    sig = inspect.signature(SPL_ForeachStat.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_spl_foreachstat_has_iteratorName():
    assert hasattr(SPL_ForeachStat, "iteratorName")
    descriptor = None
    for klass in SPL_ForeachStat.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_spl_functioncallstat_is_not_abstract():
    assert not inspect.isabstract(SPL_FunctionCallStat)


def test_spl_functioncallstat_constructor_exists():
    assert callable(SPL_FunctionCallStat.__init__)


def test_spl_functioncallstat_constructor_args():
    sig = inspect.signature(SPL_FunctionCallStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_ifstat_is_not_abstract():
    assert not inspect.isabstract(SPL_IfStat)


def test_spl_ifstat_constructor_exists():
    assert callable(SPL_IfStat.__init__)


def test_spl_ifstat_constructor_args():
    sig = inspect.signature(SPL_IfStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_whenstat_is_not_abstract():
    assert not inspect.isabstract(SPL_WhenStat)


def test_spl_whenstat_constructor_exists():
    assert callable(SPL_WhenStat.__init__)


def test_spl_whenstat_constructor_args():
    sig = inspect.signature(SPL_WhenStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_selectstat_is_not_abstract():
    assert not inspect.isabstract(SPL_SelectStat)


def test_spl_selectstat_constructor_exists():
    assert callable(SPL_SelectStat.__init__)


def test_spl_selectstat_constructor_args():
    sig = inspect.signature(SPL_SelectStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_declarationstat_is_not_abstract():
    assert not inspect.isabstract(SPL_DeclarationStat)


def test_spl_declarationstat_constructor_exists():
    assert callable(SPL_DeclarationStat.__init__)


def test_spl_declarationstat_constructor_args():
    sig = inspect.signature(SPL_DeclarationStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_continuestat_is_not_abstract():
    assert not inspect.isabstract(SPL_ContinueStat)


def test_spl_continuestat_constructor_exists():
    assert callable(SPL_ContinueStat.__init__)


def test_spl_continuestat_constructor_args():
    sig = inspect.signature(SPL_ContinueStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_compoundstat_is_not_abstract():
    assert not inspect.isabstract(SPL_CompoundStat)


def test_spl_compoundstat_constructor_exists():
    assert callable(SPL_CompoundStat.__init__)


def test_spl_compoundstat_constructor_args():
    sig = inspect.signature(SPL_CompoundStat.__init__)
    params = list(sig.parameters.keys())



def test_spl_variable_is_not_abstract():
    assert not inspect.isabstract(SPL_Variable)


def test_spl_variable_constructor_exists():
    assert callable(SPL_Variable.__init__)


def test_spl_variable_constructor_args():
    sig = inspect.signature(SPL_Variable.__init__)
    params = list(sig.parameters.keys())



def test_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(FunctionDeclaration)


def test_functiondeclaration_constructor_exists():
    assert callable(FunctionDeclaration.__init__)


def test_functiondeclaration_constructor_args():
    sig = inspect.signature(FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl_localfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL_LocalFunctionDeclaration)


def test_spl_localfunctiondeclaration_constructor_exists():
    assert callable(SPL_LocalFunctionDeclaration.__init__)


def test_spl_localfunctiondeclaration_constructor_args():
    sig = inspect.signature(SPL_LocalFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl_remotefunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL_RemoteFunctionDeclaration)


def test_spl_remotefunctiondeclaration_constructor_exists():
    assert callable(SPL_RemoteFunctionDeclaration.__init__)


def test_spl_remotefunctiondeclaration_constructor_args():
    sig = inspect.signature(SPL_RemoteFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionLocation" in params, "Missing parameter 'functionLocation'"

def test_spl_remotefunctiondeclaration_has_functionLocation():
    assert hasattr(SPL_RemoteFunctionDeclaration, "functionLocation")
    descriptor = None
    for klass in SPL_RemoteFunctionDeclaration.__mro__:
        if "functionLocation" in klass.__dict__:
            descriptor = klass.__dict__["functionLocation"]
            break
    assert isinstance(descriptor, property)



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_spl_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL_FunctionDeclaration)


def test_spl_functiondeclaration_constructor_exists():
    assert callable(SPL_FunctionDeclaration.__init__)


def test_spl_functiondeclaration_constructor_args():
    sig = inspect.signature(SPL_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl_structuredeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL_StructureDeclaration)


def test_spl_structuredeclaration_constructor_exists():
    assert callable(SPL_StructureDeclaration.__init__)


def test_spl_structuredeclaration_constructor_args():
    sig = inspect.signature(SPL_StructureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL_VariableDeclaration)


def test_spl_variabledeclaration_constructor_exists():
    assert callable(SPL_VariableDeclaration.__init__)


def test_spl_variabledeclaration_constructor_args():
    sig = inspect.signature(SPL_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_branch_is_not_abstract():
    assert not inspect.isabstract(Branch)


def test_branch_constructor_exists():
    assert callable(Branch.__init__)


def test_branch_constructor_args():
    sig = inspect.signature(Branch.__init__)
    params = list(sig.parameters.keys())



def test_spl_namedbranch_is_not_abstract():
    assert not inspect.isabstract(SPL_NamedBranch)


def test_spl_namedbranch_constructor_exists():
    assert callable(SPL_NamedBranch.__init__)


def test_spl_namedbranch_constructor_args():
    sig = inspect.signature(SPL_NamedBranch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl_namedbranch_has_name():
    assert hasattr(SPL_NamedBranch, "name")
    descriptor = None
    for klass in SPL_NamedBranch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl_defaultbranch_is_not_abstract():
    assert not inspect.isabstract(SPL_DefaultBranch)


def test_spl_defaultbranch_constructor_exists():
    assert callable(SPL_DefaultBranch.__init__)


def test_spl_defaultbranch_constructor_args():
    sig = inspect.signature(SPL_DefaultBranch.__init__)
    params = list(sig.parameters.keys())



def test_methodname_is_not_abstract():
    assert not inspect.isabstract(MethodName)


def test_methodname_constructor_exists():
    assert callable(MethodName.__init__)


def test_methodname_constructor_args():
    sig = inspect.signature(MethodName.__init__)
    params = list(sig.parameters.keys())



def test_spl_controlmethodname_is_not_abstract():
    assert not inspect.isabstract(SPL_ControlMethodName)


def test_spl_controlmethodname_constructor_exists():
    assert callable(SPL_ControlMethodName.__init__)


def test_spl_controlmethodname_constructor_args():
    sig = inspect.signature(SPL_ControlMethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl_controlmethodname_has_name():
    assert hasattr(SPL_ControlMethodName, "name")
    descriptor = None
    for klass in SPL_ControlMethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl_sipmethodname_is_not_abstract():
    assert not inspect.isabstract(SPL_SIPMethodName)


def test_spl_sipmethodname_constructor_exists():
    assert callable(SPL_SIPMethodName.__init__)


def test_spl_sipmethodname_constructor_args():
    sig = inspect.signature(SPL_SIPMethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl_sipmethodname_has_name():
    assert hasattr(SPL_SIPMethodName, "name")
    descriptor = None
    for klass in SPL_SIPMethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl_whenheader_is_not_abstract():
    assert not inspect.isabstract(SPL_WhenHeader)


def test_spl_whenheader_constructor_exists():
    assert callable(SPL_WhenHeader.__init__)


def test_spl_whenheader_constructor_args():
    sig = inspect.signature(SPL_WhenHeader.__init__)
    params = list(sig.parameters.keys())
    assert "headerId" in params, "Missing parameter 'headerId'"

def test_spl_whenheader_has_headerId():
    assert hasattr(SPL_WhenHeader, "headerId")
    descriptor = None
    for klass in SPL_WhenHeader.__mro__:
        if "headerId" in klass.__dict__:
            descriptor = klass.__dict__["headerId"]
            break
    assert isinstance(descriptor, property)



def test_spl_argument_is_not_abstract():
    assert not inspect.isabstract(SPL_Argument)


def test_spl_argument_constructor_exists():
    assert callable(SPL_Argument.__init__)


def test_spl_argument_constructor_args():
    sig = inspect.signature(SPL_Argument.__init__)
    params = list(sig.parameters.keys())



def test_typeexpression_is_not_abstract():
    assert not inspect.isabstract(TypeExpression)


def test_typeexpression_constructor_exists():
    assert callable(TypeExpression.__init__)


def test_typeexpression_constructor_args():
    sig = inspect.signature(TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_spl_definedtype_is_not_abstract():
    assert not inspect.isabstract(SPL_DefinedType)


def test_spl_definedtype_constructor_exists():
    assert callable(SPL_DefinedType.__init__)


def test_spl_definedtype_constructor_args():
    sig = inspect.signature(SPL_DefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_spl_definedtype_has_typeName():
    assert hasattr(SPL_DefinedType, "typeName")
    descriptor = None
    for klass in SPL_DefinedType.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_spl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(SPL_SequenceType)


def test_spl_sequencetype_constructor_exists():
    assert callable(SPL_SequenceType.__init__)


def test_spl_sequencetype_constructor_args():
    sig = inspect.signature(SPL_SequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "type" in params, "Missing parameter 'type'"
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_spl_sequencetype_has_size():
    assert hasattr(SPL_SequenceType, "size")
    descriptor = None
    for klass in SPL_SequenceType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_spl_sequencetype_has_type():
    assert hasattr(SPL_SequenceType, "type")
    descriptor = None
    for klass in SPL_SequenceType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_spl_sequencetype_has_modifier():
    assert hasattr(SPL_SequenceType, "modifier")
    descriptor = None
    for klass in SPL_SequenceType.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_spl_simpletype_is_not_abstract():
    assert not inspect.isabstract(SPL_SimpleType)


def test_spl_simpletype_constructor_exists():
    assert callable(SPL_SimpleType.__init__)


def test_spl_simpletype_constructor_args():
    sig = inspect.signature(SPL_SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_spl_simpletype_has_type():
    assert hasattr(SPL_SimpleType, "type")
    descriptor = None
    for klass in SPL_SimpleType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_session_is_not_abstract():
    assert not inspect.isabstract(Session)


def test_session_constructor_exists():
    assert callable(Session.__init__)


def test_session_constructor_args():
    sig = inspect.signature(Session.__init__)
    params = list(sig.parameters.keys())



def test_spl_dialog_is_not_abstract():
    assert not inspect.isabstract(SPL_Dialog)


def test_spl_dialog_constructor_exists():
    assert callable(SPL_Dialog.__init__)


def test_spl_dialog_constructor_args():
    sig = inspect.signature(SPL_Dialog.__init__)
    params = list(sig.parameters.keys())



def test_spl_event_is_not_abstract():
    assert not inspect.isabstract(SPL_Event)


def test_spl_event_constructor_exists():
    assert callable(SPL_Event.__init__)


def test_spl_event_constructor_args():
    sig = inspect.signature(SPL_Event.__init__)
    params = list(sig.parameters.keys())
    assert "eventId" in params, "Missing parameter 'eventId'"

def test_spl_event_has_eventId():
    assert hasattr(SPL_Event, "eventId")
    descriptor = None
    for klass in SPL_Event.__mro__:
        if "eventId" in klass.__dict__:
            descriptor = klass.__dict__["eventId"]
            break
    assert isinstance(descriptor, property)



def test_spl_method_is_not_abstract():
    assert not inspect.isabstract(SPL_Method)


def test_spl_method_constructor_exists():
    assert callable(SPL_Method.__init__)


def test_spl_method_constructor_args():
    sig = inspect.signature(SPL_Method.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_spl_method_has_direction():
    assert hasattr(SPL_Method, "direction")
    descriptor = None
    for klass in SPL_Method.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_spl_registration_is_not_abstract():
    assert not inspect.isabstract(SPL_Registration)


def test_spl_registration_constructor_exists():
    assert callable(SPL_Registration.__init__)


def test_spl_registration_constructor_args():
    sig = inspect.signature(SPL_Registration.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_spl_declaration_is_not_abstract():
    assert not inspect.isabstract(SPL_Declaration)


def test_spl_declaration_constructor_exists():
    assert callable(SPL_Declaration.__init__)


def test_spl_declaration_constructor_args():
    sig = inspect.signature(SPL_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl_declaration_has_name():
    assert hasattr(SPL_Declaration, "name")
    descriptor = None
    for klass in SPL_Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl_service_is_not_abstract():
    assert not inspect.isabstract(SPL_Service)


def test_spl_service_constructor_exists():
    assert callable(SPL_Service.__init__)


def test_spl_service_constructor_args():
    sig = inspect.signature(SPL_Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl_service_has_name():
    assert hasattr(SPL_Service, "name")
    descriptor = None
    for klass in SPL_Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl_constant_is_not_abstract():
    assert not inspect.isabstract(SPL_Constant)


def test_spl_constant_constructor_exists():
    assert callable(SPL_Constant.__init__)


def test_spl_constant_constructor_args():
    sig = inspect.signature(SPL_Constant.__init__)
    params = list(sig.parameters.keys())



def test_spl_statement_is_not_abstract():
    assert not inspect.isabstract(SPL_Statement)


def test_spl_statement_constructor_exists():
    assert callable(SPL_Statement.__init__)


def test_spl_statement_constructor_args():
    sig = inspect.signature(SPL_Statement.__init__)
    params = list(sig.parameters.keys())



def test_spl_messagefield_is_not_abstract():
    assert not inspect.isabstract(SPL_MessageField)


def test_spl_messagefield_constructor_exists():
    assert callable(SPL_MessageField.__init__)


def test_spl_messagefield_constructor_args():
    sig = inspect.signature(SPL_MessageField.__init__)
    params = list(sig.parameters.keys())



def test_spl_expression_is_not_abstract():
    assert not inspect.isabstract(SPL_Expression)


def test_spl_expression_constructor_exists():
    assert callable(SPL_Expression.__init__)


def test_spl_expression_constructor_args():
    sig = inspect.signature(SPL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_spl_structureproperty_is_not_abstract():
    assert not inspect.isabstract(SPL_StructureProperty)


def test_spl_structureproperty_constructor_exists():
    assert callable(SPL_StructureProperty.__init__)


def test_spl_structureproperty_constructor_args():
    sig = inspect.signature(SPL_StructureProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl_structureproperty_has_name():
    assert hasattr(SPL_StructureProperty, "name")
    descriptor = None
    for klass in SPL_StructureProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl_methodname_is_not_abstract():
    assert not inspect.isabstract(SPL_MethodName)


def test_spl_methodname_constructor_exists():
    assert callable(SPL_MethodName.__init__)


def test_spl_methodname_constructor_args():
    sig = inspect.signature(SPL_MethodName.__init__)
    params = list(sig.parameters.keys())



def test_spl_response_is_not_abstract():
    assert not inspect.isabstract(SPL_Response)


def test_spl_response_constructor_exists():
    assert callable(SPL_Response.__init__)


def test_spl_response_constructor_args():
    sig = inspect.signature(SPL_Response.__init__)
    params = list(sig.parameters.keys())



def test_spl_functioncall_is_not_abstract():
    assert not inspect.isabstract(SPL_FunctionCall)


def test_spl_functioncall_constructor_exists():
    assert callable(SPL_FunctionCall.__init__)


def test_spl_functioncall_constructor_args():
    sig = inspect.signature(SPL_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_spl_selectmember_is_not_abstract():
    assert not inspect.isabstract(SPL_SelectMember)


def test_spl_selectmember_constructor_exists():
    assert callable(SPL_SelectMember.__init__)


def test_spl_selectmember_constructor_args():
    sig = inspect.signature(SPL_SelectMember.__init__)
    params = list(sig.parameters.keys())



def test_spl_branch_is_not_abstract():
    assert not inspect.isabstract(SPL_Branch)


def test_spl_branch_constructor_exists():
    assert callable(SPL_Branch.__init__)


def test_spl_branch_constructor_args():
    sig = inspect.signature(SPL_Branch.__init__)
    params = list(sig.parameters.keys())



def test_spl_session_is_not_abstract():
    assert not inspect.isabstract(SPL_Session)


def test_spl_session_constructor_exists():
    assert callable(SPL_Session.__init__)


def test_spl_session_constructor_args():
    sig = inspect.signature(SPL_Session.__init__)
    params = list(sig.parameters.keys())



def test_spl_program_is_not_abstract():
    assert not inspect.isabstract(SPL_Program)


def test_spl_program_constructor_exists():
    assert callable(SPL_Program.__init__)


def test_spl_program_constructor_args():
    sig = inspect.signature(SPL_Program.__init__)
    params = list(sig.parameters.keys())



def test_spl_typeexpression_is_not_abstract():
    assert not inspect.isabstract(SPL_TypeExpression)


def test_spl_typeexpression_constructor_exists():
    assert callable(SPL_TypeExpression.__init__)


def test_spl_typeexpression_constructor_args():
    sig = inspect.signature(SPL_TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_spl_locatedelement_is_not_abstract():
    assert not inspect.isabstract(SPL_LocatedElement)


def test_spl_locatedelement_constructor_exists():
    assert callable(SPL_LocatedElement.__init__)


def test_spl_locatedelement_constructor_args():
    sig = inspect.signature(SPL_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"

def test_spl_locatedelement_has_commentsAfter():
    assert hasattr(SPL_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in SPL_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_spl_locatedelement_has_commentsBefore():
    assert hasattr(SPL_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in SPL_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_spl_locatedelement_has_location():
    assert hasattr(SPL_LocatedElement, "location")
    descriptor = None
    for klass in SPL_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_clienterrorkind_exists():
    # Check that the Enumeration exists
    assert ClientErrorKind is not None

def test_clienterrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClientErrorKind]
    expected_literals = [
        "FORBIDDEN",
        "TEMPORARILY_UNAVAILABLE",
        "NOT_ACCEPTABLE_HERE",
        "BUSY_HERE",
        "REQUEST_ENTITY_TOO_LARGE",
        "PROXY_AUTHENTICATION_REQUIRED",
        "LOOP_DETECTED",
        "GONE",
        "BAD_EXTENSION",
        "UNSUPPORTED_URI_SCHEME",
        "CALL_OR_TRANSACTION_DOES_NOT_EXIST",
        "EXTENSION_REQUIRED",
        "REQUEST_TERMINATED",
        "INTERVAL_TOO_BRIEF",
        "REQUEST_PENDING",
        "REQUESTURI_TOO_LONG",
        "PAYMENT_REQUIRED",
        "BAD_REQUEST",
        "TOO_MANY_HOPS",
        "ADDRESS_INCOMPLETE",
        "METHOD_NOT_ALLOWED",
        "REQUEST_TIMEOUT",
        "NOT_ACCEPTABLE",
        "AMBIGUOUS",
        "NOT_FOUND",
        "UNAUTHORIZED",
        "UNSUPPORTED_MEDIA_TYPE",
        "UNDECIPHERABLE",
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
        "unsubscribe",
        "uninvite",
        "unregister",
        "deploy",
        "undeploy",
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
        "SERVICE_UNAVAILABLE",
        "MESSAGE_TOO_LARGE",
        "SERVER_INTERNAL_ERROR",
        "VERSION_NOT_SUPPORTED",
        "SERVER_TIMEOUT",
        "NOT_IMPLEMENTED",
        "BAD_GATEWAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServerErrorKind"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "in_",
        "inout",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_functionlocation_exists():
    # Check that the Enumeration exists
    assert FunctionLocation is not None

def test_functionlocation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionLocation]
    expected_literals = [
        "remote",
        "local",
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
        "MOVED_PERMANENTLY",
        "MULTIPLE_CHOICES",
        "MOVED_TEMPORARILY",
        "ALTERNATIVE_SERVICE",
        "USE_PROXY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RedirectionErrorKind"

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "void",
        "uri",
        "int",
        "string",
        "time",
        "bool",
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
        "EVENT",
        "MAX_FORWARDS",
        "FROM",
        "SUBSCRIPTION_STATE",
        "CSEQ",
        "VIA",
        "TO",
        "CONTACT",
        "CALL_ID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIPHeader"

def test_sipmethod_exists():
    # Check that the Enumeration exists
    assert SIPMethod is not None

def test_sipmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIPMethod]
    expected_literals = [
        "REACK",
        "REREGISTER",
        "CANCEL",
        "INVITE",
        "REINVITE",
        "BYE",
        "RESUBSCRIBE",
        "OPTIONS",
        "SUBSCRIBE",
        "NOTIFY",
        "REGISTER",
        "ACK",
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
ErrorResponse_strategy = st.builds(
    ErrorResponse,
)
SPL_GlobalErrorResponse_strategy = st.builds(
    SPL_GlobalErrorResponse,
    errorKind=
        safe_text
)
SPL_ServerErrorResponse_strategy = st.builds(
    SPL_ServerErrorResponse,
    errorKind=
        safe_text
)
SPL_RedirectionErrorResponse_strategy = st.builds(
    SPL_RedirectionErrorResponse,
    errorKind=
        safe_text
)
SPL_ClientErrorResponse_strategy = st.builds(
    SPL_ClientErrorResponse,
    errorKind=
        safe_text
)
Response_strategy = st.builds(
    Response,
)
SPL_ErrorResponse_strategy = st.builds(
    SPL_ErrorResponse,
)
SPL_SuccessResponse_strategy = st.builds(
    SPL_SuccessResponse,
    successKind=
        safe_text
)
Constant_strategy = st.builds(
    Constant,
)
SPL_StringConstant_strategy = st.builds(
    SPL_StringConstant,
    value=
        safe_text
)
SPL_IntegerConstant_strategy = st.builds(
    SPL_IntegerConstant,
    value=
        st.integers()
)
SPL_URIConstant_strategy = st.builds(
    SPL_URIConstant,
    uri=
        safe_text
)
SPL_BooleanConstant_strategy = st.builds(
    SPL_BooleanConstant,
    value=
        st.booleans()
)
MessageField_strategy = st.builds(
    MessageField,
)
SPL_HeadedMessageField_strategy = st.builds(
    SPL_HeadedMessageField,
    headerId=
        safe_text
)
SPL_ReasonMessageField_strategy = st.builds(
    SPL_ReasonMessageField,
)
VariablePlace_strategy = st.builds(
    VariablePlace,
)
SPL_PropertyCallPlace_strategy = st.builds(
    SPL_PropertyCallPlace,
    propName=
        safe_text
)
Place_strategy = st.builds(
    Place,
)
SPL_VariablePlace_strategy = st.builds(
    SPL_VariablePlace,
)
SPL_SIPHeaderPlace_strategy = st.builds(
    SPL_SIPHeaderPlace,
    header=
        safe_text
)
SPL_ResponseConstant_strategy = st.builds(
    SPL_ResponseConstant,
)
SPL_SequenceConstant_strategy = st.builds(
    SPL_SequenceConstant,
)
Expression_strategy = st.builds(
    Expression,
)
SPL_BODYExp_strategy = st.builds(
    SPL_BODYExp,
)
SPL_OperatorExp_strategy = st.builds(
    SPL_OperatorExp,
    opName=
        safe_text
)
SPL_BlockExp_strategy = st.builds(
    SPL_BlockExp,
)
SPL_ForwardExp_strategy = st.builds(
    SPL_ForwardExp,
    isParallel=
        st.booleans()
)
SPL_ReasonExp_strategy = st.builds(
    SPL_ReasonExp,
)
SPL_WithExp_strategy = st.builds(
    SPL_WithExp,
)
SPL_ConstantExp_strategy = st.builds(
    SPL_ConstantExp,
)
SPL_FunctionCallExp_strategy = st.builds(
    SPL_FunctionCallExp,
)
SPL_PopExp_strategy = st.builds(
    SPL_PopExp,
)
SPL_RequestURIExp_strategy = st.builds(
    SPL_RequestURIExp,
)
SelectMember_strategy = st.builds(
    SelectMember,
)
SPL_SelectDefault_strategy = st.builds(
    SPL_SelectDefault,
)
SPL_SelectCase_strategy = st.builds(
    SPL_SelectCase,
)
SPL_Place_strategy = st.builds(
    SPL_Place,
)
Statement_strategy = st.builds(
    Statement,
)
SPL_BreakStat_strategy = st.builds(
    SPL_BreakStat,
)
SPL_PushStat_strategy = st.builds(
    SPL_PushStat,
)
SPL_ReturnStat_strategy = st.builds(
    SPL_ReturnStat,
)
SPL_SetStat_strategy = st.builds(
    SPL_SetStat,
)
SPL_ForeachStat_strategy = st.builds(
    SPL_ForeachStat,
    iteratorName=
        safe_text
)
SPL_FunctionCallStat_strategy = st.builds(
    SPL_FunctionCallStat,
)
SPL_IfStat_strategy = st.builds(
    SPL_IfStat,
)
SPL_WhenStat_strategy = st.builds(
    SPL_WhenStat,
)
SPL_SelectStat_strategy = st.builds(
    SPL_SelectStat,
)
SPL_DeclarationStat_strategy = st.builds(
    SPL_DeclarationStat,
)
SPL_ContinueStat_strategy = st.builds(
    SPL_ContinueStat,
)
SPL_CompoundStat_strategy = st.builds(
    SPL_CompoundStat,
)
SPL_Variable_strategy = st.builds(
    SPL_Variable,
)
FunctionDeclaration_strategy = st.builds(
    FunctionDeclaration,
)
SPL_LocalFunctionDeclaration_strategy = st.builds(
    SPL_LocalFunctionDeclaration,
)
SPL_RemoteFunctionDeclaration_strategy = st.builds(
    SPL_RemoteFunctionDeclaration,
    functionLocation=
        safe_text
)
Declaration_strategy = st.builds(
    Declaration,
)
SPL_FunctionDeclaration_strategy = st.builds(
    SPL_FunctionDeclaration,
)
SPL_StructureDeclaration_strategy = st.builds(
    SPL_StructureDeclaration,
)
SPL_VariableDeclaration_strategy = st.builds(
    SPL_VariableDeclaration,
)
Branch_strategy = st.builds(
    Branch,
)
SPL_NamedBranch_strategy = st.builds(
    SPL_NamedBranch,
    name=
        safe_text
)
SPL_DefaultBranch_strategy = st.builds(
    SPL_DefaultBranch,
)
MethodName_strategy = st.builds(
    MethodName,
)
SPL_ControlMethodName_strategy = st.builds(
    SPL_ControlMethodName,
    name=
        safe_text
)
SPL_SIPMethodName_strategy = st.builds(
    SPL_SIPMethodName,
    name=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
SPL_WhenHeader_strategy = st.builds(
    SPL_WhenHeader,
    headerId=
        safe_text
)
SPL_Argument_strategy = st.builds(
    SPL_Argument,
)
TypeExpression_strategy = st.builds(
    TypeExpression,
)
SPL_DefinedType_strategy = st.builds(
    SPL_DefinedType,
    typeName=
        safe_text
)
SPL_SequenceType_strategy = st.builds(
    SPL_SequenceType,
    size=
        st.integers(),
    type=
        safe_text,
    modifier=
        safe_text
)
SPL_SimpleType_strategy = st.builds(
    SPL_SimpleType,
    type=
        safe_text
)
Session_strategy = st.builds(
    Session,
)
SPL_Dialog_strategy = st.builds(
    SPL_Dialog,
)
SPL_Event_strategy = st.builds(
    SPL_Event,
    eventId=
        safe_text
)
SPL_Method_strategy = st.builds(
    SPL_Method,
    direction=
        safe_text
)
SPL_Registration_strategy = st.builds(
    SPL_Registration,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
SPL_Declaration_strategy = st.builds(
    SPL_Declaration,
    name=
        safe_text
)
SPL_Service_strategy = st.builds(
    SPL_Service,
    name=
        safe_text
)
SPL_Constant_strategy = st.builds(
    SPL_Constant,
)
SPL_Statement_strategy = st.builds(
    SPL_Statement,
)
SPL_MessageField_strategy = st.builds(
    SPL_MessageField,
)
SPL_Expression_strategy = st.builds(
    SPL_Expression,
)
SPL_StructureProperty_strategy = st.builds(
    SPL_StructureProperty,
    name=
        safe_text
)
SPL_MethodName_strategy = st.builds(
    SPL_MethodName,
)
SPL_Response_strategy = st.builds(
    SPL_Response,
)
SPL_FunctionCall_strategy = st.builds(
    SPL_FunctionCall,
)
SPL_SelectMember_strategy = st.builds(
    SPL_SelectMember,
)
SPL_Branch_strategy = st.builds(
    SPL_Branch,
)
SPL_Session_strategy = st.builds(
    SPL_Session,
)
SPL_Program_strategy = st.builds(
    SPL_Program,
)
SPL_TypeExpression_strategy = st.builds(
    SPL_TypeExpression,
)
SPL_LocatedElement_strategy = st.builds(
    SPL_LocatedElement,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)

@given(instance=ErrorResponse_strategy)
@settings(max_examples=50)
def test_errorresponse_instantiation(instance):
    assert isinstance(instance, ErrorResponse)

@given(instance=SPL_GlobalErrorResponse_strategy)
@settings(max_examples=50)
def test_spl_globalerrorresponse_instantiation(instance):
    assert isinstance(instance, SPL_GlobalErrorResponse)



@given(instance=SPL_GlobalErrorResponse_strategy)
def test_spl_globalerrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=SPL_ServerErrorResponse_strategy)
@settings(max_examples=50)
def test_spl_servererrorresponse_instantiation(instance):
    assert isinstance(instance, SPL_ServerErrorResponse)



@given(instance=SPL_ServerErrorResponse_strategy)
def test_spl_servererrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=SPL_RedirectionErrorResponse_strategy)
@settings(max_examples=50)
def test_spl_redirectionerrorresponse_instantiation(instance):
    assert isinstance(instance, SPL_RedirectionErrorResponse)



@given(instance=SPL_RedirectionErrorResponse_strategy)
def test_spl_redirectionerrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=SPL_ClientErrorResponse_strategy)
@settings(max_examples=50)
def test_spl_clienterrorresponse_instantiation(instance):
    assert isinstance(instance, SPL_ClientErrorResponse)



@given(instance=SPL_ClientErrorResponse_strategy)
def test_spl_clienterrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=Response_strategy)
@settings(max_examples=50)
def test_response_instantiation(instance):
    assert isinstance(instance, Response)

@given(instance=SPL_ErrorResponse_strategy)
@settings(max_examples=50)
def test_spl_errorresponse_instantiation(instance):
    assert isinstance(instance, SPL_ErrorResponse)

@given(instance=SPL_SuccessResponse_strategy)
@settings(max_examples=50)
def test_spl_successresponse_instantiation(instance):
    assert isinstance(instance, SPL_SuccessResponse)



@given(instance=SPL_SuccessResponse_strategy)
def test_spl_successresponse_successKind_setter(instance):
    original = instance.successKind
    instance.successKind = original
    assert instance.successKind == original

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=SPL_StringConstant_strategy)
@settings(max_examples=50)
def test_spl_stringconstant_instantiation(instance):
    assert isinstance(instance, SPL_StringConstant)



@given(instance=SPL_StringConstant_strategy)
def test_spl_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SPL_IntegerConstant_strategy)
@settings(max_examples=50)
def test_spl_integerconstant_instantiation(instance):
    assert isinstance(instance, SPL_IntegerConstant)



@given(instance=SPL_IntegerConstant_strategy)
def test_spl_integerconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SPL_URIConstant_strategy)
@settings(max_examples=50)
def test_spl_uriconstant_instantiation(instance):
    assert isinstance(instance, SPL_URIConstant)



@given(instance=SPL_URIConstant_strategy)
def test_spl_uriconstant_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=SPL_BooleanConstant_strategy)
@settings(max_examples=50)
def test_spl_booleanconstant_instantiation(instance):
    assert isinstance(instance, SPL_BooleanConstant)



@given(instance=SPL_BooleanConstant_strategy)
def test_spl_booleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MessageField_strategy)
@settings(max_examples=50)
def test_messagefield_instantiation(instance):
    assert isinstance(instance, MessageField)

@given(instance=SPL_HeadedMessageField_strategy)
@settings(max_examples=50)
def test_spl_headedmessagefield_instantiation(instance):
    assert isinstance(instance, SPL_HeadedMessageField)



@given(instance=SPL_HeadedMessageField_strategy)
def test_spl_headedmessagefield_headerId_setter(instance):
    original = instance.headerId
    instance.headerId = original
    assert instance.headerId == original

@given(instance=SPL_ReasonMessageField_strategy)
@settings(max_examples=50)
def test_spl_reasonmessagefield_instantiation(instance):
    assert isinstance(instance, SPL_ReasonMessageField)

@given(instance=VariablePlace_strategy)
@settings(max_examples=50)
def test_variableplace_instantiation(instance):
    assert isinstance(instance, VariablePlace)

@given(instance=SPL_PropertyCallPlace_strategy)
@settings(max_examples=50)
def test_spl_propertycallplace_instantiation(instance):
    assert isinstance(instance, SPL_PropertyCallPlace)



@given(instance=SPL_PropertyCallPlace_strategy)
def test_spl_propertycallplace_propName_setter(instance):
    original = instance.propName
    instance.propName = original
    assert instance.propName == original

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=SPL_VariablePlace_strategy)
@settings(max_examples=50)
def test_spl_variableplace_instantiation(instance):
    assert isinstance(instance, SPL_VariablePlace)

@given(instance=SPL_SIPHeaderPlace_strategy)
@settings(max_examples=50)
def test_spl_sipheaderplace_instantiation(instance):
    assert isinstance(instance, SPL_SIPHeaderPlace)



@given(instance=SPL_SIPHeaderPlace_strategy)
def test_spl_sipheaderplace_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original

@given(instance=SPL_ResponseConstant_strategy)
@settings(max_examples=50)
def test_spl_responseconstant_instantiation(instance):
    assert isinstance(instance, SPL_ResponseConstant)

@given(instance=SPL_SequenceConstant_strategy)
@settings(max_examples=50)
def test_spl_sequenceconstant_instantiation(instance):
    assert isinstance(instance, SPL_SequenceConstant)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=SPL_BODYExp_strategy)
@settings(max_examples=50)
def test_spl_bodyexp_instantiation(instance):
    assert isinstance(instance, SPL_BODYExp)

@given(instance=SPL_OperatorExp_strategy)
@settings(max_examples=50)
def test_spl_operatorexp_instantiation(instance):
    assert isinstance(instance, SPL_OperatorExp)



@given(instance=SPL_OperatorExp_strategy)
def test_spl_operatorexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=SPL_BlockExp_strategy)
@settings(max_examples=50)
def test_spl_blockexp_instantiation(instance):
    assert isinstance(instance, SPL_BlockExp)

@given(instance=SPL_ForwardExp_strategy)
@settings(max_examples=50)
def test_spl_forwardexp_instantiation(instance):
    assert isinstance(instance, SPL_ForwardExp)



@given(instance=SPL_ForwardExp_strategy)
def test_spl_forwardexp_isParallel_setter(instance):
    original = instance.isParallel
    instance.isParallel = original
    assert instance.isParallel == original

@given(instance=SPL_ReasonExp_strategy)
@settings(max_examples=50)
def test_spl_reasonexp_instantiation(instance):
    assert isinstance(instance, SPL_ReasonExp)

@given(instance=SPL_WithExp_strategy)
@settings(max_examples=50)
def test_spl_withexp_instantiation(instance):
    assert isinstance(instance, SPL_WithExp)

@given(instance=SPL_ConstantExp_strategy)
@settings(max_examples=50)
def test_spl_constantexp_instantiation(instance):
    assert isinstance(instance, SPL_ConstantExp)

@given(instance=SPL_FunctionCallExp_strategy)
@settings(max_examples=50)
def test_spl_functioncallexp_instantiation(instance):
    assert isinstance(instance, SPL_FunctionCallExp)

@given(instance=SPL_PopExp_strategy)
@settings(max_examples=50)
def test_spl_popexp_instantiation(instance):
    assert isinstance(instance, SPL_PopExp)

@given(instance=SPL_RequestURIExp_strategy)
@settings(max_examples=50)
def test_spl_requesturiexp_instantiation(instance):
    assert isinstance(instance, SPL_RequestURIExp)

@given(instance=SelectMember_strategy)
@settings(max_examples=50)
def test_selectmember_instantiation(instance):
    assert isinstance(instance, SelectMember)

@given(instance=SPL_SelectDefault_strategy)
@settings(max_examples=50)
def test_spl_selectdefault_instantiation(instance):
    assert isinstance(instance, SPL_SelectDefault)

@given(instance=SPL_SelectCase_strategy)
@settings(max_examples=50)
def test_spl_selectcase_instantiation(instance):
    assert isinstance(instance, SPL_SelectCase)

@given(instance=SPL_Place_strategy)
@settings(max_examples=50)
def test_spl_place_instantiation(instance):
    assert isinstance(instance, SPL_Place)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=SPL_BreakStat_strategy)
@settings(max_examples=50)
def test_spl_breakstat_instantiation(instance):
    assert isinstance(instance, SPL_BreakStat)

@given(instance=SPL_PushStat_strategy)
@settings(max_examples=50)
def test_spl_pushstat_instantiation(instance):
    assert isinstance(instance, SPL_PushStat)

@given(instance=SPL_ReturnStat_strategy)
@settings(max_examples=50)
def test_spl_returnstat_instantiation(instance):
    assert isinstance(instance, SPL_ReturnStat)

@given(instance=SPL_SetStat_strategy)
@settings(max_examples=50)
def test_spl_setstat_instantiation(instance):
    assert isinstance(instance, SPL_SetStat)

@given(instance=SPL_ForeachStat_strategy)
@settings(max_examples=50)
def test_spl_foreachstat_instantiation(instance):
    assert isinstance(instance, SPL_ForeachStat)



@given(instance=SPL_ForeachStat_strategy)
def test_spl_foreachstat_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=SPL_FunctionCallStat_strategy)
@settings(max_examples=50)
def test_spl_functioncallstat_instantiation(instance):
    assert isinstance(instance, SPL_FunctionCallStat)

@given(instance=SPL_IfStat_strategy)
@settings(max_examples=50)
def test_spl_ifstat_instantiation(instance):
    assert isinstance(instance, SPL_IfStat)

@given(instance=SPL_WhenStat_strategy)
@settings(max_examples=50)
def test_spl_whenstat_instantiation(instance):
    assert isinstance(instance, SPL_WhenStat)

@given(instance=SPL_SelectStat_strategy)
@settings(max_examples=50)
def test_spl_selectstat_instantiation(instance):
    assert isinstance(instance, SPL_SelectStat)

@given(instance=SPL_DeclarationStat_strategy)
@settings(max_examples=50)
def test_spl_declarationstat_instantiation(instance):
    assert isinstance(instance, SPL_DeclarationStat)

@given(instance=SPL_ContinueStat_strategy)
@settings(max_examples=50)
def test_spl_continuestat_instantiation(instance):
    assert isinstance(instance, SPL_ContinueStat)

@given(instance=SPL_CompoundStat_strategy)
@settings(max_examples=50)
def test_spl_compoundstat_instantiation(instance):
    assert isinstance(instance, SPL_CompoundStat)

@given(instance=SPL_Variable_strategy)
@settings(max_examples=50)
def test_spl_variable_instantiation(instance):
    assert isinstance(instance, SPL_Variable)

@given(instance=FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_functiondeclaration_instantiation(instance):
    assert isinstance(instance, FunctionDeclaration)

@given(instance=SPL_LocalFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_spl_localfunctiondeclaration_instantiation(instance):
    assert isinstance(instance, SPL_LocalFunctionDeclaration)

@given(instance=SPL_RemoteFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_spl_remotefunctiondeclaration_instantiation(instance):
    assert isinstance(instance, SPL_RemoteFunctionDeclaration)



@given(instance=SPL_RemoteFunctionDeclaration_strategy)
def test_spl_remotefunctiondeclaration_functionLocation_setter(instance):
    original = instance.functionLocation
    instance.functionLocation = original
    assert instance.functionLocation == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=SPL_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_spl_functiondeclaration_instantiation(instance):
    assert isinstance(instance, SPL_FunctionDeclaration)

@given(instance=SPL_StructureDeclaration_strategy)
@settings(max_examples=50)
def test_spl_structuredeclaration_instantiation(instance):
    assert isinstance(instance, SPL_StructureDeclaration)

@given(instance=SPL_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_spl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, SPL_VariableDeclaration)

@given(instance=Branch_strategy)
@settings(max_examples=50)
def test_branch_instantiation(instance):
    assert isinstance(instance, Branch)

@given(instance=SPL_NamedBranch_strategy)
@settings(max_examples=50)
def test_spl_namedbranch_instantiation(instance):
    assert isinstance(instance, SPL_NamedBranch)



@given(instance=SPL_NamedBranch_strategy)
def test_spl_namedbranch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL_DefaultBranch_strategy)
@settings(max_examples=50)
def test_spl_defaultbranch_instantiation(instance):
    assert isinstance(instance, SPL_DefaultBranch)

@given(instance=MethodName_strategy)
@settings(max_examples=50)
def test_methodname_instantiation(instance):
    assert isinstance(instance, MethodName)

@given(instance=SPL_ControlMethodName_strategy)
@settings(max_examples=50)
def test_spl_controlmethodname_instantiation(instance):
    assert isinstance(instance, SPL_ControlMethodName)



@given(instance=SPL_ControlMethodName_strategy)
def test_spl_controlmethodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL_SIPMethodName_strategy)
@settings(max_examples=50)
def test_spl_sipmethodname_instantiation(instance):
    assert isinstance(instance, SPL_SIPMethodName)



@given(instance=SPL_SIPMethodName_strategy)
def test_spl_sipmethodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=SPL_WhenHeader_strategy)
@settings(max_examples=50)
def test_spl_whenheader_instantiation(instance):
    assert isinstance(instance, SPL_WhenHeader)



@given(instance=SPL_WhenHeader_strategy)
def test_spl_whenheader_headerId_setter(instance):
    original = instance.headerId
    instance.headerId = original
    assert instance.headerId == original

@given(instance=SPL_Argument_strategy)
@settings(max_examples=50)
def test_spl_argument_instantiation(instance):
    assert isinstance(instance, SPL_Argument)

@given(instance=TypeExpression_strategy)
@settings(max_examples=50)
def test_typeexpression_instantiation(instance):
    assert isinstance(instance, TypeExpression)

@given(instance=SPL_DefinedType_strategy)
@settings(max_examples=50)
def test_spl_definedtype_instantiation(instance):
    assert isinstance(instance, SPL_DefinedType)



@given(instance=SPL_DefinedType_strategy)
def test_spl_definedtype_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=SPL_SequenceType_strategy)
@settings(max_examples=50)
def test_spl_sequencetype_instantiation(instance):
    assert isinstance(instance, SPL_SequenceType)



@given(instance=SPL_SequenceType_strategy)
def test_spl_sequencetype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=SPL_SequenceType_strategy)
def test_spl_sequencetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=SPL_SequenceType_strategy)
def test_spl_sequencetype_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=SPL_SimpleType_strategy)
@settings(max_examples=50)
def test_spl_simpletype_instantiation(instance):
    assert isinstance(instance, SPL_SimpleType)



@given(instance=SPL_SimpleType_strategy)
def test_spl_simpletype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Session_strategy)
@settings(max_examples=50)
def test_session_instantiation(instance):
    assert isinstance(instance, Session)

@given(instance=SPL_Dialog_strategy)
@settings(max_examples=50)
def test_spl_dialog_instantiation(instance):
    assert isinstance(instance, SPL_Dialog)

@given(instance=SPL_Event_strategy)
@settings(max_examples=50)
def test_spl_event_instantiation(instance):
    assert isinstance(instance, SPL_Event)



@given(instance=SPL_Event_strategy)
def test_spl_event_eventId_setter(instance):
    original = instance.eventId
    instance.eventId = original
    assert instance.eventId == original

@given(instance=SPL_Method_strategy)
@settings(max_examples=50)
def test_spl_method_instantiation(instance):
    assert isinstance(instance, SPL_Method)



@given(instance=SPL_Method_strategy)
def test_spl_method_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=SPL_Registration_strategy)
@settings(max_examples=50)
def test_spl_registration_instantiation(instance):
    assert isinstance(instance, SPL_Registration)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=SPL_Declaration_strategy)
@settings(max_examples=50)
def test_spl_declaration_instantiation(instance):
    assert isinstance(instance, SPL_Declaration)



@given(instance=SPL_Declaration_strategy)
def test_spl_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL_Service_strategy)
@settings(max_examples=50)
def test_spl_service_instantiation(instance):
    assert isinstance(instance, SPL_Service)



@given(instance=SPL_Service_strategy)
def test_spl_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL_Constant_strategy)
@settings(max_examples=50)
def test_spl_constant_instantiation(instance):
    assert isinstance(instance, SPL_Constant)

@given(instance=SPL_Statement_strategy)
@settings(max_examples=50)
def test_spl_statement_instantiation(instance):
    assert isinstance(instance, SPL_Statement)

@given(instance=SPL_MessageField_strategy)
@settings(max_examples=50)
def test_spl_messagefield_instantiation(instance):
    assert isinstance(instance, SPL_MessageField)

@given(instance=SPL_Expression_strategy)
@settings(max_examples=50)
def test_spl_expression_instantiation(instance):
    assert isinstance(instance, SPL_Expression)

@given(instance=SPL_StructureProperty_strategy)
@settings(max_examples=50)
def test_spl_structureproperty_instantiation(instance):
    assert isinstance(instance, SPL_StructureProperty)



@given(instance=SPL_StructureProperty_strategy)
def test_spl_structureproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL_MethodName_strategy)
@settings(max_examples=50)
def test_spl_methodname_instantiation(instance):
    assert isinstance(instance, SPL_MethodName)

@given(instance=SPL_Response_strategy)
@settings(max_examples=50)
def test_spl_response_instantiation(instance):
    assert isinstance(instance, SPL_Response)

@given(instance=SPL_FunctionCall_strategy)
@settings(max_examples=50)
def test_spl_functioncall_instantiation(instance):
    assert isinstance(instance, SPL_FunctionCall)

@given(instance=SPL_SelectMember_strategy)
@settings(max_examples=50)
def test_spl_selectmember_instantiation(instance):
    assert isinstance(instance, SPL_SelectMember)

@given(instance=SPL_Branch_strategy)
@settings(max_examples=50)
def test_spl_branch_instantiation(instance):
    assert isinstance(instance, SPL_Branch)

@given(instance=SPL_Session_strategy)
@settings(max_examples=50)
def test_spl_session_instantiation(instance):
    assert isinstance(instance, SPL_Session)

@given(instance=SPL_Program_strategy)
@settings(max_examples=50)
def test_spl_program_instantiation(instance):
    assert isinstance(instance, SPL_Program)

@given(instance=SPL_TypeExpression_strategy)
@settings(max_examples=50)
def test_spl_typeexpression_instantiation(instance):
    assert isinstance(instance, SPL_TypeExpression)

@given(instance=SPL_LocatedElement_strategy)
@settings(max_examples=50)
def test_spl_locatedelement_instantiation(instance):
    assert isinstance(instance, SPL_LocatedElement)



@given(instance=SPL_LocatedElement_strategy)
def test_spl_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=SPL_LocatedElement_strategy)
def test_spl_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=SPL_LocatedElement_strategy)
def test_spl_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
