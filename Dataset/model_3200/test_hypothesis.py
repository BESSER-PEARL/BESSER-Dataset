import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iot2::Trace,
    IntegerExpression,
    iot2::IntegerComparisonExpression,
    iot2::IntegerCalculationExpression,
    iot2::Token,
    iot2::Input,
    iot2::InputValue,
    BooleanExpression,
    iot2::BooleanBinaryExpression,
    iot2::BooleanUnaryExpression,
    Action,
    iot2::OpaqueAction,
    ExecutableNode,
    iot2::Action,
    ActivityNode,
    iot2::ExecutableNode,
    iot2::ControlNode,
    ActivityEdge,
    iot2::ControlFlow,
    Value,
    iot2::IntegerValue,
    iot2::BooleanValue,
    Variable,
    iot2::BooleanVariable,
    iot2::IntegerVariable,
    iot2::Value,
    FinalNode,
    iot2::ActivityFinalNode,
    ControlNode,
    iot2::FinalNode,
    iot2::DecisionNode,
    iot2::ForkNode,
    iot2::JoinNode,
    iot2::MergeNode,
    iot2::InitialNode,
    Expression,
    iot2::Expression::Multiplication,
    iot2::Expression::Minus,
    iot2::Expression::Larger,
    iot2::IntegerExpression,
    iot2::Expression::False,
    iot2::Expression::True,
    iot2::Expression::Negate,
    iot2::Expression::Larger::Equal,
    iot2::Expression::Function,
    iot2::BooleanExpression,
    iot2::Expression::Number,
    iot2::Expression::CallMemberFunction,
    iot2::Expression::AccessArray,
    iot2::Expression::VariableName,
    iot2::Expression::Equal,
    iot2::Expression::Division,
    iot2::Expression::Smaller::Equal,
    iot2::Expression::Not::Equal,
    iot2::Expression::Or,
    iot2::Expression::AccessMember,
    iot2::Expression::Smaller,
    iot2::Expression::Exponentiation,
    iot2::Expression::Length,
    iot2::Expression::Concatenation,
    iot2::Expression::Modulo,
    iot2::Expression::VarArgs,
    iot2::Expression::And,
    iot2::Expression::Plus,
    iot2::Expression::String,
    iot2::Expression::Invert,
    iot2::Expression::CallFunction,
    iot2::Expression::Nil,
    Statement::FunctioncallOrAssignment,
    iot2::Statement::CallFunction,
    iot2::Statement::CallMemberFunction,
    iot2::Statement::Assignment,
    LastStatement::Return,
    iot2::LastStatement::ReturnWithValue,
    Field,
    iot2::Field::AppendEntryToTable,
    iot2::Field::AddEntryToTable,
    iot2::Field::AddEntryToTable::Brackets,
    iot2::Functioncall::Arguments,
    iot2::Expression::TableConstructor,
    iot2::Statement::If::Then::Else::ElseIfPart,
    iot2::Function,
    iot2::Expression,
    IDLType,
    Statement,
    iot2::Statement::Local::Variable::Declaration,
    iot2::Statement::If::Then::Else,
    iot2::Statement::LocalFunction::Declaration,
    iot2::Statement::For::Numeric,
    iot2::Statement::FunctioncallOrAssignment,
    iot2::Statement::Repeat,
    iot2::Statement::While,
    iot2::Statement::GlobalFunction::Declaration,
    iot2::Statement::For::Generic,
    iot2::Statement::Block,
    LastStatement,
    iot2::LastStatement::Break,
    iot2::LastStatement::Return,
    iot2::LastStatement,
    iot2::Statement,
    Chunk,
    iot2::Chunk,
    iot2::PrimitiveDef,
    Typed,
    iot2::Field,
    iot2::ParameterDef,
    Contained,
    iot2::Variable,
    NamedElement,
    iot2::ActivityNode,
    iot2::ActivityEdge,
    iot2::TypedefDef,
    iot2::IDLType,
    iot2::Typed,
    iot2::NamedElement,
    iot2::Container,
    iot2::Contained,
    iot2::Block,
    iot2::ExceptionDef,
    HWComponent,
    iot2::Actuator,
    iot2::Sensor,
    iot2::OperationDef,
    iot2::Activity,
    iot2::Sketch,
    iot2::Board,
    iot2::HWComponent,
    iot2::System,
    IntegerCalculationOperator,
    PrimitiveKind,
    BooleanUnaryOperator,
    IntegerComparisonOperator,
    BooleanBinaryOperator,
    ParameterMode,
    BoardType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iot2::trace_is_not_abstract():
    assert not inspect.isabstract(iot2::Trace)


def test_iot2::trace_constructor_exists():
    assert callable(iot2::Trace.__init__)


