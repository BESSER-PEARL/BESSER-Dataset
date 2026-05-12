import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FloatType,
    OPLmetamodel_Error,
    OPLmetamodel_Entity,
    OPLmetamodel_FunctionRef,
    Constraint,
    OPLmetamodel_ForAllConstraint,
    NumericExpression,
    OPLmetamodel_FloatExpression,
    OPLmetamodel_ParameterDomain,
    NumericType,
    OPLmetamodel_FloatType,
    RangeType,
    OPLmetamodel_FloatRangeType,
    Initialization,
    OPLmetamodel_DataObject,
    OPLmetamodel_DataInitMethods,
    OPLmetamodel_Initialization,
    SetType,
    OPLmetamodel_EnumerationType,
    OPLmetamodel_ParameterDeclaration,
    OPLmetamodel_DisplayInstruction,
    AbstractType,
    OPLmetamodel_DeferredInit,
    OPLmetamodel_Declaration,
    DefinedType,
    OPLmetamodel_ArrayType,
    CollectionExpression,
    OPLmetamodel_Extension,
    OPLmetamodel_Comprehension,
    Function,
    OPLmetamodel_CumulativeFunction,
    OPLmetamodel_BuiltInFunction,
    PrimitiveType,
    OPLmetamodel_BooleanType,
    PrimitiveExpression,
    OPLmetamodel_EnumLiteral,
    OPLmetamodel_BooleanExpression,
    OPLmetamodel_BooleanBlock,
    Reference,
    OPLmetamodel_DataRef,
    OPLmetamodel_BindingRef,
    AbstractBinaryOperator,
    OPLmetamodel_BinaryOperator,
    OPLmetamodel_TupleBinding,
    OPLmetamodel_StringType,
    OPLmetamodel_StringExpression,
    PiecewiseLinearFunction,
    OPLmetamodel_StateFunction,
    ScriptStatement,
    OPLmetamodel_Writeln,
    OPLmetamodel_VariableBinding,
    OPLmetamodel_RelationalInit,
    BooleanExpression,
    BinaryExpression,
    OPLmetamodel_RelationalExpression,
    BuiltInFunction,
    OPLmetamodel_ReflectiveFunction,
    OPLmetamodel_Sequence,
    OPLmetamodel_ScriptStatement,
    OPLmetamodel_RelationalOperator,
    DataInitMethods,
    OPLmetamodel_QueryUser,
    OPLmetamodel_PrimitiveType,
    OPLmetamodel_PositiveFloatType,
    OPLmetamodel_PiecewiseLinearFunction,
    OPLmetamodel_PiecewiseExpression,
    OPLmetamodel_RecordField,
    ParameterDomain,
    OPLmetamodel_SetType,
    OPLmetamodel_Record,
    OPLmetamodel_ReadFile,
    OPLmetamodel_RangeExpression,
    OPLmetamodel_Model,
    OPLmetamodel_ParameterRef,
    OPLmetamodel_Operator,
    OPLmetamodel_NumericExpression,
    OPLmetamodel_SearchProcedure,
    OPLmetamodel_IfConstraint,
    IntegerType,
    OPLmetamodel_PositiveIntegerType,
    OPLmetamodel_IntegerRangeType,
    OPLmetamodel_IntegerExpression,
    OPLmetamodel_StepFunction,
    OPLmetamodel_NumericType,
    OPLmetamodel_RangeType,
    OPLmetamodel_Interval,
    OPLmetamodel_IntegerType,
    OPLmetamodel_In,
    OPLmetamodel_AbstractBinaryOperator,
    PathExpression,
    OPLmetamodel_PathDereference,
    OPLmetamodel_FunctionCall,
    OPLmetamodel_ArrayDereference,
    OPLmetamodel_AllExpression,
    OPLmetamodel_Expression,
    OPLmetamodel_FormalParameter,
    Expression,
    OPLmetamodel_IfExpression,
    OPLmetamodel_RecordValue,
    OPLmetamodel_Reference,
    OPLmetamodel_PathExpression,
    OPLmetamodel_BlockExpression,
    OPLmetamodel_BinaryExpression,
    OPLmetamodel_IndexValuePair,
    OPLmetamodel_PrimitiveExpression,
    OPLmetamodel_CollectionExpression,
    OPLmetamodel_UnaryExpression,
    OPLmetamodel_ArrayValue,
    OPLmetamodel_ArraySlotConstraint,
    OPLmetamodel_SetValue,
    OPLmetamodel_AggregateExp,
    OPLmetamodel_Number,
    Declaration,
    OPLmetamodel_Constraint,
    OPLmetamodel_DefinedType,
    OPLmetamodel_Function,
    OPLmetamodel_Assertion,
    OPLmetamodel_ScheduleInitialization,
    OPLmetamodel_DataDeclaration,
    OPLmetamodel_Script,
    OPLmetamodel_ResourceDeclaration,
    OPLmetamodel_Objective,
    OPLmetamodel_Setting,
    OPLmetamodel_ActivityDeclaration,
    OPLmetamodel_AbstractType,
    BinaryOp,
    MembershipOp,
    Quantifier,
    OptimizationMode,
    LogicalOp,
    UnaryOp,
    RelationalOp,
    AggOp,
    SetOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_floattype_is_not_abstract():
    assert not inspect.isabstract(FloatType)


def test_floattype_constructor_exists():
    assert callable(FloatType.__init__)


def test_floattype_constructor_args():
    sig = inspect.signature(FloatType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_error_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Error)


def test_oplmetamodel_error_constructor_exists():
    assert callable(OPLmetamodel_Error.__init__)


def test_oplmetamodel_error_constructor_args():
    sig = inspect.signature(OPLmetamodel_Error.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_entity_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Entity)


def test_oplmetamodel_entity_constructor_exists():
    assert callable(OPLmetamodel_Entity.__init__)


def test_oplmetamodel_entity_constructor_args():
    sig = inspect.signature(OPLmetamodel_Entity.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_functionref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FunctionRef)


def test_oplmetamodel_functionref_constructor_exists():
    assert callable(OPLmetamodel_FunctionRef.__init__)


def test_oplmetamodel_functionref_constructor_args():
    sig = inspect.signature(OPLmetamodel_FunctionRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel_functionref_has_name():
    assert hasattr(OPLmetamodel_FunctionRef, "name")
    descriptor = None
    for klass in OPLmetamodel_FunctionRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_forallconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ForAllConstraint)


def test_oplmetamodel_forallconstraint_constructor_exists():
    assert callable(OPLmetamodel_ForAllConstraint.__init__)


def test_oplmetamodel_forallconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel_ForAllConstraint.__init__)
    params = list(sig.parameters.keys())



def test_numericexpression_is_not_abstract():
    assert not inspect.isabstract(NumericExpression)


def test_numericexpression_constructor_exists():
    assert callable(NumericExpression.__init__)


def test_numericexpression_constructor_args():
    sig = inspect.signature(NumericExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_floatexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FloatExpression)


def test_oplmetamodel_floatexpression_constructor_exists():
    assert callable(OPLmetamodel_FloatExpression.__init__)


def test_oplmetamodel_floatexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_FloatExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel_floatexpression_has_body():
    assert hasattr(OPLmetamodel_FloatExpression, "body")
    descriptor = None
    for klass in OPLmetamodel_FloatExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_parameterdomain_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ParameterDomain)


def test_oplmetamodel_parameterdomain_constructor_exists():
    assert callable(OPLmetamodel_ParameterDomain.__init__)


def test_oplmetamodel_parameterdomain_constructor_args():
    sig = inspect.signature(OPLmetamodel_ParameterDomain.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_floattype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FloatType)


def test_oplmetamodel_floattype_constructor_exists():
    assert callable(OPLmetamodel_FloatType.__init__)


def test_oplmetamodel_floattype_constructor_args():
    sig = inspect.signature(OPLmetamodel_FloatType.__init__)
    params = list(sig.parameters.keys())



def test_rangetype_is_not_abstract():
    assert not inspect.isabstract(RangeType)


def test_rangetype_constructor_exists():
    assert callable(RangeType.__init__)


def test_rangetype_constructor_args():
    sig = inspect.signature(RangeType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_floatrangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FloatRangeType)


def test_oplmetamodel_floatrangetype_constructor_exists():
    assert callable(OPLmetamodel_FloatRangeType.__init__)


def test_oplmetamodel_floatrangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel_FloatRangeType.__init__)
    params = list(sig.parameters.keys())



def test_initialization_is_not_abstract():
    assert not inspect.isabstract(Initialization)


def test_initialization_constructor_exists():
    assert callable(Initialization.__init__)


def test_initialization_constructor_args():
    sig = inspect.signature(Initialization.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_dataobject_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DataObject)


def test_oplmetamodel_dataobject_constructor_exists():
    assert callable(OPLmetamodel_DataObject.__init__)


def test_oplmetamodel_dataobject_constructor_args():
    sig = inspect.signature(OPLmetamodel_DataObject.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel_dataobject_has_body():
    assert hasattr(OPLmetamodel_DataObject, "body")
    descriptor = None
    for klass in OPLmetamodel_DataObject.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_datainitmethods_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DataInitMethods)


def test_oplmetamodel_datainitmethods_constructor_exists():
    assert callable(OPLmetamodel_DataInitMethods.__init__)


def test_oplmetamodel_datainitmethods_constructor_args():
    sig = inspect.signature(OPLmetamodel_DataInitMethods.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_initialization_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Initialization)


def test_oplmetamodel_initialization_constructor_exists():
    assert callable(OPLmetamodel_Initialization.__init__)


