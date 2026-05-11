import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    aS3::Interface,
    aS3::Member,
    aS3::Uses,
    aS3::Import,
    aS3::directive,
    aS3::EObject,
    aS3::Imports,
    aS3::Package,
    aS3::Model,
    aS3::annotationField,
    aS3::annotationFields,
    aS3::Annotation,
    aS3::forInClauseTail,
    aS3::forInClauseDecl,
    aS3::forIter,
    aS3::forCond,
    aS3::forInit,
    aS3::traditionalForClause,
    aS3::forInClause,
    aS3::DefaultStatement,
    aS3::CaseStatement,
    aS3::finallyBlock,
    aS3::switchBlock,
    SwitchStatement,
    aS3::Condition,
    finallyBlock,
    aS3::parameterDefault,
    parameterDeclaration,
    aS3::parameterRestDeclaration,
    aS3::basicParameterDeclaration,
    aS3::parameterDeclaration,
    aS3::parameterDeclarationList,
    aS3::catchBlock,
    expressionQualifiedIdentifier,
    aS3::fullNewSubexpression,
    aS3::regexpLiteral,
    aS3::arguments,
    aS3::primaryExpression,
    aS3::unaryExpressionNotPlusMinus,
    aS3::encapsulatedExpression,
    aS3::newExpression,
    aS3::additiveExpression,
    aS3::shiftExpression,
    aS3::relationalExpression,
    aS3::equalityExpression,
    aS3::bitwiseAndExpression,
    aS3::bitwiseXorExpression,
    aS3::bitwiseOrExpression,
    aS3::logicalAndExpression,
    unaryExpressionNotPlusMinus,
    aS3::postfixExpression,
    aS3::unaryExpression,
    aS3::multiplicativeExpression,
    assignmentExpression,
    aS3::conditionalExpression,
    parameterDefault,
    encapsulatedExpression,
    Expression,
    aS3::SymbolRef,
    aS3::Undefined,
    aS3::XmlConstant,
    aS3::This,
    aS3::NumberConstant,
    aS3::BoolConstant,
    aS3::RegexpConstant,
    aS3::StringConstant,
    aS3::Null,
    nonemptyElementList,
    element,
    forInClauseTail,
    ExpressionStatement,
    brackets,
    aS3::expressionList,
    aS3::switchStatementList,
    CaseStatement,
    ThrowStatement,
    DefaultXMLNamespaceStatement,
    Condition,
    elementList,
    aS3::nonemptyElementList,
    aS3::elementList,
    aS3::arrayLiteral,
    qualifiedIdent,
    aS3::namespaceName,
    aS3::qualifiedIdentifier,
    qualifiedIdentifier,
    aS3::e4xAttributeIdentifier,
    aS3::nonAttributeQualifiedIdentifier,
    aS3::brackets,
    conditionalExpression,
    aS3::logicalOrExpression,
    aS3::conditionalSubExpression,
    aS3::identifier,
    aS3::typeExpression,
    catchBlock,
    propertyIdentifier,
    aS3::qualifiedIdent,
    aS3::element,
    aS3::fieldName,
    aS3::literalField,
    aS3::fieldList,
    exprOrObjectLiteral,
    aS3::Expression,
    aS3::objectLiteral,
    aS3::exprOrObjectLiteral,
    nonAttributeQualifiedIdentifier,
    aS3::expressionQualifiedIdentifier,
    aS3::simpleQualifiedIdentifier,
    aS3::qualifier,
    qualifier,
    aS3::propertyIdentifier,
    aS3::propOrIdent,
    aS3::assignmentExpression,
    aS3::Statement,
    aS3::MethodBody,
    aS3::Method,
    aS3::MemberVariableDeclaration,
    forInClauseDecl,
    aS3::identi,
    Statement,
    aS3::ExpressionStatement,
    aS3::TryStatement,
    aS3::WithStatement,
    aS3::ForEachStatement,
    aS3::IfStatement,
    aS3::ReturnStatement,
    aS3::WhileStatement,
    aS3::ForStatement,
    aS3::DefaultXMLNamespaceStatement,
    aS3::SwitchStatement,
    aS3::DoWhileStatement,
    aS3::ThrowStatement,
    aS3::VariableDeclaration,
    aS3::Class,
    aS3::Block,
    aS3::functionSignature,
    aS3::functionCommon,
    aS3::functionExpression,
    aS3::Parameter,
    aS3::AccessorRole,
    aS3::Modifier,
    aS3::InterfaceMethod,
    AccessLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_as3::interface_is_not_abstract():
    assert not inspect.isabstract(aS3::Interface)


def test_as3::interface_constructor_exists():
    assert callable(aS3::Interface.__init__)


def test_as3::interface_constructor_args():
    sig = inspect.signature(aS3::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "access" in params, "Missing parameter 'access'"

def test_as3::interface_has_name():
    assert hasattr(aS3::Interface, "name")
    descriptor = None
    for klass in aS3::Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3::interface_has_access():
    assert hasattr(aS3::Interface, "access")
    descriptor = None
    for klass in aS3::Interface.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_as3::member_is_not_abstract():
    assert not inspect.isabstract(aS3::Member)


def test_as3::member_constructor_exists():
    assert callable(aS3::Member.__init__)


def test_as3::member_constructor_args():
    sig = inspect.signature(aS3::Member.__init__)
    params = list(sig.parameters.keys())



def test_as3::uses_is_not_abstract():
    assert not inspect.isabstract(aS3::Uses)


def test_as3::uses_constructor_exists():
    assert callable(aS3::Uses.__init__)


def test_as3::uses_constructor_args():
    sig = inspect.signature(aS3::Uses.__init__)
    params = list(sig.parameters.keys())
    assert "anytype" in params, "Missing parameter 'anytype'"
    assert "type" in params, "Missing parameter 'type'"

def test_as3::uses_has_anytype():
    assert hasattr(aS3::Uses, "anytype")
    descriptor = None
    for klass in aS3::Uses.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)

def test_as3::uses_has_type():
    assert hasattr(aS3::Uses, "type")
    descriptor = None
    for klass in aS3::Uses.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_as3::import_is_not_abstract():
    assert not inspect.isabstract(aS3::Import)


def test_as3::import_constructor_exists():
    assert callable(aS3::Import.__init__)


