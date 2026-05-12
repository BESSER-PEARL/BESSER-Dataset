import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    aS3_Member,
    aS3_Uses,
    aS3_Import,
    aS3_directive,
    aS3_EObject,
    aS3_Imports,
    aS3_Package,
    aS3_Model,
    aS3_annotationField,
    aS3_annotationFields,
    aS3_Annotation,
    aS3_forInClauseTail,
    aS3_forInClauseDecl,
    aS3_forIter,
    aS3_forCond,
    aS3_forInit,
    aS3_traditionalForClause,
    aS3_forInClause,
    aS3_DefaultStatement,
    aS3_CaseStatement,
    aS3_finallyBlock,
    aS3_switchBlock,
    SwitchStatement,
    aS3_Condition,
    finallyBlock,
    aS3_parameterDefault,
    parameterDeclaration,
    aS3_parameterRestDeclaration,
    aS3_basicParameterDeclaration,
    aS3_parameterDeclaration,
    aS3_parameterDeclarationList,
    aS3_catchBlock,
    expressionQualifiedIdentifier,
    aS3_fullNewSubexpression,
    aS3_regexpLiteral,
    aS3_arguments,
    aS3_primaryExpression,
    aS3_unaryExpressionNotPlusMinus,
    aS3_encapsulatedExpression,
    aS3_newExpression,
    aS3_additiveExpression,
    aS3_shiftExpression,
    aS3_relationalExpression,
    aS3_equalityExpression,
    aS3_bitwiseAndExpression,
    aS3_bitwiseXorExpression,
    aS3_bitwiseOrExpression,
    aS3_logicalAndExpression,
    unaryExpressionNotPlusMinus,
    aS3_postfixExpression,
    aS3_unaryExpression,
    aS3_multiplicativeExpression,
    assignmentExpression,
    aS3_conditionalExpression,
    parameterDefault,
    encapsulatedExpression,
    Expression,
    aS3_XmlConstant,
    aS3_Undefined,
    aS3_RegexpConstant,
    aS3_NumberConstant,
    aS3_SymbolRef,
    aS3_This,
    aS3_BoolConstant,
    aS3_Null,
    aS3_StringConstant,
    nonemptyElementList,
    element,
    forInClauseTail,
    ExpressionStatement,
    brackets,
    aS3_expressionList,
    aS3_switchStatementList,
    CaseStatement,
    ThrowStatement,
    DefaultXMLNamespaceStatement,
    Condition,
    elementList,
    aS3_nonemptyElementList,
    aS3_elementList,
    aS3_arrayLiteral,
    qualifiedIdent,
    aS3_namespaceName,
    aS3_qualifiedIdentifier,
    qualifiedIdentifier,
    aS3_e4xAttributeIdentifier,
    aS3_nonAttributeQualifiedIdentifier,
    aS3_brackets,
    conditionalExpression,
    aS3_logicalOrExpression,
    aS3_conditionalSubExpression,
    aS3_identifier,
    aS3_typeExpression,
    catchBlock,
    propertyIdentifier,
    aS3_qualifiedIdent,
    aS3_element,
    aS3_fieldName,
    aS3_literalField,
    aS3_fieldList,
    exprOrObjectLiteral,
    aS3_objectLiteral,
    aS3_exprOrObjectLiteral,
    nonAttributeQualifiedIdentifier,
    aS3_expressionQualifiedIdentifier,
    aS3_simpleQualifiedIdentifier,
    aS3_qualifier,
    qualifier,
    aS3_propertyIdentifier,
    aS3_propOrIdent,
    aS3_assignmentExpression,
    aS3_Statement,
    aS3_MethodBody,
    aS3_Method,
    aS3_MemberVariableDeclaration,
    forInClauseDecl,
    aS3_identi,
    Statement,
    aS3_IfStatement,
    aS3_ForStatement,
    aS3_WithStatement,
    aS3_DefaultXMLNamespaceStatement,
    aS3_ReturnStatement,
    aS3_ExpressionStatement,
    aS3_ForEachStatement,
    aS3_ThrowStatement,
    aS3_DoWhileStatement,
    aS3_SwitchStatement,
    aS3_TryStatement,
    aS3_WhileStatement,
    aS3_VariableDeclaration,
    aS3_Class,
    aS3_Block,
    aS3_functionSignature,
    aS3_functionCommon,
    aS3_functionExpression,
    aS3_Parameter,
    aS3_AccessorRole,
    aS3_Modifier,
    aS3_InterfaceMethod,
    aS3_Interface,
    aS3_Expression,
    AccessLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_as3_member_is_not_abstract():
    assert not inspect.isabstract(aS3_Member)


def test_as3_member_constructor_exists():
    assert callable(aS3_Member.__init__)


def test_as3_member_constructor_args():
    sig = inspect.signature(aS3_Member.__init__)
    params = list(sig.parameters.keys())



def test_as3_uses_is_not_abstract():
    assert not inspect.isabstract(aS3_Uses)


def test_as3_uses_constructor_exists():
    assert callable(aS3_Uses.__init__)


def test_as3_uses_constructor_args():
    sig = inspect.signature(aS3_Uses.__init__)
    params = list(sig.parameters.keys())
    assert "anytype" in params, "Missing parameter 'anytype'"
    assert "type" in params, "Missing parameter 'type'"

def test_as3_uses_has_anytype():
    assert hasattr(aS3_Uses, "anytype")
    descriptor = None
    for klass in aS3_Uses.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)

def test_as3_uses_has_type():
    assert hasattr(aS3_Uses, "type")
    descriptor = None
    for klass in aS3_Uses.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_as3_import_is_not_abstract():
    assert not inspect.isabstract(aS3_Import)


def test_as3_import_constructor_exists():
    assert callable(aS3_Import.__init__)