def test_oplmetamodel_initialization_constructor_args():
    sig = inspect.signature(OPLmetamodel_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_settype_is_not_abstract():
    assert not inspect.isabstract(SetType)


def test_settype_constructor_exists():
    assert callable(SetType.__init__)


def test_settype_constructor_args():
    sig = inspect.signature(SetType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_EnumerationType)


def test_oplmetamodel_enumerationtype_constructor_exists():
    assert callable(OPLmetamodel_EnumerationType.__init__)


def test_oplmetamodel_enumerationtype_constructor_args():
    sig = inspect.signature(OPLmetamodel_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ParameterDeclaration)


def test_oplmetamodel_parameterdeclaration_constructor_exists():
    assert callable(OPLmetamodel_ParameterDeclaration.__init__)


def test_oplmetamodel_parameterdeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_displayinstruction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DisplayInstruction)


def test_oplmetamodel_displayinstruction_constructor_exists():
    assert callable(OPLmetamodel_DisplayInstruction.__init__)


def test_oplmetamodel_displayinstruction_constructor_args():
    sig = inspect.signature(OPLmetamodel_DisplayInstruction.__init__)
    params = list(sig.parameters.keys())



def test_abstracttype_is_not_abstract():
    assert not inspect.isabstract(AbstractType)


def test_abstracttype_constructor_exists():
    assert callable(AbstractType.__init__)


def test_abstracttype_constructor_args():
    sig = inspect.signature(AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_deferredinit_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DeferredInit)


def test_oplmetamodel_deferredinit_constructor_exists():
    assert callable(OPLmetamodel_DeferredInit.__init__)


def test_oplmetamodel_deferredinit_constructor_args():
    sig = inspect.signature(OPLmetamodel_DeferredInit.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_declaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Declaration)


def test_oplmetamodel_declaration_constructor_exists():
    assert callable(OPLmetamodel_Declaration.__init__)


def test_oplmetamodel_declaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_oplmetamodel_declaration_has_order():
    assert hasattr(OPLmetamodel_Declaration, "order")
    descriptor = None
    for klass in OPLmetamodel_Declaration.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_definedtype_is_not_abstract():
    assert not inspect.isabstract(DefinedType)


def test_definedtype_constructor_exists():
    assert callable(DefinedType.__init__)


def test_definedtype_constructor_args():
    sig = inspect.signature(DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_arraytype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ArrayType)


def test_oplmetamodel_arraytype_constructor_exists():
    assert callable(OPLmetamodel_ArrayType.__init__)


def test_oplmetamodel_arraytype_constructor_args():
    sig = inspect.signature(OPLmetamodel_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_extension_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Extension)


def test_oplmetamodel_extension_constructor_exists():
    assert callable(OPLmetamodel_Extension.__init__)


def test_oplmetamodel_extension_constructor_args():
    sig = inspect.signature(OPLmetamodel_Extension.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_comprehension_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Comprehension)


def test_oplmetamodel_comprehension_constructor_exists():
    assert callable(OPLmetamodel_Comprehension.__init__)


def test_oplmetamodel_comprehension_constructor_args():
    sig = inspect.signature(OPLmetamodel_Comprehension.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_cumulativefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_CumulativeFunction)


def test_oplmetamodel_cumulativefunction_constructor_exists():
    assert callable(OPLmetamodel_CumulativeFunction.__init__)


def test_oplmetamodel_cumulativefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_CumulativeFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_builtinfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BuiltInFunction)


def test_oplmetamodel_builtinfunction_constructor_exists():
    assert callable(OPLmetamodel_BuiltInFunction.__init__)


def test_oplmetamodel_builtinfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_BuiltInFunction.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_booleantype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BooleanType)


def test_oplmetamodel_booleantype_constructor_exists():
    assert callable(OPLmetamodel_BooleanType.__init__)


def test_oplmetamodel_booleantype_constructor_args():
    sig = inspect.signature(OPLmetamodel_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_enumliteral_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_EnumLiteral)


def test_oplmetamodel_enumliteral_constructor_exists():
    assert callable(OPLmetamodel_EnumLiteral.__init__)


def test_oplmetamodel_enumliteral_constructor_args():
    sig = inspect.signature(OPLmetamodel_EnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BooleanExpression)


def test_oplmetamodel_booleanexpression_constructor_exists():
    assert callable(OPLmetamodel_BooleanExpression.__init__)


def test_oplmetamodel_booleanexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel_booleanexpression_has_body():
    assert hasattr(OPLmetamodel_BooleanExpression, "body")
    descriptor = None
    for klass in OPLmetamodel_BooleanExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_booleanblock_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BooleanBlock)


def test_oplmetamodel_booleanblock_constructor_exists():
    assert callable(OPLmetamodel_BooleanBlock.__init__)


def test_oplmetamodel_booleanblock_constructor_args():
    sig = inspect.signature(OPLmetamodel_BooleanBlock.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_dataref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DataRef)


def test_oplmetamodel_dataref_constructor_exists():
    assert callable(OPLmetamodel_DataRef.__init__)


def test_oplmetamodel_dataref_constructor_args():
    sig = inspect.signature(OPLmetamodel_DataRef.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_bindingref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BindingRef)


def test_oplmetamodel_bindingref_constructor_exists():
    assert callable(OPLmetamodel_BindingRef.__init__)


def test_oplmetamodel_bindingref_constructor_args():
    sig = inspect.signature(OPLmetamodel_BindingRef.__init__)
    params = list(sig.parameters.keys())



def test_abstractbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(AbstractBinaryOperator)


def test_abstractbinaryoperator_constructor_exists():
    assert callable(AbstractBinaryOperator.__init__)


def test_abstractbinaryoperator_constructor_args():
    sig = inspect.signature(AbstractBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BinaryOperator)


def test_oplmetamodel_binaryoperator_constructor_exists():
    assert callable(OPLmetamodel_BinaryOperator.__init__)


def test_oplmetamodel_binaryoperator_constructor_args():
    sig = inspect.signature(OPLmetamodel_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_oplmetamodel_binaryoperator_has_op():
    assert hasattr(OPLmetamodel_BinaryOperator, "op")
    descriptor = None
    for klass in OPLmetamodel_BinaryOperator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_tuplebinding_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_TupleBinding)


def test_oplmetamodel_tuplebinding_constructor_exists():
    assert callable(OPLmetamodel_TupleBinding.__init__)


def test_oplmetamodel_tuplebinding_constructor_args():
    sig = inspect.signature(OPLmetamodel_TupleBinding.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_stringtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_StringType)


def test_oplmetamodel_stringtype_constructor_exists():
    assert callable(OPLmetamodel_StringType.__init__)


def test_oplmetamodel_stringtype_constructor_args():
    sig = inspect.signature(OPLmetamodel_StringType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_stringexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_StringExpression)


def test_oplmetamodel_stringexpression_constructor_exists():
    assert callable(OPLmetamodel_StringExpression.__init__)


def test_oplmetamodel_stringexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel_stringexpression_has_body():
    assert hasattr(OPLmetamodel_StringExpression, "body")
    descriptor = None
    for klass in OPLmetamodel_StringExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_piecewiselinearfunction_is_not_abstract():
    assert not inspect.isabstract(PiecewiseLinearFunction)


def test_piecewiselinearfunction_constructor_exists():
    assert callable(PiecewiseLinearFunction.__init__)


def test_piecewiselinearfunction_constructor_args():
    sig = inspect.signature(PiecewiseLinearFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_statefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_StateFunction)


def test_oplmetamodel_statefunction_constructor_exists():
    assert callable(OPLmetamodel_StateFunction.__init__)


def test_oplmetamodel_statefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_StateFunction.__init__)
    params = list(sig.parameters.keys())



def test_scriptstatement_is_not_abstract():
    assert not inspect.isabstract(ScriptStatement)


def test_scriptstatement_constructor_exists():
    assert callable(ScriptStatement.__init__)


def test_scriptstatement_constructor_args():
    sig = inspect.signature(ScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_writeln_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Writeln)


def test_oplmetamodel_writeln_constructor_exists():
    assert callable(OPLmetamodel_Writeln.__init__)


def test_oplmetamodel_writeln_constructor_args():
    sig = inspect.signature(OPLmetamodel_Writeln.__init__)
    params = list(sig.parameters.keys())
    assert "arg" in params, "Missing parameter 'arg'"
    assert "string" in params, "Missing parameter 'string'"

def test_oplmetamodel_writeln_has_arg():
    assert hasattr(OPLmetamodel_Writeln, "arg")
    descriptor = None
    for klass in OPLmetamodel_Writeln.__mro__:
        if "arg" in klass.__dict__:
            descriptor = klass.__dict__["arg"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel_writeln_has_string():
    assert hasattr(OPLmetamodel_Writeln, "string")
    descriptor = None
    for klass in OPLmetamodel_Writeln.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_variablebinding_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_VariableBinding)


def test_oplmetamodel_variablebinding_constructor_exists():
    assert callable(OPLmetamodel_VariableBinding.__init__)


def test_oplmetamodel_variablebinding_constructor_args():
    sig = inspect.signature(OPLmetamodel_VariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_relationalinit_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RelationalInit)


def test_oplmetamodel_relationalinit_constructor_exists():
    assert callable(OPLmetamodel_RelationalInit.__init__)


def test_oplmetamodel_relationalinit_constructor_args():
    sig = inspect.signature(OPLmetamodel_RelationalInit.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RelationalExpression)


def test_oplmetamodel_relationalexpression_constructor_exists():
    assert callable(OPLmetamodel_RelationalExpression.__init__)


def test_oplmetamodel_relationalexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedOp" in params, "Missing parameter 'redefinedOp'"

def test_oplmetamodel_relationalexpression_has_redefinedOp():
    assert hasattr(OPLmetamodel_RelationalExpression, "redefinedOp")
    descriptor = None
    for klass in OPLmetamodel_RelationalExpression.__mro__:
        if "redefinedOp" in klass.__dict__:
            descriptor = klass.__dict__["redefinedOp"]
            break
    assert isinstance(descriptor, property)



def test_builtinfunction_is_not_abstract():
    assert not inspect.isabstract(BuiltInFunction)


def test_builtinfunction_constructor_exists():
    assert callable(BuiltInFunction.__init__)


def test_builtinfunction_constructor_args():
    sig = inspect.signature(BuiltInFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_reflectivefunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ReflectiveFunction)


