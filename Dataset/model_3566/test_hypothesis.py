import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::ImportSpec,
    myDsl::PackageName,
    myDsl::ImportDecl,
    myDsl::PackageClause,
    myDsl::RecvExpr,
    myDsl::CommCaseLinha,
    myDsl::CommCase,
    myDsl::CommClause,
    myDsl::ForStmtLinhaLinha,
    myDsl::PostStmt,
    myDsl::Condition,
    myDsl::ForStmtLinha,
    myDsl::TypeList,
    myDsl::TypeSwitchCase,
    myDsl::TypeCaseClause,
    myDsl::TypeSwitchGuard,
    myDsl::ExprSwitchCase,
    myDsl::ExprCaseClause,
    myDsl::TypeSwitchStmt,
    myDsl::ExprSwitchStmt,
    myDsl::IfStmtLinha,
    myDsl::Label,
    myDsl::assign::op,
    myDsl::SimpleStmtLinha,
    myDsl::EmptyStmt,
    myDsl::DeferStmt,
    myDsl::ForStmt,
    myDsl::SelectStmt,
    myDsl::SwitchStmt,
    myDsl::IfStmt,
    myDsl::Expression::Linha,
    myDsl::FallthroughStmt,
    myDsl::GotoStmt,
    myDsl::ContinueStmt,
    myDsl::BreakStmt,
    myDsl::ReturnStmt,
    myDsl::GoStmt,
    myDsl::SimpleStmt,
    myDsl::LabeledStmt,
    myDsl::BINARY::OP,
    myDsl::Expression1,
    myDsl::TypeAssertion,
    myDsl::UnaryExpr,
    myDsl::ReceiverType,
    myDsl::Arguments,
    myDsl::Slice,
    myDsl::Index,
    myDsl::Selector,
    myDsl::MethodExpr,
    myDsl::Conversion,
    myDsl::PrimaryExprLinha,
    myDsl::PrimaryExpr,
    myDsl::FieldName,
    myDsl::Element,
    myDsl::Key,
    myDsl::KeyedElement,
    myDsl::ElementList,
    myDsl::LiteralTypeLinha,
    myDsl::LiteralValue,
    myDsl::LiteralType,
    myDsl::FunctionLit,
    myDsl::CompositeLit,
    myDsl::BasicLit,
    myDsl::OperandName,
    myDsl::Literal,
    myDsl::Operand,
    myDsl::Receiver,
    myDsl::FunctionBody,
    myDsl::FunctionName,
    myDsl::ShortVarDecl,
    myDsl::ConstSpec,
    myDsl::VarSpec,
    myDsl::TypeDef,
    myDsl::AliasDecl,
    myDsl::TypeSpec,
    myDsl::ExpressionList,
    myDsl::ChannelTypeLinha,
    myDsl::MethodDecl,
    myDsl::FunctionDecl,
    myDsl::TopLevelDecl,
    myDsl::VarDecl,
    myDsl::TypeDecl,
    myDsl::ConstDecl,
    myDsl::Declaration,
    myDsl::Statement,
    myDsl::StatementList,
    myDsl::Block,
    myDsl::Result,
    myDsl::KeyType,
    myDsl::InterfaceTypeName,
    myDsl::MethodName,
    myDsl::MethodSpec,
    myDsl::ParameterDecl,
    myDsl::ParameterList,
    myDsl::ChannelType,
    myDsl::Parameters,
    myDsl::Signature,
    myDsl::BaseType,
    myDsl::Tag,
    myDsl::EmbeddedField,
    myDsl::IdentifierList,
    myDsl::FieldDecl,
    myDsl::Expression,
    myDsl::ElementType,
    myDsl::ArrayLength,
    myDsl::MapType,
    myDsl::InterfaceType,
    myDsl::FunctionType,
    myDsl::PointerType,
    myDsl::StructType,
    myDsl::TypeLitLinha,
    myDsl::TypeNameLinha,
    myDsl::TypeLit,
    myDsl::TypeName,
    myDsl::Type,
    myDsl::SourceFile,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::importspec_is_not_abstract():
    assert not inspect.isabstract(myDsl::ImportSpec)


def test_mydsl::importspec_constructor_exists():
    assert callable(myDsl::ImportSpec.__init__)


def test_mydsl::importspec_constructor_args():
    sig = inspect.signature(myDsl::ImportSpec.__init__)
    params = list(sig.parameters.keys())
    assert "sTRING_LIT" in params, "Missing parameter 'sTRING_LIT'"

