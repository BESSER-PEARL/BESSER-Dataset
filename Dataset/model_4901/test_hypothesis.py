import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ErrorResponse,
    SPL::RedirectionErrorResponse,
    SPL::ServerErrorResponse,
    SPL::GlobalErrorResponse,
    SPL::ClientErrorResponse,
    Response,
    SPL::ErrorResponse,
    SPL::SuccessResponse,
    Constant,
    SPL::URIConstant,
    SPL::StringConstant,
    SPL::IntegerConstant,
    SPL::BooleanConstant,
    MessageField,
    SPL::HeadedMessageField,
    SPL::ReasonMessageField,
    VariablePlace,
    SPL::PropertyCallPlace,
    Place,
    SPL::VariablePlace,
    SPL::SIPHeaderPlace,
    SPL::ResponseConstant,
    SPL::SequenceConstant,
    Expression,
    SPL::BlockExp,
    SPL::ReasonExp,
    SPL::WithExp,
    SPL::BODYExp,
    SPL::OperatorExp,
    SPL::ForwardExp,
    SPL::ConstantExp,
    SPL::FunctionCallExp,
    SPL::PopExp,
    SPL::RequestURIExp,
    SelectMember,
    SPL::SelectDefault,
    SPL::SelectCase,
    SPL::Place,
    Statement,
    SPL::ContinueStat,
    SPL::FunctionCallStat,
    SPL::SelectStat,
    SPL::WhenStat,
    SPL::ForeachStat,
    SPL::IfStat,
    SPL::DeclarationStat,
    SPL::SetStat,
    SPL::BreakStat,
    SPL::PushStat,
    SPL::ReturnStat,
    SPL::CompoundStat,
    SPL::Variable,
    FunctionDeclaration,
    SPL::LocalFunctionDeclaration,
    SPL::RemoteFunctionDeclaration,
    Declaration,
    SPL::FunctionDeclaration,
    SPL::StructureDeclaration,
    SPL::VariableDeclaration,
    Branch,
    SPL::NamedBranch,
    SPL::DefaultBranch,
    MethodName,
    SPL::ControlMethodName,
    SPL::SIPMethodName,
    VariableDeclaration,
    SPL::WhenHeader,
    SPL::Argument,
    TypeExpression,
    SPL::DefinedType,
    SPL::SequenceType,
    SPL::SimpleType,
    Session,
    SPL::Event,
    SPL::Method,
    SPL::Dialog,
    SPL::Registration,
    LocatedElement,
    SPL::Branch,
    SPL::StructureProperty,
    SPL::MethodName,
    SPL::SelectMember,
    SPL::MessageField,
    SPL::Service,
    SPL::Constant,
    SPL::Session,
    SPL::FunctionCall,
    SPL::Statement,
    SPL::Declaration,
    SPL::Response,
    SPL::Expression,
    SPL::Program,
    SPL::TypeExpression,
    SPL::LocatedElement,
    SIPMethod,
    ClientErrorKind,
    SuccessKind,
    PrimitiveType,
    RedirectionErrorKind,
    Modifier,
    FunctionLocation,
    ControlMethod,
    GlobalErrorKind,
    ServerErrorKind,
    SIPHeader,
    Direction,
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



def test_spl::redirectionerrorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL::RedirectionErrorResponse)


def test_spl::redirectionerrorresponse_constructor_exists():
    assert callable(SPL::RedirectionErrorResponse.__init__)


def test_spl::redirectionerrorresponse_constructor_args():
    sig = inspect.signature(SPL::RedirectionErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_spl::redirectionerrorresponse_has_errorKind():
    assert hasattr(SPL::RedirectionErrorResponse, "errorKind")
    descriptor = None
    for klass in SPL::RedirectionErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_spl::servererrorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL::ServerErrorResponse)


def test_spl::servererrorresponse_constructor_exists():
    assert callable(SPL::ServerErrorResponse.__init__)


def test_spl::servererrorresponse_constructor_args():
    sig = inspect.signature(SPL::ServerErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_spl::servererrorresponse_has_errorKind():
    assert hasattr(SPL::ServerErrorResponse, "errorKind")
    descriptor = None
    for klass in SPL::ServerErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_spl::globalerrorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL::GlobalErrorResponse)


def test_spl::globalerrorresponse_constructor_exists():
    assert callable(SPL::GlobalErrorResponse.__init__)


def test_spl::globalerrorresponse_constructor_args():
    sig = inspect.signature(SPL::GlobalErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_spl::globalerrorresponse_has_errorKind():
    assert hasattr(SPL::GlobalErrorResponse, "errorKind")
    descriptor = None
    for klass in SPL::GlobalErrorResponse.__mro__:
        if "errorKind" in klass.__dict__:
            descriptor = klass.__dict__["errorKind"]
            break
    assert isinstance(descriptor, property)



def test_spl::clienterrorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL::ClientErrorResponse)


def test_spl::clienterrorresponse_constructor_exists():
    assert callable(SPL::ClientErrorResponse.__init__)


def test_spl::clienterrorresponse_constructor_args():
    sig = inspect.signature(SPL::ClientErrorResponse.__init__)
    params = list(sig.parameters.keys())
    assert "errorKind" in params, "Missing parameter 'errorKind'"

def test_spl::clienterrorresponse_has_errorKind():
    assert hasattr(SPL::ClientErrorResponse, "errorKind")
    descriptor = None
    for klass in SPL::ClientErrorResponse.__mro__:
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



def test_spl::errorresponse_is_not_abstract():
    assert not inspect.isabstract(SPL::ErrorResponse)


def test_spl::errorresponse_constructor_exists():
    assert callable(SPL::ErrorResponse.__init__)


def test_spl::errorresponse_constructor_args():
    sig = inspect.signature(SPL::ErrorResponse.__init__)
    params = list(sig.parameters.keys())



def test_spl::successresponse_is_not_abstract():
    assert not inspect.isabstract(SPL::SuccessResponse)


def test_spl::successresponse_constructor_exists():
    assert callable(SPL::SuccessResponse.__init__)


def test_spl::successresponse_constructor_args():
    sig = inspect.signature(SPL::SuccessResponse.__init__)
    params = list(sig.parameters.keys())
    assert "successKind" in params, "Missing parameter 'successKind'"

def test_spl::successresponse_has_successKind():
    assert hasattr(SPL::SuccessResponse, "successKind")
    descriptor = None
    for klass in SPL::SuccessResponse.__mro__:
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



def test_spl::uriconstant_is_not_abstract():
    assert not inspect.isabstract(SPL::URIConstant)


def test_spl::uriconstant_constructor_exists():
    assert callable(SPL::URIConstant.__init__)


