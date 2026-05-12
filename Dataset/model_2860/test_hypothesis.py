import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    go_SouceFile,
    float_lit,
    go_ImportPath,
    go_ImportSpec,
    go_imaginary_lit,
    go_exponent,
    go_RecvExpr,
    go_RecvStmt,
    go_CommCase,
    go_CommClause,
    go_InitStmt,
    go_PostStmt,
    go_TypeCaseClause,
    go_TypeSwitchGuard,
    go_ExprSwitchCase,
    go_ExprCaseClause,
    go_switch_stmt_linha,
    go_RangeClause,
    go_ForClause,
    go_Condition,
    go_TypeList,
    go_TypeSwitchCase,
    go_Channel,
    go_Label,
    go_Assignment,
    go_IncDecStmt,
    go_SendStmt,
    go_ExpressionStmt,
    go_GotoStmt,
    go_ContinueStmt,
    go_BreakStmt,
    go_ReturnStmt,
    go_GoStmt,
    go_LabeledStmt,
    SwitchStmt,
    go_SimpleStmt,
    go_DeferStmt,
    go_ForStmt,
    go_SelectStmt,
    go_SwitchStmt,
    go_IfStmt,
    go_ReceiverType,
    go_decimals,
    go_Slice,
    go_binary_op,
    go_ExpressionLinha,
    go_UnaryExpr,
    go_Arguments,
    go_MethodExpr,
    go_Conversion,
    go_PrimaryExprLinha,
    go_PrimaryExpr,
    go_FieldName,
    go_Index,
    go_TypeAssertion,
    go_Selector,
    go_cochetes,
    go_ponto,
    go_LiteralTypeLinha,
    go_LiteralValue,
    go_LiteralType,
    Literal,
    go_FunctionLit,
    go_CompositeLit,
    go_PackageName,
    OperandName,
    go_Key,
    go_Element,
    go_KeyedElement,
    go_ElementList,
    go_MethodDecl,
    go_FunctionDecl,
    go_ShortVarDecl,
    go_rune_lit,
    go_float_lit,
    go_BasicLit,
    go_OperandName,
    go_Literal,
    go_Operand,
    go_ExpressionList,
    go_ConstSpec,
    go_Receiver,
    go_FunctionBody,
    go_FunctionName,
    go_VarSpec,
    TypeSpec,
    go_TypeDef,
    go_AliasDecl,
    go_TypeSpec,
    go_KeyType,
    go_InterfaceTypeName,
    go_MethodName,
    go_MethodSpec,
    go_topLevelDeclLinha,
    go_VarDecl,
    go_TypeDecl,
    go_ConstDecl,
    go_Declaration,
    go_Statement,
    go_StatementList,
    go_Block,
    go_Result,
    go_Signature,
    go_string_lit,
    go_Tag,
    go_EmbeddedField,
    go_IdentifierList,
    go_FieldDecl,
    go_ParameterDecl,
    go_ParameterList,
    Receiver,
    go_Parameters,
    go_InterfaceType,
    go_FunctionType,
    go_PointerType,
    go_StructType,
    go_TypeLitLinha,
    go_QualifiedIdent,
    go_TypeNameLinha,
    go_identifier,
    go_TypeLit,
    go_Expression,
    go_ElementType,
    go_ArrayLength,
    go_ChannelType,
    go_MapType,
    go_TypeName,
    go_Type,
    go_TopLevelDecl,
    go_ImportDecl,
    go_PackageClause,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_go_soucefile_is_not_abstract():
    assert not inspect.isabstract(go_SouceFile)


def test_go_soucefile_constructor_exists():
    assert callable(go_SouceFile.__init__)


def test_go_soucefile_constructor_args():
    sig = inspect.signature(go_SouceFile.__init__)
    params = list(sig.parameters.keys())



def test_float_lit_is_not_abstract():
    assert not inspect.isabstract(float_lit)


def test_float_lit_constructor_exists():
    assert callable(float_lit.__init__)


def test_float_lit_constructor_args():
    sig = inspect.signature(float_lit.__init__)
    params = list(sig.parameters.keys())



def test_go_importpath_is_not_abstract():
    assert not inspect.isabstract(go_ImportPath)


def test_go_importpath_constructor_exists():
    assert callable(go_ImportPath.__init__)


def test_go_importpath_constructor_args():
    sig = inspect.signature(go_ImportPath.__init__)
    params = list(sig.parameters.keys())



def test_go_importspec_is_not_abstract():
    assert not inspect.isabstract(go_ImportSpec)


def test_go_importspec_constructor_exists():
    assert callable(go_ImportSpec.__init__)


def test_go_importspec_constructor_args():
    sig = inspect.signature(go_ImportSpec.__init__)
    params = list(sig.parameters.keys())



def test_go_imaginary_lit_is_not_abstract():
    assert not inspect.isabstract(go_imaginary_lit)


def test_go_imaginary_lit_constructor_exists():
    assert callable(go_imaginary_lit.__init__)


def test_go_imaginary_lit_constructor_args():
    sig = inspect.signature(go_imaginary_lit.__init__)
    params = list(sig.parameters.keys())



def test_go_exponent_is_not_abstract():
    assert not inspect.isabstract(go_exponent)


def test_go_exponent_constructor_exists():
    assert callable(go_exponent.__init__)


def test_go_exponent_constructor_args():
    sig = inspect.signature(go_exponent.__init__)
    params = list(sig.parameters.keys())



def test_go_recvexpr_is_not_abstract():
    assert not inspect.isabstract(go_RecvExpr)


def test_go_recvexpr_constructor_exists():
    assert callable(go_RecvExpr.__init__)


def test_go_recvexpr_constructor_args():
    sig = inspect.signature(go_RecvExpr.__init__)
    params = list(sig.parameters.keys())



def test_go_recvstmt_is_not_abstract():
    assert not inspect.isabstract(go_RecvStmt)


def test_go_recvstmt_constructor_exists():
    assert callable(go_RecvStmt.__init__)


