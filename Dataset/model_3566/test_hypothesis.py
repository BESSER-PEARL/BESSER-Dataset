import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_ImportSpec,
    myDsl_PackageName,
    myDsl_ImportDecl,
    myDsl_PackageClause,
    myDsl_RecvExpr,
    myDsl_CommCaseLinha,
    myDsl_CommCase,
    myDsl_CommClause,
    myDsl_ForStmtLinhaLinha,
    myDsl_PostStmt,
    myDsl_Condition,
    myDsl_ForStmtLinha,
    myDsl_TypeList,
    myDsl_TypeSwitchCase,
    myDsl_TypeCaseClause,
    myDsl_TypeSwitchGuard,
    myDsl_ExprSwitchCase,
    myDsl_ExprCaseClause,
    myDsl_TypeSwitchStmt,
    myDsl_ExprSwitchStmt,
    myDsl_IfStmtLinha,
    myDsl_Label,
    myDsl_assign_op,
    myDsl_SimpleStmtLinha,
    myDsl_EmptyStmt,
    myDsl_DeferStmt,
    myDsl_ForStmt,
    myDsl_SelectStmt,
    myDsl_SwitchStmt,
    myDsl_IfStmt,
    myDsl_Expression_Linha,
    myDsl_FallthroughStmt,
    myDsl_GotoStmt,
    myDsl_ContinueStmt,
    myDsl_BreakStmt,
    myDsl_ReturnStmt,
    myDsl_GoStmt,
    myDsl_SimpleStmt,
    myDsl_LabeledStmt,
    myDsl_BINARY_OP,
    myDsl_Expression1,
    myDsl_TypeAssertion,
    myDsl_UnaryExpr,
    myDsl_ReceiverType,
    myDsl_Arguments,
    myDsl_Slice,
    myDsl_Index,
    myDsl_Selector,
    myDsl_MethodExpr,
    myDsl_Conversion,
    myDsl_PrimaryExprLinha,
    myDsl_PrimaryExpr,
    myDsl_FieldName,
    myDsl_Element,
    myDsl_Key,
    myDsl_KeyedElement,
    myDsl_ElementList,
    myDsl_LiteralTypeLinha,
    myDsl_LiteralValue,
    myDsl_LiteralType,
    myDsl_FunctionLit,
    myDsl_CompositeLit,
    myDsl_BasicLit,
    myDsl_OperandName,
    myDsl_Literal,
    myDsl_Operand,
    myDsl_Receiver,
    myDsl_FunctionBody,
    myDsl_FunctionName,
    myDsl_ShortVarDecl,
    myDsl_ConstSpec,
    myDsl_VarSpec,
    myDsl_TypeDef,
    myDsl_AliasDecl,
    myDsl_TypeSpec,
    myDsl_ExpressionList,
    myDsl_ChannelTypeLinha,
    myDsl_MethodDecl,
    myDsl_FunctionDecl,
    myDsl_TopLevelDecl,
    myDsl_VarDecl,
    myDsl_TypeDecl,
    myDsl_ConstDecl,
    myDsl_Declaration,
    myDsl_Statement,
    myDsl_StatementList,
    myDsl_Block,
    myDsl_Result,
    myDsl_KeyType,
    myDsl_InterfaceTypeName,
    myDsl_MethodName,
    myDsl_MethodSpec,
    myDsl_ParameterDecl,
    myDsl_ParameterList,
    myDsl_ChannelType,
    myDsl_Parameters,
    myDsl_Signature,
    myDsl_BaseType,
    myDsl_Tag,
    myDsl_EmbeddedField,
    myDsl_IdentifierList,
    myDsl_FieldDecl,
    myDsl_Expression,
    myDsl_ElementType,
    myDsl_ArrayLength,
    myDsl_MapType,
    myDsl_InterfaceType,
    myDsl_FunctionType,
    myDsl_PointerType,
    myDsl_StructType,
    myDsl_TypeLitLinha,
    myDsl_TypeNameLinha,
    myDsl_TypeLit,
    myDsl_TypeName,
    myDsl_Type,
    myDsl_SourceFile,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_importspec_is_not_abstract():
    assert not inspect.isabstract(myDsl_ImportSpec)


def test_mydsl_importspec_constructor_exists():
    assert callable(myDsl_ImportSpec.__init__)


def test_mydsl_importspec_constructor_args():
    sig = inspect.signature(myDsl_ImportSpec.__init__)
    params = list(sig.parameters.keys())
    assert "sTRING_LIT" in params, "Missing parameter 'sTRING_LIT'"

