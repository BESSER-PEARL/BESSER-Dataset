import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SyntaxElement,
    xpand3::ImportStatement,
    xpand3::File,
    xpand3::SyntaxElement,
    AbstractNamedDeclaration,
    xpand3::declaration::Extension,
    xpand3::declaration::JavaExtension,
    xpand3::declaration::Definition,
    declaration::xpand3::Identifier,
    declaration::xpand3::DeclaredParameter,
    Extension,
    xpand3::declaration::CreateExtension,
    AbstractAspect,
    xpand3::declaration::DefinitionAspect,
    xpand3::declaration::ExtensionAspect,
    AbstractStatementWithBody,
    xpand3::statement::ForEachStatement,
    xpand3::statement::IfStatement,
    xpand3::statement::FileStatement,
    declaration::xpand3::File,
    xpand3::declaration::AbstractDeclaration,
    xpand3::statement::ProtectStatement,
    xpand3::statement::LetStatement,
    IfStatement,
    statement::xpand3::Identifier,
    AbstractStatement,
    xpand3::statement::ExpressionStatement,
    xpand3::statement::AbstractStatementWithBody,
    xpand3::statement::TextStatement,
    xpand3::statement::ErrorStatement,
    xpand3::statement::ExpandStatement,
    xpand3::statement::AbstractStatement,
    xpand3::expression::Case,
    Case,
    Literal,
    xpand3::expression::IntegerLiteral,
    xpand3::expression::RealLiteral,
    xpand3::expression::StringLiteral,
    xpand3::expression::NullLiteral,
    xpand3::expression::BooleanLiteral,
    expression::xpand3::Identifier,
    AbstractExpression,
    xpand3::expression::Literal,
    xpand3::expression::BinaryOperation,
    xpand3::expression::UnaryOperation,
    xpand3::expression::LetExpression,
    xpand3::expression::ChainExpression,
    xpand3::expression::SwitchExpression,
    xpand3::expression::ListLiteral,
    xpand3::expression::Cast,
    BinaryOperation,
    xpand3::expression::BooleanOperation,
    xpand3::expression::AbstractExpression,
    xpand3::DeclaredParameter,
    xpand3::expression::IfExpression,
    xpand3::expression::GlobalVarExpression,
    FeatureCall,
    xpand3::expression::OperationCall,
    xpand3::expression::TypeSelectExpression,
    xpand3::expression::CollectionExpression,
    xpand3::expression::FeatureCall,
    xpand3::expression::ConstructorCallExpression,
    xpand3::Identifier,
    AbstractDeclaration,
    xpand3::declaration::Check,
    xpand3::declaration::AbstractAspect,
    xpand3::declaration::AbstractNamedDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_syntaxelement_is_not_abstract():
    assert not inspect.isabstract(SyntaxElement)


def test_syntaxelement_constructor_exists():
    assert callable(SyntaxElement.__init__)


def test_syntaxelement_constructor_args():
    sig = inspect.signature(SyntaxElement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::importstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::ImportStatement)


def test_xpand3::importstatement_constructor_exists():
    assert callable(xpand3::ImportStatement.__init__)


def test_xpand3::importstatement_constructor_args():
    sig = inspect.signature(xpand3::ImportStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exported" in params, "Missing parameter 'exported'"

def test_xpand3::importstatement_has_exported():
    assert hasattr(xpand3::ImportStatement, "exported")
    descriptor = None
    for klass in xpand3::ImportStatement.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)



def test_xpand3::file_is_not_abstract():
    assert not inspect.isabstract(xpand3::File)


def test_xpand3::file_constructor_exists():
    assert callable(xpand3::File.__init__)


