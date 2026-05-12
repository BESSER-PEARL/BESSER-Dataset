import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedFunction,
    behaviour_UnaryFunction,
    behaviour_BinaryFunction,
    Duration,
    behaviour_MonthDuration,
    behaviour_NumericPrimitive,
    TimeExpression,
    behaviour_While,
    LocationExpression,
    behaviour_CoordinateLocationExpression,
    behaviour_NameLocationExpression,
    BinaryBooleanFunction,
    behaviour_ComparisonBooleanFunction,
    BinaryFunction,
    behaviour_BinaryArithmeticFunction,
    behaviour_BinaryLocationFunction,
    behaviour_BinaryBooleanFunction,
    UnaryFunction,
    behaviour_UnaryNumericFunction,
    behaviour_UnaryEntityFunction,
    behaviour_UnaryLocationFunction,
    behaviour_UnaryStringFunction,
    Edge,
    behaviour_TrueEdge,
    behaviour_FalseEdge,
    behaviour_UnconditionedEdge,
    PrimitiveActivity,
    behaviour_Die,
    behaviour_Reproduce,
    behaviour_Remove,
    behaviour_Add,
    behaviour_Move,
    ControlNode,
    behaviour_Join,
    behaviour_Decision,
    behaviour_Merge,
    behaviour_Fork,
    behaviour_TimeExpression,
    Node,
    behaviour_ExecutableNode,
    behaviour_ControlNode,
    behaviour_LogicBooleanFunction,
    behaviour_OccupationBooleanFunction,
    behaviour_Behavior,
    behaviour_EntityClass,
    Function,
    behaviour_NamedFunction,
    behaviour_AnonymousFunction,
    behaviour_Node,
    behaviour_Edge,
    behaviour_End,
    behaviour_Start,
    ExecutableNode,
    behaviour_PrimitiveActivity,
    behaviour_Equation,
    Behavior,
    behaviour_ActivityDiagramBehavior,
    behaviour_EquationBehaviour,
    behaviour_Duration,
    VariableClass,
    behaviour_ParameterClass,
    behaviour_AttributeClass,
    behaviour_Type,
    PrimitiveExpression,
    behaviour_BooleanPrimitive,
    behaviour_EntitySetPrimitive,
    behaviour_LocationPrimitive,
    behaviour_LocationSetPrimitive,
    behaviour_EntityPrimive,
    ConstantExpression,
    behaviour_StringConstantExpression,
    behaviour_FloatConstantExpression,
    behaviour_IntConstantExpression,
    behaviour_Function,
    Expression,
    behaviour_LocationExpression,
    behaviour_ConstantExpression,
    behaviour_FunctionCallExpression,
    behaviour_PrimitiveExpression,
    behaviour_VariableClass,
    behaviour_Expression,
    UnaryEntityFunctionEnum,
    LogicBooleanFunctionEnum,
    LocationSetPrimiveEnum,
    OccupationBooleanFunctionEnum,
    UnaryStringFunctionEnum,
    UnaryLocationFunctionEnum,
    DurationTypeEnum,
    ComparisonBooleanFunctionEnum,
    ArithmeticFunctionEnum,
    WeekDaysEnum,
    MonthsEnum,
    UnaryLocationEnum,
    LocationPrimiveEnum,
    TypeEnum,
    UnaryNumericFunctionEnum,
    EntitySetPrimiveEnum,
    BooleanPrimitiveEnum,
    EntityPrimitiveEnum,
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



def test_behaviour_unaryfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_UnaryFunction)


def test_behaviour_unaryfunction_constructor_exists():
    assert callable(behaviour_UnaryFunction.__init__)


def test_behaviour_unaryfunction_constructor_args():
    sig = inspect.signature(behaviour_UnaryFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_binaryfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_BinaryFunction)


def test_behaviour_binaryfunction_constructor_exists():
    assert callable(behaviour_BinaryFunction.__init__)


def test_behaviour_binaryfunction_constructor_args():
    sig = inspect.signature(behaviour_BinaryFunction.__init__)
    params = list(sig.parameters.keys())



def test_duration_is_not_abstract():
    assert not inspect.isabstract(Duration)


def test_duration_constructor_exists():
    assert callable(Duration.__init__)