def test_oplmetamodel_reflectivefunction_constructor_exists():
    assert callable(OPLmetamodel_ReflectiveFunction.__init__)


def test_oplmetamodel_reflectivefunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_ReflectiveFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_sequence_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Sequence)


def test_oplmetamodel_sequence_constructor_exists():
    assert callable(OPLmetamodel_Sequence.__init__)


def test_oplmetamodel_sequence_constructor_args():
    sig = inspect.signature(OPLmetamodel_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_scriptstatement_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ScriptStatement)


def test_oplmetamodel_scriptstatement_constructor_exists():
    assert callable(OPLmetamodel_ScriptStatement.__init__)


def test_oplmetamodel_scriptstatement_constructor_args():
    sig = inspect.signature(OPLmetamodel_ScriptStatement.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_relationaloperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RelationalOperator)


def test_oplmetamodel_relationaloperator_constructor_exists():
    assert callable(OPLmetamodel_RelationalOperator.__init__)


def test_oplmetamodel_relationaloperator_constructor_args():
    sig = inspect.signature(OPLmetamodel_RelationalOperator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_oplmetamodel_relationaloperator_has_op():
    assert hasattr(OPLmetamodel_RelationalOperator, "op")
    descriptor = None
    for klass in OPLmetamodel_RelationalOperator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_datainitmethods_is_not_abstract():
    assert not inspect.isabstract(DataInitMethods)


def test_datainitmethods_constructor_exists():
    assert callable(DataInitMethods.__init__)


def test_datainitmethods_constructor_args():
    sig = inspect.signature(DataInitMethods.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_queryuser_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_QueryUser)


def test_oplmetamodel_queryuser_constructor_exists():
    assert callable(OPLmetamodel_QueryUser.__init__)


def test_oplmetamodel_queryuser_constructor_args():
    sig = inspect.signature(OPLmetamodel_QueryUser.__init__)
    params = list(sig.parameters.keys())
    assert "ask" in params, "Missing parameter 'ask'"

def test_oplmetamodel_queryuser_has_ask():
    assert hasattr(OPLmetamodel_QueryUser, "ask")
    descriptor = None
    for klass in OPLmetamodel_QueryUser.__mro__:
        if "ask" in klass.__dict__:
            descriptor = klass.__dict__["ask"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_primitivetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PrimitiveType)


def test_oplmetamodel_primitivetype_constructor_exists():
    assert callable(OPLmetamodel_PrimitiveType.__init__)


def test_oplmetamodel_primitivetype_constructor_args():
    sig = inspect.signature(OPLmetamodel_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_positivefloattype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PositiveFloatType)


def test_oplmetamodel_positivefloattype_constructor_exists():
    assert callable(OPLmetamodel_PositiveFloatType.__init__)


def test_oplmetamodel_positivefloattype_constructor_args():
    sig = inspect.signature(OPLmetamodel_PositiveFloatType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_piecewiselinearfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PiecewiseLinearFunction)


def test_oplmetamodel_piecewiselinearfunction_constructor_exists():
    assert callable(OPLmetamodel_PiecewiseLinearFunction.__init__)


def test_oplmetamodel_piecewiselinearfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_PiecewiseLinearFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_piecewiseexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PiecewiseExpression)


def test_oplmetamodel_piecewiseexpression_constructor_exists():
    assert callable(OPLmetamodel_PiecewiseExpression.__init__)


def test_oplmetamodel_piecewiseexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_PiecewiseExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_recordfield_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RecordField)


def test_oplmetamodel_recordfield_constructor_exists():
    assert callable(OPLmetamodel_RecordField.__init__)


def test_oplmetamodel_recordfield_constructor_args():
    sig = inspect.signature(OPLmetamodel_RecordField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel_recordfield_has_name():
    assert hasattr(OPLmetamodel_RecordField, "name")
    descriptor = None
    for klass in OPLmetamodel_RecordField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_parameterdomain_is_not_abstract():
    assert not inspect.isabstract(ParameterDomain)


def test_parameterdomain_constructor_exists():
    assert callable(ParameterDomain.__init__)


def test_parameterdomain_constructor_args():
    sig = inspect.signature(ParameterDomain.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_settype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_SetType)


def test_oplmetamodel_settype_constructor_exists():
    assert callable(OPLmetamodel_SetType.__init__)


def test_oplmetamodel_settype_constructor_args():
    sig = inspect.signature(OPLmetamodel_SetType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel_settype_has_name():
    assert hasattr(OPLmetamodel_SetType, "name")
    descriptor = None
    for klass in OPLmetamodel_SetType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_record_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Record)


def test_oplmetamodel_record_constructor_exists():
    assert callable(OPLmetamodel_Record.__init__)


def test_oplmetamodel_record_constructor_args():
    sig = inspect.signature(OPLmetamodel_Record.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isTuple" in params, "Missing parameter 'isTuple'"

def test_oplmetamodel_record_has_name():
    assert hasattr(OPLmetamodel_Record, "name")
    descriptor = None
    for klass in OPLmetamodel_Record.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel_record_has_isTuple():
    assert hasattr(OPLmetamodel_Record, "isTuple")
    descriptor = None
    for klass in OPLmetamodel_Record.__mro__:
        if "isTuple" in klass.__dict__:
            descriptor = klass.__dict__["isTuple"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_readfile_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ReadFile)


def test_oplmetamodel_readfile_constructor_exists():
    assert callable(OPLmetamodel_ReadFile.__init__)


def test_oplmetamodel_readfile_constructor_args():
    sig = inspect.signature(OPLmetamodel_ReadFile.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_oplmetamodel_readfile_has_path():
    assert hasattr(OPLmetamodel_ReadFile, "path")
    descriptor = None
    for klass in OPLmetamodel_ReadFile.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RangeExpression)


def test_oplmetamodel_rangeexpression_constructor_exists():
    assert callable(OPLmetamodel_RangeExpression.__init__)


def test_oplmetamodel_rangeexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_RangeExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_model_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Model)


def test_oplmetamodel_model_constructor_exists():
    assert callable(OPLmetamodel_Model.__init__)


def test_oplmetamodel_model_constructor_args():
    sig = inspect.signature(OPLmetamodel_Model.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isConstraintProblem" in params, "Missing parameter 'isConstraintProblem'"

def test_oplmetamodel_model_has_id():
    assert hasattr(OPLmetamodel_Model, "id")
    descriptor = None
    for klass in OPLmetamodel_Model.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel_model_has_isConstraintProblem():
    assert hasattr(OPLmetamodel_Model, "isConstraintProblem")
    descriptor = None
    for klass in OPLmetamodel_Model.__mro__:
        if "isConstraintProblem" in klass.__dict__:
            descriptor = klass.__dict__["isConstraintProblem"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_parameterref_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ParameterRef)


def test_oplmetamodel_parameterref_constructor_exists():
    assert callable(OPLmetamodel_ParameterRef.__init__)


def test_oplmetamodel_parameterref_constructor_args():
    sig = inspect.signature(OPLmetamodel_ParameterRef.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_operator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Operator)


def test_oplmetamodel_operator_constructor_exists():
    assert callable(OPLmetamodel_Operator.__init__)


def test_oplmetamodel_operator_constructor_args():
    sig = inspect.signature(OPLmetamodel_Operator.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_numericexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_NumericExpression)


def test_oplmetamodel_numericexpression_constructor_exists():
    assert callable(OPLmetamodel_NumericExpression.__init__)


def test_oplmetamodel_numericexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_NumericExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_searchprocedure_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_SearchProcedure)


def test_oplmetamodel_searchprocedure_constructor_exists():
    assert callable(OPLmetamodel_SearchProcedure.__init__)


def test_oplmetamodel_searchprocedure_constructor_args():
    sig = inspect.signature(OPLmetamodel_SearchProcedure.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_ifconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IfConstraint)


def test_oplmetamodel_ifconstraint_constructor_exists():
    assert callable(OPLmetamodel_IfConstraint.__init__)


def test_oplmetamodel_ifconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel_IfConstraint.__init__)
    params = list(sig.parameters.keys())



def test_integertype_is_not_abstract():
    assert not inspect.isabstract(IntegerType)


def test_integertype_constructor_exists():
    assert callable(IntegerType.__init__)


def test_integertype_constructor_args():
    sig = inspect.signature(IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_positiveintegertype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PositiveIntegerType)


def test_oplmetamodel_positiveintegertype_constructor_exists():
    assert callable(OPLmetamodel_PositiveIntegerType.__init__)


def test_oplmetamodel_positiveintegertype_constructor_args():
    sig = inspect.signature(OPLmetamodel_PositiveIntegerType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_integerrangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IntegerRangeType)


def test_oplmetamodel_integerrangetype_constructor_exists():
    assert callable(OPLmetamodel_IntegerRangeType.__init__)


def test_oplmetamodel_integerrangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel_IntegerRangeType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_integerexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IntegerExpression)


def test_oplmetamodel_integerexpression_constructor_exists():
    assert callable(OPLmetamodel_IntegerExpression.__init__)


def test_oplmetamodel_integerexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_oplmetamodel_integerexpression_has_body():
    assert hasattr(OPLmetamodel_IntegerExpression, "body")
    descriptor = None
    for klass in OPLmetamodel_IntegerExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_stepfunction_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_StepFunction)


def test_oplmetamodel_stepfunction_constructor_exists():
    assert callable(OPLmetamodel_StepFunction.__init__)


def test_oplmetamodel_stepfunction_constructor_args():
    sig = inspect.signature(OPLmetamodel_StepFunction.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_numerictype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_NumericType)


def test_oplmetamodel_numerictype_constructor_exists():
    assert callable(OPLmetamodel_NumericType.__init__)


def test_oplmetamodel_numerictype_constructor_args():
    sig = inspect.signature(OPLmetamodel_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_rangetype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RangeType)


def test_oplmetamodel_rangetype_constructor_exists():
    assert callable(OPLmetamodel_RangeType.__init__)


