import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Index,
    express_IndexTerminal,
    IndexTerminal,
    express_IntLiteral,
    express_VarLiteral,
    express_Index,
    VarOrAttrib,
    express_IndexedVar,
    express_AttributeVar,
    express_SimpleVar,
    express_VarOrAttrib,
    express_CaseAction,
    Statement,
    express_IfStatement,
    express_CaseStatement,
    express_EscapeStatement,
    express_Assignment,
    express_ReturnStatement,
    express_RepeatStatement,
    express_SequenceStatement,
    express_LiteralType,
    BuiltInType,
    express_IntegerType,
    express_BooleanType,
    express_NumberType,
    express_BinaryType,
    express_RealType,
    express_LogicalType,
    express_StringType,
    DataType,
    express_EnumType,
    express_SelectType,
    express_CollectionType,
    express_GenericType,
    express_ReferenceType,
    express_BuiltInType,
    express_Intervall,
    express_FormalParam,
    express_ParameterList,
    express_FunctionExpression,
    express_Line,
    express_Statement,
    express_LocalVar,
    express_Function,
    express_ConstantVal,
    express_TypeNameList,
    express_Reference,
    express_UniqueRule,
    express_Attribute,
    express_DataType,
    ExpressConcept,
    express_Entity,
    express_WhereRule,
    express_ExpressConcept,
    express_Rule,
    express_Type,
    express_Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_express_indexterminal_is_not_abstract():
    assert not inspect.isabstract(express_IndexTerminal)


def test_express_indexterminal_constructor_exists():
    assert callable(express_IndexTerminal.__init__)


def test_express_indexterminal_constructor_args():
    sig = inspect.signature(express_IndexTerminal.__init__)
    params = list(sig.parameters.keys())



def test_indexterminal_is_not_abstract():
    assert not inspect.isabstract(IndexTerminal)


def test_indexterminal_constructor_exists():
    assert callable(IndexTerminal.__init__)


def test_indexterminal_constructor_args():
    sig = inspect.signature(IndexTerminal.__init__)
    params = list(sig.parameters.keys())



def test_express_intliteral_is_not_abstract():
    assert not inspect.isabstract(express_IntLiteral)


def test_express_intliteral_constructor_exists():
    assert callable(express_IntLiteral.__init__)