def test_as3::import_constructor_args():
    sig = inspect.signature(aS3::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_as3::import_has_importedNamespace():
    assert hasattr(aS3::Import, "importedNamespace")
    descriptor = None
    for klass in aS3::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_as3::directive_is_not_abstract():
    assert not inspect.isabstract(aS3::directive)


def test_as3::directive_constructor_exists():
    assert callable(aS3::directive.__init__)


def test_as3::directive_constructor_args():
    sig = inspect.signature(aS3::directive.__init__)
    params = list(sig.parameters.keys())



def test_as3::eobject_is_not_abstract():
    assert not inspect.isabstract(aS3::EObject)


def test_as3::eobject_constructor_exists():
    assert callable(aS3::EObject.__init__)


def test_as3::eobject_constructor_args():
    sig = inspect.signature(aS3::EObject.__init__)
    params = list(sig.parameters.keys())



def test_as3::imports_is_not_abstract():
    assert not inspect.isabstract(aS3::Imports)


def test_as3::imports_constructor_exists():
    assert callable(aS3::Imports.__init__)


def test_as3::imports_constructor_args():
    sig = inspect.signature(aS3::Imports.__init__)
    params = list(sig.parameters.keys())



def test_as3::package_is_not_abstract():
    assert not inspect.isabstract(aS3::Package)


def test_as3::package_constructor_exists():
    assert callable(aS3::Package.__init__)


def test_as3::package_constructor_args():
    sig = inspect.signature(aS3::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3::package_has_name():
    assert hasattr(aS3::Package, "name")
    descriptor = None
    for klass in aS3::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3::model_is_not_abstract():
    assert not inspect.isabstract(aS3::Model)


def test_as3::model_constructor_exists():
    assert callable(aS3::Model.__init__)


def test_as3::model_constructor_args():
    sig = inspect.signature(aS3::Model.__init__)
    params = list(sig.parameters.keys())



def test_as3::annotationfield_is_not_abstract():
    assert not inspect.isabstract(aS3::annotationField)


def test_as3::annotationfield_constructor_exists():
    assert callable(aS3::annotationField.__init__)


def test_as3::annotationfield_constructor_args():
    sig = inspect.signature(aS3::annotationField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3::annotationfield_has_name():
    assert hasattr(aS3::annotationField, "name")
    descriptor = None
    for klass in aS3::annotationField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3::annotationfields_is_not_abstract():
    assert not inspect.isabstract(aS3::annotationFields)


def test_as3::annotationfields_constructor_exists():
    assert callable(aS3::annotationFields.__init__)


def test_as3::annotationfields_constructor_args():
    sig = inspect.signature(aS3::annotationFields.__init__)
    params = list(sig.parameters.keys())



def test_as3::annotation_is_not_abstract():
    assert not inspect.isabstract(aS3::Annotation)


def test_as3::annotation_constructor_exists():
    assert callable(aS3::Annotation.__init__)


def test_as3::annotation_constructor_args():
    sig = inspect.signature(aS3::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3::annotation_has_name():
    assert hasattr(aS3::Annotation, "name")
    descriptor = None
    for klass in aS3::Annotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3::forinclausetail_is_not_abstract():
    assert not inspect.isabstract(aS3::forInClauseTail)


def test_as3::forinclausetail_constructor_exists():
    assert callable(aS3::forInClauseTail.__init__)


def test_as3::forinclausetail_constructor_args():
    sig = inspect.signature(aS3::forInClauseTail.__init__)
    params = list(sig.parameters.keys())



def test_as3::forinclausedecl_is_not_abstract():
    assert not inspect.isabstract(aS3::forInClauseDecl)


def test_as3::forinclausedecl_constructor_exists():
    assert callable(aS3::forInClauseDecl.__init__)


def test_as3::forinclausedecl_constructor_args():
    sig = inspect.signature(aS3::forInClauseDecl.__init__)
    params = list(sig.parameters.keys())



def test_as3::foriter_is_not_abstract():
    assert not inspect.isabstract(aS3::forIter)


def test_as3::foriter_constructor_exists():
    assert callable(aS3::forIter.__init__)


def test_as3::foriter_constructor_args():
    sig = inspect.signature(aS3::forIter.__init__)
    params = list(sig.parameters.keys())



def test_as3::forcond_is_not_abstract():
    assert not inspect.isabstract(aS3::forCond)


def test_as3::forcond_constructor_exists():
    assert callable(aS3::forCond.__init__)


def test_as3::forcond_constructor_args():
    sig = inspect.signature(aS3::forCond.__init__)
    params = list(sig.parameters.keys())



def test_as3::forinit_is_not_abstract():
    assert not inspect.isabstract(aS3::forInit)


def test_as3::forinit_constructor_exists():
    assert callable(aS3::forInit.__init__)


def test_as3::forinit_constructor_args():
    sig = inspect.signature(aS3::forInit.__init__)
    params = list(sig.parameters.keys())



def test_as3::traditionalforclause_is_not_abstract():
    assert not inspect.isabstract(aS3::traditionalForClause)


def test_as3::traditionalforclause_constructor_exists():
    assert callable(aS3::traditionalForClause.__init__)


def test_as3::traditionalforclause_constructor_args():
    sig = inspect.signature(aS3::traditionalForClause.__init__)
    params = list(sig.parameters.keys())



def test_as3::forinclause_is_not_abstract():
    assert not inspect.isabstract(aS3::forInClause)


def test_as3::forinclause_constructor_exists():
    assert callable(aS3::forInClause.__init__)


def test_as3::forinclause_constructor_args():
    sig = inspect.signature(aS3::forInClause.__init__)
    params = list(sig.parameters.keys())



def test_as3::defaultstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::DefaultStatement)


def test_as3::defaultstatement_constructor_exists():
    assert callable(aS3::DefaultStatement.__init__)


def test_as3::defaultstatement_constructor_args():
    sig = inspect.signature(aS3::DefaultStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::casestatement_is_not_abstract():
    assert not inspect.isabstract(aS3::CaseStatement)


def test_as3::casestatement_constructor_exists():
    assert callable(aS3::CaseStatement.__init__)


def test_as3::casestatement_constructor_args():
    sig = inspect.signature(aS3::CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::finallyblock_is_not_abstract():
    assert not inspect.isabstract(aS3::finallyBlock)


def test_as3::finallyblock_constructor_exists():
    assert callable(aS3::finallyBlock.__init__)


def test_as3::finallyblock_constructor_args():
    sig = inspect.signature(aS3::finallyBlock.__init__)
    params = list(sig.parameters.keys())



def test_as3::switchblock_is_not_abstract():
    assert not inspect.isabstract(aS3::switchBlock)


def test_as3::switchblock_constructor_exists():
    assert callable(aS3::switchBlock.__init__)


def test_as3::switchblock_constructor_args():
    sig = inspect.signature(aS3::switchBlock.__init__)
    params = list(sig.parameters.keys())



def test_switchstatement_is_not_abstract():
    assert not inspect.isabstract(SwitchStatement)


def test_switchstatement_constructor_exists():
    assert callable(SwitchStatement.__init__)


def test_switchstatement_constructor_args():
    sig = inspect.signature(SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::condition_is_not_abstract():
    assert not inspect.isabstract(aS3::Condition)


def test_as3::condition_constructor_exists():
    assert callable(aS3::Condition.__init__)


def test_as3::condition_constructor_args():
    sig = inspect.signature(aS3::Condition.__init__)
    params = list(sig.parameters.keys())



def test_finallyblock_is_not_abstract():
    assert not inspect.isabstract(finallyBlock)


def test_finallyblock_constructor_exists():
    assert callable(finallyBlock.__init__)


def test_finallyblock_constructor_args():
    sig = inspect.signature(finallyBlock.__init__)
    params = list(sig.parameters.keys())



def test_as3::parameterdefault_is_not_abstract():
    assert not inspect.isabstract(aS3::parameterDefault)


def test_as3::parameterdefault_constructor_exists():
    assert callable(aS3::parameterDefault.__init__)


def test_as3::parameterdefault_constructor_args():
    sig = inspect.signature(aS3::parameterDefault.__init__)
    params = list(sig.parameters.keys())



def test_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(parameterDeclaration)


def test_parameterdeclaration_constructor_exists():
    assert callable(parameterDeclaration.__init__)


def test_parameterdeclaration_constructor_args():
    sig = inspect.signature(parameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_as3::parameterrestdeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3::parameterRestDeclaration)


def test_as3::parameterrestdeclaration_constructor_exists():
    assert callable(aS3::parameterRestDeclaration.__init__)


def test_as3::parameterrestdeclaration_constructor_args():
    sig = inspect.signature(aS3::parameterRestDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_as3::basicparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3::basicParameterDeclaration)


def test_as3::basicparameterdeclaration_constructor_exists():
    assert callable(aS3::basicParameterDeclaration.__init__)


def test_as3::basicparameterdeclaration_constructor_args():
    sig = inspect.signature(aS3::basicParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_as3::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3::parameterDeclaration)


def test_as3::parameterdeclaration_constructor_exists():
    assert callable(aS3::parameterDeclaration.__init__)


def test_as3::parameterdeclaration_constructor_args():
    sig = inspect.signature(aS3::parameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_as3::parameterdeclarationlist_is_not_abstract():
    assert not inspect.isabstract(aS3::parameterDeclarationList)


def test_as3::parameterdeclarationlist_constructor_exists():
    assert callable(aS3::parameterDeclarationList.__init__)


def test_as3::parameterdeclarationlist_constructor_args():
    sig = inspect.signature(aS3::parameterDeclarationList.__init__)
    params = list(sig.parameters.keys())



def test_as3::catchblock_is_not_abstract():
    assert not inspect.isabstract(aS3::catchBlock)


def test_as3::catchblock_constructor_exists():
    assert callable(aS3::catchBlock.__init__)


def test_as3::catchblock_constructor_args():
    sig = inspect.signature(aS3::catchBlock.__init__)
    params = list(sig.parameters.keys())



def test_expressionqualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(expressionQualifiedIdentifier)


def test_expressionqualifiedidentifier_constructor_exists():
    assert callable(expressionQualifiedIdentifier.__init__)


def test_expressionqualifiedidentifier_constructor_args():
    sig = inspect.signature(expressionQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::fullnewsubexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::fullNewSubexpression)


def test_as3::fullnewsubexpression_constructor_exists():
    assert callable(aS3::fullNewSubexpression.__init__)


def test_as3::fullnewsubexpression_constructor_args():
    sig = inspect.signature(aS3::fullNewSubexpression.__init__)
    params = list(sig.parameters.keys())
    assert "fnsd" in params, "Missing parameter 'fnsd'"

def test_as3::fullnewsubexpression_has_fnsd():
    assert hasattr(aS3::fullNewSubexpression, "fnsd")
    descriptor = None
    for klass in aS3::fullNewSubexpression.__mro__:
        if "fnsd" in klass.__dict__:
            descriptor = klass.__dict__["fnsd"]
            break
    assert isinstance(descriptor, property)



def test_as3::regexpliteral_is_not_abstract():
    assert not inspect.isabstract(aS3::regexpLiteral)


def test_as3::regexpliteral_constructor_exists():
    assert callable(aS3::regexpLiteral.__init__)


def test_as3::regexpliteral_constructor_args():
    sig = inspect.signature(aS3::regexpLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "s" in params, "Missing parameter 's'"

def test_as3::regexpliteral_has_s():
    assert hasattr(aS3::regexpLiteral, "s")
    descriptor = None
    for klass in aS3::regexpLiteral.__mro__:
        if "s" in klass.__dict__:
            descriptor = klass.__dict__["s"]
            break
    assert isinstance(descriptor, property)



def test_as3::arguments_is_not_abstract():
    assert not inspect.isabstract(aS3::arguments)


def test_as3::arguments_constructor_exists():
    assert callable(aS3::arguments.__init__)


def test_as3::arguments_constructor_args():
    sig = inspect.signature(aS3::arguments.__init__)
    params = list(sig.parameters.keys())



def test_as3::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::primaryExpression)


def test_as3::primaryexpression_constructor_exists():
    assert callable(aS3::primaryExpression.__init__)


def test_as3::primaryexpression_constructor_args():
    sig = inspect.signature(aS3::primaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::unaryexpressionnotplusminus_is_not_abstract():
    assert not inspect.isabstract(aS3::unaryExpressionNotPlusMinus)


def test_as3::unaryexpressionnotplusminus_constructor_exists():
    assert callable(aS3::unaryExpressionNotPlusMinus.__init__)


def test_as3::unaryexpressionnotplusminus_constructor_args():
    sig = inspect.signature(aS3::unaryExpressionNotPlusMinus.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"
    assert "de" in params, "Missing parameter 'de'"

def test_as3::unaryexpressionnotplusminus_has_in_():
    assert hasattr(aS3::unaryExpressionNotPlusMinus, "in_")
    descriptor = None
    for klass in aS3::unaryExpressionNotPlusMinus.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)

def test_as3::unaryexpressionnotplusminus_has_de():
    assert hasattr(aS3::unaryExpressionNotPlusMinus, "de")
    descriptor = None
    for klass in aS3::unaryExpressionNotPlusMinus.__mro__:
        if "de" in klass.__dict__:
            descriptor = klass.__dict__["de"]
            break
    assert isinstance(descriptor, property)



def test_as3::encapsulatedexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::encapsulatedExpression)


def test_as3::encapsulatedexpression_constructor_exists():
    assert callable(aS3::encapsulatedExpression.__init__)


def test_as3::encapsulatedexpression_constructor_args():
    sig = inspect.signature(aS3::encapsulatedExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::newexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::newExpression)


def test_as3::newexpression_constructor_exists():
    assert callable(aS3::newExpression.__init__)


def test_as3::newexpression_constructor_args():
    sig = inspect.signature(aS3::newExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::additiveExpression)


def test_as3::additiveexpression_constructor_exists():
    assert callable(aS3::additiveExpression.__init__)


def test_as3::additiveexpression_constructor_args():
    sig = inspect.signature(aS3::additiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::additiveexpression_has_o():
    assert hasattr(aS3::additiveExpression, "o")
    descriptor = None
    for klass in aS3::additiveExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::shiftExpression)


def test_as3::shiftexpression_constructor_exists():
    assert callable(aS3::shiftExpression.__init__)


def test_as3::shiftexpression_constructor_args():
    sig = inspect.signature(aS3::shiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::shiftexpression_has_o():
    assert hasattr(aS3::shiftExpression, "o")
    descriptor = None
    for klass in aS3::shiftExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::relationalExpression)


def test_as3::relationalexpression_constructor_exists():
    assert callable(aS3::relationalExpression.__init__)


def test_as3::relationalexpression_constructor_args():
    sig = inspect.signature(aS3::relationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::relationalexpression_has_o():
    assert hasattr(aS3::relationalExpression, "o")
    descriptor = None
    for klass in aS3::relationalExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::equalityExpression)


def test_as3::equalityexpression_constructor_exists():
    assert callable(aS3::equalityExpression.__init__)


def test_as3::equalityexpression_constructor_args():
    sig = inspect.signature(aS3::equalityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::equalityexpression_has_o():
    assert hasattr(aS3::equalityExpression, "o")
    descriptor = None
    for klass in aS3::equalityExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3::bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::bitwiseAndExpression)


def test_as3::bitwiseandexpression_constructor_exists():
    assert callable(aS3::bitwiseAndExpression.__init__)


def test_as3::bitwiseandexpression_constructor_args():
    sig = inspect.signature(aS3::bitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::bitwiseandexpression_has_o():
    assert hasattr(aS3::bitwiseAndExpression, "o")
    descriptor = None
    for klass in aS3::bitwiseAndExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3::bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::bitwiseXorExpression)


def test_as3::bitwisexorexpression_constructor_exists():
    assert callable(aS3::bitwiseXorExpression.__init__)


def test_as3::bitwisexorexpression_constructor_args():
    sig = inspect.signature(aS3::bitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::bitwisexorexpression_has_o():
    assert hasattr(aS3::bitwiseXorExpression, "o")
    descriptor = None
    for klass in aS3::bitwiseXorExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3::bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::bitwiseOrExpression)


def test_as3::bitwiseorexpression_constructor_exists():
    assert callable(aS3::bitwiseOrExpression.__init__)


def test_as3::bitwiseorexpression_constructor_args():
    sig = inspect.signature(aS3::bitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::bitwiseorexpression_has_o():
    assert hasattr(aS3::bitwiseOrExpression, "o")
    descriptor = None
    for klass in aS3::bitwiseOrExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3::logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::logicalAndExpression)


def test_as3::logicalandexpression_constructor_exists():
    assert callable(aS3::logicalAndExpression.__init__)


def test_as3::logicalandexpression_constructor_args():
    sig = inspect.signature(aS3::logicalAndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::logicalandexpression_has_o():
    assert hasattr(aS3::logicalAndExpression, "o")
    descriptor = None
    for klass in aS3::logicalAndExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_unaryexpressionnotplusminus_is_not_abstract():
    assert not inspect.isabstract(unaryExpressionNotPlusMinus)


def test_unaryexpressionnotplusminus_constructor_exists():
    assert callable(unaryExpressionNotPlusMinus.__init__)


def test_unaryexpressionnotplusminus_constructor_args():
    sig = inspect.signature(unaryExpressionNotPlusMinus.__init__)
    params = list(sig.parameters.keys())



def test_as3::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::postfixExpression)


def test_as3::postfixexpression_constructor_exists():
    assert callable(aS3::postfixExpression.__init__)


def test_as3::postfixexpression_constructor_args():
    sig = inspect.signature(aS3::postfixExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::unaryExpression)


def test_as3::unaryexpression_constructor_exists():
    assert callable(aS3::unaryExpression.__init__)


def test_as3::unaryexpression_constructor_args():
    sig = inspect.signature(aS3::unaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::multiplicativeExpression)


def test_as3::multiplicativeexpression_constructor_exists():
    assert callable(aS3::multiplicativeExpression.__init__)


def test_as3::multiplicativeexpression_constructor_args():
    sig = inspect.signature(aS3::multiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::multiplicativeexpression_has_o():
    assert hasattr(aS3::multiplicativeExpression, "o")
    descriptor = None
    for klass in aS3::multiplicativeExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(assignmentExpression)


def test_assignmentexpression_constructor_exists():
    assert callable(assignmentExpression.__init__)


def test_assignmentexpression_constructor_args():
    sig = inspect.signature(assignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::conditionalExpression)


def test_as3::conditionalexpression_constructor_exists():
    assert callable(aS3::conditionalExpression.__init__)


def test_as3::conditionalexpression_constructor_args():
    sig = inspect.signature(aS3::conditionalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_as3::conditionalexpression_has_op():
    assert hasattr(aS3::conditionalExpression, "op")
    descriptor = None
    for klass in aS3::conditionalExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_parameterdefault_is_not_abstract():
    assert not inspect.isabstract(parameterDefault)


def test_parameterdefault_constructor_exists():
    assert callable(parameterDefault.__init__)


def test_parameterdefault_constructor_args():
    sig = inspect.signature(parameterDefault.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedexpression_is_not_abstract():
    assert not inspect.isabstract(encapsulatedExpression)


def test_encapsulatedexpression_constructor_exists():
    assert callable(encapsulatedExpression.__init__)


def test_encapsulatedexpression_constructor_args():
    sig = inspect.signature(encapsulatedExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_as3::symbolref_is_not_abstract():
    assert not inspect.isabstract(aS3::SymbolRef)


def test_as3::symbolref_constructor_exists():
    assert callable(aS3::SymbolRef.__init__)


def test_as3::symbolref_constructor_args():
    sig = inspect.signature(aS3::SymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_as3::undefined_is_not_abstract():
    assert not inspect.isabstract(aS3::Undefined)


def test_as3::undefined_constructor_exists():
    assert callable(aS3::Undefined.__init__)


def test_as3::undefined_constructor_args():
    sig = inspect.signature(aS3::Undefined.__init__)
    params = list(sig.parameters.keys())



def test_as3::xmlconstant_is_not_abstract():
    assert not inspect.isabstract(aS3::XmlConstant)


def test_as3::xmlconstant_constructor_exists():
    assert callable(aS3::XmlConstant.__init__)


def test_as3::xmlconstant_constructor_args():
    sig = inspect.signature(aS3::XmlConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_as3::xmlconstant_has_value():
    assert hasattr(aS3::XmlConstant, "value")
    descriptor = None
    for klass in aS3::XmlConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_as3::this_is_not_abstract():
    assert not inspect.isabstract(aS3::This)


def test_as3::this_constructor_exists():
    assert callable(aS3::This.__init__)


def test_as3::this_constructor_args():
    sig = inspect.signature(aS3::This.__init__)
    params = list(sig.parameters.keys())



def test_as3::numberconstant_is_not_abstract():
    assert not inspect.isabstract(aS3::NumberConstant)


def test_as3::numberconstant_constructor_exists():
    assert callable(aS3::NumberConstant.__init__)


def test_as3::numberconstant_constructor_args():
    sig = inspect.signature(aS3::NumberConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_as3::numberconstant_has_value():
    assert hasattr(aS3::NumberConstant, "value")
    descriptor = None
    for klass in aS3::NumberConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_as3::boolconstant_is_not_abstract():
    assert not inspect.isabstract(aS3::BoolConstant)


def test_as3::boolconstant_constructor_exists():
    assert callable(aS3::BoolConstant.__init__)


def test_as3::boolconstant_constructor_args():
    sig = inspect.signature(aS3::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_as3::boolconstant_has_value():
    assert hasattr(aS3::BoolConstant, "value")
    descriptor = None
    for klass in aS3::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_as3::regexpconstant_is_not_abstract():
    assert not inspect.isabstract(aS3::RegexpConstant)


def test_as3::regexpconstant_constructor_exists():
    assert callable(aS3::RegexpConstant.__init__)


def test_as3::regexpconstant_constructor_args():
    sig = inspect.signature(aS3::RegexpConstant.__init__)
    params = list(sig.parameters.keys())



def test_as3::stringconstant_is_not_abstract():
    assert not inspect.isabstract(aS3::StringConstant)


def test_as3::stringconstant_constructor_exists():
    assert callable(aS3::StringConstant.__init__)


def test_as3::stringconstant_constructor_args():
    sig = inspect.signature(aS3::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_as3::stringconstant_has_value():
    assert hasattr(aS3::StringConstant, "value")
    descriptor = None
    for klass in aS3::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_as3::null_is_not_abstract():
    assert not inspect.isabstract(aS3::Null)


def test_as3::null_constructor_exists():
    assert callable(aS3::Null.__init__)


def test_as3::null_constructor_args():
    sig = inspect.signature(aS3::Null.__init__)
    params = list(sig.parameters.keys())



def test_nonemptyelementlist_is_not_abstract():
    assert not inspect.isabstract(nonemptyElementList)


def test_nonemptyelementlist_constructor_exists():
    assert callable(nonemptyElementList.__init__)


def test_nonemptyelementlist_constructor_args():
    sig = inspect.signature(nonemptyElementList.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(element)


def test_element_constructor_exists():
    assert callable(element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(element.__init__)
    params = list(sig.parameters.keys())



def test_forinclausetail_is_not_abstract():
    assert not inspect.isabstract(forInClauseTail)


def test_forinclausetail_constructor_exists():
    assert callable(forInClauseTail.__init__)


def test_forinclausetail_constructor_args():
    sig = inspect.signature(forInClauseTail.__init__)
    params = list(sig.parameters.keys())



def test_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ExpressionStatement)


def test_expressionstatement_constructor_exists():
    assert callable(ExpressionStatement.__init__)


def test_expressionstatement_constructor_args():
    sig = inspect.signature(ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_brackets_is_not_abstract():
    assert not inspect.isabstract(brackets)


def test_brackets_constructor_exists():
    assert callable(brackets.__init__)


def test_brackets_constructor_args():
    sig = inspect.signature(brackets.__init__)
    params = list(sig.parameters.keys())



def test_as3::expressionlist_is_not_abstract():
    assert not inspect.isabstract(aS3::expressionList)


def test_as3::expressionlist_constructor_exists():
    assert callable(aS3::expressionList.__init__)


def test_as3::expressionlist_constructor_args():
    sig = inspect.signature(aS3::expressionList.__init__)
    params = list(sig.parameters.keys())



def test_as3::switchstatementlist_is_not_abstract():
    assert not inspect.isabstract(aS3::switchStatementList)


def test_as3::switchstatementlist_constructor_exists():
    assert callable(aS3::switchStatementList.__init__)


def test_as3::switchstatementlist_constructor_args():
    sig = inspect.signature(aS3::switchStatementList.__init__)
    params = list(sig.parameters.keys())



def test_casestatement_is_not_abstract():
    assert not inspect.isabstract(CaseStatement)


def test_casestatement_constructor_exists():
    assert callable(CaseStatement.__init__)


def test_casestatement_constructor_args():
    sig = inspect.signature(CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_throwstatement_is_not_abstract():
    assert not inspect.isabstract(ThrowStatement)


def test_throwstatement_constructor_exists():
    assert callable(ThrowStatement.__init__)


def test_throwstatement_constructor_args():
    sig = inspect.signature(ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_defaultxmlnamespacestatement_is_not_abstract():
    assert not inspect.isabstract(DefaultXMLNamespaceStatement)


def test_defaultxmlnamespacestatement_constructor_exists():
    assert callable(DefaultXMLNamespaceStatement.__init__)


def test_defaultxmlnamespacestatement_constructor_args():
    sig = inspect.signature(DefaultXMLNamespaceStatement.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_elementlist_is_not_abstract():
    assert not inspect.isabstract(elementList)


def test_elementlist_constructor_exists():
    assert callable(elementList.__init__)


def test_elementlist_constructor_args():
    sig = inspect.signature(elementList.__init__)
    params = list(sig.parameters.keys())



def test_as3::nonemptyelementlist_is_not_abstract():
    assert not inspect.isabstract(aS3::nonemptyElementList)


def test_as3::nonemptyelementlist_constructor_exists():
    assert callable(aS3::nonemptyElementList.__init__)


def test_as3::nonemptyelementlist_constructor_args():
    sig = inspect.signature(aS3::nonemptyElementList.__init__)
    params = list(sig.parameters.keys())



def test_as3::elementlist_is_not_abstract():
    assert not inspect.isabstract(aS3::elementList)


def test_as3::elementlist_constructor_exists():
    assert callable(aS3::elementList.__init__)


def test_as3::elementlist_constructor_args():
    sig = inspect.signature(aS3::elementList.__init__)
    params = list(sig.parameters.keys())



def test_as3::arrayliteral_is_not_abstract():
    assert not inspect.isabstract(aS3::arrayLiteral)


def test_as3::arrayliteral_constructor_exists():
    assert callable(aS3::arrayLiteral.__init__)


def test_as3::arrayliteral_constructor_args():
    sig = inspect.signature(aS3::arrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedident_is_not_abstract():
    assert not inspect.isabstract(qualifiedIdent)


def test_qualifiedident_constructor_exists():
    assert callable(qualifiedIdent.__init__)


def test_qualifiedident_constructor_args():
    sig = inspect.signature(qualifiedIdent.__init__)
    params = list(sig.parameters.keys())



def test_as3::namespacename_is_not_abstract():
    assert not inspect.isabstract(aS3::namespaceName)


def test_as3::namespacename_constructor_exists():
    assert callable(aS3::namespaceName.__init__)


def test_as3::namespacename_constructor_args():
    sig = inspect.signature(aS3::namespaceName.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_as3::namespacename_has_level():
    assert hasattr(aS3::namespaceName, "level")
    descriptor = None
    for klass in aS3::namespaceName.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_as3::qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3::qualifiedIdentifier)


def test_as3::qualifiedidentifier_constructor_exists():
    assert callable(aS3::qualifiedIdentifier.__init__)


def test_as3::qualifiedidentifier_constructor_args():
    sig = inspect.signature(aS3::qualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(qualifiedIdentifier)


def test_qualifiedidentifier_constructor_exists():
    assert callable(qualifiedIdentifier.__init__)


def test_qualifiedidentifier_constructor_args():
    sig = inspect.signature(qualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::e4xattributeidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3::e4xAttributeIdentifier)


def test_as3::e4xattributeidentifier_constructor_exists():
    assert callable(aS3::e4xAttributeIdentifier.__init__)


def test_as3::e4xattributeidentifier_constructor_args():
    sig = inspect.signature(aS3::e4xAttributeIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::nonattributequalifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3::nonAttributeQualifiedIdentifier)


def test_as3::nonattributequalifiedidentifier_constructor_exists():
    assert callable(aS3::nonAttributeQualifiedIdentifier.__init__)


def test_as3::nonattributequalifiedidentifier_constructor_args():
    sig = inspect.signature(aS3::nonAttributeQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::brackets_is_not_abstract():
    assert not inspect.isabstract(aS3::brackets)


def test_as3::brackets_constructor_exists():
    assert callable(aS3::brackets.__init__)


def test_as3::brackets_constructor_args():
    sig = inspect.signature(aS3::brackets.__init__)
    params = list(sig.parameters.keys())



def test_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(conditionalExpression)


def test_conditionalexpression_constructor_exists():
    assert callable(conditionalExpression.__init__)


def test_conditionalexpression_constructor_args():
    sig = inspect.signature(conditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::logicalOrExpression)


def test_as3::logicalorexpression_constructor_exists():
    assert callable(aS3::logicalOrExpression.__init__)


def test_as3::logicalorexpression_constructor_args():
    sig = inspect.signature(aS3::logicalOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3::logicalorexpression_has_o():
    assert hasattr(aS3::logicalOrExpression, "o")
    descriptor = None
    for klass in aS3::logicalOrExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3::conditionalsubexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::conditionalSubExpression)


def test_as3::conditionalsubexpression_constructor_exists():
    assert callable(aS3::conditionalSubExpression.__init__)


def test_as3::conditionalsubexpression_constructor_args():
    sig = inspect.signature(aS3::conditionalSubExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::identifier_is_not_abstract():
    assert not inspect.isabstract(aS3::identifier)


def test_as3::identifier_constructor_exists():
    assert callable(aS3::identifier.__init__)


def test_as3::identifier_constructor_args():
    sig = inspect.signature(aS3::identifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::typeexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::typeExpression)


def test_as3::typeexpression_constructor_exists():
    assert callable(aS3::typeExpression.__init__)


def test_as3::typeexpression_constructor_args():
    sig = inspect.signature(aS3::typeExpression.__init__)
    params = list(sig.parameters.keys())



def test_catchblock_is_not_abstract():
    assert not inspect.isabstract(catchBlock)


def test_catchblock_constructor_exists():
    assert callable(catchBlock.__init__)


def test_catchblock_constructor_args():
    sig = inspect.signature(catchBlock.__init__)
    params = list(sig.parameters.keys())



def test_propertyidentifier_is_not_abstract():
    assert not inspect.isabstract(propertyIdentifier)


def test_propertyidentifier_constructor_exists():
    assert callable(propertyIdentifier.__init__)


def test_propertyidentifier_constructor_args():
    sig = inspect.signature(propertyIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::qualifiedident_is_not_abstract():
    assert not inspect.isabstract(aS3::qualifiedIdent)


def test_as3::qualifiedident_constructor_exists():
    assert callable(aS3::qualifiedIdent.__init__)


def test_as3::qualifiedident_constructor_args():
    sig = inspect.signature(aS3::qualifiedIdent.__init__)
    params = list(sig.parameters.keys())



def test_as3::element_is_not_abstract():
    assert not inspect.isabstract(aS3::element)


def test_as3::element_constructor_exists():
    assert callable(aS3::element.__init__)


def test_as3::element_constructor_args():
    sig = inspect.signature(aS3::element.__init__)
    params = list(sig.parameters.keys())



def test_as3::fieldname_is_not_abstract():
    assert not inspect.isabstract(aS3::fieldName)


def test_as3::fieldname_constructor_exists():
    assert callable(aS3::fieldName.__init__)


def test_as3::fieldname_constructor_args():
    sig = inspect.signature(aS3::fieldName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "number" in params, "Missing parameter 'number'"

def test_as3::fieldname_has_name():
    assert hasattr(aS3::fieldName, "name")
    descriptor = None
    for klass in aS3::fieldName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3::fieldname_has_number():
    assert hasattr(aS3::fieldName, "number")
    descriptor = None
    for klass in aS3::fieldName.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_as3::literalfield_is_not_abstract():
    assert not inspect.isabstract(aS3::literalField)


def test_as3::literalfield_constructor_exists():
    assert callable(aS3::literalField.__init__)


def test_as3::literalfield_constructor_args():
    sig = inspect.signature(aS3::literalField.__init__)
    params = list(sig.parameters.keys())



def test_as3::fieldlist_is_not_abstract():
    assert not inspect.isabstract(aS3::fieldList)


def test_as3::fieldlist_constructor_exists():
    assert callable(aS3::fieldList.__init__)


def test_as3::fieldlist_constructor_args():
    sig = inspect.signature(aS3::fieldList.__init__)
    params = list(sig.parameters.keys())



def test_exprorobjectliteral_is_not_abstract():
    assert not inspect.isabstract(exprOrObjectLiteral)


def test_exprorobjectliteral_constructor_exists():
    assert callable(exprOrObjectLiteral.__init__)


def test_exprorobjectliteral_constructor_args():
    sig = inspect.signature(exprOrObjectLiteral.__init__)
    params = list(sig.parameters.keys())



def test_as3::expression_is_not_abstract():
    assert not inspect.isabstract(aS3::Expression)


def test_as3::expression_constructor_exists():
    assert callable(aS3::Expression.__init__)


def test_as3::expression_constructor_args():
    sig = inspect.signature(aS3::Expression.__init__)
    params = list(sig.parameters.keys())



def test_as3::objectliteral_is_not_abstract():
    assert not inspect.isabstract(aS3::objectLiteral)


def test_as3::objectliteral_constructor_exists():
    assert callable(aS3::objectLiteral.__init__)


def test_as3::objectliteral_constructor_args():
    sig = inspect.signature(aS3::objectLiteral.__init__)
    params = list(sig.parameters.keys())



def test_as3::exprorobjectliteral_is_not_abstract():
    assert not inspect.isabstract(aS3::exprOrObjectLiteral)


def test_as3::exprorobjectliteral_constructor_exists():
    assert callable(aS3::exprOrObjectLiteral.__init__)


def test_as3::exprorobjectliteral_constructor_args():
    sig = inspect.signature(aS3::exprOrObjectLiteral.__init__)
    params = list(sig.parameters.keys())



def test_nonattributequalifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(nonAttributeQualifiedIdentifier)


def test_nonattributequalifiedidentifier_constructor_exists():
    assert callable(nonAttributeQualifiedIdentifier.__init__)


def test_nonattributequalifiedidentifier_constructor_args():
    sig = inspect.signature(nonAttributeQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::expressionqualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3::expressionQualifiedIdentifier)


def test_as3::expressionqualifiedidentifier_constructor_exists():
    assert callable(aS3::expressionQualifiedIdentifier.__init__)


def test_as3::expressionqualifiedidentifier_constructor_args():
    sig = inspect.signature(aS3::expressionQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::simplequalifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3::simpleQualifiedIdentifier)


def test_as3::simplequalifiedidentifier_constructor_exists():
    assert callable(aS3::simpleQualifiedIdentifier.__init__)


def test_as3::simplequalifiedidentifier_constructor_args():
    sig = inspect.signature(aS3::simpleQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::qualifier_is_not_abstract():
    assert not inspect.isabstract(aS3::qualifier)


def test_as3::qualifier_constructor_exists():
    assert callable(aS3::qualifier.__init__)


def test_as3::qualifier_constructor_args():
    sig = inspect.signature(aS3::qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_as3::qualifier_has_level():
    assert hasattr(aS3::qualifier, "level")
    descriptor = None
    for klass in aS3::qualifier.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_qualifier_is_not_abstract():
    assert not inspect.isabstract(qualifier)


def test_qualifier_constructor_exists():
    assert callable(qualifier.__init__)


def test_qualifier_constructor_args():
    sig = inspect.signature(qualifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::propertyidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3::propertyIdentifier)


def test_as3::propertyidentifier_constructor_exists():
    assert callable(aS3::propertyIdentifier.__init__)


def test_as3::propertyidentifier_constructor_args():
    sig = inspect.signature(aS3::propertyIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3::proporident_is_not_abstract():
    assert not inspect.isabstract(aS3::propOrIdent)


def test_as3::proporident_constructor_exists():
    assert callable(aS3::propOrIdent.__init__)


def test_as3::proporident_constructor_args():
    sig = inspect.signature(aS3::propOrIdent.__init__)
    params = list(sig.parameters.keys())



def test_as3::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::assignmentExpression)


def test_as3::assignmentexpression_constructor_exists():
    assert callable(aS3::assignmentExpression.__init__)


def test_as3::assignmentexpression_constructor_args():
    sig = inspect.signature(aS3::assignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3::statement_is_not_abstract():
    assert not inspect.isabstract(aS3::Statement)


def test_as3::statement_constructor_exists():
    assert callable(aS3::Statement.__init__)


def test_as3::statement_constructor_args():
    sig = inspect.signature(aS3::Statement.__init__)
    params = list(sig.parameters.keys())



def test_as3::methodbody_is_not_abstract():
    assert not inspect.isabstract(aS3::MethodBody)


def test_as3::methodbody_constructor_exists():
    assert callable(aS3::MethodBody.__init__)


def test_as3::methodbody_constructor_args():
    sig = inspect.signature(aS3::MethodBody.__init__)
    params = list(sig.parameters.keys())



def test_as3::method_is_not_abstract():
    assert not inspect.isabstract(aS3::Method)


def test_as3::method_constructor_exists():
    assert callable(aS3::Method.__init__)


def test_as3::method_constructor_args():
    sig = inspect.signature(aS3::Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anytype" in params, "Missing parameter 'anytype'"

def test_as3::method_has_name():
    assert hasattr(aS3::Method, "name")
    descriptor = None
    for klass in aS3::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3::method_has_anytype():
    assert hasattr(aS3::Method, "anytype")
    descriptor = None
    for klass in aS3::Method.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)



def test_as3::membervariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3::MemberVariableDeclaration)


def test_as3::membervariabledeclaration_constructor_exists():
    assert callable(aS3::MemberVariableDeclaration.__init__)


def test_as3::membervariabledeclaration_constructor_args():
    sig = inspect.signature(aS3::MemberVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "anytype" in params, "Missing parameter 'anytype'"
    assert "name" in params, "Missing parameter 'name'"

def test_as3::membervariabledeclaration_has_anytype():
    assert hasattr(aS3::MemberVariableDeclaration, "anytype")
    descriptor = None
    for klass in aS3::MemberVariableDeclaration.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)

def test_as3::membervariabledeclaration_has_name():
    assert hasattr(aS3::MemberVariableDeclaration, "name")
    descriptor = None
    for klass in aS3::MemberVariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_forinclausedecl_is_not_abstract():
    assert not inspect.isabstract(forInClauseDecl)


def test_forinclausedecl_constructor_exists():
    assert callable(forInClauseDecl.__init__)


def test_forinclausedecl_constructor_args():
    sig = inspect.signature(forInClauseDecl.__init__)
    params = list(sig.parameters.keys())



def test_as3::identi_is_not_abstract():
    assert not inspect.isabstract(aS3::identi)


def test_as3::identi_constructor_exists():
    assert callable(aS3::identi.__init__)


def test_as3::identi_constructor_args():
    sig = inspect.signature(aS3::identi.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"

def test_as3::identi_has_i():
    assert hasattr(aS3::identi, "i")
    descriptor = None
    for klass in aS3::identi.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_as3::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::ExpressionStatement)


def test_as3::expressionstatement_constructor_exists():
    assert callable(aS3::ExpressionStatement.__init__)


def test_as3::expressionstatement_constructor_args():
    sig = inspect.signature(aS3::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::trystatement_is_not_abstract():
    assert not inspect.isabstract(aS3::TryStatement)


def test_as3::trystatement_constructor_exists():
    assert callable(aS3::TryStatement.__init__)


def test_as3::trystatement_constructor_args():
    sig = inspect.signature(aS3::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::withstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::WithStatement)


def test_as3::withstatement_constructor_exists():
    assert callable(aS3::WithStatement.__init__)


def test_as3::withstatement_constructor_args():
    sig = inspect.signature(aS3::WithStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::foreachstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::ForEachStatement)


def test_as3::foreachstatement_constructor_exists():
    assert callable(aS3::ForEachStatement.__init__)


def test_as3::foreachstatement_constructor_args():
    sig = inspect.signature(aS3::ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::ifstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::IfStatement)


def test_as3::ifstatement_constructor_exists():
    assert callable(aS3::IfStatement.__init__)


def test_as3::ifstatement_constructor_args():
    sig = inspect.signature(aS3::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::returnstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::ReturnStatement)


def test_as3::returnstatement_constructor_exists():
    assert callable(aS3::ReturnStatement.__init__)


def test_as3::returnstatement_constructor_args():
    sig = inspect.signature(aS3::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::whilestatement_is_not_abstract():
    assert not inspect.isabstract(aS3::WhileStatement)


def test_as3::whilestatement_constructor_exists():
    assert callable(aS3::WhileStatement.__init__)


def test_as3::whilestatement_constructor_args():
    sig = inspect.signature(aS3::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::forstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::ForStatement)


def test_as3::forstatement_constructor_exists():
    assert callable(aS3::ForStatement.__init__)


def test_as3::forstatement_constructor_args():
    sig = inspect.signature(aS3::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::defaultxmlnamespacestatement_is_not_abstract():
    assert not inspect.isabstract(aS3::DefaultXMLNamespaceStatement)


def test_as3::defaultxmlnamespacestatement_constructor_exists():
    assert callable(aS3::DefaultXMLNamespaceStatement.__init__)


def test_as3::defaultxmlnamespacestatement_constructor_args():
    sig = inspect.signature(aS3::DefaultXMLNamespaceStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::switchstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::SwitchStatement)


def test_as3::switchstatement_constructor_exists():
    assert callable(aS3::SwitchStatement.__init__)


def test_as3::switchstatement_constructor_args():
    sig = inspect.signature(aS3::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(aS3::DoWhileStatement)


def test_as3::dowhilestatement_constructor_exists():
    assert callable(aS3::DoWhileStatement.__init__)


def test_as3::dowhilestatement_constructor_args():
    sig = inspect.signature(aS3::DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::throwstatement_is_not_abstract():
    assert not inspect.isabstract(aS3::ThrowStatement)


def test_as3::throwstatement_constructor_exists():
    assert callable(aS3::ThrowStatement.__init__)


def test_as3::throwstatement_constructor_args():
    sig = inspect.signature(aS3::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3::VariableDeclaration)


def test_as3::variabledeclaration_constructor_exists():
    assert callable(aS3::VariableDeclaration.__init__)


def test_as3::variabledeclaration_constructor_args():
    sig = inspect.signature(aS3::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anytype" in params, "Missing parameter 'anytype'"

def test_as3::variabledeclaration_has_name():
    assert hasattr(aS3::VariableDeclaration, "name")
    descriptor = None
    for klass in aS3::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3::variabledeclaration_has_anytype():
    assert hasattr(aS3::VariableDeclaration, "anytype")
    descriptor = None
    for klass in aS3::VariableDeclaration.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)



def test_as3::class_is_not_abstract():
    assert not inspect.isabstract(aS3::Class)


def test_as3::class_constructor_exists():
    assert callable(aS3::Class.__init__)


def test_as3::class_constructor_args():
    sig = inspect.signature(aS3::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3::class_has_name():
    assert hasattr(aS3::Class, "name")
    descriptor = None
    for klass in aS3::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3::block_is_not_abstract():
    assert not inspect.isabstract(aS3::Block)


def test_as3::block_constructor_exists():
    assert callable(aS3::Block.__init__)


def test_as3::block_constructor_args():
    sig = inspect.signature(aS3::Block.__init__)
    params = list(sig.parameters.keys())



def test_as3::functionsignature_is_not_abstract():
    assert not inspect.isabstract(aS3::functionSignature)


def test_as3::functionsignature_constructor_exists():
    assert callable(aS3::functionSignature.__init__)


def test_as3::functionsignature_constructor_args():
    sig = inspect.signature(aS3::functionSignature.__init__)
    params = list(sig.parameters.keys())



def test_as3::functioncommon_is_not_abstract():
    assert not inspect.isabstract(aS3::functionCommon)


def test_as3::functioncommon_constructor_exists():
    assert callable(aS3::functionCommon.__init__)


def test_as3::functioncommon_constructor_args():
    sig = inspect.signature(aS3::functionCommon.__init__)
    params = list(sig.parameters.keys())



def test_as3::functionexpression_is_not_abstract():
    assert not inspect.isabstract(aS3::functionExpression)


def test_as3::functionexpression_constructor_exists():
    assert callable(aS3::functionExpression.__init__)


def test_as3::functionexpression_constructor_args():
    sig = inspect.signature(aS3::functionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3::functionexpression_has_name():
    assert hasattr(aS3::functionExpression, "name")
    descriptor = None
    for klass in aS3::functionExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3::parameter_is_not_abstract():
    assert not inspect.isabstract(aS3::Parameter)


def test_as3::parameter_constructor_exists():
    assert callable(aS3::Parameter.__init__)


def test_as3::parameter_constructor_args():
    sig = inspect.signature(aS3::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "anytype" in params, "Missing parameter 'anytype'"
    assert "name" in params, "Missing parameter 'name'"

def test_as3::parameter_has_anytype():
    assert hasattr(aS3::Parameter, "anytype")
    descriptor = None
    for klass in aS3::Parameter.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)

def test_as3::parameter_has_name():
    assert hasattr(aS3::Parameter, "name")
    descriptor = None
    for klass in aS3::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3::accessorrole_is_not_abstract():
    assert not inspect.isabstract(aS3::AccessorRole)


def test_as3::accessorrole_constructor_exists():
    assert callable(aS3::AccessorRole.__init__)


def test_as3::accessorrole_constructor_args():
    sig = inspect.signature(aS3::AccessorRole.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_as3::accessorrole_has_accessor():
    assert hasattr(aS3::AccessorRole, "accessor")
    descriptor = None
    for klass in aS3::AccessorRole.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_as3::modifier_is_not_abstract():
    assert not inspect.isabstract(aS3::Modifier)


def test_as3::modifier_constructor_exists():
    assert callable(aS3::Modifier.__init__)


def test_as3::modifier_constructor_args():
    sig = inspect.signature(aS3::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"
    assert "access" in params, "Missing parameter 'access'"
    assert "native" in params, "Missing parameter 'native'"
    assert "dynamic" in params, "Missing parameter 'dynamic'"

def test_as3::modifier_has_static():
    assert hasattr(aS3::Modifier, "static")
    descriptor = None
    for klass in aS3::Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_as3::modifier_has_final():
    assert hasattr(aS3::Modifier, "final")
    descriptor = None
    for klass in aS3::Modifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_as3::modifier_has_access():
    assert hasattr(aS3::Modifier, "access")
    descriptor = None
    for klass in aS3::Modifier.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)

def test_as3::modifier_has_native():
    assert hasattr(aS3::Modifier, "native")
    descriptor = None
    for klass in aS3::Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_as3::modifier_has_dynamic():
    assert hasattr(aS3::Modifier, "dynamic")
    descriptor = None
    for klass in aS3::Modifier.__mro__:
        if "dynamic" in klass.__dict__:
            descriptor = klass.__dict__["dynamic"]
            break
    assert isinstance(descriptor, property)



def test_as3::interfacemethod_is_not_abstract():
    assert not inspect.isabstract(aS3::InterfaceMethod)


def test_as3::interfacemethod_constructor_exists():
    assert callable(aS3::InterfaceMethod.__init__)


def test_as3::interfacemethod_constructor_args():
    sig = inspect.signature(aS3::InterfaceMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anytype" in params, "Missing parameter 'anytype'"

def test_as3::interfacemethod_has_name():
    assert hasattr(aS3::InterfaceMethod, "name")
    descriptor = None
    for klass in aS3::InterfaceMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3::interfacemethod_has_anytype():
    assert hasattr(aS3::InterfaceMethod, "anytype")
    descriptor = None
    for klass in aS3::InterfaceMethod.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)

def test_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
        "INTERNAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessLevel"


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
aS3::Interface_strategy = st.builds(
    aS3::Interface,
    name=
        safe_text,
    access=
        safe_text
)
aS3::Member_strategy = st.builds(
    aS3::Member,
)
aS3::Uses_strategy = st.builds(
    aS3::Uses,
    anytype=
        safe_text,
    type=
        safe_text
)
aS3::Import_strategy = st.builds(
    aS3::Import,
    importedNamespace=
        safe_text
)
aS3::directive_strategy = st.builds(
    aS3::directive,
)
aS3::EObject_strategy = st.builds(
    aS3::EObject,
)
aS3::Imports_strategy = st.builds(
    aS3::Imports,
)
aS3::Package_strategy = st.builds(
    aS3::Package,
    name=
        safe_text
)
aS3::Model_strategy = st.builds(
    aS3::Model,
)
aS3::annotationField_strategy = st.builds(
    aS3::annotationField,
    name=
        safe_text
)
aS3::annotationFields_strategy = st.builds(
    aS3::annotationFields,
)
aS3::Annotation_strategy = st.builds(
    aS3::Annotation,
    name=
        safe_text
)
aS3::forInClauseTail_strategy = st.builds(
    aS3::forInClauseTail,
)
aS3::forInClauseDecl_strategy = st.builds(
    aS3::forInClauseDecl,
)
aS3::forIter_strategy = st.builds(
    aS3::forIter,
)
aS3::forCond_strategy = st.builds(
    aS3::forCond,
)
aS3::forInit_strategy = st.builds(
    aS3::forInit,
)
aS3::traditionalForClause_strategy = st.builds(
    aS3::traditionalForClause,
)
aS3::forInClause_strategy = st.builds(
    aS3::forInClause,
)
aS3::DefaultStatement_strategy = st.builds(
    aS3::DefaultStatement,
)
aS3::CaseStatement_strategy = st.builds(
    aS3::CaseStatement,
)
aS3::finallyBlock_strategy = st.builds(
    aS3::finallyBlock,
)
aS3::switchBlock_strategy = st.builds(
    aS3::switchBlock,
)
SwitchStatement_strategy = st.builds(
    SwitchStatement,
)
aS3::Condition_strategy = st.builds(
    aS3::Condition,
)
finallyBlock_strategy = st.builds(
    finallyBlock,
)
aS3::parameterDefault_strategy = st.builds(
    aS3::parameterDefault,
)
parameterDeclaration_strategy = st.builds(
    parameterDeclaration,
)
aS3::parameterRestDeclaration_strategy = st.builds(
    aS3::parameterRestDeclaration,
)
aS3::basicParameterDeclaration_strategy = st.builds(
    aS3::basicParameterDeclaration,
)
aS3::parameterDeclaration_strategy = st.builds(
    aS3::parameterDeclaration,
)
aS3::parameterDeclarationList_strategy = st.builds(
    aS3::parameterDeclarationList,
)
aS3::catchBlock_strategy = st.builds(
    aS3::catchBlock,
)
expressionQualifiedIdentifier_strategy = st.builds(
    expressionQualifiedIdentifier,
)
aS3::fullNewSubexpression_strategy = st.builds(
    aS3::fullNewSubexpression,
    fnsd=
        safe_text
)
aS3::regexpLiteral_strategy = st.builds(
    aS3::regexpLiteral,
    s=
        safe_text
)
aS3::arguments_strategy = st.builds(
    aS3::arguments,
)
aS3::primaryExpression_strategy = st.builds(
    aS3::primaryExpression,
)
aS3::unaryExpressionNotPlusMinus_strategy = st.builds(
    aS3::unaryExpressionNotPlusMinus,
    in_=
        safe_text,
    de=
        safe_text
)
aS3::encapsulatedExpression_strategy = st.builds(
    aS3::encapsulatedExpression,
)
aS3::newExpression_strategy = st.builds(
    aS3::newExpression,
)
aS3::additiveExpression_strategy = st.builds(
    aS3::additiveExpression,
    o=
        safe_text
)
aS3::shiftExpression_strategy = st.builds(
    aS3::shiftExpression,
    o=
        safe_text
)
aS3::relationalExpression_strategy = st.builds(
    aS3::relationalExpression,
    o=
        safe_text
)
aS3::equalityExpression_strategy = st.builds(
    aS3::equalityExpression,
    o=
        safe_text
)
aS3::bitwiseAndExpression_strategy = st.builds(
    aS3::bitwiseAndExpression,
    o=
        safe_text
)
aS3::bitwiseXorExpression_strategy = st.builds(
    aS3::bitwiseXorExpression,
    o=
        safe_text
)
aS3::bitwiseOrExpression_strategy = st.builds(
    aS3::bitwiseOrExpression,
    o=
        safe_text
)
aS3::logicalAndExpression_strategy = st.builds(
    aS3::logicalAndExpression,
    o=
        safe_text
)
unaryExpressionNotPlusMinus_strategy = st.builds(
    unaryExpressionNotPlusMinus,
)
aS3::postfixExpression_strategy = st.builds(
    aS3::postfixExpression,
)
aS3::unaryExpression_strategy = st.builds(
    aS3::unaryExpression,
)
aS3::multiplicativeExpression_strategy = st.builds(
    aS3::multiplicativeExpression,
    o=
        safe_text
)
assignmentExpression_strategy = st.builds(
    assignmentExpression,
)
aS3::conditionalExpression_strategy = st.builds(
    aS3::conditionalExpression,
    op=
        safe_text
)
parameterDefault_strategy = st.builds(
    parameterDefault,
)
encapsulatedExpression_strategy = st.builds(
    encapsulatedExpression,
)
Expression_strategy = st.builds(
    Expression,
)
aS3::SymbolRef_strategy = st.builds(
    aS3::SymbolRef,
)
aS3::Undefined_strategy = st.builds(
    aS3::Undefined,
)
aS3::XmlConstant_strategy = st.builds(
    aS3::XmlConstant,
    value=
        safe_text
)
aS3::This_strategy = st.builds(
    aS3::This,
)
aS3::NumberConstant_strategy = st.builds(
    aS3::NumberConstant,
    value=
        safe_text
)
aS3::BoolConstant_strategy = st.builds(
    aS3::BoolConstant,
    value=
        safe_text
)
aS3::RegexpConstant_strategy = st.builds(
    aS3::RegexpConstant,
)
aS3::StringConstant_strategy = st.builds(
    aS3::StringConstant,
    value=
        safe_text
)
aS3::Null_strategy = st.builds(
    aS3::Null,
)
nonemptyElementList_strategy = st.builds(
    nonemptyElementList,
)
element_strategy = st.builds(
    element,
)
forInClauseTail_strategy = st.builds(
    forInClauseTail,
)
ExpressionStatement_strategy = st.builds(
    ExpressionStatement,
)
brackets_strategy = st.builds(
    brackets,
)
aS3::expressionList_strategy = st.builds(
    aS3::expressionList,
)
aS3::switchStatementList_strategy = st.builds(
    aS3::switchStatementList,
)
CaseStatement_strategy = st.builds(
    CaseStatement,
)
ThrowStatement_strategy = st.builds(
    ThrowStatement,
)
DefaultXMLNamespaceStatement_strategy = st.builds(
    DefaultXMLNamespaceStatement,
)
Condition_strategy = st.builds(
    Condition,
)
elementList_strategy = st.builds(
    elementList,
)
aS3::nonemptyElementList_strategy = st.builds(
    aS3::nonemptyElementList,
)
aS3::elementList_strategy = st.builds(
    aS3::elementList,
)
aS3::arrayLiteral_strategy = st.builds(
    aS3::arrayLiteral,
)
qualifiedIdent_strategy = st.builds(
    qualifiedIdent,
)
aS3::namespaceName_strategy = st.builds(
    aS3::namespaceName,
    level=
        safe_text
)
aS3::qualifiedIdentifier_strategy = st.builds(
    aS3::qualifiedIdentifier,
)
qualifiedIdentifier_strategy = st.builds(
    qualifiedIdentifier,
)
aS3::e4xAttributeIdentifier_strategy = st.builds(
    aS3::e4xAttributeIdentifier,
)
aS3::nonAttributeQualifiedIdentifier_strategy = st.builds(
    aS3::nonAttributeQualifiedIdentifier,
)
aS3::brackets_strategy = st.builds(
    aS3::brackets,
)
conditionalExpression_strategy = st.builds(
    conditionalExpression,
)
aS3::logicalOrExpression_strategy = st.builds(
    aS3::logicalOrExpression,
    o=
        safe_text
)
aS3::conditionalSubExpression_strategy = st.builds(
    aS3::conditionalSubExpression,
)
aS3::identifier_strategy = st.builds(
    aS3::identifier,
)
aS3::typeExpression_strategy = st.builds(
    aS3::typeExpression,
)
catchBlock_strategy = st.builds(
    catchBlock,
)
propertyIdentifier_strategy = st.builds(
    propertyIdentifier,
)
aS3::qualifiedIdent_strategy = st.builds(
    aS3::qualifiedIdent,
)
aS3::element_strategy = st.builds(
    aS3::element,
)
aS3::fieldName_strategy = st.builds(
    aS3::fieldName,
    name=
        safe_text,
    number=
        safe_text
)
aS3::literalField_strategy = st.builds(
    aS3::literalField,
)
aS3::fieldList_strategy = st.builds(
    aS3::fieldList,
)
exprOrObjectLiteral_strategy = st.builds(
    exprOrObjectLiteral,
)
aS3::Expression_strategy = st.builds(
    aS3::Expression,
)
aS3::objectLiteral_strategy = st.builds(
    aS3::objectLiteral,
)
aS3::exprOrObjectLiteral_strategy = st.builds(
    aS3::exprOrObjectLiteral,
)
nonAttributeQualifiedIdentifier_strategy = st.builds(
    nonAttributeQualifiedIdentifier,
)
aS3::expressionQualifiedIdentifier_strategy = st.builds(
    aS3::expressionQualifiedIdentifier,
)
aS3::simpleQualifiedIdentifier_strategy = st.builds(
    aS3::simpleQualifiedIdentifier,
)
aS3::qualifier_strategy = st.builds(
    aS3::qualifier,
    level=
        safe_text
)
qualifier_strategy = st.builds(
    qualifier,
)
aS3::propertyIdentifier_strategy = st.builds(
    aS3::propertyIdentifier,
)
aS3::propOrIdent_strategy = st.builds(
    aS3::propOrIdent,
)
aS3::assignmentExpression_strategy = st.builds(
    aS3::assignmentExpression,
)
aS3::Statement_strategy = st.builds(
    aS3::Statement,
)
aS3::MethodBody_strategy = st.builds(
    aS3::MethodBody,
)
aS3::Method_strategy = st.builds(
    aS3::Method,
    name=
        safe_text,
    anytype=
        safe_text
)
aS3::MemberVariableDeclaration_strategy = st.builds(
    aS3::MemberVariableDeclaration,
    anytype=
        safe_text,
    name=
        safe_text
)
forInClauseDecl_strategy = st.builds(
    forInClauseDecl,
)
aS3::identi_strategy = st.builds(
    aS3::identi,
    i=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
aS3::ExpressionStatement_strategy = st.builds(
    aS3::ExpressionStatement,
)
aS3::TryStatement_strategy = st.builds(
    aS3::TryStatement,
)
aS3::WithStatement_strategy = st.builds(
    aS3::WithStatement,
)
aS3::ForEachStatement_strategy = st.builds(
    aS3::ForEachStatement,
)
aS3::IfStatement_strategy = st.builds(
    aS3::IfStatement,
)
aS3::ReturnStatement_strategy = st.builds(
    aS3::ReturnStatement,
)
aS3::WhileStatement_strategy = st.builds(
    aS3::WhileStatement,
)
aS3::ForStatement_strategy = st.builds(
    aS3::ForStatement,
)
aS3::DefaultXMLNamespaceStatement_strategy = st.builds(
    aS3::DefaultXMLNamespaceStatement,
)
aS3::SwitchStatement_strategy = st.builds(
    aS3::SwitchStatement,
)
aS3::DoWhileStatement_strategy = st.builds(
    aS3::DoWhileStatement,
)
aS3::ThrowStatement_strategy = st.builds(
    aS3::ThrowStatement,
)
aS3::VariableDeclaration_strategy = st.builds(
    aS3::VariableDeclaration,
    name=
        safe_text,
    anytype=
        safe_text
)
aS3::Class_strategy = st.builds(
    aS3::Class,
    name=
        safe_text
)
aS3::Block_strategy = st.builds(
    aS3::Block,
)
aS3::functionSignature_strategy = st.builds(
    aS3::functionSignature,
)
aS3::functionCommon_strategy = st.builds(
    aS3::functionCommon,
)
aS3::functionExpression_strategy = st.builds(
    aS3::functionExpression,
    name=
        safe_text
)
aS3::Parameter_strategy = st.builds(
    aS3::Parameter,
    anytype=
        safe_text,
    name=
        safe_text
)
aS3::AccessorRole_strategy = st.builds(
    aS3::AccessorRole,
    accessor=
        safe_text
)
aS3::Modifier_strategy = st.builds(
    aS3::Modifier,
    static=
        st.booleans(),
    final=
        st.booleans(),
    access=
        safe_text,
    native=
        st.booleans(),
    dynamic=
        st.booleans()
)
aS3::InterfaceMethod_strategy = st.builds(
    aS3::InterfaceMethod,
    name=
        safe_text,
    anytype=
        safe_text
)

@given(instance=aS3::Interface_strategy)
@settings(max_examples=50)
def test_as3::interface_instantiation(instance):
    assert isinstance(instance, aS3::Interface)

@given(instance=aS3::Interface_strategy)
def test_as3::interface_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::Interface_strategy)
def test_as3::interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::Interface_strategy)
def test_as3::interface_access_type(instance):
    assert isinstance(instance.access, str)


@given(instance=aS3::Interface_strategy)
def test_as3::interface_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=aS3::Member_strategy)
@settings(max_examples=50)
def test_as3::member_instantiation(instance):
    assert isinstance(instance, aS3::Member)

@given(instance=aS3::Uses_strategy)
@settings(max_examples=50)
def test_as3::uses_instantiation(instance):
    assert isinstance(instance, aS3::Uses)

@given(instance=aS3::Uses_strategy)
def test_as3::uses_anytype_type(instance):
    assert isinstance(instance.anytype, str)


@given(instance=aS3::Uses_strategy)
def test_as3::uses_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3::Uses_strategy)
def test_as3::uses_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=aS3::Uses_strategy)
def test_as3::uses_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=aS3::Import_strategy)
@settings(max_examples=50)
def test_as3::import_instantiation(instance):
    assert isinstance(instance, aS3::Import)

@given(instance=aS3::Import_strategy)
def test_as3::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=aS3::Import_strategy)
def test_as3::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=aS3::directive_strategy)
@settings(max_examples=50)
def test_as3::directive_instantiation(instance):
    assert isinstance(instance, aS3::directive)

@given(instance=aS3::EObject_strategy)
@settings(max_examples=50)
def test_as3::eobject_instantiation(instance):
    assert isinstance(instance, aS3::EObject)

@given(instance=aS3::Imports_strategy)
@settings(max_examples=50)
def test_as3::imports_instantiation(instance):
    assert isinstance(instance, aS3::Imports)

@given(instance=aS3::Package_strategy)
@settings(max_examples=50)
def test_as3::package_instantiation(instance):
    assert isinstance(instance, aS3::Package)

@given(instance=aS3::Package_strategy)
def test_as3::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::Package_strategy)
def test_as3::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::Model_strategy)
@settings(max_examples=50)
def test_as3::model_instantiation(instance):
    assert isinstance(instance, aS3::Model)

@given(instance=aS3::annotationField_strategy)
@settings(max_examples=50)
def test_as3::annotationfield_instantiation(instance):
    assert isinstance(instance, aS3::annotationField)

@given(instance=aS3::annotationField_strategy)
def test_as3::annotationfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::annotationField_strategy)
def test_as3::annotationfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::annotationFields_strategy)
@settings(max_examples=50)
def test_as3::annotationfields_instantiation(instance):
    assert isinstance(instance, aS3::annotationFields)

@given(instance=aS3::Annotation_strategy)
@settings(max_examples=50)
def test_as3::annotation_instantiation(instance):
    assert isinstance(instance, aS3::Annotation)

@given(instance=aS3::Annotation_strategy)
def test_as3::annotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::Annotation_strategy)
def test_as3::annotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::forInClauseTail_strategy)
@settings(max_examples=50)
def test_as3::forinclausetail_instantiation(instance):
    assert isinstance(instance, aS3::forInClauseTail)

@given(instance=aS3::forInClauseDecl_strategy)
@settings(max_examples=50)
def test_as3::forinclausedecl_instantiation(instance):
    assert isinstance(instance, aS3::forInClauseDecl)

@given(instance=aS3::forIter_strategy)
@settings(max_examples=50)
def test_as3::foriter_instantiation(instance):
    assert isinstance(instance, aS3::forIter)

@given(instance=aS3::forCond_strategy)
@settings(max_examples=50)
def test_as3::forcond_instantiation(instance):
    assert isinstance(instance, aS3::forCond)

@given(instance=aS3::forInit_strategy)
@settings(max_examples=50)
def test_as3::forinit_instantiation(instance):
    assert isinstance(instance, aS3::forInit)

@given(instance=aS3::traditionalForClause_strategy)
@settings(max_examples=50)
def test_as3::traditionalforclause_instantiation(instance):
    assert isinstance(instance, aS3::traditionalForClause)

@given(instance=aS3::forInClause_strategy)
@settings(max_examples=50)
def test_as3::forinclause_instantiation(instance):
    assert isinstance(instance, aS3::forInClause)

@given(instance=aS3::DefaultStatement_strategy)
@settings(max_examples=50)
def test_as3::defaultstatement_instantiation(instance):
    assert isinstance(instance, aS3::DefaultStatement)

@given(instance=aS3::CaseStatement_strategy)
@settings(max_examples=50)
def test_as3::casestatement_instantiation(instance):
    assert isinstance(instance, aS3::CaseStatement)

@given(instance=aS3::finallyBlock_strategy)
@settings(max_examples=50)
def test_as3::finallyblock_instantiation(instance):
    assert isinstance(instance, aS3::finallyBlock)

@given(instance=aS3::switchBlock_strategy)
@settings(max_examples=50)
def test_as3::switchblock_instantiation(instance):
    assert isinstance(instance, aS3::switchBlock)

@given(instance=SwitchStatement_strategy)
@settings(max_examples=50)
def test_switchstatement_instantiation(instance):
    assert isinstance(instance, SwitchStatement)

@given(instance=aS3::Condition_strategy)
@settings(max_examples=50)
def test_as3::condition_instantiation(instance):
    assert isinstance(instance, aS3::Condition)

@given(instance=finallyBlock_strategy)
@settings(max_examples=50)
def test_finallyblock_instantiation(instance):
    assert isinstance(instance, finallyBlock)

@given(instance=aS3::parameterDefault_strategy)
@settings(max_examples=50)
def test_as3::parameterdefault_instantiation(instance):
    assert isinstance(instance, aS3::parameterDefault)

@given(instance=parameterDeclaration_strategy)
@settings(max_examples=50)
def test_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, parameterDeclaration)

@given(instance=aS3::parameterRestDeclaration_strategy)
@settings(max_examples=50)
def test_as3::parameterrestdeclaration_instantiation(instance):
    assert isinstance(instance, aS3::parameterRestDeclaration)

@given(instance=aS3::basicParameterDeclaration_strategy)
@settings(max_examples=50)
def test_as3::basicparameterdeclaration_instantiation(instance):
    assert isinstance(instance, aS3::basicParameterDeclaration)

@given(instance=aS3::parameterDeclaration_strategy)
@settings(max_examples=50)
def test_as3::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, aS3::parameterDeclaration)

@given(instance=aS3::parameterDeclarationList_strategy)
@settings(max_examples=50)
def test_as3::parameterdeclarationlist_instantiation(instance):
    assert isinstance(instance, aS3::parameterDeclarationList)

@given(instance=aS3::catchBlock_strategy)
@settings(max_examples=50)
def test_as3::catchblock_instantiation(instance):
    assert isinstance(instance, aS3::catchBlock)

@given(instance=expressionQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_expressionqualifiedidentifier_instantiation(instance):
    assert isinstance(instance, expressionQualifiedIdentifier)

@given(instance=aS3::fullNewSubexpression_strategy)
@settings(max_examples=50)
def test_as3::fullnewsubexpression_instantiation(instance):
    assert isinstance(instance, aS3::fullNewSubexpression)

@given(instance=aS3::fullNewSubexpression_strategy)
def test_as3::fullnewsubexpression_fnsd_type(instance):
    assert isinstance(instance.fnsd, str)


@given(instance=aS3::fullNewSubexpression_strategy)
def test_as3::fullnewsubexpression_fnsd_setter(instance):
    original = instance.fnsd
    instance.fnsd = original
    assert instance.fnsd == original

@given(instance=aS3::regexpLiteral_strategy)
@settings(max_examples=50)
def test_as3::regexpliteral_instantiation(instance):
    assert isinstance(instance, aS3::regexpLiteral)

@given(instance=aS3::regexpLiteral_strategy)
def test_as3::regexpliteral_s_type(instance):
    assert isinstance(instance.s, str)


@given(instance=aS3::regexpLiteral_strategy)
def test_as3::regexpliteral_s_setter(instance):
    original = instance.s
    instance.s = original
    assert instance.s == original

@given(instance=aS3::arguments_strategy)
@settings(max_examples=50)
def test_as3::arguments_instantiation(instance):
    assert isinstance(instance, aS3::arguments)

@given(instance=aS3::primaryExpression_strategy)
@settings(max_examples=50)
def test_as3::primaryexpression_instantiation(instance):
    assert isinstance(instance, aS3::primaryExpression)

@given(instance=aS3::unaryExpressionNotPlusMinus_strategy)
@settings(max_examples=50)
def test_as3::unaryexpressionnotplusminus_instantiation(instance):
    assert isinstance(instance, aS3::unaryExpressionNotPlusMinus)

@given(instance=aS3::unaryExpressionNotPlusMinus_strategy)
def test_as3::unaryexpressionnotplusminus_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=aS3::unaryExpressionNotPlusMinus_strategy)
def test_as3::unaryexpressionnotplusminus_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=aS3::unaryExpressionNotPlusMinus_strategy)
def test_as3::unaryexpressionnotplusminus_de_type(instance):
    assert isinstance(instance.de, str)


@given(instance=aS3::unaryExpressionNotPlusMinus_strategy)
def test_as3::unaryexpressionnotplusminus_de_setter(instance):
    original = instance.de
    instance.de = original
    assert instance.de == original

@given(instance=aS3::encapsulatedExpression_strategy)
@settings(max_examples=50)
def test_as3::encapsulatedexpression_instantiation(instance):
    assert isinstance(instance, aS3::encapsulatedExpression)

@given(instance=aS3::newExpression_strategy)
@settings(max_examples=50)
def test_as3::newexpression_instantiation(instance):
    assert isinstance(instance, aS3::newExpression)

@given(instance=aS3::additiveExpression_strategy)
@settings(max_examples=50)
def test_as3::additiveexpression_instantiation(instance):
    assert isinstance(instance, aS3::additiveExpression)

@given(instance=aS3::additiveExpression_strategy)
def test_as3::additiveexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::additiveExpression_strategy)
def test_as3::additiveexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3::shiftExpression_strategy)
@settings(max_examples=50)
def test_as3::shiftexpression_instantiation(instance):
    assert isinstance(instance, aS3::shiftExpression)

@given(instance=aS3::shiftExpression_strategy)
def test_as3::shiftexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::shiftExpression_strategy)
def test_as3::shiftexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3::relationalExpression_strategy)
@settings(max_examples=50)
def test_as3::relationalexpression_instantiation(instance):
    assert isinstance(instance, aS3::relationalExpression)

@given(instance=aS3::relationalExpression_strategy)
def test_as3::relationalexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::relationalExpression_strategy)
def test_as3::relationalexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3::equalityExpression_strategy)
@settings(max_examples=50)
def test_as3::equalityexpression_instantiation(instance):
    assert isinstance(instance, aS3::equalityExpression)

@given(instance=aS3::equalityExpression_strategy)
def test_as3::equalityexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::equalityExpression_strategy)
def test_as3::equalityexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3::bitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_as3::bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, aS3::bitwiseAndExpression)

@given(instance=aS3::bitwiseAndExpression_strategy)
def test_as3::bitwiseandexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::bitwiseAndExpression_strategy)
def test_as3::bitwiseandexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3::bitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_as3::bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, aS3::bitwiseXorExpression)

@given(instance=aS3::bitwiseXorExpression_strategy)
def test_as3::bitwisexorexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::bitwiseXorExpression_strategy)
def test_as3::bitwisexorexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3::bitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_as3::bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, aS3::bitwiseOrExpression)

@given(instance=aS3::bitwiseOrExpression_strategy)
def test_as3::bitwiseorexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::bitwiseOrExpression_strategy)
def test_as3::bitwiseorexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3::logicalAndExpression_strategy)
@settings(max_examples=50)
def test_as3::logicalandexpression_instantiation(instance):
    assert isinstance(instance, aS3::logicalAndExpression)

@given(instance=aS3::logicalAndExpression_strategy)
def test_as3::logicalandexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::logicalAndExpression_strategy)
def test_as3::logicalandexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=unaryExpressionNotPlusMinus_strategy)
@settings(max_examples=50)
def test_unaryexpressionnotplusminus_instantiation(instance):
    assert isinstance(instance, unaryExpressionNotPlusMinus)

@given(instance=aS3::postfixExpression_strategy)
@settings(max_examples=50)
def test_as3::postfixexpression_instantiation(instance):
    assert isinstance(instance, aS3::postfixExpression)

@given(instance=aS3::unaryExpression_strategy)
@settings(max_examples=50)
def test_as3::unaryexpression_instantiation(instance):
    assert isinstance(instance, aS3::unaryExpression)

@given(instance=aS3::multiplicativeExpression_strategy)
@settings(max_examples=50)
def test_as3::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, aS3::multiplicativeExpression)

@given(instance=aS3::multiplicativeExpression_strategy)
def test_as3::multiplicativeexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::multiplicativeExpression_strategy)
def test_as3::multiplicativeexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=assignmentExpression_strategy)
@settings(max_examples=50)
def test_assignmentexpression_instantiation(instance):
    assert isinstance(instance, assignmentExpression)

@given(instance=aS3::conditionalExpression_strategy)
@settings(max_examples=50)
def test_as3::conditionalexpression_instantiation(instance):
    assert isinstance(instance, aS3::conditionalExpression)

@given(instance=aS3::conditionalExpression_strategy)
def test_as3::conditionalexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=aS3::conditionalExpression_strategy)
def test_as3::conditionalexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=parameterDefault_strategy)
@settings(max_examples=50)
def test_parameterdefault_instantiation(instance):
    assert isinstance(instance, parameterDefault)

