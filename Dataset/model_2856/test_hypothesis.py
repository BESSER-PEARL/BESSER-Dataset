import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ir_AnnotationArgument,
    ir_State,
    Type,
    ir_TypeString,
    ir_TypeExternal,
    ir_TypeInt,
    ir_TypeLambda,
    ir_TypeProc,
    ir_TypeUint,
    ir_TypeList,
    ir_TypeFloat,
    ir_TypeBool,
    LambdaExpression,
    ir_TypeUser,
    PortAccess,
    ir_PortPeek,
    Block,
    Statement,
    ir_ForEach,
    ir_ProcCall,
    ir_IfStatement,
    ir_WhileLoop,
    ir_ReturnValue,
    ir_Assign,
    Connection,
    ir_ToSink,
    ir_FromSource,
    ir_Point2PointConnection,
    ir_TypeUndef,
    LiteralExpression,
    ir_StringLiteral,
    ir_BooleanLiteral,
    ir_FloatLiteral,
    ir_IntegerLiteral,
    Expression,
    ir_ListExpression,
    ir_VariableExpression,
    ir_IfExpression,
    ir_LiteralExpression,
    ExpressionCall,
    ir_TypeConstructorCall,
    ir_FunctionCall,
    ir_ExpressionCall,
    ir_UnaryExpression,
    ir_BinaryExpression,
    Variable,
    ir_PortRead,
    ir_PortWrite,
    ir_Guard,
    ir_ActorInstance,
    ir_Schedule,
    AbstractActor,
    ir_Network,
    ir_Actor,
    ir_ExternalActor,
    Scope,
    ir_Generator,
    ir_ProcExpression,
    ir_Action,
    ir_LambdaExpression,
    ir_Block,
    ir_Namespace,
    ir_TaggedExpression,
    ir_Type,
    Declaration,
    ir_TypeDeclarationImport,
    ir_ForwardDeclaration,
    ir_TypeConstructor,
    ir_VariableExternal,
    ir_TypeDeclaration,
    ir_VariableImport,
    ir_Annotation,
    ir_Node,
    Node,
    ir_Declaration,
    ir_Connection,
    ir_Expression,
    ir_Statement,
    ir_TypeRecord,
    ir_PortAccess,
    ir_PortInstance,
    ir_VariableReference,
    ir_Member,
    ir_Scope,
    ir_Variable,
    ir_Port,
    ir_TypeActor,
    ir_AbstractActor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ir_annotationargument_is_not_abstract():
    assert not inspect.isabstract(ir_AnnotationArgument)


def test_ir_annotationargument_constructor_exists():
    assert callable(ir_AnnotationArgument.__init__)