def test_iot2::trace_constructor_args():
    sig = inspect.signature(iot2::Trace.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_iot2::integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(iot2::IntegerComparisonExpression)


def test_iot2::integercomparisonexpression_constructor_exists():
    assert callable(iot2::IntegerComparisonExpression.__init__)


def test_iot2::integercomparisonexpression_constructor_args():
    sig = inspect.signature(iot2::IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot2::integercomparisonexpression_has_operator():
    assert hasattr(iot2::IntegerComparisonExpression, "operator")
    descriptor = None
    for klass in iot2::IntegerComparisonExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iot2::integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(iot2::IntegerCalculationExpression)


def test_iot2::integercalculationexpression_constructor_exists():
    assert callable(iot2::IntegerCalculationExpression.__init__)


def test_iot2::integercalculationexpression_constructor_args():
    sig = inspect.signature(iot2::IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot2::integercalculationexpression_has_operator():
    assert hasattr(iot2::IntegerCalculationExpression, "operator")
    descriptor = None
    for klass in iot2::IntegerCalculationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iot2::token_is_not_abstract():
    assert not inspect.isabstract(iot2::Token)


def test_iot2::token_constructor_exists():
    assert callable(iot2::Token.__init__)


def test_iot2::token_constructor_args():
    sig = inspect.signature(iot2::Token.__init__)
    params = list(sig.parameters.keys())



def test_iot2::input_is_not_abstract():
    assert not inspect.isabstract(iot2::Input)


def test_iot2::input_constructor_exists():
    assert callable(iot2::Input.__init__)


def test_iot2::input_constructor_args():
    sig = inspect.signature(iot2::Input.__init__)
    params = list(sig.parameters.keys())



def test_iot2::inputvalue_is_not_abstract():
    assert not inspect.isabstract(iot2::InputValue)


def test_iot2::inputvalue_constructor_exists():
    assert callable(iot2::InputValue.__init__)


def test_iot2::inputvalue_constructor_args():
    sig = inspect.signature(iot2::InputValue.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_iot2::booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(iot2::BooleanBinaryExpression)


def test_iot2::booleanbinaryexpression_constructor_exists():
    assert callable(iot2::BooleanBinaryExpression.__init__)


def test_iot2::booleanbinaryexpression_constructor_args():
    sig = inspect.signature(iot2::BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot2::booleanbinaryexpression_has_operator():
    assert hasattr(iot2::BooleanBinaryExpression, "operator")
    descriptor = None
    for klass in iot2::BooleanBinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iot2::booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(iot2::BooleanUnaryExpression)


def test_iot2::booleanunaryexpression_constructor_exists():
    assert callable(iot2::BooleanUnaryExpression.__init__)


def test_iot2::booleanunaryexpression_constructor_args():
    sig = inspect.signature(iot2::BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iot2::booleanunaryexpression_has_operator():
    assert hasattr(iot2::BooleanUnaryExpression, "operator")
    descriptor = None
    for klass in iot2::BooleanUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_iot2::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(iot2::OpaqueAction)


def test_iot2::opaqueaction_constructor_exists():
    assert callable(iot2::OpaqueAction.__init__)


def test_iot2::opaqueaction_constructor_args():
    sig = inspect.signature(iot2::OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::action_is_not_abstract():
    assert not inspect.isabstract(iot2::Action)


def test_iot2::action_constructor_exists():
    assert callable(iot2::Action.__init__)


def test_iot2::action_constructor_args():
    sig = inspect.signature(iot2::Action.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::executablenode_is_not_abstract():
    assert not inspect.isabstract(iot2::ExecutableNode)


def test_iot2::executablenode_constructor_exists():
    assert callable(iot2::ExecutableNode.__init__)


def test_iot2::executablenode_constructor_args():
    sig = inspect.signature(iot2::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::controlnode_is_not_abstract():
    assert not inspect.isabstract(iot2::ControlNode)


def test_iot2::controlnode_constructor_exists():
    assert callable(iot2::ControlNode.__init__)


def test_iot2::controlnode_constructor_args():
    sig = inspect.signature(iot2::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_iot2::controlflow_is_not_abstract():
    assert not inspect.isabstract(iot2::ControlFlow)


def test_iot2::controlflow_constructor_exists():
    assert callable(iot2::ControlFlow.__init__)


def test_iot2::controlflow_constructor_args():
    sig = inspect.signature(iot2::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_iot2::integervalue_is_not_abstract():
    assert not inspect.isabstract(iot2::IntegerValue)


def test_iot2::integervalue_constructor_exists():
    assert callable(iot2::IntegerValue.__init__)


def test_iot2::integervalue_constructor_args():
    sig = inspect.signature(iot2::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot2::integervalue_has_value():
    assert hasattr(iot2::IntegerValue, "value")
    descriptor = None
    for klass in iot2::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iot2::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(iot2::BooleanValue)


def test_iot2::booleanvalue_constructor_exists():
    assert callable(iot2::BooleanValue.__init__)


def test_iot2::booleanvalue_constructor_args():
    sig = inspect.signature(iot2::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot2::booleanvalue_has_value():
    assert hasattr(iot2::BooleanValue, "value")
    descriptor = None
    for klass in iot2::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_iot2::booleanvariable_is_not_abstract():
    assert not inspect.isabstract(iot2::BooleanVariable)


def test_iot2::booleanvariable_constructor_exists():
    assert callable(iot2::BooleanVariable.__init__)


def test_iot2::booleanvariable_constructor_args():
    sig = inspect.signature(iot2::BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_iot2::integervariable_is_not_abstract():
    assert not inspect.isabstract(iot2::IntegerVariable)


def test_iot2::integervariable_constructor_exists():
    assert callable(iot2::IntegerVariable.__init__)


def test_iot2::integervariable_constructor_args():
    sig = inspect.signature(iot2::IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_iot2::value_is_not_abstract():
    assert not inspect.isabstract(iot2::Value)


def test_iot2::value_constructor_exists():
    assert callable(iot2::Value.__init__)


def test_iot2::value_constructor_args():
    sig = inspect.signature(iot2::Value.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(iot2::ActivityFinalNode)


def test_iot2::activityfinalnode_constructor_exists():
    assert callable(iot2::ActivityFinalNode.__init__)


def test_iot2::activityfinalnode_constructor_args():
    sig = inspect.signature(iot2::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::finalnode_is_not_abstract():
    assert not inspect.isabstract(iot2::FinalNode)


def test_iot2::finalnode_constructor_exists():
    assert callable(iot2::FinalNode.__init__)


def test_iot2::finalnode_constructor_args():
    sig = inspect.signature(iot2::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::decisionnode_is_not_abstract():
    assert not inspect.isabstract(iot2::DecisionNode)


def test_iot2::decisionnode_constructor_exists():
    assert callable(iot2::DecisionNode.__init__)


def test_iot2::decisionnode_constructor_args():
    sig = inspect.signature(iot2::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::forknode_is_not_abstract():
    assert not inspect.isabstract(iot2::ForkNode)


def test_iot2::forknode_constructor_exists():
    assert callable(iot2::ForkNode.__init__)


def test_iot2::forknode_constructor_args():
    sig = inspect.signature(iot2::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::joinnode_is_not_abstract():
    assert not inspect.isabstract(iot2::JoinNode)


def test_iot2::joinnode_constructor_exists():
    assert callable(iot2::JoinNode.__init__)


def test_iot2::joinnode_constructor_args():
    sig = inspect.signature(iot2::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::mergenode_is_not_abstract():
    assert not inspect.isabstract(iot2::MergeNode)


def test_iot2::mergenode_constructor_exists():
    assert callable(iot2::MergeNode.__init__)


def test_iot2::mergenode_constructor_args():
    sig = inspect.signature(iot2::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_iot2::initialnode_is_not_abstract():
    assert not inspect.isabstract(iot2::InitialNode)


def test_iot2::initialnode_constructor_exists():
    assert callable(iot2::InitialNode.__init__)


def test_iot2::initialnode_constructor_args():
    sig = inspect.signature(iot2::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::multiplication_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Multiplication)


def test_iot2::expression::multiplication_constructor_exists():
    assert callable(iot2::Expression::Multiplication.__init__)


def test_iot2::expression::multiplication_constructor_args():
    sig = inspect.signature(iot2::Expression::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::minus_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Minus)


def test_iot2::expression::minus_constructor_exists():
    assert callable(iot2::Expression::Minus.__init__)


def test_iot2::expression::minus_constructor_args():
    sig = inspect.signature(iot2::Expression::Minus.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::larger_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Larger)


def test_iot2::expression::larger_constructor_exists():
    assert callable(iot2::Expression::Larger.__init__)


def test_iot2::expression::larger_constructor_args():
    sig = inspect.signature(iot2::Expression::Larger.__init__)
    params = list(sig.parameters.keys())



def test_iot2::integerexpression_is_not_abstract():
    assert not inspect.isabstract(iot2::IntegerExpression)


def test_iot2::integerexpression_constructor_exists():
    assert callable(iot2::IntegerExpression.__init__)


def test_iot2::integerexpression_constructor_args():
    sig = inspect.signature(iot2::IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::false_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::False)


def test_iot2::expression::false_constructor_exists():
    assert callable(iot2::Expression::False.__init__)


def test_iot2::expression::false_constructor_args():
    sig = inspect.signature(iot2::Expression::False.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::true_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::True)


def test_iot2::expression::true_constructor_exists():
    assert callable(iot2::Expression::True.__init__)


def test_iot2::expression::true_constructor_args():
    sig = inspect.signature(iot2::Expression::True.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::negate_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Negate)


def test_iot2::expression::negate_constructor_exists():
    assert callable(iot2::Expression::Negate.__init__)


def test_iot2::expression::negate_constructor_args():
    sig = inspect.signature(iot2::Expression::Negate.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::larger::equal_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Larger::Equal)


def test_iot2::expression::larger::equal_constructor_exists():
    assert callable(iot2::Expression::Larger::Equal.__init__)


def test_iot2::expression::larger::equal_constructor_args():
    sig = inspect.signature(iot2::Expression::Larger::Equal.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::function_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Function)


def test_iot2::expression::function_constructor_exists():
    assert callable(iot2::Expression::Function.__init__)


def test_iot2::expression::function_constructor_args():
    sig = inspect.signature(iot2::Expression::Function.__init__)
    params = list(sig.parameters.keys())



def test_iot2::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(iot2::BooleanExpression)


def test_iot2::booleanexpression_constructor_exists():
    assert callable(iot2::BooleanExpression.__init__)


def test_iot2::booleanexpression_constructor_args():
    sig = inspect.signature(iot2::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::number_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Number)


def test_iot2::expression::number_constructor_exists():
    assert callable(iot2::Expression::Number.__init__)


def test_iot2::expression::number_constructor_args():
    sig = inspect.signature(iot2::Expression::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot2::expression::number_has_value():
    assert hasattr(iot2::Expression::Number, "value")
    descriptor = None
    for klass in iot2::Expression::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iot2::expression::callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::CallMemberFunction)


def test_iot2::expression::callmemberfunction_constructor_exists():
    assert callable(iot2::Expression::CallMemberFunction.__init__)


def test_iot2::expression::callmemberfunction_constructor_args():
    sig = inspect.signature(iot2::Expression::CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"

def test_iot2::expression::callmemberfunction_has_memberFunctionName():
    assert hasattr(iot2::Expression::CallMemberFunction, "memberFunctionName")
    descriptor = None
    for klass in iot2::Expression::CallMemberFunction.__mro__:
        if "memberFunctionName" in klass.__dict__:
            descriptor = klass.__dict__["memberFunctionName"]
            break
    assert isinstance(descriptor, property)



def test_iot2::expression::accessarray_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::AccessArray)


def test_iot2::expression::accessarray_constructor_exists():
    assert callable(iot2::Expression::AccessArray.__init__)


def test_iot2::expression::accessarray_constructor_args():
    sig = inspect.signature(iot2::Expression::AccessArray.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::variablename_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::VariableName)


def test_iot2::expression::variablename_constructor_exists():
    assert callable(iot2::Expression::VariableName.__init__)


def test_iot2::expression::variablename_constructor_args():
    sig = inspect.signature(iot2::Expression::VariableName.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_iot2::expression::variablename_has_variable():
    assert hasattr(iot2::Expression::VariableName, "variable")
    descriptor = None
    for klass in iot2::Expression::VariableName.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_iot2::expression::equal_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Equal)


def test_iot2::expression::equal_constructor_exists():
    assert callable(iot2::Expression::Equal.__init__)


def test_iot2::expression::equal_constructor_args():
    sig = inspect.signature(iot2::Expression::Equal.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::division_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Division)


def test_iot2::expression::division_constructor_exists():
    assert callable(iot2::Expression::Division.__init__)


def test_iot2::expression::division_constructor_args():
    sig = inspect.signature(iot2::Expression::Division.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::smaller::equal_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Smaller::Equal)


def test_iot2::expression::smaller::equal_constructor_exists():
    assert callable(iot2::Expression::Smaller::Equal.__init__)


def test_iot2::expression::smaller::equal_constructor_args():
    sig = inspect.signature(iot2::Expression::Smaller::Equal.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::not::equal_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Not::Equal)


def test_iot2::expression::not::equal_constructor_exists():
    assert callable(iot2::Expression::Not::Equal.__init__)


def test_iot2::expression::not::equal_constructor_args():
    sig = inspect.signature(iot2::Expression::Not::Equal.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::or_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Or)


def test_iot2::expression::or_constructor_exists():
    assert callable(iot2::Expression::Or.__init__)


def test_iot2::expression::or_constructor_args():
    sig = inspect.signature(iot2::Expression::Or.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::accessmember_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::AccessMember)


def test_iot2::expression::accessmember_constructor_exists():
    assert callable(iot2::Expression::AccessMember.__init__)


def test_iot2::expression::accessmember_constructor_args():
    sig = inspect.signature(iot2::Expression::AccessMember.__init__)
    params = list(sig.parameters.keys())
    assert "memberName" in params, "Missing parameter 'memberName'"

def test_iot2::expression::accessmember_has_memberName():
    assert hasattr(iot2::Expression::AccessMember, "memberName")
    descriptor = None
    for klass in iot2::Expression::AccessMember.__mro__:
        if "memberName" in klass.__dict__:
            descriptor = klass.__dict__["memberName"]
            break
    assert isinstance(descriptor, property)



def test_iot2::expression::smaller_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Smaller)


def test_iot2::expression::smaller_constructor_exists():
    assert callable(iot2::Expression::Smaller.__init__)


def test_iot2::expression::smaller_constructor_args():
    sig = inspect.signature(iot2::Expression::Smaller.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::exponentiation_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Exponentiation)


def test_iot2::expression::exponentiation_constructor_exists():
    assert callable(iot2::Expression::Exponentiation.__init__)


def test_iot2::expression::exponentiation_constructor_args():
    sig = inspect.signature(iot2::Expression::Exponentiation.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::length_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Length)


def test_iot2::expression::length_constructor_exists():
    assert callable(iot2::Expression::Length.__init__)


def test_iot2::expression::length_constructor_args():
    sig = inspect.signature(iot2::Expression::Length.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::concatenation_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Concatenation)


def test_iot2::expression::concatenation_constructor_exists():
    assert callable(iot2::Expression::Concatenation.__init__)


def test_iot2::expression::concatenation_constructor_args():
    sig = inspect.signature(iot2::Expression::Concatenation.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::modulo_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Modulo)


def test_iot2::expression::modulo_constructor_exists():
    assert callable(iot2::Expression::Modulo.__init__)


def test_iot2::expression::modulo_constructor_args():
    sig = inspect.signature(iot2::Expression::Modulo.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::varargs_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::VarArgs)


def test_iot2::expression::varargs_constructor_exists():
    assert callable(iot2::Expression::VarArgs.__init__)


def test_iot2::expression::varargs_constructor_args():
    sig = inspect.signature(iot2::Expression::VarArgs.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::and_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::And)


def test_iot2::expression::and_constructor_exists():
    assert callable(iot2::Expression::And.__init__)


def test_iot2::expression::and_constructor_args():
    sig = inspect.signature(iot2::Expression::And.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::plus_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Plus)


def test_iot2::expression::plus_constructor_exists():
    assert callable(iot2::Expression::Plus.__init__)


def test_iot2::expression::plus_constructor_args():
    sig = inspect.signature(iot2::Expression::Plus.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::string_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::String)


def test_iot2::expression::string_constructor_exists():
    assert callable(iot2::Expression::String.__init__)


def test_iot2::expression::string_constructor_args():
    sig = inspect.signature(iot2::Expression::String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iot2::expression::string_has_value():
    assert hasattr(iot2::Expression::String, "value")
    descriptor = None
    for klass in iot2::Expression::String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iot2::expression::invert_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Invert)


def test_iot2::expression::invert_constructor_exists():
    assert callable(iot2::Expression::Invert.__init__)


def test_iot2::expression::invert_constructor_args():
    sig = inspect.signature(iot2::Expression::Invert.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::callfunction_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::CallFunction)


def test_iot2::expression::callfunction_constructor_exists():
    assert callable(iot2::Expression::CallFunction.__init__)


def test_iot2::expression::callfunction_constructor_args():
    sig = inspect.signature(iot2::Expression::CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::nil_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::Nil)


def test_iot2::expression::nil_constructor_exists():
    assert callable(iot2::Expression::Nil.__init__)


def test_iot2::expression::nil_constructor_args():
    sig = inspect.signature(iot2::Expression::Nil.__init__)
    params = list(sig.parameters.keys())



def test_statement::functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(Statement::FunctioncallOrAssignment)


def test_statement::functioncallorassignment_constructor_exists():
    assert callable(Statement::FunctioncallOrAssignment.__init__)


def test_statement::functioncallorassignment_constructor_args():
    sig = inspect.signature(Statement::FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement::callfunction_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::CallFunction)


def test_iot2::statement::callfunction_constructor_exists():
    assert callable(iot2::Statement::CallFunction.__init__)


def test_iot2::statement::callfunction_constructor_args():
    sig = inspect.signature(iot2::Statement::CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement::callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::CallMemberFunction)


def test_iot2::statement::callmemberfunction_constructor_exists():
    assert callable(iot2::Statement::CallMemberFunction.__init__)


def test_iot2::statement::callmemberfunction_constructor_args():
    sig = inspect.signature(iot2::Statement::CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"

def test_iot2::statement::callmemberfunction_has_memberFunctionName():
    assert hasattr(iot2::Statement::CallMemberFunction, "memberFunctionName")
    descriptor = None
    for klass in iot2::Statement::CallMemberFunction.__mro__:
        if "memberFunctionName" in klass.__dict__:
            descriptor = klass.__dict__["memberFunctionName"]
            break
    assert isinstance(descriptor, property)



def test_iot2::statement::assignment_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::Assignment)


def test_iot2::statement::assignment_constructor_exists():
    assert callable(iot2::Statement::Assignment.__init__)


def test_iot2::statement::assignment_constructor_args():
    sig = inspect.signature(iot2::Statement::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_laststatement::return_is_not_abstract():
    assert not inspect.isabstract(LastStatement::Return)


def test_laststatement::return_constructor_exists():
    assert callable(LastStatement::Return.__init__)


def test_laststatement::return_constructor_args():
    sig = inspect.signature(LastStatement::Return.__init__)
    params = list(sig.parameters.keys())



def test_iot2::laststatement::returnwithvalue_is_not_abstract():
    assert not inspect.isabstract(iot2::LastStatement::ReturnWithValue)


def test_iot2::laststatement::returnwithvalue_constructor_exists():
    assert callable(iot2::LastStatement::ReturnWithValue.__init__)


def test_iot2::laststatement::returnwithvalue_constructor_args():
    sig = inspect.signature(iot2::LastStatement::ReturnWithValue.__init__)
    params = list(sig.parameters.keys())



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_iot2::field::appendentrytotable_is_not_abstract():
    assert not inspect.isabstract(iot2::Field::AppendEntryToTable)


def test_iot2::field::appendentrytotable_constructor_exists():
    assert callable(iot2::Field::AppendEntryToTable.__init__)


def test_iot2::field::appendentrytotable_constructor_args():
    sig = inspect.signature(iot2::Field::AppendEntryToTable.__init__)
    params = list(sig.parameters.keys())



def test_iot2::field::addentrytotable_is_not_abstract():
    assert not inspect.isabstract(iot2::Field::AddEntryToTable)


def test_iot2::field::addentrytotable_constructor_exists():
    assert callable(iot2::Field::AddEntryToTable.__init__)


def test_iot2::field::addentrytotable_constructor_args():
    sig = inspect.signature(iot2::Field::AddEntryToTable.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_iot2::field::addentrytotable_has_key():
    assert hasattr(iot2::Field::AddEntryToTable, "key")
    descriptor = None
    for klass in iot2::Field::AddEntryToTable.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_iot2::field::addentrytotable::brackets_is_not_abstract():
    assert not inspect.isabstract(iot2::Field::AddEntryToTable::Brackets)


def test_iot2::field::addentrytotable::brackets_constructor_exists():
    assert callable(iot2::Field::AddEntryToTable::Brackets.__init__)


def test_iot2::field::addentrytotable::brackets_constructor_args():
    sig = inspect.signature(iot2::Field::AddEntryToTable::Brackets.__init__)
    params = list(sig.parameters.keys())



def test_iot2::functioncall::arguments_is_not_abstract():
    assert not inspect.isabstract(iot2::Functioncall::Arguments)


def test_iot2::functioncall::arguments_constructor_exists():
    assert callable(iot2::Functioncall::Arguments.__init__)


def test_iot2::functioncall::arguments_constructor_args():
    sig = inspect.signature(iot2::Functioncall::Arguments.__init__)
    params = list(sig.parameters.keys())



def test_iot2::expression::tableconstructor_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression::TableConstructor)


def test_iot2::expression::tableconstructor_constructor_exists():
    assert callable(iot2::Expression::TableConstructor.__init__)


def test_iot2::expression::tableconstructor_constructor_args():
    sig = inspect.signature(iot2::Expression::TableConstructor.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement::if::then::else::elseifpart_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::If::Then::Else::ElseIfPart)


def test_iot2::statement::if::then::else::elseifpart_constructor_exists():
    assert callable(iot2::Statement::If::Then::Else::ElseIfPart.__init__)


def test_iot2::statement::if::then::else::elseifpart_constructor_args():
    sig = inspect.signature(iot2::Statement::If::Then::Else::ElseIfPart.__init__)
    params = list(sig.parameters.keys())



def test_iot2::function_is_not_abstract():
    assert not inspect.isabstract(iot2::Function)


def test_iot2::function_constructor_exists():
    assert callable(iot2::Function.__init__)


def test_iot2::function_constructor_args():
    sig = inspect.signature(iot2::Function.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_iot2::function_has_varArgs():
    assert hasattr(iot2::Function, "varArgs")
    descriptor = None
    for klass in iot2::Function.__mro__:
        if "varArgs" in klass.__dict__:
            descriptor = klass.__dict__["varArgs"]
            break
    assert isinstance(descriptor, property)

def test_iot2::function_has_parameters():
    assert hasattr(iot2::Function, "parameters")
    descriptor = None
    for klass in iot2::Function.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_iot2::expression_is_not_abstract():
    assert not inspect.isabstract(iot2::Expression)


def test_iot2::expression_constructor_exists():
    assert callable(iot2::Expression.__init__)


def test_iot2::expression_constructor_args():
    sig = inspect.signature(iot2::Expression.__init__)
    params = list(sig.parameters.keys())



def test_idltype_is_not_abstract():
    assert not inspect.isabstract(IDLType)


def test_idltype_constructor_exists():
    assert callable(IDLType.__init__)


def test_idltype_constructor_args():
    sig = inspect.signature(IDLType.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement::local::variable::declaration_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::Local::Variable::Declaration)


def test_iot2::statement::local::variable::declaration_constructor_exists():
    assert callable(iot2::Statement::Local::Variable::Declaration.__init__)


def test_iot2::statement::local::variable::declaration_constructor_args():
    sig = inspect.signature(iot2::Statement::Local::Variable::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "variableNames" in params, "Missing parameter 'variableNames'"

def test_iot2::statement::local::variable::declaration_has_variableNames():
    assert hasattr(iot2::Statement::Local::Variable::Declaration, "variableNames")
    descriptor = None
    for klass in iot2::Statement::Local::Variable::Declaration.__mro__:
        if "variableNames" in klass.__dict__:
            descriptor = klass.__dict__["variableNames"]
            break
    assert isinstance(descriptor, property)



def test_iot2::statement::if::then::else_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::If::Then::Else)


def test_iot2::statement::if::then::else_constructor_exists():
    assert callable(iot2::Statement::If::Then::Else.__init__)


def test_iot2::statement::if::then::else_constructor_args():
    sig = inspect.signature(iot2::Statement::If::Then::Else.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement::localfunction::declaration_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::LocalFunction::Declaration)


def test_iot2::statement::localfunction::declaration_constructor_exists():
    assert callable(iot2::Statement::LocalFunction::Declaration.__init__)


def test_iot2::statement::localfunction::declaration_constructor_args():
    sig = inspect.signature(iot2::Statement::LocalFunction::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_iot2::statement::localfunction::declaration_has_functionName():
    assert hasattr(iot2::Statement::LocalFunction::Declaration, "functionName")
    descriptor = None
    for klass in iot2::Statement::LocalFunction::Declaration.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_iot2::statement::for::numeric_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::For::Numeric)


def test_iot2::statement::for::numeric_constructor_exists():
    assert callable(iot2::Statement::For::Numeric.__init__)


def test_iot2::statement::for::numeric_constructor_args():
    sig = inspect.signature(iot2::Statement::For::Numeric.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"

def test_iot2::statement::for::numeric_has_iteratorName():
    assert hasattr(iot2::Statement::For::Numeric, "iteratorName")
    descriptor = None
    for klass in iot2::Statement::For::Numeric.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)



def test_iot2::statement::functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::FunctioncallOrAssignment)


def test_iot2::statement::functioncallorassignment_constructor_exists():
    assert callable(iot2::Statement::FunctioncallOrAssignment.__init__)


def test_iot2::statement::functioncallorassignment_constructor_args():
    sig = inspect.signature(iot2::Statement::FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement::repeat_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::Repeat)


def test_iot2::statement::repeat_constructor_exists():
    assert callable(iot2::Statement::Repeat.__init__)


def test_iot2::statement::repeat_constructor_args():
    sig = inspect.signature(iot2::Statement::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement::while_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::While)


def test_iot2::statement::while_constructor_exists():
    assert callable(iot2::Statement::While.__init__)


def test_iot2::statement::while_constructor_args():
    sig = inspect.signature(iot2::Statement::While.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement::globalfunction::declaration_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::GlobalFunction::Declaration)


def test_iot2::statement::globalfunction::declaration_constructor_exists():
    assert callable(iot2::Statement::GlobalFunction::Declaration.__init__)


def test_iot2::statement::globalfunction::declaration_constructor_args():
    sig = inspect.signature(iot2::Statement::GlobalFunction::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_iot2::statement::globalfunction::declaration_has_functionName():
    assert hasattr(iot2::Statement::GlobalFunction::Declaration, "functionName")
    descriptor = None
    for klass in iot2::Statement::GlobalFunction::Declaration.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)

def test_iot2::statement::globalfunction::declaration_has_prefix():
    assert hasattr(iot2::Statement::GlobalFunction::Declaration, "prefix")
    descriptor = None
    for klass in iot2::Statement::GlobalFunction::Declaration.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_iot2::statement::for::generic_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::For::Generic)


def test_iot2::statement::for::generic_constructor_exists():
    assert callable(iot2::Statement::For::Generic.__init__)


def test_iot2::statement::for::generic_constructor_args():
    sig = inspect.signature(iot2::Statement::For::Generic.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_iot2::statement::for::generic_has_names():
    assert hasattr(iot2::Statement::For::Generic, "names")
    descriptor = None
    for klass in iot2::Statement::For::Generic.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_iot2::statement::block_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement::Block)


def test_iot2::statement::block_constructor_exists():
    assert callable(iot2::Statement::Block.__init__)


def test_iot2::statement::block_constructor_args():
    sig = inspect.signature(iot2::Statement::Block.__init__)
    params = list(sig.parameters.keys())



def test_laststatement_is_not_abstract():
    assert not inspect.isabstract(LastStatement)


def test_laststatement_constructor_exists():
    assert callable(LastStatement.__init__)


def test_laststatement_constructor_args():
    sig = inspect.signature(LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_iot2::laststatement::break_is_not_abstract():
    assert not inspect.isabstract(iot2::LastStatement::Break)


def test_iot2::laststatement::break_constructor_exists():
    assert callable(iot2::LastStatement::Break.__init__)


def test_iot2::laststatement::break_constructor_args():
    sig = inspect.signature(iot2::LastStatement::Break.__init__)
    params = list(sig.parameters.keys())



def test_iot2::laststatement::return_is_not_abstract():
    assert not inspect.isabstract(iot2::LastStatement::Return)


def test_iot2::laststatement::return_constructor_exists():
    assert callable(iot2::LastStatement::Return.__init__)


def test_iot2::laststatement::return_constructor_args():
    sig = inspect.signature(iot2::LastStatement::Return.__init__)
    params = list(sig.parameters.keys())



def test_iot2::laststatement_is_not_abstract():
    assert not inspect.isabstract(iot2::LastStatement)


def test_iot2::laststatement_constructor_exists():
    assert callable(iot2::LastStatement.__init__)


def test_iot2::laststatement_constructor_args():
    sig = inspect.signature(iot2::LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_iot2::statement_is_not_abstract():
    assert not inspect.isabstract(iot2::Statement)


def test_iot2::statement_constructor_exists():
    assert callable(iot2::Statement.__init__)


def test_iot2::statement_constructor_args():
    sig = inspect.signature(iot2::Statement.__init__)
    params = list(sig.parameters.keys())



def test_chunk_is_not_abstract():
    assert not inspect.isabstract(Chunk)


def test_chunk_constructor_exists():
    assert callable(Chunk.__init__)


def test_chunk_constructor_args():
    sig = inspect.signature(Chunk.__init__)
    params = list(sig.parameters.keys())



def test_iot2::chunk_is_not_abstract():
    assert not inspect.isabstract(iot2::Chunk)


def test_iot2::chunk_constructor_exists():
    assert callable(iot2::Chunk.__init__)


def test_iot2::chunk_constructor_args():
    sig = inspect.signature(iot2::Chunk.__init__)
    params = list(sig.parameters.keys())



def test_iot2::primitivedef_is_not_abstract():
    assert not inspect.isabstract(iot2::PrimitiveDef)


def test_iot2::primitivedef_constructor_exists():
    assert callable(iot2::PrimitiveDef.__init__)


def test_iot2::primitivedef_constructor_args():
    sig = inspect.signature(iot2::PrimitiveDef.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_iot2::primitivedef_has_kind():
    assert hasattr(iot2::PrimitiveDef, "kind")
    descriptor = None
    for klass in iot2::PrimitiveDef.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_iot2::field_is_not_abstract():
    assert not inspect.isabstract(iot2::Field)


def test_iot2::field_constructor_exists():
    assert callable(iot2::Field.__init__)


def test_iot2::field_constructor_args():
    sig = inspect.signature(iot2::Field.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_iot2::field_has_identifier():
    assert hasattr(iot2::Field, "identifier")
    descriptor = None
    for klass in iot2::Field.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_iot2::parameterdef_is_not_abstract():
    assert not inspect.isabstract(iot2::ParameterDef)


def test_iot2::parameterdef_constructor_exists():
    assert callable(iot2::ParameterDef.__init__)


def test_iot2::parameterdef_constructor_args():
    sig = inspect.signature(iot2::ParameterDef.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_iot2::parameterdef_has_direction():
    assert hasattr(iot2::ParameterDef, "direction")
    descriptor = None
    for klass in iot2::ParameterDef.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_iot2::parameterdef_has_identifier():
    assert hasattr(iot2::ParameterDef, "identifier")
    descriptor = None
    for klass in iot2::ParameterDef.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_contained_is_not_abstract():
    assert not inspect.isabstract(Contained)


def test_contained_constructor_exists():
    assert callable(Contained.__init__)


def test_contained_constructor_args():
    sig = inspect.signature(Contained.__init__)
    params = list(sig.parameters.keys())



def test_iot2::variable_is_not_abstract():
    assert not inspect.isabstract(iot2::Variable)


def test_iot2::variable_constructor_exists():
    assert callable(iot2::Variable.__init__)


def test_iot2::variable_constructor_args():
    sig = inspect.signature(iot2::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2::variable_has_name():
    assert hasattr(iot2::Variable, "name")
    descriptor = None
    for klass in iot2::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_iot2::activitynode_is_not_abstract():
    assert not inspect.isabstract(iot2::ActivityNode)


def test_iot2::activitynode_constructor_exists():
    assert callable(iot2::ActivityNode.__init__)


def test_iot2::activitynode_constructor_args():
    sig = inspect.signature(iot2::ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"

def test_iot2::activitynode_has_running():
    assert hasattr(iot2::ActivityNode, "running")
    descriptor = None
    for klass in iot2::ActivityNode.__mro__:
        if "running" in klass.__dict__:
            descriptor = klass.__dict__["running"]
            break
    assert isinstance(descriptor, property)



def test_iot2::activityedge_is_not_abstract():
    assert not inspect.isabstract(iot2::ActivityEdge)


def test_iot2::activityedge_constructor_exists():
    assert callable(iot2::ActivityEdge.__init__)


def test_iot2::activityedge_constructor_args():
    sig = inspect.signature(iot2::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_iot2::typedefdef_is_not_abstract():
    assert not inspect.isabstract(iot2::TypedefDef)


def test_iot2::typedefdef_constructor_exists():
    assert callable(iot2::TypedefDef.__init__)


def test_iot2::typedefdef_constructor_args():
    sig = inspect.signature(iot2::TypedefDef.__init__)
    params = list(sig.parameters.keys())



def test_iot2::idltype_is_not_abstract():
    assert not inspect.isabstract(iot2::IDLType)


def test_iot2::idltype_constructor_exists():
    assert callable(iot2::IDLType.__init__)


def test_iot2::idltype_constructor_args():
    sig = inspect.signature(iot2::IDLType.__init__)
    params = list(sig.parameters.keys())
    assert "typeCode" in params, "Missing parameter 'typeCode'"

def test_iot2::idltype_has_typeCode():
    assert hasattr(iot2::IDLType, "typeCode")
    descriptor = None
    for klass in iot2::IDLType.__mro__:
        if "typeCode" in klass.__dict__:
            descriptor = klass.__dict__["typeCode"]
            break
    assert isinstance(descriptor, property)



def test_iot2::typed_is_not_abstract():
    assert not inspect.isabstract(iot2::Typed)


def test_iot2::typed_constructor_exists():
    assert callable(iot2::Typed.__init__)


def test_iot2::typed_constructor_args():
    sig = inspect.signature(iot2::Typed.__init__)
    params = list(sig.parameters.keys())



def test_iot2::namedelement_is_not_abstract():
    assert not inspect.isabstract(iot2::NamedElement)


def test_iot2::namedelement_constructor_exists():
    assert callable(iot2::NamedElement.__init__)


def test_iot2::namedelement_constructor_args():
    sig = inspect.signature(iot2::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_iot2::namedelement_has_identifier():
    assert hasattr(iot2::NamedElement, "identifier")
    descriptor = None
    for klass in iot2::NamedElement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_iot2::namedelement_has_name():
    assert hasattr(iot2::NamedElement, "name")
    descriptor = None
    for klass in iot2::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2::container_is_not_abstract():
    assert not inspect.isabstract(iot2::Container)


def test_iot2::container_constructor_exists():
    assert callable(iot2::Container.__init__)


def test_iot2::container_constructor_args():
    sig = inspect.signature(iot2::Container.__init__)
    params = list(sig.parameters.keys())



def test_iot2::contained_is_not_abstract():
    assert not inspect.isabstract(iot2::Contained)


def test_iot2::contained_constructor_exists():
    assert callable(iot2::Contained.__init__)


def test_iot2::contained_constructor_args():
    sig = inspect.signature(iot2::Contained.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "absoluteName" in params, "Missing parameter 'absoluteName'"
    assert "repositoryId" in params, "Missing parameter 'repositoryId'"

def test_iot2::contained_has_version():
    assert hasattr(iot2::Contained, "version")
    descriptor = None
    for klass in iot2::Contained.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_iot2::contained_has_absoluteName():
    assert hasattr(iot2::Contained, "absoluteName")
    descriptor = None
    for klass in iot2::Contained.__mro__:
        if "absoluteName" in klass.__dict__:
            descriptor = klass.__dict__["absoluteName"]
            break
    assert isinstance(descriptor, property)

def test_iot2::contained_has_repositoryId():
    assert hasattr(iot2::Contained, "repositoryId")
    descriptor = None
    for klass in iot2::Contained.__mro__:
        if "repositoryId" in klass.__dict__:
            descriptor = klass.__dict__["repositoryId"]
            break
    assert isinstance(descriptor, property)



def test_iot2::block_is_not_abstract():
    assert not inspect.isabstract(iot2::Block)


def test_iot2::block_constructor_exists():
    assert callable(iot2::Block.__init__)


def test_iot2::block_constructor_args():
    sig = inspect.signature(iot2::Block.__init__)
    params = list(sig.parameters.keys())



def test_iot2::exceptiondef_is_not_abstract():
    assert not inspect.isabstract(iot2::ExceptionDef)


def test_iot2::exceptiondef_constructor_exists():
    assert callable(iot2::ExceptionDef.__init__)


def test_iot2::exceptiondef_constructor_args():
    sig = inspect.signature(iot2::ExceptionDef.__init__)
    params = list(sig.parameters.keys())
    assert "typeCode" in params, "Missing parameter 'typeCode'"

def test_iot2::exceptiondef_has_typeCode():
    assert hasattr(iot2::ExceptionDef, "typeCode")
    descriptor = None
    for klass in iot2::ExceptionDef.__mro__:
        if "typeCode" in klass.__dict__:
            descriptor = klass.__dict__["typeCode"]
            break
    assert isinstance(descriptor, property)



def test_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HWComponent)


def test_hwcomponent_constructor_exists():
    assert callable(HWComponent.__init__)


def test_hwcomponent_constructor_args():
    sig = inspect.signature(HWComponent.__init__)
    params = list(sig.parameters.keys())



def test_iot2::actuator_is_not_abstract():
    assert not inspect.isabstract(iot2::Actuator)


def test_iot2::actuator_constructor_exists():
    assert callable(iot2::Actuator.__init__)


def test_iot2::actuator_constructor_args():
    sig = inspect.signature(iot2::Actuator.__init__)
    params = list(sig.parameters.keys())



def test_iot2::sensor_is_not_abstract():
    assert not inspect.isabstract(iot2::Sensor)


def test_iot2::sensor_constructor_exists():
    assert callable(iot2::Sensor.__init__)


def test_iot2::sensor_constructor_args():
    sig = inspect.signature(iot2::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_iot2::operationdef_is_not_abstract():
    assert not inspect.isabstract(iot2::OperationDef)


def test_iot2::operationdef_constructor_exists():
    assert callable(iot2::OperationDef.__init__)


def test_iot2::operationdef_constructor_args():
    sig = inspect.signature(iot2::OperationDef.__init__)
    params = list(sig.parameters.keys())
    assert "isOneway" in params, "Missing parameter 'isOneway'"
    assert "contexts" in params, "Missing parameter 'contexts'"

def test_iot2::operationdef_has_isOneway():
    assert hasattr(iot2::OperationDef, "isOneway")
    descriptor = None
    for klass in iot2::OperationDef.__mro__:
        if "isOneway" in klass.__dict__:
            descriptor = klass.__dict__["isOneway"]
            break
    assert isinstance(descriptor, property)

def test_iot2::operationdef_has_contexts():
    assert hasattr(iot2::OperationDef, "contexts")
    descriptor = None
    for klass in iot2::OperationDef.__mro__:
        if "contexts" in klass.__dict__:
            descriptor = klass.__dict__["contexts"]
            break
    assert isinstance(descriptor, property)



def test_iot2::activity_is_not_abstract():
    assert not inspect.isabstract(iot2::Activity)


def test_iot2::activity_constructor_exists():
    assert callable(iot2::Activity.__init__)


def test_iot2::activity_constructor_args():
    sig = inspect.signature(iot2::Activity.__init__)
    params = list(sig.parameters.keys())



def test_iot2::sketch_is_not_abstract():
    assert not inspect.isabstract(iot2::Sketch)


def test_iot2::sketch_constructor_exists():
    assert callable(iot2::Sketch.__init__)


def test_iot2::sketch_constructor_args():
    sig = inspect.signature(iot2::Sketch.__init__)
    params = list(sig.parameters.keys())



def test_iot2::board_is_not_abstract():
    assert not inspect.isabstract(iot2::Board)


def test_iot2::board_constructor_exists():
    assert callable(iot2::Board.__init__)


def test_iot2::board_constructor_args():
    sig = inspect.signature(iot2::Board.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_iot2::board_has_type():
    assert hasattr(iot2::Board, "type")
    descriptor = None
    for klass in iot2::Board.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_iot2::board_has_name():
    assert hasattr(iot2::Board, "name")
    descriptor = None
    for klass in iot2::Board.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2::hwcomponent_is_not_abstract():
    assert not inspect.isabstract(iot2::HWComponent)


def test_iot2::hwcomponent_constructor_exists():
    assert callable(iot2::HWComponent.__init__)


def test_iot2::hwcomponent_constructor_args():
    sig = inspect.signature(iot2::HWComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2::hwcomponent_has_name():
    assert hasattr(iot2::HWComponent, "name")
    descriptor = None
    for klass in iot2::HWComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iot2::system_is_not_abstract():
    assert not inspect.isabstract(iot2::System)


def test_iot2::system_constructor_exists():
    assert callable(iot2::System.__init__)


def test_iot2::system_constructor_args():
    sig = inspect.signature(iot2::System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iot2::system_has_name():
    assert hasattr(iot2::System, "name")
    descriptor = None
    for klass in iot2::System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_integercalculationoperator_exists():
    # Check that the Enumeration exists
    assert IntegerCalculationOperator is not None

def test_integercalculationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerCalculationOperator]
    expected_literals = [
        "ADD",
        "SUBRACT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerCalculationOperator"

def test_primitivekind_exists():
    # Check that the Enumeration exists
    assert PrimitiveKind is not None

def test_primitivekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveKind]
    expected_literals = [
        "PK_NULL",
        "PK_ULONGLONG",
        "PK_BOOLEAN",
        "PK_OBJREF",
        "PK_VOID",
        "PK_LONGLONG",
        "PK_OCTET",
        "PK_WSTRING",
        "PK_ULONG",
        "PK_USHORT",
        "PK_STRING",
        "PK_SHORT",
        "PK_DOUBLE",
        "PK_TYPECODE",
        "PK_PRINCIPAL",
        "PK_CHAR",
        "PK_WCHAR",
        "PK_FLOAT",
        "PK_LONG",
        "PK_ANY",
        "PK_LONGDOUBLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveKind"

def test_booleanunaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanUnaryOperator is not None

def test_booleanunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanUnaryOperator]
    expected_literals = [
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanUnaryOperator"

def test_integercomparisonoperator_exists():
    # Check that the Enumeration exists
    assert IntegerComparisonOperator is not None

def test_integercomparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerComparisonOperator]
    expected_literals = [
        "SMALLER",
        "GREATER",
        "SMALLER_EQUALS",
        "GREATER_EQUALS",
        "EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerComparisonOperator"

def test_booleanbinaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanBinaryOperator is not None

def test_booleanbinaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanBinaryOperator]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanBinaryOperator"

def test_parametermode_exists():
    # Check that the Enumeration exists
    assert ParameterMode is not None

def test_parametermode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterMode]
    expected_literals = [
        "PARAM_OUT",
        "PARAM_INOUT",
        "PARAM_IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterMode"

def test_boardtype_exists():
    # Check that the Enumeration exists
    assert BoardType is not None

def test_boardtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoardType]
    expected_literals = [
        "Arduino",
        "RaspberryPi",
        "BeagleBoard",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoardType"


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
iot2::Trace_strategy = st.builds(
    iot2::Trace,
)
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
iot2::IntegerComparisonExpression_strategy = st.builds(
    iot2::IntegerComparisonExpression,
    operator=
        safe_text
)
iot2::IntegerCalculationExpression_strategy = st.builds(
    iot2::IntegerCalculationExpression,
    operator=
        safe_text
)
iot2::Token_strategy = st.builds(
    iot2::Token,
)
iot2::Input_strategy = st.builds(
    iot2::Input,
)
iot2::InputValue_strategy = st.builds(
    iot2::InputValue,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
iot2::BooleanBinaryExpression_strategy = st.builds(
    iot2::BooleanBinaryExpression,
    operator=
        safe_text
)
iot2::BooleanUnaryExpression_strategy = st.builds(
    iot2::BooleanUnaryExpression,
    operator=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
iot2::OpaqueAction_strategy = st.builds(
    iot2::OpaqueAction,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
iot2::Action_strategy = st.builds(
    iot2::Action,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
iot2::ExecutableNode_strategy = st.builds(
    iot2::ExecutableNode,
)
iot2::ControlNode_strategy = st.builds(
    iot2::ControlNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
iot2::ControlFlow_strategy = st.builds(
    iot2::ControlFlow,
)
Value_strategy = st.builds(
    Value,
)
iot2::IntegerValue_strategy = st.builds(
    iot2::IntegerValue,
    value=
        st.integers()
)
iot2::BooleanValue_strategy = st.builds(
    iot2::BooleanValue,
    value=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
iot2::BooleanVariable_strategy = st.builds(
    iot2::BooleanVariable,
)
iot2::IntegerVariable_strategy = st.builds(
    iot2::IntegerVariable,
)
iot2::Value_strategy = st.builds(
    iot2::Value,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
iot2::ActivityFinalNode_strategy = st.builds(
    iot2::ActivityFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
iot2::FinalNode_strategy = st.builds(
    iot2::FinalNode,
)
iot2::DecisionNode_strategy = st.builds(
    iot2::DecisionNode,
)
iot2::ForkNode_strategy = st.builds(
    iot2::ForkNode,
)
iot2::JoinNode_strategy = st.builds(
    iot2::JoinNode,
)
iot2::MergeNode_strategy = st.builds(
    iot2::MergeNode,
)
iot2::InitialNode_strategy = st.builds(
    iot2::InitialNode,
)
Expression_strategy = st.builds(
    Expression,
)
iot2::Expression::Multiplication_strategy = st.builds(
    iot2::Expression::Multiplication,
)
iot2::Expression::Minus_strategy = st.builds(
    iot2::Expression::Minus,
)
iot2::Expression::Larger_strategy = st.builds(
    iot2::Expression::Larger,
)
iot2::IntegerExpression_strategy = st.builds(
    iot2::IntegerExpression,
)
iot2::Expression::False_strategy = st.builds(
    iot2::Expression::False,
)
iot2::Expression::True_strategy = st.builds(
    iot2::Expression::True,
)
iot2::Expression::Negate_strategy = st.builds(
    iot2::Expression::Negate,
)
iot2::Expression::Larger::Equal_strategy = st.builds(
    iot2::Expression::Larger::Equal,
)
iot2::Expression::Function_strategy = st.builds(
    iot2::Expression::Function,
)
iot2::BooleanExpression_strategy = st.builds(
    iot2::BooleanExpression,
)
iot2::Expression::Number_strategy = st.builds(
    iot2::Expression::Number,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
iot2::Expression::CallMemberFunction_strategy = st.builds(
    iot2::Expression::CallMemberFunction,
    memberFunctionName=
        safe_text
)
iot2::Expression::AccessArray_strategy = st.builds(
    iot2::Expression::AccessArray,
)
iot2::Expression::VariableName_strategy = st.builds(
    iot2::Expression::VariableName,
    variable=
        safe_text
)
iot2::Expression::Equal_strategy = st.builds(
    iot2::Expression::Equal,
)
iot2::Expression::Division_strategy = st.builds(
    iot2::Expression::Division,
)
iot2::Expression::Smaller::Equal_strategy = st.builds(
    iot2::Expression::Smaller::Equal,
)
iot2::Expression::Not::Equal_strategy = st.builds(
    iot2::Expression::Not::Equal,
)
iot2::Expression::Or_strategy = st.builds(
    iot2::Expression::Or,
)
iot2::Expression::AccessMember_strategy = st.builds(
    iot2::Expression::AccessMember,
    memberName=
        safe_text
)
iot2::Expression::Smaller_strategy = st.builds(
    iot2::Expression::Smaller,
)
iot2::Expression::Exponentiation_strategy = st.builds(
    iot2::Expression::Exponentiation,
)
iot2::Expression::Length_strategy = st.builds(
    iot2::Expression::Length,
)
iot2::Expression::Concatenation_strategy = st.builds(
    iot2::Expression::Concatenation,
)
iot2::Expression::Modulo_strategy = st.builds(
    iot2::Expression::Modulo,
)
iot2::Expression::VarArgs_strategy = st.builds(
    iot2::Expression::VarArgs,
)
iot2::Expression::And_strategy = st.builds(
    iot2::Expression::And,
)
iot2::Expression::Plus_strategy = st.builds(
    iot2::Expression::Plus,
)
iot2::Expression::String_strategy = st.builds(
    iot2::Expression::String,
    value=
        safe_text
)
iot2::Expression::Invert_strategy = st.builds(
    iot2::Expression::Invert,
)
iot2::Expression::CallFunction_strategy = st.builds(
    iot2::Expression::CallFunction,
)
iot2::Expression::Nil_strategy = st.builds(
    iot2::Expression::Nil,
)
Statement::FunctioncallOrAssignment_strategy = st.builds(
    Statement::FunctioncallOrAssignment,
)
iot2::Statement::CallFunction_strategy = st.builds(
    iot2::Statement::CallFunction,
)
iot2::Statement::CallMemberFunction_strategy = st.builds(
    iot2::Statement::CallMemberFunction,
    memberFunctionName=
        safe_text
)
iot2::Statement::Assignment_strategy = st.builds(
    iot2::Statement::Assignment,
)
LastStatement::Return_strategy = st.builds(
    LastStatement::Return,
)
iot2::LastStatement::ReturnWithValue_strategy = st.builds(
    iot2::LastStatement::ReturnWithValue,
)
Field_strategy = st.builds(
    Field,
)
iot2::Field::AppendEntryToTable_strategy = st.builds(
    iot2::Field::AppendEntryToTable,
)
iot2::Field::AddEntryToTable_strategy = st.builds(
    iot2::Field::AddEntryToTable,
    key=
        safe_text
)
iot2::Field::AddEntryToTable::Brackets_strategy = st.builds(
    iot2::Field::AddEntryToTable::Brackets,
)
iot2::Functioncall::Arguments_strategy = st.builds(
    iot2::Functioncall::Arguments,
)
iot2::Expression::TableConstructor_strategy = st.builds(
    iot2::Expression::TableConstructor,
)
iot2::Statement::If::Then::Else::ElseIfPart_strategy = st.builds(
    iot2::Statement::If::Then::Else::ElseIfPart,
)
iot2::Function_strategy = st.builds(
    iot2::Function,
    varArgs=
        st.booleans(),
    parameters=
        safe_text
)
iot2::Expression_strategy = st.builds(
    iot2::Expression,
)
IDLType_strategy = st.builds(
    IDLType,
)
Statement_strategy = st.builds(
    Statement,
)
iot2::Statement::Local::Variable::Declaration_strategy = st.builds(
    iot2::Statement::Local::Variable::Declaration,
    variableNames=
        safe_text
)
iot2::Statement::If::Then::Else_strategy = st.builds(
    iot2::Statement::If::Then::Else,
)
iot2::Statement::LocalFunction::Declaration_strategy = st.builds(
    iot2::Statement::LocalFunction::Declaration,
    functionName=
        safe_text
)
iot2::Statement::For::Numeric_strategy = st.builds(
    iot2::Statement::For::Numeric,
    iteratorName=
        safe_text
)
iot2::Statement::FunctioncallOrAssignment_strategy = st.builds(
    iot2::Statement::FunctioncallOrAssignment,
)
iot2::Statement::Repeat_strategy = st.builds(
    iot2::Statement::Repeat,
)
iot2::Statement::While_strategy = st.builds(
    iot2::Statement::While,
)
iot2::Statement::GlobalFunction::Declaration_strategy = st.builds(
    iot2::Statement::GlobalFunction::Declaration,
    functionName=
        safe_text,
    prefix=
        safe_text
)
iot2::Statement::For::Generic_strategy = st.builds(
    iot2::Statement::For::Generic,
    names=
        safe_text
)
iot2::Statement::Block_strategy = st.builds(
    iot2::Statement::Block,
)
LastStatement_strategy = st.builds(
    LastStatement,
)
iot2::LastStatement::Break_strategy = st.builds(
    iot2::LastStatement::Break,
)
iot2::LastStatement::Return_strategy = st.builds(
    iot2::LastStatement::Return,
)
iot2::LastStatement_strategy = st.builds(
    iot2::LastStatement,
)
iot2::Statement_strategy = st.builds(
    iot2::Statement,
)
Chunk_strategy = st.builds(
    Chunk,
)
iot2::Chunk_strategy = st.builds(
    iot2::Chunk,
)
iot2::PrimitiveDef_strategy = st.builds(
    iot2::PrimitiveDef,
    kind=
        safe_text
)
Typed_strategy = st.builds(
    Typed,
)
iot2::Field_strategy = st.builds(
    iot2::Field,
    identifier=
        safe_text
)
iot2::ParameterDef_strategy = st.builds(
    iot2::ParameterDef,
    direction=
        safe_text,
    identifier=
        safe_text
)
Contained_strategy = st.builds(
    Contained,
)
iot2::Variable_strategy = st.builds(
    iot2::Variable,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
iot2::ActivityNode_strategy = st.builds(
    iot2::ActivityNode,
    running=
        st.booleans()
)
iot2::ActivityEdge_strategy = st.builds(
    iot2::ActivityEdge,
)
iot2::TypedefDef_strategy = st.builds(
    iot2::TypedefDef,
)
iot2::IDLType_strategy = st.builds(
    iot2::IDLType,
    typeCode=
        safe_text
)
iot2::Typed_strategy = st.builds(
    iot2::Typed,
)
iot2::NamedElement_strategy = st.builds(
    iot2::NamedElement,
    identifier=
        safe_text,
    name=
        safe_text
)
iot2::Container_strategy = st.builds(
    iot2::Container,
)
iot2::Contained_strategy = st.builds(
    iot2::Contained,
    version=
        safe_text,
    absoluteName=
        safe_text,
    repositoryId=
        safe_text
)
iot2::Block_strategy = st.builds(
    iot2::Block,
)
iot2::ExceptionDef_strategy = st.builds(
    iot2::ExceptionDef,
    typeCode=
        safe_text
)
HWComponent_strategy = st.builds(
    HWComponent,
)
iot2::Actuator_strategy = st.builds(
    iot2::Actuator,
)
iot2::Sensor_strategy = st.builds(
    iot2::Sensor,
)
iot2::OperationDef_strategy = st.builds(
    iot2::OperationDef,
    isOneway=
        st.booleans(),
    contexts=
        safe_text
)
iot2::Activity_strategy = st.builds(
    iot2::Activity,
)
iot2::Sketch_strategy = st.builds(
    iot2::Sketch,
)
iot2::Board_strategy = st.builds(
    iot2::Board,
    type=
        safe_text,
    name=
        safe_text
)
iot2::HWComponent_strategy = st.builds(
    iot2::HWComponent,
    name=
        safe_text
)
iot2::System_strategy = st.builds(
    iot2::System,
    name=
        safe_text
)

@given(instance=iot2::Trace_strategy)
@settings(max_examples=50)
def test_iot2::trace_instantiation(instance):
    assert isinstance(instance, iot2::Trace)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=iot2::IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_iot2::integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, iot2::IntegerComparisonExpression)

@given(instance=iot2::IntegerComparisonExpression_strategy)
def test_iot2::integercomparisonexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=iot2::IntegerComparisonExpression_strategy)
def test_iot2::integercomparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=iot2::IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_iot2::integercalculationexpression_instantiation(instance):
    assert isinstance(instance, iot2::IntegerCalculationExpression)

@given(instance=iot2::IntegerCalculationExpression_strategy)
def test_iot2::integercalculationexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=iot2::IntegerCalculationExpression_strategy)
def test_iot2::integercalculationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=iot2::Token_strategy)
@settings(max_examples=50)
def test_iot2::token_instantiation(instance):
    assert isinstance(instance, iot2::Token)

@given(instance=iot2::Input_strategy)
@settings(max_examples=50)
def test_iot2::input_instantiation(instance):
    assert isinstance(instance, iot2::Input)

@given(instance=iot2::InputValue_strategy)
@settings(max_examples=50)
def test_iot2::inputvalue_instantiation(instance):
    assert isinstance(instance, iot2::InputValue)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=iot2::BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_iot2::booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, iot2::BooleanBinaryExpression)

@given(instance=iot2::BooleanBinaryExpression_strategy)
def test_iot2::booleanbinaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=iot2::BooleanBinaryExpression_strategy)
def test_iot2::booleanbinaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=iot2::BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_iot2::booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, iot2::BooleanUnaryExpression)

@given(instance=iot2::BooleanUnaryExpression_strategy)
def test_iot2::booleanunaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=iot2::BooleanUnaryExpression_strategy)
def test_iot2::booleanunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=iot2::OpaqueAction_strategy)
@settings(max_examples=50)
def test_iot2::opaqueaction_instantiation(instance):
    assert isinstance(instance, iot2::OpaqueAction)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=iot2::Action_strategy)
@settings(max_examples=50)
def test_iot2::action_instantiation(instance):
    assert isinstance(instance, iot2::Action)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=iot2::ExecutableNode_strategy)
@settings(max_examples=50)
def test_iot2::executablenode_instantiation(instance):
    assert isinstance(instance, iot2::ExecutableNode)

@given(instance=iot2::ControlNode_strategy)
@settings(max_examples=50)
def test_iot2::controlnode_instantiation(instance):
    assert isinstance(instance, iot2::ControlNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=iot2::ControlFlow_strategy)
@settings(max_examples=50)
def test_iot2::controlflow_instantiation(instance):
    assert isinstance(instance, iot2::ControlFlow)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=iot2::IntegerValue_strategy)
@settings(max_examples=50)
def test_iot2::integervalue_instantiation(instance):
    assert isinstance(instance, iot2::IntegerValue)

@given(instance=iot2::IntegerValue_strategy)
def test_iot2::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=iot2::IntegerValue_strategy)
def test_iot2::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iot2::BooleanValue_strategy)
@settings(max_examples=50)
def test_iot2::booleanvalue_instantiation(instance):
    assert isinstance(instance, iot2::BooleanValue)

@given(instance=iot2::BooleanValue_strategy)
def test_iot2::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=iot2::BooleanValue_strategy)
def test_iot2::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=iot2::BooleanVariable_strategy)
@settings(max_examples=50)
def test_iot2::booleanvariable_instantiation(instance):
    assert isinstance(instance, iot2::BooleanVariable)

@given(instance=iot2::IntegerVariable_strategy)
@settings(max_examples=50)
def test_iot2::integervariable_instantiation(instance):
    assert isinstance(instance, iot2::IntegerVariable)

@given(instance=iot2::Value_strategy)
@settings(max_examples=50)
def test_iot2::value_instantiation(instance):
    assert isinstance(instance, iot2::Value)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=iot2::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_iot2::activityfinalnode_instantiation(instance):
    assert isinstance(instance, iot2::ActivityFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=iot2::FinalNode_strategy)
@settings(max_examples=50)
def test_iot2::finalnode_instantiation(instance):
    assert isinstance(instance, iot2::FinalNode)

@given(instance=iot2::DecisionNode_strategy)
@settings(max_examples=50)
def test_iot2::decisionnode_instantiation(instance):
    assert isinstance(instance, iot2::DecisionNode)

@given(instance=iot2::ForkNode_strategy)
@settings(max_examples=50)
def test_iot2::forknode_instantiation(instance):
    assert isinstance(instance, iot2::ForkNode)

@given(instance=iot2::JoinNode_strategy)
@settings(max_examples=50)
def test_iot2::joinnode_instantiation(instance):
    assert isinstance(instance, iot2::JoinNode)

@given(instance=iot2::MergeNode_strategy)
@settings(max_examples=50)
def test_iot2::mergenode_instantiation(instance):
    assert isinstance(instance, iot2::MergeNode)

@given(instance=iot2::InitialNode_strategy)
@settings(max_examples=50)
def test_iot2::initialnode_instantiation(instance):
    assert isinstance(instance, iot2::InitialNode)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=iot2::Expression::Multiplication_strategy)
@settings(max_examples=50)
def test_iot2::expression::multiplication_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Multiplication)

@given(instance=iot2::Expression::Minus_strategy)
@settings(max_examples=50)
def test_iot2::expression::minus_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Minus)

@given(instance=iot2::Expression::Larger_strategy)
@settings(max_examples=50)
def test_iot2::expression::larger_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Larger)

@given(instance=iot2::IntegerExpression_strategy)
@settings(max_examples=50)
def test_iot2::integerexpression_instantiation(instance):
    assert isinstance(instance, iot2::IntegerExpression)

@given(instance=iot2::Expression::False_strategy)
@settings(max_examples=50)
def test_iot2::expression::false_instantiation(instance):
    assert isinstance(instance, iot2::Expression::False)

@given(instance=iot2::Expression::True_strategy)
@settings(max_examples=50)
def test_iot2::expression::true_instantiation(instance):
    assert isinstance(instance, iot2::Expression::True)

@given(instance=iot2::Expression::Negate_strategy)
@settings(max_examples=50)
def test_iot2::expression::negate_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Negate)

@given(instance=iot2::Expression::Larger::Equal_strategy)
@settings(max_examples=50)
def test_iot2::expression::larger::equal_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Larger::Equal)

@given(instance=iot2::Expression::Function_strategy)
@settings(max_examples=50)
def test_iot2::expression::function_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Function)

@given(instance=iot2::BooleanExpression_strategy)
@settings(max_examples=50)
def test_iot2::booleanexpression_instantiation(instance):
    assert isinstance(instance, iot2::BooleanExpression)

@given(instance=iot2::Expression::Number_strategy)
@settings(max_examples=50)
def test_iot2::expression::number_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Number)

@given(instance=iot2::Expression::Number_strategy)
def test_iot2::expression::number_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=iot2::Expression::Number_strategy)
def test_iot2::expression::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iot2::Expression::CallMemberFunction_strategy)
@settings(max_examples=50)
def test_iot2::expression::callmemberfunction_instantiation(instance):
    assert isinstance(instance, iot2::Expression::CallMemberFunction)

@given(instance=iot2::Expression::CallMemberFunction_strategy)
def test_iot2::expression::callmemberfunction_memberFunctionName_type(instance):
    assert isinstance(instance.memberFunctionName, str)


@given(instance=iot2::Expression::CallMemberFunction_strategy)
def test_iot2::expression::callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original

@given(instance=iot2::Expression::AccessArray_strategy)
@settings(max_examples=50)
def test_iot2::expression::accessarray_instantiation(instance):
    assert isinstance(instance, iot2::Expression::AccessArray)

@given(instance=iot2::Expression::VariableName_strategy)
@settings(max_examples=50)
def test_iot2::expression::variablename_instantiation(instance):
    assert isinstance(instance, iot2::Expression::VariableName)

@given(instance=iot2::Expression::VariableName_strategy)
def test_iot2::expression::variablename_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=iot2::Expression::VariableName_strategy)
def test_iot2::expression::variablename_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=iot2::Expression::Equal_strategy)
@settings(max_examples=50)
def test_iot2::expression::equal_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Equal)

@given(instance=iot2::Expression::Division_strategy)
@settings(max_examples=50)
def test_iot2::expression::division_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Division)

@given(instance=iot2::Expression::Smaller::Equal_strategy)
@settings(max_examples=50)
def test_iot2::expression::smaller::equal_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Smaller::Equal)

@given(instance=iot2::Expression::Not::Equal_strategy)
@settings(max_examples=50)
def test_iot2::expression::not::equal_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Not::Equal)

@given(instance=iot2::Expression::Or_strategy)
@settings(max_examples=50)
def test_iot2::expression::or_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Or)

@given(instance=iot2::Expression::AccessMember_strategy)
@settings(max_examples=50)
def test_iot2::expression::accessmember_instantiation(instance):
    assert isinstance(instance, iot2::Expression::AccessMember)

@given(instance=iot2::Expression::AccessMember_strategy)
def test_iot2::expression::accessmember_memberName_type(instance):
    assert isinstance(instance.memberName, str)


@given(instance=iot2::Expression::AccessMember_strategy)
def test_iot2::expression::accessmember_memberName_setter(instance):
    original = instance.memberName
    instance.memberName = original
    assert instance.memberName == original

@given(instance=iot2::Expression::Smaller_strategy)
@settings(max_examples=50)
def test_iot2::expression::smaller_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Smaller)

@given(instance=iot2::Expression::Exponentiation_strategy)
@settings(max_examples=50)
def test_iot2::expression::exponentiation_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Exponentiation)

@given(instance=iot2::Expression::Length_strategy)
@settings(max_examples=50)
def test_iot2::expression::length_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Length)

@given(instance=iot2::Expression::Concatenation_strategy)
@settings(max_examples=50)
def test_iot2::expression::concatenation_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Concatenation)

@given(instance=iot2::Expression::Modulo_strategy)
@settings(max_examples=50)
def test_iot2::expression::modulo_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Modulo)

@given(instance=iot2::Expression::VarArgs_strategy)
@settings(max_examples=50)
def test_iot2::expression::varargs_instantiation(instance):
    assert isinstance(instance, iot2::Expression::VarArgs)

@given(instance=iot2::Expression::And_strategy)
@settings(max_examples=50)
def test_iot2::expression::and_instantiation(instance):
    assert isinstance(instance, iot2::Expression::And)

@given(instance=iot2::Expression::Plus_strategy)
@settings(max_examples=50)
def test_iot2::expression::plus_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Plus)

@given(instance=iot2::Expression::String_strategy)
@settings(max_examples=50)
def test_iot2::expression::string_instantiation(instance):
    assert isinstance(instance, iot2::Expression::String)

@given(instance=iot2::Expression::String_strategy)
def test_iot2::expression::string_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iot2::Expression::String_strategy)
def test_iot2::expression::string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iot2::Expression::Invert_strategy)
@settings(max_examples=50)
def test_iot2::expression::invert_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Invert)

@given(instance=iot2::Expression::CallFunction_strategy)
@settings(max_examples=50)
def test_iot2::expression::callfunction_instantiation(instance):
    assert isinstance(instance, iot2::Expression::CallFunction)

@given(instance=iot2::Expression::Nil_strategy)
@settings(max_examples=50)
def test_iot2::expression::nil_instantiation(instance):
    assert isinstance(instance, iot2::Expression::Nil)

@given(instance=Statement::FunctioncallOrAssignment_strategy)
@settings(max_examples=50)
def test_statement::functioncallorassignment_instantiation(instance):
    assert isinstance(instance, Statement::FunctioncallOrAssignment)

@given(instance=iot2::Statement::CallFunction_strategy)
@settings(max_examples=50)
def test_iot2::statement::callfunction_instantiation(instance):
    assert isinstance(instance, iot2::Statement::CallFunction)

@given(instance=iot2::Statement::CallMemberFunction_strategy)
@settings(max_examples=50)
def test_iot2::statement::callmemberfunction_instantiation(instance):
    assert isinstance(instance, iot2::Statement::CallMemberFunction)

@given(instance=iot2::Statement::CallMemberFunction_strategy)
def test_iot2::statement::callmemberfunction_memberFunctionName_type(instance):
    assert isinstance(instance.memberFunctionName, str)


@given(instance=iot2::Statement::CallMemberFunction_strategy)
def test_iot2::statement::callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original

@given(instance=iot2::Statement::Assignment_strategy)
@settings(max_examples=50)
def test_iot2::statement::assignment_instantiation(instance):
    assert isinstance(instance, iot2::Statement::Assignment)

@given(instance=LastStatement::Return_strategy)
@settings(max_examples=50)
def test_laststatement::return_instantiation(instance):
    assert isinstance(instance, LastStatement::Return)

@given(instance=iot2::LastStatement::ReturnWithValue_strategy)
@settings(max_examples=50)
def test_iot2::laststatement::returnwithvalue_instantiation(instance):
    assert isinstance(instance, iot2::LastStatement::ReturnWithValue)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=iot2::Field::AppendEntryToTable_strategy)