@given(instance=encapsulatedExpression_strategy)
@settings(max_examples=50)
def test_encapsulatedexpression_instantiation(instance):
    assert isinstance(instance, encapsulatedExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=aS3::SymbolRef_strategy)
@settings(max_examples=50)
def test_as3::symbolref_instantiation(instance):
    assert isinstance(instance, aS3::SymbolRef)

@given(instance=aS3::Undefined_strategy)
@settings(max_examples=50)
def test_as3::undefined_instantiation(instance):
    assert isinstance(instance, aS3::Undefined)

@given(instance=aS3::XmlConstant_strategy)
@settings(max_examples=50)
def test_as3::xmlconstant_instantiation(instance):
    assert isinstance(instance, aS3::XmlConstant)

@given(instance=aS3::XmlConstant_strategy)
def test_as3::xmlconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aS3::XmlConstant_strategy)
def test_as3::xmlconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aS3::This_strategy)
@settings(max_examples=50)
def test_as3::this_instantiation(instance):
    assert isinstance(instance, aS3::This)

@given(instance=aS3::NumberConstant_strategy)
@settings(max_examples=50)
def test_as3::numberconstant_instantiation(instance):
    assert isinstance(instance, aS3::NumberConstant)

@given(instance=aS3::NumberConstant_strategy)
def test_as3::numberconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aS3::NumberConstant_strategy)
def test_as3::numberconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aS3::BoolConstant_strategy)
@settings(max_examples=50)
def test_as3::boolconstant_instantiation(instance):
    assert isinstance(instance, aS3::BoolConstant)