def test_express_intliteral_constructor_args():
    sig = inspect.signature(express_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_express_intliteral_has_value():
    assert hasattr(express_IntLiteral, "value")
    descriptor = None
    for klass in express_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_express_varliteral_is_not_abstract():
    assert not inspect.isabstract(express_VarLiteral)


def test_express_varliteral_constructor_exists():
    assert callable(express_VarLiteral.__init__)


def test_express_varliteral_constructor_args():
    sig = inspect.signature(express_VarLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_express_varliteral_has_value():
    assert hasattr(express_VarLiteral, "value")
    descriptor = None
    for klass in express_VarLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_express_index_is_not_abstract():
    assert not inspect.isabstract(express_Index)


def test_express_index_constructor_exists():
    assert callable(express_Index.__init__)


def test_express_index_constructor_args():
    sig = inspect.signature(express_Index.__init__)
    params = list(sig.parameters.keys())



def test_varorattrib_is_not_abstract():
    assert not inspect.isabstract(VarOrAttrib)


def test_varorattrib_constructor_exists():
    assert callable(VarOrAttrib.__init__)


def test_varorattrib_constructor_args():
    sig = inspect.signature(VarOrAttrib.__init__)
    params = list(sig.parameters.keys())



def test_express_indexedvar_is_not_abstract():
    assert not inspect.isabstract(express_IndexedVar)


def test_express_indexedvar_constructor_exists():
    assert callable(express_IndexedVar.__init__)


def test_express_indexedvar_constructor_args():
    sig = inspect.signature(express_IndexedVar.__init__)
    params = list(sig.parameters.keys())



def test_express_attributevar_is_not_abstract():
    assert not inspect.isabstract(express_AttributeVar)


def test_express_attributevar_constructor_exists():
    assert callable(express_AttributeVar.__init__)


def test_express_attributevar_constructor_args():
    sig = inspect.signature(express_AttributeVar.__init__)
    params = list(sig.parameters.keys())



def test_express_simplevar_is_not_abstract():
    assert not inspect.isabstract(express_SimpleVar)


def test_express_simplevar_constructor_exists():
    assert callable(express_SimpleVar.__init__)


def test_express_simplevar_constructor_args():
    sig = inspect.signature(express_SimpleVar.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_simplevar_has_name():
    assert hasattr(express_SimpleVar, "name")
    descriptor = None
    for klass in express_SimpleVar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_varorattrib_is_not_abstract():
    assert not inspect.isabstract(express_VarOrAttrib)


def test_express_varorattrib_constructor_exists():
    assert callable(express_VarOrAttrib.__init__)


def test_express_varorattrib_constructor_args():
    sig = inspect.signature(express_VarOrAttrib.__init__)
    params = list(sig.parameters.keys())



def test_express_caseaction_is_not_abstract():
    assert not inspect.isabstract(express_CaseAction)


def test_express_caseaction_constructor_exists():
    assert callable(express_CaseAction.__init__)


def test_express_caseaction_constructor_args():
    sig = inspect.signature(express_CaseAction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_express_caseaction_has_value():
    assert hasattr(express_CaseAction, "value")
    descriptor = None
    for klass in express_CaseAction.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_express_ifstatement_is_not_abstract():
    assert not inspect.isabstract(express_IfStatement)


def test_express_ifstatement_constructor_exists():
    assert callable(express_IfStatement.__init__)


def test_express_ifstatement_constructor_args():
    sig = inspect.signature(express_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_casestatement_is_not_abstract():
    assert not inspect.isabstract(express_CaseStatement)


def test_express_casestatement_constructor_exists():
    assert callable(express_CaseStatement.__init__)


def test_express_casestatement_constructor_args():
    sig = inspect.signature(express_CaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_express_casestatement_has_variable():
    assert hasattr(express_CaseStatement, "variable")
    descriptor = None
    for klass in express_CaseStatement.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_express_escapestatement_is_not_abstract():
    assert not inspect.isabstract(express_EscapeStatement)


def test_express_escapestatement_constructor_exists():
    assert callable(express_EscapeStatement.__init__)


def test_express_escapestatement_constructor_args():
    sig = inspect.signature(express_EscapeStatement.__init__)
    params = list(sig.parameters.keys())



def test_express_assignment_is_not_abstract():
    assert not inspect.isabstract(express_Assignment)


def test_express_assignment_constructor_exists():
    assert callable(express_Assignment.__init__)


def test_express_assignment_constructor_args():
    sig = inspect.signature(express_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_express_assignment_has_expression():
    assert hasattr(express_Assignment, "expression")
    descriptor = None
    for klass in express_Assignment.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express_returnstatement_is_not_abstract():
    assert not inspect.isabstract(express_ReturnStatement)


def test_express_returnstatement_constructor_exists():
    assert callable(express_ReturnStatement.__init__)


def test_express_returnstatement_constructor_args():
    sig = inspect.signature(express_ReturnStatement.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_express_returnstatement_has_expression():
    assert hasattr(express_ReturnStatement, "expression")
    descriptor = None
    for klass in express_ReturnStatement.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express_repeatstatement_is_not_abstract():
    assert not inspect.isabstract(express_RepeatStatement)


def test_express_repeatstatement_constructor_exists():
    assert callable(express_RepeatStatement.__init__)


def test_express_repeatstatement_constructor_args():
    sig = inspect.signature(express_RepeatStatement.__init__)
    params = list(sig.parameters.keys())
    assert "idx" in params, "Missing parameter 'idx'"
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_express_repeatstatement_has_idx():
    assert hasattr(express_RepeatStatement, "idx")
    descriptor = None
    for klass in express_RepeatStatement.__mro__:
        if "idx" in klass.__dict__:
            descriptor = klass.__dict__["idx"]
            break
    assert isinstance(descriptor, property)

def test_express_repeatstatement_has_start():
    assert hasattr(express_RepeatStatement, "start")
    descriptor = None
    for klass in express_RepeatStatement.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_express_repeatstatement_has_end():
    assert hasattr(express_RepeatStatement, "end")
    descriptor = None
    for klass in express_RepeatStatement.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_express_sequencestatement_is_not_abstract():
    assert not inspect.isabstract(express_SequenceStatement)


def test_express_sequencestatement_constructor_exists():
    assert callable(express_SequenceStatement.__init__)


def test_express_sequencestatement_constructor_args():
    sig = inspect.signature(express_SequenceStatement.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_express_sequencestatement_has_expression():
    assert hasattr(express_SequenceStatement, "expression")
    descriptor = None
    for klass in express_SequenceStatement.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express_literaltype_is_not_abstract():
    assert not inspect.isabstract(express_LiteralType)


def test_express_literaltype_constructor_exists():
    assert callable(express_LiteralType.__init__)


def test_express_literaltype_constructor_args():
    sig = inspect.signature(express_LiteralType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_literaltype_has_name():
    assert hasattr(express_LiteralType, "name")
    descriptor = None
    for klass in express_LiteralType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_builtintype_is_not_abstract():
    assert not inspect.isabstract(BuiltInType)


def test_builtintype_constructor_exists():
    assert callable(BuiltInType.__init__)


def test_builtintype_constructor_args():
    sig = inspect.signature(BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_express_integertype_is_not_abstract():
    assert not inspect.isabstract(express_IntegerType)


def test_express_integertype_constructor_exists():
    assert callable(express_IntegerType.__init__)


def test_express_integertype_constructor_args():
    sig = inspect.signature(express_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_express_booleantype_is_not_abstract():
    assert not inspect.isabstract(express_BooleanType)


def test_express_booleantype_constructor_exists():
    assert callable(express_BooleanType.__init__)


def test_express_booleantype_constructor_args():
    sig = inspect.signature(express_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_express_numbertype_is_not_abstract():
    assert not inspect.isabstract(express_NumberType)


def test_express_numbertype_constructor_exists():
    assert callable(express_NumberType.__init__)


def test_express_numbertype_constructor_args():
    sig = inspect.signature(express_NumberType.__init__)
    params = list(sig.parameters.keys())



def test_express_binarytype_is_not_abstract():
    assert not inspect.isabstract(express_BinaryType)


def test_express_binarytype_constructor_exists():
    assert callable(express_BinaryType.__init__)


def test_express_binarytype_constructor_args():
    sig = inspect.signature(express_BinaryType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_express_binarytype_has_size():
    assert hasattr(express_BinaryType, "size")
    descriptor = None
    for klass in express_BinaryType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_express_realtype_is_not_abstract():
    assert not inspect.isabstract(express_RealType)


def test_express_realtype_constructor_exists():
    assert callable(express_RealType.__init__)


def test_express_realtype_constructor_args():
    sig = inspect.signature(express_RealType.__init__)
    params = list(sig.parameters.keys())



def test_express_logicaltype_is_not_abstract():
    assert not inspect.isabstract(express_LogicalType)


def test_express_logicaltype_constructor_exists():
    assert callable(express_LogicalType.__init__)


def test_express_logicaltype_constructor_args():
    sig = inspect.signature(express_LogicalType.__init__)
    params = list(sig.parameters.keys())



def test_express_stringtype_is_not_abstract():
    assert not inspect.isabstract(express_StringType)


def test_express_stringtype_constructor_exists():
    assert callable(express_StringType.__init__)


def test_express_stringtype_constructor_args():
    sig = inspect.signature(express_StringType.__init__)
    params = list(sig.parameters.keys())
    assert "fixed" in params, "Missing parameter 'fixed'"
    assert "size" in params, "Missing parameter 'size'"

def test_express_stringtype_has_fixed():
    assert hasattr(express_StringType, "fixed")
    descriptor = None
    for klass in express_StringType.__mro__:
        if "fixed" in klass.__dict__:
            descriptor = klass.__dict__["fixed"]
            break
    assert isinstance(descriptor, property)

def test_express_stringtype_has_size():
    assert hasattr(express_StringType, "size")
    descriptor = None
    for klass in express_StringType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_express_enumtype_is_not_abstract():
    assert not inspect.isabstract(express_EnumType)


def test_express_enumtype_constructor_exists():
    assert callable(express_EnumType.__init__)


def test_express_enumtype_constructor_args():
    sig = inspect.signature(express_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_express_selecttype_is_not_abstract():
    assert not inspect.isabstract(express_SelectType)


def test_express_selecttype_constructor_exists():
    assert callable(express_SelectType.__init__)


def test_express_selecttype_constructor_args():
    sig = inspect.signature(express_SelectType.__init__)
    params = list(sig.parameters.keys())



def test_express_collectiontype_is_not_abstract():
    assert not inspect.isabstract(express_CollectionType)


def test_express_collectiontype_constructor_exists():
    assert callable(express_CollectionType.__init__)


def test_express_collectiontype_constructor_args():
    sig = inspect.signature(express_CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "opt" in params, "Missing parameter 'opt'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_express_collectiontype_has_opt():
    assert hasattr(express_CollectionType, "opt")
    descriptor = None
    for klass in express_CollectionType.__mro__:
        if "opt" in klass.__dict__:
            descriptor = klass.__dict__["opt"]
            break
    assert isinstance(descriptor, property)

def test_express_collectiontype_has_unique():
    assert hasattr(express_CollectionType, "unique")
    descriptor = None
    for klass in express_CollectionType.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_express_collectiontype_has_many():
    assert hasattr(express_CollectionType, "many")
    descriptor = None
    for klass in express_CollectionType.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_express_collectiontype_has_name():
    assert hasattr(express_CollectionType, "name")
    descriptor = None
    for klass in express_CollectionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express_collectiontype_has_lowerBound():
    assert hasattr(express_CollectionType, "lowerBound")
    descriptor = None
    for klass in express_CollectionType.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_express_collectiontype_has_upperBound():
    assert hasattr(express_CollectionType, "upperBound")
    descriptor = None
    for klass in express_CollectionType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_express_generictype_is_not_abstract():
    assert not inspect.isabstract(express_GenericType)


def test_express_generictype_constructor_exists():
    assert callable(express_GenericType.__init__)


def test_express_generictype_constructor_args():
    sig = inspect.signature(express_GenericType.__init__)
    params = list(sig.parameters.keys())
    assert "typelabel" in params, "Missing parameter 'typelabel'"

def test_express_generictype_has_typelabel():
    assert hasattr(express_GenericType, "typelabel")
    descriptor = None
    for klass in express_GenericType.__mro__:
        if "typelabel" in klass.__dict__:
            descriptor = klass.__dict__["typelabel"]
            break
    assert isinstance(descriptor, property)



def test_express_referencetype_is_not_abstract():
    assert not inspect.isabstract(express_ReferenceType)


def test_express_referencetype_constructor_exists():
    assert callable(express_ReferenceType.__init__)


def test_express_referencetype_constructor_args():
    sig = inspect.signature(express_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_express_builtintype_is_not_abstract():
    assert not inspect.isabstract(express_BuiltInType)


def test_express_builtintype_constructor_exists():
    assert callable(express_BuiltInType.__init__)


def test_express_builtintype_constructor_args():
    sig = inspect.signature(express_BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_express_intervall_is_not_abstract():
    assert not inspect.isabstract(express_Intervall)


def test_express_intervall_constructor_exists():
    assert callable(express_Intervall.__init__)


def test_express_intervall_constructor_args():
    sig = inspect.signature(express_Intervall.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_express_intervall_has_expression():
    assert hasattr(express_Intervall, "expression")
    descriptor = None
    for klass in express_Intervall.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express_formalparam_is_not_abstract():
    assert not inspect.isabstract(express_FormalParam)


def test_express_formalparam_constructor_exists():
    assert callable(express_FormalParam.__init__)


def test_express_formalparam_constructor_args():
    sig = inspect.signature(express_FormalParam.__init__)
    params = list(sig.parameters.keys())
    assert "paramName" in params, "Missing parameter 'paramName'"

def test_express_formalparam_has_paramName():
    assert hasattr(express_FormalParam, "paramName")
    descriptor = None
    for klass in express_FormalParam.__mro__:
        if "paramName" in klass.__dict__:
            descriptor = klass.__dict__["paramName"]
            break
    assert isinstance(descriptor, property)



def test_express_parameterlist_is_not_abstract():
    assert not inspect.isabstract(express_ParameterList)


def test_express_parameterlist_constructor_exists():
    assert callable(express_ParameterList.__init__)


def test_express_parameterlist_constructor_args():
    sig = inspect.signature(express_ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_express_functionexpression_is_not_abstract():
    assert not inspect.isabstract(express_FunctionExpression)


def test_express_functionexpression_constructor_exists():
    assert callable(express_FunctionExpression.__init__)


def test_express_functionexpression_constructor_args():
    sig = inspect.signature(express_FunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_functionexpression_has_name():
    assert hasattr(express_FunctionExpression, "name")
    descriptor = None
    for klass in express_FunctionExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_line_is_not_abstract():
    assert not inspect.isabstract(express_Line)


def test_express_line_constructor_exists():
    assert callable(express_Line.__init__)


def test_express_line_constructor_args():
    sig = inspect.signature(express_Line.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_express_line_has_text():
    assert hasattr(express_Line, "text")
    descriptor = None
    for klass in express_Line.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_express_statement_is_not_abstract():
    assert not inspect.isabstract(express_Statement)


def test_express_statement_constructor_exists():
    assert callable(express_Statement.__init__)


def test_express_statement_constructor_args():
    sig = inspect.signature(express_Statement.__init__)
    params = list(sig.parameters.keys())



def test_express_localvar_is_not_abstract():
    assert not inspect.isabstract(express_LocalVar)


def test_express_localvar_constructor_exists():
    assert callable(express_LocalVar.__init__)


def test_express_localvar_constructor_args():
    sig = inspect.signature(express_LocalVar.__init__)
    params = list(sig.parameters.keys())
    assert "varname" in params, "Missing parameter 'varname'"

def test_express_localvar_has_varname():
    assert hasattr(express_LocalVar, "varname")
    descriptor = None
    for klass in express_LocalVar.__mro__:
        if "varname" in klass.__dict__:
            descriptor = klass.__dict__["varname"]
            break
    assert isinstance(descriptor, property)



def test_express_function_is_not_abstract():
    assert not inspect.isabstract(express_Function)


def test_express_function_constructor_exists():
    assert callable(express_Function.__init__)


def test_express_function_constructor_args():
    sig = inspect.signature(express_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_function_has_name():
    assert hasattr(express_Function, "name")
    descriptor = None
    for klass in express_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_constantval_is_not_abstract():
    assert not inspect.isabstract(express_ConstantVal)


def test_express_constantval_constructor_exists():
    assert callable(express_ConstantVal.__init__)


def test_express_constantval_constructor_args():
    sig = inspect.signature(express_ConstantVal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_constantval_has_name():
    assert hasattr(express_ConstantVal, "name")
    descriptor = None
    for klass in express_ConstantVal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_typenamelist_is_not_abstract():
    assert not inspect.isabstract(express_TypeNameList)


def test_express_typenamelist_constructor_exists():
    assert callable(express_TypeNameList.__init__)


def test_express_typenamelist_constructor_args():
    sig = inspect.signature(express_TypeNameList.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_express_typenamelist_has_type():
    assert hasattr(express_TypeNameList, "type")
    descriptor = None
    for klass in express_TypeNameList.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_express_reference_is_not_abstract():
    assert not inspect.isabstract(express_Reference)


def test_express_reference_constructor_exists():
    assert callable(express_Reference.__init__)


def test_express_reference_constructor_args():
    sig = inspect.signature(express_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "self" in params, "Missing parameter 'self'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"

def test_express_reference_has_self():
    assert hasattr(express_Reference, "self")
    descriptor = None
    for klass in express_Reference.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)

def test_express_reference_has_qualifier():
    assert hasattr(express_Reference, "qualifier")
    descriptor = None
    for klass in express_Reference.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_express_reference_has_optional():
    assert hasattr(express_Reference, "optional")
    descriptor = None
    for klass in express_Reference.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_express_reference_has_name():
    assert hasattr(express_Reference, "name")
    descriptor = None
    for klass in express_Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_uniquerule_is_not_abstract():
    assert not inspect.isabstract(express_UniqueRule)


def test_express_uniquerule_constructor_exists():
    assert callable(express_UniqueRule.__init__)


def test_express_uniquerule_constructor_args():
    sig = inspect.signature(express_UniqueRule.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "name" in params, "Missing parameter 'name'"

def test_express_uniquerule_has_attribute():
    assert hasattr(express_UniqueRule, "attribute")
    descriptor = None
    for klass in express_UniqueRule.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_express_uniquerule_has_name():
    assert hasattr(express_UniqueRule, "name")
    descriptor = None
    for klass in express_UniqueRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_attribute_is_not_abstract():
    assert not inspect.isabstract(express_Attribute)


def test_express_attribute_constructor_exists():
    assert callable(express_Attribute.__init__)


def test_express_attribute_constructor_args():
    sig = inspect.signature(express_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "self" in params, "Missing parameter 'self'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_express_attribute_has_self():
    assert hasattr(express_Attribute, "self")
    descriptor = None
    for klass in express_Attribute.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)

def test_express_attribute_has_optional():
    assert hasattr(express_Attribute, "optional")
    descriptor = None
    for klass in express_Attribute.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_express_attribute_has_name():
    assert hasattr(express_Attribute, "name")
    descriptor = None
    for klass in express_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express_attribute_has_expression():
    assert hasattr(express_Attribute, "expression")
    descriptor = None
    for klass in express_Attribute.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_express_attribute_has_qualifier():
    assert hasattr(express_Attribute, "qualifier")
    descriptor = None
    for klass in express_Attribute.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_express_datatype_is_not_abstract():
    assert not inspect.isabstract(express_DataType)


def test_express_datatype_constructor_exists():
    assert callable(express_DataType.__init__)


def test_express_datatype_constructor_args():
    sig = inspect.signature(express_DataType.__init__)
    params = list(sig.parameters.keys())



def test_expressconcept_is_not_abstract():
    assert not inspect.isabstract(ExpressConcept)


def test_expressconcept_constructor_exists():
    assert callable(ExpressConcept.__init__)


def test_expressconcept_constructor_args():
    sig = inspect.signature(ExpressConcept.__init__)
    params = list(sig.parameters.keys())



def test_express_entity_is_not_abstract():
    assert not inspect.isabstract(express_Entity)


def test_express_entity_constructor_exists():
    assert callable(express_Entity.__init__)


def test_express_entity_constructor_args():
    sig = inspect.signature(express_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_express_entity_has_abstract():
    assert hasattr(express_Entity, "abstract")
    descriptor = None
    for klass in express_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_express_whererule_is_not_abstract():
    assert not inspect.isabstract(express_WhereRule)


def test_express_whererule_constructor_exists():
    assert callable(express_WhereRule.__init__)


def test_express_whererule_constructor_args():
    sig = inspect.signature(express_WhereRule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_express_whererule_has_name():
    assert hasattr(express_WhereRule, "name")
    descriptor = None
    for klass in express_WhereRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express_whererule_has_expression():
    assert hasattr(express_WhereRule, "expression")
    descriptor = None
    for klass in express_WhereRule.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express_expressconcept_is_not_abstract():
    assert not inspect.isabstract(express_ExpressConcept)


def test_express_expressconcept_constructor_exists():
    assert callable(express_ExpressConcept.__init__)


def test_express_expressconcept_constructor_args():
    sig = inspect.signature(express_ExpressConcept.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_expressconcept_has_name():
    assert hasattr(express_ExpressConcept, "name")
    descriptor = None
    for klass in express_ExpressConcept.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_rule_is_not_abstract():
    assert not inspect.isabstract(express_Rule)


def test_express_rule_constructor_exists():
    assert callable(express_Rule.__init__)


def test_express_rule_constructor_args():
    sig = inspect.signature(express_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_rule_has_name():
    assert hasattr(express_Rule, "name")
    descriptor = None
    for klass in express_Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express_type_is_not_abstract():
    assert not inspect.isabstract(express_Type)


def test_express_type_constructor_exists():
    assert callable(express_Type.__init__)


def test_express_type_constructor_args():
    sig = inspect.signature(express_Type.__init__)
    params = list(sig.parameters.keys())



def test_express_schema_is_not_abstract():
    assert not inspect.isabstract(express_Schema)


def test_express_schema_constructor_exists():
    assert callable(express_Schema.__init__)


def test_express_schema_constructor_args():
    sig = inspect.signature(express_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express_schema_has_name():
    assert hasattr(express_Schema, "name")
    descriptor = None
    for klass in express_Schema.__mro__:
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
Index_strategy = st.builds(
    Index,
)
express_IndexTerminal_strategy = st.builds(
    express_IndexTerminal,
)
IndexTerminal_strategy = st.builds(
    IndexTerminal,
)
express_IntLiteral_strategy = st.builds(
    express_IntLiteral,
    value=
        st.integers()
)
express_VarLiteral_strategy = st.builds(
    express_VarLiteral,
    value=
        safe_text
)
express_Index_strategy = st.builds(
    express_Index,
)
VarOrAttrib_strategy = st.builds(
    VarOrAttrib,
)
express_IndexedVar_strategy = st.builds(
    express_IndexedVar,
)
express_AttributeVar_strategy = st.builds(
    express_AttributeVar,
)
express_SimpleVar_strategy = st.builds(
    express_SimpleVar,
    name=
        safe_text
)
express_VarOrAttrib_strategy = st.builds(
    express_VarOrAttrib,
)
express_CaseAction_strategy = st.builds(
    express_CaseAction,
    value=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
express_IfStatement_strategy = st.builds(
    express_IfStatement,
)
express_CaseStatement_strategy = st.builds(
    express_CaseStatement,
    variable=
        safe_text
)
express_EscapeStatement_strategy = st.builds(
    express_EscapeStatement,
)
express_Assignment_strategy = st.builds(
    express_Assignment,
    expression=
        safe_text
)
express_ReturnStatement_strategy = st.builds(
    express_ReturnStatement,
    expression=
        safe_text
)
express_RepeatStatement_strategy = st.builds(
    express_RepeatStatement,
    idx=
        safe_text,
    start=
        safe_text,
    end=
        safe_text
)
express_SequenceStatement_strategy = st.builds(
    express_SequenceStatement,
    expression=
        safe_text
)
express_LiteralType_strategy = st.builds(
    express_LiteralType,
    name=
        safe_text
)
BuiltInType_strategy = st.builds(
    BuiltInType,
)
express_IntegerType_strategy = st.builds(
    express_IntegerType,
)
express_BooleanType_strategy = st.builds(
    express_BooleanType,
)
express_NumberType_strategy = st.builds(
    express_NumberType,
)
express_BinaryType_strategy = st.builds(
    express_BinaryType,
    size=
        st.integers()
)
express_RealType_strategy = st.builds(
    express_RealType,
)
express_LogicalType_strategy = st.builds(
    express_LogicalType,
)
express_StringType_strategy = st.builds(
    express_StringType,
    fixed=
        st.booleans(),
    size=
        st.integers()
)
DataType_strategy = st.builds(
    DataType,
)
express_EnumType_strategy = st.builds(
    express_EnumType,
)
express_SelectType_strategy = st.builds(
    express_SelectType,
)
express_CollectionType_strategy = st.builds(
    express_CollectionType,
    opt=
        st.booleans(),
    unique=
        st.booleans(),
    many=
        st.booleans(),
    name=
        safe_text,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)
express_GenericType_strategy = st.builds(
    express_GenericType,
    typelabel=
        safe_text
)
express_ReferenceType_strategy = st.builds(
    express_ReferenceType,
)
express_BuiltInType_strategy = st.builds(
    express_BuiltInType,
)
express_Intervall_strategy = st.builds(
    express_Intervall,
    expression=
        safe_text
)
express_FormalParam_strategy = st.builds(
    express_FormalParam,
    paramName=
        safe_text
)
express_ParameterList_strategy = st.builds(
    express_ParameterList,
)
express_FunctionExpression_strategy = st.builds(
    express_FunctionExpression,
    name=
        safe_text
)
express_Line_strategy = st.builds(
    express_Line,
    text=
        safe_text
)
express_Statement_strategy = st.builds(
    express_Statement,
)
express_LocalVar_strategy = st.builds(
    express_LocalVar,
    varname=
        safe_text
)
express_Function_strategy = st.builds(
    express_Function,
    name=
        safe_text
)
express_ConstantVal_strategy = st.builds(
    express_ConstantVal,
    name=
        safe_text
)
express_TypeNameList_strategy = st.builds(
    express_TypeNameList,
    type=
        safe_text
)
express_Reference_strategy = st.builds(
    express_Reference,
    self=
        st.booleans(),
    qualifier=
        safe_text,
    optional=
        st.booleans(),
    name=
        safe_text
)
express_UniqueRule_strategy = st.builds(
    express_UniqueRule,
    attribute=
        safe_text,
    name=
        safe_text
)
express_Attribute_strategy = st.builds(
    express_Attribute,
    self=
        st.booleans(),
    optional=
        st.booleans(),
    name=
        safe_text,
    expression=
        safe_text,
    qualifier=
        safe_text
)
express_DataType_strategy = st.builds(
    express_DataType,
)
ExpressConcept_strategy = st.builds(
    ExpressConcept,
)
express_Entity_strategy = st.builds(
    express_Entity,
    abstract=
        st.booleans()
)
express_WhereRule_strategy = st.builds(
    express_WhereRule,
    name=
        safe_text,
    expression=
        safe_text
)
express_ExpressConcept_strategy = st.builds(
    express_ExpressConcept,
    name=
        safe_text
)
express_Rule_strategy = st.builds(
    express_Rule,
    name=
        safe_text
)
express_Type_strategy = st.builds(
    express_Type,
)
express_Schema_strategy = st.builds(
    express_Schema,
    name=
        safe_text
)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=express_IndexTerminal_strategy)
@settings(max_examples=50)
def test_express_indexterminal_instantiation(instance):
    assert isinstance(instance, express_IndexTerminal)

@given(instance=IndexTerminal_strategy)
@settings(max_examples=50)
def test_indexterminal_instantiation(instance):
    assert isinstance(instance, IndexTerminal)

@given(instance=express_IntLiteral_strategy)
@settings(max_examples=50)
def test_express_intliteral_instantiation(instance):
    assert isinstance(instance, express_IntLiteral)



@given(instance=express_IntLiteral_strategy)
def test_express_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=express_VarLiteral_strategy)
@settings(max_examples=50)
def test_express_varliteral_instantiation(instance):
    assert isinstance(instance, express_VarLiteral)



@given(instance=express_VarLiteral_strategy)
def test_express_varliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=express_Index_strategy)
@settings(max_examples=50)
def test_express_index_instantiation(instance):
    assert isinstance(instance, express_Index)

@given(instance=VarOrAttrib_strategy)
@settings(max_examples=50)
def test_varorattrib_instantiation(instance):
    assert isinstance(instance, VarOrAttrib)

@given(instance=express_IndexedVar_strategy)
@settings(max_examples=50)
def test_express_indexedvar_instantiation(instance):
    assert isinstance(instance, express_IndexedVar)

@given(instance=express_AttributeVar_strategy)
@settings(max_examples=50)
def test_express_attributevar_instantiation(instance):
    assert isinstance(instance, express_AttributeVar)

@given(instance=express_SimpleVar_strategy)
@settings(max_examples=50)
def test_express_simplevar_instantiation(instance):
    assert isinstance(instance, express_SimpleVar)



@given(instance=express_SimpleVar_strategy)
def test_express_simplevar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_VarOrAttrib_strategy)
@settings(max_examples=50)
def test_express_varorattrib_instantiation(instance):
    assert isinstance(instance, express_VarOrAttrib)

@given(instance=express_CaseAction_strategy)
@settings(max_examples=50)
def test_express_caseaction_instantiation(instance):
    assert isinstance(instance, express_CaseAction)



@given(instance=express_CaseAction_strategy)
def test_express_caseaction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=express_IfStatement_strategy)
@settings(max_examples=50)
def test_express_ifstatement_instantiation(instance):
    assert isinstance(instance, express_IfStatement)

@given(instance=express_CaseStatement_strategy)
@settings(max_examples=50)
def test_express_casestatement_instantiation(instance):
    assert isinstance(instance, express_CaseStatement)



@given(instance=express_CaseStatement_strategy)
def test_express_casestatement_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=express_EscapeStatement_strategy)
@settings(max_examples=50)
def test_express_escapestatement_instantiation(instance):
    assert isinstance(instance, express_EscapeStatement)

@given(instance=express_Assignment_strategy)
@settings(max_examples=50)
def test_express_assignment_instantiation(instance):
    assert isinstance(instance, express_Assignment)



@given(instance=express_Assignment_strategy)
def test_express_assignment_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express_ReturnStatement_strategy)
@settings(max_examples=50)
def test_express_returnstatement_instantiation(instance):
    assert isinstance(instance, express_ReturnStatement)



@given(instance=express_ReturnStatement_strategy)
def test_express_returnstatement_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express_RepeatStatement_strategy)
@settings(max_examples=50)
def test_express_repeatstatement_instantiation(instance):
    assert isinstance(instance, express_RepeatStatement)



@given(instance=express_RepeatStatement_strategy)
def test_express_repeatstatement_idx_setter(instance):
    original = instance.idx
    instance.idx = original
    assert instance.idx == original



@given(instance=express_RepeatStatement_strategy)
def test_express_repeatstatement_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=express_RepeatStatement_strategy)
def test_express_repeatstatement_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=express_SequenceStatement_strategy)
@settings(max_examples=50)
def test_express_sequencestatement_instantiation(instance):
    assert isinstance(instance, express_SequenceStatement)



@given(instance=express_SequenceStatement_strategy)
def test_express_sequencestatement_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express_LiteralType_strategy)
@settings(max_examples=50)
def test_express_literaltype_instantiation(instance):
    assert isinstance(instance, express_LiteralType)



@given(instance=express_LiteralType_strategy)
def test_express_literaltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BuiltInType_strategy)
@settings(max_examples=50)
def test_builtintype_instantiation(instance):
    assert isinstance(instance, BuiltInType)

@given(instance=express_IntegerType_strategy)
@settings(max_examples=50)
def test_express_integertype_instantiation(instance):
    assert isinstance(instance, express_IntegerType)

@given(instance=express_BooleanType_strategy)
@settings(max_examples=50)
def test_express_booleantype_instantiation(instance):
    assert isinstance(instance, express_BooleanType)

@given(instance=express_NumberType_strategy)
@settings(max_examples=50)
def test_express_numbertype_instantiation(instance):
    assert isinstance(instance, express_NumberType)

@given(instance=express_BinaryType_strategy)
@settings(max_examples=50)
def test_express_binarytype_instantiation(instance):
    assert isinstance(instance, express_BinaryType)



@given(instance=express_BinaryType_strategy)
def test_express_binarytype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=express_RealType_strategy)
@settings(max_examples=50)
def test_express_realtype_instantiation(instance):
    assert isinstance(instance, express_RealType)

@given(instance=express_LogicalType_strategy)
@settings(max_examples=50)
def test_express_logicaltype_instantiation(instance):
    assert isinstance(instance, express_LogicalType)

@given(instance=express_StringType_strategy)
@settings(max_examples=50)
def test_express_stringtype_instantiation(instance):
    assert isinstance(instance, express_StringType)



@given(instance=express_StringType_strategy)
def test_express_stringtype_fixed_setter(instance):
    original = instance.fixed
    instance.fixed = original
    assert instance.fixed == original



@given(instance=express_StringType_strategy)
def test_express_stringtype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=express_EnumType_strategy)
@settings(max_examples=50)
def test_express_enumtype_instantiation(instance):
    assert isinstance(instance, express_EnumType)

@given(instance=express_SelectType_strategy)
@settings(max_examples=50)
def test_express_selecttype_instantiation(instance):
    assert isinstance(instance, express_SelectType)

@given(instance=express_CollectionType_strategy)
@settings(max_examples=50)
def test_express_collectiontype_instantiation(instance):
    assert isinstance(instance, express_CollectionType)



@given(instance=express_CollectionType_strategy)
def test_express_collectiontype_opt_setter(instance):
    original = instance.opt
    instance.opt = original
    assert instance.opt == original



@given(instance=express_CollectionType_strategy)
def test_express_collectiontype_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=express_CollectionType_strategy)
def test_express_collectiontype_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=express_CollectionType_strategy)
def test_express_collectiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=express_CollectionType_strategy)
def test_express_collectiontype_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=express_CollectionType_strategy)
def test_express_collectiontype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=express_GenericType_strategy)
@settings(max_examples=50)
def test_express_generictype_instantiation(instance):
    assert isinstance(instance, express_GenericType)



@given(instance=express_GenericType_strategy)
def test_express_generictype_typelabel_setter(instance):
    original = instance.typelabel
    instance.typelabel = original
    assert instance.typelabel == original

@given(instance=express_ReferenceType_strategy)
@settings(max_examples=50)
def test_express_referencetype_instantiation(instance):
    assert isinstance(instance, express_ReferenceType)

@given(instance=express_BuiltInType_strategy)
@settings(max_examples=50)
def test_express_builtintype_instantiation(instance):
    assert isinstance(instance, express_BuiltInType)

@given(instance=express_Intervall_strategy)
@settings(max_examples=50)
def test_express_intervall_instantiation(instance):
    assert isinstance(instance, express_Intervall)



@given(instance=express_Intervall_strategy)
def test_express_intervall_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express_FormalParam_strategy)
@settings(max_examples=50)
def test_express_formalparam_instantiation(instance):
    assert isinstance(instance, express_FormalParam)



@given(instance=express_FormalParam_strategy)
def test_express_formalparam_paramName_setter(instance):
    original = instance.paramName
    instance.paramName = original
    assert instance.paramName == original

@given(instance=express_ParameterList_strategy)
@settings(max_examples=50)
def test_express_parameterlist_instantiation(instance):
    assert isinstance(instance, express_ParameterList)

@given(instance=express_FunctionExpression_strategy)
@settings(max_examples=50)
def test_express_functionexpression_instantiation(instance):
    assert isinstance(instance, express_FunctionExpression)



@given(instance=express_FunctionExpression_strategy)
def test_express_functionexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_Line_strategy)
@settings(max_examples=50)
def test_express_line_instantiation(instance):
    assert isinstance(instance, express_Line)



@given(instance=express_Line_strategy)
def test_express_line_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=express_Statement_strategy)
@settings(max_examples=50)
def test_express_statement_instantiation(instance):
    assert isinstance(instance, express_Statement)

@given(instance=express_LocalVar_strategy)
@settings(max_examples=50)
def test_express_localvar_instantiation(instance):
    assert isinstance(instance, express_LocalVar)



@given(instance=express_LocalVar_strategy)
def test_express_localvar_varname_setter(instance):
    original = instance.varname
    instance.varname = original
    assert instance.varname == original

@given(instance=express_Function_strategy)
@settings(max_examples=50)
def test_express_function_instantiation(instance):
    assert isinstance(instance, express_Function)



@given(instance=express_Function_strategy)
def test_express_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_ConstantVal_strategy)
@settings(max_examples=50)
def test_express_constantval_instantiation(instance):
    assert isinstance(instance, express_ConstantVal)



@given(instance=express_ConstantVal_strategy)
def test_express_constantval_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_TypeNameList_strategy)
@settings(max_examples=50)
def test_express_typenamelist_instantiation(instance):
    assert isinstance(instance, express_TypeNameList)



@given(instance=express_TypeNameList_strategy)
def test_express_typenamelist_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=express_Reference_strategy)
@settings(max_examples=50)
def test_express_reference_instantiation(instance):
    assert isinstance(instance, express_Reference)



@given(instance=express_Reference_strategy)
def test_express_reference_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original



@given(instance=express_Reference_strategy)
def test_express_reference_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original



@given(instance=express_Reference_strategy)
def test_express_reference_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=express_Reference_strategy)
def test_express_reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_UniqueRule_strategy)
@settings(max_examples=50)
def test_express_uniquerule_instantiation(instance):
    assert isinstance(instance, express_UniqueRule)



@given(instance=express_UniqueRule_strategy)
def test_express_uniquerule_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=express_UniqueRule_strategy)
def test_express_uniquerule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_Attribute_strategy)
@settings(max_examples=50)
def test_express_attribute_instantiation(instance):
    assert isinstance(instance, express_Attribute)



@given(instance=express_Attribute_strategy)
def test_express_attribute_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original



@given(instance=express_Attribute_strategy)
def test_express_attribute_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=express_Attribute_strategy)
def test_express_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=express_Attribute_strategy)
def test_express_attribute_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=express_Attribute_strategy)
def test_express_attribute_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=express_DataType_strategy)
@settings(max_examples=50)
def test_express_datatype_instantiation(instance):
    assert isinstance(instance, express_DataType)