def test_oplmetamodel_rangetype_constructor_args():
    sig = inspect.signature(OPLmetamodel_RangeType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_interval_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Interval)


def test_oplmetamodel_interval_constructor_exists():
    assert callable(OPLmetamodel_Interval.__init__)


def test_oplmetamodel_interval_constructor_args():
    sig = inspect.signature(OPLmetamodel_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_oplmetamodel_interval_has_isOptional():
    assert hasattr(OPLmetamodel_Interval, "isOptional")
    descriptor = None
    for klass in OPLmetamodel_Interval.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_integertype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IntegerType)


def test_oplmetamodel_integertype_constructor_exists():
    assert callable(OPLmetamodel_IntegerType.__init__)


def test_oplmetamodel_integertype_constructor_args():
    sig = inspect.signature(OPLmetamodel_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_in_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_In)


def test_oplmetamodel_in_constructor_exists():
    assert callable(OPLmetamodel_In.__init__)


def test_oplmetamodel_in_constructor_args():
    sig = inspect.signature(OPLmetamodel_In.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_abstractbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_AbstractBinaryOperator)


def test_oplmetamodel_abstractbinaryoperator_constructor_exists():
    assert callable(OPLmetamodel_AbstractBinaryOperator.__init__)


def test_oplmetamodel_abstractbinaryoperator_constructor_args():
    sig = inspect.signature(OPLmetamodel_AbstractBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_pathexpression_is_not_abstract():
    assert not inspect.isabstract(PathExpression)


def test_pathexpression_constructor_exists():
    assert callable(PathExpression.__init__)


def test_pathexpression_constructor_args():
    sig = inspect.signature(PathExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_pathdereference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PathDereference)


def test_oplmetamodel_pathdereference_constructor_exists():
    assert callable(OPLmetamodel_PathDereference.__init__)


def test_oplmetamodel_pathdereference_constructor_args():
    sig = inspect.signature(OPLmetamodel_PathDereference.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_functioncall_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FunctionCall)


def test_oplmetamodel_functioncall_constructor_exists():
    assert callable(OPLmetamodel_FunctionCall.__init__)


def test_oplmetamodel_functioncall_constructor_args():
    sig = inspect.signature(OPLmetamodel_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_oplmetamodel_functioncall_has_functionName():
    assert hasattr(OPLmetamodel_FunctionCall, "functionName")
    descriptor = None
    for klass in OPLmetamodel_FunctionCall.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_arraydereference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ArrayDereference)


def test_oplmetamodel_arraydereference_constructor_exists():
    assert callable(OPLmetamodel_ArrayDereference.__init__)


def test_oplmetamodel_arraydereference_constructor_args():
    sig = inspect.signature(OPLmetamodel_ArrayDereference.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_allexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_AllExpression)


def test_oplmetamodel_allexpression_constructor_exists():
    assert callable(OPLmetamodel_AllExpression.__init__)


def test_oplmetamodel_allexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_AllExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_expression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Expression)


def test_oplmetamodel_expression_constructor_exists():
    assert callable(OPLmetamodel_Expression.__init__)


def test_oplmetamodel_expression_constructor_args():
    sig = inspect.signature(OPLmetamodel_Expression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_formalparameter_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_FormalParameter)


def test_oplmetamodel_formalparameter_constructor_exists():
    assert callable(OPLmetamodel_FormalParameter.__init__)


def test_oplmetamodel_formalparameter_constructor_args():
    sig = inspect.signature(OPLmetamodel_FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_oplmetamodel_formalparameter_has_isOrdered():
    assert hasattr(OPLmetamodel_FormalParameter, "isOrdered")
    descriptor = None
    for klass in OPLmetamodel_FormalParameter.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_ifexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IfExpression)


def test_oplmetamodel_ifexpression_constructor_exists():
    assert callable(OPLmetamodel_IfExpression.__init__)


def test_oplmetamodel_ifexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_recordvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_RecordValue)


def test_oplmetamodel_recordvalue_constructor_exists():
    assert callable(OPLmetamodel_RecordValue.__init__)


def test_oplmetamodel_recordvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel_RecordValue.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_reference_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Reference)


def test_oplmetamodel_reference_constructor_exists():
    assert callable(OPLmetamodel_Reference.__init__)


def test_oplmetamodel_reference_constructor_args():
    sig = inspect.signature(OPLmetamodel_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel_reference_has_name():
    assert hasattr(OPLmetamodel_Reference, "name")
    descriptor = None
    for klass in OPLmetamodel_Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_pathexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PathExpression)


def test_oplmetamodel_pathexpression_constructor_exists():
    assert callable(OPLmetamodel_PathExpression.__init__)


def test_oplmetamodel_pathexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_PathExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_blockexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BlockExpression)


def test_oplmetamodel_blockexpression_constructor_exists():
    assert callable(OPLmetamodel_BlockExpression.__init__)


def test_oplmetamodel_blockexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_BlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_BinaryExpression)


def test_oplmetamodel_binaryexpression_constructor_exists():
    assert callable(OPLmetamodel_BinaryExpression.__init__)


def test_oplmetamodel_binaryexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_indexvaluepair_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_IndexValuePair)


def test_oplmetamodel_indexvaluepair_constructor_exists():
    assert callable(OPLmetamodel_IndexValuePair.__init__)


def test_oplmetamodel_indexvaluepair_constructor_args():
    sig = inspect.signature(OPLmetamodel_IndexValuePair.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_PrimitiveExpression)


def test_oplmetamodel_primitiveexpression_constructor_exists():
    assert callable(OPLmetamodel_PrimitiveExpression.__init__)


def test_oplmetamodel_primitiveexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_CollectionExpression)


def test_oplmetamodel_collectionexpression_constructor_exists():
    assert callable(OPLmetamodel_CollectionExpression.__init__)


def test_oplmetamodel_collectionexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_oplmetamodel_collectionexpression_has_isUnique():
    assert hasattr(OPLmetamodel_CollectionExpression, "isUnique")
    descriptor = None
    for klass in OPLmetamodel_CollectionExpression.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_UnaryExpression)


def test_oplmetamodel_unaryexpression_constructor_exists():
    assert callable(OPLmetamodel_UnaryExpression.__init__)


def test_oplmetamodel_unaryexpression_constructor_args():
    sig = inspect.signature(OPLmetamodel_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_oplmetamodel_unaryexpression_has_op():
    assert hasattr(OPLmetamodel_UnaryExpression, "op")
    descriptor = None
    for klass in OPLmetamodel_UnaryExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_arrayvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ArrayValue)


def test_oplmetamodel_arrayvalue_constructor_exists():
    assert callable(OPLmetamodel_ArrayValue.__init__)


def test_oplmetamodel_arrayvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel_ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_arrayslotconstraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ArraySlotConstraint)


def test_oplmetamodel_arrayslotconstraint_constructor_exists():
    assert callable(OPLmetamodel_ArraySlotConstraint.__init__)


def test_oplmetamodel_arrayslotconstraint_constructor_args():
    sig = inspect.signature(OPLmetamodel_ArraySlotConstraint.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_setvalue_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_SetValue)


def test_oplmetamodel_setvalue_constructor_exists():
    assert callable(OPLmetamodel_SetValue.__init__)


def test_oplmetamodel_setvalue_constructor_args():
    sig = inspect.signature(OPLmetamodel_SetValue.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_aggregateexp_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_AggregateExp)


def test_oplmetamodel_aggregateexp_constructor_exists():
    assert callable(OPLmetamodel_AggregateExp.__init__)


def test_oplmetamodel_aggregateexp_constructor_args():
    sig = inspect.signature(OPLmetamodel_AggregateExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_oplmetamodel_aggregateexp_has_op():
    assert hasattr(OPLmetamodel_AggregateExp, "op")
    descriptor = None
    for klass in OPLmetamodel_AggregateExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_number_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Number)


def test_oplmetamodel_number_constructor_exists():
    assert callable(OPLmetamodel_Number.__init__)


def test_oplmetamodel_number_constructor_args():
    sig = inspect.signature(OPLmetamodel_Number.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_constraint_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Constraint)


def test_oplmetamodel_constraint_constructor_exists():
    assert callable(OPLmetamodel_Constraint.__init__)


def test_oplmetamodel_constraint_constructor_args():
    sig = inspect.signature(OPLmetamodel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oplmetamodel_constraint_has_name():
    assert hasattr(OPLmetamodel_Constraint, "name")
    descriptor = None
    for klass in OPLmetamodel_Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_definedtype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DefinedType)


def test_oplmetamodel_definedtype_constructor_exists():
    assert callable(OPLmetamodel_DefinedType.__init__)


def test_oplmetamodel_definedtype_constructor_args():
    sig = inspect.signature(OPLmetamodel_DefinedType.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_function_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Function)


def test_oplmetamodel_function_constructor_exists():
    assert callable(OPLmetamodel_Function.__init__)


def test_oplmetamodel_function_constructor_args():
    sig = inspect.signature(OPLmetamodel_Function.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_assertion_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Assertion)


def test_oplmetamodel_assertion_constructor_exists():
    assert callable(OPLmetamodel_Assertion.__init__)


def test_oplmetamodel_assertion_constructor_args():
    sig = inspect.signature(OPLmetamodel_Assertion.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_scheduleinitialization_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ScheduleInitialization)


def test_oplmetamodel_scheduleinitialization_constructor_exists():
    assert callable(OPLmetamodel_ScheduleInitialization.__init__)


def test_oplmetamodel_scheduleinitialization_constructor_args():
    sig = inspect.signature(OPLmetamodel_ScheduleInitialization.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_datadeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_DataDeclaration)


def test_oplmetamodel_datadeclaration_constructor_exists():
    assert callable(OPLmetamodel_DataDeclaration.__init__)


def test_oplmetamodel_datadeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_DataDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isDecisionVar" in params, "Missing parameter 'isDecisionVar'"
    assert "isDecisionExpr" in params, "Missing parameter 'isDecisionExpr'"

