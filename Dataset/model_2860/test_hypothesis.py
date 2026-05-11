import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    go::ImportPath,
    go::ImportSpec,
    go::imaginary::lit,
    go::exponent,
    go::RecvExpr,
    go::RecvStmt,
    go::CommCase,
    go::CommClause,
    go::InitStmt,
    go::PostStmt,
    go::TypeCaseClause,
    go::TypeSwitchGuard,
    go::ExprSwitchCase,
    go::ExprCaseClause,
    go::switch::stmt::linha,
    go::RangeClause,
    go::ForClause,
    go::Condition,
    go::TypeList,
    go::TypeSwitchCase,
    go::Channel,
    go::Label,
    go::Assignment,
    go::IncDecStmt,
    go::SendStmt,
    go::ExpressionStmt,
    go::GotoStmt,
    go::ContinueStmt,
    go::BreakStmt,
    go::ReturnStmt,
    go::GoStmt,
    go::SouceFile,
    go::LabeledStmt,
    SwitchStmt,
    go::SimpleStmt,
    go::DeferStmt,
    go::ForStmt,
    go::SelectStmt,
    go::SwitchStmt,
    go::IfStmt,
    go::ReceiverType,
    go::Slice,
    go::binary::op,
    go::ExpressionLinha,
    go::UnaryExpr,
    go::Arguments,
    go::MethodExpr,
    go::Conversion,
    go::PrimaryExprLinha,
    go::PrimaryExpr,
    go::FieldName,
    go::Index,
    go::TypeAssertion,
    go::Selector,
    go::cochetes,
    go::ponto,
    go::LiteralTypeLinha,
    go::LiteralValue,
    go::LiteralType,
    Literal,
    go::FunctionLit,
    go::CompositeLit,
    go::PackageName,
    OperandName,
    go::Key,
    go::Element,
    go::KeyedElement,
    go::ElementList,
    go::MethodDecl,
    go::FunctionDecl,
    go::ShortVarDecl,
    go::rune::lit,
    go::float::lit,
    go::BasicLit,
    go::OperandName,
    go::Literal,
    go::Operand,
    go::ExpressionList,
    go::ConstSpec,
    go::Receiver,
    go::FunctionBody,
    go::FunctionName,
    go::VarSpec,
    TypeSpec,
    go::TypeDef,
    go::AliasDecl,
    go::TypeSpec,
    go::KeyType,
    go::InterfaceTypeName,
    go::MethodName,
    go::MethodSpec,
    go::topLevelDeclLinha,
    go::VarDecl,
    go::TypeDecl,
    go::ConstDecl,
    go::Declaration,
    go::Statement,
    go::StatementList,
    go::Block,
    go::Result,
    go::Signature,
    go::string::lit,
    go::Tag,
    go::EmbeddedField,
    go::IdentifierList,
    go::FieldDecl,
    go::ParameterDecl,
    go::ParameterList,
    Receiver,
    go::Parameters,
    go::InterfaceType,
    go::FunctionType,
    go::PointerType,
    go::StructType,
    go::TypeLitLinha,
    go::QualifiedIdent,
    go::TypeNameLinha,
    go::identifier,
    go::TypeLit,
    go::Expression,
    go::ElementType,
    go::ArrayLength,
    go::ChannelType,
    go::MapType,
    go::TypeName,
    go::Type,
    go::TopLevelDecl,
    go::ImportDecl,
    go::PackageClause,
    float::lit,
    go::decimals,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_go::importpath_is_not_abstract():
    assert not inspect.isabstract(go::ImportPath)


def test_go::importpath_constructor_exists():
    assert callable(go::ImportPath.__init__)


def test_go::importpath_constructor_args():
    sig = inspect.signature(go::ImportPath.__init__)
    params = list(sig.parameters.keys())



def test_go::importspec_is_not_abstract():
    assert not inspect.isabstract(go::ImportSpec)


def test_go::importspec_constructor_exists():
    assert callable(go::ImportSpec.__init__)


def test_go::importspec_constructor_args():
    sig = inspect.signature(go::ImportSpec.__init__)
    params = list(sig.parameters.keys())



def test_go::imaginary::lit_is_not_abstract():
    assert not inspect.isabstract(go::imaginary::lit)


def test_go::imaginary::lit_constructor_exists():
    assert callable(go::imaginary::lit.__init__)


def test_go::imaginary::lit_constructor_args():
    sig = inspect.signature(go::imaginary::lit.__init__)
    params = list(sig.parameters.keys())



def test_go::exponent_is_not_abstract():
    assert not inspect.isabstract(go::exponent)


def test_go::exponent_constructor_exists():
    assert callable(go::exponent.__init__)


def test_go::exponent_constructor_args():
    sig = inspect.signature(go::exponent.__init__)
    params = list(sig.parameters.keys())



def test_go::recvexpr_is_not_abstract():
    assert not inspect.isabstract(go::RecvExpr)


def test_go::recvexpr_constructor_exists():
    assert callable(go::RecvExpr.__init__)


def test_go::recvexpr_constructor_args():
    sig = inspect.signature(go::RecvExpr.__init__)
    params = list(sig.parameters.keys())



def test_go::recvstmt_is_not_abstract():
    assert not inspect.isabstract(go::RecvStmt)


def test_go::recvstmt_constructor_exists():
    assert callable(go::RecvStmt.__init__)


