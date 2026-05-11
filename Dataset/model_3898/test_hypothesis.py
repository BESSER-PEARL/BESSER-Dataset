import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedFunction,
    behaviour::UnaryFunction,
    behaviour::BinaryFunction,
    Duration,
    behaviour::MonthDuration,
    behaviour::NumericPrimitive,
    TimeExpression,
    behaviour::While,
    LocationExpression,
    behaviour::CoordinateLocationExpression,
    behaviour::NameLocationExpression,
    BinaryBooleanFunction,
    behaviour::ComparisonBooleanFunction,
    BinaryFunction,
    behaviour::BinaryArithmeticFunction,
    behaviour::BinaryLocationFunction,
    behaviour::BinaryBooleanFunction,
    UnaryFunction,
    behaviour::UnaryNumericFunction,
    behaviour::UnaryLocationFunction,
    behaviour::UnaryEntityFunction,
    behaviour::UnaryStringFunction,
    Edge,
    behaviour::FalseEdge,
    behaviour::TrueEdge,
    behaviour::UnconditionedEdge,
    PrimitiveActivity,
    behaviour::Remove,
    behaviour::Add,
    behaviour::Die,
    behaviour::Reproduce,
    behaviour::Move,
    ControlNode,
    behaviour::Decision,
    behaviour::Merge,
    behaviour::Fork,
    behaviour::Join,
    behaviour::TimeExpression,
    Node,
    behaviour::ExecutableNode,
    behaviour::ControlNode,
    behaviour::LogicBooleanFunction,
    behaviour::OccupationBooleanFunction,
    behaviour::Behavior,
    behaviour::EntityClass,
    Function,
    behaviour::NamedFunction,
    behaviour::AnonymousFunction,
    behaviour::Node,
    behaviour::Edge,
    behaviour::End,
    behaviour::Start,
    ExecutableNode,
    behaviour::PrimitiveActivity,
    behaviour::Equation,
    Behavior,
    behaviour::ActivityDiagramBehavior,
    behaviour::EquationBehaviour,
    behaviour::Duration,
    VariableClass,
    behaviour::ParameterClass,
    behaviour::AttributeClass,
    behaviour::Type,
    PrimitiveExpression,
    behaviour::BooleanPrimitive,
    behaviour::LocationPrimitive,
    behaviour::EntitySetPrimitive,
    behaviour::LocationSetPrimitive,
    behaviour::EntityPrimive,
    ConstantExpression,
    behaviour::FloatConstantExpression,
    behaviour::StringConstantExpression,
    behaviour::IntConstantExpression,
    behaviour::Function,
    Expression,
    behaviour::PrimitiveExpression,
    behaviour::FunctionCallExpression,
    behaviour::LocationExpression,
    behaviour::ConstantExpression,
    behaviour::VariableClass,
    behaviour::Expression,
    UnaryLocationEnum,
    WeekDaysEnum,
    TypeEnum,
    UnaryNumericFunctionEnum,
    DurationTypeEnum,
    OccupationBooleanFunctionEnum,
    ArithmeticFunctionEnum,
    UnaryLocationFunctionEnum,
    LogicBooleanFunctionEnum,
    LocationSetPrimiveEnum,
    EntityPrimitiveEnum,
    LocationPrimiveEnum,
    MonthsEnum,
    ComparisonBooleanFunctionEnum,
    UnaryStringFunctionEnum,
    BooleanPrimitiveEnum,
    EntitySetPrimiveEnum,
    UnaryEntityFunctionEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedfunction_is_not_abstract():
    assert not inspect.isabstract(NamedFunction)


def test_namedfunction_constructor_exists():
    assert callable(NamedFunction.__init__)


def test_namedfunction_constructor_args():
    sig = inspect.signature(NamedFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::unaryfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::UnaryFunction)


def test_behaviour::unaryfunction_constructor_exists():
    assert callable(behaviour::UnaryFunction.__init__)


def test_behaviour::unaryfunction_constructor_args():
    sig = inspect.signature(behaviour::UnaryFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::binaryfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::BinaryFunction)


def test_behaviour::binaryfunction_constructor_exists():
    assert callable(behaviour::BinaryFunction.__init__)


def test_behaviour::binaryfunction_constructor_args():
    sig = inspect.signature(behaviour::BinaryFunction.__init__)
    params = list(sig.parameters.keys())



def test_duration_is_not_abstract():
    assert not inspect.isabstract(Duration)


def test_duration_constructor_exists():
    assert callable(Duration.__init__)