@settings(max_examples=50)
def test_iot2::field::appendentrytotable_instantiation(instance):
    assert isinstance(instance, iot2::Field::AppendEntryToTable)

@given(instance=iot2::Field::AddEntryToTable_strategy)
@settings(max_examples=50)
def test_iot2::field::addentrytotable_instantiation(instance):
    assert isinstance(instance, iot2::Field::AddEntryToTable)

@given(instance=iot2::Field::AddEntryToTable_strategy)
def test_iot2::field::addentrytotable_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=iot2::Field::AddEntryToTable_strategy)
def test_iot2::field::addentrytotable_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=iot2::Field::AddEntryToTable::Brackets_strategy)
@settings(max_examples=50)
def test_iot2::field::addentrytotable::brackets_instantiation(instance):
    assert isinstance(instance, iot2::Field::AddEntryToTable::Brackets)

@given(instance=iot2::Functioncall::Arguments_strategy)
@settings(max_examples=50)
def test_iot2::functioncall::arguments_instantiation(instance):
    assert isinstance(instance, iot2::Functioncall::Arguments)

@given(instance=iot2::Expression::TableConstructor_strategy)
@settings(max_examples=50)
def test_iot2::expression::tableconstructor_instantiation(instance):
    assert isinstance(instance, iot2::Expression::TableConstructor)