def test_oplmetamodel_datadeclaration_has_isDecisionVar():
    assert hasattr(OPLmetamodel_DataDeclaration, "isDecisionVar")
    descriptor = None
    for klass in OPLmetamodel_DataDeclaration.__mro__:
        if "isDecisionVar" in klass.__dict__:
            descriptor = klass.__dict__["isDecisionVar"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel_datadeclaration_has_isDecisionExpr():
    assert hasattr(OPLmetamodel_DataDeclaration, "isDecisionExpr")
    descriptor = None
    for klass in OPLmetamodel_DataDeclaration.__mro__:
        if "isDecisionExpr" in klass.__dict__:
            descriptor = klass.__dict__["isDecisionExpr"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_script_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Script)


def test_oplmetamodel_script_constructor_exists():
    assert callable(OPLmetamodel_Script.__init__)


def test_oplmetamodel_script_constructor_args():
    sig = inspect.signature(OPLmetamodel_Script.__init__)
    params = list(sig.parameters.keys())
    assert "isMain" in params, "Missing parameter 'isMain'"

def test_oplmetamodel_script_has_isMain():
    assert hasattr(OPLmetamodel_Script, "isMain")
    descriptor = None
    for klass in OPLmetamodel_Script.__mro__:
        if "isMain" in klass.__dict__:
            descriptor = klass.__dict__["isMain"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_resourcedeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ResourceDeclaration)


def test_oplmetamodel_resourcedeclaration_constructor_exists():
    assert callable(OPLmetamodel_ResourceDeclaration.__init__)


def test_oplmetamodel_resourcedeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_ResourceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_objective_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Objective)


def test_oplmetamodel_objective_constructor_exists():
    assert callable(OPLmetamodel_Objective.__init__)


def test_oplmetamodel_objective_constructor_args():
    sig = inspect.signature(OPLmetamodel_Objective.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "isLinearRelaxation" in params, "Missing parameter 'isLinearRelaxation'"

def test_oplmetamodel_objective_has_action():
    assert hasattr(OPLmetamodel_Objective, "action")
    descriptor = None
    for klass in OPLmetamodel_Objective.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel_objective_has_isLinearRelaxation():
    assert hasattr(OPLmetamodel_Objective, "isLinearRelaxation")
    descriptor = None
    for klass in OPLmetamodel_Objective.__mro__:
        if "isLinearRelaxation" in klass.__dict__:
            descriptor = klass.__dict__["isLinearRelaxation"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_setting_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_Setting)


def test_oplmetamodel_setting_constructor_exists():
    assert callable(OPLmetamodel_Setting.__init__)


def test_oplmetamodel_setting_constructor_args():
    sig = inspect.signature(OPLmetamodel_Setting.__init__)
    params = list(sig.parameters.keys())



def test_oplmetamodel_activitydeclaration_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_ActivityDeclaration)


def test_oplmetamodel_activitydeclaration_constructor_exists():
    assert callable(OPLmetamodel_ActivityDeclaration.__init__)


