import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractNamedDeclaration,
    xpand3_declaration_JavaExtension,
    xpand3_declaration_Extension,
    xpand3_declaration_Definition,
    declaration_xpand3_Identifier,
    declaration_xpand3_DeclaredParameter,
    Extension,
    xpand3_declaration_CreateExtension,
    AbstractAspect,
    xpand3_declaration_DefinitionAspect,
    xpand3_declaration_ExtensionAspect,
    AbstractStatementWithBody,
    xpand3_statement_ForEachStatement,
    xpand3_statement_IfStatement,
    xpand3_statement_FileStatement,
    declaration_xpand3_File,
    xpand3_statement_ProtectStatement,
    xpand3_statement_LetStatement,
    IfStatement,
    statement_xpand3_Identifier,
    AbstractStatement,
    xpand3_statement_ErrorStatement,
    xpand3_statement_ExpressionStatement,
    xpand3_statement_TextStatement,
    xpand3_statement_AbstractStatementWithBody,
    xpand3_statement_ExpandStatement,
    Case,
    Literal,
    xpand3_expression_IntegerLiteral,
    xpand3_expression_RealLiteral,
    xpand3_expression_StringLiteral,
    xpand3_expression_NullLiteral,
    xpand3_expression_BooleanLiteral,
    expression_xpand3_Identifier,
    AbstractExpression,
    xpand3_expression_BinaryOperation,
    xpand3_expression_SwitchExpression,
    xpand3_expression_ChainExpression,
    xpand3_expression_Literal,
    xpand3_expression_LetExpression,
    xpand3_expression_ListLiteral,
    xpand3_expression_UnaryOperation,
    xpand3_expression_Cast,
    BinaryOperation,
    xpand3_expression_BooleanOperation,
    xpand3_expression_IfExpression,
    xpand3_expression_GlobalVarExpression,
    FeatureCall,
    xpand3_expression_TypeSelectExpression,
    xpand3_expression_OperationCall,
    xpand3_expression_CollectionExpression,
    xpand3_expression_FeatureCall,
    xpand3_expression_ConstructorCallExpression,
    AbstractDeclaration,
    xpand3_declaration_Check,
    xpand3_declaration_AbstractAspect,
    xpand3_declaration_AbstractNamedDeclaration,
    SyntaxElement,
    xpand3_statement_AbstractStatement,
    xpand3_expression_AbstractExpression,
    xpand3_expression_Case,
    xpand3_declaration_AbstractDeclaration,
    xpand3_Identifier,
    xpand3_DeclaredParameter,
    xpand3_ImportStatement,
    xpand3_File,
    xpand3_SyntaxElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractnameddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractNamedDeclaration)


def test_abstractnameddeclaration_constructor_exists():
    assert callable(AbstractNamedDeclaration.__init__)


def test_abstractnameddeclaration_constructor_args():
    sig = inspect.signature(AbstractNamedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_declaration_javaextension_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_JavaExtension)


def test_xpand3_declaration_javaextension_constructor_exists():
    assert callable(xpand3_declaration_JavaExtension.__init__)


def test_xpand3_declaration_javaextension_constructor_args():
    sig = inspect.signature(xpand3_declaration_JavaExtension.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_declaration_extension_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_Extension)


def test_xpand3_declaration_extension_constructor_exists():
    assert callable(xpand3_declaration_Extension.__init__)


def test_xpand3_declaration_extension_constructor_args():
    sig = inspect.signature(xpand3_declaration_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "cached" in params, "Missing parameter 'cached'"

def test_xpand3_declaration_extension_has_cached():
    assert hasattr(xpand3_declaration_Extension, "cached")
    descriptor = None
    for klass in xpand3_declaration_Extension.__mro__:
        if "cached" in klass.__dict__:
            descriptor = klass.__dict__["cached"]
            break
    assert isinstance(descriptor, property)



def test_xpand3_declaration_definition_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_Definition)


def test_xpand3_declaration_definition_constructor_exists():
    assert callable(xpand3_declaration_Definition.__init__)


def test_xpand3_declaration_definition_constructor_args():
    sig = inspect.signature(xpand3_declaration_Definition.__init__)
    params = list(sig.parameters.keys())



def test_declaration_xpand3_identifier_is_not_abstract():
    assert not inspect.isabstract(declaration_xpand3_Identifier)


def test_declaration_xpand3_identifier_constructor_exists():
    assert callable(declaration_xpand3_Identifier.__init__)


def test_declaration_xpand3_identifier_constructor_args():
    sig = inspect.signature(declaration_xpand3_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_declaration_xpand3_declaredparameter_is_not_abstract():
    assert not inspect.isabstract(declaration_xpand3_DeclaredParameter)


def test_declaration_xpand3_declaredparameter_constructor_exists():
    assert callable(declaration_xpand3_DeclaredParameter.__init__)


def test_declaration_xpand3_declaredparameter_constructor_args():
    sig = inspect.signature(declaration_xpand3_DeclaredParameter.__init__)
    params = list(sig.parameters.keys())



def test_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_declaration_createextension_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_CreateExtension)


def test_xpand3_declaration_createextension_constructor_exists():
    assert callable(xpand3_declaration_CreateExtension.__init__)


def test_xpand3_declaration_createextension_constructor_args():
    sig = inspect.signature(xpand3_declaration_CreateExtension.__init__)
    params = list(sig.parameters.keys())



def test_abstractaspect_is_not_abstract():
    assert not inspect.isabstract(AbstractAspect)


def test_abstractaspect_constructor_exists():
    assert callable(AbstractAspect.__init__)


def test_abstractaspect_constructor_args():
    sig = inspect.signature(AbstractAspect.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_declaration_definitionaspect_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_DefinitionAspect)