def test_mydsl_importspec_has_sTRING_LIT():
    assert hasattr(myDsl_ImportSpec, "sTRING_LIT")
    descriptor = None
    for klass in myDsl_ImportSpec.__mro__:
        if "sTRING_LIT" in klass.__dict__:
            descriptor = klass.__dict__["sTRING_LIT"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_packagename_is_not_abstract():
    assert not inspect.isabstract(myDsl_PackageName)


def test_mydsl_packagename_constructor_exists():
    assert callable(myDsl_PackageName.__init__)


def test_mydsl_packagename_constructor_args():
    sig = inspect.signature(myDsl_PackageName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_packagename_has_id():
    assert hasattr(myDsl_PackageName, "id")
    descriptor = None
    for klass in myDsl_PackageName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_importdecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_ImportDecl)


def test_mydsl_importdecl_constructor_exists():
    assert callable(myDsl_ImportDecl.__init__)


def test_mydsl_importdecl_constructor_args():
    sig = inspect.signature(myDsl_ImportDecl.__init__)
    params = list(sig.parameters.keys())
    assert "importt" in params, "Missing parameter 'importt'"

def test_mydsl_importdecl_has_importt():
    assert hasattr(myDsl_ImportDecl, "importt")
    descriptor = None
    for klass in myDsl_ImportDecl.__mro__:
        if "importt" in klass.__dict__:
            descriptor = klass.__dict__["importt"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_packageclause_is_not_abstract():
    assert not inspect.isabstract(myDsl_PackageClause)


def test_mydsl_packageclause_constructor_exists():
    assert callable(myDsl_PackageClause.__init__)


def test_mydsl_packageclause_constructor_args():
    sig = inspect.signature(myDsl_PackageClause.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_mydsl_packageclause_has_package():
    assert hasattr(myDsl_PackageClause, "package")
    descriptor = None
    for klass in myDsl_PackageClause.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_recvexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl_RecvExpr)


def test_mydsl_recvexpr_constructor_exists():
    assert callable(myDsl_RecvExpr.__init__)


def test_mydsl_recvexpr_constructor_args():
    sig = inspect.signature(myDsl_RecvExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_commcaselinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_CommCaseLinha)


def test_mydsl_commcaselinha_constructor_exists():
    assert callable(myDsl_CommCaseLinha.__init__)


def test_mydsl_commcaselinha_constructor_args():
    sig = inspect.signature(myDsl_CommCaseLinha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_commcase_is_not_abstract():
    assert not inspect.isabstract(myDsl_CommCase)


def test_mydsl_commcase_constructor_exists():
    assert callable(myDsl_CommCase.__init__)


def test_mydsl_commcase_constructor_args():
    sig = inspect.signature(myDsl_CommCase.__init__)
    params = list(sig.parameters.keys())
    assert "case" in params, "Missing parameter 'case'"
    assert "default" in params, "Missing parameter 'default'"

def test_mydsl_commcase_has_case():
    assert hasattr(myDsl_CommCase, "case")
    descriptor = None
    for klass in myDsl_CommCase.__mro__:
        if "case" in klass.__dict__:
            descriptor = klass.__dict__["case"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_commcase_has_default():
    assert hasattr(myDsl_CommCase, "default")
    descriptor = None
    for klass in myDsl_CommCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_commclause_is_not_abstract():
    assert not inspect.isabstract(myDsl_CommClause)


def test_mydsl_commclause_constructor_exists():
    assert callable(myDsl_CommClause.__init__)


def test_mydsl_commclause_constructor_args():
    sig = inspect.signature(myDsl_CommClause.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_forstmtlinhalinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_ForStmtLinhaLinha)


def test_mydsl_forstmtlinhalinha_constructor_exists():
    assert callable(myDsl_ForStmtLinhaLinha.__init__)


def test_mydsl_forstmtlinhalinha_constructor_args():
    sig = inspect.signature(myDsl_ForStmtLinhaLinha.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"

def test_mydsl_forstmtlinhalinha_has_range():
    assert hasattr(myDsl_ForStmtLinhaLinha, "range")
    descriptor = None
    for klass in myDsl_ForStmtLinhaLinha.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_poststmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_PostStmt)


def test_mydsl_poststmt_constructor_exists():
    assert callable(myDsl_PostStmt.__init__)


def test_mydsl_poststmt_constructor_args():
    sig = inspect.signature(myDsl_PostStmt.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_condition_is_not_abstract():
    assert not inspect.isabstract(myDsl_Condition)


def test_mydsl_condition_constructor_exists():
    assert callable(myDsl_Condition.__init__)


def test_mydsl_condition_constructor_args():
    sig = inspect.signature(myDsl_Condition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_forstmtlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_ForStmtLinha)


def test_mydsl_forstmtlinha_constructor_exists():
    assert callable(myDsl_ForStmtLinha.__init__)


def test_mydsl_forstmtlinha_constructor_args():
    sig = inspect.signature(myDsl_ForStmtLinha.__init__)
    params = list(sig.parameters.keys())
    assert "vazio" in params, "Missing parameter 'vazio'"

def test_mydsl_forstmtlinha_has_vazio():
    assert hasattr(myDsl_ForStmtLinha, "vazio")
    descriptor = None
    for klass in myDsl_ForStmtLinha.__mro__:
        if "vazio" in klass.__dict__:
            descriptor = klass.__dict__["vazio"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_typelist_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeList)


def test_mydsl_typelist_constructor_exists():
    assert callable(myDsl_TypeList.__init__)


def test_mydsl_typelist_constructor_args():
    sig = inspect.signature(myDsl_TypeList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typeswitchcase_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeSwitchCase)


def test_mydsl_typeswitchcase_constructor_exists():
    assert callable(myDsl_TypeSwitchCase.__init__)


def test_mydsl_typeswitchcase_constructor_args():
    sig = inspect.signature(myDsl_TypeSwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "case" in params, "Missing parameter 'case'"
    assert "default" in params, "Missing parameter 'default'"

def test_mydsl_typeswitchcase_has_case():
    assert hasattr(myDsl_TypeSwitchCase, "case")
    descriptor = None
    for klass in myDsl_TypeSwitchCase.__mro__:
        if "case" in klass.__dict__:
            descriptor = klass.__dict__["case"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_typeswitchcase_has_default():
    assert hasattr(myDsl_TypeSwitchCase, "default")
    descriptor = None
    for klass in myDsl_TypeSwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_typecaseclause_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeCaseClause)


def test_mydsl_typecaseclause_constructor_exists():
    assert callable(myDsl_TypeCaseClause.__init__)


def test_mydsl_typecaseclause_constructor_args():
    sig = inspect.signature(myDsl_TypeCaseClause.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typeswitchguard_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeSwitchGuard)


def test_mydsl_typeswitchguard_constructor_exists():
    assert callable(myDsl_TypeSwitchGuard.__init__)


def test_mydsl_typeswitchguard_constructor_args():
    sig = inspect.signature(myDsl_TypeSwitchGuard.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl_typeswitchguard_has_id():
    assert hasattr(myDsl_TypeSwitchGuard, "id")
    descriptor = None
    for klass in myDsl_TypeSwitchGuard.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_typeswitchguard_has_type():
    assert hasattr(myDsl_TypeSwitchGuard, "type")
    descriptor = None
    for klass in myDsl_TypeSwitchGuard.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_exprswitchcase_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprSwitchCase)


def test_mydsl_exprswitchcase_constructor_exists():
    assert callable(myDsl_ExprSwitchCase.__init__)


def test_mydsl_exprswitchcase_constructor_args():
    sig = inspect.signature(myDsl_ExprSwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "case" in params, "Missing parameter 'case'"

def test_mydsl_exprswitchcase_has_default():
    assert hasattr(myDsl_ExprSwitchCase, "default")
    descriptor = None
    for klass in myDsl_ExprSwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_exprswitchcase_has_case():
    assert hasattr(myDsl_ExprSwitchCase, "case")
    descriptor = None
    for klass in myDsl_ExprSwitchCase.__mro__:
        if "case" in klass.__dict__:
            descriptor = klass.__dict__["case"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_exprcaseclause_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprCaseClause)


def test_mydsl_exprcaseclause_constructor_exists():
    assert callable(myDsl_ExprCaseClause.__init__)


def test_mydsl_exprcaseclause_constructor_args():
    sig = inspect.signature(myDsl_ExprCaseClause.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typeswitchstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeSwitchStmt)


def test_mydsl_typeswitchstmt_constructor_exists():
    assert callable(myDsl_TypeSwitchStmt.__init__)


def test_mydsl_typeswitchstmt_constructor_args():
    sig = inspect.signature(myDsl_TypeSwitchStmt.__init__)
    params = list(sig.parameters.keys())
    assert "switch" in params, "Missing parameter 'switch'"

def test_mydsl_typeswitchstmt_has_switch():
    assert hasattr(myDsl_TypeSwitchStmt, "switch")
    descriptor = None
    for klass in myDsl_TypeSwitchStmt.__mro__:
        if "switch" in klass.__dict__:
            descriptor = klass.__dict__["switch"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_exprswitchstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprSwitchStmt)


def test_mydsl_exprswitchstmt_constructor_exists():
    assert callable(myDsl_ExprSwitchStmt.__init__)


def test_mydsl_exprswitchstmt_constructor_args():
    sig = inspect.signature(myDsl_ExprSwitchStmt.__init__)
    params = list(sig.parameters.keys())
    assert "switch" in params, "Missing parameter 'switch'"

def test_mydsl_exprswitchstmt_has_switch():
    assert hasattr(myDsl_ExprSwitchStmt, "switch")
    descriptor = None
    for klass in myDsl_ExprSwitchStmt.__mro__:
        if "switch" in klass.__dict__:
            descriptor = klass.__dict__["switch"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_ifstmtlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_IfStmtLinha)


def test_mydsl_ifstmtlinha_constructor_exists():
    assert callable(myDsl_IfStmtLinha.__init__)


def test_mydsl_ifstmtlinha_constructor_args():
    sig = inspect.signature(myDsl_IfStmtLinha.__init__)
    params = list(sig.parameters.keys())
    assert "else_" in params, "Missing parameter 'else_'"

def test_mydsl_ifstmtlinha_has_else_():
    assert hasattr(myDsl_IfStmtLinha, "else_")
    descriptor = None
    for klass in myDsl_IfStmtLinha.__mro__:
        if "else_" in klass.__dict__:
            descriptor = klass.__dict__["else_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_label_is_not_abstract():
    assert not inspect.isabstract(myDsl_Label)


def test_mydsl_label_constructor_exists():
    assert callable(myDsl_Label.__init__)


def test_mydsl_label_constructor_args():
    sig = inspect.signature(myDsl_Label.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_label_has_id():
    assert hasattr(myDsl_Label, "id")
    descriptor = None
    for klass in myDsl_Label.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_assign_op_is_not_abstract():
    assert not inspect.isabstract(myDsl_assign_op)


def test_mydsl_assign_op_constructor_exists():
    assert callable(myDsl_assign_op.__init__)


def test_mydsl_assign_op_constructor_args():
    sig = inspect.signature(myDsl_assign_op.__init__)
    params = list(sig.parameters.keys())
    assert "mUL_OP" in params, "Missing parameter 'mUL_OP'"
    assert "aDD_OP" in params, "Missing parameter 'aDD_OP'"

def test_mydsl_assign_op_has_mUL_OP():
    assert hasattr(myDsl_assign_op, "mUL_OP")
    descriptor = None
    for klass in myDsl_assign_op.__mro__:
        if "mUL_OP" in klass.__dict__:
            descriptor = klass.__dict__["mUL_OP"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_assign_op_has_aDD_OP():
    assert hasattr(myDsl_assign_op, "aDD_OP")
    descriptor = None
    for klass in myDsl_assign_op.__mro__:
        if "aDD_OP" in klass.__dict__:
            descriptor = klass.__dict__["aDD_OP"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_simplestmtlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_SimpleStmtLinha)


def test_mydsl_simplestmtlinha_constructor_exists():
    assert callable(myDsl_SimpleStmtLinha.__init__)


def test_mydsl_simplestmtlinha_constructor_args():
    sig = inspect.signature(myDsl_SimpleStmtLinha.__init__)
    params = list(sig.parameters.keys())
    assert "aNY_OTHER" in params, "Missing parameter 'aNY_OTHER'"

def test_mydsl_simplestmtlinha_has_aNY_OTHER():
    assert hasattr(myDsl_SimpleStmtLinha, "aNY_OTHER")
    descriptor = None
    for klass in myDsl_SimpleStmtLinha.__mro__:
        if "aNY_OTHER" in klass.__dict__:
            descriptor = klass.__dict__["aNY_OTHER"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_emptystmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_EmptyStmt)


def test_mydsl_emptystmt_constructor_exists():
    assert callable(myDsl_EmptyStmt.__init__)


def test_mydsl_emptystmt_constructor_args():
    sig = inspect.signature(myDsl_EmptyStmt.__init__)
    params = list(sig.parameters.keys())
    assert "aNY_OTHER" in params, "Missing parameter 'aNY_OTHER'"

def test_mydsl_emptystmt_has_aNY_OTHER():
    assert hasattr(myDsl_EmptyStmt, "aNY_OTHER")
    descriptor = None
    for klass in myDsl_EmptyStmt.__mro__:
        if "aNY_OTHER" in klass.__dict__:
            descriptor = klass.__dict__["aNY_OTHER"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_deferstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_DeferStmt)


def test_mydsl_deferstmt_constructor_exists():
    assert callable(myDsl_DeferStmt.__init__)


def test_mydsl_deferstmt_constructor_args():
    sig = inspect.signature(myDsl_DeferStmt.__init__)
    params = list(sig.parameters.keys())
    assert "defer" in params, "Missing parameter 'defer'"

def test_mydsl_deferstmt_has_defer():
    assert hasattr(myDsl_DeferStmt, "defer")
    descriptor = None
    for klass in myDsl_DeferStmt.__mro__:
        if "defer" in klass.__dict__:
            descriptor = klass.__dict__["defer"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_forstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_ForStmt)


def test_mydsl_forstmt_constructor_exists():
    assert callable(myDsl_ForStmt.__init__)


def test_mydsl_forstmt_constructor_args():
    sig = inspect.signature(myDsl_ForStmt.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"
    assert "for_" in params, "Missing parameter 'for_'"

def test_mydsl_forstmt_has_range():
    assert hasattr(myDsl_ForStmt, "range")
    descriptor = None
    for klass in myDsl_ForStmt.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_forstmt_has_for_():
    assert hasattr(myDsl_ForStmt, "for_")
    descriptor = None
    for klass in myDsl_ForStmt.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_selectstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_SelectStmt)


def test_mydsl_selectstmt_constructor_exists():
    assert callable(myDsl_SelectStmt.__init__)


def test_mydsl_selectstmt_constructor_args():
    sig = inspect.signature(myDsl_SelectStmt.__init__)
    params = list(sig.parameters.keys())
    assert "select" in params, "Missing parameter 'select'"

def test_mydsl_selectstmt_has_select():
    assert hasattr(myDsl_SelectStmt, "select")
    descriptor = None
    for klass in myDsl_SelectStmt.__mro__:
        if "select" in klass.__dict__:
            descriptor = klass.__dict__["select"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_switchstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_SwitchStmt)


def test_mydsl_switchstmt_constructor_exists():
    assert callable(myDsl_SwitchStmt.__init__)


def test_mydsl_switchstmt_constructor_args():
    sig = inspect.signature(myDsl_SwitchStmt.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_ifstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_IfStmt)


def test_mydsl_ifstmt_constructor_exists():
    assert callable(myDsl_IfStmt.__init__)


def test_mydsl_ifstmt_constructor_args():
    sig = inspect.signature(myDsl_IfStmt.__init__)
    params = list(sig.parameters.keys())
    assert "else_" in params, "Missing parameter 'else_'"
    assert "if_" in params, "Missing parameter 'if_'"

def test_mydsl_ifstmt_has_else_():
    assert hasattr(myDsl_IfStmt, "else_")
    descriptor = None
    for klass in myDsl_IfStmt.__mro__:
        if "else_" in klass.__dict__:
            descriptor = klass.__dict__["else_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_ifstmt_has_if_():
    assert hasattr(myDsl_IfStmt, "if_")
    descriptor = None
    for klass in myDsl_IfStmt.__mro__:
        if "if_" in klass.__dict__:
            descriptor = klass.__dict__["if_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expression_linha_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression_Linha)


def test_mydsl_expression_linha_constructor_exists():
    assert callable(myDsl_Expression_Linha.__init__)


def test_mydsl_expression_linha_constructor_args():
    sig = inspect.signature(myDsl_Expression_Linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_fallthroughstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_FallthroughStmt)


def test_mydsl_fallthroughstmt_constructor_exists():
    assert callable(myDsl_FallthroughStmt.__init__)


def test_mydsl_fallthroughstmt_constructor_args():
    sig = inspect.signature(myDsl_FallthroughStmt.__init__)
    params = list(sig.parameters.keys())
    assert "fallthrough" in params, "Missing parameter 'fallthrough'"

def test_mydsl_fallthroughstmt_has_fallthrough():
    assert hasattr(myDsl_FallthroughStmt, "fallthrough")
    descriptor = None
    for klass in myDsl_FallthroughStmt.__mro__:
        if "fallthrough" in klass.__dict__:
            descriptor = klass.__dict__["fallthrough"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_gotostmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_GotoStmt)


def test_mydsl_gotostmt_constructor_exists():
    assert callable(myDsl_GotoStmt.__init__)


def test_mydsl_gotostmt_constructor_args():
    sig = inspect.signature(myDsl_GotoStmt.__init__)
    params = list(sig.parameters.keys())
    assert "goto" in params, "Missing parameter 'goto'"

def test_mydsl_gotostmt_has_goto():
    assert hasattr(myDsl_GotoStmt, "goto")
    descriptor = None
    for klass in myDsl_GotoStmt.__mro__:
        if "goto" in klass.__dict__:
            descriptor = klass.__dict__["goto"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_continuestmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_ContinueStmt)


def test_mydsl_continuestmt_constructor_exists():
    assert callable(myDsl_ContinueStmt.__init__)


def test_mydsl_continuestmt_constructor_args():
    sig = inspect.signature(myDsl_ContinueStmt.__init__)
    params = list(sig.parameters.keys())
    assert "continue_" in params, "Missing parameter 'continue_'"

def test_mydsl_continuestmt_has_continue_():
    assert hasattr(myDsl_ContinueStmt, "continue_")
    descriptor = None
    for klass in myDsl_ContinueStmt.__mro__:
        if "continue_" in klass.__dict__:
            descriptor = klass.__dict__["continue_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_breakstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_BreakStmt)


def test_mydsl_breakstmt_constructor_exists():
    assert callable(myDsl_BreakStmt.__init__)


def test_mydsl_breakstmt_constructor_args():
    sig = inspect.signature(myDsl_BreakStmt.__init__)
    params = list(sig.parameters.keys())
    assert "break_" in params, "Missing parameter 'break_'"

def test_mydsl_breakstmt_has_break_():
    assert hasattr(myDsl_BreakStmt, "break_")
    descriptor = None
    for klass in myDsl_BreakStmt.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_returnstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_ReturnStmt)


def test_mydsl_returnstmt_constructor_exists():
    assert callable(myDsl_ReturnStmt.__init__)


def test_mydsl_returnstmt_constructor_args():
    sig = inspect.signature(myDsl_ReturnStmt.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"

def test_mydsl_returnstmt_has_return_():
    assert hasattr(myDsl_ReturnStmt, "return_")
    descriptor = None
    for klass in myDsl_ReturnStmt.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_gostmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_GoStmt)


def test_mydsl_gostmt_constructor_exists():
    assert callable(myDsl_GoStmt.__init__)


def test_mydsl_gostmt_constructor_args():
    sig = inspect.signature(myDsl_GoStmt.__init__)
    params = list(sig.parameters.keys())
    assert "go" in params, "Missing parameter 'go'"

def test_mydsl_gostmt_has_go():
    assert hasattr(myDsl_GoStmt, "go")
    descriptor = None
    for klass in myDsl_GoStmt.__mro__:
        if "go" in klass.__dict__:
            descriptor = klass.__dict__["go"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_simplestmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_SimpleStmt)


def test_mydsl_simplestmt_constructor_exists():
    assert callable(myDsl_SimpleStmt.__init__)


def test_mydsl_simplestmt_constructor_args():
    sig = inspect.signature(myDsl_SimpleStmt.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_labeledstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl_LabeledStmt)


def test_mydsl_labeledstmt_constructor_exists():
    assert callable(myDsl_LabeledStmt.__init__)


def test_mydsl_labeledstmt_constructor_args():
    sig = inspect.signature(myDsl_LabeledStmt.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_binary_op_is_not_abstract():
    assert not inspect.isabstract(myDsl_BINARY_OP)


def test_mydsl_binary_op_constructor_exists():
    assert callable(myDsl_BINARY_OP.__init__)


def test_mydsl_binary_op_constructor_args():
    sig = inspect.signature(myDsl_BINARY_OP.__init__)
    params = list(sig.parameters.keys())
    assert "rEL_OP" in params, "Missing parameter 'rEL_OP'"
    assert "aDD_OP" in params, "Missing parameter 'aDD_OP'"

def test_mydsl_binary_op_has_rEL_OP():
    assert hasattr(myDsl_BINARY_OP, "rEL_OP")
    descriptor = None
    for klass in myDsl_BINARY_OP.__mro__:
        if "rEL_OP" in klass.__dict__:
            descriptor = klass.__dict__["rEL_OP"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_binary_op_has_aDD_OP():
    assert hasattr(myDsl_BINARY_OP, "aDD_OP")
    descriptor = None
    for klass in myDsl_BINARY_OP.__mro__:
        if "aDD_OP" in klass.__dict__:
            descriptor = klass.__dict__["aDD_OP"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expression1_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression1)


def test_mydsl_expression1_constructor_exists():
    assert callable(myDsl_Expression1.__init__)


def test_mydsl_expression1_constructor_args():
    sig = inspect.signature(myDsl_Expression1.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typeassertion_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeAssertion)


def test_mydsl_typeassertion_constructor_exists():
    assert callable(myDsl_TypeAssertion.__init__)


def test_mydsl_typeassertion_constructor_args():
    sig = inspect.signature(myDsl_TypeAssertion.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_unaryexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl_UnaryExpr)


def test_mydsl_unaryexpr_constructor_exists():
    assert callable(myDsl_UnaryExpr.__init__)


def test_mydsl_unaryexpr_constructor_args():
    sig = inspect.signature(myDsl_UnaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_receivertype_is_not_abstract():
    assert not inspect.isabstract(myDsl_ReceiverType)


def test_mydsl_receivertype_constructor_exists():
    assert callable(myDsl_ReceiverType.__init__)


def test_mydsl_receivertype_constructor_args():
    sig = inspect.signature(myDsl_ReceiverType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arguments_is_not_abstract():
    assert not inspect.isabstract(myDsl_Arguments)


def test_mydsl_arguments_constructor_exists():
    assert callable(myDsl_Arguments.__init__)


def test_mydsl_arguments_constructor_args():
    sig = inspect.signature(myDsl_Arguments.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_slice_is_not_abstract():
    assert not inspect.isabstract(myDsl_Slice)


def test_mydsl_slice_constructor_exists():
    assert callable(myDsl_Slice.__init__)


def test_mydsl_slice_constructor_args():
    sig = inspect.signature(myDsl_Slice.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_index_is_not_abstract():
    assert not inspect.isabstract(myDsl_Index)


def test_mydsl_index_constructor_exists():
    assert callable(myDsl_Index.__init__)


def test_mydsl_index_constructor_args():
    sig = inspect.signature(myDsl_Index.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_selector_is_not_abstract():
    assert not inspect.isabstract(myDsl_Selector)


def test_mydsl_selector_constructor_exists():
    assert callable(myDsl_Selector.__init__)


def test_mydsl_selector_constructor_args():
    sig = inspect.signature(myDsl_Selector.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_selector_has_id():
    assert hasattr(myDsl_Selector, "id")
    descriptor = None
    for klass in myDsl_Selector.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_methodexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl_MethodExpr)


def test_mydsl_methodexpr_constructor_exists():
    assert callable(myDsl_MethodExpr.__init__)


def test_mydsl_methodexpr_constructor_args():
    sig = inspect.signature(myDsl_MethodExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_conversion_is_not_abstract():
    assert not inspect.isabstract(myDsl_Conversion)


def test_mydsl_conversion_constructor_exists():
    assert callable(myDsl_Conversion.__init__)


def test_mydsl_conversion_constructor_args():
    sig = inspect.signature(myDsl_Conversion.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_primaryexprlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_PrimaryExprLinha)


def test_mydsl_primaryexprlinha_constructor_exists():
    assert callable(myDsl_PrimaryExprLinha.__init__)


def test_mydsl_primaryexprlinha_constructor_args():
    sig = inspect.signature(myDsl_PrimaryExprLinha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_primaryexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl_PrimaryExpr)


def test_mydsl_primaryexpr_constructor_exists():
    assert callable(myDsl_PrimaryExpr.__init__)


def test_mydsl_primaryexpr_constructor_args():
    sig = inspect.signature(myDsl_PrimaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_fieldname_is_not_abstract():
    assert not inspect.isabstract(myDsl_FieldName)


def test_mydsl_fieldname_constructor_exists():
    assert callable(myDsl_FieldName.__init__)


def test_mydsl_fieldname_constructor_args():
    sig = inspect.signature(myDsl_FieldName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_fieldname_has_id():
    assert hasattr(myDsl_FieldName, "id")
    descriptor = None
    for klass in myDsl_FieldName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_element_is_not_abstract():
    assert not inspect.isabstract(myDsl_Element)


def test_mydsl_element_constructor_exists():
    assert callable(myDsl_Element.__init__)


def test_mydsl_element_constructor_args():
    sig = inspect.signature(myDsl_Element.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_key_is_not_abstract():
    assert not inspect.isabstract(myDsl_Key)


def test_mydsl_key_constructor_exists():
    assert callable(myDsl_Key.__init__)


def test_mydsl_key_constructor_args():
    sig = inspect.signature(myDsl_Key.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_keyedelement_is_not_abstract():
    assert not inspect.isabstract(myDsl_KeyedElement)


def test_mydsl_keyedelement_constructor_exists():
    assert callable(myDsl_KeyedElement.__init__)


def test_mydsl_keyedelement_constructor_args():
    sig = inspect.signature(myDsl_KeyedElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_elementlist_is_not_abstract():
    assert not inspect.isabstract(myDsl_ElementList)


def test_mydsl_elementlist_constructor_exists():
    assert callable(myDsl_ElementList.__init__)


def test_mydsl_elementlist_constructor_args():
    sig = inspect.signature(myDsl_ElementList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_literaltypelinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_LiteralTypeLinha)


def test_mydsl_literaltypelinha_constructor_exists():
    assert callable(myDsl_LiteralTypeLinha.__init__)


def test_mydsl_literaltypelinha_constructor_args():
    sig = inspect.signature(myDsl_LiteralTypeLinha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_literalvalue_is_not_abstract():
    assert not inspect.isabstract(myDsl_LiteralValue)


def test_mydsl_literalvalue_constructor_exists():
    assert callable(myDsl_LiteralValue.__init__)


def test_mydsl_literalvalue_constructor_args():
    sig = inspect.signature(myDsl_LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_literaltype_is_not_abstract():
    assert not inspect.isabstract(myDsl_LiteralType)


def test_mydsl_literaltype_constructor_exists():
    assert callable(myDsl_LiteralType.__init__)


def test_mydsl_literaltype_constructor_args():
    sig = inspect.signature(myDsl_LiteralType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_functionlit_is_not_abstract():
    assert not inspect.isabstract(myDsl_FunctionLit)


def test_mydsl_functionlit_constructor_exists():
    assert callable(myDsl_FunctionLit.__init__)


def test_mydsl_functionlit_constructor_args():
    sig = inspect.signature(myDsl_FunctionLit.__init__)
    params = list(sig.parameters.keys())
    assert "func" in params, "Missing parameter 'func'"

def test_mydsl_functionlit_has_func():
    assert hasattr(myDsl_FunctionLit, "func")
    descriptor = None
    for klass in myDsl_FunctionLit.__mro__:
        if "func" in klass.__dict__:
            descriptor = klass.__dict__["func"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_compositelit_is_not_abstract():
    assert not inspect.isabstract(myDsl_CompositeLit)


def test_mydsl_compositelit_constructor_exists():
    assert callable(myDsl_CompositeLit.__init__)


def test_mydsl_compositelit_constructor_args():
    sig = inspect.signature(myDsl_CompositeLit.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_basiclit_is_not_abstract():
    assert not inspect.isabstract(myDsl_BasicLit)


def test_mydsl_basiclit_constructor_exists():
    assert callable(myDsl_BasicLit.__init__)


def test_mydsl_basiclit_constructor_args():
    sig = inspect.signature(myDsl_BasicLit.__init__)
    params = list(sig.parameters.keys())
    assert "int_lit" in params, "Missing parameter 'int_lit'"
    assert "imaginary_lit" in params, "Missing parameter 'imaginary_lit'"
    assert "rune_lit" in params, "Missing parameter 'rune_lit'"
    assert "float_lit" in params, "Missing parameter 'float_lit'"
    assert "string_lit" in params, "Missing parameter 'string_lit'"

def test_mydsl_basiclit_has_int_lit():
    assert hasattr(myDsl_BasicLit, "int_lit")
    descriptor = None
    for klass in myDsl_BasicLit.__mro__:
        if "int_lit" in klass.__dict__:
            descriptor = klass.__dict__["int_lit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_basiclit_has_imaginary_lit():
    assert hasattr(myDsl_BasicLit, "imaginary_lit")
    descriptor = None
    for klass in myDsl_BasicLit.__mro__:
        if "imaginary_lit" in klass.__dict__:
            descriptor = klass.__dict__["imaginary_lit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_basiclit_has_rune_lit():
    assert hasattr(myDsl_BasicLit, "rune_lit")
    descriptor = None
    for klass in myDsl_BasicLit.__mro__:
        if "rune_lit" in klass.__dict__:
            descriptor = klass.__dict__["rune_lit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_basiclit_has_float_lit():
    assert hasattr(myDsl_BasicLit, "float_lit")
    descriptor = None
    for klass in myDsl_BasicLit.__mro__:
        if "float_lit" in klass.__dict__:
            descriptor = klass.__dict__["float_lit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_basiclit_has_string_lit():
    assert hasattr(myDsl_BasicLit, "string_lit")
    descriptor = None
    for klass in myDsl_BasicLit.__mro__:
        if "string_lit" in klass.__dict__:
            descriptor = klass.__dict__["string_lit"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_operandname_is_not_abstract():
    assert not inspect.isabstract(myDsl_OperandName)


def test_mydsl_operandname_constructor_exists():
    assert callable(myDsl_OperandName.__init__)


def test_mydsl_operandname_constructor_args():
    sig = inspect.signature(myDsl_OperandName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_operandname_has_id():
    assert hasattr(myDsl_OperandName, "id")
    descriptor = None
    for klass in myDsl_OperandName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_literal_is_not_abstract():
    assert not inspect.isabstract(myDsl_Literal)


def test_mydsl_literal_constructor_exists():
    assert callable(myDsl_Literal.__init__)


def test_mydsl_literal_constructor_args():
    sig = inspect.signature(myDsl_Literal.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_operand_is_not_abstract():
    assert not inspect.isabstract(myDsl_Operand)


def test_mydsl_operand_constructor_exists():
    assert callable(myDsl_Operand.__init__)


def test_mydsl_operand_constructor_args():
    sig = inspect.signature(myDsl_Operand.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_receiver_is_not_abstract():
    assert not inspect.isabstract(myDsl_Receiver)


def test_mydsl_receiver_constructor_exists():
    assert callable(myDsl_Receiver.__init__)


def test_mydsl_receiver_constructor_args():
    sig = inspect.signature(myDsl_Receiver.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_functionbody_is_not_abstract():
    assert not inspect.isabstract(myDsl_FunctionBody)


def test_mydsl_functionbody_constructor_exists():
    assert callable(myDsl_FunctionBody.__init__)


def test_mydsl_functionbody_constructor_args():
    sig = inspect.signature(myDsl_FunctionBody.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_functionname_is_not_abstract():
    assert not inspect.isabstract(myDsl_FunctionName)


def test_mydsl_functionname_constructor_exists():
    assert callable(myDsl_FunctionName.__init__)


def test_mydsl_functionname_constructor_args():
    sig = inspect.signature(myDsl_FunctionName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_functionname_has_id():
    assert hasattr(myDsl_FunctionName, "id")
    descriptor = None
    for klass in myDsl_FunctionName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_shortvardecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_ShortVarDecl)


def test_mydsl_shortvardecl_constructor_exists():
    assert callable(myDsl_ShortVarDecl.__init__)


def test_mydsl_shortvardecl_constructor_args():
    sig = inspect.signature(myDsl_ShortVarDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_constspec_is_not_abstract():
    assert not inspect.isabstract(myDsl_ConstSpec)


def test_mydsl_constspec_constructor_exists():
    assert callable(myDsl_ConstSpec.__init__)


def test_mydsl_constspec_constructor_args():
    sig = inspect.signature(myDsl_ConstSpec.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_varspec_is_not_abstract():
    assert not inspect.isabstract(myDsl_VarSpec)


def test_mydsl_varspec_constructor_exists():
    assert callable(myDsl_VarSpec.__init__)


def test_mydsl_varspec_constructor_args():
    sig = inspect.signature(myDsl_VarSpec.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typedef_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeDef)


def test_mydsl_typedef_constructor_exists():
    assert callable(myDsl_TypeDef.__init__)


def test_mydsl_typedef_constructor_args():
    sig = inspect.signature(myDsl_TypeDef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_typedef_has_id():
    assert hasattr(myDsl_TypeDef, "id")
    descriptor = None
    for klass in myDsl_TypeDef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_aliasdecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_AliasDecl)


def test_mydsl_aliasdecl_constructor_exists():
    assert callable(myDsl_AliasDecl.__init__)


def test_mydsl_aliasdecl_constructor_args():
    sig = inspect.signature(myDsl_AliasDecl.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_aliasdecl_has_id():
    assert hasattr(myDsl_AliasDecl, "id")
    descriptor = None
    for klass in myDsl_AliasDecl.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_typespec_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeSpec)


def test_mydsl_typespec_constructor_exists():
    assert callable(myDsl_TypeSpec.__init__)


def test_mydsl_typespec_constructor_args():
    sig = inspect.signature(myDsl_TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expressionlist_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExpressionList)


def test_mydsl_expressionlist_constructor_exists():
    assert callable(myDsl_ExpressionList.__init__)


def test_mydsl_expressionlist_constructor_args():
    sig = inspect.signature(myDsl_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_channeltypelinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_ChannelTypeLinha)


def test_mydsl_channeltypelinha_constructor_exists():
    assert callable(myDsl_ChannelTypeLinha.__init__)


def test_mydsl_channeltypelinha_constructor_args():
    sig = inspect.signature(myDsl_ChannelTypeLinha.__init__)
    params = list(sig.parameters.keys())
    assert "aNY_OTHER" in params, "Missing parameter 'aNY_OTHER'"

def test_mydsl_channeltypelinha_has_aNY_OTHER():
    assert hasattr(myDsl_ChannelTypeLinha, "aNY_OTHER")
    descriptor = None
    for klass in myDsl_ChannelTypeLinha.__mro__:
        if "aNY_OTHER" in klass.__dict__:
            descriptor = klass.__dict__["aNY_OTHER"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_methoddecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_MethodDecl)


def test_mydsl_methoddecl_constructor_exists():
    assert callable(myDsl_MethodDecl.__init__)


def test_mydsl_methoddecl_constructor_args():
    sig = inspect.signature(myDsl_MethodDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_functiondecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_FunctionDecl)


def test_mydsl_functiondecl_constructor_exists():
    assert callable(myDsl_FunctionDecl.__init__)


def test_mydsl_functiondecl_constructor_args():
    sig = inspect.signature(myDsl_FunctionDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_topleveldecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_TopLevelDecl)


def test_mydsl_topleveldecl_constructor_exists():
    assert callable(myDsl_TopLevelDecl.__init__)


def test_mydsl_topleveldecl_constructor_args():
    sig = inspect.signature(myDsl_TopLevelDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_vardecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_VarDecl)


def test_mydsl_vardecl_constructor_exists():
    assert callable(myDsl_VarDecl.__init__)


def test_mydsl_vardecl_constructor_args():
    sig = inspect.signature(myDsl_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_mydsl_vardecl_has_var():
    assert hasattr(myDsl_VarDecl, "var")
    descriptor = None
    for klass in myDsl_VarDecl.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_typedecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeDecl)


def test_mydsl_typedecl_constructor_exists():
    assert callable(myDsl_TypeDecl.__init__)


def test_mydsl_typedecl_constructor_args():
    sig = inspect.signature(myDsl_TypeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "typekeyword" in params, "Missing parameter 'typekeyword'"

def test_mydsl_typedecl_has_typekeyword():
    assert hasattr(myDsl_TypeDecl, "typekeyword")
    descriptor = None
    for klass in myDsl_TypeDecl.__mro__:
        if "typekeyword" in klass.__dict__:
            descriptor = klass.__dict__["typekeyword"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_constdecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_ConstDecl)


def test_mydsl_constdecl_constructor_exists():
    assert callable(myDsl_ConstDecl.__init__)


def test_mydsl_constdecl_constructor_args():
    sig = inspect.signature(myDsl_ConstDecl.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"

def test_mydsl_constdecl_has_const():
    assert hasattr(myDsl_ConstDecl, "const")
    descriptor = None
    for klass in myDsl_ConstDecl.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl_Declaration)


def test_mydsl_declaration_constructor_exists():
    assert callable(myDsl_Declaration.__init__)


def test_mydsl_declaration_constructor_args():
    sig = inspect.signature(myDsl_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_statement_is_not_abstract():
    assert not inspect.isabstract(myDsl_Statement)


def test_mydsl_statement_constructor_exists():
    assert callable(myDsl_Statement.__init__)


def test_mydsl_statement_constructor_args():
    sig = inspect.signature(myDsl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_statementlist_is_not_abstract():
    assert not inspect.isabstract(myDsl_StatementList)


def test_mydsl_statementlist_constructor_exists():
    assert callable(myDsl_StatementList.__init__)


def test_mydsl_statementlist_constructor_args():
    sig = inspect.signature(myDsl_StatementList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_block_is_not_abstract():
    assert not inspect.isabstract(myDsl_Block)


def test_mydsl_block_constructor_exists():
    assert callable(myDsl_Block.__init__)


def test_mydsl_block_constructor_args():
    sig = inspect.signature(myDsl_Block.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_result_is_not_abstract():
    assert not inspect.isabstract(myDsl_Result)


def test_mydsl_result_constructor_exists():
    assert callable(myDsl_Result.__init__)


def test_mydsl_result_constructor_args():
    sig = inspect.signature(myDsl_Result.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_keytype_is_not_abstract():
    assert not inspect.isabstract(myDsl_KeyType)


def test_mydsl_keytype_constructor_exists():
    assert callable(myDsl_KeyType.__init__)


def test_mydsl_keytype_constructor_args():
    sig = inspect.signature(myDsl_KeyType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_interfacetypename_is_not_abstract():
    assert not inspect.isabstract(myDsl_InterfaceTypeName)


def test_mydsl_interfacetypename_constructor_exists():
    assert callable(myDsl_InterfaceTypeName.__init__)


def test_mydsl_interfacetypename_constructor_args():
    sig = inspect.signature(myDsl_InterfaceTypeName.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_methodname_is_not_abstract():
    assert not inspect.isabstract(myDsl_MethodName)


def test_mydsl_methodname_constructor_exists():
    assert callable(myDsl_MethodName.__init__)


def test_mydsl_methodname_constructor_args():
    sig = inspect.signature(myDsl_MethodName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_methodname_has_id():
    assert hasattr(myDsl_MethodName, "id")
    descriptor = None
    for klass in myDsl_MethodName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_methodspec_is_not_abstract():
    assert not inspect.isabstract(myDsl_MethodSpec)


def test_mydsl_methodspec_constructor_exists():
    assert callable(myDsl_MethodSpec.__init__)


def test_mydsl_methodspec_constructor_args():
    sig = inspect.signature(myDsl_MethodSpec.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameterdecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_ParameterDecl)


def test_mydsl_parameterdecl_constructor_exists():
    assert callable(myDsl_ParameterDecl.__init__)


def test_mydsl_parameterdecl_constructor_args():
    sig = inspect.signature(myDsl_ParameterDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_parameterlist_is_not_abstract():
    assert not inspect.isabstract(myDsl_ParameterList)


def test_mydsl_parameterlist_constructor_exists():
    assert callable(myDsl_ParameterList.__init__)


def test_mydsl_parameterlist_constructor_args():
    sig = inspect.signature(myDsl_ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_channeltype_is_not_abstract():
    assert not inspect.isabstract(myDsl_ChannelType)


def test_mydsl_channeltype_constructor_exists():
    assert callable(myDsl_ChannelType.__init__)


def test_mydsl_channeltype_constructor_args():
    sig = inspect.signature(myDsl_ChannelType.__init__)
    params = list(sig.parameters.keys())
    assert "chan" in params, "Missing parameter 'chan'"

def test_mydsl_channeltype_has_chan():
    assert hasattr(myDsl_ChannelType, "chan")
    descriptor = None
    for klass in myDsl_ChannelType.__mro__:
        if "chan" in klass.__dict__:
            descriptor = klass.__dict__["chan"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_parameters_is_not_abstract():
    assert not inspect.isabstract(myDsl_Parameters)


def test_mydsl_parameters_constructor_exists():
    assert callable(myDsl_Parameters.__init__)


def test_mydsl_parameters_constructor_args():
    sig = inspect.signature(myDsl_Parameters.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_signature_is_not_abstract():
    assert not inspect.isabstract(myDsl_Signature)


def test_mydsl_signature_constructor_exists():
    assert callable(myDsl_Signature.__init__)


def test_mydsl_signature_constructor_args():
    sig = inspect.signature(myDsl_Signature.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_basetype_is_not_abstract():
    assert not inspect.isabstract(myDsl_BaseType)


def test_mydsl_basetype_constructor_exists():
    assert callable(myDsl_BaseType.__init__)


def test_mydsl_basetype_constructor_args():
    sig = inspect.signature(myDsl_BaseType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_tag_is_not_abstract():
    assert not inspect.isabstract(myDsl_Tag)


def test_mydsl_tag_constructor_exists():
    assert callable(myDsl_Tag.__init__)


def test_mydsl_tag_constructor_args():
    sig = inspect.signature(myDsl_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "string_lit" in params, "Missing parameter 'string_lit'"

def test_mydsl_tag_has_string_lit():
    assert hasattr(myDsl_Tag, "string_lit")
    descriptor = None
    for klass in myDsl_Tag.__mro__:
        if "string_lit" in klass.__dict__:
            descriptor = klass.__dict__["string_lit"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_embeddedfield_is_not_abstract():
    assert not inspect.isabstract(myDsl_EmbeddedField)


def test_mydsl_embeddedfield_constructor_exists():
    assert callable(myDsl_EmbeddedField.__init__)


def test_mydsl_embeddedfield_constructor_args():
    sig = inspect.signature(myDsl_EmbeddedField.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_identifierlist_is_not_abstract():
    assert not inspect.isabstract(myDsl_IdentifierList)


def test_mydsl_identifierlist_constructor_exists():
    assert callable(myDsl_IdentifierList.__init__)


def test_mydsl_identifierlist_constructor_args():
    sig = inspect.signature(myDsl_IdentifierList.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "id1" in params, "Missing parameter 'id1'"

def test_mydsl_identifierlist_has_id():
    assert hasattr(myDsl_IdentifierList, "id")
    descriptor = None
    for klass in myDsl_IdentifierList.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_identifierlist_has_id1():
    assert hasattr(myDsl_IdentifierList, "id1")
    descriptor = None
    for klass in myDsl_IdentifierList.__mro__:
        if "id1" in klass.__dict__:
            descriptor = klass.__dict__["id1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_fielddecl_is_not_abstract():
    assert not inspect.isabstract(myDsl_FieldDecl)


def test_mydsl_fielddecl_constructor_exists():
    assert callable(myDsl_FieldDecl.__init__)


def test_mydsl_fielddecl_constructor_args():
    sig = inspect.signature(myDsl_FieldDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_Expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_elementtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_ElementType)


def test_mydsl_elementtype_constructor_exists():
    assert callable(myDsl_ElementType.__init__)


def test_mydsl_elementtype_constructor_args():
    sig = inspect.signature(myDsl_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arraylength_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArrayLength)


def test_mydsl_arraylength_constructor_exists():
    assert callable(myDsl_ArrayLength.__init__)


def test_mydsl_arraylength_constructor_args():
    sig = inspect.signature(myDsl_ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_maptype_is_not_abstract():
    assert not inspect.isabstract(myDsl_MapType)


def test_mydsl_maptype_constructor_exists():
    assert callable(myDsl_MapType.__init__)


def test_mydsl_maptype_constructor_args():
    sig = inspect.signature(myDsl_MapType.__init__)
    params = list(sig.parameters.keys())
    assert "map" in params, "Missing parameter 'map'"

def test_mydsl_maptype_has_map():
    assert hasattr(myDsl_MapType, "map")
    descriptor = None
    for klass in myDsl_MapType.__mro__:
        if "map" in klass.__dict__:
            descriptor = klass.__dict__["map"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_interfacetype_is_not_abstract():
    assert not inspect.isabstract(myDsl_InterfaceType)


def test_mydsl_interfacetype_constructor_exists():
    assert callable(myDsl_InterfaceType.__init__)


def test_mydsl_interfacetype_constructor_args():
    sig = inspect.signature(myDsl_InterfaceType.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_mydsl_interfacetype_has_interface():
    assert hasattr(myDsl_InterfaceType, "interface")
    descriptor = None
    for klass in myDsl_InterfaceType.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_functiontype_is_not_abstract():
    assert not inspect.isabstract(myDsl_FunctionType)


def test_mydsl_functiontype_constructor_exists():
    assert callable(myDsl_FunctionType.__init__)


def test_mydsl_functiontype_constructor_args():
    sig = inspect.signature(myDsl_FunctionType.__init__)
    params = list(sig.parameters.keys())
    assert "func" in params, "Missing parameter 'func'"

def test_mydsl_functiontype_has_func():
    assert hasattr(myDsl_FunctionType, "func")
    descriptor = None
    for klass in myDsl_FunctionType.__mro__:
        if "func" in klass.__dict__:
            descriptor = klass.__dict__["func"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_pointertype_is_not_abstract():
    assert not inspect.isabstract(myDsl_PointerType)


def test_mydsl_pointertype_constructor_exists():
    assert callable(myDsl_PointerType.__init__)


def test_mydsl_pointertype_constructor_args():
    sig = inspect.signature(myDsl_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_structtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_StructType)


def test_mydsl_structtype_constructor_exists():
    assert callable(myDsl_StructType.__init__)


def test_mydsl_structtype_constructor_args():
    sig = inspect.signature(myDsl_StructType.__init__)
    params = list(sig.parameters.keys())
    assert "struct" in params, "Missing parameter 'struct'"

def test_mydsl_structtype_has_struct():
    assert hasattr(myDsl_StructType, "struct")
    descriptor = None
    for klass in myDsl_StructType.__mro__:
        if "struct" in klass.__dict__:
            descriptor = klass.__dict__["struct"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_typelitlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeLitLinha)


def test_mydsl_typelitlinha_constructor_exists():
    assert callable(myDsl_TypeLitLinha.__init__)


def test_mydsl_typelitlinha_constructor_args():
    sig = inspect.signature(myDsl_TypeLitLinha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typenamelinha_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeNameLinha)


def test_mydsl_typenamelinha_constructor_exists():
    assert callable(myDsl_TypeNameLinha.__init__)


def test_mydsl_typenamelinha_constructor_args():
    sig = inspect.signature(myDsl_TypeNameLinha.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_typenamelinha_has_id():
    assert hasattr(myDsl_TypeNameLinha, "id")
    descriptor = None
    for klass in myDsl_TypeNameLinha.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_typelit_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeLit)


def test_mydsl_typelit_constructor_exists():
    assert callable(myDsl_TypeLit.__init__)


def test_mydsl_typelit_constructor_args():
    sig = inspect.signature(myDsl_TypeLit.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_typename_is_not_abstract():
    assert not inspect.isabstract(myDsl_TypeName)


def test_mydsl_typename_constructor_exists():
    assert callable(myDsl_TypeName.__init__)


def test_mydsl_typename_constructor_args():
    sig = inspect.signature(myDsl_TypeName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl_typename_has_id():
    assert hasattr(myDsl_TypeName, "id")
    descriptor = None
    for klass in myDsl_TypeName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_type_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type)


def test_mydsl_type_constructor_exists():
    assert callable(myDsl_Type.__init__)


def test_mydsl_type_constructor_args():
    sig = inspect.signature(myDsl_Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_sourcefile_is_not_abstract():
    assert not inspect.isabstract(myDsl_SourceFile)


def test_mydsl_sourcefile_constructor_exists():
    assert callable(myDsl_SourceFile.__init__)


def test_mydsl_sourcefile_constructor_args():
    sig = inspect.signature(myDsl_SourceFile.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
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
myDsl_ImportSpec_strategy = st.builds(
    myDsl_ImportSpec,
    sTRING_LIT=
        safe_text
)
myDsl_PackageName_strategy = st.builds(
    myDsl_PackageName,
    id=
        safe_text
)
myDsl_ImportDecl_strategy = st.builds(
    myDsl_ImportDecl,
    importt=
        safe_text
)
myDsl_PackageClause_strategy = st.builds(
    myDsl_PackageClause,
    package=
        safe_text
)
myDsl_RecvExpr_strategy = st.builds(
    myDsl_RecvExpr,
)
myDsl_CommCaseLinha_strategy = st.builds(
    myDsl_CommCaseLinha,
)
myDsl_CommCase_strategy = st.builds(
    myDsl_CommCase,
    case=
        safe_text,
    default=
        safe_text
)
myDsl_CommClause_strategy = st.builds(
    myDsl_CommClause,
)
myDsl_ForStmtLinhaLinha_strategy = st.builds(
    myDsl_ForStmtLinhaLinha,
    range=
        safe_text
)
myDsl_PostStmt_strategy = st.builds(
    myDsl_PostStmt,
)
myDsl_Condition_strategy = st.builds(
    myDsl_Condition,
)
myDsl_ForStmtLinha_strategy = st.builds(
    myDsl_ForStmtLinha,
    vazio=
        safe_text
)
myDsl_TypeList_strategy = st.builds(
    myDsl_TypeList,
)
myDsl_TypeSwitchCase_strategy = st.builds(
    myDsl_TypeSwitchCase,
    case=
        safe_text,
    default=
        safe_text
)
myDsl_TypeCaseClause_strategy = st.builds(
    myDsl_TypeCaseClause,
)
myDsl_TypeSwitchGuard_strategy = st.builds(
    myDsl_TypeSwitchGuard,
    id=
        safe_text,
    type=
        safe_text
)
myDsl_ExprSwitchCase_strategy = st.builds(
    myDsl_ExprSwitchCase,
    default=
        safe_text,
    case=
        safe_text
)
myDsl_ExprCaseClause_strategy = st.builds(
    myDsl_ExprCaseClause,
)
myDsl_TypeSwitchStmt_strategy = st.builds(
    myDsl_TypeSwitchStmt,
    switch=
        safe_text
)
myDsl_ExprSwitchStmt_strategy = st.builds(
    myDsl_ExprSwitchStmt,
    switch=
        safe_text
)
myDsl_IfStmtLinha_strategy = st.builds(
    myDsl_IfStmtLinha,
    else_=
        safe_text
)
myDsl_Label_strategy = st.builds(
    myDsl_Label,
    id=
        safe_text
)
myDsl_assign_op_strategy = st.builds(
    myDsl_assign_op,
    mUL_OP=
        safe_text,
    aDD_OP=
        safe_text
)
myDsl_SimpleStmtLinha_strategy = st.builds(
    myDsl_SimpleStmtLinha,
    aNY_OTHER=
        safe_text
)
myDsl_EmptyStmt_strategy = st.builds(
    myDsl_EmptyStmt,
    aNY_OTHER=
        safe_text
)
myDsl_DeferStmt_strategy = st.builds(
    myDsl_DeferStmt,
    defer=
        safe_text
)
myDsl_ForStmt_strategy = st.builds(
    myDsl_ForStmt,
    range=
        safe_text,
    for_=
        safe_text
)
myDsl_SelectStmt_strategy = st.builds(
    myDsl_SelectStmt,
    select=
        safe_text
)
myDsl_SwitchStmt_strategy = st.builds(
    myDsl_SwitchStmt,
)
myDsl_IfStmt_strategy = st.builds(
    myDsl_IfStmt,
    else_=
        safe_text,
    if_=
        safe_text
)
myDsl_Expression_Linha_strategy = st.builds(
    myDsl_Expression_Linha,
)
myDsl_FallthroughStmt_strategy = st.builds(
    myDsl_FallthroughStmt,
    fallthrough=
        safe_text
)
myDsl_GotoStmt_strategy = st.builds(
    myDsl_GotoStmt,
    goto=
        safe_text
)
myDsl_ContinueStmt_strategy = st.builds(
    myDsl_ContinueStmt,
    continue_=
        safe_text
)
myDsl_BreakStmt_strategy = st.builds(
    myDsl_BreakStmt,
    break_=
        safe_text
)
myDsl_ReturnStmt_strategy = st.builds(
    myDsl_ReturnStmt,
    return_=
        safe_text
)
myDsl_GoStmt_strategy = st.builds(
    myDsl_GoStmt,
    go=
        safe_text
)
myDsl_SimpleStmt_strategy = st.builds(
    myDsl_SimpleStmt,
)
myDsl_LabeledStmt_strategy = st.builds(
    myDsl_LabeledStmt,
)
myDsl_BINARY_OP_strategy = st.builds(
    myDsl_BINARY_OP,
    rEL_OP=
        safe_text,
    aDD_OP=
        safe_text
)
myDsl_Expression1_strategy = st.builds(
    myDsl_Expression1,
)
myDsl_TypeAssertion_strategy = st.builds(
    myDsl_TypeAssertion,
)
myDsl_UnaryExpr_strategy = st.builds(
    myDsl_UnaryExpr,
)
myDsl_ReceiverType_strategy = st.builds(
    myDsl_ReceiverType,
)
myDsl_Arguments_strategy = st.builds(
    myDsl_Arguments,
)
myDsl_Slice_strategy = st.builds(
    myDsl_Slice,
)
myDsl_Index_strategy = st.builds(
    myDsl_Index,
)
myDsl_Selector_strategy = st.builds(
    myDsl_Selector,
    id=
        safe_text
)
myDsl_MethodExpr_strategy = st.builds(
    myDsl_MethodExpr,
)
myDsl_Conversion_strategy = st.builds(
    myDsl_Conversion,
)
myDsl_PrimaryExprLinha_strategy = st.builds(
    myDsl_PrimaryExprLinha,
)
myDsl_PrimaryExpr_strategy = st.builds(
    myDsl_PrimaryExpr,
)
myDsl_FieldName_strategy = st.builds(
    myDsl_FieldName,
    id=
        safe_text
)
myDsl_Element_strategy = st.builds(
    myDsl_Element,
)
myDsl_Key_strategy = st.builds(
    myDsl_Key,
)
myDsl_KeyedElement_strategy = st.builds(
    myDsl_KeyedElement,
)
myDsl_ElementList_strategy = st.builds(
    myDsl_ElementList,
)
myDsl_LiteralTypeLinha_strategy = st.builds(
    myDsl_LiteralTypeLinha,
)
myDsl_LiteralValue_strategy = st.builds(
    myDsl_LiteralValue,
)
myDsl_LiteralType_strategy = st.builds(
    myDsl_LiteralType,
)
myDsl_FunctionLit_strategy = st.builds(
    myDsl_FunctionLit,
    func=
        safe_text
)
myDsl_CompositeLit_strategy = st.builds(
    myDsl_CompositeLit,
)
myDsl_BasicLit_strategy = st.builds(
    myDsl_BasicLit,
    int_lit=
        safe_text,
    imaginary_lit=
        safe_text,
    rune_lit=
        safe_text,
    float_lit=
        safe_text,
    string_lit=
        safe_text
)
myDsl_OperandName_strategy = st.builds(
    myDsl_OperandName,
    id=
        safe_text
)
myDsl_Literal_strategy = st.builds(
    myDsl_Literal,
)
myDsl_Operand_strategy = st.builds(
    myDsl_Operand,
)
myDsl_Receiver_strategy = st.builds(
    myDsl_Receiver,
)
myDsl_FunctionBody_strategy = st.builds(
    myDsl_FunctionBody,
)
myDsl_FunctionName_strategy = st.builds(
    myDsl_FunctionName,
    id=
        safe_text
)
myDsl_ShortVarDecl_strategy = st.builds(
    myDsl_ShortVarDecl,
)
myDsl_ConstSpec_strategy = st.builds(
    myDsl_ConstSpec,
)
myDsl_VarSpec_strategy = st.builds(
    myDsl_VarSpec,
)
myDsl_TypeDef_strategy = st.builds(
    myDsl_TypeDef,
    id=
        safe_text
)
myDsl_AliasDecl_strategy = st.builds(
    myDsl_AliasDecl,
    id=
        safe_text
)
myDsl_TypeSpec_strategy = st.builds(
    myDsl_TypeSpec,
)
myDsl_ExpressionList_strategy = st.builds(
    myDsl_ExpressionList,
)
myDsl_ChannelTypeLinha_strategy = st.builds(
    myDsl_ChannelTypeLinha,
    aNY_OTHER=
        safe_text
)
myDsl_MethodDecl_strategy = st.builds(
    myDsl_MethodDecl,
)
myDsl_FunctionDecl_strategy = st.builds(
    myDsl_FunctionDecl,
)
myDsl_TopLevelDecl_strategy = st.builds(
    myDsl_TopLevelDecl,
)
myDsl_VarDecl_strategy = st.builds(
    myDsl_VarDecl,
    var=
        safe_text
)
myDsl_TypeDecl_strategy = st.builds(
    myDsl_TypeDecl,
    typekeyword=
        safe_text
)
myDsl_ConstDecl_strategy = st.builds(
    myDsl_ConstDecl,
    const=
        safe_text
)
myDsl_Declaration_strategy = st.builds(
    myDsl_Declaration,
)
myDsl_Statement_strategy = st.builds(
    myDsl_Statement,
)
myDsl_StatementList_strategy = st.builds(
    myDsl_StatementList,
)
myDsl_Block_strategy = st.builds(
    myDsl_Block,
)
myDsl_Result_strategy = st.builds(
    myDsl_Result,
)
myDsl_KeyType_strategy = st.builds(
    myDsl_KeyType,
)
myDsl_InterfaceTypeName_strategy = st.builds(
    myDsl_InterfaceTypeName,
)
myDsl_MethodName_strategy = st.builds(
    myDsl_MethodName,
    id=
        safe_text
)
myDsl_MethodSpec_strategy = st.builds(
    myDsl_MethodSpec,
)
myDsl_ParameterDecl_strategy = st.builds(
    myDsl_ParameterDecl,
)
myDsl_ParameterList_strategy = st.builds(
    myDsl_ParameterList,
)
myDsl_ChannelType_strategy = st.builds(
    myDsl_ChannelType,
    chan=
        safe_text
)
myDsl_Parameters_strategy = st.builds(
    myDsl_Parameters,
)
myDsl_Signature_strategy = st.builds(
    myDsl_Signature,
)
myDsl_BaseType_strategy = st.builds(
    myDsl_BaseType,
)
myDsl_Tag_strategy = st.builds(
    myDsl_Tag,
    string_lit=
        safe_text
)
myDsl_EmbeddedField_strategy = st.builds(
    myDsl_EmbeddedField,
)
myDsl_IdentifierList_strategy = st.builds(
    myDsl_IdentifierList,
    id=
        safe_text,
    id1=
        safe_text
)
myDsl_FieldDecl_strategy = st.builds(
    myDsl_FieldDecl,
)
myDsl_Expression_strategy = st.builds(
    myDsl_Expression,
)
myDsl_ElementType_strategy = st.builds(
    myDsl_ElementType,
)
myDsl_ArrayLength_strategy = st.builds(
    myDsl_ArrayLength,
)
myDsl_MapType_strategy = st.builds(
    myDsl_MapType,
    map=
        safe_text
)
myDsl_InterfaceType_strategy = st.builds(
    myDsl_InterfaceType,
    interface=
        safe_text
)
myDsl_FunctionType_strategy = st.builds(
    myDsl_FunctionType,
    func=
        safe_text
)
myDsl_PointerType_strategy = st.builds(
    myDsl_PointerType,
)
myDsl_StructType_strategy = st.builds(
    myDsl_StructType,
    struct=
        safe_text
)
myDsl_TypeLitLinha_strategy = st.builds(
    myDsl_TypeLitLinha,
)
myDsl_TypeNameLinha_strategy = st.builds(
    myDsl_TypeNameLinha,
    id=
        safe_text
)
myDsl_TypeLit_strategy = st.builds(
    myDsl_TypeLit,
)
myDsl_TypeName_strategy = st.builds(
    myDsl_TypeName,
    id=
        safe_text
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
)
myDsl_SourceFile_strategy = st.builds(
    myDsl_SourceFile,
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=myDsl_ImportSpec_strategy)
@settings(max_examples=50)
def test_mydsl_importspec_instantiation(instance):
    assert isinstance(instance, myDsl_ImportSpec)



@given(instance=myDsl_ImportSpec_strategy)
def test_mydsl_importspec_sTRING_LIT_setter(instance):
    original = instance.sTRING_LIT
    instance.sTRING_LIT = original
    assert instance.sTRING_LIT == original

@given(instance=myDsl_PackageName_strategy)
@settings(max_examples=50)
def test_mydsl_packagename_instantiation(instance):
    assert isinstance(instance, myDsl_PackageName)



@given(instance=myDsl_PackageName_strategy)
def test_mydsl_packagename_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_ImportDecl_strategy)
@settings(max_examples=50)
def test_mydsl_importdecl_instantiation(instance):
    assert isinstance(instance, myDsl_ImportDecl)



@given(instance=myDsl_ImportDecl_strategy)
def test_mydsl_importdecl_importt_setter(instance):
    original = instance.importt
    instance.importt = original
    assert instance.importt == original

@given(instance=myDsl_PackageClause_strategy)
@settings(max_examples=50)
def test_mydsl_packageclause_instantiation(instance):
    assert isinstance(instance, myDsl_PackageClause)



@given(instance=myDsl_PackageClause_strategy)
def test_mydsl_packageclause_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=myDsl_RecvExpr_strategy)
@settings(max_examples=50)
def test_mydsl_recvexpr_instantiation(instance):
    assert isinstance(instance, myDsl_RecvExpr)

@given(instance=myDsl_CommCaseLinha_strategy)
@settings(max_examples=50)
def test_mydsl_commcaselinha_instantiation(instance):
    assert isinstance(instance, myDsl_CommCaseLinha)

@given(instance=myDsl_CommCase_strategy)
@settings(max_examples=50)
def test_mydsl_commcase_instantiation(instance):
    assert isinstance(instance, myDsl_CommCase)



@given(instance=myDsl_CommCase_strategy)
def test_mydsl_commcase_case_setter(instance):
    original = instance.case
    instance.case = original
    assert instance.case == original



@given(instance=myDsl_CommCase_strategy)
def test_mydsl_commcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=myDsl_CommClause_strategy)
@settings(max_examples=50)
def test_mydsl_commclause_instantiation(instance):
    assert isinstance(instance, myDsl_CommClause)

@given(instance=myDsl_ForStmtLinhaLinha_strategy)
@settings(max_examples=50)
def test_mydsl_forstmtlinhalinha_instantiation(instance):
    assert isinstance(instance, myDsl_ForStmtLinhaLinha)



@given(instance=myDsl_ForStmtLinhaLinha_strategy)
def test_mydsl_forstmtlinhalinha_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=myDsl_PostStmt_strategy)
@settings(max_examples=50)
def test_mydsl_poststmt_instantiation(instance):
    assert isinstance(instance, myDsl_PostStmt)

@given(instance=myDsl_Condition_strategy)
@settings(max_examples=50)
def test_mydsl_condition_instantiation(instance):
    assert isinstance(instance, myDsl_Condition)

@given(instance=myDsl_ForStmtLinha_strategy)
@settings(max_examples=50)
def test_mydsl_forstmtlinha_instantiation(instance):
    assert isinstance(instance, myDsl_ForStmtLinha)



@given(instance=myDsl_ForStmtLinha_strategy)
def test_mydsl_forstmtlinha_vazio_setter(instance):
    original = instance.vazio
    instance.vazio = original
    assert instance.vazio == original

@given(instance=myDsl_TypeList_strategy)
@settings(max_examples=50)
def test_mydsl_typelist_instantiation(instance):
    assert isinstance(instance, myDsl_TypeList)

@given(instance=myDsl_TypeSwitchCase_strategy)
@settings(max_examples=50)
def test_mydsl_typeswitchcase_instantiation(instance):
    assert isinstance(instance, myDsl_TypeSwitchCase)



@given(instance=myDsl_TypeSwitchCase_strategy)
def test_mydsl_typeswitchcase_case_setter(instance):
    original = instance.case
    instance.case = original
    assert instance.case == original



@given(instance=myDsl_TypeSwitchCase_strategy)
def test_mydsl_typeswitchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=myDsl_TypeCaseClause_strategy)
@settings(max_examples=50)
def test_mydsl_typecaseclause_instantiation(instance):
    assert isinstance(instance, myDsl_TypeCaseClause)

@given(instance=myDsl_TypeSwitchGuard_strategy)
@settings(max_examples=50)
def test_mydsl_typeswitchguard_instantiation(instance):
    assert isinstance(instance, myDsl_TypeSwitchGuard)



@given(instance=myDsl_TypeSwitchGuard_strategy)
def test_mydsl_typeswitchguard_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=myDsl_TypeSwitchGuard_strategy)
def test_mydsl_typeswitchguard_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl_ExprSwitchCase_strategy)
@settings(max_examples=50)
def test_mydsl_exprswitchcase_instantiation(instance):
    assert isinstance(instance, myDsl_ExprSwitchCase)



@given(instance=myDsl_ExprSwitchCase_strategy)
def test_mydsl_exprswitchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=myDsl_ExprSwitchCase_strategy)
def test_mydsl_exprswitchcase_case_setter(instance):
    original = instance.case
    instance.case = original
    assert instance.case == original

@given(instance=myDsl_ExprCaseClause_strategy)
@settings(max_examples=50)
def test_mydsl_exprcaseclause_instantiation(instance):
    assert isinstance(instance, myDsl_ExprCaseClause)

@given(instance=myDsl_TypeSwitchStmt_strategy)
@settings(max_examples=50)
def test_mydsl_typeswitchstmt_instantiation(instance):
    assert isinstance(instance, myDsl_TypeSwitchStmt)



@given(instance=myDsl_TypeSwitchStmt_strategy)
def test_mydsl_typeswitchstmt_switch_setter(instance):
    original = instance.switch
    instance.switch = original
    assert instance.switch == original

@given(instance=myDsl_ExprSwitchStmt_strategy)
@settings(max_examples=50)
def test_mydsl_exprswitchstmt_instantiation(instance):
    assert isinstance(instance, myDsl_ExprSwitchStmt)



@given(instance=myDsl_ExprSwitchStmt_strategy)
def test_mydsl_exprswitchstmt_switch_setter(instance):
    original = instance.switch
    instance.switch = original
    assert instance.switch == original

@given(instance=myDsl_IfStmtLinha_strategy)
@settings(max_examples=50)
def test_mydsl_ifstmtlinha_instantiation(instance):
    assert isinstance(instance, myDsl_IfStmtLinha)



@given(instance=myDsl_IfStmtLinha_strategy)
def test_mydsl_ifstmtlinha_else__setter(instance):
    original = instance.else_
    instance.else_ = original
    assert instance.else_ == original

@given(instance=myDsl_Label_strategy)
@settings(max_examples=50)
def test_mydsl_label_instantiation(instance):
    assert isinstance(instance, myDsl_Label)



@given(instance=myDsl_Label_strategy)
def test_mydsl_label_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_assign_op_strategy)
@settings(max_examples=50)
def test_mydsl_assign_op_instantiation(instance):
    assert isinstance(instance, myDsl_assign_op)



@given(instance=myDsl_assign_op_strategy)
def test_mydsl_assign_op_mUL_OP_setter(instance):
    original = instance.mUL_OP
    instance.mUL_OP = original
    assert instance.mUL_OP == original



@given(instance=myDsl_assign_op_strategy)
def test_mydsl_assign_op_aDD_OP_setter(instance):
    original = instance.aDD_OP
    instance.aDD_OP = original
    assert instance.aDD_OP == original

@given(instance=myDsl_SimpleStmtLinha_strategy)
@settings(max_examples=50)
def test_mydsl_simplestmtlinha_instantiation(instance):
    assert isinstance(instance, myDsl_SimpleStmtLinha)



@given(instance=myDsl_SimpleStmtLinha_strategy)
def test_mydsl_simplestmtlinha_aNY_OTHER_setter(instance):
    original = instance.aNY_OTHER
    instance.aNY_OTHER = original
    assert instance.aNY_OTHER == original

@given(instance=myDsl_EmptyStmt_strategy)
@settings(max_examples=50)
def test_mydsl_emptystmt_instantiation(instance):
    assert isinstance(instance, myDsl_EmptyStmt)



@given(instance=myDsl_EmptyStmt_strategy)
def test_mydsl_emptystmt_aNY_OTHER_setter(instance):
    original = instance.aNY_OTHER
    instance.aNY_OTHER = original
    assert instance.aNY_OTHER == original

@given(instance=myDsl_DeferStmt_strategy)
@settings(max_examples=50)
def test_mydsl_deferstmt_instantiation(instance):
    assert isinstance(instance, myDsl_DeferStmt)



@given(instance=myDsl_DeferStmt_strategy)
def test_mydsl_deferstmt_defer_setter(instance):
    original = instance.defer
    instance.defer = original
    assert instance.defer == original

@given(instance=myDsl_ForStmt_strategy)
@settings(max_examples=50)
def test_mydsl_forstmt_instantiation(instance):
    assert isinstance(instance, myDsl_ForStmt)



@given(instance=myDsl_ForStmt_strategy)
def test_mydsl_forstmt_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original



@given(instance=myDsl_ForStmt_strategy)
def test_mydsl_forstmt_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original

@given(instance=myDsl_SelectStmt_strategy)
@settings(max_examples=50)
def test_mydsl_selectstmt_instantiation(instance):
    assert isinstance(instance, myDsl_SelectStmt)



@given(instance=myDsl_SelectStmt_strategy)
def test_mydsl_selectstmt_select_setter(instance):
    original = instance.select
    instance.select = original
    assert instance.select == original

@given(instance=myDsl_SwitchStmt_strategy)
@settings(max_examples=50)
def test_mydsl_switchstmt_instantiation(instance):
    assert isinstance(instance, myDsl_SwitchStmt)

@given(instance=myDsl_IfStmt_strategy)
@settings(max_examples=50)
def test_mydsl_ifstmt_instantiation(instance):
    assert isinstance(instance, myDsl_IfStmt)



@given(instance=myDsl_IfStmt_strategy)
def test_mydsl_ifstmt_else__setter(instance):
    original = instance.else_
    instance.else_ = original
    assert instance.else_ == original



@given(instance=myDsl_IfStmt_strategy)
def test_mydsl_ifstmt_if__setter(instance):
    original = instance.if_
    instance.if_ = original
    assert instance.if_ == original

@given(instance=myDsl_Expression_Linha_strategy)
@settings(max_examples=50)
def test_mydsl_expression_linha_instantiation(instance):
    assert isinstance(instance, myDsl_Expression_Linha)

@given(instance=myDsl_FallthroughStmt_strategy)
@settings(max_examples=50)
def test_mydsl_fallthroughstmt_instantiation(instance):
    assert isinstance(instance, myDsl_FallthroughStmt)



@given(instance=myDsl_FallthroughStmt_strategy)
def test_mydsl_fallthroughstmt_fallthrough_setter(instance):
    original = instance.fallthrough
    instance.fallthrough = original
    assert instance.fallthrough == original

@given(instance=myDsl_GotoStmt_strategy)
@settings(max_examples=50)
def test_mydsl_gotostmt_instantiation(instance):
    assert isinstance(instance, myDsl_GotoStmt)



@given(instance=myDsl_GotoStmt_strategy)
def test_mydsl_gotostmt_goto_setter(instance):
    original = instance.goto
    instance.goto = original
    assert instance.goto == original

@given(instance=myDsl_ContinueStmt_strategy)
@settings(max_examples=50)
def test_mydsl_continuestmt_instantiation(instance):
    assert isinstance(instance, myDsl_ContinueStmt)



@given(instance=myDsl_ContinueStmt_strategy)
def test_mydsl_continuestmt_continue__setter(instance):
    original = instance.continue_
    instance.continue_ = original
    assert instance.continue_ == original

@given(instance=myDsl_BreakStmt_strategy)
@settings(max_examples=50)
def test_mydsl_breakstmt_instantiation(instance):
    assert isinstance(instance, myDsl_BreakStmt)



@given(instance=myDsl_BreakStmt_strategy)
def test_mydsl_breakstmt_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=myDsl_ReturnStmt_strategy)
@settings(max_examples=50)
def test_mydsl_returnstmt_instantiation(instance):
    assert isinstance(instance, myDsl_ReturnStmt)



@given(instance=myDsl_ReturnStmt_strategy)
def test_mydsl_returnstmt_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=myDsl_GoStmt_strategy)
@settings(max_examples=50)
def test_mydsl_gostmt_instantiation(instance):
    assert isinstance(instance, myDsl_GoStmt)



@given(instance=myDsl_GoStmt_strategy)
def test_mydsl_gostmt_go_setter(instance):
    original = instance.go
    instance.go = original
    assert instance.go == original

@given(instance=myDsl_SimpleStmt_strategy)
@settings(max_examples=50)
def test_mydsl_simplestmt_instantiation(instance):
    assert isinstance(instance, myDsl_SimpleStmt)

@given(instance=myDsl_LabeledStmt_strategy)
@settings(max_examples=50)
def test_mydsl_labeledstmt_instantiation(instance):
    assert isinstance(instance, myDsl_LabeledStmt)

@given(instance=myDsl_BINARY_OP_strategy)
@settings(max_examples=50)
def test_mydsl_binary_op_instantiation(instance):
    assert isinstance(instance, myDsl_BINARY_OP)



@given(instance=myDsl_BINARY_OP_strategy)
def test_mydsl_binary_op_rEL_OP_setter(instance):
    original = instance.rEL_OP
    instance.rEL_OP = original
    assert instance.rEL_OP == original



@given(instance=myDsl_BINARY_OP_strategy)
def test_mydsl_binary_op_aDD_OP_setter(instance):
    original = instance.aDD_OP
    instance.aDD_OP = original
    assert instance.aDD_OP == original

@given(instance=myDsl_Expression1_strategy)
@settings(max_examples=50)
def test_mydsl_expression1_instantiation(instance):
    assert isinstance(instance, myDsl_Expression1)

@given(instance=myDsl_TypeAssertion_strategy)
@settings(max_examples=50)
def test_mydsl_typeassertion_instantiation(instance):
    assert isinstance(instance, myDsl_TypeAssertion)

@given(instance=myDsl_UnaryExpr_strategy)
@settings(max_examples=50)
def test_mydsl_unaryexpr_instantiation(instance):
    assert isinstance(instance, myDsl_UnaryExpr)

@given(instance=myDsl_ReceiverType_strategy)
@settings(max_examples=50)
def test_mydsl_receivertype_instantiation(instance):
    assert isinstance(instance, myDsl_ReceiverType)

@given(instance=myDsl_Arguments_strategy)
@settings(max_examples=50)
def test_mydsl_arguments_instantiation(instance):
    assert isinstance(instance, myDsl_Arguments)

@given(instance=myDsl_Slice_strategy)
@settings(max_examples=50)
def test_mydsl_slice_instantiation(instance):
    assert isinstance(instance, myDsl_Slice)

@given(instance=myDsl_Index_strategy)
@settings(max_examples=50)
def test_mydsl_index_instantiation(instance):
    assert isinstance(instance, myDsl_Index)

@given(instance=myDsl_Selector_strategy)
@settings(max_examples=50)
def test_mydsl_selector_instantiation(instance):
    assert isinstance(instance, myDsl_Selector)



@given(instance=myDsl_Selector_strategy)
def test_mydsl_selector_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_MethodExpr_strategy)
@settings(max_examples=50)
def test_mydsl_methodexpr_instantiation(instance):
    assert isinstance(instance, myDsl_MethodExpr)

@given(instance=myDsl_Conversion_strategy)
@settings(max_examples=50)
def test_mydsl_conversion_instantiation(instance):
    assert isinstance(instance, myDsl_Conversion)

@given(instance=myDsl_PrimaryExprLinha_strategy)
@settings(max_examples=50)
def test_mydsl_primaryexprlinha_instantiation(instance):
    assert isinstance(instance, myDsl_PrimaryExprLinha)

@given(instance=myDsl_PrimaryExpr_strategy)
@settings(max_examples=50)
def test_mydsl_primaryexpr_instantiation(instance):
    assert isinstance(instance, myDsl_PrimaryExpr)

@given(instance=myDsl_FieldName_strategy)
@settings(max_examples=50)
def test_mydsl_fieldname_instantiation(instance):
    assert isinstance(instance, myDsl_FieldName)



@given(instance=myDsl_FieldName_strategy)
def test_mydsl_fieldname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_Element_strategy)
@settings(max_examples=50)
def test_mydsl_element_instantiation(instance):
    assert isinstance(instance, myDsl_Element)

@given(instance=myDsl_Key_strategy)
@settings(max_examples=50)
def test_mydsl_key_instantiation(instance):
    assert isinstance(instance, myDsl_Key)

@given(instance=myDsl_KeyedElement_strategy)
@settings(max_examples=50)
def test_mydsl_keyedelement_instantiation(instance):
    assert isinstance(instance, myDsl_KeyedElement)

@given(instance=myDsl_ElementList_strategy)
@settings(max_examples=50)
def test_mydsl_elementlist_instantiation(instance):
    assert isinstance(instance, myDsl_ElementList)

@given(instance=myDsl_LiteralTypeLinha_strategy)
@settings(max_examples=50)
def test_mydsl_literaltypelinha_instantiation(instance):
    assert isinstance(instance, myDsl_LiteralTypeLinha)

@given(instance=myDsl_LiteralValue_strategy)
@settings(max_examples=50)
def test_mydsl_literalvalue_instantiation(instance):
    assert isinstance(instance, myDsl_LiteralValue)

@given(instance=myDsl_LiteralType_strategy)
@settings(max_examples=50)
def test_mydsl_literaltype_instantiation(instance):
    assert isinstance(instance, myDsl_LiteralType)

@given(instance=myDsl_FunctionLit_strategy)
@settings(max_examples=50)
def test_mydsl_functionlit_instantiation(instance):
    assert isinstance(instance, myDsl_FunctionLit)



@given(instance=myDsl_FunctionLit_strategy)
def test_mydsl_functionlit_func_setter(instance):
    original = instance.func
    instance.func = original
    assert instance.func == original

@given(instance=myDsl_CompositeLit_strategy)
@settings(max_examples=50)
def test_mydsl_compositelit_instantiation(instance):
    assert isinstance(instance, myDsl_CompositeLit)

@given(instance=myDsl_BasicLit_strategy)
@settings(max_examples=50)
def test_mydsl_basiclit_instantiation(instance):
    assert isinstance(instance, myDsl_BasicLit)



@given(instance=myDsl_BasicLit_strategy)
def test_mydsl_basiclit_int_lit_setter(instance):
    original = instance.int_lit
    instance.int_lit = original
    assert instance.int_lit == original



@given(instance=myDsl_BasicLit_strategy)
def test_mydsl_basiclit_imaginary_lit_setter(instance):
    original = instance.imaginary_lit
    instance.imaginary_lit = original
    assert instance.imaginary_lit == original



@given(instance=myDsl_BasicLit_strategy)
def test_mydsl_basiclit_rune_lit_setter(instance):
    original = instance.rune_lit
    instance.rune_lit = original
    assert instance.rune_lit == original



@given(instance=myDsl_BasicLit_strategy)
def test_mydsl_basiclit_float_lit_setter(instance):
    original = instance.float_lit
    instance.float_lit = original
    assert instance.float_lit == original



@given(instance=myDsl_BasicLit_strategy)
def test_mydsl_basiclit_string_lit_setter(instance):
    original = instance.string_lit
    instance.string_lit = original
    assert instance.string_lit == original

@given(instance=myDsl_OperandName_strategy)
@settings(max_examples=50)
def test_mydsl_operandname_instantiation(instance):
    assert isinstance(instance, myDsl_OperandName)



@given(instance=myDsl_OperandName_strategy)
def test_mydsl_operandname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_Literal_strategy)
@settings(max_examples=50)
def test_mydsl_literal_instantiation(instance):
    assert isinstance(instance, myDsl_Literal)

@given(instance=myDsl_Operand_strategy)
@settings(max_examples=50)
def test_mydsl_operand_instantiation(instance):
    assert isinstance(instance, myDsl_Operand)

@given(instance=myDsl_Receiver_strategy)
@settings(max_examples=50)
def test_mydsl_receiver_instantiation(instance):
    assert isinstance(instance, myDsl_Receiver)

@given(instance=myDsl_FunctionBody_strategy)
@settings(max_examples=50)
def test_mydsl_functionbody_instantiation(instance):
    assert isinstance(instance, myDsl_FunctionBody)

@given(instance=myDsl_FunctionName_strategy)
@settings(max_examples=50)
def test_mydsl_functionname_instantiation(instance):
    assert isinstance(instance, myDsl_FunctionName)



@given(instance=myDsl_FunctionName_strategy)
def test_mydsl_functionname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_ShortVarDecl_strategy)
@settings(max_examples=50)
def test_mydsl_shortvardecl_instantiation(instance):
    assert isinstance(instance, myDsl_ShortVarDecl)

@given(instance=myDsl_ConstSpec_strategy)
@settings(max_examples=50)
def test_mydsl_constspec_instantiation(instance):
    assert isinstance(instance, myDsl_ConstSpec)

@given(instance=myDsl_VarSpec_strategy)
@settings(max_examples=50)
def test_mydsl_varspec_instantiation(instance):
    assert isinstance(instance, myDsl_VarSpec)

@given(instance=myDsl_TypeDef_strategy)
@settings(max_examples=50)
def test_mydsl_typedef_instantiation(instance):
    assert isinstance(instance, myDsl_TypeDef)



@given(instance=myDsl_TypeDef_strategy)
def test_mydsl_typedef_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_AliasDecl_strategy)
@settings(max_examples=50)
def test_mydsl_aliasdecl_instantiation(instance):
    assert isinstance(instance, myDsl_AliasDecl)



@given(instance=myDsl_AliasDecl_strategy)
def test_mydsl_aliasdecl_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_TypeSpec_strategy)
@settings(max_examples=50)
def test_mydsl_typespec_instantiation(instance):
    assert isinstance(instance, myDsl_TypeSpec)

@given(instance=myDsl_ExpressionList_strategy)
@settings(max_examples=50)
def test_mydsl_expressionlist_instantiation(instance):
    assert isinstance(instance, myDsl_ExpressionList)

@given(instance=myDsl_ChannelTypeLinha_strategy)
@settings(max_examples=50)
def test_mydsl_channeltypelinha_instantiation(instance):
    assert isinstance(instance, myDsl_ChannelTypeLinha)



@given(instance=myDsl_ChannelTypeLinha_strategy)
def test_mydsl_channeltypelinha_aNY_OTHER_setter(instance):
    original = instance.aNY_OTHER
    instance.aNY_OTHER = original
    assert instance.aNY_OTHER == original

@given(instance=myDsl_MethodDecl_strategy)
@settings(max_examples=50)
def test_mydsl_methoddecl_instantiation(instance):
    assert isinstance(instance, myDsl_MethodDecl)

@given(instance=myDsl_FunctionDecl_strategy)
@settings(max_examples=50)
def test_mydsl_functiondecl_instantiation(instance):
    assert isinstance(instance, myDsl_FunctionDecl)

@given(instance=myDsl_TopLevelDecl_strategy)
@settings(max_examples=50)
def test_mydsl_topleveldecl_instantiation(instance):
    assert isinstance(instance, myDsl_TopLevelDecl)

@given(instance=myDsl_VarDecl_strategy)
@settings(max_examples=50)
def test_mydsl_vardecl_instantiation(instance):
    assert isinstance(instance, myDsl_VarDecl)



@given(instance=myDsl_VarDecl_strategy)
def test_mydsl_vardecl_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=myDsl_TypeDecl_strategy)
@settings(max_examples=50)
def test_mydsl_typedecl_instantiation(instance):
    assert isinstance(instance, myDsl_TypeDecl)



@given(instance=myDsl_TypeDecl_strategy)
def test_mydsl_typedecl_typekeyword_setter(instance):
    original = instance.typekeyword
    instance.typekeyword = original
    assert instance.typekeyword == original

@given(instance=myDsl_ConstDecl_strategy)
@settings(max_examples=50)
def test_mydsl_constdecl_instantiation(instance):
    assert isinstance(instance, myDsl_ConstDecl)



@given(instance=myDsl_ConstDecl_strategy)
def test_mydsl_constdecl_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=myDsl_Declaration_strategy)
@settings(max_examples=50)
def test_mydsl_declaration_instantiation(instance):
    assert isinstance(instance, myDsl_Declaration)

@given(instance=myDsl_Statement_strategy)
@settings(max_examples=50)
def test_mydsl_statement_instantiation(instance):
    assert isinstance(instance, myDsl_Statement)

@given(instance=myDsl_StatementList_strategy)
@settings(max_examples=50)
def test_mydsl_statementlist_instantiation(instance):
    assert isinstance(instance, myDsl_StatementList)

@given(instance=myDsl_Block_strategy)
@settings(max_examples=50)
def test_mydsl_block_instantiation(instance):
    assert isinstance(instance, myDsl_Block)

@given(instance=myDsl_Result_strategy)
@settings(max_examples=50)
def test_mydsl_result_instantiation(instance):
    assert isinstance(instance, myDsl_Result)

@given(instance=myDsl_KeyType_strategy)
@settings(max_examples=50)
def test_mydsl_keytype_instantiation(instance):
    assert isinstance(instance, myDsl_KeyType)

@given(instance=myDsl_InterfaceTypeName_strategy)
@settings(max_examples=50)
def test_mydsl_interfacetypename_instantiation(instance):
    assert isinstance(instance, myDsl_InterfaceTypeName)

@given(instance=myDsl_MethodName_strategy)
@settings(max_examples=50)
def test_mydsl_methodname_instantiation(instance):
    assert isinstance(instance, myDsl_MethodName)



@given(instance=myDsl_MethodName_strategy)
def test_mydsl_methodname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_MethodSpec_strategy)
@settings(max_examples=50)
def test_mydsl_methodspec_instantiation(instance):
    assert isinstance(instance, myDsl_MethodSpec)

@given(instance=myDsl_ParameterDecl_strategy)
@settings(max_examples=50)
def test_mydsl_parameterdecl_instantiation(instance):
    assert isinstance(instance, myDsl_ParameterDecl)

@given(instance=myDsl_ParameterList_strategy)
@settings(max_examples=50)
def test_mydsl_parameterlist_instantiation(instance):
    assert isinstance(instance, myDsl_ParameterList)

@given(instance=myDsl_ChannelType_strategy)
@settings(max_examples=50)
def test_mydsl_channeltype_instantiation(instance):
    assert isinstance(instance, myDsl_ChannelType)



@given(instance=myDsl_ChannelType_strategy)
def test_mydsl_channeltype_chan_setter(instance):
    original = instance.chan
    instance.chan = original
    assert instance.chan == original

@given(instance=myDsl_Parameters_strategy)
@settings(max_examples=50)
def test_mydsl_parameters_instantiation(instance):
    assert isinstance(instance, myDsl_Parameters)

@given(instance=myDsl_Signature_strategy)
@settings(max_examples=50)
def test_mydsl_signature_instantiation(instance):
    assert isinstance(instance, myDsl_Signature)

@given(instance=myDsl_BaseType_strategy)
@settings(max_examples=50)
def test_mydsl_basetype_instantiation(instance):
    assert isinstance(instance, myDsl_BaseType)

@given(instance=myDsl_Tag_strategy)
@settings(max_examples=50)
def test_mydsl_tag_instantiation(instance):
    assert isinstance(instance, myDsl_Tag)



@given(instance=myDsl_Tag_strategy)
def test_mydsl_tag_string_lit_setter(instance):
    original = instance.string_lit
    instance.string_lit = original
    assert instance.string_lit == original

@given(instance=myDsl_EmbeddedField_strategy)
@settings(max_examples=50)
def test_mydsl_embeddedfield_instantiation(instance):
    assert isinstance(instance, myDsl_EmbeddedField)

@given(instance=myDsl_IdentifierList_strategy)
@settings(max_examples=50)
def test_mydsl_identifierlist_instantiation(instance):
    assert isinstance(instance, myDsl_IdentifierList)



@given(instance=myDsl_IdentifierList_strategy)
def test_mydsl_identifierlist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=myDsl_IdentifierList_strategy)
def test_mydsl_identifierlist_id1_setter(instance):
    original = instance.id1
    instance.id1 = original
    assert instance.id1 == original

@given(instance=myDsl_FieldDecl_strategy)
@settings(max_examples=50)
def test_mydsl_fielddecl_instantiation(instance):
    assert isinstance(instance, myDsl_FieldDecl)

@given(instance=myDsl_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Expression)

@given(instance=myDsl_ElementType_strategy)
@settings(max_examples=50)
def test_mydsl_elementtype_instantiation(instance):
    assert isinstance(instance, myDsl_ElementType)

@given(instance=myDsl_ArrayLength_strategy)
@settings(max_examples=50)
def test_mydsl_arraylength_instantiation(instance):
    assert isinstance(instance, myDsl_ArrayLength)

@given(instance=myDsl_MapType_strategy)
@settings(max_examples=50)
def test_mydsl_maptype_instantiation(instance):
    assert isinstance(instance, myDsl_MapType)



@given(instance=myDsl_MapType_strategy)
def test_mydsl_maptype_map_setter(instance):
    original = instance.map
    instance.map = original
    assert instance.map == original

@given(instance=myDsl_InterfaceType_strategy)
@settings(max_examples=50)
def test_mydsl_interfacetype_instantiation(instance):
    assert isinstance(instance, myDsl_InterfaceType)



@given(instance=myDsl_InterfaceType_strategy)
def test_mydsl_interfacetype_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=myDsl_FunctionType_strategy)
@settings(max_examples=50)
def test_mydsl_functiontype_instantiation(instance):
    assert isinstance(instance, myDsl_FunctionType)



@given(instance=myDsl_FunctionType_strategy)
def test_mydsl_functiontype_func_setter(instance):
    original = instance.func
    instance.func = original
    assert instance.func == original

@given(instance=myDsl_PointerType_strategy)
@settings(max_examples=50)
def test_mydsl_pointertype_instantiation(instance):
    assert isinstance(instance, myDsl_PointerType)

@given(instance=myDsl_StructType_strategy)
@settings(max_examples=50)
def test_mydsl_structtype_instantiation(instance):
    assert isinstance(instance, myDsl_StructType)



@given(instance=myDsl_StructType_strategy)
def test_mydsl_structtype_struct_setter(instance):
    original = instance.struct
    instance.struct = original
    assert instance.struct == original

@given(instance=myDsl_TypeLitLinha_strategy)
@settings(max_examples=50)
def test_mydsl_typelitlinha_instantiation(instance):
    assert isinstance(instance, myDsl_TypeLitLinha)

@given(instance=myDsl_TypeNameLinha_strategy)
@settings(max_examples=50)
def test_mydsl_typenamelinha_instantiation(instance):
    assert isinstance(instance, myDsl_TypeNameLinha)



@given(instance=myDsl_TypeNameLinha_strategy)
def test_mydsl_typenamelinha_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_TypeLit_strategy)
@settings(max_examples=50)
def test_mydsl_typelit_instantiation(instance):
    assert isinstance(instance, myDsl_TypeLit)

@given(instance=myDsl_TypeName_strategy)
@settings(max_examples=50)
def test_mydsl_typename_instantiation(instance):
    assert isinstance(instance, myDsl_TypeName)



@given(instance=myDsl_TypeName_strategy)
def test_mydsl_typename_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)

@given(instance=myDsl_SourceFile_strategy)
@settings(max_examples=50)
def test_mydsl_sourcefile_instantiation(instance):
    assert isinstance(instance, myDsl_SourceFile)

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)
