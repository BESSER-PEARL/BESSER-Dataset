import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Else,
    limp_ElseIf,
    limp_NoElse,
    limp_ElseBlock,
    AttributeBlock,
    limp_NoAttributeBlock,
    limp_SomeAttributeBlock,
    Type,
    limp_BoolType,
    limp_RecordType,
    limp_IntegerType,
    limp_TupleType,
    limp_StringType,
    limp_ArrayType,
    limp_RealType,
    limp_EnumType,
    limp_VoidType,
    VarBlock,
    limp_NoVarBlock,
    limp_SomeVarBlock,
    limp_ExprList,
    limp_NamedType,
    limp_AbstractType,
    Expr,
    limp_ArrayUpdateExpr,
    limp_RecordUpdateExpr,
    limp_SecondInit,
    limp_IntegerLiteralExpr,
    limp_ChoiceExpr,
    limp_ArrayAccessExpr,
    limp_UnaryNegationExpr,
    limp_StringLiteralExpr,
    limp_RecordAccessExpr,
    limp_IfThenElseExpr,
    limp_BinaryExpr,
    limp_RealLiteralExpr,
    limp_UnaryMinusExpr,
    limp_IntegerWildCardExpr,
    limp_FreshVariable,
    limp_InitExpr,
    limp_FcnCallExpr,
    limp_BooleanLiteralExpr,
    limp_IdExpr,
    limp_ArrayExpr,
    limp_FunctionRef,
    limp_Equation,
    limp_RecordFieldExpr,
    limp_RecordExpr,
    limp_IdList,
    Equation,
    Statement,
    limp_LabelStatement,
    limp_ReturnStatement,
    limp_ContinueStatement,
    limp_IfThenElseStatement,
    limp_ForStatement,
    limp_BreakStatement,
    limp_AssignmentStatement,
    limp_GotoStatement,
    limp_VoidStatement,
    limp_Statement,
    limp_DefineUseRef,
    limp_WhileStatement,
    limp_Else,
    limp_VariableRef,
    limp_Expr,
    Attribute,
    limp_Uses,
    limp_Define,
    limp_Postcondition,
    limp_Precondition,
    limp_Attribute,
    limp_RecordFieldType,
    VariableRef,
    limp_LocalArg,
    limp_InputArg,
    limp_EnumValue,
    TypeDeclaration,
    limp_TypeAlias,
    limp_RecordTypeDef,
    limp_EnumTypeDef,
    limp_StatementBlock,
    limp_EquationBlock,
    limp_AbstractTypeDef,
    limp_Type,
    limp_ArrayTypeDef,
    limp_AttributeBlock,
    limp_OutputArgList,
    limp_OutputArg,
    limp_InputArgList,
    FunctionRef,
    Declaration,
    limp_LocalProcedure,
    limp_ConstantDeclaration,
    limp_ExternalFunction,
    limp_GlobalDeclaration,
    limp_ExternalProcedure,
    limp_TypeDeclaration,
    limp_Import,
    limp_Comment,
    limp_Declaration,
    limp_Specification,
    limp_VarBlock,
    limp_LocalFunction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_else_is_not_abstract():
    assert not inspect.isabstract(Else)


def test_else_constructor_exists():
    assert callable(Else.__init__)


def test_else_constructor_args():
    sig = inspect.signature(Else.__init__)
    params = list(sig.parameters.keys())



def test_limp_elseif_is_not_abstract():
    assert not inspect.isabstract(limp_ElseIf)


def test_limp_elseif_constructor_exists():
    assert callable(limp_ElseIf.__init__)


def test_limp_elseif_constructor_args():
    sig = inspect.signature(limp_ElseIf.__init__)
    params = list(sig.parameters.keys())



def test_limp_noelse_is_not_abstract():
    assert not inspect.isabstract(limp_NoElse)


def test_limp_noelse_constructor_exists():
    assert callable(limp_NoElse.__init__)


def test_limp_noelse_constructor_args():
    sig = inspect.signature(limp_NoElse.__init__)
    params = list(sig.parameters.keys())



def test_limp_elseblock_is_not_abstract():
    assert not inspect.isabstract(limp_ElseBlock)


def test_limp_elseblock_constructor_exists():
    assert callable(limp_ElseBlock.__init__)


def test_limp_elseblock_constructor_args():
    sig = inspect.signature(limp_ElseBlock.__init__)
    params = list(sig.parameters.keys())



def test_attributeblock_is_not_abstract():
    assert not inspect.isabstract(AttributeBlock)


def test_attributeblock_constructor_exists():
    assert callable(AttributeBlock.__init__)