def test_xpand3::file_constructor_args():
    sig = inspect.signature(xpand3::File.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::syntaxelement_is_not_abstract():
    assert not inspect.isabstract(xpand3::SyntaxElement)


def test_xpand3::syntaxelement_constructor_exists():
    assert callable(xpand3::SyntaxElement.__init__)


def test_xpand3::syntaxelement_constructor_args():
    sig = inspect.signature(xpand3::SyntaxElement.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_xpand3::syntaxelement_has_line():
    assert hasattr(xpand3::SyntaxElement, "line")
    descriptor = None
    for klass in xpand3::SyntaxElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_xpand3::syntaxelement_has_fileName():
    assert hasattr(xpand3::SyntaxElement, "fileName")
    descriptor = None
    for klass in xpand3::SyntaxElement.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_xpand3::syntaxelement_has_end():
    assert hasattr(xpand3::SyntaxElement, "end")
    descriptor = None
    for klass in xpand3::SyntaxElement.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_xpand3::syntaxelement_has_start():
    assert hasattr(xpand3::SyntaxElement, "start")
    descriptor = None
    for klass in xpand3::SyntaxElement.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_abstractnameddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractNamedDeclaration)


def test_abstractnameddeclaration_constructor_exists():
    assert callable(AbstractNamedDeclaration.__init__)


def test_abstractnameddeclaration_constructor_args():
    sig = inspect.signature(AbstractNamedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::declaration::extension_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::Extension)


def test_xpand3::declaration::extension_constructor_exists():
    assert callable(xpand3::declaration::Extension.__init__)


def test_xpand3::declaration::extension_constructor_args():
    sig = inspect.signature(xpand3::declaration::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "cached" in params, "Missing parameter 'cached'"

def test_xpand3::declaration::extension_has_cached():
    assert hasattr(xpand3::declaration::Extension, "cached")
    descriptor = None
    for klass in xpand3::declaration::Extension.__mro__:
        if "cached" in klass.__dict__:
            descriptor = klass.__dict__["cached"]
            break
    assert isinstance(descriptor, property)



def test_xpand3::declaration::javaextension_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::JavaExtension)


def test_xpand3::declaration::javaextension_constructor_exists():
    assert callable(xpand3::declaration::JavaExtension.__init__)


def test_xpand3::declaration::javaextension_constructor_args():
    sig = inspect.signature(xpand3::declaration::JavaExtension.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::declaration::definition_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::Definition)


def test_xpand3::declaration::definition_constructor_exists():
    assert callable(xpand3::declaration::Definition.__init__)


def test_xpand3::declaration::definition_constructor_args():
    sig = inspect.signature(xpand3::declaration::Definition.__init__)
    params = list(sig.parameters.keys())



def test_declaration::xpand3::identifier_is_not_abstract():
    assert not inspect.isabstract(declaration::xpand3::Identifier)


def test_declaration::xpand3::identifier_constructor_exists():
    assert callable(declaration::xpand3::Identifier.__init__)


def test_declaration::xpand3::identifier_constructor_args():
    sig = inspect.signature(declaration::xpand3::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_declaration::xpand3::declaredparameter_is_not_abstract():
    assert not inspect.isabstract(declaration::xpand3::DeclaredParameter)


def test_declaration::xpand3::declaredparameter_constructor_exists():
    assert callable(declaration::xpand3::DeclaredParameter.__init__)


def test_declaration::xpand3::declaredparameter_constructor_args():
    sig = inspect.signature(declaration::xpand3::DeclaredParameter.__init__)
    params = list(sig.parameters.keys())



def test_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::declaration::createextension_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::CreateExtension)


def test_xpand3::declaration::createextension_constructor_exists():
    assert callable(xpand3::declaration::CreateExtension.__init__)


def test_xpand3::declaration::createextension_constructor_args():
    sig = inspect.signature(xpand3::declaration::CreateExtension.__init__)
    params = list(sig.parameters.keys())



def test_abstractaspect_is_not_abstract():
    assert not inspect.isabstract(AbstractAspect)


def test_abstractaspect_constructor_exists():
    assert callable(AbstractAspect.__init__)


def test_abstractaspect_constructor_args():
    sig = inspect.signature(AbstractAspect.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::declaration::definitionaspect_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::DefinitionAspect)


def test_xpand3::declaration::definitionaspect_constructor_exists():
    assert callable(xpand3::declaration::DefinitionAspect.__init__)


def test_xpand3::declaration::definitionaspect_constructor_args():
    sig = inspect.signature(xpand3::declaration::DefinitionAspect.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::declaration::extensionaspect_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::ExtensionAspect)


def test_xpand3::declaration::extensionaspect_constructor_exists():
    assert callable(xpand3::declaration::ExtensionAspect.__init__)


def test_xpand3::declaration::extensionaspect_constructor_args():
    sig = inspect.signature(xpand3::declaration::ExtensionAspect.__init__)
    params = list(sig.parameters.keys())



def test_abstractstatementwithbody_is_not_abstract():
    assert not inspect.isabstract(AbstractStatementWithBody)


def test_abstractstatementwithbody_constructor_exists():
    assert callable(AbstractStatementWithBody.__init__)


def test_abstractstatementwithbody_constructor_args():
    sig = inspect.signature(AbstractStatementWithBody.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::statement::foreachstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::ForEachStatement)


def test_xpand3::statement::foreachstatement_constructor_exists():
    assert callable(xpand3::statement::ForEachStatement.__init__)


def test_xpand3::statement::foreachstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::statement::ifstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::IfStatement)


def test_xpand3::statement::ifstatement_constructor_exists():
    assert callable(xpand3::statement::IfStatement.__init__)


def test_xpand3::statement::ifstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::statement::filestatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::FileStatement)


def test_xpand3::statement::filestatement_constructor_exists():
    assert callable(xpand3::statement::FileStatement.__init__)


def test_xpand3::statement::filestatement_constructor_args():
    sig = inspect.signature(xpand3::statement::FileStatement.__init__)
    params = list(sig.parameters.keys())
    assert "once" in params, "Missing parameter 'once'"

def test_xpand3::statement::filestatement_has_once():
    assert hasattr(xpand3::statement::FileStatement, "once")
    descriptor = None
    for klass in xpand3::statement::FileStatement.__mro__:
        if "once" in klass.__dict__:
            descriptor = klass.__dict__["once"]
            break
    assert isinstance(descriptor, property)



def test_declaration::xpand3::file_is_not_abstract():
    assert not inspect.isabstract(declaration::xpand3::File)


def test_declaration::xpand3::file_constructor_exists():
    assert callable(declaration::xpand3::File.__init__)


def test_declaration::xpand3::file_constructor_args():
    sig = inspect.signature(declaration::xpand3::File.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::declaration::abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::AbstractDeclaration)


def test_xpand3::declaration::abstractdeclaration_constructor_exists():
    assert callable(xpand3::declaration::AbstractDeclaration.__init__)


def test_xpand3::declaration::abstractdeclaration_constructor_args():
    sig = inspect.signature(xpand3::declaration::AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"

def test_xpand3::declaration::abstractdeclaration_has_isPrivate():
    assert hasattr(xpand3::declaration::AbstractDeclaration, "isPrivate")
    descriptor = None
    for klass in xpand3::declaration::AbstractDeclaration.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)



def test_xpand3::statement::protectstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::ProtectStatement)


def test_xpand3::statement::protectstatement_constructor_exists():
    assert callable(xpand3::statement::ProtectStatement.__init__)


def test_xpand3::statement::protectstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::ProtectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "disable" in params, "Missing parameter 'disable'"

def test_xpand3::statement::protectstatement_has_disable():
    assert hasattr(xpand3::statement::ProtectStatement, "disable")
    descriptor = None
    for klass in xpand3::statement::ProtectStatement.__mro__:
        if "disable" in klass.__dict__:
            descriptor = klass.__dict__["disable"]
            break
    assert isinstance(descriptor, property)



def test_xpand3::statement::letstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::LetStatement)


def test_xpand3::statement::letstatement_constructor_exists():
    assert callable(xpand3::statement::LetStatement.__init__)


def test_xpand3::statement::letstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::LetStatement.__init__)
    params = list(sig.parameters.keys())



def test_ifstatement_is_not_abstract():
    assert not inspect.isabstract(IfStatement)


def test_ifstatement_constructor_exists():
    assert callable(IfStatement.__init__)