@given(instance=aS3::BoolConstant_strategy)
def test_as3::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aS3::BoolConstant_strategy)
def test_as3::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aS3::RegexpConstant_strategy)
@settings(max_examples=50)
def test_as3::regexpconstant_instantiation(instance):
    assert isinstance(instance, aS3::RegexpConstant)

@given(instance=aS3::StringConstant_strategy)
@settings(max_examples=50)
def test_as3::stringconstant_instantiation(instance):
    assert isinstance(instance, aS3::StringConstant)

@given(instance=aS3::StringConstant_strategy)
def test_as3::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aS3::StringConstant_strategy)
def test_as3::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aS3::Null_strategy)
@settings(max_examples=50)
def test_as3::null_instantiation(instance):
    assert isinstance(instance, aS3::Null)

@given(instance=nonemptyElementList_strategy)
@settings(max_examples=50)
def test_nonemptyelementlist_instantiation(instance):
    assert isinstance(instance, nonemptyElementList)

@given(instance=element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, element)

@given(instance=forInClauseTail_strategy)
@settings(max_examples=50)
def test_forinclausetail_instantiation(instance):
    assert isinstance(instance, forInClauseTail)

@given(instance=ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expressionstatement_instantiation(instance):
    assert isinstance(instance, ExpressionStatement)

@given(instance=brackets_strategy)
@settings(max_examples=50)
def test_brackets_instantiation(instance):
    assert isinstance(instance, brackets)

@given(instance=aS3::expressionList_strategy)
@settings(max_examples=50)
def test_as3::expressionlist_instantiation(instance):
    assert isinstance(instance, aS3::expressionList)

@given(instance=aS3::switchStatementList_strategy)
@settings(max_examples=50)
def test_as3::switchstatementlist_instantiation(instance):
    assert isinstance(instance, aS3::switchStatementList)

@given(instance=CaseStatement_strategy)
@settings(max_examples=50)
def test_casestatement_instantiation(instance):
    assert isinstance(instance, CaseStatement)

@given(instance=ThrowStatement_strategy)
@settings(max_examples=50)
def test_throwstatement_instantiation(instance):
    assert isinstance(instance, ThrowStatement)

@given(instance=DefaultXMLNamespaceStatement_strategy)
@settings(max_examples=50)
def test_defaultxmlnamespacestatement_instantiation(instance):
    assert isinstance(instance, DefaultXMLNamespaceStatement)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=elementList_strategy)
