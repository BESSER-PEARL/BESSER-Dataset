import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Else,
    limp::NoElse,
    limp::ElseIf,
    limp::ElseBlock,
    AttributeBlock,
    limp::NoAttributeBlock,
    limp::SomeAttributeBlock,
    Type,
    limp::RecordType,
    limp::ArrayType,
    limp::RealType,
    limp::StringType,
    limp::EnumType,
    limp::BoolType,
    limp::TupleType,
    limp::IntegerType,
    limp::VoidType,
    VarBlock,
    limp::NoVarBlock,
    limp::SomeVarBlock,
    limp::ExprList,
    limp::NamedType,
    limp::AbstractType,
    Expr,
    limp::IfThenElseExpr,
    limp::InitExpr,
    limp::BinaryExpr,
    limp::FreshVariable,
    limp::RecordUpdateExpr,
    limp::FcnCallExpr,
    limp::UnaryNegationExpr,
    limp::ChoiceExpr,
    limp::IntegerLiteralExpr,
    limp::ArrayUpdateExpr,
    limp::RecordAccessExpr,
    limp::UnaryMinusExpr,
    limp::BooleanLiteralExpr,
    limp::IdExpr,
    limp::SecondInit,
    limp::ArrayAccessExpr,
    limp::RealLiteralExpr,
    limp::StringLiteralExpr,
    limp::IntegerWildCardExpr,
    limp::ArrayExpr,
    limp::FunctionRef,
    limp::Equation,
    limp::RecordFieldExpr,
    limp::RecordExpr,
    limp::IdList,
    Equation,
    Statement,
    limp::ReturnStatement,
    limp::GotoStatement,
    limp::AssignmentStatement,
    limp::IfThenElseStatement,
    limp::LabelStatement,
    limp::ForStatement,
    limp::ContinueStatement,
    limp::BreakStatement,
    limp::VoidStatement,
    limp::Statement,
    limp::DefineUseRef,
    limp::WhileStatement,
    limp::Else,
    limp::VariableRef,
    limp::Expr,
    Attribute,
    limp::Uses,
    limp::Define,
    limp::Postcondition,
    limp::Precondition,
    limp::Attribute,
    limp::RecordFieldType,
    VariableRef,
    limp::LocalArg,
    limp::InputArg,
    limp::EnumValue,
    TypeDeclaration,
    limp::TypeAlias,
    limp::RecordTypeDef,
    limp::EnumTypeDef,
    limp::StatementBlock,
    limp::EquationBlock,
    limp::AbstractTypeDef,
    limp::Type,
    limp::ArrayTypeDef,
    limp::AttributeBlock,
    limp::OutputArgList,
    limp::OutputArg,
    limp::InputArgList,
    FunctionRef,
    Declaration,
    limp::ExternalProcedure,
    limp::LocalProcedure,
    limp::TypeDeclaration,
    limp::Import,
    limp::ExternalFunction,
    limp::ConstantDeclaration,
    limp::GlobalDeclaration,
    limp::Comment,
    limp::Declaration,
    limp::Specification,
    limp::VarBlock,
    limp::LocalFunction,
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



def test_limp::noelse_is_not_abstract():
    assert not inspect.isabstract(limp::NoElse)


def test_limp::noelse_constructor_exists():
    assert callable(limp::NoElse.__init__)


def test_limp::noelse_constructor_args():
    sig = inspect.signature(limp::NoElse.__init__)
    params = list(sig.parameters.keys())



def test_limp::elseif_is_not_abstract():
    assert not inspect.isabstract(limp::ElseIf)


def test_limp::elseif_constructor_exists():
    assert callable(limp::ElseIf.__init__)


def test_limp::elseif_constructor_args():
    sig = inspect.signature(limp::ElseIf.__init__)
    params = list(sig.parameters.keys())



def test_limp::elseblock_is_not_abstract():
    assert not inspect.isabstract(limp::ElseBlock)


def test_limp::elseblock_constructor_exists():
    assert callable(limp::ElseBlock.__init__)


def test_limp::elseblock_constructor_args():
    sig = inspect.signature(limp::ElseBlock.__init__)
    params = list(sig.parameters.keys())



def test_attributeblock_is_not_abstract():
    assert not inspect.isabstract(AttributeBlock)


def test_attributeblock_constructor_exists():
    assert callable(AttributeBlock.__init__)