def test_ifstatement_constructor_args():
    sig = inspect.signature(IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement::xpand3::identifier_is_not_abstract():
    assert not inspect.isabstract(statement::xpand3::Identifier)


def test_statement::xpand3::identifier_constructor_exists():
    assert callable(statement::xpand3::Identifier.__init__)


def test_statement::xpand3::identifier_constructor_args():
    sig = inspect.signature(statement::xpand3::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_abstractstatement_is_not_abstract():
    assert not inspect.isabstract(AbstractStatement)


def test_abstractstatement_constructor_exists():
    assert callable(AbstractStatement.__init__)


def test_abstractstatement_constructor_args():
    sig = inspect.signature(AbstractStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::statement::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::ExpressionStatement)


def test_xpand3::statement::expressionstatement_constructor_exists():
    assert callable(xpand3::statement::ExpressionStatement.__init__)


def test_xpand3::statement::expressionstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::statement::abstractstatementwithbody_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::AbstractStatementWithBody)


def test_xpand3::statement::abstractstatementwithbody_constructor_exists():
    assert callable(xpand3::statement::AbstractStatementWithBody.__init__)


def test_xpand3::statement::abstractstatementwithbody_constructor_args():
    sig = inspect.signature(xpand3::statement::AbstractStatementWithBody.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::statement::textstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::TextStatement)


def test_xpand3::statement::textstatement_constructor_exists():
    assert callable(xpand3::statement::TextStatement.__init__)


def test_xpand3::statement::textstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::TextStatement.__init__)
    params = list(sig.parameters.keys())
    assert "deleteLine" in params, "Missing parameter 'deleteLine'"
    assert "value" in params, "Missing parameter 'value'"

def test_xpand3::statement::textstatement_has_deleteLine():
    assert hasattr(xpand3::statement::TextStatement, "deleteLine")
    descriptor = None
    for klass in xpand3::statement::TextStatement.__mro__:
        if "deleteLine" in klass.__dict__:
            descriptor = klass.__dict__["deleteLine"]
            break
    assert isinstance(descriptor, property)

def test_xpand3::statement::textstatement_has_value():
    assert hasattr(xpand3::statement::TextStatement, "value")
    descriptor = None
    for klass in xpand3::statement::TextStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xpand3::statement::errorstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::ErrorStatement)


def test_xpand3::statement::errorstatement_constructor_exists():
    assert callable(xpand3::statement::ErrorStatement.__init__)


def test_xpand3::statement::errorstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::ErrorStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::statement::expandstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::ExpandStatement)


def test_xpand3::statement::expandstatement_constructor_exists():
    assert callable(xpand3::statement::ExpandStatement.__init__)


def test_xpand3::statement::expandstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::ExpandStatement.__init__)
    params = list(sig.parameters.keys())
    assert "foreach" in params, "Missing parameter 'foreach'"

def test_xpand3::statement::expandstatement_has_foreach():
    assert hasattr(xpand3::statement::ExpandStatement, "foreach")
    descriptor = None
    for klass in xpand3::statement::ExpandStatement.__mro__:
        if "foreach" in klass.__dict__:
            descriptor = klass.__dict__["foreach"]
            break
    assert isinstance(descriptor, property)



def test_xpand3::statement::abstractstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3::statement::AbstractStatement)


def test_xpand3::statement::abstractstatement_constructor_exists():
    assert callable(xpand3::statement::AbstractStatement.__init__)


def test_xpand3::statement::abstractstatement_constructor_args():
    sig = inspect.signature(xpand3::statement::AbstractStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::case_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::Case)


def test_xpand3::expression::case_constructor_exists():
    assert callable(xpand3::expression::Case.__init__)


def test_xpand3::expression::case_constructor_args():
    sig = inspect.signature(xpand3::expression::Case.__init__)
    params = list(sig.parameters.keys())



def test_case_is_not_abstract():
    assert not inspect.isabstract(Case)


def test_case_constructor_exists():
    assert callable(Case.__init__)


def test_case_constructor_args():
    sig = inspect.signature(Case.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::integerliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::IntegerLiteral)


def test_xpand3::expression::integerliteral_constructor_exists():
    assert callable(xpand3::expression::IntegerLiteral.__init__)


def test_xpand3::expression::integerliteral_constructor_args():
    sig = inspect.signature(xpand3::expression::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::realliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::RealLiteral)


def test_xpand3::expression::realliteral_constructor_exists():
    assert callable(xpand3::expression::RealLiteral.__init__)


def test_xpand3::expression::realliteral_constructor_args():
    sig = inspect.signature(xpand3::expression::RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::stringliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::StringLiteral)


def test_xpand3::expression::stringliteral_constructor_exists():
    assert callable(xpand3::expression::StringLiteral.__init__)


def test_xpand3::expression::stringliteral_constructor_args():
    sig = inspect.signature(xpand3::expression::StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::nullliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::NullLiteral)


def test_xpand3::expression::nullliteral_constructor_exists():
    assert callable(xpand3::expression::NullLiteral.__init__)


def test_xpand3::expression::nullliteral_constructor_args():
    sig = inspect.signature(xpand3::expression::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::BooleanLiteral)


def test_xpand3::expression::booleanliteral_constructor_exists():
    assert callable(xpand3::expression::BooleanLiteral.__init__)


