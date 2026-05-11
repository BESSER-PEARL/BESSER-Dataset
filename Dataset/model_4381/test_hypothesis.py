import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Prefix,
    AffectationPrefixStatement,
    leek::PrefixIncrement,
    leek::PrefixDecrement,
    Postfix,
    AffectationPostfixStatement,
    leek::PostfixDecrement,
    leek::PostfixIncrement,
    ForInVariableReference,
    Expression,
    leek::IntLiteral,
    leek::FalseLiteral,
    leek::Multi,
    leek::TypedDifferent,
    leek::NullLiteral,
    leek::StringLiteral,
    leek::ArrayLiteral,
    leek::Equals,
    leek::Postfix,
    leek::Comparison,
    leek::RealLiteral,
    leek::Prefix,
    leek::Different,
    leek::TrueLiteral,
    leek::ForInVariableReference,
    leek::ForAffectation,
    leek::Script,
    leek::ForInitializer,
    Iteration,
    leek::ForIn,
    leek::For,
    leek::While,
    leek::IfCondition,
    leek::VariableReference,
    ForAffectation,
    ForInitializer,
    leek::VariableDeclaration,
    IfCondition,
    leek::Expression,
    AffectationStatement,
    leek::AffectationDecrement,
    leek::AffectationPrefixStatement,
    leek::AffectationIncrement,
    leek::AffectationPostfixStatement,
    leek::Affectation,
    Statement,
    leek::Include,
    leek::EmptyStatement,
    leek::FunctionCall,
    leek::Iteration,
    leek::ContinueStatement,
    leek::GlobalDeclaration,
    leek::AffectationStatement,
    leek::ReturnStatement,
    leek::If,
    leek::StatementBlock,
    leek::LocalDeclaration,
    leek::FunctionDeclaration,
    leek::BreakStatement,
    leek::Statement,
    leek::Not,
    leek::UnitaryMinus,
    leek::TernaryIf,
    leek::Div,
    leek::Minus,
    leek::Plus,
    leek::And,
    leek::Or,
    leek::More,
    leek::MoreOrEquals,
    leek::Less,
    leek::LessOrEquals,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prefix_is_not_abstract():
    assert not inspect.isabstract(Prefix)


def test_prefix_constructor_exists():
    assert callable(Prefix.__init__)


def test_prefix_constructor_args():
    sig = inspect.signature(Prefix.__init__)
    params = list(sig.parameters.keys())



def test_affectationprefixstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationPrefixStatement)


def test_affectationprefixstatement_constructor_exists():
    assert callable(AffectationPrefixStatement.__init__)


def test_affectationprefixstatement_constructor_args():
    sig = inspect.signature(AffectationPrefixStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::prefixincrement_is_not_abstract():
    assert not inspect.isabstract(leek::PrefixIncrement)


def test_leek::prefixincrement_constructor_exists():
    assert callable(leek::PrefixIncrement.__init__)


def test_leek::prefixincrement_constructor_args():
    sig = inspect.signature(leek::PrefixIncrement.__init__)
    params = list(sig.parameters.keys())



def test_leek::prefixdecrement_is_not_abstract():
    assert not inspect.isabstract(leek::PrefixDecrement)


def test_leek::prefixdecrement_constructor_exists():
    assert callable(leek::PrefixDecrement.__init__)


def test_leek::prefixdecrement_constructor_args():
    sig = inspect.signature(leek::PrefixDecrement.__init__)
    params = list(sig.parameters.keys())



def test_postfix_is_not_abstract():
    assert not inspect.isabstract(Postfix)


def test_postfix_constructor_exists():
    assert callable(Postfix.__init__)


def test_postfix_constructor_args():
    sig = inspect.signature(Postfix.__init__)
    params = list(sig.parameters.keys())



def test_affectationpostfixstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationPostfixStatement)


def test_affectationpostfixstatement_constructor_exists():
    assert callable(AffectationPostfixStatement.__init__)