def test_xpand3_declaration_definitionaspect_constructor_exists():
    assert callable(xpand3_declaration_DefinitionAspect.__init__)


def test_xpand3_declaration_definitionaspect_constructor_args():
    sig = inspect.signature(xpand3_declaration_DefinitionAspect.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_declaration_extensionaspect_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_ExtensionAspect)


def test_xpand3_declaration_extensionaspect_constructor_exists():
    assert callable(xpand3_declaration_ExtensionAspect.__init__)


def test_xpand3_declaration_extensionaspect_constructor_args():
    sig = inspect.signature(xpand3_declaration_ExtensionAspect.__init__)
    params = list(sig.parameters.keys())



def test_abstractstatementwithbody_is_not_abstract():
    assert not inspect.isabstract(AbstractStatementWithBody)


def test_abstractstatementwithbody_constructor_exists():
    assert callable(AbstractStatementWithBody.__init__)


def test_abstractstatementwithbody_constructor_args():
    sig = inspect.signature(AbstractStatementWithBody.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_ForEachStatement)


def test_xpand3_statement_foreachstatement_constructor_exists():
    assert callable(xpand3_statement_ForEachStatement.__init__)


def test_xpand3_statement_foreachstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_ifstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_IfStatement)


def test_xpand3_statement_ifstatement_constructor_exists():
    assert callable(xpand3_statement_IfStatement.__init__)


def test_xpand3_statement_ifstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_filestatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_FileStatement)


def test_xpand3_statement_filestatement_constructor_exists():
    assert callable(xpand3_statement_FileStatement.__init__)


def test_xpand3_statement_filestatement_constructor_args():
    sig = inspect.signature(xpand3_statement_FileStatement.__init__)
    params = list(sig.parameters.keys())
    assert "once" in params, "Missing parameter 'once'"

def test_xpand3_statement_filestatement_has_once():
    assert hasattr(xpand3_statement_FileStatement, "once")
    descriptor = None
    for klass in xpand3_statement_FileStatement.__mro__:
        if "once" in klass.__dict__:
            descriptor = klass.__dict__["once"]
            break
    assert isinstance(descriptor, property)



def test_declaration_xpand3_file_is_not_abstract():
    assert not inspect.isabstract(declaration_xpand3_File)


def test_declaration_xpand3_file_constructor_exists():
    assert callable(declaration_xpand3_File.__init__)


def test_declaration_xpand3_file_constructor_args():
    sig = inspect.signature(declaration_xpand3_File.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_protectstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_ProtectStatement)


def test_xpand3_statement_protectstatement_constructor_exists():
    assert callable(xpand3_statement_ProtectStatement.__init__)


def test_xpand3_statement_protectstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_ProtectStatement.__init__)
    params = list(sig.parameters.keys())
    assert "disable" in params, "Missing parameter 'disable'"

def test_xpand3_statement_protectstatement_has_disable():
    assert hasattr(xpand3_statement_ProtectStatement, "disable")
    descriptor = None
    for klass in xpand3_statement_ProtectStatement.__mro__:
        if "disable" in klass.__dict__:
            descriptor = klass.__dict__["disable"]
            break
    assert isinstance(descriptor, property)



def test_xpand3_statement_letstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_LetStatement)


def test_xpand3_statement_letstatement_constructor_exists():
    assert callable(xpand3_statement_LetStatement.__init__)


def test_xpand3_statement_letstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_LetStatement.__init__)
    params = list(sig.parameters.keys())



def test_ifstatement_is_not_abstract():
    assert not inspect.isabstract(IfStatement)


def test_ifstatement_constructor_exists():
    assert callable(IfStatement.__init__)


def test_ifstatement_constructor_args():
    sig = inspect.signature(IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement_xpand3_identifier_is_not_abstract():
    assert not inspect.isabstract(statement_xpand3_Identifier)


def test_statement_xpand3_identifier_constructor_exists():
    assert callable(statement_xpand3_Identifier.__init__)


def test_statement_xpand3_identifier_constructor_args():
    sig = inspect.signature(statement_xpand3_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_abstractstatement_is_not_abstract():
    assert not inspect.isabstract(AbstractStatement)


def test_abstractstatement_constructor_exists():
    assert callable(AbstractStatement.__init__)


def test_abstractstatement_constructor_args():
    sig = inspect.signature(AbstractStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_errorstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_ErrorStatement)


def test_xpand3_statement_errorstatement_constructor_exists():
    assert callable(xpand3_statement_ErrorStatement.__init__)


def test_xpand3_statement_errorstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_ErrorStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_ExpressionStatement)


def test_xpand3_statement_expressionstatement_constructor_exists():
    assert callable(xpand3_statement_ExpressionStatement.__init__)


def test_xpand3_statement_expressionstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_textstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_TextStatement)


def test_xpand3_statement_textstatement_constructor_exists():
    assert callable(xpand3_statement_TextStatement.__init__)


def test_xpand3_statement_textstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_TextStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "deleteLine" in params, "Missing parameter 'deleteLine'"

def test_xpand3_statement_textstatement_has_value():
    assert hasattr(xpand3_statement_TextStatement, "value")
    descriptor = None
    for klass in xpand3_statement_TextStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xpand3_statement_textstatement_has_deleteLine():
    assert hasattr(xpand3_statement_TextStatement, "deleteLine")
    descriptor = None
    for klass in xpand3_statement_TextStatement.__mro__:
        if "deleteLine" in klass.__dict__:
            descriptor = klass.__dict__["deleteLine"]
            break
    assert isinstance(descriptor, property)



def test_xpand3_statement_abstractstatementwithbody_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_AbstractStatementWithBody)


def test_xpand3_statement_abstractstatementwithbody_constructor_exists():
    assert callable(xpand3_statement_AbstractStatementWithBody.__init__)