def test_go_recvstmt_constructor_args():
    sig = inspect.signature(go_RecvStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_commcase_is_not_abstract():
    assert not inspect.isabstract(go_CommCase)


def test_go_commcase_constructor_exists():
    assert callable(go_CommCase.__init__)


def test_go_commcase_constructor_args():
    sig = inspect.signature(go_CommCase.__init__)
    params = list(sig.parameters.keys())



def test_go_commclause_is_not_abstract():
    assert not inspect.isabstract(go_CommClause)


def test_go_commclause_constructor_exists():
    assert callable(go_CommClause.__init__)


def test_go_commclause_constructor_args():
    sig = inspect.signature(go_CommClause.__init__)
    params = list(sig.parameters.keys())



def test_go_initstmt_is_not_abstract():
    assert not inspect.isabstract(go_InitStmt)


def test_go_initstmt_constructor_exists():
    assert callable(go_InitStmt.__init__)


def test_go_initstmt_constructor_args():
    sig = inspect.signature(go_InitStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_poststmt_is_not_abstract():
    assert not inspect.isabstract(go_PostStmt)


def test_go_poststmt_constructor_exists():
    assert callable(go_PostStmt.__init__)


def test_go_poststmt_constructor_args():
    sig = inspect.signature(go_PostStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_typecaseclause_is_not_abstract():
    assert not inspect.isabstract(go_TypeCaseClause)


def test_go_typecaseclause_constructor_exists():
    assert callable(go_TypeCaseClause.__init__)


def test_go_typecaseclause_constructor_args():
    sig = inspect.signature(go_TypeCaseClause.__init__)
    params = list(sig.parameters.keys())



def test_go_typeswitchguard_is_not_abstract():
    assert not inspect.isabstract(go_TypeSwitchGuard)


def test_go_typeswitchguard_constructor_exists():
    assert callable(go_TypeSwitchGuard.__init__)


def test_go_typeswitchguard_constructor_args():
    sig = inspect.signature(go_TypeSwitchGuard.__init__)
    params = list(sig.parameters.keys())



def test_go_exprswitchcase_is_not_abstract():
    assert not inspect.isabstract(go_ExprSwitchCase)


def test_go_exprswitchcase_constructor_exists():
    assert callable(go_ExprSwitchCase.__init__)


def test_go_exprswitchcase_constructor_args():
    sig = inspect.signature(go_ExprSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_go_exprcaseclause_is_not_abstract():
    assert not inspect.isabstract(go_ExprCaseClause)


def test_go_exprcaseclause_constructor_exists():
    assert callable(go_ExprCaseClause.__init__)


def test_go_exprcaseclause_constructor_args():
    sig = inspect.signature(go_ExprCaseClause.__init__)
    params = list(sig.parameters.keys())



def test_go_switch_stmt_linha_is_not_abstract():
    assert not inspect.isabstract(go_switch_stmt_linha)


def test_go_switch_stmt_linha_constructor_exists():
    assert callable(go_switch_stmt_linha.__init__)


def test_go_switch_stmt_linha_constructor_args():
    sig = inspect.signature(go_switch_stmt_linha.__init__)
    params = list(sig.parameters.keys())



def test_go_rangeclause_is_not_abstract():
    assert not inspect.isabstract(go_RangeClause)


def test_go_rangeclause_constructor_exists():
    assert callable(go_RangeClause.__init__)


def test_go_rangeclause_constructor_args():
    sig = inspect.signature(go_RangeClause.__init__)
    params = list(sig.parameters.keys())



def test_go_forclause_is_not_abstract():
    assert not inspect.isabstract(go_ForClause)


def test_go_forclause_constructor_exists():
    assert callable(go_ForClause.__init__)


def test_go_forclause_constructor_args():
    sig = inspect.signature(go_ForClause.__init__)
    params = list(sig.parameters.keys())



def test_go_condition_is_not_abstract():
    assert not inspect.isabstract(go_Condition)


def test_go_condition_constructor_exists():
    assert callable(go_Condition.__init__)


def test_go_condition_constructor_args():
    sig = inspect.signature(go_Condition.__init__)
    params = list(sig.parameters.keys())



def test_go_typelist_is_not_abstract():
    assert not inspect.isabstract(go_TypeList)


def test_go_typelist_constructor_exists():
    assert callable(go_TypeList.__init__)


def test_go_typelist_constructor_args():
    sig = inspect.signature(go_TypeList.__init__)
    params = list(sig.parameters.keys())



def test_go_typeswitchcase_is_not_abstract():
    assert not inspect.isabstract(go_TypeSwitchCase)


def test_go_typeswitchcase_constructor_exists():
    assert callable(go_TypeSwitchCase.__init__)


def test_go_typeswitchcase_constructor_args():
    sig = inspect.signature(go_TypeSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_go_channel_is_not_abstract():
    assert not inspect.isabstract(go_Channel)


def test_go_channel_constructor_exists():
    assert callable(go_Channel.__init__)


def test_go_channel_constructor_args():
    sig = inspect.signature(go_Channel.__init__)
    params = list(sig.parameters.keys())



def test_go_label_is_not_abstract():
    assert not inspect.isabstract(go_Label)


def test_go_label_constructor_exists():
    assert callable(go_Label.__init__)


def test_go_label_constructor_args():
    sig = inspect.signature(go_Label.__init__)
    params = list(sig.parameters.keys())



def test_go_assignment_is_not_abstract():
    assert not inspect.isabstract(go_Assignment)


def test_go_assignment_constructor_exists():
    assert callable(go_Assignment.__init__)


def test_go_assignment_constructor_args():
    sig = inspect.signature(go_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "assign_op" in params, "Missing parameter 'assign_op'"

def test_go_assignment_has_assign_op():
    assert hasattr(go_Assignment, "assign_op")
    descriptor = None
    for klass in go_Assignment.__mro__:
        if "assign_op" in klass.__dict__:
            descriptor = klass.__dict__["assign_op"]
            break
    assert isinstance(descriptor, property)



def test_go_incdecstmt_is_not_abstract():
    assert not inspect.isabstract(go_IncDecStmt)


def test_go_incdecstmt_constructor_exists():
    assert callable(go_IncDecStmt.__init__)


def test_go_incdecstmt_constructor_args():
    sig = inspect.signature(go_IncDecStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_sendstmt_is_not_abstract():
    assert not inspect.isabstract(go_SendStmt)


def test_go_sendstmt_constructor_exists():
    assert callable(go_SendStmt.__init__)


def test_go_sendstmt_constructor_args():
    sig = inspect.signature(go_SendStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_expressionstmt_is_not_abstract():
    assert not inspect.isabstract(go_ExpressionStmt)


def test_go_expressionstmt_constructor_exists():
    assert callable(go_ExpressionStmt.__init__)


def test_go_expressionstmt_constructor_args():
    sig = inspect.signature(go_ExpressionStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_gotostmt_is_not_abstract():
    assert not inspect.isabstract(go_GotoStmt)


def test_go_gotostmt_constructor_exists():
    assert callable(go_GotoStmt.__init__)


def test_go_gotostmt_constructor_args():
    sig = inspect.signature(go_GotoStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_continuestmt_is_not_abstract():
    assert not inspect.isabstract(go_ContinueStmt)


def test_go_continuestmt_constructor_exists():
    assert callable(go_ContinueStmt.__init__)


def test_go_continuestmt_constructor_args():
    sig = inspect.signature(go_ContinueStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_breakstmt_is_not_abstract():
    assert not inspect.isabstract(go_BreakStmt)


def test_go_breakstmt_constructor_exists():
    assert callable(go_BreakStmt.__init__)


def test_go_breakstmt_constructor_args():
    sig = inspect.signature(go_BreakStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_returnstmt_is_not_abstract():
    assert not inspect.isabstract(go_ReturnStmt)


def test_go_returnstmt_constructor_exists():
    assert callable(go_ReturnStmt.__init__)


def test_go_returnstmt_constructor_args():
    sig = inspect.signature(go_ReturnStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_gostmt_is_not_abstract():
    assert not inspect.isabstract(go_GoStmt)


def test_go_gostmt_constructor_exists():
    assert callable(go_GoStmt.__init__)


def test_go_gostmt_constructor_args():
    sig = inspect.signature(go_GoStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_labeledstmt_is_not_abstract():
    assert not inspect.isabstract(go_LabeledStmt)


def test_go_labeledstmt_constructor_exists():
    assert callable(go_LabeledStmt.__init__)


def test_go_labeledstmt_constructor_args():
    sig = inspect.signature(go_LabeledStmt.__init__)
    params = list(sig.parameters.keys())



def test_switchstmt_is_not_abstract():
    assert not inspect.isabstract(SwitchStmt)


def test_switchstmt_constructor_exists():
    assert callable(SwitchStmt.__init__)


def test_switchstmt_constructor_args():
    sig = inspect.signature(SwitchStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_simplestmt_is_not_abstract():
    assert not inspect.isabstract(go_SimpleStmt)


def test_go_simplestmt_constructor_exists():
    assert callable(go_SimpleStmt.__init__)


def test_go_simplestmt_constructor_args():
    sig = inspect.signature(go_SimpleStmt.__init__)
    params = list(sig.parameters.keys())
    assert "EmptyStmt" in params, "Missing parameter 'EmptyStmt'"

def test_go_simplestmt_has_EmptyStmt():
    assert hasattr(go_SimpleStmt, "EmptyStmt")
    descriptor = None
    for klass in go_SimpleStmt.__mro__:
        if "EmptyStmt" in klass.__dict__:
            descriptor = klass.__dict__["EmptyStmt"]
            break
    assert isinstance(descriptor, property)



def test_go_deferstmt_is_not_abstract():
    assert not inspect.isabstract(go_DeferStmt)


def test_go_deferstmt_constructor_exists():
    assert callable(go_DeferStmt.__init__)


def test_go_deferstmt_constructor_args():
    sig = inspect.signature(go_DeferStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_forstmt_is_not_abstract():
    assert not inspect.isabstract(go_ForStmt)


def test_go_forstmt_constructor_exists():
    assert callable(go_ForStmt.__init__)


def test_go_forstmt_constructor_args():
    sig = inspect.signature(go_ForStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_selectstmt_is_not_abstract():
    assert not inspect.isabstract(go_SelectStmt)


def test_go_selectstmt_constructor_exists():
    assert callable(go_SelectStmt.__init__)


def test_go_selectstmt_constructor_args():
    sig = inspect.signature(go_SelectStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_switchstmt_is_not_abstract():
    assert not inspect.isabstract(go_SwitchStmt)


def test_go_switchstmt_constructor_exists():
    assert callable(go_SwitchStmt.__init__)


def test_go_switchstmt_constructor_args():
    sig = inspect.signature(go_SwitchStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_ifstmt_is_not_abstract():
    assert not inspect.isabstract(go_IfStmt)


def test_go_ifstmt_constructor_exists():
    assert callable(go_IfStmt.__init__)


def test_go_ifstmt_constructor_args():
    sig = inspect.signature(go_IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_receivertype_is_not_abstract():
    assert not inspect.isabstract(go_ReceiverType)


def test_go_receivertype_constructor_exists():
    assert callable(go_ReceiverType.__init__)


def test_go_receivertype_constructor_args():
    sig = inspect.signature(go_ReceiverType.__init__)
    params = list(sig.parameters.keys())



def test_go_decimals_is_not_abstract():
    assert not inspect.isabstract(go_decimals)


def test_go_decimals_constructor_exists():
    assert callable(go_decimals.__init__)


def test_go_decimals_constructor_args():
    sig = inspect.signature(go_decimals.__init__)
    params = list(sig.parameters.keys())
    assert "DECIMAL_DIGIT" in params, "Missing parameter 'DECIMAL_DIGIT'"

def test_go_decimals_has_DECIMAL_DIGIT():
    assert hasattr(go_decimals, "DECIMAL_DIGIT")
    descriptor = None
    for klass in go_decimals.__mro__:
        if "DECIMAL_DIGIT" in klass.__dict__:
            descriptor = klass.__dict__["DECIMAL_DIGIT"]
            break
    assert isinstance(descriptor, property)



def test_go_slice_is_not_abstract():
    assert not inspect.isabstract(go_Slice)


def test_go_slice_constructor_exists():
    assert callable(go_Slice.__init__)


def test_go_slice_constructor_args():
    sig = inspect.signature(go_Slice.__init__)
    params = list(sig.parameters.keys())



def test_go_binary_op_is_not_abstract():
    assert not inspect.isabstract(go_binary_op)


def test_go_binary_op_constructor_exists():
    assert callable(go_binary_op.__init__)


def test_go_binary_op_constructor_args():
    sig = inspect.signature(go_binary_op.__init__)
    params = list(sig.parameters.keys())
    assert "mul_op" in params, "Missing parameter 'mul_op'"
    assert "rel_op" in params, "Missing parameter 'rel_op'"
    assert "add_op" in params, "Missing parameter 'add_op'"

def test_go_binary_op_has_mul_op():
    assert hasattr(go_binary_op, "mul_op")
    descriptor = None
    for klass in go_binary_op.__mro__:
        if "mul_op" in klass.__dict__:
            descriptor = klass.__dict__["mul_op"]
            break
    assert isinstance(descriptor, property)

def test_go_binary_op_has_rel_op():
    assert hasattr(go_binary_op, "rel_op")
    descriptor = None
    for klass in go_binary_op.__mro__:
        if "rel_op" in klass.__dict__:
            descriptor = klass.__dict__["rel_op"]
            break
    assert isinstance(descriptor, property)

def test_go_binary_op_has_add_op():
    assert hasattr(go_binary_op, "add_op")
    descriptor = None
    for klass in go_binary_op.__mro__:
        if "add_op" in klass.__dict__:
            descriptor = klass.__dict__["add_op"]
            break
    assert isinstance(descriptor, property)



def test_go_expressionlinha_is_not_abstract():
    assert not inspect.isabstract(go_ExpressionLinha)


def test_go_expressionlinha_constructor_exists():
    assert callable(go_ExpressionLinha.__init__)


def test_go_expressionlinha_constructor_args():
    sig = inspect.signature(go_ExpressionLinha.__init__)
    params = list(sig.parameters.keys())



def test_go_unaryexpr_is_not_abstract():
    assert not inspect.isabstract(go_UnaryExpr)


def test_go_unaryexpr_constructor_exists():
    assert callable(go_UnaryExpr.__init__)


def test_go_unaryexpr_constructor_args():
    sig = inspect.signature(go_UnaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "unary_op" in params, "Missing parameter 'unary_op'"

def test_go_unaryexpr_has_unary_op():
    assert hasattr(go_UnaryExpr, "unary_op")
    descriptor = None
    for klass in go_UnaryExpr.__mro__:
        if "unary_op" in klass.__dict__:
            descriptor = klass.__dict__["unary_op"]
            break
    assert isinstance(descriptor, property)



def test_go_arguments_is_not_abstract():
    assert not inspect.isabstract(go_Arguments)


def test_go_arguments_constructor_exists():
    assert callable(go_Arguments.__init__)


def test_go_arguments_constructor_args():
    sig = inspect.signature(go_Arguments.__init__)
    params = list(sig.parameters.keys())



def test_go_methodexpr_is_not_abstract():
    assert not inspect.isabstract(go_MethodExpr)


def test_go_methodexpr_constructor_exists():
    assert callable(go_MethodExpr.__init__)


def test_go_methodexpr_constructor_args():
    sig = inspect.signature(go_MethodExpr.__init__)
    params = list(sig.parameters.keys())



def test_go_conversion_is_not_abstract():
    assert not inspect.isabstract(go_Conversion)


def test_go_conversion_constructor_exists():
    assert callable(go_Conversion.__init__)


def test_go_conversion_constructor_args():
    sig = inspect.signature(go_Conversion.__init__)
    params = list(sig.parameters.keys())



def test_go_primaryexprlinha_is_not_abstract():
    assert not inspect.isabstract(go_PrimaryExprLinha)


def test_go_primaryexprlinha_constructor_exists():
    assert callable(go_PrimaryExprLinha.__init__)


def test_go_primaryexprlinha_constructor_args():
    sig = inspect.signature(go_PrimaryExprLinha.__init__)
    params = list(sig.parameters.keys())



def test_go_primaryexpr_is_not_abstract():
    assert not inspect.isabstract(go_PrimaryExpr)


def test_go_primaryexpr_constructor_exists():
    assert callable(go_PrimaryExpr.__init__)


def test_go_primaryexpr_constructor_args():
    sig = inspect.signature(go_PrimaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_go_fieldname_is_not_abstract():
    assert not inspect.isabstract(go_FieldName)


def test_go_fieldname_constructor_exists():
    assert callable(go_FieldName.__init__)


def test_go_fieldname_constructor_args():
    sig = inspect.signature(go_FieldName.__init__)
    params = list(sig.parameters.keys())



def test_go_index_is_not_abstract():
    assert not inspect.isabstract(go_Index)


def test_go_index_constructor_exists():
    assert callable(go_Index.__init__)


def test_go_index_constructor_args():
    sig = inspect.signature(go_Index.__init__)
    params = list(sig.parameters.keys())



def test_go_typeassertion_is_not_abstract():
    assert not inspect.isabstract(go_TypeAssertion)


def test_go_typeassertion_constructor_exists():
    assert callable(go_TypeAssertion.__init__)


def test_go_typeassertion_constructor_args():
    sig = inspect.signature(go_TypeAssertion.__init__)
    params = list(sig.parameters.keys())



def test_go_selector_is_not_abstract():
    assert not inspect.isabstract(go_Selector)


def test_go_selector_constructor_exists():
    assert callable(go_Selector.__init__)


def test_go_selector_constructor_args():
    sig = inspect.signature(go_Selector.__init__)
    params = list(sig.parameters.keys())



def test_go_cochetes_is_not_abstract():
    assert not inspect.isabstract(go_cochetes)


def test_go_cochetes_constructor_exists():
    assert callable(go_cochetes.__init__)


def test_go_cochetes_constructor_args():
    sig = inspect.signature(go_cochetes.__init__)
    params = list(sig.parameters.keys())



def test_go_ponto_is_not_abstract():
    assert not inspect.isabstract(go_ponto)


def test_go_ponto_constructor_exists():
    assert callable(go_ponto.__init__)


def test_go_ponto_constructor_args():
    sig = inspect.signature(go_ponto.__init__)
    params = list(sig.parameters.keys())



def test_go_literaltypelinha_is_not_abstract():
    assert not inspect.isabstract(go_LiteralTypeLinha)


def test_go_literaltypelinha_constructor_exists():
    assert callable(go_LiteralTypeLinha.__init__)


def test_go_literaltypelinha_constructor_args():
    sig = inspect.signature(go_LiteralTypeLinha.__init__)
    params = list(sig.parameters.keys())



def test_go_literalvalue_is_not_abstract():
    assert not inspect.isabstract(go_LiteralValue)


def test_go_literalvalue_constructor_exists():
    assert callable(go_LiteralValue.__init__)


def test_go_literalvalue_constructor_args():
    sig = inspect.signature(go_LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_go_literaltype_is_not_abstract():
    assert not inspect.isabstract(go_LiteralType)


def test_go_literaltype_constructor_exists():
    assert callable(go_LiteralType.__init__)


def test_go_literaltype_constructor_args():
    sig = inspect.signature(go_LiteralType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_go_functionlit_is_not_abstract():
    assert not inspect.isabstract(go_FunctionLit)


def test_go_functionlit_constructor_exists():
    assert callable(go_FunctionLit.__init__)


def test_go_functionlit_constructor_args():
    sig = inspect.signature(go_FunctionLit.__init__)
    params = list(sig.parameters.keys())



def test_go_compositelit_is_not_abstract():
    assert not inspect.isabstract(go_CompositeLit)


def test_go_compositelit_constructor_exists():
    assert callable(go_CompositeLit.__init__)


def test_go_compositelit_constructor_args():
    sig = inspect.signature(go_CompositeLit.__init__)
    params = list(sig.parameters.keys())



def test_go_packagename_is_not_abstract():
    assert not inspect.isabstract(go_PackageName)


def test_go_packagename_constructor_exists():
    assert callable(go_PackageName.__init__)


def test_go_packagename_constructor_args():
    sig = inspect.signature(go_PackageName.__init__)
    params = list(sig.parameters.keys())



def test_operandname_is_not_abstract():
    assert not inspect.isabstract(OperandName)


def test_operandname_constructor_exists():
    assert callable(OperandName.__init__)


def test_operandname_constructor_args():
    sig = inspect.signature(OperandName.__init__)
    params = list(sig.parameters.keys())



def test_go_key_is_not_abstract():
    assert not inspect.isabstract(go_Key)


def test_go_key_constructor_exists():
    assert callable(go_Key.__init__)


def test_go_key_constructor_args():
    sig = inspect.signature(go_Key.__init__)
    params = list(sig.parameters.keys())



def test_go_element_is_not_abstract():
    assert not inspect.isabstract(go_Element)


def test_go_element_constructor_exists():
    assert callable(go_Element.__init__)


def test_go_element_constructor_args():
    sig = inspect.signature(go_Element.__init__)
    params = list(sig.parameters.keys())



def test_go_keyedelement_is_not_abstract():
    assert not inspect.isabstract(go_KeyedElement)


def test_go_keyedelement_constructor_exists():
    assert callable(go_KeyedElement.__init__)


def test_go_keyedelement_constructor_args():
    sig = inspect.signature(go_KeyedElement.__init__)
    params = list(sig.parameters.keys())



def test_go_elementlist_is_not_abstract():
    assert not inspect.isabstract(go_ElementList)


def test_go_elementlist_constructor_exists():
    assert callable(go_ElementList.__init__)


def test_go_elementlist_constructor_args():
    sig = inspect.signature(go_ElementList.__init__)
    params = list(sig.parameters.keys())



def test_go_methoddecl_is_not_abstract():
    assert not inspect.isabstract(go_MethodDecl)


def test_go_methoddecl_constructor_exists():
    assert callable(go_MethodDecl.__init__)


def test_go_methoddecl_constructor_args():
    sig = inspect.signature(go_MethodDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_functiondecl_is_not_abstract():
    assert not inspect.isabstract(go_FunctionDecl)


def test_go_functiondecl_constructor_exists():
    assert callable(go_FunctionDecl.__init__)


def test_go_functiondecl_constructor_args():
    sig = inspect.signature(go_FunctionDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_shortvardecl_is_not_abstract():
    assert not inspect.isabstract(go_ShortVarDecl)


def test_go_shortvardecl_constructor_exists():
    assert callable(go_ShortVarDecl.__init__)


def test_go_shortvardecl_constructor_args():
    sig = inspect.signature(go_ShortVarDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_rune_lit_is_not_abstract():
    assert not inspect.isabstract(go_rune_lit)


def test_go_rune_lit_constructor_exists():
    assert callable(go_rune_lit.__init__)


def test_go_rune_lit_constructor_args():
    sig = inspect.signature(go_rune_lit.__init__)
    params = list(sig.parameters.keys())
    assert "unicode_value" in params, "Missing parameter 'unicode_value'"
    assert "byte_value" in params, "Missing parameter 'byte_value'"

def test_go_rune_lit_has_unicode_value():
    assert hasattr(go_rune_lit, "unicode_value")
    descriptor = None
    for klass in go_rune_lit.__mro__:
        if "unicode_value" in klass.__dict__:
            descriptor = klass.__dict__["unicode_value"]
            break
    assert isinstance(descriptor, property)

def test_go_rune_lit_has_byte_value():
    assert hasattr(go_rune_lit, "byte_value")
    descriptor = None
    for klass in go_rune_lit.__mro__:
        if "byte_value" in klass.__dict__:
            descriptor = klass.__dict__["byte_value"]
            break
    assert isinstance(descriptor, property)



def test_go_float_lit_is_not_abstract():
    assert not inspect.isabstract(go_float_lit)


def test_go_float_lit_constructor_exists():
    assert callable(go_float_lit.__init__)


def test_go_float_lit_constructor_args():
    sig = inspect.signature(go_float_lit.__init__)
    params = list(sig.parameters.keys())



def test_go_basiclit_is_not_abstract():
    assert not inspect.isabstract(go_BasicLit)


def test_go_basiclit_constructor_exists():
    assert callable(go_BasicLit.__init__)


def test_go_basiclit_constructor_args():
    sig = inspect.signature(go_BasicLit.__init__)
    params = list(sig.parameters.keys())
    assert "int_lit" in params, "Missing parameter 'int_lit'"

def test_go_basiclit_has_int_lit():
    assert hasattr(go_BasicLit, "int_lit")
    descriptor = None
    for klass in go_BasicLit.__mro__:
        if "int_lit" in klass.__dict__:
            descriptor = klass.__dict__["int_lit"]
            break
    assert isinstance(descriptor, property)



def test_go_operandname_is_not_abstract():
    assert not inspect.isabstract(go_OperandName)


def test_go_operandname_constructor_exists():
    assert callable(go_OperandName.__init__)


def test_go_operandname_constructor_args():
    sig = inspect.signature(go_OperandName.__init__)
    params = list(sig.parameters.keys())



def test_go_literal_is_not_abstract():
    assert not inspect.isabstract(go_Literal)


def test_go_literal_constructor_exists():
    assert callable(go_Literal.__init__)


def test_go_literal_constructor_args():
    sig = inspect.signature(go_Literal.__init__)
    params = list(sig.parameters.keys())



def test_go_operand_is_not_abstract():
    assert not inspect.isabstract(go_Operand)


def test_go_operand_constructor_exists():
    assert callable(go_Operand.__init__)


def test_go_operand_constructor_args():
    sig = inspect.signature(go_Operand.__init__)
    params = list(sig.parameters.keys())



def test_go_expressionlist_is_not_abstract():
    assert not inspect.isabstract(go_ExpressionList)


def test_go_expressionlist_constructor_exists():
    assert callable(go_ExpressionList.__init__)


def test_go_expressionlist_constructor_args():
    sig = inspect.signature(go_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_go_constspec_is_not_abstract():
    assert not inspect.isabstract(go_ConstSpec)


def test_go_constspec_constructor_exists():
    assert callable(go_ConstSpec.__init__)


def test_go_constspec_constructor_args():
    sig = inspect.signature(go_ConstSpec.__init__)
    params = list(sig.parameters.keys())



def test_go_receiver_is_not_abstract():
    assert not inspect.isabstract(go_Receiver)


def test_go_receiver_constructor_exists():
    assert callable(go_Receiver.__init__)


def test_go_receiver_constructor_args():
    sig = inspect.signature(go_Receiver.__init__)
    params = list(sig.parameters.keys())



def test_go_functionbody_is_not_abstract():
    assert not inspect.isabstract(go_FunctionBody)


def test_go_functionbody_constructor_exists():
    assert callable(go_FunctionBody.__init__)


def test_go_functionbody_constructor_args():
    sig = inspect.signature(go_FunctionBody.__init__)
    params = list(sig.parameters.keys())



def test_go_functionname_is_not_abstract():
    assert not inspect.isabstract(go_FunctionName)


def test_go_functionname_constructor_exists():
    assert callable(go_FunctionName.__init__)


def test_go_functionname_constructor_args():
    sig = inspect.signature(go_FunctionName.__init__)
    params = list(sig.parameters.keys())



def test_go_varspec_is_not_abstract():
    assert not inspect.isabstract(go_VarSpec)


def test_go_varspec_constructor_exists():
    assert callable(go_VarSpec.__init__)


def test_go_varspec_constructor_args():
    sig = inspect.signature(go_VarSpec.__init__)
    params = list(sig.parameters.keys())



def test_typespec_is_not_abstract():
    assert not inspect.isabstract(TypeSpec)


def test_typespec_constructor_exists():
    assert callable(TypeSpec.__init__)


def test_typespec_constructor_args():
    sig = inspect.signature(TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_go_typedef_is_not_abstract():
    assert not inspect.isabstract(go_TypeDef)


def test_go_typedef_constructor_exists():
    assert callable(go_TypeDef.__init__)


def test_go_typedef_constructor_args():
    sig = inspect.signature(go_TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_go_aliasdecl_is_not_abstract():
    assert not inspect.isabstract(go_AliasDecl)


def test_go_aliasdecl_constructor_exists():
    assert callable(go_AliasDecl.__init__)


def test_go_aliasdecl_constructor_args():
    sig = inspect.signature(go_AliasDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_typespec_is_not_abstract():
    assert not inspect.isabstract(go_TypeSpec)


def test_go_typespec_constructor_exists():
    assert callable(go_TypeSpec.__init__)


def test_go_typespec_constructor_args():
    sig = inspect.signature(go_TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_go_keytype_is_not_abstract():
    assert not inspect.isabstract(go_KeyType)


def test_go_keytype_constructor_exists():
    assert callable(go_KeyType.__init__)


def test_go_keytype_constructor_args():
    sig = inspect.signature(go_KeyType.__init__)
    params = list(sig.parameters.keys())



def test_go_interfacetypename_is_not_abstract():
    assert not inspect.isabstract(go_InterfaceTypeName)


def test_go_interfacetypename_constructor_exists():
    assert callable(go_InterfaceTypeName.__init__)


def test_go_interfacetypename_constructor_args():
    sig = inspect.signature(go_InterfaceTypeName.__init__)
    params = list(sig.parameters.keys())



def test_go_methodname_is_not_abstract():
    assert not inspect.isabstract(go_MethodName)


def test_go_methodname_constructor_exists():
    assert callable(go_MethodName.__init__)


def test_go_methodname_constructor_args():
    sig = inspect.signature(go_MethodName.__init__)
    params = list(sig.parameters.keys())



def test_go_methodspec_is_not_abstract():
    assert not inspect.isabstract(go_MethodSpec)


def test_go_methodspec_constructor_exists():
    assert callable(go_MethodSpec.__init__)


def test_go_methodspec_constructor_args():
    sig = inspect.signature(go_MethodSpec.__init__)
    params = list(sig.parameters.keys())



def test_go_topleveldecllinha_is_not_abstract():
    assert not inspect.isabstract(go_topLevelDeclLinha)


def test_go_topleveldecllinha_constructor_exists():
    assert callable(go_topLevelDeclLinha.__init__)


def test_go_topleveldecllinha_constructor_args():
    sig = inspect.signature(go_topLevelDeclLinha.__init__)
    params = list(sig.parameters.keys())



def test_go_vardecl_is_not_abstract():
    assert not inspect.isabstract(go_VarDecl)


def test_go_vardecl_constructor_exists():
    assert callable(go_VarDecl.__init__)


def test_go_vardecl_constructor_args():
    sig = inspect.signature(go_VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_typedecl_is_not_abstract():
    assert not inspect.isabstract(go_TypeDecl)


def test_go_typedecl_constructor_exists():
    assert callable(go_TypeDecl.__init__)


def test_go_typedecl_constructor_args():
    sig = inspect.signature(go_TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_constdecl_is_not_abstract():
    assert not inspect.isabstract(go_ConstDecl)


def test_go_constdecl_constructor_exists():
    assert callable(go_ConstDecl.__init__)


def test_go_constdecl_constructor_args():
    sig = inspect.signature(go_ConstDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_declaration_is_not_abstract():
    assert not inspect.isabstract(go_Declaration)


def test_go_declaration_constructor_exists():
    assert callable(go_Declaration.__init__)


def test_go_declaration_constructor_args():
    sig = inspect.signature(go_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_go_statement_is_not_abstract():
    assert not inspect.isabstract(go_Statement)


def test_go_statement_constructor_exists():
    assert callable(go_Statement.__init__)


def test_go_statement_constructor_args():
    sig = inspect.signature(go_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "FallthroughStmt" in params, "Missing parameter 'FallthroughStmt'"

def test_go_statement_has_FallthroughStmt():
    assert hasattr(go_Statement, "FallthroughStmt")
    descriptor = None
    for klass in go_Statement.__mro__:
        if "FallthroughStmt" in klass.__dict__:
            descriptor = klass.__dict__["FallthroughStmt"]
            break
    assert isinstance(descriptor, property)



def test_go_statementlist_is_not_abstract():
    assert not inspect.isabstract(go_StatementList)


def test_go_statementlist_constructor_exists():
    assert callable(go_StatementList.__init__)


def test_go_statementlist_constructor_args():
    sig = inspect.signature(go_StatementList.__init__)
    params = list(sig.parameters.keys())



def test_go_block_is_not_abstract():
    assert not inspect.isabstract(go_Block)


def test_go_block_constructor_exists():
    assert callable(go_Block.__init__)


def test_go_block_constructor_args():
    sig = inspect.signature(go_Block.__init__)
    params = list(sig.parameters.keys())



def test_go_result_is_not_abstract():
    assert not inspect.isabstract(go_Result)


def test_go_result_constructor_exists():
    assert callable(go_Result.__init__)


def test_go_result_constructor_args():
    sig = inspect.signature(go_Result.__init__)
    params = list(sig.parameters.keys())



def test_go_signature_is_not_abstract():
    assert not inspect.isabstract(go_Signature)


def test_go_signature_constructor_exists():
    assert callable(go_Signature.__init__)


def test_go_signature_constructor_args():
    sig = inspect.signature(go_Signature.__init__)
    params = list(sig.parameters.keys())



def test_go_string_lit_is_not_abstract():
    assert not inspect.isabstract(go_string_lit)


def test_go_string_lit_constructor_exists():
    assert callable(go_string_lit.__init__)


def test_go_string_lit_constructor_args():
    sig = inspect.signature(go_string_lit.__init__)
    params = list(sig.parameters.keys())
    assert "interpreted_string_lit" in params, "Missing parameter 'interpreted_string_lit'"
    assert "raw_string_lit" in params, "Missing parameter 'raw_string_lit'"

def test_go_string_lit_has_interpreted_string_lit():
    assert hasattr(go_string_lit, "interpreted_string_lit")
    descriptor = None
    for klass in go_string_lit.__mro__:
        if "interpreted_string_lit" in klass.__dict__:
            descriptor = klass.__dict__["interpreted_string_lit"]
            break
    assert isinstance(descriptor, property)

def test_go_string_lit_has_raw_string_lit():
    assert hasattr(go_string_lit, "raw_string_lit")
    descriptor = None
    for klass in go_string_lit.__mro__:
        if "raw_string_lit" in klass.__dict__:
            descriptor = klass.__dict__["raw_string_lit"]
            break
    assert isinstance(descriptor, property)



def test_go_tag_is_not_abstract():
    assert not inspect.isabstract(go_Tag)


def test_go_tag_constructor_exists():
    assert callable(go_Tag.__init__)


def test_go_tag_constructor_args():
    sig = inspect.signature(go_Tag.__init__)
    params = list(sig.parameters.keys())



def test_go_embeddedfield_is_not_abstract():
    assert not inspect.isabstract(go_EmbeddedField)


def test_go_embeddedfield_constructor_exists():
    assert callable(go_EmbeddedField.__init__)


def test_go_embeddedfield_constructor_args():
    sig = inspect.signature(go_EmbeddedField.__init__)
    params = list(sig.parameters.keys())



def test_go_identifierlist_is_not_abstract():
    assert not inspect.isabstract(go_IdentifierList)


def test_go_identifierlist_constructor_exists():
    assert callable(go_IdentifierList.__init__)


def test_go_identifierlist_constructor_args():
    sig = inspect.signature(go_IdentifierList.__init__)
    params = list(sig.parameters.keys())



def test_go_fielddecl_is_not_abstract():
    assert not inspect.isabstract(go_FieldDecl)


def test_go_fielddecl_constructor_exists():
    assert callable(go_FieldDecl.__init__)


def test_go_fielddecl_constructor_args():
    sig = inspect.signature(go_FieldDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_parameterdecl_is_not_abstract():
    assert not inspect.isabstract(go_ParameterDecl)


def test_go_parameterdecl_constructor_exists():
    assert callable(go_ParameterDecl.__init__)


def test_go_parameterdecl_constructor_args():
    sig = inspect.signature(go_ParameterDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_parameterlist_is_not_abstract():
    assert not inspect.isabstract(go_ParameterList)


def test_go_parameterlist_constructor_exists():
    assert callable(go_ParameterList.__init__)


def test_go_parameterlist_constructor_args():
    sig = inspect.signature(go_ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_receiver_is_not_abstract():
    assert not inspect.isabstract(Receiver)


def test_receiver_constructor_exists():
    assert callable(Receiver.__init__)


def test_receiver_constructor_args():
    sig = inspect.signature(Receiver.__init__)
    params = list(sig.parameters.keys())



def test_go_parameters_is_not_abstract():
    assert not inspect.isabstract(go_Parameters)


def test_go_parameters_constructor_exists():
    assert callable(go_Parameters.__init__)


def test_go_parameters_constructor_args():
    sig = inspect.signature(go_Parameters.__init__)
    params = list(sig.parameters.keys())



def test_go_interfacetype_is_not_abstract():
    assert not inspect.isabstract(go_InterfaceType)


def test_go_interfacetype_constructor_exists():
    assert callable(go_InterfaceType.__init__)


def test_go_interfacetype_constructor_args():
    sig = inspect.signature(go_InterfaceType.__init__)
    params = list(sig.parameters.keys())



def test_go_functiontype_is_not_abstract():
    assert not inspect.isabstract(go_FunctionType)


def test_go_functiontype_constructor_exists():
    assert callable(go_FunctionType.__init__)


def test_go_functiontype_constructor_args():
    sig = inspect.signature(go_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_go_pointertype_is_not_abstract():
    assert not inspect.isabstract(go_PointerType)


def test_go_pointertype_constructor_exists():
    assert callable(go_PointerType.__init__)


def test_go_pointertype_constructor_args():
    sig = inspect.signature(go_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_go_structtype_is_not_abstract():
    assert not inspect.isabstract(go_StructType)


def test_go_structtype_constructor_exists():
    assert callable(go_StructType.__init__)


def test_go_structtype_constructor_args():
    sig = inspect.signature(go_StructType.__init__)
    params = list(sig.parameters.keys())



def test_go_typelitlinha_is_not_abstract():
    assert not inspect.isabstract(go_TypeLitLinha)


def test_go_typelitlinha_constructor_exists():
    assert callable(go_TypeLitLinha.__init__)


def test_go_typelitlinha_constructor_args():
    sig = inspect.signature(go_TypeLitLinha.__init__)
    params = list(sig.parameters.keys())



def test_go_qualifiedident_is_not_abstract():
    assert not inspect.isabstract(go_QualifiedIdent)


def test_go_qualifiedident_constructor_exists():
    assert callable(go_QualifiedIdent.__init__)


def test_go_qualifiedident_constructor_args():
    sig = inspect.signature(go_QualifiedIdent.__init__)
    params = list(sig.parameters.keys())



def test_go_typenamelinha_is_not_abstract():
    assert not inspect.isabstract(go_TypeNameLinha)


def test_go_typenamelinha_constructor_exists():
    assert callable(go_TypeNameLinha.__init__)


def test_go_typenamelinha_constructor_args():
    sig = inspect.signature(go_TypeNameLinha.__init__)
    params = list(sig.parameters.keys())



def test_go_identifier_is_not_abstract():
    assert not inspect.isabstract(go_identifier)


def test_go_identifier_constructor_exists():
    assert callable(go_identifier.__init__)


def test_go_identifier_constructor_args():
    sig = inspect.signature(go_identifier.__init__)
    params = list(sig.parameters.keys())
    assert "LETTER" in params, "Missing parameter 'LETTER'"
    assert "DECIMAL_DIGIT" in params, "Missing parameter 'DECIMAL_DIGIT'"

def test_go_identifier_has_LETTER():
    assert hasattr(go_identifier, "LETTER")
    descriptor = None
    for klass in go_identifier.__mro__:
        if "LETTER" in klass.__dict__:
            descriptor = klass.__dict__["LETTER"]
            break
    assert isinstance(descriptor, property)

def test_go_identifier_has_DECIMAL_DIGIT():
    assert hasattr(go_identifier, "DECIMAL_DIGIT")
    descriptor = None
    for klass in go_identifier.__mro__:
        if "DECIMAL_DIGIT" in klass.__dict__:
            descriptor = klass.__dict__["DECIMAL_DIGIT"]
            break
    assert isinstance(descriptor, property)



def test_go_typelit_is_not_abstract():
    assert not inspect.isabstract(go_TypeLit)


def test_go_typelit_constructor_exists():
    assert callable(go_TypeLit.__init__)


def test_go_typelit_constructor_args():
    sig = inspect.signature(go_TypeLit.__init__)
    params = list(sig.parameters.keys())



def test_go_expression_is_not_abstract():
    assert not inspect.isabstract(go_Expression)


def test_go_expression_constructor_exists():
    assert callable(go_Expression.__init__)


def test_go_expression_constructor_args():
    sig = inspect.signature(go_Expression.__init__)
    params = list(sig.parameters.keys())



def test_go_elementtype_is_not_abstract():
    assert not inspect.isabstract(go_ElementType)


def test_go_elementtype_constructor_exists():
    assert callable(go_ElementType.__init__)


def test_go_elementtype_constructor_args():
    sig = inspect.signature(go_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_go_arraylength_is_not_abstract():
    assert not inspect.isabstract(go_ArrayLength)


def test_go_arraylength_constructor_exists():
    assert callable(go_ArrayLength.__init__)


def test_go_arraylength_constructor_args():
    sig = inspect.signature(go_ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_go_channeltype_is_not_abstract():
    assert not inspect.isabstract(go_ChannelType)


def test_go_channeltype_constructor_exists():
    assert callable(go_ChannelType.__init__)


def test_go_channeltype_constructor_args():
    sig = inspect.signature(go_ChannelType.__init__)
    params = list(sig.parameters.keys())



def test_go_maptype_is_not_abstract():
    assert not inspect.isabstract(go_MapType)


def test_go_maptype_constructor_exists():
    assert callable(go_MapType.__init__)


def test_go_maptype_constructor_args():
    sig = inspect.signature(go_MapType.__init__)
    params = list(sig.parameters.keys())



def test_go_typename_is_not_abstract():
    assert not inspect.isabstract(go_TypeName)


def test_go_typename_constructor_exists():
    assert callable(go_TypeName.__init__)


def test_go_typename_constructor_args():
    sig = inspect.signature(go_TypeName.__init__)
    params = list(sig.parameters.keys())



def test_go_type_is_not_abstract():
    assert not inspect.isabstract(go_Type)


def test_go_type_constructor_exists():
    assert callable(go_Type.__init__)


def test_go_type_constructor_args():
    sig = inspect.signature(go_Type.__init__)
    params = list(sig.parameters.keys())



def test_go_topleveldecl_is_not_abstract():
    assert not inspect.isabstract(go_TopLevelDecl)


def test_go_topleveldecl_constructor_exists():
    assert callable(go_TopLevelDecl.__init__)


def test_go_topleveldecl_constructor_args():
    sig = inspect.signature(go_TopLevelDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_importdecl_is_not_abstract():
    assert not inspect.isabstract(go_ImportDecl)


def test_go_importdecl_constructor_exists():
    assert callable(go_ImportDecl.__init__)


def test_go_importdecl_constructor_args():
    sig = inspect.signature(go_ImportDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_packageclause_is_not_abstract():
    assert not inspect.isabstract(go_PackageClause)


def test_go_packageclause_constructor_exists():
    assert callable(go_PackageClause.__init__)


def test_go_packageclause_constructor_args():
    sig = inspect.signature(go_PackageClause.__init__)
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
go_SouceFile_strategy = st.builds(
    go_SouceFile,
)
float_lit_strategy = st.builds(
    float_lit,
)
go_ImportPath_strategy = st.builds(
    go_ImportPath,
)
go_ImportSpec_strategy = st.builds(
    go_ImportSpec,
)
go_imaginary_lit_strategy = st.builds(
    go_imaginary_lit,
)
go_exponent_strategy = st.builds(
    go_exponent,
)
go_RecvExpr_strategy = st.builds(
    go_RecvExpr,
)
go_RecvStmt_strategy = st.builds(
    go_RecvStmt,
)
go_CommCase_strategy = st.builds(
    go_CommCase,
)
go_CommClause_strategy = st.builds(
    go_CommClause,
)
go_InitStmt_strategy = st.builds(
    go_InitStmt,
)
go_PostStmt_strategy = st.builds(
    go_PostStmt,
)
go_TypeCaseClause_strategy = st.builds(
    go_TypeCaseClause,
)
go_TypeSwitchGuard_strategy = st.builds(
    go_TypeSwitchGuard,
)
go_ExprSwitchCase_strategy = st.builds(
    go_ExprSwitchCase,
)
go_ExprCaseClause_strategy = st.builds(
    go_ExprCaseClause,
)
go_switch_stmt_linha_strategy = st.builds(
    go_switch_stmt_linha,
)
go_RangeClause_strategy = st.builds(
    go_RangeClause,
)
go_ForClause_strategy = st.builds(
    go_ForClause,
)
go_Condition_strategy = st.builds(
    go_Condition,
)
go_TypeList_strategy = st.builds(
    go_TypeList,
)
go_TypeSwitchCase_strategy = st.builds(
    go_TypeSwitchCase,
)
go_Channel_strategy = st.builds(
    go_Channel,
)
go_Label_strategy = st.builds(
    go_Label,
)
go_Assignment_strategy = st.builds(
    go_Assignment,
    assign_op=
        safe_text
)
go_IncDecStmt_strategy = st.builds(
    go_IncDecStmt,
)
go_SendStmt_strategy = st.builds(
    go_SendStmt,
)
go_ExpressionStmt_strategy = st.builds(
    go_ExpressionStmt,
)
go_GotoStmt_strategy = st.builds(
    go_GotoStmt,
)
go_ContinueStmt_strategy = st.builds(
    go_ContinueStmt,
)
go_BreakStmt_strategy = st.builds(
    go_BreakStmt,
)
go_ReturnStmt_strategy = st.builds(
    go_ReturnStmt,
)
go_GoStmt_strategy = st.builds(
    go_GoStmt,
)
go_LabeledStmt_strategy = st.builds(
    go_LabeledStmt,
)
SwitchStmt_strategy = st.builds(
    SwitchStmt,
)
go_SimpleStmt_strategy = st.builds(
    go_SimpleStmt,
    EmptyStmt=
        safe_text
)
go_DeferStmt_strategy = st.builds(
    go_DeferStmt,
)
go_ForStmt_strategy = st.builds(
    go_ForStmt,
)
go_SelectStmt_strategy = st.builds(
    go_SelectStmt,
)
go_SwitchStmt_strategy = st.builds(
    go_SwitchStmt,
)
go_IfStmt_strategy = st.builds(
    go_IfStmt,
)
go_ReceiverType_strategy = st.builds(
    go_ReceiverType,
)
go_decimals_strategy = st.builds(
    go_decimals,
    DECIMAL_DIGIT=
        safe_text
)
go_Slice_strategy = st.builds(
    go_Slice,
)
go_binary_op_strategy = st.builds(
    go_binary_op,
    mul_op=
        safe_text,
    rel_op=
        safe_text,
    add_op=
        safe_text
)
go_ExpressionLinha_strategy = st.builds(
    go_ExpressionLinha,
)
go_UnaryExpr_strategy = st.builds(
    go_UnaryExpr,
    unary_op=
        safe_text
)
go_Arguments_strategy = st.builds(
    go_Arguments,
)
go_MethodExpr_strategy = st.builds(
    go_MethodExpr,
)
go_Conversion_strategy = st.builds(
    go_Conversion,
)
go_PrimaryExprLinha_strategy = st.builds(
    go_PrimaryExprLinha,
)
go_PrimaryExpr_strategy = st.builds(
    go_PrimaryExpr,
)
go_FieldName_strategy = st.builds(
    go_FieldName,
)
go_Index_strategy = st.builds(
    go_Index,
)
go_TypeAssertion_strategy = st.builds(
    go_TypeAssertion,
)
go_Selector_strategy = st.builds(
    go_Selector,
)
go_cochetes_strategy = st.builds(
    go_cochetes,
)
go_ponto_strategy = st.builds(
    go_ponto,
)
go_LiteralTypeLinha_strategy = st.builds(
    go_LiteralTypeLinha,
)
go_LiteralValue_strategy = st.builds(
    go_LiteralValue,
)
go_LiteralType_strategy = st.builds(
    go_LiteralType,
)
Literal_strategy = st.builds(
    Literal,
)
go_FunctionLit_strategy = st.builds(
    go_FunctionLit,
)
go_CompositeLit_strategy = st.builds(
    go_CompositeLit,
)
go_PackageName_strategy = st.builds(
    go_PackageName,
)
OperandName_strategy = st.builds(
    OperandName,
)
go_Key_strategy = st.builds(
    go_Key,
)
go_Element_strategy = st.builds(
    go_Element,
)
go_KeyedElement_strategy = st.builds(
    go_KeyedElement,
)
go_ElementList_strategy = st.builds(
    go_ElementList,
)
go_MethodDecl_strategy = st.builds(
    go_MethodDecl,
)
go_FunctionDecl_strategy = st.builds(
    go_FunctionDecl,
)
go_ShortVarDecl_strategy = st.builds(
    go_ShortVarDecl,
)
go_rune_lit_strategy = st.builds(
    go_rune_lit,
    unicode_value=
        safe_text,
    byte_value=
        safe_text
)
go_float_lit_strategy = st.builds(
    go_float_lit,
)
go_BasicLit_strategy = st.builds(
    go_BasicLit,
    int_lit=
        safe_text
)
go_OperandName_strategy = st.builds(
    go_OperandName,
)
go_Literal_strategy = st.builds(
    go_Literal,
)
go_Operand_strategy = st.builds(
    go_Operand,
)
go_ExpressionList_strategy = st.builds(
    go_ExpressionList,
)
go_ConstSpec_strategy = st.builds(
    go_ConstSpec,
)
go_Receiver_strategy = st.builds(
    go_Receiver,
)
go_FunctionBody_strategy = st.builds(
    go_FunctionBody,
)
go_FunctionName_strategy = st.builds(
    go_FunctionName,
)
go_VarSpec_strategy = st.builds(
    go_VarSpec,
)
TypeSpec_strategy = st.builds(
    TypeSpec,
)
go_TypeDef_strategy = st.builds(
    go_TypeDef,
)
go_AliasDecl_strategy = st.builds(
    go_AliasDecl,
)
go_TypeSpec_strategy = st.builds(
    go_TypeSpec,
)
go_KeyType_strategy = st.builds(
    go_KeyType,
)
go_InterfaceTypeName_strategy = st.builds(
    go_InterfaceTypeName,
)
go_MethodName_strategy = st.builds(
    go_MethodName,
)
go_MethodSpec_strategy = st.builds(
    go_MethodSpec,
)
go_topLevelDeclLinha_strategy = st.builds(
    go_topLevelDeclLinha,
)
go_VarDecl_strategy = st.builds(
    go_VarDecl,
)
go_TypeDecl_strategy = st.builds(
    go_TypeDecl,
)
go_ConstDecl_strategy = st.builds(
    go_ConstDecl,
)
go_Declaration_strategy = st.builds(
    go_Declaration,
)
go_Statement_strategy = st.builds(
    go_Statement,
    FallthroughStmt=
        safe_text
)
go_StatementList_strategy = st.builds(
    go_StatementList,
)
go_Block_strategy = st.builds(
    go_Block,
)
go_Result_strategy = st.builds(
    go_Result,
)
go_Signature_strategy = st.builds(
    go_Signature,
)
go_string_lit_strategy = st.builds(
    go_string_lit,
    interpreted_string_lit=
        safe_text,
    raw_string_lit=
        safe_text
)
go_Tag_strategy = st.builds(
    go_Tag,
)
go_EmbeddedField_strategy = st.builds(
    go_EmbeddedField,
)
go_IdentifierList_strategy = st.builds(
    go_IdentifierList,
)
go_FieldDecl_strategy = st.builds(
    go_FieldDecl,
)
go_ParameterDecl_strategy = st.builds(
    go_ParameterDecl,
)
go_ParameterList_strategy = st.builds(
    go_ParameterList,
)
Receiver_strategy = st.builds(
    Receiver,
)
go_Parameters_strategy = st.builds(
    go_Parameters,
)
go_InterfaceType_strategy = st.builds(
    go_InterfaceType,
)
go_FunctionType_strategy = st.builds(
    go_FunctionType,
)
go_PointerType_strategy = st.builds(
    go_PointerType,
)
go_StructType_strategy = st.builds(
    go_StructType,
)
go_TypeLitLinha_strategy = st.builds(
    go_TypeLitLinha,
)
go_QualifiedIdent_strategy = st.builds(
    go_QualifiedIdent,
)
go_TypeNameLinha_strategy = st.builds(
    go_TypeNameLinha,
)
go_identifier_strategy = st.builds(
    go_identifier,
    LETTER=
        safe_text,
    DECIMAL_DIGIT=
        safe_text
)
go_TypeLit_strategy = st.builds(
    go_TypeLit,
)
go_Expression_strategy = st.builds(
    go_Expression,
)
go_ElementType_strategy = st.builds(
    go_ElementType,
)
go_ArrayLength_strategy = st.builds(
    go_ArrayLength,
)
go_ChannelType_strategy = st.builds(
    go_ChannelType,
)
go_MapType_strategy = st.builds(
    go_MapType,
)
go_TypeName_strategy = st.builds(
    go_TypeName,
)
go_Type_strategy = st.builds(
    go_Type,
)
go_TopLevelDecl_strategy = st.builds(
    go_TopLevelDecl,
)
go_ImportDecl_strategy = st.builds(
    go_ImportDecl,
)
go_PackageClause_strategy = st.builds(
    go_PackageClause,
)

@given(instance=go_SouceFile_strategy)
@settings(max_examples=50)
def test_go_soucefile_instantiation(instance):
    assert isinstance(instance, go_SouceFile)

@given(instance=float_lit_strategy)
@settings(max_examples=50)
def test_float_lit_instantiation(instance):
    assert isinstance(instance, float_lit)

@given(instance=go_ImportPath_strategy)
@settings(max_examples=50)
def test_go_importpath_instantiation(instance):
    assert isinstance(instance, go_ImportPath)

@given(instance=go_ImportSpec_strategy)
@settings(max_examples=50)
def test_go_importspec_instantiation(instance):
    assert isinstance(instance, go_ImportSpec)

@given(instance=go_imaginary_lit_strategy)
@settings(max_examples=50)
def test_go_imaginary_lit_instantiation(instance):
    assert isinstance(instance, go_imaginary_lit)

@given(instance=go_exponent_strategy)
@settings(max_examples=50)
def test_go_exponent_instantiation(instance):
    assert isinstance(instance, go_exponent)

@given(instance=go_RecvExpr_strategy)
@settings(max_examples=50)
def test_go_recvexpr_instantiation(instance):
    assert isinstance(instance, go_RecvExpr)

@given(instance=go_RecvStmt_strategy)
@settings(max_examples=50)
def test_go_recvstmt_instantiation(instance):
    assert isinstance(instance, go_RecvStmt)

@given(instance=go_CommCase_strategy)
@settings(max_examples=50)
def test_go_commcase_instantiation(instance):
    assert isinstance(instance, go_CommCase)

@given(instance=go_CommClause_strategy)
@settings(max_examples=50)
def test_go_commclause_instantiation(instance):
    assert isinstance(instance, go_CommClause)

@given(instance=go_InitStmt_strategy)
@settings(max_examples=50)
def test_go_initstmt_instantiation(instance):
    assert isinstance(instance, go_InitStmt)

@given(instance=go_PostStmt_strategy)
@settings(max_examples=50)
def test_go_poststmt_instantiation(instance):
    assert isinstance(instance, go_PostStmt)

@given(instance=go_TypeCaseClause_strategy)
@settings(max_examples=50)
def test_go_typecaseclause_instantiation(instance):
    assert isinstance(instance, go_TypeCaseClause)

@given(instance=go_TypeSwitchGuard_strategy)
@settings(max_examples=50)
def test_go_typeswitchguard_instantiation(instance):
    assert isinstance(instance, go_TypeSwitchGuard)

@given(instance=go_ExprSwitchCase_strategy)
@settings(max_examples=50)
def test_go_exprswitchcase_instantiation(instance):
    assert isinstance(instance, go_ExprSwitchCase)

@given(instance=go_ExprCaseClause_strategy)
@settings(max_examples=50)
def test_go_exprcaseclause_instantiation(instance):
    assert isinstance(instance, go_ExprCaseClause)

@given(instance=go_switch_stmt_linha_strategy)
@settings(max_examples=50)
def test_go_switch_stmt_linha_instantiation(instance):
    assert isinstance(instance, go_switch_stmt_linha)

@given(instance=go_RangeClause_strategy)
@settings(max_examples=50)
def test_go_rangeclause_instantiation(instance):
    assert isinstance(instance, go_RangeClause)

@given(instance=go_ForClause_strategy)
@settings(max_examples=50)
def test_go_forclause_instantiation(instance):
    assert isinstance(instance, go_ForClause)

@given(instance=go_Condition_strategy)
@settings(max_examples=50)
def test_go_condition_instantiation(instance):
    assert isinstance(instance, go_Condition)

@given(instance=go_TypeList_strategy)
@settings(max_examples=50)
def test_go_typelist_instantiation(instance):
    assert isinstance(instance, go_TypeList)

@given(instance=go_TypeSwitchCase_strategy)
@settings(max_examples=50)
def test_go_typeswitchcase_instantiation(instance):
    assert isinstance(instance, go_TypeSwitchCase)

@given(instance=go_Channel_strategy)
@settings(max_examples=50)
def test_go_channel_instantiation(instance):
    assert isinstance(instance, go_Channel)

@given(instance=go_Label_strategy)
@settings(max_examples=50)
def test_go_label_instantiation(instance):
    assert isinstance(instance, go_Label)

@given(instance=go_Assignment_strategy)
@settings(max_examples=50)
def test_go_assignment_instantiation(instance):
    assert isinstance(instance, go_Assignment)



@given(instance=go_Assignment_strategy)
def test_go_assignment_assign_op_setter(instance):
    original = instance.assign_op
    instance.assign_op = original
    assert instance.assign_op == original

@given(instance=go_IncDecStmt_strategy)
@settings(max_examples=50)
def test_go_incdecstmt_instantiation(instance):
    assert isinstance(instance, go_IncDecStmt)

@given(instance=go_SendStmt_strategy)
@settings(max_examples=50)
def test_go_sendstmt_instantiation(instance):
    assert isinstance(instance, go_SendStmt)

@given(instance=go_ExpressionStmt_strategy)
@settings(max_examples=50)
def test_go_expressionstmt_instantiation(instance):
    assert isinstance(instance, go_ExpressionStmt)

@given(instance=go_GotoStmt_strategy)
@settings(max_examples=50)
def test_go_gotostmt_instantiation(instance):
    assert isinstance(instance, go_GotoStmt)

@given(instance=go_ContinueStmt_strategy)
@settings(max_examples=50)
def test_go_continuestmt_instantiation(instance):
    assert isinstance(instance, go_ContinueStmt)

@given(instance=go_BreakStmt_strategy)
@settings(max_examples=50)
def test_go_breakstmt_instantiation(instance):
    assert isinstance(instance, go_BreakStmt)

@given(instance=go_ReturnStmt_strategy)
@settings(max_examples=50)
def test_go_returnstmt_instantiation(instance):
    assert isinstance(instance, go_ReturnStmt)

@given(instance=go_GoStmt_strategy)
@settings(max_examples=50)
def test_go_gostmt_instantiation(instance):
    assert isinstance(instance, go_GoStmt)

@given(instance=go_LabeledStmt_strategy)
@settings(max_examples=50)
def test_go_labeledstmt_instantiation(instance):
    assert isinstance(instance, go_LabeledStmt)

@given(instance=SwitchStmt_strategy)
@settings(max_examples=50)
def test_switchstmt_instantiation(instance):
    assert isinstance(instance, SwitchStmt)

@given(instance=go_SimpleStmt_strategy)
@settings(max_examples=50)
def test_go_simplestmt_instantiation(instance):
    assert isinstance(instance, go_SimpleStmt)



@given(instance=go_SimpleStmt_strategy)
def test_go_simplestmt_EmptyStmt_setter(instance):
    original = instance.EmptyStmt
    instance.EmptyStmt = original
    assert instance.EmptyStmt == original

@given(instance=go_DeferStmt_strategy)
@settings(max_examples=50)
def test_go_deferstmt_instantiation(instance):
    assert isinstance(instance, go_DeferStmt)

@given(instance=go_ForStmt_strategy)
@settings(max_examples=50)
def test_go_forstmt_instantiation(instance):
    assert isinstance(instance, go_ForStmt)

@given(instance=go_SelectStmt_strategy)
@settings(max_examples=50)
def test_go_selectstmt_instantiation(instance):
    assert isinstance(instance, go_SelectStmt)

@given(instance=go_SwitchStmt_strategy)
@settings(max_examples=50)
def test_go_switchstmt_instantiation(instance):
    assert isinstance(instance, go_SwitchStmt)

@given(instance=go_IfStmt_strategy)
@settings(max_examples=50)
def test_go_ifstmt_instantiation(instance):
    assert isinstance(instance, go_IfStmt)

@given(instance=go_ReceiverType_strategy)
@settings(max_examples=50)
def test_go_receivertype_instantiation(instance):
    assert isinstance(instance, go_ReceiverType)

@given(instance=go_decimals_strategy)
@settings(max_examples=50)
def test_go_decimals_instantiation(instance):
    assert isinstance(instance, go_decimals)



@given(instance=go_decimals_strategy)
def test_go_decimals_DECIMAL_DIGIT_setter(instance):
    original = instance.DECIMAL_DIGIT
    instance.DECIMAL_DIGIT = original
    assert instance.DECIMAL_DIGIT == original

@given(instance=go_Slice_strategy)
@settings(max_examples=50)
def test_go_slice_instantiation(instance):
    assert isinstance(instance, go_Slice)

@given(instance=go_binary_op_strategy)
@settings(max_examples=50)
def test_go_binary_op_instantiation(instance):
    assert isinstance(instance, go_binary_op)



@given(instance=go_binary_op_strategy)
def test_go_binary_op_mul_op_setter(instance):
    original = instance.mul_op
    instance.mul_op = original
    assert instance.mul_op == original



@given(instance=go_binary_op_strategy)
def test_go_binary_op_rel_op_setter(instance):
    original = instance.rel_op
    instance.rel_op = original
    assert instance.rel_op == original



@given(instance=go_binary_op_strategy)
def test_go_binary_op_add_op_setter(instance):
    original = instance.add_op
    instance.add_op = original
    assert instance.add_op == original

@given(instance=go_ExpressionLinha_strategy)
@settings(max_examples=50)
def test_go_expressionlinha_instantiation(instance):
    assert isinstance(instance, go_ExpressionLinha)

@given(instance=go_UnaryExpr_strategy)
@settings(max_examples=50)
def test_go_unaryexpr_instantiation(instance):
    assert isinstance(instance, go_UnaryExpr)



@given(instance=go_UnaryExpr_strategy)
def test_go_unaryexpr_unary_op_setter(instance):
    original = instance.unary_op
    instance.unary_op = original
    assert instance.unary_op == original

@given(instance=go_Arguments_strategy)
@settings(max_examples=50)
def test_go_arguments_instantiation(instance):
    assert isinstance(instance, go_Arguments)

@given(instance=go_MethodExpr_strategy)
@settings(max_examples=50)
def test_go_methodexpr_instantiation(instance):
    assert isinstance(instance, go_MethodExpr)

@given(instance=go_Conversion_strategy)
@settings(max_examples=50)
def test_go_conversion_instantiation(instance):
    assert isinstance(instance, go_Conversion)

@given(instance=go_PrimaryExprLinha_strategy)
@settings(max_examples=50)
def test_go_primaryexprlinha_instantiation(instance):
    assert isinstance(instance, go_PrimaryExprLinha)

@given(instance=go_PrimaryExpr_strategy)
@settings(max_examples=50)
def test_go_primaryexpr_instantiation(instance):
    assert isinstance(instance, go_PrimaryExpr)

@given(instance=go_FieldName_strategy)
@settings(max_examples=50)
def test_go_fieldname_instantiation(instance):
    assert isinstance(instance, go_FieldName)

@given(instance=go_Index_strategy)
@settings(max_examples=50)
def test_go_index_instantiation(instance):
    assert isinstance(instance, go_Index)

@given(instance=go_TypeAssertion_strategy)
@settings(max_examples=50)
def test_go_typeassertion_instantiation(instance):
    assert isinstance(instance, go_TypeAssertion)

@given(instance=go_Selector_strategy)
@settings(max_examples=50)
def test_go_selector_instantiation(instance):
    assert isinstance(instance, go_Selector)

@given(instance=go_cochetes_strategy)
@settings(max_examples=50)
def test_go_cochetes_instantiation(instance):
    assert isinstance(instance, go_cochetes)

@given(instance=go_ponto_strategy)
@settings(max_examples=50)
def test_go_ponto_instantiation(instance):
    assert isinstance(instance, go_ponto)

@given(instance=go_LiteralTypeLinha_strategy)
@settings(max_examples=50)
def test_go_literaltypelinha_instantiation(instance):
    assert isinstance(instance, go_LiteralTypeLinha)

@given(instance=go_LiteralValue_strategy)
@settings(max_examples=50)
def test_go_literalvalue_instantiation(instance):
    assert isinstance(instance, go_LiteralValue)

@given(instance=go_LiteralType_strategy)
@settings(max_examples=50)
def test_go_literaltype_instantiation(instance):
    assert isinstance(instance, go_LiteralType)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=go_FunctionLit_strategy)
@settings(max_examples=50)
def test_go_functionlit_instantiation(instance):
    assert isinstance(instance, go_FunctionLit)

@given(instance=go_CompositeLit_strategy)
@settings(max_examples=50)
def test_go_compositelit_instantiation(instance):
    assert isinstance(instance, go_CompositeLit)

@given(instance=go_PackageName_strategy)
@settings(max_examples=50)
def test_go_packagename_instantiation(instance):
    assert isinstance(instance, go_PackageName)

@given(instance=OperandName_strategy)
@settings(max_examples=50)
def test_operandname_instantiation(instance):
    assert isinstance(instance, OperandName)

@given(instance=go_Key_strategy)
@settings(max_examples=50)
def test_go_key_instantiation(instance):
    assert isinstance(instance, go_Key)

@given(instance=go_Element_strategy)
@settings(max_examples=50)
def test_go_element_instantiation(instance):
    assert isinstance(instance, go_Element)

@given(instance=go_KeyedElement_strategy)
@settings(max_examples=50)
def test_go_keyedelement_instantiation(instance):
    assert isinstance(instance, go_KeyedElement)

@given(instance=go_ElementList_strategy)
@settings(max_examples=50)
def test_go_elementlist_instantiation(instance):
    assert isinstance(instance, go_ElementList)

@given(instance=go_MethodDecl_strategy)
@settings(max_examples=50)
def test_go_methoddecl_instantiation(instance):
    assert isinstance(instance, go_MethodDecl)

@given(instance=go_FunctionDecl_strategy)
@settings(max_examples=50)
def test_go_functiondecl_instantiation(instance):
    assert isinstance(instance, go_FunctionDecl)

@given(instance=go_ShortVarDecl_strategy)
@settings(max_examples=50)
def test_go_shortvardecl_instantiation(instance):
    assert isinstance(instance, go_ShortVarDecl)

@given(instance=go_rune_lit_strategy)
@settings(max_examples=50)
def test_go_rune_lit_instantiation(instance):
    assert isinstance(instance, go_rune_lit)



@given(instance=go_rune_lit_strategy)
def test_go_rune_lit_unicode_value_setter(instance):
    original = instance.unicode_value
    instance.unicode_value = original
    assert instance.unicode_value == original



@given(instance=go_rune_lit_strategy)
def test_go_rune_lit_byte_value_setter(instance):
    original = instance.byte_value
    instance.byte_value = original
    assert instance.byte_value == original

@given(instance=go_float_lit_strategy)
@settings(max_examples=50)
def test_go_float_lit_instantiation(instance):
    assert isinstance(instance, go_float_lit)

@given(instance=go_BasicLit_strategy)
@settings(max_examples=50)
def test_go_basiclit_instantiation(instance):
    assert isinstance(instance, go_BasicLit)



@given(instance=go_BasicLit_strategy)
def test_go_basiclit_int_lit_setter(instance):
    original = instance.int_lit
    instance.int_lit = original
    assert instance.int_lit == original

@given(instance=go_OperandName_strategy)
@settings(max_examples=50)
def test_go_operandname_instantiation(instance):
    assert isinstance(instance, go_OperandName)

@given(instance=go_Literal_strategy)
@settings(max_examples=50)
def test_go_literal_instantiation(instance):
    assert isinstance(instance, go_Literal)

@given(instance=go_Operand_strategy)
@settings(max_examples=50)
def test_go_operand_instantiation(instance):
    assert isinstance(instance, go_Operand)

@given(instance=go_ExpressionList_strategy)
@settings(max_examples=50)
def test_go_expressionlist_instantiation(instance):
    assert isinstance(instance, go_ExpressionList)

@given(instance=go_ConstSpec_strategy)
@settings(max_examples=50)
def test_go_constspec_instantiation(instance):
    assert isinstance(instance, go_ConstSpec)

@given(instance=go_Receiver_strategy)
@settings(max_examples=50)
def test_go_receiver_instantiation(instance):
    assert isinstance(instance, go_Receiver)

@given(instance=go_FunctionBody_strategy)
@settings(max_examples=50)
def test_go_functionbody_instantiation(instance):
    assert isinstance(instance, go_FunctionBody)

@given(instance=go_FunctionName_strategy)
@settings(max_examples=50)
def test_go_functionname_instantiation(instance):
    assert isinstance(instance, go_FunctionName)

@given(instance=go_VarSpec_strategy)
@settings(max_examples=50)
def test_go_varspec_instantiation(instance):
    assert isinstance(instance, go_VarSpec)

@given(instance=TypeSpec_strategy)
@settings(max_examples=50)
def test_typespec_instantiation(instance):
    assert isinstance(instance, TypeSpec)

@given(instance=go_TypeDef_strategy)
@settings(max_examples=50)
def test_go_typedef_instantiation(instance):
    assert isinstance(instance, go_TypeDef)

@given(instance=go_AliasDecl_strategy)
@settings(max_examples=50)
def test_go_aliasdecl_instantiation(instance):
    assert isinstance(instance, go_AliasDecl)

@given(instance=go_TypeSpec_strategy)
@settings(max_examples=50)
def test_go_typespec_instantiation(instance):
    assert isinstance(instance, go_TypeSpec)

@given(instance=go_KeyType_strategy)
@settings(max_examples=50)
def test_go_keytype_instantiation(instance):
    assert isinstance(instance, go_KeyType)

@given(instance=go_InterfaceTypeName_strategy)
@settings(max_examples=50)
def test_go_interfacetypename_instantiation(instance):
    assert isinstance(instance, go_InterfaceTypeName)

@given(instance=go_MethodName_strategy)
@settings(max_examples=50)
def test_go_methodname_instantiation(instance):
    assert isinstance(instance, go_MethodName)

@given(instance=go_MethodSpec_strategy)
@settings(max_examples=50)
def test_go_methodspec_instantiation(instance):
    assert isinstance(instance, go_MethodSpec)

@given(instance=go_topLevelDeclLinha_strategy)
@settings(max_examples=50)
def test_go_topleveldecllinha_instantiation(instance):
    assert isinstance(instance, go_topLevelDeclLinha)

@given(instance=go_VarDecl_strategy)
@settings(max_examples=50)
def test_go_vardecl_instantiation(instance):
    assert isinstance(instance, go_VarDecl)

@given(instance=go_TypeDecl_strategy)
@settings(max_examples=50)
def test_go_typedecl_instantiation(instance):
    assert isinstance(instance, go_TypeDecl)

@given(instance=go_ConstDecl_strategy)
@settings(max_examples=50)
def test_go_constdecl_instantiation(instance):
    assert isinstance(instance, go_ConstDecl)

@given(instance=go_Declaration_strategy)
@settings(max_examples=50)
def test_go_declaration_instantiation(instance):
    assert isinstance(instance, go_Declaration)

@given(instance=go_Statement_strategy)
@settings(max_examples=50)
def test_go_statement_instantiation(instance):
    assert isinstance(instance, go_Statement)



@given(instance=go_Statement_strategy)
def test_go_statement_FallthroughStmt_setter(instance):
    original = instance.FallthroughStmt
    instance.FallthroughStmt = original
    assert instance.FallthroughStmt == original

@given(instance=go_StatementList_strategy)
@settings(max_examples=50)
def test_go_statementlist_instantiation(instance):
    assert isinstance(instance, go_StatementList)

@given(instance=go_Block_strategy)
@settings(max_examples=50)
def test_go_block_instantiation(instance):
    assert isinstance(instance, go_Block)

@given(instance=go_Result_strategy)
@settings(max_examples=50)
def test_go_result_instantiation(instance):
    assert isinstance(instance, go_Result)

@given(instance=go_Signature_strategy)
@settings(max_examples=50)
def test_go_signature_instantiation(instance):
    assert isinstance(instance, go_Signature)

@given(instance=go_string_lit_strategy)
@settings(max_examples=50)
def test_go_string_lit_instantiation(instance):
    assert isinstance(instance, go_string_lit)



@given(instance=go_string_lit_strategy)
def test_go_string_lit_interpreted_string_lit_setter(instance):
    original = instance.interpreted_string_lit
    instance.interpreted_string_lit = original
    assert instance.interpreted_string_lit == original



@given(instance=go_string_lit_strategy)
def test_go_string_lit_raw_string_lit_setter(instance):
    original = instance.raw_string_lit
    instance.raw_string_lit = original
    assert instance.raw_string_lit == original

@given(instance=go_Tag_strategy)
@settings(max_examples=50)
def test_go_tag_instantiation(instance):
    assert isinstance(instance, go_Tag)

@given(instance=go_EmbeddedField_strategy)
@settings(max_examples=50)
def test_go_embeddedfield_instantiation(instance):
    assert isinstance(instance, go_EmbeddedField)

@given(instance=go_IdentifierList_strategy)
@settings(max_examples=50)
def test_go_identifierlist_instantiation(instance):
    assert isinstance(instance, go_IdentifierList)

@given(instance=go_FieldDecl_strategy)
@settings(max_examples=50)
def test_go_fielddecl_instantiation(instance):
    assert isinstance(instance, go_FieldDecl)

@given(instance=go_ParameterDecl_strategy)
@settings(max_examples=50)
def test_go_parameterdecl_instantiation(instance):
    assert isinstance(instance, go_ParameterDecl)

@given(instance=go_ParameterList_strategy)
@settings(max_examples=50)
def test_go_parameterlist_instantiation(instance):
    assert isinstance(instance, go_ParameterList)

@given(instance=Receiver_strategy)
@settings(max_examples=50)
def test_receiver_instantiation(instance):
    assert isinstance(instance, Receiver)

@given(instance=go_Parameters_strategy)
@settings(max_examples=50)
def test_go_parameters_instantiation(instance):
    assert isinstance(instance, go_Parameters)

@given(instance=go_InterfaceType_strategy)
@settings(max_examples=50)
def test_go_interfacetype_instantiation(instance):
    assert isinstance(instance, go_InterfaceType)

@given(instance=go_FunctionType_strategy)
@settings(max_examples=50)
def test_go_functiontype_instantiation(instance):
    assert isinstance(instance, go_FunctionType)

@given(instance=go_PointerType_strategy)
@settings(max_examples=50)
def test_go_pointertype_instantiation(instance):
    assert isinstance(instance, go_PointerType)

@given(instance=go_StructType_strategy)
@settings(max_examples=50)
def test_go_structtype_instantiation(instance):
    assert isinstance(instance, go_StructType)

@given(instance=go_TypeLitLinha_strategy)
@settings(max_examples=50)
def test_go_typelitlinha_instantiation(instance):
    assert isinstance(instance, go_TypeLitLinha)

@given(instance=go_QualifiedIdent_strategy)
@settings(max_examples=50)
def test_go_qualifiedident_instantiation(instance):
    assert isinstance(instance, go_QualifiedIdent)

@given(instance=go_TypeNameLinha_strategy)
@settings(max_examples=50)
def test_go_typenamelinha_instantiation(instance):
    assert isinstance(instance, go_TypeNameLinha)

@given(instance=go_identifier_strategy)
@settings(max_examples=50)
def test_go_identifier_instantiation(instance):
    assert isinstance(instance, go_identifier)



@given(instance=go_identifier_strategy)
def test_go_identifier_LETTER_setter(instance):
    original = instance.LETTER
    instance.LETTER = original
    assert instance.LETTER == original



@given(instance=go_identifier_strategy)
def test_go_identifier_DECIMAL_DIGIT_setter(instance):
    original = instance.DECIMAL_DIGIT
    instance.DECIMAL_DIGIT = original
    assert instance.DECIMAL_DIGIT == original

@given(instance=go_TypeLit_strategy)
@settings(max_examples=50)
def test_go_typelit_instantiation(instance):
    assert isinstance(instance, go_TypeLit)

@given(instance=go_Expression_strategy)
@settings(max_examples=50)
def test_go_expression_instantiation(instance):
    assert isinstance(instance, go_Expression)

@given(instance=go_ElementType_strategy)
@settings(max_examples=50)
def test_go_elementtype_instantiation(instance):
    assert isinstance(instance, go_ElementType)

@given(instance=go_ArrayLength_strategy)
@settings(max_examples=50)
def test_go_arraylength_instantiation(instance):
    assert isinstance(instance, go_ArrayLength)

@given(instance=go_ChannelType_strategy)
@settings(max_examples=50)
def test_go_channeltype_instantiation(instance):
    assert isinstance(instance, go_ChannelType)

@given(instance=go_MapType_strategy)
@settings(max_examples=50)
def test_go_maptype_instantiation(instance):
    assert isinstance(instance, go_MapType)

@given(instance=go_TypeName_strategy)
@settings(max_examples=50)
def test_go_typename_instantiation(instance):
    assert isinstance(instance, go_TypeName)

@given(instance=go_Type_strategy)
@settings(max_examples=50)
def test_go_type_instantiation(instance):
    assert isinstance(instance, go_Type)

@given(instance=go_TopLevelDecl_strategy)
@settings(max_examples=50)
def test_go_topleveldecl_instantiation(instance):
    assert isinstance(instance, go_TopLevelDecl)

@given(instance=go_ImportDecl_strategy)
@settings(max_examples=50)
def test_go_importdecl_instantiation(instance):
    assert isinstance(instance, go_ImportDecl)

@given(instance=go_PackageClause_strategy)
@settings(max_examples=50)
def test_go_packageclause_instantiation(instance):
    assert isinstance(instance, go_PackageClause)