def test_attributeblock_constructor_args():
    sig = inspect.signature(AttributeBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::noattributeblock_is_not_abstract():
    assert not inspect.isabstract(limp::NoAttributeBlock)


def test_limp::noattributeblock_constructor_exists():
    assert callable(limp::NoAttributeBlock.__init__)


def test_limp::noattributeblock_constructor_args():
    sig = inspect.signature(limp::NoAttributeBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::someattributeblock_is_not_abstract():
    assert not inspect.isabstract(limp::SomeAttributeBlock)


def test_limp::someattributeblock_constructor_exists():
    assert callable(limp::SomeAttributeBlock.__init__)


def test_limp::someattributeblock_constructor_args():
    sig = inspect.signature(limp::SomeAttributeBlock.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_limp::recordtype_is_not_abstract():
    assert not inspect.isabstract(limp::RecordType)


def test_limp::recordtype_constructor_exists():
    assert callable(limp::RecordType.__init__)


def test_limp::recordtype_constructor_args():
    sig = inspect.signature(limp::RecordType.__init__)
    params = list(sig.parameters.keys())



def test_limp::arraytype_is_not_abstract():
    assert not inspect.isabstract(limp::ArrayType)


def test_limp::arraytype_constructor_exists():
    assert callable(limp::ArrayType.__init__)


def test_limp::arraytype_constructor_args():
    sig = inspect.signature(limp::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_limp::realtype_is_not_abstract():
    assert not inspect.isabstract(limp::RealType)


def test_limp::realtype_constructor_exists():
    assert callable(limp::RealType.__init__)


def test_limp::realtype_constructor_args():
    sig = inspect.signature(limp::RealType.__init__)
    params = list(sig.parameters.keys())



def test_limp::stringtype_is_not_abstract():
    assert not inspect.isabstract(limp::StringType)


def test_limp::stringtype_constructor_exists():
    assert callable(limp::StringType.__init__)


def test_limp::stringtype_constructor_args():
    sig = inspect.signature(limp::StringType.__init__)
    params = list(sig.parameters.keys())



def test_limp::enumtype_is_not_abstract():
    assert not inspect.isabstract(limp::EnumType)


def test_limp::enumtype_constructor_exists():
    assert callable(limp::EnumType.__init__)


def test_limp::enumtype_constructor_args():
    sig = inspect.signature(limp::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_limp::booltype_is_not_abstract():
    assert not inspect.isabstract(limp::BoolType)


def test_limp::booltype_constructor_exists():
    assert callable(limp::BoolType.__init__)


def test_limp::booltype_constructor_args():
    sig = inspect.signature(limp::BoolType.__init__)
    params = list(sig.parameters.keys())



def test_limp::tupletype_is_not_abstract():
    assert not inspect.isabstract(limp::TupleType)


def test_limp::tupletype_constructor_exists():
    assert callable(limp::TupleType.__init__)


def test_limp::tupletype_constructor_args():
    sig = inspect.signature(limp::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_limp::integertype_is_not_abstract():
    assert not inspect.isabstract(limp::IntegerType)


def test_limp::integertype_constructor_exists():
    assert callable(limp::IntegerType.__init__)


def test_limp::integertype_constructor_args():
    sig = inspect.signature(limp::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_limp::voidtype_is_not_abstract():
    assert not inspect.isabstract(limp::VoidType)


def test_limp::voidtype_constructor_exists():
    assert callable(limp::VoidType.__init__)


def test_limp::voidtype_constructor_args():
    sig = inspect.signature(limp::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_varblock_is_not_abstract():
    assert not inspect.isabstract(VarBlock)


def test_varblock_constructor_exists():
    assert callable(VarBlock.__init__)


def test_varblock_constructor_args():
    sig = inspect.signature(VarBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::novarblock_is_not_abstract():
    assert not inspect.isabstract(limp::NoVarBlock)


def test_limp::novarblock_constructor_exists():
    assert callable(limp::NoVarBlock.__init__)


def test_limp::novarblock_constructor_args():
    sig = inspect.signature(limp::NoVarBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::somevarblock_is_not_abstract():
    assert not inspect.isabstract(limp::SomeVarBlock)


def test_limp::somevarblock_constructor_exists():
    assert callable(limp::SomeVarBlock.__init__)


def test_limp::somevarblock_constructor_args():
    sig = inspect.signature(limp::SomeVarBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::exprlist_is_not_abstract():
    assert not inspect.isabstract(limp::ExprList)


def test_limp::exprlist_constructor_exists():
    assert callable(limp::ExprList.__init__)


def test_limp::exprlist_constructor_args():
    sig = inspect.signature(limp::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_limp::namedtype_is_not_abstract():
    assert not inspect.isabstract(limp::NamedType)


def test_limp::namedtype_constructor_exists():
    assert callable(limp::NamedType.__init__)


def test_limp::namedtype_constructor_args():
    sig = inspect.signature(limp::NamedType.__init__)
    params = list(sig.parameters.keys())



def test_limp::abstracttype_is_not_abstract():
    assert not inspect.isabstract(limp::AbstractType)


def test_limp::abstracttype_constructor_exists():
    assert callable(limp::AbstractType.__init__)


def test_limp::abstracttype_constructor_args():
    sig = inspect.signature(limp::AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_limp::ifthenelseexpr_is_not_abstract():
    assert not inspect.isabstract(limp::IfThenElseExpr)


def test_limp::ifthenelseexpr_constructor_exists():
    assert callable(limp::IfThenElseExpr.__init__)


def test_limp::ifthenelseexpr_constructor_args():
    sig = inspect.signature(limp::IfThenElseExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::initexpr_is_not_abstract():
    assert not inspect.isabstract(limp::InitExpr)


def test_limp::initexpr_constructor_exists():
    assert callable(limp::InitExpr.__init__)


def test_limp::initexpr_constructor_args():
    sig = inspect.signature(limp::InitExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::binaryexpr_is_not_abstract():
    assert not inspect.isabstract(limp::BinaryExpr)


def test_limp::binaryexpr_constructor_exists():
    assert callable(limp::BinaryExpr.__init__)


def test_limp::binaryexpr_constructor_args():
    sig = inspect.signature(limp::BinaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_limp::binaryexpr_has_op():
    assert hasattr(limp::BinaryExpr, "op")
    descriptor = None
    for klass in limp::BinaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_limp::freshvariable_is_not_abstract():
    assert not inspect.isabstract(limp::FreshVariable)


def test_limp::freshvariable_constructor_exists():
    assert callable(limp::FreshVariable.__init__)


def test_limp::freshvariable_constructor_args():
    sig = inspect.signature(limp::FreshVariable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_limp::freshvariable_has_value():
    assert hasattr(limp::FreshVariable, "value")
    descriptor = None
    for klass in limp::FreshVariable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_limp::recordupdateexpr_is_not_abstract():
    assert not inspect.isabstract(limp::RecordUpdateExpr)


def test_limp::recordupdateexpr_constructor_exists():
    assert callable(limp::RecordUpdateExpr.__init__)


def test_limp::recordupdateexpr_constructor_args():
    sig = inspect.signature(limp::RecordUpdateExpr.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_limp::recordupdateexpr_has_field():
    assert hasattr(limp::RecordUpdateExpr, "field")
    descriptor = None
    for klass in limp::RecordUpdateExpr.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_limp::fcncallexpr_is_not_abstract():
    assert not inspect.isabstract(limp::FcnCallExpr)


def test_limp::fcncallexpr_constructor_exists():
    assert callable(limp::FcnCallExpr.__init__)


def test_limp::fcncallexpr_constructor_args():
    sig = inspect.signature(limp::FcnCallExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::unarynegationexpr_is_not_abstract():
    assert not inspect.isabstract(limp::UnaryNegationExpr)


def test_limp::unarynegationexpr_constructor_exists():
    assert callable(limp::UnaryNegationExpr.__init__)


def test_limp::unarynegationexpr_constructor_args():
    sig = inspect.signature(limp::UnaryNegationExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::choiceexpr_is_not_abstract():
    assert not inspect.isabstract(limp::ChoiceExpr)


def test_limp::choiceexpr_constructor_exists():
    assert callable(limp::ChoiceExpr.__init__)


def test_limp::choiceexpr_constructor_args():
    sig = inspect.signature(limp::ChoiceExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::integerliteralexpr_is_not_abstract():
    assert not inspect.isabstract(limp::IntegerLiteralExpr)


def test_limp::integerliteralexpr_constructor_exists():
    assert callable(limp::IntegerLiteralExpr.__init__)


def test_limp::integerliteralexpr_constructor_args():
    sig = inspect.signature(limp::IntegerLiteralExpr.__init__)
    params = list(sig.parameters.keys())
    assert "intVal" in params, "Missing parameter 'intVal'"

def test_limp::integerliteralexpr_has_intVal():
    assert hasattr(limp::IntegerLiteralExpr, "intVal")
    descriptor = None
    for klass in limp::IntegerLiteralExpr.__mro__:
        if "intVal" in klass.__dict__:
            descriptor = klass.__dict__["intVal"]
            break
    assert isinstance(descriptor, property)



def test_limp::arrayupdateexpr_is_not_abstract():
    assert not inspect.isabstract(limp::ArrayUpdateExpr)


def test_limp::arrayupdateexpr_constructor_exists():
    assert callable(limp::ArrayUpdateExpr.__init__)


def test_limp::arrayupdateexpr_constructor_args():
    sig = inspect.signature(limp::ArrayUpdateExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::recordaccessexpr_is_not_abstract():
    assert not inspect.isabstract(limp::RecordAccessExpr)


def test_limp::recordaccessexpr_constructor_exists():
    assert callable(limp::RecordAccessExpr.__init__)


def test_limp::recordaccessexpr_constructor_args():
    sig = inspect.signature(limp::RecordAccessExpr.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_limp::recordaccessexpr_has_field():
    assert hasattr(limp::RecordAccessExpr, "field")
    descriptor = None
    for klass in limp::RecordAccessExpr.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_limp::unaryminusexpr_is_not_abstract():
    assert not inspect.isabstract(limp::UnaryMinusExpr)


def test_limp::unaryminusexpr_constructor_exists():
    assert callable(limp::UnaryMinusExpr.__init__)


def test_limp::unaryminusexpr_constructor_args():
    sig = inspect.signature(limp::UnaryMinusExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::booleanliteralexpr_is_not_abstract():
    assert not inspect.isabstract(limp::BooleanLiteralExpr)


def test_limp::booleanliteralexpr_constructor_exists():
    assert callable(limp::BooleanLiteralExpr.__init__)


def test_limp::booleanliteralexpr_constructor_args():
    sig = inspect.signature(limp::BooleanLiteralExpr.__init__)
    params = list(sig.parameters.keys())
    assert "boolVal" in params, "Missing parameter 'boolVal'"

def test_limp::booleanliteralexpr_has_boolVal():
    assert hasattr(limp::BooleanLiteralExpr, "boolVal")
    descriptor = None
    for klass in limp::BooleanLiteralExpr.__mro__:
        if "boolVal" in klass.__dict__:
            descriptor = klass.__dict__["boolVal"]
            break
    assert isinstance(descriptor, property)



def test_limp::idexpr_is_not_abstract():
    assert not inspect.isabstract(limp::IdExpr)


def test_limp::idexpr_constructor_exists():
    assert callable(limp::IdExpr.__init__)


def test_limp::idexpr_constructor_args():
    sig = inspect.signature(limp::IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::secondinit_is_not_abstract():
    assert not inspect.isabstract(limp::SecondInit)


def test_limp::secondinit_constructor_exists():
    assert callable(limp::SecondInit.__init__)


def test_limp::secondinit_constructor_args():
    sig = inspect.signature(limp::SecondInit.__init__)
    params = list(sig.parameters.keys())



def test_limp::arrayaccessexpr_is_not_abstract():
    assert not inspect.isabstract(limp::ArrayAccessExpr)


def test_limp::arrayaccessexpr_constructor_exists():
    assert callable(limp::ArrayAccessExpr.__init__)


def test_limp::arrayaccessexpr_constructor_args():
    sig = inspect.signature(limp::ArrayAccessExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::realliteralexpr_is_not_abstract():
    assert not inspect.isabstract(limp::RealLiteralExpr)


def test_limp::realliteralexpr_constructor_exists():
    assert callable(limp::RealLiteralExpr.__init__)


def test_limp::realliteralexpr_constructor_args():
    sig = inspect.signature(limp::RealLiteralExpr.__init__)
    params = list(sig.parameters.keys())
    assert "realVal" in params, "Missing parameter 'realVal'"

def test_limp::realliteralexpr_has_realVal():
    assert hasattr(limp::RealLiteralExpr, "realVal")
    descriptor = None
    for klass in limp::RealLiteralExpr.__mro__:
        if "realVal" in klass.__dict__:
            descriptor = klass.__dict__["realVal"]
            break
    assert isinstance(descriptor, property)



def test_limp::stringliteralexpr_is_not_abstract():
    assert not inspect.isabstract(limp::StringLiteralExpr)


def test_limp::stringliteralexpr_constructor_exists():
    assert callable(limp::StringLiteralExpr.__init__)


def test_limp::stringliteralexpr_constructor_args():
    sig = inspect.signature(limp::StringLiteralExpr.__init__)
    params = list(sig.parameters.keys())
    assert "stringVal" in params, "Missing parameter 'stringVal'"

def test_limp::stringliteralexpr_has_stringVal():
    assert hasattr(limp::StringLiteralExpr, "stringVal")
    descriptor = None
    for klass in limp::StringLiteralExpr.__mro__:
        if "stringVal" in klass.__dict__:
            descriptor = klass.__dict__["stringVal"]
            break
    assert isinstance(descriptor, property)



def test_limp::integerwildcardexpr_is_not_abstract():
    assert not inspect.isabstract(limp::IntegerWildCardExpr)


def test_limp::integerwildcardexpr_constructor_exists():
    assert callable(limp::IntegerWildCardExpr.__init__)


def test_limp::integerwildcardexpr_constructor_args():
    sig = inspect.signature(limp::IntegerWildCardExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::arrayexpr_is_not_abstract():
    assert not inspect.isabstract(limp::ArrayExpr)


def test_limp::arrayexpr_constructor_exists():
    assert callable(limp::ArrayExpr.__init__)


def test_limp::arrayexpr_constructor_args():
    sig = inspect.signature(limp::ArrayExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::functionref_is_not_abstract():
    assert not inspect.isabstract(limp::FunctionRef)


def test_limp::functionref_constructor_exists():
    assert callable(limp::FunctionRef.__init__)


def test_limp::functionref_constructor_args():
    sig = inspect.signature(limp::FunctionRef.__init__)
    params = list(sig.parameters.keys())



def test_limp::equation_is_not_abstract():
    assert not inspect.isabstract(limp::Equation)


def test_limp::equation_constructor_exists():
    assert callable(limp::Equation.__init__)


def test_limp::equation_constructor_args():
    sig = inspect.signature(limp::Equation.__init__)
    params = list(sig.parameters.keys())



def test_limp::recordfieldexpr_is_not_abstract():
    assert not inspect.isabstract(limp::RecordFieldExpr)


def test_limp::recordfieldexpr_constructor_exists():
    assert callable(limp::RecordFieldExpr.__init__)


def test_limp::recordfieldexpr_constructor_args():
    sig = inspect.signature(limp::RecordFieldExpr.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_limp::recordfieldexpr_has_fieldName():
    assert hasattr(limp::RecordFieldExpr, "fieldName")
    descriptor = None
    for klass in limp::RecordFieldExpr.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_limp::recordexpr_is_not_abstract():
    assert not inspect.isabstract(limp::RecordExpr)


def test_limp::recordexpr_constructor_exists():
    assert callable(limp::RecordExpr.__init__)


def test_limp::recordexpr_constructor_args():
    sig = inspect.signature(limp::RecordExpr.__init__)
    params = list(sig.parameters.keys())



def test_limp::idlist_is_not_abstract():
    assert not inspect.isabstract(limp::IdList)


def test_limp::idlist_constructor_exists():
    assert callable(limp::IdList.__init__)


def test_limp::idlist_constructor_args():
    sig = inspect.signature(limp::IdList.__init__)
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



def test_limp::returnstatement_is_not_abstract():
    assert not inspect.isabstract(limp::ReturnStatement)


def test_limp::returnstatement_constructor_exists():
    assert callable(limp::ReturnStatement.__init__)


def test_limp::returnstatement_constructor_args():
    sig = inspect.signature(limp::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::gotostatement_is_not_abstract():
    assert not inspect.isabstract(limp::GotoStatement)


def test_limp::gotostatement_constructor_exists():
    assert callable(limp::GotoStatement.__init__)


def test_limp::gotostatement_constructor_args():
    sig = inspect.signature(limp::GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(limp::AssignmentStatement)


def test_limp::assignmentstatement_constructor_exists():
    assert callable(limp::AssignmentStatement.__init__)


def test_limp::assignmentstatement_constructor_args():
    sig = inspect.signature(limp::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::ifthenelsestatement_is_not_abstract():
    assert not inspect.isabstract(limp::IfThenElseStatement)


def test_limp::ifthenelsestatement_constructor_exists():
    assert callable(limp::IfThenElseStatement.__init__)


def test_limp::ifthenelsestatement_constructor_args():
    sig = inspect.signature(limp::IfThenElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::labelstatement_is_not_abstract():
    assert not inspect.isabstract(limp::LabelStatement)


def test_limp::labelstatement_constructor_exists():
    assert callable(limp::LabelStatement.__init__)


def test_limp::labelstatement_constructor_args():
    sig = inspect.signature(limp::LabelStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::labelstatement_has_name():
    assert hasattr(limp::LabelStatement, "name")
    descriptor = None
    for klass in limp::LabelStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp::forstatement_is_not_abstract():
    assert not inspect.isabstract(limp::ForStatement)


def test_limp::forstatement_constructor_exists():
    assert callable(limp::ForStatement.__init__)


def test_limp::forstatement_constructor_args():
    sig = inspect.signature(limp::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::continuestatement_is_not_abstract():
    assert not inspect.isabstract(limp::ContinueStatement)


def test_limp::continuestatement_constructor_exists():
    assert callable(limp::ContinueStatement.__init__)


def test_limp::continuestatement_constructor_args():
    sig = inspect.signature(limp::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::breakstatement_is_not_abstract():
    assert not inspect.isabstract(limp::BreakStatement)


def test_limp::breakstatement_constructor_exists():
    assert callable(limp::BreakStatement.__init__)


def test_limp::breakstatement_constructor_args():
    sig = inspect.signature(limp::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::voidstatement_is_not_abstract():
    assert not inspect.isabstract(limp::VoidStatement)


def test_limp::voidstatement_constructor_exists():
    assert callable(limp::VoidStatement.__init__)


def test_limp::voidstatement_constructor_args():
    sig = inspect.signature(limp::VoidStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::statement_is_not_abstract():
    assert not inspect.isabstract(limp::Statement)


def test_limp::statement_constructor_exists():
    assert callable(limp::Statement.__init__)


def test_limp::statement_constructor_args():
    sig = inspect.signature(limp::Statement.__init__)
    params = list(sig.parameters.keys())



def test_limp::defineuseref_is_not_abstract():
    assert not inspect.isabstract(limp::DefineUseRef)


def test_limp::defineuseref_constructor_exists():
    assert callable(limp::DefineUseRef.__init__)


def test_limp::defineuseref_constructor_args():
    sig = inspect.signature(limp::DefineUseRef.__init__)
    params = list(sig.parameters.keys())



def test_limp::whilestatement_is_not_abstract():
    assert not inspect.isabstract(limp::WhileStatement)


def test_limp::whilestatement_constructor_exists():
    assert callable(limp::WhileStatement.__init__)


def test_limp::whilestatement_constructor_args():
    sig = inspect.signature(limp::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_limp::else_is_not_abstract():
    assert not inspect.isabstract(limp::Else)


def test_limp::else_constructor_exists():
    assert callable(limp::Else.__init__)


def test_limp::else_constructor_args():
    sig = inspect.signature(limp::Else.__init__)
    params = list(sig.parameters.keys())



def test_limp::variableref_is_not_abstract():
    assert not inspect.isabstract(limp::VariableRef)


def test_limp::variableref_constructor_exists():
    assert callable(limp::VariableRef.__init__)


def test_limp::variableref_constructor_args():
    sig = inspect.signature(limp::VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::variableref_has_name():
    assert hasattr(limp::VariableRef, "name")
    descriptor = None
    for klass in limp::VariableRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp::expr_is_not_abstract():
    assert not inspect.isabstract(limp::Expr)


def test_limp::expr_constructor_exists():
    assert callable(limp::Expr.__init__)


def test_limp::expr_constructor_args():
    sig = inspect.signature(limp::Expr.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_limp::uses_is_not_abstract():
    assert not inspect.isabstract(limp::Uses)


def test_limp::uses_constructor_exists():
    assert callable(limp::Uses.__init__)


def test_limp::uses_constructor_args():
    sig = inspect.signature(limp::Uses.__init__)
    params = list(sig.parameters.keys())



def test_limp::define_is_not_abstract():
    assert not inspect.isabstract(limp::Define)


def test_limp::define_constructor_exists():
    assert callable(limp::Define.__init__)


def test_limp::define_constructor_args():
    sig = inspect.signature(limp::Define.__init__)
    params = list(sig.parameters.keys())



def test_limp::postcondition_is_not_abstract():
    assert not inspect.isabstract(limp::Postcondition)


def test_limp::postcondition_constructor_exists():
    assert callable(limp::Postcondition.__init__)


def test_limp::postcondition_constructor_args():
    sig = inspect.signature(limp::Postcondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::postcondition_has_name():
    assert hasattr(limp::Postcondition, "name")
    descriptor = None
    for klass in limp::Postcondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp::precondition_is_not_abstract():
    assert not inspect.isabstract(limp::Precondition)


def test_limp::precondition_constructor_exists():
    assert callable(limp::Precondition.__init__)


def test_limp::precondition_constructor_args():
    sig = inspect.signature(limp::Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::precondition_has_name():
    assert hasattr(limp::Precondition, "name")
    descriptor = None
    for klass in limp::Precondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp::attribute_is_not_abstract():
    assert not inspect.isabstract(limp::Attribute)


def test_limp::attribute_constructor_exists():
    assert callable(limp::Attribute.__init__)


def test_limp::attribute_constructor_args():
    sig = inspect.signature(limp::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_limp::recordfieldtype_is_not_abstract():
    assert not inspect.isabstract(limp::RecordFieldType)


def test_limp::recordfieldtype_constructor_exists():
    assert callable(limp::RecordFieldType.__init__)


def test_limp::recordfieldtype_constructor_args():
    sig = inspect.signature(limp::RecordFieldType.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_limp::recordfieldtype_has_fieldName():
    assert hasattr(limp::RecordFieldType, "fieldName")
    descriptor = None
    for klass in limp::RecordFieldType.__mro__:
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



def test_limp::localarg_is_not_abstract():
    assert not inspect.isabstract(limp::LocalArg)


def test_limp::localarg_constructor_exists():
    assert callable(limp::LocalArg.__init__)


def test_limp::localarg_constructor_args():
    sig = inspect.signature(limp::LocalArg.__init__)
    params = list(sig.parameters.keys())



def test_limp::inputarg_is_not_abstract():
    assert not inspect.isabstract(limp::InputArg)


def test_limp::inputarg_constructor_exists():
    assert callable(limp::InputArg.__init__)


def test_limp::inputarg_constructor_args():
    sig = inspect.signature(limp::InputArg.__init__)
    params = list(sig.parameters.keys())



def test_limp::enumvalue_is_not_abstract():
    assert not inspect.isabstract(limp::EnumValue)


def test_limp::enumvalue_constructor_exists():
    assert callable(limp::EnumValue.__init__)


def test_limp::enumvalue_constructor_args():
    sig = inspect.signature(limp::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_limp::typealias_is_not_abstract():
    assert not inspect.isabstract(limp::TypeAlias)


def test_limp::typealias_constructor_exists():
    assert callable(limp::TypeAlias.__init__)


def test_limp::typealias_constructor_args():
    sig = inspect.signature(limp::TypeAlias.__init__)
    params = list(sig.parameters.keys())



def test_limp::recordtypedef_is_not_abstract():
    assert not inspect.isabstract(limp::RecordTypeDef)


def test_limp::recordtypedef_constructor_exists():
    assert callable(limp::RecordTypeDef.__init__)


def test_limp::recordtypedef_constructor_args():
    sig = inspect.signature(limp::RecordTypeDef.__init__)
    params = list(sig.parameters.keys())



def test_limp::enumtypedef_is_not_abstract():
    assert not inspect.isabstract(limp::EnumTypeDef)


def test_limp::enumtypedef_constructor_exists():
    assert callable(limp::EnumTypeDef.__init__)


def test_limp::enumtypedef_constructor_args():
    sig = inspect.signature(limp::EnumTypeDef.__init__)
    params = list(sig.parameters.keys())



def test_limp::statementblock_is_not_abstract():
    assert not inspect.isabstract(limp::StatementBlock)


def test_limp::statementblock_constructor_exists():
    assert callable(limp::StatementBlock.__init__)


def test_limp::statementblock_constructor_args():
    sig = inspect.signature(limp::StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::equationblock_is_not_abstract():
    assert not inspect.isabstract(limp::EquationBlock)


def test_limp::equationblock_constructor_exists():
    assert callable(limp::EquationBlock.__init__)


def test_limp::equationblock_constructor_args():
    sig = inspect.signature(limp::EquationBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::abstracttypedef_is_not_abstract():
    assert not inspect.isabstract(limp::AbstractTypeDef)


def test_limp::abstracttypedef_constructor_exists():
    assert callable(limp::AbstractTypeDef.__init__)


def test_limp::abstracttypedef_constructor_args():
    sig = inspect.signature(limp::AbstractTypeDef.__init__)
    params = list(sig.parameters.keys())



def test_limp::type_is_not_abstract():
    assert not inspect.isabstract(limp::Type)


def test_limp::type_constructor_exists():
    assert callable(limp::Type.__init__)


def test_limp::type_constructor_args():
    sig = inspect.signature(limp::Type.__init__)
    params = list(sig.parameters.keys())



def test_limp::arraytypedef_is_not_abstract():
    assert not inspect.isabstract(limp::ArrayTypeDef)


def test_limp::arraytypedef_constructor_exists():
    assert callable(limp::ArrayTypeDef.__init__)


def test_limp::arraytypedef_constructor_args():
    sig = inspect.signature(limp::ArrayTypeDef.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_limp::arraytypedef_has_size():
    assert hasattr(limp::ArrayTypeDef, "size")
    descriptor = None
    for klass in limp::ArrayTypeDef.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_limp::attributeblock_is_not_abstract():
    assert not inspect.isabstract(limp::AttributeBlock)


def test_limp::attributeblock_constructor_exists():
    assert callable(limp::AttributeBlock.__init__)


def test_limp::attributeblock_constructor_args():
    sig = inspect.signature(limp::AttributeBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::outputarglist_is_not_abstract():
    assert not inspect.isabstract(limp::OutputArgList)


def test_limp::outputarglist_constructor_exists():
    assert callable(limp::OutputArgList.__init__)


def test_limp::outputarglist_constructor_args():
    sig = inspect.signature(limp::OutputArgList.__init__)
    params = list(sig.parameters.keys())



def test_limp::outputarg_is_not_abstract():
    assert not inspect.isabstract(limp::OutputArg)


def test_limp::outputarg_constructor_exists():
    assert callable(limp::OutputArg.__init__)


def test_limp::outputarg_constructor_args():
    sig = inspect.signature(limp::OutputArg.__init__)
    params = list(sig.parameters.keys())



def test_limp::inputarglist_is_not_abstract():
    assert not inspect.isabstract(limp::InputArgList)


def test_limp::inputarglist_constructor_exists():
    assert callable(limp::InputArgList.__init__)


def test_limp::inputarglist_constructor_args():
    sig = inspect.signature(limp::InputArgList.__init__)
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



def test_limp::externalprocedure_is_not_abstract():
    assert not inspect.isabstract(limp::ExternalProcedure)


def test_limp::externalprocedure_constructor_exists():
    assert callable(limp::ExternalProcedure.__init__)


def test_limp::externalprocedure_constructor_args():
    sig = inspect.signature(limp::ExternalProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::externalprocedure_has_name():
    assert hasattr(limp::ExternalProcedure, "name")
    descriptor = None
    for klass in limp::ExternalProcedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp::localprocedure_is_not_abstract():
    assert not inspect.isabstract(limp::LocalProcedure)


def test_limp::localprocedure_constructor_exists():
    assert callable(limp::LocalProcedure.__init__)


def test_limp::localprocedure_constructor_args():
    sig = inspect.signature(limp::LocalProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::localprocedure_has_name():
    assert hasattr(limp::LocalProcedure, "name")
    descriptor = None
    for klass in limp::LocalProcedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(limp::TypeDeclaration)


def test_limp::typedeclaration_constructor_exists():
    assert callable(limp::TypeDeclaration.__init__)


def test_limp::typedeclaration_constructor_args():
    sig = inspect.signature(limp::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::typedeclaration_has_name():
    assert hasattr(limp::TypeDeclaration, "name")
    descriptor = None
    for klass in limp::TypeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp::import_is_not_abstract():
    assert not inspect.isabstract(limp::Import)


def test_limp::import_constructor_exists():
    assert callable(limp::Import.__init__)


def test_limp::import_constructor_args():
    sig = inspect.signature(limp::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_limp::import_has_importURI():
    assert hasattr(limp::Import, "importURI")
    descriptor = None
    for klass in limp::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_limp::externalfunction_is_not_abstract():
    assert not inspect.isabstract(limp::ExternalFunction)


def test_limp::externalfunction_constructor_exists():
    assert callable(limp::ExternalFunction.__init__)


def test_limp::externalfunction_constructor_args():
    sig = inspect.signature(limp::ExternalFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::externalfunction_has_name():
    assert hasattr(limp::ExternalFunction, "name")
    descriptor = None
    for klass in limp::ExternalFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_limp::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(limp::ConstantDeclaration)


def test_limp::constantdeclaration_constructor_exists():
    assert callable(limp::ConstantDeclaration.__init__)


def test_limp::constantdeclaration_constructor_args():
    sig = inspect.signature(limp::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_limp::globaldeclaration_is_not_abstract():
    assert not inspect.isabstract(limp::GlobalDeclaration)


def test_limp::globaldeclaration_constructor_exists():
    assert callable(limp::GlobalDeclaration.__init__)


def test_limp::globaldeclaration_constructor_args():
    sig = inspect.signature(limp::GlobalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_limp::comment_is_not_abstract():
    assert not inspect.isabstract(limp::Comment)


def test_limp::comment_constructor_exists():
    assert callable(limp::Comment.__init__)


def test_limp::comment_constructor_args():
    sig = inspect.signature(limp::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_limp::comment_has_comment():
    assert hasattr(limp::Comment, "comment")
    descriptor = None
    for klass in limp::Comment.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_limp::declaration_is_not_abstract():
    assert not inspect.isabstract(limp::Declaration)


def test_limp::declaration_constructor_exists():
    assert callable(limp::Declaration.__init__)


def test_limp::declaration_constructor_args():
    sig = inspect.signature(limp::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_limp::specification_is_not_abstract():
    assert not inspect.isabstract(limp::Specification)


def test_limp::specification_constructor_exists():
    assert callable(limp::Specification.__init__)


def test_limp::specification_constructor_args():
    sig = inspect.signature(limp::Specification.__init__)
    params = list(sig.parameters.keys())



def test_limp::varblock_is_not_abstract():
    assert not inspect.isabstract(limp::VarBlock)


def test_limp::varblock_constructor_exists():
    assert callable(limp::VarBlock.__init__)


def test_limp::varblock_constructor_args():
    sig = inspect.signature(limp::VarBlock.__init__)
    params = list(sig.parameters.keys())



def test_limp::localfunction_is_not_abstract():
    assert not inspect.isabstract(limp::LocalFunction)


def test_limp::localfunction_constructor_exists():
    assert callable(limp::LocalFunction.__init__)


def test_limp::localfunction_constructor_args():
    sig = inspect.signature(limp::LocalFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_limp::localfunction_has_name():
    assert hasattr(limp::LocalFunction, "name")
    descriptor = None
    for klass in limp::LocalFunction.__mro__:
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
limp::NoElse_strategy = st.builds(
    limp::NoElse,
)
limp::ElseIf_strategy = st.builds(
    limp::ElseIf,
)
limp::ElseBlock_strategy = st.builds(
    limp::ElseBlock,
)
AttributeBlock_strategy = st.builds(
    AttributeBlock,
)
limp::NoAttributeBlock_strategy = st.builds(
    limp::NoAttributeBlock,
)
limp::SomeAttributeBlock_strategy = st.builds(
    limp::SomeAttributeBlock,
)
Type_strategy = st.builds(
    Type,
)
limp::RecordType_strategy = st.builds(
    limp::RecordType,
)
limp::ArrayType_strategy = st.builds(
    limp::ArrayType,
)
limp::RealType_strategy = st.builds(
    limp::RealType,
)
limp::StringType_strategy = st.builds(
    limp::StringType,
)
limp::EnumType_strategy = st.builds(
    limp::EnumType,
)
limp::BoolType_strategy = st.builds(
    limp::BoolType,
)
limp::TupleType_strategy = st.builds(
    limp::TupleType,
)
limp::IntegerType_strategy = st.builds(
    limp::IntegerType,
)
limp::VoidType_strategy = st.builds(
    limp::VoidType,
)
VarBlock_strategy = st.builds(
    VarBlock,
)
limp::NoVarBlock_strategy = st.builds(
    limp::NoVarBlock,
)
limp::SomeVarBlock_strategy = st.builds(
    limp::SomeVarBlock,
)
limp::ExprList_strategy = st.builds(
    limp::ExprList,
)
limp::NamedType_strategy = st.builds(
    limp::NamedType,
)
limp::AbstractType_strategy = st.builds(
    limp::AbstractType,
)
Expr_strategy = st.builds(
    Expr,
)
limp::IfThenElseExpr_strategy = st.builds(
    limp::IfThenElseExpr,
)
limp::InitExpr_strategy = st.builds(
    limp::InitExpr,
)
limp::BinaryExpr_strategy = st.builds(
    limp::BinaryExpr,
    op=
        safe_text
)
limp::FreshVariable_strategy = st.builds(
    limp::FreshVariable,
    value=
        safe_text
)
limp::RecordUpdateExpr_strategy = st.builds(
    limp::RecordUpdateExpr,
    field=
        safe_text
)
limp::FcnCallExpr_strategy = st.builds(
    limp::FcnCallExpr,
)
limp::UnaryNegationExpr_strategy = st.builds(
    limp::UnaryNegationExpr,
)
limp::ChoiceExpr_strategy = st.builds(
    limp::ChoiceExpr,
)
limp::IntegerLiteralExpr_strategy = st.builds(
    limp::IntegerLiteralExpr,
    intVal=
        safe_text
)
limp::ArrayUpdateExpr_strategy = st.builds(
    limp::ArrayUpdateExpr,
)
limp::RecordAccessExpr_strategy = st.builds(
    limp::RecordAccessExpr,
    field=
        safe_text
)
limp::UnaryMinusExpr_strategy = st.builds(
    limp::UnaryMinusExpr,
)
limp::BooleanLiteralExpr_strategy = st.builds(
    limp::BooleanLiteralExpr,
    boolVal=
        safe_text
)
limp::IdExpr_strategy = st.builds(
    limp::IdExpr,
)
limp::SecondInit_strategy = st.builds(
    limp::SecondInit,
)
limp::ArrayAccessExpr_strategy = st.builds(
    limp::ArrayAccessExpr,
)
limp::RealLiteralExpr_strategy = st.builds(
    limp::RealLiteralExpr,
    realVal=
        safe_text
)
limp::StringLiteralExpr_strategy = st.builds(
    limp::StringLiteralExpr,
    stringVal=
        safe_text
)
limp::IntegerWildCardExpr_strategy = st.builds(
    limp::IntegerWildCardExpr,
)
limp::ArrayExpr_strategy = st.builds(
    limp::ArrayExpr,
)
limp::FunctionRef_strategy = st.builds(
    limp::FunctionRef,
)
limp::Equation_strategy = st.builds(
    limp::Equation,
)
limp::RecordFieldExpr_strategy = st.builds(
    limp::RecordFieldExpr,
    fieldName=
        safe_text
)
limp::RecordExpr_strategy = st.builds(
    limp::RecordExpr,
)
limp::IdList_strategy = st.builds(
    limp::IdList,
)
Equation_strategy = st.builds(
    Equation,
)
Statement_strategy = st.builds(
    Statement,
)
limp::ReturnStatement_strategy = st.builds(
    limp::ReturnStatement,
)
limp::GotoStatement_strategy = st.builds(
    limp::GotoStatement,
)
limp::AssignmentStatement_strategy = st.builds(
    limp::AssignmentStatement,
)
limp::IfThenElseStatement_strategy = st.builds(
    limp::IfThenElseStatement,
)
limp::LabelStatement_strategy = st.builds(
    limp::LabelStatement,
    name=
        safe_text
)
limp::ForStatement_strategy = st.builds(
    limp::ForStatement,
)
limp::ContinueStatement_strategy = st.builds(
    limp::ContinueStatement,
)
limp::BreakStatement_strategy = st.builds(
    limp::BreakStatement,
)
limp::VoidStatement_strategy = st.builds(
    limp::VoidStatement,
)
limp::Statement_strategy = st.builds(
    limp::Statement,
)
limp::DefineUseRef_strategy = st.builds(
    limp::DefineUseRef,
)
limp::WhileStatement_strategy = st.builds(
    limp::WhileStatement,
)
limp::Else_strategy = st.builds(
    limp::Else,
)
limp::VariableRef_strategy = st.builds(
    limp::VariableRef,
    name=
        safe_text
)
limp::Expr_strategy = st.builds(
    limp::Expr,
)
Attribute_strategy = st.builds(
    Attribute,
)
limp::Uses_strategy = st.builds(
    limp::Uses,
)
limp::Define_strategy = st.builds(
    limp::Define,
)
limp::Postcondition_strategy = st.builds(
    limp::Postcondition,
    name=
        safe_text
)
limp::Precondition_strategy = st.builds(
    limp::Precondition,
    name=
        safe_text
)
limp::Attribute_strategy = st.builds(
    limp::Attribute,
)
limp::RecordFieldType_strategy = st.builds(
    limp::RecordFieldType,
    fieldName=
        safe_text
)
VariableRef_strategy = st.builds(
    VariableRef,
)
limp::LocalArg_strategy = st.builds(
    limp::LocalArg,
)
limp::InputArg_strategy = st.builds(
    limp::InputArg,
)
limp::EnumValue_strategy = st.builds(
    limp::EnumValue,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
limp::TypeAlias_strategy = st.builds(
    limp::TypeAlias,
)
limp::RecordTypeDef_strategy = st.builds(
    limp::RecordTypeDef,
)
limp::EnumTypeDef_strategy = st.builds(
    limp::EnumTypeDef,
)
limp::StatementBlock_strategy = st.builds(
    limp::StatementBlock,
)
limp::EquationBlock_strategy = st.builds(
    limp::EquationBlock,
)
limp::AbstractTypeDef_strategy = st.builds(
    limp::AbstractTypeDef,
)
limp::Type_strategy = st.builds(
    limp::Type,
)
limp::ArrayTypeDef_strategy = st.builds(
    limp::ArrayTypeDef,
    size=
        safe_text
)
limp::AttributeBlock_strategy = st.builds(
    limp::AttributeBlock,
)
limp::OutputArgList_strategy = st.builds(
    limp::OutputArgList,
)
limp::OutputArg_strategy = st.builds(
    limp::OutputArg,
)
limp::InputArgList_strategy = st.builds(
    limp::InputArgList,
)
FunctionRef_strategy = st.builds(
    FunctionRef,
)
Declaration_strategy = st.builds(
    Declaration,
)
limp::ExternalProcedure_strategy = st.builds(
    limp::ExternalProcedure,
    name=
        safe_text
)
limp::LocalProcedure_strategy = st.builds(
    limp::LocalProcedure,
    name=
        safe_text
)
limp::TypeDeclaration_strategy = st.builds(
    limp::TypeDeclaration,
    name=
        safe_text
)
limp::Import_strategy = st.builds(
    limp::Import,
    importURI=
        safe_text
)
limp::ExternalFunction_strategy = st.builds(
    limp::ExternalFunction,
    name=
        safe_text
)
limp::ConstantDeclaration_strategy = st.builds(
    limp::ConstantDeclaration,
)
limp::GlobalDeclaration_strategy = st.builds(
    limp::GlobalDeclaration,
)
limp::Comment_strategy = st.builds(
    limp::Comment,
    comment=
        safe_text
)
limp::Declaration_strategy = st.builds(
    limp::Declaration,
)
limp::Specification_strategy = st.builds(
    limp::Specification,
)
limp::VarBlock_strategy = st.builds(
    limp::VarBlock,
)
limp::LocalFunction_strategy = st.builds(
    limp::LocalFunction,
    name=
        safe_text
)

@given(instance=Else_strategy)
@settings(max_examples=50)
def test_else_instantiation(instance):
    assert isinstance(instance, Else)

@given(instance=limp::NoElse_strategy)
@settings(max_examples=50)
def test_limp::noelse_instantiation(instance):
    assert isinstance(instance, limp::NoElse)

@given(instance=limp::ElseIf_strategy)
@settings(max_examples=50)
def test_limp::elseif_instantiation(instance):
    assert isinstance(instance, limp::ElseIf)

@given(instance=limp::ElseBlock_strategy)
@settings(max_examples=50)
def test_limp::elseblock_instantiation(instance):
    assert isinstance(instance, limp::ElseBlock)

@given(instance=AttributeBlock_strategy)
@settings(max_examples=50)
def test_attributeblock_instantiation(instance):
    assert isinstance(instance, AttributeBlock)

@given(instance=limp::NoAttributeBlock_strategy)
@settings(max_examples=50)
def test_limp::noattributeblock_instantiation(instance):
    assert isinstance(instance, limp::NoAttributeBlock)

@given(instance=limp::SomeAttributeBlock_strategy)
@settings(max_examples=50)
def test_limp::someattributeblock_instantiation(instance):
    assert isinstance(instance, limp::SomeAttributeBlock)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=limp::RecordType_strategy)
@settings(max_examples=50)
def test_limp::recordtype_instantiation(instance):
    assert isinstance(instance, limp::RecordType)

@given(instance=limp::ArrayType_strategy)
@settings(max_examples=50)
def test_limp::arraytype_instantiation(instance):
    assert isinstance(instance, limp::ArrayType)

@given(instance=limp::RealType_strategy)
@settings(max_examples=50)
def test_limp::realtype_instantiation(instance):
    assert isinstance(instance, limp::RealType)

@given(instance=limp::StringType_strategy)
@settings(max_examples=50)
def test_limp::stringtype_instantiation(instance):
    assert isinstance(instance, limp::StringType)

@given(instance=limp::EnumType_strategy)
@settings(max_examples=50)
def test_limp::enumtype_instantiation(instance):
    assert isinstance(instance, limp::EnumType)

@given(instance=limp::BoolType_strategy)
@settings(max_examples=50)
def test_limp::booltype_instantiation(instance):
    assert isinstance(instance, limp::BoolType)

@given(instance=limp::TupleType_strategy)
@settings(max_examples=50)
def test_limp::tupletype_instantiation(instance):
    assert isinstance(instance, limp::TupleType)

@given(instance=limp::IntegerType_strategy)
@settings(max_examples=50)
def test_limp::integertype_instantiation(instance):
    assert isinstance(instance, limp::IntegerType)

@given(instance=limp::VoidType_strategy)
@settings(max_examples=50)
def test_limp::voidtype_instantiation(instance):
    assert isinstance(instance, limp::VoidType)

@given(instance=VarBlock_strategy)
@settings(max_examples=50)
def test_varblock_instantiation(instance):
    assert isinstance(instance, VarBlock)

@given(instance=limp::NoVarBlock_strategy)
@settings(max_examples=50)
def test_limp::novarblock_instantiation(instance):
    assert isinstance(instance, limp::NoVarBlock)

@given(instance=limp::SomeVarBlock_strategy)
@settings(max_examples=50)
def test_limp::somevarblock_instantiation(instance):
    assert isinstance(instance, limp::SomeVarBlock)

@given(instance=limp::ExprList_strategy)
@settings(max_examples=50)
def test_limp::exprlist_instantiation(instance):
    assert isinstance(instance, limp::ExprList)

@given(instance=limp::NamedType_strategy)
@settings(max_examples=50)
def test_limp::namedtype_instantiation(instance):
    assert isinstance(instance, limp::NamedType)

@given(instance=limp::AbstractType_strategy)
@settings(max_examples=50)
def test_limp::abstracttype_instantiation(instance):
    assert isinstance(instance, limp::AbstractType)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=limp::IfThenElseExpr_strategy)
@settings(max_examples=50)
def test_limp::ifthenelseexpr_instantiation(instance):
    assert isinstance(instance, limp::IfThenElseExpr)

@given(instance=limp::InitExpr_strategy)
@settings(max_examples=50)
def test_limp::initexpr_instantiation(instance):
    assert isinstance(instance, limp::InitExpr)

@given(instance=limp::BinaryExpr_strategy)
@settings(max_examples=50)
def test_limp::binaryexpr_instantiation(instance):
    assert isinstance(instance, limp::BinaryExpr)

@given(instance=limp::BinaryExpr_strategy)
def test_limp::binaryexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=limp::BinaryExpr_strategy)
def test_limp::binaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=limp::FreshVariable_strategy)
@settings(max_examples=50)
def test_limp::freshvariable_instantiation(instance):
    assert isinstance(instance, limp::FreshVariable)

@given(instance=limp::FreshVariable_strategy)
def test_limp::freshvariable_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=limp::FreshVariable_strategy)
def test_limp::freshvariable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=limp::RecordUpdateExpr_strategy)
@settings(max_examples=50)
def test_limp::recordupdateexpr_instantiation(instance):
    assert isinstance(instance, limp::RecordUpdateExpr)

@given(instance=limp::RecordUpdateExpr_strategy)
def test_limp::recordupdateexpr_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=limp::RecordUpdateExpr_strategy)
def test_limp::recordupdateexpr_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=limp::FcnCallExpr_strategy)
@settings(max_examples=50)
def test_limp::fcncallexpr_instantiation(instance):
    assert isinstance(instance, limp::FcnCallExpr)

@given(instance=limp::UnaryNegationExpr_strategy)
@settings(max_examples=50)
def test_limp::unarynegationexpr_instantiation(instance):
    assert isinstance(instance, limp::UnaryNegationExpr)

@given(instance=limp::ChoiceExpr_strategy)
@settings(max_examples=50)
def test_limp::choiceexpr_instantiation(instance):
    assert isinstance(instance, limp::ChoiceExpr)

@given(instance=limp::IntegerLiteralExpr_strategy)
@settings(max_examples=50)
def test_limp::integerliteralexpr_instantiation(instance):
    assert isinstance(instance, limp::IntegerLiteralExpr)

@given(instance=limp::IntegerLiteralExpr_strategy)
def test_limp::integerliteralexpr_intVal_type(instance):
    assert isinstance(instance.intVal, str)


@given(instance=limp::IntegerLiteralExpr_strategy)
def test_limp::integerliteralexpr_intVal_setter(instance):
    original = instance.intVal
    instance.intVal = original
    assert instance.intVal == original

@given(instance=limp::ArrayUpdateExpr_strategy)
@settings(max_examples=50)
def test_limp::arrayupdateexpr_instantiation(instance):
    assert isinstance(instance, limp::ArrayUpdateExpr)

@given(instance=limp::RecordAccessExpr_strategy)
@settings(max_examples=50)
def test_limp::recordaccessexpr_instantiation(instance):
    assert isinstance(instance, limp::RecordAccessExpr)

@given(instance=limp::RecordAccessExpr_strategy)
def test_limp::recordaccessexpr_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=limp::RecordAccessExpr_strategy)
def test_limp::recordaccessexpr_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=limp::UnaryMinusExpr_strategy)
@settings(max_examples=50)
def test_limp::unaryminusexpr_instantiation(instance):
    assert isinstance(instance, limp::UnaryMinusExpr)

@given(instance=limp::BooleanLiteralExpr_strategy)
@settings(max_examples=50)
def test_limp::booleanliteralexpr_instantiation(instance):
    assert isinstance(instance, limp::BooleanLiteralExpr)

@given(instance=limp::BooleanLiteralExpr_strategy)
def test_limp::booleanliteralexpr_boolVal_type(instance):
    assert isinstance(instance.boolVal, str)


@given(instance=limp::BooleanLiteralExpr_strategy)
def test_limp::booleanliteralexpr_boolVal_setter(instance):
    original = instance.boolVal
    instance.boolVal = original
    assert instance.boolVal == original

@given(instance=limp::IdExpr_strategy)
@settings(max_examples=50)
def test_limp::idexpr_instantiation(instance):
    assert isinstance(instance, limp::IdExpr)

@given(instance=limp::SecondInit_strategy)
@settings(max_examples=50)
def test_limp::secondinit_instantiation(instance):
    assert isinstance(instance, limp::SecondInit)

@given(instance=limp::ArrayAccessExpr_strategy)
@settings(max_examples=50)
def test_limp::arrayaccessexpr_instantiation(instance):
    assert isinstance(instance, limp::ArrayAccessExpr)

@given(instance=limp::RealLiteralExpr_strategy)
@settings(max_examples=50)
def test_limp::realliteralexpr_instantiation(instance):
    assert isinstance(instance, limp::RealLiteralExpr)

@given(instance=limp::RealLiteralExpr_strategy)
def test_limp::realliteralexpr_realVal_type(instance):
    assert isinstance(instance.realVal, str)


@given(instance=limp::RealLiteralExpr_strategy)
def test_limp::realliteralexpr_realVal_setter(instance):
    original = instance.realVal
    instance.realVal = original
    assert instance.realVal == original

@given(instance=limp::StringLiteralExpr_strategy)
@settings(max_examples=50)
def test_limp::stringliteralexpr_instantiation(instance):
    assert isinstance(instance, limp::StringLiteralExpr)

@given(instance=limp::StringLiteralExpr_strategy)
def test_limp::stringliteralexpr_stringVal_type(instance):
    assert isinstance(instance.stringVal, str)


@given(instance=limp::StringLiteralExpr_strategy)
def test_limp::stringliteralexpr_stringVal_setter(instance):
    original = instance.stringVal
    instance.stringVal = original
    assert instance.stringVal == original

@given(instance=limp::IntegerWildCardExpr_strategy)
@settings(max_examples=50)
def test_limp::integerwildcardexpr_instantiation(instance):
    assert isinstance(instance, limp::IntegerWildCardExpr)

@given(instance=limp::ArrayExpr_strategy)
@settings(max_examples=50)
def test_limp::arrayexpr_instantiation(instance):
    assert isinstance(instance, limp::ArrayExpr)

@given(instance=limp::FunctionRef_strategy)
@settings(max_examples=50)
def test_limp::functionref_instantiation(instance):
    assert isinstance(instance, limp::FunctionRef)

@given(instance=limp::Equation_strategy)
@settings(max_examples=50)
def test_limp::equation_instantiation(instance):
    assert isinstance(instance, limp::Equation)

@given(instance=limp::RecordFieldExpr_strategy)
@settings(max_examples=50)
def test_limp::recordfieldexpr_instantiation(instance):
    assert isinstance(instance, limp::RecordFieldExpr)

@given(instance=limp::RecordFieldExpr_strategy)
def test_limp::recordfieldexpr_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=limp::RecordFieldExpr_strategy)
def test_limp::recordfieldexpr_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=limp::RecordExpr_strategy)
@settings(max_examples=50)
def test_limp::recordexpr_instantiation(instance):
    assert isinstance(instance, limp::RecordExpr)

@given(instance=limp::IdList_strategy)
@settings(max_examples=50)
def test_limp::idlist_instantiation(instance):
    assert isinstance(instance, limp::IdList)

@given(instance=Equation_strategy)
@settings(max_examples=50)
def test_equation_instantiation(instance):
    assert isinstance(instance, Equation)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=limp::ReturnStatement_strategy)
@settings(max_examples=50)
def test_limp::returnstatement_instantiation(instance):
    assert isinstance(instance, limp::ReturnStatement)

@given(instance=limp::GotoStatement_strategy)
@settings(max_examples=50)
def test_limp::gotostatement_instantiation(instance):
    assert isinstance(instance, limp::GotoStatement)

@given(instance=limp::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_limp::assignmentstatement_instantiation(instance):
    assert isinstance(instance, limp::AssignmentStatement)

@given(instance=limp::IfThenElseStatement_strategy)
@settings(max_examples=50)
def test_limp::ifthenelsestatement_instantiation(instance):
    assert isinstance(instance, limp::IfThenElseStatement)

@given(instance=limp::LabelStatement_strategy)
@settings(max_examples=50)
def test_limp::labelstatement_instantiation(instance):
    assert isinstance(instance, limp::LabelStatement)

@given(instance=limp::LabelStatement_strategy)
def test_limp::labelstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::LabelStatement_strategy)
def test_limp::labelstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp::ForStatement_strategy)
@settings(max_examples=50)
def test_limp::forstatement_instantiation(instance):
    assert isinstance(instance, limp::ForStatement)

@given(instance=limp::ContinueStatement_strategy)
@settings(max_examples=50)
def test_limp::continuestatement_instantiation(instance):
    assert isinstance(instance, limp::ContinueStatement)

@given(instance=limp::BreakStatement_strategy)
@settings(max_examples=50)
def test_limp::breakstatement_instantiation(instance):
    assert isinstance(instance, limp::BreakStatement)

@given(instance=limp::VoidStatement_strategy)
@settings(max_examples=50)
def test_limp::voidstatement_instantiation(instance):
    assert isinstance(instance, limp::VoidStatement)

@given(instance=limp::Statement_strategy)
@settings(max_examples=50)
def test_limp::statement_instantiation(instance):
    assert isinstance(instance, limp::Statement)

@given(instance=limp::DefineUseRef_strategy)
@settings(max_examples=50)
def test_limp::defineuseref_instantiation(instance):
    assert isinstance(instance, limp::DefineUseRef)

@given(instance=limp::WhileStatement_strategy)
@settings(max_examples=50)
def test_limp::whilestatement_instantiation(instance):
    assert isinstance(instance, limp::WhileStatement)

@given(instance=limp::Else_strategy)
@settings(max_examples=50)
def test_limp::else_instantiation(instance):
    assert isinstance(instance, limp::Else)

@given(instance=limp::VariableRef_strategy)
@settings(max_examples=50)
def test_limp::variableref_instantiation(instance):
    assert isinstance(instance, limp::VariableRef)

@given(instance=limp::VariableRef_strategy)
def test_limp::variableref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::VariableRef_strategy)
def test_limp::variableref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp::Expr_strategy)
@settings(max_examples=50)
def test_limp::expr_instantiation(instance):
    assert isinstance(instance, limp::Expr)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=limp::Uses_strategy)
@settings(max_examples=50)
def test_limp::uses_instantiation(instance):
    assert isinstance(instance, limp::Uses)

@given(instance=limp::Define_strategy)
@settings(max_examples=50)
def test_limp::define_instantiation(instance):
    assert isinstance(instance, limp::Define)

@given(instance=limp::Postcondition_strategy)
@settings(max_examples=50)
def test_limp::postcondition_instantiation(instance):
    assert isinstance(instance, limp::Postcondition)

@given(instance=limp::Postcondition_strategy)
def test_limp::postcondition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::Postcondition_strategy)
def test_limp::postcondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp::Precondition_strategy)
@settings(max_examples=50)
def test_limp::precondition_instantiation(instance):
    assert isinstance(instance, limp::Precondition)

@given(instance=limp::Precondition_strategy)
def test_limp::precondition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::Precondition_strategy)
def test_limp::precondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp::Attribute_strategy)
@settings(max_examples=50)
def test_limp::attribute_instantiation(instance):
    assert isinstance(instance, limp::Attribute)

@given(instance=limp::RecordFieldType_strategy)
@settings(max_examples=50)
def test_limp::recordfieldtype_instantiation(instance):
    assert isinstance(instance, limp::RecordFieldType)

@given(instance=limp::RecordFieldType_strategy)
def test_limp::recordfieldtype_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=limp::RecordFieldType_strategy)
def test_limp::recordfieldtype_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=VariableRef_strategy)
@settings(max_examples=50)
def test_variableref_instantiation(instance):
    assert isinstance(instance, VariableRef)

@given(instance=limp::LocalArg_strategy)
@settings(max_examples=50)
def test_limp::localarg_instantiation(instance):
    assert isinstance(instance, limp::LocalArg)

@given(instance=limp::InputArg_strategy)
@settings(max_examples=50)
def test_limp::inputarg_instantiation(instance):
    assert isinstance(instance, limp::InputArg)

@given(instance=limp::EnumValue_strategy)
@settings(max_examples=50)
def test_limp::enumvalue_instantiation(instance):
    assert isinstance(instance, limp::EnumValue)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=limp::TypeAlias_strategy)
@settings(max_examples=50)
def test_limp::typealias_instantiation(instance):
    assert isinstance(instance, limp::TypeAlias)

@given(instance=limp::RecordTypeDef_strategy)
@settings(max_examples=50)
def test_limp::recordtypedef_instantiation(instance):
    assert isinstance(instance, limp::RecordTypeDef)

@given(instance=limp::EnumTypeDef_strategy)
@settings(max_examples=50)
def test_limp::enumtypedef_instantiation(instance):
    assert isinstance(instance, limp::EnumTypeDef)

@given(instance=limp::StatementBlock_strategy)
@settings(max_examples=50)
def test_limp::statementblock_instantiation(instance):
    assert isinstance(instance, limp::StatementBlock)

@given(instance=limp::EquationBlock_strategy)
@settings(max_examples=50)
def test_limp::equationblock_instantiation(instance):
    assert isinstance(instance, limp::EquationBlock)

@given(instance=limp::AbstractTypeDef_strategy)
@settings(max_examples=50)
def test_limp::abstracttypedef_instantiation(instance):
    assert isinstance(instance, limp::AbstractTypeDef)

@given(instance=limp::Type_strategy)
@settings(max_examples=50)
def test_limp::type_instantiation(instance):
    assert isinstance(instance, limp::Type)

@given(instance=limp::ArrayTypeDef_strategy)
@settings(max_examples=50)
def test_limp::arraytypedef_instantiation(instance):
    assert isinstance(instance, limp::ArrayTypeDef)

@given(instance=limp::ArrayTypeDef_strategy)
def test_limp::arraytypedef_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=limp::ArrayTypeDef_strategy)
def test_limp::arraytypedef_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=limp::AttributeBlock_strategy)
@settings(max_examples=50)
def test_limp::attributeblock_instantiation(instance):
    assert isinstance(instance, limp::AttributeBlock)

@given(instance=limp::OutputArgList_strategy)
@settings(max_examples=50)
def test_limp::outputarglist_instantiation(instance):
    assert isinstance(instance, limp::OutputArgList)

@given(instance=limp::OutputArg_strategy)
@settings(max_examples=50)
def test_limp::outputarg_instantiation(instance):
    assert isinstance(instance, limp::OutputArg)

@given(instance=limp::InputArgList_strategy)
@settings(max_examples=50)
def test_limp::inputarglist_instantiation(instance):
    assert isinstance(instance, limp::InputArgList)

@given(instance=FunctionRef_strategy)
@settings(max_examples=50)
def test_functionref_instantiation(instance):
    assert isinstance(instance, FunctionRef)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=limp::ExternalProcedure_strategy)
@settings(max_examples=50)
def test_limp::externalprocedure_instantiation(instance):
    assert isinstance(instance, limp::ExternalProcedure)

@given(instance=limp::ExternalProcedure_strategy)
def test_limp::externalprocedure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::ExternalProcedure_strategy)
def test_limp::externalprocedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp::LocalProcedure_strategy)
@settings(max_examples=50)
def test_limp::localprocedure_instantiation(instance):
    assert isinstance(instance, limp::LocalProcedure)

@given(instance=limp::LocalProcedure_strategy)
def test_limp::localprocedure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::LocalProcedure_strategy)
def test_limp::localprocedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_limp::typedeclaration_instantiation(instance):
    assert isinstance(instance, limp::TypeDeclaration)

@given(instance=limp::TypeDeclaration_strategy)
def test_limp::typedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::TypeDeclaration_strategy)
def test_limp::typedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp::Import_strategy)
@settings(max_examples=50)
def test_limp::import_instantiation(instance):
    assert isinstance(instance, limp::Import)

@given(instance=limp::Import_strategy)
def test_limp::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=limp::Import_strategy)
def test_limp::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=limp::ExternalFunction_strategy)
@settings(max_examples=50)
def test_limp::externalfunction_instantiation(instance):
    assert isinstance(instance, limp::ExternalFunction)

@given(instance=limp::ExternalFunction_strategy)
def test_limp::externalfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::ExternalFunction_strategy)
def test_limp::externalfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=limp::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_limp::constantdeclaration_instantiation(instance):
    assert isinstance(instance, limp::ConstantDeclaration)

@given(instance=limp::GlobalDeclaration_strategy)
@settings(max_examples=50)
def test_limp::globaldeclaration_instantiation(instance):
    assert isinstance(instance, limp::GlobalDeclaration)

@given(instance=limp::Comment_strategy)
@settings(max_examples=50)
def test_limp::comment_instantiation(instance):
    assert isinstance(instance, limp::Comment)

@given(instance=limp::Comment_strategy)
def test_limp::comment_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=limp::Comment_strategy)
def test_limp::comment_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=limp::Declaration_strategy)
@settings(max_examples=50)
def test_limp::declaration_instantiation(instance):
    assert isinstance(instance, limp::Declaration)

@given(instance=limp::Specification_strategy)
@settings(max_examples=50)
def test_limp::specification_instantiation(instance):
    assert isinstance(instance, limp::Specification)

@given(instance=limp::VarBlock_strategy)
@settings(max_examples=50)
def test_limp::varblock_instantiation(instance):
    assert isinstance(instance, limp::VarBlock)

@given(instance=limp::LocalFunction_strategy)
@settings(max_examples=50)
def test_limp::localfunction_instantiation(instance):
    assert isinstance(instance, limp::LocalFunction)

@given(instance=limp::LocalFunction_strategy)
def test_limp::localfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=limp::LocalFunction_strategy)
def test_limp::localfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