@given(instance=iot2::Statement::If::Then::Else::ElseIfPart_strategy)
@settings(max_examples=50)
def test_iot2::statement::if::then::else::elseifpart_instantiation(instance):
    assert isinstance(instance, iot2::Statement::If::Then::Else::ElseIfPart)

@given(instance=iot2::Function_strategy)
@settings(max_examples=50)
def test_iot2::function_instantiation(instance):
    assert isinstance(instance, iot2::Function)

@given(instance=iot2::Function_strategy)
def test_iot2::function_varArgs_type(instance):
    assert isinstance(instance.varArgs, bool)


@given(instance=iot2::Function_strategy)
def test_iot2::function_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original

@given(instance=iot2::Function_strategy)
def test_iot2::function_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=iot2::Function_strategy)
def test_iot2::function_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=iot2::Expression_strategy)
@settings(max_examples=50)
def test_iot2::expression_instantiation(instance):
    assert isinstance(instance, iot2::Expression)

@given(instance=IDLType_strategy)
@settings(max_examples=50)
def test_idltype_instantiation(instance):
    assert isinstance(instance, IDLType)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=iot2::Statement::Local::Variable::Declaration_strategy)
@settings(max_examples=50)
def test_iot2::statement::local::variable::declaration_instantiation(instance):
    assert isinstance(instance, iot2::Statement::Local::Variable::Declaration)

