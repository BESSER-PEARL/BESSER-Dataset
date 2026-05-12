import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    classifierTypeRule,
    ale_ClassifierType,
    Expression,
    ale_Comp,
    ale_Not,
    ale_Conditional,
    ale_Lit,
    ale_Or,
    ale_Xor,
    ale_Min,
    ale_VarRef,
    ale_And,
    ale_Implie,
    ale_Let,
    ale_Call,
    typeLiteral,
    ale_IntType,
    ale_StringType,
    ale_SetType,
    ale_BoolType,
    ale_RealType,
    ale_SeqType,
    ale_ClassifierSetType,
    ale_classifierTypeRule,
    rType,
    literal,
    ale_Sequence,
    ale_Int,
    ale_False,
    ale_Null,
    ale_String,
    ale_Real,
    ale_Enum,
    ale_True,
    ale_OrderedSet,
    ale_literal,
    ale_Add,
    ale_Mult,
    ale_Apply,
    ale_Feature,
    ale_rCase,
    ale_typeLiteral,
    ale_binding,
    ale_EObject,
    ale_Collection,
    ale_rSwitch,
    ale_Block,
    ale_Variable,
    ale_rType,
    ale_Tag,
    ale_Expression,
    Statement,
    ale_If,
    ale_ForEach,
    ale_Insert,
    ale_Assign,
    ale_While,
    ale_Remove,
    ale_VarDecl,
    ale_Statement,
    ale_ExpressionStmt,
    ale_rOpposite,
    ale_Unit,
    BehavioredClass,
    ale_RuntimeClass,
    ale_ExtendedClass,
    ale_Operation,
    ale_Attribute,
    ale_BehavioredClass,
    ale_Service,
    ale_Import,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classifiertyperule_is_not_abstract():
    assert not inspect.isabstract(classifierTypeRule)


def test_classifiertyperule_constructor_exists():
    assert callable(classifierTypeRule.__init__)


def test_classifiertyperule_constructor_args():
    sig = inspect.signature(classifierTypeRule.__init__)
    params = list(sig.parameters.keys())



def test_ale_classifiertype_is_not_abstract():
    assert not inspect.isabstract(ale_ClassifierType)


def test_ale_classifiertype_constructor_exists():
    assert callable(ale_ClassifierType.__init__)