def test_xpand3::expression::booleanliteral_constructor_args():
    sig = inspect.signature(xpand3::expression::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression::xpand3::identifier_is_not_abstract():
    assert not inspect.isabstract(expression::xpand3::Identifier)


def test_expression::xpand3::identifier_constructor_exists():
    assert callable(expression::xpand3::Identifier.__init__)


def test_expression::xpand3::identifier_constructor_args():
    sig = inspect.signature(expression::xpand3::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_abstractexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractExpression)


def test_abstractexpression_constructor_exists():
    assert callable(AbstractExpression.__init__)


def test_abstractexpression_constructor_args():
    sig = inspect.signature(AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::literal_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::Literal)


def test_xpand3::expression::literal_constructor_exists():
    assert callable(xpand3::expression::Literal.__init__)


def test_xpand3::expression::literal_constructor_args():
    sig = inspect.signature(xpand3::expression::Literal.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::binaryoperation_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::BinaryOperation)


def test_xpand3::expression::binaryoperation_constructor_exists():
    assert callable(xpand3::expression::BinaryOperation.__init__)


def test_xpand3::expression::binaryoperation_constructor_args():
    sig = inspect.signature(xpand3::expression::BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::unaryoperation_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::UnaryOperation)


def test_xpand3::expression::unaryoperation_constructor_exists():
    assert callable(xpand3::expression::UnaryOperation.__init__)


def test_xpand3::expression::unaryoperation_constructor_args():
    sig = inspect.signature(xpand3::expression::UnaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::letexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::LetExpression)


def test_xpand3::expression::letexpression_constructor_exists():
    assert callable(xpand3::expression::LetExpression.__init__)


def test_xpand3::expression::letexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::chainexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::ChainExpression)


def test_xpand3::expression::chainexpression_constructor_exists():
    assert callable(xpand3::expression::ChainExpression.__init__)


def test_xpand3::expression::chainexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::ChainExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::switchexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::SwitchExpression)


def test_xpand3::expression::switchexpression_constructor_exists():
    assert callable(xpand3::expression::SwitchExpression.__init__)


def test_xpand3::expression::switchexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::SwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::listliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::ListLiteral)


def test_xpand3::expression::listliteral_constructor_exists():
    assert callable(xpand3::expression::ListLiteral.__init__)


def test_xpand3::expression::listliteral_constructor_args():
    sig = inspect.signature(xpand3::expression::ListLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::cast_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::Cast)


def test_xpand3::expression::cast_constructor_exists():
    assert callable(xpand3::expression::Cast.__init__)


def test_xpand3::expression::cast_constructor_args():
    sig = inspect.signature(xpand3::expression::Cast.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(BinaryOperation)


def test_binaryoperation_constructor_exists():
    assert callable(BinaryOperation.__init__)


def test_binaryoperation_constructor_args():
    sig = inspect.signature(BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::booleanoperation_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::BooleanOperation)


def test_xpand3::expression::booleanoperation_constructor_exists():
    assert callable(xpand3::expression::BooleanOperation.__init__)


def test_xpand3::expression::booleanoperation_constructor_args():
    sig = inspect.signature(xpand3::expression::BooleanOperation.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::abstractexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::AbstractExpression)


def test_xpand3::expression::abstractexpression_constructor_exists():
    assert callable(xpand3::expression::AbstractExpression.__init__)


def test_xpand3::expression::abstractexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::declaredparameter_is_not_abstract():
    assert not inspect.isabstract(xpand3::DeclaredParameter)


def test_xpand3::declaredparameter_constructor_exists():
    assert callable(xpand3::DeclaredParameter.__init__)


def test_xpand3::declaredparameter_constructor_args():
    sig = inspect.signature(xpand3::DeclaredParameter.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::ifexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::IfExpression)


def test_xpand3::expression::ifexpression_constructor_exists():
    assert callable(xpand3::expression::IfExpression.__init__)


def test_xpand3::expression::ifexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::globalvarexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::GlobalVarExpression)


def test_xpand3::expression::globalvarexpression_constructor_exists():
    assert callable(xpand3::expression::GlobalVarExpression.__init__)


def test_xpand3::expression::globalvarexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::GlobalVarExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecall_is_not_abstract():
    assert not inspect.isabstract(FeatureCall)


def test_featurecall_constructor_exists():
    assert callable(FeatureCall.__init__)


def test_featurecall_constructor_args():
    sig = inspect.signature(FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::operationcall_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::OperationCall)


def test_xpand3::expression::operationcall_constructor_exists():
    assert callable(xpand3::expression::OperationCall.__init__)


def test_xpand3::expression::operationcall_constructor_args():
    sig = inspect.signature(xpand3::expression::OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::typeselectexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::TypeSelectExpression)


def test_xpand3::expression::typeselectexpression_constructor_exists():
    assert callable(xpand3::expression::TypeSelectExpression.__init__)


def test_xpand3::expression::typeselectexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::TypeSelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::collectionexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::CollectionExpression)


def test_xpand3::expression::collectionexpression_constructor_exists():
    assert callable(xpand3::expression::CollectionExpression.__init__)


def test_xpand3::expression::collectionexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::featurecall_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::FeatureCall)


def test_xpand3::expression::featurecall_constructor_exists():
    assert callable(xpand3::expression::FeatureCall.__init__)


def test_xpand3::expression::featurecall_constructor_args():
    sig = inspect.signature(xpand3::expression::FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::expression::constructorcallexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3::expression::ConstructorCallExpression)


def test_xpand3::expression::constructorcallexpression_constructor_exists():
    assert callable(xpand3::expression::ConstructorCallExpression.__init__)


def test_xpand3::expression::constructorcallexpression_constructor_args():
    sig = inspect.signature(xpand3::expression::ConstructorCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::identifier_is_not_abstract():
    assert not inspect.isabstract(xpand3::Identifier)


def test_xpand3::identifier_constructor_exists():
    assert callable(xpand3::Identifier.__init__)


def test_xpand3::identifier_constructor_args():
    sig = inspect.signature(xpand3::Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xpand3::identifier_has_value():
    assert hasattr(xpand3::Identifier, "value")
    descriptor = None
    for klass in xpand3::Identifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractDeclaration)


def test_abstractdeclaration_constructor_exists():
    assert callable(AbstractDeclaration.__init__)


def test_abstractdeclaration_constructor_args():
    sig = inspect.signature(AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xpand3::declaration::check_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::Check)


def test_xpand3::declaration::check_constructor_exists():
    assert callable(xpand3::declaration::Check.__init__)


def test_xpand3::declaration::check_constructor_args():
    sig = inspect.signature(xpand3::declaration::Check.__init__)
    params = list(sig.parameters.keys())
    assert "errorSeverity" in params, "Missing parameter 'errorSeverity'"
    assert "feature" in params, "Missing parameter 'feature'"

def test_xpand3::declaration::check_has_errorSeverity():
    assert hasattr(xpand3::declaration::Check, "errorSeverity")
    descriptor = None
    for klass in xpand3::declaration::Check.__mro__:
        if "errorSeverity" in klass.__dict__:
            descriptor = klass.__dict__["errorSeverity"]
            break
    assert isinstance(descriptor, property)

def test_xpand3::declaration::check_has_feature():
    assert hasattr(xpand3::declaration::Check, "feature")
    descriptor = None
    for klass in xpand3::declaration::Check.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_xpand3::declaration::abstractaspect_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::AbstractAspect)