@given(instance=iot2::Statement::Local::Variable::Declaration_strategy)
def test_iot2::statement::local::variable::declaration_variableNames_type(instance):
    assert isinstance(instance.variableNames, str)


@given(instance=iot2::Statement::Local::Variable::Declaration_strategy)
def test_iot2::statement::local::variable::declaration_variableNames_setter(instance):
    original = instance.variableNames
    instance.variableNames = original
    assert instance.variableNames == original

@given(instance=iot2::Statement::If::Then::Else_strategy)
@settings(max_examples=50)
def test_iot2::statement::if::then::else_instantiation(instance):
    assert isinstance(instance, iot2::Statement::If::Then::Else)

@given(instance=iot2::Statement::LocalFunction::Declaration_strategy)
@settings(max_examples=50)
def test_iot2::statement::localfunction::declaration_instantiation(instance):
    assert isinstance(instance, iot2::Statement::LocalFunction::Declaration)

@given(instance=iot2::Statement::LocalFunction::Declaration_strategy)
def test_iot2::statement::localfunction::declaration_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=iot2::Statement::LocalFunction::Declaration_strategy)
def test_iot2::statement::localfunction::declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=iot2::Statement::For::Numeric_strategy)
@settings(max_examples=50)
def test_iot2::statement::for::numeric_instantiation(instance):
    assert isinstance(instance, iot2::Statement::For::Numeric)