def test_mydsl::importspec_has_sTRING_LIT():
    assert hasattr(myDsl::ImportSpec, "sTRING_LIT")
    descriptor = None
    for klass in myDsl::ImportSpec.__mro__:
        if "sTRING_LIT" in klass.__dict__:
            descriptor = klass.__dict__["sTRING_LIT"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::packagename_is_not_abstract():
    assert not inspect.isabstract(myDsl::PackageName)


def test_mydsl::packagename_constructor_exists():
    assert callable(myDsl::PackageName.__init__)


def test_mydsl::packagename_constructor_args():
    sig = inspect.signature(myDsl::PackageName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::packagename_has_id():
    assert hasattr(myDsl::PackageName, "id")
    descriptor = None
    for klass in myDsl::PackageName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::importdecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::ImportDecl)


def test_mydsl::importdecl_constructor_exists():
    assert callable(myDsl::ImportDecl.__init__)


def test_mydsl::importdecl_constructor_args():
    sig = inspect.signature(myDsl::ImportDecl.__init__)
    params = list(sig.parameters.keys())
    assert "importt" in params, "Missing parameter 'importt'"

def test_mydsl::importdecl_has_importt():
    assert hasattr(myDsl::ImportDecl, "importt")
    descriptor = None
    for klass in myDsl::ImportDecl.__mro__:
        if "importt" in klass.__dict__:
            descriptor = klass.__dict__["importt"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::packageclause_is_not_abstract():
    assert not inspect.isabstract(myDsl::PackageClause)


def test_mydsl::packageclause_constructor_exists():
    assert callable(myDsl::PackageClause.__init__)


def test_mydsl::packageclause_constructor_args():
    sig = inspect.signature(myDsl::PackageClause.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_mydsl::packageclause_has_package():
    assert hasattr(myDsl::PackageClause, "package")
    descriptor = None
    for klass in myDsl::PackageClause.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::recvexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl::RecvExpr)


def test_mydsl::recvexpr_constructor_exists():
    assert callable(myDsl::RecvExpr.__init__)


def test_mydsl::recvexpr_constructor_args():
    sig = inspect.signature(myDsl::RecvExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::commcaselinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::CommCaseLinha)


def test_mydsl::commcaselinha_constructor_exists():
    assert callable(myDsl::CommCaseLinha.__init__)


def test_mydsl::commcaselinha_constructor_args():
    sig = inspect.signature(myDsl::CommCaseLinha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::commcase_is_not_abstract():
    assert not inspect.isabstract(myDsl::CommCase)


def test_mydsl::commcase_constructor_exists():
    assert callable(myDsl::CommCase.__init__)


def test_mydsl::commcase_constructor_args():
    sig = inspect.signature(myDsl::CommCase.__init__)
    params = list(sig.parameters.keys())
    assert "case" in params, "Missing parameter 'case'"
    assert "default" in params, "Missing parameter 'default'"

def test_mydsl::commcase_has_case():
    assert hasattr(myDsl::CommCase, "case")
    descriptor = None
    for klass in myDsl::CommCase.__mro__:
        if "case" in klass.__dict__:
            descriptor = klass.__dict__["case"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::commcase_has_default():
    assert hasattr(myDsl::CommCase, "default")
    descriptor = None
    for klass in myDsl::CommCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::commclause_is_not_abstract():
    assert not inspect.isabstract(myDsl::CommClause)


def test_mydsl::commclause_constructor_exists():
    assert callable(myDsl::CommClause.__init__)


def test_mydsl::commclause_constructor_args():
    sig = inspect.signature(myDsl::CommClause.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::forstmtlinhalinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::ForStmtLinhaLinha)


def test_mydsl::forstmtlinhalinha_constructor_exists():
    assert callable(myDsl::ForStmtLinhaLinha.__init__)


def test_mydsl::forstmtlinhalinha_constructor_args():
    sig = inspect.signature(myDsl::ForStmtLinhaLinha.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"

def test_mydsl::forstmtlinhalinha_has_range():
    assert hasattr(myDsl::ForStmtLinhaLinha, "range")
    descriptor = None
    for klass in myDsl::ForStmtLinhaLinha.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::poststmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::PostStmt)


def test_mydsl::poststmt_constructor_exists():
    assert callable(myDsl::PostStmt.__init__)


def test_mydsl::poststmt_constructor_args():
    sig = inspect.signature(myDsl::PostStmt.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::condition_is_not_abstract():
    assert not inspect.isabstract(myDsl::Condition)


def test_mydsl::condition_constructor_exists():
    assert callable(myDsl::Condition.__init__)


def test_mydsl::condition_constructor_args():
    sig = inspect.signature(myDsl::Condition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::forstmtlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::ForStmtLinha)


def test_mydsl::forstmtlinha_constructor_exists():
    assert callable(myDsl::ForStmtLinha.__init__)


def test_mydsl::forstmtlinha_constructor_args():
    sig = inspect.signature(myDsl::ForStmtLinha.__init__)
    params = list(sig.parameters.keys())
    assert "vazio" in params, "Missing parameter 'vazio'"

def test_mydsl::forstmtlinha_has_vazio():
    assert hasattr(myDsl::ForStmtLinha, "vazio")
    descriptor = None
    for klass in myDsl::ForStmtLinha.__mro__:
        if "vazio" in klass.__dict__:
            descriptor = klass.__dict__["vazio"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::typelist_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeList)


def test_mydsl::typelist_constructor_exists():
    assert callable(myDsl::TypeList.__init__)


def test_mydsl::typelist_constructor_args():
    sig = inspect.signature(myDsl::TypeList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::typeswitchcase_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeSwitchCase)


def test_mydsl::typeswitchcase_constructor_exists():
    assert callable(myDsl::TypeSwitchCase.__init__)


def test_mydsl::typeswitchcase_constructor_args():
    sig = inspect.signature(myDsl::TypeSwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "case" in params, "Missing parameter 'case'"
    assert "default" in params, "Missing parameter 'default'"

def test_mydsl::typeswitchcase_has_case():
    assert hasattr(myDsl::TypeSwitchCase, "case")
    descriptor = None
    for klass in myDsl::TypeSwitchCase.__mro__:
        if "case" in klass.__dict__:
            descriptor = klass.__dict__["case"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::typeswitchcase_has_default():
    assert hasattr(myDsl::TypeSwitchCase, "default")
    descriptor = None
    for klass in myDsl::TypeSwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::typecaseclause_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeCaseClause)


def test_mydsl::typecaseclause_constructor_exists():
    assert callable(myDsl::TypeCaseClause.__init__)


def test_mydsl::typecaseclause_constructor_args():
    sig = inspect.signature(myDsl::TypeCaseClause.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::typeswitchguard_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeSwitchGuard)


def test_mydsl::typeswitchguard_constructor_exists():
    assert callable(myDsl::TypeSwitchGuard.__init__)


def test_mydsl::typeswitchguard_constructor_args():
    sig = inspect.signature(myDsl::TypeSwitchGuard.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl::typeswitchguard_has_id():
    assert hasattr(myDsl::TypeSwitchGuard, "id")
    descriptor = None
    for klass in myDsl::TypeSwitchGuard.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::typeswitchguard_has_type():
    assert hasattr(myDsl::TypeSwitchGuard, "type")
    descriptor = None
    for klass in myDsl::TypeSwitchGuard.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::exprswitchcase_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprSwitchCase)


def test_mydsl::exprswitchcase_constructor_exists():
    assert callable(myDsl::ExprSwitchCase.__init__)


def test_mydsl::exprswitchcase_constructor_args():
    sig = inspect.signature(myDsl::ExprSwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "case" in params, "Missing parameter 'case'"
    assert "default" in params, "Missing parameter 'default'"

def test_mydsl::exprswitchcase_has_case():
    assert hasattr(myDsl::ExprSwitchCase, "case")
    descriptor = None
    for klass in myDsl::ExprSwitchCase.__mro__:
        if "case" in klass.__dict__:
            descriptor = klass.__dict__["case"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::exprswitchcase_has_default():
    assert hasattr(myDsl::ExprSwitchCase, "default")
    descriptor = None
    for klass in myDsl::ExprSwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::exprcaseclause_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprCaseClause)


def test_mydsl::exprcaseclause_constructor_exists():
    assert callable(myDsl::ExprCaseClause.__init__)


def test_mydsl::exprcaseclause_constructor_args():
    sig = inspect.signature(myDsl::ExprCaseClause.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::typeswitchstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeSwitchStmt)


def test_mydsl::typeswitchstmt_constructor_exists():
    assert callable(myDsl::TypeSwitchStmt.__init__)


def test_mydsl::typeswitchstmt_constructor_args():
    sig = inspect.signature(myDsl::TypeSwitchStmt.__init__)
    params = list(sig.parameters.keys())
    assert "switch" in params, "Missing parameter 'switch'"

def test_mydsl::typeswitchstmt_has_switch():
    assert hasattr(myDsl::TypeSwitchStmt, "switch")
    descriptor = None
    for klass in myDsl::TypeSwitchStmt.__mro__:
        if "switch" in klass.__dict__:
            descriptor = klass.__dict__["switch"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::exprswitchstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprSwitchStmt)


def test_mydsl::exprswitchstmt_constructor_exists():
    assert callable(myDsl::ExprSwitchStmt.__init__)


def test_mydsl::exprswitchstmt_constructor_args():
    sig = inspect.signature(myDsl::ExprSwitchStmt.__init__)
    params = list(sig.parameters.keys())
    assert "switch" in params, "Missing parameter 'switch'"

def test_mydsl::exprswitchstmt_has_switch():
    assert hasattr(myDsl::ExprSwitchStmt, "switch")
    descriptor = None
    for klass in myDsl::ExprSwitchStmt.__mro__:
        if "switch" in klass.__dict__:
            descriptor = klass.__dict__["switch"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::ifstmtlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::IfStmtLinha)


def test_mydsl::ifstmtlinha_constructor_exists():
    assert callable(myDsl::IfStmtLinha.__init__)


def test_mydsl::ifstmtlinha_constructor_args():
    sig = inspect.signature(myDsl::IfStmtLinha.__init__)
    params = list(sig.parameters.keys())
    assert "else_" in params, "Missing parameter 'else_'"

def test_mydsl::ifstmtlinha_has_else_():
    assert hasattr(myDsl::IfStmtLinha, "else_")
    descriptor = None
    for klass in myDsl::IfStmtLinha.__mro__:
        if "else_" in klass.__dict__:
            descriptor = klass.__dict__["else_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::label_is_not_abstract():
    assert not inspect.isabstract(myDsl::Label)


def test_mydsl::label_constructor_exists():
    assert callable(myDsl::Label.__init__)


def test_mydsl::label_constructor_args():
    sig = inspect.signature(myDsl::Label.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::label_has_id():
    assert hasattr(myDsl::Label, "id")
    descriptor = None
    for klass in myDsl::Label.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::assign::op_is_not_abstract():
    assert not inspect.isabstract(myDsl::assign::op)


def test_mydsl::assign::op_constructor_exists():
    assert callable(myDsl::assign::op.__init__)


def test_mydsl::assign::op_constructor_args():
    sig = inspect.signature(myDsl::assign::op.__init__)
    params = list(sig.parameters.keys())
    assert "aDD_OP" in params, "Missing parameter 'aDD_OP'"
    assert "mUL_OP" in params, "Missing parameter 'mUL_OP'"

def test_mydsl::assign::op_has_aDD_OP():
    assert hasattr(myDsl::assign::op, "aDD_OP")
    descriptor = None
    for klass in myDsl::assign::op.__mro__:
        if "aDD_OP" in klass.__dict__:
            descriptor = klass.__dict__["aDD_OP"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assign::op_has_mUL_OP():
    assert hasattr(myDsl::assign::op, "mUL_OP")
    descriptor = None
    for klass in myDsl::assign::op.__mro__:
        if "mUL_OP" in klass.__dict__:
            descriptor = klass.__dict__["mUL_OP"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::simplestmtlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::SimpleStmtLinha)


def test_mydsl::simplestmtlinha_constructor_exists():
    assert callable(myDsl::SimpleStmtLinha.__init__)


def test_mydsl::simplestmtlinha_constructor_args():
    sig = inspect.signature(myDsl::SimpleStmtLinha.__init__)
    params = list(sig.parameters.keys())
    assert "aNY_OTHER" in params, "Missing parameter 'aNY_OTHER'"

def test_mydsl::simplestmtlinha_has_aNY_OTHER():
    assert hasattr(myDsl::SimpleStmtLinha, "aNY_OTHER")
    descriptor = None
    for klass in myDsl::SimpleStmtLinha.__mro__:
        if "aNY_OTHER" in klass.__dict__:
            descriptor = klass.__dict__["aNY_OTHER"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::emptystmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::EmptyStmt)


def test_mydsl::emptystmt_constructor_exists():
    assert callable(myDsl::EmptyStmt.__init__)


def test_mydsl::emptystmt_constructor_args():
    sig = inspect.signature(myDsl::EmptyStmt.__init__)
    params = list(sig.parameters.keys())
    assert "aNY_OTHER" in params, "Missing parameter 'aNY_OTHER'"

def test_mydsl::emptystmt_has_aNY_OTHER():
    assert hasattr(myDsl::EmptyStmt, "aNY_OTHER")
    descriptor = None
    for klass in myDsl::EmptyStmt.__mro__:
        if "aNY_OTHER" in klass.__dict__:
            descriptor = klass.__dict__["aNY_OTHER"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::deferstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::DeferStmt)


def test_mydsl::deferstmt_constructor_exists():
    assert callable(myDsl::DeferStmt.__init__)


def test_mydsl::deferstmt_constructor_args():
    sig = inspect.signature(myDsl::DeferStmt.__init__)
    params = list(sig.parameters.keys())
    assert "defer" in params, "Missing parameter 'defer'"

def test_mydsl::deferstmt_has_defer():
    assert hasattr(myDsl::DeferStmt, "defer")
    descriptor = None
    for klass in myDsl::DeferStmt.__mro__:
        if "defer" in klass.__dict__:
            descriptor = klass.__dict__["defer"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::forstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::ForStmt)


def test_mydsl::forstmt_constructor_exists():
    assert callable(myDsl::ForStmt.__init__)


def test_mydsl::forstmt_constructor_args():
    sig = inspect.signature(myDsl::ForStmt.__init__)
    params = list(sig.parameters.keys())
    assert "range" in params, "Missing parameter 'range'"
    assert "for_" in params, "Missing parameter 'for_'"

def test_mydsl::forstmt_has_range():
    assert hasattr(myDsl::ForStmt, "range")
    descriptor = None
    for klass in myDsl::ForStmt.__mro__:
        if "range" in klass.__dict__:
            descriptor = klass.__dict__["range"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::forstmt_has_for_():
    assert hasattr(myDsl::ForStmt, "for_")
    descriptor = None
    for klass in myDsl::ForStmt.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::selectstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::SelectStmt)


def test_mydsl::selectstmt_constructor_exists():
    assert callable(myDsl::SelectStmt.__init__)


def test_mydsl::selectstmt_constructor_args():
    sig = inspect.signature(myDsl::SelectStmt.__init__)
    params = list(sig.parameters.keys())
    assert "select" in params, "Missing parameter 'select'"

def test_mydsl::selectstmt_has_select():
    assert hasattr(myDsl::SelectStmt, "select")
    descriptor = None
    for klass in myDsl::SelectStmt.__mro__:
        if "select" in klass.__dict__:
            descriptor = klass.__dict__["select"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::switchstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::SwitchStmt)


def test_mydsl::switchstmt_constructor_exists():
    assert callable(myDsl::SwitchStmt.__init__)


def test_mydsl::switchstmt_constructor_args():
    sig = inspect.signature(myDsl::SwitchStmt.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::ifstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::IfStmt)


def test_mydsl::ifstmt_constructor_exists():
    assert callable(myDsl::IfStmt.__init__)


def test_mydsl::ifstmt_constructor_args():
    sig = inspect.signature(myDsl::IfStmt.__init__)
    params = list(sig.parameters.keys())
    assert "else_" in params, "Missing parameter 'else_'"
    assert "if_" in params, "Missing parameter 'if_'"

def test_mydsl::ifstmt_has_else_():
    assert hasattr(myDsl::IfStmt, "else_")
    descriptor = None
    for klass in myDsl::IfStmt.__mro__:
        if "else_" in klass.__dict__:
            descriptor = klass.__dict__["else_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::ifstmt_has_if_():
    assert hasattr(myDsl::IfStmt, "if_")
    descriptor = None
    for klass in myDsl::IfStmt.__mro__:
        if "if_" in klass.__dict__:
            descriptor = klass.__dict__["if_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expression::Linha)


def test_mydsl::expression::linha_constructor_exists():
    assert callable(myDsl::Expression::Linha.__init__)


def test_mydsl::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::Expression::Linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::fallthroughstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::FallthroughStmt)


def test_mydsl::fallthroughstmt_constructor_exists():
    assert callable(myDsl::FallthroughStmt.__init__)


def test_mydsl::fallthroughstmt_constructor_args():
    sig = inspect.signature(myDsl::FallthroughStmt.__init__)
    params = list(sig.parameters.keys())
    assert "fallthrough" in params, "Missing parameter 'fallthrough'"

def test_mydsl::fallthroughstmt_has_fallthrough():
    assert hasattr(myDsl::FallthroughStmt, "fallthrough")
    descriptor = None
    for klass in myDsl::FallthroughStmt.__mro__:
        if "fallthrough" in klass.__dict__:
            descriptor = klass.__dict__["fallthrough"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::gotostmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::GotoStmt)


def test_mydsl::gotostmt_constructor_exists():
    assert callable(myDsl::GotoStmt.__init__)


def test_mydsl::gotostmt_constructor_args():
    sig = inspect.signature(myDsl::GotoStmt.__init__)
    params = list(sig.parameters.keys())
    assert "goto" in params, "Missing parameter 'goto'"

def test_mydsl::gotostmt_has_goto():
    assert hasattr(myDsl::GotoStmt, "goto")
    descriptor = None
    for klass in myDsl::GotoStmt.__mro__:
        if "goto" in klass.__dict__:
            descriptor = klass.__dict__["goto"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::continuestmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::ContinueStmt)


def test_mydsl::continuestmt_constructor_exists():
    assert callable(myDsl::ContinueStmt.__init__)


def test_mydsl::continuestmt_constructor_args():
    sig = inspect.signature(myDsl::ContinueStmt.__init__)
    params = list(sig.parameters.keys())
    assert "continue_" in params, "Missing parameter 'continue_'"

def test_mydsl::continuestmt_has_continue_():
    assert hasattr(myDsl::ContinueStmt, "continue_")
    descriptor = None
    for klass in myDsl::ContinueStmt.__mro__:
        if "continue_" in klass.__dict__:
            descriptor = klass.__dict__["continue_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::breakstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::BreakStmt)


def test_mydsl::breakstmt_constructor_exists():
    assert callable(myDsl::BreakStmt.__init__)


def test_mydsl::breakstmt_constructor_args():
    sig = inspect.signature(myDsl::BreakStmt.__init__)
    params = list(sig.parameters.keys())
    assert "break_" in params, "Missing parameter 'break_'"

def test_mydsl::breakstmt_has_break_():
    assert hasattr(myDsl::BreakStmt, "break_")
    descriptor = None
    for klass in myDsl::BreakStmt.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::returnstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReturnStmt)


def test_mydsl::returnstmt_constructor_exists():
    assert callable(myDsl::ReturnStmt.__init__)


def test_mydsl::returnstmt_constructor_args():
    sig = inspect.signature(myDsl::ReturnStmt.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"

def test_mydsl::returnstmt_has_return_():
    assert hasattr(myDsl::ReturnStmt, "return_")
    descriptor = None
    for klass in myDsl::ReturnStmt.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::gostmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::GoStmt)


def test_mydsl::gostmt_constructor_exists():
    assert callable(myDsl::GoStmt.__init__)


def test_mydsl::gostmt_constructor_args():
    sig = inspect.signature(myDsl::GoStmt.__init__)
    params = list(sig.parameters.keys())
    assert "go" in params, "Missing parameter 'go'"

def test_mydsl::gostmt_has_go():
    assert hasattr(myDsl::GoStmt, "go")
    descriptor = None
    for klass in myDsl::GoStmt.__mro__:
        if "go" in klass.__dict__:
            descriptor = klass.__dict__["go"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::simplestmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::SimpleStmt)


def test_mydsl::simplestmt_constructor_exists():
    assert callable(myDsl::SimpleStmt.__init__)


def test_mydsl::simplestmt_constructor_args():
    sig = inspect.signature(myDsl::SimpleStmt.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::labeledstmt_is_not_abstract():
    assert not inspect.isabstract(myDsl::LabeledStmt)


def test_mydsl::labeledstmt_constructor_exists():
    assert callable(myDsl::LabeledStmt.__init__)


def test_mydsl::labeledstmt_constructor_args():
    sig = inspect.signature(myDsl::LabeledStmt.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::binary::op_is_not_abstract():
    assert not inspect.isabstract(myDsl::BINARY::OP)


def test_mydsl::binary::op_constructor_exists():
    assert callable(myDsl::BINARY::OP.__init__)


def test_mydsl::binary::op_constructor_args():
    sig = inspect.signature(myDsl::BINARY::OP.__init__)
    params = list(sig.parameters.keys())
    assert "rEL_OP" in params, "Missing parameter 'rEL_OP'"
    assert "aDD_OP" in params, "Missing parameter 'aDD_OP'"

def test_mydsl::binary::op_has_rEL_OP():
    assert hasattr(myDsl::BINARY::OP, "rEL_OP")
    descriptor = None
    for klass in myDsl::BINARY::OP.__mro__:
        if "rEL_OP" in klass.__dict__:
            descriptor = klass.__dict__["rEL_OP"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::binary::op_has_aDD_OP():
    assert hasattr(myDsl::BINARY::OP, "aDD_OP")
    descriptor = None
    for klass in myDsl::BINARY::OP.__mro__:
        if "aDD_OP" in klass.__dict__:
            descriptor = klass.__dict__["aDD_OP"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expression1_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expression1)


def test_mydsl::expression1_constructor_exists():
    assert callable(myDsl::Expression1.__init__)


def test_mydsl::expression1_constructor_args():
    sig = inspect.signature(myDsl::Expression1.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::typeassertion_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeAssertion)


def test_mydsl::typeassertion_constructor_exists():
    assert callable(myDsl::TypeAssertion.__init__)


def test_mydsl::typeassertion_constructor_args():
    sig = inspect.signature(myDsl::TypeAssertion.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::unaryexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl::UnaryExpr)


def test_mydsl::unaryexpr_constructor_exists():
    assert callable(myDsl::UnaryExpr.__init__)


def test_mydsl::unaryexpr_constructor_args():
    sig = inspect.signature(myDsl::UnaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::receivertype_is_not_abstract():
    assert not inspect.isabstract(myDsl::ReceiverType)


def test_mydsl::receivertype_constructor_exists():
    assert callable(myDsl::ReceiverType.__init__)


def test_mydsl::receivertype_constructor_args():
    sig = inspect.signature(myDsl::ReceiverType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::arguments_is_not_abstract():
    assert not inspect.isabstract(myDsl::Arguments)


def test_mydsl::arguments_constructor_exists():
    assert callable(myDsl::Arguments.__init__)


def test_mydsl::arguments_constructor_args():
    sig = inspect.signature(myDsl::Arguments.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::slice_is_not_abstract():
    assert not inspect.isabstract(myDsl::Slice)


def test_mydsl::slice_constructor_exists():
    assert callable(myDsl::Slice.__init__)


def test_mydsl::slice_constructor_args():
    sig = inspect.signature(myDsl::Slice.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::index_is_not_abstract():
    assert not inspect.isabstract(myDsl::Index)


def test_mydsl::index_constructor_exists():
    assert callable(myDsl::Index.__init__)


def test_mydsl::index_constructor_args():
    sig = inspect.signature(myDsl::Index.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::selector_is_not_abstract():
    assert not inspect.isabstract(myDsl::Selector)


def test_mydsl::selector_constructor_exists():
    assert callable(myDsl::Selector.__init__)


def test_mydsl::selector_constructor_args():
    sig = inspect.signature(myDsl::Selector.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::selector_has_id():
    assert hasattr(myDsl::Selector, "id")
    descriptor = None
    for klass in myDsl::Selector.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::methodexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl::MethodExpr)


def test_mydsl::methodexpr_constructor_exists():
    assert callable(myDsl::MethodExpr.__init__)


def test_mydsl::methodexpr_constructor_args():
    sig = inspect.signature(myDsl::MethodExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::conversion_is_not_abstract():
    assert not inspect.isabstract(myDsl::Conversion)


def test_mydsl::conversion_constructor_exists():
    assert callable(myDsl::Conversion.__init__)


def test_mydsl::conversion_constructor_args():
    sig = inspect.signature(myDsl::Conversion.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::primaryexprlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::PrimaryExprLinha)


def test_mydsl::primaryexprlinha_constructor_exists():
    assert callable(myDsl::PrimaryExprLinha.__init__)


def test_mydsl::primaryexprlinha_constructor_args():
    sig = inspect.signature(myDsl::PrimaryExprLinha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::primaryexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl::PrimaryExpr)


def test_mydsl::primaryexpr_constructor_exists():
    assert callable(myDsl::PrimaryExpr.__init__)


def test_mydsl::primaryexpr_constructor_args():
    sig = inspect.signature(myDsl::PrimaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::fieldname_is_not_abstract():
    assert not inspect.isabstract(myDsl::FieldName)


def test_mydsl::fieldname_constructor_exists():
    assert callable(myDsl::FieldName.__init__)


def test_mydsl::fieldname_constructor_args():
    sig = inspect.signature(myDsl::FieldName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::fieldname_has_id():
    assert hasattr(myDsl::FieldName, "id")
    descriptor = None
    for klass in myDsl::FieldName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::element_is_not_abstract():
    assert not inspect.isabstract(myDsl::Element)


def test_mydsl::element_constructor_exists():
    assert callable(myDsl::Element.__init__)


def test_mydsl::element_constructor_args():
    sig = inspect.signature(myDsl::Element.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::key_is_not_abstract():
    assert not inspect.isabstract(myDsl::Key)


def test_mydsl::key_constructor_exists():
    assert callable(myDsl::Key.__init__)


def test_mydsl::key_constructor_args():
    sig = inspect.signature(myDsl::Key.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::keyedelement_is_not_abstract():
    assert not inspect.isabstract(myDsl::KeyedElement)


def test_mydsl::keyedelement_constructor_exists():
    assert callable(myDsl::KeyedElement.__init__)


def test_mydsl::keyedelement_constructor_args():
    sig = inspect.signature(myDsl::KeyedElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::elementlist_is_not_abstract():
    assert not inspect.isabstract(myDsl::ElementList)


def test_mydsl::elementlist_constructor_exists():
    assert callable(myDsl::ElementList.__init__)


def test_mydsl::elementlist_constructor_args():
    sig = inspect.signature(myDsl::ElementList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::literaltypelinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::LiteralTypeLinha)


def test_mydsl::literaltypelinha_constructor_exists():
    assert callable(myDsl::LiteralTypeLinha.__init__)


def test_mydsl::literaltypelinha_constructor_args():
    sig = inspect.signature(myDsl::LiteralTypeLinha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::literalvalue_is_not_abstract():
    assert not inspect.isabstract(myDsl::LiteralValue)


def test_mydsl::literalvalue_constructor_exists():
    assert callable(myDsl::LiteralValue.__init__)


def test_mydsl::literalvalue_constructor_args():
    sig = inspect.signature(myDsl::LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::literaltype_is_not_abstract():
    assert not inspect.isabstract(myDsl::LiteralType)


def test_mydsl::literaltype_constructor_exists():
    assert callable(myDsl::LiteralType.__init__)


def test_mydsl::literaltype_constructor_args():
    sig = inspect.signature(myDsl::LiteralType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::functionlit_is_not_abstract():
    assert not inspect.isabstract(myDsl::FunctionLit)


def test_mydsl::functionlit_constructor_exists():
    assert callable(myDsl::FunctionLit.__init__)


def test_mydsl::functionlit_constructor_args():
    sig = inspect.signature(myDsl::FunctionLit.__init__)
    params = list(sig.parameters.keys())
    assert "func" in params, "Missing parameter 'func'"

def test_mydsl::functionlit_has_func():
    assert hasattr(myDsl::FunctionLit, "func")
    descriptor = None
    for klass in myDsl::FunctionLit.__mro__:
        if "func" in klass.__dict__:
            descriptor = klass.__dict__["func"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::compositelit_is_not_abstract():
    assert not inspect.isabstract(myDsl::CompositeLit)


def test_mydsl::compositelit_constructor_exists():
    assert callable(myDsl::CompositeLit.__init__)


def test_mydsl::compositelit_constructor_args():
    sig = inspect.signature(myDsl::CompositeLit.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::basiclit_is_not_abstract():
    assert not inspect.isabstract(myDsl::BasicLit)


def test_mydsl::basiclit_constructor_exists():
    assert callable(myDsl::BasicLit.__init__)


def test_mydsl::basiclit_constructor_args():
    sig = inspect.signature(myDsl::BasicLit.__init__)
    params = list(sig.parameters.keys())
    assert "imaginary_lit" in params, "Missing parameter 'imaginary_lit'"
    assert "float_lit" in params, "Missing parameter 'float_lit'"
    assert "int_lit" in params, "Missing parameter 'int_lit'"
    assert "string_lit" in params, "Missing parameter 'string_lit'"
    assert "rune_lit" in params, "Missing parameter 'rune_lit'"

def test_mydsl::basiclit_has_imaginary_lit():
    assert hasattr(myDsl::BasicLit, "imaginary_lit")
    descriptor = None
    for klass in myDsl::BasicLit.__mro__:
        if "imaginary_lit" in klass.__dict__:
            descriptor = klass.__dict__["imaginary_lit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::basiclit_has_float_lit():
    assert hasattr(myDsl::BasicLit, "float_lit")
    descriptor = None
    for klass in myDsl::BasicLit.__mro__:
        if "float_lit" in klass.__dict__:
            descriptor = klass.__dict__["float_lit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::basiclit_has_int_lit():
    assert hasattr(myDsl::BasicLit, "int_lit")
    descriptor = None
    for klass in myDsl::BasicLit.__mro__:
        if "int_lit" in klass.__dict__:
            descriptor = klass.__dict__["int_lit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::basiclit_has_string_lit():
    assert hasattr(myDsl::BasicLit, "string_lit")
    descriptor = None
    for klass in myDsl::BasicLit.__mro__:
        if "string_lit" in klass.__dict__:
            descriptor = klass.__dict__["string_lit"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::basiclit_has_rune_lit():
    assert hasattr(myDsl::BasicLit, "rune_lit")
    descriptor = None
    for klass in myDsl::BasicLit.__mro__:
        if "rune_lit" in klass.__dict__:
            descriptor = klass.__dict__["rune_lit"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::operandname_is_not_abstract():
    assert not inspect.isabstract(myDsl::OperandName)


def test_mydsl::operandname_constructor_exists():
    assert callable(myDsl::OperandName.__init__)


def test_mydsl::operandname_constructor_args():
    sig = inspect.signature(myDsl::OperandName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::operandname_has_id():
    assert hasattr(myDsl::OperandName, "id")
    descriptor = None
    for klass in myDsl::OperandName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::literal_is_not_abstract():
    assert not inspect.isabstract(myDsl::Literal)


def test_mydsl::literal_constructor_exists():
    assert callable(myDsl::Literal.__init__)


def test_mydsl::literal_constructor_args():
    sig = inspect.signature(myDsl::Literal.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::operand_is_not_abstract():
    assert not inspect.isabstract(myDsl::Operand)


def test_mydsl::operand_constructor_exists():
    assert callable(myDsl::Operand.__init__)


def test_mydsl::operand_constructor_args():
    sig = inspect.signature(myDsl::Operand.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::receiver_is_not_abstract():
    assert not inspect.isabstract(myDsl::Receiver)


def test_mydsl::receiver_constructor_exists():
    assert callable(myDsl::Receiver.__init__)


def test_mydsl::receiver_constructor_args():
    sig = inspect.signature(myDsl::Receiver.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::functionbody_is_not_abstract():
    assert not inspect.isabstract(myDsl::FunctionBody)


def test_mydsl::functionbody_constructor_exists():
    assert callable(myDsl::FunctionBody.__init__)


def test_mydsl::functionbody_constructor_args():
    sig = inspect.signature(myDsl::FunctionBody.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::functionname_is_not_abstract():
    assert not inspect.isabstract(myDsl::FunctionName)


def test_mydsl::functionname_constructor_exists():
    assert callable(myDsl::FunctionName.__init__)


def test_mydsl::functionname_constructor_args():
    sig = inspect.signature(myDsl::FunctionName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::functionname_has_id():
    assert hasattr(myDsl::FunctionName, "id")
    descriptor = None
    for klass in myDsl::FunctionName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::shortvardecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::ShortVarDecl)


def test_mydsl::shortvardecl_constructor_exists():
    assert callable(myDsl::ShortVarDecl.__init__)


def test_mydsl::shortvardecl_constructor_args():
    sig = inspect.signature(myDsl::ShortVarDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::constspec_is_not_abstract():
    assert not inspect.isabstract(myDsl::ConstSpec)


def test_mydsl::constspec_constructor_exists():
    assert callable(myDsl::ConstSpec.__init__)


def test_mydsl::constspec_constructor_args():
    sig = inspect.signature(myDsl::ConstSpec.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::varspec_is_not_abstract():
    assert not inspect.isabstract(myDsl::VarSpec)


def test_mydsl::varspec_constructor_exists():
    assert callable(myDsl::VarSpec.__init__)


def test_mydsl::varspec_constructor_args():
    sig = inspect.signature(myDsl::VarSpec.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::typedef_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeDef)


def test_mydsl::typedef_constructor_exists():
    assert callable(myDsl::TypeDef.__init__)


def test_mydsl::typedef_constructor_args():
    sig = inspect.signature(myDsl::TypeDef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::typedef_has_id():
    assert hasattr(myDsl::TypeDef, "id")
    descriptor = None
    for klass in myDsl::TypeDef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::aliasdecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::AliasDecl)


def test_mydsl::aliasdecl_constructor_exists():
    assert callable(myDsl::AliasDecl.__init__)


def test_mydsl::aliasdecl_constructor_args():
    sig = inspect.signature(myDsl::AliasDecl.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::aliasdecl_has_id():
    assert hasattr(myDsl::AliasDecl, "id")
    descriptor = None
    for klass in myDsl::AliasDecl.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::typespec_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeSpec)


def test_mydsl::typespec_constructor_exists():
    assert callable(myDsl::TypeSpec.__init__)


def test_mydsl::typespec_constructor_args():
    sig = inspect.signature(myDsl::TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expressionlist_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExpressionList)


def test_mydsl::expressionlist_constructor_exists():
    assert callable(myDsl::ExpressionList.__init__)


def test_mydsl::expressionlist_constructor_args():
    sig = inspect.signature(myDsl::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::channeltypelinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::ChannelTypeLinha)


def test_mydsl::channeltypelinha_constructor_exists():
    assert callable(myDsl::ChannelTypeLinha.__init__)


def test_mydsl::channeltypelinha_constructor_args():
    sig = inspect.signature(myDsl::ChannelTypeLinha.__init__)
    params = list(sig.parameters.keys())
    assert "aNY_OTHER" in params, "Missing parameter 'aNY_OTHER'"

def test_mydsl::channeltypelinha_has_aNY_OTHER():
    assert hasattr(myDsl::ChannelTypeLinha, "aNY_OTHER")
    descriptor = None
    for klass in myDsl::ChannelTypeLinha.__mro__:
        if "aNY_OTHER" in klass.__dict__:
            descriptor = klass.__dict__["aNY_OTHER"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::methoddecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::MethodDecl)


def test_mydsl::methoddecl_constructor_exists():
    assert callable(myDsl::MethodDecl.__init__)


def test_mydsl::methoddecl_constructor_args():
    sig = inspect.signature(myDsl::MethodDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::functiondecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::FunctionDecl)


def test_mydsl::functiondecl_constructor_exists():
    assert callable(myDsl::FunctionDecl.__init__)


def test_mydsl::functiondecl_constructor_args():
    sig = inspect.signature(myDsl::FunctionDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::topleveldecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::TopLevelDecl)


def test_mydsl::topleveldecl_constructor_exists():
    assert callable(myDsl::TopLevelDecl.__init__)


def test_mydsl::topleveldecl_constructor_args():
    sig = inspect.signature(myDsl::TopLevelDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::vardecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::VarDecl)


def test_mydsl::vardecl_constructor_exists():
    assert callable(myDsl::VarDecl.__init__)


def test_mydsl::vardecl_constructor_args():
    sig = inspect.signature(myDsl::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_mydsl::vardecl_has_var():
    assert hasattr(myDsl::VarDecl, "var")
    descriptor = None
    for klass in myDsl::VarDecl.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::typedecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeDecl)


def test_mydsl::typedecl_constructor_exists():
    assert callable(myDsl::TypeDecl.__init__)


def test_mydsl::typedecl_constructor_args():
    sig = inspect.signature(myDsl::TypeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "typekeyword" in params, "Missing parameter 'typekeyword'"

def test_mydsl::typedecl_has_typekeyword():
    assert hasattr(myDsl::TypeDecl, "typekeyword")
    descriptor = None
    for klass in myDsl::TypeDecl.__mro__:
        if "typekeyword" in klass.__dict__:
            descriptor = klass.__dict__["typekeyword"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::constdecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::ConstDecl)


def test_mydsl::constdecl_constructor_exists():
    assert callable(myDsl::ConstDecl.__init__)


def test_mydsl::constdecl_constructor_args():
    sig = inspect.signature(myDsl::ConstDecl.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"

def test_mydsl::constdecl_has_const():
    assert hasattr(myDsl::ConstDecl, "const")
    descriptor = None
    for klass in myDsl::ConstDecl.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::Declaration)


def test_mydsl::declaration_constructor_exists():
    assert callable(myDsl::Declaration.__init__)


def test_mydsl::declaration_constructor_args():
    sig = inspect.signature(myDsl::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::Statement)


def test_mydsl::statement_constructor_exists():
    assert callable(myDsl::Statement.__init__)


def test_mydsl::statement_constructor_args():
    sig = inspect.signature(myDsl::Statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::statementlist_is_not_abstract():
    assert not inspect.isabstract(myDsl::StatementList)


def test_mydsl::statementlist_constructor_exists():
    assert callable(myDsl::StatementList.__init__)


def test_mydsl::statementlist_constructor_args():
    sig = inspect.signature(myDsl::StatementList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block_is_not_abstract():
    assert not inspect.isabstract(myDsl::Block)


def test_mydsl::block_constructor_exists():
    assert callable(myDsl::Block.__init__)


def test_mydsl::block_constructor_args():
    sig = inspect.signature(myDsl::Block.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::result_is_not_abstract():
    assert not inspect.isabstract(myDsl::Result)


def test_mydsl::result_constructor_exists():
    assert callable(myDsl::Result.__init__)


def test_mydsl::result_constructor_args():
    sig = inspect.signature(myDsl::Result.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::keytype_is_not_abstract():
    assert not inspect.isabstract(myDsl::KeyType)


def test_mydsl::keytype_constructor_exists():
    assert callable(myDsl::KeyType.__init__)


def test_mydsl::keytype_constructor_args():
    sig = inspect.signature(myDsl::KeyType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::interfacetypename_is_not_abstract():
    assert not inspect.isabstract(myDsl::InterfaceTypeName)


def test_mydsl::interfacetypename_constructor_exists():
    assert callable(myDsl::InterfaceTypeName.__init__)


def test_mydsl::interfacetypename_constructor_args():
    sig = inspect.signature(myDsl::InterfaceTypeName.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::methodname_is_not_abstract():
    assert not inspect.isabstract(myDsl::MethodName)


def test_mydsl::methodname_constructor_exists():
    assert callable(myDsl::MethodName.__init__)


def test_mydsl::methodname_constructor_args():
    sig = inspect.signature(myDsl::MethodName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::methodname_has_id():
    assert hasattr(myDsl::MethodName, "id")
    descriptor = None
    for klass in myDsl::MethodName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::methodspec_is_not_abstract():
    assert not inspect.isabstract(myDsl::MethodSpec)


def test_mydsl::methodspec_constructor_exists():
    assert callable(myDsl::MethodSpec.__init__)


def test_mydsl::methodspec_constructor_args():
    sig = inspect.signature(myDsl::MethodSpec.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameterdecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::ParameterDecl)


def test_mydsl::parameterdecl_constructor_exists():
    assert callable(myDsl::ParameterDecl.__init__)


def test_mydsl::parameterdecl_constructor_args():
    sig = inspect.signature(myDsl::ParameterDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameterlist_is_not_abstract():
    assert not inspect.isabstract(myDsl::ParameterList)


def test_mydsl::parameterlist_constructor_exists():
    assert callable(myDsl::ParameterList.__init__)


def test_mydsl::parameterlist_constructor_args():
    sig = inspect.signature(myDsl::ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::channeltype_is_not_abstract():
    assert not inspect.isabstract(myDsl::ChannelType)


def test_mydsl::channeltype_constructor_exists():
    assert callable(myDsl::ChannelType.__init__)


def test_mydsl::channeltype_constructor_args():
    sig = inspect.signature(myDsl::ChannelType.__init__)
    params = list(sig.parameters.keys())
    assert "chan" in params, "Missing parameter 'chan'"

def test_mydsl::channeltype_has_chan():
    assert hasattr(myDsl::ChannelType, "chan")
    descriptor = None
    for klass in myDsl::ChannelType.__mro__:
        if "chan" in klass.__dict__:
            descriptor = klass.__dict__["chan"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::parameters_is_not_abstract():
    assert not inspect.isabstract(myDsl::Parameters)


def test_mydsl::parameters_constructor_exists():
    assert callable(myDsl::Parameters.__init__)


def test_mydsl::parameters_constructor_args():
    sig = inspect.signature(myDsl::Parameters.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::signature_is_not_abstract():
    assert not inspect.isabstract(myDsl::Signature)


def test_mydsl::signature_constructor_exists():
    assert callable(myDsl::Signature.__init__)


def test_mydsl::signature_constructor_args():
    sig = inspect.signature(myDsl::Signature.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::basetype_is_not_abstract():
    assert not inspect.isabstract(myDsl::BaseType)


def test_mydsl::basetype_constructor_exists():
    assert callable(myDsl::BaseType.__init__)


def test_mydsl::basetype_constructor_args():
    sig = inspect.signature(myDsl::BaseType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::tag_is_not_abstract():
    assert not inspect.isabstract(myDsl::Tag)


def test_mydsl::tag_constructor_exists():
    assert callable(myDsl::Tag.__init__)


def test_mydsl::tag_constructor_args():
    sig = inspect.signature(myDsl::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "string_lit" in params, "Missing parameter 'string_lit'"

def test_mydsl::tag_has_string_lit():
    assert hasattr(myDsl::Tag, "string_lit")
    descriptor = None
    for klass in myDsl::Tag.__mro__:
        if "string_lit" in klass.__dict__:
            descriptor = klass.__dict__["string_lit"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::embeddedfield_is_not_abstract():
    assert not inspect.isabstract(myDsl::EmbeddedField)


def test_mydsl::embeddedfield_constructor_exists():
    assert callable(myDsl::EmbeddedField.__init__)


def test_mydsl::embeddedfield_constructor_args():
    sig = inspect.signature(myDsl::EmbeddedField.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::identifierlist_is_not_abstract():
    assert not inspect.isabstract(myDsl::IdentifierList)


def test_mydsl::identifierlist_constructor_exists():
    assert callable(myDsl::IdentifierList.__init__)


def test_mydsl::identifierlist_constructor_args():
    sig = inspect.signature(myDsl::IdentifierList.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "id1" in params, "Missing parameter 'id1'"

def test_mydsl::identifierlist_has_id():
    assert hasattr(myDsl::IdentifierList, "id")
    descriptor = None
    for klass in myDsl::IdentifierList.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::identifierlist_has_id1():
    assert hasattr(myDsl::IdentifierList, "id1")
    descriptor = None
    for klass in myDsl::IdentifierList.__mro__:
        if "id1" in klass.__dict__:
            descriptor = klass.__dict__["id1"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::fielddecl_is_not_abstract():
    assert not inspect.isabstract(myDsl::FieldDecl)


def test_mydsl::fielddecl_constructor_exists():
    assert callable(myDsl::FieldDecl.__init__)


def test_mydsl::fielddecl_constructor_args():
    sig = inspect.signature(myDsl::FieldDecl.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expression)


def test_mydsl::expression_constructor_exists():
    assert callable(myDsl::Expression.__init__)


def test_mydsl::expression_constructor_args():
    sig = inspect.signature(myDsl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::elementtype_is_not_abstract():
    assert not inspect.isabstract(myDsl::ElementType)


def test_mydsl::elementtype_constructor_exists():
    assert callable(myDsl::ElementType.__init__)


def test_mydsl::elementtype_constructor_args():
    sig = inspect.signature(myDsl::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::arraylength_is_not_abstract():
    assert not inspect.isabstract(myDsl::ArrayLength)


def test_mydsl::arraylength_constructor_exists():
    assert callable(myDsl::ArrayLength.__init__)


def test_mydsl::arraylength_constructor_args():
    sig = inspect.signature(myDsl::ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::maptype_is_not_abstract():
    assert not inspect.isabstract(myDsl::MapType)


def test_mydsl::maptype_constructor_exists():
    assert callable(myDsl::MapType.__init__)


def test_mydsl::maptype_constructor_args():
    sig = inspect.signature(myDsl::MapType.__init__)
    params = list(sig.parameters.keys())
    assert "map" in params, "Missing parameter 'map'"

def test_mydsl::maptype_has_map():
    assert hasattr(myDsl::MapType, "map")
    descriptor = None
    for klass in myDsl::MapType.__mro__:
        if "map" in klass.__dict__:
            descriptor = klass.__dict__["map"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::interfacetype_is_not_abstract():
    assert not inspect.isabstract(myDsl::InterfaceType)


def test_mydsl::interfacetype_constructor_exists():
    assert callable(myDsl::InterfaceType.__init__)


def test_mydsl::interfacetype_constructor_args():
    sig = inspect.signature(myDsl::InterfaceType.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"

def test_mydsl::interfacetype_has_interface():
    assert hasattr(myDsl::InterfaceType, "interface")
    descriptor = None
    for klass in myDsl::InterfaceType.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::functiontype_is_not_abstract():
    assert not inspect.isabstract(myDsl::FunctionType)


def test_mydsl::functiontype_constructor_exists():
    assert callable(myDsl::FunctionType.__init__)


def test_mydsl::functiontype_constructor_args():
    sig = inspect.signature(myDsl::FunctionType.__init__)
    params = list(sig.parameters.keys())
    assert "func" in params, "Missing parameter 'func'"

def test_mydsl::functiontype_has_func():
    assert hasattr(myDsl::FunctionType, "func")
    descriptor = None
    for klass in myDsl::FunctionType.__mro__:
        if "func" in klass.__dict__:
            descriptor = klass.__dict__["func"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::pointertype_is_not_abstract():
    assert not inspect.isabstract(myDsl::PointerType)


def test_mydsl::pointertype_constructor_exists():
    assert callable(myDsl::PointerType.__init__)


def test_mydsl::pointertype_constructor_args():
    sig = inspect.signature(myDsl::PointerType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::structtype_is_not_abstract():
    assert not inspect.isabstract(myDsl::StructType)


def test_mydsl::structtype_constructor_exists():
    assert callable(myDsl::StructType.__init__)


def test_mydsl::structtype_constructor_args():
    sig = inspect.signature(myDsl::StructType.__init__)
    params = list(sig.parameters.keys())
    assert "struct" in params, "Missing parameter 'struct'"

def test_mydsl::structtype_has_struct():
    assert hasattr(myDsl::StructType, "struct")
    descriptor = None
    for klass in myDsl::StructType.__mro__:
        if "struct" in klass.__dict__:
            descriptor = klass.__dict__["struct"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::typelitlinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeLitLinha)


def test_mydsl::typelitlinha_constructor_exists():
    assert callable(myDsl::TypeLitLinha.__init__)


def test_mydsl::typelitlinha_constructor_args():
    sig = inspect.signature(myDsl::TypeLitLinha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::typenamelinha_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeNameLinha)


def test_mydsl::typenamelinha_constructor_exists():
    assert callable(myDsl::TypeNameLinha.__init__)


def test_mydsl::typenamelinha_constructor_args():
    sig = inspect.signature(myDsl::TypeNameLinha.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::typenamelinha_has_id():
    assert hasattr(myDsl::TypeNameLinha, "id")
    descriptor = None
    for klass in myDsl::TypeNameLinha.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::typelit_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeLit)


def test_mydsl::typelit_constructor_exists():
    assert callable(myDsl::TypeLit.__init__)


def test_mydsl::typelit_constructor_args():
    sig = inspect.signature(myDsl::TypeLit.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::typename_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeName)


def test_mydsl::typename_constructor_exists():
    assert callable(myDsl::TypeName.__init__)


def test_mydsl::typename_constructor_args():
    sig = inspect.signature(myDsl::TypeName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::typename_has_id():
    assert hasattr(myDsl::TypeName, "id")
    descriptor = None
    for klass in myDsl::TypeName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::sourcefile_is_not_abstract():
    assert not inspect.isabstract(myDsl::SourceFile)


def test_mydsl::sourcefile_constructor_exists():
    assert callable(myDsl::SourceFile.__init__)


def test_mydsl::sourcefile_constructor_args():
    sig = inspect.signature(myDsl::SourceFile.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
myDsl::ImportSpec_strategy = st.builds(
    myDsl::ImportSpec,
    sTRING_LIT=
        safe_text
)
myDsl::PackageName_strategy = st.builds(
    myDsl::PackageName,
    id=
        safe_text
)
myDsl::ImportDecl_strategy = st.builds(
    myDsl::ImportDecl,
    importt=
        safe_text
)
myDsl::PackageClause_strategy = st.builds(
    myDsl::PackageClause,
    package=
        safe_text
)
myDsl::RecvExpr_strategy = st.builds(
    myDsl::RecvExpr,
)
myDsl::CommCaseLinha_strategy = st.builds(
    myDsl::CommCaseLinha,
)
myDsl::CommCase_strategy = st.builds(
    myDsl::CommCase,
    case=
        safe_text,
    default=
        safe_text
)
myDsl::CommClause_strategy = st.builds(
    myDsl::CommClause,
)
myDsl::ForStmtLinhaLinha_strategy = st.builds(
    myDsl::ForStmtLinhaLinha,
    range=
        safe_text
)
myDsl::PostStmt_strategy = st.builds(
    myDsl::PostStmt,
)
myDsl::Condition_strategy = st.builds(
    myDsl::Condition,
)
myDsl::ForStmtLinha_strategy = st.builds(
    myDsl::ForStmtLinha,
    vazio=
        safe_text
)
myDsl::TypeList_strategy = st.builds(
    myDsl::TypeList,
)
myDsl::TypeSwitchCase_strategy = st.builds(
    myDsl::TypeSwitchCase,
    case=
        safe_text,
    default=
        safe_text
)
myDsl::TypeCaseClause_strategy = st.builds(
    myDsl::TypeCaseClause,
)
myDsl::TypeSwitchGuard_strategy = st.builds(
    myDsl::TypeSwitchGuard,
    id=
        safe_text,
    type=
        safe_text
)
myDsl::ExprSwitchCase_strategy = st.builds(
    myDsl::ExprSwitchCase,
    case=
        safe_text,
    default=
        safe_text
)
myDsl::ExprCaseClause_strategy = st.builds(
    myDsl::ExprCaseClause,
)
myDsl::TypeSwitchStmt_strategy = st.builds(
    myDsl::TypeSwitchStmt,
    switch=
        safe_text
)
myDsl::ExprSwitchStmt_strategy = st.builds(
    myDsl::ExprSwitchStmt,
    switch=
        safe_text
)
myDsl::IfStmtLinha_strategy = st.builds(
    myDsl::IfStmtLinha,
    else_=
        safe_text
)
myDsl::Label_strategy = st.builds(
    myDsl::Label,
    id=
        safe_text
)
myDsl::assign::op_strategy = st.builds(
    myDsl::assign::op,
    aDD_OP=
        safe_text,
    mUL_OP=
        safe_text
)
myDsl::SimpleStmtLinha_strategy = st.builds(
    myDsl::SimpleStmtLinha,
    aNY_OTHER=
        safe_text
)
myDsl::EmptyStmt_strategy = st.builds(
    myDsl::EmptyStmt,
    aNY_OTHER=
        safe_text
)
myDsl::DeferStmt_strategy = st.builds(
    myDsl::DeferStmt,
    defer=
        safe_text
)
myDsl::ForStmt_strategy = st.builds(
    myDsl::ForStmt,
    range=
        safe_text,
    for_=
        safe_text
)
myDsl::SelectStmt_strategy = st.builds(
    myDsl::SelectStmt,
    select=
        safe_text
)
myDsl::SwitchStmt_strategy = st.builds(
    myDsl::SwitchStmt,
)
myDsl::IfStmt_strategy = st.builds(
    myDsl::IfStmt,
    else_=
        safe_text,
    if_=
        safe_text
)
myDsl::Expression::Linha_strategy = st.builds(
    myDsl::Expression::Linha,
)
myDsl::FallthroughStmt_strategy = st.builds(
    myDsl::FallthroughStmt,
    fallthrough=
        safe_text
)
myDsl::GotoStmt_strategy = st.builds(
    myDsl::GotoStmt,
    goto=
        safe_text
)
myDsl::ContinueStmt_strategy = st.builds(
    myDsl::ContinueStmt,
    continue_=
        safe_text
)
myDsl::BreakStmt_strategy = st.builds(
    myDsl::BreakStmt,
    break_=
        safe_text
)
myDsl::ReturnStmt_strategy = st.builds(
    myDsl::ReturnStmt,
    return_=
        safe_text
)
myDsl::GoStmt_strategy = st.builds(
    myDsl::GoStmt,
    go=
        safe_text
)
myDsl::SimpleStmt_strategy = st.builds(
    myDsl::SimpleStmt,
)
myDsl::LabeledStmt_strategy = st.builds(
    myDsl::LabeledStmt,
)
myDsl::BINARY::OP_strategy = st.builds(
    myDsl::BINARY::OP,
    rEL_OP=
        safe_text,
    aDD_OP=
        safe_text
)
myDsl::Expression1_strategy = st.builds(
    myDsl::Expression1,
)
myDsl::TypeAssertion_strategy = st.builds(
    myDsl::TypeAssertion,
)
myDsl::UnaryExpr_strategy = st.builds(
    myDsl::UnaryExpr,
)
myDsl::ReceiverType_strategy = st.builds(
    myDsl::ReceiverType,
)
myDsl::Arguments_strategy = st.builds(
    myDsl::Arguments,
)
myDsl::Slice_strategy = st.builds(
    myDsl::Slice,
)
myDsl::Index_strategy = st.builds(
    myDsl::Index,
)
myDsl::Selector_strategy = st.builds(
    myDsl::Selector,
    id=
        safe_text
)
myDsl::MethodExpr_strategy = st.builds(
    myDsl::MethodExpr,
)
myDsl::Conversion_strategy = st.builds(
    myDsl::Conversion,
)
myDsl::PrimaryExprLinha_strategy = st.builds(
    myDsl::PrimaryExprLinha,
)
myDsl::PrimaryExpr_strategy = st.builds(
    myDsl::PrimaryExpr,
)
myDsl::FieldName_strategy = st.builds(
    myDsl::FieldName,
    id=
        safe_text
)
myDsl::Element_strategy = st.builds(
    myDsl::Element,
)
myDsl::Key_strategy = st.builds(
    myDsl::Key,
)
myDsl::KeyedElement_strategy = st.builds(
    myDsl::KeyedElement,
)
myDsl::ElementList_strategy = st.builds(
    myDsl::ElementList,
)
myDsl::LiteralTypeLinha_strategy = st.builds(
    myDsl::LiteralTypeLinha,
)
myDsl::LiteralValue_strategy = st.builds(
    myDsl::LiteralValue,
)
myDsl::LiteralType_strategy = st.builds(
    myDsl::LiteralType,
)
myDsl::FunctionLit_strategy = st.builds(
    myDsl::FunctionLit,
    func=
        safe_text
)
myDsl::CompositeLit_strategy = st.builds(
    myDsl::CompositeLit,
)
myDsl::BasicLit_strategy = st.builds(
    myDsl::BasicLit,
    imaginary_lit=
        safe_text,
    float_lit=
        safe_text,
    int_lit=
        safe_text,
    string_lit=
        safe_text,
    rune_lit=
        safe_text
)
myDsl::OperandName_strategy = st.builds(
    myDsl::OperandName,
    id=
        safe_text
)
myDsl::Literal_strategy = st.builds(
    myDsl::Literal,
)
myDsl::Operand_strategy = st.builds(
    myDsl::Operand,
)
myDsl::Receiver_strategy = st.builds(
    myDsl::Receiver,
)
myDsl::FunctionBody_strategy = st.builds(
    myDsl::FunctionBody,
)
myDsl::FunctionName_strategy = st.builds(
    myDsl::FunctionName,
    id=
        safe_text
)
myDsl::ShortVarDecl_strategy = st.builds(
    myDsl::ShortVarDecl,
)
myDsl::ConstSpec_strategy = st.builds(
    myDsl::ConstSpec,
)
myDsl::VarSpec_strategy = st.builds(
    myDsl::VarSpec,
)
myDsl::TypeDef_strategy = st.builds(
    myDsl::TypeDef,
    id=
        safe_text
)
myDsl::AliasDecl_strategy = st.builds(
    myDsl::AliasDecl,
    id=
        safe_text
)
myDsl::TypeSpec_strategy = st.builds(
    myDsl::TypeSpec,
)
myDsl::ExpressionList_strategy = st.builds(
    myDsl::ExpressionList,
)
myDsl::ChannelTypeLinha_strategy = st.builds(
    myDsl::ChannelTypeLinha,
    aNY_OTHER=
        safe_text
)
myDsl::MethodDecl_strategy = st.builds(
    myDsl::MethodDecl,
)
myDsl::FunctionDecl_strategy = st.builds(
    myDsl::FunctionDecl,
)
myDsl::TopLevelDecl_strategy = st.builds(
    myDsl::TopLevelDecl,
)
myDsl::VarDecl_strategy = st.builds(
    myDsl::VarDecl,
    var=
        safe_text
)
myDsl::TypeDecl_strategy = st.builds(
    myDsl::TypeDecl,
    typekeyword=
        safe_text
)
myDsl::ConstDecl_strategy = st.builds(
    myDsl::ConstDecl,
    const=
        safe_text
)
myDsl::Declaration_strategy = st.builds(
    myDsl::Declaration,
)
myDsl::Statement_strategy = st.builds(
    myDsl::Statement,
)
myDsl::StatementList_strategy = st.builds(
    myDsl::StatementList,
)
myDsl::Block_strategy = st.builds(
    myDsl::Block,
)
myDsl::Result_strategy = st.builds(
    myDsl::Result,
)
myDsl::KeyType_strategy = st.builds(
    myDsl::KeyType,
)
myDsl::InterfaceTypeName_strategy = st.builds(
    myDsl::InterfaceTypeName,
)
myDsl::MethodName_strategy = st.builds(
    myDsl::MethodName,
    id=
        safe_text
)
myDsl::MethodSpec_strategy = st.builds(
    myDsl::MethodSpec,
)
myDsl::ParameterDecl_strategy = st.builds(
    myDsl::ParameterDecl,
)
myDsl::ParameterList_strategy = st.builds(
    myDsl::ParameterList,
)
myDsl::ChannelType_strategy = st.builds(
    myDsl::ChannelType,
    chan=
        safe_text
)
myDsl::Parameters_strategy = st.builds(
    myDsl::Parameters,
)
myDsl::Signature_strategy = st.builds(
    myDsl::Signature,
)
myDsl::BaseType_strategy = st.builds(
    myDsl::BaseType,
)
myDsl::Tag_strategy = st.builds(
    myDsl::Tag,
    string_lit=
        safe_text
)
myDsl::EmbeddedField_strategy = st.builds(
    myDsl::EmbeddedField,
)
myDsl::IdentifierList_strategy = st.builds(
    myDsl::IdentifierList,
    id=
        safe_text,
    id1=
        safe_text
)
myDsl::FieldDecl_strategy = st.builds(
    myDsl::FieldDecl,
)
myDsl::Expression_strategy = st.builds(
    myDsl::Expression,
)
myDsl::ElementType_strategy = st.builds(
    myDsl::ElementType,
)
myDsl::ArrayLength_strategy = st.builds(
    myDsl::ArrayLength,
)
myDsl::MapType_strategy = st.builds(
    myDsl::MapType,
    map=
        safe_text
)
myDsl::InterfaceType_strategy = st.builds(
    myDsl::InterfaceType,
    interface=
        safe_text
)
myDsl::FunctionType_strategy = st.builds(
    myDsl::FunctionType,
    func=
        safe_text
)
myDsl::PointerType_strategy = st.builds(
    myDsl::PointerType,
)
myDsl::StructType_strategy = st.builds(
    myDsl::StructType,
    struct=
        safe_text
)
myDsl::TypeLitLinha_strategy = st.builds(
    myDsl::TypeLitLinha,
)
myDsl::TypeNameLinha_strategy = st.builds(
    myDsl::TypeNameLinha,
    id=
        safe_text
)
myDsl::TypeLit_strategy = st.builds(
    myDsl::TypeLit,
)
myDsl::TypeName_strategy = st.builds(
    myDsl::TypeName,
    id=
        safe_text
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
)
myDsl::SourceFile_strategy = st.builds(
    myDsl::SourceFile,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=myDsl::ImportSpec_strategy)
@settings(max_examples=50)
def test_mydsl::importspec_instantiation(instance):
    assert isinstance(instance, myDsl::ImportSpec)

@given(instance=myDsl::ImportSpec_strategy)
def test_mydsl::importspec_sTRING_LIT_type(instance):
    assert isinstance(instance.sTRING_LIT, str)


@given(instance=myDsl::ImportSpec_strategy)
def test_mydsl::importspec_sTRING_LIT_setter(instance):
    original = instance.sTRING_LIT
    instance.sTRING_LIT = original
    assert instance.sTRING_LIT == original

@given(instance=myDsl::PackageName_strategy)
@settings(max_examples=50)
def test_mydsl::packagename_instantiation(instance):
    assert isinstance(instance, myDsl::PackageName)

@given(instance=myDsl::PackageName_strategy)
def test_mydsl::packagename_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::PackageName_strategy)
def test_mydsl::packagename_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::ImportDecl_strategy)
@settings(max_examples=50)
def test_mydsl::importdecl_instantiation(instance):
    assert isinstance(instance, myDsl::ImportDecl)

@given(instance=myDsl::ImportDecl_strategy)
def test_mydsl::importdecl_importt_type(instance):
    assert isinstance(instance.importt, str)


@given(instance=myDsl::ImportDecl_strategy)
def test_mydsl::importdecl_importt_setter(instance):
    original = instance.importt
    instance.importt = original
    assert instance.importt == original

@given(instance=myDsl::PackageClause_strategy)
@settings(max_examples=50)
def test_mydsl::packageclause_instantiation(instance):
    assert isinstance(instance, myDsl::PackageClause)

@given(instance=myDsl::PackageClause_strategy)
def test_mydsl::packageclause_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=myDsl::PackageClause_strategy)
def test_mydsl::packageclause_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=myDsl::RecvExpr_strategy)
@settings(max_examples=50)
def test_mydsl::recvexpr_instantiation(instance):
    assert isinstance(instance, myDsl::RecvExpr)

@given(instance=myDsl::CommCaseLinha_strategy)
@settings(max_examples=50)
def test_mydsl::commcaselinha_instantiation(instance):
    assert isinstance(instance, myDsl::CommCaseLinha)

@given(instance=myDsl::CommCase_strategy)
@settings(max_examples=50)
def test_mydsl::commcase_instantiation(instance):
    assert isinstance(instance, myDsl::CommCase)

@given(instance=myDsl::CommCase_strategy)
def test_mydsl::commcase_case_type(instance):
    assert isinstance(instance.case, str)


@given(instance=myDsl::CommCase_strategy)
def test_mydsl::commcase_case_setter(instance):
    original = instance.case
    instance.case = original
    assert instance.case == original

@given(instance=myDsl::CommCase_strategy)
def test_mydsl::commcase_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=myDsl::CommCase_strategy)
def test_mydsl::commcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=myDsl::CommClause_strategy)
@settings(max_examples=50)
def test_mydsl::commclause_instantiation(instance):
    assert isinstance(instance, myDsl::CommClause)

@given(instance=myDsl::ForStmtLinhaLinha_strategy)
@settings(max_examples=50)
def test_mydsl::forstmtlinhalinha_instantiation(instance):
    assert isinstance(instance, myDsl::ForStmtLinhaLinha)

@given(instance=myDsl::ForStmtLinhaLinha_strategy)
def test_mydsl::forstmtlinhalinha_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=myDsl::ForStmtLinhaLinha_strategy)
def test_mydsl::forstmtlinhalinha_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=myDsl::PostStmt_strategy)
@settings(max_examples=50)
def test_mydsl::poststmt_instantiation(instance):
    assert isinstance(instance, myDsl::PostStmt)

@given(instance=myDsl::Condition_strategy)
@settings(max_examples=50)
def test_mydsl::condition_instantiation(instance):
    assert isinstance(instance, myDsl::Condition)

@given(instance=myDsl::ForStmtLinha_strategy)
@settings(max_examples=50)
def test_mydsl::forstmtlinha_instantiation(instance):
    assert isinstance(instance, myDsl::ForStmtLinha)

@given(instance=myDsl::ForStmtLinha_strategy)
def test_mydsl::forstmtlinha_vazio_type(instance):
    assert isinstance(instance.vazio, str)


@given(instance=myDsl::ForStmtLinha_strategy)
def test_mydsl::forstmtlinha_vazio_setter(instance):
    original = instance.vazio
    instance.vazio = original
    assert instance.vazio == original

@given(instance=myDsl::TypeList_strategy)
@settings(max_examples=50)
def test_mydsl::typelist_instantiation(instance):
    assert isinstance(instance, myDsl::TypeList)

@given(instance=myDsl::TypeSwitchCase_strategy)
@settings(max_examples=50)
def test_mydsl::typeswitchcase_instantiation(instance):
    assert isinstance(instance, myDsl::TypeSwitchCase)

@given(instance=myDsl::TypeSwitchCase_strategy)
def test_mydsl::typeswitchcase_case_type(instance):
    assert isinstance(instance.case, str)


@given(instance=myDsl::TypeSwitchCase_strategy)
def test_mydsl::typeswitchcase_case_setter(instance):
    original = instance.case
    instance.case = original
    assert instance.case == original

@given(instance=myDsl::TypeSwitchCase_strategy)
def test_mydsl::typeswitchcase_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=myDsl::TypeSwitchCase_strategy)
def test_mydsl::typeswitchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=myDsl::TypeCaseClause_strategy)
@settings(max_examples=50)
def test_mydsl::typecaseclause_instantiation(instance):
    assert isinstance(instance, myDsl::TypeCaseClause)

@given(instance=myDsl::TypeSwitchGuard_strategy)
@settings(max_examples=50)
def test_mydsl::typeswitchguard_instantiation(instance):
    assert isinstance(instance, myDsl::TypeSwitchGuard)

@given(instance=myDsl::TypeSwitchGuard_strategy)
def test_mydsl::typeswitchguard_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::TypeSwitchGuard_strategy)
def test_mydsl::typeswitchguard_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::TypeSwitchGuard_strategy)
def test_mydsl::typeswitchguard_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl::TypeSwitchGuard_strategy)
def test_mydsl::typeswitchguard_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl::ExprSwitchCase_strategy)
@settings(max_examples=50)
def test_mydsl::exprswitchcase_instantiation(instance):
    assert isinstance(instance, myDsl::ExprSwitchCase)

@given(instance=myDsl::ExprSwitchCase_strategy)
def test_mydsl::exprswitchcase_case_type(instance):
    assert isinstance(instance.case, str)


@given(instance=myDsl::ExprSwitchCase_strategy)
def test_mydsl::exprswitchcase_case_setter(instance):
    original = instance.case
    instance.case = original
    assert instance.case == original

@given(instance=myDsl::ExprSwitchCase_strategy)
def test_mydsl::exprswitchcase_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=myDsl::ExprSwitchCase_strategy)
def test_mydsl::exprswitchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=myDsl::ExprCaseClause_strategy)
@settings(max_examples=50)
def test_mydsl::exprcaseclause_instantiation(instance):
    assert isinstance(instance, myDsl::ExprCaseClause)

@given(instance=myDsl::TypeSwitchStmt_strategy)
@settings(max_examples=50)
def test_mydsl::typeswitchstmt_instantiation(instance):
    assert isinstance(instance, myDsl::TypeSwitchStmt)

@given(instance=myDsl::TypeSwitchStmt_strategy)
def test_mydsl::typeswitchstmt_switch_type(instance):
    assert isinstance(instance.switch, str)


@given(instance=myDsl::TypeSwitchStmt_strategy)
def test_mydsl::typeswitchstmt_switch_setter(instance):
    original = instance.switch
    instance.switch = original
    assert instance.switch == original

@given(instance=myDsl::ExprSwitchStmt_strategy)
@settings(max_examples=50)
def test_mydsl::exprswitchstmt_instantiation(instance):
    assert isinstance(instance, myDsl::ExprSwitchStmt)

@given(instance=myDsl::ExprSwitchStmt_strategy)
def test_mydsl::exprswitchstmt_switch_type(instance):
    assert isinstance(instance.switch, str)


@given(instance=myDsl::ExprSwitchStmt_strategy)
def test_mydsl::exprswitchstmt_switch_setter(instance):
    original = instance.switch
    instance.switch = original
    assert instance.switch == original

@given(instance=myDsl::IfStmtLinha_strategy)
@settings(max_examples=50)
def test_mydsl::ifstmtlinha_instantiation(instance):
    assert isinstance(instance, myDsl::IfStmtLinha)

@given(instance=myDsl::IfStmtLinha_strategy)
def test_mydsl::ifstmtlinha_else__type(instance):
    assert isinstance(instance.else_, str)


@given(instance=myDsl::IfStmtLinha_strategy)
def test_mydsl::ifstmtlinha_else__setter(instance):
    original = instance.else_
    instance.else_ = original
    assert instance.else_ == original

@given(instance=myDsl::Label_strategy)
@settings(max_examples=50)
def test_mydsl::label_instantiation(instance):
    assert isinstance(instance, myDsl::Label)

@given(instance=myDsl::Label_strategy)
def test_mydsl::label_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::Label_strategy)
def test_mydsl::label_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::assign::op_strategy)
@settings(max_examples=50)
def test_mydsl::assign::op_instantiation(instance):
    assert isinstance(instance, myDsl::assign::op)

@given(instance=myDsl::assign::op_strategy)
def test_mydsl::assign::op_aDD_OP_type(instance):
    assert isinstance(instance.aDD_OP, str)


@given(instance=myDsl::assign::op_strategy)
def test_mydsl::assign::op_aDD_OP_setter(instance):
    original = instance.aDD_OP
    instance.aDD_OP = original
    assert instance.aDD_OP == original

@given(instance=myDsl::assign::op_strategy)
def test_mydsl::assign::op_mUL_OP_type(instance):
    assert isinstance(instance.mUL_OP, str)


@given(instance=myDsl::assign::op_strategy)
def test_mydsl::assign::op_mUL_OP_setter(instance):
    original = instance.mUL_OP
    instance.mUL_OP = original
    assert instance.mUL_OP == original

@given(instance=myDsl::SimpleStmtLinha_strategy)
@settings(max_examples=50)
def test_mydsl::simplestmtlinha_instantiation(instance):
    assert isinstance(instance, myDsl::SimpleStmtLinha)

@given(instance=myDsl::SimpleStmtLinha_strategy)
def test_mydsl::simplestmtlinha_aNY_OTHER_type(instance):
    assert isinstance(instance.aNY_OTHER, str)


@given(instance=myDsl::SimpleStmtLinha_strategy)
def test_mydsl::simplestmtlinha_aNY_OTHER_setter(instance):
    original = instance.aNY_OTHER
    instance.aNY_OTHER = original
    assert instance.aNY_OTHER == original

@given(instance=myDsl::EmptyStmt_strategy)
@settings(max_examples=50)
def test_mydsl::emptystmt_instantiation(instance):
    assert isinstance(instance, myDsl::EmptyStmt)

@given(instance=myDsl::EmptyStmt_strategy)
def test_mydsl::emptystmt_aNY_OTHER_type(instance):
    assert isinstance(instance.aNY_OTHER, str)


@given(instance=myDsl::EmptyStmt_strategy)
def test_mydsl::emptystmt_aNY_OTHER_setter(instance):
    original = instance.aNY_OTHER
    instance.aNY_OTHER = original
    assert instance.aNY_OTHER == original

@given(instance=myDsl::DeferStmt_strategy)
@settings(max_examples=50)
def test_mydsl::deferstmt_instantiation(instance):
    assert isinstance(instance, myDsl::DeferStmt)

@given(instance=myDsl::DeferStmt_strategy)
def test_mydsl::deferstmt_defer_type(instance):
    assert isinstance(instance.defer, str)


@given(instance=myDsl::DeferStmt_strategy)
def test_mydsl::deferstmt_defer_setter(instance):
    original = instance.defer
    instance.defer = original
    assert instance.defer == original

@given(instance=myDsl::ForStmt_strategy)
@settings(max_examples=50)
def test_mydsl::forstmt_instantiation(instance):
    assert isinstance(instance, myDsl::ForStmt)

@given(instance=myDsl::ForStmt_strategy)
def test_mydsl::forstmt_range_type(instance):
    assert isinstance(instance.range, str)


@given(instance=myDsl::ForStmt_strategy)
def test_mydsl::forstmt_range_setter(instance):
    original = instance.range
    instance.range = original
    assert instance.range == original

@given(instance=myDsl::ForStmt_strategy)
def test_mydsl::forstmt_for__type(instance):
    assert isinstance(instance.for_, str)


@given(instance=myDsl::ForStmt_strategy)
def test_mydsl::forstmt_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original

@given(instance=myDsl::SelectStmt_strategy)
@settings(max_examples=50)
def test_mydsl::selectstmt_instantiation(instance):
    assert isinstance(instance, myDsl::SelectStmt)

@given(instance=myDsl::SelectStmt_strategy)
def test_mydsl::selectstmt_select_type(instance):
    assert isinstance(instance.select, str)


@given(instance=myDsl::SelectStmt_strategy)
def test_mydsl::selectstmt_select_setter(instance):
    original = instance.select
    instance.select = original
    assert instance.select == original

@given(instance=myDsl::SwitchStmt_strategy)
@settings(max_examples=50)
def test_mydsl::switchstmt_instantiation(instance):
    assert isinstance(instance, myDsl::SwitchStmt)

@given(instance=myDsl::IfStmt_strategy)
@settings(max_examples=50)
def test_mydsl::ifstmt_instantiation(instance):
    assert isinstance(instance, myDsl::IfStmt)

@given(instance=myDsl::IfStmt_strategy)
def test_mydsl::ifstmt_else__type(instance):
    assert isinstance(instance.else_, str)


@given(instance=myDsl::IfStmt_strategy)
def test_mydsl::ifstmt_else__setter(instance):
    original = instance.else_
    instance.else_ = original
    assert instance.else_ == original

@given(instance=myDsl::IfStmt_strategy)
def test_mydsl::ifstmt_if__type(instance):
    assert isinstance(instance.if_, str)


@given(instance=myDsl::IfStmt_strategy)
def test_mydsl::ifstmt_if__setter(instance):
    original = instance.if_
    instance.if_ = original
    assert instance.if_ == original

@given(instance=myDsl::Expression::Linha_strategy)
@settings(max_examples=50)
def test_mydsl::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::Expression::Linha)

@given(instance=myDsl::FallthroughStmt_strategy)
@settings(max_examples=50)
def test_mydsl::fallthroughstmt_instantiation(instance):
    assert isinstance(instance, myDsl::FallthroughStmt)

@given(instance=myDsl::FallthroughStmt_strategy)
def test_mydsl::fallthroughstmt_fallthrough_type(instance):
    assert isinstance(instance.fallthrough, str)


@given(instance=myDsl::FallthroughStmt_strategy)
def test_mydsl::fallthroughstmt_fallthrough_setter(instance):
    original = instance.fallthrough
    instance.fallthrough = original
    assert instance.fallthrough == original

@given(instance=myDsl::GotoStmt_strategy)
@settings(max_examples=50)
def test_mydsl::gotostmt_instantiation(instance):
    assert isinstance(instance, myDsl::GotoStmt)

@given(instance=myDsl::GotoStmt_strategy)
def test_mydsl::gotostmt_goto_type(instance):
    assert isinstance(instance.goto, str)


@given(instance=myDsl::GotoStmt_strategy)
def test_mydsl::gotostmt_goto_setter(instance):
    original = instance.goto
    instance.goto = original
    assert instance.goto == original

@given(instance=myDsl::ContinueStmt_strategy)
@settings(max_examples=50)
def test_mydsl::continuestmt_instantiation(instance):
    assert isinstance(instance, myDsl::ContinueStmt)

@given(instance=myDsl::ContinueStmt_strategy)
def test_mydsl::continuestmt_continue__type(instance):
    assert isinstance(instance.continue_, str)


@given(instance=myDsl::ContinueStmt_strategy)
def test_mydsl::continuestmt_continue__setter(instance):
    original = instance.continue_
    instance.continue_ = original
    assert instance.continue_ == original

@given(instance=myDsl::BreakStmt_strategy)
@settings(max_examples=50)
def test_mydsl::breakstmt_instantiation(instance):
    assert isinstance(instance, myDsl::BreakStmt)

@given(instance=myDsl::BreakStmt_strategy)
def test_mydsl::breakstmt_break__type(instance):
    assert isinstance(instance.break_, str)


@given(instance=myDsl::BreakStmt_strategy)
def test_mydsl::breakstmt_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=myDsl::ReturnStmt_strategy)
@settings(max_examples=50)
def test_mydsl::returnstmt_instantiation(instance):
    assert isinstance(instance, myDsl::ReturnStmt)

@given(instance=myDsl::ReturnStmt_strategy)
def test_mydsl::returnstmt_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=myDsl::ReturnStmt_strategy)
def test_mydsl::returnstmt_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=myDsl::GoStmt_strategy)
@settings(max_examples=50)
def test_mydsl::gostmt_instantiation(instance):
    assert isinstance(instance, myDsl::GoStmt)

@given(instance=myDsl::GoStmt_strategy)
def test_mydsl::gostmt_go_type(instance):
    assert isinstance(instance.go, str)


@given(instance=myDsl::GoStmt_strategy)
def test_mydsl::gostmt_go_setter(instance):
    original = instance.go
    instance.go = original
    assert instance.go == original

@given(instance=myDsl::SimpleStmt_strategy)
@settings(max_examples=50)
def test_mydsl::simplestmt_instantiation(instance):
    assert isinstance(instance, myDsl::SimpleStmt)

@given(instance=myDsl::LabeledStmt_strategy)
@settings(max_examples=50)
def test_mydsl::labeledstmt_instantiation(instance):
    assert isinstance(instance, myDsl::LabeledStmt)

@given(instance=myDsl::BINARY::OP_strategy)
@settings(max_examples=50)
def test_mydsl::binary::op_instantiation(instance):
    assert isinstance(instance, myDsl::BINARY::OP)

@given(instance=myDsl::BINARY::OP_strategy)
def test_mydsl::binary::op_rEL_OP_type(instance):
    assert isinstance(instance.rEL_OP, str)


@given(instance=myDsl::BINARY::OP_strategy)
def test_mydsl::binary::op_rEL_OP_setter(instance):
    original = instance.rEL_OP
    instance.rEL_OP = original
    assert instance.rEL_OP == original

@given(instance=myDsl::BINARY::OP_strategy)
def test_mydsl::binary::op_aDD_OP_type(instance):
    assert isinstance(instance.aDD_OP, str)


@given(instance=myDsl::BINARY::OP_strategy)
def test_mydsl::binary::op_aDD_OP_setter(instance):
    original = instance.aDD_OP
    instance.aDD_OP = original
    assert instance.aDD_OP == original

@given(instance=myDsl::Expression1_strategy)
@settings(max_examples=50)
def test_mydsl::expression1_instantiation(instance):
    assert isinstance(instance, myDsl::Expression1)

@given(instance=myDsl::TypeAssertion_strategy)
@settings(max_examples=50)
def test_mydsl::typeassertion_instantiation(instance):
    assert isinstance(instance, myDsl::TypeAssertion)

@given(instance=myDsl::UnaryExpr_strategy)
@settings(max_examples=50)
def test_mydsl::unaryexpr_instantiation(instance):
    assert isinstance(instance, myDsl::UnaryExpr)

@given(instance=myDsl::ReceiverType_strategy)
@settings(max_examples=50)
def test_mydsl::receivertype_instantiation(instance):
    assert isinstance(instance, myDsl::ReceiverType)

@given(instance=myDsl::Arguments_strategy)
@settings(max_examples=50)
def test_mydsl::arguments_instantiation(instance):
    assert isinstance(instance, myDsl::Arguments)

@given(instance=myDsl::Slice_strategy)
@settings(max_examples=50)
def test_mydsl::slice_instantiation(instance):
    assert isinstance(instance, myDsl::Slice)

@given(instance=myDsl::Index_strategy)
@settings(max_examples=50)
def test_mydsl::index_instantiation(instance):
    assert isinstance(instance, myDsl::Index)

@given(instance=myDsl::Selector_strategy)
@settings(max_examples=50)
def test_mydsl::selector_instantiation(instance):
    assert isinstance(instance, myDsl::Selector)

@given(instance=myDsl::Selector_strategy)
def test_mydsl::selector_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::Selector_strategy)
def test_mydsl::selector_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::MethodExpr_strategy)
@settings(max_examples=50)
def test_mydsl::methodexpr_instantiation(instance):
    assert isinstance(instance, myDsl::MethodExpr)

@given(instance=myDsl::Conversion_strategy)
@settings(max_examples=50)
def test_mydsl::conversion_instantiation(instance):
    assert isinstance(instance, myDsl::Conversion)

@given(instance=myDsl::PrimaryExprLinha_strategy)
@settings(max_examples=50)
def test_mydsl::primaryexprlinha_instantiation(instance):
    assert isinstance(instance, myDsl::PrimaryExprLinha)

@given(instance=myDsl::PrimaryExpr_strategy)
@settings(max_examples=50)
def test_mydsl::primaryexpr_instantiation(instance):
    assert isinstance(instance, myDsl::PrimaryExpr)

@given(instance=myDsl::FieldName_strategy)
@settings(max_examples=50)
def test_mydsl::fieldname_instantiation(instance):
    assert isinstance(instance, myDsl::FieldName)

@given(instance=myDsl::FieldName_strategy)
def test_mydsl::fieldname_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::FieldName_strategy)
def test_mydsl::fieldname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::Element_strategy)
@settings(max_examples=50)
def test_mydsl::element_instantiation(instance):
    assert isinstance(instance, myDsl::Element)

@given(instance=myDsl::Key_strategy)
@settings(max_examples=50)
def test_mydsl::key_instantiation(instance):
    assert isinstance(instance, myDsl::Key)

@given(instance=myDsl::KeyedElement_strategy)
@settings(max_examples=50)
def test_mydsl::keyedelement_instantiation(instance):
    assert isinstance(instance, myDsl::KeyedElement)

@given(instance=myDsl::ElementList_strategy)
@settings(max_examples=50)
def test_mydsl::elementlist_instantiation(instance):
    assert isinstance(instance, myDsl::ElementList)

@given(instance=myDsl::LiteralTypeLinha_strategy)
@settings(max_examples=50)
def test_mydsl::literaltypelinha_instantiation(instance):
    assert isinstance(instance, myDsl::LiteralTypeLinha)

@given(instance=myDsl::LiteralValue_strategy)
@settings(max_examples=50)
def test_mydsl::literalvalue_instantiation(instance):
    assert isinstance(instance, myDsl::LiteralValue)

@given(instance=myDsl::LiteralType_strategy)
@settings(max_examples=50)
def test_mydsl::literaltype_instantiation(instance):
    assert isinstance(instance, myDsl::LiteralType)

@given(instance=myDsl::FunctionLit_strategy)
@settings(max_examples=50)
def test_mydsl::functionlit_instantiation(instance):
    assert isinstance(instance, myDsl::FunctionLit)

@given(instance=myDsl::FunctionLit_strategy)
def test_mydsl::functionlit_func_type(instance):
    assert isinstance(instance.func, str)


@given(instance=myDsl::FunctionLit_strategy)
def test_mydsl::functionlit_func_setter(instance):
    original = instance.func
    instance.func = original
    assert instance.func == original

@given(instance=myDsl::CompositeLit_strategy)
@settings(max_examples=50)
def test_mydsl::compositelit_instantiation(instance):
    assert isinstance(instance, myDsl::CompositeLit)

@given(instance=myDsl::BasicLit_strategy)
@settings(max_examples=50)
def test_mydsl::basiclit_instantiation(instance):
    assert isinstance(instance, myDsl::BasicLit)

@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_imaginary_lit_type(instance):
    assert isinstance(instance.imaginary_lit, str)


@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_imaginary_lit_setter(instance):
    original = instance.imaginary_lit
    instance.imaginary_lit = original
    assert instance.imaginary_lit == original

@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_float_lit_type(instance):
    assert isinstance(instance.float_lit, str)


@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_float_lit_setter(instance):
    original = instance.float_lit
    instance.float_lit = original
    assert instance.float_lit == original

@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_int_lit_type(instance):
    assert isinstance(instance.int_lit, str)


@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_int_lit_setter(instance):
    original = instance.int_lit
    instance.int_lit = original
    assert instance.int_lit == original

@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_string_lit_type(instance):
    assert isinstance(instance.string_lit, str)


@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_string_lit_setter(instance):
    original = instance.string_lit
    instance.string_lit = original
    assert instance.string_lit == original

@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_rune_lit_type(instance):
    assert isinstance(instance.rune_lit, str)


@given(instance=myDsl::BasicLit_strategy)
def test_mydsl::basiclit_rune_lit_setter(instance):
    original = instance.rune_lit
    instance.rune_lit = original
    assert instance.rune_lit == original

@given(instance=myDsl::OperandName_strategy)
@settings(max_examples=50)
def test_mydsl::operandname_instantiation(instance):
    assert isinstance(instance, myDsl::OperandName)

@given(instance=myDsl::OperandName_strategy)
def test_mydsl::operandname_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::OperandName_strategy)
def test_mydsl::operandname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::Literal_strategy)
@settings(max_examples=50)
def test_mydsl::literal_instantiation(instance):
    assert isinstance(instance, myDsl::Literal)

@given(instance=myDsl::Operand_strategy)
@settings(max_examples=50)
def test_mydsl::operand_instantiation(instance):
    assert isinstance(instance, myDsl::Operand)

@given(instance=myDsl::Receiver_strategy)
@settings(max_examples=50)
def test_mydsl::receiver_instantiation(instance):
    assert isinstance(instance, myDsl::Receiver)

@given(instance=myDsl::FunctionBody_strategy)
@settings(max_examples=50)
def test_mydsl::functionbody_instantiation(instance):
    assert isinstance(instance, myDsl::FunctionBody)

@given(instance=myDsl::FunctionName_strategy)
@settings(max_examples=50)
def test_mydsl::functionname_instantiation(instance):
    assert isinstance(instance, myDsl::FunctionName)

@given(instance=myDsl::FunctionName_strategy)
def test_mydsl::functionname_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::FunctionName_strategy)
def test_mydsl::functionname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::ShortVarDecl_strategy)
@settings(max_examples=50)
def test_mydsl::shortvardecl_instantiation(instance):
    assert isinstance(instance, myDsl::ShortVarDecl)

@given(instance=myDsl::ConstSpec_strategy)
@settings(max_examples=50)
def test_mydsl::constspec_instantiation(instance):
    assert isinstance(instance, myDsl::ConstSpec)

@given(instance=myDsl::VarSpec_strategy)
@settings(max_examples=50)
def test_mydsl::varspec_instantiation(instance):
    assert isinstance(instance, myDsl::VarSpec)

@given(instance=myDsl::TypeDef_strategy)
@settings(max_examples=50)
def test_mydsl::typedef_instantiation(instance):
    assert isinstance(instance, myDsl::TypeDef)

@given(instance=myDsl::TypeDef_strategy)
def test_mydsl::typedef_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::TypeDef_strategy)
def test_mydsl::typedef_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::AliasDecl_strategy)
@settings(max_examples=50)
def test_mydsl::aliasdecl_instantiation(instance):
    assert isinstance(instance, myDsl::AliasDecl)

@given(instance=myDsl::AliasDecl_strategy)
def test_mydsl::aliasdecl_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::AliasDecl_strategy)
def test_mydsl::aliasdecl_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::TypeSpec_strategy)
@settings(max_examples=50)
def test_mydsl::typespec_instantiation(instance):
    assert isinstance(instance, myDsl::TypeSpec)

@given(instance=myDsl::ExpressionList_strategy)
@settings(max_examples=50)
def test_mydsl::expressionlist_instantiation(instance):
    assert isinstance(instance, myDsl::ExpressionList)

@given(instance=myDsl::ChannelTypeLinha_strategy)
@settings(max_examples=50)
def test_mydsl::channeltypelinha_instantiation(instance):
    assert isinstance(instance, myDsl::ChannelTypeLinha)

@given(instance=myDsl::ChannelTypeLinha_strategy)
def test_mydsl::channeltypelinha_aNY_OTHER_type(instance):
    assert isinstance(instance.aNY_OTHER, str)


@given(instance=myDsl::ChannelTypeLinha_strategy)
def test_mydsl::channeltypelinha_aNY_OTHER_setter(instance):
    original = instance.aNY_OTHER
    instance.aNY_OTHER = original
    assert instance.aNY_OTHER == original

@given(instance=myDsl::MethodDecl_strategy)
@settings(max_examples=50)
def test_mydsl::methoddecl_instantiation(instance):
    assert isinstance(instance, myDsl::MethodDecl)

@given(instance=myDsl::FunctionDecl_strategy)
@settings(max_examples=50)
def test_mydsl::functiondecl_instantiation(instance):
    assert isinstance(instance, myDsl::FunctionDecl)

@given(instance=myDsl::TopLevelDecl_strategy)
@settings(max_examples=50)
def test_mydsl::topleveldecl_instantiation(instance):
    assert isinstance(instance, myDsl::TopLevelDecl)

@given(instance=myDsl::VarDecl_strategy)
@settings(max_examples=50)
def test_mydsl::vardecl_instantiation(instance):
    assert isinstance(instance, myDsl::VarDecl)

@given(instance=myDsl::VarDecl_strategy)
def test_mydsl::vardecl_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=myDsl::VarDecl_strategy)
def test_mydsl::vardecl_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=myDsl::TypeDecl_strategy)
@settings(max_examples=50)
def test_mydsl::typedecl_instantiation(instance):
    assert isinstance(instance, myDsl::TypeDecl)

@given(instance=myDsl::TypeDecl_strategy)
def test_mydsl::typedecl_typekeyword_type(instance):
    assert isinstance(instance.typekeyword, str)


@given(instance=myDsl::TypeDecl_strategy)
def test_mydsl::typedecl_typekeyword_setter(instance):
    original = instance.typekeyword
    instance.typekeyword = original
    assert instance.typekeyword == original

@given(instance=myDsl::ConstDecl_strategy)
@settings(max_examples=50)
def test_mydsl::constdecl_instantiation(instance):
    assert isinstance(instance, myDsl::ConstDecl)

@given(instance=myDsl::ConstDecl_strategy)
def test_mydsl::constdecl_const_type(instance):
    assert isinstance(instance.const, str)


@given(instance=myDsl::ConstDecl_strategy)
def test_mydsl::constdecl_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=myDsl::Declaration_strategy)
@settings(max_examples=50)
def test_mydsl::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::Declaration)

@given(instance=myDsl::Statement_strategy)
@settings(max_examples=50)
def test_mydsl::statement_instantiation(instance):
    assert isinstance(instance, myDsl::Statement)

@given(instance=myDsl::StatementList_strategy)
@settings(max_examples=50)
def test_mydsl::statementlist_instantiation(instance):
    assert isinstance(instance, myDsl::StatementList)

@given(instance=myDsl::Block_strategy)
@settings(max_examples=50)
def test_mydsl::block_instantiation(instance):
    assert isinstance(instance, myDsl::Block)

@given(instance=myDsl::Result_strategy)
@settings(max_examples=50)
def test_mydsl::result_instantiation(instance):
    assert isinstance(instance, myDsl::Result)

@given(instance=myDsl::KeyType_strategy)
@settings(max_examples=50)
def test_mydsl::keytype_instantiation(instance):
    assert isinstance(instance, myDsl::KeyType)

@given(instance=myDsl::InterfaceTypeName_strategy)
@settings(max_examples=50)
def test_mydsl::interfacetypename_instantiation(instance):
    assert isinstance(instance, myDsl::InterfaceTypeName)

@given(instance=myDsl::MethodName_strategy)
@settings(max_examples=50)
def test_mydsl::methodname_instantiation(instance):
    assert isinstance(instance, myDsl::MethodName)

@given(instance=myDsl::MethodName_strategy)
def test_mydsl::methodname_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::MethodName_strategy)
def test_mydsl::methodname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::MethodSpec_strategy)
@settings(max_examples=50)
def test_mydsl::methodspec_instantiation(instance):
    assert isinstance(instance, myDsl::MethodSpec)

@given(instance=myDsl::ParameterDecl_strategy)
@settings(max_examples=50)
def test_mydsl::parameterdecl_instantiation(instance):
    assert isinstance(instance, myDsl::ParameterDecl)

@given(instance=myDsl::ParameterList_strategy)
@settings(max_examples=50)
def test_mydsl::parameterlist_instantiation(instance):
    assert isinstance(instance, myDsl::ParameterList)

@given(instance=myDsl::ChannelType_strategy)
@settings(max_examples=50)
def test_mydsl::channeltype_instantiation(instance):
    assert isinstance(instance, myDsl::ChannelType)

@given(instance=myDsl::ChannelType_strategy)
def test_mydsl::channeltype_chan_type(instance):
    assert isinstance(instance.chan, str)


@given(instance=myDsl::ChannelType_strategy)
def test_mydsl::channeltype_chan_setter(instance):
    original = instance.chan
    instance.chan = original
    assert instance.chan == original

@given(instance=myDsl::Parameters_strategy)
@settings(max_examples=50)
def test_mydsl::parameters_instantiation(instance):
    assert isinstance(instance, myDsl::Parameters)

@given(instance=myDsl::Signature_strategy)
@settings(max_examples=50)
def test_mydsl::signature_instantiation(instance):
    assert isinstance(instance, myDsl::Signature)

@given(instance=myDsl::BaseType_strategy)
@settings(max_examples=50)
def test_mydsl::basetype_instantiation(instance):
    assert isinstance(instance, myDsl::BaseType)

@given(instance=myDsl::Tag_strategy)
@settings(max_examples=50)
def test_mydsl::tag_instantiation(instance):
    assert isinstance(instance, myDsl::Tag)

@given(instance=myDsl::Tag_strategy)
def test_mydsl::tag_string_lit_type(instance):
    assert isinstance(instance.string_lit, str)


@given(instance=myDsl::Tag_strategy)
def test_mydsl::tag_string_lit_setter(instance):
    original = instance.string_lit
    instance.string_lit = original
    assert instance.string_lit == original

@given(instance=myDsl::EmbeddedField_strategy)
@settings(max_examples=50)
def test_mydsl::embeddedfield_instantiation(instance):
    assert isinstance(instance, myDsl::EmbeddedField)

@given(instance=myDsl::IdentifierList_strategy)
@settings(max_examples=50)
def test_mydsl::identifierlist_instantiation(instance):
    assert isinstance(instance, myDsl::IdentifierList)

@given(instance=myDsl::IdentifierList_strategy)
def test_mydsl::identifierlist_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::IdentifierList_strategy)
def test_mydsl::identifierlist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::IdentifierList_strategy)
def test_mydsl::identifierlist_id1_type(instance):
    assert isinstance(instance.id1, str)


@given(instance=myDsl::IdentifierList_strategy)
def test_mydsl::identifierlist_id1_setter(instance):
    original = instance.id1
    instance.id1 = original
    assert instance.id1 == original

@given(instance=myDsl::FieldDecl_strategy)
@settings(max_examples=50)
def test_mydsl::fielddecl_instantiation(instance):
    assert isinstance(instance, myDsl::FieldDecl)

@given(instance=myDsl::Expression_strategy)
@settings(max_examples=50)
def test_mydsl::expression_instantiation(instance):
    assert isinstance(instance, myDsl::Expression)

@given(instance=myDsl::ElementType_strategy)
@settings(max_examples=50)
def test_mydsl::elementtype_instantiation(instance):
    assert isinstance(instance, myDsl::ElementType)

@given(instance=myDsl::ArrayLength_strategy)
@settings(max_examples=50)
def test_mydsl::arraylength_instantiation(instance):
    assert isinstance(instance, myDsl::ArrayLength)

@given(instance=myDsl::MapType_strategy)
@settings(max_examples=50)
def test_mydsl::maptype_instantiation(instance):
    assert isinstance(instance, myDsl::MapType)

@given(instance=myDsl::MapType_strategy)
def test_mydsl::maptype_map_type(instance):
    assert isinstance(instance.map, str)


@given(instance=myDsl::MapType_strategy)
def test_mydsl::maptype_map_setter(instance):
    original = instance.map
    instance.map = original
    assert instance.map == original

@given(instance=myDsl::InterfaceType_strategy)
@settings(max_examples=50)
def test_mydsl::interfacetype_instantiation(instance):
    assert isinstance(instance, myDsl::InterfaceType)

@given(instance=myDsl::InterfaceType_strategy)
def test_mydsl::interfacetype_interface_type(instance):
    assert isinstance(instance.interface, str)


@given(instance=myDsl::InterfaceType_strategy)
def test_mydsl::interfacetype_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

@given(instance=myDsl::FunctionType_strategy)
@settings(max_examples=50)
def test_mydsl::functiontype_instantiation(instance):
    assert isinstance(instance, myDsl::FunctionType)

@given(instance=myDsl::FunctionType_strategy)
def test_mydsl::functiontype_func_type(instance):
    assert isinstance(instance.func, str)


@given(instance=myDsl::FunctionType_strategy)
def test_mydsl::functiontype_func_setter(instance):
    original = instance.func
    instance.func = original
    assert instance.func == original

@given(instance=myDsl::PointerType_strategy)
@settings(max_examples=50)
def test_mydsl::pointertype_instantiation(instance):
    assert isinstance(instance, myDsl::PointerType)

@given(instance=myDsl::StructType_strategy)
@settings(max_examples=50)
def test_mydsl::structtype_instantiation(instance):
    assert isinstance(instance, myDsl::StructType)

@given(instance=myDsl::StructType_strategy)
def test_mydsl::structtype_struct_type(instance):
    assert isinstance(instance.struct, str)


@given(instance=myDsl::StructType_strategy)
def test_mydsl::structtype_struct_setter(instance):
    original = instance.struct
    instance.struct = original
    assert instance.struct == original

@given(instance=myDsl::TypeLitLinha_strategy)
@settings(max_examples=50)
def test_mydsl::typelitlinha_instantiation(instance):
    assert isinstance(instance, myDsl::TypeLitLinha)

@given(instance=myDsl::TypeNameLinha_strategy)
@settings(max_examples=50)
def test_mydsl::typenamelinha_instantiation(instance):
    assert isinstance(instance, myDsl::TypeNameLinha)

@given(instance=myDsl::TypeNameLinha_strategy)
def test_mydsl::typenamelinha_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::TypeNameLinha_strategy)
def test_mydsl::typenamelinha_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::TypeLit_strategy)
@settings(max_examples=50)
def test_mydsl::typelit_instantiation(instance):
    assert isinstance(instance, myDsl::TypeLit)

@given(instance=myDsl::TypeName_strategy)
@settings(max_examples=50)
def test_mydsl::typename_instantiation(instance):
    assert isinstance(instance, myDsl::TypeName)

@given(instance=myDsl::TypeName_strategy)
def test_mydsl::typename_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::TypeName_strategy)
def test_mydsl::typename_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::SourceFile_strategy)
@settings(max_examples=50)
def test_mydsl::sourcefile_instantiation(instance):
    assert isinstance(instance, myDsl::SourceFile)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