def test_oplmetamodel_activitydeclaration_constructor_args():
    sig = inspect.signature(OPLmetamodel_ActivityDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "latestEndTime" in params, "Missing parameter 'latestEndTime'"
    assert "earliestStartTime" in params, "Missing parameter 'earliestStartTime'"

def test_oplmetamodel_activitydeclaration_has_latestEndTime():
    assert hasattr(OPLmetamodel_ActivityDeclaration, "latestEndTime")
    descriptor = None
    for klass in OPLmetamodel_ActivityDeclaration.__mro__:
        if "latestEndTime" in klass.__dict__:
            descriptor = klass.__dict__["latestEndTime"]
            break
    assert isinstance(descriptor, property)

def test_oplmetamodel_activitydeclaration_has_earliestStartTime():
    assert hasattr(OPLmetamodel_ActivityDeclaration, "earliestStartTime")
    descriptor = None
    for klass in OPLmetamodel_ActivityDeclaration.__mro__:
        if "earliestStartTime" in klass.__dict__:
            descriptor = klass.__dict__["earliestStartTime"]
            break
    assert isinstance(descriptor, property)



def test_oplmetamodel_abstracttype_is_not_abstract():
    assert not inspect.isabstract(OPLmetamodel_AbstractType)


def test_oplmetamodel_abstracttype_constructor_exists():
    assert callable(OPLmetamodel_AbstractType.__init__)


def test_oplmetamodel_abstracttype_constructor_args():
    sig = inspect.signature(OPLmetamodel_AbstractType.__init__)
    params = list(sig.parameters.keys())

def test_binaryop_exists():
    # Check that the Enumeration exists
    assert BinaryOp is not None

def test_binaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOp]
    expected_literals = [
        "divide",
        "union",
        "power",
        "symdiff",
        "multiply",
        "inter",
        "subtract",
        "diff",
        "mod",
        "percent",
        "add",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"

def test_membershipop_exists():
    # Check that the Enumeration exists
    assert MembershipOp is not None

def test_membershipop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MembershipOp]
    expected_literals = [
        "and_",
        "or_",
        "in_",
        "conjunction",
        "not_in",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MembershipOp"

def test_quantifier_exists():
    # Check that the Enumeration exists
    assert Quantifier is not None

def test_quantifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Quantifier]
    expected_literals = [
        "forAll",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Quantifier"

def test_optimizationmode_exists():
    # Check that the Enumeration exists
    assert OptimizationMode is not None

def test_optimizationmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimizationMode]
    expected_literals = [
        "maximize",
        "minimize",
        "solve",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimizationMode"

def test_logicalop_exists():
    # Check that the Enumeration exists
    assert LogicalOp is not None

def test_logicalop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOp]
    expected_literals = [
        "negation",
        "conjunction",
        "or_",
        "and_",
        "disjunction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOp"

def test_unaryop_exists():
    # Check that the Enumeration exists
    assert UnaryOp is not None

def test_unaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOp]
    expected_literals = [
        "negate",
        "unaryMinus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOp"

def test_relationalop_exists():
    # Check that the Enumeration exists
    assert RelationalOp is not None

def test_relationalop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOp]
    expected_literals = [
        "lessThanOrEqualTo",
        "greaterThan",
        "equalTo",
        "lessThan",
        "notEqualTo",
        "greaterThanOrEqualTo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOp"

def test_aggop_exists():
    # Check that the Enumeration exists
    assert AggOp is not None

def test_aggop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggOp]
    expected_literals = [
        "max",
        "and_",
        "min",
        "sum",
        "or_",
        "prod",
        "inter",
        "union",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggOp"

def test_setop_exists():
    # Check that the Enumeration exists
    assert SetOp is not None

def test_setop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SetOp]
    expected_literals = [
        "inter",
        "union",
        "symdiff",
        "diff",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SetOp"


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
FloatType_strategy = st.builds(
    FloatType,
)
OPLmetamodel_Error_strategy = st.builds(
    OPLmetamodel_Error,
)
OPLmetamodel_Entity_strategy = st.builds(
    OPLmetamodel_Entity,
)
OPLmetamodel_FunctionRef_strategy = st.builds(
    OPLmetamodel_FunctionRef,
    name=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
OPLmetamodel_ForAllConstraint_strategy = st.builds(
    OPLmetamodel_ForAllConstraint,
)
NumericExpression_strategy = st.builds(
    NumericExpression,
)
OPLmetamodel_FloatExpression_strategy = st.builds(
    OPLmetamodel_FloatExpression,
    body=
        safe_text
)
OPLmetamodel_ParameterDomain_strategy = st.builds(
    OPLmetamodel_ParameterDomain,
)
NumericType_strategy = st.builds(
    NumericType,
)
OPLmetamodel_FloatType_strategy = st.builds(
    OPLmetamodel_FloatType,
)
RangeType_strategy = st.builds(
    RangeType,
)
OPLmetamodel_FloatRangeType_strategy = st.builds(
    OPLmetamodel_FloatRangeType,
)
Initialization_strategy = st.builds(
    Initialization,
)
OPLmetamodel_DataObject_strategy = st.builds(
    OPLmetamodel_DataObject,
    body=
        safe_text
)
OPLmetamodel_DataInitMethods_strategy = st.builds(
    OPLmetamodel_DataInitMethods,
)
OPLmetamodel_Initialization_strategy = st.builds(
    OPLmetamodel_Initialization,
)
SetType_strategy = st.builds(
    SetType,
)
OPLmetamodel_EnumerationType_strategy = st.builds(
    OPLmetamodel_EnumerationType,
)
OPLmetamodel_ParameterDeclaration_strategy = st.builds(
    OPLmetamodel_ParameterDeclaration,
)
OPLmetamodel_DisplayInstruction_strategy = st.builds(
    OPLmetamodel_DisplayInstruction,
)
AbstractType_strategy = st.builds(
    AbstractType,
)
OPLmetamodel_DeferredInit_strategy = st.builds(
    OPLmetamodel_DeferredInit,
)
OPLmetamodel_Declaration_strategy = st.builds(
    OPLmetamodel_Declaration,
    order=
        st.none()
)
DefinedType_strategy = st.builds(
    DefinedType,
)
OPLmetamodel_ArrayType_strategy = st.builds(
    OPLmetamodel_ArrayType,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
OPLmetamodel_Extension_strategy = st.builds(
    OPLmetamodel_Extension,
)
OPLmetamodel_Comprehension_strategy = st.builds(
    OPLmetamodel_Comprehension,
)
Function_strategy = st.builds(
    Function,
)
OPLmetamodel_CumulativeFunction_strategy = st.builds(
    OPLmetamodel_CumulativeFunction,
)
OPLmetamodel_BuiltInFunction_strategy = st.builds(
    OPLmetamodel_BuiltInFunction,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
OPLmetamodel_BooleanType_strategy = st.builds(
    OPLmetamodel_BooleanType,
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
OPLmetamodel_EnumLiteral_strategy = st.builds(
    OPLmetamodel_EnumLiteral,
)
OPLmetamodel_BooleanExpression_strategy = st.builds(
    OPLmetamodel_BooleanExpression,
    body=
        safe_text
)
OPLmetamodel_BooleanBlock_strategy = st.builds(
    OPLmetamodel_BooleanBlock,
)
Reference_strategy = st.builds(
    Reference,
)
OPLmetamodel_DataRef_strategy = st.builds(
    OPLmetamodel_DataRef,
)
OPLmetamodel_BindingRef_strategy = st.builds(
    OPLmetamodel_BindingRef,
)
AbstractBinaryOperator_strategy = st.builds(
    AbstractBinaryOperator,
)
OPLmetamodel_BinaryOperator_strategy = st.builds(
    OPLmetamodel_BinaryOperator,
    op=
        safe_text
)
OPLmetamodel_TupleBinding_strategy = st.builds(
    OPLmetamodel_TupleBinding,
)
OPLmetamodel_StringType_strategy = st.builds(
    OPLmetamodel_StringType,
)
OPLmetamodel_StringExpression_strategy = st.builds(
    OPLmetamodel_StringExpression,
    body=
        safe_text
)
PiecewiseLinearFunction_strategy = st.builds(
    PiecewiseLinearFunction,
)
OPLmetamodel_StateFunction_strategy = st.builds(
    OPLmetamodel_StateFunction,
)
ScriptStatement_strategy = st.builds(
    ScriptStatement,
)
OPLmetamodel_Writeln_strategy = st.builds(
    OPLmetamodel_Writeln,
    arg=
        safe_text,
    string=
        safe_text
)
OPLmetamodel_VariableBinding_strategy = st.builds(
    OPLmetamodel_VariableBinding,
)
OPLmetamodel_RelationalInit_strategy = st.builds(
    OPLmetamodel_RelationalInit,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
OPLmetamodel_RelationalExpression_strategy = st.builds(
    OPLmetamodel_RelationalExpression,
    redefinedOp=
        safe_text
)
BuiltInFunction_strategy = st.builds(
    BuiltInFunction,
)
OPLmetamodel_ReflectiveFunction_strategy = st.builds(
    OPLmetamodel_ReflectiveFunction,
)
OPLmetamodel_Sequence_strategy = st.builds(
    OPLmetamodel_Sequence,
)
OPLmetamodel_ScriptStatement_strategy = st.builds(
    OPLmetamodel_ScriptStatement,
)
OPLmetamodel_RelationalOperator_strategy = st.builds(
    OPLmetamodel_RelationalOperator,
    op=
        safe_text
)
DataInitMethods_strategy = st.builds(
    DataInitMethods,
)
OPLmetamodel_QueryUser_strategy = st.builds(
    OPLmetamodel_QueryUser,
    ask=
        safe_text
)
OPLmetamodel_PrimitiveType_strategy = st.builds(
    OPLmetamodel_PrimitiveType,
)
OPLmetamodel_PositiveFloatType_strategy = st.builds(
    OPLmetamodel_PositiveFloatType,
)
OPLmetamodel_PiecewiseLinearFunction_strategy = st.builds(
    OPLmetamodel_PiecewiseLinearFunction,
)
OPLmetamodel_PiecewiseExpression_strategy = st.builds(
    OPLmetamodel_PiecewiseExpression,
)
OPLmetamodel_RecordField_strategy = st.builds(
    OPLmetamodel_RecordField,
    name=
        safe_text
)
ParameterDomain_strategy = st.builds(
    ParameterDomain,
)
OPLmetamodel_SetType_strategy = st.builds(
    OPLmetamodel_SetType,
    name=
        safe_text
)
OPLmetamodel_Record_strategy = st.builds(
    OPLmetamodel_Record,
    name=
        safe_text,
    isTuple=
        st.booleans()
)
OPLmetamodel_ReadFile_strategy = st.builds(
    OPLmetamodel_ReadFile,
    path=
        safe_text
)
OPLmetamodel_RangeExpression_strategy = st.builds(
    OPLmetamodel_RangeExpression,
)
OPLmetamodel_Model_strategy = st.builds(
    OPLmetamodel_Model,
    id=
        safe_text,
    isConstraintProblem=
        st.booleans()
)
OPLmetamodel_ParameterRef_strategy = st.builds(
    OPLmetamodel_ParameterRef,
)
OPLmetamodel_Operator_strategy = st.builds(
    OPLmetamodel_Operator,
)
OPLmetamodel_NumericExpression_strategy = st.builds(
    OPLmetamodel_NumericExpression,
)
OPLmetamodel_SearchProcedure_strategy = st.builds(
    OPLmetamodel_SearchProcedure,
)
OPLmetamodel_IfConstraint_strategy = st.builds(
    OPLmetamodel_IfConstraint,
)
IntegerType_strategy = st.builds(
    IntegerType,
)
OPLmetamodel_PositiveIntegerType_strategy = st.builds(
    OPLmetamodel_PositiveIntegerType,
)
OPLmetamodel_IntegerRangeType_strategy = st.builds(
    OPLmetamodel_IntegerRangeType,
)
OPLmetamodel_IntegerExpression_strategy = st.builds(
    OPLmetamodel_IntegerExpression,
    body=
        safe_text
)
OPLmetamodel_StepFunction_strategy = st.builds(
    OPLmetamodel_StepFunction,
)
OPLmetamodel_NumericType_strategy = st.builds(
    OPLmetamodel_NumericType,
)
OPLmetamodel_RangeType_strategy = st.builds(
    OPLmetamodel_RangeType,
)
OPLmetamodel_Interval_strategy = st.builds(
    OPLmetamodel_Interval,
    isOptional=
        st.booleans()
)
OPLmetamodel_IntegerType_strategy = st.builds(
    OPLmetamodel_IntegerType,
)
OPLmetamodel_In_strategy = st.builds(
    OPLmetamodel_In,
)
OPLmetamodel_AbstractBinaryOperator_strategy = st.builds(
    OPLmetamodel_AbstractBinaryOperator,
)
PathExpression_strategy = st.builds(
    PathExpression,
)
OPLmetamodel_PathDereference_strategy = st.builds(
    OPLmetamodel_PathDereference,
)
OPLmetamodel_FunctionCall_strategy = st.builds(
    OPLmetamodel_FunctionCall,
    functionName=
        safe_text
)
OPLmetamodel_ArrayDereference_strategy = st.builds(
    OPLmetamodel_ArrayDereference,
)
OPLmetamodel_AllExpression_strategy = st.builds(
    OPLmetamodel_AllExpression,
)
OPLmetamodel_Expression_strategy = st.builds(
    OPLmetamodel_Expression,
)
OPLmetamodel_FormalParameter_strategy = st.builds(
    OPLmetamodel_FormalParameter,
    isOrdered=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
OPLmetamodel_IfExpression_strategy = st.builds(
    OPLmetamodel_IfExpression,
)
OPLmetamodel_RecordValue_strategy = st.builds(
    OPLmetamodel_RecordValue,
)
OPLmetamodel_Reference_strategy = st.builds(
    OPLmetamodel_Reference,
    name=
        safe_text
)
OPLmetamodel_PathExpression_strategy = st.builds(
    OPLmetamodel_PathExpression,
)
OPLmetamodel_BlockExpression_strategy = st.builds(
    OPLmetamodel_BlockExpression,
)
OPLmetamodel_BinaryExpression_strategy = st.builds(
    OPLmetamodel_BinaryExpression,
)
OPLmetamodel_IndexValuePair_strategy = st.builds(
    OPLmetamodel_IndexValuePair,
)
OPLmetamodel_PrimitiveExpression_strategy = st.builds(
    OPLmetamodel_PrimitiveExpression,
)
OPLmetamodel_CollectionExpression_strategy = st.builds(
    OPLmetamodel_CollectionExpression,
    isUnique=
        st.booleans()
)
OPLmetamodel_UnaryExpression_strategy = st.builds(
    OPLmetamodel_UnaryExpression,
    op=
        safe_text
)
OPLmetamodel_ArrayValue_strategy = st.builds(
    OPLmetamodel_ArrayValue,
)
OPLmetamodel_ArraySlotConstraint_strategy = st.builds(
    OPLmetamodel_ArraySlotConstraint,
)
OPLmetamodel_SetValue_strategy = st.builds(
    OPLmetamodel_SetValue,
)
OPLmetamodel_AggregateExp_strategy = st.builds(
    OPLmetamodel_AggregateExp,
    op=
        safe_text
)
OPLmetamodel_Number_strategy = st.builds(
    OPLmetamodel_Number,
)
Declaration_strategy = st.builds(
    Declaration,
)
OPLmetamodel_Constraint_strategy = st.builds(
    OPLmetamodel_Constraint,
    name=
        safe_text
)
OPLmetamodel_DefinedType_strategy = st.builds(
    OPLmetamodel_DefinedType,
)
OPLmetamodel_Function_strategy = st.builds(
    OPLmetamodel_Function,
)
OPLmetamodel_Assertion_strategy = st.builds(
    OPLmetamodel_Assertion,
)
OPLmetamodel_ScheduleInitialization_strategy = st.builds(
    OPLmetamodel_ScheduleInitialization,
)
OPLmetamodel_DataDeclaration_strategy = st.builds(
    OPLmetamodel_DataDeclaration,
    isDecisionVar=
        st.booleans(),
    isDecisionExpr=
        st.booleans()
)
OPLmetamodel_Script_strategy = st.builds(
    OPLmetamodel_Script,
    isMain=
        st.booleans()
)
OPLmetamodel_ResourceDeclaration_strategy = st.builds(
    OPLmetamodel_ResourceDeclaration,
)
OPLmetamodel_Objective_strategy = st.builds(
    OPLmetamodel_Objective,
    action=
        safe_text,
    isLinearRelaxation=
        st.booleans()
)
OPLmetamodel_Setting_strategy = st.builds(
    OPLmetamodel_Setting,
)
OPLmetamodel_ActivityDeclaration_strategy = st.builds(
    OPLmetamodel_ActivityDeclaration,
    latestEndTime=
        safe_text,
    earliestStartTime=
        safe_text
)
OPLmetamodel_AbstractType_strategy = st.builds(
    OPLmetamodel_AbstractType,
)

@given(instance=FloatType_strategy)
@settings(max_examples=50)
def test_floattype_instantiation(instance):
    assert isinstance(instance, FloatType)

@given(instance=OPLmetamodel_Error_strategy)
@settings(max_examples=50)
def test_oplmetamodel_error_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Error)

@given(instance=OPLmetamodel_Entity_strategy)
@settings(max_examples=50)
def test_oplmetamodel_entity_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Entity)

@given(instance=OPLmetamodel_FunctionRef_strategy)
@settings(max_examples=50)
def test_oplmetamodel_functionref_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FunctionRef)



@given(instance=OPLmetamodel_FunctionRef_strategy)
def test_oplmetamodel_functionref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=OPLmetamodel_ForAllConstraint_strategy)
@settings(max_examples=50)
def test_oplmetamodel_forallconstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ForAllConstraint)

@given(instance=NumericExpression_strategy)
@settings(max_examples=50)
def test_numericexpression_instantiation(instance):
    assert isinstance(instance, NumericExpression)

@given(instance=OPLmetamodel_FloatExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_floatexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FloatExpression)



@given(instance=OPLmetamodel_FloatExpression_strategy)
def test_oplmetamodel_floatexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel_ParameterDomain_strategy)
@settings(max_examples=50)
def test_oplmetamodel_parameterdomain_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ParameterDomain)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=OPLmetamodel_FloatType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_floattype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FloatType)