@given(instance=iot2::Statement::For::Numeric_strategy)
def test_iot2::statement::for::numeric_iteratorName_type(instance):
    assert isinstance(instance.iteratorName, str)


@given(instance=iot2::Statement::For::Numeric_strategy)
def test_iot2::statement::for::numeric_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original

@given(instance=iot2::Statement::FunctioncallOrAssignment_strategy)
@settings(max_examples=50)
def test_iot2::statement::functioncallorassignment_instantiation(instance):
    assert isinstance(instance, iot2::Statement::FunctioncallOrAssignment)

@given(instance=iot2::Statement::Repeat_strategy)
@settings(max_examples=50)
def test_iot2::statement::repeat_instantiation(instance):
    assert isinstance(instance, iot2::Statement::Repeat)

@given(instance=iot2::Statement::While_strategy)
@settings(max_examples=50)
def test_iot2::statement::while_instantiation(instance):
    assert isinstance(instance, iot2::Statement::While)

@given(instance=iot2::Statement::GlobalFunction::Declaration_strategy)
@settings(max_examples=50)
def test_iot2::statement::globalfunction::declaration_instantiation(instance):
    assert isinstance(instance, iot2::Statement::GlobalFunction::Declaration)

@given(instance=iot2::Statement::GlobalFunction::Declaration_strategy)
def test_iot2::statement::globalfunction::declaration_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=iot2::Statement::GlobalFunction::Declaration_strategy)
def test_iot2::statement::globalfunction::declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=iot2::Statement::GlobalFunction::Declaration_strategy)
def test_iot2::statement::globalfunction::declaration_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=iot2::Statement::GlobalFunction::Declaration_strategy)
def test_iot2::statement::globalfunction::declaration_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=iot2::Statement::For::Generic_strategy)
@settings(max_examples=50)
def test_iot2::statement::for::generic_instantiation(instance):
    assert isinstance(instance, iot2::Statement::For::Generic)

