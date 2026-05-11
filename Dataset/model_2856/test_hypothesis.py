import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ir::AnnotationArgument,
    ir::State,
    Type,
    ir::TypeFloat,
    ir::TypeInt,
    ir::TypeLambda,
    ir::TypeList,
    ir::TypeExternal,
    ir::TypeProc,
    ir::TypeUint,
    ir::TypeString,
    ir::TypeBool,
    LambdaExpression,
    ir::TypeUser,
    ir::TypeUndef,
    PortAccess,
    ir::PortPeek,
    Block,
    Statement,
    ir::WhileLoop,
    ir::IfStatement,
    ir::ReturnValue,
    ir::ProcCall,
    ir::ForEach,
    ir::Assign,
    Connection,
    ir::FromSource,
    ir::ToSink,
    ir::Point2PointConnection,
    LiteralExpression,
    ir::BooleanLiteral,
    ir::StringLiteral,
    ir::FloatLiteral,
    ir::IntegerLiteral,
    Expression,
    ir::IfExpression,
    ir::VariableExpression,
    ir::ListExpression,
    ir::LiteralExpression,
    ExpressionCall,
    ir::TypeConstructorCall,
    ir::FunctionCall,
    ir::ExpressionCall,
    ir::UnaryExpression,
    ir::BinaryExpression,
    Variable,
    ir::PortRead,
    ir::PortWrite,
    ir::Guard,
    ir::ActorInstance,
    ir::Schedule,
    AbstractActor,
    ir::Actor,
    ir::Network,
    ir::ExternalActor,
    Scope,
    ir::Action,
    ir::AbstractActor,
    ir::Block,
    ir::ProcExpression,
    ir::LambdaExpression,
    ir::Generator,
    ir::Namespace,
    ir::TaggedExpression,
    ir::Type,
    Declaration,
    ir::TypeDeclarationImport,
    ir::VariableExternal,
    ir::TypeConstructor,
    ir::ForwardDeclaration,
    ir::TypeDeclaration,
    ir::VariableImport,
    ir::Annotation,
    ir::Node,
    Node,
    ir::PortInstance,
    ir::Expression,
    ir::PortAccess,
    ir::TypeRecord,
    ir::VariableReference,
    ir::Connection,
    ir::Member,
    ir::Statement,
    ir::Declaration,
    ir::Scope,
    ir::Variable,
    ir::Port,
    ir::TypeActor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ir::annotationargument_is_not_abstract():
    assert not inspect.isabstract(ir::AnnotationArgument)


def test_ir::annotationargument_constructor_exists():
    assert callable(ir::AnnotationArgument.__init__)