def test_xpand3_statement_abstractstatementwithbody_constructor_args():
    sig = inspect.signature(xpand3_statement_AbstractStatementWithBody.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_expandstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_ExpandStatement)


def test_xpand3_statement_expandstatement_constructor_exists():
    assert callable(xpand3_statement_ExpandStatement.__init__)


def test_xpand3_statement_expandstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_ExpandStatement.__init__)
    params = list(sig.parameters.keys())
    assert "foreach" in params, "Missing parameter 'foreach'"

def test_xpand3_statement_expandstatement_has_foreach():
    assert hasattr(xpand3_statement_ExpandStatement, "foreach")
    descriptor = None
    for klass in xpand3_statement_ExpandStatement.__mro__:
        if "foreach" in klass.__dict__:
            descriptor = klass.__dict__["foreach"]
            break
    assert isinstance(descriptor, property)



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



def test_xpand3_expression_integerliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_IntegerLiteral)


def test_xpand3_expression_integerliteral_constructor_exists():
    assert callable(xpand3_expression_IntegerLiteral.__init__)


def test_xpand3_expression_integerliteral_constructor_args():
    sig = inspect.signature(xpand3_expression_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_realliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_RealLiteral)


def test_xpand3_expression_realliteral_constructor_exists():
    assert callable(xpand3_expression_RealLiteral.__init__)


def test_xpand3_expression_realliteral_constructor_args():
    sig = inspect.signature(xpand3_expression_RealLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_stringliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_StringLiteral)


def test_xpand3_expression_stringliteral_constructor_exists():
    assert callable(xpand3_expression_StringLiteral.__init__)


def test_xpand3_expression_stringliteral_constructor_args():
    sig = inspect.signature(xpand3_expression_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_nullliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_NullLiteral)


def test_xpand3_expression_nullliteral_constructor_exists():
    assert callable(xpand3_expression_NullLiteral.__init__)


def test_xpand3_expression_nullliteral_constructor_args():
    sig = inspect.signature(xpand3_expression_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_BooleanLiteral)


def test_xpand3_expression_booleanliteral_constructor_exists():
    assert callable(xpand3_expression_BooleanLiteral.__init__)


def test_xpand3_expression_booleanliteral_constructor_args():
    sig = inspect.signature(xpand3_expression_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression_xpand3_identifier_is_not_abstract():
    assert not inspect.isabstract(expression_xpand3_Identifier)


def test_expression_xpand3_identifier_constructor_exists():
    assert callable(expression_xpand3_Identifier.__init__)


def test_expression_xpand3_identifier_constructor_args():
    sig = inspect.signature(expression_xpand3_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_abstractexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractExpression)


def test_abstractexpression_constructor_exists():
    assert callable(AbstractExpression.__init__)


def test_abstractexpression_constructor_args():
    sig = inspect.signature(AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_BinaryOperation)


def test_xpand3_expression_binaryoperation_constructor_exists():
    assert callable(xpand3_expression_BinaryOperation.__init__)


def test_xpand3_expression_binaryoperation_constructor_args():
    sig = inspect.signature(xpand3_expression_BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_switchexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_SwitchExpression)


def test_xpand3_expression_switchexpression_constructor_exists():
    assert callable(xpand3_expression_SwitchExpression.__init__)


def test_xpand3_expression_switchexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_SwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_chainexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_ChainExpression)


def test_xpand3_expression_chainexpression_constructor_exists():
    assert callable(xpand3_expression_ChainExpression.__init__)


def test_xpand3_expression_chainexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_ChainExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_literal_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_Literal)


def test_xpand3_expression_literal_constructor_exists():
    assert callable(xpand3_expression_Literal.__init__)


def test_xpand3_expression_literal_constructor_args():
    sig = inspect.signature(xpand3_expression_Literal.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_letexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_LetExpression)


def test_xpand3_expression_letexpression_constructor_exists():
    assert callable(xpand3_expression_LetExpression.__init__)


def test_xpand3_expression_letexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_listliteral_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_ListLiteral)


def test_xpand3_expression_listliteral_constructor_exists():
    assert callable(xpand3_expression_ListLiteral.__init__)


def test_xpand3_expression_listliteral_constructor_args():
    sig = inspect.signature(xpand3_expression_ListLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_unaryoperation_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_UnaryOperation)


def test_xpand3_expression_unaryoperation_constructor_exists():
    assert callable(xpand3_expression_UnaryOperation.__init__)


def test_xpand3_expression_unaryoperation_constructor_args():
    sig = inspect.signature(xpand3_expression_UnaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_cast_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_Cast)


def test_xpand3_expression_cast_constructor_exists():
    assert callable(xpand3_expression_Cast.__init__)


def test_xpand3_expression_cast_constructor_args():
    sig = inspect.signature(xpand3_expression_Cast.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(BinaryOperation)


def test_binaryoperation_constructor_exists():
    assert callable(BinaryOperation.__init__)


def test_binaryoperation_constructor_args():
    sig = inspect.signature(BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_booleanoperation_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_BooleanOperation)


def test_xpand3_expression_booleanoperation_constructor_exists():
    assert callable(xpand3_expression_BooleanOperation.__init__)


def test_xpand3_expression_booleanoperation_constructor_args():
    sig = inspect.signature(xpand3_expression_BooleanOperation.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_ifexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_IfExpression)


def test_xpand3_expression_ifexpression_constructor_exists():
    assert callable(xpand3_expression_IfExpression.__init__)


def test_xpand3_expression_ifexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_globalvarexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_GlobalVarExpression)


def test_xpand3_expression_globalvarexpression_constructor_exists():
    assert callable(xpand3_expression_GlobalVarExpression.__init__)