def test_xpand3::declaration::abstractaspect_constructor_exists():
    assert callable(xpand3::declaration::AbstractAspect.__init__)


def test_xpand3::declaration::abstractaspect_constructor_args():
    sig = inspect.signature(xpand3::declaration::AbstractAspect.__init__)
    params = list(sig.parameters.keys())
    assert "wildparams" in params, "Missing parameter 'wildparams'"

def test_xpand3::declaration::abstractaspect_has_wildparams():
    assert hasattr(xpand3::declaration::AbstractAspect, "wildparams")
    descriptor = None
    for klass in xpand3::declaration::AbstractAspect.__mro__:
        if "wildparams" in klass.__dict__:
            descriptor = klass.__dict__["wildparams"]
            break
    assert isinstance(descriptor, property)



def test_xpand3::declaration::abstractnameddeclaration_is_not_abstract():
    assert not inspect.isabstract(xpand3::declaration::AbstractNamedDeclaration)


def test_xpand3::declaration::abstractnameddeclaration_constructor_exists():
    assert callable(xpand3::declaration::AbstractNamedDeclaration.__init__)


def test_xpand3::declaration::abstractnameddeclaration_constructor_args():
    sig = inspect.signature(xpand3::declaration::AbstractNamedDeclaration.__init__)
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
SyntaxElement_strategy = st.builds(
    SyntaxElement,
)
xpand3::ImportStatement_strategy = st.builds(
    xpand3::ImportStatement,
    exported=
        st.booleans()
)
xpand3::File_strategy = st.builds(
    xpand3::File,
)
xpand3::SyntaxElement_strategy = st.builds(
    xpand3::SyntaxElement,
    line=
        st.integers(),
    fileName=
        safe_text,
    end=
        st.integers(),
    start=
        st.integers()
)
AbstractNamedDeclaration_strategy = st.builds(
    AbstractNamedDeclaration,
)
xpand3::declaration::Extension_strategy = st.builds(
    xpand3::declaration::Extension,
    cached=
        st.booleans()
)
xpand3::declaration::JavaExtension_strategy = st.builds(
    xpand3::declaration::JavaExtension,
)
xpand3::declaration::Definition_strategy = st.builds(
    xpand3::declaration::Definition,
)
declaration::xpand3::Identifier_strategy = st.builds(
    declaration::xpand3::Identifier,
)
declaration::xpand3::DeclaredParameter_strategy = st.builds(
    declaration::xpand3::DeclaredParameter,
)
Extension_strategy = st.builds(
    Extension,
)
xpand3::declaration::CreateExtension_strategy = st.builds(
    xpand3::declaration::CreateExtension,
)
AbstractAspect_strategy = st.builds(
    AbstractAspect,
)
xpand3::declaration::DefinitionAspect_strategy = st.builds(
    xpand3::declaration::DefinitionAspect,
)
xpand3::declaration::ExtensionAspect_strategy = st.builds(
    xpand3::declaration::ExtensionAspect,
)
AbstractStatementWithBody_strategy = st.builds(
    AbstractStatementWithBody,
)
xpand3::statement::ForEachStatement_strategy = st.builds(
    xpand3::statement::ForEachStatement,
)
xpand3::statement::IfStatement_strategy = st.builds(
    xpand3::statement::IfStatement,
)
xpand3::statement::FileStatement_strategy = st.builds(
    xpand3::statement::FileStatement,
    once=
        st.booleans()
)
declaration::xpand3::File_strategy = st.builds(
    declaration::xpand3::File,
)
xpand3::declaration::AbstractDeclaration_strategy = st.builds(
    xpand3::declaration::AbstractDeclaration,
    isPrivate=
        st.booleans()
)
xpand3::statement::ProtectStatement_strategy = st.builds(
    xpand3::statement::ProtectStatement,
    disable=
        st.booleans()
)
xpand3::statement::LetStatement_strategy = st.builds(
    xpand3::statement::LetStatement,
)
IfStatement_strategy = st.builds(
    IfStatement,
)
statement::xpand3::Identifier_strategy = st.builds(
    statement::xpand3::Identifier,
)
AbstractStatement_strategy = st.builds(
    AbstractStatement,
)
xpand3::statement::ExpressionStatement_strategy = st.builds(
    xpand3::statement::ExpressionStatement,
)
xpand3::statement::AbstractStatementWithBody_strategy = st.builds(
    xpand3::statement::AbstractStatementWithBody,
)
xpand3::statement::TextStatement_strategy = st.builds(
    xpand3::statement::TextStatement,
    deleteLine=
        st.booleans(),
    value=
        safe_text
)
xpand3::statement::ErrorStatement_strategy = st.builds(
    xpand3::statement::ErrorStatement,
)
xpand3::statement::ExpandStatement_strategy = st.builds(
    xpand3::statement::ExpandStatement,
    foreach=
        st.booleans()
)
xpand3::statement::AbstractStatement_strategy = st.builds(
    xpand3::statement::AbstractStatement,
)
xpand3::expression::Case_strategy = st.builds(
    xpand3::expression::Case,
)
Case_strategy = st.builds(
    Case,
)
Literal_strategy = st.builds(
    Literal,
)
xpand3::expression::IntegerLiteral_strategy = st.builds(
    xpand3::expression::IntegerLiteral,
)
xpand3::expression::RealLiteral_strategy = st.builds(
    xpand3::expression::RealLiteral,
)
xpand3::expression::StringLiteral_strategy = st.builds(
    xpand3::expression::StringLiteral,
)
xpand3::expression::NullLiteral_strategy = st.builds(
    xpand3::expression::NullLiteral,
)
xpand3::expression::BooleanLiteral_strategy = st.builds(
    xpand3::expression::BooleanLiteral,
)
expression::xpand3::Identifier_strategy = st.builds(
    expression::xpand3::Identifier,
)
AbstractExpression_strategy = st.builds(
    AbstractExpression,
)
xpand3::expression::Literal_strategy = st.builds(
    xpand3::expression::Literal,
)
xpand3::expression::BinaryOperation_strategy = st.builds(
    xpand3::expression::BinaryOperation,
)
xpand3::expression::UnaryOperation_strategy = st.builds(
    xpand3::expression::UnaryOperation,
)
xpand3::expression::LetExpression_strategy = st.builds(
    xpand3::expression::LetExpression,
)
xpand3::expression::ChainExpression_strategy = st.builds(
    xpand3::expression::ChainExpression,
)
xpand3::expression::SwitchExpression_strategy = st.builds(
    xpand3::expression::SwitchExpression,
)
xpand3::expression::ListLiteral_strategy = st.builds(
    xpand3::expression::ListLiteral,
)
xpand3::expression::Cast_strategy = st.builds(
    xpand3::expression::Cast,
)
BinaryOperation_strategy = st.builds(
    BinaryOperation,
)
xpand3::expression::BooleanOperation_strategy = st.builds(
    xpand3::expression::BooleanOperation,
)
xpand3::expression::AbstractExpression_strategy = st.builds(
    xpand3::expression::AbstractExpression,
)
xpand3::DeclaredParameter_strategy = st.builds(
    xpand3::DeclaredParameter,
)
xpand3::expression::IfExpression_strategy = st.builds(
    xpand3::expression::IfExpression,
)
xpand3::expression::GlobalVarExpression_strategy = st.builds(
    xpand3::expression::GlobalVarExpression,
)
FeatureCall_strategy = st.builds(
    FeatureCall,
)
xpand3::expression::OperationCall_strategy = st.builds(
    xpand3::expression::OperationCall,
)
xpand3::expression::TypeSelectExpression_strategy = st.builds(
    xpand3::expression::TypeSelectExpression,
)
xpand3::expression::CollectionExpression_strategy = st.builds(
    xpand3::expression::CollectionExpression,
)
xpand3::expression::FeatureCall_strategy = st.builds(
    xpand3::expression::FeatureCall,
)
xpand3::expression::ConstructorCallExpression_strategy = st.builds(
    xpand3::expression::ConstructorCallExpression,
)
xpand3::Identifier_strategy = st.builds(
    xpand3::Identifier,
    value=
        safe_text
)
AbstractDeclaration_strategy = st.builds(
    AbstractDeclaration,
)
xpand3::declaration::Check_strategy = st.builds(
    xpand3::declaration::Check,
    errorSeverity=
        st.booleans(),
    feature=
        safe_text
)
xpand3::declaration::AbstractAspect_strategy = st.builds(
    xpand3::declaration::AbstractAspect,
    wildparams=
        st.booleans()
)
xpand3::declaration::AbstractNamedDeclaration_strategy = st.builds(
    xpand3::declaration::AbstractNamedDeclaration,
)