@given(instance=RangeType_strategy)
@settings(max_examples=50)
def test_rangetype_instantiation(instance):
    assert isinstance(instance, RangeType)

@given(instance=OPLmetamodel_FloatRangeType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_floatrangetype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FloatRangeType)

@given(instance=Initialization_strategy)
@settings(max_examples=50)
def test_initialization_instantiation(instance):
    assert isinstance(instance, Initialization)

@given(instance=OPLmetamodel_DataObject_strategy)
@settings(max_examples=50)
def test_oplmetamodel_dataobject_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DataObject)



@given(instance=OPLmetamodel_DataObject_strategy)
def test_oplmetamodel_dataobject_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel_DataInitMethods_strategy)
@settings(max_examples=50)
def test_oplmetamodel_datainitmethods_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DataInitMethods)

@given(instance=OPLmetamodel_Initialization_strategy)
@settings(max_examples=50)
def test_oplmetamodel_initialization_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Initialization)

@given(instance=SetType_strategy)
@settings(max_examples=50)
def test_settype_instantiation(instance):
    assert isinstance(instance, SetType)

@given(instance=OPLmetamodel_EnumerationType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_enumerationtype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_EnumerationType)

@given(instance=OPLmetamodel_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ParameterDeclaration)

@given(instance=OPLmetamodel_DisplayInstruction_strategy)
@settings(max_examples=50)
def test_oplmetamodel_displayinstruction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DisplayInstruction)

@given(instance=AbstractType_strategy)
@settings(max_examples=50)
def test_abstracttype_instantiation(instance):
    assert isinstance(instance, AbstractType)

@given(instance=OPLmetamodel_DeferredInit_strategy)
@settings(max_examples=50)
def test_oplmetamodel_deferredinit_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DeferredInit)

@given(instance=OPLmetamodel_Declaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel_declaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Declaration)



@given(instance=OPLmetamodel_Declaration_strategy)
def test_oplmetamodel_declaration_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=DefinedType_strategy)
@settings(max_examples=50)
def test_definedtype_instantiation(instance):
    assert isinstance(instance, DefinedType)

@given(instance=OPLmetamodel_ArrayType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_arraytype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ArrayType)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=OPLmetamodel_Extension_strategy)
@settings(max_examples=50)
def test_oplmetamodel_extension_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Extension)

@given(instance=OPLmetamodel_Comprehension_strategy)
@settings(max_examples=50)
def test_oplmetamodel_comprehension_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Comprehension)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=OPLmetamodel_CumulativeFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel_cumulativefunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_CumulativeFunction)

@given(instance=OPLmetamodel_BuiltInFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel_builtinfunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BuiltInFunction)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=OPLmetamodel_BooleanType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_booleantype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BooleanType)

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=OPLmetamodel_EnumLiteral_strategy)
@settings(max_examples=50)
def test_oplmetamodel_enumliteral_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_EnumLiteral)

@given(instance=OPLmetamodel_BooleanExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_booleanexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BooleanExpression)



@given(instance=OPLmetamodel_BooleanExpression_strategy)
def test_oplmetamodel_booleanexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel_BooleanBlock_strategy)
@settings(max_examples=50)
def test_oplmetamodel_booleanblock_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BooleanBlock)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=OPLmetamodel_DataRef_strategy)
@settings(max_examples=50)
def test_oplmetamodel_dataref_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DataRef)

@given(instance=OPLmetamodel_BindingRef_strategy)
@settings(max_examples=50)
def test_oplmetamodel_bindingref_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BindingRef)

@given(instance=AbstractBinaryOperator_strategy)
@settings(max_examples=50)
def test_abstractbinaryoperator_instantiation(instance):
    assert isinstance(instance, AbstractBinaryOperator)

@given(instance=OPLmetamodel_BinaryOperator_strategy)
@settings(max_examples=50)
def test_oplmetamodel_binaryoperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BinaryOperator)



@given(instance=OPLmetamodel_BinaryOperator_strategy)
def test_oplmetamodel_binaryoperator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OPLmetamodel_TupleBinding_strategy)
@settings(max_examples=50)
def test_oplmetamodel_tuplebinding_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_TupleBinding)

@given(instance=OPLmetamodel_StringType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_stringtype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_StringType)

@given(instance=OPLmetamodel_StringExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_stringexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_StringExpression)



@given(instance=OPLmetamodel_StringExpression_strategy)
def test_oplmetamodel_stringexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=PiecewiseLinearFunction_strategy)
@settings(max_examples=50)
def test_piecewiselinearfunction_instantiation(instance):
    assert isinstance(instance, PiecewiseLinearFunction)

@given(instance=OPLmetamodel_StateFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel_statefunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_StateFunction)

@given(instance=ScriptStatement_strategy)
@settings(max_examples=50)
def test_scriptstatement_instantiation(instance):
    assert isinstance(instance, ScriptStatement)

@given(instance=OPLmetamodel_Writeln_strategy)
@settings(max_examples=50)
def test_oplmetamodel_writeln_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Writeln)



@given(instance=OPLmetamodel_Writeln_strategy)
def test_oplmetamodel_writeln_arg_setter(instance):
    original = instance.arg
    instance.arg = original
    assert instance.arg == original



@given(instance=OPLmetamodel_Writeln_strategy)
def test_oplmetamodel_writeln_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=OPLmetamodel_VariableBinding_strategy)
@settings(max_examples=50)
def test_oplmetamodel_variablebinding_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_VariableBinding)

@given(instance=OPLmetamodel_RelationalInit_strategy)
@settings(max_examples=50)
def test_oplmetamodel_relationalinit_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RelationalInit)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=OPLmetamodel_RelationalExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_relationalexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RelationalExpression)



@given(instance=OPLmetamodel_RelationalExpression_strategy)
def test_oplmetamodel_relationalexpression_redefinedOp_setter(instance):
    original = instance.redefinedOp
    instance.redefinedOp = original
    assert instance.redefinedOp == original

@given(instance=BuiltInFunction_strategy)
@settings(max_examples=50)
def test_builtinfunction_instantiation(instance):
    assert isinstance(instance, BuiltInFunction)

@given(instance=OPLmetamodel_ReflectiveFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel_reflectivefunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ReflectiveFunction)

@given(instance=OPLmetamodel_Sequence_strategy)
@settings(max_examples=50)
def test_oplmetamodel_sequence_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Sequence)

@given(instance=OPLmetamodel_ScriptStatement_strategy)
@settings(max_examples=50)
def test_oplmetamodel_scriptstatement_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ScriptStatement)

@given(instance=OPLmetamodel_RelationalOperator_strategy)
@settings(max_examples=50)
def test_oplmetamodel_relationaloperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RelationalOperator)



@given(instance=OPLmetamodel_RelationalOperator_strategy)
def test_oplmetamodel_relationaloperator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=DataInitMethods_strategy)
@settings(max_examples=50)
def test_datainitmethods_instantiation(instance):
    assert isinstance(instance, DataInitMethods)

@given(instance=OPLmetamodel_QueryUser_strategy)
@settings(max_examples=50)
def test_oplmetamodel_queryuser_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_QueryUser)



@given(instance=OPLmetamodel_QueryUser_strategy)
def test_oplmetamodel_queryuser_ask_setter(instance):
    original = instance.ask
    instance.ask = original
    assert instance.ask == original

@given(instance=OPLmetamodel_PrimitiveType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_primitivetype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PrimitiveType)

@given(instance=OPLmetamodel_PositiveFloatType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_positivefloattype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PositiveFloatType)

@given(instance=OPLmetamodel_PiecewiseLinearFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel_piecewiselinearfunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PiecewiseLinearFunction)

@given(instance=OPLmetamodel_PiecewiseExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_piecewiseexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PiecewiseExpression)

@given(instance=OPLmetamodel_RecordField_strategy)
@settings(max_examples=50)
def test_oplmetamodel_recordfield_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RecordField)



@given(instance=OPLmetamodel_RecordField_strategy)
def test_oplmetamodel_recordfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ParameterDomain_strategy)
@settings(max_examples=50)
def test_parameterdomain_instantiation(instance):
    assert isinstance(instance, ParameterDomain)

@given(instance=OPLmetamodel_SetType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_settype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_SetType)



@given(instance=OPLmetamodel_SetType_strategy)
def test_oplmetamodel_settype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OPLmetamodel_Record_strategy)
@settings(max_examples=50)
def test_oplmetamodel_record_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Record)