def test_affectationpostfixstatement_constructor_args():
    sig = inspect.signature(AffectationPostfixStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::postfixdecrement_is_not_abstract():
    assert not inspect.isabstract(leek::PostfixDecrement)


def test_leek::postfixdecrement_constructor_exists():
    assert callable(leek::PostfixDecrement.__init__)


def test_leek::postfixdecrement_constructor_args():
    sig = inspect.signature(leek::PostfixDecrement.__init__)
    params = list(sig.parameters.keys())



def test_leek::postfixincrement_is_not_abstract():
    assert not inspect.isabstract(leek::PostfixIncrement)


def test_leek::postfixincrement_constructor_exists():
    assert callable(leek::PostfixIncrement.__init__)


def test_leek::postfixincrement_constructor_args():
    sig = inspect.signature(leek::PostfixIncrement.__init__)
    params = list(sig.parameters.keys())



def test_forinvariablereference_is_not_abstract():
    assert not inspect.isabstract(ForInVariableReference)


def test_forinvariablereference_constructor_exists():
    assert callable(ForInVariableReference.__init__)


def test_forinvariablereference_constructor_args():
    sig = inspect.signature(ForInVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_leek::intliteral_is_not_abstract():
    assert not inspect.isabstract(leek::IntLiteral)


def test_leek::intliteral_constructor_exists():
    assert callable(leek::IntLiteral.__init__)


def test_leek::intliteral_constructor_args():
    sig = inspect.signature(leek::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_leek::intliteral_has_value():
    assert hasattr(leek::IntLiteral, "value")
    descriptor = None
    for klass in leek::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_leek::falseliteral_is_not_abstract():
    assert not inspect.isabstract(leek::FalseLiteral)


def test_leek::falseliteral_constructor_exists():
    assert callable(leek::FalseLiteral.__init__)


def test_leek::falseliteral_constructor_args():
    sig = inspect.signature(leek::FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_leek::multi_is_not_abstract():
    assert not inspect.isabstract(leek::Multi)


def test_leek::multi_constructor_exists():
    assert callable(leek::Multi.__init__)


def test_leek::multi_constructor_args():
    sig = inspect.signature(leek::Multi.__init__)
    params = list(sig.parameters.keys())



def test_leek::typeddifferent_is_not_abstract():
    assert not inspect.isabstract(leek::TypedDifferent)


def test_leek::typeddifferent_constructor_exists():
    assert callable(leek::TypedDifferent.__init__)


def test_leek::typeddifferent_constructor_args():
    sig = inspect.signature(leek::TypedDifferent.__init__)
    params = list(sig.parameters.keys())



def test_leek::nullliteral_is_not_abstract():
    assert not inspect.isabstract(leek::NullLiteral)


def test_leek::nullliteral_constructor_exists():
    assert callable(leek::NullLiteral.__init__)


def test_leek::nullliteral_constructor_args():
    sig = inspect.signature(leek::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_leek::stringliteral_is_not_abstract():
    assert not inspect.isabstract(leek::StringLiteral)


def test_leek::stringliteral_constructor_exists():
    assert callable(leek::StringLiteral.__init__)


def test_leek::stringliteral_constructor_args():
    sig = inspect.signature(leek::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_leek::stringliteral_has_value():
    assert hasattr(leek::StringLiteral, "value")
    descriptor = None
    for klass in leek::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_leek::arrayliteral_is_not_abstract():
    assert not inspect.isabstract(leek::ArrayLiteral)


def test_leek::arrayliteral_constructor_exists():
    assert callable(leek::ArrayLiteral.__init__)


def test_leek::arrayliteral_constructor_args():
    sig = inspect.signature(leek::ArrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_leek::equals_is_not_abstract():
    assert not inspect.isabstract(leek::Equals)


def test_leek::equals_constructor_exists():
    assert callable(leek::Equals.__init__)


def test_leek::equals_constructor_args():
    sig = inspect.signature(leek::Equals.__init__)
    params = list(sig.parameters.keys())



def test_leek::postfix_is_not_abstract():
    assert not inspect.isabstract(leek::Postfix)


def test_leek::postfix_constructor_exists():
    assert callable(leek::Postfix.__init__)


def test_leek::postfix_constructor_args():
    sig = inspect.signature(leek::Postfix.__init__)
    params = list(sig.parameters.keys())



def test_leek::comparison_is_not_abstract():
    assert not inspect.isabstract(leek::Comparison)


def test_leek::comparison_constructor_exists():
    assert callable(leek::Comparison.__init__)


def test_leek::comparison_constructor_args():
    sig = inspect.signature(leek::Comparison.__init__)
    params = list(sig.parameters.keys())



def test_leek::realliteral_is_not_abstract():
    assert not inspect.isabstract(leek::RealLiteral)


def test_leek::realliteral_constructor_exists():
    assert callable(leek::RealLiteral.__init__)


def test_leek::realliteral_constructor_args():
    sig = inspect.signature(leek::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_leek::realliteral_has_value():
    assert hasattr(leek::RealLiteral, "value")
    descriptor = None
    for klass in leek::RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_leek::prefix_is_not_abstract():
    assert not inspect.isabstract(leek::Prefix)


def test_leek::prefix_constructor_exists():
    assert callable(leek::Prefix.__init__)


def test_leek::prefix_constructor_args():
    sig = inspect.signature(leek::Prefix.__init__)
    params = list(sig.parameters.keys())



def test_leek::different_is_not_abstract():
    assert not inspect.isabstract(leek::Different)


def test_leek::different_constructor_exists():
    assert callable(leek::Different.__init__)


def test_leek::different_constructor_args():
    sig = inspect.signature(leek::Different.__init__)
    params = list(sig.parameters.keys())



def test_leek::trueliteral_is_not_abstract():
    assert not inspect.isabstract(leek::TrueLiteral)


def test_leek::trueliteral_constructor_exists():
    assert callable(leek::TrueLiteral.__init__)


def test_leek::trueliteral_constructor_args():
    sig = inspect.signature(leek::TrueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_leek::forinvariablereference_is_not_abstract():
    assert not inspect.isabstract(leek::ForInVariableReference)


def test_leek::forinvariablereference_constructor_exists():
    assert callable(leek::ForInVariableReference.__init__)


def test_leek::forinvariablereference_constructor_args():
    sig = inspect.signature(leek::ForInVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_leek::foraffectation_is_not_abstract():
    assert not inspect.isabstract(leek::ForAffectation)


def test_leek::foraffectation_constructor_exists():
    assert callable(leek::ForAffectation.__init__)


def test_leek::foraffectation_constructor_args():
    sig = inspect.signature(leek::ForAffectation.__init__)
    params = list(sig.parameters.keys())



def test_leek::script_is_not_abstract():
    assert not inspect.isabstract(leek::Script)


def test_leek::script_constructor_exists():
    assert callable(leek::Script.__init__)


def test_leek::script_constructor_args():
    sig = inspect.signature(leek::Script.__init__)
    params = list(sig.parameters.keys())



def test_leek::forinitializer_is_not_abstract():
    assert not inspect.isabstract(leek::ForInitializer)


def test_leek::forinitializer_constructor_exists():
    assert callable(leek::ForInitializer.__init__)


def test_leek::forinitializer_constructor_args():
    sig = inspect.signature(leek::ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_iteration_is_not_abstract():
    assert not inspect.isabstract(Iteration)


def test_iteration_constructor_exists():
    assert callable(Iteration.__init__)


def test_iteration_constructor_args():
    sig = inspect.signature(Iteration.__init__)
    params = list(sig.parameters.keys())



def test_leek::forin_is_not_abstract():
    assert not inspect.isabstract(leek::ForIn)


def test_leek::forin_constructor_exists():
    assert callable(leek::ForIn.__init__)


def test_leek::forin_constructor_args():
    sig = inspect.signature(leek::ForIn.__init__)
    params = list(sig.parameters.keys())



def test_leek::for_is_not_abstract():
    assert not inspect.isabstract(leek::For)


def test_leek::for_constructor_exists():
    assert callable(leek::For.__init__)


def test_leek::for_constructor_args():
    sig = inspect.signature(leek::For.__init__)
    params = list(sig.parameters.keys())



def test_leek::while_is_not_abstract():
    assert not inspect.isabstract(leek::While)


def test_leek::while_constructor_exists():
    assert callable(leek::While.__init__)


def test_leek::while_constructor_args():
    sig = inspect.signature(leek::While.__init__)
    params = list(sig.parameters.keys())



def test_leek::ifcondition_is_not_abstract():
    assert not inspect.isabstract(leek::IfCondition)


def test_leek::ifcondition_constructor_exists():
    assert callable(leek::IfCondition.__init__)


def test_leek::ifcondition_constructor_args():
    sig = inspect.signature(leek::IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_leek::variablereference_is_not_abstract():
    assert not inspect.isabstract(leek::VariableReference)


def test_leek::variablereference_constructor_exists():
    assert callable(leek::VariableReference.__init__)


def test_leek::variablereference_constructor_args():
    sig = inspect.signature(leek::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_foraffectation_is_not_abstract():
    assert not inspect.isabstract(ForAffectation)


def test_foraffectation_constructor_exists():
    assert callable(ForAffectation.__init__)


def test_foraffectation_constructor_args():
    sig = inspect.signature(ForAffectation.__init__)
    params = list(sig.parameters.keys())



def test_forinitializer_is_not_abstract():
    assert not inspect.isabstract(ForInitializer)


def test_forinitializer_constructor_exists():
    assert callable(ForInitializer.__init__)


def test_forinitializer_constructor_args():
    sig = inspect.signature(ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_leek::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(leek::VariableDeclaration)


def test_leek::variabledeclaration_constructor_exists():
    assert callable(leek::VariableDeclaration.__init__)


def test_leek::variabledeclaration_constructor_args():
    sig = inspect.signature(leek::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "byAdress" in params, "Missing parameter 'byAdress'"

def test_leek::variabledeclaration_has_name():
    assert hasattr(leek::VariableDeclaration, "name")
    descriptor = None
    for klass in leek::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_leek::variabledeclaration_has_byAdress():
    assert hasattr(leek::VariableDeclaration, "byAdress")
    descriptor = None
    for klass in leek::VariableDeclaration.__mro__:
        if "byAdress" in klass.__dict__:
            descriptor = klass.__dict__["byAdress"]
            break
    assert isinstance(descriptor, property)



def test_ifcondition_is_not_abstract():
    assert not inspect.isabstract(IfCondition)


def test_ifcondition_constructor_exists():
    assert callable(IfCondition.__init__)


def test_ifcondition_constructor_args():
    sig = inspect.signature(IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_leek::expression_is_not_abstract():
    assert not inspect.isabstract(leek::Expression)


def test_leek::expression_constructor_exists():
    assert callable(leek::Expression.__init__)


def test_leek::expression_constructor_args():
    sig = inspect.signature(leek::Expression.__init__)
    params = list(sig.parameters.keys())



def test_affectationstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationStatement)


def test_affectationstatement_constructor_exists():
    assert callable(AffectationStatement.__init__)


def test_affectationstatement_constructor_args():
    sig = inspect.signature(AffectationStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::affectationdecrement_is_not_abstract():
    assert not inspect.isabstract(leek::AffectationDecrement)


def test_leek::affectationdecrement_constructor_exists():
    assert callable(leek::AffectationDecrement.__init__)


def test_leek::affectationdecrement_constructor_args():
    sig = inspect.signature(leek::AffectationDecrement.__init__)
    params = list(sig.parameters.keys())



def test_leek::affectationprefixstatement_is_not_abstract():
    assert not inspect.isabstract(leek::AffectationPrefixStatement)


def test_leek::affectationprefixstatement_constructor_exists():
    assert callable(leek::AffectationPrefixStatement.__init__)


def test_leek::affectationprefixstatement_constructor_args():
    sig = inspect.signature(leek::AffectationPrefixStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::affectationincrement_is_not_abstract():
    assert not inspect.isabstract(leek::AffectationIncrement)


def test_leek::affectationincrement_constructor_exists():
    assert callable(leek::AffectationIncrement.__init__)


def test_leek::affectationincrement_constructor_args():
    sig = inspect.signature(leek::AffectationIncrement.__init__)
    params = list(sig.parameters.keys())



def test_leek::affectationpostfixstatement_is_not_abstract():
    assert not inspect.isabstract(leek::AffectationPostfixStatement)


def test_leek::affectationpostfixstatement_constructor_exists():
    assert callable(leek::AffectationPostfixStatement.__init__)


def test_leek::affectationpostfixstatement_constructor_args():
    sig = inspect.signature(leek::AffectationPostfixStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::affectation_is_not_abstract():
    assert not inspect.isabstract(leek::Affectation)


def test_leek::affectation_constructor_exists():
    assert callable(leek::Affectation.__init__)


def test_leek::affectation_constructor_args():
    sig = inspect.signature(leek::Affectation.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_leek::include_is_not_abstract():
    assert not inspect.isabstract(leek::Include)


def test_leek::include_constructor_exists():
    assert callable(leek::Include.__init__)


def test_leek::include_constructor_args():
    sig = inspect.signature(leek::Include.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_leek::include_has_importURI():
    assert hasattr(leek::Include, "importURI")
    descriptor = None
    for klass in leek::Include.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_leek::emptystatement_is_not_abstract():
    assert not inspect.isabstract(leek::EmptyStatement)


def test_leek::emptystatement_constructor_exists():
    assert callable(leek::EmptyStatement.__init__)


def test_leek::emptystatement_constructor_args():
    sig = inspect.signature(leek::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::functioncall_is_not_abstract():
    assert not inspect.isabstract(leek::FunctionCall)


def test_leek::functioncall_constructor_exists():
    assert callable(leek::FunctionCall.__init__)


def test_leek::functioncall_constructor_args():
    sig = inspect.signature(leek::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_leek::iteration_is_not_abstract():
    assert not inspect.isabstract(leek::Iteration)


def test_leek::iteration_constructor_exists():
    assert callable(leek::Iteration.__init__)


def test_leek::iteration_constructor_args():
    sig = inspect.signature(leek::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_leek::continuestatement_is_not_abstract():
    assert not inspect.isabstract(leek::ContinueStatement)


def test_leek::continuestatement_constructor_exists():
    assert callable(leek::ContinueStatement.__init__)


def test_leek::continuestatement_constructor_args():
    sig = inspect.signature(leek::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::globaldeclaration_is_not_abstract():
    assert not inspect.isabstract(leek::GlobalDeclaration)


def test_leek::globaldeclaration_constructor_exists():
    assert callable(leek::GlobalDeclaration.__init__)


def test_leek::globaldeclaration_constructor_args():
    sig = inspect.signature(leek::GlobalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_leek::affectationstatement_is_not_abstract():
    assert not inspect.isabstract(leek::AffectationStatement)


def test_leek::affectationstatement_constructor_exists():
    assert callable(leek::AffectationStatement.__init__)


def test_leek::affectationstatement_constructor_args():
    sig = inspect.signature(leek::AffectationStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::returnstatement_is_not_abstract():
    assert not inspect.isabstract(leek::ReturnStatement)


def test_leek::returnstatement_constructor_exists():
    assert callable(leek::ReturnStatement.__init__)


def test_leek::returnstatement_constructor_args():
    sig = inspect.signature(leek::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::if_is_not_abstract():
    assert not inspect.isabstract(leek::If)


def test_leek::if_constructor_exists():
    assert callable(leek::If.__init__)


def test_leek::if_constructor_args():
    sig = inspect.signature(leek::If.__init__)
    params = list(sig.parameters.keys())



def test_leek::statementblock_is_not_abstract():
    assert not inspect.isabstract(leek::StatementBlock)


def test_leek::statementblock_constructor_exists():
    assert callable(leek::StatementBlock.__init__)


def test_leek::statementblock_constructor_args():
    sig = inspect.signature(leek::StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_leek::localdeclaration_is_not_abstract():
    assert not inspect.isabstract(leek::LocalDeclaration)


def test_leek::localdeclaration_constructor_exists():
    assert callable(leek::LocalDeclaration.__init__)


def test_leek::localdeclaration_constructor_args():
    sig = inspect.signature(leek::LocalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_leek::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(leek::FunctionDeclaration)


def test_leek::functiondeclaration_constructor_exists():
    assert callable(leek::FunctionDeclaration.__init__)


def test_leek::functiondeclaration_constructor_args():
    sig = inspect.signature(leek::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_leek::functiondeclaration_has_name():
    assert hasattr(leek::FunctionDeclaration, "name")
    descriptor = None
    for klass in leek::FunctionDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_leek::breakstatement_is_not_abstract():
    assert not inspect.isabstract(leek::BreakStatement)


def test_leek::breakstatement_constructor_exists():
    assert callable(leek::BreakStatement.__init__)


def test_leek::breakstatement_constructor_args():
    sig = inspect.signature(leek::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_leek::statement_is_not_abstract():
    assert not inspect.isabstract(leek::Statement)


def test_leek::statement_constructor_exists():
    assert callable(leek::Statement.__init__)


def test_leek::statement_constructor_args():
    sig = inspect.signature(leek::Statement.__init__)
    params = list(sig.parameters.keys())



def test_leek::not_is_not_abstract():
    assert not inspect.isabstract(leek::Not)


def test_leek::not_constructor_exists():
    assert callable(leek::Not.__init__)


def test_leek::not_constructor_args():
    sig = inspect.signature(leek::Not.__init__)
    params = list(sig.parameters.keys())



def test_leek::unitaryminus_is_not_abstract():
    assert not inspect.isabstract(leek::UnitaryMinus)


def test_leek::unitaryminus_constructor_exists():
    assert callable(leek::UnitaryMinus.__init__)


def test_leek::unitaryminus_constructor_args():
    sig = inspect.signature(leek::UnitaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_leek::ternaryif_is_not_abstract():
    assert not inspect.isabstract(leek::TernaryIf)


def test_leek::ternaryif_constructor_exists():
    assert callable(leek::TernaryIf.__init__)


def test_leek::ternaryif_constructor_args():
    sig = inspect.signature(leek::TernaryIf.__init__)
    params = list(sig.parameters.keys())



def test_leek::div_is_not_abstract():
    assert not inspect.isabstract(leek::Div)


def test_leek::div_constructor_exists():
    assert callable(leek::Div.__init__)


def test_leek::div_constructor_args():
    sig = inspect.signature(leek::Div.__init__)
    params = list(sig.parameters.keys())



def test_leek::minus_is_not_abstract():
    assert not inspect.isabstract(leek::Minus)


def test_leek::minus_constructor_exists():
    assert callable(leek::Minus.__init__)


def test_leek::minus_constructor_args():
    sig = inspect.signature(leek::Minus.__init__)
    params = list(sig.parameters.keys())



def test_leek::plus_is_not_abstract():
    assert not inspect.isabstract(leek::Plus)


def test_leek::plus_constructor_exists():
    assert callable(leek::Plus.__init__)


def test_leek::plus_constructor_args():
    sig = inspect.signature(leek::Plus.__init__)
    params = list(sig.parameters.keys())



def test_leek::and_is_not_abstract():
    assert not inspect.isabstract(leek::And)


def test_leek::and_constructor_exists():
    assert callable(leek::And.__init__)


def test_leek::and_constructor_args():
    sig = inspect.signature(leek::And.__init__)
    params = list(sig.parameters.keys())



def test_leek::or_is_not_abstract():
    assert not inspect.isabstract(leek::Or)


def test_leek::or_constructor_exists():
    assert callable(leek::Or.__init__)


def test_leek::or_constructor_args():
    sig = inspect.signature(leek::Or.__init__)
    params = list(sig.parameters.keys())



def test_leek::more_is_not_abstract():
    assert not inspect.isabstract(leek::More)


def test_leek::more_constructor_exists():
    assert callable(leek::More.__init__)


def test_leek::more_constructor_args():
    sig = inspect.signature(leek::More.__init__)
    params = list(sig.parameters.keys())



def test_leek::moreorequals_is_not_abstract():
    assert not inspect.isabstract(leek::MoreOrEquals)


def test_leek::moreorequals_constructor_exists():
    assert callable(leek::MoreOrEquals.__init__)


def test_leek::moreorequals_constructor_args():
    sig = inspect.signature(leek::MoreOrEquals.__init__)
    params = list(sig.parameters.keys())



def test_leek::less_is_not_abstract():
    assert not inspect.isabstract(leek::Less)


def test_leek::less_constructor_exists():
    assert callable(leek::Less.__init__)


def test_leek::less_constructor_args():
    sig = inspect.signature(leek::Less.__init__)
    params = list(sig.parameters.keys())



def test_leek::lessorequals_is_not_abstract():
    assert not inspect.isabstract(leek::LessOrEquals)


def test_leek::lessorequals_constructor_exists():
    assert callable(leek::LessOrEquals.__init__)


def test_leek::lessorequals_constructor_args():
    sig = inspect.signature(leek::LessOrEquals.__init__)
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
Prefix_strategy = st.builds(
    Prefix,
)
AffectationPrefixStatement_strategy = st.builds(
    AffectationPrefixStatement,
)
leek::PrefixIncrement_strategy = st.builds(
    leek::PrefixIncrement,
)
leek::PrefixDecrement_strategy = st.builds(
    leek::PrefixDecrement,
)
Postfix_strategy = st.builds(
    Postfix,
)
AffectationPostfixStatement_strategy = st.builds(
    AffectationPostfixStatement,
)
leek::PostfixDecrement_strategy = st.builds(
    leek::PostfixDecrement,
)
leek::PostfixIncrement_strategy = st.builds(
    leek::PostfixIncrement,
)
ForInVariableReference_strategy = st.builds(
    ForInVariableReference,
)
Expression_strategy = st.builds(
    Expression,
)
leek::IntLiteral_strategy = st.builds(
    leek::IntLiteral,
    value=
        st.integers()
)
leek::FalseLiteral_strategy = st.builds(
    leek::FalseLiteral,
)
leek::Multi_strategy = st.builds(
    leek::Multi,
)
leek::TypedDifferent_strategy = st.builds(
    leek::TypedDifferent,
)
leek::NullLiteral_strategy = st.builds(
    leek::NullLiteral,
)
leek::StringLiteral_strategy = st.builds(
    leek::StringLiteral,
    value=
        safe_text
)
leek::ArrayLiteral_strategy = st.builds(
    leek::ArrayLiteral,
)
leek::Equals_strategy = st.builds(
    leek::Equals,
)
leek::Postfix_strategy = st.builds(
    leek::Postfix,
)
leek::Comparison_strategy = st.builds(
    leek::Comparison,
)
leek::RealLiteral_strategy = st.builds(
    leek::RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
leek::Prefix_strategy = st.builds(
    leek::Prefix,
)
leek::Different_strategy = st.builds(
    leek::Different,
)
leek::TrueLiteral_strategy = st.builds(
    leek::TrueLiteral,
)
leek::ForInVariableReference_strategy = st.builds(
    leek::ForInVariableReference,
)
leek::ForAffectation_strategy = st.builds(
    leek::ForAffectation,
)
leek::Script_strategy = st.builds(
    leek::Script,
)
leek::ForInitializer_strategy = st.builds(
    leek::ForInitializer,
)
Iteration_strategy = st.builds(
    Iteration,
)
leek::ForIn_strategy = st.builds(
    leek::ForIn,
)
leek::For_strategy = st.builds(
    leek::For,
)
leek::While_strategy = st.builds(
    leek::While,
)
leek::IfCondition_strategy = st.builds(
    leek::IfCondition,
)
leek::VariableReference_strategy = st.builds(
    leek::VariableReference,
)
ForAffectation_strategy = st.builds(
    ForAffectation,
)
ForInitializer_strategy = st.builds(
    ForInitializer,
)
leek::VariableDeclaration_strategy = st.builds(
    leek::VariableDeclaration,
    name=
        safe_text,
    byAdress=
        st.booleans()
)
IfCondition_strategy = st.builds(
    IfCondition,
)
leek::Expression_strategy = st.builds(
    leek::Expression,
)
AffectationStatement_strategy = st.builds(
    AffectationStatement,
)
leek::AffectationDecrement_strategy = st.builds(
    leek::AffectationDecrement,
)
leek::AffectationPrefixStatement_strategy = st.builds(
    leek::AffectationPrefixStatement,
)
leek::AffectationIncrement_strategy = st.builds(
    leek::AffectationIncrement,
)
leek::AffectationPostfixStatement_strategy = st.builds(
    leek::AffectationPostfixStatement,
)
leek::Affectation_strategy = st.builds(
    leek::Affectation,
)
Statement_strategy = st.builds(
    Statement,
)
leek::Include_strategy = st.builds(
    leek::Include,
    importURI=
        safe_text
)
leek::EmptyStatement_strategy = st.builds(
    leek::EmptyStatement,
)
leek::FunctionCall_strategy = st.builds(
    leek::FunctionCall,
)
leek::Iteration_strategy = st.builds(
    leek::Iteration,
)
leek::ContinueStatement_strategy = st.builds(
    leek::ContinueStatement,
)
leek::GlobalDeclaration_strategy = st.builds(
    leek::GlobalDeclaration,
)
leek::AffectationStatement_strategy = st.builds(
    leek::AffectationStatement,
)
leek::ReturnStatement_strategy = st.builds(
    leek::ReturnStatement,
)
leek::If_strategy = st.builds(
    leek::If,
)
leek::StatementBlock_strategy = st.builds(
    leek::StatementBlock,
)
leek::LocalDeclaration_strategy = st.builds(
    leek::LocalDeclaration,
)
leek::FunctionDeclaration_strategy = st.builds(
    leek::FunctionDeclaration,
    name=
        safe_text
)
leek::BreakStatement_strategy = st.builds(
    leek::BreakStatement,
)
leek::Statement_strategy = st.builds(
    leek::Statement,
)
leek::Not_strategy = st.builds(
    leek::Not,
)
leek::UnitaryMinus_strategy = st.builds(
    leek::UnitaryMinus,
)
leek::TernaryIf_strategy = st.builds(
    leek::TernaryIf,
)
leek::Div_strategy = st.builds(
    leek::Div,
)
leek::Minus_strategy = st.builds(
    leek::Minus,
)
leek::Plus_strategy = st.builds(
    leek::Plus,
)
leek::And_strategy = st.builds(
    leek::And,
)
leek::Or_strategy = st.builds(
    leek::Or,
)
leek::More_strategy = st.builds(
    leek::More,
)
leek::MoreOrEquals_strategy = st.builds(
    leek::MoreOrEquals,
)
leek::Less_strategy = st.builds(
    leek::Less,
)
leek::LessOrEquals_strategy = st.builds(
    leek::LessOrEquals,
)

@given(instance=Prefix_strategy)
@settings(max_examples=50)
def test_prefix_instantiation(instance):
    assert isinstance(instance, Prefix)

@given(instance=AffectationPrefixStatement_strategy)
@settings(max_examples=50)
def test_affectationprefixstatement_instantiation(instance):
    assert isinstance(instance, AffectationPrefixStatement)

@given(instance=leek::PrefixIncrement_strategy)
@settings(max_examples=50)
def test_leek::prefixincrement_instantiation(instance):
    assert isinstance(instance, leek::PrefixIncrement)

@given(instance=leek::PrefixDecrement_strategy)
@settings(max_examples=50)
def test_leek::prefixdecrement_instantiation(instance):
    assert isinstance(instance, leek::PrefixDecrement)

@given(instance=Postfix_strategy)
@settings(max_examples=50)
def test_postfix_instantiation(instance):
    assert isinstance(instance, Postfix)

@given(instance=AffectationPostfixStatement_strategy)
@settings(max_examples=50)
def test_affectationpostfixstatement_instantiation(instance):
    assert isinstance(instance, AffectationPostfixStatement)

@given(instance=leek::PostfixDecrement_strategy)
@settings(max_examples=50)
def test_leek::postfixdecrement_instantiation(instance):
    assert isinstance(instance, leek::PostfixDecrement)

@given(instance=leek::PostfixIncrement_strategy)
@settings(max_examples=50)
def test_leek::postfixincrement_instantiation(instance):
    assert isinstance(instance, leek::PostfixIncrement)

@given(instance=ForInVariableReference_strategy)
@settings(max_examples=50)
def test_forinvariablereference_instantiation(instance):
    assert isinstance(instance, ForInVariableReference)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=leek::IntLiteral_strategy)
@settings(max_examples=50)
def test_leek::intliteral_instantiation(instance):
    assert isinstance(instance, leek::IntLiteral)

@given(instance=leek::IntLiteral_strategy)
def test_leek::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=leek::IntLiteral_strategy)
def test_leek::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=leek::FalseLiteral_strategy)
@settings(max_examples=50)
def test_leek::falseliteral_instantiation(instance):
    assert isinstance(instance, leek::FalseLiteral)

@given(instance=leek::Multi_strategy)
@settings(max_examples=50)
def test_leek::multi_instantiation(instance):
    assert isinstance(instance, leek::Multi)

@given(instance=leek::TypedDifferent_strategy)
@settings(max_examples=50)
def test_leek::typeddifferent_instantiation(instance):
    assert isinstance(instance, leek::TypedDifferent)

@given(instance=leek::NullLiteral_strategy)
@settings(max_examples=50)
def test_leek::nullliteral_instantiation(instance):
    assert isinstance(instance, leek::NullLiteral)

@given(instance=leek::StringLiteral_strategy)
@settings(max_examples=50)
def test_leek::stringliteral_instantiation(instance):
    assert isinstance(instance, leek::StringLiteral)

@given(instance=leek::StringLiteral_strategy)
def test_leek::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=leek::StringLiteral_strategy)
def test_leek::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=leek::ArrayLiteral_strategy)
@settings(max_examples=50)
def test_leek::arrayliteral_instantiation(instance):
    assert isinstance(instance, leek::ArrayLiteral)

@given(instance=leek::Equals_strategy)
@settings(max_examples=50)
def test_leek::equals_instantiation(instance):
    assert isinstance(instance, leek::Equals)

@given(instance=leek::Postfix_strategy)
@settings(max_examples=50)
def test_leek::postfix_instantiation(instance):
    assert isinstance(instance, leek::Postfix)

@given(instance=leek::Comparison_strategy)
@settings(max_examples=50)
def test_leek::comparison_instantiation(instance):
    assert isinstance(instance, leek::Comparison)

@given(instance=leek::RealLiteral_strategy)
@settings(max_examples=50)
def test_leek::realliteral_instantiation(instance):
    assert isinstance(instance, leek::RealLiteral)

@given(instance=leek::RealLiteral_strategy)
def test_leek::realliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=leek::RealLiteral_strategy)
def test_leek::realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=leek::Prefix_strategy)
@settings(max_examples=50)
def test_leek::prefix_instantiation(instance):
    assert isinstance(instance, leek::Prefix)

@given(instance=leek::Different_strategy)
@settings(max_examples=50)
def test_leek::different_instantiation(instance):
    assert isinstance(instance, leek::Different)

@given(instance=leek::TrueLiteral_strategy)
@settings(max_examples=50)
def test_leek::trueliteral_instantiation(instance):
    assert isinstance(instance, leek::TrueLiteral)

@given(instance=leek::ForInVariableReference_strategy)
@settings(max_examples=50)
def test_leek::forinvariablereference_instantiation(instance):
    assert isinstance(instance, leek::ForInVariableReference)

@given(instance=leek::ForAffectation_strategy)
@settings(max_examples=50)
def test_leek::foraffectation_instantiation(instance):
    assert isinstance(instance, leek::ForAffectation)

@given(instance=leek::Script_strategy)
@settings(max_examples=50)
def test_leek::script_instantiation(instance):
    assert isinstance(instance, leek::Script)

@given(instance=leek::ForInitializer_strategy)
@settings(max_examples=50)
def test_leek::forinitializer_instantiation(instance):
    assert isinstance(instance, leek::ForInitializer)

@given(instance=Iteration_strategy)
@settings(max_examples=50)
def test_iteration_instantiation(instance):
    assert isinstance(instance, Iteration)

@given(instance=leek::ForIn_strategy)
@settings(max_examples=50)
def test_leek::forin_instantiation(instance):
    assert isinstance(instance, leek::ForIn)

@given(instance=leek::For_strategy)
@settings(max_examples=50)
def test_leek::for_instantiation(instance):
    assert isinstance(instance, leek::For)

@given(instance=leek::While_strategy)
@settings(max_examples=50)
def test_leek::while_instantiation(instance):
    assert isinstance(instance, leek::While)

@given(instance=leek::IfCondition_strategy)
@settings(max_examples=50)
def test_leek::ifcondition_instantiation(instance):
    assert isinstance(instance, leek::IfCondition)

@given(instance=leek::VariableReference_strategy)
@settings(max_examples=50)
def test_leek::variablereference_instantiation(instance):
    assert isinstance(instance, leek::VariableReference)

@given(instance=ForAffectation_strategy)
@settings(max_examples=50)
def test_foraffectation_instantiation(instance):
    assert isinstance(instance, ForAffectation)

@given(instance=ForInitializer_strategy)
@settings(max_examples=50)
def test_forinitializer_instantiation(instance):
    assert isinstance(instance, ForInitializer)

@given(instance=leek::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_leek::variabledeclaration_instantiation(instance):
    assert isinstance(instance, leek::VariableDeclaration)

@given(instance=leek::VariableDeclaration_strategy)
def test_leek::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=leek::VariableDeclaration_strategy)
def test_leek::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=leek::VariableDeclaration_strategy)
def test_leek::variabledeclaration_byAdress_type(instance):
    assert isinstance(instance.byAdress, bool)


@given(instance=leek::VariableDeclaration_strategy)
def test_leek::variabledeclaration_byAdress_setter(instance):
    original = instance.byAdress
    instance.byAdress = original
    assert instance.byAdress == original

@given(instance=IfCondition_strategy)
@settings(max_examples=50)
def test_ifcondition_instantiation(instance):
    assert isinstance(instance, IfCondition)

@given(instance=leek::Expression_strategy)
@settings(max_examples=50)
def test_leek::expression_instantiation(instance):
    assert isinstance(instance, leek::Expression)

@given(instance=AffectationStatement_strategy)
@settings(max_examples=50)
def test_affectationstatement_instantiation(instance):
    assert isinstance(instance, AffectationStatement)

@given(instance=leek::AffectationDecrement_strategy)
@settings(max_examples=50)
def test_leek::affectationdecrement_instantiation(instance):
    assert isinstance(instance, leek::AffectationDecrement)

@given(instance=leek::AffectationPrefixStatement_strategy)
@settings(max_examples=50)
def test_leek::affectationprefixstatement_instantiation(instance):
    assert isinstance(instance, leek::AffectationPrefixStatement)

@given(instance=leek::AffectationIncrement_strategy)
@settings(max_examples=50)
def test_leek::affectationincrement_instantiation(instance):
    assert isinstance(instance, leek::AffectationIncrement)

@given(instance=leek::AffectationPostfixStatement_strategy)
@settings(max_examples=50)
def test_leek::affectationpostfixstatement_instantiation(instance):
    assert isinstance(instance, leek::AffectationPostfixStatement)

@given(instance=leek::Affectation_strategy)
@settings(max_examples=50)
def test_leek::affectation_instantiation(instance):
    assert isinstance(instance, leek::Affectation)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=leek::Include_strategy)
@settings(max_examples=50)
def test_leek::include_instantiation(instance):
    assert isinstance(instance, leek::Include)

@given(instance=leek::Include_strategy)
def test_leek::include_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=leek::Include_strategy)
def test_leek::include_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=leek::EmptyStatement_strategy)
@settings(max_examples=50)
def test_leek::emptystatement_instantiation(instance):
    assert isinstance(instance, leek::EmptyStatement)

@given(instance=leek::FunctionCall_strategy)
@settings(max_examples=50)
def test_leek::functioncall_instantiation(instance):
    assert isinstance(instance, leek::FunctionCall)

@given(instance=leek::Iteration_strategy)
@settings(max_examples=50)
def test_leek::iteration_instantiation(instance):
    assert isinstance(instance, leek::Iteration)

@given(instance=leek::ContinueStatement_strategy)
@settings(max_examples=50)
def test_leek::continuestatement_instantiation(instance):
    assert isinstance(instance, leek::ContinueStatement)

@given(instance=leek::GlobalDeclaration_strategy)
@settings(max_examples=50)
def test_leek::globaldeclaration_instantiation(instance):
    assert isinstance(instance, leek::GlobalDeclaration)

@given(instance=leek::AffectationStatement_strategy)
@settings(max_examples=50)
def test_leek::affectationstatement_instantiation(instance):
    assert isinstance(instance, leek::AffectationStatement)

@given(instance=leek::ReturnStatement_strategy)
@settings(max_examples=50)
def test_leek::returnstatement_instantiation(instance):
    assert isinstance(instance, leek::ReturnStatement)

@given(instance=leek::If_strategy)
@settings(max_examples=50)
def test_leek::if_instantiation(instance):
    assert isinstance(instance, leek::If)

@given(instance=leek::StatementBlock_strategy)
@settings(max_examples=50)
def test_leek::statementblock_instantiation(instance):
    assert isinstance(instance, leek::StatementBlock)

@given(instance=leek::LocalDeclaration_strategy)
@settings(max_examples=50)
def test_leek::localdeclaration_instantiation(instance):
    assert isinstance(instance, leek::LocalDeclaration)

@given(instance=leek::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_leek::functiondeclaration_instantiation(instance):
    assert isinstance(instance, leek::FunctionDeclaration)

@given(instance=leek::FunctionDeclaration_strategy)
def test_leek::functiondeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=leek::FunctionDeclaration_strategy)
def test_leek::functiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=leek::BreakStatement_strategy)
@settings(max_examples=50)
def test_leek::breakstatement_instantiation(instance):
    assert isinstance(instance, leek::BreakStatement)

@given(instance=leek::Statement_strategy)
@settings(max_examples=50)
def test_leek::statement_instantiation(instance):
    assert isinstance(instance, leek::Statement)

@given(instance=leek::Not_strategy)
@settings(max_examples=50)
def test_leek::not_instantiation(instance):
    assert isinstance(instance, leek::Not)

@given(instance=leek::UnitaryMinus_strategy)
@settings(max_examples=50)
def test_leek::unitaryminus_instantiation(instance):
    assert isinstance(instance, leek::UnitaryMinus)

@given(instance=leek::TernaryIf_strategy)
@settings(max_examples=50)
def test_leek::ternaryif_instantiation(instance):
    assert isinstance(instance, leek::TernaryIf)

@given(instance=leek::Div_strategy)
@settings(max_examples=50)
def test_leek::div_instantiation(instance):
    assert isinstance(instance, leek::Div)

@given(instance=leek::Minus_strategy)
@settings(max_examples=50)
def test_leek::minus_instantiation(instance):
    assert isinstance(instance, leek::Minus)

@given(instance=leek::Plus_strategy)
@settings(max_examples=50)
def test_leek::plus_instantiation(instance):
    assert isinstance(instance, leek::Plus)

@given(instance=leek::And_strategy)
@settings(max_examples=50)
def test_leek::and_instantiation(instance):
    assert isinstance(instance, leek::And)

@given(instance=leek::Or_strategy)
@settings(max_examples=50)
def test_leek::or_instantiation(instance):
    assert isinstance(instance, leek::Or)

@given(instance=leek::More_strategy)
@settings(max_examples=50)
def test_leek::more_instantiation(instance):
    assert isinstance(instance, leek::More)

@given(instance=leek::MoreOrEquals_strategy)
@settings(max_examples=50)
def test_leek::moreorequals_instantiation(instance):
    assert isinstance(instance, leek::MoreOrEquals)

@given(instance=leek::Less_strategy)
@settings(max_examples=50)
def test_leek::less_instantiation(instance):
    assert isinstance(instance, leek::Less)

@given(instance=leek::LessOrEquals_strategy)
@settings(max_examples=50)
def test_leek::lessorequals_instantiation(instance):
    assert isinstance(instance, leek::LessOrEquals)