def test_duration_constructor_args():
    sig = inspect.signature(Duration.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_monthduration_is_not_abstract():
    assert not inspect.isabstract(behaviour_MonthDuration)


def test_behaviour_monthduration_constructor_exists():
    assert callable(behaviour_MonthDuration.__init__)


def test_behaviour_monthduration_constructor_args():
    sig = inspect.signature(behaviour_MonthDuration.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"

def test_behaviour_monthduration_has_month():
    assert hasattr(behaviour_MonthDuration, "month")
    descriptor = None
    for klass in behaviour_MonthDuration.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_numericprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour_NumericPrimitive)


def test_behaviour_numericprimitive_constructor_exists():
    assert callable(behaviour_NumericPrimitive.__init__)


def test_behaviour_numericprimitive_constructor_args():
    sig = inspect.signature(behaviour_NumericPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_timeexpression_is_not_abstract():
    assert not inspect.isabstract(TimeExpression)


def test_timeexpression_constructor_exists():
    assert callable(TimeExpression.__init__)


def test_timeexpression_constructor_args():
    sig = inspect.signature(TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_while_is_not_abstract():
    assert not inspect.isabstract(behaviour_While)


def test_behaviour_while_constructor_exists():
    assert callable(behaviour_While.__init__)


def test_behaviour_while_constructor_args():
    sig = inspect.signature(behaviour_While.__init__)
    params = list(sig.parameters.keys())



def test_locationexpression_is_not_abstract():
    assert not inspect.isabstract(LocationExpression)


def test_locationexpression_constructor_exists():
    assert callable(LocationExpression.__init__)


def test_locationexpression_constructor_args():
    sig = inspect.signature(LocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_coordinatelocationexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_CoordinateLocationExpression)


def test_behaviour_coordinatelocationexpression_constructor_exists():
    assert callable(behaviour_CoordinateLocationExpression.__init__)


def test_behaviour_coordinatelocationexpression_constructor_args():
    sig = inspect.signature(behaviour_CoordinateLocationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_behaviour_coordinatelocationexpression_has_x():
    assert hasattr(behaviour_CoordinateLocationExpression, "x")
    descriptor = None
    for klass in behaviour_CoordinateLocationExpression.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_coordinatelocationexpression_has_y():
    assert hasattr(behaviour_CoordinateLocationExpression, "y")
    descriptor = None
    for klass in behaviour_CoordinateLocationExpression.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_namelocationexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_NameLocationExpression)


def test_behaviour_namelocationexpression_constructor_exists():
    assert callable(behaviour_NameLocationExpression.__init__)


def test_behaviour_namelocationexpression_constructor_args():
    sig = inspect.signature(behaviour_NameLocationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behaviour_namelocationexpression_has_name():
    assert hasattr(behaviour_NameLocationExpression, "name")
    descriptor = None
    for klass in behaviour_NameLocationExpression.__mro__:
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



def test_behaviour_comparisonbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_ComparisonBooleanFunction)


def test_behaviour_comparisonbooleanfunction_constructor_exists():
    assert callable(behaviour_ComparisonBooleanFunction.__init__)


def test_behaviour_comparisonbooleanfunction_constructor_args():
    sig = inspect.signature(behaviour_ComparisonBooleanFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour_comparisonbooleanfunction_has_functionName():
    assert hasattr(behaviour_ComparisonBooleanFunction, "functionName")
    descriptor = None
    for klass in behaviour_ComparisonBooleanFunction.__mro__:
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



def test_behaviour_binaryarithmeticfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_BinaryArithmeticFunction)


def test_behaviour_binaryarithmeticfunction_constructor_exists():
    assert callable(behaviour_BinaryArithmeticFunction.__init__)


def test_behaviour_binaryarithmeticfunction_constructor_args():
    sig = inspect.signature(behaviour_BinaryArithmeticFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour_binaryarithmeticfunction_has_functionName():
    assert hasattr(behaviour_BinaryArithmeticFunction, "functionName")
    descriptor = None
    for klass in behaviour_BinaryArithmeticFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_binarylocationfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_BinaryLocationFunction)


def test_behaviour_binarylocationfunction_constructor_exists():
    assert callable(behaviour_BinaryLocationFunction.__init__)


def test_behaviour_binarylocationfunction_constructor_args():
    sig = inspect.signature(behaviour_BinaryLocationFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_binarybooleanfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_BinaryBooleanFunction)


def test_behaviour_binarybooleanfunction_constructor_exists():
    assert callable(behaviour_BinaryBooleanFunction.__init__)


def test_behaviour_binarybooleanfunction_constructor_args():
    sig = inspect.signature(behaviour_BinaryBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_unaryfunction_is_not_abstract():
    assert not inspect.isabstract(UnaryFunction)


def test_unaryfunction_constructor_exists():
    assert callable(UnaryFunction.__init__)


def test_unaryfunction_constructor_args():
    sig = inspect.signature(UnaryFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_unarynumericfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_UnaryNumericFunction)


def test_behaviour_unarynumericfunction_constructor_exists():
    assert callable(behaviour_UnaryNumericFunction.__init__)


def test_behaviour_unarynumericfunction_constructor_args():
    sig = inspect.signature(behaviour_UnaryNumericFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour_unarynumericfunction_has_functionName():
    assert hasattr(behaviour_UnaryNumericFunction, "functionName")
    descriptor = None
    for klass in behaviour_UnaryNumericFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_unaryentityfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_UnaryEntityFunction)


def test_behaviour_unaryentityfunction_constructor_exists():
    assert callable(behaviour_UnaryEntityFunction.__init__)


def test_behaviour_unaryentityfunction_constructor_args():
    sig = inspect.signature(behaviour_UnaryEntityFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour_unaryentityfunction_has_functionName():
    assert hasattr(behaviour_UnaryEntityFunction, "functionName")
    descriptor = None
    for klass in behaviour_UnaryEntityFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_unarylocationfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_UnaryLocationFunction)


def test_behaviour_unarylocationfunction_constructor_exists():
    assert callable(behaviour_UnaryLocationFunction.__init__)


def test_behaviour_unarylocationfunction_constructor_args():
    sig = inspect.signature(behaviour_UnaryLocationFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour_unarylocationfunction_has_functionName():
    assert hasattr(behaviour_UnaryLocationFunction, "functionName")
    descriptor = None
    for klass in behaviour_UnaryLocationFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_unarystringfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_UnaryStringFunction)


def test_behaviour_unarystringfunction_constructor_exists():
    assert callable(behaviour_UnaryStringFunction.__init__)


def test_behaviour_unarystringfunction_constructor_args():
    sig = inspect.signature(behaviour_UnaryStringFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour_unarystringfunction_has_functionName():
    assert hasattr(behaviour_UnaryStringFunction, "functionName")
    descriptor = None
    for klass in behaviour_UnaryStringFunction.__mro__:
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



def test_behaviour_trueedge_is_not_abstract():
    assert not inspect.isabstract(behaviour_TrueEdge)


def test_behaviour_trueedge_constructor_exists():
    assert callable(behaviour_TrueEdge.__init__)


def test_behaviour_trueedge_constructor_args():
    sig = inspect.signature(behaviour_TrueEdge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_falseedge_is_not_abstract():
    assert not inspect.isabstract(behaviour_FalseEdge)


def test_behaviour_falseedge_constructor_exists():
    assert callable(behaviour_FalseEdge.__init__)


def test_behaviour_falseedge_constructor_args():
    sig = inspect.signature(behaviour_FalseEdge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_unconditionededge_is_not_abstract():
    assert not inspect.isabstract(behaviour_UnconditionedEdge)


def test_behaviour_unconditionededge_constructor_exists():
    assert callable(behaviour_UnconditionedEdge.__init__)


def test_behaviour_unconditionededge_constructor_args():
    sig = inspect.signature(behaviour_UnconditionedEdge.__init__)
    params = list(sig.parameters.keys())



def test_primitiveactivity_is_not_abstract():
    assert not inspect.isabstract(PrimitiveActivity)


def test_primitiveactivity_constructor_exists():
    assert callable(PrimitiveActivity.__init__)


def test_primitiveactivity_constructor_args():
    sig = inspect.signature(PrimitiveActivity.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_die_is_not_abstract():
    assert not inspect.isabstract(behaviour_Die)


def test_behaviour_die_constructor_exists():
    assert callable(behaviour_Die.__init__)


def test_behaviour_die_constructor_args():
    sig = inspect.signature(behaviour_Die.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_reproduce_is_not_abstract():
    assert not inspect.isabstract(behaviour_Reproduce)


def test_behaviour_reproduce_constructor_exists():
    assert callable(behaviour_Reproduce.__init__)


def test_behaviour_reproduce_constructor_args():
    sig = inspect.signature(behaviour_Reproduce.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_remove_is_not_abstract():
    assert not inspect.isabstract(behaviour_Remove)


def test_behaviour_remove_constructor_exists():
    assert callable(behaviour_Remove.__init__)


def test_behaviour_remove_constructor_args():
    sig = inspect.signature(behaviour_Remove.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_add_is_not_abstract():
    assert not inspect.isabstract(behaviour_Add)


def test_behaviour_add_constructor_exists():
    assert callable(behaviour_Add.__init__)


def test_behaviour_add_constructor_args():
    sig = inspect.signature(behaviour_Add.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_move_is_not_abstract():
    assert not inspect.isabstract(behaviour_Move)


def test_behaviour_move_constructor_exists():
    assert callable(behaviour_Move.__init__)


def test_behaviour_move_constructor_args():
    sig = inspect.signature(behaviour_Move.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_join_is_not_abstract():
    assert not inspect.isabstract(behaviour_Join)


def test_behaviour_join_constructor_exists():
    assert callable(behaviour_Join.__init__)


def test_behaviour_join_constructor_args():
    sig = inspect.signature(behaviour_Join.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_decision_is_not_abstract():
    assert not inspect.isabstract(behaviour_Decision)


def test_behaviour_decision_constructor_exists():
    assert callable(behaviour_Decision.__init__)


def test_behaviour_decision_constructor_args():
    sig = inspect.signature(behaviour_Decision.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_merge_is_not_abstract():
    assert not inspect.isabstract(behaviour_Merge)


def test_behaviour_merge_constructor_exists():
    assert callable(behaviour_Merge.__init__)


def test_behaviour_merge_constructor_args():
    sig = inspect.signature(behaviour_Merge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_fork_is_not_abstract():
    assert not inspect.isabstract(behaviour_Fork)


def test_behaviour_fork_constructor_exists():
    assert callable(behaviour_Fork.__init__)


def test_behaviour_fork_constructor_args():
    sig = inspect.signature(behaviour_Fork.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_timeexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_TimeExpression)


def test_behaviour_timeexpression_constructor_exists():
    assert callable(behaviour_TimeExpression.__init__)


def test_behaviour_timeexpression_constructor_args():
    sig = inspect.signature(behaviour_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_executablenode_is_not_abstract():
    assert not inspect.isabstract(behaviour_ExecutableNode)


def test_behaviour_executablenode_constructor_exists():
    assert callable(behaviour_ExecutableNode.__init__)


def test_behaviour_executablenode_constructor_args():
    sig = inspect.signature(behaviour_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_controlnode_is_not_abstract():
    assert not inspect.isabstract(behaviour_ControlNode)


def test_behaviour_controlnode_constructor_exists():
    assert callable(behaviour_ControlNode.__init__)


def test_behaviour_controlnode_constructor_args():
    sig = inspect.signature(behaviour_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_logicbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_LogicBooleanFunction)


def test_behaviour_logicbooleanfunction_constructor_exists():
    assert callable(behaviour_LogicBooleanFunction.__init__)


def test_behaviour_logicbooleanfunction_constructor_args():
    sig = inspect.signature(behaviour_LogicBooleanFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour_logicbooleanfunction_has_functionName():
    assert hasattr(behaviour_LogicBooleanFunction, "functionName")
    descriptor = None
    for klass in behaviour_LogicBooleanFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_occupationbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_OccupationBooleanFunction)


def test_behaviour_occupationbooleanfunction_constructor_exists():
    assert callable(behaviour_OccupationBooleanFunction.__init__)


def test_behaviour_occupationbooleanfunction_constructor_args():
    sig = inspect.signature(behaviour_OccupationBooleanFunction.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_behaviour_occupationbooleanfunction_has_functionName():
    assert hasattr(behaviour_OccupationBooleanFunction, "functionName")
    descriptor = None
    for klass in behaviour_OccupationBooleanFunction.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_behavior_is_not_abstract():
    assert not inspect.isabstract(behaviour_Behavior)


def test_behaviour_behavior_constructor_exists():
    assert callable(behaviour_Behavior.__init__)


def test_behaviour_behavior_constructor_args():
    sig = inspect.signature(behaviour_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_behaviour_behavior_has_behaviorName():
    assert hasattr(behaviour_Behavior, "behaviorName")
    descriptor = None
    for klass in behaviour_Behavior.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_behavior_has_frequency():
    assert hasattr(behaviour_Behavior, "frequency")
    descriptor = None
    for klass in behaviour_Behavior.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_entityclass_is_not_abstract():
    assert not inspect.isabstract(behaviour_EntityClass)


def test_behaviour_entityclass_constructor_exists():
    assert callable(behaviour_EntityClass.__init__)


def test_behaviour_entityclass_constructor_args():
    sig = inspect.signature(behaviour_EntityClass.__init__)
    params = list(sig.parameters.keys())
    assert "entityName" in params, "Missing parameter 'entityName'"

def test_behaviour_entityclass_has_entityName():
    assert hasattr(behaviour_EntityClass, "entityName")
    descriptor = None
    for klass in behaviour_EntityClass.__mro__:
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



def test_behaviour_namedfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_NamedFunction)


def test_behaviour_namedfunction_constructor_exists():
    assert callable(behaviour_NamedFunction.__init__)


def test_behaviour_namedfunction_constructor_args():
    sig = inspect.signature(behaviour_NamedFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_anonymousfunction_is_not_abstract():
    assert not inspect.isabstract(behaviour_AnonymousFunction)


def test_behaviour_anonymousfunction_constructor_exists():
    assert callable(behaviour_AnonymousFunction.__init__)


def test_behaviour_anonymousfunction_constructor_args():
    sig = inspect.signature(behaviour_AnonymousFunction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_node_is_not_abstract():
    assert not inspect.isabstract(behaviour_Node)


def test_behaviour_node_constructor_exists():
    assert callable(behaviour_Node.__init__)


def test_behaviour_node_constructor_args():
    sig = inspect.signature(behaviour_Node.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_edge_is_not_abstract():
    assert not inspect.isabstract(behaviour_Edge)


def test_behaviour_edge_constructor_exists():
    assert callable(behaviour_Edge.__init__)


def test_behaviour_edge_constructor_args():
    sig = inspect.signature(behaviour_Edge.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_end_is_not_abstract():
    assert not inspect.isabstract(behaviour_End)


def test_behaviour_end_constructor_exists():
    assert callable(behaviour_End.__init__)


def test_behaviour_end_constructor_args():
    sig = inspect.signature(behaviour_End.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_start_is_not_abstract():
    assert not inspect.isabstract(behaviour_Start)


def test_behaviour_start_constructor_exists():
    assert callable(behaviour_Start.__init__)


def test_behaviour_start_constructor_args():
    sig = inspect.signature(behaviour_Start.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_primitiveactivity_is_not_abstract():
    assert not inspect.isabstract(behaviour_PrimitiveActivity)


def test_behaviour_primitiveactivity_constructor_exists():
    assert callable(behaviour_PrimitiveActivity.__init__)


def test_behaviour_primitiveactivity_constructor_args():
    sig = inspect.signature(behaviour_PrimitiveActivity.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_equation_is_not_abstract():
    assert not inspect.isabstract(behaviour_Equation)


def test_behaviour_equation_constructor_exists():
    assert callable(behaviour_Equation.__init__)


def test_behaviour_equation_constructor_args():
    sig = inspect.signature(behaviour_Equation.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_activitydiagrambehavior_is_not_abstract():
    assert not inspect.isabstract(behaviour_ActivityDiagramBehavior)


def test_behaviour_activitydiagrambehavior_constructor_exists():
    assert callable(behaviour_ActivityDiagramBehavior.__init__)


def test_behaviour_activitydiagrambehavior_constructor_args():
    sig = inspect.signature(behaviour_ActivityDiagramBehavior.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_equationbehaviour_is_not_abstract():
    assert not inspect.isabstract(behaviour_EquationBehaviour)


def test_behaviour_equationbehaviour_constructor_exists():
    assert callable(behaviour_EquationBehaviour.__init__)


def test_behaviour_equationbehaviour_constructor_args():
    sig = inspect.signature(behaviour_EquationBehaviour.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_duration_is_not_abstract():
    assert not inspect.isabstract(behaviour_Duration)


def test_behaviour_duration_constructor_exists():
    assert callable(behaviour_Duration.__init__)


def test_behaviour_duration_constructor_args():
    sig = inspect.signature(behaviour_Duration.__init__)
    params = list(sig.parameters.keys())
    assert "durationTime" in params, "Missing parameter 'durationTime'"

def test_behaviour_duration_has_durationTime():
    assert hasattr(behaviour_Duration, "durationTime")
    descriptor = None
    for klass in behaviour_Duration.__mro__:
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



def test_behaviour_parameterclass_is_not_abstract():
    assert not inspect.isabstract(behaviour_ParameterClass)


def test_behaviour_parameterclass_constructor_exists():
    assert callable(behaviour_ParameterClass.__init__)


def test_behaviour_parameterclass_constructor_args():
    sig = inspect.signature(behaviour_ParameterClass.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_attributeclass_is_not_abstract():
    assert not inspect.isabstract(behaviour_AttributeClass)


def test_behaviour_attributeclass_constructor_exists():
    assert callable(behaviour_AttributeClass.__init__)


def test_behaviour_attributeclass_constructor_args():
    sig = inspect.signature(behaviour_AttributeClass.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_type_is_not_abstract():
    assert not inspect.isabstract(behaviour_Type)


def test_behaviour_type_constructor_exists():
    assert callable(behaviour_Type.__init__)


def test_behaviour_type_constructor_args():
    sig = inspect.signature(behaviour_Type.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_behaviour_type_has_type():
    assert hasattr(behaviour_Type, "type")
    descriptor = None
    for klass in behaviour_Type.__mro__:
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



def test_behaviour_booleanprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour_BooleanPrimitive)


def test_behaviour_booleanprimitive_constructor_exists():
    assert callable(behaviour_BooleanPrimitive.__init__)


def test_behaviour_booleanprimitive_constructor_args():
    sig = inspect.signature(behaviour_BooleanPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour_booleanprimitive_has_primitive():
    assert hasattr(behaviour_BooleanPrimitive, "primitive")
    descriptor = None
    for klass in behaviour_BooleanPrimitive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_entitysetprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour_EntitySetPrimitive)


def test_behaviour_entitysetprimitive_constructor_exists():
    assert callable(behaviour_EntitySetPrimitive.__init__)


def test_behaviour_entitysetprimitive_constructor_args():
    sig = inspect.signature(behaviour_EntitySetPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour_entitysetprimitive_has_primitive():
    assert hasattr(behaviour_EntitySetPrimitive, "primitive")
    descriptor = None
    for klass in behaviour_EntitySetPrimitive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_locationprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour_LocationPrimitive)


def test_behaviour_locationprimitive_constructor_exists():
    assert callable(behaviour_LocationPrimitive.__init__)


def test_behaviour_locationprimitive_constructor_args():
    sig = inspect.signature(behaviour_LocationPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour_locationprimitive_has_primitive():
    assert hasattr(behaviour_LocationPrimitive, "primitive")
    descriptor = None
    for klass in behaviour_LocationPrimitive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_locationsetprimitive_is_not_abstract():
    assert not inspect.isabstract(behaviour_LocationSetPrimitive)


def test_behaviour_locationsetprimitive_constructor_exists():
    assert callable(behaviour_LocationSetPrimitive.__init__)


def test_behaviour_locationsetprimitive_constructor_args():
    sig = inspect.signature(behaviour_LocationSetPrimitive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour_locationsetprimitive_has_primitive():
    assert hasattr(behaviour_LocationSetPrimitive, "primitive")
    descriptor = None
    for klass in behaviour_LocationSetPrimitive.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_entityprimive_is_not_abstract():
    assert not inspect.isabstract(behaviour_EntityPrimive)


def test_behaviour_entityprimive_constructor_exists():
    assert callable(behaviour_EntityPrimive.__init__)


def test_behaviour_entityprimive_constructor_args():
    sig = inspect.signature(behaviour_EntityPrimive.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_behaviour_entityprimive_has_primitive():
    assert hasattr(behaviour_EntityPrimive, "primitive")
    descriptor = None
    for klass in behaviour_EntityPrimive.__mro__:
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



def test_behaviour_stringconstantexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_StringConstantExpression)


def test_behaviour_stringconstantexpression_constructor_exists():
    assert callable(behaviour_StringConstantExpression.__init__)


def test_behaviour_stringconstantexpression_constructor_args():
    sig = inspect.signature(behaviour_StringConstantExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_behaviour_stringconstantexpression_has_value():
    assert hasattr(behaviour_StringConstantExpression, "value")
    descriptor = None
    for klass in behaviour_StringConstantExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_floatconstantexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_FloatConstantExpression)


def test_behaviour_floatconstantexpression_constructor_exists():
    assert callable(behaviour_FloatConstantExpression.__init__)


def test_behaviour_floatconstantexpression_constructor_args():
    sig = inspect.signature(behaviour_FloatConstantExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_behaviour_floatconstantexpression_has_value():
    assert hasattr(behaviour_FloatConstantExpression, "value")
    descriptor = None
    for klass in behaviour_FloatConstantExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_intconstantexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_IntConstantExpression)


def test_behaviour_intconstantexpression_constructor_exists():
    assert callable(behaviour_IntConstantExpression.__init__)


def test_behaviour_intconstantexpression_constructor_args():
    sig = inspect.signature(behaviour_IntConstantExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_behaviour_intconstantexpression_has_value():
    assert hasattr(behaviour_IntConstantExpression, "value")
    descriptor = None
    for klass in behaviour_IntConstantExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_function_is_not_abstract():
    assert not inspect.isabstract(behaviour_Function)


def test_behaviour_function_constructor_exists():
    assert callable(behaviour_Function.__init__)


def test_behaviour_function_constructor_args():
    sig = inspect.signature(behaviour_Function.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_locationexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_LocationExpression)


def test_behaviour_locationexpression_constructor_exists():
    assert callable(behaviour_LocationExpression.__init__)


def test_behaviour_locationexpression_constructor_args():
    sig = inspect.signature(behaviour_LocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_constantexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_ConstantExpression)


def test_behaviour_constantexpression_constructor_exists():
    assert callable(behaviour_ConstantExpression.__init__)


def test_behaviour_constantexpression_constructor_args():
    sig = inspect.signature(behaviour_ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_FunctionCallExpression)


def test_behaviour_functioncallexpression_constructor_exists():
    assert callable(behaviour_FunctionCallExpression.__init__)


def test_behaviour_functioncallexpression_constructor_args():
    sig = inspect.signature(behaviour_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_PrimitiveExpression)


def test_behaviour_primitiveexpression_constructor_exists():
    assert callable(behaviour_PrimitiveExpression.__init__)


def test_behaviour_primitiveexpression_constructor_args():
    sig = inspect.signature(behaviour_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_variableclass_is_not_abstract():
    assert not inspect.isabstract(behaviour_VariableClass)


def test_behaviour_variableclass_constructor_exists():
    assert callable(behaviour_VariableClass.__init__)


def test_behaviour_variableclass_constructor_args():
    sig = inspect.signature(behaviour_VariableClass.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_behaviour_variableclass_has_variableName():
    assert hasattr(behaviour_VariableClass, "variableName")
    descriptor = None
    for klass in behaviour_VariableClass.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_expression_is_not_abstract():
    assert not inspect.isabstract(behaviour_Expression)


def test_behaviour_expression_constructor_exists():
    assert callable(behaviour_Expression.__init__)


def test_behaviour_expression_constructor_args():
    sig = inspect.signature(behaviour_Expression.__init__)
    params = list(sig.parameters.keys())

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

def test_logicbooleanfunctionenum_exists():
    # Check that the Enumeration exists
    assert LogicBooleanFunctionEnum is not None

def test_logicbooleanfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicBooleanFunctionEnum]
    expected_literals = [
        "NOT",
        "OR",
        "AND",
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

def test_unarylocationfunctionenum_exists():
    # Check that the Enumeration exists
    assert UnaryLocationFunctionEnum is not None

def test_unarylocationfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryLocationFunctionEnum]
    expected_literals = [
        "BottomLocation",
        "TopRightLocation",
        "RightLocation",
        "RandomLocation",
        "RandomNeighbourhoodLocation",
        "BottomRightLocation",
        "TopLocation",
        "LeftLocation",
        "BottomLeftLocation",
        "TopLeftLocation",
        "OneOf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryLocationFunctionEnum"

def test_durationtypeenum_exists():
    # Check that the Enumeration exists
    assert DurationTypeEnum is not None

def test_durationtypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DurationTypeEnum]
    expected_literals = [
        "monthly",
        "weekly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DurationTypeEnum"

def test_comparisonbooleanfunctionenum_exists():
    # Check that the Enumeration exists
    assert ComparisonBooleanFunctionEnum is not None

def test_comparisonbooleanfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonBooleanFunctionEnum]
    expected_literals = [
        "GreaterThan",
        "Equal",
        "GreaterOrEequalThan",
        "LessThan",
        "NotEqual",
        "LessOrEqualThan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonBooleanFunctionEnum"

def test_arithmeticfunctionenum_exists():
    # Check that the Enumeration exists
    assert ArithmeticFunctionEnum is not None

def test_arithmeticfunctionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticFunctionEnum]
    expected_literals = [
        "Minus",
        "Times",
        "Division",
        "Sum",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticFunctionEnum"

def test_weekdaysenum_exists():
    # Check that the Enumeration exists
    assert WeekDaysEnum is not None

def test_weekdaysenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WeekDaysEnum]
    expected_literals = [
        "sunday",
        "tuesday",
        "saturday",
        "monday",
        "friday",
        "thursday",
        "wednesday",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WeekDaysEnum"

def test_monthsenum_exists():
    # Check that the Enumeration exists
    assert MonthsEnum is not None

def test_monthsenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MonthsEnum]
    expected_literals = [
        "July",
        "October",
        "March",
        "May",
        "August",
        "June",
        "January",
        "April",
        "September",
        "December",
        "November",
        "Februrary",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MonthsEnum"

def test_unarylocationenum_exists():
    # Check that the Enumeration exists
    assert UnaryLocationEnum is not None

def test_unarylocationenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryLocationEnum]
    expected_literals = [
        "toplocation",
        "oneof",
        "oneofneighbour",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryLocationEnum"

def test_locationprimiveenum_exists():
    # Check that the Enumeration exists
    assert LocationPrimiveEnum is not None

def test_locationprimiveenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationPrimiveEnum]
    expected_literals = [
        "left",
        "top",
        "here",
        "bottom",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationPrimiveEnum"

def test_typeenum_exists():
    # Check that the Enumeration exists
    assert TypeEnum is not None

def test_typeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeEnum]
    expected_literals = [
        "entity",
        "location",
        "float",
        "int",
        "entityset",
        "boolean",
        "locationset",
        "string",
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

def test_entitysetprimiveenum_exists():
    # Check that the Enumeration exists
    assert EntitySetPrimiveEnum is not None

def test_entitysetprimiveenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntitySetPrimiveEnum]
    expected_literals = [
        "neighbours",
        "all",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntitySetPrimiveEnum"

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
behaviour_UnaryFunction_strategy = st.builds(
    behaviour_UnaryFunction,
)
behaviour_BinaryFunction_strategy = st.builds(
    behaviour_BinaryFunction,
)
Duration_strategy = st.builds(
    Duration,
)
behaviour_MonthDuration_strategy = st.builds(
    behaviour_MonthDuration,
    month=
        safe_text
)
behaviour_NumericPrimitive_strategy = st.builds(
    behaviour_NumericPrimitive,
)
TimeExpression_strategy = st.builds(
    TimeExpression,
)
behaviour_While_strategy = st.builds(
    behaviour_While,
)
LocationExpression_strategy = st.builds(
    LocationExpression,
)
behaviour_CoordinateLocationExpression_strategy = st.builds(
    behaviour_CoordinateLocationExpression,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_NameLocationExpression_strategy = st.builds(
    behaviour_NameLocationExpression,
    name=
        safe_text
)
BinaryBooleanFunction_strategy = st.builds(
    BinaryBooleanFunction,
)
behaviour_ComparisonBooleanFunction_strategy = st.builds(
    behaviour_ComparisonBooleanFunction,
    functionName=
        safe_text
)
BinaryFunction_strategy = st.builds(
    BinaryFunction,
)
behaviour_BinaryArithmeticFunction_strategy = st.builds(
    behaviour_BinaryArithmeticFunction,
    functionName=
        safe_text
)
behaviour_BinaryLocationFunction_strategy = st.builds(
    behaviour_BinaryLocationFunction,
)
behaviour_BinaryBooleanFunction_strategy = st.builds(
    behaviour_BinaryBooleanFunction,
)
UnaryFunction_strategy = st.builds(
    UnaryFunction,
)
behaviour_UnaryNumericFunction_strategy = st.builds(
    behaviour_UnaryNumericFunction,
    functionName=
        safe_text
)
behaviour_UnaryEntityFunction_strategy = st.builds(
    behaviour_UnaryEntityFunction,
    functionName=
        safe_text
)
behaviour_UnaryLocationFunction_strategy = st.builds(
    behaviour_UnaryLocationFunction,
    functionName=
        safe_text
)
behaviour_UnaryStringFunction_strategy = st.builds(
    behaviour_UnaryStringFunction,
    functionName=
        safe_text
)
Edge_strategy = st.builds(
    Edge,
)
behaviour_TrueEdge_strategy = st.builds(
    behaviour_TrueEdge,
)
behaviour_FalseEdge_strategy = st.builds(
    behaviour_FalseEdge,
)
behaviour_UnconditionedEdge_strategy = st.builds(
    behaviour_UnconditionedEdge,
)
PrimitiveActivity_strategy = st.builds(
    PrimitiveActivity,
)
behaviour_Die_strategy = st.builds(
    behaviour_Die,
)
behaviour_Reproduce_strategy = st.builds(
    behaviour_Reproduce,
)
behaviour_Remove_strategy = st.builds(
    behaviour_Remove,
)
behaviour_Add_strategy = st.builds(
    behaviour_Add,
)
behaviour_Move_strategy = st.builds(
    behaviour_Move,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
behaviour_Join_strategy = st.builds(
    behaviour_Join,
)
behaviour_Decision_strategy = st.builds(
    behaviour_Decision,
)
behaviour_Merge_strategy = st.builds(
    behaviour_Merge,
)
behaviour_Fork_strategy = st.builds(
    behaviour_Fork,
)
behaviour_TimeExpression_strategy = st.builds(
    behaviour_TimeExpression,
)
Node_strategy = st.builds(
    Node,
)
behaviour_ExecutableNode_strategy = st.builds(
    behaviour_ExecutableNode,
)
behaviour_ControlNode_strategy = st.builds(
    behaviour_ControlNode,
)
behaviour_LogicBooleanFunction_strategy = st.builds(
    behaviour_LogicBooleanFunction,
    functionName=
        safe_text
)
behaviour_OccupationBooleanFunction_strategy = st.builds(
    behaviour_OccupationBooleanFunction,
    functionName=
        safe_text
)
behaviour_Behavior_strategy = st.builds(
    behaviour_Behavior,
    behaviorName=
        safe_text,
    frequency=
        safe_text
)
behaviour_EntityClass_strategy = st.builds(
    behaviour_EntityClass,
    entityName=
        safe_text
)
Function_strategy = st.builds(
    Function,
)
behaviour_NamedFunction_strategy = st.builds(
    behaviour_NamedFunction,
)
behaviour_AnonymousFunction_strategy = st.builds(
    behaviour_AnonymousFunction,
)
behaviour_Node_strategy = st.builds(
    behaviour_Node,
)
behaviour_Edge_strategy = st.builds(
    behaviour_Edge,
)
behaviour_End_strategy = st.builds(
    behaviour_End,
)
behaviour_Start_strategy = st.builds(
    behaviour_Start,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
behaviour_PrimitiveActivity_strategy = st.builds(
    behaviour_PrimitiveActivity,
)
behaviour_Equation_strategy = st.builds(
    behaviour_Equation,
)
Behavior_strategy = st.builds(
    Behavior,
)
behaviour_ActivityDiagramBehavior_strategy = st.builds(
    behaviour_ActivityDiagramBehavior,
)
behaviour_EquationBehaviour_strategy = st.builds(
    behaviour_EquationBehaviour,
)
behaviour_Duration_strategy = st.builds(
    behaviour_Duration,
    durationTime=
        st.integers()
)
VariableClass_strategy = st.builds(
    VariableClass,
)
behaviour_ParameterClass_strategy = st.builds(
    behaviour_ParameterClass,
)
behaviour_AttributeClass_strategy = st.builds(
    behaviour_AttributeClass,
)
behaviour_Type_strategy = st.builds(
    behaviour_Type,
    type=
        safe_text
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
behaviour_BooleanPrimitive_strategy = st.builds(
    behaviour_BooleanPrimitive,
    primitive=
        safe_text
)
behaviour_EntitySetPrimitive_strategy = st.builds(
    behaviour_EntitySetPrimitive,
    primitive=
        safe_text
)
behaviour_LocationPrimitive_strategy = st.builds(
    behaviour_LocationPrimitive,
    primitive=
        safe_text
)
behaviour_LocationSetPrimitive_strategy = st.builds(
    behaviour_LocationSetPrimitive,
    primitive=
        safe_text
)
behaviour_EntityPrimive_strategy = st.builds(
    behaviour_EntityPrimive,
    primitive=
        safe_text
)
ConstantExpression_strategy = st.builds(
    ConstantExpression,
)
behaviour_StringConstantExpression_strategy = st.builds(
    behaviour_StringConstantExpression,
    value=
        safe_text
)
behaviour_FloatConstantExpression_strategy = st.builds(
    behaviour_FloatConstantExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_IntConstantExpression_strategy = st.builds(
    behaviour_IntConstantExpression,
    value=
        st.integers()
)
behaviour_Function_strategy = st.builds(
    behaviour_Function,
)
Expression_strategy = st.builds(
    Expression,
)
behaviour_LocationExpression_strategy = st.builds(
    behaviour_LocationExpression,
)
behaviour_ConstantExpression_strategy = st.builds(
    behaviour_ConstantExpression,
)
behaviour_FunctionCallExpression_strategy = st.builds(
    behaviour_FunctionCallExpression,
)
behaviour_PrimitiveExpression_strategy = st.builds(
    behaviour_PrimitiveExpression,
)
behaviour_VariableClass_strategy = st.builds(
    behaviour_VariableClass,
    variableName=
        safe_text
)
behaviour_Expression_strategy = st.builds(
    behaviour_Expression,
)

@given(instance=NamedFunction_strategy)
@settings(max_examples=50)
def test_namedfunction_instantiation(instance):
    assert isinstance(instance, NamedFunction)

@given(instance=behaviour_UnaryFunction_strategy)
@settings(max_examples=50)
def test_behaviour_unaryfunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryFunction)

@given(instance=behaviour_BinaryFunction_strategy)
@settings(max_examples=50)
def test_behaviour_binaryfunction_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryFunction)

@given(instance=Duration_strategy)
@settings(max_examples=50)
def test_duration_instantiation(instance):
    assert isinstance(instance, Duration)

@given(instance=behaviour_MonthDuration_strategy)
@settings(max_examples=50)
def test_behaviour_monthduration_instantiation(instance):
    assert isinstance(instance, behaviour_MonthDuration)



@given(instance=behaviour_MonthDuration_strategy)
def test_behaviour_monthduration_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=behaviour_NumericPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour_numericprimitive_instantiation(instance):
    assert isinstance(instance, behaviour_NumericPrimitive)

@given(instance=TimeExpression_strategy)
@settings(max_examples=50)
def test_timeexpression_instantiation(instance):
    assert isinstance(instance, TimeExpression)

@given(instance=behaviour_While_strategy)
@settings(max_examples=50)
def test_behaviour_while_instantiation(instance):
    assert isinstance(instance, behaviour_While)

@given(instance=LocationExpression_strategy)
@settings(max_examples=50)
def test_locationexpression_instantiation(instance):
    assert isinstance(instance, LocationExpression)

@given(instance=behaviour_CoordinateLocationExpression_strategy)
@settings(max_examples=50)
def test_behaviour_coordinatelocationexpression_instantiation(instance):
    assert isinstance(instance, behaviour_CoordinateLocationExpression)



@given(instance=behaviour_CoordinateLocationExpression_strategy)
def test_behaviour_coordinatelocationexpression_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=behaviour_CoordinateLocationExpression_strategy)
def test_behaviour_coordinatelocationexpression_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=behaviour_NameLocationExpression_strategy)
@settings(max_examples=50)
def test_behaviour_namelocationexpression_instantiation(instance):
    assert isinstance(instance, behaviour_NameLocationExpression)



@given(instance=behaviour_NameLocationExpression_strategy)
def test_behaviour_namelocationexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BinaryBooleanFunction_strategy)
@settings(max_examples=50)
def test_binarybooleanfunction_instantiation(instance):
    assert isinstance(instance, BinaryBooleanFunction)

@given(instance=behaviour_ComparisonBooleanFunction_strategy)
@settings(max_examples=50)
def test_behaviour_comparisonbooleanfunction_instantiation(instance):
    assert isinstance(instance, behaviour_ComparisonBooleanFunction)



@given(instance=behaviour_ComparisonBooleanFunction_strategy)
def test_behaviour_comparisonbooleanfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=BinaryFunction_strategy)
@settings(max_examples=50)
def test_binaryfunction_instantiation(instance):
    assert isinstance(instance, BinaryFunction)

@given(instance=behaviour_BinaryArithmeticFunction_strategy)
@settings(max_examples=50)
def test_behaviour_binaryarithmeticfunction_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryArithmeticFunction)



@given(instance=behaviour_BinaryArithmeticFunction_strategy)
def test_behaviour_binaryarithmeticfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour_BinaryLocationFunction_strategy)
@settings(max_examples=50)
def test_behaviour_binarylocationfunction_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryLocationFunction)

@given(instance=behaviour_BinaryBooleanFunction_strategy)
@settings(max_examples=50)
def test_behaviour_binarybooleanfunction_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryBooleanFunction)

@given(instance=UnaryFunction_strategy)
@settings(max_examples=50)
def test_unaryfunction_instantiation(instance):
    assert isinstance(instance, UnaryFunction)

@given(instance=behaviour_UnaryNumericFunction_strategy)
@settings(max_examples=50)
def test_behaviour_unarynumericfunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryNumericFunction)



@given(instance=behaviour_UnaryNumericFunction_strategy)
def test_behaviour_unarynumericfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour_UnaryEntityFunction_strategy)
@settings(max_examples=50)
def test_behaviour_unaryentityfunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryEntityFunction)



@given(instance=behaviour_UnaryEntityFunction_strategy)
def test_behaviour_unaryentityfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour_UnaryLocationFunction_strategy)
@settings(max_examples=50)
def test_behaviour_unarylocationfunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryLocationFunction)



@given(instance=behaviour_UnaryLocationFunction_strategy)
def test_behaviour_unarylocationfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour_UnaryStringFunction_strategy)
@settings(max_examples=50)
def test_behaviour_unarystringfunction_instantiation(instance):
    assert isinstance(instance, behaviour_UnaryStringFunction)



@given(instance=behaviour_UnaryStringFunction_strategy)
def test_behaviour_unarystringfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=behaviour_TrueEdge_strategy)
@settings(max_examples=50)
def test_behaviour_trueedge_instantiation(instance):
    assert isinstance(instance, behaviour_TrueEdge)

@given(instance=behaviour_FalseEdge_strategy)
@settings(max_examples=50)
def test_behaviour_falseedge_instantiation(instance):
    assert isinstance(instance, behaviour_FalseEdge)

@given(instance=behaviour_UnconditionedEdge_strategy)
@settings(max_examples=50)
def test_behaviour_unconditionededge_instantiation(instance):
    assert isinstance(instance, behaviour_UnconditionedEdge)

@given(instance=PrimitiveActivity_strategy)
@settings(max_examples=50)
def test_primitiveactivity_instantiation(instance):
    assert isinstance(instance, PrimitiveActivity)

@given(instance=behaviour_Die_strategy)
@settings(max_examples=50)
def test_behaviour_die_instantiation(instance):
    assert isinstance(instance, behaviour_Die)

@given(instance=behaviour_Reproduce_strategy)
@settings(max_examples=50)
def test_behaviour_reproduce_instantiation(instance):
    assert isinstance(instance, behaviour_Reproduce)

@given(instance=behaviour_Remove_strategy)
@settings(max_examples=50)
def test_behaviour_remove_instantiation(instance):
    assert isinstance(instance, behaviour_Remove)

@given(instance=behaviour_Add_strategy)
@settings(max_examples=50)
def test_behaviour_add_instantiation(instance):
    assert isinstance(instance, behaviour_Add)

@given(instance=behaviour_Move_strategy)
@settings(max_examples=50)
def test_behaviour_move_instantiation(instance):
    assert isinstance(instance, behaviour_Move)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=behaviour_Join_strategy)
@settings(max_examples=50)
def test_behaviour_join_instantiation(instance):
    assert isinstance(instance, behaviour_Join)

@given(instance=behaviour_Decision_strategy)
@settings(max_examples=50)
def test_behaviour_decision_instantiation(instance):
    assert isinstance(instance, behaviour_Decision)

@given(instance=behaviour_Merge_strategy)
@settings(max_examples=50)
def test_behaviour_merge_instantiation(instance):
    assert isinstance(instance, behaviour_Merge)

@given(instance=behaviour_Fork_strategy)
@settings(max_examples=50)
def test_behaviour_fork_instantiation(instance):
    assert isinstance(instance, behaviour_Fork)

@given(instance=behaviour_TimeExpression_strategy)
@settings(max_examples=50)
def test_behaviour_timeexpression_instantiation(instance):
    assert isinstance(instance, behaviour_TimeExpression)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=behaviour_ExecutableNode_strategy)
@settings(max_examples=50)
def test_behaviour_executablenode_instantiation(instance):
    assert isinstance(instance, behaviour_ExecutableNode)

@given(instance=behaviour_ControlNode_strategy)
@settings(max_examples=50)
def test_behaviour_controlnode_instantiation(instance):
    assert isinstance(instance, behaviour_ControlNode)

@given(instance=behaviour_LogicBooleanFunction_strategy)
@settings(max_examples=50)
def test_behaviour_logicbooleanfunction_instantiation(instance):
    assert isinstance(instance, behaviour_LogicBooleanFunction)



@given(instance=behaviour_LogicBooleanFunction_strategy)
def test_behaviour_logicbooleanfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour_OccupationBooleanFunction_strategy)
@settings(max_examples=50)
def test_behaviour_occupationbooleanfunction_instantiation(instance):
    assert isinstance(instance, behaviour_OccupationBooleanFunction)



@given(instance=behaviour_OccupationBooleanFunction_strategy)
def test_behaviour_occupationbooleanfunction_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=behaviour_Behavior_strategy)
@settings(max_examples=50)
def test_behaviour_behavior_instantiation(instance):
    assert isinstance(instance, behaviour_Behavior)



@given(instance=behaviour_Behavior_strategy)
def test_behaviour_behavior_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original



@given(instance=behaviour_Behavior_strategy)
def test_behaviour_behavior_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=behaviour_EntityClass_strategy)
@settings(max_examples=50)
def test_behaviour_entityclass_instantiation(instance):
    assert isinstance(instance, behaviour_EntityClass)



@given(instance=behaviour_EntityClass_strategy)
def test_behaviour_entityclass_entityName_setter(instance):
    original = instance.entityName
    instance.entityName = original
    assert instance.entityName == original

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=behaviour_NamedFunction_strategy)
@settings(max_examples=50)
def test_behaviour_namedfunction_instantiation(instance):
    assert isinstance(instance, behaviour_NamedFunction)

@given(instance=behaviour_AnonymousFunction_strategy)
@settings(max_examples=50)
def test_behaviour_anonymousfunction_instantiation(instance):
    assert isinstance(instance, behaviour_AnonymousFunction)

@given(instance=behaviour_Node_strategy)
@settings(max_examples=50)
def test_behaviour_node_instantiation(instance):
    assert isinstance(instance, behaviour_Node)

@given(instance=behaviour_Edge_strategy)
@settings(max_examples=50)
def test_behaviour_edge_instantiation(instance):
    assert isinstance(instance, behaviour_Edge)

@given(instance=behaviour_End_strategy)
@settings(max_examples=50)
def test_behaviour_end_instantiation(instance):
    assert isinstance(instance, behaviour_End)

@given(instance=behaviour_Start_strategy)
@settings(max_examples=50)
def test_behaviour_start_instantiation(instance):
    assert isinstance(instance, behaviour_Start)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=behaviour_PrimitiveActivity_strategy)
@settings(max_examples=50)
def test_behaviour_primitiveactivity_instantiation(instance):
    assert isinstance(instance, behaviour_PrimitiveActivity)

@given(instance=behaviour_Equation_strategy)
@settings(max_examples=50)
def test_behaviour_equation_instantiation(instance):
    assert isinstance(instance, behaviour_Equation)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=behaviour_ActivityDiagramBehavior_strategy)
@settings(max_examples=50)
def test_behaviour_activitydiagrambehavior_instantiation(instance):
    assert isinstance(instance, behaviour_ActivityDiagramBehavior)

@given(instance=behaviour_EquationBehaviour_strategy)
@settings(max_examples=50)
def test_behaviour_equationbehaviour_instantiation(instance):
    assert isinstance(instance, behaviour_EquationBehaviour)

@given(instance=behaviour_Duration_strategy)
@settings(max_examples=50)
def test_behaviour_duration_instantiation(instance):
    assert isinstance(instance, behaviour_Duration)



@given(instance=behaviour_Duration_strategy)
def test_behaviour_duration_durationTime_setter(instance):
    original = instance.durationTime
    instance.durationTime = original
    assert instance.durationTime == original

@given(instance=VariableClass_strategy)
@settings(max_examples=50)
def test_variableclass_instantiation(instance):
    assert isinstance(instance, VariableClass)

@given(instance=behaviour_ParameterClass_strategy)
@settings(max_examples=50)
def test_behaviour_parameterclass_instantiation(instance):
    assert isinstance(instance, behaviour_ParameterClass)

@given(instance=behaviour_AttributeClass_strategy)
@settings(max_examples=50)
def test_behaviour_attributeclass_instantiation(instance):
    assert isinstance(instance, behaviour_AttributeClass)

@given(instance=behaviour_Type_strategy)
@settings(max_examples=50)
def test_behaviour_type_instantiation(instance):
    assert isinstance(instance, behaviour_Type)



@given(instance=behaviour_Type_strategy)
def test_behaviour_type_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=behaviour_BooleanPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour_booleanprimitive_instantiation(instance):
    assert isinstance(instance, behaviour_BooleanPrimitive)



@given(instance=behaviour_BooleanPrimitive_strategy)
def test_behaviour_booleanprimitive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=behaviour_EntitySetPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour_entitysetprimitive_instantiation(instance):
    assert isinstance(instance, behaviour_EntitySetPrimitive)



@given(instance=behaviour_EntitySetPrimitive_strategy)
def test_behaviour_entitysetprimitive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=behaviour_LocationPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour_locationprimitive_instantiation(instance):
    assert isinstance(instance, behaviour_LocationPrimitive)



@given(instance=behaviour_LocationPrimitive_strategy)
def test_behaviour_locationprimitive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=behaviour_LocationSetPrimitive_strategy)
@settings(max_examples=50)
def test_behaviour_locationsetprimitive_instantiation(instance):
    assert isinstance(instance, behaviour_LocationSetPrimitive)



@given(instance=behaviour_LocationSetPrimitive_strategy)
def test_behaviour_locationsetprimitive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=behaviour_EntityPrimive_strategy)
@settings(max_examples=50)
def test_behaviour_entityprimive_instantiation(instance):
    assert isinstance(instance, behaviour_EntityPrimive)



@given(instance=behaviour_EntityPrimive_strategy)
def test_behaviour_entityprimive_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=ConstantExpression_strategy)
@settings(max_examples=50)
def test_constantexpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)

@given(instance=behaviour_StringConstantExpression_strategy)
@settings(max_examples=50)
def test_behaviour_stringconstantexpression_instantiation(instance):
    assert isinstance(instance, behaviour_StringConstantExpression)



@given(instance=behaviour_StringConstantExpression_strategy)
def test_behaviour_stringconstantexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behaviour_FloatConstantExpression_strategy)
@settings(max_examples=50)
def test_behaviour_floatconstantexpression_instantiation(instance):
    assert isinstance(instance, behaviour_FloatConstantExpression)



@given(instance=behaviour_FloatConstantExpression_strategy)
def test_behaviour_floatconstantexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behaviour_IntConstantExpression_strategy)
@settings(max_examples=50)
def test_behaviour_intconstantexpression_instantiation(instance):
    assert isinstance(instance, behaviour_IntConstantExpression)



@given(instance=behaviour_IntConstantExpression_strategy)
def test_behaviour_intconstantexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=behaviour_Function_strategy)
@settings(max_examples=50)
def test_behaviour_function_instantiation(instance):
    assert isinstance(instance, behaviour_Function)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=behaviour_LocationExpression_strategy)
@settings(max_examples=50)
def test_behaviour_locationexpression_instantiation(instance):
    assert isinstance(instance, behaviour_LocationExpression)

@given(instance=behaviour_ConstantExpression_strategy)
@settings(max_examples=50)
def test_behaviour_constantexpression_instantiation(instance):
    assert isinstance(instance, behaviour_ConstantExpression)

@given(instance=behaviour_FunctionCallExpression_strategy)
@settings(max_examples=50)
def test_behaviour_functioncallexpression_instantiation(instance):
    assert isinstance(instance, behaviour_FunctionCallExpression)

@given(instance=behaviour_PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_behaviour_primitiveexpression_instantiation(instance):
    assert isinstance(instance, behaviour_PrimitiveExpression)

@given(instance=behaviour_VariableClass_strategy)
@settings(max_examples=50)
def test_behaviour_variableclass_instantiation(instance):
    assert isinstance(instance, behaviour_VariableClass)



@given(instance=behaviour_VariableClass_strategy)
def test_behaviour_variableclass_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=behaviour_Expression_strategy)
@settings(max_examples=50)
def test_behaviour_expression_instantiation(instance):
    assert isinstance(instance, behaviour_Expression)