def test_attributeblock_constructor_args():
    sig = inspect.signature(AttributeBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_noattributeblock_is_not_abstract():
    assert not inspect.isabstract(limp_NoAttributeBlock)


def test_limp_noattributeblock_constructor_exists():
    assert callable(limp_NoAttributeBlock.__init__)


def test_limp_noattributeblock_constructor_args():
    sig = inspect.signature(limp_NoAttributeBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_someattributeblock_is_not_abstract():
    assert not inspect.isabstract(limp_SomeAttributeBlock)


def test_limp_someattributeblock_constructor_exists():
    assert callable(limp_SomeAttributeBlock.__init__)


def test_limp_someattributeblock_constructor_args():
    sig = inspect.signature(limp_SomeAttributeBlock.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_limp_booltype_is_not_abstract():
    assert not inspect.isabstract(limp_BoolType)


def test_limp_booltype_constructor_exists():
    assert callable(limp_BoolType.__init__)


def test_limp_booltype_constructor_args():
    sig = inspect.signature(limp_BoolType.__init__)
    params = list(sig.parameters.keys())



def test_limp_recordtype_is_not_abstract():
    assert not inspect.isabstract(limp_RecordType)


def test_limp_recordtype_constructor_exists():
    assert callable(limp_RecordType.__init__)


def test_limp_recordtype_constructor_args():
    sig = inspect.signature(limp_RecordType.__init__)
    params = list(sig.parameters.keys())



def test_limp_integertype_is_not_abstract():
    assert not inspect.isabstract(limp_IntegerType)


def test_limp_integertype_constructor_exists():
    assert callable(limp_IntegerType.__init__)


def test_limp_integertype_constructor_args():
    sig = inspect.signature(limp_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_limp_tupletype_is_not_abstract():
    assert not inspect.isabstract(limp_TupleType)


def test_limp_tupletype_constructor_exists():
    assert callable(limp_TupleType.__init__)


def test_limp_tupletype_constructor_args():
    sig = inspect.signature(limp_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_limp_stringtype_is_not_abstract():
    assert not inspect.isabstract(limp_StringType)


def test_limp_stringtype_constructor_exists():
    assert callable(limp_StringType.__init__)


def test_limp_stringtype_constructor_args():
    sig = inspect.signature(limp_StringType.__init__)
    params = list(sig.parameters.keys())



def test_limp_arraytype_is_not_abstract():
    assert not inspect.isabstract(limp_ArrayType)


def test_limp_arraytype_constructor_exists():
    assert callable(limp_ArrayType.__init__)


def test_limp_arraytype_constructor_args():
    sig = inspect.signature(limp_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_limp_realtype_is_not_abstract():
    assert not inspect.isabstract(limp_RealType)


def test_limp_realtype_constructor_exists():
    assert callable(limp_RealType.__init__)


def test_limp_realtype_constructor_args():
    sig = inspect.signature(limp_RealType.__init__)
    params = list(sig.parameters.keys())



def test_limp_enumtype_is_not_abstract():
    assert not inspect.isabstract(limp_EnumType)


def test_limp_enumtype_constructor_exists():
    assert callable(limp_EnumType.__init__)


def test_limp_enumtype_constructor_args():
    sig = inspect.signature(limp_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_limp_voidtype_is_not_abstract():
    assert not inspect.isabstract(limp_VoidType)


def test_limp_voidtype_constructor_exists():
    assert callable(limp_VoidType.__init__)


def test_limp_voidtype_constructor_args():
    sig = inspect.signature(limp_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_varblock_is_not_abstract():
    assert not inspect.isabstract(VarBlock)


def test_varblock_constructor_exists():
    assert callable(VarBlock.__init__)


def test_varblock_constructor_args():
    sig = inspect.signature(VarBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_novarblock_is_not_abstract():
    assert not inspect.isabstract(limp_NoVarBlock)


def test_limp_novarblock_constructor_exists():
    assert callable(limp_NoVarBlock.__init__)


def test_limp_novarblock_constructor_args():
    sig = inspect.signature(limp_NoVarBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_somevarblock_is_not_abstract():
    assert not inspect.isabstract(limp_SomeVarBlock)


def test_limp_somevarblock_constructor_exists():
    assert callable(limp_SomeVarBlock.__init__)


def test_limp_somevarblock_constructor_args():
    sig = inspect.signature(limp_SomeVarBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_exprlist_is_not_abstract():
    assert not inspect.isabstract(limp_ExprList)


def test_limp_exprlist_constructor_exists():
    assert callable(limp_ExprList.__init__)


def test_limp_exprlist_constructor_args():
    sig = inspect.signature(limp_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_limp_namedtype_is_not_abstract():
    assert not inspect.isabstract(limp_NamedType)


def test_limp_namedtype_constructor_exists():
    assert callable(limp_NamedType.__init__)


def test_limp_namedtype_constructor_args():
    sig = inspect.signature(limp_NamedType.__init__)
    params = list(sig.parameters.keys())



def test_limp_abstracttype_is_not_abstract():
    assert not inspect.isabstract(limp_AbstractType)


def test_limp_abstracttype_constructor_exists():
    assert callable(limp_AbstractType.__init__)


def test_limp_abstracttype_constructor_args():
    sig = inspect.signature(limp_AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_limp_arrayupdateexpr_is_not_abstract():
    assert not inspect.isabstract(limp_ArrayUpdateExpr)


def test_limp_arrayupdateexpr_constructor_exists():
    assert callable(limp_ArrayUpdateExpr.__init__)


def test_limp_arrayupdateexpr_constructor_args():
    sig = inspect.signature(limp_ArrayUpdateExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_recordupdateexpr_is_not_abstract():
    assert not inspect.isabstract(limp_RecordUpdateExpr)


def test_limp_recordupdateexpr_constructor_exists():
    assert callable(limp_RecordUpdateExpr.__init__)


def test_limp_recordupdateexpr_constructor_args():
    sig = inspect.signature(limp_RecordUpdateExpr.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_limp_recordupdateexpr_has_field():
    assert hasattr(limp_RecordUpdateExpr, "field")
    descriptor = None
    for klass in limp_RecordUpdateExpr.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_limp_secondinit_is_not_abstract():
    assert not inspect.isabstract(limp_SecondInit)


def test_limp_secondinit_constructor_exists():
    assert callable(limp_SecondInit.__init__)


def test_limp_secondinit_constructor_args():
    sig = inspect.signature(limp_SecondInit.__init__)
    params = list(sig.parameters.keys())



def test_limp_integerliteralexpr_is_not_abstract():
    assert not inspect.isabstract(limp_IntegerLiteralExpr)


def test_limp_integerliteralexpr_constructor_exists():
    assert callable(limp_IntegerLiteralExpr.__init__)


def test_limp_integerliteralexpr_constructor_args():
    sig = inspect.signature(limp_IntegerLiteralExpr.__init__)
    params = list(sig.parameters.keys())
    assert "intVal" in params, "Missing parameter 'intVal'"

def test_limp_integerliteralexpr_has_intVal():
    assert hasattr(limp_IntegerLiteralExpr, "intVal")
    descriptor = None
    for klass in limp_IntegerLiteralExpr.__mro__:
        if "intVal" in klass.__dict__:
            descriptor = klass.__dict__["intVal"]
            break
    assert isinstance(descriptor, property)



def test_limp_choiceexpr_is_not_abstract():
    assert not inspect.isabstract(limp_ChoiceExpr)


def test_limp_choiceexpr_constructor_exists():
    assert callable(limp_ChoiceExpr.__init__)


def test_limp_choiceexpr_constructor_args():
    sig = inspect.signature(limp_ChoiceExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_arrayaccessexpr_is_not_abstract():
    assert not inspect.isabstract(limp_ArrayAccessExpr)


def test_limp_arrayaccessexpr_constructor_exists():
    assert callable(limp_ArrayAccessExpr.__init__)


def test_limp_arrayaccessexpr_constructor_args():
    sig = inspect.signature(limp_ArrayAccessExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_unarynegationexpr_is_not_abstract():
    assert not inspect.isabstract(limp_UnaryNegationExpr)


def test_limp_unarynegationexpr_constructor_exists():
    assert callable(limp_UnaryNegationExpr.__init__)


def test_limp_unarynegationexpr_constructor_args():
    sig = inspect.signature(limp_UnaryNegationExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_stringliteralexpr_is_not_abstract():
    assert not inspect.isabstract(limp_StringLiteralExpr)


def test_limp_stringliteralexpr_constructor_exists():
    assert callable(limp_StringLiteralExpr.__init__)


def test_limp_stringliteralexpr_constructor_args():
    sig = inspect.signature(limp_StringLiteralExpr.__init__)
    params = list(sig.parameters.keys())
    assert "stringVal" in params, "Missing parameter 'stringVal'"

def test_limp_stringliteralexpr_has_stringVal():
    assert hasattr(limp_StringLiteralExpr, "stringVal")
    descriptor = None
    for klass in limp_StringLiteralExpr.__mro__:
        if "stringVal" in klass.__dict__:
            descriptor = klass.__dict__["stringVal"]
            break
    assert isinstance(descriptor, property)



def test_limp_recordaccessexpr_is_not_abstract():
    assert not inspect.isabstract(limp_RecordAccessExpr)


def test_limp_recordaccessexpr_constructor_exists():
    assert callable(limp_RecordAccessExpr.__init__)


def test_limp_recordaccessexpr_constructor_args():
    sig = inspect.signature(limp_RecordAccessExpr.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_limp_recordaccessexpr_has_field():
    assert hasattr(limp_RecordAccessExpr, "field")
    descriptor = None
    for klass in limp_RecordAccessExpr.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_limp_ifthenelseexpr_is_not_abstract():
    assert not inspect.isabstract(limp_IfThenElseExpr)


def test_limp_ifthenelseexpr_constructor_exists():
    assert callable(limp_IfThenElseExpr.__init__)


def test_limp_ifthenelseexpr_constructor_args():
    sig = inspect.signature(limp_IfThenElseExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_binaryexpr_is_not_abstract():
    assert not inspect.isabstract(limp_BinaryExpr)


def test_limp_binaryexpr_constructor_exists():
    assert callable(limp_BinaryExpr.__init__)


def test_limp_binaryexpr_constructor_args():
    sig = inspect.signature(limp_BinaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_limp_binaryexpr_has_op():
    assert hasattr(limp_BinaryExpr, "op")
    descriptor = None
    for klass in limp_BinaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_limp_realliteralexpr_is_not_abstract():
    assert not inspect.isabstract(limp_RealLiteralExpr)


def test_limp_realliteralexpr_constructor_exists():
    assert callable(limp_RealLiteralExpr.__init__)


def test_limp_realliteralexpr_constructor_args():
    sig = inspect.signature(limp_RealLiteralExpr.__init__)
    params = list(sig.parameters.keys())
    assert "realVal" in params, "Missing parameter 'realVal'"

def test_limp_realliteralexpr_has_realVal():
    assert hasattr(limp_RealLiteralExpr, "realVal")
    descriptor = None
    for klass in limp_RealLiteralExpr.__mro__:
        if "realVal" in klass.__dict__:
            descriptor = klass.__dict__["realVal"]
            break
    assert isinstance(descriptor, property)



def test_limp_unaryminusexpr_is_not_abstract():
    assert not inspect.isabstract(limp_UnaryMinusExpr)


def test_limp_unaryminusexpr_constructor_exists():
    assert callable(limp_UnaryMinusExpr.__init__)


def test_limp_unaryminusexpr_constructor_args():
    sig = inspect.signature(limp_UnaryMinusExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_integerwildcardexpr_is_not_abstract():
    assert not inspect.isabstract(limp_IntegerWildCardExpr)


def test_limp_integerwildcardexpr_constructor_exists():
    assert callable(limp_IntegerWildCardExpr.__init__)


def test_limp_integerwildcardexpr_constructor_args():
    sig = inspect.signature(limp_IntegerWildCardExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_freshvariable_is_not_abstract():
    assert not inspect.isabstract(limp_FreshVariable)


def test_limp_freshvariable_constructor_exists():
    assert callable(limp_FreshVariable.__init__)


def test_limp_freshvariable_constructor_args():
    sig = inspect.signature(limp_FreshVariable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_limp_freshvariable_has_value():
    assert hasattr(limp_FreshVariable, "value")
    descriptor = None
    for klass in limp_FreshVariable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_limp_initexpr_is_not_abstract():
    assert not inspect.isabstract(limp_InitExpr)


def test_limp_initexpr_constructor_exists():
    assert callable(limp_InitExpr.__init__)


def test_limp_initexpr_constructor_args():
    sig = inspect.signature(limp_InitExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_fcncallexpr_is_not_abstract():
    assert not inspect.isabstract(limp_FcnCallExpr)


def test_limp_fcncallexpr_constructor_exists():
    assert callable(limp_FcnCallExpr.__init__)


def test_limp_fcncallexpr_constructor_args():
    sig = inspect.signature(limp_FcnCallExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_booleanliteralexpr_is_not_abstract():
    assert not inspect.isabstract(limp_BooleanLiteralExpr)


def test_limp_booleanliteralexpr_constructor_exists():
    assert callable(limp_BooleanLiteralExpr.__init__)


def test_limp_booleanliteralexpr_constructor_args():
    sig = inspect.signature(limp_BooleanLiteralExpr.__init__)
    params = list(sig.parameters.keys())
    assert "boolVal" in params, "Missing parameter 'boolVal'"

def test_limp_booleanliteralexpr_has_boolVal():
    assert hasattr(limp_BooleanLiteralExpr, "boolVal")
    descriptor = None
    for klass in limp_BooleanLiteralExpr.__mro__:
        if "boolVal" in klass.__dict__:
            descriptor = klass.__dict__["boolVal"]
            break
    assert isinstance(descriptor, property)



def test_limp_idexpr_is_not_abstract():
    assert not inspect.isabstract(limp_IdExpr)


def test_limp_idexpr_constructor_exists():
    assert callable(limp_IdExpr.__init__)


def test_limp_idexpr_constructor_args():
    sig = inspect.signature(limp_IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_arrayexpr_is_not_abstract():
    assert not inspect.isabstract(limp_ArrayExpr)


def test_limp_arrayexpr_constructor_exists():
    assert callable(limp_ArrayExpr.__init__)


def test_limp_arrayexpr_constructor_args():
    sig = inspect.signature(limp_ArrayExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_functionref_is_not_abstract():
    assert not inspect.isabstract(limp_FunctionRef)


def test_limp_functionref_constructor_exists():
    assert callable(limp_FunctionRef.__init__)


def test_limp_functionref_constructor_args():
    sig = inspect.signature(limp_FunctionRef.__init__)
    params = list(sig.parameters.keys())



def test_limp_equation_is_not_abstract():
    assert not inspect.isabstract(limp_Equation)


def test_limp_equation_constructor_exists():
    assert callable(limp_Equation.__init__)


def test_limp_equation_constructor_args():
    sig = inspect.signature(limp_Equation.__init__)
    params = list(sig.parameters.keys())



def test_limp_recordfieldexpr_is_not_abstract():
    assert not inspect.isabstract(limp_RecordFieldExpr)


def test_limp_recordfieldexpr_constructor_exists():
    assert callable(limp_RecordFieldExpr.__init__)


def test_limp_recordfieldexpr_constructor_args():
    sig = inspect.signature(limp_RecordFieldExpr.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_limp_recordfieldexpr_has_fieldName():
    assert hasattr(limp_RecordFieldExpr, "fieldName")
    descriptor = None
    for klass in limp_RecordFieldExpr.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_limp_recordexpr_is_not_abstract():
    assert not inspect.isabstract(limp_RecordExpr)


def test_limp_recordexpr_constructor_exists():
    assert callable(limp_RecordExpr.__init__)


def test_limp_recordexpr_constructor_args():
    sig = inspect.signature(limp_RecordExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp_idlist_is_not_abstract():
    assert not inspect.isabstract(limp_IdList)


def test_limp_idlist_constructor_exists():
    assert callable(limp_IdList.__init__)


def test_limp_idlist_constructor_args():
    sig = inspect.signature(limp_IdList.__init__)
    params = list(sig.parameters.keys())



def test_equation_is_not_abstract():
    assert not inspect.isabstract(Equation)


def test_equation_constructor_exists():
    assert callable(Equation.__init__)


def test_equation_constructor_args():
    sig = inspect.signature(Equation.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_limp_labelstatement_is_not_abstract():
    assert not inspect.isabstract(limp_LabelStatement)


def test_limp_labelstatement_constructor_exists():
    assert callable(limp_LabelStatement.__init__)


def test_limp_labelstatement_constructor_args():
    sig = inspect.signature(limp_LabelStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_labelstatement_has_name():
    assert hasattr(limp_LabelStatement, "name")
    descriptor = None
    for klass in limp_LabelStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp_returnstatement_is_not_abstract():
    assert not inspect.isabstract(limp_ReturnStatement)


def test_limp_returnstatement_constructor_exists():
    assert callable(limp_ReturnStatement.__init__)


def test_limp_returnstatement_constructor_args():
    sig = inspect.signature(limp_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_continuestatement_is_not_abstract():
    assert not inspect.isabstract(limp_ContinueStatement)


def test_limp_continuestatement_constructor_exists():
    assert callable(limp_ContinueStatement.__init__)


def test_limp_continuestatement_constructor_args():
    sig = inspect.signature(limp_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_ifthenelsestatement_is_not_abstract():
    assert not inspect.isabstract(limp_IfThenElseStatement)


def test_limp_ifthenelsestatement_constructor_exists():
    assert callable(limp_IfThenElseStatement.__init__)


def test_limp_ifthenelsestatement_constructor_args():
    sig = inspect.signature(limp_IfThenElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_forstatement_is_not_abstract():
    assert not inspect.isabstract(limp_ForStatement)


def test_limp_forstatement_constructor_exists():
    assert callable(limp_ForStatement.__init__)


def test_limp_forstatement_constructor_args():
    sig = inspect.signature(limp_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_breakstatement_is_not_abstract():
    assert not inspect.isabstract(limp_BreakStatement)


def test_limp_breakstatement_constructor_exists():
    assert callable(limp_BreakStatement.__init__)


def test_limp_breakstatement_constructor_args():
    sig = inspect.signature(limp_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(limp_AssignmentStatement)


def test_limp_assignmentstatement_constructor_exists():
    assert callable(limp_AssignmentStatement.__init__)


def test_limp_assignmentstatement_constructor_args():
    sig = inspect.signature(limp_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_gotostatement_is_not_abstract():
    assert not inspect.isabstract(limp_GotoStatement)


def test_limp_gotostatement_constructor_exists():
    assert callable(limp_GotoStatement.__init__)


def test_limp_gotostatement_constructor_args():
    sig = inspect.signature(limp_GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_voidstatement_is_not_abstract():
    assert not inspect.isabstract(limp_VoidStatement)


def test_limp_voidstatement_constructor_exists():
    assert callable(limp_VoidStatement.__init__)


def test_limp_voidstatement_constructor_args():
    sig = inspect.signature(limp_VoidStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_statement_is_not_abstract():
    assert not inspect.isabstract(limp_Statement)


def test_limp_statement_constructor_exists():
    assert callable(limp_Statement.__init__)


def test_limp_statement_constructor_args():
    sig = inspect.signature(limp_Statement.__init__)
    params = list(sig.parameters.keys())



def test_limp_defineuseref_is_not_abstract():
    assert not inspect.isabstract(limp_DefineUseRef)


def test_limp_defineuseref_constructor_exists():
    assert callable(limp_DefineUseRef.__init__)


def test_limp_defineuseref_constructor_args():
    sig = inspect.signature(limp_DefineUseRef.__init__)
    params = list(sig.parameters.keys())



def test_limp_whilestatement_is_not_abstract():
    assert not inspect.isabstract(limp_WhileStatement)


def test_limp_whilestatement_constructor_exists():
    assert callable(limp_WhileStatement.__init__)


def test_limp_whilestatement_constructor_args():
    sig = inspect.signature(limp_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp_else_is_not_abstract():
    assert not inspect.isabstract(limp_Else)


def test_limp_else_constructor_exists():
    assert callable(limp_Else.__init__)


def test_limp_else_constructor_args():
    sig = inspect.signature(limp_Else.__init__)
    params = list(sig.parameters.keys())



def test_limp_variableref_is_not_abstract():
    assert not inspect.isabstract(limp_VariableRef)


def test_limp_variableref_constructor_exists():
    assert callable(limp_VariableRef.__init__)


def test_limp_variableref_constructor_args():
    sig = inspect.signature(limp_VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_variableref_has_name():
    assert hasattr(limp_VariableRef, "name")
    descriptor = None
    for klass in limp_VariableRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp_expr_is_not_abstract():
    assert not inspect.isabstract(limp_Expr)


def test_limp_expr_constructor_exists():
    assert callable(limp_Expr.__init__)


def test_limp_expr_constructor_args():
    sig = inspect.signature(limp_Expr.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_limp_uses_is_not_abstract():
    assert not inspect.isabstract(limp_Uses)


def test_limp_uses_constructor_exists():
    assert callable(limp_Uses.__init__)


def test_limp_uses_constructor_args():
    sig = inspect.signature(limp_Uses.__init__)
    params = list(sig.parameters.keys())



def test_limp_define_is_not_abstract():
    assert not inspect.isabstract(limp_Define)


def test_limp_define_constructor_exists():
    assert callable(limp_Define.__init__)


def test_limp_define_constructor_args():
    sig = inspect.signature(limp_Define.__init__)
    params = list(sig.parameters.keys())



def test_limp_postcondition_is_not_abstract():
    assert not inspect.isabstract(limp_Postcondition)


def test_limp_postcondition_constructor_exists():
    assert callable(limp_Postcondition.__init__)


def test_limp_postcondition_constructor_args():
    sig = inspect.signature(limp_Postcondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_postcondition_has_name():
    assert hasattr(limp_Postcondition, "name")
    descriptor = None
    for klass in limp_Postcondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp_precondition_is_not_abstract():
    assert not inspect.isabstract(limp_Precondition)


def test_limp_precondition_constructor_exists():
    assert callable(limp_Precondition.__init__)


def test_limp_precondition_constructor_args():
    sig = inspect.signature(limp_Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_precondition_has_name():
    assert hasattr(limp_Precondition, "name")
    descriptor = None
    for klass in limp_Precondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp_attribute_is_not_abstract():
    assert not inspect.isabstract(limp_Attribute)


def test_limp_attribute_constructor_exists():
    assert callable(limp_Attribute.__init__)


def test_limp_attribute_constructor_args():
    sig = inspect.signature(limp_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_limp_recordfieldtype_is_not_abstract():
    assert not inspect.isabstract(limp_RecordFieldType)


def test_limp_recordfieldtype_constructor_exists():
    assert callable(limp_RecordFieldType.__init__)


def test_limp_recordfieldtype_constructor_args():
    sig = inspect.signature(limp_RecordFieldType.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_limp_recordfieldtype_has_fieldName():
    assert hasattr(limp_RecordFieldType, "fieldName")
    descriptor = None
    for klass in limp_RecordFieldType.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_variableref_is_not_abstract():
    assert not inspect.isabstract(VariableRef)


def test_variableref_constructor_exists():
    assert callable(VariableRef.__init__)


def test_variableref_constructor_args():
    sig = inspect.signature(VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_limp_localarg_is_not_abstract():
    assert not inspect.isabstract(limp_LocalArg)


def test_limp_localarg_constructor_exists():
    assert callable(limp_LocalArg.__init__)


def test_limp_localarg_constructor_args():
    sig = inspect.signature(limp_LocalArg.__init__)
    params = list(sig.parameters.keys())



def test_limp_inputarg_is_not_abstract():
    assert not inspect.isabstract(limp_InputArg)


def test_limp_inputarg_constructor_exists():
    assert callable(limp_InputArg.__init__)


def test_limp_inputarg_constructor_args():
    sig = inspect.signature(limp_InputArg.__init__)
    params = list(sig.parameters.keys())



def test_limp_enumvalue_is_not_abstract():
    assert not inspect.isabstract(limp_EnumValue)


def test_limp_enumvalue_constructor_exists():
    assert callable(limp_EnumValue.__init__)


def test_limp_enumvalue_constructor_args():
    sig = inspect.signature(limp_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_limp_typealias_is_not_abstract():
    assert not inspect.isabstract(limp_TypeAlias)


def test_limp_typealias_constructor_exists():
    assert callable(limp_TypeAlias.__init__)


def test_limp_typealias_constructor_args():
    sig = inspect.signature(limp_TypeAlias.__init__)
    params = list(sig.parameters.keys())



def test_limp_recordtypedef_is_not_abstract():
    assert not inspect.isabstract(limp_RecordTypeDef)


def test_limp_recordtypedef_constructor_exists():
    assert callable(limp_RecordTypeDef.__init__)


def test_limp_recordtypedef_constructor_args():
    sig = inspect.signature(limp_RecordTypeDef.__init__)
    params = list(sig.parameters.keys())



def test_limp_enumtypedef_is_not_abstract():
    assert not inspect.isabstract(limp_EnumTypeDef)


def test_limp_enumtypedef_constructor_exists():
    assert callable(limp_EnumTypeDef.__init__)


def test_limp_enumtypedef_constructor_args():
    sig = inspect.signature(limp_EnumTypeDef.__init__)
    params = list(sig.parameters.keys())



def test_limp_statementblock_is_not_abstract():
    assert not inspect.isabstract(limp_StatementBlock)


def test_limp_statementblock_constructor_exists():
    assert callable(limp_StatementBlock.__init__)


def test_limp_statementblock_constructor_args():
    sig = inspect.signature(limp_StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_equationblock_is_not_abstract():
    assert not inspect.isabstract(limp_EquationBlock)


def test_limp_equationblock_constructor_exists():
    assert callable(limp_EquationBlock.__init__)


def test_limp_equationblock_constructor_args():
    sig = inspect.signature(limp_EquationBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_abstracttypedef_is_not_abstract():
    assert not inspect.isabstract(limp_AbstractTypeDef)


def test_limp_abstracttypedef_constructor_exists():
    assert callable(limp_AbstractTypeDef.__init__)


def test_limp_abstracttypedef_constructor_args():
    sig = inspect.signature(limp_AbstractTypeDef.__init__)
    params = list(sig.parameters.keys())



def test_limp_type_is_not_abstract():
    assert not inspect.isabstract(limp_Type)


def test_limp_type_constructor_exists():
    assert callable(limp_Type.__init__)


def test_limp_type_constructor_args():
    sig = inspect.signature(limp_Type.__init__)
    params = list(sig.parameters.keys())



def test_limp_arraytypedef_is_not_abstract():
    assert not inspect.isabstract(limp_ArrayTypeDef)


def test_limp_arraytypedef_constructor_exists():
    assert callable(limp_ArrayTypeDef.__init__)


def test_limp_arraytypedef_constructor_args():
    sig = inspect.signature(limp_ArrayTypeDef.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_limp_arraytypedef_has_size():
    assert hasattr(limp_ArrayTypeDef, "size")
    descriptor = None
    for klass in limp_ArrayTypeDef.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_limp_attributeblock_is_not_abstract():
    assert not inspect.isabstract(limp_AttributeBlock)


def test_limp_attributeblock_constructor_exists():
    assert callable(limp_AttributeBlock.__init__)


def test_limp_attributeblock_constructor_args():
    sig = inspect.signature(limp_AttributeBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_outputarglist_is_not_abstract():
    assert not inspect.isabstract(limp_OutputArgList)


def test_limp_outputarglist_constructor_exists():
    assert callable(limp_OutputArgList.__init__)


def test_limp_outputarglist_constructor_args():
    sig = inspect.signature(limp_OutputArgList.__init__)
    params = list(sig.parameters.keys())



def test_limp_outputarg_is_not_abstract():
    assert not inspect.isabstract(limp_OutputArg)


def test_limp_outputarg_constructor_exists():
    assert callable(limp_OutputArg.__init__)


def test_limp_outputarg_constructor_args():
    sig = inspect.signature(limp_OutputArg.__init__)
    params = list(sig.parameters.keys())



def test_limp_inputarglist_is_not_abstract():
    assert not inspect.isabstract(limp_InputArgList)


def test_limp_inputarglist_constructor_exists():
    assert callable(limp_InputArgList.__init__)


def test_limp_inputarglist_constructor_args():
    sig = inspect.signature(limp_InputArgList.__init__)
    params = list(sig.parameters.keys())



def test_functionref_is_not_abstract():
    assert not inspect.isabstract(FunctionRef)


def test_functionref_constructor_exists():
    assert callable(FunctionRef.__init__)


def test_functionref_constructor_args():
    sig = inspect.signature(FunctionRef.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_limp_localprocedure_is_not_abstract():
    assert not inspect.isabstract(limp_LocalProcedure)


def test_limp_localprocedure_constructor_exists():
    assert callable(limp_LocalProcedure.__init__)


def test_limp_localprocedure_constructor_args():
    sig = inspect.signature(limp_LocalProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_localprocedure_has_name():
    assert hasattr(limp_LocalProcedure, "name")
    descriptor = None
    for klass in limp_LocalProcedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(limp_ConstantDeclaration)


def test_limp_constantdeclaration_constructor_exists():
    assert callable(limp_ConstantDeclaration.__init__)


def test_limp_constantdeclaration_constructor_args():
    sig = inspect.signature(limp_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_limp_externalfunction_is_not_abstract():
    assert not inspect.isabstract(limp_ExternalFunction)


def test_limp_externalfunction_constructor_exists():
    assert callable(limp_ExternalFunction.__init__)


def test_limp_externalfunction_constructor_args():
    sig = inspect.signature(limp_ExternalFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_externalfunction_has_name():
    assert hasattr(limp_ExternalFunction, "name")
    descriptor = None
    for klass in limp_ExternalFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp_globaldeclaration_is_not_abstract():
    assert not inspect.isabstract(limp_GlobalDeclaration)


def test_limp_globaldeclaration_constructor_exists():
    assert callable(limp_GlobalDeclaration.__init__)


def test_limp_globaldeclaration_constructor_args():
    sig = inspect.signature(limp_GlobalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_limp_externalprocedure_is_not_abstract():
    assert not inspect.isabstract(limp_ExternalProcedure)


def test_limp_externalprocedure_constructor_exists():
    assert callable(limp_ExternalProcedure.__init__)


def test_limp_externalprocedure_constructor_args():
    sig = inspect.signature(limp_ExternalProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_externalprocedure_has_name():
    assert hasattr(limp_ExternalProcedure, "name")
    descriptor = None
    for klass in limp_ExternalProcedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(limp_TypeDeclaration)


def test_limp_typedeclaration_constructor_exists():
    assert callable(limp_TypeDeclaration.__init__)


def test_limp_typedeclaration_constructor_args():
    sig = inspect.signature(limp_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_typedeclaration_has_name():
    assert hasattr(limp_TypeDeclaration, "name")
    descriptor = None
    for klass in limp_TypeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp_import_is_not_abstract():
    assert not inspect.isabstract(limp_Import)


def test_limp_import_constructor_exists():
    assert callable(limp_Import.__init__)


def test_limp_import_constructor_args():
    sig = inspect.signature(limp_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_limp_import_has_importURI():
    assert hasattr(limp_Import, "importURI")
    descriptor = None
    for klass in limp_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_limp_comment_is_not_abstract():
    assert not inspect.isabstract(limp_Comment)


def test_limp_comment_constructor_exists():
    assert callable(limp_Comment.__init__)


def test_limp_comment_constructor_args():
    sig = inspect.signature(limp_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_limp_comment_has_comment():
    assert hasattr(limp_Comment, "comment")
    descriptor = None
    for klass in limp_Comment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_limp_declaration_is_not_abstract():
    assert not inspect.isabstract(limp_Declaration)


def test_limp_declaration_constructor_exists():
    assert callable(limp_Declaration.__init__)


def test_limp_declaration_constructor_args():
    sig = inspect.signature(limp_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_limp_specification_is_not_abstract():
    assert not inspect.isabstract(limp_Specification)


def test_limp_specification_constructor_exists():
    assert callable(limp_Specification.__init__)


def test_limp_specification_constructor_args():
    sig = inspect.signature(limp_Specification.__init__)
    params = list(sig.parameters.keys())



def test_limp_varblock_is_not_abstract():
    assert not inspect.isabstract(limp_VarBlock)


def test_limp_varblock_constructor_exists():
    assert callable(limp_VarBlock.__init__)


def test_limp_varblock_constructor_args():
    sig = inspect.signature(limp_VarBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp_localfunction_is_not_abstract():
    assert not inspect.isabstract(limp_LocalFunction)


def test_limp_localfunction_constructor_exists():
    assert callable(limp_LocalFunction.__init__)


def test_limp_localfunction_constructor_args():
    sig = inspect.signature(limp_LocalFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp_localfunction_has_name():
    assert hasattr(limp_LocalFunction, "name")
    descriptor = None
    for klass in limp_LocalFunction.__mro__:
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
Else_strategy = st.builds(
    Else,
)
limp_ElseIf_strategy = st.builds(
    limp_ElseIf,
)
limp_NoElse_strategy = st.builds(
    limp_NoElse,
)
limp_ElseBlock_strategy = st.builds(
    limp_ElseBlock,
)
AttributeBlock_strategy = st.builds(
    AttributeBlock,
)
limp_NoAttributeBlock_strategy = st.builds(
    limp_NoAttributeBlock,
)
limp_SomeAttributeBlock_strategy = st.builds(
    limp_SomeAttributeBlock,
)
Type_strategy = st.builds(
    Type,
)
limp_BoolType_strategy = st.builds(
    limp_BoolType,
)
limp_RecordType_strategy = st.builds(
    limp_RecordType,
)
limp_IntegerType_strategy = st.builds(
    limp_IntegerType,
)
limp_TupleType_strategy = st.builds(
    limp_TupleType,
)
limp_StringType_strategy = st.builds(
    limp_StringType,
)
limp_ArrayType_strategy = st.builds(
    limp_ArrayType,
)
limp_RealType_strategy = st.builds(
    limp_RealType,
)
limp_EnumType_strategy = st.builds(
    limp_EnumType,
)
limp_VoidType_strategy = st.builds(
    limp_VoidType,
)
VarBlock_strategy = st.builds(
    VarBlock,
)
limp_NoVarBlock_strategy = st.builds(
    limp_NoVarBlock,
)
limp_SomeVarBlock_strategy = st.builds(
    limp_SomeVarBlock,
)
limp_ExprList_strategy = st.builds(
    limp_ExprList,
)
limp_NamedType_strategy = st.builds(
    limp_NamedType,
)
limp_AbstractType_strategy = st.builds(
    limp_AbstractType,
)
Expr_strategy = st.builds(
    Expr,
)
limp_ArrayUpdateExpr_strategy = st.builds(
    limp_ArrayUpdateExpr,
)
limp_RecordUpdateExpr_strategy = st.builds(
    limp_RecordUpdateExpr,
    field=
        safe_text
)
limp_SecondInit_strategy = st.builds(
    limp_SecondInit,
)
limp_IntegerLiteralExpr_strategy = st.builds(
    limp_IntegerLiteralExpr,
    intVal=
        safe_text
)
limp_ChoiceExpr_strategy = st.builds(
    limp_ChoiceExpr,
)
limp_ArrayAccessExpr_strategy = st.builds(
    limp_ArrayAccessExpr,
)
limp_UnaryNegationExpr_strategy = st.builds(
    limp_UnaryNegationExpr,
)
limp_StringLiteralExpr_strategy = st.builds(
    limp_StringLiteralExpr,
    stringVal=
        safe_text
)
limp_RecordAccessExpr_strategy = st.builds(
    limp_RecordAccessExpr,
    field=
        safe_text
)
limp_IfThenElseExpr_strategy = st.builds(
    limp_IfThenElseExpr,
)
limp_BinaryExpr_strategy = st.builds(
    limp_BinaryExpr,
    op=
        safe_text
)
limp_RealLiteralExpr_strategy = st.builds(
    limp_RealLiteralExpr,
    realVal=
        safe_text
)
limp_UnaryMinusExpr_strategy = st.builds(
    limp_UnaryMinusExpr,
)
limp_IntegerWildCardExpr_strategy = st.builds(
    limp_IntegerWildCardExpr,
)
limp_FreshVariable_strategy = st.builds(
    limp_FreshVariable,
    value=
        safe_text
)
limp_InitExpr_strategy = st.builds(
    limp_InitExpr,
)
limp_FcnCallExpr_strategy = st.builds(
    limp_FcnCallExpr,
)
limp_BooleanLiteralExpr_strategy = st.builds(
    limp_BooleanLiteralExpr,
    boolVal=
        safe_text
)
limp_IdExpr_strategy = st.builds(
    limp_IdExpr,
)
limp_ArrayExpr_strategy = st.builds(
    limp_ArrayExpr,
)
limp_FunctionRef_strategy = st.builds(
    limp_FunctionRef,
)
limp_Equation_strategy = st.builds(
    limp_Equation,
)
limp_RecordFieldExpr_strategy = st.builds(
    limp_RecordFieldExpr,
    fieldName=
        safe_text
)
limp_RecordExpr_strategy = st.builds(
    limp_RecordExpr,
)
limp_IdList_strategy = st.builds(
    limp_IdList,
)
Equation_strategy = st.builds(
    Equation,
)
Statement_strategy = st.builds(
    Statement,
)
limp_LabelStatement_strategy = st.builds(
    limp_LabelStatement,
    name=
        safe_text
)
limp_ReturnStatement_strategy = st.builds(
    limp_ReturnStatement,
)
limp_ContinueStatement_strategy = st.builds(
    limp_ContinueStatement,
)
limp_IfThenElseStatement_strategy = st.builds(
    limp_IfThenElseStatement,
)
limp_ForStatement_strategy = st.builds(
    limp_ForStatement,
)
limp_BreakStatement_strategy = st.builds(
    limp_BreakStatement,
)
limp_AssignmentStatement_strategy = st.builds(
    limp_AssignmentStatement,
)
limp_GotoStatement_strategy = st.builds(
    limp_GotoStatement,
)
limp_VoidStatement_strategy = st.builds(
    limp_VoidStatement,
)
limp_Statement_strategy = st.builds(
    limp_Statement,
)
limp_DefineUseRef_strategy = st.builds(
    limp_DefineUseRef,
)
limp_WhileStatement_strategy = st.builds(
    limp_WhileStatement,
)
limp_Else_strategy = st.builds(
    limp_Else,
)
limp_VariableRef_strategy = st.builds(
    limp_VariableRef,
    name=
        safe_text
)
limp_Expr_strategy = st.builds(
    limp_Expr,
)
Attribute_strategy = st.builds(
    Attribute,
)
limp_Uses_strategy = st.builds(
    limp_Uses,
)
limp_Define_strategy = st.builds(
    limp_Define,
)
limp_Postcondition_strategy = st.builds(
    limp_Postcondition,
    name=
        safe_text
)
limp_Precondition_strategy = st.builds(
    limp_Precondition,
    name=
        safe_text
)
limp_Attribute_strategy = st.builds(
    limp_Attribute,
)
limp_RecordFieldType_strategy = st.builds(
    limp_RecordFieldType,
    fieldName=
        safe_text
)
VariableRef_strategy = st.builds(
    VariableRef,
)
limp_LocalArg_strategy = st.builds(
    limp_LocalArg,
)
limp_InputArg_strategy = st.builds(
    limp_InputArg,
)
limp_EnumValue_strategy = st.builds(
    limp_EnumValue,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
limp_TypeAlias_strategy = st.builds(
    limp_TypeAlias,
)
limp_RecordTypeDef_strategy = st.builds(
    limp_RecordTypeDef,
)
limp_EnumTypeDef_strategy = st.builds(
    limp_EnumTypeDef,
)
limp_StatementBlock_strategy = st.builds(
    limp_StatementBlock,
)
limp_EquationBlock_strategy = st.builds(
    limp_EquationBlock,
)
limp_AbstractTypeDef_strategy = st.builds(
    limp_AbstractTypeDef,
)
limp_Type_strategy = st.builds(
    limp_Type,
)
limp_ArrayTypeDef_strategy = st.builds(
    limp_ArrayTypeDef,
    size=
        safe_text
)
limp_AttributeBlock_strategy = st.builds(
    limp_AttributeBlock,
)
limp_OutputArgList_strategy = st.builds(
    limp_OutputArgList,
)
limp_OutputArg_strategy = st.builds(
    limp_OutputArg,
)
limp_InputArgList_strategy = st.builds(
    limp_InputArgList,
)
FunctionRef_strategy = st.builds(
    FunctionRef,
)
Declaration_strategy = st.builds(
    Declaration,
)
limp_LocalProcedure_strategy = st.builds(
    limp_LocalProcedure,
    name=
        safe_text
)
limp_ConstantDeclaration_strategy = st.builds(
    limp_ConstantDeclaration,
)
limp_ExternalFunction_strategy = st.builds(
    limp_ExternalFunction,
    name=
        safe_text
)
limp_GlobalDeclaration_strategy = st.builds(
    limp_GlobalDeclaration,
)
limp_ExternalProcedure_strategy = st.builds(
    limp_ExternalProcedure,
    name=
        safe_text
)
limp_TypeDeclaration_strategy = st.builds(
    limp_TypeDeclaration,
    name=
        safe_text
)
limp_Import_strategy = st.builds(
    limp_Import,
    importURI=
        safe_text
)
limp_Comment_strategy = st.builds(
    limp_Comment,
    comment=
        safe_text
)
limp_Declaration_strategy = st.builds(
    limp_Declaration,
)
limp_Specification_strategy = st.builds(
    limp_Specification,
)
limp_VarBlock_strategy = st.builds(
    limp_VarBlock,
)
limp_LocalFunction_strategy = st.builds(
    limp_LocalFunction,
    name=
        safe_text
)

@given(instance=Else_strategy)
@settings(max_examples=50)
def test_else_instantiation(instance):
    assert isinstance(instance, Else)

@given(instance=limp_ElseIf_strategy)
@settings(max_examples=50)
def test_limp_elseif_instantiation(instance):
    assert isinstance(instance, limp_ElseIf)

@given(instance=limp_NoElse_strategy)
@settings(max_examples=50)
def test_limp_noelse_instantiation(instance):
    assert isinstance(instance, limp_NoElse)

@given(instance=limp_ElseBlock_strategy)
@settings(max_examples=50)
def test_limp_elseblock_instantiation(instance):
    assert isinstance(instance, limp_ElseBlock)

@given(instance=AttributeBlock_strategy)
@settings(max_examples=50)
def test_attributeblock_instantiation(instance):
    assert isinstance(instance, AttributeBlock)

@given(instance=limp_NoAttributeBlock_strategy)
@settings(max_examples=50)
def test_limp_noattributeblock_instantiation(instance):
    assert isinstance(instance, limp_NoAttributeBlock)

@given(instance=limp_SomeAttributeBlock_strategy)
@settings(max_examples=50)
def test_limp_someattributeblock_instantiation(instance):
    assert isinstance(instance, limp_SomeAttributeBlock)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=limp_BoolType_strategy)
@settings(max_examples=50)
def test_limp_booltype_instantiation(instance):
    assert isinstance(instance, limp_BoolType)

@given(instance=limp_RecordType_strategy)
@settings(max_examples=50)
def test_limp_recordtype_instantiation(instance):
    assert isinstance(instance, limp_RecordType)

@given(instance=limp_IntegerType_strategy)
@settings(max_examples=50)
def test_limp_integertype_instantiation(instance):
    assert isinstance(instance, limp_IntegerType)

@given(instance=limp_TupleType_strategy)
@settings(max_examples=50)
def test_limp_tupletype_instantiation(instance):
    assert isinstance(instance, limp_TupleType)

@given(instance=limp_StringType_strategy)
@settings(max_examples=50)
def test_limp_stringtype_instantiation(instance):
    assert isinstance(instance, limp_StringType)

@given(instance=limp_ArrayType_strategy)
@settings(max_examples=50)
def test_limp_arraytype_instantiation(instance):
    assert isinstance(instance, limp_ArrayType)

@given(instance=limp_RealType_strategy)
@settings(max_examples=50)
def test_limp_realtype_instantiation(instance):
    assert isinstance(instance, limp_RealType)

@given(instance=limp_EnumType_strategy)
@settings(max_examples=50)
def test_limp_enumtype_instantiation(instance):
    assert isinstance(instance, limp_EnumType)

@given(instance=limp_VoidType_strategy)
@settings(max_examples=50)
def test_limp_voidtype_instantiation(instance):
    assert isinstance(instance, limp_VoidType)

@given(instance=VarBlock_strategy)
@settings(max_examples=50)
def test_varblock_instantiation(instance):
    assert isinstance(instance, VarBlock)

@given(instance=limp_NoVarBlock_strategy)
@settings(max_examples=50)
def test_limp_novarblock_instantiation(instance):
    assert isinstance(instance, limp_NoVarBlock)

@given(instance=limp_SomeVarBlock_strategy)
@settings(max_examples=50)
def test_limp_somevarblock_instantiation(instance):
    assert isinstance(instance, limp_SomeVarBlock)

@given(instance=limp_ExprList_strategy)
@settings(max_examples=50)
def test_limp_exprlist_instantiation(instance):
    assert isinstance(instance, limp_ExprList)

@given(instance=limp_NamedType_strategy)
@settings(max_examples=50)
def test_limp_namedtype_instantiation(instance):
    assert isinstance(instance, limp_NamedType)

@given(instance=limp_AbstractType_strategy)
@settings(max_examples=50)
def test_limp_abstracttype_instantiation(instance):
    assert isinstance(instance, limp_AbstractType)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=limp_ArrayUpdateExpr_strategy)
@settings(max_examples=50)
def test_limp_arrayupdateexpr_instantiation(instance):
    assert isinstance(instance, limp_ArrayUpdateExpr)

@given(instance=limp_RecordUpdateExpr_strategy)
@settings(max_examples=50)
def test_limp_recordupdateexpr_instantiation(instance):
    assert isinstance(instance, limp_RecordUpdateExpr)



@given(instance=limp_RecordUpdateExpr_strategy)
def test_limp_recordupdateexpr_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=limp_SecondInit_strategy)
@settings(max_examples=50)
def test_limp_secondinit_instantiation(instance):
    assert isinstance(instance, limp_SecondInit)

@given(instance=limp_IntegerLiteralExpr_strategy)
@settings(max_examples=50)
def test_limp_integerliteralexpr_instantiation(instance):
    assert isinstance(instance, limp_IntegerLiteralExpr)



@given(instance=limp_IntegerLiteralExpr_strategy)
def test_limp_integerliteralexpr_intVal_setter(instance):
    original = instance.intVal
    instance.intVal = original
    assert instance.intVal == original

@given(instance=limp_ChoiceExpr_strategy)
@settings(max_examples=50)
def test_limp_choiceexpr_instantiation(instance):
    assert isinstance(instance, limp_ChoiceExpr)

@given(instance=limp_ArrayAccessExpr_strategy)
@settings(max_examples=50)
def test_limp_arrayaccessexpr_instantiation(instance):
    assert isinstance(instance, limp_ArrayAccessExpr)

@given(instance=limp_UnaryNegationExpr_strategy)
@settings(max_examples=50)
def test_limp_unarynegationexpr_instantiation(instance):
    assert isinstance(instance, limp_UnaryNegationExpr)

@given(instance=limp_StringLiteralExpr_strategy)
@settings(max_examples=50)
def test_limp_stringliteralexpr_instantiation(instance):
    assert isinstance(instance, limp_StringLiteralExpr)



@given(instance=limp_StringLiteralExpr_strategy)
def test_limp_stringliteralexpr_stringVal_setter(instance):
    original = instance.stringVal
    instance.stringVal = original
    assert instance.stringVal == original

@given(instance=limp_RecordAccessExpr_strategy)
@settings(max_examples=50)
def test_limp_recordaccessexpr_instantiation(instance):
    assert isinstance(instance, limp_RecordAccessExpr)



@given(instance=limp_RecordAccessExpr_strategy)
def test_limp_recordaccessexpr_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=limp_IfThenElseExpr_strategy)
@settings(max_examples=50)
def test_limp_ifthenelseexpr_instantiation(instance):
    assert isinstance(instance, limp_IfThenElseExpr)

@given(instance=limp_BinaryExpr_strategy)
@settings(max_examples=50)
def test_limp_binaryexpr_instantiation(instance):
    assert isinstance(instance, limp_BinaryExpr)



@given(instance=limp_BinaryExpr_strategy)
def test_limp_binaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=limp_RealLiteralExpr_strategy)
@settings(max_examples=50)
def test_limp_realliteralexpr_instantiation(instance):
    assert isinstance(instance, limp_RealLiteralExpr)



@given(instance=limp_RealLiteralExpr_strategy)
def test_limp_realliteralexpr_realVal_setter(instance):
    original = instance.realVal
    instance.realVal = original
    assert instance.realVal == original

@given(instance=limp_UnaryMinusExpr_strategy)
@settings(max_examples=50)
def test_limp_unaryminusexpr_instantiation(instance):
    assert isinstance(instance, limp_UnaryMinusExpr)

@given(instance=limp_IntegerWildCardExpr_strategy)
@settings(max_examples=50)
def test_limp_integerwildcardexpr_instantiation(instance):
    assert isinstance(instance, limp_IntegerWildCardExpr)

@given(instance=limp_FreshVariable_strategy)
@settings(max_examples=50)
def test_limp_freshvariable_instantiation(instance):
    assert isinstance(instance, limp_FreshVariable)



@given(instance=limp_FreshVariable_strategy)
def test_limp_freshvariable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=limp_InitExpr_strategy)
@settings(max_examples=50)
def test_limp_initexpr_instantiation(instance):
    assert isinstance(instance, limp_InitExpr)

@given(instance=limp_FcnCallExpr_strategy)
@settings(max_examples=50)
def test_limp_fcncallexpr_instantiation(instance):
    assert isinstance(instance, limp_FcnCallExpr)

@given(instance=limp_BooleanLiteralExpr_strategy)
@settings(max_examples=50)
def test_limp_booleanliteralexpr_instantiation(instance):
    assert isinstance(instance, limp_BooleanLiteralExpr)



@given(instance=limp_BooleanLiteralExpr_strategy)
def test_limp_booleanliteralexpr_boolVal_setter(instance):
    original = instance.boolVal
    instance.boolVal = original
    assert instance.boolVal == original

@given(instance=limp_IdExpr_strategy)
@settings(max_examples=50)
def test_limp_idexpr_instantiation(instance):
    assert isinstance(instance, limp_IdExpr)

@given(instance=limp_ArrayExpr_strategy)
@settings(max_examples=50)
def test_limp_arrayexpr_instantiation(instance):
    assert isinstance(instance, limp_ArrayExpr)

@given(instance=limp_FunctionRef_strategy)
@settings(max_examples=50)
def test_limp_functionref_instantiation(instance):
    assert isinstance(instance, limp_FunctionRef)

@given(instance=limp_Equation_strategy)
@settings(max_examples=50)
def test_limp_equation_instantiation(instance):
    assert isinstance(instance, limp_Equation)

@given(instance=limp_RecordFieldExpr_strategy)
@settings(max_examples=50)
def test_limp_recordfieldexpr_instantiation(instance):
    assert isinstance(instance, limp_RecordFieldExpr)



@given(instance=limp_RecordFieldExpr_strategy)
def test_limp_recordfieldexpr_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=limp_RecordExpr_strategy)
@settings(max_examples=50)
def test_limp_recordexpr_instantiation(instance):
    assert isinstance(instance, limp_RecordExpr)

@given(instance=limp_IdList_strategy)
@settings(max_examples=50)
def test_limp_idlist_instantiation(instance):
    assert isinstance(instance, limp_IdList)

@given(instance=Equation_strategy)
@settings(max_examples=50)
def test_equation_instantiation(instance):
    assert isinstance(instance, Equation)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=limp_LabelStatement_strategy)
@settings(max_examples=50)
def test_limp_labelstatement_instantiation(instance):
    assert isinstance(instance, limp_LabelStatement)



@given(instance=limp_LabelStatement_strategy)
def test_limp_labelstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp_ReturnStatement_strategy)
@settings(max_examples=50)
def test_limp_returnstatement_instantiation(instance):
    assert isinstance(instance, limp_ReturnStatement)

@given(instance=limp_ContinueStatement_strategy)
@settings(max_examples=50)
def test_limp_continuestatement_instantiation(instance):
    assert isinstance(instance, limp_ContinueStatement)

@given(instance=limp_IfThenElseStatement_strategy)
@settings(max_examples=50)
def test_limp_ifthenelsestatement_instantiation(instance):
    assert isinstance(instance, limp_IfThenElseStatement)

@given(instance=limp_ForStatement_strategy)
@settings(max_examples=50)
def test_limp_forstatement_instantiation(instance):
    assert isinstance(instance, limp_ForStatement)

@given(instance=limp_BreakStatement_strategy)
@settings(max_examples=50)
def test_limp_breakstatement_instantiation(instance):
    assert isinstance(instance, limp_BreakStatement)

@given(instance=limp_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_limp_assignmentstatement_instantiation(instance):
    assert isinstance(instance, limp_AssignmentStatement)

@given(instance=limp_GotoStatement_strategy)
@settings(max_examples=50)
def test_limp_gotostatement_instantiation(instance):
    assert isinstance(instance, limp_GotoStatement)

@given(instance=limp_VoidStatement_strategy)
@settings(max_examples=50)
def test_limp_voidstatement_instantiation(instance):
    assert isinstance(instance, limp_VoidStatement)

@given(instance=limp_Statement_strategy)
@settings(max_examples=50)
def test_limp_statement_instantiation(instance):
    assert isinstance(instance, limp_Statement)

@given(instance=limp_DefineUseRef_strategy)
@settings(max_examples=50)
def test_limp_defineuseref_instantiation(instance):
    assert isinstance(instance, limp_DefineUseRef)

@given(instance=limp_WhileStatement_strategy)
@settings(max_examples=50)
def test_limp_whilestatement_instantiation(instance):
    assert isinstance(instance, limp_WhileStatement)

@given(instance=limp_Else_strategy)
@settings(max_examples=50)
def test_limp_else_instantiation(instance):
    assert isinstance(instance, limp_Else)

@given(instance=limp_VariableRef_strategy)
@settings(max_examples=50)
def test_limp_variableref_instantiation(instance):
    assert isinstance(instance, limp_VariableRef)



@given(instance=limp_VariableRef_strategy)
def test_limp_variableref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp_Expr_strategy)
@settings(max_examples=50)
def test_limp_expr_instantiation(instance):
    assert isinstance(instance, limp_Expr)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=limp_Uses_strategy)
@settings(max_examples=50)
def test_limp_uses_instantiation(instance):
    assert isinstance(instance, limp_Uses)

@given(instance=limp_Define_strategy)
@settings(max_examples=50)
def test_limp_define_instantiation(instance):
    assert isinstance(instance, limp_Define)

@given(instance=limp_Postcondition_strategy)
@settings(max_examples=50)
def test_limp_postcondition_instantiation(instance):
    assert isinstance(instance, limp_Postcondition)



@given(instance=limp_Postcondition_strategy)
def test_limp_postcondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp_Precondition_strategy)
@settings(max_examples=50)
def test_limp_precondition_instantiation(instance):
    assert isinstance(instance, limp_Precondition)



@given(instance=limp_Precondition_strategy)
def test_limp_precondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp_Attribute_strategy)
@settings(max_examples=50)
def test_limp_attribute_instantiation(instance):
    assert isinstance(instance, limp_Attribute)

@given(instance=limp_RecordFieldType_strategy)
@settings(max_examples=50)
def test_limp_recordfieldtype_instantiation(instance):
    assert isinstance(instance, limp_RecordFieldType)



@given(instance=limp_RecordFieldType_strategy)
def test_limp_recordfieldtype_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=VariableRef_strategy)
@settings(max_examples=50)
def test_variableref_instantiation(instance):
    assert isinstance(instance, VariableRef)

@given(instance=limp_LocalArg_strategy)
@settings(max_examples=50)
def test_limp_localarg_instantiation(instance):
    assert isinstance(instance, limp_LocalArg)

@given(instance=limp_InputArg_strategy)
@settings(max_examples=50)
def test_limp_inputarg_instantiation(instance):
    assert isinstance(instance, limp_InputArg)

@given(instance=limp_EnumValue_strategy)
@settings(max_examples=50)
def test_limp_enumvalue_instantiation(instance):
    assert isinstance(instance, limp_EnumValue)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=limp_TypeAlias_strategy)
@settings(max_examples=50)
def test_limp_typealias_instantiation(instance):
    assert isinstance(instance, limp_TypeAlias)

@given(instance=limp_RecordTypeDef_strategy)
@settings(max_examples=50)
def test_limp_recordtypedef_instantiation(instance):
    assert isinstance(instance, limp_RecordTypeDef)

@given(instance=limp_EnumTypeDef_strategy)
@settings(max_examples=50)
def test_limp_enumtypedef_instantiation(instance):
    assert isinstance(instance, limp_EnumTypeDef)

@given(instance=limp_StatementBlock_strategy)
@settings(max_examples=50)
def test_limp_statementblock_instantiation(instance):
    assert isinstance(instance, limp_StatementBlock)

@given(instance=limp_EquationBlock_strategy)
@settings(max_examples=50)
def test_limp_equationblock_instantiation(instance):
    assert isinstance(instance, limp_EquationBlock)

@given(instance=limp_AbstractTypeDef_strategy)
@settings(max_examples=50)
def test_limp_abstracttypedef_instantiation(instance):
    assert isinstance(instance, limp_AbstractTypeDef)

@given(instance=limp_Type_strategy)
@settings(max_examples=50)
def test_limp_type_instantiation(instance):
    assert isinstance(instance, limp_Type)

@given(instance=limp_ArrayTypeDef_strategy)
@settings(max_examples=50)
def test_limp_arraytypedef_instantiation(instance):
    assert isinstance(instance, limp_ArrayTypeDef)



@given(instance=limp_ArrayTypeDef_strategy)
def test_limp_arraytypedef_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=limp_AttributeBlock_strategy)
@settings(max_examples=50)
def test_limp_attributeblock_instantiation(instance):
    assert isinstance(instance, limp_AttributeBlock)

@given(instance=limp_OutputArgList_strategy)
@settings(max_examples=50)
def test_limp_outputarglist_instantiation(instance):
    assert isinstance(instance, limp_OutputArgList)

@given(instance=limp_OutputArg_strategy)
@settings(max_examples=50)
def test_limp_outputarg_instantiation(instance):
    assert isinstance(instance, limp_OutputArg)

@given(instance=limp_InputArgList_strategy)
@settings(max_examples=50)
def test_limp_inputarglist_instantiation(instance):
    assert isinstance(instance, limp_InputArgList)

@given(instance=FunctionRef_strategy)
@settings(max_examples=50)
def test_functionref_instantiation(instance):
    assert isinstance(instance, FunctionRef)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=limp_LocalProcedure_strategy)
@settings(max_examples=50)
def test_limp_localprocedure_instantiation(instance):
    assert isinstance(instance, limp_LocalProcedure)



@given(instance=limp_LocalProcedure_strategy)
def test_limp_localprocedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_limp_constantdeclaration_instantiation(instance):
    assert isinstance(instance, limp_ConstantDeclaration)

@given(instance=limp_ExternalFunction_strategy)
@settings(max_examples=50)
def test_limp_externalfunction_instantiation(instance):
    assert isinstance(instance, limp_ExternalFunction)



@given(instance=limp_ExternalFunction_strategy)
def test_limp_externalfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp_GlobalDeclaration_strategy)
@settings(max_examples=50)
def test_limp_globaldeclaration_instantiation(instance):
    assert isinstance(instance, limp_GlobalDeclaration)

@given(instance=limp_ExternalProcedure_strategy)
@settings(max_examples=50)
def test_limp_externalprocedure_instantiation(instance):
    assert isinstance(instance, limp_ExternalProcedure)



@given(instance=limp_ExternalProcedure_strategy)
def test_limp_externalprocedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_limp_typedeclaration_instantiation(instance):
    assert isinstance(instance, limp_TypeDeclaration)



@given(instance=limp_TypeDeclaration_strategy)
def test_limp_typedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp_Import_strategy)
@settings(max_examples=50)
def test_limp_import_instantiation(instance):
    assert isinstance(instance, limp_Import)



@given(instance=limp_Import_strategy)
def test_limp_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=limp_Comment_strategy)
@settings(max_examples=50)
def test_limp_comment_instantiation(instance):
    assert isinstance(instance, limp_Comment)



@given(instance=limp_Comment_strategy)
def test_limp_comment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=limp_Declaration_strategy)
@settings(max_examples=50)
def test_limp_declaration_instantiation(instance):
    assert isinstance(instance, limp_Declaration)

@given(instance=limp_Specification_strategy)
@settings(max_examples=50)
def test_limp_specification_instantiation(instance):
    assert isinstance(instance, limp_Specification)

@given(instance=limp_VarBlock_strategy)
@settings(max_examples=50)
def test_limp_varblock_instantiation(instance):
    assert isinstance(instance, limp_VarBlock)

@given(instance=limp_LocalFunction_strategy)
@settings(max_examples=50)
def test_limp_localfunction_instantiation(instance):
    assert isinstance(instance, limp_LocalFunction)



@given(instance=limp_LocalFunction_strategy)
def test_limp_localfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