def test_as3_import_constructor_args():
    sig = inspect.signature(aS3_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_as3_import_has_importedNamespace():
    assert hasattr(aS3_Import, "importedNamespace")
    descriptor = None
    for klass in aS3_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_as3_directive_is_not_abstract():
    assert not inspect.isabstract(aS3_directive)


def test_as3_directive_constructor_exists():
    assert callable(aS3_directive.__init__)


def test_as3_directive_constructor_args():
    sig = inspect.signature(aS3_directive.__init__)
    params = list(sig.parameters.keys())



def test_as3_eobject_is_not_abstract():
    assert not inspect.isabstract(aS3_EObject)


def test_as3_eobject_constructor_exists():
    assert callable(aS3_EObject.__init__)


def test_as3_eobject_constructor_args():
    sig = inspect.signature(aS3_EObject.__init__)
    params = list(sig.parameters.keys())



def test_as3_imports_is_not_abstract():
    assert not inspect.isabstract(aS3_Imports)


def test_as3_imports_constructor_exists():
    assert callable(aS3_Imports.__init__)


def test_as3_imports_constructor_args():
    sig = inspect.signature(aS3_Imports.__init__)
    params = list(sig.parameters.keys())



def test_as3_package_is_not_abstract():
    assert not inspect.isabstract(aS3_Package)


def test_as3_package_constructor_exists():
    assert callable(aS3_Package.__init__)


def test_as3_package_constructor_args():
    sig = inspect.signature(aS3_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3_package_has_name():
    assert hasattr(aS3_Package, "name")
    descriptor = None
    for klass in aS3_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3_model_is_not_abstract():
    assert not inspect.isabstract(aS3_Model)


def test_as3_model_constructor_exists():
    assert callable(aS3_Model.__init__)


def test_as3_model_constructor_args():
    sig = inspect.signature(aS3_Model.__init__)
    params = list(sig.parameters.keys())



def test_as3_annotationfield_is_not_abstract():
    assert not inspect.isabstract(aS3_annotationField)


def test_as3_annotationfield_constructor_exists():
    assert callable(aS3_annotationField.__init__)


def test_as3_annotationfield_constructor_args():
    sig = inspect.signature(aS3_annotationField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3_annotationfield_has_name():
    assert hasattr(aS3_annotationField, "name")
    descriptor = None
    for klass in aS3_annotationField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3_annotationfields_is_not_abstract():
    assert not inspect.isabstract(aS3_annotationFields)


def test_as3_annotationfields_constructor_exists():
    assert callable(aS3_annotationFields.__init__)


def test_as3_annotationfields_constructor_args():
    sig = inspect.signature(aS3_annotationFields.__init__)
    params = list(sig.parameters.keys())



def test_as3_annotation_is_not_abstract():
    assert not inspect.isabstract(aS3_Annotation)


def test_as3_annotation_constructor_exists():
    assert callable(aS3_Annotation.__init__)


def test_as3_annotation_constructor_args():
    sig = inspect.signature(aS3_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3_annotation_has_name():
    assert hasattr(aS3_Annotation, "name")
    descriptor = None
    for klass in aS3_Annotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3_forinclausetail_is_not_abstract():
    assert not inspect.isabstract(aS3_forInClauseTail)


def test_as3_forinclausetail_constructor_exists():
    assert callable(aS3_forInClauseTail.__init__)


def test_as3_forinclausetail_constructor_args():
    sig = inspect.signature(aS3_forInClauseTail.__init__)
    params = list(sig.parameters.keys())



def test_as3_forinclausedecl_is_not_abstract():
    assert not inspect.isabstract(aS3_forInClauseDecl)


def test_as3_forinclausedecl_constructor_exists():
    assert callable(aS3_forInClauseDecl.__init__)


def test_as3_forinclausedecl_constructor_args():
    sig = inspect.signature(aS3_forInClauseDecl.__init__)
    params = list(sig.parameters.keys())



def test_as3_foriter_is_not_abstract():
    assert not inspect.isabstract(aS3_forIter)


def test_as3_foriter_constructor_exists():
    assert callable(aS3_forIter.__init__)


def test_as3_foriter_constructor_args():
    sig = inspect.signature(aS3_forIter.__init__)
    params = list(sig.parameters.keys())



def test_as3_forcond_is_not_abstract():
    assert not inspect.isabstract(aS3_forCond)


def test_as3_forcond_constructor_exists():
    assert callable(aS3_forCond.__init__)


def test_as3_forcond_constructor_args():
    sig = inspect.signature(aS3_forCond.__init__)
    params = list(sig.parameters.keys())



def test_as3_forinit_is_not_abstract():
    assert not inspect.isabstract(aS3_forInit)


def test_as3_forinit_constructor_exists():
    assert callable(aS3_forInit.__init__)


def test_as3_forinit_constructor_args():
    sig = inspect.signature(aS3_forInit.__init__)
    params = list(sig.parameters.keys())



def test_as3_traditionalforclause_is_not_abstract():
    assert not inspect.isabstract(aS3_traditionalForClause)


def test_as3_traditionalforclause_constructor_exists():
    assert callable(aS3_traditionalForClause.__init__)


def test_as3_traditionalforclause_constructor_args():
    sig = inspect.signature(aS3_traditionalForClause.__init__)
    params = list(sig.parameters.keys())



def test_as3_forinclause_is_not_abstract():
    assert not inspect.isabstract(aS3_forInClause)


def test_as3_forinclause_constructor_exists():
    assert callable(aS3_forInClause.__init__)


def test_as3_forinclause_constructor_args():
    sig = inspect.signature(aS3_forInClause.__init__)
    params = list(sig.parameters.keys())



def test_as3_defaultstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_DefaultStatement)


def test_as3_defaultstatement_constructor_exists():
    assert callable(aS3_DefaultStatement.__init__)


def test_as3_defaultstatement_constructor_args():
    sig = inspect.signature(aS3_DefaultStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_casestatement_is_not_abstract():
    assert not inspect.isabstract(aS3_CaseStatement)


def test_as3_casestatement_constructor_exists():
    assert callable(aS3_CaseStatement.__init__)


def test_as3_casestatement_constructor_args():
    sig = inspect.signature(aS3_CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_finallyblock_is_not_abstract():
    assert not inspect.isabstract(aS3_finallyBlock)


def test_as3_finallyblock_constructor_exists():
    assert callable(aS3_finallyBlock.__init__)


def test_as3_finallyblock_constructor_args():
    sig = inspect.signature(aS3_finallyBlock.__init__)
    params = list(sig.parameters.keys())



def test_as3_switchblock_is_not_abstract():
    assert not inspect.isabstract(aS3_switchBlock)


def test_as3_switchblock_constructor_exists():
    assert callable(aS3_switchBlock.__init__)


def test_as3_switchblock_constructor_args():
    sig = inspect.signature(aS3_switchBlock.__init__)
    params = list(sig.parameters.keys())



def test_switchstatement_is_not_abstract():
    assert not inspect.isabstract(SwitchStatement)


def test_switchstatement_constructor_exists():
    assert callable(SwitchStatement.__init__)


def test_switchstatement_constructor_args():
    sig = inspect.signature(SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_condition_is_not_abstract():
    assert not inspect.isabstract(aS3_Condition)


def test_as3_condition_constructor_exists():
    assert callable(aS3_Condition.__init__)


def test_as3_condition_constructor_args():
    sig = inspect.signature(aS3_Condition.__init__)
    params = list(sig.parameters.keys())



def test_finallyblock_is_not_abstract():
    assert not inspect.isabstract(finallyBlock)


def test_finallyblock_constructor_exists():
    assert callable(finallyBlock.__init__)


def test_finallyblock_constructor_args():
    sig = inspect.signature(finallyBlock.__init__)
    params = list(sig.parameters.keys())



def test_as3_parameterdefault_is_not_abstract():
    assert not inspect.isabstract(aS3_parameterDefault)


def test_as3_parameterdefault_constructor_exists():
    assert callable(aS3_parameterDefault.__init__)


def test_as3_parameterdefault_constructor_args():
    sig = inspect.signature(aS3_parameterDefault.__init__)
    params = list(sig.parameters.keys())



def test_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(parameterDeclaration)


def test_parameterdeclaration_constructor_exists():
    assert callable(parameterDeclaration.__init__)


def test_parameterdeclaration_constructor_args():
    sig = inspect.signature(parameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_as3_parameterrestdeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3_parameterRestDeclaration)


def test_as3_parameterrestdeclaration_constructor_exists():
    assert callable(aS3_parameterRestDeclaration.__init__)


def test_as3_parameterrestdeclaration_constructor_args():
    sig = inspect.signature(aS3_parameterRestDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_as3_basicparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3_basicParameterDeclaration)


def test_as3_basicparameterdeclaration_constructor_exists():
    assert callable(aS3_basicParameterDeclaration.__init__)


def test_as3_basicparameterdeclaration_constructor_args():
    sig = inspect.signature(aS3_basicParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_as3_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3_parameterDeclaration)


def test_as3_parameterdeclaration_constructor_exists():
    assert callable(aS3_parameterDeclaration.__init__)


def test_as3_parameterdeclaration_constructor_args():
    sig = inspect.signature(aS3_parameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_as3_parameterdeclarationlist_is_not_abstract():
    assert not inspect.isabstract(aS3_parameterDeclarationList)


def test_as3_parameterdeclarationlist_constructor_exists():
    assert callable(aS3_parameterDeclarationList.__init__)


def test_as3_parameterdeclarationlist_constructor_args():
    sig = inspect.signature(aS3_parameterDeclarationList.__init__)
    params = list(sig.parameters.keys())



def test_as3_catchblock_is_not_abstract():
    assert not inspect.isabstract(aS3_catchBlock)


def test_as3_catchblock_constructor_exists():
    assert callable(aS3_catchBlock.__init__)


def test_as3_catchblock_constructor_args():
    sig = inspect.signature(aS3_catchBlock.__init__)
    params = list(sig.parameters.keys())



def test_expressionqualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(expressionQualifiedIdentifier)


def test_expressionqualifiedidentifier_constructor_exists():
    assert callable(expressionQualifiedIdentifier.__init__)


def test_expressionqualifiedidentifier_constructor_args():
    sig = inspect.signature(expressionQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_fullnewsubexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_fullNewSubexpression)


def test_as3_fullnewsubexpression_constructor_exists():
    assert callable(aS3_fullNewSubexpression.__init__)


def test_as3_fullnewsubexpression_constructor_args():
    sig = inspect.signature(aS3_fullNewSubexpression.__init__)
    params = list(sig.parameters.keys())
    assert "fnsd" in params, "Missing parameter 'fnsd'"

def test_as3_fullnewsubexpression_has_fnsd():
    assert hasattr(aS3_fullNewSubexpression, "fnsd")
    descriptor = None
    for klass in aS3_fullNewSubexpression.__mro__:
        if "fnsd" in klass.__dict__:
            descriptor = klass.__dict__["fnsd"]
            break
    assert isinstance(descriptor, property)



def test_as3_regexpliteral_is_not_abstract():
    assert not inspect.isabstract(aS3_regexpLiteral)


def test_as3_regexpliteral_constructor_exists():
    assert callable(aS3_regexpLiteral.__init__)


def test_as3_regexpliteral_constructor_args():
    sig = inspect.signature(aS3_regexpLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "s" in params, "Missing parameter 's'"

def test_as3_regexpliteral_has_s():
    assert hasattr(aS3_regexpLiteral, "s")
    descriptor = None
    for klass in aS3_regexpLiteral.__mro__:
        if "s" in klass.__dict__:
            descriptor = klass.__dict__["s"]
            break
    assert isinstance(descriptor, property)



def test_as3_arguments_is_not_abstract():
    assert not inspect.isabstract(aS3_arguments)


def test_as3_arguments_constructor_exists():
    assert callable(aS3_arguments.__init__)


def test_as3_arguments_constructor_args():
    sig = inspect.signature(aS3_arguments.__init__)
    params = list(sig.parameters.keys())



def test_as3_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_primaryExpression)


def test_as3_primaryexpression_constructor_exists():
    assert callable(aS3_primaryExpression.__init__)


def test_as3_primaryexpression_constructor_args():
    sig = inspect.signature(aS3_primaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3_unaryexpressionnotplusminus_is_not_abstract():
    assert not inspect.isabstract(aS3_unaryExpressionNotPlusMinus)


def test_as3_unaryexpressionnotplusminus_constructor_exists():
    assert callable(aS3_unaryExpressionNotPlusMinus.__init__)


def test_as3_unaryexpressionnotplusminus_constructor_args():
    sig = inspect.signature(aS3_unaryExpressionNotPlusMinus.__init__)
    params = list(sig.parameters.keys())
    assert "de" in params, "Missing parameter 'de'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_as3_unaryexpressionnotplusminus_has_de():
    assert hasattr(aS3_unaryExpressionNotPlusMinus, "de")
    descriptor = None
    for klass in aS3_unaryExpressionNotPlusMinus.__mro__:
        if "de" in klass.__dict__:
            descriptor = klass.__dict__["de"]
            break
    assert isinstance(descriptor, property)

def test_as3_unaryexpressionnotplusminus_has_in_():
    assert hasattr(aS3_unaryExpressionNotPlusMinus, "in_")
    descriptor = None
    for klass in aS3_unaryExpressionNotPlusMinus.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_as3_encapsulatedexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_encapsulatedExpression)


def test_as3_encapsulatedexpression_constructor_exists():
    assert callable(aS3_encapsulatedExpression.__init__)


def test_as3_encapsulatedexpression_constructor_args():
    sig = inspect.signature(aS3_encapsulatedExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3_newexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_newExpression)


def test_as3_newexpression_constructor_exists():
    assert callable(aS3_newExpression.__init__)


def test_as3_newexpression_constructor_args():
    sig = inspect.signature(aS3_newExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_additiveExpression)


def test_as3_additiveexpression_constructor_exists():
    assert callable(aS3_additiveExpression.__init__)


def test_as3_additiveexpression_constructor_args():
    sig = inspect.signature(aS3_additiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_additiveexpression_has_o():
    assert hasattr(aS3_additiveExpression, "o")
    descriptor = None
    for klass in aS3_additiveExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_shiftExpression)


def test_as3_shiftexpression_constructor_exists():
    assert callable(aS3_shiftExpression.__init__)


def test_as3_shiftexpression_constructor_args():
    sig = inspect.signature(aS3_shiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_shiftexpression_has_o():
    assert hasattr(aS3_shiftExpression, "o")
    descriptor = None
    for klass in aS3_shiftExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_relationalExpression)


def test_as3_relationalexpression_constructor_exists():
    assert callable(aS3_relationalExpression.__init__)


def test_as3_relationalexpression_constructor_args():
    sig = inspect.signature(aS3_relationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_relationalexpression_has_o():
    assert hasattr(aS3_relationalExpression, "o")
    descriptor = None
    for klass in aS3_relationalExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_equalityExpression)


def test_as3_equalityexpression_constructor_exists():
    assert callable(aS3_equalityExpression.__init__)


def test_as3_equalityexpression_constructor_args():
    sig = inspect.signature(aS3_equalityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_equalityexpression_has_o():
    assert hasattr(aS3_equalityExpression, "o")
    descriptor = None
    for klass in aS3_equalityExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3_bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_bitwiseAndExpression)


def test_as3_bitwiseandexpression_constructor_exists():
    assert callable(aS3_bitwiseAndExpression.__init__)


def test_as3_bitwiseandexpression_constructor_args():
    sig = inspect.signature(aS3_bitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_bitwiseandexpression_has_o():
    assert hasattr(aS3_bitwiseAndExpression, "o")
    descriptor = None
    for klass in aS3_bitwiseAndExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3_bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_bitwiseXorExpression)


def test_as3_bitwisexorexpression_constructor_exists():
    assert callable(aS3_bitwiseXorExpression.__init__)


def test_as3_bitwisexorexpression_constructor_args():
    sig = inspect.signature(aS3_bitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_bitwisexorexpression_has_o():
    assert hasattr(aS3_bitwiseXorExpression, "o")
    descriptor = None
    for klass in aS3_bitwiseXorExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3_bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_bitwiseOrExpression)


def test_as3_bitwiseorexpression_constructor_exists():
    assert callable(aS3_bitwiseOrExpression.__init__)


def test_as3_bitwiseorexpression_constructor_args():
    sig = inspect.signature(aS3_bitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_bitwiseorexpression_has_o():
    assert hasattr(aS3_bitwiseOrExpression, "o")
    descriptor = None
    for klass in aS3_bitwiseOrExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3_logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_logicalAndExpression)


def test_as3_logicalandexpression_constructor_exists():
    assert callable(aS3_logicalAndExpression.__init__)


def test_as3_logicalandexpression_constructor_args():
    sig = inspect.signature(aS3_logicalAndExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_logicalandexpression_has_o():
    assert hasattr(aS3_logicalAndExpression, "o")
    descriptor = None
    for klass in aS3_logicalAndExpression.__mro__:
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



def test_as3_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_postfixExpression)


def test_as3_postfixexpression_constructor_exists():
    assert callable(aS3_postfixExpression.__init__)


def test_as3_postfixexpression_constructor_args():
    sig = inspect.signature(aS3_postfixExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_unaryExpression)


def test_as3_unaryexpression_constructor_exists():
    assert callable(aS3_unaryExpression.__init__)


def test_as3_unaryexpression_constructor_args():
    sig = inspect.signature(aS3_unaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_multiplicativeExpression)


def test_as3_multiplicativeexpression_constructor_exists():
    assert callable(aS3_multiplicativeExpression.__init__)


def test_as3_multiplicativeexpression_constructor_args():
    sig = inspect.signature(aS3_multiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_multiplicativeexpression_has_o():
    assert hasattr(aS3_multiplicativeExpression, "o")
    descriptor = None
    for klass in aS3_multiplicativeExpression.__mro__:
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



def test_as3_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_conditionalExpression)


def test_as3_conditionalexpression_constructor_exists():
    assert callable(aS3_conditionalExpression.__init__)


def test_as3_conditionalexpression_constructor_args():
    sig = inspect.signature(aS3_conditionalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_as3_conditionalexpression_has_op():
    assert hasattr(aS3_conditionalExpression, "op")
    descriptor = None
    for klass in aS3_conditionalExpression.__mro__:
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



def test_as3_xmlconstant_is_not_abstract():
    assert not inspect.isabstract(aS3_XmlConstant)


def test_as3_xmlconstant_constructor_exists():
    assert callable(aS3_XmlConstant.__init__)


def test_as3_xmlconstant_constructor_args():
    sig = inspect.signature(aS3_XmlConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_as3_xmlconstant_has_value():
    assert hasattr(aS3_XmlConstant, "value")
    descriptor = None
    for klass in aS3_XmlConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_as3_undefined_is_not_abstract():
    assert not inspect.isabstract(aS3_Undefined)


def test_as3_undefined_constructor_exists():
    assert callable(aS3_Undefined.__init__)


def test_as3_undefined_constructor_args():
    sig = inspect.signature(aS3_Undefined.__init__)
    params = list(sig.parameters.keys())



def test_as3_regexpconstant_is_not_abstract():
    assert not inspect.isabstract(aS3_RegexpConstant)


def test_as3_regexpconstant_constructor_exists():
    assert callable(aS3_RegexpConstant.__init__)


def test_as3_regexpconstant_constructor_args():
    sig = inspect.signature(aS3_RegexpConstant.__init__)
    params = list(sig.parameters.keys())



def test_as3_numberconstant_is_not_abstract():
    assert not inspect.isabstract(aS3_NumberConstant)


def test_as3_numberconstant_constructor_exists():
    assert callable(aS3_NumberConstant.__init__)


def test_as3_numberconstant_constructor_args():
    sig = inspect.signature(aS3_NumberConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_as3_numberconstant_has_value():
    assert hasattr(aS3_NumberConstant, "value")
    descriptor = None
    for klass in aS3_NumberConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_as3_symbolref_is_not_abstract():
    assert not inspect.isabstract(aS3_SymbolRef)


def test_as3_symbolref_constructor_exists():
    assert callable(aS3_SymbolRef.__init__)


def test_as3_symbolref_constructor_args():
    sig = inspect.signature(aS3_SymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_as3_this_is_not_abstract():
    assert not inspect.isabstract(aS3_This)


def test_as3_this_constructor_exists():
    assert callable(aS3_This.__init__)


def test_as3_this_constructor_args():
    sig = inspect.signature(aS3_This.__init__)
    params = list(sig.parameters.keys())



def test_as3_boolconstant_is_not_abstract():
    assert not inspect.isabstract(aS3_BoolConstant)


def test_as3_boolconstant_constructor_exists():
    assert callable(aS3_BoolConstant.__init__)


def test_as3_boolconstant_constructor_args():
    sig = inspect.signature(aS3_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_as3_boolconstant_has_value():
    assert hasattr(aS3_BoolConstant, "value")
    descriptor = None
    for klass in aS3_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_as3_null_is_not_abstract():
    assert not inspect.isabstract(aS3_Null)


def test_as3_null_constructor_exists():
    assert callable(aS3_Null.__init__)


def test_as3_null_constructor_args():
    sig = inspect.signature(aS3_Null.__init__)
    params = list(sig.parameters.keys())



def test_as3_stringconstant_is_not_abstract():
    assert not inspect.isabstract(aS3_StringConstant)


def test_as3_stringconstant_constructor_exists():
    assert callable(aS3_StringConstant.__init__)


def test_as3_stringconstant_constructor_args():
    sig = inspect.signature(aS3_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_as3_stringconstant_has_value():
    assert hasattr(aS3_StringConstant, "value")
    descriptor = None
    for klass in aS3_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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



def test_as3_expressionlist_is_not_abstract():
    assert not inspect.isabstract(aS3_expressionList)


def test_as3_expressionlist_constructor_exists():
    assert callable(aS3_expressionList.__init__)


def test_as3_expressionlist_constructor_args():
    sig = inspect.signature(aS3_expressionList.__init__)
    params = list(sig.parameters.keys())



def test_as3_switchstatementlist_is_not_abstract():
    assert not inspect.isabstract(aS3_switchStatementList)


def test_as3_switchstatementlist_constructor_exists():
    assert callable(aS3_switchStatementList.__init__)


def test_as3_switchstatementlist_constructor_args():
    sig = inspect.signature(aS3_switchStatementList.__init__)
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



def test_as3_nonemptyelementlist_is_not_abstract():
    assert not inspect.isabstract(aS3_nonemptyElementList)


def test_as3_nonemptyelementlist_constructor_exists():
    assert callable(aS3_nonemptyElementList.__init__)


def test_as3_nonemptyelementlist_constructor_args():
    sig = inspect.signature(aS3_nonemptyElementList.__init__)
    params = list(sig.parameters.keys())



def test_as3_elementlist_is_not_abstract():
    assert not inspect.isabstract(aS3_elementList)


def test_as3_elementlist_constructor_exists():
    assert callable(aS3_elementList.__init__)


def test_as3_elementlist_constructor_args():
    sig = inspect.signature(aS3_elementList.__init__)
    params = list(sig.parameters.keys())



def test_as3_arrayliteral_is_not_abstract():
    assert not inspect.isabstract(aS3_arrayLiteral)


def test_as3_arrayliteral_constructor_exists():
    assert callable(aS3_arrayLiteral.__init__)


def test_as3_arrayliteral_constructor_args():
    sig = inspect.signature(aS3_arrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedident_is_not_abstract():
    assert not inspect.isabstract(qualifiedIdent)


def test_qualifiedident_constructor_exists():
    assert callable(qualifiedIdent.__init__)


def test_qualifiedident_constructor_args():
    sig = inspect.signature(qualifiedIdent.__init__)
    params = list(sig.parameters.keys())



def test_as3_namespacename_is_not_abstract():
    assert not inspect.isabstract(aS3_namespaceName)


def test_as3_namespacename_constructor_exists():
    assert callable(aS3_namespaceName.__init__)


def test_as3_namespacename_constructor_args():
    sig = inspect.signature(aS3_namespaceName.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_as3_namespacename_has_level():
    assert hasattr(aS3_namespaceName, "level")
    descriptor = None
    for klass in aS3_namespaceName.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_as3_qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3_qualifiedIdentifier)


def test_as3_qualifiedidentifier_constructor_exists():
    assert callable(aS3_qualifiedIdentifier.__init__)


def test_as3_qualifiedidentifier_constructor_args():
    sig = inspect.signature(aS3_qualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(qualifiedIdentifier)


def test_qualifiedidentifier_constructor_exists():
    assert callable(qualifiedIdentifier.__init__)


def test_qualifiedidentifier_constructor_args():
    sig = inspect.signature(qualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_e4xattributeidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3_e4xAttributeIdentifier)


def test_as3_e4xattributeidentifier_constructor_exists():
    assert callable(aS3_e4xAttributeIdentifier.__init__)


def test_as3_e4xattributeidentifier_constructor_args():
    sig = inspect.signature(aS3_e4xAttributeIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_nonattributequalifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3_nonAttributeQualifiedIdentifier)


def test_as3_nonattributequalifiedidentifier_constructor_exists():
    assert callable(aS3_nonAttributeQualifiedIdentifier.__init__)


def test_as3_nonattributequalifiedidentifier_constructor_args():
    sig = inspect.signature(aS3_nonAttributeQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_brackets_is_not_abstract():
    assert not inspect.isabstract(aS3_brackets)


def test_as3_brackets_constructor_exists():
    assert callable(aS3_brackets.__init__)


def test_as3_brackets_constructor_args():
    sig = inspect.signature(aS3_brackets.__init__)
    params = list(sig.parameters.keys())



def test_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(conditionalExpression)


def test_conditionalexpression_constructor_exists():
    assert callable(conditionalExpression.__init__)


def test_conditionalexpression_constructor_args():
    sig = inspect.signature(conditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3_logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_logicalOrExpression)


def test_as3_logicalorexpression_constructor_exists():
    assert callable(aS3_logicalOrExpression.__init__)


def test_as3_logicalorexpression_constructor_args():
    sig = inspect.signature(aS3_logicalOrExpression.__init__)
    params = list(sig.parameters.keys())
    assert "o" in params, "Missing parameter 'o'"

def test_as3_logicalorexpression_has_o():
    assert hasattr(aS3_logicalOrExpression, "o")
    descriptor = None
    for klass in aS3_logicalOrExpression.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)



def test_as3_conditionalsubexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_conditionalSubExpression)


def test_as3_conditionalsubexpression_constructor_exists():
    assert callable(aS3_conditionalSubExpression.__init__)


def test_as3_conditionalsubexpression_constructor_args():
    sig = inspect.signature(aS3_conditionalSubExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3_identifier_is_not_abstract():
    assert not inspect.isabstract(aS3_identifier)


def test_as3_identifier_constructor_exists():
    assert callable(aS3_identifier.__init__)


def test_as3_identifier_constructor_args():
    sig = inspect.signature(aS3_identifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_typeexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_typeExpression)


def test_as3_typeexpression_constructor_exists():
    assert callable(aS3_typeExpression.__init__)


def test_as3_typeexpression_constructor_args():
    sig = inspect.signature(aS3_typeExpression.__init__)
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



def test_as3_qualifiedident_is_not_abstract():
    assert not inspect.isabstract(aS3_qualifiedIdent)


def test_as3_qualifiedident_constructor_exists():
    assert callable(aS3_qualifiedIdent.__init__)


def test_as3_qualifiedident_constructor_args():
    sig = inspect.signature(aS3_qualifiedIdent.__init__)
    params = list(sig.parameters.keys())



def test_as3_element_is_not_abstract():
    assert not inspect.isabstract(aS3_element)


def test_as3_element_constructor_exists():
    assert callable(aS3_element.__init__)


def test_as3_element_constructor_args():
    sig = inspect.signature(aS3_element.__init__)
    params = list(sig.parameters.keys())



def test_as3_fieldname_is_not_abstract():
    assert not inspect.isabstract(aS3_fieldName)


def test_as3_fieldname_constructor_exists():
    assert callable(aS3_fieldName.__init__)


def test_as3_fieldname_constructor_args():
    sig = inspect.signature(aS3_fieldName.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"

def test_as3_fieldname_has_number():
    assert hasattr(aS3_fieldName, "number")
    descriptor = None
    for klass in aS3_fieldName.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_as3_fieldname_has_name():
    assert hasattr(aS3_fieldName, "name")
    descriptor = None
    for klass in aS3_fieldName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3_literalfield_is_not_abstract():
    assert not inspect.isabstract(aS3_literalField)


def test_as3_literalfield_constructor_exists():
    assert callable(aS3_literalField.__init__)


def test_as3_literalfield_constructor_args():
    sig = inspect.signature(aS3_literalField.__init__)
    params = list(sig.parameters.keys())



def test_as3_fieldlist_is_not_abstract():
    assert not inspect.isabstract(aS3_fieldList)


def test_as3_fieldlist_constructor_exists():
    assert callable(aS3_fieldList.__init__)


def test_as3_fieldlist_constructor_args():
    sig = inspect.signature(aS3_fieldList.__init__)
    params = list(sig.parameters.keys())



def test_exprorobjectliteral_is_not_abstract():
    assert not inspect.isabstract(exprOrObjectLiteral)


def test_exprorobjectliteral_constructor_exists():
    assert callable(exprOrObjectLiteral.__init__)


def test_exprorobjectliteral_constructor_args():
    sig = inspect.signature(exprOrObjectLiteral.__init__)
    params = list(sig.parameters.keys())



def test_as3_objectliteral_is_not_abstract():
    assert not inspect.isabstract(aS3_objectLiteral)


def test_as3_objectliteral_constructor_exists():
    assert callable(aS3_objectLiteral.__init__)


def test_as3_objectliteral_constructor_args():
    sig = inspect.signature(aS3_objectLiteral.__init__)
    params = list(sig.parameters.keys())



def test_as3_exprorobjectliteral_is_not_abstract():
    assert not inspect.isabstract(aS3_exprOrObjectLiteral)


def test_as3_exprorobjectliteral_constructor_exists():
    assert callable(aS3_exprOrObjectLiteral.__init__)


def test_as3_exprorobjectliteral_constructor_args():
    sig = inspect.signature(aS3_exprOrObjectLiteral.__init__)
    params = list(sig.parameters.keys())



def test_nonattributequalifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(nonAttributeQualifiedIdentifier)


def test_nonattributequalifiedidentifier_constructor_exists():
    assert callable(nonAttributeQualifiedIdentifier.__init__)


def test_nonattributequalifiedidentifier_constructor_args():
    sig = inspect.signature(nonAttributeQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_expressionqualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3_expressionQualifiedIdentifier)


def test_as3_expressionqualifiedidentifier_constructor_exists():
    assert callable(aS3_expressionQualifiedIdentifier.__init__)


def test_as3_expressionqualifiedidentifier_constructor_args():
    sig = inspect.signature(aS3_expressionQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_simplequalifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3_simpleQualifiedIdentifier)


def test_as3_simplequalifiedidentifier_constructor_exists():
    assert callable(aS3_simpleQualifiedIdentifier.__init__)


def test_as3_simplequalifiedidentifier_constructor_args():
    sig = inspect.signature(aS3_simpleQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_qualifier_is_not_abstract():
    assert not inspect.isabstract(aS3_qualifier)


def test_as3_qualifier_constructor_exists():
    assert callable(aS3_qualifier.__init__)


def test_as3_qualifier_constructor_args():
    sig = inspect.signature(aS3_qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_as3_qualifier_has_level():
    assert hasattr(aS3_qualifier, "level")
    descriptor = None
    for klass in aS3_qualifier.__mro__:
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



def test_as3_propertyidentifier_is_not_abstract():
    assert not inspect.isabstract(aS3_propertyIdentifier)


def test_as3_propertyidentifier_constructor_exists():
    assert callable(aS3_propertyIdentifier.__init__)


def test_as3_propertyidentifier_constructor_args():
    sig = inspect.signature(aS3_propertyIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_as3_proporident_is_not_abstract():
    assert not inspect.isabstract(aS3_propOrIdent)


def test_as3_proporident_constructor_exists():
    assert callable(aS3_propOrIdent.__init__)


def test_as3_proporident_constructor_args():
    sig = inspect.signature(aS3_propOrIdent.__init__)
    params = list(sig.parameters.keys())



def test_as3_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_assignmentExpression)


def test_as3_assignmentexpression_constructor_exists():
    assert callable(aS3_assignmentExpression.__init__)


def test_as3_assignmentexpression_constructor_args():
    sig = inspect.signature(aS3_assignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_as3_statement_is_not_abstract():
    assert not inspect.isabstract(aS3_Statement)


def test_as3_statement_constructor_exists():
    assert callable(aS3_Statement.__init__)


def test_as3_statement_constructor_args():
    sig = inspect.signature(aS3_Statement.__init__)
    params = list(sig.parameters.keys())



def test_as3_methodbody_is_not_abstract():
    assert not inspect.isabstract(aS3_MethodBody)


def test_as3_methodbody_constructor_exists():
    assert callable(aS3_MethodBody.__init__)


def test_as3_methodbody_constructor_args():
    sig = inspect.signature(aS3_MethodBody.__init__)
    params = list(sig.parameters.keys())



def test_as3_method_is_not_abstract():
    assert not inspect.isabstract(aS3_Method)


def test_as3_method_constructor_exists():
    assert callable(aS3_Method.__init__)


def test_as3_method_constructor_args():
    sig = inspect.signature(aS3_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anytype" in params, "Missing parameter 'anytype'"

def test_as3_method_has_name():
    assert hasattr(aS3_Method, "name")
    descriptor = None
    for klass in aS3_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3_method_has_anytype():
    assert hasattr(aS3_Method, "anytype")
    descriptor = None
    for klass in aS3_Method.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)



def test_as3_membervariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3_MemberVariableDeclaration)


def test_as3_membervariabledeclaration_constructor_exists():
    assert callable(aS3_MemberVariableDeclaration.__init__)


def test_as3_membervariabledeclaration_constructor_args():
    sig = inspect.signature(aS3_MemberVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "anytype" in params, "Missing parameter 'anytype'"
    assert "name" in params, "Missing parameter 'name'"

def test_as3_membervariabledeclaration_has_anytype():
    assert hasattr(aS3_MemberVariableDeclaration, "anytype")
    descriptor = None
    for klass in aS3_MemberVariableDeclaration.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)

def test_as3_membervariabledeclaration_has_name():
    assert hasattr(aS3_MemberVariableDeclaration, "name")
    descriptor = None
    for klass in aS3_MemberVariableDeclaration.__mro__:
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



def test_as3_identi_is_not_abstract():
    assert not inspect.isabstract(aS3_identi)


def test_as3_identi_constructor_exists():
    assert callable(aS3_identi.__init__)


def test_as3_identi_constructor_args():
    sig = inspect.signature(aS3_identi.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"

def test_as3_identi_has_i():
    assert hasattr(aS3_identi, "i")
    descriptor = None
    for klass in aS3_identi.__mro__:
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



def test_as3_ifstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_IfStatement)


def test_as3_ifstatement_constructor_exists():
    assert callable(aS3_IfStatement.__init__)


def test_as3_ifstatement_constructor_args():
    sig = inspect.signature(aS3_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_forstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_ForStatement)


def test_as3_forstatement_constructor_exists():
    assert callable(aS3_ForStatement.__init__)


def test_as3_forstatement_constructor_args():
    sig = inspect.signature(aS3_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_withstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_WithStatement)


def test_as3_withstatement_constructor_exists():
    assert callable(aS3_WithStatement.__init__)


def test_as3_withstatement_constructor_args():
    sig = inspect.signature(aS3_WithStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_defaultxmlnamespacestatement_is_not_abstract():
    assert not inspect.isabstract(aS3_DefaultXMLNamespaceStatement)


def test_as3_defaultxmlnamespacestatement_constructor_exists():
    assert callable(aS3_DefaultXMLNamespaceStatement.__init__)


def test_as3_defaultxmlnamespacestatement_constructor_args():
    sig = inspect.signature(aS3_DefaultXMLNamespaceStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_returnstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_ReturnStatement)


def test_as3_returnstatement_constructor_exists():
    assert callable(aS3_ReturnStatement.__init__)


def test_as3_returnstatement_constructor_args():
    sig = inspect.signature(aS3_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_ExpressionStatement)


def test_as3_expressionstatement_constructor_exists():
    assert callable(aS3_ExpressionStatement.__init__)


def test_as3_expressionstatement_constructor_args():
    sig = inspect.signature(aS3_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_ForEachStatement)


def test_as3_foreachstatement_constructor_exists():
    assert callable(aS3_ForEachStatement.__init__)


def test_as3_foreachstatement_constructor_args():
    sig = inspect.signature(aS3_ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_throwstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_ThrowStatement)


def test_as3_throwstatement_constructor_exists():
    assert callable(aS3_ThrowStatement.__init__)


def test_as3_throwstatement_constructor_args():
    sig = inspect.signature(aS3_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(aS3_DoWhileStatement)


def test_as3_dowhilestatement_constructor_exists():
    assert callable(aS3_DoWhileStatement.__init__)


def test_as3_dowhilestatement_constructor_args():
    sig = inspect.signature(aS3_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_switchstatement_is_not_abstract():
    assert not inspect.isabstract(aS3_SwitchStatement)


def test_as3_switchstatement_constructor_exists():
    assert callable(aS3_SwitchStatement.__init__)


def test_as3_switchstatement_constructor_args():
    sig = inspect.signature(aS3_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_trystatement_is_not_abstract():
    assert not inspect.isabstract(aS3_TryStatement)


def test_as3_trystatement_constructor_exists():
    assert callable(aS3_TryStatement.__init__)


def test_as3_trystatement_constructor_args():
    sig = inspect.signature(aS3_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_whilestatement_is_not_abstract():
    assert not inspect.isabstract(aS3_WhileStatement)


def test_as3_whilestatement_constructor_exists():
    assert callable(aS3_WhileStatement.__init__)


def test_as3_whilestatement_constructor_args():
    sig = inspect.signature(aS3_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_as3_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(aS3_VariableDeclaration)


def test_as3_variabledeclaration_constructor_exists():
    assert callable(aS3_VariableDeclaration.__init__)


def test_as3_variabledeclaration_constructor_args():
    sig = inspect.signature(aS3_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anytype" in params, "Missing parameter 'anytype'"

def test_as3_variabledeclaration_has_name():
    assert hasattr(aS3_VariableDeclaration, "name")
    descriptor = None
    for klass in aS3_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3_variabledeclaration_has_anytype():
    assert hasattr(aS3_VariableDeclaration, "anytype")
    descriptor = None
    for klass in aS3_VariableDeclaration.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)



def test_as3_class_is_not_abstract():
    assert not inspect.isabstract(aS3_Class)


def test_as3_class_constructor_exists():
    assert callable(aS3_Class.__init__)


def test_as3_class_constructor_args():
    sig = inspect.signature(aS3_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3_class_has_name():
    assert hasattr(aS3_Class, "name")
    descriptor = None
    for klass in aS3_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3_block_is_not_abstract():
    assert not inspect.isabstract(aS3_Block)


def test_as3_block_constructor_exists():
    assert callable(aS3_Block.__init__)


def test_as3_block_constructor_args():
    sig = inspect.signature(aS3_Block.__init__)
    params = list(sig.parameters.keys())



def test_as3_functionsignature_is_not_abstract():
    assert not inspect.isabstract(aS3_functionSignature)


def test_as3_functionsignature_constructor_exists():
    assert callable(aS3_functionSignature.__init__)


def test_as3_functionsignature_constructor_args():
    sig = inspect.signature(aS3_functionSignature.__init__)
    params = list(sig.parameters.keys())



def test_as3_functioncommon_is_not_abstract():
    assert not inspect.isabstract(aS3_functionCommon)


def test_as3_functioncommon_constructor_exists():
    assert callable(aS3_functionCommon.__init__)


def test_as3_functioncommon_constructor_args():
    sig = inspect.signature(aS3_functionCommon.__init__)
    params = list(sig.parameters.keys())



def test_as3_functionexpression_is_not_abstract():
    assert not inspect.isabstract(aS3_functionExpression)


def test_as3_functionexpression_constructor_exists():
    assert callable(aS3_functionExpression.__init__)


def test_as3_functionexpression_constructor_args():
    sig = inspect.signature(aS3_functionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_as3_functionexpression_has_name():
    assert hasattr(aS3_functionExpression, "name")
    descriptor = None
    for klass in aS3_functionExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_as3_parameter_is_not_abstract():
    assert not inspect.isabstract(aS3_Parameter)


def test_as3_parameter_constructor_exists():
    assert callable(aS3_Parameter.__init__)


def test_as3_parameter_constructor_args():
    sig = inspect.signature(aS3_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anytype" in params, "Missing parameter 'anytype'"

def test_as3_parameter_has_name():
    assert hasattr(aS3_Parameter, "name")
    descriptor = None
    for klass in aS3_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3_parameter_has_anytype():
    assert hasattr(aS3_Parameter, "anytype")
    descriptor = None
    for klass in aS3_Parameter.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)



def test_as3_accessorrole_is_not_abstract():
    assert not inspect.isabstract(aS3_AccessorRole)


def test_as3_accessorrole_constructor_exists():
    assert callable(aS3_AccessorRole.__init__)


def test_as3_accessorrole_constructor_args():
    sig = inspect.signature(aS3_AccessorRole.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_as3_accessorrole_has_accessor():
    assert hasattr(aS3_AccessorRole, "accessor")
    descriptor = None
    for klass in aS3_AccessorRole.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_as3_modifier_is_not_abstract():
    assert not inspect.isabstract(aS3_Modifier)


def test_as3_modifier_constructor_exists():
    assert callable(aS3_Modifier.__init__)


def test_as3_modifier_constructor_args():
    sig = inspect.signature(aS3_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "access" in params, "Missing parameter 'access'"
    assert "static" in params, "Missing parameter 'static'"
    assert "dynamic" in params, "Missing parameter 'dynamic'"
    assert "native" in params, "Missing parameter 'native'"

def test_as3_modifier_has_final():
    assert hasattr(aS3_Modifier, "final")
    descriptor = None
    for klass in aS3_Modifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_as3_modifier_has_access():
    assert hasattr(aS3_Modifier, "access")
    descriptor = None
    for klass in aS3_Modifier.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)

def test_as3_modifier_has_static():
    assert hasattr(aS3_Modifier, "static")
    descriptor = None
    for klass in aS3_Modifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_as3_modifier_has_dynamic():
    assert hasattr(aS3_Modifier, "dynamic")
    descriptor = None
    for klass in aS3_Modifier.__mro__:
        if "dynamic" in klass.__dict__:
            descriptor = klass.__dict__["dynamic"]
            break
    assert isinstance(descriptor, property)

def test_as3_modifier_has_native():
    assert hasattr(aS3_Modifier, "native")
    descriptor = None
    for klass in aS3_Modifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)



def test_as3_interfacemethod_is_not_abstract():
    assert not inspect.isabstract(aS3_InterfaceMethod)


def test_as3_interfacemethod_constructor_exists():
    assert callable(aS3_InterfaceMethod.__init__)


def test_as3_interfacemethod_constructor_args():
    sig = inspect.signature(aS3_InterfaceMethod.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "anytype" in params, "Missing parameter 'anytype'"

def test_as3_interfacemethod_has_name():
    assert hasattr(aS3_InterfaceMethod, "name")
    descriptor = None
    for klass in aS3_InterfaceMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3_interfacemethod_has_anytype():
    assert hasattr(aS3_InterfaceMethod, "anytype")
    descriptor = None
    for klass in aS3_InterfaceMethod.__mro__:
        if "anytype" in klass.__dict__:
            descriptor = klass.__dict__["anytype"]
            break
    assert isinstance(descriptor, property)



def test_as3_interface_is_not_abstract():
    assert not inspect.isabstract(aS3_Interface)


def test_as3_interface_constructor_exists():
    assert callable(aS3_Interface.__init__)


def test_as3_interface_constructor_args():
    sig = inspect.signature(aS3_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "access" in params, "Missing parameter 'access'"

def test_as3_interface_has_name():
    assert hasattr(aS3_Interface, "name")
    descriptor = None
    for klass in aS3_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_as3_interface_has_access():
    assert hasattr(aS3_Interface, "access")
    descriptor = None
    for klass in aS3_Interface.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_as3_expression_is_not_abstract():
    assert not inspect.isabstract(aS3_Expression)


def test_as3_expression_constructor_exists():
    assert callable(aS3_Expression.__init__)


def test_as3_expression_constructor_args():
    sig = inspect.signature(aS3_Expression.__init__)
    params = list(sig.parameters.keys())

def test_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PROTECTED",
        "PRIVATE",
        "PUBLIC",
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
aS3_Member_strategy = st.builds(
    aS3_Member,
)
aS3_Uses_strategy = st.builds(
    aS3_Uses,
    anytype=
        safe_text,
    type=
        safe_text
)
aS3_Import_strategy = st.builds(
    aS3_Import,
    importedNamespace=
        safe_text
)
aS3_directive_strategy = st.builds(
    aS3_directive,
)
aS3_EObject_strategy = st.builds(
    aS3_EObject,
)
aS3_Imports_strategy = st.builds(
    aS3_Imports,
)
aS3_Package_strategy = st.builds(
    aS3_Package,
    name=
        safe_text
)
aS3_Model_strategy = st.builds(
    aS3_Model,
)
aS3_annotationField_strategy = st.builds(
    aS3_annotationField,
    name=
        safe_text
)
aS3_annotationFields_strategy = st.builds(
    aS3_annotationFields,
)
aS3_Annotation_strategy = st.builds(
    aS3_Annotation,
    name=
        safe_text
)
aS3_forInClauseTail_strategy = st.builds(
    aS3_forInClauseTail,
)
aS3_forInClauseDecl_strategy = st.builds(
    aS3_forInClauseDecl,
)
aS3_forIter_strategy = st.builds(
    aS3_forIter,
)
aS3_forCond_strategy = st.builds(
    aS3_forCond,
)
aS3_forInit_strategy = st.builds(
    aS3_forInit,
)
aS3_traditionalForClause_strategy = st.builds(
    aS3_traditionalForClause,
)
aS3_forInClause_strategy = st.builds(
    aS3_forInClause,
)
aS3_DefaultStatement_strategy = st.builds(
    aS3_DefaultStatement,
)
aS3_CaseStatement_strategy = st.builds(
    aS3_CaseStatement,
)
aS3_finallyBlock_strategy = st.builds(
    aS3_finallyBlock,
)
aS3_switchBlock_strategy = st.builds(
    aS3_switchBlock,
)
SwitchStatement_strategy = st.builds(
    SwitchStatement,
)
aS3_Condition_strategy = st.builds(
    aS3_Condition,
)
finallyBlock_strategy = st.builds(
    finallyBlock,
)
aS3_parameterDefault_strategy = st.builds(
    aS3_parameterDefault,
)
parameterDeclaration_strategy = st.builds(
    parameterDeclaration,
)
aS3_parameterRestDeclaration_strategy = st.builds(
    aS3_parameterRestDeclaration,
)
aS3_basicParameterDeclaration_strategy = st.builds(
    aS3_basicParameterDeclaration,
)
aS3_parameterDeclaration_strategy = st.builds(
    aS3_parameterDeclaration,
)
aS3_parameterDeclarationList_strategy = st.builds(
    aS3_parameterDeclarationList,
)
aS3_catchBlock_strategy = st.builds(
    aS3_catchBlock,
)
expressionQualifiedIdentifier_strategy = st.builds(
    expressionQualifiedIdentifier,
)
aS3_fullNewSubexpression_strategy = st.builds(
    aS3_fullNewSubexpression,
    fnsd=
        safe_text
)
aS3_regexpLiteral_strategy = st.builds(
    aS3_regexpLiteral,
    s=
        safe_text
)
aS3_arguments_strategy = st.builds(
    aS3_arguments,
)
aS3_primaryExpression_strategy = st.builds(
    aS3_primaryExpression,
)
aS3_unaryExpressionNotPlusMinus_strategy = st.builds(
    aS3_unaryExpressionNotPlusMinus,
    de=
        safe_text,
    in_=
        safe_text
)
aS3_encapsulatedExpression_strategy = st.builds(
    aS3_encapsulatedExpression,
)
aS3_newExpression_strategy = st.builds(
    aS3_newExpression,
)
aS3_additiveExpression_strategy = st.builds(
    aS3_additiveExpression,
    o=
        safe_text
)
aS3_shiftExpression_strategy = st.builds(
    aS3_shiftExpression,
    o=
        safe_text
)
aS3_relationalExpression_strategy = st.builds(
    aS3_relationalExpression,
    o=
        safe_text
)
aS3_equalityExpression_strategy = st.builds(
    aS3_equalityExpression,
    o=
        safe_text
)
aS3_bitwiseAndExpression_strategy = st.builds(
    aS3_bitwiseAndExpression,
    o=
        safe_text
)
aS3_bitwiseXorExpression_strategy = st.builds(
    aS3_bitwiseXorExpression,
    o=
        safe_text
)
aS3_bitwiseOrExpression_strategy = st.builds(
    aS3_bitwiseOrExpression,
    o=
        safe_text
)
aS3_logicalAndExpression_strategy = st.builds(
    aS3_logicalAndExpression,
    o=
        safe_text
)
unaryExpressionNotPlusMinus_strategy = st.builds(
    unaryExpressionNotPlusMinus,
)
aS3_postfixExpression_strategy = st.builds(
    aS3_postfixExpression,
)
aS3_unaryExpression_strategy = st.builds(
    aS3_unaryExpression,
)
aS3_multiplicativeExpression_strategy = st.builds(
    aS3_multiplicativeExpression,
    o=
        safe_text
)
assignmentExpression_strategy = st.builds(
    assignmentExpression,
)
aS3_conditionalExpression_strategy = st.builds(
    aS3_conditionalExpression,
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
aS3_XmlConstant_strategy = st.builds(
    aS3_XmlConstant,
    value=
        safe_text
)
aS3_Undefined_strategy = st.builds(
    aS3_Undefined,
)
aS3_RegexpConstant_strategy = st.builds(
    aS3_RegexpConstant,
)
aS3_NumberConstant_strategy = st.builds(
    aS3_NumberConstant,
    value=
        safe_text
)
aS3_SymbolRef_strategy = st.builds(
    aS3_SymbolRef,
)
aS3_This_strategy = st.builds(
    aS3_This,
)
aS3_BoolConstant_strategy = st.builds(
    aS3_BoolConstant,
    value=
        safe_text
)
aS3_Null_strategy = st.builds(
    aS3_Null,
)
aS3_StringConstant_strategy = st.builds(
    aS3_StringConstant,
    value=
        safe_text
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
aS3_expressionList_strategy = st.builds(
    aS3_expressionList,
)
aS3_switchStatementList_strategy = st.builds(
    aS3_switchStatementList,
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
aS3_nonemptyElementList_strategy = st.builds(
    aS3_nonemptyElementList,
)
aS3_elementList_strategy = st.builds(
    aS3_elementList,
)
aS3_arrayLiteral_strategy = st.builds(
    aS3_arrayLiteral,
)
qualifiedIdent_strategy = st.builds(
    qualifiedIdent,
)
aS3_namespaceName_strategy = st.builds(
    aS3_namespaceName,
    level=
        safe_text
)
aS3_qualifiedIdentifier_strategy = st.builds(
    aS3_qualifiedIdentifier,
)
qualifiedIdentifier_strategy = st.builds(
    qualifiedIdentifier,
)
aS3_e4xAttributeIdentifier_strategy = st.builds(
    aS3_e4xAttributeIdentifier,
)
aS3_nonAttributeQualifiedIdentifier_strategy = st.builds(
    aS3_nonAttributeQualifiedIdentifier,
)
aS3_brackets_strategy = st.builds(
    aS3_brackets,
)
conditionalExpression_strategy = st.builds(
    conditionalExpression,
)
aS3_logicalOrExpression_strategy = st.builds(
    aS3_logicalOrExpression,
    o=
        safe_text
)
aS3_conditionalSubExpression_strategy = st.builds(
    aS3_conditionalSubExpression,
)
aS3_identifier_strategy = st.builds(
    aS3_identifier,
)
aS3_typeExpression_strategy = st.builds(
    aS3_typeExpression,
)
catchBlock_strategy = st.builds(
    catchBlock,
)
propertyIdentifier_strategy = st.builds(
    propertyIdentifier,
)
aS3_qualifiedIdent_strategy = st.builds(
    aS3_qualifiedIdent,
)
aS3_element_strategy = st.builds(
    aS3_element,
)
aS3_fieldName_strategy = st.builds(
    aS3_fieldName,
    number=
        safe_text,
    name=
        safe_text
)
aS3_literalField_strategy = st.builds(
    aS3_literalField,
)
aS3_fieldList_strategy = st.builds(
    aS3_fieldList,
)
exprOrObjectLiteral_strategy = st.builds(
    exprOrObjectLiteral,
)
aS3_objectLiteral_strategy = st.builds(
    aS3_objectLiteral,
)
aS3_exprOrObjectLiteral_strategy = st.builds(
    aS3_exprOrObjectLiteral,
)
nonAttributeQualifiedIdentifier_strategy = st.builds(
    nonAttributeQualifiedIdentifier,
)
aS3_expressionQualifiedIdentifier_strategy = st.builds(
    aS3_expressionQualifiedIdentifier,
)
aS3_simpleQualifiedIdentifier_strategy = st.builds(
    aS3_simpleQualifiedIdentifier,
)
aS3_qualifier_strategy = st.builds(
    aS3_qualifier,
    level=
        safe_text
)
qualifier_strategy = st.builds(
    qualifier,
)
aS3_propertyIdentifier_strategy = st.builds(
    aS3_propertyIdentifier,
)
aS3_propOrIdent_strategy = st.builds(
    aS3_propOrIdent,
)
aS3_assignmentExpression_strategy = st.builds(
    aS3_assignmentExpression,
)
aS3_Statement_strategy = st.builds(
    aS3_Statement,
)
aS3_MethodBody_strategy = st.builds(
    aS3_MethodBody,
)
aS3_Method_strategy = st.builds(
    aS3_Method,
    name=
        safe_text,
    anytype=
        safe_text
)
aS3_MemberVariableDeclaration_strategy = st.builds(
    aS3_MemberVariableDeclaration,
    anytype=
        safe_text,
    name=
        safe_text
)
forInClauseDecl_strategy = st.builds(
    forInClauseDecl,
)
aS3_identi_strategy = st.builds(
    aS3_identi,
    i=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
aS3_IfStatement_strategy = st.builds(
    aS3_IfStatement,
)
aS3_ForStatement_strategy = st.builds(
    aS3_ForStatement,
)
aS3_WithStatement_strategy = st.builds(
    aS3_WithStatement,
)
aS3_DefaultXMLNamespaceStatement_strategy = st.builds(
    aS3_DefaultXMLNamespaceStatement,
)
aS3_ReturnStatement_strategy = st.builds(
    aS3_ReturnStatement,
)
aS3_ExpressionStatement_strategy = st.builds(
    aS3_ExpressionStatement,
)
aS3_ForEachStatement_strategy = st.builds(
    aS3_ForEachStatement,
)
aS3_ThrowStatement_strategy = st.builds(
    aS3_ThrowStatement,
)
aS3_DoWhileStatement_strategy = st.builds(
    aS3_DoWhileStatement,
)
aS3_SwitchStatement_strategy = st.builds(
    aS3_SwitchStatement,
)
aS3_TryStatement_strategy = st.builds(
    aS3_TryStatement,
)
aS3_WhileStatement_strategy = st.builds(
    aS3_WhileStatement,
)
aS3_VariableDeclaration_strategy = st.builds(
    aS3_VariableDeclaration,
    name=
        safe_text,
    anytype=
        safe_text
)
aS3_Class_strategy = st.builds(
    aS3_Class,
    name=
        safe_text
)
aS3_Block_strategy = st.builds(
    aS3_Block,
)
aS3_functionSignature_strategy = st.builds(
    aS3_functionSignature,
)
aS3_functionCommon_strategy = st.builds(
    aS3_functionCommon,
)
aS3_functionExpression_strategy = st.builds(
    aS3_functionExpression,
    name=
        safe_text
)
aS3_Parameter_strategy = st.builds(
    aS3_Parameter,
    name=
        safe_text,
    anytype=
        safe_text
)
aS3_AccessorRole_strategy = st.builds(
    aS3_AccessorRole,
    accessor=
        safe_text
)
aS3_Modifier_strategy = st.builds(
    aS3_Modifier,
    final=
        st.booleans(),
    access=
        safe_text,
    static=
        st.booleans(),
    dynamic=
        st.booleans(),
    native=
        st.booleans()
)
aS3_InterfaceMethod_strategy = st.builds(
    aS3_InterfaceMethod,
    name=
        safe_text,
    anytype=
        safe_text
)
aS3_Interface_strategy = st.builds(
    aS3_Interface,
    name=
        safe_text,
    access=
        safe_text
)
aS3_Expression_strategy = st.builds(
    aS3_Expression,
)

@given(instance=aS3_Member_strategy)
@settings(max_examples=50)
def test_as3_member_instantiation(instance):
    assert isinstance(instance, aS3_Member)

@given(instance=aS3_Uses_strategy)
@settings(max_examples=50)
def test_as3_uses_instantiation(instance):
    assert isinstance(instance, aS3_Uses)



@given(instance=aS3_Uses_strategy)
def test_as3_uses_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original



@given(instance=aS3_Uses_strategy)
def test_as3_uses_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=aS3_Import_strategy)
@settings(max_examples=50)
def test_as3_import_instantiation(instance):
    assert isinstance(instance, aS3_Import)



@given(instance=aS3_Import_strategy)
def test_as3_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=aS3_directive_strategy)
@settings(max_examples=50)
def test_as3_directive_instantiation(instance):
    assert isinstance(instance, aS3_directive)

@given(instance=aS3_EObject_strategy)
@settings(max_examples=50)
def test_as3_eobject_instantiation(instance):
    assert isinstance(instance, aS3_EObject)

@given(instance=aS3_Imports_strategy)
@settings(max_examples=50)
def test_as3_imports_instantiation(instance):
    assert isinstance(instance, aS3_Imports)

@given(instance=aS3_Package_strategy)
@settings(max_examples=50)
def test_as3_package_instantiation(instance):
    assert isinstance(instance, aS3_Package)



@given(instance=aS3_Package_strategy)
def test_as3_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3_Model_strategy)
@settings(max_examples=50)
def test_as3_model_instantiation(instance):
    assert isinstance(instance, aS3_Model)

@given(instance=aS3_annotationField_strategy)
@settings(max_examples=50)
def test_as3_annotationfield_instantiation(instance):
    assert isinstance(instance, aS3_annotationField)



@given(instance=aS3_annotationField_strategy)
def test_as3_annotationfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3_annotationFields_strategy)
@settings(max_examples=50)
def test_as3_annotationfields_instantiation(instance):
    assert isinstance(instance, aS3_annotationFields)

@given(instance=aS3_Annotation_strategy)
@settings(max_examples=50)
def test_as3_annotation_instantiation(instance):
    assert isinstance(instance, aS3_Annotation)



@given(instance=aS3_Annotation_strategy)
def test_as3_annotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3_forInClauseTail_strategy)
@settings(max_examples=50)
def test_as3_forinclausetail_instantiation(instance):
    assert isinstance(instance, aS3_forInClauseTail)

@given(instance=aS3_forInClauseDecl_strategy)
@settings(max_examples=50)
def test_as3_forinclausedecl_instantiation(instance):
    assert isinstance(instance, aS3_forInClauseDecl)

@given(instance=aS3_forIter_strategy)
@settings(max_examples=50)
def test_as3_foriter_instantiation(instance):
    assert isinstance(instance, aS3_forIter)

@given(instance=aS3_forCond_strategy)
@settings(max_examples=50)
def test_as3_forcond_instantiation(instance):
    assert isinstance(instance, aS3_forCond)

@given(instance=aS3_forInit_strategy)
@settings(max_examples=50)
def test_as3_forinit_instantiation(instance):
    assert isinstance(instance, aS3_forInit)

@given(instance=aS3_traditionalForClause_strategy)
@settings(max_examples=50)
def test_as3_traditionalforclause_instantiation(instance):
    assert isinstance(instance, aS3_traditionalForClause)

@given(instance=aS3_forInClause_strategy)
@settings(max_examples=50)
def test_as3_forinclause_instantiation(instance):
    assert isinstance(instance, aS3_forInClause)

@given(instance=aS3_DefaultStatement_strategy)
@settings(max_examples=50)
def test_as3_defaultstatement_instantiation(instance):
    assert isinstance(instance, aS3_DefaultStatement)

@given(instance=aS3_CaseStatement_strategy)
@settings(max_examples=50)
def test_as3_casestatement_instantiation(instance):
    assert isinstance(instance, aS3_CaseStatement)

@given(instance=aS3_finallyBlock_strategy)
@settings(max_examples=50)
def test_as3_finallyblock_instantiation(instance):
    assert isinstance(instance, aS3_finallyBlock)

@given(instance=aS3_switchBlock_strategy)
@settings(max_examples=50)
def test_as3_switchblock_instantiation(instance):
    assert isinstance(instance, aS3_switchBlock)

@given(instance=SwitchStatement_strategy)
@settings(max_examples=50)
def test_switchstatement_instantiation(instance):
    assert isinstance(instance, SwitchStatement)

@given(instance=aS3_Condition_strategy)
@settings(max_examples=50)
def test_as3_condition_instantiation(instance):
    assert isinstance(instance, aS3_Condition)

@given(instance=finallyBlock_strategy)
@settings(max_examples=50)
def test_finallyblock_instantiation(instance):
    assert isinstance(instance, finallyBlock)

@given(instance=aS3_parameterDefault_strategy)
@settings(max_examples=50)
def test_as3_parameterdefault_instantiation(instance):
    assert isinstance(instance, aS3_parameterDefault)

@given(instance=parameterDeclaration_strategy)
@settings(max_examples=50)
def test_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, parameterDeclaration)

@given(instance=aS3_parameterRestDeclaration_strategy)
@settings(max_examples=50)
def test_as3_parameterrestdeclaration_instantiation(instance):
    assert isinstance(instance, aS3_parameterRestDeclaration)

@given(instance=aS3_basicParameterDeclaration_strategy)
@settings(max_examples=50)
def test_as3_basicparameterdeclaration_instantiation(instance):
    assert isinstance(instance, aS3_basicParameterDeclaration)

@given(instance=aS3_parameterDeclaration_strategy)
@settings(max_examples=50)
def test_as3_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, aS3_parameterDeclaration)

@given(instance=aS3_parameterDeclarationList_strategy)
@settings(max_examples=50)
def test_as3_parameterdeclarationlist_instantiation(instance):
    assert isinstance(instance, aS3_parameterDeclarationList)

@given(instance=aS3_catchBlock_strategy)
@settings(max_examples=50)
def test_as3_catchblock_instantiation(instance):
    assert isinstance(instance, aS3_catchBlock)

@given(instance=expressionQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_expressionqualifiedidentifier_instantiation(instance):
    assert isinstance(instance, expressionQualifiedIdentifier)

@given(instance=aS3_fullNewSubexpression_strategy)
@settings(max_examples=50)
def test_as3_fullnewsubexpression_instantiation(instance):
    assert isinstance(instance, aS3_fullNewSubexpression)



@given(instance=aS3_fullNewSubexpression_strategy)
def test_as3_fullnewsubexpression_fnsd_setter(instance):
    original = instance.fnsd
    instance.fnsd = original
    assert instance.fnsd == original

@given(instance=aS3_regexpLiteral_strategy)
@settings(max_examples=50)
def test_as3_regexpliteral_instantiation(instance):
    assert isinstance(instance, aS3_regexpLiteral)



@given(instance=aS3_regexpLiteral_strategy)
def test_as3_regexpliteral_s_setter(instance):
    original = instance.s
    instance.s = original
    assert instance.s == original

@given(instance=aS3_arguments_strategy)
@settings(max_examples=50)
def test_as3_arguments_instantiation(instance):
    assert isinstance(instance, aS3_arguments)

@given(instance=aS3_primaryExpression_strategy)
@settings(max_examples=50)
def test_as3_primaryexpression_instantiation(instance):
    assert isinstance(instance, aS3_primaryExpression)

@given(instance=aS3_unaryExpressionNotPlusMinus_strategy)
@settings(max_examples=50)
def test_as3_unaryexpressionnotplusminus_instantiation(instance):
    assert isinstance(instance, aS3_unaryExpressionNotPlusMinus)



@given(instance=aS3_unaryExpressionNotPlusMinus_strategy)
def test_as3_unaryexpressionnotplusminus_de_setter(instance):
    original = instance.de
    instance.de = original
    assert instance.de == original



@given(instance=aS3_unaryExpressionNotPlusMinus_strategy)
def test_as3_unaryexpressionnotplusminus_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=aS3_encapsulatedExpression_strategy)
@settings(max_examples=50)
def test_as3_encapsulatedexpression_instantiation(instance):
    assert isinstance(instance, aS3_encapsulatedExpression)

@given(instance=aS3_newExpression_strategy)
@settings(max_examples=50)
def test_as3_newexpression_instantiation(instance):
    assert isinstance(instance, aS3_newExpression)

@given(instance=aS3_additiveExpression_strategy)
@settings(max_examples=50)
def test_as3_additiveexpression_instantiation(instance):
    assert isinstance(instance, aS3_additiveExpression)



@given(instance=aS3_additiveExpression_strategy)
def test_as3_additiveexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3_shiftExpression_strategy)
@settings(max_examples=50)
def test_as3_shiftexpression_instantiation(instance):
    assert isinstance(instance, aS3_shiftExpression)



@given(instance=aS3_shiftExpression_strategy)
def test_as3_shiftexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3_relationalExpression_strategy)
@settings(max_examples=50)
def test_as3_relationalexpression_instantiation(instance):
    assert isinstance(instance, aS3_relationalExpression)



@given(instance=aS3_relationalExpression_strategy)
def test_as3_relationalexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3_equalityExpression_strategy)
@settings(max_examples=50)
def test_as3_equalityexpression_instantiation(instance):
    assert isinstance(instance, aS3_equalityExpression)



@given(instance=aS3_equalityExpression_strategy)
def test_as3_equalityexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3_bitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_as3_bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, aS3_bitwiseAndExpression)



@given(instance=aS3_bitwiseAndExpression_strategy)
def test_as3_bitwiseandexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3_bitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_as3_bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, aS3_bitwiseXorExpression)



@given(instance=aS3_bitwiseXorExpression_strategy)
def test_as3_bitwisexorexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3_bitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_as3_bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, aS3_bitwiseOrExpression)



@given(instance=aS3_bitwiseOrExpression_strategy)
def test_as3_bitwiseorexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3_logicalAndExpression_strategy)
@settings(max_examples=50)
def test_as3_logicalandexpression_instantiation(instance):
    assert isinstance(instance, aS3_logicalAndExpression)



@given(instance=aS3_logicalAndExpression_strategy)
def test_as3_logicalandexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=unaryExpressionNotPlusMinus_strategy)
@settings(max_examples=50)
def test_unaryexpressionnotplusminus_instantiation(instance):
    assert isinstance(instance, unaryExpressionNotPlusMinus)

@given(instance=aS3_postfixExpression_strategy)
@settings(max_examples=50)
def test_as3_postfixexpression_instantiation(instance):
    assert isinstance(instance, aS3_postfixExpression)

@given(instance=aS3_unaryExpression_strategy)
@settings(max_examples=50)
def test_as3_unaryexpression_instantiation(instance):
    assert isinstance(instance, aS3_unaryExpression)

@given(instance=aS3_multiplicativeExpression_strategy)
@settings(max_examples=50)
def test_as3_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, aS3_multiplicativeExpression)



@given(instance=aS3_multiplicativeExpression_strategy)
def test_as3_multiplicativeexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=assignmentExpression_strategy)
@settings(max_examples=50)
def test_assignmentexpression_instantiation(instance):
    assert isinstance(instance, assignmentExpression)

@given(instance=aS3_conditionalExpression_strategy)
@settings(max_examples=50)
def test_as3_conditionalexpression_instantiation(instance):
    assert isinstance(instance, aS3_conditionalExpression)



@given(instance=aS3_conditionalExpression_strategy)
def test_as3_conditionalexpression_op_setter(instance):
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

@given(instance=aS3_XmlConstant_strategy)
@settings(max_examples=50)
def test_as3_xmlconstant_instantiation(instance):
    assert isinstance(instance, aS3_XmlConstant)



@given(instance=aS3_XmlConstant_strategy)
def test_as3_xmlconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aS3_Undefined_strategy)
@settings(max_examples=50)
def test_as3_undefined_instantiation(instance):
    assert isinstance(instance, aS3_Undefined)

@given(instance=aS3_RegexpConstant_strategy)
@settings(max_examples=50)
def test_as3_regexpconstant_instantiation(instance):
    assert isinstance(instance, aS3_RegexpConstant)

@given(instance=aS3_NumberConstant_strategy)
@settings(max_examples=50)
def test_as3_numberconstant_instantiation(instance):
    assert isinstance(instance, aS3_NumberConstant)



@given(instance=aS3_NumberConstant_strategy)
def test_as3_numberconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aS3_SymbolRef_strategy)
@settings(max_examples=50)
def test_as3_symbolref_instantiation(instance):
    assert isinstance(instance, aS3_SymbolRef)

@given(instance=aS3_This_strategy)
@settings(max_examples=50)
def test_as3_this_instantiation(instance):
    assert isinstance(instance, aS3_This)

@given(instance=aS3_BoolConstant_strategy)
@settings(max_examples=50)
def test_as3_boolconstant_instantiation(instance):
    assert isinstance(instance, aS3_BoolConstant)



@given(instance=aS3_BoolConstant_strategy)
def test_as3_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aS3_Null_strategy)
@settings(max_examples=50)
def test_as3_null_instantiation(instance):
    assert isinstance(instance, aS3_Null)

@given(instance=aS3_StringConstant_strategy)
@settings(max_examples=50)
def test_as3_stringconstant_instantiation(instance):
    assert isinstance(instance, aS3_StringConstant)



@given(instance=aS3_StringConstant_strategy)
def test_as3_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=aS3_expressionList_strategy)
@settings(max_examples=50)
def test_as3_expressionlist_instantiation(instance):
    assert isinstance(instance, aS3_expressionList)

@given(instance=aS3_switchStatementList_strategy)
@settings(max_examples=50)
def test_as3_switchstatementlist_instantiation(instance):
    assert isinstance(instance, aS3_switchStatementList)

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

@given(instance=aS3_nonemptyElementList_strategy)
@settings(max_examples=50)
def test_as3_nonemptyelementlist_instantiation(instance):
    assert isinstance(instance, aS3_nonemptyElementList)

@given(instance=aS3_elementList_strategy)
@settings(max_examples=50)
def test_as3_elementlist_instantiation(instance):
    assert isinstance(instance, aS3_elementList)

@given(instance=aS3_arrayLiteral_strategy)
@settings(max_examples=50)
def test_as3_arrayliteral_instantiation(instance):
    assert isinstance(instance, aS3_arrayLiteral)

@given(instance=qualifiedIdent_strategy)
@settings(max_examples=50)
def test_qualifiedident_instantiation(instance):
    assert isinstance(instance, qualifiedIdent)

@given(instance=aS3_namespaceName_strategy)
@settings(max_examples=50)
def test_as3_namespacename_instantiation(instance):
    assert isinstance(instance, aS3_namespaceName)



@given(instance=aS3_namespaceName_strategy)
def test_as3_namespacename_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=aS3_qualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_as3_qualifiedidentifier_instantiation(instance):
    assert isinstance(instance, aS3_qualifiedIdentifier)

@given(instance=qualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_qualifiedidentifier_instantiation(instance):
    assert isinstance(instance, qualifiedIdentifier)

@given(instance=aS3_e4xAttributeIdentifier_strategy)
@settings(max_examples=50)
def test_as3_e4xattributeidentifier_instantiation(instance):
    assert isinstance(instance, aS3_e4xAttributeIdentifier)

@given(instance=aS3_nonAttributeQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_as3_nonattributequalifiedidentifier_instantiation(instance):
    assert isinstance(instance, aS3_nonAttributeQualifiedIdentifier)

@given(instance=aS3_brackets_strategy)
@settings(max_examples=50)
def test_as3_brackets_instantiation(instance):
    assert isinstance(instance, aS3_brackets)

@given(instance=conditionalExpression_strategy)
@settings(max_examples=50)
def test_conditionalexpression_instantiation(instance):
    assert isinstance(instance, conditionalExpression)

@given(instance=aS3_logicalOrExpression_strategy)
@settings(max_examples=50)
def test_as3_logicalorexpression_instantiation(instance):
    assert isinstance(instance, aS3_logicalOrExpression)



@given(instance=aS3_logicalOrExpression_strategy)
def test_as3_logicalorexpression_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=aS3_conditionalSubExpression_strategy)
@settings(max_examples=50)
def test_as3_conditionalsubexpression_instantiation(instance):
    assert isinstance(instance, aS3_conditionalSubExpression)

@given(instance=aS3_identifier_strategy)
@settings(max_examples=50)
def test_as3_identifier_instantiation(instance):
    assert isinstance(instance, aS3_identifier)

@given(instance=aS3_typeExpression_strategy)
@settings(max_examples=50)
def test_as3_typeexpression_instantiation(instance):
    assert isinstance(instance, aS3_typeExpression)

@given(instance=catchBlock_strategy)
@settings(max_examples=50)
def test_catchblock_instantiation(instance):
    assert isinstance(instance, catchBlock)

@given(instance=propertyIdentifier_strategy)
@settings(max_examples=50)
def test_propertyidentifier_instantiation(instance):
    assert isinstance(instance, propertyIdentifier)

@given(instance=aS3_qualifiedIdent_strategy)
@settings(max_examples=50)
def test_as3_qualifiedident_instantiation(instance):
    assert isinstance(instance, aS3_qualifiedIdent)

@given(instance=aS3_element_strategy)
@settings(max_examples=50)
def test_as3_element_instantiation(instance):
    assert isinstance(instance, aS3_element)

@given(instance=aS3_fieldName_strategy)
@settings(max_examples=50)
def test_as3_fieldname_instantiation(instance):
    assert isinstance(instance, aS3_fieldName)



@given(instance=aS3_fieldName_strategy)
def test_as3_fieldname_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=aS3_fieldName_strategy)
def test_as3_fieldname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3_literalField_strategy)
@settings(max_examples=50)
def test_as3_literalfield_instantiation(instance):
    assert isinstance(instance, aS3_literalField)

@given(instance=aS3_fieldList_strategy)
@settings(max_examples=50)
def test_as3_fieldlist_instantiation(instance):
    assert isinstance(instance, aS3_fieldList)

@given(instance=exprOrObjectLiteral_strategy)
@settings(max_examples=50)
def test_exprorobjectliteral_instantiation(instance):
    assert isinstance(instance, exprOrObjectLiteral)

@given(instance=aS3_objectLiteral_strategy)
@settings(max_examples=50)
def test_as3_objectliteral_instantiation(instance):
    assert isinstance(instance, aS3_objectLiteral)

@given(instance=aS3_exprOrObjectLiteral_strategy)
@settings(max_examples=50)
def test_as3_exprorobjectliteral_instantiation(instance):
    assert isinstance(instance, aS3_exprOrObjectLiteral)

@given(instance=nonAttributeQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_nonattributequalifiedidentifier_instantiation(instance):
    assert isinstance(instance, nonAttributeQualifiedIdentifier)

@given(instance=aS3_expressionQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_as3_expressionqualifiedidentifier_instantiation(instance):
    assert isinstance(instance, aS3_expressionQualifiedIdentifier)

@given(instance=aS3_simpleQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_as3_simplequalifiedidentifier_instantiation(instance):
    assert isinstance(instance, aS3_simpleQualifiedIdentifier)

@given(instance=aS3_qualifier_strategy)
@settings(max_examples=50)
def test_as3_qualifier_instantiation(instance):
    assert isinstance(instance, aS3_qualifier)



@given(instance=aS3_qualifier_strategy)
def test_as3_qualifier_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=qualifier_strategy)
@settings(max_examples=50)
def test_qualifier_instantiation(instance):
    assert isinstance(instance, qualifier)

@given(instance=aS3_propertyIdentifier_strategy)
@settings(max_examples=50)
def test_as3_propertyidentifier_instantiation(instance):
    assert isinstance(instance, aS3_propertyIdentifier)

@given(instance=aS3_propOrIdent_strategy)
@settings(max_examples=50)
def test_as3_proporident_instantiation(instance):
    assert isinstance(instance, aS3_propOrIdent)

@given(instance=aS3_assignmentExpression_strategy)
@settings(max_examples=50)
def test_as3_assignmentexpression_instantiation(instance):
    assert isinstance(instance, aS3_assignmentExpression)

@given(instance=aS3_Statement_strategy)
@settings(max_examples=50)
def test_as3_statement_instantiation(instance):
    assert isinstance(instance, aS3_Statement)

@given(instance=aS3_MethodBody_strategy)
@settings(max_examples=50)
def test_as3_methodbody_instantiation(instance):
    assert isinstance(instance, aS3_MethodBody)

@given(instance=aS3_Method_strategy)
@settings(max_examples=50)
def test_as3_method_instantiation(instance):
    assert isinstance(instance, aS3_Method)



@given(instance=aS3_Method_strategy)
def test_as3_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aS3_Method_strategy)
def test_as3_method_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3_MemberVariableDeclaration_strategy)
@settings(max_examples=50)
def test_as3_membervariabledeclaration_instantiation(instance):
    assert isinstance(instance, aS3_MemberVariableDeclaration)



@given(instance=aS3_MemberVariableDeclaration_strategy)
def test_as3_membervariabledeclaration_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original



@given(instance=aS3_MemberVariableDeclaration_strategy)
def test_as3_membervariabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=forInClauseDecl_strategy)
@settings(max_examples=50)
def test_forinclausedecl_instantiation(instance):
    assert isinstance(instance, forInClauseDecl)

@given(instance=aS3_identi_strategy)
@settings(max_examples=50)
def test_as3_identi_instantiation(instance):
    assert isinstance(instance, aS3_identi)



@given(instance=aS3_identi_strategy)
def test_as3_identi_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=aS3_IfStatement_strategy)
@settings(max_examples=50)
def test_as3_ifstatement_instantiation(instance):
    assert isinstance(instance, aS3_IfStatement)

@given(instance=aS3_ForStatement_strategy)
@settings(max_examples=50)
def test_as3_forstatement_instantiation(instance):
    assert isinstance(instance, aS3_ForStatement)

@given(instance=aS3_WithStatement_strategy)
@settings(max_examples=50)
def test_as3_withstatement_instantiation(instance):
    assert isinstance(instance, aS3_WithStatement)

@given(instance=aS3_DefaultXMLNamespaceStatement_strategy)
@settings(max_examples=50)
def test_as3_defaultxmlnamespacestatement_instantiation(instance):
    assert isinstance(instance, aS3_DefaultXMLNamespaceStatement)

@given(instance=aS3_ReturnStatement_strategy)
@settings(max_examples=50)
def test_as3_returnstatement_instantiation(instance):
    assert isinstance(instance, aS3_ReturnStatement)

@given(instance=aS3_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_as3_expressionstatement_instantiation(instance):
    assert isinstance(instance, aS3_ExpressionStatement)

@given(instance=aS3_ForEachStatement_strategy)
@settings(max_examples=50)
def test_as3_foreachstatement_instantiation(instance):
    assert isinstance(instance, aS3_ForEachStatement)

@given(instance=aS3_ThrowStatement_strategy)
@settings(max_examples=50)
def test_as3_throwstatement_instantiation(instance):
    assert isinstance(instance, aS3_ThrowStatement)

@given(instance=aS3_DoWhileStatement_strategy)
@settings(max_examples=50)
def test_as3_dowhilestatement_instantiation(instance):
    assert isinstance(instance, aS3_DoWhileStatement)

@given(instance=aS3_SwitchStatement_strategy)
@settings(max_examples=50)
def test_as3_switchstatement_instantiation(instance):
    assert isinstance(instance, aS3_SwitchStatement)

@given(instance=aS3_TryStatement_strategy)
@settings(max_examples=50)
def test_as3_trystatement_instantiation(instance):
    assert isinstance(instance, aS3_TryStatement)

@given(instance=aS3_WhileStatement_strategy)
@settings(max_examples=50)
def test_as3_whilestatement_instantiation(instance):
    assert isinstance(instance, aS3_WhileStatement)

@given(instance=aS3_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_as3_variabledeclaration_instantiation(instance):
    assert isinstance(instance, aS3_VariableDeclaration)



@given(instance=aS3_VariableDeclaration_strategy)
def test_as3_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aS3_VariableDeclaration_strategy)
def test_as3_variabledeclaration_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3_Class_strategy)
@settings(max_examples=50)
def test_as3_class_instantiation(instance):
    assert isinstance(instance, aS3_Class)



@given(instance=aS3_Class_strategy)
def test_as3_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3_Block_strategy)
@settings(max_examples=50)
def test_as3_block_instantiation(instance):
    assert isinstance(instance, aS3_Block)

@given(instance=aS3_functionSignature_strategy)
@settings(max_examples=50)
def test_as3_functionsignature_instantiation(instance):
    assert isinstance(instance, aS3_functionSignature)

@given(instance=aS3_functionCommon_strategy)
@settings(max_examples=50)
def test_as3_functioncommon_instantiation(instance):
    assert isinstance(instance, aS3_functionCommon)

@given(instance=aS3_functionExpression_strategy)
@settings(max_examples=50)
def test_as3_functionexpression_instantiation(instance):
    assert isinstance(instance, aS3_functionExpression)



@given(instance=aS3_functionExpression_strategy)
def test_as3_functionexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aS3_Parameter_strategy)
@settings(max_examples=50)
def test_as3_parameter_instantiation(instance):
    assert isinstance(instance, aS3_Parameter)



@given(instance=aS3_Parameter_strategy)
def test_as3_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aS3_Parameter_strategy)
def test_as3_parameter_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3_AccessorRole_strategy)
@settings(max_examples=50)
def test_as3_accessorrole_instantiation(instance):
    assert isinstance(instance, aS3_AccessorRole)



@given(instance=aS3_AccessorRole_strategy)
def test_as3_accessorrole_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=aS3_Modifier_strategy)
@settings(max_examples=50)
def test_as3_modifier_instantiation(instance):
    assert isinstance(instance, aS3_Modifier)



@given(instance=aS3_Modifier_strategy)
def test_as3_modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=aS3_Modifier_strategy)
def test_as3_modifier_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original



@given(instance=aS3_Modifier_strategy)
def test_as3_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=aS3_Modifier_strategy)
def test_as3_modifier_dynamic_setter(instance):
    original = instance.dynamic
    instance.dynamic = original
    assert instance.dynamic == original



@given(instance=aS3_Modifier_strategy)
def test_as3_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=aS3_InterfaceMethod_strategy)
@settings(max_examples=50)
def test_as3_interfacemethod_instantiation(instance):
    assert isinstance(instance, aS3_InterfaceMethod)



@given(instance=aS3_InterfaceMethod_strategy)
def test_as3_interfacemethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aS3_InterfaceMethod_strategy)
def test_as3_interfacemethod_anytype_setter(instance):
    original = instance.anytype
    instance.anytype = original
    assert instance.anytype == original

@given(instance=aS3_Interface_strategy)
@settings(max_examples=50)
def test_as3_interface_instantiation(instance):
    assert isinstance(instance, aS3_Interface)



@given(instance=aS3_Interface_strategy)
def test_as3_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aS3_Interface_strategy)
def test_as3_interface_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=aS3_Expression_strategy)
@settings(max_examples=50)
def test_as3_expression_instantiation(instance):
    assert isinstance(instance, aS3_Expression)