@given(instance=iot2::Statement::For::Generic_strategy)
def test_iot2::statement::for::generic_names_type(instance):
    assert isinstance(instance.names, str)


@given(instance=iot2::Statement::For::Generic_strategy)
def test_iot2::statement::for::generic_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=iot2::Statement::Block_strategy)
@settings(max_examples=50)
def test_iot2::statement::block_instantiation(instance):
    assert isinstance(instance, iot2::Statement::Block)

@given(instance=LastStatement_strategy)
@settings(max_examples=50)
def test_laststatement_instantiation(instance):
    assert isinstance(instance, LastStatement)

@given(instance=iot2::LastStatement::Break_strategy)
@settings(max_examples=50)
def test_iot2::laststatement::break_instantiation(instance):
    assert isinstance(instance, iot2::LastStatement::Break)

@given(instance=iot2::LastStatement::Return_strategy)
@settings(max_examples=50)
def test_iot2::laststatement::return_instantiation(instance):
    assert isinstance(instance, iot2::LastStatement::Return)

@given(instance=iot2::LastStatement_strategy)
@settings(max_examples=50)
def test_iot2::laststatement_instantiation(instance):
    assert isinstance(instance, iot2::LastStatement)

@given(instance=iot2::Statement_strategy)
@settings(max_examples=50)
def test_iot2::statement_instantiation(instance):
    assert isinstance(instance, iot2::Statement)