def test_go::recvstmt_constructor_args():
    sig = inspect.signature(go::RecvStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::commcase_is_not_abstract():
    assert not inspect.isabstract(go::CommCase)


def test_go::commcase_constructor_exists():
    assert callable(go::CommCase.__init__)


def test_go::commcase_constructor_args():
    sig = inspect.signature(go::CommCase.__init__)
    params = list(sig.parameters.keys())



def test_go::commclause_is_not_abstract():
    assert not inspect.isabstract(go::CommClause)


def test_go::commclause_constructor_exists():
    assert callable(go::CommClause.__init__)


def test_go::commclause_constructor_args():
    sig = inspect.signature(go::CommClause.__init__)
    params = list(sig.parameters.keys())



def test_go::initstmt_is_not_abstract():
    assert not inspect.isabstract(go::InitStmt)


def test_go::initstmt_constructor_exists():
    assert callable(go::InitStmt.__init__)


def test_go::initstmt_constructor_args():
    sig = inspect.signature(go::InitStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::poststmt_is_not_abstract():
    assert not inspect.isabstract(go::PostStmt)


def test_go::poststmt_constructor_exists():
    assert callable(go::PostStmt.__init__)


def test_go::poststmt_constructor_args():
    sig = inspect.signature(go::PostStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::typecaseclause_is_not_abstract():
    assert not inspect.isabstract(go::TypeCaseClause)


def test_go::typecaseclause_constructor_exists():
    assert callable(go::TypeCaseClause.__init__)


def test_go::typecaseclause_constructor_args():
    sig = inspect.signature(go::TypeCaseClause.__init__)
    params = list(sig.parameters.keys())



def test_go::typeswitchguard_is_not_abstract():
    assert not inspect.isabstract(go::TypeSwitchGuard)


def test_go::typeswitchguard_constructor_exists():
    assert callable(go::TypeSwitchGuard.__init__)


def test_go::typeswitchguard_constructor_args():
    sig = inspect.signature(go::TypeSwitchGuard.__init__)
    params = list(sig.parameters.keys())



def test_go::exprswitchcase_is_not_abstract():
    assert not inspect.isabstract(go::ExprSwitchCase)


def test_go::exprswitchcase_constructor_exists():
    assert callable(go::ExprSwitchCase.__init__)


def test_go::exprswitchcase_constructor_args():
    sig = inspect.signature(go::ExprSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_go::exprcaseclause_is_not_abstract():
    assert not inspect.isabstract(go::ExprCaseClause)


def test_go::exprcaseclause_constructor_exists():
    assert callable(go::ExprCaseClause.__init__)


def test_go::exprcaseclause_constructor_args():
    sig = inspect.signature(go::ExprCaseClause.__init__)
    params = list(sig.parameters.keys())



def test_go::switch::stmt::linha_is_not_abstract():
    assert not inspect.isabstract(go::switch::stmt::linha)


def test_go::switch::stmt::linha_constructor_exists():
    assert callable(go::switch::stmt::linha.__init__)


def test_go::switch::stmt::linha_constructor_args():
    sig = inspect.signature(go::switch::stmt::linha.__init__)
    params = list(sig.parameters.keys())



def test_go::rangeclause_is_not_abstract():
    assert not inspect.isabstract(go::RangeClause)


def test_go::rangeclause_constructor_exists():
    assert callable(go::RangeClause.__init__)


def test_go::rangeclause_constructor_args():
    sig = inspect.signature(go::RangeClause.__init__)
    params = list(sig.parameters.keys())



def test_go::forclause_is_not_abstract():
    assert not inspect.isabstract(go::ForClause)


def test_go::forclause_constructor_exists():
    assert callable(go::ForClause.__init__)


def test_go::forclause_constructor_args():
    sig = inspect.signature(go::ForClause.__init__)
    params = list(sig.parameters.keys())



def test_go::condition_is_not_abstract():
    assert not inspect.isabstract(go::Condition)


def test_go::condition_constructor_exists():
    assert callable(go::Condition.__init__)


def test_go::condition_constructor_args():
    sig = inspect.signature(go::Condition.__init__)
    params = list(sig.parameters.keys())



def test_go::typelist_is_not_abstract():
    assert not inspect.isabstract(go::TypeList)


def test_go::typelist_constructor_exists():
    assert callable(go::TypeList.__init__)


def test_go::typelist_constructor_args():
    sig = inspect.signature(go::TypeList.__init__)
    params = list(sig.parameters.keys())



def test_go::typeswitchcase_is_not_abstract():
    assert not inspect.isabstract(go::TypeSwitchCase)


def test_go::typeswitchcase_constructor_exists():
    assert callable(go::TypeSwitchCase.__init__)


def test_go::typeswitchcase_constructor_args():
    sig = inspect.signature(go::TypeSwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_go::channel_is_not_abstract():
    assert not inspect.isabstract(go::Channel)


def test_go::channel_constructor_exists():
    assert callable(go::Channel.__init__)


def test_go::channel_constructor_args():
    sig = inspect.signature(go::Channel.__init__)
    params = list(sig.parameters.keys())



def test_go::label_is_not_abstract():
    assert not inspect.isabstract(go::Label)


def test_go::label_constructor_exists():
    assert callable(go::Label.__init__)


def test_go::label_constructor_args():
    sig = inspect.signature(go::Label.__init__)
    params = list(sig.parameters.keys())



def test_go::assignment_is_not_abstract():
    assert not inspect.isabstract(go::Assignment)


def test_go::assignment_constructor_exists():
    assert callable(go::Assignment.__init__)


def test_go::assignment_constructor_args():
    sig = inspect.signature(go::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "assign_op" in params, "Missing parameter 'assign_op'"

def test_go::assignment_has_assign_op():
    assert hasattr(go::Assignment, "assign_op")
    descriptor = None
    for klass in go::Assignment.__mro__:
        if "assign_op" in klass.__dict__:
            descriptor = klass.__dict__["assign_op"]
            break
    assert isinstance(descriptor, property)



def test_go::incdecstmt_is_not_abstract():
    assert not inspect.isabstract(go::IncDecStmt)


def test_go::incdecstmt_constructor_exists():
    assert callable(go::IncDecStmt.__init__)


def test_go::incdecstmt_constructor_args():
    sig = inspect.signature(go::IncDecStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::sendstmt_is_not_abstract():
    assert not inspect.isabstract(go::SendStmt)


def test_go::sendstmt_constructor_exists():
    assert callable(go::SendStmt.__init__)


def test_go::sendstmt_constructor_args():
    sig = inspect.signature(go::SendStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::expressionstmt_is_not_abstract():
    assert not inspect.isabstract(go::ExpressionStmt)


def test_go::expressionstmt_constructor_exists():
    assert callable(go::ExpressionStmt.__init__)


def test_go::expressionstmt_constructor_args():
    sig = inspect.signature(go::ExpressionStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::gotostmt_is_not_abstract():
    assert not inspect.isabstract(go::GotoStmt)


def test_go::gotostmt_constructor_exists():
    assert callable(go::GotoStmt.__init__)


def test_go::gotostmt_constructor_args():
    sig = inspect.signature(go::GotoStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::continuestmt_is_not_abstract():
    assert not inspect.isabstract(go::ContinueStmt)


def test_go::continuestmt_constructor_exists():
    assert callable(go::ContinueStmt.__init__)


def test_go::continuestmt_constructor_args():
    sig = inspect.signature(go::ContinueStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::breakstmt_is_not_abstract():
    assert not inspect.isabstract(go::BreakStmt)


def test_go::breakstmt_constructor_exists():
    assert callable(go::BreakStmt.__init__)


def test_go::breakstmt_constructor_args():
    sig = inspect.signature(go::BreakStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::returnstmt_is_not_abstract():
    assert not inspect.isabstract(go::ReturnStmt)


def test_go::returnstmt_constructor_exists():
    assert callable(go::ReturnStmt.__init__)


def test_go::returnstmt_constructor_args():
    sig = inspect.signature(go::ReturnStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::gostmt_is_not_abstract():
    assert not inspect.isabstract(go::GoStmt)


def test_go::gostmt_constructor_exists():
    assert callable(go::GoStmt.__init__)


def test_go::gostmt_constructor_args():
    sig = inspect.signature(go::GoStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::soucefile_is_not_abstract():
    assert not inspect.isabstract(go::SouceFile)


def test_go::soucefile_constructor_exists():
    assert callable(go::SouceFile.__init__)


def test_go::soucefile_constructor_args():
    sig = inspect.signature(go::SouceFile.__init__)
    params = list(sig.parameters.keys())



def test_go::labeledstmt_is_not_abstract():
    assert not inspect.isabstract(go::LabeledStmt)


def test_go::labeledstmt_constructor_exists():
    assert callable(go::LabeledStmt.__init__)


def test_go::labeledstmt_constructor_args():
    sig = inspect.signature(go::LabeledStmt.__init__)
    params = list(sig.parameters.keys())



def test_switchstmt_is_not_abstract():
    assert not inspect.isabstract(SwitchStmt)


def test_switchstmt_constructor_exists():
    assert callable(SwitchStmt.__init__)


def test_switchstmt_constructor_args():
    sig = inspect.signature(SwitchStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::simplestmt_is_not_abstract():
    assert not inspect.isabstract(go::SimpleStmt)


def test_go::simplestmt_constructor_exists():
    assert callable(go::SimpleStmt.__init__)


def test_go::simplestmt_constructor_args():
    sig = inspect.signature(go::SimpleStmt.__init__)
    params = list(sig.parameters.keys())
    assert "EmptyStmt" in params, "Missing parameter 'EmptyStmt'"

def test_go::simplestmt_has_EmptyStmt():
    assert hasattr(go::SimpleStmt, "EmptyStmt")
    descriptor = None
    for klass in go::SimpleStmt.__mro__:
        if "EmptyStmt" in klass.__dict__:
            descriptor = klass.__dict__["EmptyStmt"]
            break
    assert isinstance(descriptor, property)



def test_go::deferstmt_is_not_abstract():
    assert not inspect.isabstract(go::DeferStmt)


def test_go::deferstmt_constructor_exists():
    assert callable(go::DeferStmt.__init__)


def test_go::deferstmt_constructor_args():
    sig = inspect.signature(go::DeferStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::forstmt_is_not_abstract():
    assert not inspect.isabstract(go::ForStmt)


def test_go::forstmt_constructor_exists():
    assert callable(go::ForStmt.__init__)


def test_go::forstmt_constructor_args():
    sig = inspect.signature(go::ForStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::selectstmt_is_not_abstract():
    assert not inspect.isabstract(go::SelectStmt)


def test_go::selectstmt_constructor_exists():
    assert callable(go::SelectStmt.__init__)


def test_go::selectstmt_constructor_args():
    sig = inspect.signature(go::SelectStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::switchstmt_is_not_abstract():
    assert not inspect.isabstract(go::SwitchStmt)


def test_go::switchstmt_constructor_exists():
    assert callable(go::SwitchStmt.__init__)


def test_go::switchstmt_constructor_args():
    sig = inspect.signature(go::SwitchStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::ifstmt_is_not_abstract():
    assert not inspect.isabstract(go::IfStmt)


def test_go::ifstmt_constructor_exists():
    assert callable(go::IfStmt.__init__)


def test_go::ifstmt_constructor_args():
    sig = inspect.signature(go::IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::receivertype_is_not_abstract():
    assert not inspect.isabstract(go::ReceiverType)


def test_go::receivertype_constructor_exists():
    assert callable(go::ReceiverType.__init__)


def test_go::receivertype_constructor_args():
    sig = inspect.signature(go::ReceiverType.__init__)
    params = list(sig.parameters.keys())



def test_go::slice_is_not_abstract():
    assert not inspect.isabstract(go::Slice)


def test_go::slice_constructor_exists():
    assert callable(go::Slice.__init__)


def test_go::slice_constructor_args():
    sig = inspect.signature(go::Slice.__init__)
    params = list(sig.parameters.keys())



def test_go::binary::op_is_not_abstract():
    assert not inspect.isabstract(go::binary::op)


def test_go::binary::op_constructor_exists():
    assert callable(go::binary::op.__init__)


def test_go::binary::op_constructor_args():
    sig = inspect.signature(go::binary::op.__init__)
    params = list(sig.parameters.keys())
    assert "mul_op" in params, "Missing parameter 'mul_op'"
    assert "add_op" in params, "Missing parameter 'add_op'"
    assert "rel_op" in params, "Missing parameter 'rel_op'"

def test_go::binary::op_has_mul_op():
    assert hasattr(go::binary::op, "mul_op")
    descriptor = None
    for klass in go::binary::op.__mro__:
        if "mul_op" in klass.__dict__:
            descriptor = klass.__dict__["mul_op"]
            break
    assert isinstance(descriptor, property)

def test_go::binary::op_has_add_op():
    assert hasattr(go::binary::op, "add_op")
    descriptor = None
    for klass in go::binary::op.__mro__:
        if "add_op" in klass.__dict__:
            descriptor = klass.__dict__["add_op"]
            break
    assert isinstance(descriptor, property)

def test_go::binary::op_has_rel_op():
    assert hasattr(go::binary::op, "rel_op")
    descriptor = None
    for klass in go::binary::op.__mro__:
        if "rel_op" in klass.__dict__:
            descriptor = klass.__dict__["rel_op"]
            break
    assert isinstance(descriptor, property)



def test_go::expressionlinha_is_not_abstract():
    assert not inspect.isabstract(go::ExpressionLinha)


def test_go::expressionlinha_constructor_exists():
    assert callable(go::ExpressionLinha.__init__)


def test_go::expressionlinha_constructor_args():
    sig = inspect.signature(go::ExpressionLinha.__init__)
    params = list(sig.parameters.keys())



def test_go::unaryexpr_is_not_abstract():
    assert not inspect.isabstract(go::UnaryExpr)


def test_go::unaryexpr_constructor_exists():
    assert callable(go::UnaryExpr.__init__)


def test_go::unaryexpr_constructor_args():
    sig = inspect.signature(go::UnaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "unary_op" in params, "Missing parameter 'unary_op'"

def test_go::unaryexpr_has_unary_op():
    assert hasattr(go::UnaryExpr, "unary_op")
    descriptor = None
    for klass in go::UnaryExpr.__mro__:
        if "unary_op" in klass.__dict__:
            descriptor = klass.__dict__["unary_op"]
            break
    assert isinstance(descriptor, property)



def test_go::arguments_is_not_abstract():
    assert not inspect.isabstract(go::Arguments)


def test_go::arguments_constructor_exists():
    assert callable(go::Arguments.__init__)


def test_go::arguments_constructor_args():
    sig = inspect.signature(go::Arguments.__init__)
    params = list(sig.parameters.keys())



def test_go::methodexpr_is_not_abstract():
    assert not inspect.isabstract(go::MethodExpr)


def test_go::methodexpr_constructor_exists():
    assert callable(go::MethodExpr.__init__)


def test_go::methodexpr_constructor_args():
    sig = inspect.signature(go::MethodExpr.__init__)
    params = list(sig.parameters.keys())



def test_go::conversion_is_not_abstract():
    assert not inspect.isabstract(go::Conversion)


def test_go::conversion_constructor_exists():
    assert callable(go::Conversion.__init__)


def test_go::conversion_constructor_args():
    sig = inspect.signature(go::Conversion.__init__)
    params = list(sig.parameters.keys())



def test_go::primaryexprlinha_is_not_abstract():
    assert not inspect.isabstract(go::PrimaryExprLinha)


def test_go::primaryexprlinha_constructor_exists():
    assert callable(go::PrimaryExprLinha.__init__)


def test_go::primaryexprlinha_constructor_args():
    sig = inspect.signature(go::PrimaryExprLinha.__init__)
    params = list(sig.parameters.keys())



def test_go::primaryexpr_is_not_abstract():
    assert not inspect.isabstract(go::PrimaryExpr)


def test_go::primaryexpr_constructor_exists():
    assert callable(go::PrimaryExpr.__init__)


def test_go::primaryexpr_constructor_args():
    sig = inspect.signature(go::PrimaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_go::fieldname_is_not_abstract():
    assert not inspect.isabstract(go::FieldName)


def test_go::fieldname_constructor_exists():
    assert callable(go::FieldName.__init__)


def test_go::fieldname_constructor_args():
    sig = inspect.signature(go::FieldName.__init__)
    params = list(sig.parameters.keys())



def test_go::index_is_not_abstract():
    assert not inspect.isabstract(go::Index)


def test_go::index_constructor_exists():
    assert callable(go::Index.__init__)


def test_go::index_constructor_args():
    sig = inspect.signature(go::Index.__init__)
    params = list(sig.parameters.keys())



def test_go::typeassertion_is_not_abstract():
    assert not inspect.isabstract(go::TypeAssertion)


def test_go::typeassertion_constructor_exists():
    assert callable(go::TypeAssertion.__init__)


def test_go::typeassertion_constructor_args():
    sig = inspect.signature(go::TypeAssertion.__init__)
    params = list(sig.parameters.keys())



def test_go::selector_is_not_abstract():
    assert not inspect.isabstract(go::Selector)


def test_go::selector_constructor_exists():
    assert callable(go::Selector.__init__)


def test_go::selector_constructor_args():
    sig = inspect.signature(go::Selector.__init__)
    params = list(sig.parameters.keys())



def test_go::cochetes_is_not_abstract():
    assert not inspect.isabstract(go::cochetes)


def test_go::cochetes_constructor_exists():
    assert callable(go::cochetes.__init__)


def test_go::cochetes_constructor_args():
    sig = inspect.signature(go::cochetes.__init__)
    params = list(sig.parameters.keys())



def test_go::ponto_is_not_abstract():
    assert not inspect.isabstract(go::ponto)


def test_go::ponto_constructor_exists():
    assert callable(go::ponto.__init__)


def test_go::ponto_constructor_args():
    sig = inspect.signature(go::ponto.__init__)
    params = list(sig.parameters.keys())



def test_go::literaltypelinha_is_not_abstract():
    assert not inspect.isabstract(go::LiteralTypeLinha)


def test_go::literaltypelinha_constructor_exists():
    assert callable(go::LiteralTypeLinha.__init__)


def test_go::literaltypelinha_constructor_args():
    sig = inspect.signature(go::LiteralTypeLinha.__init__)
    params = list(sig.parameters.keys())



def test_go::literalvalue_is_not_abstract():
    assert not inspect.isabstract(go::LiteralValue)


def test_go::literalvalue_constructor_exists():
    assert callable(go::LiteralValue.__init__)


def test_go::literalvalue_constructor_args():
    sig = inspect.signature(go::LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_go::literaltype_is_not_abstract():
    assert not inspect.isabstract(go::LiteralType)


def test_go::literaltype_constructor_exists():
    assert callable(go::LiteralType.__init__)


def test_go::literaltype_constructor_args():
    sig = inspect.signature(go::LiteralType.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_go::functionlit_is_not_abstract():
    assert not inspect.isabstract(go::FunctionLit)


def test_go::functionlit_constructor_exists():
    assert callable(go::FunctionLit.__init__)


def test_go::functionlit_constructor_args():
    sig = inspect.signature(go::FunctionLit.__init__)
    params = list(sig.parameters.keys())



def test_go::compositelit_is_not_abstract():
    assert not inspect.isabstract(go::CompositeLit)


def test_go::compositelit_constructor_exists():
    assert callable(go::CompositeLit.__init__)


def test_go::compositelit_constructor_args():
    sig = inspect.signature(go::CompositeLit.__init__)
    params = list(sig.parameters.keys())



def test_go::packagename_is_not_abstract():
    assert not inspect.isabstract(go::PackageName)


def test_go::packagename_constructor_exists():
    assert callable(go::PackageName.__init__)


def test_go::packagename_constructor_args():
    sig = inspect.signature(go::PackageName.__init__)
    params = list(sig.parameters.keys())



def test_operandname_is_not_abstract():
    assert not inspect.isabstract(OperandName)


def test_operandname_constructor_exists():
    assert callable(OperandName.__init__)


def test_operandname_constructor_args():
    sig = inspect.signature(OperandName.__init__)
    params = list(sig.parameters.keys())



def test_go::key_is_not_abstract():
    assert not inspect.isabstract(go::Key)


def test_go::key_constructor_exists():
    assert callable(go::Key.__init__)


def test_go::key_constructor_args():
    sig = inspect.signature(go::Key.__init__)
    params = list(sig.parameters.keys())



def test_go::element_is_not_abstract():
    assert not inspect.isabstract(go::Element)


def test_go::element_constructor_exists():
    assert callable(go::Element.__init__)


def test_go::element_constructor_args():
    sig = inspect.signature(go::Element.__init__)
    params = list(sig.parameters.keys())



def test_go::keyedelement_is_not_abstract():
    assert not inspect.isabstract(go::KeyedElement)


def test_go::keyedelement_constructor_exists():
    assert callable(go::KeyedElement.__init__)


def test_go::keyedelement_constructor_args():
    sig = inspect.signature(go::KeyedElement.__init__)
    params = list(sig.parameters.keys())



def test_go::elementlist_is_not_abstract():
    assert not inspect.isabstract(go::ElementList)


def test_go::elementlist_constructor_exists():
    assert callable(go::ElementList.__init__)


def test_go::elementlist_constructor_args():
    sig = inspect.signature(go::ElementList.__init__)
    params = list(sig.parameters.keys())



def test_go::methoddecl_is_not_abstract():
    assert not inspect.isabstract(go::MethodDecl)


def test_go::methoddecl_constructor_exists():
    assert callable(go::MethodDecl.__init__)


def test_go::methoddecl_constructor_args():
    sig = inspect.signature(go::MethodDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::functiondecl_is_not_abstract():
    assert not inspect.isabstract(go::FunctionDecl)


def test_go::functiondecl_constructor_exists():
    assert callable(go::FunctionDecl.__init__)


def test_go::functiondecl_constructor_args():
    sig = inspect.signature(go::FunctionDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::shortvardecl_is_not_abstract():
    assert not inspect.isabstract(go::ShortVarDecl)


def test_go::shortvardecl_constructor_exists():
    assert callable(go::ShortVarDecl.__init__)


def test_go::shortvardecl_constructor_args():
    sig = inspect.signature(go::ShortVarDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::rune::lit_is_not_abstract():
    assert not inspect.isabstract(go::rune::lit)


def test_go::rune::lit_constructor_exists():
    assert callable(go::rune::lit.__init__)


def test_go::rune::lit_constructor_args():
    sig = inspect.signature(go::rune::lit.__init__)
    params = list(sig.parameters.keys())
    assert "byte_value" in params, "Missing parameter 'byte_value'"
    assert "unicode_value" in params, "Missing parameter 'unicode_value'"

def test_go::rune::lit_has_byte_value():
    assert hasattr(go::rune::lit, "byte_value")
    descriptor = None
    for klass in go::rune::lit.__mro__:
        if "byte_value" in klass.__dict__:
            descriptor = klass.__dict__["byte_value"]
            break
    assert isinstance(descriptor, property)

def test_go::rune::lit_has_unicode_value():
    assert hasattr(go::rune::lit, "unicode_value")
    descriptor = None
    for klass in go::rune::lit.__mro__:
        if "unicode_value" in klass.__dict__:
            descriptor = klass.__dict__["unicode_value"]
            break
    assert isinstance(descriptor, property)



def test_go::float::lit_is_not_abstract():
    assert not inspect.isabstract(go::float::lit)


def test_go::float::lit_constructor_exists():
    assert callable(go::float::lit.__init__)


def test_go::float::lit_constructor_args():
    sig = inspect.signature(go::float::lit.__init__)
    params = list(sig.parameters.keys())



def test_go::basiclit_is_not_abstract():
    assert not inspect.isabstract(go::BasicLit)


def test_go::basiclit_constructor_exists():
    assert callable(go::BasicLit.__init__)


def test_go::basiclit_constructor_args():
    sig = inspect.signature(go::BasicLit.__init__)
    params = list(sig.parameters.keys())
    assert "int_lit" in params, "Missing parameter 'int_lit'"

def test_go::basiclit_has_int_lit():
    assert hasattr(go::BasicLit, "int_lit")
    descriptor = None
    for klass in go::BasicLit.__mro__:
        if "int_lit" in klass.__dict__:
            descriptor = klass.__dict__["int_lit"]
            break
    assert isinstance(descriptor, property)



def test_go::operandname_is_not_abstract():
    assert not inspect.isabstract(go::OperandName)


def test_go::operandname_constructor_exists():
    assert callable(go::OperandName.__init__)


def test_go::operandname_constructor_args():
    sig = inspect.signature(go::OperandName.__init__)
    params = list(sig.parameters.keys())



def test_go::literal_is_not_abstract():
    assert not inspect.isabstract(go::Literal)


def test_go::literal_constructor_exists():
    assert callable(go::Literal.__init__)


def test_go::literal_constructor_args():
    sig = inspect.signature(go::Literal.__init__)
    params = list(sig.parameters.keys())



def test_go::operand_is_not_abstract():
    assert not inspect.isabstract(go::Operand)


def test_go::operand_constructor_exists():
    assert callable(go::Operand.__init__)


def test_go::operand_constructor_args():
    sig = inspect.signature(go::Operand.__init__)
    params = list(sig.parameters.keys())



def test_go::expressionlist_is_not_abstract():
    assert not inspect.isabstract(go::ExpressionList)


def test_go::expressionlist_constructor_exists():
    assert callable(go::ExpressionList.__init__)


def test_go::expressionlist_constructor_args():
    sig = inspect.signature(go::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_go::constspec_is_not_abstract():
    assert not inspect.isabstract(go::ConstSpec)


def test_go::constspec_constructor_exists():
    assert callable(go::ConstSpec.__init__)


def test_go::constspec_constructor_args():
    sig = inspect.signature(go::ConstSpec.__init__)
    params = list(sig.parameters.keys())



def test_go::receiver_is_not_abstract():
    assert not inspect.isabstract(go::Receiver)


def test_go::receiver_constructor_exists():
    assert callable(go::Receiver.__init__)


def test_go::receiver_constructor_args():
    sig = inspect.signature(go::Receiver.__init__)
    params = list(sig.parameters.keys())



def test_go::functionbody_is_not_abstract():
    assert not inspect.isabstract(go::FunctionBody)


def test_go::functionbody_constructor_exists():
    assert callable(go::FunctionBody.__init__)


def test_go::functionbody_constructor_args():
    sig = inspect.signature(go::FunctionBody.__init__)
    params = list(sig.parameters.keys())



def test_go::functionname_is_not_abstract():
    assert not inspect.isabstract(go::FunctionName)


def test_go::functionname_constructor_exists():
    assert callable(go::FunctionName.__init__)


def test_go::functionname_constructor_args():
    sig = inspect.signature(go::FunctionName.__init__)
    params = list(sig.parameters.keys())



def test_go::varspec_is_not_abstract():
    assert not inspect.isabstract(go::VarSpec)


def test_go::varspec_constructor_exists():
    assert callable(go::VarSpec.__init__)


def test_go::varspec_constructor_args():
    sig = inspect.signature(go::VarSpec.__init__)
    params = list(sig.parameters.keys())



def test_typespec_is_not_abstract():
    assert not inspect.isabstract(TypeSpec)


def test_typespec_constructor_exists():
    assert callable(TypeSpec.__init__)


def test_typespec_constructor_args():
    sig = inspect.signature(TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_go::typedef_is_not_abstract():
    assert not inspect.isabstract(go::TypeDef)


def test_go::typedef_constructor_exists():
    assert callable(go::TypeDef.__init__)


def test_go::typedef_constructor_args():
    sig = inspect.signature(go::TypeDef.__init__)
    params = list(sig.parameters.keys())



def test_go::aliasdecl_is_not_abstract():
    assert not inspect.isabstract(go::AliasDecl)


def test_go::aliasdecl_constructor_exists():
    assert callable(go::AliasDecl.__init__)


def test_go::aliasdecl_constructor_args():
    sig = inspect.signature(go::AliasDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::typespec_is_not_abstract():
    assert not inspect.isabstract(go::TypeSpec)


def test_go::typespec_constructor_exists():
    assert callable(go::TypeSpec.__init__)


def test_go::typespec_constructor_args():
    sig = inspect.signature(go::TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_go::keytype_is_not_abstract():
    assert not inspect.isabstract(go::KeyType)


def test_go::keytype_constructor_exists():
    assert callable(go::KeyType.__init__)


def test_go::keytype_constructor_args():
    sig = inspect.signature(go::KeyType.__init__)
    params = list(sig.parameters.keys())



def test_go::interfacetypename_is_not_abstract():
    assert not inspect.isabstract(go::InterfaceTypeName)


def test_go::interfacetypename_constructor_exists():
    assert callable(go::InterfaceTypeName.__init__)


def test_go::interfacetypename_constructor_args():
    sig = inspect.signature(go::InterfaceTypeName.__init__)
    params = list(sig.parameters.keys())



def test_go::methodname_is_not_abstract():
    assert not inspect.isabstract(go::MethodName)


def test_go::methodname_constructor_exists():
    assert callable(go::MethodName.__init__)


def test_go::methodname_constructor_args():
    sig = inspect.signature(go::MethodName.__init__)
    params = list(sig.parameters.keys())



def test_go::methodspec_is_not_abstract():
    assert not inspect.isabstract(go::MethodSpec)


def test_go::methodspec_constructor_exists():
    assert callable(go::MethodSpec.__init__)


def test_go::methodspec_constructor_args():
    sig = inspect.signature(go::MethodSpec.__init__)
    params = list(sig.parameters.keys())



def test_go::topleveldecllinha_is_not_abstract():
    assert not inspect.isabstract(go::topLevelDeclLinha)


def test_go::topleveldecllinha_constructor_exists():
    assert callable(go::topLevelDeclLinha.__init__)


def test_go::topleveldecllinha_constructor_args():
    sig = inspect.signature(go::topLevelDeclLinha.__init__)
    params = list(sig.parameters.keys())



def test_go::vardecl_is_not_abstract():
    assert not inspect.isabstract(go::VarDecl)


def test_go::vardecl_constructor_exists():
    assert callable(go::VarDecl.__init__)


def test_go::vardecl_constructor_args():
    sig = inspect.signature(go::VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::typedecl_is_not_abstract():
    assert not inspect.isabstract(go::TypeDecl)


def test_go::typedecl_constructor_exists():
    assert callable(go::TypeDecl.__init__)


def test_go::typedecl_constructor_args():
    sig = inspect.signature(go::TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::constdecl_is_not_abstract():
    assert not inspect.isabstract(go::ConstDecl)


def test_go::constdecl_constructor_exists():
    assert callable(go::ConstDecl.__init__)


def test_go::constdecl_constructor_args():
    sig = inspect.signature(go::ConstDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::declaration_is_not_abstract():
    assert not inspect.isabstract(go::Declaration)


def test_go::declaration_constructor_exists():
    assert callable(go::Declaration.__init__)


def test_go::declaration_constructor_args():
    sig = inspect.signature(go::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_go::statement_is_not_abstract():
    assert not inspect.isabstract(go::Statement)


def test_go::statement_constructor_exists():
    assert callable(go::Statement.__init__)


def test_go::statement_constructor_args():
    sig = inspect.signature(go::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "FallthroughStmt" in params, "Missing parameter 'FallthroughStmt'"

def test_go::statement_has_FallthroughStmt():
    assert hasattr(go::Statement, "FallthroughStmt")
    descriptor = None
    for klass in go::Statement.__mro__:
        if "FallthroughStmt" in klass.__dict__:
            descriptor = klass.__dict__["FallthroughStmt"]
            break
    assert isinstance(descriptor, property)



def test_go::statementlist_is_not_abstract():
    assert not inspect.isabstract(go::StatementList)


def test_go::statementlist_constructor_exists():
    assert callable(go::StatementList.__init__)


def test_go::statementlist_constructor_args():
    sig = inspect.signature(go::StatementList.__init__)
    params = list(sig.parameters.keys())



def test_go::block_is_not_abstract():
    assert not inspect.isabstract(go::Block)


def test_go::block_constructor_exists():
    assert callable(go::Block.__init__)


def test_go::block_constructor_args():
    sig = inspect.signature(go::Block.__init__)
    params = list(sig.parameters.keys())



def test_go::result_is_not_abstract():
    assert not inspect.isabstract(go::Result)


def test_go::result_constructor_exists():
    assert callable(go::Result.__init__)


def test_go::result_constructor_args():
    sig = inspect.signature(go::Result.__init__)
    params = list(sig.parameters.keys())



def test_go::signature_is_not_abstract():
    assert not inspect.isabstract(go::Signature)


def test_go::signature_constructor_exists():
    assert callable(go::Signature.__init__)


def test_go::signature_constructor_args():
    sig = inspect.signature(go::Signature.__init__)
    params = list(sig.parameters.keys())



def test_go::string::lit_is_not_abstract():
    assert not inspect.isabstract(go::string::lit)


def test_go::string::lit_constructor_exists():
    assert callable(go::string::lit.__init__)


def test_go::string::lit_constructor_args():
    sig = inspect.signature(go::string::lit.__init__)
    params = list(sig.parameters.keys())
    assert "interpreted_string_lit" in params, "Missing parameter 'interpreted_string_lit'"
    assert "raw_string_lit" in params, "Missing parameter 'raw_string_lit'"

def test_go::string::lit_has_interpreted_string_lit():
    assert hasattr(go::string::lit, "interpreted_string_lit")
    descriptor = None
    for klass in go::string::lit.__mro__:
        if "interpreted_string_lit" in klass.__dict__:
            descriptor = klass.__dict__["interpreted_string_lit"]
            break
    assert isinstance(descriptor, property)

def test_go::string::lit_has_raw_string_lit():
    assert hasattr(go::string::lit, "raw_string_lit")
    descriptor = None
    for klass in go::string::lit.__mro__:
        if "raw_string_lit" in klass.__dict__:
            descriptor = klass.__dict__["raw_string_lit"]
            break
    assert isinstance(descriptor, property)



def test_go::tag_is_not_abstract():
    assert not inspect.isabstract(go::Tag)


def test_go::tag_constructor_exists():
    assert callable(go::Tag.__init__)


def test_go::tag_constructor_args():
    sig = inspect.signature(go::Tag.__init__)
    params = list(sig.parameters.keys())



def test_go::embeddedfield_is_not_abstract():
    assert not inspect.isabstract(go::EmbeddedField)


def test_go::embeddedfield_constructor_exists():
    assert callable(go::EmbeddedField.__init__)


def test_go::embeddedfield_constructor_args():
    sig = inspect.signature(go::EmbeddedField.__init__)
    params = list(sig.parameters.keys())



def test_go::identifierlist_is_not_abstract():
    assert not inspect.isabstract(go::IdentifierList)


def test_go::identifierlist_constructor_exists():
    assert callable(go::IdentifierList.__init__)


def test_go::identifierlist_constructor_args():
    sig = inspect.signature(go::IdentifierList.__init__)
    params = list(sig.parameters.keys())



def test_go::fielddecl_is_not_abstract():
    assert not inspect.isabstract(go::FieldDecl)


def test_go::fielddecl_constructor_exists():
    assert callable(go::FieldDecl.__init__)


def test_go::fielddecl_constructor_args():
    sig = inspect.signature(go::FieldDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::parameterdecl_is_not_abstract():
    assert not inspect.isabstract(go::ParameterDecl)


def test_go::parameterdecl_constructor_exists():
    assert callable(go::ParameterDecl.__init__)


def test_go::parameterdecl_constructor_args():
    sig = inspect.signature(go::ParameterDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::parameterlist_is_not_abstract():
    assert not inspect.isabstract(go::ParameterList)


def test_go::parameterlist_constructor_exists():
    assert callable(go::ParameterList.__init__)


def test_go::parameterlist_constructor_args():
    sig = inspect.signature(go::ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_receiver_is_not_abstract():
    assert not inspect.isabstract(Receiver)


def test_receiver_constructor_exists():
    assert callable(Receiver.__init__)


def test_receiver_constructor_args():
    sig = inspect.signature(Receiver.__init__)
    params = list(sig.parameters.keys())



def test_go::parameters_is_not_abstract():
    assert not inspect.isabstract(go::Parameters)


def test_go::parameters_constructor_exists():
    assert callable(go::Parameters.__init__)


def test_go::parameters_constructor_args():
    sig = inspect.signature(go::Parameters.__init__)
    params = list(sig.parameters.keys())



def test_go::interfacetype_is_not_abstract():
    assert not inspect.isabstract(go::InterfaceType)


def test_go::interfacetype_constructor_exists():
    assert callable(go::InterfaceType.__init__)


def test_go::interfacetype_constructor_args():
    sig = inspect.signature(go::InterfaceType.__init__)
    params = list(sig.parameters.keys())



def test_go::functiontype_is_not_abstract():
    assert not inspect.isabstract(go::FunctionType)


def test_go::functiontype_constructor_exists():
    assert callable(go::FunctionType.__init__)


def test_go::functiontype_constructor_args():
    sig = inspect.signature(go::FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_go::pointertype_is_not_abstract():
    assert not inspect.isabstract(go::PointerType)


def test_go::pointertype_constructor_exists():
    assert callable(go::PointerType.__init__)


def test_go::pointertype_constructor_args():
    sig = inspect.signature(go::PointerType.__init__)
    params = list(sig.parameters.keys())



def test_go::structtype_is_not_abstract():
    assert not inspect.isabstract(go::StructType)


def test_go::structtype_constructor_exists():
    assert callable(go::StructType.__init__)


def test_go::structtype_constructor_args():
    sig = inspect.signature(go::StructType.__init__)
    params = list(sig.parameters.keys())



def test_go::typelitlinha_is_not_abstract():
    assert not inspect.isabstract(go::TypeLitLinha)


def test_go::typelitlinha_constructor_exists():
    assert callable(go::TypeLitLinha.__init__)


def test_go::typelitlinha_constructor_args():
    sig = inspect.signature(go::TypeLitLinha.__init__)
    params = list(sig.parameters.keys())



def test_go::qualifiedident_is_not_abstract():
    assert not inspect.isabstract(go::QualifiedIdent)


def test_go::qualifiedident_constructor_exists():
    assert callable(go::QualifiedIdent.__init__)


def test_go::qualifiedident_constructor_args():
    sig = inspect.signature(go::QualifiedIdent.__init__)
    params = list(sig.parameters.keys())



def test_go::typenamelinha_is_not_abstract():
    assert not inspect.isabstract(go::TypeNameLinha)


def test_go::typenamelinha_constructor_exists():
    assert callable(go::TypeNameLinha.__init__)


def test_go::typenamelinha_constructor_args():
    sig = inspect.signature(go::TypeNameLinha.__init__)
    params = list(sig.parameters.keys())



def test_go::identifier_is_not_abstract():
    assert not inspect.isabstract(go::identifier)


def test_go::identifier_constructor_exists():
    assert callable(go::identifier.__init__)


def test_go::identifier_constructor_args():
    sig = inspect.signature(go::identifier.__init__)
    params = list(sig.parameters.keys())
    assert "LETTER" in params, "Missing parameter 'LETTER'"
    assert "DECIMAL_DIGIT" in params, "Missing parameter 'DECIMAL_DIGIT'"

def test_go::identifier_has_LETTER():
    assert hasattr(go::identifier, "LETTER")
    descriptor = None
    for klass in go::identifier.__mro__:
        if "LETTER" in klass.__dict__:
            descriptor = klass.__dict__["LETTER"]
            break
    assert isinstance(descriptor, property)

def test_go::identifier_has_DECIMAL_DIGIT():
    assert hasattr(go::identifier, "DECIMAL_DIGIT")
    descriptor = None
    for klass in go::identifier.__mro__:
        if "DECIMAL_DIGIT" in klass.__dict__:
            descriptor = klass.__dict__["DECIMAL_DIGIT"]
            break
    assert isinstance(descriptor, property)



def test_go::typelit_is_not_abstract():
    assert not inspect.isabstract(go::TypeLit)


def test_go::typelit_constructor_exists():
    assert callable(go::TypeLit.__init__)


def test_go::typelit_constructor_args():
    sig = inspect.signature(go::TypeLit.__init__)
    params = list(sig.parameters.keys())



def test_go::expression_is_not_abstract():
    assert not inspect.isabstract(go::Expression)


def test_go::expression_constructor_exists():
    assert callable(go::Expression.__init__)


def test_go::expression_constructor_args():
    sig = inspect.signature(go::Expression.__init__)
    params = list(sig.parameters.keys())



def test_go::elementtype_is_not_abstract():
    assert not inspect.isabstract(go::ElementType)


def test_go::elementtype_constructor_exists():
    assert callable(go::ElementType.__init__)


def test_go::elementtype_constructor_args():
    sig = inspect.signature(go::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_go::arraylength_is_not_abstract():
    assert not inspect.isabstract(go::ArrayLength)


def test_go::arraylength_constructor_exists():
    assert callable(go::ArrayLength.__init__)


def test_go::arraylength_constructor_args():
    sig = inspect.signature(go::ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_go::channeltype_is_not_abstract():
    assert not inspect.isabstract(go::ChannelType)


def test_go::channeltype_constructor_exists():
    assert callable(go::ChannelType.__init__)


def test_go::channeltype_constructor_args():
    sig = inspect.signature(go::ChannelType.__init__)
    params = list(sig.parameters.keys())



def test_go::maptype_is_not_abstract():
    assert not inspect.isabstract(go::MapType)


def test_go::maptype_constructor_exists():
    assert callable(go::MapType.__init__)


def test_go::maptype_constructor_args():
    sig = inspect.signature(go::MapType.__init__)
    params = list(sig.parameters.keys())



def test_go::typename_is_not_abstract():
    assert not inspect.isabstract(go::TypeName)


def test_go::typename_constructor_exists():
    assert callable(go::TypeName.__init__)


def test_go::typename_constructor_args():
    sig = inspect.signature(go::TypeName.__init__)
    params = list(sig.parameters.keys())



def test_go::type_is_not_abstract():
    assert not inspect.isabstract(go::Type)


def test_go::type_constructor_exists():
    assert callable(go::Type.__init__)


def test_go::type_constructor_args():
    sig = inspect.signature(go::Type.__init__)
    params = list(sig.parameters.keys())



def test_go::topleveldecl_is_not_abstract():
    assert not inspect.isabstract(go::TopLevelDecl)


def test_go::topleveldecl_constructor_exists():
    assert callable(go::TopLevelDecl.__init__)


def test_go::topleveldecl_constructor_args():
    sig = inspect.signature(go::TopLevelDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::importdecl_is_not_abstract():
    assert not inspect.isabstract(go::ImportDecl)


def test_go::importdecl_constructor_exists():
    assert callable(go::ImportDecl.__init__)


def test_go::importdecl_constructor_args():
    sig = inspect.signature(go::ImportDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::packageclause_is_not_abstract():
    assert not inspect.isabstract(go::PackageClause)


def test_go::packageclause_constructor_exists():
    assert callable(go::PackageClause.__init__)


def test_go::packageclause_constructor_args():
    sig = inspect.signature(go::PackageClause.__init__)
    params = list(sig.parameters.keys())



def test_float::lit_is_not_abstract():
    assert not inspect.isabstract(float::lit)


def test_float::lit_constructor_exists():
    assert callable(float::lit.__init__)


def test_float::lit_constructor_args():
    sig = inspect.signature(float::lit.__init__)
    params = list(sig.parameters.keys())



def test_go::decimals_is_not_abstract():
    assert not inspect.isabstract(go::decimals)


def test_go::decimals_constructor_exists():
    assert callable(go::decimals.__init__)


def test_go::decimals_constructor_args():
    sig = inspect.signature(go::decimals.__init__)
    params = list(sig.parameters.keys())
    assert "DECIMAL_DIGIT" in params, "Missing parameter 'DECIMAL_DIGIT'"

def test_go::decimals_has_DECIMAL_DIGIT():
    assert hasattr(go::decimals, "DECIMAL_DIGIT")
    descriptor = None
    for klass in go::decimals.__mro__:
        if "DECIMAL_DIGIT" in klass.__dict__:
            descriptor = klass.__dict__["DECIMAL_DIGIT"]
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
go::ImportPath_strategy = st.builds(
    go::ImportPath,
)
go::ImportSpec_strategy = st.builds(
    go::ImportSpec,
)
go::imaginary::lit_strategy = st.builds(
    go::imaginary::lit,
)
go::exponent_strategy = st.builds(
    go::exponent,
)
go::RecvExpr_strategy = st.builds(
    go::RecvExpr,
)
go::RecvStmt_strategy = st.builds(
    go::RecvStmt,
)
go::CommCase_strategy = st.builds(
    go::CommCase,
)
go::CommClause_strategy = st.builds(
    go::CommClause,
)
go::InitStmt_strategy = st.builds(
    go::InitStmt,
)
go::PostStmt_strategy = st.builds(
    go::PostStmt,
)
go::TypeCaseClause_strategy = st.builds(
    go::TypeCaseClause,
)
go::TypeSwitchGuard_strategy = st.builds(
    go::TypeSwitchGuard,
)
go::ExprSwitchCase_strategy = st.builds(
    go::ExprSwitchCase,
)
go::ExprCaseClause_strategy = st.builds(
    go::ExprCaseClause,
)
go::switch::stmt::linha_strategy = st.builds(
    go::switch::stmt::linha,
)
go::RangeClause_strategy = st.builds(
    go::RangeClause,
)
go::ForClause_strategy = st.builds(
    go::ForClause,
)
go::Condition_strategy = st.builds(
    go::Condition,
)
go::TypeList_strategy = st.builds(
    go::TypeList,
)
go::TypeSwitchCase_strategy = st.builds(
    go::TypeSwitchCase,
)
go::Channel_strategy = st.builds(
    go::Channel,
)
go::Label_strategy = st.builds(
    go::Label,
)
go::Assignment_strategy = st.builds(
    go::Assignment,
    assign_op=
        safe_text
)
go::IncDecStmt_strategy = st.builds(
    go::IncDecStmt,
)
go::SendStmt_strategy = st.builds(
    go::SendStmt,
)
go::ExpressionStmt_strategy = st.builds(
    go::ExpressionStmt,
)
go::GotoStmt_strategy = st.builds(
    go::GotoStmt,
)
go::ContinueStmt_strategy = st.builds(
    go::ContinueStmt,
)
go::BreakStmt_strategy = st.builds(
    go::BreakStmt,
)
go::ReturnStmt_strategy = st.builds(
    go::ReturnStmt,
)
go::GoStmt_strategy = st.builds(
    go::GoStmt,
)
go::SouceFile_strategy = st.builds(
    go::SouceFile,
)
go::LabeledStmt_strategy = st.builds(
    go::LabeledStmt,
)
SwitchStmt_strategy = st.builds(
    SwitchStmt,
)
go::SimpleStmt_strategy = st.builds(
    go::SimpleStmt,
    EmptyStmt=
        safe_text
)
go::DeferStmt_strategy = st.builds(
    go::DeferStmt,
)
go::ForStmt_strategy = st.builds(
    go::ForStmt,
)
go::SelectStmt_strategy = st.builds(
    go::SelectStmt,
)
go::SwitchStmt_strategy = st.builds(
    go::SwitchStmt,
)
go::IfStmt_strategy = st.builds(
    go::IfStmt,
)
go::ReceiverType_strategy = st.builds(
    go::ReceiverType,
)
go::Slice_strategy = st.builds(
    go::Slice,
)
go::binary::op_strategy = st.builds(
    go::binary::op,
    mul_op=
        safe_text,
    add_op=
        safe_text,
    rel_op=
        safe_text
)
go::ExpressionLinha_strategy = st.builds(
    go::ExpressionLinha,
)
go::UnaryExpr_strategy = st.builds(
    go::UnaryExpr,
    unary_op=
        safe_text
)
go::Arguments_strategy = st.builds(
    go::Arguments,
)
go::MethodExpr_strategy = st.builds(
    go::MethodExpr,
)
go::Conversion_strategy = st.builds(
    go::Conversion,
)
go::PrimaryExprLinha_strategy = st.builds(
    go::PrimaryExprLinha,
)
go::PrimaryExpr_strategy = st.builds(
    go::PrimaryExpr,
)
go::FieldName_strategy = st.builds(
    go::FieldName,
)
go::Index_strategy = st.builds(
    go::Index,
)
go::TypeAssertion_strategy = st.builds(
    go::TypeAssertion,
)
go::Selector_strategy = st.builds(
    go::Selector,
)
go::cochetes_strategy = st.builds(
    go::cochetes,
)
go::ponto_strategy = st.builds(
    go::ponto,
)
go::LiteralTypeLinha_strategy = st.builds(
    go::LiteralTypeLinha,
)
go::LiteralValue_strategy = st.builds(
    go::LiteralValue,
)
go::LiteralType_strategy = st.builds(
    go::LiteralType,
)
Literal_strategy = st.builds(
    Literal,
)
go::FunctionLit_strategy = st.builds(
    go::FunctionLit,
)
go::CompositeLit_strategy = st.builds(
    go::CompositeLit,
)
go::PackageName_strategy = st.builds(
    go::PackageName,
)
OperandName_strategy = st.builds(
    OperandName,
)
go::Key_strategy = st.builds(
    go::Key,
)
go::Element_strategy = st.builds(
    go::Element,
)
go::KeyedElement_strategy = st.builds(
    go::KeyedElement,
)
go::ElementList_strategy = st.builds(
    go::ElementList,
)
go::MethodDecl_strategy = st.builds(
    go::MethodDecl,
)
go::FunctionDecl_strategy = st.builds(
    go::FunctionDecl,
)
go::ShortVarDecl_strategy = st.builds(
    go::ShortVarDecl,
)
go::rune::lit_strategy = st.builds(
    go::rune::lit,
    byte_value=
        safe_text,
    unicode_value=
        safe_text
)
go::float::lit_strategy = st.builds(
    go::float::lit,
)
go::BasicLit_strategy = st.builds(
    go::BasicLit,
    int_lit=
        safe_text
)
go::OperandName_strategy = st.builds(
    go::OperandName,
)
go::Literal_strategy = st.builds(
    go::Literal,
)
go::Operand_strategy = st.builds(
    go::Operand,
)
go::ExpressionList_strategy = st.builds(
    go::ExpressionList,
)
go::ConstSpec_strategy = st.builds(
    go::ConstSpec,
)
go::Receiver_strategy = st.builds(
    go::Receiver,
)
go::FunctionBody_strategy = st.builds(
    go::FunctionBody,
)
go::FunctionName_strategy = st.builds(
    go::FunctionName,
)
go::VarSpec_strategy = st.builds(
    go::VarSpec,
)
TypeSpec_strategy = st.builds(
    TypeSpec,
)
go::TypeDef_strategy = st.builds(
    go::TypeDef,
)
go::AliasDecl_strategy = st.builds(
    go::AliasDecl,
)
go::TypeSpec_strategy = st.builds(
    go::TypeSpec,
)
go::KeyType_strategy = st.builds(
    go::KeyType,
)
go::InterfaceTypeName_strategy = st.builds(
    go::InterfaceTypeName,
)
go::MethodName_strategy = st.builds(
    go::MethodName,
)
go::MethodSpec_strategy = st.builds(
    go::MethodSpec,
)
go::topLevelDeclLinha_strategy = st.builds(
    go::topLevelDeclLinha,
)
go::VarDecl_strategy = st.builds(
    go::VarDecl,
)
go::TypeDecl_strategy = st.builds(
    go::TypeDecl,
)
go::ConstDecl_strategy = st.builds(
    go::ConstDecl,
)
go::Declaration_strategy = st.builds(
    go::Declaration,
)
go::Statement_strategy = st.builds(
    go::Statement,
    FallthroughStmt=
        safe_text
)
go::StatementList_strategy = st.builds(
    go::StatementList,
)
go::Block_strategy = st.builds(
    go::Block,
)
go::Result_strategy = st.builds(
    go::Result,
)
go::Signature_strategy = st.builds(
    go::Signature,
)
go::string::lit_strategy = st.builds(
    go::string::lit,
    interpreted_string_lit=
        safe_text,
    raw_string_lit=
        safe_text
)
go::Tag_strategy = st.builds(
    go::Tag,
)
go::EmbeddedField_strategy = st.builds(
    go::EmbeddedField,
)
go::IdentifierList_strategy = st.builds(
    go::IdentifierList,
)
go::FieldDecl_strategy = st.builds(
    go::FieldDecl,
)
go::ParameterDecl_strategy = st.builds(
    go::ParameterDecl,
)
go::ParameterList_strategy = st.builds(
    go::ParameterList,
)
Receiver_strategy = st.builds(
    Receiver,
)
go::Parameters_strategy = st.builds(
    go::Parameters,
)
go::InterfaceType_strategy = st.builds(
    go::InterfaceType,
)
go::FunctionType_strategy = st.builds(
    go::FunctionType,
)
go::PointerType_strategy = st.builds(
    go::PointerType,
)
go::StructType_strategy = st.builds(
    go::StructType,
)
go::TypeLitLinha_strategy = st.builds(
    go::TypeLitLinha,
)
go::QualifiedIdent_strategy = st.builds(
    go::QualifiedIdent,
)
go::TypeNameLinha_strategy = st.builds(
    go::TypeNameLinha,
)
go::identifier_strategy = st.builds(
    go::identifier,
    LETTER=
        safe_text,
    DECIMAL_DIGIT=
        safe_text
)
go::TypeLit_strategy = st.builds(
    go::TypeLit,
)
go::Expression_strategy = st.builds(
    go::Expression,
)
go::ElementType_strategy = st.builds(
    go::ElementType,
)
go::ArrayLength_strategy = st.builds(
    go::ArrayLength,
)
go::ChannelType_strategy = st.builds(
    go::ChannelType,
)
go::MapType_strategy = st.builds(
    go::MapType,
)
go::TypeName_strategy = st.builds(
    go::TypeName,
)
go::Type_strategy = st.builds(
    go::Type,
)
go::TopLevelDecl_strategy = st.builds(
    go::TopLevelDecl,
)
go::ImportDecl_strategy = st.builds(
    go::ImportDecl,
)
go::PackageClause_strategy = st.builds(
    go::PackageClause,
)
float::lit_strategy = st.builds(
    float::lit,
)
go::decimals_strategy = st.builds(
    go::decimals,
    DECIMAL_DIGIT=
        safe_text
)

@given(instance=go::ImportPath_strategy)
@settings(max_examples=50)
def test_go::importpath_instantiation(instance):
    assert isinstance(instance, go::ImportPath)

@given(instance=go::ImportSpec_strategy)
@settings(max_examples=50)
def test_go::importspec_instantiation(instance):
    assert isinstance(instance, go::ImportSpec)

@given(instance=go::imaginary::lit_strategy)
@settings(max_examples=50)
def test_go::imaginary::lit_instantiation(instance):
    assert isinstance(instance, go::imaginary::lit)

@given(instance=go::exponent_strategy)
@settings(max_examples=50)
def test_go::exponent_instantiation(instance):
    assert isinstance(instance, go::exponent)

@given(instance=go::RecvExpr_strategy)
@settings(max_examples=50)
def test_go::recvexpr_instantiation(instance):
    assert isinstance(instance, go::RecvExpr)

@given(instance=go::RecvStmt_strategy)
@settings(max_examples=50)
def test_go::recvstmt_instantiation(instance):
    assert isinstance(instance, go::RecvStmt)

@given(instance=go::CommCase_strategy)
@settings(max_examples=50)
def test_go::commcase_instantiation(instance):
    assert isinstance(instance, go::CommCase)

@given(instance=go::CommClause_strategy)
@settings(max_examples=50)
def test_go::commclause_instantiation(instance):
    assert isinstance(instance, go::CommClause)

@given(instance=go::InitStmt_strategy)
@settings(max_examples=50)
def test_go::initstmt_instantiation(instance):
    assert isinstance(instance, go::InitStmt)

@given(instance=go::PostStmt_strategy)
@settings(max_examples=50)
def test_go::poststmt_instantiation(instance):
    assert isinstance(instance, go::PostStmt)

@given(instance=go::TypeCaseClause_strategy)
@settings(max_examples=50)
def test_go::typecaseclause_instantiation(instance):
    assert isinstance(instance, go::TypeCaseClause)

@given(instance=go::TypeSwitchGuard_strategy)
@settings(max_examples=50)
def test_go::typeswitchguard_instantiation(instance):
    assert isinstance(instance, go::TypeSwitchGuard)

@given(instance=go::ExprSwitchCase_strategy)
@settings(max_examples=50)
def test_go::exprswitchcase_instantiation(instance):
    assert isinstance(instance, go::ExprSwitchCase)

@given(instance=go::ExprCaseClause_strategy)
@settings(max_examples=50)
def test_go::exprcaseclause_instantiation(instance):
    assert isinstance(instance, go::ExprCaseClause)

@given(instance=go::switch::stmt::linha_strategy)
@settings(max_examples=50)
def test_go::switch::stmt::linha_instantiation(instance):
    assert isinstance(instance, go::switch::stmt::linha)

@given(instance=go::RangeClause_strategy)
@settings(max_examples=50)
def test_go::rangeclause_instantiation(instance):
    assert isinstance(instance, go::RangeClause)

@given(instance=go::ForClause_strategy)
@settings(max_examples=50)
def test_go::forclause_instantiation(instance):
    assert isinstance(instance, go::ForClause)

@given(instance=go::Condition_strategy)
@settings(max_examples=50)
def test_go::condition_instantiation(instance):
    assert isinstance(instance, go::Condition)

@given(instance=go::TypeList_strategy)
@settings(max_examples=50)
def test_go::typelist_instantiation(instance):
    assert isinstance(instance, go::TypeList)

@given(instance=go::TypeSwitchCase_strategy)
@settings(max_examples=50)
def test_go::typeswitchcase_instantiation(instance):
    assert isinstance(instance, go::TypeSwitchCase)

@given(instance=go::Channel_strategy)
@settings(max_examples=50)
def test_go::channel_instantiation(instance):
    assert isinstance(instance, go::Channel)

@given(instance=go::Label_strategy)
@settings(max_examples=50)
def test_go::label_instantiation(instance):
    assert isinstance(instance, go::Label)

@given(instance=go::Assignment_strategy)
@settings(max_examples=50)
def test_go::assignment_instantiation(instance):
    assert isinstance(instance, go::Assignment)

@given(instance=go::Assignment_strategy)
def test_go::assignment_assign_op_type(instance):
    assert isinstance(instance.assign_op, str)


@given(instance=go::Assignment_strategy)
def test_go::assignment_assign_op_setter(instance):
    original = instance.assign_op
    instance.assign_op = original
    assert instance.assign_op == original

@given(instance=go::IncDecStmt_strategy)
@settings(max_examples=50)
def test_go::incdecstmt_instantiation(instance):
    assert isinstance(instance, go::IncDecStmt)

@given(instance=go::SendStmt_strategy)
@settings(max_examples=50)
def test_go::sendstmt_instantiation(instance):
    assert isinstance(instance, go::SendStmt)

@given(instance=go::ExpressionStmt_strategy)
@settings(max_examples=50)
def test_go::expressionstmt_instantiation(instance):
    assert isinstance(instance, go::ExpressionStmt)

@given(instance=go::GotoStmt_strategy)
@settings(max_examples=50)
def test_go::gotostmt_instantiation(instance):
    assert isinstance(instance, go::GotoStmt)

@given(instance=go::ContinueStmt_strategy)
@settings(max_examples=50)
def test_go::continuestmt_instantiation(instance):
    assert isinstance(instance, go::ContinueStmt)

@given(instance=go::BreakStmt_strategy)
@settings(max_examples=50)
def test_go::breakstmt_instantiation(instance):
    assert isinstance(instance, go::BreakStmt)

@given(instance=go::ReturnStmt_strategy)
@settings(max_examples=50)
def test_go::returnstmt_instantiation(instance):
    assert isinstance(instance, go::ReturnStmt)

@given(instance=go::GoStmt_strategy)
@settings(max_examples=50)
def test_go::gostmt_instantiation(instance):
    assert isinstance(instance, go::GoStmt)

@given(instance=go::SouceFile_strategy)
@settings(max_examples=50)
def test_go::soucefile_instantiation(instance):
    assert isinstance(instance, go::SouceFile)

@given(instance=go::LabeledStmt_strategy)
@settings(max_examples=50)
def test_go::labeledstmt_instantiation(instance):
    assert isinstance(instance, go::LabeledStmt)

@given(instance=SwitchStmt_strategy)
@settings(max_examples=50)
def test_switchstmt_instantiation(instance):
    assert isinstance(instance, SwitchStmt)

@given(instance=go::SimpleStmt_strategy)
@settings(max_examples=50)
def test_go::simplestmt_instantiation(instance):
    assert isinstance(instance, go::SimpleStmt)

@given(instance=go::SimpleStmt_strategy)
def test_go::simplestmt_EmptyStmt_type(instance):
    assert isinstance(instance.EmptyStmt, str)


@given(instance=go::SimpleStmt_strategy)
def test_go::simplestmt_EmptyStmt_setter(instance):
    original = instance.EmptyStmt
    instance.EmptyStmt = original
    assert instance.EmptyStmt == original

@given(instance=go::DeferStmt_strategy)
@settings(max_examples=50)
def test_go::deferstmt_instantiation(instance):
    assert isinstance(instance, go::DeferStmt)

@given(instance=go::ForStmt_strategy)
@settings(max_examples=50)
def test_go::forstmt_instantiation(instance):
    assert isinstance(instance, go::ForStmt)

@given(instance=go::SelectStmt_strategy)
@settings(max_examples=50)
def test_go::selectstmt_instantiation(instance):
    assert isinstance(instance, go::SelectStmt)

@given(instance=go::SwitchStmt_strategy)
@settings(max_examples=50)
def test_go::switchstmt_instantiation(instance):
    assert isinstance(instance, go::SwitchStmt)

@given(instance=go::IfStmt_strategy)
@settings(max_examples=50)
def test_go::ifstmt_instantiation(instance):
    assert isinstance(instance, go::IfStmt)

@given(instance=go::ReceiverType_strategy)
@settings(max_examples=50)
def test_go::receivertype_instantiation(instance):
    assert isinstance(instance, go::ReceiverType)

@given(instance=go::Slice_strategy)
@settings(max_examples=50)
def test_go::slice_instantiation(instance):
    assert isinstance(instance, go::Slice)

@given(instance=go::binary::op_strategy)
@settings(max_examples=50)
def test_go::binary::op_instantiation(instance):
    assert isinstance(instance, go::binary::op)

@given(instance=go::binary::op_strategy)
def test_go::binary::op_mul_op_type(instance):
    assert isinstance(instance.mul_op, str)


@given(instance=go::binary::op_strategy)
def test_go::binary::op_mul_op_setter(instance):
    original = instance.mul_op
    instance.mul_op = original
    assert instance.mul_op == original

@given(instance=go::binary::op_strategy)
def test_go::binary::op_add_op_type(instance):
    assert isinstance(instance.add_op, str)


@given(instance=go::binary::op_strategy)
def test_go::binary::op_add_op_setter(instance):
    original = instance.add_op
    instance.add_op = original
    assert instance.add_op == original

@given(instance=go::binary::op_strategy)
def test_go::binary::op_rel_op_type(instance):
    assert isinstance(instance.rel_op, str)


@given(instance=go::binary::op_strategy)
def test_go::binary::op_rel_op_setter(instance):
    original = instance.rel_op
    instance.rel_op = original
    assert instance.rel_op == original

@given(instance=go::ExpressionLinha_strategy)
@settings(max_examples=50)
def test_go::expressionlinha_instantiation(instance):
    assert isinstance(instance, go::ExpressionLinha)

@given(instance=go::UnaryExpr_strategy)
@settings(max_examples=50)
def test_go::unaryexpr_instantiation(instance):
    assert isinstance(instance, go::UnaryExpr)

@given(instance=go::UnaryExpr_strategy)
def test_go::unaryexpr_unary_op_type(instance):
    assert isinstance(instance.unary_op, str)


@given(instance=go::UnaryExpr_strategy)
def test_go::unaryexpr_unary_op_setter(instance):
    original = instance.unary_op
    instance.unary_op = original
    assert instance.unary_op == original

@given(instance=go::Arguments_strategy)
@settings(max_examples=50)
def test_go::arguments_instantiation(instance):
    assert isinstance(instance, go::Arguments)

@given(instance=go::MethodExpr_strategy)
@settings(max_examples=50)
def test_go::methodexpr_instantiation(instance):
    assert isinstance(instance, go::MethodExpr)

@given(instance=go::Conversion_strategy)
@settings(max_examples=50)
def test_go::conversion_instantiation(instance):
    assert isinstance(instance, go::Conversion)

@given(instance=go::PrimaryExprLinha_strategy)
@settings(max_examples=50)
def test_go::primaryexprlinha_instantiation(instance):
    assert isinstance(instance, go::PrimaryExprLinha)

@given(instance=go::PrimaryExpr_strategy)
@settings(max_examples=50)
def test_go::primaryexpr_instantiation(instance):
    assert isinstance(instance, go::PrimaryExpr)

@given(instance=go::FieldName_strategy)
@settings(max_examples=50)
def test_go::fieldname_instantiation(instance):
    assert isinstance(instance, go::FieldName)

@given(instance=go::Index_strategy)
@settings(max_examples=50)
def test_go::index_instantiation(instance):
    assert isinstance(instance, go::Index)

@given(instance=go::TypeAssertion_strategy)
@settings(max_examples=50)
def test_go::typeassertion_instantiation(instance):
    assert isinstance(instance, go::TypeAssertion)

@given(instance=go::Selector_strategy)
@settings(max_examples=50)
def test_go::selector_instantiation(instance):
    assert isinstance(instance, go::Selector)

@given(instance=go::cochetes_strategy)
@settings(max_examples=50)
def test_go::cochetes_instantiation(instance):
    assert isinstance(instance, go::cochetes)

@given(instance=go::ponto_strategy)
@settings(max_examples=50)
def test_go::ponto_instantiation(instance):
    assert isinstance(instance, go::ponto)

@given(instance=go::LiteralTypeLinha_strategy)
@settings(max_examples=50)
def test_go::literaltypelinha_instantiation(instance):
    assert isinstance(instance, go::LiteralTypeLinha)

@given(instance=go::LiteralValue_strategy)
@settings(max_examples=50)
def test_go::literalvalue_instantiation(instance):
    assert isinstance(instance, go::LiteralValue)

@given(instance=go::LiteralType_strategy)
@settings(max_examples=50)
def test_go::literaltype_instantiation(instance):
    assert isinstance(instance, go::LiteralType)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=go::FunctionLit_strategy)
@settings(max_examples=50)
def test_go::functionlit_instantiation(instance):
    assert isinstance(instance, go::FunctionLit)

@given(instance=go::CompositeLit_strategy)
@settings(max_examples=50)
def test_go::compositelit_instantiation(instance):
    assert isinstance(instance, go::CompositeLit)

@given(instance=go::PackageName_strategy)
@settings(max_examples=50)
def test_go::packagename_instantiation(instance):
    assert isinstance(instance, go::PackageName)

@given(instance=OperandName_strategy)
@settings(max_examples=50)
def test_operandname_instantiation(instance):
    assert isinstance(instance, OperandName)

@given(instance=go::Key_strategy)
@settings(max_examples=50)
def test_go::key_instantiation(instance):
    assert isinstance(instance, go::Key)

@given(instance=go::Element_strategy)
@settings(max_examples=50)
def test_go::element_instantiation(instance):
    assert isinstance(instance, go::Element)

@given(instance=go::KeyedElement_strategy)
@settings(max_examples=50)
def test_go::keyedelement_instantiation(instance):
    assert isinstance(instance, go::KeyedElement)

@given(instance=go::ElementList_strategy)
@settings(max_examples=50)
def test_go::elementlist_instantiation(instance):
    assert isinstance(instance, go::ElementList)

@given(instance=go::MethodDecl_strategy)
@settings(max_examples=50)
def test_go::methoddecl_instantiation(instance):
    assert isinstance(instance, go::MethodDecl)

@given(instance=go::FunctionDecl_strategy)
@settings(max_examples=50)
def test_go::functiondecl_instantiation(instance):
    assert isinstance(instance, go::FunctionDecl)

@given(instance=go::ShortVarDecl_strategy)
@settings(max_examples=50)
def test_go::shortvardecl_instantiation(instance):
    assert isinstance(instance, go::ShortVarDecl)

@given(instance=go::rune::lit_strategy)
@settings(max_examples=50)
def test_go::rune::lit_instantiation(instance):
    assert isinstance(instance, go::rune::lit)

@given(instance=go::rune::lit_strategy)
def test_go::rune::lit_byte_value_type(instance):
    assert isinstance(instance.byte_value, str)


@given(instance=go::rune::lit_strategy)
def test_go::rune::lit_byte_value_setter(instance):
    original = instance.byte_value
    instance.byte_value = original
    assert instance.byte_value == original

@given(instance=go::rune::lit_strategy)
def test_go::rune::lit_unicode_value_type(instance):
    assert isinstance(instance.unicode_value, str)


@given(instance=go::rune::lit_strategy)
def test_go::rune::lit_unicode_value_setter(instance):
    original = instance.unicode_value
    instance.unicode_value = original
    assert instance.unicode_value == original

@given(instance=go::float::lit_strategy)
@settings(max_examples=50)
def test_go::float::lit_instantiation(instance):
    assert isinstance(instance, go::float::lit)

@given(instance=go::BasicLit_strategy)
@settings(max_examples=50)
def test_go::basiclit_instantiation(instance):
    assert isinstance(instance, go::BasicLit)

@given(instance=go::BasicLit_strategy)
def test_go::basiclit_int_lit_type(instance):
    assert isinstance(instance.int_lit, str)


@given(instance=go::BasicLit_strategy)
def test_go::basiclit_int_lit_setter(instance):
    original = instance.int_lit
    instance.int_lit = original
    assert instance.int_lit == original

@given(instance=go::OperandName_strategy)
@settings(max_examples=50)
def test_go::operandname_instantiation(instance):
    assert isinstance(instance, go::OperandName)

@given(instance=go::Literal_strategy)
@settings(max_examples=50)
def test_go::literal_instantiation(instance):
    assert isinstance(instance, go::Literal)

@given(instance=go::Operand_strategy)
@settings(max_examples=50)
def test_go::operand_instantiation(instance):
    assert isinstance(instance, go::Operand)

@given(instance=go::ExpressionList_strategy)
@settings(max_examples=50)
def test_go::expressionlist_instantiation(instance):
    assert isinstance(instance, go::ExpressionList)

@given(instance=go::ConstSpec_strategy)
@settings(max_examples=50)
def test_go::constspec_instantiation(instance):
    assert isinstance(instance, go::ConstSpec)

@given(instance=go::Receiver_strategy)
@settings(max_examples=50)
def test_go::receiver_instantiation(instance):
    assert isinstance(instance, go::Receiver)

@given(instance=go::FunctionBody_strategy)
@settings(max_examples=50)
def test_go::functionbody_instantiation(instance):
    assert isinstance(instance, go::FunctionBody)

@given(instance=go::FunctionName_strategy)
@settings(max_examples=50)
def test_go::functionname_instantiation(instance):
    assert isinstance(instance, go::FunctionName)

@given(instance=go::VarSpec_strategy)
@settings(max_examples=50)
def test_go::varspec_instantiation(instance):
    assert isinstance(instance, go::VarSpec)

@given(instance=TypeSpec_strategy)
@settings(max_examples=50)
def test_typespec_instantiation(instance):
    assert isinstance(instance, TypeSpec)

@given(instance=go::TypeDef_strategy)
@settings(max_examples=50)
def test_go::typedef_instantiation(instance):
    assert isinstance(instance, go::TypeDef)

@given(instance=go::AliasDecl_strategy)
@settings(max_examples=50)
def test_go::aliasdecl_instantiation(instance):
    assert isinstance(instance, go::AliasDecl)

@given(instance=go::TypeSpec_strategy)
@settings(max_examples=50)
def test_go::typespec_instantiation(instance):
    assert isinstance(instance, go::TypeSpec)

@given(instance=go::KeyType_strategy)
@settings(max_examples=50)
def test_go::keytype_instantiation(instance):
    assert isinstance(instance, go::KeyType)

@given(instance=go::InterfaceTypeName_strategy)
@settings(max_examples=50)
def test_go::interfacetypename_instantiation(instance):
    assert isinstance(instance, go::InterfaceTypeName)

@given(instance=go::MethodName_strategy)
@settings(max_examples=50)
def test_go::methodname_instantiation(instance):
    assert isinstance(instance, go::MethodName)

@given(instance=go::MethodSpec_strategy)
@settings(max_examples=50)
def test_go::methodspec_instantiation(instance):
    assert isinstance(instance, go::MethodSpec)

@given(instance=go::topLevelDeclLinha_strategy)
@settings(max_examples=50)
def test_go::topleveldecllinha_instantiation(instance):
    assert isinstance(instance, go::topLevelDeclLinha)

@given(instance=go::VarDecl_strategy)
@settings(max_examples=50)
def test_go::vardecl_instantiation(instance):
    assert isinstance(instance, go::VarDecl)

@given(instance=go::TypeDecl_strategy)
@settings(max_examples=50)
def test_go::typedecl_instantiation(instance):
    assert isinstance(instance, go::TypeDecl)

@given(instance=go::ConstDecl_strategy)
@settings(max_examples=50)
def test_go::constdecl_instantiation(instance):
    assert isinstance(instance, go::ConstDecl)

@given(instance=go::Declaration_strategy)
@settings(max_examples=50)
def test_go::declaration_instantiation(instance):
    assert isinstance(instance, go::Declaration)

@given(instance=go::Statement_strategy)
@settings(max_examples=50)
def test_go::statement_instantiation(instance):
    assert isinstance(instance, go::Statement)

@given(instance=go::Statement_strategy)
def test_go::statement_FallthroughStmt_type(instance):
    assert isinstance(instance.FallthroughStmt, str)


@given(instance=go::Statement_strategy)
def test_go::statement_FallthroughStmt_setter(instance):
    original = instance.FallthroughStmt
    instance.FallthroughStmt = original
    assert instance.FallthroughStmt == original

@given(instance=go::StatementList_strategy)
@settings(max_examples=50)
def test_go::statementlist_instantiation(instance):
    assert isinstance(instance, go::StatementList)

@given(instance=go::Block_strategy)
@settings(max_examples=50)
def test_go::block_instantiation(instance):
    assert isinstance(instance, go::Block)

@given(instance=go::Result_strategy)
@settings(max_examples=50)
def test_go::result_instantiation(instance):
    assert isinstance(instance, go::Result)

@given(instance=go::Signature_strategy)
@settings(max_examples=50)
def test_go::signature_instantiation(instance):
    assert isinstance(instance, go::Signature)

@given(instance=go::string::lit_strategy)
@settings(max_examples=50)
def test_go::string::lit_instantiation(instance):
    assert isinstance(instance, go::string::lit)

@given(instance=go::string::lit_strategy)
def test_go::string::lit_interpreted_string_lit_type(instance):
    assert isinstance(instance.interpreted_string_lit, str)


@given(instance=go::string::lit_strategy)
def test_go::string::lit_interpreted_string_lit_setter(instance):
    original = instance.interpreted_string_lit
    instance.interpreted_string_lit = original
    assert instance.interpreted_string_lit == original

@given(instance=go::string::lit_strategy)
def test_go::string::lit_raw_string_lit_type(instance):
    assert isinstance(instance.raw_string_lit, str)


@given(instance=go::string::lit_strategy)
def test_go::string::lit_raw_string_lit_setter(instance):
    original = instance.raw_string_lit
    instance.raw_string_lit = original
    assert instance.raw_string_lit == original

@given(instance=go::Tag_strategy)
@settings(max_examples=50)
def test_go::tag_instantiation(instance):
    assert isinstance(instance, go::Tag)

@given(instance=go::EmbeddedField_strategy)
@settings(max_examples=50)
def test_go::embeddedfield_instantiation(instance):
    assert isinstance(instance, go::EmbeddedField)

@given(instance=go::IdentifierList_strategy)
@settings(max_examples=50)
def test_go::identifierlist_instantiation(instance):
    assert isinstance(instance, go::IdentifierList)

@given(instance=go::FieldDecl_strategy)
@settings(max_examples=50)
def test_go::fielddecl_instantiation(instance):
    assert isinstance(instance, go::FieldDecl)

@given(instance=go::ParameterDecl_strategy)
@settings(max_examples=50)
def test_go::parameterdecl_instantiation(instance):
    assert isinstance(instance, go::ParameterDecl)

@given(instance=go::ParameterList_strategy)
@settings(max_examples=50)
def test_go::parameterlist_instantiation(instance):
    assert isinstance(instance, go::ParameterList)

@given(instance=Receiver_strategy)
@settings(max_examples=50)
def test_receiver_instantiation(instance):
    assert isinstance(instance, Receiver)

@given(instance=go::Parameters_strategy)
@settings(max_examples=50)
def test_go::parameters_instantiation(instance):
    assert isinstance(instance, go::Parameters)

@given(instance=go::InterfaceType_strategy)
@settings(max_examples=50)
def test_go::interfacetype_instantiation(instance):
    assert isinstance(instance, go::InterfaceType)

@given(instance=go::FunctionType_strategy)
@settings(max_examples=50)
def test_go::functiontype_instantiation(instance):
    assert isinstance(instance, go::FunctionType)

@given(instance=go::PointerType_strategy)
@settings(max_examples=50)
def test_go::pointertype_instantiation(instance):
    assert isinstance(instance, go::PointerType)

@given(instance=go::StructType_strategy)
@settings(max_examples=50)
def test_go::structtype_instantiation(instance):
    assert isinstance(instance, go::StructType)

@given(instance=go::TypeLitLinha_strategy)
@settings(max_examples=50)
def test_go::typelitlinha_instantiation(instance):
    assert isinstance(instance, go::TypeLitLinha)

@given(instance=go::QualifiedIdent_strategy)
@settings(max_examples=50)
def test_go::qualifiedident_instantiation(instance):
    assert isinstance(instance, go::QualifiedIdent)

@given(instance=go::TypeNameLinha_strategy)
@settings(max_examples=50)
def test_go::typenamelinha_instantiation(instance):
    assert isinstance(instance, go::TypeNameLinha)

@given(instance=go::identifier_strategy)
@settings(max_examples=50)
def test_go::identifier_instantiation(instance):
    assert isinstance(instance, go::identifier)

@given(instance=go::identifier_strategy)
def test_go::identifier_LETTER_type(instance):
    assert isinstance(instance.LETTER, str)


@given(instance=go::identifier_strategy)
def test_go::identifier_LETTER_setter(instance):
    original = instance.LETTER
    instance.LETTER = original
    assert instance.LETTER == original

@given(instance=go::identifier_strategy)
def test_go::identifier_DECIMAL_DIGIT_type(instance):
    assert isinstance(instance.DECIMAL_DIGIT, str)


@given(instance=go::identifier_strategy)
def test_go::identifier_DECIMAL_DIGIT_setter(instance):
    original = instance.DECIMAL_DIGIT
    instance.DECIMAL_DIGIT = original
    assert instance.DECIMAL_DIGIT == original

@given(instance=go::TypeLit_strategy)
@settings(max_examples=50)
def test_go::typelit_instantiation(instance):
    assert isinstance(instance, go::TypeLit)

@given(instance=go::Expression_strategy)
@settings(max_examples=50)
def test_go::expression_instantiation(instance):
    assert isinstance(instance, go::Expression)

@given(instance=go::ElementType_strategy)
@settings(max_examples=50)
def test_go::elementtype_instantiation(instance):
    assert isinstance(instance, go::ElementType)

@given(instance=go::ArrayLength_strategy)
@settings(max_examples=50)
def test_go::arraylength_instantiation(instance):
    assert isinstance(instance, go::ArrayLength)

@given(instance=go::ChannelType_strategy)
@settings(max_examples=50)
def test_go::channeltype_instantiation(instance):
    assert isinstance(instance, go::ChannelType)

@given(instance=go::MapType_strategy)
@settings(max_examples=50)
def test_go::maptype_instantiation(instance):
    assert isinstance(instance, go::MapType)

@given(instance=go::TypeName_strategy)
@settings(max_examples=50)
def test_go::typename_instantiation(instance):
    assert isinstance(instance, go::TypeName)

@given(instance=go::Type_strategy)
@settings(max_examples=50)
def test_go::type_instantiation(instance):
    assert isinstance(instance, go::Type)

@given(instance=go::TopLevelDecl_strategy)
@settings(max_examples=50)
def test_go::topleveldecl_instantiation(instance):
    assert isinstance(instance, go::TopLevelDecl)

@given(instance=go::ImportDecl_strategy)
@settings(max_examples=50)
def test_go::importdecl_instantiation(instance):
    assert isinstance(instance, go::ImportDecl)

@given(instance=go::PackageClause_strategy)
@settings(max_examples=50)
def test_go::packageclause_instantiation(instance):
    assert isinstance(instance, go::PackageClause)

@given(instance=float::lit_strategy)
@settings(max_examples=50)
def test_float::lit_instantiation(instance):
    assert isinstance(instance, float::lit)

@given(instance=go::decimals_strategy)
@settings(max_examples=50)
def test_go::decimals_instantiation(instance):
    assert isinstance(instance, go::decimals)

@given(instance=go::decimals_strategy)
def test_go::decimals_DECIMAL_DIGIT_type(instance):
    assert isinstance(instance.DECIMAL_DIGIT, str)


@given(instance=go::decimals_strategy)
def test_go::decimals_DECIMAL_DIGIT_setter(instance):
    original = instance.DECIMAL_DIGIT
    instance.DECIMAL_DIGIT = original
    assert instance.DECIMAL_DIGIT == original