@settings(max_examples=50)
def test_elementlist_instantiation(instance):
    assert isinstance(instance, elementList)

@given(instance=aS3::nonemptyElementList_strategy)
@settings(max_examples=50)
def test_as3::nonemptyelementlist_instantiation(instance):
    assert isinstance(instance, aS3::nonemptyElementList)

@given(instance=aS3::elementList_strategy)
@settings(max_examples=50)
def test_as3::elementlist_instantiation(instance):
    assert isinstance(instance, aS3::elementList)

@given(instance=aS3::arrayLiteral_strategy)
@settings(max_examples=50)
def test_as3::arrayliteral_instantiation(instance):
    assert isinstance(instance, aS3::arrayLiteral)

@given(instance=qualifiedIdent_strategy)
@settings(max_examples=50)
def test_qualifiedident_instantiation(instance):
    assert isinstance(instance, qualifiedIdent)

@given(instance=aS3::namespaceName_strategy)
@settings(max_examples=50)
def test_as3::namespacename_instantiation(instance):
    assert isinstance(instance, aS3::namespaceName)

@given(instance=aS3::namespaceName_strategy)
def test_as3::namespacename_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=aS3::namespaceName_strategy)
def test_as3::namespacename_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=aS3::qualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_as3::qualifiedidentifier_instantiation(instance):
    assert isinstance(instance, aS3::qualifiedIdentifier)