@given(instance=ExpressConcept_strategy)
@settings(max_examples=50)
def test_expressconcept_instantiation(instance):
    assert isinstance(instance, ExpressConcept)

@given(instance=express_Entity_strategy)
@settings(max_examples=50)
def test_express_entity_instantiation(instance):
    assert isinstance(instance, express_Entity)



@given(instance=express_Entity_strategy)
def test_express_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=express_WhereRule_strategy)
@settings(max_examples=50)
def test_express_whererule_instantiation(instance):
    assert isinstance(instance, express_WhereRule)



@given(instance=express_WhereRule_strategy)
def test_express_whererule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=express_WhereRule_strategy)
def test_express_whererule_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express_ExpressConcept_strategy)
@settings(max_examples=50)
def test_express_expressconcept_instantiation(instance):
    assert isinstance(instance, express_ExpressConcept)



@given(instance=express_ExpressConcept_strategy)
def test_express_expressconcept_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_Rule_strategy)
@settings(max_examples=50)
def test_express_rule_instantiation(instance):
    assert isinstance(instance, express_Rule)



@given(instance=express_Rule_strategy)
def test_express_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express_Type_strategy)
@settings(max_examples=50)
def test_express_type_instantiation(instance):
    assert isinstance(instance, express_Type)

@given(instance=express_Schema_strategy)
@settings(max_examples=50)
def test_express_schema_instantiation(instance):
    assert isinstance(instance, express_Schema)



@given(instance=express_Schema_strategy)
def test_express_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