@given(instance=SyntaxElement_strategy)
@settings(max_examples=50)
def test_syntaxelement_instantiation(instance):
    assert isinstance(instance, SyntaxElement)

@given(instance=xpand3::ImportStatement_strategy)
@settings(max_examples=50)
def test_xpand3::importstatement_instantiation(instance):
    assert isinstance(instance, xpand3::ImportStatement)

@given(instance=xpand3::ImportStatement_strategy)
def test_xpand3::importstatement_exported_type(instance):
    assert isinstance(instance.exported, bool)


@given(instance=xpand3::ImportStatement_strategy)
def test_xpand3::importstatement_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original

@given(instance=xpand3::File_strategy)
@settings(max_examples=50)
def test_xpand3::file_instantiation(instance):
    assert isinstance(instance, xpand3::File)

@given(instance=xpand3::SyntaxElement_strategy)
@settings(max_examples=50)
def test_xpand3::syntaxelement_instantiation(instance):
    assert isinstance(instance, xpand3::SyntaxElement)

@given(instance=xpand3::SyntaxElement_strategy)
def test_xpand3::syntaxelement_line_type(instance):
    assert isinstance(instance.line, int)


@given(instance=xpand3::SyntaxElement_strategy)
def test_xpand3::syntaxelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=xpand3::SyntaxElement_strategy)
def test_xpand3::syntaxelement_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=xpand3::SyntaxElement_strategy)
def test_xpand3::syntaxelement_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=xpand3::SyntaxElement_strategy)
def test_xpand3::syntaxelement_end_type(instance):
    assert isinstance(instance.end, int)


@given(instance=xpand3::SyntaxElement_strategy)
def test_xpand3::syntaxelement_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=xpand3::SyntaxElement_strategy)
def test_xpand3::syntaxelement_start_type(instance):
    assert isinstance(instance.start, int)


@given(instance=xpand3::SyntaxElement_strategy)
def test_xpand3::syntaxelement_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=AbstractNamedDeclaration_strategy)
@settings(max_examples=50)
def test_abstractnameddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractNamedDeclaration)

@given(instance=xpand3::declaration::Extension_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::extension_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::Extension)

@given(instance=xpand3::declaration::Extension_strategy)
def test_xpand3::declaration::extension_cached_type(instance):
    assert isinstance(instance.cached, bool)


@given(instance=xpand3::declaration::Extension_strategy)
def test_xpand3::declaration::extension_cached_setter(instance):
    original = instance.cached
    instance.cached = original
    assert instance.cached == original

@given(instance=xpand3::declaration::JavaExtension_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::javaextension_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::JavaExtension)

@given(instance=xpand3::declaration::Definition_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::definition_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::Definition)

@given(instance=declaration::xpand3::Identifier_strategy)
@settings(max_examples=50)
def test_declaration::xpand3::identifier_instantiation(instance):
    assert isinstance(instance, declaration::xpand3::Identifier)