def test_xpand3_expression_globalvarexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_GlobalVarExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecall_is_not_abstract():
    assert not inspect.isabstract(FeatureCall)


def test_featurecall_constructor_exists():
    assert callable(FeatureCall.__init__)


def test_featurecall_constructor_args():
    sig = inspect.signature(FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_typeselectexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_TypeSelectExpression)


def test_xpand3_expression_typeselectexpression_constructor_exists():
    assert callable(xpand3_expression_TypeSelectExpression.__init__)


def test_xpand3_expression_typeselectexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_TypeSelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_operationcall_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_OperationCall)


def test_xpand3_expression_operationcall_constructor_exists():
    assert callable(xpand3_expression_OperationCall.__init__)


def test_xpand3_expression_operationcall_constructor_args():
    sig = inspect.signature(xpand3_expression_OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_CollectionExpression)


def test_xpand3_expression_collectionexpression_constructor_exists():
    assert callable(xpand3_expression_CollectionExpression.__init__)


def test_xpand3_expression_collectionexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_featurecall_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_FeatureCall)


def test_xpand3_expression_featurecall_constructor_exists():
    assert callable(xpand3_expression_FeatureCall.__init__)


def test_xpand3_expression_featurecall_constructor_args():
    sig = inspect.signature(xpand3_expression_FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_constructorcallexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_ConstructorCallExpression)


def test_xpand3_expression_constructorcallexpression_constructor_exists():
    assert callable(xpand3_expression_ConstructorCallExpression.__init__)


def test_xpand3_expression_constructorcallexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_ConstructorCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractDeclaration)


def test_abstractdeclaration_constructor_exists():
    assert callable(AbstractDeclaration.__init__)


def test_abstractdeclaration_constructor_args():
    sig = inspect.signature(AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_declaration_check_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_Check)


def test_xpand3_declaration_check_constructor_exists():
    assert callable(xpand3_declaration_Check.__init__)


def test_xpand3_declaration_check_constructor_args():
    sig = inspect.signature(xpand3_declaration_Check.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"
    assert "errorSeverity" in params, "Missing parameter 'errorSeverity'"

def test_xpand3_declaration_check_has_feature():
    assert hasattr(xpand3_declaration_Check, "feature")
    descriptor = None
    for klass in xpand3_declaration_Check.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)

def test_xpand3_declaration_check_has_errorSeverity():
    assert hasattr(xpand3_declaration_Check, "errorSeverity")
    descriptor = None
    for klass in xpand3_declaration_Check.__mro__:
        if "errorSeverity" in klass.__dict__:
            descriptor = klass.__dict__["errorSeverity"]
            break
    assert isinstance(descriptor, property)



def test_xpand3_declaration_abstractaspect_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_AbstractAspect)


def test_xpand3_declaration_abstractaspect_constructor_exists():
    assert callable(xpand3_declaration_AbstractAspect.__init__)


def test_xpand3_declaration_abstractaspect_constructor_args():
    sig = inspect.signature(xpand3_declaration_AbstractAspect.__init__)
    params = list(sig.parameters.keys())
    assert "wildparams" in params, "Missing parameter 'wildparams'"

def test_xpand3_declaration_abstractaspect_has_wildparams():
    assert hasattr(xpand3_declaration_AbstractAspect, "wildparams")
    descriptor = None
    for klass in xpand3_declaration_AbstractAspect.__mro__:
        if "wildparams" in klass.__dict__:
            descriptor = klass.__dict__["wildparams"]
            break
    assert isinstance(descriptor, property)



def test_xpand3_declaration_abstractnameddeclaration_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_AbstractNamedDeclaration)


def test_xpand3_declaration_abstractnameddeclaration_constructor_exists():
    assert callable(xpand3_declaration_AbstractNamedDeclaration.__init__)