@given(instance=Chunk_strategy)
@settings(max_examples=50)
def test_chunk_instantiation(instance):
    assert isinstance(instance, Chunk)

@given(instance=iot2::Chunk_strategy)
@settings(max_examples=50)
def test_iot2::chunk_instantiation(instance):
    assert isinstance(instance, iot2::Chunk)

@given(instance=iot2::PrimitiveDef_strategy)
@settings(max_examples=50)
def test_iot2::primitivedef_instantiation(instance):
    assert isinstance(instance, iot2::PrimitiveDef)

@given(instance=iot2::PrimitiveDef_strategy)
def test_iot2::primitivedef_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=iot2::PrimitiveDef_strategy)
def test_iot2::primitivedef_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Typed_strategy)
@settings(max_examples=50)
def test_typed_instantiation(instance):
    assert isinstance(instance, Typed)

@given(instance=iot2::Field_strategy)
@settings(max_examples=50)
def test_iot2::field_instantiation(instance):
    assert isinstance(instance, iot2::Field)

@given(instance=iot2::Field_strategy)
def test_iot2::field_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=iot2::Field_strategy)
def test_iot2::field_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=iot2::ParameterDef_strategy)
@settings(max_examples=50)
def test_iot2::parameterdef_instantiation(instance):
    assert isinstance(instance, iot2::ParameterDef)

@given(instance=iot2::ParameterDef_strategy)
def test_iot2::parameterdef_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=iot2::ParameterDef_strategy)
def test_iot2::parameterdef_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=iot2::ParameterDef_strategy)
def test_iot2::parameterdef_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=iot2::ParameterDef_strategy)
def test_iot2::parameterdef_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=Contained_strategy)
@settings(max_examples=50)
def test_contained_instantiation(instance):
    assert isinstance(instance, Contained)

@given(instance=iot2::Variable_strategy)
@settings(max_examples=50)
def test_iot2::variable_instantiation(instance):
    assert isinstance(instance, iot2::Variable)

@given(instance=iot2::Variable_strategy)
def test_iot2::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot2::Variable_strategy)
def test_iot2::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=iot2::ActivityNode_strategy)
@settings(max_examples=50)
def test_iot2::activitynode_instantiation(instance):
    assert isinstance(instance, iot2::ActivityNode)

@given(instance=iot2::ActivityNode_strategy)
def test_iot2::activitynode_running_type(instance):
    assert isinstance(instance.running, bool)


@given(instance=iot2::ActivityNode_strategy)
def test_iot2::activitynode_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original

@given(instance=iot2::ActivityEdge_strategy)
@settings(max_examples=50)
def test_iot2::activityedge_instantiation(instance):
    assert isinstance(instance, iot2::ActivityEdge)

@given(instance=iot2::TypedefDef_strategy)
@settings(max_examples=50)
def test_iot2::typedefdef_instantiation(instance):
    assert isinstance(instance, iot2::TypedefDef)

@given(instance=iot2::IDLType_strategy)
@settings(max_examples=50)
def test_iot2::idltype_instantiation(instance):
    assert isinstance(instance, iot2::IDLType)

@given(instance=iot2::IDLType_strategy)
def test_iot2::idltype_typeCode_type(instance):
    assert isinstance(instance.typeCode, str)


@given(instance=iot2::IDLType_strategy)
def test_iot2::idltype_typeCode_setter(instance):
    original = instance.typeCode
    instance.typeCode = original
    assert instance.typeCode == original

@given(instance=iot2::Typed_strategy)
@settings(max_examples=50)
def test_iot2::typed_instantiation(instance):
    assert isinstance(instance, iot2::Typed)

@given(instance=iot2::NamedElement_strategy)
@settings(max_examples=50)
def test_iot2::namedelement_instantiation(instance):
    assert isinstance(instance, iot2::NamedElement)

@given(instance=iot2::NamedElement_strategy)
def test_iot2::namedelement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=iot2::NamedElement_strategy)
def test_iot2::namedelement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=iot2::NamedElement_strategy)
def test_iot2::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot2::NamedElement_strategy)
def test_iot2::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2::Container_strategy)
@settings(max_examples=50)
def test_iot2::container_instantiation(instance):
    assert isinstance(instance, iot2::Container)

@given(instance=iot2::Contained_strategy)
@settings(max_examples=50)
def test_iot2::contained_instantiation(instance):
    assert isinstance(instance, iot2::Contained)

@given(instance=iot2::Contained_strategy)
def test_iot2::contained_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=iot2::Contained_strategy)
def test_iot2::contained_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=iot2::Contained_strategy)
def test_iot2::contained_absoluteName_type(instance):
    assert isinstance(instance.absoluteName, str)


@given(instance=iot2::Contained_strategy)
def test_iot2::contained_absoluteName_setter(instance):
    original = instance.absoluteName
    instance.absoluteName = original
    assert instance.absoluteName == original

@given(instance=iot2::Contained_strategy)
def test_iot2::contained_repositoryId_type(instance):
    assert isinstance(instance.repositoryId, str)


@given(instance=iot2::Contained_strategy)
def test_iot2::contained_repositoryId_setter(instance):
    original = instance.repositoryId
    instance.repositoryId = original
    assert instance.repositoryId == original

@given(instance=iot2::Block_strategy)
@settings(max_examples=50)
def test_iot2::block_instantiation(instance):
    assert isinstance(instance, iot2::Block)

@given(instance=iot2::ExceptionDef_strategy)
@settings(max_examples=50)
def test_iot2::exceptiondef_instantiation(instance):
    assert isinstance(instance, iot2::ExceptionDef)

@given(instance=iot2::ExceptionDef_strategy)
def test_iot2::exceptiondef_typeCode_type(instance):
    assert isinstance(instance.typeCode, str)


@given(instance=iot2::ExceptionDef_strategy)
def test_iot2::exceptiondef_typeCode_setter(instance):
    original = instance.typeCode
    instance.typeCode = original
    assert instance.typeCode == original

@given(instance=HWComponent_strategy)
@settings(max_examples=50)
def test_hwcomponent_instantiation(instance):
    assert isinstance(instance, HWComponent)

@given(instance=iot2::Actuator_strategy)
@settings(max_examples=50)
def test_iot2::actuator_instantiation(instance):
    assert isinstance(instance, iot2::Actuator)

@given(instance=iot2::Sensor_strategy)
@settings(max_examples=50)
def test_iot2::sensor_instantiation(instance):
    assert isinstance(instance, iot2::Sensor)

@given(instance=iot2::OperationDef_strategy)
@settings(max_examples=50)
def test_iot2::operationdef_instantiation(instance):
    assert isinstance(instance, iot2::OperationDef)

@given(instance=iot2::OperationDef_strategy)
def test_iot2::operationdef_isOneway_type(instance):
    assert isinstance(instance.isOneway, bool)


@given(instance=iot2::OperationDef_strategy)
def test_iot2::operationdef_isOneway_setter(instance):
    original = instance.isOneway
    instance.isOneway = original
    assert instance.isOneway == original

@given(instance=iot2::OperationDef_strategy)
def test_iot2::operationdef_contexts_type(instance):
    assert isinstance(instance.contexts, str)


@given(instance=iot2::OperationDef_strategy)
def test_iot2::operationdef_contexts_setter(instance):
    original = instance.contexts
    instance.contexts = original
    assert instance.contexts == original

@given(instance=iot2::Activity_strategy)
@settings(max_examples=50)
def test_iot2::activity_instantiation(instance):
    assert isinstance(instance, iot2::Activity)

@given(instance=iot2::Sketch_strategy)
@settings(max_examples=50)
def test_iot2::sketch_instantiation(instance):
    assert isinstance(instance, iot2::Sketch)

@given(instance=iot2::Board_strategy)
@settings(max_examples=50)
def test_iot2::board_instantiation(instance):
    assert isinstance(instance, iot2::Board)

@given(instance=iot2::Board_strategy)
def test_iot2::board_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=iot2::Board_strategy)
def test_iot2::board_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=iot2::Board_strategy)
def test_iot2::board_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot2::Board_strategy)
def test_iot2::board_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2::HWComponent_strategy)
@settings(max_examples=50)
def test_iot2::hwcomponent_instantiation(instance):
    assert isinstance(instance, iot2::HWComponent)

@given(instance=iot2::HWComponent_strategy)
def test_iot2::hwcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot2::HWComponent_strategy)
def test_iot2::hwcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iot2::System_strategy)
@settings(max_examples=50)
def test_iot2::system_instantiation(instance):
    assert isinstance(instance, iot2::System)

@given(instance=iot2::System_strategy)
def test_iot2::system_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iot2::System_strategy)
def test_iot2::system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