@given(instance=declaration::xpand3::DeclaredParameter_strategy)
@settings(max_examples=50)
def test_declaration::xpand3::declaredparameter_instantiation(instance):
    assert isinstance(instance, declaration::xpand3::DeclaredParameter)

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)

@given(instance=xpand3::declaration::CreateExtension_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::createextension_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::CreateExtension)

@given(instance=AbstractAspect_strategy)
@settings(max_examples=50)
def test_abstractaspect_instantiation(instance):
    assert isinstance(instance, AbstractAspect)

@given(instance=xpand3::declaration::DefinitionAspect_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::definitionaspect_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::DefinitionAspect)

@given(instance=xpand3::declaration::ExtensionAspect_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::extensionaspect_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::ExtensionAspect)

@given(instance=AbstractStatementWithBody_strategy)
@settings(max_examples=50)
def test_abstractstatementwithbody_instantiation(instance):
    assert isinstance(instance, AbstractStatementWithBody)

@given(instance=xpand3::statement::ForEachStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::foreachstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::ForEachStatement)

@given(instance=xpand3::statement::IfStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::ifstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::IfStatement)

@given(instance=xpand3::statement::FileStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::filestatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::FileStatement)

@given(instance=xpand3::statement::FileStatement_strategy)
def test_xpand3::statement::filestatement_once_type(instance):
    assert isinstance(instance.once, bool)


@given(instance=xpand3::statement::FileStatement_strategy)
def test_xpand3::statement::filestatement_once_setter(instance):
    original = instance.once
    instance.once = original
    assert instance.once == original

@given(instance=declaration::xpand3::File_strategy)
@settings(max_examples=50)
def test_declaration::xpand3::file_instantiation(instance):
    assert isinstance(instance, declaration::xpand3::File)

@given(instance=xpand3::declaration::AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::abstractdeclaration_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::AbstractDeclaration)

@given(instance=xpand3::declaration::AbstractDeclaration_strategy)
def test_xpand3::declaration::abstractdeclaration_isPrivate_type(instance):
    assert isinstance(instance.isPrivate, bool)


@given(instance=xpand3::declaration::AbstractDeclaration_strategy)
def test_xpand3::declaration::abstractdeclaration_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original

@given(instance=xpand3::statement::ProtectStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::protectstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::ProtectStatement)

@given(instance=xpand3::statement::ProtectStatement_strategy)
def test_xpand3::statement::protectstatement_disable_type(instance):
    assert isinstance(instance.disable, bool)


@given(instance=xpand3::statement::ProtectStatement_strategy)
def test_xpand3::statement::protectstatement_disable_setter(instance):
    original = instance.disable
    instance.disable = original
    assert instance.disable == original

@given(instance=xpand3::statement::LetStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::letstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::LetStatement)

@given(instance=IfStatement_strategy)
@settings(max_examples=50)
def test_ifstatement_instantiation(instance):
    assert isinstance(instance, IfStatement)

@given(instance=statement::xpand3::Identifier_strategy)
@settings(max_examples=50)
def test_statement::xpand3::identifier_instantiation(instance):
    assert isinstance(instance, statement::xpand3::Identifier)

@given(instance=AbstractStatement_strategy)
@settings(max_examples=50)
def test_abstractstatement_instantiation(instance):
    assert isinstance(instance, AbstractStatement)

@given(instance=xpand3::statement::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::expressionstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::ExpressionStatement)

@given(instance=xpand3::statement::AbstractStatementWithBody_strategy)
@settings(max_examples=50)
def test_xpand3::statement::abstractstatementwithbody_instantiation(instance):
    assert isinstance(instance, xpand3::statement::AbstractStatementWithBody)

@given(instance=xpand3::statement::TextStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::textstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::TextStatement)

@given(instance=xpand3::statement::TextStatement_strategy)
def test_xpand3::statement::textstatement_deleteLine_type(instance):
    assert isinstance(instance.deleteLine, bool)


@given(instance=xpand3::statement::TextStatement_strategy)
def test_xpand3::statement::textstatement_deleteLine_setter(instance):
    original = instance.deleteLine
    instance.deleteLine = original
    assert instance.deleteLine == original

@given(instance=xpand3::statement::TextStatement_strategy)
def test_xpand3::statement::textstatement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xpand3::statement::TextStatement_strategy)
def test_xpand3::statement::textstatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xpand3::statement::ErrorStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::errorstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::ErrorStatement)

@given(instance=xpand3::statement::ExpandStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::expandstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::ExpandStatement)

@given(instance=xpand3::statement::ExpandStatement_strategy)
def test_xpand3::statement::expandstatement_foreach_type(instance):
    assert isinstance(instance.foreach, bool)


@given(instance=xpand3::statement::ExpandStatement_strategy)
def test_xpand3::statement::expandstatement_foreach_setter(instance):
    original = instance.foreach
    instance.foreach = original
    assert instance.foreach == original

@given(instance=xpand3::statement::AbstractStatement_strategy)
@settings(max_examples=50)
def test_xpand3::statement::abstractstatement_instantiation(instance):
    assert isinstance(instance, xpand3::statement::AbstractStatement)

@given(instance=xpand3::expression::Case_strategy)
@settings(max_examples=50)
def test_xpand3::expression::case_instantiation(instance):
    assert isinstance(instance, xpand3::expression::Case)

@given(instance=Case_strategy)
@settings(max_examples=50)
def test_case_instantiation(instance):
    assert isinstance(instance, Case)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=xpand3::expression::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_xpand3::expression::integerliteral_instantiation(instance):
    assert isinstance(instance, xpand3::expression::IntegerLiteral)

@given(instance=xpand3::expression::RealLiteral_strategy)
@settings(max_examples=50)
def test_xpand3::expression::realliteral_instantiation(instance):
    assert isinstance(instance, xpand3::expression::RealLiteral)