@given(instance=qualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_qualifiedidentifier_instantiation(instance):
    assert isinstance(instance, qualifiedIdentifier)

@given(instance=aS3::e4xAttributeIdentifier_strategy)
@settings(max_examples=50)
def test_as3::e4xattributeidentifier_instantiation(instance):
    assert isinstance(instance, aS3::e4xAttributeIdentifier)

@given(instance=aS3::nonAttributeQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_as3::nonattributequalifiedidentifier_instantiation(instance):
    assert isinstance(instance, aS3::nonAttributeQualifiedIdentifier)

@given(instance=aS3::brackets_strategy)
@settings(max_examples=50)
def test_as3::brackets_instantiation(instance):
    assert isinstance(instance, aS3::brackets)

@given(instance=conditionalExpression_strategy)
@settings(max_examples=50)
def test_conditionalexpression_instantiation(instance):
    assert isinstance(instance, conditionalExpression)

@given(instance=aS3::logicalOrExpression_strategy)
@settings(max_examples=50)
def test_as3::logicalorexpression_instantiation(instance):
    assert isinstance(instance, aS3::logicalOrExpression)

@given(instance=aS3::logicalOrExpression_strategy)
def test_as3::logicalorexpression_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=aS3::logicalOrExpression_strategy)
def test_as3::logicalorexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3::conditionalSubExpression_strategy)
@settings(max_examples=50)
def test_as3::conditionalsubexpression_instantiation(instance):
    assert isinstance(instance, aS3::conditionalSubExpression)