@given(instance=OPLmetamodel_Record_strategy)
def test_oplmetamodel_record_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=OPLmetamodel_Record_strategy)
def test_oplmetamodel_record_isTuple_setter(instance):
    original = instance.isTuple
    instance.isTuple = original
    assert instance.isTuple == original

@given(instance=OPLmetamodel_ReadFile_strategy)
@settings(max_examples=50)
def test_oplmetamodel_readfile_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ReadFile)



@given(instance=OPLmetamodel_ReadFile_strategy)
def test_oplmetamodel_readfile_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=OPLmetamodel_RangeExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_rangeexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RangeExpression)

@given(instance=OPLmetamodel_Model_strategy)
@settings(max_examples=50)
def test_oplmetamodel_model_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Model)



@given(instance=OPLmetamodel_Model_strategy)
def test_oplmetamodel_model_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=OPLmetamodel_Model_strategy)
def test_oplmetamodel_model_isConstraintProblem_setter(instance):
    original = instance.isConstraintProblem
    instance.isConstraintProblem = original
    assert instance.isConstraintProblem == original

@given(instance=OPLmetamodel_ParameterRef_strategy)
@settings(max_examples=50)
def test_oplmetamodel_parameterref_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ParameterRef)

@given(instance=OPLmetamodel_Operator_strategy)
@settings(max_examples=50)
def test_oplmetamodel_operator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Operator)

@given(instance=OPLmetamodel_NumericExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_numericexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_NumericExpression)

@given(instance=OPLmetamodel_SearchProcedure_strategy)
@settings(max_examples=50)
def test_oplmetamodel_searchprocedure_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_SearchProcedure)

@given(instance=OPLmetamodel_IfConstraint_strategy)
@settings(max_examples=50)
def test_oplmetamodel_ifconstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IfConstraint)

@given(instance=IntegerType_strategy)
@settings(max_examples=50)
def test_integertype_instantiation(instance):
    assert isinstance(instance, IntegerType)

@given(instance=OPLmetamodel_PositiveIntegerType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_positiveintegertype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PositiveIntegerType)

@given(instance=OPLmetamodel_IntegerRangeType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_integerrangetype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IntegerRangeType)

@given(instance=OPLmetamodel_IntegerExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_integerexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IntegerExpression)



@given(instance=OPLmetamodel_IntegerExpression_strategy)
def test_oplmetamodel_integerexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=OPLmetamodel_StepFunction_strategy)
@settings(max_examples=50)
def test_oplmetamodel_stepfunction_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_StepFunction)

@given(instance=OPLmetamodel_NumericType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_numerictype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_NumericType)

@given(instance=OPLmetamodel_RangeType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_rangetype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RangeType)

@given(instance=OPLmetamodel_Interval_strategy)
@settings(max_examples=50)
def test_oplmetamodel_interval_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Interval)



@given(instance=OPLmetamodel_Interval_strategy)
def test_oplmetamodel_interval_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=OPLmetamodel_IntegerType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_integertype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IntegerType)

@given(instance=OPLmetamodel_In_strategy)
@settings(max_examples=50)
def test_oplmetamodel_in_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_In)

@given(instance=OPLmetamodel_AbstractBinaryOperator_strategy)
@settings(max_examples=50)
def test_oplmetamodel_abstractbinaryoperator_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_AbstractBinaryOperator)

@given(instance=PathExpression_strategy)
@settings(max_examples=50)
def test_pathexpression_instantiation(instance):
    assert isinstance(instance, PathExpression)

@given(instance=OPLmetamodel_PathDereference_strategy)
@settings(max_examples=50)
def test_oplmetamodel_pathdereference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PathDereference)

@given(instance=OPLmetamodel_FunctionCall_strategy)
@settings(max_examples=50)
def test_oplmetamodel_functioncall_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FunctionCall)



@given(instance=OPLmetamodel_FunctionCall_strategy)
def test_oplmetamodel_functioncall_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=OPLmetamodel_ArrayDereference_strategy)
@settings(max_examples=50)
def test_oplmetamodel_arraydereference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ArrayDereference)

@given(instance=OPLmetamodel_AllExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_allexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_AllExpression)

@given(instance=OPLmetamodel_Expression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_expression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Expression)

@given(instance=OPLmetamodel_FormalParameter_strategy)
@settings(max_examples=50)
def test_oplmetamodel_formalparameter_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_FormalParameter)



@given(instance=OPLmetamodel_FormalParameter_strategy)
def test_oplmetamodel_formalparameter_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=OPLmetamodel_IfExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_ifexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IfExpression)

@given(instance=OPLmetamodel_RecordValue_strategy)
@settings(max_examples=50)
def test_oplmetamodel_recordvalue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_RecordValue)

@given(instance=OPLmetamodel_Reference_strategy)
@settings(max_examples=50)
def test_oplmetamodel_reference_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Reference)



@given(instance=OPLmetamodel_Reference_strategy)
def test_oplmetamodel_reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OPLmetamodel_PathExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_pathexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PathExpression)

@given(instance=OPLmetamodel_BlockExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_blockexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BlockExpression)

@given(instance=OPLmetamodel_BinaryExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_binaryexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_BinaryExpression)

@given(instance=OPLmetamodel_IndexValuePair_strategy)
@settings(max_examples=50)
def test_oplmetamodel_indexvaluepair_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_IndexValuePair)

@given(instance=OPLmetamodel_PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_primitiveexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_PrimitiveExpression)

@given(instance=OPLmetamodel_CollectionExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_collectionexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_CollectionExpression)



@given(instance=OPLmetamodel_CollectionExpression_strategy)
def test_oplmetamodel_collectionexpression_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=OPLmetamodel_UnaryExpression_strategy)
@settings(max_examples=50)
def test_oplmetamodel_unaryexpression_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_UnaryExpression)



@given(instance=OPLmetamodel_UnaryExpression_strategy)
def test_oplmetamodel_unaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OPLmetamodel_ArrayValue_strategy)
@settings(max_examples=50)
def test_oplmetamodel_arrayvalue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ArrayValue)

@given(instance=OPLmetamodel_ArraySlotConstraint_strategy)
@settings(max_examples=50)
def test_oplmetamodel_arrayslotconstraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ArraySlotConstraint)

@given(instance=OPLmetamodel_SetValue_strategy)
@settings(max_examples=50)
def test_oplmetamodel_setvalue_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_SetValue)

@given(instance=OPLmetamodel_AggregateExp_strategy)
@settings(max_examples=50)
def test_oplmetamodel_aggregateexp_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_AggregateExp)



@given(instance=OPLmetamodel_AggregateExp_strategy)
def test_oplmetamodel_aggregateexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OPLmetamodel_Number_strategy)
@settings(max_examples=50)
def test_oplmetamodel_number_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Number)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=OPLmetamodel_Constraint_strategy)
@settings(max_examples=50)
def test_oplmetamodel_constraint_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Constraint)



@given(instance=OPLmetamodel_Constraint_strategy)
def test_oplmetamodel_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OPLmetamodel_DefinedType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_definedtype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DefinedType)

@given(instance=OPLmetamodel_Function_strategy)
@settings(max_examples=50)
def test_oplmetamodel_function_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Function)

@given(instance=OPLmetamodel_Assertion_strategy)
@settings(max_examples=50)
def test_oplmetamodel_assertion_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Assertion)

@given(instance=OPLmetamodel_ScheduleInitialization_strategy)
@settings(max_examples=50)
def test_oplmetamodel_scheduleinitialization_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ScheduleInitialization)

@given(instance=OPLmetamodel_DataDeclaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel_datadeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_DataDeclaration)



@given(instance=OPLmetamodel_DataDeclaration_strategy)
def test_oplmetamodel_datadeclaration_isDecisionVar_setter(instance):
    original = instance.isDecisionVar
    instance.isDecisionVar = original
    assert instance.isDecisionVar == original



@given(instance=OPLmetamodel_DataDeclaration_strategy)
def test_oplmetamodel_datadeclaration_isDecisionExpr_setter(instance):
    original = instance.isDecisionExpr
    instance.isDecisionExpr = original
    assert instance.isDecisionExpr == original

@given(instance=OPLmetamodel_Script_strategy)
@settings(max_examples=50)
def test_oplmetamodel_script_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Script)



@given(instance=OPLmetamodel_Script_strategy)
def test_oplmetamodel_script_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original

@given(instance=OPLmetamodel_ResourceDeclaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel_resourcedeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ResourceDeclaration)

@given(instance=OPLmetamodel_Objective_strategy)
@settings(max_examples=50)
def test_oplmetamodel_objective_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Objective)



@given(instance=OPLmetamodel_Objective_strategy)
def test_oplmetamodel_objective_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=OPLmetamodel_Objective_strategy)
def test_oplmetamodel_objective_isLinearRelaxation_setter(instance):
    original = instance.isLinearRelaxation
    instance.isLinearRelaxation = original
    assert instance.isLinearRelaxation == original

@given(instance=OPLmetamodel_Setting_strategy)
@settings(max_examples=50)
def test_oplmetamodel_setting_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_Setting)

@given(instance=OPLmetamodel_ActivityDeclaration_strategy)
@settings(max_examples=50)
def test_oplmetamodel_activitydeclaration_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_ActivityDeclaration)



@given(instance=OPLmetamodel_ActivityDeclaration_strategy)
def test_oplmetamodel_activitydeclaration_latestEndTime_setter(instance):
    original = instance.latestEndTime
    instance.latestEndTime = original
    assert instance.latestEndTime == original



@given(instance=OPLmetamodel_ActivityDeclaration_strategy)
def test_oplmetamodel_activitydeclaration_earliestStartTime_setter(instance):
    original = instance.earliestStartTime
    instance.earliestStartTime = original
    assert instance.earliestStartTime == original

@given(instance=OPLmetamodel_AbstractType_strategy)
@settings(max_examples=50)
def test_oplmetamodel_abstracttype_instantiation(instance):
    assert isinstance(instance, OPLmetamodel_AbstractType)