def test_spl::uriconstant_constructor_args():
    sig = inspect.signature(SPL::URIConstant.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_spl::uriconstant_has_uri():
    assert hasattr(SPL::URIConstant, "uri")
    descriptor = None
    for klass in SPL::URIConstant.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_spl::stringconstant_is_not_abstract():
    assert not inspect.isabstract(SPL::StringConstant)


def test_spl::stringconstant_constructor_exists():
    assert callable(SPL::StringConstant.__init__)


def test_spl::stringconstant_constructor_args():
    sig = inspect.signature(SPL::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spl::stringconstant_has_value():
    assert hasattr(SPL::StringConstant, "value")
    descriptor = None
    for klass in SPL::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spl::integerconstant_is_not_abstract():
    assert not inspect.isabstract(SPL::IntegerConstant)


def test_spl::integerconstant_constructor_exists():
    assert callable(SPL::IntegerConstant.__init__)


def test_spl::integerconstant_constructor_args():
    sig = inspect.signature(SPL::IntegerConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spl::integerconstant_has_value():
    assert hasattr(SPL::IntegerConstant, "value")
    descriptor = None
    for klass in SPL::IntegerConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spl::booleanconstant_is_not_abstract():
    assert not inspect.isabstract(SPL::BooleanConstant)


def test_spl::booleanconstant_constructor_exists():
    assert callable(SPL::BooleanConstant.__init__)


def test_spl::booleanconstant_constructor_args():
    sig = inspect.signature(SPL::BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spl::booleanconstant_has_value():
    assert hasattr(SPL::BooleanConstant, "value")
    descriptor = None
    for klass in SPL::BooleanConstant.__mro__:
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



def test_spl::headedmessagefield_is_not_abstract():
    assert not inspect.isabstract(SPL::HeadedMessageField)


def test_spl::headedmessagefield_constructor_exists():
    assert callable(SPL::HeadedMessageField.__init__)


def test_spl::headedmessagefield_constructor_args():
    sig = inspect.signature(SPL::HeadedMessageField.__init__)
    params = list(sig.parameters.keys())
    assert "headerId" in params, "Missing parameter 'headerId'"

def test_spl::headedmessagefield_has_headerId():
    assert hasattr(SPL::HeadedMessageField, "headerId")
    descriptor = None
    for klass in SPL::HeadedMessageField.__mro__:
        if "headerId" in klass.__dict__:
            descriptor = klass.__dict__["headerId"]
            break
    assert isinstance(descriptor, property)



def test_spl::reasonmessagefield_is_not_abstract():
    assert not inspect.isabstract(SPL::ReasonMessageField)


def test_spl::reasonmessagefield_constructor_exists():
    assert callable(SPL::ReasonMessageField.__init__)


def test_spl::reasonmessagefield_constructor_args():
    sig = inspect.signature(SPL::ReasonMessageField.__init__)
    params = list(sig.parameters.keys())



def test_variableplace_is_not_abstract():
    assert not inspect.isabstract(VariablePlace)


def test_variableplace_constructor_exists():
    assert callable(VariablePlace.__init__)


def test_variableplace_constructor_args():
    sig = inspect.signature(VariablePlace.__init__)
    params = list(sig.parameters.keys())



def test_spl::propertycallplace_is_not_abstract():
    assert not inspect.isabstract(SPL::PropertyCallPlace)


def test_spl::propertycallplace_constructor_exists():
    assert callable(SPL::PropertyCallPlace.__init__)


def test_spl::propertycallplace_constructor_args():
    sig = inspect.signature(SPL::PropertyCallPlace.__init__)
    params = list(sig.parameters.keys())
    assert "propName" in params, "Missing parameter 'propName'"

def test_spl::propertycallplace_has_propName():
    assert hasattr(SPL::PropertyCallPlace, "propName")
    descriptor = None
    for klass in SPL::PropertyCallPlace.__mro__:
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



def test_spl::variableplace_is_not_abstract():
    assert not inspect.isabstract(SPL::VariablePlace)


def test_spl::variableplace_constructor_exists():
    assert callable(SPL::VariablePlace.__init__)


def test_spl::variableplace_constructor_args():
    sig = inspect.signature(SPL::VariablePlace.__init__)
    params = list(sig.parameters.keys())



def test_spl::sipheaderplace_is_not_abstract():
    assert not inspect.isabstract(SPL::SIPHeaderPlace)


def test_spl::sipheaderplace_constructor_exists():
    assert callable(SPL::SIPHeaderPlace.__init__)


def test_spl::sipheaderplace_constructor_args():
    sig = inspect.signature(SPL::SIPHeaderPlace.__init__)
    params = list(sig.parameters.keys())
    assert "header" in params, "Missing parameter 'header'"

def test_spl::sipheaderplace_has_header():
    assert hasattr(SPL::SIPHeaderPlace, "header")
    descriptor = None
    for klass in SPL::SIPHeaderPlace.__mro__:
        if "header" in klass.__dict__:
            descriptor = klass.__dict__["header"]
            break
    assert isinstance(descriptor, property)



def test_spl::responseconstant_is_not_abstract():
    assert not inspect.isabstract(SPL::ResponseConstant)


def test_spl::responseconstant_constructor_exists():
    assert callable(SPL::ResponseConstant.__init__)


def test_spl::responseconstant_constructor_args():
    sig = inspect.signature(SPL::ResponseConstant.__init__)
    params = list(sig.parameters.keys())



def test_spl::sequenceconstant_is_not_abstract():
    assert not inspect.isabstract(SPL::SequenceConstant)


def test_spl::sequenceconstant_constructor_exists():
    assert callable(SPL::SequenceConstant.__init__)


def test_spl::sequenceconstant_constructor_args():
    sig = inspect.signature(SPL::SequenceConstant.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_spl::blockexp_is_not_abstract():
    assert not inspect.isabstract(SPL::BlockExp)


def test_spl::blockexp_constructor_exists():
    assert callable(SPL::BlockExp.__init__)


def test_spl::blockexp_constructor_args():
    sig = inspect.signature(SPL::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_spl::reasonexp_is_not_abstract():
    assert not inspect.isabstract(SPL::ReasonExp)


def test_spl::reasonexp_constructor_exists():
    assert callable(SPL::ReasonExp.__init__)


def test_spl::reasonexp_constructor_args():
    sig = inspect.signature(SPL::ReasonExp.__init__)
    params = list(sig.parameters.keys())



def test_spl::withexp_is_not_abstract():
    assert not inspect.isabstract(SPL::WithExp)


def test_spl::withexp_constructor_exists():
    assert callable(SPL::WithExp.__init__)


def test_spl::withexp_constructor_args():
    sig = inspect.signature(SPL::WithExp.__init__)
    params = list(sig.parameters.keys())



def test_spl::bodyexp_is_not_abstract():
    assert not inspect.isabstract(SPL::BODYExp)


def test_spl::bodyexp_constructor_exists():
    assert callable(SPL::BODYExp.__init__)


def test_spl::bodyexp_constructor_args():
    sig = inspect.signature(SPL::BODYExp.__init__)
    params = list(sig.parameters.keys())



def test_spl::operatorexp_is_not_abstract():
    assert not inspect.isabstract(SPL::OperatorExp)


def test_spl::operatorexp_constructor_exists():
    assert callable(SPL::OperatorExp.__init__)


def test_spl::operatorexp_constructor_args():
    sig = inspect.signature(SPL::OperatorExp.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_spl::operatorexp_has_opName():
    assert hasattr(SPL::OperatorExp, "opName")
    descriptor = None
    for klass in SPL::OperatorExp.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_spl::forwardexp_is_not_abstract():
    assert not inspect.isabstract(SPL::ForwardExp)


def test_spl::forwardexp_constructor_exists():
    assert callable(SPL::ForwardExp.__init__)


def test_spl::forwardexp_constructor_args():
    sig = inspect.signature(SPL::ForwardExp.__init__)
    params = list(sig.parameters.keys())
    assert "isParallel" in params, "Missing parameter 'isParallel'"

def test_spl::forwardexp_has_isParallel():
    assert hasattr(SPL::ForwardExp, "isParallel")
    descriptor = None
    for klass in SPL::ForwardExp.__mro__:
        if "isParallel" in klass.__dict__:
            descriptor = klass.__dict__["isParallel"]
            break
    assert isinstance(descriptor, property)



def test_spl::constantexp_is_not_abstract():
    assert not inspect.isabstract(SPL::ConstantExp)


def test_spl::constantexp_constructor_exists():
    assert callable(SPL::ConstantExp.__init__)


def test_spl::constantexp_constructor_args():
    sig = inspect.signature(SPL::ConstantExp.__init__)
    params = list(sig.parameters.keys())



def test_spl::functioncallexp_is_not_abstract():
    assert not inspect.isabstract(SPL::FunctionCallExp)


def test_spl::functioncallexp_constructor_exists():
    assert callable(SPL::FunctionCallExp.__init__)


def test_spl::functioncallexp_constructor_args():
    sig = inspect.signature(SPL::FunctionCallExp.__init__)
    params = list(sig.parameters.keys())



def test_spl::popexp_is_not_abstract():
    assert not inspect.isabstract(SPL::PopExp)


def test_spl::popexp_constructor_exists():
    assert callable(SPL::PopExp.__init__)


def test_spl::popexp_constructor_args():
    sig = inspect.signature(SPL::PopExp.__init__)
    params = list(sig.parameters.keys())



def test_spl::requesturiexp_is_not_abstract():
    assert not inspect.isabstract(SPL::RequestURIExp)


def test_spl::requesturiexp_constructor_exists():
    assert callable(SPL::RequestURIExp.__init__)


def test_spl::requesturiexp_constructor_args():
    sig = inspect.signature(SPL::RequestURIExp.__init__)
    params = list(sig.parameters.keys())



def test_selectmember_is_not_abstract():
    assert not inspect.isabstract(SelectMember)


def test_selectmember_constructor_exists():
    assert callable(SelectMember.__init__)


def test_selectmember_constructor_args():
    sig = inspect.signature(SelectMember.__init__)
    params = list(sig.parameters.keys())



def test_spl::selectdefault_is_not_abstract():
    assert not inspect.isabstract(SPL::SelectDefault)


def test_spl::selectdefault_constructor_exists():
    assert callable(SPL::SelectDefault.__init__)


def test_spl::selectdefault_constructor_args():
    sig = inspect.signature(SPL::SelectDefault.__init__)
    params = list(sig.parameters.keys())



def test_spl::selectcase_is_not_abstract():
    assert not inspect.isabstract(SPL::SelectCase)


def test_spl::selectcase_constructor_exists():
    assert callable(SPL::SelectCase.__init__)


def test_spl::selectcase_constructor_args():
    sig = inspect.signature(SPL::SelectCase.__init__)
    params = list(sig.parameters.keys())



def test_spl::place_is_not_abstract():
    assert not inspect.isabstract(SPL::Place)


def test_spl::place_constructor_exists():
    assert callable(SPL::Place.__init__)


def test_spl::place_constructor_args():
    sig = inspect.signature(SPL::Place.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_spl::continuestat_is_not_abstract():
    assert not inspect.isabstract(SPL::ContinueStat)


def test_spl::continuestat_constructor_exists():
    assert callable(SPL::ContinueStat.__init__)


def test_spl::continuestat_constructor_args():
    sig = inspect.signature(SPL::ContinueStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::functioncallstat_is_not_abstract():
    assert not inspect.isabstract(SPL::FunctionCallStat)


def test_spl::functioncallstat_constructor_exists():
    assert callable(SPL::FunctionCallStat.__init__)


def test_spl::functioncallstat_constructor_args():
    sig = inspect.signature(SPL::FunctionCallStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::selectstat_is_not_abstract():
    assert not inspect.isabstract(SPL::SelectStat)


def test_spl::selectstat_constructor_exists():
    assert callable(SPL::SelectStat.__init__)


def test_spl::selectstat_constructor_args():
    sig = inspect.signature(SPL::SelectStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::whenstat_is_not_abstract():
    assert not inspect.isabstract(SPL::WhenStat)


def test_spl::whenstat_constructor_exists():
    assert callable(SPL::WhenStat.__init__)


def test_spl::whenstat_constructor_args():
    sig = inspect.signature(SPL::WhenStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::foreachstat_is_not_abstract():
    assert not inspect.isabstract(SPL::ForeachStat)


def test_spl::foreachstat_constructor_exists():
    assert callable(SPL::ForeachStat.__init__)


def test_spl::foreachstat_constructor_args():
    sig = inspect.signature(SPL::ForeachStat.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_spl::foreachstat_has_iteratorName():
    assert hasattr(SPL::ForeachStat, "iteratorName")
    descriptor = None
    for klass in SPL::ForeachStat.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_spl::ifstat_is_not_abstract():
    assert not inspect.isabstract(SPL::IfStat)


def test_spl::ifstat_constructor_exists():
    assert callable(SPL::IfStat.__init__)


def test_spl::ifstat_constructor_args():
    sig = inspect.signature(SPL::IfStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::declarationstat_is_not_abstract():
    assert not inspect.isabstract(SPL::DeclarationStat)


def test_spl::declarationstat_constructor_exists():
    assert callable(SPL::DeclarationStat.__init__)


def test_spl::declarationstat_constructor_args():
    sig = inspect.signature(SPL::DeclarationStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::setstat_is_not_abstract():
    assert not inspect.isabstract(SPL::SetStat)


def test_spl::setstat_constructor_exists():
    assert callable(SPL::SetStat.__init__)


def test_spl::setstat_constructor_args():
    sig = inspect.signature(SPL::SetStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::breakstat_is_not_abstract():
    assert not inspect.isabstract(SPL::BreakStat)


def test_spl::breakstat_constructor_exists():
    assert callable(SPL::BreakStat.__init__)


def test_spl::breakstat_constructor_args():
    sig = inspect.signature(SPL::BreakStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::pushstat_is_not_abstract():
    assert not inspect.isabstract(SPL::PushStat)


def test_spl::pushstat_constructor_exists():
    assert callable(SPL::PushStat.__init__)


def test_spl::pushstat_constructor_args():
    sig = inspect.signature(SPL::PushStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::returnstat_is_not_abstract():
    assert not inspect.isabstract(SPL::ReturnStat)


def test_spl::returnstat_constructor_exists():
    assert callable(SPL::ReturnStat.__init__)


def test_spl::returnstat_constructor_args():
    sig = inspect.signature(SPL::ReturnStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::compoundstat_is_not_abstract():
    assert not inspect.isabstract(SPL::CompoundStat)


def test_spl::compoundstat_constructor_exists():
    assert callable(SPL::CompoundStat.__init__)


def test_spl::compoundstat_constructor_args():
    sig = inspect.signature(SPL::CompoundStat.__init__)
    params = list(sig.parameters.keys())



def test_spl::variable_is_not_abstract():
    assert not inspect.isabstract(SPL::Variable)


def test_spl::variable_constructor_exists():
    assert callable(SPL::Variable.__init__)


def test_spl::variable_constructor_args():
    sig = inspect.signature(SPL::Variable.__init__)
    params = list(sig.parameters.keys())



def test_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(FunctionDeclaration)


def test_functiondeclaration_constructor_exists():
    assert callable(FunctionDeclaration.__init__)


def test_functiondeclaration_constructor_args():
    sig = inspect.signature(FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl::localfunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL::LocalFunctionDeclaration)


def test_spl::localfunctiondeclaration_constructor_exists():
    assert callable(SPL::LocalFunctionDeclaration.__init__)


def test_spl::localfunctiondeclaration_constructor_args():
    sig = inspect.signature(SPL::LocalFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl::remotefunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL::RemoteFunctionDeclaration)


def test_spl::remotefunctiondeclaration_constructor_exists():
    assert callable(SPL::RemoteFunctionDeclaration.__init__)


def test_spl::remotefunctiondeclaration_constructor_args():
    sig = inspect.signature(SPL::RemoteFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionLocation" in params, "Missing parameter 'functionLocation'"

def test_spl::remotefunctiondeclaration_has_functionLocation():
    assert hasattr(SPL::RemoteFunctionDeclaration, "functionLocation")
    descriptor = None
    for klass in SPL::RemoteFunctionDeclaration.__mro__:
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



def test_spl::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL::FunctionDeclaration)


def test_spl::functiondeclaration_constructor_exists():
    assert callable(SPL::FunctionDeclaration.__init__)


def test_spl::functiondeclaration_constructor_args():
    sig = inspect.signature(SPL::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl::structuredeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL::StructureDeclaration)


def test_spl::structuredeclaration_constructor_exists():
    assert callable(SPL::StructureDeclaration.__init__)


def test_spl::structuredeclaration_constructor_args():
    sig = inspect.signature(SPL::StructureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_spl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SPL::VariableDeclaration)


def test_spl::variabledeclaration_constructor_exists():
    assert callable(SPL::VariableDeclaration.__init__)


def test_spl::variabledeclaration_constructor_args():
    sig = inspect.signature(SPL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_branch_is_not_abstract():
    assert not inspect.isabstract(Branch)


def test_branch_constructor_exists():
    assert callable(Branch.__init__)


def test_branch_constructor_args():
    sig = inspect.signature(Branch.__init__)
    params = list(sig.parameters.keys())



def test_spl::namedbranch_is_not_abstract():
    assert not inspect.isabstract(SPL::NamedBranch)


def test_spl::namedbranch_constructor_exists():
    assert callable(SPL::NamedBranch.__init__)


def test_spl::namedbranch_constructor_args():
    sig = inspect.signature(SPL::NamedBranch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl::namedbranch_has_name():
    assert hasattr(SPL::NamedBranch, "name")
    descriptor = None
    for klass in SPL::NamedBranch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl::defaultbranch_is_not_abstract():
    assert not inspect.isabstract(SPL::DefaultBranch)


def test_spl::defaultbranch_constructor_exists():
    assert callable(SPL::DefaultBranch.__init__)


def test_spl::defaultbranch_constructor_args():
    sig = inspect.signature(SPL::DefaultBranch.__init__)
    params = list(sig.parameters.keys())



def test_methodname_is_not_abstract():
    assert not inspect.isabstract(MethodName)


def test_methodname_constructor_exists():
    assert callable(MethodName.__init__)


def test_methodname_constructor_args():
    sig = inspect.signature(MethodName.__init__)
    params = list(sig.parameters.keys())



def test_spl::controlmethodname_is_not_abstract():
    assert not inspect.isabstract(SPL::ControlMethodName)


def test_spl::controlmethodname_constructor_exists():
    assert callable(SPL::ControlMethodName.__init__)


def test_spl::controlmethodname_constructor_args():
    sig = inspect.signature(SPL::ControlMethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl::controlmethodname_has_name():
    assert hasattr(SPL::ControlMethodName, "name")
    descriptor = None
    for klass in SPL::ControlMethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl::sipmethodname_is_not_abstract():
    assert not inspect.isabstract(SPL::SIPMethodName)


def test_spl::sipmethodname_constructor_exists():
    assert callable(SPL::SIPMethodName.__init__)


def test_spl::sipmethodname_constructor_args():
    sig = inspect.signature(SPL::SIPMethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl::sipmethodname_has_name():
    assert hasattr(SPL::SIPMethodName, "name")
    descriptor = None
    for klass in SPL::SIPMethodName.__mro__:
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



def test_spl::whenheader_is_not_abstract():
    assert not inspect.isabstract(SPL::WhenHeader)


def test_spl::whenheader_constructor_exists():
    assert callable(SPL::WhenHeader.__init__)


def test_spl::whenheader_constructor_args():
    sig = inspect.signature(SPL::WhenHeader.__init__)
    params = list(sig.parameters.keys())
    assert "headerId" in params, "Missing parameter 'headerId'"

def test_spl::whenheader_has_headerId():
    assert hasattr(SPL::WhenHeader, "headerId")
    descriptor = None
    for klass in SPL::WhenHeader.__mro__:
        if "headerId" in klass.__dict__:
            descriptor = klass.__dict__["headerId"]
            break
    assert isinstance(descriptor, property)



def test_spl::argument_is_not_abstract():
    assert not inspect.isabstract(SPL::Argument)


def test_spl::argument_constructor_exists():
    assert callable(SPL::Argument.__init__)


def test_spl::argument_constructor_args():
    sig = inspect.signature(SPL::Argument.__init__)
    params = list(sig.parameters.keys())



def test_typeexpression_is_not_abstract():
    assert not inspect.isabstract(TypeExpression)


def test_typeexpression_constructor_exists():
    assert callable(TypeExpression.__init__)


def test_typeexpression_constructor_args():
    sig = inspect.signature(TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_spl::definedtype_is_not_abstract():
    assert not inspect.isabstract(SPL::DefinedType)


def test_spl::definedtype_constructor_exists():
    assert callable(SPL::DefinedType.__init__)


def test_spl::definedtype_constructor_args():
    sig = inspect.signature(SPL::DefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_spl::definedtype_has_typeName():
    assert hasattr(SPL::DefinedType, "typeName")
    descriptor = None
    for klass in SPL::DefinedType.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_spl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(SPL::SequenceType)


def test_spl::sequencetype_constructor_exists():
    assert callable(SPL::SequenceType.__init__)


def test_spl::sequencetype_constructor_args():
    sig = inspect.signature(SPL::SequenceType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "size" in params, "Missing parameter 'size'"

def test_spl::sequencetype_has_type():
    assert hasattr(SPL::SequenceType, "type")
    descriptor = None
    for klass in SPL::SequenceType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_spl::sequencetype_has_modifier():
    assert hasattr(SPL::SequenceType, "modifier")
    descriptor = None
    for klass in SPL::SequenceType.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_spl::sequencetype_has_size():
    assert hasattr(SPL::SequenceType, "size")
    descriptor = None
    for klass in SPL::SequenceType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_spl::simpletype_is_not_abstract():
    assert not inspect.isabstract(SPL::SimpleType)


def test_spl::simpletype_constructor_exists():
    assert callable(SPL::SimpleType.__init__)


def test_spl::simpletype_constructor_args():
    sig = inspect.signature(SPL::SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_spl::simpletype_has_type():
    assert hasattr(SPL::SimpleType, "type")
    descriptor = None
    for klass in SPL::SimpleType.__mro__:
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



def test_spl::event_is_not_abstract():
    assert not inspect.isabstract(SPL::Event)


def test_spl::event_constructor_exists():
    assert callable(SPL::Event.__init__)


def test_spl::event_constructor_args():
    sig = inspect.signature(SPL::Event.__init__)
    params = list(sig.parameters.keys())
    assert "eventId" in params, "Missing parameter 'eventId'"

def test_spl::event_has_eventId():
    assert hasattr(SPL::Event, "eventId")
    descriptor = None
    for klass in SPL::Event.__mro__:
        if "eventId" in klass.__dict__:
            descriptor = klass.__dict__["eventId"]
            break
    assert isinstance(descriptor, property)



def test_spl::method_is_not_abstract():
    assert not inspect.isabstract(SPL::Method)


def test_spl::method_constructor_exists():
    assert callable(SPL::Method.__init__)


def test_spl::method_constructor_args():
    sig = inspect.signature(SPL::Method.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_spl::method_has_direction():
    assert hasattr(SPL::Method, "direction")
    descriptor = None
    for klass in SPL::Method.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_spl::dialog_is_not_abstract():
    assert not inspect.isabstract(SPL::Dialog)


def test_spl::dialog_constructor_exists():
    assert callable(SPL::Dialog.__init__)


def test_spl::dialog_constructor_args():
    sig = inspect.signature(SPL::Dialog.__init__)
    params = list(sig.parameters.keys())



def test_spl::registration_is_not_abstract():
    assert not inspect.isabstract(SPL::Registration)


def test_spl::registration_constructor_exists():
    assert callable(SPL::Registration.__init__)


def test_spl::registration_constructor_args():
    sig = inspect.signature(SPL::Registration.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_spl::branch_is_not_abstract():
    assert not inspect.isabstract(SPL::Branch)


def test_spl::branch_constructor_exists():
    assert callable(SPL::Branch.__init__)


def test_spl::branch_constructor_args():
    sig = inspect.signature(SPL::Branch.__init__)
    params = list(sig.parameters.keys())



def test_spl::structureproperty_is_not_abstract():
    assert not inspect.isabstract(SPL::StructureProperty)


def test_spl::structureproperty_constructor_exists():
    assert callable(SPL::StructureProperty.__init__)


def test_spl::structureproperty_constructor_args():
    sig = inspect.signature(SPL::StructureProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl::structureproperty_has_name():
    assert hasattr(SPL::StructureProperty, "name")
    descriptor = None
    for klass in SPL::StructureProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl::methodname_is_not_abstract():
    assert not inspect.isabstract(SPL::MethodName)


def test_spl::methodname_constructor_exists():
    assert callable(SPL::MethodName.__init__)


def test_spl::methodname_constructor_args():
    sig = inspect.signature(SPL::MethodName.__init__)
    params = list(sig.parameters.keys())



def test_spl::selectmember_is_not_abstract():
    assert not inspect.isabstract(SPL::SelectMember)


def test_spl::selectmember_constructor_exists():
    assert callable(SPL::SelectMember.__init__)


def test_spl::selectmember_constructor_args():
    sig = inspect.signature(SPL::SelectMember.__init__)
    params = list(sig.parameters.keys())



def test_spl::messagefield_is_not_abstract():
    assert not inspect.isabstract(SPL::MessageField)


def test_spl::messagefield_constructor_exists():
    assert callable(SPL::MessageField.__init__)


def test_spl::messagefield_constructor_args():
    sig = inspect.signature(SPL::MessageField.__init__)
    params = list(sig.parameters.keys())



def test_spl::service_is_not_abstract():
    assert not inspect.isabstract(SPL::Service)


def test_spl::service_constructor_exists():
    assert callable(SPL::Service.__init__)


def test_spl::service_constructor_args():
    sig = inspect.signature(SPL::Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl::service_has_name():
    assert hasattr(SPL::Service, "name")
    descriptor = None
    for klass in SPL::Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl::constant_is_not_abstract():
    assert not inspect.isabstract(SPL::Constant)


def test_spl::constant_constructor_exists():
    assert callable(SPL::Constant.__init__)


def test_spl::constant_constructor_args():
    sig = inspect.signature(SPL::Constant.__init__)
    params = list(sig.parameters.keys())



def test_spl::session_is_not_abstract():
    assert not inspect.isabstract(SPL::Session)


def test_spl::session_constructor_exists():
    assert callable(SPL::Session.__init__)


def test_spl::session_constructor_args():
    sig = inspect.signature(SPL::Session.__init__)
    params = list(sig.parameters.keys())



def test_spl::functioncall_is_not_abstract():
    assert not inspect.isabstract(SPL::FunctionCall)


def test_spl::functioncall_constructor_exists():
    assert callable(SPL::FunctionCall.__init__)


def test_spl::functioncall_constructor_args():
    sig = inspect.signature(SPL::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_spl::statement_is_not_abstract():
    assert not inspect.isabstract(SPL::Statement)


def test_spl::statement_constructor_exists():
    assert callable(SPL::Statement.__init__)


def test_spl::statement_constructor_args():
    sig = inspect.signature(SPL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_spl::declaration_is_not_abstract():
    assert not inspect.isabstract(SPL::Declaration)


def test_spl::declaration_constructor_exists():
    assert callable(SPL::Declaration.__init__)


def test_spl::declaration_constructor_args():
    sig = inspect.signature(SPL::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spl::declaration_has_name():
    assert hasattr(SPL::Declaration, "name")
    descriptor = None
    for klass in SPL::Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spl::response_is_not_abstract():
    assert not inspect.isabstract(SPL::Response)


def test_spl::response_constructor_exists():
    assert callable(SPL::Response.__init__)


def test_spl::response_constructor_args():
    sig = inspect.signature(SPL::Response.__init__)
    params = list(sig.parameters.keys())



def test_spl::expression_is_not_abstract():
    assert not inspect.isabstract(SPL::Expression)


def test_spl::expression_constructor_exists():
    assert callable(SPL::Expression.__init__)


def test_spl::expression_constructor_args():
    sig = inspect.signature(SPL::Expression.__init__)
    params = list(sig.parameters.keys())



def test_spl::program_is_not_abstract():
    assert not inspect.isabstract(SPL::Program)


def test_spl::program_constructor_exists():
    assert callable(SPL::Program.__init__)


def test_spl::program_constructor_args():
    sig = inspect.signature(SPL::Program.__init__)
    params = list(sig.parameters.keys())



def test_spl::typeexpression_is_not_abstract():
    assert not inspect.isabstract(SPL::TypeExpression)


def test_spl::typeexpression_constructor_exists():
    assert callable(SPL::TypeExpression.__init__)


def test_spl::typeexpression_constructor_args():
    sig = inspect.signature(SPL::TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_spl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(SPL::LocatedElement)


def test_spl::locatedelement_constructor_exists():
    assert callable(SPL::LocatedElement.__init__)


def test_spl::locatedelement_constructor_args():
    sig = inspect.signature(SPL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"

def test_spl::locatedelement_has_commentsBefore():
    assert hasattr(SPL::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in SPL::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_spl::locatedelement_has_commentsAfter():
    assert hasattr(SPL::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in SPL::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_spl::locatedelement_has_location():
    assert hasattr(SPL::LocatedElement, "location")
    descriptor = None
    for klass in SPL::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_sipmethod_exists():
    # Check that the Enumeration exists
    assert SIPMethod is not None

def test_sipmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIPMethod]
    expected_literals = [
        "BYE",
        "OPTIONS",
        "INVITE",
        "REINVITE",
        "NOTIFY",
        "CANCEL",
        "REACK",
        "RESUBSCRIBE",
        "REREGISTER",
        "ACK",
        "SUBSCRIBE",
        "REGISTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIPMethod"

def test_clienterrorkind_exists():
    # Check that the Enumeration exists
    assert ClientErrorKind is not None

def test_clienterrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClientErrorKind]
    expected_literals = [
        "REQUEST_TIMEOUT",
        "BAD_EXTENSION",
        "PROXY_AUTHENTICATION_REQUIRED",
        "FORBIDDEN",
        "INTERVAL_TOO_BRIEF",
        "EXTENSION_REQUIRED",
        "CALL_OR_TRANSACTION_DOES_NOT_EXIST",
        "REQUEST_PENDING",
        "AMBIGUOUS",
        "BAD_REQUEST",
        "NOT_ACCEPTABLE",
        "UNSUPPORTED_URI_SCHEME",
        "TOO_MANY_HOPS",
        "LOOP_DETECTED",
        "UNDECIPHERABLE",
        "NOT_FOUND",
        "NOT_ACCEPTABLE_HERE",
        "REQUEST_TERMINATED",
        "PAYMENT_REQUIRED",
        "TEMPORARILY_UNAVAILABLE",
        "REQUESTURI_TOO_LONG",
        "BUSY_HERE",
        "ADDRESS_INCOMPLETE",
        "GONE",
        "UNAUTHORIZED",
        "METHOD_NOT_ALLOWED",
        "UNSUPPORTED_MEDIA_TYPE",
        "REQUEST_ENTITY_TOO_LARGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClientErrorKind"

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

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "bool",
        "string",
        "time",
        "void",
        "response",
        "int",
        "uri",
        "request",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"

def test_redirectionerrorkind_exists():
    # Check that the Enumeration exists
    assert RedirectionErrorKind is not None

def test_redirectionerrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RedirectionErrorKind]
    expected_literals = [
        "MOVED_PERMANENTLY",
        "MOVED_TEMPORARILY",
        "USE_PROXY",
        "MULTIPLE_CHOICES",
        "ALTERNATIVE_SERVICE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RedirectionErrorKind"

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
        "remote",
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionLocation"

def test_controlmethod_exists():
    # Check that the Enumeration exists
    assert ControlMethod is not None

def test_controlmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ControlMethod]
    expected_literals = [
        "deploy",
        "undeploy",
        "unregister",
        "unsubscribe",
        "uninvite",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ControlMethod"

def test_globalerrorkind_exists():
    # Check that the Enumeration exists
    assert GlobalErrorKind is not None

def test_globalerrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GlobalErrorKind]
    expected_literals = [
        "DOES_NOT_EXIST_ANYWHERE",
        "BUSY_EVERYWHERE",
        "DECLINE",
        "NOT_ACCEPTABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GlobalErrorKind"

def test_servererrorkind_exists():
    # Check that the Enumeration exists
    assert ServerErrorKind is not None

def test_servererrorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServerErrorKind]
    expected_literals = [
        "BAD_GATEWAY",
        "SERVER_INTERNAL_ERROR",
        "VERSION_NOT_SUPPORTED",
        "SERVER_TIMEOUT",
        "NOT_IMPLEMENTED",
        "SERVICE_UNAVAILABLE",
        "MESSAGE_TOO_LARGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServerErrorKind"

def test_sipheader_exists():
    # Check that the Enumeration exists
    assert SIPHeader is not None

def test_sipheader_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIPHeader]
    expected_literals = [
        "FROM",
        "SUBSCRIPTION_STATE",
        "TO",
        "VIA",
        "CONTACT",
        "CSEQ",
        "EVENT",
        "CALL_ID",
        "MAX_FORWARDS",
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
        "in_",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
SPL::RedirectionErrorResponse_strategy = st.builds(
    SPL::RedirectionErrorResponse,
    errorKind=
        safe_text
)
SPL::ServerErrorResponse_strategy = st.builds(
    SPL::ServerErrorResponse,
    errorKind=
        safe_text
)
SPL::GlobalErrorResponse_strategy = st.builds(
    SPL::GlobalErrorResponse,
    errorKind=
        safe_text
)
SPL::ClientErrorResponse_strategy = st.builds(
    SPL::ClientErrorResponse,
    errorKind=
        safe_text
)
Response_strategy = st.builds(
    Response,
)
SPL::ErrorResponse_strategy = st.builds(
    SPL::ErrorResponse,
)
SPL::SuccessResponse_strategy = st.builds(
    SPL::SuccessResponse,
    successKind=
        safe_text
)
Constant_strategy = st.builds(
    Constant,
)
SPL::URIConstant_strategy = st.builds(
    SPL::URIConstant,
    uri=
        safe_text
)
SPL::StringConstant_strategy = st.builds(
    SPL::StringConstant,
    value=
        safe_text
)
SPL::IntegerConstant_strategy = st.builds(
    SPL::IntegerConstant,
    value=
        st.integers()
)
SPL::BooleanConstant_strategy = st.builds(
    SPL::BooleanConstant,
    value=
        st.booleans()
)
MessageField_strategy = st.builds(
    MessageField,
)
SPL::HeadedMessageField_strategy = st.builds(
    SPL::HeadedMessageField,
    headerId=
        safe_text
)
SPL::ReasonMessageField_strategy = st.builds(
    SPL::ReasonMessageField,
)
VariablePlace_strategy = st.builds(
    VariablePlace,
)
SPL::PropertyCallPlace_strategy = st.builds(
    SPL::PropertyCallPlace,
    propName=
        safe_text
)
Place_strategy = st.builds(
    Place,
)
SPL::VariablePlace_strategy = st.builds(
    SPL::VariablePlace,
)
SPL::SIPHeaderPlace_strategy = st.builds(
    SPL::SIPHeaderPlace,
    header=
        safe_text
)
SPL::ResponseConstant_strategy = st.builds(
    SPL::ResponseConstant,
)
SPL::SequenceConstant_strategy = st.builds(
    SPL::SequenceConstant,
)
Expression_strategy = st.builds(
    Expression,
)
SPL::BlockExp_strategy = st.builds(
    SPL::BlockExp,
)
SPL::ReasonExp_strategy = st.builds(
    SPL::ReasonExp,
)
SPL::WithExp_strategy = st.builds(
    SPL::WithExp,
)
SPL::BODYExp_strategy = st.builds(
    SPL::BODYExp,
)
SPL::OperatorExp_strategy = st.builds(
    SPL::OperatorExp,
    opName=
        safe_text
)
SPL::ForwardExp_strategy = st.builds(
    SPL::ForwardExp,
    isParallel=
        st.booleans()
)
SPL::ConstantExp_strategy = st.builds(
    SPL::ConstantExp,
)
SPL::FunctionCallExp_strategy = st.builds(
    SPL::FunctionCallExp,
)
SPL::PopExp_strategy = st.builds(
    SPL::PopExp,
)
SPL::RequestURIExp_strategy = st.builds(
    SPL::RequestURIExp,
)
SelectMember_strategy = st.builds(
    SelectMember,
)
SPL::SelectDefault_strategy = st.builds(
    SPL::SelectDefault,
)
SPL::SelectCase_strategy = st.builds(
    SPL::SelectCase,
)
SPL::Place_strategy = st.builds(
    SPL::Place,
)
Statement_strategy = st.builds(
    Statement,
)
SPL::ContinueStat_strategy = st.builds(
    SPL::ContinueStat,
)
SPL::FunctionCallStat_strategy = st.builds(
    SPL::FunctionCallStat,
)
SPL::SelectStat_strategy = st.builds(
    SPL::SelectStat,
)
SPL::WhenStat_strategy = st.builds(
    SPL::WhenStat,
)
SPL::ForeachStat_strategy = st.builds(
    SPL::ForeachStat,
    iteratorName=
        safe_text
)
SPL::IfStat_strategy = st.builds(
    SPL::IfStat,
)
SPL::DeclarationStat_strategy = st.builds(
    SPL::DeclarationStat,
)
SPL::SetStat_strategy = st.builds(
    SPL::SetStat,
)
SPL::BreakStat_strategy = st.builds(
    SPL::BreakStat,
)
SPL::PushStat_strategy = st.builds(
    SPL::PushStat,
)
SPL::ReturnStat_strategy = st.builds(
    SPL::ReturnStat,
)
SPL::CompoundStat_strategy = st.builds(
    SPL::CompoundStat,
)
SPL::Variable_strategy = st.builds(
    SPL::Variable,
)
FunctionDeclaration_strategy = st.builds(
    FunctionDeclaration,
)
SPL::LocalFunctionDeclaration_strategy = st.builds(
    SPL::LocalFunctionDeclaration,
)
SPL::RemoteFunctionDeclaration_strategy = st.builds(
    SPL::RemoteFunctionDeclaration,
    functionLocation=
        safe_text
)
Declaration_strategy = st.builds(
    Declaration,
)
SPL::FunctionDeclaration_strategy = st.builds(
    SPL::FunctionDeclaration,
)
SPL::StructureDeclaration_strategy = st.builds(
    SPL::StructureDeclaration,
)
SPL::VariableDeclaration_strategy = st.builds(
    SPL::VariableDeclaration,
)
Branch_strategy = st.builds(
    Branch,
)
SPL::NamedBranch_strategy = st.builds(
    SPL::NamedBranch,
    name=
        safe_text
)
SPL::DefaultBranch_strategy = st.builds(
    SPL::DefaultBranch,
)
MethodName_strategy = st.builds(
    MethodName,
)
SPL::ControlMethodName_strategy = st.builds(
    SPL::ControlMethodName,
    name=
        safe_text
)
SPL::SIPMethodName_strategy = st.builds(
    SPL::SIPMethodName,
    name=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
SPL::WhenHeader_strategy = st.builds(
    SPL::WhenHeader,
    headerId=
        safe_text
)
SPL::Argument_strategy = st.builds(
    SPL::Argument,
)
TypeExpression_strategy = st.builds(
    TypeExpression,
)
SPL::DefinedType_strategy = st.builds(
    SPL::DefinedType,
    typeName=
        safe_text
)
SPL::SequenceType_strategy = st.builds(
    SPL::SequenceType,
    type=
        safe_text,
    modifier=
        safe_text,
    size=
        st.integers()
)
SPL::SimpleType_strategy = st.builds(
    SPL::SimpleType,
    type=
        safe_text
)
Session_strategy = st.builds(
    Session,
)
SPL::Event_strategy = st.builds(
    SPL::Event,
    eventId=
        safe_text
)
SPL::Method_strategy = st.builds(
    SPL::Method,
    direction=
        safe_text
)
SPL::Dialog_strategy = st.builds(
    SPL::Dialog,
)
SPL::Registration_strategy = st.builds(
    SPL::Registration,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
SPL::Branch_strategy = st.builds(
    SPL::Branch,
)
SPL::StructureProperty_strategy = st.builds(
    SPL::StructureProperty,
    name=
        safe_text
)
SPL::MethodName_strategy = st.builds(
    SPL::MethodName,
)
SPL::SelectMember_strategy = st.builds(
    SPL::SelectMember,
)
SPL::MessageField_strategy = st.builds(
    SPL::MessageField,
)
SPL::Service_strategy = st.builds(
    SPL::Service,
    name=
        safe_text
)
SPL::Constant_strategy = st.builds(
    SPL::Constant,
)
SPL::Session_strategy = st.builds(
    SPL::Session,
)
SPL::FunctionCall_strategy = st.builds(
    SPL::FunctionCall,
)
SPL::Statement_strategy = st.builds(
    SPL::Statement,
)
SPL::Declaration_strategy = st.builds(
    SPL::Declaration,
    name=
        safe_text
)
SPL::Response_strategy = st.builds(
    SPL::Response,
)
SPL::Expression_strategy = st.builds(
    SPL::Expression,
)
SPL::Program_strategy = st.builds(
    SPL::Program,
)
SPL::TypeExpression_strategy = st.builds(
    SPL::TypeExpression,
)
SPL::LocatedElement_strategy = st.builds(
    SPL::LocatedElement,
    commentsBefore=
        safe_text,
    commentsAfter=
        safe_text,
    location=
        safe_text
)

@given(instance=ErrorResponse_strategy)
@settings(max_examples=50)
def test_errorresponse_instantiation(instance):
    assert isinstance(instance, ErrorResponse)

@given(instance=SPL::RedirectionErrorResponse_strategy)
@settings(max_examples=50)
def test_spl::redirectionerrorresponse_instantiation(instance):
    assert isinstance(instance, SPL::RedirectionErrorResponse)

@given(instance=SPL::RedirectionErrorResponse_strategy)
def test_spl::redirectionerrorresponse_errorKind_type(instance):
    assert isinstance(instance.errorKind, str)


@given(instance=SPL::RedirectionErrorResponse_strategy)
def test_spl::redirectionerrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=SPL::ServerErrorResponse_strategy)
@settings(max_examples=50)
def test_spl::servererrorresponse_instantiation(instance):
    assert isinstance(instance, SPL::ServerErrorResponse)

@given(instance=SPL::ServerErrorResponse_strategy)
def test_spl::servererrorresponse_errorKind_type(instance):
    assert isinstance(instance.errorKind, str)


@given(instance=SPL::ServerErrorResponse_strategy)
def test_spl::servererrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=SPL::GlobalErrorResponse_strategy)
@settings(max_examples=50)
def test_spl::globalerrorresponse_instantiation(instance):
    assert isinstance(instance, SPL::GlobalErrorResponse)

@given(instance=SPL::GlobalErrorResponse_strategy)
def test_spl::globalerrorresponse_errorKind_type(instance):
    assert isinstance(instance.errorKind, str)


@given(instance=SPL::GlobalErrorResponse_strategy)
def test_spl::globalerrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=SPL::ClientErrorResponse_strategy)
@settings(max_examples=50)
def test_spl::clienterrorresponse_instantiation(instance):
    assert isinstance(instance, SPL::ClientErrorResponse)

@given(instance=SPL::ClientErrorResponse_strategy)
def test_spl::clienterrorresponse_errorKind_type(instance):
    assert isinstance(instance.errorKind, str)


@given(instance=SPL::ClientErrorResponse_strategy)
def test_spl::clienterrorresponse_errorKind_setter(instance):
    original = instance.errorKind
    instance.errorKind = original
    assert instance.errorKind == original

@given(instance=Response_strategy)
@settings(max_examples=50)
def test_response_instantiation(instance):
    assert isinstance(instance, Response)

@given(instance=SPL::ErrorResponse_strategy)
@settings(max_examples=50)
def test_spl::errorresponse_instantiation(instance):
    assert isinstance(instance, SPL::ErrorResponse)

@given(instance=SPL::SuccessResponse_strategy)
@settings(max_examples=50)
def test_spl::successresponse_instantiation(instance):
    assert isinstance(instance, SPL::SuccessResponse)

@given(instance=SPL::SuccessResponse_strategy)
def test_spl::successresponse_successKind_type(instance):
    assert isinstance(instance.successKind, str)


@given(instance=SPL::SuccessResponse_strategy)
def test_spl::successresponse_successKind_setter(instance):
    original = instance.successKind
    instance.successKind = original
    assert instance.successKind == original

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=SPL::URIConstant_strategy)
@settings(max_examples=50)
def test_spl::uriconstant_instantiation(instance):
    assert isinstance(instance, SPL::URIConstant)

@given(instance=SPL::URIConstant_strategy)
def test_spl::uriconstant_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=SPL::URIConstant_strategy)
def test_spl::uriconstant_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=SPL::StringConstant_strategy)
@settings(max_examples=50)
def test_spl::stringconstant_instantiation(instance):
    assert isinstance(instance, SPL::StringConstant)

@given(instance=SPL::StringConstant_strategy)
def test_spl::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SPL::StringConstant_strategy)
def test_spl::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SPL::IntegerConstant_strategy)
@settings(max_examples=50)
def test_spl::integerconstant_instantiation(instance):
    assert isinstance(instance, SPL::IntegerConstant)

@given(instance=SPL::IntegerConstant_strategy)
def test_spl::integerconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=SPL::IntegerConstant_strategy)
def test_spl::integerconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SPL::BooleanConstant_strategy)
@settings(max_examples=50)
def test_spl::booleanconstant_instantiation(instance):
    assert isinstance(instance, SPL::BooleanConstant)

@given(instance=SPL::BooleanConstant_strategy)
def test_spl::booleanconstant_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=SPL::BooleanConstant_strategy)
def test_spl::booleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MessageField_strategy)
@settings(max_examples=50)
def test_messagefield_instantiation(instance):
    assert isinstance(instance, MessageField)

@given(instance=SPL::HeadedMessageField_strategy)
@settings(max_examples=50)
def test_spl::headedmessagefield_instantiation(instance):
    assert isinstance(instance, SPL::HeadedMessageField)

@given(instance=SPL::HeadedMessageField_strategy)
def test_spl::headedmessagefield_headerId_type(instance):
    assert isinstance(instance.headerId, str)


@given(instance=SPL::HeadedMessageField_strategy)
def test_spl::headedmessagefield_headerId_setter(instance):
    original = instance.headerId
    instance.headerId = original
    assert instance.headerId == original

@given(instance=SPL::ReasonMessageField_strategy)
@settings(max_examples=50)
def test_spl::reasonmessagefield_instantiation(instance):
    assert isinstance(instance, SPL::ReasonMessageField)

@given(instance=VariablePlace_strategy)
@settings(max_examples=50)
def test_variableplace_instantiation(instance):
    assert isinstance(instance, VariablePlace)

@given(instance=SPL::PropertyCallPlace_strategy)
@settings(max_examples=50)
def test_spl::propertycallplace_instantiation(instance):
    assert isinstance(instance, SPL::PropertyCallPlace)

@given(instance=SPL::PropertyCallPlace_strategy)
def test_spl::propertycallplace_propName_type(instance):
    assert isinstance(instance.propName, str)


@given(instance=SPL::PropertyCallPlace_strategy)
def test_spl::propertycallplace_propName_setter(instance):
    original = instance.propName
    instance.propName = original
    assert instance.propName == original

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=SPL::VariablePlace_strategy)
@settings(max_examples=50)
def test_spl::variableplace_instantiation(instance):
    assert isinstance(instance, SPL::VariablePlace)

@given(instance=SPL::SIPHeaderPlace_strategy)
@settings(max_examples=50)
def test_spl::sipheaderplace_instantiation(instance):
    assert isinstance(instance, SPL::SIPHeaderPlace)

@given(instance=SPL::SIPHeaderPlace_strategy)
def test_spl::sipheaderplace_header_type(instance):
    assert isinstance(instance.header, str)


@given(instance=SPL::SIPHeaderPlace_strategy)
def test_spl::sipheaderplace_header_setter(instance):
    original = instance.header
    instance.header = original
    assert instance.header == original

@given(instance=SPL::ResponseConstant_strategy)
@settings(max_examples=50)
def test_spl::responseconstant_instantiation(instance):
    assert isinstance(instance, SPL::ResponseConstant)

@given(instance=SPL::SequenceConstant_strategy)
@settings(max_examples=50)
def test_spl::sequenceconstant_instantiation(instance):
    assert isinstance(instance, SPL::SequenceConstant)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=SPL::BlockExp_strategy)
@settings(max_examples=50)
def test_spl::blockexp_instantiation(instance):
    assert isinstance(instance, SPL::BlockExp)

@given(instance=SPL::ReasonExp_strategy)
@settings(max_examples=50)
def test_spl::reasonexp_instantiation(instance):
    assert isinstance(instance, SPL::ReasonExp)

@given(instance=SPL::WithExp_strategy)
@settings(max_examples=50)
def test_spl::withexp_instantiation(instance):
    assert isinstance(instance, SPL::WithExp)

@given(instance=SPL::BODYExp_strategy)
@settings(max_examples=50)
def test_spl::bodyexp_instantiation(instance):
    assert isinstance(instance, SPL::BODYExp)

@given(instance=SPL::OperatorExp_strategy)
@settings(max_examples=50)
def test_spl::operatorexp_instantiation(instance):
    assert isinstance(instance, SPL::OperatorExp)

@given(instance=SPL::OperatorExp_strategy)
def test_spl::operatorexp_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=SPL::OperatorExp_strategy)
def test_spl::operatorexp_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=SPL::ForwardExp_strategy)
@settings(max_examples=50)
def test_spl::forwardexp_instantiation(instance):
    assert isinstance(instance, SPL::ForwardExp)

@given(instance=SPL::ForwardExp_strategy)
def test_spl::forwardexp_isParallel_type(instance):
    assert isinstance(instance.isParallel, bool)


@given(instance=SPL::ForwardExp_strategy)
def test_spl::forwardexp_isParallel_setter(instance):
    original = instance.isParallel
    instance.isParallel = original
    assert instance.isParallel == original

@given(instance=SPL::ConstantExp_strategy)
@settings(max_examples=50)
def test_spl::constantexp_instantiation(instance):
    assert isinstance(instance, SPL::ConstantExp)

@given(instance=SPL::FunctionCallExp_strategy)
@settings(max_examples=50)
def test_spl::functioncallexp_instantiation(instance):
    assert isinstance(instance, SPL::FunctionCallExp)

@given(instance=SPL::PopExp_strategy)
@settings(max_examples=50)
def test_spl::popexp_instantiation(instance):
    assert isinstance(instance, SPL::PopExp)

@given(instance=SPL::RequestURIExp_strategy)
@settings(max_examples=50)
def test_spl::requesturiexp_instantiation(instance):
    assert isinstance(instance, SPL::RequestURIExp)

@given(instance=SelectMember_strategy)
@settings(max_examples=50)
def test_selectmember_instantiation(instance):
    assert isinstance(instance, SelectMember)

@given(instance=SPL::SelectDefault_strategy)
@settings(max_examples=50)
def test_spl::selectdefault_instantiation(instance):
    assert isinstance(instance, SPL::SelectDefault)

@given(instance=SPL::SelectCase_strategy)
@settings(max_examples=50)
def test_spl::selectcase_instantiation(instance):
    assert isinstance(instance, SPL::SelectCase)

@given(instance=SPL::Place_strategy)
@settings(max_examples=50)
def test_spl::place_instantiation(instance):
    assert isinstance(instance, SPL::Place)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=SPL::ContinueStat_strategy)
@settings(max_examples=50)
def test_spl::continuestat_instantiation(instance):
    assert isinstance(instance, SPL::ContinueStat)

@given(instance=SPL::FunctionCallStat_strategy)
@settings(max_examples=50)
def test_spl::functioncallstat_instantiation(instance):
    assert isinstance(instance, SPL::FunctionCallStat)

@given(instance=SPL::SelectStat_strategy)
@settings(max_examples=50)
def test_spl::selectstat_instantiation(instance):
    assert isinstance(instance, SPL::SelectStat)

@given(instance=SPL::WhenStat_strategy)
@settings(max_examples=50)
def test_spl::whenstat_instantiation(instance):
    assert isinstance(instance, SPL::WhenStat)

@given(instance=SPL::ForeachStat_strategy)
@settings(max_examples=50)
def test_spl::foreachstat_instantiation(instance):
    assert isinstance(instance, SPL::ForeachStat)

@given(instance=SPL::ForeachStat_strategy)
def test_spl::foreachstat_iteratorName_type(instance):
    assert isinstance(instance.iteratorName, str)


@given(instance=SPL::ForeachStat_strategy)
def test_spl::foreachstat_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=SPL::IfStat_strategy)
@settings(max_examples=50)
def test_spl::ifstat_instantiation(instance):
    assert isinstance(instance, SPL::IfStat)

@given(instance=SPL::DeclarationStat_strategy)
@settings(max_examples=50)
def test_spl::declarationstat_instantiation(instance):
    assert isinstance(instance, SPL::DeclarationStat)

@given(instance=SPL::SetStat_strategy)
@settings(max_examples=50)
def test_spl::setstat_instantiation(instance):
    assert isinstance(instance, SPL::SetStat)

@given(instance=SPL::BreakStat_strategy)
@settings(max_examples=50)
def test_spl::breakstat_instantiation(instance):
    assert isinstance(instance, SPL::BreakStat)

@given(instance=SPL::PushStat_strategy)
@settings(max_examples=50)
def test_spl::pushstat_instantiation(instance):
    assert isinstance(instance, SPL::PushStat)

@given(instance=SPL::ReturnStat_strategy)
@settings(max_examples=50)
def test_spl::returnstat_instantiation(instance):
    assert isinstance(instance, SPL::ReturnStat)

@given(instance=SPL::CompoundStat_strategy)
@settings(max_examples=50)
def test_spl::compoundstat_instantiation(instance):
    assert isinstance(instance, SPL::CompoundStat)

@given(instance=SPL::Variable_strategy)
@settings(max_examples=50)
def test_spl::variable_instantiation(instance):
    assert isinstance(instance, SPL::Variable)

@given(instance=FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_functiondeclaration_instantiation(instance):
    assert isinstance(instance, FunctionDeclaration)

@given(instance=SPL::LocalFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_spl::localfunctiondeclaration_instantiation(instance):
    assert isinstance(instance, SPL::LocalFunctionDeclaration)

@given(instance=SPL::RemoteFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_spl::remotefunctiondeclaration_instantiation(instance):
    assert isinstance(instance, SPL::RemoteFunctionDeclaration)

@given(instance=SPL::RemoteFunctionDeclaration_strategy)
def test_spl::remotefunctiondeclaration_functionLocation_type(instance):
    assert isinstance(instance.functionLocation, str)


@given(instance=SPL::RemoteFunctionDeclaration_strategy)
def test_spl::remotefunctiondeclaration_functionLocation_setter(instance):
    original = instance.functionLocation
    instance.functionLocation = original
    assert instance.functionLocation == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=SPL::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_spl::functiondeclaration_instantiation(instance):
    assert isinstance(instance, SPL::FunctionDeclaration)

@given(instance=SPL::StructureDeclaration_strategy)
@settings(max_examples=50)
def test_spl::structuredeclaration_instantiation(instance):
    assert isinstance(instance, SPL::StructureDeclaration)

@given(instance=SPL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_spl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, SPL::VariableDeclaration)

@given(instance=Branch_strategy)
@settings(max_examples=50)
def test_branch_instantiation(instance):
    assert isinstance(instance, Branch)

@given(instance=SPL::NamedBranch_strategy)
@settings(max_examples=50)
def test_spl::namedbranch_instantiation(instance):
    assert isinstance(instance, SPL::NamedBranch)

@given(instance=SPL::NamedBranch_strategy)
def test_spl::namedbranch_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SPL::NamedBranch_strategy)
def test_spl::namedbranch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL::DefaultBranch_strategy)
@settings(max_examples=50)
def test_spl::defaultbranch_instantiation(instance):
    assert isinstance(instance, SPL::DefaultBranch)

@given(instance=MethodName_strategy)
@settings(max_examples=50)
def test_methodname_instantiation(instance):
    assert isinstance(instance, MethodName)

@given(instance=SPL::ControlMethodName_strategy)
@settings(max_examples=50)
def test_spl::controlmethodname_instantiation(instance):
    assert isinstance(instance, SPL::ControlMethodName)

@given(instance=SPL::ControlMethodName_strategy)
def test_spl::controlmethodname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SPL::ControlMethodName_strategy)
def test_spl::controlmethodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL::SIPMethodName_strategy)
@settings(max_examples=50)
def test_spl::sipmethodname_instantiation(instance):
    assert isinstance(instance, SPL::SIPMethodName)

@given(instance=SPL::SIPMethodName_strategy)
def test_spl::sipmethodname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SPL::SIPMethodName_strategy)
def test_spl::sipmethodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=SPL::WhenHeader_strategy)
@settings(max_examples=50)
def test_spl::whenheader_instantiation(instance):
    assert isinstance(instance, SPL::WhenHeader)

@given(instance=SPL::WhenHeader_strategy)
def test_spl::whenheader_headerId_type(instance):
    assert isinstance(instance.headerId, str)


@given(instance=SPL::WhenHeader_strategy)
def test_spl::whenheader_headerId_setter(instance):
    original = instance.headerId
    instance.headerId = original
    assert instance.headerId == original

@given(instance=SPL::Argument_strategy)
@settings(max_examples=50)
def test_spl::argument_instantiation(instance):
    assert isinstance(instance, SPL::Argument)

@given(instance=TypeExpression_strategy)
@settings(max_examples=50)
def test_typeexpression_instantiation(instance):
    assert isinstance(instance, TypeExpression)

@given(instance=SPL::DefinedType_strategy)
@settings(max_examples=50)
def test_spl::definedtype_instantiation(instance):
    assert isinstance(instance, SPL::DefinedType)

@given(instance=SPL::DefinedType_strategy)
def test_spl::definedtype_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=SPL::DefinedType_strategy)
def test_spl::definedtype_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=SPL::SequenceType_strategy)
@settings(max_examples=50)
def test_spl::sequencetype_instantiation(instance):
    assert isinstance(instance, SPL::SequenceType)

@given(instance=SPL::SequenceType_strategy)
def test_spl::sequencetype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SPL::SequenceType_strategy)
def test_spl::sequencetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SPL::SequenceType_strategy)
def test_spl::sequencetype_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=SPL::SequenceType_strategy)
def test_spl::sequencetype_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=SPL::SequenceType_strategy)
def test_spl::sequencetype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=SPL::SequenceType_strategy)
def test_spl::sequencetype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=SPL::SimpleType_strategy)
@settings(max_examples=50)
def test_spl::simpletype_instantiation(instance):
    assert isinstance(instance, SPL::SimpleType)

@given(instance=SPL::SimpleType_strategy)
def test_spl::simpletype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SPL::SimpleType_strategy)
def test_spl::simpletype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Session_strategy)
@settings(max_examples=50)
def test_session_instantiation(instance):
    assert isinstance(instance, Session)

@given(instance=SPL::Event_strategy)
@settings(max_examples=50)
def test_spl::event_instantiation(instance):
    assert isinstance(instance, SPL::Event)

@given(instance=SPL::Event_strategy)
def test_spl::event_eventId_type(instance):
    assert isinstance(instance.eventId, str)


@given(instance=SPL::Event_strategy)
def test_spl::event_eventId_setter(instance):
    original = instance.eventId
    instance.eventId = original
    assert instance.eventId == original

@given(instance=SPL::Method_strategy)
@settings(max_examples=50)
def test_spl::method_instantiation(instance):
    assert isinstance(instance, SPL::Method)

@given(instance=SPL::Method_strategy)
def test_spl::method_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=SPL::Method_strategy)
def test_spl::method_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=SPL::Dialog_strategy)
@settings(max_examples=50)
def test_spl::dialog_instantiation(instance):
    assert isinstance(instance, SPL::Dialog)

@given(instance=SPL::Registration_strategy)
@settings(max_examples=50)
def test_spl::registration_instantiation(instance):
    assert isinstance(instance, SPL::Registration)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=SPL::Branch_strategy)
@settings(max_examples=50)
def test_spl::branch_instantiation(instance):
    assert isinstance(instance, SPL::Branch)

@given(instance=SPL::StructureProperty_strategy)
@settings(max_examples=50)
def test_spl::structureproperty_instantiation(instance):
    assert isinstance(instance, SPL::StructureProperty)

@given(instance=SPL::StructureProperty_strategy)
def test_spl::structureproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SPL::StructureProperty_strategy)
def test_spl::structureproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL::MethodName_strategy)
@settings(max_examples=50)
def test_spl::methodname_instantiation(instance):
    assert isinstance(instance, SPL::MethodName)

@given(instance=SPL::SelectMember_strategy)
@settings(max_examples=50)
def test_spl::selectmember_instantiation(instance):
    assert isinstance(instance, SPL::SelectMember)

@given(instance=SPL::MessageField_strategy)
@settings(max_examples=50)
def test_spl::messagefield_instantiation(instance):
    assert isinstance(instance, SPL::MessageField)

@given(instance=SPL::Service_strategy)
@settings(max_examples=50)
def test_spl::service_instantiation(instance):
    assert isinstance(instance, SPL::Service)

@given(instance=SPL::Service_strategy)
def test_spl::service_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SPL::Service_strategy)
def test_spl::service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL::Constant_strategy)
@settings(max_examples=50)
def test_spl::constant_instantiation(instance):
    assert isinstance(instance, SPL::Constant)

@given(instance=SPL::Session_strategy)
@settings(max_examples=50)
def test_spl::session_instantiation(instance):
    assert isinstance(instance, SPL::Session)

@given(instance=SPL::FunctionCall_strategy)
@settings(max_examples=50)
def test_spl::functioncall_instantiation(instance):
    assert isinstance(instance, SPL::FunctionCall)

@given(instance=SPL::Statement_strategy)
@settings(max_examples=50)
def test_spl::statement_instantiation(instance):
    assert isinstance(instance, SPL::Statement)

@given(instance=SPL::Declaration_strategy)
@settings(max_examples=50)
def test_spl::declaration_instantiation(instance):
    assert isinstance(instance, SPL::Declaration)

@given(instance=SPL::Declaration_strategy)
def test_spl::declaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SPL::Declaration_strategy)
def test_spl::declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SPL::Response_strategy)
@settings(max_examples=50)
def test_spl::response_instantiation(instance):
    assert isinstance(instance, SPL::Response)

@given(instance=SPL::Expression_strategy)
@settings(max_examples=50)
def test_spl::expression_instantiation(instance):
    assert isinstance(instance, SPL::Expression)

@given(instance=SPL::Program_strategy)
@settings(max_examples=50)
def test_spl::program_instantiation(instance):
    assert isinstance(instance, SPL::Program)

@given(instance=SPL::TypeExpression_strategy)
@settings(max_examples=50)
def test_spl::typeexpression_instantiation(instance):
    assert isinstance(instance, SPL::TypeExpression)

@given(instance=SPL::LocatedElement_strategy)
@settings(max_examples=50)
def test_spl::locatedelement_instantiation(instance):
    assert isinstance(instance, SPL::LocatedElement)

@given(instance=SPL::LocatedElement_strategy)
def test_spl::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=SPL::LocatedElement_strategy)
def test_spl::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=SPL::LocatedElement_strategy)
def test_spl::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=SPL::LocatedElement_strategy)
def test_spl::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=SPL::LocatedElement_strategy)
def test_spl::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=SPL::LocatedElement_strategy)
def test_spl::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