def test_ir::annotationargument_constructor_args():
    sig = inspect.signature(ir::AnnotationArgument.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"

def test_ir::annotationargument_has_value():
    assert hasattr(ir::AnnotationArgument, "value")
    descriptor = None
    for klass in ir::AnnotationArgument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ir::annotationargument_has_id():
    assert hasattr(ir::AnnotationArgument, "id")
    descriptor = None
    for klass in ir::AnnotationArgument.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ir::state_is_not_abstract():
    assert not inspect.isabstract(ir::State)


def test_ir::state_constructor_exists():
    assert callable(ir::State.__init__)


def test_ir::state_constructor_args():
    sig = inspect.signature(ir::State.__init__)
    params = list(sig.parameters.keys())
    assert "PriorityGraph" in params, "Missing parameter 'PriorityGraph'"
    assert "Action2TargetMap" in params, "Missing parameter 'Action2TargetMap'"
    assert "name" in params, "Missing parameter 'name'"

def test_ir::state_has_PriorityGraph():
    assert hasattr(ir::State, "PriorityGraph")
    descriptor = None
    for klass in ir::State.__mro__:
        if "PriorityGraph" in klass.__dict__:
            descriptor = klass.__dict__["PriorityGraph"]
            break
    assert isinstance(descriptor, property)

def test_ir::state_has_Action2TargetMap():
    assert hasattr(ir::State, "Action2TargetMap")
    descriptor = None
    for klass in ir::State.__mro__:
        if "Action2TargetMap" in klass.__dict__:
            descriptor = klass.__dict__["Action2TargetMap"]
            break
    assert isinstance(descriptor, property)

def test_ir::state_has_name():
    assert hasattr(ir::State, "name")
    descriptor = None
    for klass in ir::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ir::typefloat_is_not_abstract():
    assert not inspect.isabstract(ir::TypeFloat)


def test_ir::typefloat_constructor_exists():
    assert callable(ir::TypeFloat.__init__)


def test_ir::typefloat_constructor_args():
    sig = inspect.signature(ir::TypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_ir::typeint_is_not_abstract():
    assert not inspect.isabstract(ir::TypeInt)


def test_ir::typeint_constructor_exists():
    assert callable(ir::TypeInt.__init__)


def test_ir::typeint_constructor_args():
    sig = inspect.signature(ir::TypeInt.__init__)
    params = list(sig.parameters.keys())



def test_ir::typelambda_is_not_abstract():
    assert not inspect.isabstract(ir::TypeLambda)


def test_ir::typelambda_constructor_exists():
    assert callable(ir::TypeLambda.__init__)


def test_ir::typelambda_constructor_args():
    sig = inspect.signature(ir::TypeLambda.__init__)
    params = list(sig.parameters.keys())



def test_ir::typelist_is_not_abstract():
    assert not inspect.isabstract(ir::TypeList)


def test_ir::typelist_constructor_exists():
    assert callable(ir::TypeList.__init__)


def test_ir::typelist_constructor_args():
    sig = inspect.signature(ir::TypeList.__init__)
    params = list(sig.parameters.keys())



def test_ir::typeexternal_is_not_abstract():
    assert not inspect.isabstract(ir::TypeExternal)


def test_ir::typeexternal_constructor_exists():
    assert callable(ir::TypeExternal.__init__)


def test_ir::typeexternal_constructor_args():
    sig = inspect.signature(ir::TypeExternal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "scopeName" in params, "Missing parameter 'scopeName'"

def test_ir::typeexternal_has_name():
    assert hasattr(ir::TypeExternal, "name")
    descriptor = None
    for klass in ir::TypeExternal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir::typeexternal_has_scopeName():
    assert hasattr(ir::TypeExternal, "scopeName")
    descriptor = None
    for klass in ir::TypeExternal.__mro__:
        if "scopeName" in klass.__dict__:
            descriptor = klass.__dict__["scopeName"]
            break
    assert isinstance(descriptor, property)



def test_ir::typeproc_is_not_abstract():
    assert not inspect.isabstract(ir::TypeProc)


def test_ir::typeproc_constructor_exists():
    assert callable(ir::TypeProc.__init__)


def test_ir::typeproc_constructor_args():
    sig = inspect.signature(ir::TypeProc.__init__)
    params = list(sig.parameters.keys())



def test_ir::typeuint_is_not_abstract():
    assert not inspect.isabstract(ir::TypeUint)


def test_ir::typeuint_constructor_exists():
    assert callable(ir::TypeUint.__init__)


def test_ir::typeuint_constructor_args():
    sig = inspect.signature(ir::TypeUint.__init__)
    params = list(sig.parameters.keys())



def test_ir::typestring_is_not_abstract():
    assert not inspect.isabstract(ir::TypeString)


def test_ir::typestring_constructor_exists():
    assert callable(ir::TypeString.__init__)


def test_ir::typestring_constructor_args():
    sig = inspect.signature(ir::TypeString.__init__)
    params = list(sig.parameters.keys())



def test_ir::typebool_is_not_abstract():
    assert not inspect.isabstract(ir::TypeBool)


def test_ir::typebool_constructor_exists():
    assert callable(ir::TypeBool.__init__)


def test_ir::typebool_constructor_args():
    sig = inspect.signature(ir::TypeBool.__init__)
    params = list(sig.parameters.keys())



def test_lambdaexpression_is_not_abstract():
    assert not inspect.isabstract(LambdaExpression)


def test_lambdaexpression_constructor_exists():
    assert callable(LambdaExpression.__init__)


def test_lambdaexpression_constructor_args():
    sig = inspect.signature(LambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir::typeuser_is_not_abstract():
    assert not inspect.isabstract(ir::TypeUser)


def test_ir::typeuser_constructor_exists():
    assert callable(ir::TypeUser.__init__)


def test_ir::typeuser_constructor_args():
    sig = inspect.signature(ir::TypeUser.__init__)
    params = list(sig.parameters.keys())



def test_ir::typeundef_is_not_abstract():
    assert not inspect.isabstract(ir::TypeUndef)


def test_ir::typeundef_constructor_exists():
    assert callable(ir::TypeUndef.__init__)


def test_ir::typeundef_constructor_args():
    sig = inspect.signature(ir::TypeUndef.__init__)
    params = list(sig.parameters.keys())



def test_portaccess_is_not_abstract():
    assert not inspect.isabstract(PortAccess)


def test_portaccess_constructor_exists():
    assert callable(PortAccess.__init__)


def test_portaccess_constructor_args():
    sig = inspect.signature(PortAccess.__init__)
    params = list(sig.parameters.keys())



def test_ir::portpeek_is_not_abstract():
    assert not inspect.isabstract(ir::PortPeek)


def test_ir::portpeek_constructor_exists():
    assert callable(ir::PortPeek.__init__)


def test_ir::portpeek_constructor_args():
    sig = inspect.signature(ir::PortPeek.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_ir::portpeek_has_position():
    assert hasattr(ir::PortPeek, "position")
    descriptor = None
    for klass in ir::PortPeek.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ir::whileloop_is_not_abstract():
    assert not inspect.isabstract(ir::WhileLoop)


def test_ir::whileloop_constructor_exists():
    assert callable(ir::WhileLoop.__init__)


def test_ir::whileloop_constructor_args():
    sig = inspect.signature(ir::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_ir::ifstatement_is_not_abstract():
    assert not inspect.isabstract(ir::IfStatement)


def test_ir::ifstatement_constructor_exists():
    assert callable(ir::IfStatement.__init__)


def test_ir::ifstatement_constructor_args():
    sig = inspect.signature(ir::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ir::returnvalue_is_not_abstract():
    assert not inspect.isabstract(ir::ReturnValue)


def test_ir::returnvalue_constructor_exists():
    assert callable(ir::ReturnValue.__init__)


def test_ir::returnvalue_constructor_args():
    sig = inspect.signature(ir::ReturnValue.__init__)
    params = list(sig.parameters.keys())



def test_ir::proccall_is_not_abstract():
    assert not inspect.isabstract(ir::ProcCall)


def test_ir::proccall_constructor_exists():
    assert callable(ir::ProcCall.__init__)


def test_ir::proccall_constructor_args():
    sig = inspect.signature(ir::ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_ir::foreach_is_not_abstract():
    assert not inspect.isabstract(ir::ForEach)


def test_ir::foreach_constructor_exists():
    assert callable(ir::ForEach.__init__)


def test_ir::foreach_constructor_args():
    sig = inspect.signature(ir::ForEach.__init__)
    params = list(sig.parameters.keys())



def test_ir::assign_is_not_abstract():
    assert not inspect.isabstract(ir::Assign)


def test_ir::assign_constructor_exists():
    assert callable(ir::Assign.__init__)


def test_ir::assign_constructor_args():
    sig = inspect.signature(ir::Assign.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_ir::fromsource_is_not_abstract():
    assert not inspect.isabstract(ir::FromSource)


def test_ir::fromsource_constructor_exists():
    assert callable(ir::FromSource.__init__)


def test_ir::fromsource_constructor_args():
    sig = inspect.signature(ir::FromSource.__init__)
    params = list(sig.parameters.keys())



def test_ir::tosink_is_not_abstract():
    assert not inspect.isabstract(ir::ToSink)


def test_ir::tosink_constructor_exists():
    assert callable(ir::ToSink.__init__)


def test_ir::tosink_constructor_args():
    sig = inspect.signature(ir::ToSink.__init__)
    params = list(sig.parameters.keys())



def test_ir::point2pointconnection_is_not_abstract():
    assert not inspect.isabstract(ir::Point2PointConnection)


def test_ir::point2pointconnection_constructor_exists():
    assert callable(ir::Point2PointConnection.__init__)


def test_ir::point2pointconnection_constructor_args():
    sig = inspect.signature(ir::Point2PointConnection.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(ir::BooleanLiteral)


def test_ir::booleanliteral_constructor_exists():
    assert callable(ir::BooleanLiteral.__init__)


def test_ir::booleanliteral_constructor_args():
    sig = inspect.signature(ir::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::booleanliteral_has_value():
    assert hasattr(ir::BooleanLiteral, "value")
    descriptor = None
    for klass in ir::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::stringliteral_is_not_abstract():
    assert not inspect.isabstract(ir::StringLiteral)


def test_ir::stringliteral_constructor_exists():
    assert callable(ir::StringLiteral.__init__)


def test_ir::stringliteral_constructor_args():
    sig = inspect.signature(ir::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::stringliteral_has_value():
    assert hasattr(ir::StringLiteral, "value")
    descriptor = None
    for klass in ir::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::floatliteral_is_not_abstract():
    assert not inspect.isabstract(ir::FloatLiteral)


def test_ir::floatliteral_constructor_exists():
    assert callable(ir::FloatLiteral.__init__)


def test_ir::floatliteral_constructor_args():
    sig = inspect.signature(ir::FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::floatliteral_has_value():
    assert hasattr(ir::FloatLiteral, "value")
    descriptor = None
    for klass in ir::FloatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::integerliteral_is_not_abstract():
    assert not inspect.isabstract(ir::IntegerLiteral)


def test_ir::integerliteral_constructor_exists():
    assert callable(ir::IntegerLiteral.__init__)


def test_ir::integerliteral_constructor_args():
    sig = inspect.signature(ir::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::integerliteral_has_value():
    assert hasattr(ir::IntegerLiteral, "value")
    descriptor = None
    for klass in ir::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ir::ifexpression_is_not_abstract():
    assert not inspect.isabstract(ir::IfExpression)


def test_ir::ifexpression_constructor_exists():
    assert callable(ir::IfExpression.__init__)


def test_ir::ifexpression_constructor_args():
    sig = inspect.signature(ir::IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir::variableexpression_is_not_abstract():
    assert not inspect.isabstract(ir::VariableExpression)


def test_ir::variableexpression_constructor_exists():
    assert callable(ir::VariableExpression.__init__)


def test_ir::variableexpression_constructor_args():
    sig = inspect.signature(ir::VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir::listexpression_is_not_abstract():
    assert not inspect.isabstract(ir::ListExpression)


def test_ir::listexpression_constructor_exists():
    assert callable(ir::ListExpression.__init__)


def test_ir::listexpression_constructor_args():
    sig = inspect.signature(ir::ListExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir::literalexpression_is_not_abstract():
    assert not inspect.isabstract(ir::LiteralExpression)


def test_ir::literalexpression_constructor_exists():
    assert callable(ir::LiteralExpression.__init__)


def test_ir::literalexpression_constructor_args():
    sig = inspect.signature(ir::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressioncall_is_not_abstract():
    assert not inspect.isabstract(ExpressionCall)


def test_expressioncall_constructor_exists():
    assert callable(ExpressionCall.__init__)


def test_expressioncall_constructor_args():
    sig = inspect.signature(ExpressionCall.__init__)
    params = list(sig.parameters.keys())



def test_ir::typeconstructorcall_is_not_abstract():
    assert not inspect.isabstract(ir::TypeConstructorCall)


def test_ir::typeconstructorcall_constructor_exists():
    assert callable(ir::TypeConstructorCall.__init__)


def test_ir::typeconstructorcall_constructor_args():
    sig = inspect.signature(ir::TypeConstructorCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::typeconstructorcall_has_name():
    assert hasattr(ir::TypeConstructorCall, "name")
    descriptor = None
    for klass in ir::TypeConstructorCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::functioncall_is_not_abstract():
    assert not inspect.isabstract(ir::FunctionCall)


def test_ir::functioncall_constructor_exists():
    assert callable(ir::FunctionCall.__init__)


def test_ir::functioncall_constructor_args():
    sig = inspect.signature(ir::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_ir::expressioncall_is_not_abstract():
    assert not inspect.isabstract(ir::ExpressionCall)


def test_ir::expressioncall_constructor_exists():
    assert callable(ir::ExpressionCall.__init__)


def test_ir::expressioncall_constructor_args():
    sig = inspect.signature(ir::ExpressionCall.__init__)
    params = list(sig.parameters.keys())



def test_ir::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(ir::UnaryExpression)


def test_ir::unaryexpression_constructor_exists():
    assert callable(ir::UnaryExpression.__init__)


def test_ir::unaryexpression_constructor_args():
    sig = inspect.signature(ir::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir::unaryexpression_has_operator():
    assert hasattr(ir::UnaryExpression, "operator")
    descriptor = None
    for klass in ir::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ir::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(ir::BinaryExpression)


def test_ir::binaryexpression_constructor_exists():
    assert callable(ir::BinaryExpression.__init__)


def test_ir::binaryexpression_constructor_args():
    sig = inspect.signature(ir::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir::binaryexpression_has_operator():
    assert hasattr(ir::BinaryExpression, "operator")
    descriptor = None
    for klass in ir::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_ir::portread_is_not_abstract():
    assert not inspect.isabstract(ir::PortRead)


def test_ir::portread_constructor_exists():
    assert callable(ir::PortRead.__init__)


def test_ir::portread_constructor_args():
    sig = inspect.signature(ir::PortRead.__init__)
    params = list(sig.parameters.keys())



def test_ir::portwrite_is_not_abstract():
    assert not inspect.isabstract(ir::PortWrite)


def test_ir::portwrite_constructor_exists():
    assert callable(ir::PortWrite.__init__)


def test_ir::portwrite_constructor_args():
    sig = inspect.signature(ir::PortWrite.__init__)
    params = list(sig.parameters.keys())



def test_ir::guard_is_not_abstract():
    assert not inspect.isabstract(ir::Guard)


def test_ir::guard_constructor_exists():
    assert callable(ir::Guard.__init__)


def test_ir::guard_constructor_args():
    sig = inspect.signature(ir::Guard.__init__)
    params = list(sig.parameters.keys())



def test_ir::actorinstance_is_not_abstract():
    assert not inspect.isabstract(ir::ActorInstance)


def test_ir::actorinstance_constructor_exists():
    assert callable(ir::ActorInstance.__init__)


def test_ir::actorinstance_constructor_args():
    sig = inspect.signature(ir::ActorInstance.__init__)
    params = list(sig.parameters.keys())



def test_ir::schedule_is_not_abstract():
    assert not inspect.isabstract(ir::Schedule)


def test_ir::schedule_constructor_exists():
    assert callable(ir::Schedule.__init__)


def test_ir::schedule_constructor_args():
    sig = inspect.signature(ir::Schedule.__init__)
    params = list(sig.parameters.keys())
    assert "PriorityGraph" in params, "Missing parameter 'PriorityGraph'"

def test_ir::schedule_has_PriorityGraph():
    assert hasattr(ir::Schedule, "PriorityGraph")
    descriptor = None
    for klass in ir::Schedule.__mro__:
        if "PriorityGraph" in klass.__dict__:
            descriptor = klass.__dict__["PriorityGraph"]
            break
    assert isinstance(descriptor, property)



def test_abstractactor_is_not_abstract():
    assert not inspect.isabstract(AbstractActor)


def test_abstractactor_constructor_exists():
    assert callable(AbstractActor.__init__)


def test_abstractactor_constructor_args():
    sig = inspect.signature(AbstractActor.__init__)
    params = list(sig.parameters.keys())



def test_ir::actor_is_not_abstract():
    assert not inspect.isabstract(ir::Actor)


def test_ir::actor_constructor_exists():
    assert callable(ir::Actor.__init__)


def test_ir::actor_constructor_args():
    sig = inspect.signature(ir::Actor.__init__)
    params = list(sig.parameters.keys())



def test_ir::network_is_not_abstract():
    assert not inspect.isabstract(ir::Network)


def test_ir::network_constructor_exists():
    assert callable(ir::Network.__init__)


def test_ir::network_constructor_args():
    sig = inspect.signature(ir::Network.__init__)
    params = list(sig.parameters.keys())



def test_ir::externalactor_is_not_abstract():
    assert not inspect.isabstract(ir::ExternalActor)


def test_ir::externalactor_constructor_exists():
    assert callable(ir::ExternalActor.__init__)


def test_ir::externalactor_constructor_args():
    sig = inspect.signature(ir::ExternalActor.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_ir::action_is_not_abstract():
    assert not inspect.isabstract(ir::Action)


def test_ir::action_constructor_exists():
    assert callable(ir::Action.__init__)


def test_ir::action_constructor_args():
    sig = inspect.signature(ir::Action.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"

def test_ir::action_has_tag():
    assert hasattr(ir::Action, "tag")
    descriptor = None
    for klass in ir::Action.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_ir::abstractactor_is_not_abstract():
    assert not inspect.isabstract(ir::AbstractActor)


def test_ir::abstractactor_constructor_exists():
    assert callable(ir::AbstractActor.__init__)


def test_ir::abstractactor_constructor_args():
    sig = inspect.signature(ir::AbstractActor.__init__)
    params = list(sig.parameters.keys())



def test_ir::block_is_not_abstract():
    assert not inspect.isabstract(ir::Block)


def test_ir::block_constructor_exists():
    assert callable(ir::Block.__init__)


def test_ir::block_constructor_args():
    sig = inspect.signature(ir::Block.__init__)
    params = list(sig.parameters.keys())



def test_ir::procexpression_is_not_abstract():
    assert not inspect.isabstract(ir::ProcExpression)


def test_ir::procexpression_constructor_exists():
    assert callable(ir::ProcExpression.__init__)


def test_ir::procexpression_constructor_args():
    sig = inspect.signature(ir::ProcExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir::lambdaexpression_is_not_abstract():
    assert not inspect.isabstract(ir::LambdaExpression)


def test_ir::lambdaexpression_constructor_exists():
    assert callable(ir::LambdaExpression.__init__)


def test_ir::lambdaexpression_constructor_args():
    sig = inspect.signature(ir::LambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir::generator_is_not_abstract():
    assert not inspect.isabstract(ir::Generator)


def test_ir::generator_constructor_exists():
    assert callable(ir::Generator.__init__)


def test_ir::generator_constructor_args():
    sig = inspect.signature(ir::Generator.__init__)
    params = list(sig.parameters.keys())



def test_ir::namespace_is_not_abstract():
    assert not inspect.isabstract(ir::Namespace)


def test_ir::namespace_constructor_exists():
    assert callable(ir::Namespace.__init__)


def test_ir::namespace_constructor_args():
    sig = inspect.signature(ir::Namespace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::namespace_has_name():
    assert hasattr(ir::Namespace, "name")
    descriptor = None
    for klass in ir::Namespace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::taggedexpression_is_not_abstract():
    assert not inspect.isabstract(ir::TaggedExpression)


def test_ir::taggedexpression_constructor_exists():
    assert callable(ir::TaggedExpression.__init__)


def test_ir::taggedexpression_constructor_args():
    sig = inspect.signature(ir::TaggedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"

def test_ir::taggedexpression_has_tag():
    assert hasattr(ir::TaggedExpression, "tag")
    descriptor = None
    for klass in ir::TaggedExpression.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_ir::type_is_not_abstract():
    assert not inspect.isabstract(ir::Type)


def test_ir::type_constructor_exists():
    assert callable(ir::Type.__init__)


def test_ir::type_constructor_args():
    sig = inspect.signature(ir::Type.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_ir::typedeclarationimport_is_not_abstract():
    assert not inspect.isabstract(ir::TypeDeclarationImport)


def test_ir::typedeclarationimport_constructor_exists():
    assert callable(ir::TypeDeclarationImport.__init__)


def test_ir::typedeclarationimport_constructor_args():
    sig = inspect.signature(ir::TypeDeclarationImport.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_ir::typedeclarationimport_has_namespace():
    assert hasattr(ir::TypeDeclarationImport, "namespace")
    descriptor = None
    for klass in ir::TypeDeclarationImport.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_ir::variableexternal_is_not_abstract():
    assert not inspect.isabstract(ir::VariableExternal)


def test_ir::variableexternal_constructor_exists():
    assert callable(ir::VariableExternal.__init__)


def test_ir::variableexternal_constructor_args():
    sig = inspect.signature(ir::VariableExternal.__init__)
    params = list(sig.parameters.keys())



def test_ir::typeconstructor_is_not_abstract():
    assert not inspect.isabstract(ir::TypeConstructor)


def test_ir::typeconstructor_constructor_exists():
    assert callable(ir::TypeConstructor.__init__)


def test_ir::typeconstructor_constructor_args():
    sig = inspect.signature(ir::TypeConstructor.__init__)
    params = list(sig.parameters.keys())



def test_ir::forwarddeclaration_is_not_abstract():
    assert not inspect.isabstract(ir::ForwardDeclaration)


def test_ir::forwarddeclaration_constructor_exists():
    assert callable(ir::ForwardDeclaration.__init__)


def test_ir::forwarddeclaration_constructor_args():
    sig = inspect.signature(ir::ForwardDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ir::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(ir::TypeDeclaration)


def test_ir::typedeclaration_constructor_exists():
    assert callable(ir::TypeDeclaration.__init__)


def test_ir::typedeclaration_constructor_args():
    sig = inspect.signature(ir::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ir::variableimport_is_not_abstract():
    assert not inspect.isabstract(ir::VariableImport)


def test_ir::variableimport_constructor_exists():
    assert callable(ir::VariableImport.__init__)


def test_ir::variableimport_constructor_args():
    sig = inspect.signature(ir::VariableImport.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_ir::variableimport_has_namespace():
    assert hasattr(ir::VariableImport, "namespace")
    descriptor = None
    for klass in ir::VariableImport.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_ir::annotation_is_not_abstract():
    assert not inspect.isabstract(ir::Annotation)


def test_ir::annotation_constructor_exists():
    assert callable(ir::Annotation.__init__)


def test_ir::annotation_constructor_args():
    sig = inspect.signature(ir::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::annotation_has_name():
    assert hasattr(ir::Annotation, "name")
    descriptor = None
    for klass in ir::Annotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::node_is_not_abstract():
    assert not inspect.isabstract(ir::Node)


def test_ir::node_constructor_exists():
    assert callable(ir::Node.__init__)


def test_ir::node_constructor_args():
    sig = inspect.signature(ir::Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ir::node_has_id():
    assert hasattr(ir::Node, "id")
    descriptor = None
    for klass in ir::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_ir::portinstance_is_not_abstract():
    assert not inspect.isabstract(ir::PortInstance)


def test_ir::portinstance_constructor_exists():
    assert callable(ir::PortInstance.__init__)


def test_ir::portinstance_constructor_args():
    sig = inspect.signature(ir::PortInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::portinstance_has_name():
    assert hasattr(ir::PortInstance, "name")
    descriptor = None
    for klass in ir::PortInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::expression_is_not_abstract():
    assert not inspect.isabstract(ir::Expression)


def test_ir::expression_constructor_exists():
    assert callable(ir::Expression.__init__)


def test_ir::expression_constructor_args():
    sig = inspect.signature(ir::Expression.__init__)
    params = list(sig.parameters.keys())



def test_ir::portaccess_is_not_abstract():
    assert not inspect.isabstract(ir::PortAccess)


def test_ir::portaccess_constructor_exists():
    assert callable(ir::PortAccess.__init__)


def test_ir::portaccess_constructor_args():
    sig = inspect.signature(ir::PortAccess.__init__)
    params = list(sig.parameters.keys())



def test_ir::typerecord_is_not_abstract():
    assert not inspect.isabstract(ir::TypeRecord)


def test_ir::typerecord_constructor_exists():
    assert callable(ir::TypeRecord.__init__)


def test_ir::typerecord_constructor_args():
    sig = inspect.signature(ir::TypeRecord.__init__)
    params = list(sig.parameters.keys())



def test_ir::variablereference_is_not_abstract():
    assert not inspect.isabstract(ir::VariableReference)


def test_ir::variablereference_constructor_exists():
    assert callable(ir::VariableReference.__init__)


def test_ir::variablereference_constructor_args():
    sig = inspect.signature(ir::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_ir::connection_is_not_abstract():
    assert not inspect.isabstract(ir::Connection)


def test_ir::connection_constructor_exists():
    assert callable(ir::Connection.__init__)


def test_ir::connection_constructor_args():
    sig = inspect.signature(ir::Connection.__init__)
    params = list(sig.parameters.keys())



def test_ir::member_is_not_abstract():
    assert not inspect.isabstract(ir::Member)


def test_ir::member_constructor_exists():
    assert callable(ir::Member.__init__)


def test_ir::member_constructor_args():
    sig = inspect.signature(ir::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::member_has_name():
    assert hasattr(ir::Member, "name")
    descriptor = None
    for klass in ir::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::statement_is_not_abstract():
    assert not inspect.isabstract(ir::Statement)


def test_ir::statement_constructor_exists():
    assert callable(ir::Statement.__init__)


def test_ir::statement_constructor_args():
    sig = inspect.signature(ir::Statement.__init__)
    params = list(sig.parameters.keys())



def test_ir::declaration_is_not_abstract():
    assert not inspect.isabstract(ir::Declaration)


def test_ir::declaration_constructor_exists():
    assert callable(ir::Declaration.__init__)


def test_ir::declaration_constructor_args():
    sig = inspect.signature(ir::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::declaration_has_name():
    assert hasattr(ir::Declaration, "name")
    descriptor = None
    for klass in ir::Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::scope_is_not_abstract():
    assert not inspect.isabstract(ir::Scope)


def test_ir::scope_constructor_exists():
    assert callable(ir::Scope.__init__)


def test_ir::scope_constructor_args():
    sig = inspect.signature(ir::Scope.__init__)
    params = list(sig.parameters.keys())



def test_ir::variable_is_not_abstract():
    assert not inspect.isabstract(ir::Variable)


def test_ir::variable_constructor_exists():
    assert callable(ir::Variable.__init__)


def test_ir::variable_constructor_args():
    sig = inspect.signature(ir::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_ir::variable_has_constant():
    assert hasattr(ir::Variable, "constant")
    descriptor = None
    for klass in ir::Variable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_ir::variable_has_parameter():
    assert hasattr(ir::Variable, "parameter")
    descriptor = None
    for klass in ir::Variable.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_ir::port_is_not_abstract():
    assert not inspect.isabstract(ir::Port)


def test_ir::port_constructor_exists():
    assert callable(ir::Port.__init__)


def test_ir::port_constructor_args():
    sig = inspect.signature(ir::Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::port_has_name():
    assert hasattr(ir::Port, "name")
    descriptor = None
    for klass in ir::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::typeactor_is_not_abstract():
    assert not inspect.isabstract(ir::TypeActor)


def test_ir::typeactor_constructor_exists():
    assert callable(ir::TypeActor.__init__)


def test_ir::typeactor_constructor_args():
    sig = inspect.signature(ir::TypeActor.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "name" in params, "Missing parameter 'name'"

def test_ir::typeactor_has_namespace():
    assert hasattr(ir::TypeActor, "namespace")
    descriptor = None
    for klass in ir::TypeActor.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_ir::typeactor_has_name():
    assert hasattr(ir::TypeActor, "name")
    descriptor = None
    for klass in ir::TypeActor.__mro__:
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
ir::AnnotationArgument_strategy = st.builds(
    ir::AnnotationArgument,
    value=
        safe_text,
    id=
        safe_text
)
ir::State_strategy = st.builds(
    ir::State,
    PriorityGraph=
        safe_text,
    Action2TargetMap=
        safe_text,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ir::TypeFloat_strategy = st.builds(
    ir::TypeFloat,
)
ir::TypeInt_strategy = st.builds(
    ir::TypeInt,
)
ir::TypeLambda_strategy = st.builds(
    ir::TypeLambda,
)
ir::TypeList_strategy = st.builds(
    ir::TypeList,
)
ir::TypeExternal_strategy = st.builds(
    ir::TypeExternal,
    name=
        safe_text,
    scopeName=
        safe_text
)
ir::TypeProc_strategy = st.builds(
    ir::TypeProc,
)
ir::TypeUint_strategy = st.builds(
    ir::TypeUint,
)
ir::TypeString_strategy = st.builds(
    ir::TypeString,
)
ir::TypeBool_strategy = st.builds(
    ir::TypeBool,
)
LambdaExpression_strategy = st.builds(
    LambdaExpression,
)
ir::TypeUser_strategy = st.builds(
    ir::TypeUser,
)
ir::TypeUndef_strategy = st.builds(
    ir::TypeUndef,
)
PortAccess_strategy = st.builds(
    PortAccess,
)
ir::PortPeek_strategy = st.builds(
    ir::PortPeek,
    position=
        st.integers()
)
Block_strategy = st.builds(
    Block,
)
Statement_strategy = st.builds(
    Statement,
)
ir::WhileLoop_strategy = st.builds(
    ir::WhileLoop,
)
ir::IfStatement_strategy = st.builds(
    ir::IfStatement,
)
ir::ReturnValue_strategy = st.builds(
    ir::ReturnValue,
)
ir::ProcCall_strategy = st.builds(
    ir::ProcCall,
)
ir::ForEach_strategy = st.builds(
    ir::ForEach,
)
ir::Assign_strategy = st.builds(
    ir::Assign,
)
Connection_strategy = st.builds(
    Connection,
)
ir::FromSource_strategy = st.builds(
    ir::FromSource,
)
ir::ToSink_strategy = st.builds(
    ir::ToSink,
)
ir::Point2PointConnection_strategy = st.builds(
    ir::Point2PointConnection,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
ir::BooleanLiteral_strategy = st.builds(
    ir::BooleanLiteral,
    value=
        st.booleans()
)
ir::StringLiteral_strategy = st.builds(
    ir::StringLiteral,
    value=
        safe_text
)
ir::FloatLiteral_strategy = st.builds(
    ir::FloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ir::IntegerLiteral_strategy = st.builds(
    ir::IntegerLiteral,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
ir::IfExpression_strategy = st.builds(
    ir::IfExpression,
)
ir::VariableExpression_strategy = st.builds(
    ir::VariableExpression,
)
ir::ListExpression_strategy = st.builds(
    ir::ListExpression,
)
ir::LiteralExpression_strategy = st.builds(
    ir::LiteralExpression,
)
ExpressionCall_strategy = st.builds(
    ExpressionCall,
)
ir::TypeConstructorCall_strategy = st.builds(
    ir::TypeConstructorCall,
    name=
        safe_text
)
ir::FunctionCall_strategy = st.builds(
    ir::FunctionCall,
)
ir::ExpressionCall_strategy = st.builds(
    ir::ExpressionCall,
)
ir::UnaryExpression_strategy = st.builds(
    ir::UnaryExpression,
    operator=
        safe_text
)
ir::BinaryExpression_strategy = st.builds(
    ir::BinaryExpression,
    operator=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
ir::PortRead_strategy = st.builds(
    ir::PortRead,
)
ir::PortWrite_strategy = st.builds(
    ir::PortWrite,
)
ir::Guard_strategy = st.builds(
    ir::Guard,
)
ir::ActorInstance_strategy = st.builds(
    ir::ActorInstance,
)
ir::Schedule_strategy = st.builds(
    ir::Schedule,
    PriorityGraph=
        safe_text
)
AbstractActor_strategy = st.builds(
    AbstractActor,
)
ir::Actor_strategy = st.builds(
    ir::Actor,
)
ir::Network_strategy = st.builds(
    ir::Network,
)
ir::ExternalActor_strategy = st.builds(
    ir::ExternalActor,
)
Scope_strategy = st.builds(
    Scope,
)
ir::Action_strategy = st.builds(
    ir::Action,
    tag=
        safe_text
)
ir::AbstractActor_strategy = st.builds(
    ir::AbstractActor,
)
ir::Block_strategy = st.builds(
    ir::Block,
)
ir::ProcExpression_strategy = st.builds(
    ir::ProcExpression,
)
ir::LambdaExpression_strategy = st.builds(
    ir::LambdaExpression,
)
ir::Generator_strategy = st.builds(
    ir::Generator,
)
ir::Namespace_strategy = st.builds(
    ir::Namespace,
    name=
        safe_text
)
ir::TaggedExpression_strategy = st.builds(
    ir::TaggedExpression,
    tag=
        safe_text
)
ir::Type_strategy = st.builds(
    ir::Type,
)
Declaration_strategy = st.builds(
    Declaration,
)
ir::TypeDeclarationImport_strategy = st.builds(
    ir::TypeDeclarationImport,
    namespace=
        safe_text
)
ir::VariableExternal_strategy = st.builds(
    ir::VariableExternal,
)
ir::TypeConstructor_strategy = st.builds(
    ir::TypeConstructor,
)
ir::ForwardDeclaration_strategy = st.builds(
    ir::ForwardDeclaration,
)
ir::TypeDeclaration_strategy = st.builds(
    ir::TypeDeclaration,
)
ir::VariableImport_strategy = st.builds(
    ir::VariableImport,
    namespace=
        safe_text
)
ir::Annotation_strategy = st.builds(
    ir::Annotation,
    name=
        safe_text
)
ir::Node_strategy = st.builds(
    ir::Node,
    id=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
ir::PortInstance_strategy = st.builds(
    ir::PortInstance,
    name=
        safe_text
)
ir::Expression_strategy = st.builds(
    ir::Expression,
)
ir::PortAccess_strategy = st.builds(
    ir::PortAccess,
)
ir::TypeRecord_strategy = st.builds(
    ir::TypeRecord,
)
ir::VariableReference_strategy = st.builds(
    ir::VariableReference,
)
ir::Connection_strategy = st.builds(
    ir::Connection,
)
ir::Member_strategy = st.builds(
    ir::Member,
    name=
        safe_text
)
ir::Statement_strategy = st.builds(
    ir::Statement,
)
ir::Declaration_strategy = st.builds(
    ir::Declaration,
    name=
        safe_text
)
ir::Scope_strategy = st.builds(
    ir::Scope,
)
ir::Variable_strategy = st.builds(
    ir::Variable,
    constant=
        st.booleans(),
    parameter=
        st.booleans()
)
ir::Port_strategy = st.builds(
    ir::Port,
    name=
        safe_text
)
ir::TypeActor_strategy = st.builds(
    ir::TypeActor,
    namespace=
        safe_text,
    name=
        safe_text
)

@given(instance=ir::AnnotationArgument_strategy)
@settings(max_examples=50)
def test_ir::annotationargument_instantiation(instance):
    assert isinstance(instance, ir::AnnotationArgument)

@given(instance=ir::AnnotationArgument_strategy)
def test_ir::annotationargument_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ir::AnnotationArgument_strategy)
def test_ir::annotationargument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::AnnotationArgument_strategy)
def test_ir::annotationargument_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ir::AnnotationArgument_strategy)
def test_ir::annotationargument_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ir::State_strategy)
@settings(max_examples=50)
def test_ir::state_instantiation(instance):
    assert isinstance(instance, ir::State)

@given(instance=ir::State_strategy)
def test_ir::state_PriorityGraph_type(instance):
    assert isinstance(instance.PriorityGraph, str)


@given(instance=ir::State_strategy)
def test_ir::state_PriorityGraph_setter(instance):
    original = instance.PriorityGraph
    instance.PriorityGraph = original
    assert instance.PriorityGraph == original

@given(instance=ir::State_strategy)
def test_ir::state_Action2TargetMap_type(instance):
    assert isinstance(instance.Action2TargetMap, str)


@given(instance=ir::State_strategy)
def test_ir::state_Action2TargetMap_setter(instance):
    original = instance.Action2TargetMap
    instance.Action2TargetMap = original
    assert instance.Action2TargetMap == original

@given(instance=ir::State_strategy)
def test_ir::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::State_strategy)
def test_ir::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ir::TypeFloat_strategy)
@settings(max_examples=50)
def test_ir::typefloat_instantiation(instance):
    assert isinstance(instance, ir::TypeFloat)

@given(instance=ir::TypeInt_strategy)
@settings(max_examples=50)
def test_ir::typeint_instantiation(instance):
    assert isinstance(instance, ir::TypeInt)

@given(instance=ir::TypeLambda_strategy)
@settings(max_examples=50)
def test_ir::typelambda_instantiation(instance):
    assert isinstance(instance, ir::TypeLambda)

@given(instance=ir::TypeList_strategy)
@settings(max_examples=50)
def test_ir::typelist_instantiation(instance):
    assert isinstance(instance, ir::TypeList)

@given(instance=ir::TypeExternal_strategy)
@settings(max_examples=50)
def test_ir::typeexternal_instantiation(instance):
    assert isinstance(instance, ir::TypeExternal)

@given(instance=ir::TypeExternal_strategy)
def test_ir::typeexternal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::TypeExternal_strategy)
def test_ir::typeexternal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::TypeExternal_strategy)
def test_ir::typeexternal_scopeName_type(instance):
    assert isinstance(instance.scopeName, str)


@given(instance=ir::TypeExternal_strategy)
def test_ir::typeexternal_scopeName_setter(instance):
    original = instance.scopeName
    instance.scopeName = original
    assert instance.scopeName == original

@given(instance=ir::TypeProc_strategy)
@settings(max_examples=50)
def test_ir::typeproc_instantiation(instance):
    assert isinstance(instance, ir::TypeProc)

@given(instance=ir::TypeUint_strategy)
@settings(max_examples=50)
def test_ir::typeuint_instantiation(instance):
    assert isinstance(instance, ir::TypeUint)

@given(instance=ir::TypeString_strategy)
@settings(max_examples=50)
def test_ir::typestring_instantiation(instance):
    assert isinstance(instance, ir::TypeString)

@given(instance=ir::TypeBool_strategy)
@settings(max_examples=50)
def test_ir::typebool_instantiation(instance):
    assert isinstance(instance, ir::TypeBool)

@given(instance=LambdaExpression_strategy)
@settings(max_examples=50)
def test_lambdaexpression_instantiation(instance):
    assert isinstance(instance, LambdaExpression)

@given(instance=ir::TypeUser_strategy)
@settings(max_examples=50)
def test_ir::typeuser_instantiation(instance):
    assert isinstance(instance, ir::TypeUser)

@given(instance=ir::TypeUndef_strategy)
@settings(max_examples=50)
def test_ir::typeundef_instantiation(instance):
    assert isinstance(instance, ir::TypeUndef)

@given(instance=PortAccess_strategy)
@settings(max_examples=50)
def test_portaccess_instantiation(instance):
    assert isinstance(instance, PortAccess)

@given(instance=ir::PortPeek_strategy)
@settings(max_examples=50)
def test_ir::portpeek_instantiation(instance):
    assert isinstance(instance, ir::PortPeek)

@given(instance=ir::PortPeek_strategy)
def test_ir::portpeek_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=ir::PortPeek_strategy)
def test_ir::portpeek_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ir::WhileLoop_strategy)
@settings(max_examples=50)
def test_ir::whileloop_instantiation(instance):
    assert isinstance(instance, ir::WhileLoop)

@given(instance=ir::IfStatement_strategy)
@settings(max_examples=50)
def test_ir::ifstatement_instantiation(instance):
    assert isinstance(instance, ir::IfStatement)

@given(instance=ir::ReturnValue_strategy)
@settings(max_examples=50)
def test_ir::returnvalue_instantiation(instance):
    assert isinstance(instance, ir::ReturnValue)

@given(instance=ir::ProcCall_strategy)
@settings(max_examples=50)
def test_ir::proccall_instantiation(instance):
    assert isinstance(instance, ir::ProcCall)

@given(instance=ir::ForEach_strategy)
@settings(max_examples=50)
def test_ir::foreach_instantiation(instance):
    assert isinstance(instance, ir::ForEach)

@given(instance=ir::Assign_strategy)
@settings(max_examples=50)
def test_ir::assign_instantiation(instance):
    assert isinstance(instance, ir::Assign)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=ir::FromSource_strategy)
@settings(max_examples=50)
def test_ir::fromsource_instantiation(instance):
    assert isinstance(instance, ir::FromSource)

@given(instance=ir::ToSink_strategy)
@settings(max_examples=50)
def test_ir::tosink_instantiation(instance):
    assert isinstance(instance, ir::ToSink)

@given(instance=ir::Point2PointConnection_strategy)
@settings(max_examples=50)
def test_ir::point2pointconnection_instantiation(instance):
    assert isinstance(instance, ir::Point2PointConnection)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=ir::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_ir::booleanliteral_instantiation(instance):
    assert isinstance(instance, ir::BooleanLiteral)

@given(instance=ir::BooleanLiteral_strategy)
def test_ir::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=ir::BooleanLiteral_strategy)
def test_ir::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::StringLiteral_strategy)
@settings(max_examples=50)
def test_ir::stringliteral_instantiation(instance):
    assert isinstance(instance, ir::StringLiteral)

@given(instance=ir::StringLiteral_strategy)
def test_ir::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ir::StringLiteral_strategy)
def test_ir::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::FloatLiteral_strategy)
@settings(max_examples=50)
def test_ir::floatliteral_instantiation(instance):
    assert isinstance(instance, ir::FloatLiteral)

@given(instance=ir::FloatLiteral_strategy)
def test_ir::floatliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=ir::FloatLiteral_strategy)
def test_ir::floatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_ir::integerliteral_instantiation(instance):
    assert isinstance(instance, ir::IntegerLiteral)

@given(instance=ir::IntegerLiteral_strategy)
def test_ir::integerliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ir::IntegerLiteral_strategy)
def test_ir::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ir::IfExpression_strategy)
@settings(max_examples=50)
def test_ir::ifexpression_instantiation(instance):
    assert isinstance(instance, ir::IfExpression)

@given(instance=ir::VariableExpression_strategy)
@settings(max_examples=50)
def test_ir::variableexpression_instantiation(instance):
    assert isinstance(instance, ir::VariableExpression)

@given(instance=ir::ListExpression_strategy)
@settings(max_examples=50)
def test_ir::listexpression_instantiation(instance):
    assert isinstance(instance, ir::ListExpression)

@given(instance=ir::LiteralExpression_strategy)
@settings(max_examples=50)
def test_ir::literalexpression_instantiation(instance):
    assert isinstance(instance, ir::LiteralExpression)

@given(instance=ExpressionCall_strategy)
@settings(max_examples=50)
def test_expressioncall_instantiation(instance):
    assert isinstance(instance, ExpressionCall)

@given(instance=ir::TypeConstructorCall_strategy)
@settings(max_examples=50)
def test_ir::typeconstructorcall_instantiation(instance):
    assert isinstance(instance, ir::TypeConstructorCall)

@given(instance=ir::TypeConstructorCall_strategy)
def test_ir::typeconstructorcall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::TypeConstructorCall_strategy)
def test_ir::typeconstructorcall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::FunctionCall_strategy)
@settings(max_examples=50)
def test_ir::functioncall_instantiation(instance):
    assert isinstance(instance, ir::FunctionCall)

@given(instance=ir::ExpressionCall_strategy)
@settings(max_examples=50)
def test_ir::expressioncall_instantiation(instance):
    assert isinstance(instance, ir::ExpressionCall)

@given(instance=ir::UnaryExpression_strategy)
@settings(max_examples=50)
def test_ir::unaryexpression_instantiation(instance):
    assert isinstance(instance, ir::UnaryExpression)

@given(instance=ir::UnaryExpression_strategy)
def test_ir::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ir::UnaryExpression_strategy)
def test_ir::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ir::BinaryExpression_strategy)
@settings(max_examples=50)
def test_ir::binaryexpression_instantiation(instance):
    assert isinstance(instance, ir::BinaryExpression)

@given(instance=ir::BinaryExpression_strategy)
def test_ir::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ir::BinaryExpression_strategy)
def test_ir::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ir::PortRead_strategy)
@settings(max_examples=50)
def test_ir::portread_instantiation(instance):
    assert isinstance(instance, ir::PortRead)

@given(instance=ir::PortWrite_strategy)
@settings(max_examples=50)
def test_ir::portwrite_instantiation(instance):
    assert isinstance(instance, ir::PortWrite)

@given(instance=ir::Guard_strategy)
@settings(max_examples=50)
def test_ir::guard_instantiation(instance):
    assert isinstance(instance, ir::Guard)

@given(instance=ir::ActorInstance_strategy)
@settings(max_examples=50)
def test_ir::actorinstance_instantiation(instance):
    assert isinstance(instance, ir::ActorInstance)

@given(instance=ir::Schedule_strategy)
@settings(max_examples=50)
def test_ir::schedule_instantiation(instance):
    assert isinstance(instance, ir::Schedule)

@given(instance=ir::Schedule_strategy)
def test_ir::schedule_PriorityGraph_type(instance):
    assert isinstance(instance.PriorityGraph, str)


@given(instance=ir::Schedule_strategy)
def test_ir::schedule_PriorityGraph_setter(instance):
    original = instance.PriorityGraph
    instance.PriorityGraph = original
    assert instance.PriorityGraph == original

@given(instance=AbstractActor_strategy)
@settings(max_examples=50)
def test_abstractactor_instantiation(instance):
    assert isinstance(instance, AbstractActor)

@given(instance=ir::Actor_strategy)
@settings(max_examples=50)
def test_ir::actor_instantiation(instance):
    assert isinstance(instance, ir::Actor)

@given(instance=ir::Network_strategy)
@settings(max_examples=50)
def test_ir::network_instantiation(instance):
    assert isinstance(instance, ir::Network)

@given(instance=ir::ExternalActor_strategy)
@settings(max_examples=50)
def test_ir::externalactor_instantiation(instance):
    assert isinstance(instance, ir::ExternalActor)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=ir::Action_strategy)
@settings(max_examples=50)
def test_ir::action_instantiation(instance):
    assert isinstance(instance, ir::Action)

@given(instance=ir::Action_strategy)
def test_ir::action_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=ir::Action_strategy)
def test_ir::action_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=ir::AbstractActor_strategy)
@settings(max_examples=50)
def test_ir::abstractactor_instantiation(instance):
    assert isinstance(instance, ir::AbstractActor)

@given(instance=ir::Block_strategy)
@settings(max_examples=50)
def test_ir::block_instantiation(instance):
    assert isinstance(instance, ir::Block)

@given(instance=ir::ProcExpression_strategy)
@settings(max_examples=50)
def test_ir::procexpression_instantiation(instance):
    assert isinstance(instance, ir::ProcExpression)

@given(instance=ir::LambdaExpression_strategy)
@settings(max_examples=50)
def test_ir::lambdaexpression_instantiation(instance):
    assert isinstance(instance, ir::LambdaExpression)

@given(instance=ir::Generator_strategy)
@settings(max_examples=50)
def test_ir::generator_instantiation(instance):
    assert isinstance(instance, ir::Generator)

@given(instance=ir::Namespace_strategy)
@settings(max_examples=50)
def test_ir::namespace_instantiation(instance):
    assert isinstance(instance, ir::Namespace)

@given(instance=ir::Namespace_strategy)
def test_ir::namespace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Namespace_strategy)
def test_ir::namespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::TaggedExpression_strategy)
@settings(max_examples=50)
def test_ir::taggedexpression_instantiation(instance):
    assert isinstance(instance, ir::TaggedExpression)

@given(instance=ir::TaggedExpression_strategy)
def test_ir::taggedexpression_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=ir::TaggedExpression_strategy)
def test_ir::taggedexpression_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=ir::Type_strategy)
@settings(max_examples=50)
def test_ir::type_instantiation(instance):
    assert isinstance(instance, ir::Type)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=ir::TypeDeclarationImport_strategy)
@settings(max_examples=50)
def test_ir::typedeclarationimport_instantiation(instance):
    assert isinstance(instance, ir::TypeDeclarationImport)

@given(instance=ir::TypeDeclarationImport_strategy)
def test_ir::typedeclarationimport_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=ir::TypeDeclarationImport_strategy)
def test_ir::typedeclarationimport_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=ir::VariableExternal_strategy)
@settings(max_examples=50)
def test_ir::variableexternal_instantiation(instance):
    assert isinstance(instance, ir::VariableExternal)

@given(instance=ir::TypeConstructor_strategy)
@settings(max_examples=50)
def test_ir::typeconstructor_instantiation(instance):
    assert isinstance(instance, ir::TypeConstructor)

@given(instance=ir::ForwardDeclaration_strategy)
@settings(max_examples=50)
def test_ir::forwarddeclaration_instantiation(instance):
    assert isinstance(instance, ir::ForwardDeclaration)

@given(instance=ir::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_ir::typedeclaration_instantiation(instance):
    assert isinstance(instance, ir::TypeDeclaration)

@given(instance=ir::VariableImport_strategy)
@settings(max_examples=50)
def test_ir::variableimport_instantiation(instance):
    assert isinstance(instance, ir::VariableImport)

@given(instance=ir::VariableImport_strategy)
def test_ir::variableimport_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=ir::VariableImport_strategy)
def test_ir::variableimport_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=ir::Annotation_strategy)
@settings(max_examples=50)
def test_ir::annotation_instantiation(instance):
    assert isinstance(instance, ir::Annotation)

@given(instance=ir::Annotation_strategy)
def test_ir::annotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Annotation_strategy)
def test_ir::annotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Node_strategy)
@settings(max_examples=50)
def test_ir::node_instantiation(instance):
    assert isinstance(instance, ir::Node)

@given(instance=ir::Node_strategy)
def test_ir::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ir::Node_strategy)
def test_ir::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ir::PortInstance_strategy)
@settings(max_examples=50)
def test_ir::portinstance_instantiation(instance):
    assert isinstance(instance, ir::PortInstance)

@given(instance=ir::PortInstance_strategy)
def test_ir::portinstance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::PortInstance_strategy)
def test_ir::portinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Expression_strategy)
@settings(max_examples=50)
def test_ir::expression_instantiation(instance):
    assert isinstance(instance, ir::Expression)

@given(instance=ir::PortAccess_strategy)
@settings(max_examples=50)
def test_ir::portaccess_instantiation(instance):
    assert isinstance(instance, ir::PortAccess)

@given(instance=ir::TypeRecord_strategy)
@settings(max_examples=50)
def test_ir::typerecord_instantiation(instance):
    assert isinstance(instance, ir::TypeRecord)

@given(instance=ir::VariableReference_strategy)
@settings(max_examples=50)
def test_ir::variablereference_instantiation(instance):
    assert isinstance(instance, ir::VariableReference)

@given(instance=ir::Connection_strategy)
@settings(max_examples=50)
def test_ir::connection_instantiation(instance):
    assert isinstance(instance, ir::Connection)

@given(instance=ir::Member_strategy)
@settings(max_examples=50)
def test_ir::member_instantiation(instance):
    assert isinstance(instance, ir::Member)

@given(instance=ir::Member_strategy)
def test_ir::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Member_strategy)
def test_ir::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Statement_strategy)
@settings(max_examples=50)
def test_ir::statement_instantiation(instance):
    assert isinstance(instance, ir::Statement)

@given(instance=ir::Declaration_strategy)
@settings(max_examples=50)
def test_ir::declaration_instantiation(instance):
    assert isinstance(instance, ir::Declaration)

@given(instance=ir::Declaration_strategy)
def test_ir::declaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Declaration_strategy)
def test_ir::declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Scope_strategy)
@settings(max_examples=50)
def test_ir::scope_instantiation(instance):
    assert isinstance(instance, ir::Scope)

@given(instance=ir::Variable_strategy)
@settings(max_examples=50)
def test_ir::variable_instantiation(instance):
    assert isinstance(instance, ir::Variable)

@given(instance=ir::Variable_strategy)
def test_ir::variable_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=ir::Variable_strategy)
def test_ir::variable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=ir::Variable_strategy)
def test_ir::variable_parameter_type(instance):
    assert isinstance(instance.parameter, bool)


@given(instance=ir::Variable_strategy)
def test_ir::variable_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=ir::Port_strategy)
@settings(max_examples=50)
def test_ir::port_instantiation(instance):
    assert isinstance(instance, ir::Port)

@given(instance=ir::Port_strategy)
def test_ir::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Port_strategy)
def test_ir::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::TypeActor_strategy)
@settings(max_examples=50)
def test_ir::typeactor_instantiation(instance):
    assert isinstance(instance, ir::TypeActor)

@given(instance=ir::TypeActor_strategy)
def test_ir::typeactor_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=ir::TypeActor_strategy)
def test_ir::typeactor_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=ir::TypeActor_strategy)
def test_ir::typeactor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::TypeActor_strategy)
def test_ir::typeactor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