def test_duration_constructor_args():
    sig = inspect.signature(Duration.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::monthduration_is_not_abstract():
    assert not inspect.isabstract(behaviour::MonthDuration)


def test_behaviour::monthduration_constructor_exists():
    assert callable(behaviour::MonthDuration.__init__)


def test_behaviour::monthduration_constructor_args():
    sig = inspect.signature(behaviour::MonthDuration.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"

def test_behaviour::monthduration_has_month():
    assert hasattr(behaviour::MonthDuration, "month")
    descriptor = None
    for klass in behaviour::MonthDuration.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::numericprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour::NumericPrimitive)


def test_behaviour::numericprimitive_constructor_exists():
    assert callable(behaviour::NumericPrimitive.__init__)


def test_behaviour::numericprimitive_constructor_args():
    sig = inspect.signature(behaviour::NumericPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_timeexpression_is_not_abstract():
    assert not inspect.isabstract(TimeExpression)


def test_timeexpression_constructor_exists():
    assert callable(TimeExpression.__init__)


def test_timeexpression_constructor_args():
    sig = inspect.signature(TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::while_is_not_abstract():
    assert not inspect.isabstract(behaviour::While)


def test_behaviour::while_constructor_exists():
    assert callable(behaviour::While.__init__)


def test_behaviour::while_constructor_args():
    sig = inspect.signature(behaviour::While.__init__)
    params = list(sig.parameters.keys())



def test_locationexpression_is_not_abstract():
    assert not inspect.isabstract(LocationExpression)


def test_locationexpression_constructor_exists():
    assert callable(LocationExpression.__init__)


def test_locationexpression_constructor_args():
    sig = inspect.signature(LocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::coordinatelocationexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::CoordinateLocationExpression)


def test_behaviour::coordinatelocationexpression_constructor_exists():
    assert callable(behaviour::CoordinateLocationExpression.__init__)


def test_behaviour::coordinatelocationexpression_constructor_args():
    sig = inspect.signature(behaviour::CoordinateLocationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_behaviour::coordinatelocationexpression_has_y():
    assert hasattr(behaviour::CoordinateLocationExpression, "y")
    descriptor = None
    for klass in behaviour::CoordinateLocationExpression.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::coordinatelocationexpression_has_x():
    assert hasattr(behaviour::CoordinateLocationExpression, "x")
    descriptor = None
    for klass in behaviour::CoordinateLocationExpression.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::namelocationexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::NameLocationExpression)


def test_behaviour::namelocationexpression_constructor_exists():
    assert callable(behaviour::NameLocationExpression.__init__)


def test_behaviour::namelocationexpression_constructor_args():
    sig = inspect.signature(behaviour::NameLocationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behaviour::namelocationexpression_has_name():
    assert hasattr(behaviour::NameLocationExpression, "name")
    descriptor = None
    for klass in behaviour::NameLocationExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_binarybooleanfunction_is_not_abstract():
    assert not inspect.isabstract(BinaryBooleanFunction)


def test_binarybooleanfunction_constructor_exists():
    assert callable(BinaryBooleanFunction.__init__)


def test_binarybooleanfunction_constructor_args():
    sig = inspect.signature(BinaryBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::comparisonbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::ComparisonBooleanFunction)


def test_behaviour::comparisonbooleanfunction_constructor_exists():
    assert callable(behaviour::ComparisonBooleanFunction.__init__)


def test_behaviour::comparisonbooleanfunction_constructor_args():
    sig = inspect.signature(behaviour::ComparisonBooleanFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour::comparisonbooleanfunction_has_functionName():
    assert hasattr(behaviour::ComparisonBooleanFunction, "functionName")
    descriptor = None
    for klass in behaviour::ComparisonBooleanFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_binaryfunction_is_not_abstract():
    assert not inspect.isabstract(BinaryFunction)


def test_binaryfunction_constructor_exists():
    assert callable(BinaryFunction.__init__)


def test_binaryfunction_constructor_args():
    sig = inspect.signature(BinaryFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::binaryarithmeticfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::BinaryArithmeticFunction)


def test_behaviour::binaryarithmeticfunction_constructor_exists():
    assert callable(behaviour::BinaryArithmeticFunction.__init__)


def test_behaviour::binaryarithmeticfunction_constructor_args():
    sig = inspect.signature(behaviour::BinaryArithmeticFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour::binaryarithmeticfunction_has_functionName():
    assert hasattr(behaviour::BinaryArithmeticFunction, "functionName")
    descriptor = None
    for klass in behaviour::BinaryArithmeticFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::binarylocationfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::BinaryLocationFunction)


def test_behaviour::binarylocationfunction_constructor_exists():
    assert callable(behaviour::BinaryLocationFunction.__init__)


def test_behaviour::binarylocationfunction_constructor_args():
    sig = inspect.signature(behaviour::BinaryLocationFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::binarybooleanfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::BinaryBooleanFunction)


def test_behaviour::binarybooleanfunction_constructor_exists():
    assert callable(behaviour::BinaryBooleanFunction.__init__)


def test_behaviour::binarybooleanfunction_constructor_args():
    sig = inspect.signature(behaviour::BinaryBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_unaryfunction_is_not_abstract():
    assert not inspect.isabstract(UnaryFunction)


def test_unaryfunction_constructor_exists():
    assert callable(UnaryFunction.__init__)


def test_unaryfunction_constructor_args():
    sig = inspect.signature(UnaryFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::unarynumericfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::UnaryNumericFunction)


def test_behaviour::unarynumericfunction_constructor_exists():
    assert callable(behaviour::UnaryNumericFunction.__init__)


def test_behaviour::unarynumericfunction_constructor_args():
    sig = inspect.signature(behaviour::UnaryNumericFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour::unarynumericfunction_has_functionName():
    assert hasattr(behaviour::UnaryNumericFunction, "functionName")
    descriptor = None
    for klass in behaviour::UnaryNumericFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::unarylocationfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::UnaryLocationFunction)


def test_behaviour::unarylocationfunction_constructor_exists():
    assert callable(behaviour::UnaryLocationFunction.__init__)


def test_behaviour::unarylocationfunction_constructor_args():
    sig = inspect.signature(behaviour::UnaryLocationFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour::unarylocationfunction_has_functionName():
    assert hasattr(behaviour::UnaryLocationFunction, "functionName")
    descriptor = None
    for klass in behaviour::UnaryLocationFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::unaryentityfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::UnaryEntityFunction)


def test_behaviour::unaryentityfunction_constructor_exists():
    assert callable(behaviour::UnaryEntityFunction.__init__)


def test_behaviour::unaryentityfunction_constructor_args():
    sig = inspect.signature(behaviour::UnaryEntityFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour::unaryentityfunction_has_functionName():
    assert hasattr(behaviour::UnaryEntityFunction, "functionName")
    descriptor = None
    for klass in behaviour::UnaryEntityFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::unarystringfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::UnaryStringFunction)


def test_behaviour::unarystringfunction_constructor_exists():
    assert callable(behaviour::UnaryStringFunction.__init__)


def test_behaviour::unarystringfunction_constructor_args():
    sig = inspect.signature(behaviour::UnaryStringFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour::unarystringfunction_has_functionName():
    assert hasattr(behaviour::UnaryStringFunction, "functionName")
    descriptor = None
    for klass in behaviour::UnaryStringFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::falseedge_is_not_abstract():
    assert not inspect.isabstract(behaviour::FalseEdge)


def test_behaviour::falseedge_constructor_exists():
    assert callable(behaviour::FalseEdge.__init__)


def test_behaviour::falseedge_constructor_args():
    sig = inspect.signature(behaviour::FalseEdge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::trueedge_is_not_abstract():
    assert not inspect.isabstract(behaviour::TrueEdge)


def test_behaviour::trueedge_constructor_exists():
    assert callable(behaviour::TrueEdge.__init__)


def test_behaviour::trueedge_constructor_args():
    sig = inspect.signature(behaviour::TrueEdge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::unconditionededge_is_not_abstract():
    assert not inspect.isabstract(behaviour::UnconditionedEdge)


def test_behaviour::unconditionededge_constructor_exists():
    assert callable(behaviour::UnconditionedEdge.__init__)


def test_behaviour::unconditionededge_constructor_args():
    sig = inspect.signature(behaviour::UnconditionedEdge.__init__)
    params = list(sig.parameters.keys())



def test_primitiveactivity_is_not_abstract():
    assert not inspect.isabstract(PrimitiveActivity)


def test_primitiveactivity_constructor_exists():
    assert callable(PrimitiveActivity.__init__)


def test_primitiveactivity_constructor_args():
    sig = inspect.signature(PrimitiveActivity.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::remove_is_not_abstract():
    assert not inspect.isabstract(behaviour::Remove)


def test_behaviour::remove_constructor_exists():
    assert callable(behaviour::Remove.__init__)


def test_behaviour::remove_constructor_args():
    sig = inspect.signature(behaviour::Remove.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::add_is_not_abstract():
    assert not inspect.isabstract(behaviour::Add)


def test_behaviour::add_constructor_exists():
    assert callable(behaviour::Add.__init__)


def test_behaviour::add_constructor_args():
    sig = inspect.signature(behaviour::Add.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::die_is_not_abstract():
    assert not inspect.isabstract(behaviour::Die)


def test_behaviour::die_constructor_exists():
    assert callable(behaviour::Die.__init__)


def test_behaviour::die_constructor_args():
    sig = inspect.signature(behaviour::Die.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::reproduce_is_not_abstract():
    assert not inspect.isabstract(behaviour::Reproduce)


def test_behaviour::reproduce_constructor_exists():
    assert callable(behaviour::Reproduce.__init__)


def test_behaviour::reproduce_constructor_args():
    sig = inspect.signature(behaviour::Reproduce.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::move_is_not_abstract():
    assert not inspect.isabstract(behaviour::Move)


def test_behaviour::move_constructor_exists():
    assert callable(behaviour::Move.__init__)


def test_behaviour::move_constructor_args():
    sig = inspect.signature(behaviour::Move.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::decision_is_not_abstract():
    assert not inspect.isabstract(behaviour::Decision)


def test_behaviour::decision_constructor_exists():
    assert callable(behaviour::Decision.__init__)


def test_behaviour::decision_constructor_args():
    sig = inspect.signature(behaviour::Decision.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::merge_is_not_abstract():
    assert not inspect.isabstract(behaviour::Merge)


def test_behaviour::merge_constructor_exists():
    assert callable(behaviour::Merge.__init__)


def test_behaviour::merge_constructor_args():
    sig = inspect.signature(behaviour::Merge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::fork_is_not_abstract():
    assert not inspect.isabstract(behaviour::Fork)


def test_behaviour::fork_constructor_exists():
    assert callable(behaviour::Fork.__init__)


def test_behaviour::fork_constructor_args():
    sig = inspect.signature(behaviour::Fork.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::join_is_not_abstract():
    assert not inspect.isabstract(behaviour::Join)


def test_behaviour::join_constructor_exists():
    assert callable(behaviour::Join.__init__)


def test_behaviour::join_constructor_args():
    sig = inspect.signature(behaviour::Join.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::timeexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::TimeExpression)


def test_behaviour::timeexpression_constructor_exists():
    assert callable(behaviour::TimeExpression.__init__)


def test_behaviour::timeexpression_constructor_args():
    sig = inspect.signature(behaviour::TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::executablenode_is_not_abstract():
    assert not inspect.isabstract(behaviour::ExecutableNode)


def test_behaviour::executablenode_constructor_exists():
    assert callable(behaviour::ExecutableNode.__init__)


def test_behaviour::executablenode_constructor_args():
    sig = inspect.signature(behaviour::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::controlnode_is_not_abstract():
    assert not inspect.isabstract(behaviour::ControlNode)


def test_behaviour::controlnode_constructor_exists():
    assert callable(behaviour::ControlNode.__init__)


def test_behaviour::controlnode_constructor_args():
    sig = inspect.signature(behaviour::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::logicbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::LogicBooleanFunction)


def test_behaviour::logicbooleanfunction_constructor_exists():
    assert callable(behaviour::LogicBooleanFunction.__init__)


def test_behaviour::logicbooleanfunction_constructor_args():
    sig = inspect.signature(behaviour::LogicBooleanFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour::logicbooleanfunction_has_functionName():
    assert hasattr(behaviour::LogicBooleanFunction, "functionName")
    descriptor = None
    for klass in behaviour::LogicBooleanFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::occupationbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::OccupationBooleanFunction)


def test_behaviour::occupationbooleanfunction_constructor_exists():
    assert callable(behaviour::OccupationBooleanFunction.__init__)


def test_behaviour::occupationbooleanfunction_constructor_args():
    sig = inspect.signature(behaviour::OccupationBooleanFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour::occupationbooleanfunction_has_functionName():
    assert hasattr(behaviour::OccupationBooleanFunction, "functionName")
    descriptor = None
    for klass in behaviour::OccupationBooleanFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::behavior_is_not_abstract():
    assert not inspect.isabstract(behaviour::Behavior)


def test_behaviour::behavior_constructor_exists():
    assert callable(behaviour::Behavior.__init__)


def test_behaviour::behavior_constructor_args():
    sig = inspect.signature(behaviour::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_behaviour::behavior_has_behaviorName():
    assert hasattr(behaviour::Behavior, "behaviorName")
    descriptor = None
    for klass in behaviour::Behavior.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::behavior_has_frequency():
    assert hasattr(behaviour::Behavior, "frequency")
    descriptor = None
    for klass in behaviour::Behavior.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::entityclass_is_not_abstract():
    assert not inspect.isabstract(behaviour::EntityClass)


def test_behaviour::entityclass_constructor_exists():
    assert callable(behaviour::EntityClass.__init__)


def test_behaviour::entityclass_constructor_args():
    sig = inspect.signature(behaviour::EntityClass.__init__)
    params = list(sig.parameters.keys())
    assert "entityName" in params, "Missing parameter 'entityName'"

def test_behaviour::entityclass_has_entityName():
    assert hasattr(behaviour::EntityClass, "entityName")
    descriptor = None
    for klass in behaviour::EntityClass.__mro__:
        if "entityName" in klass.__dict__:
            descriptor = klass.__dict__["entityName"]
            break
    assert isinstance(descriptor, property)



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::namedfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::NamedFunction)


def test_behaviour::namedfunction_constructor_exists():
    assert callable(behaviour::NamedFunction.__init__)


def test_behaviour::namedfunction_constructor_args():
    sig = inspect.signature(behaviour::NamedFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::anonymousfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour::AnonymousFunction)


def test_behaviour::anonymousfunction_constructor_exists():
    assert callable(behaviour::AnonymousFunction.__init__)


def test_behaviour::anonymousfunction_constructor_args():
    sig = inspect.signature(behaviour::AnonymousFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::node_is_not_abstract():
    assert not inspect.isabstract(behaviour::Node)


def test_behaviour::node_constructor_exists():
    assert callable(behaviour::Node.__init__)


def test_behaviour::node_constructor_args():
    sig = inspect.signature(behaviour::Node.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::edge_is_not_abstract():
    assert not inspect.isabstract(behaviour::Edge)


def test_behaviour::edge_constructor_exists():
    assert callable(behaviour::Edge.__init__)


def test_behaviour::edge_constructor_args():
    sig = inspect.signature(behaviour::Edge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::end_is_not_abstract():
    assert not inspect.isabstract(behaviour::End)


def test_behaviour::end_constructor_exists():
    assert callable(behaviour::End.__init__)


def test_behaviour::end_constructor_args():
    sig = inspect.signature(behaviour::End.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::start_is_not_abstract():
    assert not inspect.isabstract(behaviour::Start)


def test_behaviour::start_constructor_exists():
    assert callable(behaviour::Start.__init__)


def test_behaviour::start_constructor_args():
    sig = inspect.signature(behaviour::Start.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::primitiveactivity_is_not_abstract():
    assert not inspect.isabstract(behaviour::PrimitiveActivity)


def test_behaviour::primitiveactivity_constructor_exists():
    assert callable(behaviour::PrimitiveActivity.__init__)


def test_behaviour::primitiveactivity_constructor_args():
    sig = inspect.signature(behaviour::PrimitiveActivity.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::equation_is_not_abstract():
    assert not inspect.isabstract(behaviour::Equation)


def test_behaviour::equation_constructor_exists():
    assert callable(behaviour::Equation.__init__)


def test_behaviour::equation_constructor_args():
    sig = inspect.signature(behaviour::Equation.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::activitydiagrambehavior_is_not_abstract():
    assert not inspect.isabstract(behaviour::ActivityDiagramBehavior)


def test_behaviour::activitydiagrambehavior_constructor_exists():
    assert callable(behaviour::ActivityDiagramBehavior.__init__)


def test_behaviour::activitydiagrambehavior_constructor_args():
    sig = inspect.signature(behaviour::ActivityDiagramBehavior.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::equationbehaviour_is_not_abstract():
    assert not inspect.isabstract(behaviour::EquationBehaviour)


def test_behaviour::equationbehaviour_constructor_exists():
    assert callable(behaviour::EquationBehaviour.__init__)


def test_behaviour::equationbehaviour_constructor_args():
    sig = inspect.signature(behaviour::EquationBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::duration_is_not_abstract():
    assert not inspect.isabstract(behaviour::Duration)


def test_behaviour::duration_constructor_exists():
    assert callable(behaviour::Duration.__init__)


def test_behaviour::duration_constructor_args():
    sig = inspect.signature(behaviour::Duration.__init__)
    params = list(sig.parameters.keys())
    assert "durationTime" in params, "Missing parameter 'durationTime'"

def test_behaviour::duration_has_durationTime():
    assert hasattr(behaviour::Duration, "durationTime")
    descriptor = None
    for klass in behaviour::Duration.__mro__:
        if "durationTime" in klass.__dict__:
            descriptor = klass.__dict__["durationTime"]
            break
    assert isinstance(descriptor, property)



def test_variableclass_is_not_abstract():
    assert not inspect.isabstract(VariableClass)


def test_variableclass_constructor_exists():
    assert callable(VariableClass.__init__)


def test_variableclass_constructor_args():
    sig = inspect.signature(VariableClass.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::parameterclass_is_not_abstract():
    assert not inspect.isabstract(behaviour::ParameterClass)


def test_behaviour::parameterclass_constructor_exists():
    assert callable(behaviour::ParameterClass.__init__)


def test_behaviour::parameterclass_constructor_args():
    sig = inspect.signature(behaviour::ParameterClass.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::attributeclass_is_not_abstract():
    assert not inspect.isabstract(behaviour::AttributeClass)


def test_behaviour::attributeclass_constructor_exists():
    assert callable(behaviour::AttributeClass.__init__)


def test_behaviour::attributeclass_constructor_args():
    sig = inspect.signature(behaviour::AttributeClass.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::type_is_not_abstract():
    assert not inspect.isabstract(behaviour::Type)


def test_behaviour::type_constructor_exists():
    assert callable(behaviour::Type.__init__)


def test_behaviour::type_constructor_args():
    sig = inspect.signature(behaviour::Type.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_behaviour::type_has_type():
    assert hasattr(behaviour::Type, "type")
    descriptor = None
    for klass in behaviour::Type.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::booleanprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour::BooleanPrimitive)


def test_behaviour::booleanprimitive_constructor_exists():
    assert callable(behaviour::BooleanPrimitive.__init__)


def test_behaviour::booleanprimitive_constructor_args():
    sig = inspect.signature(behaviour::BooleanPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour::booleanprimitive_has_primitive():
    assert hasattr(behaviour::BooleanPrimitive, "primitive")
    descriptor = None
    for klass in behaviour::BooleanPrimitive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::locationprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour::LocationPrimitive)


def test_behaviour::locationprimitive_constructor_exists():
    assert callable(behaviour::LocationPrimitive.__init__)


def test_behaviour::locationprimitive_constructor_args():
    sig = inspect.signature(behaviour::LocationPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour::locationprimitive_has_primitive():
    assert hasattr(behaviour::LocationPrimitive, "primitive")
    descriptor = None
    for klass in behaviour::LocationPrimitive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::entitysetprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour::EntitySetPrimitive)


def test_behaviour::entitysetprimitive_constructor_exists():
    assert callable(behaviour::EntitySetPrimitive.__init__)


def test_behaviour::entitysetprimitive_constructor_args():
    sig = inspect.signature(behaviour::EntitySetPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour::entitysetprimitive_has_primitive():
    assert hasattr(behaviour::EntitySetPrimitive, "primitive")
    descriptor = None
    for klass in behaviour::EntitySetPrimitive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::locationsetprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour::LocationSetPrimitive)


def test_behaviour::locationsetprimitive_constructor_exists():
    assert callable(behaviour::LocationSetPrimitive.__init__)


def test_behaviour::locationsetprimitive_constructor_args():
    sig = inspect.signature(behaviour::LocationSetPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour::locationsetprimitive_has_primitive():
    assert hasattr(behaviour::LocationSetPrimitive, "primitive")
    descriptor = None
    for klass in behaviour::LocationSetPrimitive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::entityprimive_is_not_abstract():
    assert not inspect.isabstract(behaviour::EntityPrimive)


def test_behaviour::entityprimive_constructor_exists():
    assert callable(behaviour::EntityPrimive.__init__)


def test_behaviour::entityprimive_constructor_args():
    sig = inspect.signature(behaviour::EntityPrimive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour::entityprimive_has_primitive():
    assert hasattr(behaviour::EntityPrimive, "primitive")
    descriptor = None
    for klass in behaviour::EntityPrimive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_constantexpression_is_not_abstract():
    assert not inspect.isabstract(ConstantExpression)


def test_constantexpression_constructor_exists():
    assert callable(ConstantExpression.__init__)


def test_constantexpression_constructor_args():
    sig = inspect.signature(ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::floatconstantexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::FloatConstantExpression)


def test_behaviour::floatconstantexpression_constructor_exists():
    assert callable(behaviour::FloatConstantExpression.__init__)


def test_behaviour::floatconstantexpression_constructor_args():
    sig = inspect.signature(behaviour::FloatConstantExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_behaviour::floatconstantexpression_has_value():
    assert hasattr(behaviour::FloatConstantExpression, "value")
    descriptor = None
    for klass in behaviour::FloatConstantExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::stringconstantexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::StringConstantExpression)


def test_behaviour::stringconstantexpression_constructor_exists():
    assert callable(behaviour::StringConstantExpression.__init__)


def test_behaviour::stringconstantexpression_constructor_args():
    sig = inspect.signature(behaviour::StringConstantExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_behaviour::stringconstantexpression_has_value():
    assert hasattr(behaviour::StringConstantExpression, "value")
    descriptor = None
    for klass in behaviour::StringConstantExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::intconstantexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::IntConstantExpression)


def test_behaviour::intconstantexpression_constructor_exists():
    assert callable(behaviour::IntConstantExpression.__init__)


def test_behaviour::intconstantexpression_constructor_args():
    sig = inspect.signature(behaviour::IntConstantExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_behaviour::intconstantexpression_has_value():
    assert hasattr(behaviour::IntConstantExpression, "value")
    descriptor = None
    for klass in behaviour::IntConstantExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::function_is_not_abstract():
    assert not inspect.isabstract(behaviour::Function)


def test_behaviour::function_constructor_exists():
    assert callable(behaviour::Function.__init__)


def test_behaviour::function_constructor_args():
    sig = inspect.signature(behaviour::Function.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::PrimitiveExpression)


def test_behaviour::primitiveexpression_constructor_exists():
    assert callable(behaviour::PrimitiveExpression.__init__)


def test_behaviour::primitiveexpression_constructor_args():
    sig = inspect.signature(behaviour::PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::FunctionCallExpression)


def test_behaviour::functioncallexpression_constructor_exists():
    assert callable(behaviour::FunctionCallExpression.__init__)


def test_behaviour::functioncallexpression_constructor_args():
    sig = inspect.signature(behaviour::FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::locationexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::LocationExpression)


def test_behaviour::locationexpression_constructor_exists():
    assert callable(behaviour::LocationExpression.__init__)


def test_behaviour::locationexpression_constructor_args():
    sig = inspect.signature(behaviour::LocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::constantexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::ConstantExpression)


def test_behaviour::constantexpression_constructor_exists():
    assert callable(behaviour::ConstantExpression.__init__)


def test_behaviour::constantexpression_constructor_args():
    sig = inspect.signature(behaviour::ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::variableclass_is_not_abstract():
    assert not inspect.isabstract(behaviour::VariableClass)


def test_behaviour::variableclass_constructor_exists():
    assert callable(behaviour::VariableClass.__init__)


def test_behaviour::variableclass_constructor_args():
    sig = inspect.signature(behaviour::VariableClass.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_behaviour::variableclass_has_variableName():
    assert hasattr(behaviour::VariableClass, "variableName")
    descriptor = None
    for klass in behaviour::VariableClass.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::expression_is_not_abstract():
    assert not inspect.isabstract(behaviour::Expression)


def test_behaviour::expression_constructor_exists():
    assert callable(behaviour::Expression.__init__)


def test_behaviour::expression_constructor_args():
    sig = inspect.signature(behaviour::Expression.__init__)
    params = list(sig.parameters.keys())

def test_unarylocationenum_exists():
    # Check that the Enumeration exists
    assert UnaryLocationEnum is not None

def test_unarylocationenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryLocationEnum]
    expected_literals = [
        "toplocation",
        "oneofneighbour",
        "oneof",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryLocationEnum"

def test_weekdaysenum_exists():
    # Check that the Enumeration exists
    assert WeekDaysEnum is not None

def test_weekdaysenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WeekDaysEnum]
    expected_literals = [
        "wednesday",
        "tuesday",
        "saturday",
        "thursday",
        "friday",
        "monday",
        "sunday",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WeekDaysEnum"

def test_typeenum_exists():
    # Check that the Enumeration exists
    assert TypeEnum is not None

def test_typeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeEnum]
    expected_literals = [
        "string",
        "int",
        "locationset",
        "boolean",
        "location",
        "entityset",
        "entity",
        "float",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeEnum"

def test_unarynumericfunctionenum_exists():
    # Check that the Enumeration exists
    assert UnaryNumericFunctionEnum is not None

def test_unarynumericfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryNumericFunctionEnum]
    expected_literals = [
        "random",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryNumericFunctionEnum"

def test_durationtypeenum_exists():
    # Check that the Enumeration exists
    assert DurationTypeEnum is not None

def test_durationtypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DurationTypeEnum]
    expected_literals = [
        "weekly",
        "monthly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DurationTypeEnum"

def test_occupationbooleanfunctionenum_exists():
    # Check that the Enumeration exists
    assert OccupationBooleanFunctionEnum is not None

def test_occupationbooleanfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OccupationBooleanFunctionEnum]
    expected_literals = [
        "Occupied",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OccupationBooleanFunctionEnum"

def test_arithmeticfunctionenum_exists():
    # Check that the Enumeration exists
    assert ArithmeticFunctionEnum is not None

def test_arithmeticfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticFunctionEnum]
    expected_literals = [
        "Division",
        "Times",
        "Sum",
        "Minus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticFunctionEnum"

def test_unarylocationfunctionenum_exists():
    # Check that the Enumeration exists
    assert UnaryLocationFunctionEnum is not None

def test_unarylocationfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryLocationFunctionEnum]
    expected_literals = [
        "RandomNeighbourhoodLocation",
        "OneOf",
        "BottomLocation",
        "BottomLeftLocation",
        "RightLocation",
        "TopRightLocation",
        "TopLeftLocation",
        "RandomLocation",
        "BottomRightLocation",
        "LeftLocation",
        "TopLocation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryLocationFunctionEnum"

def test_logicbooleanfunctionenum_exists():
    # Check that the Enumeration exists
    assert LogicBooleanFunctionEnum is not None

def test_logicbooleanfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicBooleanFunctionEnum]
    expected_literals = [
        "NOT",
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicBooleanFunctionEnum"

def test_locationsetprimiveenum_exists():
    # Check that the Enumeration exists
    assert LocationSetPrimiveEnum is not None

def test_locationsetprimiveenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationSetPrimiveEnum]
    expected_literals = [
        "space",
        "neighbourhood",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationSetPrimiveEnum"

def test_entityprimitiveenum_exists():
    # Check that the Enumeration exists
    assert EntityPrimitiveEnum is not None

def test_entityprimitiveenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityPrimitiveEnum]
    expected_literals = [
        "oneOf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityPrimitiveEnum"

def test_locationprimiveenum_exists():
    # Check that the Enumeration exists
    assert LocationPrimiveEnum is not None

def test_locationprimiveenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationPrimiveEnum]
    expected_literals = [
        "bottom",
        "left",
        "right",
        "here",
        "top",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationPrimiveEnum"

def test_monthsenum_exists():
    # Check that the Enumeration exists
    assert MonthsEnum is not None

def test_monthsenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MonthsEnum]
    expected_literals = [
        "September",
        "March",
        "November",
        "August",
        "October",
        "January",
        "December",
        "Februrary",
        "June",
        "July",
        "April",
        "May",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MonthsEnum"

def test_comparisonbooleanfunctionenum_exists():
    # Check that the Enumeration exists
    assert ComparisonBooleanFunctionEnum is not None

def test_comparisonbooleanfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonBooleanFunctionEnum]
    expected_literals = [
        "GreaterThan",
        "GreaterOrEequalThan",
        "LessOrEqualThan",
        "LessThan",
        "Equal",
        "NotEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonBooleanFunctionEnum"

def test_unarystringfunctionenum_exists():
    # Check that the Enumeration exists
    assert UnaryStringFunctionEnum is not None

def test_unarystringfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryStringFunctionEnum]
    expected_literals = [
        "Get",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryStringFunctionEnum"

def test_booleanprimitiveenum_exists():
    # Check that the Enumeration exists
    assert BooleanPrimitiveEnum is not None

def test_booleanprimitiveenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanPrimitiveEnum]
    expected_literals = [
        "true",
        "false",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanPrimitiveEnum"

def test_entitysetprimiveenum_exists():
    # Check that the Enumeration exists
    assert EntitySetPrimiveEnum is not None

def test_entitysetprimiveenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntitySetPrimiveEnum]
    expected_literals = [
        "all",
        "neighbours",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntitySetPrimiveEnum"

def test_unaryentityfunctionenum_exists():
    # Check that the Enumeration exists
    assert UnaryEntityFunctionEnum is not None

def test_unaryentityfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryEntityFunctionEnum]
    expected_literals = [
        "oneof",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryEntityFunctionEnum"


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
NamedFunction_strategy = st.builds(
    NamedFunction,
)
behaviour::UnaryFunction_strategy = st.builds(
    behaviour::UnaryFunction,
)
behaviour::BinaryFunction_strategy = st.builds(
    behaviour::BinaryFunction,
)
Duration_strategy = st.builds(
    Duration,
)
behaviour::MonthDuration_strategy = st.builds(
    behaviour::MonthDuration,
    month=
        safe_text
)
behaviour::NumericPrimitive_strategy = st.builds(
    behaviour::NumericPrimitive,
)
TimeExpression_strategy = st.builds(
    TimeExpression,
)
behaviour::While_strategy = st.builds(
    behaviour::While,
)
LocationExpression_strategy = st.builds(
    LocationExpression,
)
behaviour::CoordinateLocationExpression_strategy = st.builds(
    behaviour::CoordinateLocationExpression,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour::NameLocationExpression_strategy = st.builds(
    behaviour::NameLocationExpression,
    name=
        safe_text
)
BinaryBooleanFunction_strategy = st.builds(
    BinaryBooleanFunction,
)
behaviour::ComparisonBooleanFunction_strategy = st.builds(
    behaviour::ComparisonBooleanFunction,
    functionName=
        safe_text
)
BinaryFunction_strategy = st.builds(
    BinaryFunction,
)
behaviour::BinaryArithmeticFunction_strategy = st.builds(
    behaviour::BinaryArithmeticFunction,
    functionName=
        safe_text
)
behaviour::BinaryLocationFunction_strategy = st.builds(
    behaviour::BinaryLocationFunction,
)
behaviour::BinaryBooleanFunction_strategy = st.builds(
    behaviour::BinaryBooleanFunction,
)
UnaryFunction_strategy = st.builds(
    UnaryFunction,
)
behaviour::UnaryNumericFunction_strategy = st.builds(
    behaviour::UnaryNumericFunction,
    functionName=
        safe_text
)
behaviour::UnaryLocationFunction_strategy = st.builds(
    behaviour::UnaryLocationFunction,
    functionName=
        safe_text
)
behaviour::UnaryEntityFunction_strategy = st.builds(
    behaviour::UnaryEntityFunction,
    functionName=
        safe_text
)
behaviour::UnaryStringFunction_strategy = st.builds(
    behaviour::UnaryStringFunction,
    functionName=
        safe_text
)
Edge_strategy = st.builds(
    Edge,
)
behaviour::FalseEdge_strategy = st.builds(
    behaviour::FalseEdge,
)
behaviour::TrueEdge_strategy = st.builds(
    behaviour::TrueEdge,
)
behaviour::UnconditionedEdge_strategy = st.builds(
    behaviour::UnconditionedEdge,
)
PrimitiveActivity_strategy = st.builds(
    PrimitiveActivity,
)
behaviour::Remove_strategy = st.builds(
    behaviour::Remove,
)
behaviour::Add_strategy = st.builds(
    behaviour::Add,
)
behaviour::Die_strategy = st.builds(
    behaviour::Die,
)
behaviour::Reproduce_strategy = st.builds(
    behaviour::Reproduce,
)
behaviour::Move_strategy = st.builds(
    behaviour::Move,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
behaviour::Decision_strategy = st.builds(
    behaviour::Decision,
)
behaviour::Merge_strategy = st.builds(
    behaviour::Merge,
)
behaviour::Fork_strategy = st.builds(
    behaviour::Fork,
)
behaviour::Join_strategy = st.builds(
    behaviour::Join,
)
behaviour::TimeExpression_strategy = st.builds(
    behaviour::TimeExpression,
)
Node_strategy = st.builds(
    Node,
)
behaviour::ExecutableNode_strategy = st.builds(
    behaviour::ExecutableNode,
)
behaviour::ControlNode_strategy = st.builds(
    behaviour::ControlNode,
)
behaviour::LogicBooleanFunction_strategy = st.builds(
    behaviour::LogicBooleanFunction,
    functionName=
        safe_text
)
behaviour::OccupationBooleanFunction_strategy = st.builds(
    behaviour::OccupationBooleanFunction,
    functionName=
        safe_text
)
behaviour::Behavior_strategy = st.builds(
    behaviour::Behavior,
    behaviorName=
        safe_text,
    frequency=
        safe_text
)
behaviour::EntityClass_strategy = st.builds(
    behaviour::EntityClass,
    entityName=
        safe_text
)
Function_strategy = st.builds(
    Function,
)
behaviour::NamedFunction_strategy = st.builds(
    behaviour::NamedFunction,
)
behaviour::AnonymousFunction_strategy = st.builds(
    behaviour::AnonymousFunction,
)
behaviour::Node_strategy = st.builds(
    behaviour::Node,
)
behaviour::Edge_strategy = st.builds(
    behaviour::Edge,
)
behaviour::End_strategy = st.builds(
    behaviour::End,
)
behaviour::Start_strategy = st.builds(
    behaviour::Start,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
behaviour::PrimitiveActivity_strategy = st.builds(
    behaviour::PrimitiveActivity,
)
behaviour::Equation_strategy = st.builds(
    behaviour::Equation,
)
Behavior_strategy = st.builds(
    Behavior,
)
behaviour::ActivityDiagramBehavior_strategy = st.builds(
    behaviour::ActivityDiagramBehavior,
)
behaviour::EquationBehaviour_strategy = st.builds(
    behaviour::EquationBehaviour,
)
behaviour::Duration_strategy = st.builds(
    behaviour::Duration,
    durationTime=
        st.integers()
)
VariableClass_strategy = st.builds(
    VariableClass,
)
behaviour::ParameterClass_strategy = st.builds(
    behaviour::ParameterClass,
)
behaviour::AttributeClass_strategy = st.builds(
    behaviour::AttributeClass,
)
behaviour::Type_strategy = st.builds(
    behaviour::Type,
    type=
        safe_text
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
behaviour::BooleanPrimitive_strategy = st.builds(
    behaviour::BooleanPrimitive,
    primitive=
        safe_text
)
behaviour::LocationPrimitive_strategy = st.builds(
    behaviour::LocationPrimitive,
    primitive=
        safe_text
)
behaviour::EntitySetPrimitive_strategy = st.builds(
    behaviour::EntitySetPrimitive,
    primitive=
        safe_text
)
behaviour::LocationSetPrimitive_strategy = st.builds(
    behaviour::LocationSetPrimitive,
    primitive=
        safe_text
)
behaviour::EntityPrimive_strategy = st.builds(
    behaviour::EntityPrimive,
    primitive=
        safe_text
)
ConstantExpression_strategy = st.builds(
    ConstantExpression,
)
behaviour::FloatConstantExpression_strategy = st.builds(
    behaviour::FloatConstantExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour::StringConstantExpression_strategy = st.builds(
    behaviour::StringConstantExpression,
    value=
        safe_text
)
behaviour::IntConstantExpression_strategy = st.builds(
    behaviour::IntConstantExpression,
    value=
        st.integers()
)
behaviour::Function_strategy = st.builds(
    behaviour::Function,
)
Expression_strategy = st.builds(
    Expression,
)
behaviour::PrimitiveExpression_strategy = st.builds(
    behaviour::PrimitiveExpression,
)
behaviour::FunctionCallExpression_strategy = st.builds(
    behaviour::FunctionCallExpression,
)
behaviour::LocationExpression_strategy = st.builds(
    behaviour::LocationExpression,
)
behaviour::ConstantExpression_strategy = st.builds(
    behaviour::ConstantExpression,
)
behaviour::VariableClass_strategy = st.builds(
    behaviour::VariableClass,
    variableName=
        safe_text
)
behaviour::Expression_strategy = st.builds(
    behaviour::Expression,
)

@given(instance=NamedFunction_strategy)
@settings(max_examples=50)
def test_namedfunction_instantiation(instance):
    assert isinstance(instance, NamedFunction)

@given(instance=behaviour::UnaryFunction_strategy)
@settings(max_examples=50)
def test_behaviour::unaryfunction_instantiation(instance):
    assert isinstance(instance, behaviour::UnaryFunction)

@given(instance=behaviour::BinaryFunction_strategy)
@settings(max_examples=50)
def test_behaviour::binaryfunction_instantiation(instance):
    assert isinstance(instance, behaviour::BinaryFunction)

@given(instance=Duration_strategy)
@settings(max_examples=50)
def test_duration_instantiation(instance):
    assert isinstance(instance, Duration)

@given(instance=behaviour::MonthDuration_strategy)
@settings(max_examples=50)
def test_behaviour::monthduration_instantiation(instance):
    assert isinstance(instance, behaviour::MonthDuration)

@given(instance=behaviour::MonthDuration_strategy)
def test_behaviour::monthduration_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=behaviour::MonthDuration_strategy)
def test_behaviour::monthduration_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=behaviour::NumericPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour::numericprimitive_instantiation(instance):
    assert isinstance(instance, behaviour::NumericPrimitive)

@given(instance=TimeExpression_strategy)
@settings(max_examples=50)
def test_timeexpression_instantiation(instance):
    assert isinstance(instance, TimeExpression)

@given(instance=behaviour::While_strategy)
@settings(max_examples=50)
def test_behaviour::while_instantiation(instance):
    assert isinstance(instance, behaviour::While)

@given(instance=LocationExpression_strategy)
@settings(max_examples=50)
def test_locationexpression_instantiation(instance):
    assert isinstance(instance, LocationExpression)

@given(instance=behaviour::CoordinateLocationExpression_strategy)
@settings(max_examples=50)
def test_behaviour::coordinatelocationexpression_instantiation(instance):
    assert isinstance(instance, behaviour::CoordinateLocationExpression)

@given(instance=behaviour::CoordinateLocationExpression_strategy)
def test_behaviour::coordinatelocationexpression_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=behaviour::CoordinateLocationExpression_strategy)
def test_behaviour::coordinatelocationexpression_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=behaviour::CoordinateLocationExpression_strategy)
def test_behaviour::coordinatelocationexpression_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=behaviour::CoordinateLocationExpression_strategy)
def test_behaviour::coordinatelocationexpression_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=behaviour::NameLocationExpression_strategy)
@settings(max_examples=50)
def test_behaviour::namelocationexpression_instantiation(instance):
    assert isinstance(instance, behaviour::NameLocationExpression)

@given(instance=behaviour::NameLocationExpression_strategy)
def test_behaviour::namelocationexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behaviour::NameLocationExpression_strategy)
def test_behaviour::namelocationexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BinaryBooleanFunction_strategy)
@settings(max_examples=50)
def test_binarybooleanfunction_instantiation(instance):
    assert isinstance(instance, BinaryBooleanFunction)

@given(instance=behaviour::ComparisonBooleanFunction_strategy)
@settings(max_examples=50)
def test_behaviour::comparisonbooleanfunction_instantiation(instance):
    assert isinstance(instance, behaviour::ComparisonBooleanFunction)

@given(instance=behaviour::ComparisonBooleanFunction_strategy)
def test_behaviour::comparisonbooleanfunction_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=behaviour::ComparisonBooleanFunction_strategy)
def test_behaviour::comparisonbooleanfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=BinaryFunction_strategy)
@settings(max_examples=50)
def test_binaryfunction_instantiation(instance):
    assert isinstance(instance, BinaryFunction)

@given(instance=behaviour::BinaryArithmeticFunction_strategy)
@settings(max_examples=50)
def test_behaviour::binaryarithmeticfunction_instantiation(instance):
    assert isinstance(instance, behaviour::BinaryArithmeticFunction)

@given(instance=behaviour::BinaryArithmeticFunction_strategy)
def test_behaviour::binaryarithmeticfunction_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=behaviour::BinaryArithmeticFunction_strategy)
def test_behaviour::binaryarithmeticfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour::BinaryLocationFunction_strategy)
@settings(max_examples=50)
def test_behaviour::binarylocationfunction_instantiation(instance):
    assert isinstance(instance, behaviour::BinaryLocationFunction)

@given(instance=behaviour::BinaryBooleanFunction_strategy)
@settings(max_examples=50)
def test_behaviour::binarybooleanfunction_instantiation(instance):
    assert isinstance(instance, behaviour::BinaryBooleanFunction)

@given(instance=UnaryFunction_strategy)
@settings(max_examples=50)
def test_unaryfunction_instantiation(instance):
    assert isinstance(instance, UnaryFunction)

@given(instance=behaviour::UnaryNumericFunction_strategy)
@settings(max_examples=50)
def test_behaviour::unarynumericfunction_instantiation(instance):
    assert isinstance(instance, behaviour::UnaryNumericFunction)

@given(instance=behaviour::UnaryNumericFunction_strategy)
def test_behaviour::unarynumericfunction_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=behaviour::UnaryNumericFunction_strategy)
def test_behaviour::unarynumericfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour::UnaryLocationFunction_strategy)
@settings(max_examples=50)
def test_behaviour::unarylocationfunction_instantiation(instance):
    assert isinstance(instance, behaviour::UnaryLocationFunction)

@given(instance=behaviour::UnaryLocationFunction_strategy)
def test_behaviour::unarylocationfunction_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=behaviour::UnaryLocationFunction_strategy)
def test_behaviour::unarylocationfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour::UnaryEntityFunction_strategy)
@settings(max_examples=50)
def test_behaviour::unaryentityfunction_instantiation(instance):
    assert isinstance(instance, behaviour::UnaryEntityFunction)

@given(instance=behaviour::UnaryEntityFunction_strategy)
def test_behaviour::unaryentityfunction_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=behaviour::UnaryEntityFunction_strategy)
def test_behaviour::unaryentityfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour::UnaryStringFunction_strategy)
@settings(max_examples=50)
def test_behaviour::unarystringfunction_instantiation(instance):
    assert isinstance(instance, behaviour::UnaryStringFunction)

@given(instance=behaviour::UnaryStringFunction_strategy)
def test_behaviour::unarystringfunction_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=behaviour::UnaryStringFunction_strategy)
def test_behaviour::unarystringfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=behaviour::FalseEdge_strategy)
@settings(max_examples=50)
def test_behaviour::falseedge_instantiation(instance):
    assert isinstance(instance, behaviour::FalseEdge)

@given(instance=behaviour::TrueEdge_strategy)
@settings(max_examples=50)
def test_behaviour::trueedge_instantiation(instance):
    assert isinstance(instance, behaviour::TrueEdge)

@given(instance=behaviour::UnconditionedEdge_strategy)
@settings(max_examples=50)
def test_behaviour::unconditionededge_instantiation(instance):
    assert isinstance(instance, behaviour::UnconditionedEdge)

@given(instance=PrimitiveActivity_strategy)
@settings(max_examples=50)
def test_primitiveactivity_instantiation(instance):
    assert isinstance(instance, PrimitiveActivity)

@given(instance=behaviour::Remove_strategy)
@settings(max_examples=50)
def test_behaviour::remove_instantiation(instance):
    assert isinstance(instance, behaviour::Remove)

@given(instance=behaviour::Add_strategy)
@settings(max_examples=50)
def test_behaviour::add_instantiation(instance):
    assert isinstance(instance, behaviour::Add)

@given(instance=behaviour::Die_strategy)
@settings(max_examples=50)
def test_behaviour::die_instantiation(instance):
    assert isinstance(instance, behaviour::Die)

@given(instance=behaviour::Reproduce_strategy)
@settings(max_examples=50)
def test_behaviour::reproduce_instantiation(instance):
    assert isinstance(instance, behaviour::Reproduce)

@given(instance=behaviour::Move_strategy)
@settings(max_examples=50)
def test_behaviour::move_instantiation(instance):
    assert isinstance(instance, behaviour::Move)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=behaviour::Decision_strategy)
@settings(max_examples=50)
def test_behaviour::decision_instantiation(instance):
    assert isinstance(instance, behaviour::Decision)

@given(instance=behaviour::Merge_strategy)
@settings(max_examples=50)
def test_behaviour::merge_instantiation(instance):
    assert isinstance(instance, behaviour::Merge)

@given(instance=behaviour::Fork_strategy)
@settings(max_examples=50)
def test_behaviour::fork_instantiation(instance):
    assert isinstance(instance, behaviour::Fork)

@given(instance=behaviour::Join_strategy)
@settings(max_examples=50)
def test_behaviour::join_instantiation(instance):
    assert isinstance(instance, behaviour::Join)

@given(instance=behaviour::TimeExpression_strategy)
@settings(max_examples=50)
def test_behaviour::timeexpression_instantiation(instance):
    assert isinstance(instance, behaviour::TimeExpression)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=behaviour::ExecutableNode_strategy)
@settings(max_examples=50)
def test_behaviour::executablenode_instantiation(instance):
    assert isinstance(instance, behaviour::ExecutableNode)

@given(instance=behaviour::ControlNode_strategy)
@settings(max_examples=50)
def test_behaviour::controlnode_instantiation(instance):
    assert isinstance(instance, behaviour::ControlNode)

@given(instance=behaviour::LogicBooleanFunction_strategy)
@settings(max_examples=50)
def test_behaviour::logicbooleanfunction_instantiation(instance):
    assert isinstance(instance, behaviour::LogicBooleanFunction)

@given(instance=behaviour::LogicBooleanFunction_strategy)
def test_behaviour::logicbooleanfunction_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=behaviour::LogicBooleanFunction_strategy)
def test_behaviour::logicbooleanfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour::OccupationBooleanFunction_strategy)
@settings(max_examples=50)
def test_behaviour::occupationbooleanfunction_instantiation(instance):
    assert isinstance(instance, behaviour::OccupationBooleanFunction)

@given(instance=behaviour::OccupationBooleanFunction_strategy)
def test_behaviour::occupationbooleanfunction_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=behaviour::OccupationBooleanFunction_strategy)
def test_behaviour::occupationbooleanfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour::Behavior_strategy)
@settings(max_examples=50)
def test_behaviour::behavior_instantiation(instance):
    assert isinstance(instance, behaviour::Behavior)

@given(instance=behaviour::Behavior_strategy)
def test_behaviour::behavior_behaviorName_type(instance):
    assert isinstance(instance.behaviorName, str)


@given(instance=behaviour::Behavior_strategy)
def test_behaviour::behavior_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original

@given(instance=behaviour::Behavior_strategy)
def test_behaviour::behavior_frequency_type(instance):
    assert isinstance(instance.frequency, str)


@given(instance=behaviour::Behavior_strategy)
def test_behaviour::behavior_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=behaviour::EntityClass_strategy)
@settings(max_examples=50)
def test_behaviour::entityclass_instantiation(instance):
    assert isinstance(instance, behaviour::EntityClass)

@given(instance=behaviour::EntityClass_strategy)
def test_behaviour::entityclass_entityName_type(instance):
    assert isinstance(instance.entityName, str)


@given(instance=behaviour::EntityClass_strategy)
def test_behaviour::entityclass_entityName_setter(instance):
    original = instance.entityName
    instance.entityName = original
    assert instance.entityName == original

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=behaviour::NamedFunction_strategy)
@settings(max_examples=50)
def test_behaviour::namedfunction_instantiation(instance):
    assert isinstance(instance, behaviour::NamedFunction)

@given(instance=behaviour::AnonymousFunction_strategy)
@settings(max_examples=50)
def test_behaviour::anonymousfunction_instantiation(instance):
    assert isinstance(instance, behaviour::AnonymousFunction)

@given(instance=behaviour::Node_strategy)
@settings(max_examples=50)
def test_behaviour::node_instantiation(instance):
    assert isinstance(instance, behaviour::Node)

@given(instance=behaviour::Edge_strategy)
@settings(max_examples=50)
def test_behaviour::edge_instantiation(instance):
    assert isinstance(instance, behaviour::Edge)

@given(instance=behaviour::End_strategy)
@settings(max_examples=50)
def test_behaviour::end_instantiation(instance):
    assert isinstance(instance, behaviour::End)

@given(instance=behaviour::Start_strategy)
@settings(max_examples=50)
def test_behaviour::start_instantiation(instance):
    assert isinstance(instance, behaviour::Start)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=behaviour::PrimitiveActivity_strategy)
@settings(max_examples=50)
def test_behaviour::primitiveactivity_instantiation(instance):
    assert isinstance(instance, behaviour::PrimitiveActivity)

@given(instance=behaviour::Equation_strategy)
@settings(max_examples=50)
def test_behaviour::equation_instantiation(instance):
    assert isinstance(instance, behaviour::Equation)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=behaviour::ActivityDiagramBehavior_strategy)
@settings(max_examples=50)
def test_behaviour::activitydiagrambehavior_instantiation(instance):
    assert isinstance(instance, behaviour::ActivityDiagramBehavior)

@given(instance=behaviour::EquationBehaviour_strategy)
@settings(max_examples=50)
def test_behaviour::equationbehaviour_instantiation(instance):
    assert isinstance(instance, behaviour::EquationBehaviour)

@given(instance=behaviour::Duration_strategy)
@settings(max_examples=50)
def test_behaviour::duration_instantiation(instance):
    assert isinstance(instance, behaviour::Duration)

@given(instance=behaviour::Duration_strategy)
def test_behaviour::duration_durationTime_type(instance):
    assert isinstance(instance.durationTime, int)


@given(instance=behaviour::Duration_strategy)
def test_behaviour::duration_durationTime_setter(instance):
    original = instance.durationTime
    instance.durationTime = original
    assert instance.durationTime == original

@given(instance=VariableClass_strategy)
@settings(max_examples=50)
def test_variableclass_instantiation(instance):
    assert isinstance(instance, VariableClass)

@given(instance=behaviour::ParameterClass_strategy)
@settings(max_examples=50)
def test_behaviour::parameterclass_instantiation(instance):
    assert isinstance(instance, behaviour::ParameterClass)

@given(instance=behaviour::AttributeClass_strategy)
@settings(max_examples=50)
def test_behaviour::attributeclass_instantiation(instance):
    assert isinstance(instance, behaviour::AttributeClass)

@given(instance=behaviour::Type_strategy)
@settings(max_examples=50)
def test_behaviour::type_instantiation(instance):
    assert isinstance(instance, behaviour::Type)

@given(instance=behaviour::Type_strategy)
def test_behaviour::type_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=behaviour::Type_strategy)
def test_behaviour::type_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=behaviour::BooleanPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour::booleanprimitive_instantiation(instance):
    assert isinstance(instance, behaviour::BooleanPrimitive)

@given(instance=behaviour::BooleanPrimitive_strategy)
def test_behaviour::booleanprimitive_primitive_type(instance):
    assert isinstance(instance.primitive, str)


@given(instance=behaviour::BooleanPrimitive_strategy)
def test_behaviour::booleanprimitive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=behaviour::LocationPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour::locationprimitive_instantiation(instance):
    assert isinstance(instance, behaviour::LocationPrimitive)

@given(instance=behaviour::LocationPrimitive_strategy)
def test_behaviour::locationprimitive_primitive_type(instance):
    assert isinstance(instance.primitive, str)


@given(instance=behaviour::LocationPrimitive_strategy)
def test_behaviour::locationprimitive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=behaviour::EntitySetPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour::entitysetprimitive_instantiation(instance):
    assert isinstance(instance, behaviour::EntitySetPrimitive)

@given(instance=behaviour::EntitySetPrimitive_strategy)
def test_behaviour::entitysetprimitive_primitive_type(instance):
    assert isinstance(instance.primitive, str)


@given(instance=behaviour::EntitySetPrimitive_strategy)
def test_behaviour::entitysetprimitive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=behaviour::LocationSetPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour::locationsetprimitive_instantiation(instance):
    assert isinstance(instance, behaviour::LocationSetPrimitive)

@given(instance=behaviour::LocationSetPrimitive_strategy)
def test_behaviour::locationsetprimitive_primitive_type(instance):
    assert isinstance(instance.primitive, str)


@given(instance=behaviour::LocationSetPrimitive_strategy)
def test_behaviour::locationsetprimitive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=behaviour::EntityPrimive_strategy)
@settings(max_examples=50)
def test_behaviour::entityprimive_instantiation(instance):
    assert isinstance(instance, behaviour::EntityPrimive)

@given(instance=behaviour::EntityPrimive_strategy)
def test_behaviour::entityprimive_primitive_type(instance):
    assert isinstance(instance.primitive, str)


@given(instance=behaviour::EntityPrimive_strategy)
def test_behaviour::entityprimive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=ConstantExpression_strategy)
@settings(max_examples=50)
def test_constantexpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)

@given(instance=behaviour::FloatConstantExpression_strategy)
@settings(max_examples=50)
def test_behaviour::floatconstantexpression_instantiation(instance):
    assert isinstance(instance, behaviour::FloatConstantExpression)

@given(instance=behaviour::FloatConstantExpression_strategy)
def test_behaviour::floatconstantexpression_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=behaviour::FloatConstantExpression_strategy)
def test_behaviour::floatconstantexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behaviour::StringConstantExpression_strategy)
@settings(max_examples=50)
def test_behaviour::stringconstantexpression_instantiation(instance):
    assert isinstance(instance, behaviour::StringConstantExpression)

@given(instance=behaviour::StringConstantExpression_strategy)
def test_behaviour::stringconstantexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=behaviour::StringConstantExpression_strategy)
def test_behaviour::stringconstantexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behaviour::IntConstantExpression_strategy)
@settings(max_examples=50)
def test_behaviour::intconstantexpression_instantiation(instance):
    assert isinstance(instance, behaviour::IntConstantExpression)

@given(instance=behaviour::IntConstantExpression_strategy)
def test_behaviour::intconstantexpression_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=behaviour::IntConstantExpression_strategy)
def test_behaviour::intconstantexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behaviour::Function_strategy)
@settings(max_examples=50)
def test_behaviour::function_instantiation(instance):
    assert isinstance(instance, behaviour::Function)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=behaviour::PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_behaviour::primitiveexpression_instantiation(instance):
    assert isinstance(instance, behaviour::PrimitiveExpression)

@given(instance=behaviour::FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_behaviour::functioncallexpression_instantiation(instance):
    assert isinstance(instance, behaviour::FunctionCallExpression)

@given(instance=behaviour::LocationExpression_strategy)
@settings(max_examples=50)
def test_behaviour::locationexpression_instantiation(instance):
    assert isinstance(instance, behaviour::LocationExpression)

@given(instance=behaviour::ConstantExpression_strategy)
@settings(max_examples=50)
def test_behaviour::constantexpression_instantiation(instance):
    assert isinstance(instance, behaviour::ConstantExpression)

@given(instance=behaviour::VariableClass_strategy)
@settings(max_examples=50)
def test_behaviour::variableclass_instantiation(instance):
    assert isinstance(instance, behaviour::VariableClass)

@given(instance=behaviour::VariableClass_strategy)
def test_behaviour::variableclass_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=behaviour::VariableClass_strategy)
def test_behaviour::variableclass_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=behaviour::Expression_strategy)
@settings(max_examples=50)
def test_behaviour::expression_instantiation(instance):
    assert isinstance(instance, behaviour::Expression)