@given(instance=aS3::identifier_strategy)
@settings(max_examples=50)
def test_as3::identifier_instantiation(instance):
    assert isinstance(instance, aS3::identifier)

@given(instance=aS3::typeExpression_strategy)
@settings(max_examples=50)
def test_as3::typeexpression_instantiation(instance):
    assert isinstance(instance, aS3::typeExpression)

@given(instance=catchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, catchBlock)

@given(instance=propertyIdentifier_strategy)
@settings(max_examples=50)
def test_propertyidentifier_instantiation(instance):
    assert isinstance(instance, propertyIdentifier)

@given(instance=aS3::qualifiedIdent_strategy)
@settings(max_examples=50)
def test_as3::qualifiedident_instantiation(instance):
    assert isinstance(instance, aS3::qualifiedIdent)

@given(instance=aS3::element_strategy)
@settings(max_examples=50)
def test_as3::element_instantiation(instance):
    assert isinstance(instance, aS3::element)

@given(instance=aS3::fieldName_strategy)
@settings(max_examples=50)
def test_as3::fieldname_instantiation(instance):
    assert isinstance(instance, aS3::fieldName)

@given(instance=aS3::fieldName_strategy)
def test_as3::fieldname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::fieldName_strategy)
def test_as3::fieldname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::fieldName_strategy)
def test_as3::fieldname_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=aS3::fieldName_strategy)
def test_as3::fieldname_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=aS3::literalField_strategy)
@settings(max_examples=50)
def test_as3::literalfield_instantiation(instance):
    assert isinstance(instance, aS3::literalField)