def test_ale_classifiertype_constructor_args():
    sig = inspect.signature(ale_ClassifierType.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "packageName" in params, "Missing parameter 'packageName'"

def test_ale_classifiertype_has_className():
    assert hasattr(ale_ClassifierType, "className")
    descriptor = None
    for klass in ale_ClassifierType.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_ale_classifiertype_has_packageName():
    assert hasattr(ale_ClassifierType, "packageName")
    descriptor = None
    for klass in ale_ClassifierType.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ale_comp_is_not_abstract():
    assert not inspect.isabstract(ale_Comp)


def test_ale_comp_constructor_exists():
    assert callable(ale_Comp.__init__)


def test_ale_comp_constructor_args():
    sig = inspect.signature(ale_Comp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_ale_comp_has_op():
    assert hasattr(ale_Comp, "op")
    descriptor = None
    for klass in ale_Comp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_ale_not_is_not_abstract():
    assert not inspect.isabstract(ale_Not)


def test_ale_not_constructor_exists():
    assert callable(ale_Not.__init__)


def test_ale_not_constructor_args():
    sig = inspect.signature(ale_Not.__init__)
    params = list(sig.parameters.keys())



def test_ale_conditional_is_not_abstract():
    assert not inspect.isabstract(ale_Conditional)


def test_ale_conditional_constructor_exists():
    assert callable(ale_Conditional.__init__)


def test_ale_conditional_constructor_args():
    sig = inspect.signature(ale_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_ale_lit_is_not_abstract():
    assert not inspect.isabstract(ale_Lit)


def test_ale_lit_constructor_exists():
    assert callable(ale_Lit.__init__)


def test_ale_lit_constructor_args():
    sig = inspect.signature(ale_Lit.__init__)
    params = list(sig.parameters.keys())



def test_ale_or_is_not_abstract():
    assert not inspect.isabstract(ale_Or)


def test_ale_or_constructor_exists():
    assert callable(ale_Or.__init__)


def test_ale_or_constructor_args():
    sig = inspect.signature(ale_Or.__init__)
    params = list(sig.parameters.keys())



def test_ale_xor_is_not_abstract():
    assert not inspect.isabstract(ale_Xor)


def test_ale_xor_constructor_exists():
    assert callable(ale_Xor.__init__)


def test_ale_xor_constructor_args():
    sig = inspect.signature(ale_Xor.__init__)
    params = list(sig.parameters.keys())



def test_ale_min_is_not_abstract():
    assert not inspect.isabstract(ale_Min)


def test_ale_min_constructor_exists():
    assert callable(ale_Min.__init__)


def test_ale_min_constructor_args():
    sig = inspect.signature(ale_Min.__init__)
    params = list(sig.parameters.keys())



def test_ale_varref_is_not_abstract():
    assert not inspect.isabstract(ale_VarRef)


def test_ale_varref_constructor_exists():
    assert callable(ale_VarRef.__init__)


def test_ale_varref_constructor_args():
    sig = inspect.signature(ale_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_ale_varref_has_ID():
    assert hasattr(ale_VarRef, "ID")
    descriptor = None
    for klass in ale_VarRef.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_ale_and_is_not_abstract():
    assert not inspect.isabstract(ale_And)


def test_ale_and_constructor_exists():
    assert callable(ale_And.__init__)


def test_ale_and_constructor_args():
    sig = inspect.signature(ale_And.__init__)
    params = list(sig.parameters.keys())



def test_ale_implie_is_not_abstract():
    assert not inspect.isabstract(ale_Implie)


def test_ale_implie_constructor_exists():
    assert callable(ale_Implie.__init__)


def test_ale_implie_constructor_args():
    sig = inspect.signature(ale_Implie.__init__)
    params = list(sig.parameters.keys())



def test_ale_let_is_not_abstract():
    assert not inspect.isabstract(ale_Let)


def test_ale_let_constructor_exists():
    assert callable(ale_Let.__init__)


def test_ale_let_constructor_args():
    sig = inspect.signature(ale_Let.__init__)
    params = list(sig.parameters.keys())



def test_ale_call_is_not_abstract():
    assert not inspect.isabstract(ale_Call)


def test_ale_call_constructor_exists():
    assert callable(ale_Call.__init__)


def test_ale_call_constructor_args():
    sig = inspect.signature(ale_Call.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_call_has_name():
    assert hasattr(ale_Call, "name")
    descriptor = None
    for klass in ale_Call.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeliteral_is_not_abstract():
    assert not inspect.isabstract(typeLiteral)


def test_typeliteral_constructor_exists():
    assert callable(typeLiteral.__init__)


def test_typeliteral_constructor_args():
    sig = inspect.signature(typeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ale_inttype_is_not_abstract():
    assert not inspect.isabstract(ale_IntType)


def test_ale_inttype_constructor_exists():
    assert callable(ale_IntType.__init__)


def test_ale_inttype_constructor_args():
    sig = inspect.signature(ale_IntType.__init__)
    params = list(sig.parameters.keys())



def test_ale_stringtype_is_not_abstract():
    assert not inspect.isabstract(ale_StringType)


def test_ale_stringtype_constructor_exists():
    assert callable(ale_StringType.__init__)


def test_ale_stringtype_constructor_args():
    sig = inspect.signature(ale_StringType.__init__)
    params = list(sig.parameters.keys())



def test_ale_settype_is_not_abstract():
    assert not inspect.isabstract(ale_SetType)


def test_ale_settype_constructor_exists():
    assert callable(ale_SetType.__init__)


def test_ale_settype_constructor_args():
    sig = inspect.signature(ale_SetType.__init__)
    params = list(sig.parameters.keys())



def test_ale_booltype_is_not_abstract():
    assert not inspect.isabstract(ale_BoolType)


def test_ale_booltype_constructor_exists():
    assert callable(ale_BoolType.__init__)


def test_ale_booltype_constructor_args():
    sig = inspect.signature(ale_BoolType.__init__)
    params = list(sig.parameters.keys())



def test_ale_realtype_is_not_abstract():
    assert not inspect.isabstract(ale_RealType)


def test_ale_realtype_constructor_exists():
    assert callable(ale_RealType.__init__)


def test_ale_realtype_constructor_args():
    sig = inspect.signature(ale_RealType.__init__)
    params = list(sig.parameters.keys())



def test_ale_seqtype_is_not_abstract():
    assert not inspect.isabstract(ale_SeqType)


def test_ale_seqtype_constructor_exists():
    assert callable(ale_SeqType.__init__)


def test_ale_seqtype_constructor_args():
    sig = inspect.signature(ale_SeqType.__init__)
    params = list(sig.parameters.keys())



def test_ale_classifiersettype_is_not_abstract():
    assert not inspect.isabstract(ale_ClassifierSetType)


def test_ale_classifiersettype_constructor_exists():
    assert callable(ale_ClassifierSetType.__init__)


def test_ale_classifiersettype_constructor_args():
    sig = inspect.signature(ale_ClassifierSetType.__init__)
    params = list(sig.parameters.keys())



def test_ale_classifiertyperule_is_not_abstract():
    assert not inspect.isabstract(ale_classifierTypeRule)


def test_ale_classifiertyperule_constructor_exists():
    assert callable(ale_classifierTypeRule.__init__)


def test_ale_classifiertyperule_constructor_args():
    sig = inspect.signature(ale_classifierTypeRule.__init__)
    params = list(sig.parameters.keys())



def test_rtype_is_not_abstract():
    assert not inspect.isabstract(rType)


def test_rtype_constructor_exists():
    assert callable(rType.__init__)


def test_rtype_constructor_args():
    sig = inspect.signature(rType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(literal)


def test_literal_constructor_exists():
    assert callable(literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(literal.__init__)
    params = list(sig.parameters.keys())



def test_ale_sequence_is_not_abstract():
    assert not inspect.isabstract(ale_Sequence)


def test_ale_sequence_constructor_exists():
    assert callable(ale_Sequence.__init__)


def test_ale_sequence_constructor_args():
    sig = inspect.signature(ale_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_ale_int_is_not_abstract():
    assert not inspect.isabstract(ale_Int)


def test_ale_int_constructor_exists():
    assert callable(ale_Int.__init__)


def test_ale_int_constructor_args():
    sig = inspect.signature(ale_Int.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ale_int_has_value():
    assert hasattr(ale_Int, "value")
    descriptor = None
    for klass in ale_Int.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ale_false_is_not_abstract():
    assert not inspect.isabstract(ale_False)


def test_ale_false_constructor_exists():
    assert callable(ale_False.__init__)


def test_ale_false_constructor_args():
    sig = inspect.signature(ale_False.__init__)
    params = list(sig.parameters.keys())



def test_ale_null_is_not_abstract():
    assert not inspect.isabstract(ale_Null)


def test_ale_null_constructor_exists():
    assert callable(ale_Null.__init__)


def test_ale_null_constructor_args():
    sig = inspect.signature(ale_Null.__init__)
    params = list(sig.parameters.keys())



def test_ale_string_is_not_abstract():
    assert not inspect.isabstract(ale_String)


def test_ale_string_constructor_exists():
    assert callable(ale_String.__init__)


def test_ale_string_constructor_args():
    sig = inspect.signature(ale_String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ale_string_has_value():
    assert hasattr(ale_String, "value")
    descriptor = None
    for klass in ale_String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ale_real_is_not_abstract():
    assert not inspect.isabstract(ale_Real)


def test_ale_real_constructor_exists():
    assert callable(ale_Real.__init__)


def test_ale_real_constructor_args():
    sig = inspect.signature(ale_Real.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ale_real_has_value():
    assert hasattr(ale_Real, "value")
    descriptor = None
    for klass in ale_Real.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ale_enum_is_not_abstract():
    assert not inspect.isabstract(ale_Enum)


def test_ale_enum_constructor_exists():
    assert callable(ale_Enum.__init__)


def test_ale_enum_constructor_args():
    sig = inspect.signature(ale_Enum.__init__)
    params = list(sig.parameters.keys())



def test_ale_true_is_not_abstract():
    assert not inspect.isabstract(ale_True)


def test_ale_true_constructor_exists():
    assert callable(ale_True.__init__)


def test_ale_true_constructor_args():
    sig = inspect.signature(ale_True.__init__)
    params = list(sig.parameters.keys())



def test_ale_orderedset_is_not_abstract():
    assert not inspect.isabstract(ale_OrderedSet)


def test_ale_orderedset_constructor_exists():
    assert callable(ale_OrderedSet.__init__)


def test_ale_orderedset_constructor_args():
    sig = inspect.signature(ale_OrderedSet.__init__)
    params = list(sig.parameters.keys())



def test_ale_literal_is_not_abstract():
    assert not inspect.isabstract(ale_literal)


def test_ale_literal_constructor_exists():
    assert callable(ale_literal.__init__)


def test_ale_literal_constructor_args():
    sig = inspect.signature(ale_literal.__init__)
    params = list(sig.parameters.keys())



def test_ale_add_is_not_abstract():
    assert not inspect.isabstract(ale_Add)


def test_ale_add_constructor_exists():
    assert callable(ale_Add.__init__)


def test_ale_add_constructor_args():
    sig = inspect.signature(ale_Add.__init__)
    params = list(sig.parameters.keys())



def test_ale_mult_is_not_abstract():
    assert not inspect.isabstract(ale_Mult)


def test_ale_mult_constructor_exists():
    assert callable(ale_Mult.__init__)


def test_ale_mult_constructor_args():
    sig = inspect.signature(ale_Mult.__init__)
    params = list(sig.parameters.keys())



def test_ale_apply_is_not_abstract():
    assert not inspect.isabstract(ale_Apply)


def test_ale_apply_constructor_exists():
    assert callable(ale_Apply.__init__)


def test_ale_apply_constructor_args():
    sig = inspect.signature(ale_Apply.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_ale_apply_has_name():
    assert hasattr(ale_Apply, "name")
    descriptor = None
    for klass in ale_Apply.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ale_apply_has_varName():
    assert hasattr(ale_Apply, "varName")
    descriptor = None
    for klass in ale_Apply.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_ale_feature_is_not_abstract():
    assert not inspect.isabstract(ale_Feature)


def test_ale_feature_constructor_exists():
    assert callable(ale_Feature.__init__)


def test_ale_feature_constructor_args():
    sig = inspect.signature(ale_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_ale_feature_has_feature():
    assert hasattr(ale_Feature, "feature")
    descriptor = None
    for klass in ale_Feature.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_ale_rcase_is_not_abstract():
    assert not inspect.isabstract(ale_rCase)


def test_ale_rcase_constructor_exists():
    assert callable(ale_rCase.__init__)


def test_ale_rcase_constructor_args():
    sig = inspect.signature(ale_rCase.__init__)
    params = list(sig.parameters.keys())



def test_ale_typeliteral_is_not_abstract():
    assert not inspect.isabstract(ale_typeLiteral)


def test_ale_typeliteral_constructor_exists():
    assert callable(ale_typeLiteral.__init__)


def test_ale_typeliteral_constructor_args():
    sig = inspect.signature(ale_typeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ale_binding_is_not_abstract():
    assert not inspect.isabstract(ale_binding)


def test_ale_binding_constructor_exists():
    assert callable(ale_binding.__init__)


def test_ale_binding_constructor_args():
    sig = inspect.signature(ale_binding.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_binding_has_name():
    assert hasattr(ale_binding, "name")
    descriptor = None
    for klass in ale_binding.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_eobject_is_not_abstract():
    assert not inspect.isabstract(ale_EObject)


def test_ale_eobject_constructor_exists():
    assert callable(ale_EObject.__init__)


def test_ale_eobject_constructor_args():
    sig = inspect.signature(ale_EObject.__init__)
    params = list(sig.parameters.keys())



def test_ale_collection_is_not_abstract():
    assert not inspect.isabstract(ale_Collection)


def test_ale_collection_constructor_exists():
    assert callable(ale_Collection.__init__)


def test_ale_collection_constructor_args():
    sig = inspect.signature(ale_Collection.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_ale_collection_has_min():
    assert hasattr(ale_Collection, "min")
    descriptor = None
    for klass in ale_Collection.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_ale_collection_has_max():
    assert hasattr(ale_Collection, "max")
    descriptor = None
    for klass in ale_Collection.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_ale_rswitch_is_not_abstract():
    assert not inspect.isabstract(ale_rSwitch)


def test_ale_rswitch_constructor_exists():
    assert callable(ale_rSwitch.__init__)


def test_ale_rswitch_constructor_args():
    sig = inspect.signature(ale_rSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "paramName" in params, "Missing parameter 'paramName'"

def test_ale_rswitch_has_paramName():
    assert hasattr(ale_rSwitch, "paramName")
    descriptor = None
    for klass in ale_rSwitch.__mro__:
        if "paramName" in klass.__dict__:
            descriptor = klass.__dict__["paramName"]
            break
    assert isinstance(descriptor, property)



def test_ale_block_is_not_abstract():
    assert not inspect.isabstract(ale_Block)


def test_ale_block_constructor_exists():
    assert callable(ale_Block.__init__)


def test_ale_block_constructor_args():
    sig = inspect.signature(ale_Block.__init__)
    params = list(sig.parameters.keys())



def test_ale_variable_is_not_abstract():
    assert not inspect.isabstract(ale_Variable)


def test_ale_variable_constructor_exists():
    assert callable(ale_Variable.__init__)


def test_ale_variable_constructor_args():
    sig = inspect.signature(ale_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_variable_has_name():
    assert hasattr(ale_Variable, "name")
    descriptor = None
    for klass in ale_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_rtype_is_not_abstract():
    assert not inspect.isabstract(ale_rType)


def test_ale_rtype_constructor_exists():
    assert callable(ale_rType.__init__)


def test_ale_rtype_constructor_args():
    sig = inspect.signature(ale_rType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_rtype_has_name():
    assert hasattr(ale_rType, "name")
    descriptor = None
    for klass in ale_rType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_tag_is_not_abstract():
    assert not inspect.isabstract(ale_Tag)


def test_ale_tag_constructor_exists():
    assert callable(ale_Tag.__init__)


def test_ale_tag_constructor_args():
    sig = inspect.signature(ale_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_tag_has_name():
    assert hasattr(ale_Tag, "name")
    descriptor = None
    for klass in ale_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_expression_is_not_abstract():
    assert not inspect.isabstract(ale_Expression)


def test_ale_expression_constructor_exists():
    assert callable(ale_Expression.__init__)


def test_ale_expression_constructor_args():
    sig = inspect.signature(ale_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_ale_if_is_not_abstract():
    assert not inspect.isabstract(ale_If)


def test_ale_if_constructor_exists():
    assert callable(ale_If.__init__)


def test_ale_if_constructor_args():
    sig = inspect.signature(ale_If.__init__)
    params = list(sig.parameters.keys())



def test_ale_foreach_is_not_abstract():
    assert not inspect.isabstract(ale_ForEach)


def test_ale_foreach_constructor_exists():
    assert callable(ale_ForEach.__init__)


def test_ale_foreach_constructor_args():
    sig = inspect.signature(ale_ForEach.__init__)
    params = list(sig.parameters.keys())
    assert "iterator" in params, "Missing parameter 'iterator'"

def test_ale_foreach_has_iterator():
    assert hasattr(ale_ForEach, "iterator")
    descriptor = None
    for klass in ale_ForEach.__mro__:
        if "iterator" in klass.__dict__:
            descriptor = klass.__dict__["iterator"]
            break
    assert isinstance(descriptor, property)



def test_ale_insert_is_not_abstract():
    assert not inspect.isabstract(ale_Insert)


def test_ale_insert_constructor_exists():
    assert callable(ale_Insert.__init__)


def test_ale_insert_constructor_args():
    sig = inspect.signature(ale_Insert.__init__)
    params = list(sig.parameters.keys())



def test_ale_assign_is_not_abstract():
    assert not inspect.isabstract(ale_Assign)


def test_ale_assign_constructor_exists():
    assert callable(ale_Assign.__init__)


def test_ale_assign_constructor_args():
    sig = inspect.signature(ale_Assign.__init__)
    params = list(sig.parameters.keys())



def test_ale_while_is_not_abstract():
    assert not inspect.isabstract(ale_While)


def test_ale_while_constructor_exists():
    assert callable(ale_While.__init__)


def test_ale_while_constructor_args():
    sig = inspect.signature(ale_While.__init__)
    params = list(sig.parameters.keys())



def test_ale_remove_is_not_abstract():
    assert not inspect.isabstract(ale_Remove)


def test_ale_remove_constructor_exists():
    assert callable(ale_Remove.__init__)


def test_ale_remove_constructor_args():
    sig = inspect.signature(ale_Remove.__init__)
    params = list(sig.parameters.keys())



def test_ale_vardecl_is_not_abstract():
    assert not inspect.isabstract(ale_VarDecl)


def test_ale_vardecl_constructor_exists():
    assert callable(ale_VarDecl.__init__)


def test_ale_vardecl_constructor_args():
    sig = inspect.signature(ale_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_vardecl_has_name():
    assert hasattr(ale_VarDecl, "name")
    descriptor = None
    for klass in ale_VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_statement_is_not_abstract():
    assert not inspect.isabstract(ale_Statement)


def test_ale_statement_constructor_exists():
    assert callable(ale_Statement.__init__)


def test_ale_statement_constructor_args():
    sig = inspect.signature(ale_Statement.__init__)
    params = list(sig.parameters.keys())



def test_ale_expressionstmt_is_not_abstract():
    assert not inspect.isabstract(ale_ExpressionStmt)


def test_ale_expressionstmt_constructor_exists():
    assert callable(ale_ExpressionStmt.__init__)


def test_ale_expressionstmt_constructor_args():
    sig = inspect.signature(ale_ExpressionStmt.__init__)
    params = list(sig.parameters.keys())



def test_ale_ropposite_is_not_abstract():
    assert not inspect.isabstract(ale_rOpposite)


def test_ale_ropposite_constructor_exists():
    assert callable(ale_rOpposite.__init__)


def test_ale_ropposite_constructor_args():
    sig = inspect.signature(ale_rOpposite.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_ropposite_has_name():
    assert hasattr(ale_rOpposite, "name")
    descriptor = None
    for klass in ale_rOpposite.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_unit_is_not_abstract():
    assert not inspect.isabstract(ale_Unit)


def test_ale_unit_constructor_exists():
    assert callable(ale_Unit.__init__)


def test_ale_unit_constructor_args():
    sig = inspect.signature(ale_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_unit_has_name():
    assert hasattr(ale_Unit, "name")
    descriptor = None
    for klass in ale_Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_behavioredclass_is_not_abstract():
    assert not inspect.isabstract(BehavioredClass)


def test_behavioredclass_constructor_exists():
    assert callable(BehavioredClass.__init__)


def test_behavioredclass_constructor_args():
    sig = inspect.signature(BehavioredClass.__init__)
    params = list(sig.parameters.keys())



def test_ale_runtimeclass_is_not_abstract():
    assert not inspect.isabstract(ale_RuntimeClass)


def test_ale_runtimeclass_constructor_exists():
    assert callable(ale_RuntimeClass.__init__)


def test_ale_runtimeclass_constructor_args():
    sig = inspect.signature(ale_RuntimeClass.__init__)
    params = list(sig.parameters.keys())



def test_ale_extendedclass_is_not_abstract():
    assert not inspect.isabstract(ale_ExtendedClass)


def test_ale_extendedclass_constructor_exists():
    assert callable(ale_ExtendedClass.__init__)


def test_ale_extendedclass_constructor_args():
    sig = inspect.signature(ale_ExtendedClass.__init__)
    params = list(sig.parameters.keys())
    assert "extends" in params, "Missing parameter 'extends'"

def test_ale_extendedclass_has_extends():
    assert hasattr(ale_ExtendedClass, "extends")
    descriptor = None
    for klass in ale_ExtendedClass.__mro__:
        if "extends" in klass.__dict__:
            descriptor = klass.__dict__["extends"]
            break
    assert isinstance(descriptor, property)



def test_ale_operation_is_not_abstract():
    assert not inspect.isabstract(ale_Operation)


def test_ale_operation_constructor_exists():
    assert callable(ale_Operation.__init__)


def test_ale_operation_constructor_args():
    sig = inspect.signature(ale_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_operation_has_name():
    assert hasattr(ale_Operation, "name")
    descriptor = None
    for klass in ale_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_attribute_is_not_abstract():
    assert not inspect.isabstract(ale_Attribute)


def test_ale_attribute_constructor_exists():
    assert callable(ale_Attribute.__init__)


def test_ale_attribute_constructor_args():
    sig = inspect.signature(ale_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "modifier" in params, "Missing parameter 'modifier'"
    assert "bounds" in params, "Missing parameter 'bounds'"

def test_ale_attribute_has_name():
    assert hasattr(ale_Attribute, "name")
    descriptor = None
    for klass in ale_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ale_attribute_has_modifier():
    assert hasattr(ale_Attribute, "modifier")
    descriptor = None
    for klass in ale_Attribute.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)

def test_ale_attribute_has_bounds():
    assert hasattr(ale_Attribute, "bounds")
    descriptor = None
    for klass in ale_Attribute.__mro__:
        if "bounds" in klass.__dict__:
            descriptor = klass.__dict__["bounds"]
            break
    assert isinstance(descriptor, property)



def test_ale_behavioredclass_is_not_abstract():
    assert not inspect.isabstract(ale_BehavioredClass)


def test_ale_behavioredclass_constructor_exists():
    assert callable(ale_BehavioredClass.__init__)


def test_ale_behavioredclass_constructor_args():
    sig = inspect.signature(ale_BehavioredClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_behavioredclass_has_name():
    assert hasattr(ale_BehavioredClass, "name")
    descriptor = None
    for klass in ale_BehavioredClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_service_is_not_abstract():
    assert not inspect.isabstract(ale_Service)


def test_ale_service_constructor_exists():
    assert callable(ale_Service.__init__)


def test_ale_service_constructor_args():
    sig = inspect.signature(ale_Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ale_service_has_name():
    assert hasattr(ale_Service, "name")
    descriptor = None
    for klass in ale_Service.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ale_import_is_not_abstract():
    assert not inspect.isabstract(ale_Import)


def test_ale_import_constructor_exists():
    assert callable(ale_Import.__init__)


def test_ale_import_constructor_args():
    sig = inspect.signature(ale_Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_ale_import_has_name():
    assert hasattr(ale_Import, "name")
    descriptor = None
    for klass in ale_Import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ale_import_has_alias():
    assert hasattr(ale_Import, "alias")
    descriptor = None
    for klass in ale_Import.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
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
classifierTypeRule_strategy = st.builds(
    classifierTypeRule,
)
ale_ClassifierType_strategy = st.builds(
    ale_ClassifierType,
    className=
        safe_text,
    packageName=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
ale_Comp_strategy = st.builds(
    ale_Comp,
    op=
        safe_text
)
ale_Not_strategy = st.builds(
    ale_Not,
)
ale_Conditional_strategy = st.builds(
    ale_Conditional,
)
ale_Lit_strategy = st.builds(
    ale_Lit,
)
ale_Or_strategy = st.builds(
    ale_Or,
)
ale_Xor_strategy = st.builds(
    ale_Xor,
)
ale_Min_strategy = st.builds(
    ale_Min,
)
ale_VarRef_strategy = st.builds(
    ale_VarRef,
    ID=
        safe_text
)
ale_And_strategy = st.builds(
    ale_And,
)
ale_Implie_strategy = st.builds(
    ale_Implie,
)
ale_Let_strategy = st.builds(
    ale_Let,
)
ale_Call_strategy = st.builds(
    ale_Call,
    name=
        safe_text
)
typeLiteral_strategy = st.builds(
    typeLiteral,
)
ale_IntType_strategy = st.builds(
    ale_IntType,
)
ale_StringType_strategy = st.builds(
    ale_StringType,
)
ale_SetType_strategy = st.builds(
    ale_SetType,
)
ale_BoolType_strategy = st.builds(
    ale_BoolType,
)
ale_RealType_strategy = st.builds(
    ale_RealType,
)
ale_SeqType_strategy = st.builds(
    ale_SeqType,
)
ale_ClassifierSetType_strategy = st.builds(
    ale_ClassifierSetType,
)
ale_classifierTypeRule_strategy = st.builds(
    ale_classifierTypeRule,
)
rType_strategy = st.builds(
    rType,
)
literal_strategy = st.builds(
    literal,
)
ale_Sequence_strategy = st.builds(
    ale_Sequence,
)
ale_Int_strategy = st.builds(
    ale_Int,
    value=
        st.integers()
)
ale_False_strategy = st.builds(
    ale_False,
)
ale_Null_strategy = st.builds(
    ale_Null,
)
ale_String_strategy = st.builds(
    ale_String,
    value=
        safe_text
)
ale_Real_strategy = st.builds(
    ale_Real,
    value=
        safe_text
)
ale_Enum_strategy = st.builds(
    ale_Enum,
)
ale_True_strategy = st.builds(
    ale_True,
)
ale_OrderedSet_strategy = st.builds(
    ale_OrderedSet,
)
ale_literal_strategy = st.builds(
    ale_literal,
)
ale_Add_strategy = st.builds(
    ale_Add,
)
ale_Mult_strategy = st.builds(
    ale_Mult,
)
ale_Apply_strategy = st.builds(
    ale_Apply,
    name=
        safe_text,
    varName=
        safe_text
)
ale_Feature_strategy = st.builds(
    ale_Feature,
    feature=
        safe_text
)
ale_rCase_strategy = st.builds(
    ale_rCase,
)
ale_typeLiteral_strategy = st.builds(
    ale_typeLiteral,
)
ale_binding_strategy = st.builds(
    ale_binding,
    name=
        safe_text
)
ale_EObject_strategy = st.builds(
    ale_EObject,
)
ale_Collection_strategy = st.builds(
    ale_Collection,
    min=
        st.integers(),
    max=
        st.integers()
)
ale_rSwitch_strategy = st.builds(
    ale_rSwitch,
    paramName=
        safe_text
)
ale_Block_strategy = st.builds(
    ale_Block,
)
ale_Variable_strategy = st.builds(
    ale_Variable,
    name=
        safe_text
)
ale_rType_strategy = st.builds(
    ale_rType,
    name=
        safe_text
)
ale_Tag_strategy = st.builds(
    ale_Tag,
    name=
        safe_text
)
ale_Expression_strategy = st.builds(
    ale_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
ale_If_strategy = st.builds(
    ale_If,
)
ale_ForEach_strategy = st.builds(
    ale_ForEach,
    iterator=
        safe_text
)
ale_Insert_strategy = st.builds(
    ale_Insert,
)
ale_Assign_strategy = st.builds(
    ale_Assign,
)
ale_While_strategy = st.builds(
    ale_While,
)
ale_Remove_strategy = st.builds(
    ale_Remove,
)
ale_VarDecl_strategy = st.builds(
    ale_VarDecl,
    name=
        safe_text
)
ale_Statement_strategy = st.builds(
    ale_Statement,
)
ale_ExpressionStmt_strategy = st.builds(
    ale_ExpressionStmt,
)
ale_rOpposite_strategy = st.builds(
    ale_rOpposite,
    name=
        safe_text
)
ale_Unit_strategy = st.builds(
    ale_Unit,
    name=
        safe_text
)
BehavioredClass_strategy = st.builds(
    BehavioredClass,
)
ale_RuntimeClass_strategy = st.builds(
    ale_RuntimeClass,
)
ale_ExtendedClass_strategy = st.builds(
    ale_ExtendedClass,
    extends=
        safe_text
)
ale_Operation_strategy = st.builds(
    ale_Operation,
    name=
        safe_text
)
ale_Attribute_strategy = st.builds(
    ale_Attribute,
    name=
        safe_text,
    modifier=
        safe_text,
    bounds=
        safe_text
)
ale_BehavioredClass_strategy = st.builds(
    ale_BehavioredClass,
    name=
        safe_text
)
ale_Service_strategy = st.builds(
    ale_Service,
    name=
        safe_text
)
ale_Import_strategy = st.builds(
    ale_Import,
    name=
        safe_text,
    alias=
        safe_text
)

@given(instance=classifierTypeRule_strategy)
@settings(max_examples=50)
def test_classifiertyperule_instantiation(instance):
    assert isinstance(instance, classifierTypeRule)

@given(instance=ale_ClassifierType_strategy)
@settings(max_examples=50)
def test_ale_classifiertype_instantiation(instance):
    assert isinstance(instance, ale_ClassifierType)



@given(instance=ale_ClassifierType_strategy)
def test_ale_classifiertype_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=ale_ClassifierType_strategy)
def test_ale_classifiertype_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ale_Comp_strategy)
@settings(max_examples=50)
def test_ale_comp_instantiation(instance):
    assert isinstance(instance, ale_Comp)



@given(instance=ale_Comp_strategy)
def test_ale_comp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ale_Not_strategy)
@settings(max_examples=50)
def test_ale_not_instantiation(instance):
    assert isinstance(instance, ale_Not)

@given(instance=ale_Conditional_strategy)
@settings(max_examples=50)
def test_ale_conditional_instantiation(instance):
    assert isinstance(instance, ale_Conditional)

@given(instance=ale_Lit_strategy)
@settings(max_examples=50)
def test_ale_lit_instantiation(instance):
    assert isinstance(instance, ale_Lit)

@given(instance=ale_Or_strategy)
@settings(max_examples=50)
def test_ale_or_instantiation(instance):
    assert isinstance(instance, ale_Or)

@given(instance=ale_Xor_strategy)
@settings(max_examples=50)
def test_ale_xor_instantiation(instance):
    assert isinstance(instance, ale_Xor)

@given(instance=ale_Min_strategy)
@settings(max_examples=50)
def test_ale_min_instantiation(instance):
    assert isinstance(instance, ale_Min)

@given(instance=ale_VarRef_strategy)
@settings(max_examples=50)
def test_ale_varref_instantiation(instance):
    assert isinstance(instance, ale_VarRef)



@given(instance=ale_VarRef_strategy)
def test_ale_varref_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=ale_And_strategy)
@settings(max_examples=50)
def test_ale_and_instantiation(instance):
    assert isinstance(instance, ale_And)

@given(instance=ale_Implie_strategy)
@settings(max_examples=50)
def test_ale_implie_instantiation(instance):
    assert isinstance(instance, ale_Implie)

@given(instance=ale_Let_strategy)
@settings(max_examples=50)
def test_ale_let_instantiation(instance):
    assert isinstance(instance, ale_Let)

@given(instance=ale_Call_strategy)
@settings(max_examples=50)
def test_ale_call_instantiation(instance):
    assert isinstance(instance, ale_Call)



@given(instance=ale_Call_strategy)
def test_ale_call_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeLiteral_strategy)
@settings(max_examples=50)
def test_typeliteral_instantiation(instance):
    assert isinstance(instance, typeLiteral)

@given(instance=ale_IntType_strategy)
@settings(max_examples=50)
def test_ale_inttype_instantiation(instance):
    assert isinstance(instance, ale_IntType)

@given(instance=ale_StringType_strategy)
@settings(max_examples=50)
def test_ale_stringtype_instantiation(instance):
    assert isinstance(instance, ale_StringType)

@given(instance=ale_SetType_strategy)
@settings(max_examples=50)
def test_ale_settype_instantiation(instance):
    assert isinstance(instance, ale_SetType)

@given(instance=ale_BoolType_strategy)
@settings(max_examples=50)
def test_ale_booltype_instantiation(instance):
    assert isinstance(instance, ale_BoolType)

@given(instance=ale_RealType_strategy)
@settings(max_examples=50)
def test_ale_realtype_instantiation(instance):
    assert isinstance(instance, ale_RealType)

@given(instance=ale_SeqType_strategy)
@settings(max_examples=50)
def test_ale_seqtype_instantiation(instance):
    assert isinstance(instance, ale_SeqType)

@given(instance=ale_ClassifierSetType_strategy)
@settings(max_examples=50)
def test_ale_classifiersettype_instantiation(instance):
    assert isinstance(instance, ale_ClassifierSetType)

@given(instance=ale_classifierTypeRule_strategy)
@settings(max_examples=50)
def test_ale_classifiertyperule_instantiation(instance):
    assert isinstance(instance, ale_classifierTypeRule)

@given(instance=rType_strategy)
@settings(max_examples=50)
def test_rtype_instantiation(instance):
    assert isinstance(instance, rType)

@given(instance=literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, literal)

@given(instance=ale_Sequence_strategy)
@settings(max_examples=50)
def test_ale_sequence_instantiation(instance):
    assert isinstance(instance, ale_Sequence)

@given(instance=ale_Int_strategy)
@settings(max_examples=50)
def test_ale_int_instantiation(instance):
    assert isinstance(instance, ale_Int)



@given(instance=ale_Int_strategy)
def test_ale_int_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ale_False_strategy)
@settings(max_examples=50)
def test_ale_false_instantiation(instance):
    assert isinstance(instance, ale_False)

@given(instance=ale_Null_strategy)
@settings(max_examples=50)
def test_ale_null_instantiation(instance):
    assert isinstance(instance, ale_Null)

@given(instance=ale_String_strategy)
@settings(max_examples=50)
def test_ale_string_instantiation(instance):
    assert isinstance(instance, ale_String)



@given(instance=ale_String_strategy)
def test_ale_string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ale_Real_strategy)
@settings(max_examples=50)
def test_ale_real_instantiation(instance):
    assert isinstance(instance, ale_Real)



@given(instance=ale_Real_strategy)
def test_ale_real_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ale_Enum_strategy)
@settings(max_examples=50)
def test_ale_enum_instantiation(instance):
    assert isinstance(instance, ale_Enum)

@given(instance=ale_True_strategy)
@settings(max_examples=50)
def test_ale_true_instantiation(instance):
    assert isinstance(instance, ale_True)

@given(instance=ale_OrderedSet_strategy)
@settings(max_examples=50)
def test_ale_orderedset_instantiation(instance):
    assert isinstance(instance, ale_OrderedSet)

@given(instance=ale_literal_strategy)
@settings(max_examples=50)
def test_ale_literal_instantiation(instance):
    assert isinstance(instance, ale_literal)

@given(instance=ale_Add_strategy)
@settings(max_examples=50)
def test_ale_add_instantiation(instance):
    assert isinstance(instance, ale_Add)

@given(instance=ale_Mult_strategy)
@settings(max_examples=50)
def test_ale_mult_instantiation(instance):
    assert isinstance(instance, ale_Mult)

@given(instance=ale_Apply_strategy)
@settings(max_examples=50)
def test_ale_apply_instantiation(instance):
    assert isinstance(instance, ale_Apply)



@given(instance=ale_Apply_strategy)
def test_ale_apply_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ale_Apply_strategy)
def test_ale_apply_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=ale_Feature_strategy)
@settings(max_examples=50)
def test_ale_feature_instantiation(instance):
    assert isinstance(instance, ale_Feature)



@given(instance=ale_Feature_strategy)
def test_ale_feature_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=ale_rCase_strategy)
@settings(max_examples=50)
def test_ale_rcase_instantiation(instance):
    assert isinstance(instance, ale_rCase)

@given(instance=ale_typeLiteral_strategy)
@settings(max_examples=50)
def test_ale_typeliteral_instantiation(instance):
    assert isinstance(instance, ale_typeLiteral)

@given(instance=ale_binding_strategy)
@settings(max_examples=50)
def test_ale_binding_instantiation(instance):
    assert isinstance(instance, ale_binding)



@given(instance=ale_binding_strategy)
def test_ale_binding_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_EObject_strategy)
@settings(max_examples=50)
def test_ale_eobject_instantiation(instance):
    assert isinstance(instance, ale_EObject)

@given(instance=ale_Collection_strategy)
@settings(max_examples=50)
def test_ale_collection_instantiation(instance):
    assert isinstance(instance, ale_Collection)



@given(instance=ale_Collection_strategy)
def test_ale_collection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=ale_Collection_strategy)
def test_ale_collection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=ale_rSwitch_strategy)
@settings(max_examples=50)
def test_ale_rswitch_instantiation(instance):
    assert isinstance(instance, ale_rSwitch)



@given(instance=ale_rSwitch_strategy)
def test_ale_rswitch_paramName_setter(instance):
    original = instance.paramName
    instance.paramName = original
    assert instance.paramName == original

@given(instance=ale_Block_strategy)
@settings(max_examples=50)
def test_ale_block_instantiation(instance):
    assert isinstance(instance, ale_Block)

@given(instance=ale_Variable_strategy)
@settings(max_examples=50)
def test_ale_variable_instantiation(instance):
    assert isinstance(instance, ale_Variable)



@given(instance=ale_Variable_strategy)
def test_ale_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_rType_strategy)
@settings(max_examples=50)
def test_ale_rtype_instantiation(instance):
    assert isinstance(instance, ale_rType)



@given(instance=ale_rType_strategy)
def test_ale_rtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_Tag_strategy)
@settings(max_examples=50)
def test_ale_tag_instantiation(instance):
    assert isinstance(instance, ale_Tag)



@given(instance=ale_Tag_strategy)
def test_ale_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_Expression_strategy)
@settings(max_examples=50)
def test_ale_expression_instantiation(instance):
    assert isinstance(instance, ale_Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ale_If_strategy)
@settings(max_examples=50)
def test_ale_if_instantiation(instance):
    assert isinstance(instance, ale_If)

@given(instance=ale_ForEach_strategy)
@settings(max_examples=50)
def test_ale_foreach_instantiation(instance):
    assert isinstance(instance, ale_ForEach)



@given(instance=ale_ForEach_strategy)
def test_ale_foreach_iterator_setter(instance):
    original = instance.iterator
    instance.iterator = original
    assert instance.iterator == original

@given(instance=ale_Insert_strategy)
@settings(max_examples=50)
def test_ale_insert_instantiation(instance):
    assert isinstance(instance, ale_Insert)

@given(instance=ale_Assign_strategy)
@settings(max_examples=50)
def test_ale_assign_instantiation(instance):
    assert isinstance(instance, ale_Assign)

@given(instance=ale_While_strategy)
@settings(max_examples=50)
def test_ale_while_instantiation(instance):
    assert isinstance(instance, ale_While)

@given(instance=ale_Remove_strategy)
@settings(max_examples=50)
def test_ale_remove_instantiation(instance):
    assert isinstance(instance, ale_Remove)

@given(instance=ale_VarDecl_strategy)
@settings(max_examples=50)
def test_ale_vardecl_instantiation(instance):
    assert isinstance(instance, ale_VarDecl)



@given(instance=ale_VarDecl_strategy)
def test_ale_vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_Statement_strategy)
@settings(max_examples=50)
def test_ale_statement_instantiation(instance):
    assert isinstance(instance, ale_Statement)

@given(instance=ale_ExpressionStmt_strategy)
@settings(max_examples=50)
def test_ale_expressionstmt_instantiation(instance):
    assert isinstance(instance, ale_ExpressionStmt)

@given(instance=ale_rOpposite_strategy)
@settings(max_examples=50)
def test_ale_ropposite_instantiation(instance):
    assert isinstance(instance, ale_rOpposite)



@given(instance=ale_rOpposite_strategy)
def test_ale_ropposite_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_Unit_strategy)
@settings(max_examples=50)
def test_ale_unit_instantiation(instance):
    assert isinstance(instance, ale_Unit)



@given(instance=ale_Unit_strategy)
def test_ale_unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BehavioredClass_strategy)
@settings(max_examples=50)
def test_behavioredclass_instantiation(instance):
    assert isinstance(instance, BehavioredClass)

@given(instance=ale_RuntimeClass_strategy)
@settings(max_examples=50)
def test_ale_runtimeclass_instantiation(instance):
    assert isinstance(instance, ale_RuntimeClass)

@given(instance=ale_ExtendedClass_strategy)
@settings(max_examples=50)
def test_ale_extendedclass_instantiation(instance):
    assert isinstance(instance, ale_ExtendedClass)



@given(instance=ale_ExtendedClass_strategy)
def test_ale_extendedclass_extends_setter(instance):
    original = instance.extends
    instance.extends = original
    assert instance.extends == original

@given(instance=ale_Operation_strategy)
@settings(max_examples=50)
def test_ale_operation_instantiation(instance):
    assert isinstance(instance, ale_Operation)



@given(instance=ale_Operation_strategy)
def test_ale_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_Attribute_strategy)
@settings(max_examples=50)
def test_ale_attribute_instantiation(instance):
    assert isinstance(instance, ale_Attribute)



@given(instance=ale_Attribute_strategy)
def test_ale_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ale_Attribute_strategy)
def test_ale_attribute_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original



@given(instance=ale_Attribute_strategy)
def test_ale_attribute_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original

@given(instance=ale_BehavioredClass_strategy)
@settings(max_examples=50)
def test_ale_behavioredclass_instantiation(instance):
    assert isinstance(instance, ale_BehavioredClass)



@given(instance=ale_BehavioredClass_strategy)
def test_ale_behavioredclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_Service_strategy)
@settings(max_examples=50)
def test_ale_service_instantiation(instance):
    assert isinstance(instance, ale_Service)



@given(instance=ale_Service_strategy)
def test_ale_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ale_Import_strategy)
@settings(max_examples=50)
def test_ale_import_instantiation(instance):
    assert isinstance(instance, ale_Import)



@given(instance=ale_Import_strategy)
def test_ale_import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ale_Import_strategy)
def test_ale_import_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original
