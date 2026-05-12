import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    nabla_Cardinality,
    nabla_Mul,
    nabla_Div,
    nabla_Plus,
    nabla_Modulo,
    nabla_Or,
    nabla_UnaryMinus,
    nabla_And,
    nabla_VectorConstant,
    nabla_MaxConstant,
    nabla_RealConstant,
    nabla_Minus,
    nabla_Equality,
    nabla_BoolConstant,
    nabla_MinConstant,
    nabla_FunctionCall,
    nabla_Parenthesis,
    nabla_Not,
    nabla_Comparison,
    nabla_ContractedIf,
    nabla_BaseTypeConstant,
    nabla_IntConstant,
    FunctionOrReduction,
    nabla_FunctionOrReduction,
    Var,
    nabla_ConnectivityVar,
    nabla_ArgOrVar,
    TimeIteratorRef,
    nabla_InitTimeIteratorRef,
    nabla_NextTimeIteratorRef,
    nabla_CurrentTimeIteratorRef,
    nabla_TimeIteratorRef,
    ArgOrVar,
    nabla_Arg,
    nabla_TimeIterator,
    ConnectivityCall,
    nabla_ItemRef,
    nabla_ConnectivityCall,
    nabla_Var,
    nabla_SingletonDefinition,
    IterationBlock,
    nabla_Interval,
    nabla_SpaceIterator,
    Container,
    nabla_SetRef,
    nabla_Container,
    nabla_MultipleConnectivityCall,
    nabla_SingleConnectivityCall,
    nabla_Item,
    nabla_ArgOrVarRef,
    Iterable,
    nabla_ReductionCall,
    nabla_Reduction,
    nabla_Connectivity,
    nabla_BaseType,
    Instruction,
    nabla_Affectation,
    nabla_SetDefinition,
    nabla_If,
    nabla_ItemDefinition,
    nabla_InstructionBlock,
    nabla_Loop,
    nabla_Exit,
    nabla_Return,
    nabla_IterationBlock,
    nabla_Iterable,
    nabla_Instruction,
    Connectivity,
    nabla_SingleConnectivity,
    nabla_MultipleConnectivity,
    nabla_Expression,
    nabla_SimpleVar,
    nabla_Job,
    nabla_TimeIteratorDefinition,
    nabla_VarGroupDeclaration,
    nabla_SimpleVarDefinition,
    nabla_OptDefinition,
    nabla_Function,
    nabla_ItemType,
    nabla_Import,
    nabla_NablaModule,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_nabla_cardinality_is_not_abstract():
    assert not inspect.isabstract(nabla_Cardinality)


def test_nabla_cardinality_constructor_exists():
    assert callable(nabla_Cardinality.__init__)