def test_xpand3_declaration_abstractnameddeclaration_constructor_args():
    sig = inspect.signature(xpand3_declaration_AbstractNamedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_syntaxelement_is_not_abstract():
    assert not inspect.isabstract(SyntaxElement)


def test_syntaxelement_constructor_exists():
    assert callable(SyntaxElement.__init__)


def test_syntaxelement_constructor_args():
    sig = inspect.signature(SyntaxElement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_statement_abstractstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_statement_AbstractStatement)


def test_xpand3_statement_abstractstatement_constructor_exists():
    assert callable(xpand3_statement_AbstractStatement.__init__)


def test_xpand3_statement_abstractstatement_constructor_args():
    sig = inspect.signature(xpand3_statement_AbstractStatement.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_abstractexpression_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_AbstractExpression)


def test_xpand3_expression_abstractexpression_constructor_exists():
    assert callable(xpand3_expression_AbstractExpression.__init__)


def test_xpand3_expression_abstractexpression_constructor_args():
    sig = inspect.signature(xpand3_expression_AbstractExpression.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_expression_case_is_not_abstract():
    assert not inspect.isabstract(xpand3_expression_Case)


def test_xpand3_expression_case_constructor_exists():
    assert callable(xpand3_expression_Case.__init__)


def test_xpand3_expression_case_constructor_args():
    sig = inspect.signature(xpand3_expression_Case.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_declaration_abstractdeclaration_is_not_abstract():
    assert not inspect.isabstract(xpand3_declaration_AbstractDeclaration)


def test_xpand3_declaration_abstractdeclaration_constructor_exists():
    assert callable(xpand3_declaration_AbstractDeclaration.__init__)


def test_xpand3_declaration_abstractdeclaration_constructor_args():
    sig = inspect.signature(xpand3_declaration_AbstractDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"

def test_xpand3_declaration_abstractdeclaration_has_isPrivate():
    assert hasattr(xpand3_declaration_AbstractDeclaration, "isPrivate")
    descriptor = None
    for klass in xpand3_declaration_AbstractDeclaration.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)



def test_xpand3_identifier_is_not_abstract():
    assert not inspect.isabstract(xpand3_Identifier)


def test_xpand3_identifier_constructor_exists():
    assert callable(xpand3_Identifier.__init__)


def test_xpand3_identifier_constructor_args():
    sig = inspect.signature(xpand3_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xpand3_identifier_has_value():
    assert hasattr(xpand3_Identifier, "value")
    descriptor = None
    for klass in xpand3_Identifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xpand3_declaredparameter_is_not_abstract():
    assert not inspect.isabstract(xpand3_DeclaredParameter)


def test_xpand3_declaredparameter_constructor_exists():
    assert callable(xpand3_DeclaredParameter.__init__)


def test_xpand3_declaredparameter_constructor_args():
    sig = inspect.signature(xpand3_DeclaredParameter.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_importstatement_is_not_abstract():
    assert not inspect.isabstract(xpand3_ImportStatement)


def test_xpand3_importstatement_constructor_exists():
    assert callable(xpand3_ImportStatement.__init__)


def test_xpand3_importstatement_constructor_args():
    sig = inspect.signature(xpand3_ImportStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exported" in params, "Missing parameter 'exported'"

def test_xpand3_importstatement_has_exported():
    assert hasattr(xpand3_ImportStatement, "exported")
    descriptor = None
    for klass in xpand3_ImportStatement.__mro__:
        if "exported" in klass.__dict__:
            descriptor = klass.__dict__["exported"]
            break
    assert isinstance(descriptor, property)



def test_xpand3_file_is_not_abstract():
    assert not inspect.isabstract(xpand3_File)


def test_xpand3_file_constructor_exists():
    assert callable(xpand3_File.__init__)


def test_xpand3_file_constructor_args():
    sig = inspect.signature(xpand3_File.__init__)
    params = list(sig.parameters.keys())



def test_xpand3_syntaxelement_is_not_abstract():
    assert not inspect.isabstract(xpand3_SyntaxElement)


def test_xpand3_syntaxelement_constructor_exists():
    assert callable(xpand3_SyntaxElement.__init__)


def test_xpand3_syntaxelement_constructor_args():
    sig = inspect.signature(xpand3_SyntaxElement.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_xpand3_syntaxelement_has_line():
    assert hasattr(xpand3_SyntaxElement, "line")
    descriptor = None
    for klass in xpand3_SyntaxElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_xpand3_syntaxelement_has_fileName():
    assert hasattr(xpand3_SyntaxElement, "fileName")
    descriptor = None
    for klass in xpand3_SyntaxElement.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_xpand3_syntaxelement_has_start():
    assert hasattr(xpand3_SyntaxElement, "start")
    descriptor = None
    for klass in xpand3_SyntaxElement.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_xpand3_syntaxelement_has_end():
    assert hasattr(xpand3_SyntaxElement, "end")
    descriptor = None
    for klass in xpand3_SyntaxElement.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
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
AbstractNamedDeclaration_strategy = st.builds(
    AbstractNamedDeclaration,
)
xpand3_declaration_JavaExtension_strategy = st.builds(
    xpand3_declaration_JavaExtension,
)
xpand3_declaration_Extension_strategy = st.builds(
    xpand3_declaration_Extension,
    cached=
        st.booleans()
)
xpand3_declaration_Definition_strategy = st.builds(
    xpand3_declaration_Definition,
)
declaration_xpand3_Identifier_strategy = st.builds(
    declaration_xpand3_Identifier,
)
declaration_xpand3_DeclaredParameter_strategy = st.builds(
    declaration_xpand3_DeclaredParameter,
)
Extension_strategy = st.builds(
    Extension,
)
xpand3_declaration_CreateExtension_strategy = st.builds(
    xpand3_declaration_CreateExtension,
)
AbstractAspect_strategy = st.builds(
    AbstractAspect,
)
xpand3_declaration_DefinitionAspect_strategy = st.builds(
    xpand3_declaration_DefinitionAspect,
)
xpand3_declaration_ExtensionAspect_strategy = st.builds(
    xpand3_declaration_ExtensionAspect,
)
AbstractStatementWithBody_strategy = st.builds(
    AbstractStatementWithBody,
)
xpand3_statement_ForEachStatement_strategy = st.builds(
    xpand3_statement_ForEachStatement,
)
xpand3_statement_IfStatement_strategy = st.builds(
    xpand3_statement_IfStatement,
)
xpand3_statement_FileStatement_strategy = st.builds(
    xpand3_statement_FileStatement,
    once=
        st.booleans()
)
declaration_xpand3_File_strategy = st.builds(
    declaration_xpand3_File,
)
xpand3_statement_ProtectStatement_strategy = st.builds(
    xpand3_statement_ProtectStatement,
    disable=
        st.booleans()
)
xpand3_statement_LetStatement_strategy = st.builds(
    xpand3_statement_LetStatement,
)
IfStatement_strategy = st.builds(
    IfStatement,
)
statement_xpand3_Identifier_strategy = st.builds(
    statement_xpand3_Identifier,
)
AbstractStatement_strategy = st.builds(
    AbstractStatement,
)
xpand3_statement_ErrorStatement_strategy = st.builds(
    xpand3_statement_ErrorStatement,
)
xpand3_statement_ExpressionStatement_strategy = st.builds(
    xpand3_statement_ExpressionStatement,
)
xpand3_statement_TextStatement_strategy = st.builds(
    xpand3_statement_TextStatement,
    value=
        safe_text,
    deleteLine=
        st.booleans()
)
xpand3_statement_AbstractStatementWithBody_strategy = st.builds(
    xpand3_statement_AbstractStatementWithBody,
)
xpand3_statement_ExpandStatement_strategy = st.builds(
    xpand3_statement_ExpandStatement,
    foreach=
        st.booleans()
)
Case_strategy = st.builds(
    Case,
)
Literal_strategy = st.builds(
    Literal,
)
xpand3_expression_IntegerLiteral_strategy = st.builds(
    xpand3_expression_IntegerLiteral,
)
xpand3_expression_RealLiteral_strategy = st.builds(
    xpand3_expression_RealLiteral,
)
xpand3_expression_StringLiteral_strategy = st.builds(
    xpand3_expression_StringLiteral,
)
xpand3_expression_NullLiteral_strategy = st.builds(
    xpand3_expression_NullLiteral,
)
xpand3_expression_BooleanLiteral_strategy = st.builds(
    xpand3_expression_BooleanLiteral,
)
expression_xpand3_Identifier_strategy = st.builds(
    expression_xpand3_Identifier,
)
AbstractExpression_strategy = st.builds(
    AbstractExpression,
)
xpand3_expression_BinaryOperation_strategy = st.builds(
    xpand3_expression_BinaryOperation,
)
xpand3_expression_SwitchExpression_strategy = st.builds(
    xpand3_expression_SwitchExpression,
)
xpand3_expression_ChainExpression_strategy = st.builds(
    xpand3_expression_ChainExpression,
)
xpand3_expression_Literal_strategy = st.builds(
    xpand3_expression_Literal,
)
xpand3_expression_LetExpression_strategy = st.builds(
    xpand3_expression_LetExpression,
)
xpand3_expression_ListLiteral_strategy = st.builds(
    xpand3_expression_ListLiteral,
)
xpand3_expression_UnaryOperation_strategy = st.builds(
    xpand3_expression_UnaryOperation,
)
xpand3_expression_Cast_strategy = st.builds(
    xpand3_expression_Cast,
)
BinaryOperation_strategy = st.builds(
    BinaryOperation,
)
xpand3_expression_BooleanOperation_strategy = st.builds(
    xpand3_expression_BooleanOperation,
)
xpand3_expression_IfExpression_strategy = st.builds(
    xpand3_expression_IfExpression,
)
xpand3_expression_GlobalVarExpression_strategy = st.builds(
    xpand3_expression_GlobalVarExpression,
)
FeatureCall_strategy = st.builds(
    FeatureCall,
)
xpand3_expression_TypeSelectExpression_strategy = st.builds(
    xpand3_expression_TypeSelectExpression,
)
xpand3_expression_OperationCall_strategy = st.builds(
    xpand3_expression_OperationCall,
)
xpand3_expression_CollectionExpression_strategy = st.builds(
    xpand3_expression_CollectionExpression,
)
xpand3_expression_FeatureCall_strategy = st.builds(
    xpand3_expression_FeatureCall,
)
xpand3_expression_ConstructorCallExpression_strategy = st.builds(
    xpand3_expression_ConstructorCallExpression,
)
AbstractDeclaration_strategy = st.builds(
    AbstractDeclaration,
)
xpand3_declaration_Check_strategy = st.builds(
    xpand3_declaration_Check,
    feature=
        safe_text,
    errorSeverity=
        st.booleans()
)
xpand3_declaration_AbstractAspect_strategy = st.builds(
    xpand3_declaration_AbstractAspect,
    wildparams=
        st.booleans()
)
xpand3_declaration_AbstractNamedDeclaration_strategy = st.builds(
    xpand3_declaration_AbstractNamedDeclaration,
)
SyntaxElement_strategy = st.builds(
    SyntaxElement,
)
xpand3_statement_AbstractStatement_strategy = st.builds(
    xpand3_statement_AbstractStatement,
)
xpand3_expression_AbstractExpression_strategy = st.builds(
    xpand3_expression_AbstractExpression,
)
xpand3_expression_Case_strategy = st.builds(
    xpand3_expression_Case,
)
xpand3_declaration_AbstractDeclaration_strategy = st.builds(
    xpand3_declaration_AbstractDeclaration,
    isPrivate=
        st.booleans()
)
xpand3_Identifier_strategy = st.builds(
    xpand3_Identifier,
    value=
        safe_text
)
xpand3_DeclaredParameter_strategy = st.builds(
    xpand3_DeclaredParameter,
)
xpand3_ImportStatement_strategy = st.builds(
    xpand3_ImportStatement,
    exported=
        st.booleans()
)
xpand3_File_strategy = st.builds(
    xpand3_File,
)
xpand3_SyntaxElement_strategy = st.builds(
    xpand3_SyntaxElement,
    line=
        st.integers(),
    fileName=
        safe_text,
    start=
        st.integers(),
    end=
        st.integers()
)

@given(instance=AbstractNamedDeclaration_strategy)
@settings(max_examples=50)
def test_abstractnameddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractNamedDeclaration)

@given(instance=xpand3_declaration_JavaExtension_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_javaextension_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_JavaExtension)

@given(instance=xpand3_declaration_Extension_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_extension_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_Extension)



@given(instance=xpand3_declaration_Extension_strategy)
def test_xpand3_declaration_extension_cached_setter(instance):
    original = instance.cached
    instance.cached = original
    assert instance.cached == original

@given(instance=xpand3_declaration_Definition_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_definition_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_Definition)

@given(instance=declaration_xpand3_Identifier_strategy)
@settings(max_examples=50)
def test_declaration_xpand3_identifier_instantiation(instance):
    assert isinstance(instance, declaration_xpand3_Identifier)

@given(instance=declaration_xpand3_DeclaredParameter_strategy)
@settings(max_examples=50)
def test_declaration_xpand3_declaredparameter_instantiation(instance):
    assert isinstance(instance, declaration_xpand3_DeclaredParameter)

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)

@given(instance=xpand3_declaration_CreateExtension_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_createextension_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_CreateExtension)

@given(instance=AbstractAspect_strategy)
@settings(max_examples=50)
def test_abstractaspect_instantiation(instance):
    assert isinstance(instance, AbstractAspect)

@given(instance=xpand3_declaration_DefinitionAspect_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_definitionaspect_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_DefinitionAspect)

@given(instance=xpand3_declaration_ExtensionAspect_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_extensionaspect_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_ExtensionAspect)

@given(instance=AbstractStatementWithBody_strategy)
@settings(max_examples=50)
def test_abstractstatementwithbody_instantiation(instance):
    assert isinstance(instance, AbstractStatementWithBody)

@given(instance=xpand3_statement_ForEachStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_foreachstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_ForEachStatement)

@given(instance=xpand3_statement_IfStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_ifstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_IfStatement)

@given(instance=xpand3_statement_FileStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_filestatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_FileStatement)



@given(instance=xpand3_statement_FileStatement_strategy)
def test_xpand3_statement_filestatement_once_setter(instance):
    original = instance.once
    instance.once = original
    assert instance.once == original

@given(instance=declaration_xpand3_File_strategy)
@settings(max_examples=50)
def test_declaration_xpand3_file_instantiation(instance):
    assert isinstance(instance, declaration_xpand3_File)

@given(instance=xpand3_statement_ProtectStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_protectstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_ProtectStatement)



@given(instance=xpand3_statement_ProtectStatement_strategy)
def test_xpand3_statement_protectstatement_disable_setter(instance):
    original = instance.disable
    instance.disable = original
    assert instance.disable == original

@given(instance=xpand3_statement_LetStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_letstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_LetStatement)

@given(instance=IfStatement_strategy)
@settings(max_examples=50)
def test_ifstatement_instantiation(instance):
    assert isinstance(instance, IfStatement)

@given(instance=statement_xpand3_Identifier_strategy)
@settings(max_examples=50)
def test_statement_xpand3_identifier_instantiation(instance):
    assert isinstance(instance, statement_xpand3_Identifier)

@given(instance=AbstractStatement_strategy)
@settings(max_examples=50)
def test_abstractstatement_instantiation(instance):
    assert isinstance(instance, AbstractStatement)

@given(instance=xpand3_statement_ErrorStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_errorstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_ErrorStatement)

@given(instance=xpand3_statement_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_expressionstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_ExpressionStatement)

@given(instance=xpand3_statement_TextStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_textstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_TextStatement)



@given(instance=xpand3_statement_TextStatement_strategy)
def test_xpand3_statement_textstatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=xpand3_statement_TextStatement_strategy)
def test_xpand3_statement_textstatement_deleteLine_setter(instance):
    original = instance.deleteLine
    instance.deleteLine = original
    assert instance.deleteLine == original

@given(instance=xpand3_statement_AbstractStatementWithBody_strategy)
@settings(max_examples=50)
def test_xpand3_statement_abstractstatementwithbody_instantiation(instance):
    assert isinstance(instance, xpand3_statement_AbstractStatementWithBody)

@given(instance=xpand3_statement_ExpandStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_expandstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_ExpandStatement)



@given(instance=xpand3_statement_ExpandStatement_strategy)
def test_xpand3_statement_expandstatement_foreach_setter(instance):
    original = instance.foreach
    instance.foreach = original
    assert instance.foreach == original

@given(instance=Case_strategy)
@settings(max_examples=50)
def test_case_instantiation(instance):
    assert isinstance(instance, Case)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=xpand3_expression_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_xpand3_expression_integerliteral_instantiation(instance):
    assert isinstance(instance, xpand3_expression_IntegerLiteral)

@given(instance=xpand3_expression_RealLiteral_strategy)
@settings(max_examples=50)
def test_xpand3_expression_realliteral_instantiation(instance):
    assert isinstance(instance, xpand3_expression_RealLiteral)

@given(instance=xpand3_expression_StringLiteral_strategy)
@settings(max_examples=50)
def test_xpand3_expression_stringliteral_instantiation(instance):
    assert isinstance(instance, xpand3_expression_StringLiteral)

@given(instance=xpand3_expression_NullLiteral_strategy)
@settings(max_examples=50)
def test_xpand3_expression_nullliteral_instantiation(instance):
    assert isinstance(instance, xpand3_expression_NullLiteral)

@given(instance=xpand3_expression_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_xpand3_expression_booleanliteral_instantiation(instance):
    assert isinstance(instance, xpand3_expression_BooleanLiteral)

@given(instance=expression_xpand3_Identifier_strategy)
@settings(max_examples=50)
def test_expression_xpand3_identifier_instantiation(instance):
    assert isinstance(instance, expression_xpand3_Identifier)

@given(instance=AbstractExpression_strategy)
@settings(max_examples=50)
def test_abstractexpression_instantiation(instance):
    assert isinstance(instance, AbstractExpression)

@given(instance=xpand3_expression_BinaryOperation_strategy)
@settings(max_examples=50)
def test_xpand3_expression_binaryoperation_instantiation(instance):
    assert isinstance(instance, xpand3_expression_BinaryOperation)

@given(instance=xpand3_expression_SwitchExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_switchexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_SwitchExpression)

@given(instance=xpand3_expression_ChainExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_chainexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_ChainExpression)

@given(instance=xpand3_expression_Literal_strategy)
@settings(max_examples=50)
def test_xpand3_expression_literal_instantiation(instance):
    assert isinstance(instance, xpand3_expression_Literal)

@given(instance=xpand3_expression_LetExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_letexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_LetExpression)

@given(instance=xpand3_expression_ListLiteral_strategy)
@settings(max_examples=50)
def test_xpand3_expression_listliteral_instantiation(instance):
    assert isinstance(instance, xpand3_expression_ListLiteral)

@given(instance=xpand3_expression_UnaryOperation_strategy)
@settings(max_examples=50)
def test_xpand3_expression_unaryoperation_instantiation(instance):
    assert isinstance(instance, xpand3_expression_UnaryOperation)

@given(instance=xpand3_expression_Cast_strategy)
@settings(max_examples=50)
def test_xpand3_expression_cast_instantiation(instance):
    assert isinstance(instance, xpand3_expression_Cast)

@given(instance=BinaryOperation_strategy)
@settings(max_examples=50)
def test_binaryoperation_instantiation(instance):
    assert isinstance(instance, BinaryOperation)

@given(instance=xpand3_expression_BooleanOperation_strategy)
@settings(max_examples=50)
def test_xpand3_expression_booleanoperation_instantiation(instance):
    assert isinstance(instance, xpand3_expression_BooleanOperation)

@given(instance=xpand3_expression_IfExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_ifexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_IfExpression)

@given(instance=xpand3_expression_GlobalVarExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_globalvarexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_GlobalVarExpression)

@given(instance=FeatureCall_strategy)
@settings(max_examples=50)
def test_featurecall_instantiation(instance):
    assert isinstance(instance, FeatureCall)

@given(instance=xpand3_expression_TypeSelectExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_typeselectexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_TypeSelectExpression)

@given(instance=xpand3_expression_OperationCall_strategy)
@settings(max_examples=50)
def test_xpand3_expression_operationcall_instantiation(instance):
    assert isinstance(instance, xpand3_expression_OperationCall)

@given(instance=xpand3_expression_CollectionExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_collectionexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_CollectionExpression)

@given(instance=xpand3_expression_FeatureCall_strategy)
@settings(max_examples=50)
def test_xpand3_expression_featurecall_instantiation(instance):
    assert isinstance(instance, xpand3_expression_FeatureCall)

@given(instance=xpand3_expression_ConstructorCallExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_constructorcallexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_ConstructorCallExpression)

@given(instance=AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, AbstractDeclaration)

@given(instance=xpand3_declaration_Check_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_check_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_Check)



@given(instance=xpand3_declaration_Check_strategy)
def test_xpand3_declaration_check_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original



@given(instance=xpand3_declaration_Check_strategy)
def test_xpand3_declaration_check_errorSeverity_setter(instance):
    original = instance.errorSeverity
    instance.errorSeverity = original
    assert instance.errorSeverity == original

@given(instance=xpand3_declaration_AbstractAspect_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_abstractaspect_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_AbstractAspect)



@given(instance=xpand3_declaration_AbstractAspect_strategy)
def test_xpand3_declaration_abstractaspect_wildparams_setter(instance):
    original = instance.wildparams
    instance.wildparams = original
    assert instance.wildparams == original

@given(instance=xpand3_declaration_AbstractNamedDeclaration_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_abstractnameddeclaration_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_AbstractNamedDeclaration)

@given(instance=SyntaxElement_strategy)
@settings(max_examples=50)
def test_syntaxelement_instantiation(instance):
    assert isinstance(instance, SyntaxElement)

@given(instance=xpand3_statement_AbstractStatement_strategy)
@settings(max_examples=50)
def test_xpand3_statement_abstractstatement_instantiation(instance):
    assert isinstance(instance, xpand3_statement_AbstractStatement)

@given(instance=xpand3_expression_AbstractExpression_strategy)
@settings(max_examples=50)
def test_xpand3_expression_abstractexpression_instantiation(instance):
    assert isinstance(instance, xpand3_expression_AbstractExpression)

@given(instance=xpand3_expression_Case_strategy)
@settings(max_examples=50)
def test_xpand3_expression_case_instantiation(instance):
    assert isinstance(instance, xpand3_expression_Case)

@given(instance=xpand3_declaration_AbstractDeclaration_strategy)
@settings(max_examples=50)
def test_xpand3_declaration_abstractdeclaration_instantiation(instance):
    assert isinstance(instance, xpand3_declaration_AbstractDeclaration)



@given(instance=xpand3_declaration_AbstractDeclaration_strategy)
def test_xpand3_declaration_abstractdeclaration_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original

@given(instance=xpand3_Identifier_strategy)
@settings(max_examples=50)
def test_xpand3_identifier_instantiation(instance):
    assert isinstance(instance, xpand3_Identifier)



@given(instance=xpand3_Identifier_strategy)
def test_xpand3_identifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xpand3_DeclaredParameter_strategy)
@settings(max_examples=50)
def test_xpand3_declaredparameter_instantiation(instance):
    assert isinstance(instance, xpand3_DeclaredParameter)

@given(instance=xpand3_ImportStatement_strategy)
@settings(max_examples=50)
def test_xpand3_importstatement_instantiation(instance):
    assert isinstance(instance, xpand3_ImportStatement)



@given(instance=xpand3_ImportStatement_strategy)
def test_xpand3_importstatement_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original

@given(instance=xpand3_File_strategy)
@settings(max_examples=50)
def test_xpand3_file_instantiation(instance):
    assert isinstance(instance, xpand3_File)

@given(instance=xpand3_SyntaxElement_strategy)
@settings(max_examples=50)
def test_xpand3_syntaxelement_instantiation(instance):
    assert isinstance(instance, xpand3_SyntaxElement)



@given(instance=xpand3_SyntaxElement_strategy)
def test_xpand3_syntaxelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original



@given(instance=xpand3_SyntaxElement_strategy)
def test_xpand3_syntaxelement_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=xpand3_SyntaxElement_strategy)
def test_xpand3_syntaxelement_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=xpand3_SyntaxElement_strategy)
def test_xpand3_syntaxelement_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original