@given(instance=aS3::fieldList_strategy)
@settings(max_examples=50)
def test_as3::fieldlist_instantiation(instance):
    assert isinstance(instance, aS3::fieldList)

@given(instance=exprOrObjectLiteral_strategy)
@settings(max_examples=50)
def test_exprorobjectliteral_instantiation(instance):
    assert isinstance(instance, exprOrObjectLiteral)

@given(instance=aS3::Expression_strategy)
@settings(max_examples=50)
def test_as3::expression_instantiation(instance):
    assert isinstance(instance, aS3::Expression)

@given(instance=aS3::objectLiteral_strategy)
@settings(max_examples=50)
def test_as3::objectliteral_instantiation(instance):
    assert isinstance(instance, aS3::objectLiteral)

@given(instance=aS3::exprOrObjectLiteral_strategy)
@settings(max_examples=50)
def test_as3::exprorobjectliteral_instantiation(instance):
    assert isinstance(instance, aS3::exprOrObjectLiteral)

@given(instance=nonAttributeQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_nonattributequalifiedidentifier_instantiation(instance):
    assert isinstance(instance, nonAttributeQualifiedIdentifier)

@given(instance=aS3::expressionQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_as3::expressionqualifiedidentifier_instantiation(instance):
    assert isinstance(instance, aS3::expressionQualifiedIdentifier)

@given(instance=aS3::simpleQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_as3::simplequalifiedidentifier_instantiation(instance):
    assert isinstance(instance, aS3::simpleQualifiedIdentifier)

@given(instance=aS3::qualifier_strategy)
@settings(max_examples=50)
def test_as3::qualifier_instantiation(instance):
    assert isinstance(instance, aS3::qualifier)

@given(instance=aS3::qualifier_strategy)
def test_as3::qualifier_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=aS3::qualifier_strategy)
def test_as3::qualifier_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=qualifier_strategy)
@settings(max_examples=50)
def test_qualifier_instantiation(instance):
    assert isinstance(instance, qualifier)

@given(instance=aS3::propertyIdentifier_strategy)
@settings(max_examples=50)
def test_as3::propertyidentifier_instantiation(instance):
    assert isinstance(instance, aS3::propertyIdentifier)

@given(instance=aS3::propOrIdent_strategy)
@settings(max_examples=50)
def test_as3::proporident_instantiation(instance):
    assert isinstance(instance, aS3::propOrIdent)

@given(instance=aS3::assignmentExpression_strategy)
@settings(max_examples=50)
def test_as3::assignmentexpression_instantiation(instance):
    assert isinstance(instance, aS3::assignmentExpression)

@given(instance=aS3::Statement_strategy)
@settings(max_examples=50)
def test_as3::statement_instantiation(instance):
    assert isinstance(instance, aS3::Statement)

@given(instance=aS3::MethodBody_strategy)
@settings(max_examples=50)
def test_as3::methodbody_instantiation(instance):
    assert isinstance(instance, aS3::MethodBody)

@given(instance=aS3::Method_strategy)
@settings(max_examples=50)
def test_as3::method_instantiation(instance):
    assert isinstance(instance, aS3::Method)

@given(instance=aS3::Method_strategy)
def test_as3::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::Method_strategy)
def test_as3::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::Method_strategy)
def test_as3::method_anytype_type(instance):
    assert isinstance(instance.anytype, str)


@given(instance=aS3::Method_strategy)
def test_as3::method_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3::MemberVariableDeclaration_strategy)
@settings(max_examples=50)
def test_as3::membervariabledeclaration_instantiation(instance):
    assert isinstance(instance, aS3::MemberVariableDeclaration)

@given(instance=aS3::MemberVariableDeclaration_strategy)
def test_as3::membervariabledeclaration_anytype_type(instance):
    assert isinstance(instance.anytype, str)


@given(instance=aS3::MemberVariableDeclaration_strategy)
def test_as3::membervariabledeclaration_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3::MemberVariableDeclaration_strategy)
def test_as3::membervariabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::MemberVariableDeclaration_strategy)
def test_as3::membervariabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=forInClauseDecl_strategy)
@settings(max_examples=50)
def test_forinclausedecl_instantiation(instance):
    assert isinstance(instance, forInClauseDecl)

@given(instance=aS3::identi_strategy)
@settings(max_examples=50)
def test_as3::identi_instantiation(instance):
    assert isinstance(instance, aS3::identi)

@given(instance=aS3::identi_strategy)
def test_as3::identi_i_type(instance):
    assert isinstance(instance.i, str)


@given(instance=aS3::identi_strategy)
def test_as3::identi_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=aS3::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_as3::expressionstatement_instantiation(instance):
    assert isinstance(instance, aS3::ExpressionStatement)

@given(instance=aS3::TryStatement_strategy)
@settings(max_examples=50)
def test_as3::trystatement_instantiation(instance):
    assert isinstance(instance, aS3::TryStatement)

@given(instance=aS3::WithStatement_strategy)
@settings(max_examples=50)
def test_as3::withstatement_instantiation(instance):
    assert isinstance(instance, aS3::WithStatement)

@given(instance=aS3::ForEachStatement_strategy)
@settings(max_examples=50)
def test_as3::foreachstatement_instantiation(instance):
    assert isinstance(instance, aS3::ForEachStatement)

@given(instance=aS3::IfStatement_strategy)
@settings(max_examples=50)
def test_as3::ifstatement_instantiation(instance):
    assert isinstance(instance, aS3::IfStatement)

@given(instance=aS3::ReturnStatement_strategy)
@settings(max_examples=50)
def test_as3::returnstatement_instantiation(instance):
    assert isinstance(instance, aS3::ReturnStatement)

@given(instance=aS3::WhileStatement_strategy)
@settings(max_examples=50)
def test_as3::whilestatement_instantiation(instance):
    assert isinstance(instance, aS3::WhileStatement)

@given(instance=aS3::ForStatement_strategy)
@settings(max_examples=50)
def test_as3::forstatement_instantiation(instance):
    assert isinstance(instance, aS3::ForStatement)

@given(instance=aS3::DefaultXMLNamespaceStatement_strategy)
@settings(max_examples=50)
def test_as3::defaultxmlnamespacestatement_instantiation(instance):
    assert isinstance(instance, aS3::DefaultXMLNamespaceStatement)

@given(instance=aS3::SwitchStatement_strategy)
@settings(max_examples=50)
def test_as3::switchstatement_instantiation(instance):
    assert isinstance(instance, aS3::SwitchStatement)

@given(instance=aS3::DoWhileStatement_strategy)
@settings(max_examples=50)
def test_as3::dowhilestatement_instantiation(instance):
    assert isinstance(instance, aS3::DoWhileStatement)

@given(instance=aS3::ThrowStatement_strategy)
@settings(max_examples=50)
def test_as3::throwstatement_instantiation(instance):
    assert isinstance(instance, aS3::ThrowStatement)

@given(instance=aS3::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_as3::variabledeclaration_instantiation(instance):
    assert isinstance(instance, aS3::VariableDeclaration)

@given(instance=aS3::VariableDeclaration_strategy)
def test_as3::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::VariableDeclaration_strategy)
def test_as3::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::VariableDeclaration_strategy)
def test_as3::variabledeclaration_anytype_type(instance):
    assert isinstance(instance.anytype, str)


@given(instance=aS3::VariableDeclaration_strategy)
def test_as3::variabledeclaration_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3::Class_strategy)
@settings(max_examples=50)
def test_as3::class_instantiation(instance):
    assert isinstance(instance, aS3::Class)

@given(instance=aS3::Class_strategy)
def test_as3::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::Class_strategy)
def test_as3::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::Block_strategy)
@settings(max_examples=50)
def test_as3::block_instantiation(instance):
    assert isinstance(instance, aS3::Block)

@given(instance=aS3::functionSignature_strategy)
@settings(max_examples=50)
def test_as3::functionsignature_instantiation(instance):
    assert isinstance(instance, aS3::functionSignature)

@given(instance=aS3::functionCommon_strategy)
@settings(max_examples=50)
def test_as3::functioncommon_instantiation(instance):
    assert isinstance(instance, aS3::functionCommon)

@given(instance=aS3::functionExpression_strategy)
@settings(max_examples=50)
def test_as3::functionexpression_instantiation(instance):
    assert isinstance(instance, aS3::functionExpression)

@given(instance=aS3::functionExpression_strategy)
def test_as3::functionexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::functionExpression_strategy)
def test_as3::functionexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::Parameter_strategy)
@settings(max_examples=50)
def test_as3::parameter_instantiation(instance):
    assert isinstance(instance, aS3::Parameter)

@given(instance=aS3::Parameter_strategy)
def test_as3::parameter_anytype_type(instance):
    assert isinstance(instance.anytype, str)


@given(instance=aS3::Parameter_strategy)
def test_as3::parameter_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3::Parameter_strategy)
def test_as3::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::Parameter_strategy)
def test_as3::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::AccessorRole_strategy)
@settings(max_examples=50)
def test_as3::accessorrole_instantiation(instance):
    assert isinstance(instance, aS3::AccessorRole)

@given(instance=aS3::AccessorRole_strategy)
def test_as3::accessorrole_accessor_type(instance):
    assert isinstance(instance.accessor, str)


@given(instance=aS3::AccessorRole_strategy)
def test_as3::accessorrole_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=aS3::Modifier_strategy)
@settings(max_examples=50)
def test_as3::modifier_instantiation(instance):
    assert isinstance(instance, aS3::Modifier)

@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_access_type(instance):
    assert isinstance(instance.access, str)


@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_native_type(instance):
    assert isinstance(instance.native, bool)


@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_dynamic_type(instance):
    assert isinstance(instance.dynamic, bool)


@given(instance=aS3::Modifier_strategy)
def test_as3::modifier_dynamic_setter(instance):
    original = instance.dynamic
    instance.dynamic = original
    assert instance.dynamic == original

@given(instance=aS3::InterfaceMethod_strategy)
@settings(max_examples=50)
def test_as3::interfacemethod_instantiation(instance):
    assert isinstance(instance, aS3::InterfaceMethod)

@given(instance=aS3::InterfaceMethod_strategy)
def test_as3::interfacemethod_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aS3::InterfaceMethod_strategy)
def test_as3::interfacemethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3::InterfaceMethod_strategy)
def test_as3::interfacemethod_anytype_type(instance):
    assert isinstance(instance.anytype, str)


@given(instance=aS3::InterfaceMethod_strategy)
def test_as3::interfacemethod_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original