def test_nabla_cardinality_constructor_args():
    sig = inspect.signature(nabla_Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_nabla_mul_is_not_abstract():
    assert not inspect.isabstract(nabla_Mul)


def test_nabla_mul_constructor_exists():
    assert callable(nabla_Mul.__init__)


def test_nabla_mul_constructor_args():
    sig = inspect.signature(nabla_Mul.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_mul_has_op():
    assert hasattr(nabla_Mul, "op")
    descriptor = None
    for klass in nabla_Mul.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_div_is_not_abstract():
    assert not inspect.isabstract(nabla_Div)


def test_nabla_div_constructor_exists():
    assert callable(nabla_Div.__init__)


def test_nabla_div_constructor_args():
    sig = inspect.signature(nabla_Div.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_div_has_op():
    assert hasattr(nabla_Div, "op")
    descriptor = None
    for klass in nabla_Div.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_plus_is_not_abstract():
    assert not inspect.isabstract(nabla_Plus)


def test_nabla_plus_constructor_exists():
    assert callable(nabla_Plus.__init__)


def test_nabla_plus_constructor_args():
    sig = inspect.signature(nabla_Plus.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_plus_has_op():
    assert hasattr(nabla_Plus, "op")
    descriptor = None
    for klass in nabla_Plus.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_modulo_is_not_abstract():
    assert not inspect.isabstract(nabla_Modulo)


def test_nabla_modulo_constructor_exists():
    assert callable(nabla_Modulo.__init__)


def test_nabla_modulo_constructor_args():
    sig = inspect.signature(nabla_Modulo.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_modulo_has_op():
    assert hasattr(nabla_Modulo, "op")
    descriptor = None
    for klass in nabla_Modulo.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_or_is_not_abstract():
    assert not inspect.isabstract(nabla_Or)


def test_nabla_or_constructor_exists():
    assert callable(nabla_Or.__init__)


def test_nabla_or_constructor_args():
    sig = inspect.signature(nabla_Or.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_or_has_op():
    assert hasattr(nabla_Or, "op")
    descriptor = None
    for klass in nabla_Or.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_unaryminus_is_not_abstract():
    assert not inspect.isabstract(nabla_UnaryMinus)


def test_nabla_unaryminus_constructor_exists():
    assert callable(nabla_UnaryMinus.__init__)


def test_nabla_unaryminus_constructor_args():
    sig = inspect.signature(nabla_UnaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_nabla_and_is_not_abstract():
    assert not inspect.isabstract(nabla_And)


def test_nabla_and_constructor_exists():
    assert callable(nabla_And.__init__)


def test_nabla_and_constructor_args():
    sig = inspect.signature(nabla_And.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_and_has_op():
    assert hasattr(nabla_And, "op")
    descriptor = None
    for klass in nabla_And.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_vectorconstant_is_not_abstract():
    assert not inspect.isabstract(nabla_VectorConstant)


def test_nabla_vectorconstant_constructor_exists():
    assert callable(nabla_VectorConstant.__init__)


def test_nabla_vectorconstant_constructor_args():
    sig = inspect.signature(nabla_VectorConstant.__init__)
    params = list(sig.parameters.keys())



def test_nabla_maxconstant_is_not_abstract():
    assert not inspect.isabstract(nabla_MaxConstant)


def test_nabla_maxconstant_constructor_exists():
    assert callable(nabla_MaxConstant.__init__)


def test_nabla_maxconstant_constructor_args():
    sig = inspect.signature(nabla_MaxConstant.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_nabla_maxconstant_has_type():
    assert hasattr(nabla_MaxConstant, "type")
    descriptor = None
    for klass in nabla_MaxConstant.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_nabla_realconstant_is_not_abstract():
    assert not inspect.isabstract(nabla_RealConstant)


def test_nabla_realconstant_constructor_exists():
    assert callable(nabla_RealConstant.__init__)


def test_nabla_realconstant_constructor_args():
    sig = inspect.signature(nabla_RealConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla_realconstant_has_value():
    assert hasattr(nabla_RealConstant, "value")
    descriptor = None
    for klass in nabla_RealConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nabla_minus_is_not_abstract():
    assert not inspect.isabstract(nabla_Minus)


def test_nabla_minus_constructor_exists():
    assert callable(nabla_Minus.__init__)


def test_nabla_minus_constructor_args():
    sig = inspect.signature(nabla_Minus.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_minus_has_op():
    assert hasattr(nabla_Minus, "op")
    descriptor = None
    for klass in nabla_Minus.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_equality_is_not_abstract():
    assert not inspect.isabstract(nabla_Equality)


def test_nabla_equality_constructor_exists():
    assert callable(nabla_Equality.__init__)


def test_nabla_equality_constructor_args():
    sig = inspect.signature(nabla_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_equality_has_op():
    assert hasattr(nabla_Equality, "op")
    descriptor = None
    for klass in nabla_Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_boolconstant_is_not_abstract():
    assert not inspect.isabstract(nabla_BoolConstant)


def test_nabla_boolconstant_constructor_exists():
    assert callable(nabla_BoolConstant.__init__)


def test_nabla_boolconstant_constructor_args():
    sig = inspect.signature(nabla_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla_boolconstant_has_value():
    assert hasattr(nabla_BoolConstant, "value")
    descriptor = None
    for klass in nabla_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nabla_minconstant_is_not_abstract():
    assert not inspect.isabstract(nabla_MinConstant)


def test_nabla_minconstant_constructor_exists():
    assert callable(nabla_MinConstant.__init__)


def test_nabla_minconstant_constructor_args():
    sig = inspect.signature(nabla_MinConstant.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_nabla_minconstant_has_type():
    assert hasattr(nabla_MinConstant, "type")
    descriptor = None
    for klass in nabla_MinConstant.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_nabla_functioncall_is_not_abstract():
    assert not inspect.isabstract(nabla_FunctionCall)


def test_nabla_functioncall_constructor_exists():
    assert callable(nabla_FunctionCall.__init__)


def test_nabla_functioncall_constructor_args():
    sig = inspect.signature(nabla_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla_parenthesis_is_not_abstract():
    assert not inspect.isabstract(nabla_Parenthesis)


def test_nabla_parenthesis_constructor_exists():
    assert callable(nabla_Parenthesis.__init__)


def test_nabla_parenthesis_constructor_args():
    sig = inspect.signature(nabla_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_nabla_not_is_not_abstract():
    assert not inspect.isabstract(nabla_Not)


def test_nabla_not_constructor_exists():
    assert callable(nabla_Not.__init__)


def test_nabla_not_constructor_args():
    sig = inspect.signature(nabla_Not.__init__)
    params = list(sig.parameters.keys())



def test_nabla_comparison_is_not_abstract():
    assert not inspect.isabstract(nabla_Comparison)


def test_nabla_comparison_constructor_exists():
    assert callable(nabla_Comparison.__init__)


def test_nabla_comparison_constructor_args():
    sig = inspect.signature(nabla_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_nabla_comparison_has_op():
    assert hasattr(nabla_Comparison, "op")
    descriptor = None
    for klass in nabla_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nabla_contractedif_is_not_abstract():
    assert not inspect.isabstract(nabla_ContractedIf)


def test_nabla_contractedif_constructor_exists():
    assert callable(nabla_ContractedIf.__init__)


def test_nabla_contractedif_constructor_args():
    sig = inspect.signature(nabla_ContractedIf.__init__)
    params = list(sig.parameters.keys())



def test_nabla_basetypeconstant_is_not_abstract():
    assert not inspect.isabstract(nabla_BaseTypeConstant)


def test_nabla_basetypeconstant_constructor_exists():
    assert callable(nabla_BaseTypeConstant.__init__)


def test_nabla_basetypeconstant_constructor_args():
    sig = inspect.signature(nabla_BaseTypeConstant.__init__)
    params = list(sig.parameters.keys())



def test_nabla_intconstant_is_not_abstract():
    assert not inspect.isabstract(nabla_IntConstant)


def test_nabla_intconstant_constructor_exists():
    assert callable(nabla_IntConstant.__init__)


def test_nabla_intconstant_constructor_args():
    sig = inspect.signature(nabla_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla_intconstant_has_value():
    assert hasattr(nabla_IntConstant, "value")
    descriptor = None
    for klass in nabla_IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_functionorreduction_is_not_abstract():
    assert not inspect.isabstract(FunctionOrReduction)


def test_functionorreduction_constructor_exists():
    assert callable(FunctionOrReduction.__init__)


def test_functionorreduction_constructor_args():
    sig = inspect.signature(FunctionOrReduction.__init__)
    params = list(sig.parameters.keys())



def test_nabla_functionorreduction_is_not_abstract():
    assert not inspect.isabstract(nabla_FunctionOrReduction)


def test_nabla_functionorreduction_constructor_exists():
    assert callable(nabla_FunctionOrReduction.__init__)


def test_nabla_functionorreduction_constructor_args():
    sig = inspect.signature(nabla_FunctionOrReduction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla_functionorreduction_has_name():
    assert hasattr(nabla_FunctionOrReduction, "name")
    descriptor = None
    for klass in nabla_FunctionOrReduction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_var_is_not_abstract():
    assert not inspect.isabstract(Var)


def test_var_constructor_exists():
    assert callable(Var.__init__)


def test_var_constructor_args():
    sig = inspect.signature(Var.__init__)
    params = list(sig.parameters.keys())



def test_nabla_connectivityvar_is_not_abstract():
    assert not inspect.isabstract(nabla_ConnectivityVar)


def test_nabla_connectivityvar_constructor_exists():
    assert callable(nabla_ConnectivityVar.__init__)


def test_nabla_connectivityvar_constructor_args():
    sig = inspect.signature(nabla_ConnectivityVar.__init__)
    params = list(sig.parameters.keys())



def test_nabla_argorvar_is_not_abstract():
    assert not inspect.isabstract(nabla_ArgOrVar)


def test_nabla_argorvar_constructor_exists():
    assert callable(nabla_ArgOrVar.__init__)


def test_nabla_argorvar_constructor_args():
    sig = inspect.signature(nabla_ArgOrVar.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla_argorvar_has_name():
    assert hasattr(nabla_ArgOrVar, "name")
    descriptor = None
    for klass in nabla_ArgOrVar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timeiteratorref_is_not_abstract():
    assert not inspect.isabstract(TimeIteratorRef)


def test_timeiteratorref_constructor_exists():
    assert callable(TimeIteratorRef.__init__)


def test_timeiteratorref_constructor_args():
    sig = inspect.signature(TimeIteratorRef.__init__)
    params = list(sig.parameters.keys())



def test_nabla_inittimeiteratorref_is_not_abstract():
    assert not inspect.isabstract(nabla_InitTimeIteratorRef)


def test_nabla_inittimeiteratorref_constructor_exists():
    assert callable(nabla_InitTimeIteratorRef.__init__)


def test_nabla_inittimeiteratorref_constructor_args():
    sig = inspect.signature(nabla_InitTimeIteratorRef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla_inittimeiteratorref_has_value():
    assert hasattr(nabla_InitTimeIteratorRef, "value")
    descriptor = None
    for klass in nabla_InitTimeIteratorRef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nabla_nexttimeiteratorref_is_not_abstract():
    assert not inspect.isabstract(nabla_NextTimeIteratorRef)


def test_nabla_nexttimeiteratorref_constructor_exists():
    assert callable(nabla_NextTimeIteratorRef.__init__)


def test_nabla_nexttimeiteratorref_constructor_args():
    sig = inspect.signature(nabla_NextTimeIteratorRef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nabla_nexttimeiteratorref_has_value():
    assert hasattr(nabla_NextTimeIteratorRef, "value")
    descriptor = None
    for klass in nabla_NextTimeIteratorRef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nabla_currenttimeiteratorref_is_not_abstract():
    assert not inspect.isabstract(nabla_CurrentTimeIteratorRef)


def test_nabla_currenttimeiteratorref_constructor_exists():
    assert callable(nabla_CurrentTimeIteratorRef.__init__)


def test_nabla_currenttimeiteratorref_constructor_args():
    sig = inspect.signature(nabla_CurrentTimeIteratorRef.__init__)
    params = list(sig.parameters.keys())



def test_nabla_timeiteratorref_is_not_abstract():
    assert not inspect.isabstract(nabla_TimeIteratorRef)


def test_nabla_timeiteratorref_constructor_exists():
    assert callable(nabla_TimeIteratorRef.__init__)


def test_nabla_timeiteratorref_constructor_args():
    sig = inspect.signature(nabla_TimeIteratorRef.__init__)
    params = list(sig.parameters.keys())



def test_argorvar_is_not_abstract():
    assert not inspect.isabstract(ArgOrVar)


def test_argorvar_constructor_exists():
    assert callable(ArgOrVar.__init__)


def test_argorvar_constructor_args():
    sig = inspect.signature(ArgOrVar.__init__)
    params = list(sig.parameters.keys())



def test_nabla_arg_is_not_abstract():
    assert not inspect.isabstract(nabla_Arg)


def test_nabla_arg_constructor_exists():
    assert callable(nabla_Arg.__init__)


def test_nabla_arg_constructor_args():
    sig = inspect.signature(nabla_Arg.__init__)
    params = list(sig.parameters.keys())



def test_nabla_timeiterator_is_not_abstract():
    assert not inspect.isabstract(nabla_TimeIterator)


def test_nabla_timeiterator_constructor_exists():
    assert callable(nabla_TimeIterator.__init__)


def test_nabla_timeiterator_constructor_args():
    sig = inspect.signature(nabla_TimeIterator.__init__)
    params = list(sig.parameters.keys())



def test_connectivitycall_is_not_abstract():
    assert not inspect.isabstract(ConnectivityCall)


def test_connectivitycall_constructor_exists():
    assert callable(ConnectivityCall.__init__)


def test_connectivitycall_constructor_args():
    sig = inspect.signature(ConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla_itemref_is_not_abstract():
    assert not inspect.isabstract(nabla_ItemRef)


def test_nabla_itemref_constructor_exists():
    assert callable(nabla_ItemRef.__init__)


def test_nabla_itemref_constructor_args():
    sig = inspect.signature(nabla_ItemRef.__init__)
    params = list(sig.parameters.keys())
    assert "inc" in params, "Missing parameter 'inc'"
    assert "dec" in params, "Missing parameter 'dec'"

def test_nabla_itemref_has_inc():
    assert hasattr(nabla_ItemRef, "inc")
    descriptor = None
    for klass in nabla_ItemRef.__mro__:
        if "inc" in klass.__dict__:
            descriptor = klass.__dict__["inc"]
            break
    assert isinstance(descriptor, property)

def test_nabla_itemref_has_dec():
    assert hasattr(nabla_ItemRef, "dec")
    descriptor = None
    for klass in nabla_ItemRef.__mro__:
        if "dec" in klass.__dict__:
            descriptor = klass.__dict__["dec"]
            break
    assert isinstance(descriptor, property)



def test_nabla_connectivitycall_is_not_abstract():
    assert not inspect.isabstract(nabla_ConnectivityCall)


def test_nabla_connectivitycall_constructor_exists():
    assert callable(nabla_ConnectivityCall.__init__)


def test_nabla_connectivitycall_constructor_args():
    sig = inspect.signature(nabla_ConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla_var_is_not_abstract():
    assert not inspect.isabstract(nabla_Var)


def test_nabla_var_constructor_exists():
    assert callable(nabla_Var.__init__)


def test_nabla_var_constructor_args():
    sig = inspect.signature(nabla_Var.__init__)
    params = list(sig.parameters.keys())



def test_nabla_singletondefinition_is_not_abstract():
    assert not inspect.isabstract(nabla_SingletonDefinition)


def test_nabla_singletondefinition_constructor_exists():
    assert callable(nabla_SingletonDefinition.__init__)


def test_nabla_singletondefinition_constructor_args():
    sig = inspect.signature(nabla_SingletonDefinition.__init__)
    params = list(sig.parameters.keys())



def test_iterationblock_is_not_abstract():
    assert not inspect.isabstract(IterationBlock)


def test_iterationblock_constructor_exists():
    assert callable(IterationBlock.__init__)


def test_iterationblock_constructor_args():
    sig = inspect.signature(IterationBlock.__init__)
    params = list(sig.parameters.keys())



def test_nabla_interval_is_not_abstract():
    assert not inspect.isabstract(nabla_Interval)


def test_nabla_interval_constructor_exists():
    assert callable(nabla_Interval.__init__)


def test_nabla_interval_constructor_args():
    sig = inspect.signature(nabla_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"

def test_nabla_interval_has_from_():
    assert hasattr(nabla_Interval, "from_")
    descriptor = None
    for klass in nabla_Interval.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_nabla_spaceiterator_is_not_abstract():
    assert not inspect.isabstract(nabla_SpaceIterator)


def test_nabla_spaceiterator_constructor_exists():
    assert callable(nabla_SpaceIterator.__init__)


def test_nabla_spaceiterator_constructor_args():
    sig = inspect.signature(nabla_SpaceIterator.__init__)
    params = list(sig.parameters.keys())



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_nabla_setref_is_not_abstract():
    assert not inspect.isabstract(nabla_SetRef)


def test_nabla_setref_constructor_exists():
    assert callable(nabla_SetRef.__init__)


def test_nabla_setref_constructor_args():
    sig = inspect.signature(nabla_SetRef.__init__)
    params = list(sig.parameters.keys())



def test_nabla_container_is_not_abstract():
    assert not inspect.isabstract(nabla_Container)


def test_nabla_container_constructor_exists():
    assert callable(nabla_Container.__init__)


def test_nabla_container_constructor_args():
    sig = inspect.signature(nabla_Container.__init__)
    params = list(sig.parameters.keys())



def test_nabla_multipleconnectivitycall_is_not_abstract():
    assert not inspect.isabstract(nabla_MultipleConnectivityCall)


def test_nabla_multipleconnectivitycall_constructor_exists():
    assert callable(nabla_MultipleConnectivityCall.__init__)


def test_nabla_multipleconnectivitycall_constructor_args():
    sig = inspect.signature(nabla_MultipleConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla_singleconnectivitycall_is_not_abstract():
    assert not inspect.isabstract(nabla_SingleConnectivityCall)


def test_nabla_singleconnectivitycall_constructor_exists():
    assert callable(nabla_SingleConnectivityCall.__init__)


def test_nabla_singleconnectivitycall_constructor_args():
    sig = inspect.signature(nabla_SingleConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla_item_is_not_abstract():
    assert not inspect.isabstract(nabla_Item)


def test_nabla_item_constructor_exists():
    assert callable(nabla_Item.__init__)


def test_nabla_item_constructor_args():
    sig = inspect.signature(nabla_Item.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla_item_has_name():
    assert hasattr(nabla_Item, "name")
    descriptor = None
    for klass in nabla_Item.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla_argorvarref_is_not_abstract():
    assert not inspect.isabstract(nabla_ArgOrVarRef)


def test_nabla_argorvarref_constructor_exists():
    assert callable(nabla_ArgOrVarRef.__init__)


def test_nabla_argorvarref_constructor_args():
    sig = inspect.signature(nabla_ArgOrVarRef.__init__)
    params = list(sig.parameters.keys())



def test_iterable_is_not_abstract():
    assert not inspect.isabstract(Iterable)


def test_iterable_constructor_exists():
    assert callable(Iterable.__init__)


def test_iterable_constructor_args():
    sig = inspect.signature(Iterable.__init__)
    params = list(sig.parameters.keys())



def test_nabla_reductioncall_is_not_abstract():
    assert not inspect.isabstract(nabla_ReductionCall)


def test_nabla_reductioncall_constructor_exists():
    assert callable(nabla_ReductionCall.__init__)


def test_nabla_reductioncall_constructor_args():
    sig = inspect.signature(nabla_ReductionCall.__init__)
    params = list(sig.parameters.keys())



def test_nabla_reduction_is_not_abstract():
    assert not inspect.isabstract(nabla_Reduction)


def test_nabla_reduction_constructor_exists():
    assert callable(nabla_Reduction.__init__)


def test_nabla_reduction_constructor_args():
    sig = inspect.signature(nabla_Reduction.__init__)
    params = list(sig.parameters.keys())



def test_nabla_connectivity_is_not_abstract():
    assert not inspect.isabstract(nabla_Connectivity)


def test_nabla_connectivity_constructor_exists():
    assert callable(nabla_Connectivity.__init__)


def test_nabla_connectivity_constructor_args():
    sig = inspect.signature(nabla_Connectivity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla_connectivity_has_name():
    assert hasattr(nabla_Connectivity, "name")
    descriptor = None
    for klass in nabla_Connectivity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla_basetype_is_not_abstract():
    assert not inspect.isabstract(nabla_BaseType)


def test_nabla_basetype_constructor_exists():
    assert callable(nabla_BaseType.__init__)


def test_nabla_basetype_constructor_args():
    sig = inspect.signature(nabla_BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_nabla_basetype_has_primitive():
    assert hasattr(nabla_BaseType, "primitive")
    descriptor = None
    for klass in nabla_BaseType.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_nabla_affectation_is_not_abstract():
    assert not inspect.isabstract(nabla_Affectation)


def test_nabla_affectation_constructor_exists():
    assert callable(nabla_Affectation.__init__)


def test_nabla_affectation_constructor_args():
    sig = inspect.signature(nabla_Affectation.__init__)
    params = list(sig.parameters.keys())



def test_nabla_setdefinition_is_not_abstract():
    assert not inspect.isabstract(nabla_SetDefinition)


def test_nabla_setdefinition_constructor_exists():
    assert callable(nabla_SetDefinition.__init__)


def test_nabla_setdefinition_constructor_args():
    sig = inspect.signature(nabla_SetDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla_setdefinition_has_name():
    assert hasattr(nabla_SetDefinition, "name")
    descriptor = None
    for klass in nabla_SetDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla_if_is_not_abstract():
    assert not inspect.isabstract(nabla_If)


def test_nabla_if_constructor_exists():
    assert callable(nabla_If.__init__)


def test_nabla_if_constructor_args():
    sig = inspect.signature(nabla_If.__init__)
    params = list(sig.parameters.keys())



def test_nabla_itemdefinition_is_not_abstract():
    assert not inspect.isabstract(nabla_ItemDefinition)


def test_nabla_itemdefinition_constructor_exists():
    assert callable(nabla_ItemDefinition.__init__)


def test_nabla_itemdefinition_constructor_args():
    sig = inspect.signature(nabla_ItemDefinition.__init__)
    params = list(sig.parameters.keys())



def test_nabla_instructionblock_is_not_abstract():
    assert not inspect.isabstract(nabla_InstructionBlock)


def test_nabla_instructionblock_constructor_exists():
    assert callable(nabla_InstructionBlock.__init__)


def test_nabla_instructionblock_constructor_args():
    sig = inspect.signature(nabla_InstructionBlock.__init__)
    params = list(sig.parameters.keys())



def test_nabla_loop_is_not_abstract():
    assert not inspect.isabstract(nabla_Loop)


def test_nabla_loop_constructor_exists():
    assert callable(nabla_Loop.__init__)


def test_nabla_loop_constructor_args():
    sig = inspect.signature(nabla_Loop.__init__)
    params = list(sig.parameters.keys())



def test_nabla_exit_is_not_abstract():
    assert not inspect.isabstract(nabla_Exit)


def test_nabla_exit_constructor_exists():
    assert callable(nabla_Exit.__init__)


def test_nabla_exit_constructor_args():
    sig = inspect.signature(nabla_Exit.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_nabla_exit_has_message():
    assert hasattr(nabla_Exit, "message")
    descriptor = None
    for klass in nabla_Exit.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_nabla_return_is_not_abstract():
    assert not inspect.isabstract(nabla_Return)


def test_nabla_return_constructor_exists():
    assert callable(nabla_Return.__init__)


def test_nabla_return_constructor_args():
    sig = inspect.signature(nabla_Return.__init__)
    params = list(sig.parameters.keys())



def test_nabla_iterationblock_is_not_abstract():
    assert not inspect.isabstract(nabla_IterationBlock)


def test_nabla_iterationblock_constructor_exists():
    assert callable(nabla_IterationBlock.__init__)


def test_nabla_iterationblock_constructor_args():
    sig = inspect.signature(nabla_IterationBlock.__init__)
    params = list(sig.parameters.keys())



def test_nabla_iterable_is_not_abstract():
    assert not inspect.isabstract(nabla_Iterable)


def test_nabla_iterable_constructor_exists():
    assert callable(nabla_Iterable.__init__)


def test_nabla_iterable_constructor_args():
    sig = inspect.signature(nabla_Iterable.__init__)
    params = list(sig.parameters.keys())



def test_nabla_instruction_is_not_abstract():
    assert not inspect.isabstract(nabla_Instruction)


def test_nabla_instruction_constructor_exists():
    assert callable(nabla_Instruction.__init__)


def test_nabla_instruction_constructor_args():
    sig = inspect.signature(nabla_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_connectivity_is_not_abstract():
    assert not inspect.isabstract(Connectivity)


def test_connectivity_constructor_exists():
    assert callable(Connectivity.__init__)


def test_connectivity_constructor_args():
    sig = inspect.signature(Connectivity.__init__)
    params = list(sig.parameters.keys())



def test_nabla_singleconnectivity_is_not_abstract():
    assert not inspect.isabstract(nabla_SingleConnectivity)


def test_nabla_singleconnectivity_constructor_exists():
    assert callable(nabla_SingleConnectivity.__init__)


def test_nabla_singleconnectivity_constructor_args():
    sig = inspect.signature(nabla_SingleConnectivity.__init__)
    params = list(sig.parameters.keys())



def test_nabla_multipleconnectivity_is_not_abstract():
    assert not inspect.isabstract(nabla_MultipleConnectivity)


def test_nabla_multipleconnectivity_constructor_exists():
    assert callable(nabla_MultipleConnectivity.__init__)


def test_nabla_multipleconnectivity_constructor_args():
    sig = inspect.signature(nabla_MultipleConnectivity.__init__)
    params = list(sig.parameters.keys())



def test_nabla_expression_is_not_abstract():
    assert not inspect.isabstract(nabla_Expression)


def test_nabla_expression_constructor_exists():
    assert callable(nabla_Expression.__init__)


def test_nabla_expression_constructor_args():
    sig = inspect.signature(nabla_Expression.__init__)
    params = list(sig.parameters.keys())



def test_nabla_simplevar_is_not_abstract():
    assert not inspect.isabstract(nabla_SimpleVar)


def test_nabla_simplevar_constructor_exists():
    assert callable(nabla_SimpleVar.__init__)


def test_nabla_simplevar_constructor_args():
    sig = inspect.signature(nabla_SimpleVar.__init__)
    params = list(sig.parameters.keys())



def test_nabla_job_is_not_abstract():
    assert not inspect.isabstract(nabla_Job)


def test_nabla_job_constructor_exists():
    assert callable(nabla_Job.__init__)


def test_nabla_job_constructor_args():
    sig = inspect.signature(nabla_Job.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla_job_has_name():
    assert hasattr(nabla_Job, "name")
    descriptor = None
    for klass in nabla_Job.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla_timeiteratordefinition_is_not_abstract():
    assert not inspect.isabstract(nabla_TimeIteratorDefinition)


def test_nabla_timeiteratordefinition_constructor_exists():
    assert callable(nabla_TimeIteratorDefinition.__init__)


def test_nabla_timeiteratordefinition_constructor_args():
    sig = inspect.signature(nabla_TimeIteratorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_nabla_vargroupdeclaration_is_not_abstract():
    assert not inspect.isabstract(nabla_VarGroupDeclaration)


def test_nabla_vargroupdeclaration_constructor_exists():
    assert callable(nabla_VarGroupDeclaration.__init__)


def test_nabla_vargroupdeclaration_constructor_args():
    sig = inspect.signature(nabla_VarGroupDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nabla_simplevardefinition_is_not_abstract():
    assert not inspect.isabstract(nabla_SimpleVarDefinition)


def test_nabla_simplevardefinition_constructor_exists():
    assert callable(nabla_SimpleVarDefinition.__init__)


def test_nabla_simplevardefinition_constructor_args():
    sig = inspect.signature(nabla_SimpleVarDefinition.__init__)
    params = list(sig.parameters.keys())



def test_nabla_optdefinition_is_not_abstract():
    assert not inspect.isabstract(nabla_OptDefinition)


def test_nabla_optdefinition_constructor_exists():
    assert callable(nabla_OptDefinition.__init__)


def test_nabla_optdefinition_constructor_args():
    sig = inspect.signature(nabla_OptDefinition.__init__)
    params = list(sig.parameters.keys())



def test_nabla_function_is_not_abstract():
    assert not inspect.isabstract(nabla_Function)


def test_nabla_function_constructor_exists():
    assert callable(nabla_Function.__init__)


def test_nabla_function_constructor_args():
    sig = inspect.signature(nabla_Function.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"

def test_nabla_function_has_external():
    assert hasattr(nabla_Function, "external")
    descriptor = None
    for klass in nabla_Function.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)



def test_nabla_itemtype_is_not_abstract():
    assert not inspect.isabstract(nabla_ItemType)


def test_nabla_itemtype_constructor_exists():
    assert callable(nabla_ItemType.__init__)


def test_nabla_itemtype_constructor_args():
    sig = inspect.signature(nabla_ItemType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla_itemtype_has_name():
    assert hasattr(nabla_ItemType, "name")
    descriptor = None
    for klass in nabla_ItemType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nabla_import_is_not_abstract():
    assert not inspect.isabstract(nabla_Import)


def test_nabla_import_constructor_exists():
    assert callable(nabla_Import.__init__)


def test_nabla_import_constructor_args():
    sig = inspect.signature(nabla_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_nabla_import_has_importedNamespace():
    assert hasattr(nabla_Import, "importedNamespace")
    descriptor = None
    for klass in nabla_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_nabla_nablamodule_is_not_abstract():
    assert not inspect.isabstract(nabla_NablaModule)


def test_nabla_nablamodule_constructor_exists():
    assert callable(nabla_NablaModule.__init__)


def test_nabla_nablamodule_constructor_args():
    sig = inspect.signature(nabla_NablaModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nabla_nablamodule_has_name():
    assert hasattr(nabla_NablaModule, "name")
    descriptor = None
    for klass in nabla_NablaModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "Int",
        "Bool",
        "Real",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


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
Expression_strategy = st.builds(
    Expression,
)
nabla_Cardinality_strategy = st.builds(
    nabla_Cardinality,
)
nabla_Mul_strategy = st.builds(
    nabla_Mul,
    op=
        safe_text
)
nabla_Div_strategy = st.builds(
    nabla_Div,
    op=
        safe_text
)
nabla_Plus_strategy = st.builds(
    nabla_Plus,
    op=
        safe_text
)
nabla_Modulo_strategy = st.builds(
    nabla_Modulo,
    op=
        safe_text
)
nabla_Or_strategy = st.builds(
    nabla_Or,
    op=
        safe_text
)
nabla_UnaryMinus_strategy = st.builds(
    nabla_UnaryMinus,
)
nabla_And_strategy = st.builds(
    nabla_And,
    op=
        safe_text
)
nabla_VectorConstant_strategy = st.builds(
    nabla_VectorConstant,
)
nabla_MaxConstant_strategy = st.builds(
    nabla_MaxConstant,
    type=
        safe_text
)
nabla_RealConstant_strategy = st.builds(
    nabla_RealConstant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
nabla_Minus_strategy = st.builds(
    nabla_Minus,
    op=
        safe_text
)
nabla_Equality_strategy = st.builds(
    nabla_Equality,
    op=
        safe_text
)
nabla_BoolConstant_strategy = st.builds(
    nabla_BoolConstant,
    value=
        st.booleans()
)
nabla_MinConstant_strategy = st.builds(
    nabla_MinConstant,
    type=
        safe_text
)
nabla_FunctionCall_strategy = st.builds(
    nabla_FunctionCall,
)
nabla_Parenthesis_strategy = st.builds(
    nabla_Parenthesis,
)
nabla_Not_strategy = st.builds(
    nabla_Not,
)
nabla_Comparison_strategy = st.builds(
    nabla_Comparison,
    op=
        safe_text
)
nabla_ContractedIf_strategy = st.builds(
    nabla_ContractedIf,
)
nabla_BaseTypeConstant_strategy = st.builds(
    nabla_BaseTypeConstant,
)
nabla_IntConstant_strategy = st.builds(
    nabla_IntConstant,
    value=
        st.integers()
)
FunctionOrReduction_strategy = st.builds(
    FunctionOrReduction,
)
nabla_FunctionOrReduction_strategy = st.builds(
    nabla_FunctionOrReduction,
    name=
        safe_text
)
Var_strategy = st.builds(
    Var,
)
nabla_ConnectivityVar_strategy = st.builds(
    nabla_ConnectivityVar,
)
nabla_ArgOrVar_strategy = st.builds(
    nabla_ArgOrVar,
    name=
        safe_text
)
TimeIteratorRef_strategy = st.builds(
    TimeIteratorRef,
)
nabla_InitTimeIteratorRef_strategy = st.builds(
    nabla_InitTimeIteratorRef,
    value=
        st.integers()
)
nabla_NextTimeIteratorRef_strategy = st.builds(
    nabla_NextTimeIteratorRef,
    value=
        st.integers()
)
nabla_CurrentTimeIteratorRef_strategy = st.builds(
    nabla_CurrentTimeIteratorRef,
)
nabla_TimeIteratorRef_strategy = st.builds(
    nabla_TimeIteratorRef,
)
ArgOrVar_strategy = st.builds(
    ArgOrVar,
)
nabla_Arg_strategy = st.builds(
    nabla_Arg,
)
nabla_TimeIterator_strategy = st.builds(
    nabla_TimeIterator,
)
ConnectivityCall_strategy = st.builds(
    ConnectivityCall,
)
nabla_ItemRef_strategy = st.builds(
    nabla_ItemRef,
    inc=
        st.integers(),
    dec=
        st.integers()
)
nabla_ConnectivityCall_strategy = st.builds(
    nabla_ConnectivityCall,
)
nabla_Var_strategy = st.builds(
    nabla_Var,
)
nabla_SingletonDefinition_strategy = st.builds(
    nabla_SingletonDefinition,
)
IterationBlock_strategy = st.builds(
    IterationBlock,
)
nabla_Interval_strategy = st.builds(
    nabla_Interval,
    from_=
        st.integers()
)
nabla_SpaceIterator_strategy = st.builds(
    nabla_SpaceIterator,
)
Container_strategy = st.builds(
    Container,
)
nabla_SetRef_strategy = st.builds(
    nabla_SetRef,
)
nabla_Container_strategy = st.builds(
    nabla_Container,
)
nabla_MultipleConnectivityCall_strategy = st.builds(
    nabla_MultipleConnectivityCall,
)
nabla_SingleConnectivityCall_strategy = st.builds(
    nabla_SingleConnectivityCall,
)
nabla_Item_strategy = st.builds(
    nabla_Item,
    name=
        safe_text
)
nabla_ArgOrVarRef_strategy = st.builds(
    nabla_ArgOrVarRef,
)
Iterable_strategy = st.builds(
    Iterable,
)
nabla_ReductionCall_strategy = st.builds(
    nabla_ReductionCall,
)
nabla_Reduction_strategy = st.builds(
    nabla_Reduction,
)
nabla_Connectivity_strategy = st.builds(
    nabla_Connectivity,
    name=
        safe_text
)
nabla_BaseType_strategy = st.builds(
    nabla_BaseType,
    primitive=
        safe_text
)
Instruction_strategy = st.builds(
    Instruction,
)
nabla_Affectation_strategy = st.builds(
    nabla_Affectation,
)
nabla_SetDefinition_strategy = st.builds(
    nabla_SetDefinition,
    name=
        safe_text
)
nabla_If_strategy = st.builds(
    nabla_If,
)
nabla_ItemDefinition_strategy = st.builds(
    nabla_ItemDefinition,
)
nabla_InstructionBlock_strategy = st.builds(
    nabla_InstructionBlock,
)
nabla_Loop_strategy = st.builds(
    nabla_Loop,
)
nabla_Exit_strategy = st.builds(
    nabla_Exit,
    message=
        safe_text
)
nabla_Return_strategy = st.builds(
    nabla_Return,
)
nabla_IterationBlock_strategy = st.builds(
    nabla_IterationBlock,
)
nabla_Iterable_strategy = st.builds(
    nabla_Iterable,
)
nabla_Instruction_strategy = st.builds(
    nabla_Instruction,
)
Connectivity_strategy = st.builds(
    Connectivity,
)
nabla_SingleConnectivity_strategy = st.builds(
    nabla_SingleConnectivity,
)
nabla_MultipleConnectivity_strategy = st.builds(
    nabla_MultipleConnectivity,
)
nabla_Expression_strategy = st.builds(
    nabla_Expression,
)
nabla_SimpleVar_strategy = st.builds(
    nabla_SimpleVar,
)
nabla_Job_strategy = st.builds(
    nabla_Job,
    name=
        safe_text
)
nabla_TimeIteratorDefinition_strategy = st.builds(
    nabla_TimeIteratorDefinition,
)
nabla_VarGroupDeclaration_strategy = st.builds(
    nabla_VarGroupDeclaration,
)
nabla_SimpleVarDefinition_strategy = st.builds(
    nabla_SimpleVarDefinition,
)
nabla_OptDefinition_strategy = st.builds(
    nabla_OptDefinition,
)
nabla_Function_strategy = st.builds(
    nabla_Function,
    external=
        st.booleans()
)
nabla_ItemType_strategy = st.builds(
    nabla_ItemType,
    name=
        safe_text
)
nabla_Import_strategy = st.builds(
    nabla_Import,
    importedNamespace=
        safe_text
)
nabla_NablaModule_strategy = st.builds(
    nabla_NablaModule,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=nabla_Cardinality_strategy)
@settings(max_examples=50)
def test_nabla_cardinality_instantiation(instance):
    assert isinstance(instance, nabla_Cardinality)

@given(instance=nabla_Mul_strategy)
@settings(max_examples=50)
def test_nabla_mul_instantiation(instance):
    assert isinstance(instance, nabla_Mul)



@given(instance=nabla_Mul_strategy)
def test_nabla_mul_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_Div_strategy)
@settings(max_examples=50)
def test_nabla_div_instantiation(instance):
    assert isinstance(instance, nabla_Div)



@given(instance=nabla_Div_strategy)
def test_nabla_div_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_Plus_strategy)
@settings(max_examples=50)
def test_nabla_plus_instantiation(instance):
    assert isinstance(instance, nabla_Plus)



@given(instance=nabla_Plus_strategy)
def test_nabla_plus_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_Modulo_strategy)
@settings(max_examples=50)
def test_nabla_modulo_instantiation(instance):
    assert isinstance(instance, nabla_Modulo)



@given(instance=nabla_Modulo_strategy)
def test_nabla_modulo_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_Or_strategy)
@settings(max_examples=50)
def test_nabla_or_instantiation(instance):
    assert isinstance(instance, nabla_Or)



@given(instance=nabla_Or_strategy)
def test_nabla_or_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_UnaryMinus_strategy)
@settings(max_examples=50)
def test_nabla_unaryminus_instantiation(instance):
    assert isinstance(instance, nabla_UnaryMinus)

@given(instance=nabla_And_strategy)
@settings(max_examples=50)
def test_nabla_and_instantiation(instance):
    assert isinstance(instance, nabla_And)



@given(instance=nabla_And_strategy)
def test_nabla_and_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_VectorConstant_strategy)
@settings(max_examples=50)
def test_nabla_vectorconstant_instantiation(instance):
    assert isinstance(instance, nabla_VectorConstant)

@given(instance=nabla_MaxConstant_strategy)
@settings(max_examples=50)
def test_nabla_maxconstant_instantiation(instance):
    assert isinstance(instance, nabla_MaxConstant)



@given(instance=nabla_MaxConstant_strategy)
def test_nabla_maxconstant_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=nabla_RealConstant_strategy)
@settings(max_examples=50)
def test_nabla_realconstant_instantiation(instance):
    assert isinstance(instance, nabla_RealConstant)



@given(instance=nabla_RealConstant_strategy)
def test_nabla_realconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nabla_Minus_strategy)
@settings(max_examples=50)
def test_nabla_minus_instantiation(instance):
    assert isinstance(instance, nabla_Minus)



@given(instance=nabla_Minus_strategy)
def test_nabla_minus_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_Equality_strategy)
@settings(max_examples=50)
def test_nabla_equality_instantiation(instance):
    assert isinstance(instance, nabla_Equality)



@given(instance=nabla_Equality_strategy)
def test_nabla_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_BoolConstant_strategy)
@settings(max_examples=50)
def test_nabla_boolconstant_instantiation(instance):
    assert isinstance(instance, nabla_BoolConstant)



@given(instance=nabla_BoolConstant_strategy)
def test_nabla_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nabla_MinConstant_strategy)
@settings(max_examples=50)
def test_nabla_minconstant_instantiation(instance):
    assert isinstance(instance, nabla_MinConstant)



@given(instance=nabla_MinConstant_strategy)
def test_nabla_minconstant_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=nabla_FunctionCall_strategy)
@settings(max_examples=50)
def test_nabla_functioncall_instantiation(instance):
    assert isinstance(instance, nabla_FunctionCall)

@given(instance=nabla_Parenthesis_strategy)
@settings(max_examples=50)
def test_nabla_parenthesis_instantiation(instance):
    assert isinstance(instance, nabla_Parenthesis)

@given(instance=nabla_Not_strategy)
@settings(max_examples=50)
def test_nabla_not_instantiation(instance):
    assert isinstance(instance, nabla_Not)

@given(instance=nabla_Comparison_strategy)
@settings(max_examples=50)
def test_nabla_comparison_instantiation(instance):
    assert isinstance(instance, nabla_Comparison)



@given(instance=nabla_Comparison_strategy)
def test_nabla_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nabla_ContractedIf_strategy)
@settings(max_examples=50)
def test_nabla_contractedif_instantiation(instance):
    assert isinstance(instance, nabla_ContractedIf)

@given(instance=nabla_BaseTypeConstant_strategy)
@settings(max_examples=50)
def test_nabla_basetypeconstant_instantiation(instance):
    assert isinstance(instance, nabla_BaseTypeConstant)

@given(instance=nabla_IntConstant_strategy)
@settings(max_examples=50)
def test_nabla_intconstant_instantiation(instance):
    assert isinstance(instance, nabla_IntConstant)



@given(instance=nabla_IntConstant_strategy)
def test_nabla_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FunctionOrReduction_strategy)
@settings(max_examples=50)
def test_functionorreduction_instantiation(instance):
    assert isinstance(instance, FunctionOrReduction)

@given(instance=nabla_FunctionOrReduction_strategy)
@settings(max_examples=50)
def test_nabla_functionorreduction_instantiation(instance):
    assert isinstance(instance, nabla_FunctionOrReduction)



@given(instance=nabla_FunctionOrReduction_strategy)
def test_nabla_functionorreduction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Var_strategy)
@settings(max_examples=50)
def test_var_instantiation(instance):
    assert isinstance(instance, Var)

@given(instance=nabla_ConnectivityVar_strategy)
@settings(max_examples=50)
def test_nabla_connectivityvar_instantiation(instance):
    assert isinstance(instance, nabla_ConnectivityVar)

@given(instance=nabla_ArgOrVar_strategy)
@settings(max_examples=50)
def test_nabla_argorvar_instantiation(instance):
    assert isinstance(instance, nabla_ArgOrVar)



@given(instance=nabla_ArgOrVar_strategy)
def test_nabla_argorvar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TimeIteratorRef_strategy)
@settings(max_examples=50)
def test_timeiteratorref_instantiation(instance):
    assert isinstance(instance, TimeIteratorRef)

@given(instance=nabla_InitTimeIteratorRef_strategy)
@settings(max_examples=50)
def test_nabla_inittimeiteratorref_instantiation(instance):
    assert isinstance(instance, nabla_InitTimeIteratorRef)



@given(instance=nabla_InitTimeIteratorRef_strategy)
def test_nabla_inittimeiteratorref_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nabla_NextTimeIteratorRef_strategy)
@settings(max_examples=50)
def test_nabla_nexttimeiteratorref_instantiation(instance):
    assert isinstance(instance, nabla_NextTimeIteratorRef)



@given(instance=nabla_NextTimeIteratorRef_strategy)
def test_nabla_nexttimeiteratorref_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nabla_CurrentTimeIteratorRef_strategy)
@settings(max_examples=50)
def test_nabla_currenttimeiteratorref_instantiation(instance):
    assert isinstance(instance, nabla_CurrentTimeIteratorRef)

@given(instance=nabla_TimeIteratorRef_strategy)
@settings(max_examples=50)
def test_nabla_timeiteratorref_instantiation(instance):
    assert isinstance(instance, nabla_TimeIteratorRef)

@given(instance=ArgOrVar_strategy)
@settings(max_examples=50)
def test_argorvar_instantiation(instance):
    assert isinstance(instance, ArgOrVar)

@given(instance=nabla_Arg_strategy)
@settings(max_examples=50)
def test_nabla_arg_instantiation(instance):
    assert isinstance(instance, nabla_Arg)

@given(instance=nabla_TimeIterator_strategy)
@settings(max_examples=50)
def test_nabla_timeiterator_instantiation(instance):
    assert isinstance(instance, nabla_TimeIterator)

@given(instance=ConnectivityCall_strategy)
@settings(max_examples=50)
def test_connectivitycall_instantiation(instance):
    assert isinstance(instance, ConnectivityCall)

@given(instance=nabla_ItemRef_strategy)
@settings(max_examples=50)
def test_nabla_itemref_instantiation(instance):
    assert isinstance(instance, nabla_ItemRef)



@given(instance=nabla_ItemRef_strategy)
def test_nabla_itemref_inc_setter(instance):
    original = instance.inc
    instance.inc = original
    assert instance.inc == original



@given(instance=nabla_ItemRef_strategy)
def test_nabla_itemref_dec_setter(instance):
    original = instance.dec
    instance.dec = original
    assert instance.dec == original

@given(instance=nabla_ConnectivityCall_strategy)
@settings(max_examples=50)
def test_nabla_connectivitycall_instantiation(instance):
    assert isinstance(instance, nabla_ConnectivityCall)

@given(instance=nabla_Var_strategy)
@settings(max_examples=50)
def test_nabla_var_instantiation(instance):
    assert isinstance(instance, nabla_Var)

@given(instance=nabla_SingletonDefinition_strategy)
@settings(max_examples=50)
def test_nabla_singletondefinition_instantiation(instance):
    assert isinstance(instance, nabla_SingletonDefinition)

@given(instance=IterationBlock_strategy)
@settings(max_examples=50)
def test_iterationblock_instantiation(instance):
    assert isinstance(instance, IterationBlock)

@given(instance=nabla_Interval_strategy)
@settings(max_examples=50)
def test_nabla_interval_instantiation(instance):
    assert isinstance(instance, nabla_Interval)



@given(instance=nabla_Interval_strategy)
def test_nabla_interval_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=nabla_SpaceIterator_strategy)
@settings(max_examples=50)
def test_nabla_spaceiterator_instantiation(instance):
    assert isinstance(instance, nabla_SpaceIterator)

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=nabla_SetRef_strategy)
@settings(max_examples=50)
def test_nabla_setref_instantiation(instance):
    assert isinstance(instance, nabla_SetRef)

@given(instance=nabla_Container_strategy)
@settings(max_examples=50)
def test_nabla_container_instantiation(instance):
    assert isinstance(instance, nabla_Container)

@given(instance=nabla_MultipleConnectivityCall_strategy)
@settings(max_examples=50)
def test_nabla_multipleconnectivitycall_instantiation(instance):
    assert isinstance(instance, nabla_MultipleConnectivityCall)

@given(instance=nabla_SingleConnectivityCall_strategy)
@settings(max_examples=50)
def test_nabla_singleconnectivitycall_instantiation(instance):
    assert isinstance(instance, nabla_SingleConnectivityCall)

@given(instance=nabla_Item_strategy)
@settings(max_examples=50)
def test_nabla_item_instantiation(instance):
    assert isinstance(instance, nabla_Item)



@given(instance=nabla_Item_strategy)
def test_nabla_item_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla_ArgOrVarRef_strategy)
@settings(max_examples=50)
def test_nabla_argorvarref_instantiation(instance):
    assert isinstance(instance, nabla_ArgOrVarRef)

@given(instance=Iterable_strategy)
@settings(max_examples=50)
def test_iterable_instantiation(instance):
    assert isinstance(instance, Iterable)

@given(instance=nabla_ReductionCall_strategy)
@settings(max_examples=50)
def test_nabla_reductioncall_instantiation(instance):
    assert isinstance(instance, nabla_ReductionCall)

@given(instance=nabla_Reduction_strategy)
@settings(max_examples=50)
def test_nabla_reduction_instantiation(instance):
    assert isinstance(instance, nabla_Reduction)

@given(instance=nabla_Connectivity_strategy)
@settings(max_examples=50)
def test_nabla_connectivity_instantiation(instance):
    assert isinstance(instance, nabla_Connectivity)



@given(instance=nabla_Connectivity_strategy)
def test_nabla_connectivity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla_BaseType_strategy)
@settings(max_examples=50)
def test_nabla_basetype_instantiation(instance):
    assert isinstance(instance, nabla_BaseType)



@given(instance=nabla_BaseType_strategy)
def test_nabla_basetype_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=nabla_Affectation_strategy)
@settings(max_examples=50)
def test_nabla_affectation_instantiation(instance):
    assert isinstance(instance, nabla_Affectation)

@given(instance=nabla_SetDefinition_strategy)
@settings(max_examples=50)
def test_nabla_setdefinition_instantiation(instance):
    assert isinstance(instance, nabla_SetDefinition)



@given(instance=nabla_SetDefinition_strategy)
def test_nabla_setdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla_If_strategy)
@settings(max_examples=50)
def test_nabla_if_instantiation(instance):
    assert isinstance(instance, nabla_If)

@given(instance=nabla_ItemDefinition_strategy)
@settings(max_examples=50)
def test_nabla_itemdefinition_instantiation(instance):
    assert isinstance(instance, nabla_ItemDefinition)

@given(instance=nabla_InstructionBlock_strategy)
@settings(max_examples=50)
def test_nabla_instructionblock_instantiation(instance):
    assert isinstance(instance, nabla_InstructionBlock)

@given(instance=nabla_Loop_strategy)
@settings(max_examples=50)
def test_nabla_loop_instantiation(instance):
    assert isinstance(instance, nabla_Loop)

@given(instance=nabla_Exit_strategy)
@settings(max_examples=50)
def test_nabla_exit_instantiation(instance):
    assert isinstance(instance, nabla_Exit)



@given(instance=nabla_Exit_strategy)
def test_nabla_exit_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=nabla_Return_strategy)
@settings(max_examples=50)
def test_nabla_return_instantiation(instance):
    assert isinstance(instance, nabla_Return)

@given(instance=nabla_IterationBlock_strategy)
@settings(max_examples=50)
def test_nabla_iterationblock_instantiation(instance):
    assert isinstance(instance, nabla_IterationBlock)

@given(instance=nabla_Iterable_strategy)
@settings(max_examples=50)
def test_nabla_iterable_instantiation(instance):
    assert isinstance(instance, nabla_Iterable)

@given(instance=nabla_Instruction_strategy)
@settings(max_examples=50)
def test_nabla_instruction_instantiation(instance):
    assert isinstance(instance, nabla_Instruction)

@given(instance=Connectivity_strategy)
@settings(max_examples=50)
def test_connectivity_instantiation(instance):
    assert isinstance(instance, Connectivity)

@given(instance=nabla_SingleConnectivity_strategy)
@settings(max_examples=50)
def test_nabla_singleconnectivity_instantiation(instance):
    assert isinstance(instance, nabla_SingleConnectivity)

@given(instance=nabla_MultipleConnectivity_strategy)
@settings(max_examples=50)
def test_nabla_multipleconnectivity_instantiation(instance):
    assert isinstance(instance, nabla_MultipleConnectivity)

@given(instance=nabla_Expression_strategy)
@settings(max_examples=50)
def test_nabla_expression_instantiation(instance):
    assert isinstance(instance, nabla_Expression)

@given(instance=nabla_SimpleVar_strategy)
@settings(max_examples=50)
def test_nabla_simplevar_instantiation(instance):
    assert isinstance(instance, nabla_SimpleVar)

@given(instance=nabla_Job_strategy)
@settings(max_examples=50)
def test_nabla_job_instantiation(instance):
    assert isinstance(instance, nabla_Job)



@given(instance=nabla_Job_strategy)
def test_nabla_job_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla_TimeIteratorDefinition_strategy)
@settings(max_examples=50)
def test_nabla_timeiteratordefinition_instantiation(instance):
    assert isinstance(instance, nabla_TimeIteratorDefinition)

@given(instance=nabla_VarGroupDeclaration_strategy)
@settings(max_examples=50)
def test_nabla_vargroupdeclaration_instantiation(instance):
    assert isinstance(instance, nabla_VarGroupDeclaration)

@given(instance=nabla_SimpleVarDefinition_strategy)
@settings(max_examples=50)
def test_nabla_simplevardefinition_instantiation(instance):
    assert isinstance(instance, nabla_SimpleVarDefinition)

@given(instance=nabla_OptDefinition_strategy)
@settings(max_examples=50)
def test_nabla_optdefinition_instantiation(instance):
    assert isinstance(instance, nabla_OptDefinition)

@given(instance=nabla_Function_strategy)
@settings(max_examples=50)
def test_nabla_function_instantiation(instance):
    assert isinstance(instance, nabla_Function)



@given(instance=nabla_Function_strategy)
def test_nabla_function_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=nabla_ItemType_strategy)
@settings(max_examples=50)
def test_nabla_itemtype_instantiation(instance):
    assert isinstance(instance, nabla_ItemType)



@given(instance=nabla_ItemType_strategy)
def test_nabla_itemtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nabla_Import_strategy)
@settings(max_examples=50)
def test_nabla_import_instantiation(instance):
    assert isinstance(instance, nabla_Import)



@given(instance=nabla_Import_strategy)
def test_nabla_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=nabla_NablaModule_strategy)
@settings(max_examples=50)
def test_nabla_nablamodule_instantiation(instance):
    assert isinstance(instance, nabla_NablaModule)



@given(instance=nabla_NablaModule_strategy)
def test_nabla_nablamodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