@given(instance=xpand3::expression::StringLiteral_strategy)
@settings(max_examples=50)
def test_xpand3::expression::stringliteral_instantiation(instance):
    assert isinstance(instance, xpand3::expression::StringLiteral)

@given(instance=xpand3::expression::NullLiteral_strategy)
@settings(max_examples=50)
def test_xpand3::expression::nullliteral_instantiation(instance):
    assert isinstance(instance, xpand3::expression::NullLiteral)

@given(instance=xpand3::expression::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_xpand3::expression::booleanliteral_instantiation(instance):
    assert isinstance(instance, xpand3::expression::BooleanLiteral)

@given(instance=expression::xpand3::Identifier_strategy)
@settings(max_examples=50)
def test_expression::xpand3::identifier_instantiation(instance):
    assert isinstance(instance, expression::xpand3::Identifier)

@given(instance=AbstractExpression_strategy)
@settings(max_examples=50)
def test_abstractexpression_instantiation(instance):
    assert isinstance(instance, AbstractExpression)

@given(instance=xpand3::expression::Literal_strategy)
@settings(max_examples=50)
def test_xpand3::expression::literal_instantiation(instance):
    assert isinstance(instance, xpand3::expression::Literal)

@given(instance=xpand3::expression::BinaryOperation_strategy)
@settings(max_examples=50)
def test_xpand3::expression::binaryoperation_instantiation(instance):
    assert isinstance(instance, xpand3::expression::BinaryOperation)

@given(instance=xpand3::expression::UnaryOperation_strategy)
@settings(max_examples=50)
def test_xpand3::expression::unaryoperation_instantiation(instance):
    assert isinstance(instance, xpand3::expression::UnaryOperation)

@given(instance=xpand3::expression::LetExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::letexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::LetExpression)

@given(instance=xpand3::expression::ChainExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::chainexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::ChainExpression)

@given(instance=xpand3::expression::SwitchExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::switchexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::SwitchExpression)

@given(instance=xpand3::expression::ListLiteral_strategy)
@settings(max_examples=50)
def test_xpand3::expression::listliteral_instantiation(instance):
    assert isinstance(instance, xpand3::expression::ListLiteral)

@given(instance=xpand3::expression::Cast_strategy)
@settings(max_examples=50)
def test_xpand3::expression::cast_instantiation(instance):
    assert isinstance(instance, xpand3::expression::Cast)

@given(instance=BinaryOperation_strategy)
@settings(max_examples=50)
def test_binaryoperation_instantiation(instance):
    assert isinstance(instance, BinaryOperation)

@given(instance=xpand3::expression::BooleanOperation_strategy)
@settings(max_examples=50)
def test_xpand3::expression::booleanoperation_instantiation(instance):
    assert isinstance(instance, xpand3::expression::BooleanOperation)

@given(instance=xpand3::expression::AbstractExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::abstractexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::AbstractExpression)

@given(instance=xpand3::DeclaredParameter_strategy)
@settings(max_examples=50)
def test_xpand3::declaredparameter_instantiation(instance):
    assert isinstance(instance, xpand3::DeclaredParameter)

@given(instance=xpand3::expression::IfExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::ifexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::IfExpression)

@given(instance=xpand3::expression::GlobalVarExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::globalvarexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::GlobalVarExpression)

@given(instance=FeatureCall_strategy)
@settings(max_examples=50)
def test_featurecall_instantiation(instance):
    assert isinstance(instance, FeatureCall)

@given(instance=xpand3::expression::OperationCall_strategy)
@settings(max_examples=50)
def test_xpand3::expression::operationcall_instantiation(instance):
    assert isinstance(instance, xpand3::expression::OperationCall)

@given(instance=xpand3::expression::TypeSelectExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::typeselectexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::TypeSelectExpression)

@given(instance=xpand3::expression::CollectionExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::collectionexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::CollectionExpression)

@given(instance=xpand3::expression::FeatureCall_strategy)
@settings(max_examples=50)
def test_xpand3::expression::featurecall_instantiation(instance):
    assert isinstance(instance, xpand3::expression::FeatureCall)

@given(instance=xpand3::expression::ConstructorCallExpression_strategy)
@settings(max_examples=50)
def test_xpand3::expression::constructorcallexpression_instantiation(instance):
    assert isinstance(instance, xpand3::expression::ConstructorCallExpression)

@given(instance=xpand3::Identifier_strategy)
@settings(max_examples=50)
def test_xpand3::identifier_instantiation(instance):
    assert isinstance(instance, xpand3::Identifier)

@given(instance=xpand3::Identifier_strategy)
def test_xpand3::identifier_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xpand3::Identifier_strategy)
def test_xpand3::identifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, AbstractDeclaration)

@given(instance=xpand3::declaration::Check_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::check_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::Check)

@given(instance=xpand3::declaration::Check_strategy)
def test_xpand3::declaration::check_errorSeverity_type(instance):
    assert isinstance(instance.errorSeverity, bool)


@given(instance=xpand3::declaration::Check_strategy)
def test_xpand3::declaration::check_errorSeverity_setter(instance):
    original = instance.errorSeverity
    instance.errorSeverity = original
    assert instance.errorSeverity == original

@given(instance=xpand3::declaration::Check_strategy)
def test_xpand3::declaration::check_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=xpand3::declaration::Check_strategy)
def test_xpand3::declaration::check_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=xpand3::declaration::AbstractAspect_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::abstractaspect_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::AbstractAspect)

@given(instance=xpand3::declaration::AbstractAspect_strategy)
def test_xpand3::declaration::abstractaspect_wildparams_type(instance):
    assert isinstance(instance.wildparams, bool)


@given(instance=xpand3::declaration::AbstractAspect_strategy)
def test_xpand3::declaration::abstractaspect_wildparams_setter(instance):
    original = instance.wildparams
    instance.wildparams = original
    assert instance.wildparams == original

@given(instance=xpand3::declaration::AbstractNamedDeclaration_strategy)
@settings(max_examples=50)
def test_xpand3::declaration::abstractnameddeclaration_instantiation(instance):
    assert isinstance(instance, xpand3::declaration::AbstractNamedDeclaration)