def test_ir_annotationargument_constructor_args():
    sig = inspect.signature(ir_AnnotationArgument.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"

def test_ir_annotationargument_has_value():
    assert hasattr(ir_AnnotationArgument, "value")
    descriptor = None
    for klass in ir_AnnotationArgument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ir_annotationargument_has_id():
    assert hasattr(ir_AnnotationArgument, "id")
    descriptor = None
    for klass in ir_AnnotationArgument.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ir_state_is_not_abstract():
    assert not inspect.isabstract(ir_State)


def test_ir_state_constructor_exists():
    assert callable(ir_State.__init__)


def test_ir_state_constructor_args():
    sig = inspect.signature(ir_State.__init__)
    params = list(sig.parameters.keys())
    assert "Action2TargetMap" in params, "Missing parameter 'Action2TargetMap'"
    assert "name" in params, "Missing parameter 'name'"
    assert "PriorityGraph" in params, "Missing parameter 'PriorityGraph'"

def test_ir_state_has_Action2TargetMap():
    assert hasattr(ir_State, "Action2TargetMap")
    descriptor = None
    for klass in ir_State.__mro__:
        if "Action2TargetMap" in klass.__dict__:
            descriptor = klass.__dict__["Action2TargetMap"]
            break
    assert isinstance(descriptor, property)

def test_ir_state_has_name():
    assert hasattr(ir_State, "name")
    descriptor = None
    for klass in ir_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir_state_has_PriorityGraph():
    assert hasattr(ir_State, "PriorityGraph")
    descriptor = None
    for klass in ir_State.__mro__:
        if "PriorityGraph" in klass.__dict__:
            descriptor = klass.__dict__["PriorityGraph"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ir_typestring_is_not_abstract():
    assert not inspect.isabstract(ir_TypeString)


def test_ir_typestring_constructor_exists():
    assert callable(ir_TypeString.__init__)


def test_ir_typestring_constructor_args():
    sig = inspect.signature(ir_TypeString.__init__)
    params = list(sig.parameters.keys())



def test_ir_typeexternal_is_not_abstract():
    assert not inspect.isabstract(ir_TypeExternal)


def test_ir_typeexternal_constructor_exists():
    assert callable(ir_TypeExternal.__init__)


def test_ir_typeexternal_constructor_args():
    sig = inspect.signature(ir_TypeExternal.__init__)
    params = list(sig.parameters.keys())
    assert "scopeName" in params, "Missing parameter 'scopeName'"
    assert "name" in params, "Missing parameter 'name'"

def test_ir_typeexternal_has_scopeName():
    assert hasattr(ir_TypeExternal, "scopeName")
    descriptor = None
    for klass in ir_TypeExternal.__mro__:
        if "scopeName" in klass.__dict__:
            descriptor = klass.__dict__["scopeName"]
            break
    assert isinstance(descriptor, property)

def test_ir_typeexternal_has_name():
    assert hasattr(ir_TypeExternal, "name")
    descriptor = None
    for klass in ir_TypeExternal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_typeint_is_not_abstract():
    assert not inspect.isabstract(ir_TypeInt)


def test_ir_typeint_constructor_exists():
    assert callable(ir_TypeInt.__init__)


def test_ir_typeint_constructor_args():
    sig = inspect.signature(ir_TypeInt.__init__)
    params = list(sig.parameters.keys())



def test_ir_typelambda_is_not_abstract():
    assert not inspect.isabstract(ir_TypeLambda)


def test_ir_typelambda_constructor_exists():
    assert callable(ir_TypeLambda.__init__)


def test_ir_typelambda_constructor_args():
    sig = inspect.signature(ir_TypeLambda.__init__)
    params = list(sig.parameters.keys())



def test_ir_typeproc_is_not_abstract():
    assert not inspect.isabstract(ir_TypeProc)


def test_ir_typeproc_constructor_exists():
    assert callable(ir_TypeProc.__init__)


def test_ir_typeproc_constructor_args():
    sig = inspect.signature(ir_TypeProc.__init__)
    params = list(sig.parameters.keys())



def test_ir_typeuint_is_not_abstract():
    assert not inspect.isabstract(ir_TypeUint)


def test_ir_typeuint_constructor_exists():
    assert callable(ir_TypeUint.__init__)


def test_ir_typeuint_constructor_args():
    sig = inspect.signature(ir_TypeUint.__init__)
    params = list(sig.parameters.keys())



def test_ir_typelist_is_not_abstract():
    assert not inspect.isabstract(ir_TypeList)


def test_ir_typelist_constructor_exists():
    assert callable(ir_TypeList.__init__)


def test_ir_typelist_constructor_args():
    sig = inspect.signature(ir_TypeList.__init__)
    params = list(sig.parameters.keys())



def test_ir_typefloat_is_not_abstract():
    assert not inspect.isabstract(ir_TypeFloat)


def test_ir_typefloat_constructor_exists():
    assert callable(ir_TypeFloat.__init__)


def test_ir_typefloat_constructor_args():
    sig = inspect.signature(ir_TypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_ir_typebool_is_not_abstract():
    assert not inspect.isabstract(ir_TypeBool)


def test_ir_typebool_constructor_exists():
    assert callable(ir_TypeBool.__init__)


def test_ir_typebool_constructor_args():
    sig = inspect.signature(ir_TypeBool.__init__)
    params = list(sig.parameters.keys())



def test_lambdaexpression_is_not_abstract():
    assert not inspect.isabstract(LambdaExpression)


def test_lambdaexpression_constructor_exists():
    assert callable(LambdaExpression.__init__)


def test_lambdaexpression_constructor_args():
    sig = inspect.signature(LambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir_typeuser_is_not_abstract():
    assert not inspect.isabstract(ir_TypeUser)


def test_ir_typeuser_constructor_exists():
    assert callable(ir_TypeUser.__init__)


def test_ir_typeuser_constructor_args():
    sig = inspect.signature(ir_TypeUser.__init__)
    params = list(sig.parameters.keys())



def test_portaccess_is_not_abstract():
    assert not inspect.isabstract(PortAccess)


def test_portaccess_constructor_exists():
    assert callable(PortAccess.__init__)


def test_portaccess_constructor_args():
    sig = inspect.signature(PortAccess.__init__)
    params = list(sig.parameters.keys())



def test_ir_portpeek_is_not_abstract():
    assert not inspect.isabstract(ir_PortPeek)


def test_ir_portpeek_constructor_exists():
    assert callable(ir_PortPeek.__init__)


def test_ir_portpeek_constructor_args():
    sig = inspect.signature(ir_PortPeek.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_ir_portpeek_has_position():
    assert hasattr(ir_PortPeek, "position")
    descriptor = None
    for klass in ir_PortPeek.__mro__:
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



def test_ir_foreach_is_not_abstract():
    assert not inspect.isabstract(ir_ForEach)


def test_ir_foreach_constructor_exists():
    assert callable(ir_ForEach.__init__)


def test_ir_foreach_constructor_args():
    sig = inspect.signature(ir_ForEach.__init__)
    params = list(sig.parameters.keys())



def test_ir_proccall_is_not_abstract():
    assert not inspect.isabstract(ir_ProcCall)


def test_ir_proccall_constructor_exists():
    assert callable(ir_ProcCall.__init__)


def test_ir_proccall_constructor_args():
    sig = inspect.signature(ir_ProcCall.__init__)
    params = list(sig.parameters.keys())



def test_ir_ifstatement_is_not_abstract():
    assert not inspect.isabstract(ir_IfStatement)


def test_ir_ifstatement_constructor_exists():
    assert callable(ir_IfStatement.__init__)


def test_ir_ifstatement_constructor_args():
    sig = inspect.signature(ir_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_ir_whileloop_is_not_abstract():
    assert not inspect.isabstract(ir_WhileLoop)


def test_ir_whileloop_constructor_exists():
    assert callable(ir_WhileLoop.__init__)


def test_ir_whileloop_constructor_args():
    sig = inspect.signature(ir_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_ir_returnvalue_is_not_abstract():
    assert not inspect.isabstract(ir_ReturnValue)


def test_ir_returnvalue_constructor_exists():
    assert callable(ir_ReturnValue.__init__)


def test_ir_returnvalue_constructor_args():
    sig = inspect.signature(ir_ReturnValue.__init__)
    params = list(sig.parameters.keys())



def test_ir_assign_is_not_abstract():
    assert not inspect.isabstract(ir_Assign)


def test_ir_assign_constructor_exists():
    assert callable(ir_Assign.__init__)


def test_ir_assign_constructor_args():
    sig = inspect.signature(ir_Assign.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_ir_tosink_is_not_abstract():
    assert not inspect.isabstract(ir_ToSink)


def test_ir_tosink_constructor_exists():
    assert callable(ir_ToSink.__init__)


def test_ir_tosink_constructor_args():
    sig = inspect.signature(ir_ToSink.__init__)
    params = list(sig.parameters.keys())



def test_ir_fromsource_is_not_abstract():
    assert not inspect.isabstract(ir_FromSource)


def test_ir_fromsource_constructor_exists():
    assert callable(ir_FromSource.__init__)


def test_ir_fromsource_constructor_args():
    sig = inspect.signature(ir_FromSource.__init__)
    params = list(sig.parameters.keys())



def test_ir_point2pointconnection_is_not_abstract():
    assert not inspect.isabstract(ir_Point2PointConnection)


def test_ir_point2pointconnection_constructor_exists():
    assert callable(ir_Point2PointConnection.__init__)


def test_ir_point2pointconnection_constructor_args():
    sig = inspect.signature(ir_Point2PointConnection.__init__)
    params = list(sig.parameters.keys())



def test_ir_typeundef_is_not_abstract():
    assert not inspect.isabstract(ir_TypeUndef)


def test_ir_typeundef_constructor_exists():
    assert callable(ir_TypeUndef.__init__)


def test_ir_typeundef_constructor_args():
    sig = inspect.signature(ir_TypeUndef.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir_stringliteral_is_not_abstract():
    assert not inspect.isabstract(ir_StringLiteral)


def test_ir_stringliteral_constructor_exists():
    assert callable(ir_StringLiteral.__init__)


def test_ir_stringliteral_constructor_args():
    sig = inspect.signature(ir_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_stringliteral_has_value():
    assert hasattr(ir_StringLiteral, "value")
    descriptor = None
    for klass in ir_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(ir_BooleanLiteral)


def test_ir_booleanliteral_constructor_exists():
    assert callable(ir_BooleanLiteral.__init__)


def test_ir_booleanliteral_constructor_args():
    sig = inspect.signature(ir_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_booleanliteral_has_value():
    assert hasattr(ir_BooleanLiteral, "value")
    descriptor = None
    for klass in ir_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_floatliteral_is_not_abstract():
    assert not inspect.isabstract(ir_FloatLiteral)


def test_ir_floatliteral_constructor_exists():
    assert callable(ir_FloatLiteral.__init__)


def test_ir_floatliteral_constructor_args():
    sig = inspect.signature(ir_FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_floatliteral_has_value():
    assert hasattr(ir_FloatLiteral, "value")
    descriptor = None
    for klass in ir_FloatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_integerliteral_is_not_abstract():
    assert not inspect.isabstract(ir_IntegerLiteral)


def test_ir_integerliteral_constructor_exists():
    assert callable(ir_IntegerLiteral.__init__)


def test_ir_integerliteral_constructor_args():
    sig = inspect.signature(ir_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_integerliteral_has_value():
    assert hasattr(ir_IntegerLiteral, "value")
    descriptor = None
    for klass in ir_IntegerLiteral.__mro__:
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



def test_ir_listexpression_is_not_abstract():
    assert not inspect.isabstract(ir_ListExpression)


def test_ir_listexpression_constructor_exists():
    assert callable(ir_ListExpression.__init__)


def test_ir_listexpression_constructor_args():
    sig = inspect.signature(ir_ListExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir_variableexpression_is_not_abstract():
    assert not inspect.isabstract(ir_VariableExpression)


def test_ir_variableexpression_constructor_exists():
    assert callable(ir_VariableExpression.__init__)


def test_ir_variableexpression_constructor_args():
    sig = inspect.signature(ir_VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir_ifexpression_is_not_abstract():
    assert not inspect.isabstract(ir_IfExpression)


def test_ir_ifexpression_constructor_exists():
    assert callable(ir_IfExpression.__init__)


def test_ir_ifexpression_constructor_args():
    sig = inspect.signature(ir_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir_literalexpression_is_not_abstract():
    assert not inspect.isabstract(ir_LiteralExpression)


def test_ir_literalexpression_constructor_exists():
    assert callable(ir_LiteralExpression.__init__)


def test_ir_literalexpression_constructor_args():
    sig = inspect.signature(ir_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressioncall_is_not_abstract():
    assert not inspect.isabstract(ExpressionCall)


def test_expressioncall_constructor_exists():
    assert callable(ExpressionCall.__init__)


def test_expressioncall_constructor_args():
    sig = inspect.signature(ExpressionCall.__init__)
    params = list(sig.parameters.keys())



def test_ir_typeconstructorcall_is_not_abstract():
    assert not inspect.isabstract(ir_TypeConstructorCall)


def test_ir_typeconstructorcall_constructor_exists():
    assert callable(ir_TypeConstructorCall.__init__)


def test_ir_typeconstructorcall_constructor_args():
    sig = inspect.signature(ir_TypeConstructorCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_typeconstructorcall_has_name():
    assert hasattr(ir_TypeConstructorCall, "name")
    descriptor = None
    for klass in ir_TypeConstructorCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_functioncall_is_not_abstract():
    assert not inspect.isabstract(ir_FunctionCall)


def test_ir_functioncall_constructor_exists():
    assert callable(ir_FunctionCall.__init__)


def test_ir_functioncall_constructor_args():
    sig = inspect.signature(ir_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_ir_expressioncall_is_not_abstract():
    assert not inspect.isabstract(ir_ExpressionCall)


def test_ir_expressioncall_constructor_exists():
    assert callable(ir_ExpressionCall.__init__)


def test_ir_expressioncall_constructor_args():
    sig = inspect.signature(ir_ExpressionCall.__init__)
    params = list(sig.parameters.keys())



def test_ir_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(ir_UnaryExpression)


def test_ir_unaryexpression_constructor_exists():
    assert callable(ir_UnaryExpression.__init__)


def test_ir_unaryexpression_constructor_args():
    sig = inspect.signature(ir_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir_unaryexpression_has_operator():
    assert hasattr(ir_UnaryExpression, "operator")
    descriptor = None
    for klass in ir_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ir_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(ir_BinaryExpression)


def test_ir_binaryexpression_constructor_exists():
    assert callable(ir_BinaryExpression.__init__)


def test_ir_binaryexpression_constructor_args():
    sig = inspect.signature(ir_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir_binaryexpression_has_operator():
    assert hasattr(ir_BinaryExpression, "operator")
    descriptor = None
    for klass in ir_BinaryExpression.__mro__:
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



def test_ir_portread_is_not_abstract():
    assert not inspect.isabstract(ir_PortRead)


def test_ir_portread_constructor_exists():
    assert callable(ir_PortRead.__init__)


def test_ir_portread_constructor_args():
    sig = inspect.signature(ir_PortRead.__init__)
    params = list(sig.parameters.keys())



def test_ir_portwrite_is_not_abstract():
    assert not inspect.isabstract(ir_PortWrite)


def test_ir_portwrite_constructor_exists():
    assert callable(ir_PortWrite.__init__)


def test_ir_portwrite_constructor_args():
    sig = inspect.signature(ir_PortWrite.__init__)
    params = list(sig.parameters.keys())



def test_ir_guard_is_not_abstract():
    assert not inspect.isabstract(ir_Guard)


def test_ir_guard_constructor_exists():
    assert callable(ir_Guard.__init__)


def test_ir_guard_constructor_args():
    sig = inspect.signature(ir_Guard.__init__)
    params = list(sig.parameters.keys())



def test_ir_actorinstance_is_not_abstract():
    assert not inspect.isabstract(ir_ActorInstance)


def test_ir_actorinstance_constructor_exists():
    assert callable(ir_ActorInstance.__init__)


def test_ir_actorinstance_constructor_args():
    sig = inspect.signature(ir_ActorInstance.__init__)
    params = list(sig.parameters.keys())



def test_ir_schedule_is_not_abstract():
    assert not inspect.isabstract(ir_Schedule)


def test_ir_schedule_constructor_exists():
    assert callable(ir_Schedule.__init__)


def test_ir_schedule_constructor_args():
    sig = inspect.signature(ir_Schedule.__init__)
    params = list(sig.parameters.keys())
    assert "PriorityGraph" in params, "Missing parameter 'PriorityGraph'"

def test_ir_schedule_has_PriorityGraph():
    assert hasattr(ir_Schedule, "PriorityGraph")
    descriptor = None
    for klass in ir_Schedule.__mro__:
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



def test_ir_network_is_not_abstract():
    assert not inspect.isabstract(ir_Network)


def test_ir_network_constructor_exists():
    assert callable(ir_Network.__init__)


def test_ir_network_constructor_args():
    sig = inspect.signature(ir_Network.__init__)
    params = list(sig.parameters.keys())



def test_ir_actor_is_not_abstract():
    assert not inspect.isabstract(ir_Actor)


def test_ir_actor_constructor_exists():
    assert callable(ir_Actor.__init__)


def test_ir_actor_constructor_args():
    sig = inspect.signature(ir_Actor.__init__)
    params = list(sig.parameters.keys())



def test_ir_externalactor_is_not_abstract():
    assert not inspect.isabstract(ir_ExternalActor)


def test_ir_externalactor_constructor_exists():
    assert callable(ir_ExternalActor.__init__)


def test_ir_externalactor_constructor_args():
    sig = inspect.signature(ir_ExternalActor.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_ir_generator_is_not_abstract():
    assert not inspect.isabstract(ir_Generator)


def test_ir_generator_constructor_exists():
    assert callable(ir_Generator.__init__)


def test_ir_generator_constructor_args():
    sig = inspect.signature(ir_Generator.__init__)
    params = list(sig.parameters.keys())



def test_ir_procexpression_is_not_abstract():
    assert not inspect.isabstract(ir_ProcExpression)


def test_ir_procexpression_constructor_exists():
    assert callable(ir_ProcExpression.__init__)


def test_ir_procexpression_constructor_args():
    sig = inspect.signature(ir_ProcExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir_action_is_not_abstract():
    assert not inspect.isabstract(ir_Action)


def test_ir_action_constructor_exists():
    assert callable(ir_Action.__init__)


def test_ir_action_constructor_args():
    sig = inspect.signature(ir_Action.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"

def test_ir_action_has_tag():
    assert hasattr(ir_Action, "tag")
    descriptor = None
    for klass in ir_Action.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_ir_lambdaexpression_is_not_abstract():
    assert not inspect.isabstract(ir_LambdaExpression)


def test_ir_lambdaexpression_constructor_exists():
    assert callable(ir_LambdaExpression.__init__)


def test_ir_lambdaexpression_constructor_args():
    sig = inspect.signature(ir_LambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir_block_is_not_abstract():
    assert not inspect.isabstract(ir_Block)


def test_ir_block_constructor_exists():
    assert callable(ir_Block.__init__)


def test_ir_block_constructor_args():
    sig = inspect.signature(ir_Block.__init__)
    params = list(sig.parameters.keys())



def test_ir_namespace_is_not_abstract():
    assert not inspect.isabstract(ir_Namespace)


def test_ir_namespace_constructor_exists():
    assert callable(ir_Namespace.__init__)


def test_ir_namespace_constructor_args():
    sig = inspect.signature(ir_Namespace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_namespace_has_name():
    assert hasattr(ir_Namespace, "name")
    descriptor = None
    for klass in ir_Namespace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_taggedexpression_is_not_abstract():
    assert not inspect.isabstract(ir_TaggedExpression)


def test_ir_taggedexpression_constructor_exists():
    assert callable(ir_TaggedExpression.__init__)


def test_ir_taggedexpression_constructor_args():
    sig = inspect.signature(ir_TaggedExpression.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"

def test_ir_taggedexpression_has_tag():
    assert hasattr(ir_TaggedExpression, "tag")
    descriptor = None
    for klass in ir_TaggedExpression.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_ir_type_is_not_abstract():
    assert not inspect.isabstract(ir_Type)


def test_ir_type_constructor_exists():
    assert callable(ir_Type.__init__)


def test_ir_type_constructor_args():
    sig = inspect.signature(ir_Type.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_ir_typedeclarationimport_is_not_abstract():
    assert not inspect.isabstract(ir_TypeDeclarationImport)


def test_ir_typedeclarationimport_constructor_exists():
    assert callable(ir_TypeDeclarationImport.__init__)


def test_ir_typedeclarationimport_constructor_args():
    sig = inspect.signature(ir_TypeDeclarationImport.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_ir_typedeclarationimport_has_namespace():
    assert hasattr(ir_TypeDeclarationImport, "namespace")
    descriptor = None
    for klass in ir_TypeDeclarationImport.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_ir_forwarddeclaration_is_not_abstract():
    assert not inspect.isabstract(ir_ForwardDeclaration)


def test_ir_forwarddeclaration_constructor_exists():
    assert callable(ir_ForwardDeclaration.__init__)


def test_ir_forwarddeclaration_constructor_args():
    sig = inspect.signature(ir_ForwardDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ir_typeconstructor_is_not_abstract():
    assert not inspect.isabstract(ir_TypeConstructor)


def test_ir_typeconstructor_constructor_exists():
    assert callable(ir_TypeConstructor.__init__)


def test_ir_typeconstructor_constructor_args():
    sig = inspect.signature(ir_TypeConstructor.__init__)
    params = list(sig.parameters.keys())



def test_ir_variableexternal_is_not_abstract():
    assert not inspect.isabstract(ir_VariableExternal)


def test_ir_variableexternal_constructor_exists():
    assert callable(ir_VariableExternal.__init__)


def test_ir_variableexternal_constructor_args():
    sig = inspect.signature(ir_VariableExternal.__init__)
    params = list(sig.parameters.keys())



def test_ir_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(ir_TypeDeclaration)


def test_ir_typedeclaration_constructor_exists():
    assert callable(ir_TypeDeclaration.__init__)


def test_ir_typedeclaration_constructor_args():
    sig = inspect.signature(ir_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ir_variableimport_is_not_abstract():
    assert not inspect.isabstract(ir_VariableImport)


def test_ir_variableimport_constructor_exists():
    assert callable(ir_VariableImport.__init__)


def test_ir_variableimport_constructor_args():
    sig = inspect.signature(ir_VariableImport.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_ir_variableimport_has_namespace():
    assert hasattr(ir_VariableImport, "namespace")
    descriptor = None
    for klass in ir_VariableImport.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_ir_annotation_is_not_abstract():
    assert not inspect.isabstract(ir_Annotation)


def test_ir_annotation_constructor_exists():
    assert callable(ir_Annotation.__init__)


def test_ir_annotation_constructor_args():
    sig = inspect.signature(ir_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_annotation_has_name():
    assert hasattr(ir_Annotation, "name")
    descriptor = None
    for klass in ir_Annotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_node_is_not_abstract():
    assert not inspect.isabstract(ir_Node)


def test_ir_node_constructor_exists():
    assert callable(ir_Node.__init__)


def test_ir_node_constructor_args():
    sig = inspect.signature(ir_Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ir_node_has_id():
    assert hasattr(ir_Node, "id")
    descriptor = None
    for klass in ir_Node.__mro__:
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



def test_ir_declaration_is_not_abstract():
    assert not inspect.isabstract(ir_Declaration)


def test_ir_declaration_constructor_exists():
    assert callable(ir_Declaration.__init__)


def test_ir_declaration_constructor_args():
    sig = inspect.signature(ir_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_declaration_has_name():
    assert hasattr(ir_Declaration, "name")
    descriptor = None
    for klass in ir_Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_connection_is_not_abstract():
    assert not inspect.isabstract(ir_Connection)


def test_ir_connection_constructor_exists():
    assert callable(ir_Connection.__init__)


def test_ir_connection_constructor_args():
    sig = inspect.signature(ir_Connection.__init__)
    params = list(sig.parameters.keys())



def test_ir_expression_is_not_abstract():
    assert not inspect.isabstract(ir_Expression)


def test_ir_expression_constructor_exists():
    assert callable(ir_Expression.__init__)


def test_ir_expression_constructor_args():
    sig = inspect.signature(ir_Expression.__init__)
    params = list(sig.parameters.keys())



def test_ir_statement_is_not_abstract():
    assert not inspect.isabstract(ir_Statement)


def test_ir_statement_constructor_exists():
    assert callable(ir_Statement.__init__)


def test_ir_statement_constructor_args():
    sig = inspect.signature(ir_Statement.__init__)
    params = list(sig.parameters.keys())



def test_ir_typerecord_is_not_abstract():
    assert not inspect.isabstract(ir_TypeRecord)


def test_ir_typerecord_constructor_exists():
    assert callable(ir_TypeRecord.__init__)


def test_ir_typerecord_constructor_args():
    sig = inspect.signature(ir_TypeRecord.__init__)
    params = list(sig.parameters.keys())



def test_ir_portaccess_is_not_abstract():
    assert not inspect.isabstract(ir_PortAccess)


def test_ir_portaccess_constructor_exists():
    assert callable(ir_PortAccess.__init__)


def test_ir_portaccess_constructor_args():
    sig = inspect.signature(ir_PortAccess.__init__)
    params = list(sig.parameters.keys())



def test_ir_portinstance_is_not_abstract():
    assert not inspect.isabstract(ir_PortInstance)


def test_ir_portinstance_constructor_exists():
    assert callable(ir_PortInstance.__init__)


def test_ir_portinstance_constructor_args():
    sig = inspect.signature(ir_PortInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_portinstance_has_name():
    assert hasattr(ir_PortInstance, "name")
    descriptor = None
    for klass in ir_PortInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_variablereference_is_not_abstract():
    assert not inspect.isabstract(ir_VariableReference)


def test_ir_variablereference_constructor_exists():
    assert callable(ir_VariableReference.__init__)


def test_ir_variablereference_constructor_args():
    sig = inspect.signature(ir_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_ir_member_is_not_abstract():
    assert not inspect.isabstract(ir_Member)


def test_ir_member_constructor_exists():
    assert callable(ir_Member.__init__)


def test_ir_member_constructor_args():
    sig = inspect.signature(ir_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_member_has_name():
    assert hasattr(ir_Member, "name")
    descriptor = None
    for klass in ir_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_scope_is_not_abstract():
    assert not inspect.isabstract(ir_Scope)


def test_ir_scope_constructor_exists():
    assert callable(ir_Scope.__init__)


def test_ir_scope_constructor_args():
    sig = inspect.signature(ir_Scope.__init__)
    params = list(sig.parameters.keys())



def test_ir_variable_is_not_abstract():
    assert not inspect.isabstract(ir_Variable)


def test_ir_variable_constructor_exists():
    assert callable(ir_Variable.__init__)


def test_ir_variable_constructor_args():
    sig = inspect.signature(ir_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_ir_variable_has_constant():
    assert hasattr(ir_Variable, "constant")
    descriptor = None
    for klass in ir_Variable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_ir_variable_has_parameter():
    assert hasattr(ir_Variable, "parameter")
    descriptor = None
    for klass in ir_Variable.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_ir_port_is_not_abstract():
    assert not inspect.isabstract(ir_Port)


def test_ir_port_constructor_exists():
    assert callable(ir_Port.__init__)


def test_ir_port_constructor_args():
    sig = inspect.signature(ir_Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_port_has_name():
    assert hasattr(ir_Port, "name")
    descriptor = None
    for klass in ir_Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_typeactor_is_not_abstract():
    assert not inspect.isabstract(ir_TypeActor)


def test_ir_typeactor_constructor_exists():
    assert callable(ir_TypeActor.__init__)


def test_ir_typeactor_constructor_args():
    sig = inspect.signature(ir_TypeActor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_ir_typeactor_has_name():
    assert hasattr(ir_TypeActor, "name")
    descriptor = None
    for klass in ir_TypeActor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir_typeactor_has_namespace():
    assert hasattr(ir_TypeActor, "namespace")
    descriptor = None
    for klass in ir_TypeActor.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_ir_abstractactor_is_not_abstract():
    assert not inspect.isabstract(ir_AbstractActor)


def test_ir_abstractactor_constructor_exists():
    assert callable(ir_AbstractActor.__init__)


def test_ir_abstractactor_constructor_args():
    sig = inspect.signature(ir_AbstractActor.__init__)
    params = list(sig.parameters.keys())


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
ir_AnnotationArgument_strategy = st.builds(
    ir_AnnotationArgument,
    value=
        safe_text,
    id=
        safe_text
)
ir_State_strategy = st.builds(
    ir_State,
    Action2TargetMap=
        safe_text,
    name=
        safe_text,
    PriorityGraph=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
ir_TypeString_strategy = st.builds(
    ir_TypeString,
)
ir_TypeExternal_strategy = st.builds(
    ir_TypeExternal,
    scopeName=
        safe_text,
    name=
        safe_text
)
ir_TypeInt_strategy = st.builds(
    ir_TypeInt,
)
ir_TypeLambda_strategy = st.builds(
    ir_TypeLambda,
)
ir_TypeProc_strategy = st.builds(
    ir_TypeProc,
)
ir_TypeUint_strategy = st.builds(
    ir_TypeUint,
)
ir_TypeList_strategy = st.builds(
    ir_TypeList,
)
ir_TypeFloat_strategy = st.builds(
    ir_TypeFloat,
)
ir_TypeBool_strategy = st.builds(
    ir_TypeBool,
)
LambdaExpression_strategy = st.builds(
    LambdaExpression,
)
ir_TypeUser_strategy = st.builds(
    ir_TypeUser,
)
PortAccess_strategy = st.builds(
    PortAccess,
)
ir_PortPeek_strategy = st.builds(
    ir_PortPeek,
    position=
        st.integers()
)
Block_strategy = st.builds(
    Block,
)
Statement_strategy = st.builds(
    Statement,
)
ir_ForEach_strategy = st.builds(
    ir_ForEach,
)
ir_ProcCall_strategy = st.builds(
    ir_ProcCall,
)
ir_IfStatement_strategy = st.builds(
    ir_IfStatement,
)
ir_WhileLoop_strategy = st.builds(
    ir_WhileLoop,
)
ir_ReturnValue_strategy = st.builds(
    ir_ReturnValue,
)
ir_Assign_strategy = st.builds(
    ir_Assign,
)
Connection_strategy = st.builds(
    Connection,
)
ir_ToSink_strategy = st.builds(
    ir_ToSink,
)
ir_FromSource_strategy = st.builds(
    ir_FromSource,
)
ir_Point2PointConnection_strategy = st.builds(
    ir_Point2PointConnection,
)
ir_TypeUndef_strategy = st.builds(
    ir_TypeUndef,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
ir_StringLiteral_strategy = st.builds(
    ir_StringLiteral,
    value=
        safe_text
)
ir_BooleanLiteral_strategy = st.builds(
    ir_BooleanLiteral,
    value=
        st.booleans()
)
ir_FloatLiteral_strategy = st.builds(
    ir_FloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ir_IntegerLiteral_strategy = st.builds(
    ir_IntegerLiteral,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
ir_ListExpression_strategy = st.builds(
    ir_ListExpression,
)
ir_VariableExpression_strategy = st.builds(
    ir_VariableExpression,
)
ir_IfExpression_strategy = st.builds(
    ir_IfExpression,
)
ir_LiteralExpression_strategy = st.builds(
    ir_LiteralExpression,
)
ExpressionCall_strategy = st.builds(
    ExpressionCall,
)
ir_TypeConstructorCall_strategy = st.builds(
    ir_TypeConstructorCall,
    name=
        safe_text
)
ir_FunctionCall_strategy = st.builds(
    ir_FunctionCall,
)
ir_ExpressionCall_strategy = st.builds(
    ir_ExpressionCall,
)
ir_UnaryExpression_strategy = st.builds(
    ir_UnaryExpression,
    operator=
        safe_text
)
ir_BinaryExpression_strategy = st.builds(
    ir_BinaryExpression,
    operator=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
ir_PortRead_strategy = st.builds(
    ir_PortRead,
)
ir_PortWrite_strategy = st.builds(
    ir_PortWrite,
)
ir_Guard_strategy = st.builds(
    ir_Guard,
)
ir_ActorInstance_strategy = st.builds(
    ir_ActorInstance,
)
ir_Schedule_strategy = st.builds(
    ir_Schedule,
    PriorityGraph=
        safe_text
)
AbstractActor_strategy = st.builds(
    AbstractActor,
)
ir_Network_strategy = st.builds(
    ir_Network,
)
ir_Actor_strategy = st.builds(
    ir_Actor,
)
ir_ExternalActor_strategy = st.builds(
    ir_ExternalActor,
)
Scope_strategy = st.builds(
    Scope,
)
ir_Generator_strategy = st.builds(
    ir_Generator,
)
ir_ProcExpression_strategy = st.builds(
    ir_ProcExpression,
)
ir_Action_strategy = st.builds(
    ir_Action,
    tag=
        safe_text
)
ir_LambdaExpression_strategy = st.builds(
    ir_LambdaExpression,
)
ir_Block_strategy = st.builds(
    ir_Block,
)
ir_Namespace_strategy = st.builds(
    ir_Namespace,
    name=
        safe_text
)
ir_TaggedExpression_strategy = st.builds(
    ir_TaggedExpression,
    tag=
        safe_text
)
ir_Type_strategy = st.builds(
    ir_Type,
)
Declaration_strategy = st.builds(
    Declaration,
)
ir_TypeDeclarationImport_strategy = st.builds(
    ir_TypeDeclarationImport,
    namespace=
        safe_text
)
ir_ForwardDeclaration_strategy = st.builds(
    ir_ForwardDeclaration,
)
ir_TypeConstructor_strategy = st.builds(
    ir_TypeConstructor,
)
ir_VariableExternal_strategy = st.builds(
    ir_VariableExternal,
)
ir_TypeDeclaration_strategy = st.builds(
    ir_TypeDeclaration,
)
ir_VariableImport_strategy = st.builds(
    ir_VariableImport,
    namespace=
        safe_text
)
ir_Annotation_strategy = st.builds(
    ir_Annotation,
    name=
        safe_text
)
ir_Node_strategy = st.builds(
    ir_Node,
    id=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
ir_Declaration_strategy = st.builds(
    ir_Declaration,
    name=
        safe_text
)
ir_Connection_strategy = st.builds(
    ir_Connection,
)
ir_Expression_strategy = st.builds(
    ir_Expression,
)
ir_Statement_strategy = st.builds(
    ir_Statement,
)
ir_TypeRecord_strategy = st.builds(
    ir_TypeRecord,
)
ir_PortAccess_strategy = st.builds(
    ir_PortAccess,
)
ir_PortInstance_strategy = st.builds(
    ir_PortInstance,
    name=
        safe_text
)
ir_VariableReference_strategy = st.builds(
    ir_VariableReference,
)
ir_Member_strategy = st.builds(
    ir_Member,
    name=
        safe_text
)
ir_Scope_strategy = st.builds(
    ir_Scope,
)
ir_Variable_strategy = st.builds(
    ir_Variable,
    constant=
        st.booleans(),
    parameter=
        st.booleans()
)
ir_Port_strategy = st.builds(
    ir_Port,
    name=
        safe_text
)
ir_TypeActor_strategy = st.builds(
    ir_TypeActor,
    name=
        safe_text,
    namespace=
        safe_text
)
ir_AbstractActor_strategy = st.builds(
    ir_AbstractActor,
)

@given(instance=ir_AnnotationArgument_strategy)
@settings(max_examples=50)
def test_ir_annotationargument_instantiation(instance):
    assert isinstance(instance, ir_AnnotationArgument)



@given(instance=ir_AnnotationArgument_strategy)
def test_ir_annotationargument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ir_AnnotationArgument_strategy)
def test_ir_annotationargument_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ir_State_strategy)
@settings(max_examples=50)
def test_ir_state_instantiation(instance):
    assert isinstance(instance, ir_State)



@given(instance=ir_State_strategy)
def test_ir_state_Action2TargetMap_setter(instance):
    original = instance.Action2TargetMap
    instance.Action2TargetMap = original
    assert instance.Action2TargetMap == original



@given(instance=ir_State_strategy)
def test_ir_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ir_State_strategy)
def test_ir_state_PriorityGraph_setter(instance):
    original = instance.PriorityGraph
    instance.PriorityGraph = original
    assert instance.PriorityGraph == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=ir_TypeString_strategy)
@settings(max_examples=50)
def test_ir_typestring_instantiation(instance):
    assert isinstance(instance, ir_TypeString)

@given(instance=ir_TypeExternal_strategy)
@settings(max_examples=50)
def test_ir_typeexternal_instantiation(instance):
    assert isinstance(instance, ir_TypeExternal)



@given(instance=ir_TypeExternal_strategy)
def test_ir_typeexternal_scopeName_setter(instance):
    original = instance.scopeName
    instance.scopeName = original
    assert instance.scopeName == original



@given(instance=ir_TypeExternal_strategy)
def test_ir_typeexternal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_TypeInt_strategy)
@settings(max_examples=50)
def test_ir_typeint_instantiation(instance):
    assert isinstance(instance, ir_TypeInt)

@given(instance=ir_TypeLambda_strategy)
@settings(max_examples=50)
def test_ir_typelambda_instantiation(instance):
    assert isinstance(instance, ir_TypeLambda)

@given(instance=ir_TypeProc_strategy)
@settings(max_examples=50)
def test_ir_typeproc_instantiation(instance):
    assert isinstance(instance, ir_TypeProc)

@given(instance=ir_TypeUint_strategy)
@settings(max_examples=50)
def test_ir_typeuint_instantiation(instance):
    assert isinstance(instance, ir_TypeUint)

@given(instance=ir_TypeList_strategy)
@settings(max_examples=50)
def test_ir_typelist_instantiation(instance):
    assert isinstance(instance, ir_TypeList)

@given(instance=ir_TypeFloat_strategy)
@settings(max_examples=50)
def test_ir_typefloat_instantiation(instance):
    assert isinstance(instance, ir_TypeFloat)

@given(instance=ir_TypeBool_strategy)
@settings(max_examples=50)
def test_ir_typebool_instantiation(instance):
    assert isinstance(instance, ir_TypeBool)

@given(instance=LambdaExpression_strategy)
@settings(max_examples=50)
def test_lambdaexpression_instantiation(instance):
    assert isinstance(instance, LambdaExpression)

@given(instance=ir_TypeUser_strategy)
@settings(max_examples=50)
def test_ir_typeuser_instantiation(instance):
    assert isinstance(instance, ir_TypeUser)

@given(instance=PortAccess_strategy)
@settings(max_examples=50)
def test_portaccess_instantiation(instance):
    assert isinstance(instance, PortAccess)

@given(instance=ir_PortPeek_strategy)
@settings(max_examples=50)
def test_ir_portpeek_instantiation(instance):
    assert isinstance(instance, ir_PortPeek)



@given(instance=ir_PortPeek_strategy)
def test_ir_portpeek_position_setter(instance):
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

@given(instance=ir_ForEach_strategy)
@settings(max_examples=50)
def test_ir_foreach_instantiation(instance):
    assert isinstance(instance, ir_ForEach)

@given(instance=ir_ProcCall_strategy)
@settings(max_examples=50)
def test_ir_proccall_instantiation(instance):
    assert isinstance(instance, ir_ProcCall)

@given(instance=ir_IfStatement_strategy)
@settings(max_examples=50)
def test_ir_ifstatement_instantiation(instance):
    assert isinstance(instance, ir_IfStatement)

@given(instance=ir_WhileLoop_strategy)
@settings(max_examples=50)
def test_ir_whileloop_instantiation(instance):
    assert isinstance(instance, ir_WhileLoop)

@given(instance=ir_ReturnValue_strategy)
@settings(max_examples=50)
def test_ir_returnvalue_instantiation(instance):
    assert isinstance(instance, ir_ReturnValue)

@given(instance=ir_Assign_strategy)
@settings(max_examples=50)
def test_ir_assign_instantiation(instance):
    assert isinstance(instance, ir_Assign)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=ir_ToSink_strategy)
@settings(max_examples=50)
def test_ir_tosink_instantiation(instance):
    assert isinstance(instance, ir_ToSink)

@given(instance=ir_FromSource_strategy)
@settings(max_examples=50)
def test_ir_fromsource_instantiation(instance):
    assert isinstance(instance, ir_FromSource)

@given(instance=ir_Point2PointConnection_strategy)
@settings(max_examples=50)
def test_ir_point2pointconnection_instantiation(instance):
    assert isinstance(instance, ir_Point2PointConnection)

@given(instance=ir_TypeUndef_strategy)
@settings(max_examples=50)
def test_ir_typeundef_instantiation(instance):
    assert isinstance(instance, ir_TypeUndef)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=ir_StringLiteral_strategy)
@settings(max_examples=50)
def test_ir_stringliteral_instantiation(instance):
    assert isinstance(instance, ir_StringLiteral)



@given(instance=ir_StringLiteral_strategy)
def test_ir_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_ir_booleanliteral_instantiation(instance):
    assert isinstance(instance, ir_BooleanLiteral)



@given(instance=ir_BooleanLiteral_strategy)
def test_ir_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_FloatLiteral_strategy)
@settings(max_examples=50)
def test_ir_floatliteral_instantiation(instance):
    assert isinstance(instance, ir_FloatLiteral)



@given(instance=ir_FloatLiteral_strategy)
def test_ir_floatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_ir_integerliteral_instantiation(instance):
    assert isinstance(instance, ir_IntegerLiteral)



@given(instance=ir_IntegerLiteral_strategy)
def test_ir_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ir_ListExpression_strategy)
@settings(max_examples=50)
def test_ir_listexpression_instantiation(instance):
    assert isinstance(instance, ir_ListExpression)

@given(instance=ir_VariableExpression_strategy)
@settings(max_examples=50)
def test_ir_variableexpression_instantiation(instance):
    assert isinstance(instance, ir_VariableExpression)

@given(instance=ir_IfExpression_strategy)
@settings(max_examples=50)
def test_ir_ifexpression_instantiation(instance):
    assert isinstance(instance, ir_IfExpression)

@given(instance=ir_LiteralExpression_strategy)
@settings(max_examples=50)
def test_ir_literalexpression_instantiation(instance):
    assert isinstance(instance, ir_LiteralExpression)

@given(instance=ExpressionCall_strategy)
@settings(max_examples=50)
def test_expressioncall_instantiation(instance):
    assert isinstance(instance, ExpressionCall)

@given(instance=ir_TypeConstructorCall_strategy)
@settings(max_examples=50)
def test_ir_typeconstructorcall_instantiation(instance):
    assert isinstance(instance, ir_TypeConstructorCall)



@given(instance=ir_TypeConstructorCall_strategy)
def test_ir_typeconstructorcall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_FunctionCall_strategy)
@settings(max_examples=50)
def test_ir_functioncall_instantiation(instance):
    assert isinstance(instance, ir_FunctionCall)

@given(instance=ir_ExpressionCall_strategy)
@settings(max_examples=50)
def test_ir_expressioncall_instantiation(instance):
    assert isinstance(instance, ir_ExpressionCall)

@given(instance=ir_UnaryExpression_strategy)
@settings(max_examples=50)
def test_ir_unaryexpression_instantiation(instance):
    assert isinstance(instance, ir_UnaryExpression)



@given(instance=ir_UnaryExpression_strategy)
def test_ir_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ir_BinaryExpression_strategy)
@settings(max_examples=50)
def test_ir_binaryexpression_instantiation(instance):
    assert isinstance(instance, ir_BinaryExpression)



@given(instance=ir_BinaryExpression_strategy)
def test_ir_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ir_PortRead_strategy)
@settings(max_examples=50)
def test_ir_portread_instantiation(instance):
    assert isinstance(instance, ir_PortRead)

@given(instance=ir_PortWrite_strategy)
@settings(max_examples=50)
def test_ir_portwrite_instantiation(instance):
    assert isinstance(instance, ir_PortWrite)

@given(instance=ir_Guard_strategy)
@settings(max_examples=50)
def test_ir_guard_instantiation(instance):
    assert isinstance(instance, ir_Guard)

@given(instance=ir_ActorInstance_strategy)
@settings(max_examples=50)
def test_ir_actorinstance_instantiation(instance):
    assert isinstance(instance, ir_ActorInstance)

@given(instance=ir_Schedule_strategy)
@settings(max_examples=50)
def test_ir_schedule_instantiation(instance):
    assert isinstance(instance, ir_Schedule)



@given(instance=ir_Schedule_strategy)
def test_ir_schedule_PriorityGraph_setter(instance):
    original = instance.PriorityGraph
    instance.PriorityGraph = original
    assert instance.PriorityGraph == original

@given(instance=AbstractActor_strategy)
@settings(max_examples=50)
def test_abstractactor_instantiation(instance):
    assert isinstance(instance, AbstractActor)

@given(instance=ir_Network_strategy)
@settings(max_examples=50)
def test_ir_network_instantiation(instance):
    assert isinstance(instance, ir_Network)

@given(instance=ir_Actor_strategy)
@settings(max_examples=50)
def test_ir_actor_instantiation(instance):
    assert isinstance(instance, ir_Actor)

@given(instance=ir_ExternalActor_strategy)
@settings(max_examples=50)
def test_ir_externalactor_instantiation(instance):
    assert isinstance(instance, ir_ExternalActor)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=ir_Generator_strategy)
@settings(max_examples=50)
def test_ir_generator_instantiation(instance):
    assert isinstance(instance, ir_Generator)

@given(instance=ir_ProcExpression_strategy)
@settings(max_examples=50)
def test_ir_procexpression_instantiation(instance):
    assert isinstance(instance, ir_ProcExpression)

@given(instance=ir_Action_strategy)
@settings(max_examples=50)
def test_ir_action_instantiation(instance):
    assert isinstance(instance, ir_Action)



@given(instance=ir_Action_strategy)
def test_ir_action_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=ir_LambdaExpression_strategy)
@settings(max_examples=50)
def test_ir_lambdaexpression_instantiation(instance):
    assert isinstance(instance, ir_LambdaExpression)

@given(instance=ir_Block_strategy)
@settings(max_examples=50)
def test_ir_block_instantiation(instance):
    assert isinstance(instance, ir_Block)

@given(instance=ir_Namespace_strategy)
@settings(max_examples=50)
def test_ir_namespace_instantiation(instance):
    assert isinstance(instance, ir_Namespace)



@given(instance=ir_Namespace_strategy)
def test_ir_namespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_TaggedExpression_strategy)
@settings(max_examples=50)
def test_ir_taggedexpression_instantiation(instance):
    assert isinstance(instance, ir_TaggedExpression)



@given(instance=ir_TaggedExpression_strategy)
def test_ir_taggedexpression_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=ir_Type_strategy)
@settings(max_examples=50)
def test_ir_type_instantiation(instance):
    assert isinstance(instance, ir_Type)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=ir_TypeDeclarationImport_strategy)
@settings(max_examples=50)
def test_ir_typedeclarationimport_instantiation(instance):
    assert isinstance(instance, ir_TypeDeclarationImport)



@given(instance=ir_TypeDeclarationImport_strategy)
def test_ir_typedeclarationimport_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=ir_ForwardDeclaration_strategy)
@settings(max_examples=50)
def test_ir_forwarddeclaration_instantiation(instance):
    assert isinstance(instance, ir_ForwardDeclaration)

@given(instance=ir_TypeConstructor_strategy)
@settings(max_examples=50)
def test_ir_typeconstructor_instantiation(instance):
    assert isinstance(instance, ir_TypeConstructor)

@given(instance=ir_VariableExternal_strategy)
@settings(max_examples=50)
def test_ir_variableexternal_instantiation(instance):
    assert isinstance(instance, ir_VariableExternal)

@given(instance=ir_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_ir_typedeclaration_instantiation(instance):
    assert isinstance(instance, ir_TypeDeclaration)

@given(instance=ir_VariableImport_strategy)
@settings(max_examples=50)
def test_ir_variableimport_instantiation(instance):
    assert isinstance(instance, ir_VariableImport)



@given(instance=ir_VariableImport_strategy)
def test_ir_variableimport_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=ir_Annotation_strategy)
@settings(max_examples=50)
def test_ir_annotation_instantiation(instance):
    assert isinstance(instance, ir_Annotation)



@given(instance=ir_Annotation_strategy)
def test_ir_annotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_Node_strategy)
@settings(max_examples=50)
def test_ir_node_instantiation(instance):
    assert isinstance(instance, ir_Node)



@given(instance=ir_Node_strategy)
def test_ir_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ir_Declaration_strategy)
@settings(max_examples=50)
def test_ir_declaration_instantiation(instance):
    assert isinstance(instance, ir_Declaration)



@given(instance=ir_Declaration_strategy)
def test_ir_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_Connection_strategy)
@settings(max_examples=50)
def test_ir_connection_instantiation(instance):
    assert isinstance(instance, ir_Connection)

@given(instance=ir_Expression_strategy)
@settings(max_examples=50)
def test_ir_expression_instantiation(instance):
    assert isinstance(instance, ir_Expression)

@given(instance=ir_Statement_strategy)
@settings(max_examples=50)
def test_ir_statement_instantiation(instance):
    assert isinstance(instance, ir_Statement)

@given(instance=ir_TypeRecord_strategy)
@settings(max_examples=50)
def test_ir_typerecord_instantiation(instance):
    assert isinstance(instance, ir_TypeRecord)

@given(instance=ir_PortAccess_strategy)
@settings(max_examples=50)
def test_ir_portaccess_instantiation(instance):
    assert isinstance(instance, ir_PortAccess)

@given(instance=ir_PortInstance_strategy)
@settings(max_examples=50)
def test_ir_portinstance_instantiation(instance):
    assert isinstance(instance, ir_PortInstance)



@given(instance=ir_PortInstance_strategy)
def test_ir_portinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_VariableReference_strategy)
@settings(max_examples=50)
def test_ir_variablereference_instantiation(instance):
    assert isinstance(instance, ir_VariableReference)

@given(instance=ir_Member_strategy)
@settings(max_examples=50)
def test_ir_member_instantiation(instance):
    assert isinstance(instance, ir_Member)



@given(instance=ir_Member_strategy)
def test_ir_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_Scope_strategy)
@settings(max_examples=50)
def test_ir_scope_instantiation(instance):
    assert isinstance(instance, ir_Scope)

@given(instance=ir_Variable_strategy)
@settings(max_examples=50)
def test_ir_variable_instantiation(instance):
    assert isinstance(instance, ir_Variable)



@given(instance=ir_Variable_strategy)
def test_ir_variable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original



@given(instance=ir_Variable_strategy)
def test_ir_variable_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=ir_Port_strategy)
@settings(max_examples=50)
def test_ir_port_instantiation(instance):
    assert isinstance(instance, ir_Port)



@given(instance=ir_Port_strategy)
def test_ir_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_TypeActor_strategy)
@settings(max_examples=50)
def test_ir_typeactor_instantiation(instance):
    assert isinstance(instance, ir_TypeActor)



@given(instance=ir_TypeActor_strategy)
def test_ir_typeactor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ir_TypeActor_strategy)
def test_ir_typeactor_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=ir_AbstractActor_strategy)
@settings(max_examples=50)
def test_ir_abstractactor_instantiation(instance):
    assert isinstance(instance, ir_AbstractActor)
