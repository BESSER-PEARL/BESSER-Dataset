import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HaxeComment,
    haxe::HaxeHaxedocComment,
    HaxeASTNode,
    haxe::HaxeTextElement,
    haxe::HaxeTagElement,
    haxe::HaxeNamedElement,
    haxe::HaxeComment,
    HaxeModelElement,
    haxe::HaxeASTNode,
    haxe::HaxeModelElement,
    haxe::HaxeModel,
    haxe::HaxeMetadataContainer,
    HaxeDependencyDeclaration,
    haxe::HaxeUsingDeclaration,
    haxe::HaxeImportDeclaration,
    HaxeAbstractOperation,
    haxe::HaxeAbstractFunction,
    HaxeSingleVariableDeclaration,
    HaxeField,
    HaxeClassifier,
    haxe::HaxeEnum,
    haxe::HaxeClass,
    haxe::HaxeAbstract,
    haxe::HaxeTypedElement,
    HaxeTypeAccess,
    haxe::HaxeFunctionTypeAccess,
    haxe::HaxeConstructor,
    haxe::HaxeAttribute,
    HaxeMetadataContainer,
    HaxeFieldContainer,
    HaxeType,
    haxe::HaxeTypedef,
    haxe::HaxeClassifier,
    haxe::HaxeTypeParameter,
    HaxePathReferentiable,
    haxe::HaxeType,
    HaxeVariableDeclaration,
    haxe::HaxeEnumConstructor,
    haxe::HaxeVariableDeclarationFragment,
    haxe::HaxeAbstractMethodInvocation,
    HaxePathReference,
    haxe::HaxeDependencyDeclaration,
    haxe::HaxeClassifierAccess,
    HaxeMethodInvocation,
    haxe::HaxeSuperConstructorInvocation,
    HaxeAbstractMethodInvocation,
    HaxeTypedElement,
    haxe::HaxeOperation,
    haxe::HaxeVariableDeclarationGroup,
    HaxeAbstractFunction,
    haxe::HaxeAbstractOperation,
    HaxeConstant,
    haxe::HaxeBooleanLiteral,
    haxe::HaxeNumberLiteral,
    haxe::HaxeNullLiteral,
    haxe::HaxeRegexLiteral,
    haxe::HaxeIdentifierLiteral,
    haxe::HaxeStringLiteral,
    HaxeExpressionStatement,
    haxe::HaxeThrowExpression,
    haxe::HaxeReturn,
    HaxeBinaryExpression,
    haxe::HaxeAssignment,
    haxe::HaxeInfixExpression,
    HaxeUnaryExpression,
    haxe::HaxePostfixExpression,
    haxe::HaxePrefixExpression,
    haxe::HaxeSingleVariableDeclaration,
    HaxeLoopStatement,
    haxe::HaxeDoWhileStatement,
    haxe::HaxeWhileStatement,
    haxe::HaxeForStatement,
    HaxeConditionalExpression,
    haxe::HaxeTernaryExpression,
    haxe::HaxeIfStatement,
    HaxeExpression,
    haxe::HaxeObjectDeclaration,
    haxe::HaxeSuperMethodInvocation,
    haxe::HaxeConditionalExpression,
    haxe::HaxeSingleVariableAccess,
    haxe::HaxeSwitch,
    haxe::HaxeBinaryExpression,
    haxe::HaxeArrayInitializer,
    haxe::HaxeConstant,
    haxe::HaxeExpressionStatement,
    haxe::HaxeVariableDeclarationExpression,
    haxe::HaxeFieldAccess,
    haxe::HaxeCase,
    haxe::HaxeBreak,
    haxe::HaxeContinue,
    haxe::HaxeUnsafeCastExpression,
    haxe::HaxeInExpression,
    haxe::HaxeArrayCreation,
    haxe::HaxeBlock,
    haxe::HaxeTypeAccess,
    haxe::HaxeCatchClause,
    haxe::HaxeParenthizedExpression,
    haxe::HaxeMethodInvocation,
    haxe::HaxeFunctionExpression,
    haxe::HaxePackageAccess,
    haxe::HaxeThisExpression,
    haxe::HaxeTypeCheckExpression,
    haxe::HaxeTryExpression,
    haxe::HaxeCallExpression,
    haxe::HaxeUnaryExpression,
    haxe::HaxeEmptyStatement,
    haxe::HaxeCastingExpression,
    haxe::HaxeArrayAccess,
    haxe::HaxeLoopStatement,
    haxe::HaxeExpression,
    haxe::HaxeFieldContainer,
    haxe::HaxePathReference,
    haxe::HaxePackage,
    HaxeNamedElement,
    haxe::HaxeMetadata,
    haxe::HaxePathReferentiable,
    haxe::HaxeField,
    haxe::HaxeFieldDeclaration,
    haxe::HaxeVariableDeclaration,
    haxe::HaxeModule,
    HaxeAssignmentOperator,
    HaxeTarget,
    HaxeInfixOperators,
    HaxeAttributeProperty,
    HaxePrefixOperators,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_haxecomment_is_not_abstract():
    assert not inspect.isabstract(HaxeComment)


def test_haxecomment_constructor_exists():
    assert callable(HaxeComment.__init__)


def test_haxecomment_constructor_args():
    sig = inspect.signature(HaxeComment.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxehaxedoccomment_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeHaxedocComment)


def test_haxe::haxehaxedoccomment_constructor_exists():
    assert callable(haxe::HaxeHaxedocComment.__init__)


def test_haxe::haxehaxedoccomment_constructor_args():
    sig = inspect.signature(haxe::HaxeHaxedocComment.__init__)
    params = list(sig.parameters.keys())



def test_haxeastnode_is_not_abstract():
    assert not inspect.isabstract(HaxeASTNode)


def test_haxeastnode_constructor_exists():
    assert callable(HaxeASTNode.__init__)


def test_haxeastnode_constructor_args():
    sig = inspect.signature(HaxeASTNode.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxetextelement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTextElement)


def test_haxe::haxetextelement_constructor_exists():
    assert callable(haxe::HaxeTextElement.__init__)


def test_haxe::haxetextelement_constructor_args():
    sig = inspect.signature(haxe::HaxeTextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_haxe::haxetextelement_has_text():
    assert hasattr(haxe::HaxeTextElement, "text")
    descriptor = None
    for klass in haxe::HaxeTextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxetagelement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTagElement)


def test_haxe::haxetagelement_constructor_exists():
    assert callable(haxe::HaxeTagElement.__init__)


def test_haxe::haxetagelement_constructor_args():
    sig = inspect.signature(haxe::HaxeTagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_haxe::haxetagelement_has_tagName():
    assert hasattr(haxe::HaxeTagElement, "tagName")
    descriptor = None
    for klass in haxe::HaxeTagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxenamedelement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeNamedElement)


def test_haxe::haxenamedelement_constructor_exists():
    assert callable(haxe::HaxeNamedElement.__init__)


def test_haxe::haxenamedelement_constructor_args():
    sig = inspect.signature(haxe::HaxeNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_haxe::haxenamedelement_has_name():
    assert hasattr(haxe::HaxeNamedElement, "name")
    descriptor = None
    for klass in haxe::HaxeNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxecomment_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeComment)


def test_haxe::haxecomment_constructor_exists():
    assert callable(haxe::HaxeComment.__init__)


def test_haxe::haxecomment_constructor_args():
    sig = inspect.signature(haxe::HaxeComment.__init__)
    params = list(sig.parameters.keys())
    assert "prefixOfParent" in params, "Missing parameter 'prefixOfParent'"
    assert "enclosedByParent" in params, "Missing parameter 'enclosedByParent'"
    assert "lineComment" in params, "Missing parameter 'lineComment'"
    assert "content" in params, "Missing parameter 'content'"

def test_haxe::haxecomment_has_prefixOfParent():
    assert hasattr(haxe::HaxeComment, "prefixOfParent")
    descriptor = None
    for klass in haxe::HaxeComment.__mro__:
        if "prefixOfParent" in klass.__dict__:
            descriptor = klass.__dict__["prefixOfParent"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxecomment_has_enclosedByParent():
    assert hasattr(haxe::HaxeComment, "enclosedByParent")
    descriptor = None
    for klass in haxe::HaxeComment.__mro__:
        if "enclosedByParent" in klass.__dict__:
            descriptor = klass.__dict__["enclosedByParent"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxecomment_has_lineComment():
    assert hasattr(haxe::HaxeComment, "lineComment")
    descriptor = None
    for klass in haxe::HaxeComment.__mro__:
        if "lineComment" in klass.__dict__:
            descriptor = klass.__dict__["lineComment"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxecomment_has_content():
    assert hasattr(haxe::HaxeComment, "content")
    descriptor = None
    for klass in haxe::HaxeComment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_haxemodelelement_is_not_abstract():
    assert not inspect.isabstract(HaxeModelElement)


def test_haxemodelelement_constructor_exists():
    assert callable(HaxeModelElement.__init__)


def test_haxemodelelement_constructor_args():
    sig = inspect.signature(HaxeModelElement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeastnode_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeASTNode)


def test_haxe::haxeastnode_constructor_exists():
    assert callable(haxe::HaxeASTNode.__init__)


def test_haxe::haxeastnode_constructor_args():
    sig = inspect.signature(haxe::HaxeASTNode.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxemodelelement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeModelElement)


def test_haxe::haxemodelelement_constructor_exists():
    assert callable(haxe::HaxeModelElement.__init__)


def test_haxe::haxemodelelement_constructor_args():
    sig = inspect.signature(haxe::HaxeModelElement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxemodel_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeModel)


def test_haxe::haxemodel_constructor_exists():
    assert callable(haxe::HaxeModel.__init__)


def test_haxe::haxemodel_constructor_args():
    sig = inspect.signature(haxe::HaxeModel.__init__)
    params = list(sig.parameters.keys())
    assert "sourceFolder" in params, "Missing parameter 'sourceFolder'"
    assert "targetFolder" in params, "Missing parameter 'targetFolder'"
    assert "target" in params, "Missing parameter 'target'"
    assert "name" in params, "Missing parameter 'name'"

def test_haxe::haxemodel_has_sourceFolder():
    assert hasattr(haxe::HaxeModel, "sourceFolder")
    descriptor = None
    for klass in haxe::HaxeModel.__mro__:
        if "sourceFolder" in klass.__dict__:
            descriptor = klass.__dict__["sourceFolder"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxemodel_has_targetFolder():
    assert hasattr(haxe::HaxeModel, "targetFolder")
    descriptor = None
    for klass in haxe::HaxeModel.__mro__:
        if "targetFolder" in klass.__dict__:
            descriptor = klass.__dict__["targetFolder"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxemodel_has_target():
    assert hasattr(haxe::HaxeModel, "target")
    descriptor = None
    for klass in haxe::HaxeModel.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxemodel_has_name():
    assert hasattr(haxe::HaxeModel, "name")
    descriptor = None
    for klass in haxe::HaxeModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxemetadatacontainer_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeMetadataContainer)


def test_haxe::haxemetadatacontainer_constructor_exists():
    assert callable(haxe::HaxeMetadataContainer.__init__)


def test_haxe::haxemetadatacontainer_constructor_args():
    sig = inspect.signature(haxe::HaxeMetadataContainer.__init__)
    params = list(sig.parameters.keys())



def test_haxedependencydeclaration_is_not_abstract():
    assert not inspect.isabstract(HaxeDependencyDeclaration)


def test_haxedependencydeclaration_constructor_exists():
    assert callable(HaxeDependencyDeclaration.__init__)


def test_haxedependencydeclaration_constructor_args():
    sig = inspect.signature(HaxeDependencyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeusingdeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeUsingDeclaration)


def test_haxe::haxeusingdeclaration_constructor_exists():
    assert callable(haxe::HaxeUsingDeclaration.__init__)


def test_haxe::haxeusingdeclaration_constructor_args():
    sig = inspect.signature(haxe::HaxeUsingDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeImportDeclaration)


def test_haxe::haxeimportdeclaration_constructor_exists():
    assert callable(haxe::HaxeImportDeclaration.__init__)


def test_haxe::haxeimportdeclaration_constructor_args():
    sig = inspect.signature(haxe::HaxeImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxeabstractoperation_is_not_abstract():
    assert not inspect.isabstract(HaxeAbstractOperation)


def test_haxeabstractoperation_constructor_exists():
    assert callable(HaxeAbstractOperation.__init__)


def test_haxeabstractoperation_constructor_args():
    sig = inspect.signature(HaxeAbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeabstractfunction_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeAbstractFunction)


def test_haxe::haxeabstractfunction_constructor_exists():
    assert callable(haxe::HaxeAbstractFunction.__init__)


def test_haxe::haxeabstractfunction_constructor_args():
    sig = inspect.signature(haxe::HaxeAbstractFunction.__init__)
    params = list(sig.parameters.keys())



def test_haxesinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(HaxeSingleVariableDeclaration)


def test_haxesinglevariabledeclaration_constructor_exists():
    assert callable(HaxeSingleVariableDeclaration.__init__)


def test_haxesinglevariabledeclaration_constructor_args():
    sig = inspect.signature(HaxeSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxefield_is_not_abstract():
    assert not inspect.isabstract(HaxeField)


def test_haxefield_constructor_exists():
    assert callable(HaxeField.__init__)


def test_haxefield_constructor_args():
    sig = inspect.signature(HaxeField.__init__)
    params = list(sig.parameters.keys())



def test_haxeclassifier_is_not_abstract():
    assert not inspect.isabstract(HaxeClassifier)


def test_haxeclassifier_constructor_exists():
    assert callable(HaxeClassifier.__init__)


def test_haxeclassifier_constructor_args():
    sig = inspect.signature(HaxeClassifier.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeenum_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeEnum)


def test_haxe::haxeenum_constructor_exists():
    assert callable(haxe::HaxeEnum.__init__)


def test_haxe::haxeenum_constructor_args():
    sig = inspect.signature(haxe::HaxeEnum.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeclass_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeClass)


def test_haxe::haxeclass_constructor_exists():
    assert callable(haxe::HaxeClass.__init__)


def test_haxe::haxeclass_constructor_args():
    sig = inspect.signature(haxe::HaxeClass.__init__)
    params = list(sig.parameters.keys())
    assert "isInterface" in params, "Missing parameter 'isInterface'"

def test_haxe::haxeclass_has_isInterface():
    assert hasattr(haxe::HaxeClass, "isInterface")
    descriptor = None
    for klass in haxe::HaxeClass.__mro__:
        if "isInterface" in klass.__dict__:
            descriptor = klass.__dict__["isInterface"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxeabstract_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeAbstract)


def test_haxe::haxeabstract_constructor_exists():
    assert callable(haxe::HaxeAbstract.__init__)


def test_haxe::haxeabstract_constructor_args():
    sig = inspect.signature(haxe::HaxeAbstract.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxetypedelement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTypedElement)


def test_haxe::haxetypedelement_constructor_exists():
    assert callable(haxe::HaxeTypedElement.__init__)


def test_haxe::haxetypedelement_constructor_args():
    sig = inspect.signature(haxe::HaxeTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_haxetypeaccess_is_not_abstract():
    assert not inspect.isabstract(HaxeTypeAccess)


def test_haxetypeaccess_constructor_exists():
    assert callable(HaxeTypeAccess.__init__)


def test_haxetypeaccess_constructor_args():
    sig = inspect.signature(HaxeTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxefunctiontypeaccess_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeFunctionTypeAccess)


def test_haxe::haxefunctiontypeaccess_constructor_exists():
    assert callable(haxe::HaxeFunctionTypeAccess.__init__)


def test_haxe::haxefunctiontypeaccess_constructor_args():
    sig = inspect.signature(haxe::HaxeFunctionTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeconstructor_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeConstructor)


def test_haxe::haxeconstructor_constructor_exists():
    assert callable(haxe::HaxeConstructor.__init__)


def test_haxe::haxeconstructor_constructor_args():
    sig = inspect.signature(haxe::HaxeConstructor.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeattribute_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeAttribute)


def test_haxe::haxeattribute_constructor_exists():
    assert callable(haxe::HaxeAttribute.__init__)


def test_haxe::haxeattribute_constructor_args():
    sig = inspect.signature(haxe::HaxeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "getterProperty" in params, "Missing parameter 'getterProperty'"
    assert "setterProperty" in params, "Missing parameter 'setterProperty'"

def test_haxe::haxeattribute_has_getterProperty():
    assert hasattr(haxe::HaxeAttribute, "getterProperty")
    descriptor = None
    for klass in haxe::HaxeAttribute.__mro__:
        if "getterProperty" in klass.__dict__:
            descriptor = klass.__dict__["getterProperty"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxeattribute_has_setterProperty():
    assert hasattr(haxe::HaxeAttribute, "setterProperty")
    descriptor = None
    for klass in haxe::HaxeAttribute.__mro__:
        if "setterProperty" in klass.__dict__:
            descriptor = klass.__dict__["setterProperty"]
            break
    assert isinstance(descriptor, property)



def test_haxemetadatacontainer_is_not_abstract():
    assert not inspect.isabstract(HaxeMetadataContainer)


def test_haxemetadatacontainer_constructor_exists():
    assert callable(HaxeMetadataContainer.__init__)


def test_haxemetadatacontainer_constructor_args():
    sig = inspect.signature(HaxeMetadataContainer.__init__)
    params = list(sig.parameters.keys())



def test_haxefieldcontainer_is_not_abstract():
    assert not inspect.isabstract(HaxeFieldContainer)


def test_haxefieldcontainer_constructor_exists():
    assert callable(HaxeFieldContainer.__init__)


def test_haxefieldcontainer_constructor_args():
    sig = inspect.signature(HaxeFieldContainer.__init__)
    params = list(sig.parameters.keys())



def test_haxetype_is_not_abstract():
    assert not inspect.isabstract(HaxeType)


def test_haxetype_constructor_exists():
    assert callable(HaxeType.__init__)


def test_haxetype_constructor_args():
    sig = inspect.signature(HaxeType.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxetypedef_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTypedef)


def test_haxe::haxetypedef_constructor_exists():
    assert callable(haxe::HaxeTypedef.__init__)


def test_haxe::haxetypedef_constructor_args():
    sig = inspect.signature(haxe::HaxeTypedef.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeclassifier_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeClassifier)


def test_haxe::haxeclassifier_constructor_exists():
    assert callable(haxe::HaxeClassifier.__init__)


def test_haxe::haxeclassifier_constructor_args():
    sig = inspect.signature(haxe::HaxeClassifier.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxetypeparameter_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTypeParameter)


def test_haxe::haxetypeparameter_constructor_exists():
    assert callable(haxe::HaxeTypeParameter.__init__)


def test_haxe::haxetypeparameter_constructor_args():
    sig = inspect.signature(haxe::HaxeTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_haxepathreferentiable_is_not_abstract():
    assert not inspect.isabstract(HaxePathReferentiable)


def test_haxepathreferentiable_constructor_exists():
    assert callable(HaxePathReferentiable.__init__)


def test_haxepathreferentiable_constructor_args():
    sig = inspect.signature(HaxePathReferentiable.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxetype_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeType)


def test_haxe::haxetype_constructor_exists():
    assert callable(haxe::HaxeType.__init__)


def test_haxe::haxetype_constructor_args():
    sig = inspect.signature(haxe::HaxeType.__init__)
    params = list(sig.parameters.keys())
    assert "private" in params, "Missing parameter 'private'"
    assert "extern" in params, "Missing parameter 'extern'"

def test_haxe::haxetype_has_private():
    assert hasattr(haxe::HaxeType, "private")
    descriptor = None
    for klass in haxe::HaxeType.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxetype_has_extern():
    assert hasattr(haxe::HaxeType, "extern")
    descriptor = None
    for klass in haxe::HaxeType.__mro__:
        if "extern" in klass.__dict__:
            descriptor = klass.__dict__["extern"]
            break
    assert isinstance(descriptor, property)



def test_haxevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(HaxeVariableDeclaration)


def test_haxevariabledeclaration_constructor_exists():
    assert callable(HaxeVariableDeclaration.__init__)


def test_haxevariabledeclaration_constructor_args():
    sig = inspect.signature(HaxeVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeenumconstructor_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeEnumConstructor)


def test_haxe::haxeenumconstructor_constructor_exists():
    assert callable(haxe::HaxeEnumConstructor.__init__)


def test_haxe::haxeenumconstructor_constructor_args():
    sig = inspect.signature(haxe::HaxeEnumConstructor.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxevariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeVariableDeclarationFragment)


def test_haxe::haxevariabledeclarationfragment_constructor_exists():
    assert callable(haxe::HaxeVariableDeclarationFragment.__init__)


def test_haxe::haxevariabledeclarationfragment_constructor_args():
    sig = inspect.signature(haxe::HaxeVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeabstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeAbstractMethodInvocation)


def test_haxe::haxeabstractmethodinvocation_constructor_exists():
    assert callable(haxe::HaxeAbstractMethodInvocation.__init__)


def test_haxe::haxeabstractmethodinvocation_constructor_args():
    sig = inspect.signature(haxe::HaxeAbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxepathreference_is_not_abstract():
    assert not inspect.isabstract(HaxePathReference)


def test_haxepathreference_constructor_exists():
    assert callable(HaxePathReference.__init__)


def test_haxepathreference_constructor_args():
    sig = inspect.signature(HaxePathReference.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxedependencydeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeDependencyDeclaration)


def test_haxe::haxedependencydeclaration_constructor_exists():
    assert callable(haxe::HaxeDependencyDeclaration.__init__)


def test_haxe::haxedependencydeclaration_constructor_args():
    sig = inspect.signature(haxe::HaxeDependencyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeclassifieraccess_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeClassifierAccess)


def test_haxe::haxeclassifieraccess_constructor_exists():
    assert callable(haxe::HaxeClassifierAccess.__init__)


def test_haxe::haxeclassifieraccess_constructor_args():
    sig = inspect.signature(haxe::HaxeClassifierAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(HaxeMethodInvocation)


def test_haxemethodinvocation_constructor_exists():
    assert callable(HaxeMethodInvocation.__init__)


def test_haxemethodinvocation_constructor_args():
    sig = inspect.signature(HaxeMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxesuperconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeSuperConstructorInvocation)


def test_haxe::haxesuperconstructorinvocation_constructor_exists():
    assert callable(haxe::HaxeSuperConstructorInvocation.__init__)


def test_haxe::haxesuperconstructorinvocation_constructor_args():
    sig = inspect.signature(haxe::HaxeSuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxeabstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(HaxeAbstractMethodInvocation)


def test_haxeabstractmethodinvocation_constructor_exists():
    assert callable(HaxeAbstractMethodInvocation.__init__)


def test_haxeabstractmethodinvocation_constructor_args():
    sig = inspect.signature(HaxeAbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxetypedelement_is_not_abstract():
    assert not inspect.isabstract(HaxeTypedElement)


def test_haxetypedelement_constructor_exists():
    assert callable(HaxeTypedElement.__init__)


def test_haxetypedelement_constructor_args():
    sig = inspect.signature(HaxeTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeoperation_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeOperation)


def test_haxe::haxeoperation_constructor_exists():
    assert callable(haxe::HaxeOperation.__init__)


def test_haxe::haxeoperation_constructor_args():
    sig = inspect.signature(haxe::HaxeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "macro" in params, "Missing parameter 'macro'"

def test_haxe::haxeoperation_has_macro():
    assert hasattr(haxe::HaxeOperation, "macro")
    descriptor = None
    for klass in haxe::HaxeOperation.__mro__:
        if "macro" in klass.__dict__:
            descriptor = klass.__dict__["macro"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxevariabledeclarationgroup_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeVariableDeclarationGroup)


def test_haxe::haxevariabledeclarationgroup_constructor_exists():
    assert callable(haxe::HaxeVariableDeclarationGroup.__init__)


def test_haxe::haxevariabledeclarationgroup_constructor_args():
    sig = inspect.signature(haxe::HaxeVariableDeclarationGroup.__init__)
    params = list(sig.parameters.keys())



def test_haxeabstractfunction_is_not_abstract():
    assert not inspect.isabstract(HaxeAbstractFunction)


def test_haxeabstractfunction_constructor_exists():
    assert callable(HaxeAbstractFunction.__init__)


def test_haxeabstractfunction_constructor_args():
    sig = inspect.signature(HaxeAbstractFunction.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeabstractoperation_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeAbstractOperation)


def test_haxe::haxeabstractoperation_constructor_exists():
    assert callable(haxe::HaxeAbstractOperation.__init__)


def test_haxe::haxeabstractoperation_constructor_args():
    sig = inspect.signature(haxe::HaxeAbstractOperation.__init__)
    params = list(sig.parameters.keys())
    assert "overrides" in params, "Missing parameter 'overrides'"
    assert "isInline" in params, "Missing parameter 'isInline'"

def test_haxe::haxeabstractoperation_has_overrides():
    assert hasattr(haxe::HaxeAbstractOperation, "overrides")
    descriptor = None
    for klass in haxe::HaxeAbstractOperation.__mro__:
        if "overrides" in klass.__dict__:
            descriptor = klass.__dict__["overrides"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxeabstractoperation_has_isInline():
    assert hasattr(haxe::HaxeAbstractOperation, "isInline")
    descriptor = None
    for klass in haxe::HaxeAbstractOperation.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)



def test_haxeconstant_is_not_abstract():
    assert not inspect.isabstract(HaxeConstant)


def test_haxeconstant_constructor_exists():
    assert callable(HaxeConstant.__init__)


def test_haxeconstant_constructor_args():
    sig = inspect.signature(HaxeConstant.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxebooleanliteral_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeBooleanLiteral)


def test_haxe::haxebooleanliteral_constructor_exists():
    assert callable(haxe::HaxeBooleanLiteral.__init__)


def test_haxe::haxebooleanliteral_constructor_args():
    sig = inspect.signature(haxe::HaxeBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_haxe::haxebooleanliteral_has_value():
    assert hasattr(haxe::HaxeBooleanLiteral, "value")
    descriptor = None
    for klass in haxe::HaxeBooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxenumberliteral_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeNumberLiteral)


def test_haxe::haxenumberliteral_constructor_exists():
    assert callable(haxe::HaxeNumberLiteral.__init__)


def test_haxe::haxenumberliteral_constructor_args():
    sig = inspect.signature(haxe::HaxeNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_haxe::haxenumberliteral_has_value():
    assert hasattr(haxe::HaxeNumberLiteral, "value")
    descriptor = None
    for klass in haxe::HaxeNumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxenullliteral_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeNullLiteral)


def test_haxe::haxenullliteral_constructor_exists():
    assert callable(haxe::HaxeNullLiteral.__init__)


def test_haxe::haxenullliteral_constructor_args():
    sig = inspect.signature(haxe::HaxeNullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeregexliteral_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeRegexLiteral)


def test_haxe::haxeregexliteral_constructor_exists():
    assert callable(haxe::HaxeRegexLiteral.__init__)


def test_haxe::haxeregexliteral_constructor_args():
    sig = inspect.signature(haxe::HaxeRegexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "options" in params, "Missing parameter 'options'"

def test_haxe::haxeregexliteral_has_pattern():
    assert hasattr(haxe::HaxeRegexLiteral, "pattern")
    descriptor = None
    for klass in haxe::HaxeRegexLiteral.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxeregexliteral_has_options():
    assert hasattr(haxe::HaxeRegexLiteral, "options")
    descriptor = None
    for klass in haxe::HaxeRegexLiteral.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxeidentifierliteral_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeIdentifierLiteral)


def test_haxe::haxeidentifierliteral_constructor_exists():
    assert callable(haxe::HaxeIdentifierLiteral.__init__)


def test_haxe::haxeidentifierliteral_constructor_args():
    sig = inspect.signature(haxe::HaxeIdentifierLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_haxe::haxeidentifierliteral_has_value():
    assert hasattr(haxe::HaxeIdentifierLiteral, "value")
    descriptor = None
    for klass in haxe::HaxeIdentifierLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxestringliteral_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeStringLiteral)


def test_haxe::haxestringliteral_constructor_exists():
    assert callable(haxe::HaxeStringLiteral.__init__)


def test_haxe::haxestringliteral_constructor_args():
    sig = inspect.signature(haxe::HaxeStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_haxe::haxestringliteral_has_escapedValue():
    assert hasattr(haxe::HaxeStringLiteral, "escapedValue")
    descriptor = None
    for klass in haxe::HaxeStringLiteral.__mro__:
        if "escapedValue" in klass.__dict__:
            descriptor = klass.__dict__["escapedValue"]
            break
    assert isinstance(descriptor, property)



def test_haxeexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(HaxeExpressionStatement)


def test_haxeexpressionstatement_constructor_exists():
    assert callable(HaxeExpressionStatement.__init__)


def test_haxeexpressionstatement_constructor_args():
    sig = inspect.signature(HaxeExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxethrowexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeThrowExpression)


def test_haxe::haxethrowexpression_constructor_exists():
    assert callable(haxe::HaxeThrowExpression.__init__)


def test_haxe::haxethrowexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeThrowExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxereturn_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeReturn)


def test_haxe::haxereturn_constructor_exists():
    assert callable(haxe::HaxeReturn.__init__)


def test_haxe::haxereturn_constructor_args():
    sig = inspect.signature(haxe::HaxeReturn.__init__)
    params = list(sig.parameters.keys())



def test_haxebinaryexpression_is_not_abstract():
    assert not inspect.isabstract(HaxeBinaryExpression)


def test_haxebinaryexpression_constructor_exists():
    assert callable(HaxeBinaryExpression.__init__)


def test_haxebinaryexpression_constructor_args():
    sig = inspect.signature(HaxeBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeassignment_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeAssignment)


def test_haxe::haxeassignment_constructor_exists():
    assert callable(haxe::HaxeAssignment.__init__)


def test_haxe::haxeassignment_constructor_args():
    sig = inspect.signature(haxe::HaxeAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_haxe::haxeassignment_has_operator():
    assert hasattr(haxe::HaxeAssignment, "operator")
    descriptor = None
    for klass in haxe::HaxeAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxeinfixexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeInfixExpression)


def test_haxe::haxeinfixexpression_constructor_exists():
    assert callable(haxe::HaxeInfixExpression.__init__)


def test_haxe::haxeinfixexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeInfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_haxe::haxeinfixexpression_has_operator():
    assert hasattr(haxe::HaxeInfixExpression, "operator")
    descriptor = None
    for klass in haxe::HaxeInfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_haxeunaryexpression_is_not_abstract():
    assert not inspect.isabstract(HaxeUnaryExpression)


def test_haxeunaryexpression_constructor_exists():
    assert callable(HaxeUnaryExpression.__init__)


def test_haxeunaryexpression_constructor_args():
    sig = inspect.signature(HaxeUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxepostfixexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxePostfixExpression)


def test_haxe::haxepostfixexpression_constructor_exists():
    assert callable(haxe::HaxePostfixExpression.__init__)


def test_haxe::haxepostfixexpression_constructor_args():
    sig = inspect.signature(haxe::HaxePostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isIncrement" in params, "Missing parameter 'isIncrement'"

def test_haxe::haxepostfixexpression_has_isIncrement():
    assert hasattr(haxe::HaxePostfixExpression, "isIncrement")
    descriptor = None
    for klass in haxe::HaxePostfixExpression.__mro__:
        if "isIncrement" in klass.__dict__:
            descriptor = klass.__dict__["isIncrement"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxeprefixexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxePrefixExpression)


def test_haxe::haxeprefixexpression_constructor_exists():
    assert callable(haxe::HaxePrefixExpression.__init__)


def test_haxe::haxeprefixexpression_constructor_args():
    sig = inspect.signature(haxe::HaxePrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_haxe::haxeprefixexpression_has_operator():
    assert hasattr(haxe::HaxePrefixExpression, "operator")
    descriptor = None
    for klass in haxe::HaxePrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxesinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeSingleVariableDeclaration)


def test_haxe::haxesinglevariabledeclaration_constructor_exists():
    assert callable(haxe::HaxeSingleVariableDeclaration.__init__)


def test_haxe::haxesinglevariabledeclaration_constructor_args():
    sig = inspect.signature(haxe::HaxeSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_haxe::haxesinglevariabledeclaration_has_isOptional():
    assert hasattr(haxe::HaxeSingleVariableDeclaration, "isOptional")
    descriptor = None
    for klass in haxe::HaxeSingleVariableDeclaration.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_haxeloopstatement_is_not_abstract():
    assert not inspect.isabstract(HaxeLoopStatement)


def test_haxeloopstatement_constructor_exists():
    assert callable(HaxeLoopStatement.__init__)


def test_haxeloopstatement_constructor_args():
    sig = inspect.signature(HaxeLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxedowhilestatement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeDoWhileStatement)


def test_haxe::haxedowhilestatement_constructor_exists():
    assert callable(haxe::HaxeDoWhileStatement.__init__)


def test_haxe::haxedowhilestatement_constructor_args():
    sig = inspect.signature(haxe::HaxeDoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxewhilestatement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeWhileStatement)


def test_haxe::haxewhilestatement_constructor_exists():
    assert callable(haxe::HaxeWhileStatement.__init__)


def test_haxe::haxewhilestatement_constructor_args():
    sig = inspect.signature(haxe::HaxeWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeforstatement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeForStatement)


def test_haxe::haxeforstatement_constructor_exists():
    assert callable(haxe::HaxeForStatement.__init__)


def test_haxe::haxeforstatement_constructor_args():
    sig = inspect.signature(haxe::HaxeForStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxeconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(HaxeConditionalExpression)


def test_haxeconditionalexpression_constructor_exists():
    assert callable(HaxeConditionalExpression.__init__)


def test_haxeconditionalexpression_constructor_args():
    sig = inspect.signature(HaxeConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeternaryexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTernaryExpression)


def test_haxe::haxeternaryexpression_constructor_exists():
    assert callable(haxe::HaxeTernaryExpression.__init__)


def test_haxe::haxeternaryexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeTernaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeifstatement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeIfStatement)


def test_haxe::haxeifstatement_constructor_exists():
    assert callable(haxe::HaxeIfStatement.__init__)


def test_haxe::haxeifstatement_constructor_args():
    sig = inspect.signature(haxe::HaxeIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxeexpression_is_not_abstract():
    assert not inspect.isabstract(HaxeExpression)


def test_haxeexpression_constructor_exists():
    assert callable(HaxeExpression.__init__)


def test_haxeexpression_constructor_args():
    sig = inspect.signature(HaxeExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeobjectdeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeObjectDeclaration)


def test_haxe::haxeobjectdeclaration_constructor_exists():
    assert callable(haxe::HaxeObjectDeclaration.__init__)


def test_haxe::haxeobjectdeclaration_constructor_args():
    sig = inspect.signature(haxe::HaxeObjectDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxesupermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeSuperMethodInvocation)


def test_haxe::haxesupermethodinvocation_constructor_exists():
    assert callable(haxe::HaxeSuperMethodInvocation.__init__)


def test_haxe::haxesupermethodinvocation_constructor_args():
    sig = inspect.signature(haxe::HaxeSuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeConditionalExpression)


def test_haxe::haxeconditionalexpression_constructor_exists():
    assert callable(haxe::HaxeConditionalExpression.__init__)


def test_haxe::haxeconditionalexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxesinglevariableaccess_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeSingleVariableAccess)


def test_haxe::haxesinglevariableaccess_constructor_exists():
    assert callable(haxe::HaxeSingleVariableAccess.__init__)


def test_haxe::haxesinglevariableaccess_constructor_args():
    sig = inspect.signature(haxe::HaxeSingleVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeswitch_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeSwitch)


def test_haxe::haxeswitch_constructor_exists():
    assert callable(haxe::HaxeSwitch.__init__)


def test_haxe::haxeswitch_constructor_args():
    sig = inspect.signature(haxe::HaxeSwitch.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxebinaryexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeBinaryExpression)


def test_haxe::haxebinaryexpression_constructor_exists():
    assert callable(haxe::HaxeBinaryExpression.__init__)


def test_haxe::haxebinaryexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxearrayinitializer_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeArrayInitializer)


def test_haxe::haxearrayinitializer_constructor_exists():
    assert callable(haxe::HaxeArrayInitializer.__init__)


def test_haxe::haxearrayinitializer_constructor_args():
    sig = inspect.signature(haxe::HaxeArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeconstant_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeConstant)


def test_haxe::haxeconstant_constructor_exists():
    assert callable(haxe::HaxeConstant.__init__)


def test_haxe::haxeconstant_constructor_args():
    sig = inspect.signature(haxe::HaxeConstant.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeExpressionStatement)


def test_haxe::haxeexpressionstatement_constructor_exists():
    assert callable(haxe::HaxeExpressionStatement.__init__)


def test_haxe::haxeexpressionstatement_constructor_args():
    sig = inspect.signature(haxe::HaxeExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxevariabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeVariableDeclarationExpression)


def test_haxe::haxevariabledeclarationexpression_constructor_exists():
    assert callable(haxe::HaxeVariableDeclarationExpression.__init__)


def test_haxe::haxevariabledeclarationexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeVariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxefieldaccess_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeFieldAccess)


def test_haxe::haxefieldaccess_constructor_exists():
    assert callable(haxe::HaxeFieldAccess.__init__)


def test_haxe::haxefieldaccess_constructor_args():
    sig = inspect.signature(haxe::HaxeFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxecase_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeCase)


def test_haxe::haxecase_constructor_exists():
    assert callable(haxe::HaxeCase.__init__)


def test_haxe::haxecase_constructor_args():
    sig = inspect.signature(haxe::HaxeCase.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxebreak_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeBreak)


def test_haxe::haxebreak_constructor_exists():
    assert callable(haxe::HaxeBreak.__init__)


def test_haxe::haxebreak_constructor_args():
    sig = inspect.signature(haxe::HaxeBreak.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxecontinue_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeContinue)


def test_haxe::haxecontinue_constructor_exists():
    assert callable(haxe::HaxeContinue.__init__)


def test_haxe::haxecontinue_constructor_args():
    sig = inspect.signature(haxe::HaxeContinue.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeunsafecastexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeUnsafeCastExpression)


def test_haxe::haxeunsafecastexpression_constructor_exists():
    assert callable(haxe::HaxeUnsafeCastExpression.__init__)


def test_haxe::haxeunsafecastexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeUnsafeCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeinexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeInExpression)


def test_haxe::haxeinexpression_constructor_exists():
    assert callable(haxe::HaxeInExpression.__init__)


def test_haxe::haxeinexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeInExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxearraycreation_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeArrayCreation)


def test_haxe::haxearraycreation_constructor_exists():
    assert callable(haxe::HaxeArrayCreation.__init__)


def test_haxe::haxearraycreation_constructor_args():
    sig = inspect.signature(haxe::HaxeArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeblock_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeBlock)


def test_haxe::haxeblock_constructor_exists():
    assert callable(haxe::HaxeBlock.__init__)


def test_haxe::haxeblock_constructor_args():
    sig = inspect.signature(haxe::HaxeBlock.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxetypeaccess_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTypeAccess)


def test_haxe::haxetypeaccess_constructor_exists():
    assert callable(haxe::HaxeTypeAccess.__init__)


def test_haxe::haxetypeaccess_constructor_args():
    sig = inspect.signature(haxe::HaxeTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxecatchclause_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeCatchClause)


def test_haxe::haxecatchclause_constructor_exists():
    assert callable(haxe::HaxeCatchClause.__init__)


def test_haxe::haxecatchclause_constructor_args():
    sig = inspect.signature(haxe::HaxeCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeparenthizedexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeParenthizedExpression)


def test_haxe::haxeparenthizedexpression_constructor_exists():
    assert callable(haxe::HaxeParenthizedExpression.__init__)


def test_haxe::haxeparenthizedexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeParenthizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeMethodInvocation)


def test_haxe::haxemethodinvocation_constructor_exists():
    assert callable(haxe::HaxeMethodInvocation.__init__)


def test_haxe::haxemethodinvocation_constructor_args():
    sig = inspect.signature(haxe::HaxeMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxefunctionexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeFunctionExpression)


def test_haxe::haxefunctionexpression_constructor_exists():
    assert callable(haxe::HaxeFunctionExpression.__init__)


def test_haxe::haxefunctionexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeFunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxepackageaccess_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxePackageAccess)


def test_haxe::haxepackageaccess_constructor_exists():
    assert callable(haxe::HaxePackageAccess.__init__)


def test_haxe::haxepackageaccess_constructor_args():
    sig = inspect.signature(haxe::HaxePackageAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxethisexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeThisExpression)


def test_haxe::haxethisexpression_constructor_exists():
    assert callable(haxe::HaxeThisExpression.__init__)


def test_haxe::haxethisexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxetypecheckexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTypeCheckExpression)


def test_haxe::haxetypecheckexpression_constructor_exists():
    assert callable(haxe::HaxeTypeCheckExpression.__init__)


def test_haxe::haxetypecheckexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeTypeCheckExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxetryexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeTryExpression)


def test_haxe::haxetryexpression_constructor_exists():
    assert callable(haxe::HaxeTryExpression.__init__)


def test_haxe::haxetryexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeTryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxecallexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeCallExpression)


def test_haxe::haxecallexpression_constructor_exists():
    assert callable(haxe::HaxeCallExpression.__init__)


def test_haxe::haxecallexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeunaryexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeUnaryExpression)


def test_haxe::haxeunaryexpression_constructor_exists():
    assert callable(haxe::HaxeUnaryExpression.__init__)


def test_haxe::haxeunaryexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeemptystatement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeEmptyStatement)


def test_haxe::haxeemptystatement_constructor_exists():
    assert callable(haxe::HaxeEmptyStatement.__init__)


def test_haxe::haxeemptystatement_constructor_args():
    sig = inspect.signature(haxe::HaxeEmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxecastingexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeCastingExpression)


def test_haxe::haxecastingexpression_constructor_exists():
    assert callable(haxe::HaxeCastingExpression.__init__)


def test_haxe::haxecastingexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeCastingExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxearrayaccess_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeArrayAccess)


def test_haxe::haxearrayaccess_constructor_exists():
    assert callable(haxe::HaxeArrayAccess.__init__)


def test_haxe::haxearrayaccess_constructor_args():
    sig = inspect.signature(haxe::HaxeArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeloopstatement_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeLoopStatement)


def test_haxe::haxeloopstatement_constructor_exists():
    assert callable(haxe::HaxeLoopStatement.__init__)


def test_haxe::haxeloopstatement_constructor_args():
    sig = inspect.signature(haxe::HaxeLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxeexpression_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeExpression)


def test_haxe::haxeexpression_constructor_exists():
    assert callable(haxe::HaxeExpression.__init__)


def test_haxe::haxeexpression_constructor_args():
    sig = inspect.signature(haxe::HaxeExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxefieldcontainer_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeFieldContainer)


def test_haxe::haxefieldcontainer_constructor_exists():
    assert callable(haxe::HaxeFieldContainer.__init__)


def test_haxe::haxefieldcontainer_constructor_args():
    sig = inspect.signature(haxe::HaxeFieldContainer.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxepathreference_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxePathReference)


def test_haxe::haxepathreference_constructor_exists():
    assert callable(haxe::HaxePathReference.__init__)


def test_haxe::haxepathreference_constructor_args():
    sig = inspect.signature(haxe::HaxePathReference.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxepackage_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxePackage)


def test_haxe::haxepackage_constructor_exists():
    assert callable(haxe::HaxePackage.__init__)


def test_haxe::haxepackage_constructor_args():
    sig = inspect.signature(haxe::HaxePackage.__init__)
    params = list(sig.parameters.keys())



def test_haxenamedelement_is_not_abstract():
    assert not inspect.isabstract(HaxeNamedElement)


def test_haxenamedelement_constructor_exists():
    assert callable(HaxeNamedElement.__init__)


def test_haxenamedelement_constructor_args():
    sig = inspect.signature(HaxeNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxemetadata_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeMetadata)


def test_haxe::haxemetadata_constructor_exists():
    assert callable(haxe::HaxeMetadata.__init__)


def test_haxe::haxemetadata_constructor_args():
    sig = inspect.signature(haxe::HaxeMetadata.__init__)
    params = list(sig.parameters.keys())
    assert "compilerMetadata" in params, "Missing parameter 'compilerMetadata'"

def test_haxe::haxemetadata_has_compilerMetadata():
    assert hasattr(haxe::HaxeMetadata, "compilerMetadata")
    descriptor = None
    for klass in haxe::HaxeMetadata.__mro__:
        if "compilerMetadata" in klass.__dict__:
            descriptor = klass.__dict__["compilerMetadata"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxepathreferentiable_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxePathReferentiable)


def test_haxe::haxepathreferentiable_constructor_exists():
    assert callable(haxe::HaxePathReferentiable.__init__)


def test_haxe::haxepathreferentiable_constructor_args():
    sig = inspect.signature(haxe::HaxePathReferentiable.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxefield_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeField)


def test_haxe::haxefield_constructor_exists():
    assert callable(haxe::HaxeField.__init__)


def test_haxe::haxefield_constructor_args():
    sig = inspect.signature(haxe::HaxeField.__init__)
    params = list(sig.parameters.keys())
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_haxe::haxefield_has_isPrivate():
    assert hasattr(haxe::HaxeField, "isPrivate")
    descriptor = None
    for klass in haxe::HaxeField.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)

def test_haxe::haxefield_has_isStatic():
    assert hasattr(haxe::HaxeField, "isStatic")
    descriptor = None
    for klass in haxe::HaxeField.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_haxe::haxefielddeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeFieldDeclaration)


def test_haxe::haxefielddeclaration_constructor_exists():
    assert callable(haxe::HaxeFieldDeclaration.__init__)


def test_haxe::haxefielddeclaration_constructor_args():
    sig = inspect.signature(haxe::HaxeFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeVariableDeclaration)


def test_haxe::haxevariabledeclaration_constructor_exists():
    assert callable(haxe::HaxeVariableDeclaration.__init__)


def test_haxe::haxevariabledeclaration_constructor_args():
    sig = inspect.signature(haxe::HaxeVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe::haxemodule_is_not_abstract():
    assert not inspect.isabstract(haxe::HaxeModule)


def test_haxe::haxemodule_constructor_exists():
    assert callable(haxe::HaxeModule.__init__)


def test_haxe::haxemodule_constructor_args():
    sig = inspect.signature(haxe::HaxeModule.__init__)
    params = list(sig.parameters.keys())

def test_haxeassignmentoperator_exists():
    # Check that the Enumeration exists
    assert HaxeAssignmentOperator is not None

def test_haxeassignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxeAssignmentOperator]
    expected_literals = [
        "DIVISION_ASSIGN",
        "SHIFT_RIGTH_ASSIGN",
        "MINUS_ASSIGN",
        "BITWISE_OR_ASSIGN",
        "SHIFT_ARITH_ASSIGN",
        "BITWISE_AND_ASSIGN",
        "ASSIGN",
        "REMAINDER_ASSIGN",
        "PLUS_ASSIGN",
        "XOR_ASSIGN",
        "TIMES_ASSIGN",
        "SHIFT_LEFT_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxeAssignmentOperator"

def test_haxetarget_exists():
    # Check that the Enumeration exists
    assert HaxeTarget is not None

def test_haxetarget_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxeTarget]
    expected_literals = [
        "cpp",
        "flash",
        "java",
        "js",
        "cs",
        "neko",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxeTarget"

def test_haxeinfixoperators_exists():
    # Check that the Enumeration exists
    assert HaxeInfixOperators is not None

def test_haxeinfixoperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxeInfixOperators]
    expected_literals = [
        "NEQ",
        "RANGE",
        "BITWISE_OR",
        "LESS_THAN",
        "SHIFT_LEFT",
        "SHIFT_ARITH",
        "PLUS",
        "EQ",
        "OR",
        "TIMES",
        "GREATER_THAN",
        "SHIFT_RIGTH",
        "AND",
        "XOR",
        "REMAINDER",
        "GREATER_EQUALS",
        "MINUS",
        "BITWISE_AND",
        "DIVISION",
        "LESS_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxeInfixOperators"

def test_haxeattributeproperty_exists():
    # Check that the Enumeration exists
    assert HaxeAttributeProperty is not None

def test_haxeattributeproperty_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxeAttributeProperty]
    expected_literals = [
        "method",
        "dynamic",
        "default",
        "null",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxeAttributeProperty"

def test_haxeprefixoperators_exists():
    # Check that the Enumeration exists
    assert HaxePrefixOperators is not None

def test_haxeprefixoperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxePrefixOperators]
    expected_literals = [
        "NOT",
        "INCREMENT",
        "PLUS",
        "ONECOMPLEMENT",
        "DECREMENT",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxePrefixOperators"


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
HaxeComment_strategy = st.builds(
    HaxeComment,
)
haxe::HaxeHaxedocComment_strategy = st.builds(
    haxe::HaxeHaxedocComment,
)
HaxeASTNode_strategy = st.builds(
    HaxeASTNode,
)
haxe::HaxeTextElement_strategy = st.builds(
    haxe::HaxeTextElement,
    text=
        safe_text
)
haxe::HaxeTagElement_strategy = st.builds(
    haxe::HaxeTagElement,
    tagName=
        safe_text
)
haxe::HaxeNamedElement_strategy = st.builds(
    haxe::HaxeNamedElement,
    name=
        safe_text
)
haxe::HaxeComment_strategy = st.builds(
    haxe::HaxeComment,
    prefixOfParent=
        st.booleans(),
    enclosedByParent=
        st.booleans(),
    lineComment=
        st.booleans(),
    content=
        safe_text
)
HaxeModelElement_strategy = st.builds(
    HaxeModelElement,
)
haxe::HaxeASTNode_strategy = st.builds(
    haxe::HaxeASTNode,
)
haxe::HaxeModelElement_strategy = st.builds(
    haxe::HaxeModelElement,
)
haxe::HaxeModel_strategy = st.builds(
    haxe::HaxeModel,
    sourceFolder=
        safe_text,
    targetFolder=
        safe_text,
    target=
        safe_text,
    name=
        safe_text
)
haxe::HaxeMetadataContainer_strategy = st.builds(
    haxe::HaxeMetadataContainer,
)
HaxeDependencyDeclaration_strategy = st.builds(
    HaxeDependencyDeclaration,
)
haxe::HaxeUsingDeclaration_strategy = st.builds(
    haxe::HaxeUsingDeclaration,
)
haxe::HaxeImportDeclaration_strategy = st.builds(
    haxe::HaxeImportDeclaration,
)
HaxeAbstractOperation_strategy = st.builds(
    HaxeAbstractOperation,
)
haxe::HaxeAbstractFunction_strategy = st.builds(
    haxe::HaxeAbstractFunction,
)
HaxeSingleVariableDeclaration_strategy = st.builds(
    HaxeSingleVariableDeclaration,
)
HaxeField_strategy = st.builds(
    HaxeField,
)
HaxeClassifier_strategy = st.builds(
    HaxeClassifier,
)
haxe::HaxeEnum_strategy = st.builds(
    haxe::HaxeEnum,
)
haxe::HaxeClass_strategy = st.builds(
    haxe::HaxeClass,
    isInterface=
        st.booleans()
)
haxe::HaxeAbstract_strategy = st.builds(
    haxe::HaxeAbstract,
)
haxe::HaxeTypedElement_strategy = st.builds(
    haxe::HaxeTypedElement,
)
HaxeTypeAccess_strategy = st.builds(
    HaxeTypeAccess,
)
haxe::HaxeFunctionTypeAccess_strategy = st.builds(
    haxe::HaxeFunctionTypeAccess,
)
haxe::HaxeConstructor_strategy = st.builds(
    haxe::HaxeConstructor,
)
haxe::HaxeAttribute_strategy = st.builds(
    haxe::HaxeAttribute,
    getterProperty=
        safe_text,
    setterProperty=
        safe_text
)
HaxeMetadataContainer_strategy = st.builds(
    HaxeMetadataContainer,
)
HaxeFieldContainer_strategy = st.builds(
    HaxeFieldContainer,
)
HaxeType_strategy = st.builds(
    HaxeType,
)
haxe::HaxeTypedef_strategy = st.builds(
    haxe::HaxeTypedef,
)
haxe::HaxeClassifier_strategy = st.builds(
    haxe::HaxeClassifier,
)
haxe::HaxeTypeParameter_strategy = st.builds(
    haxe::HaxeTypeParameter,
)
HaxePathReferentiable_strategy = st.builds(
    HaxePathReferentiable,
)
haxe::HaxeType_strategy = st.builds(
    haxe::HaxeType,
    private=
        st.booleans(),
    extern=
        st.booleans()
)
HaxeVariableDeclaration_strategy = st.builds(
    HaxeVariableDeclaration,
)
haxe::HaxeEnumConstructor_strategy = st.builds(
    haxe::HaxeEnumConstructor,
)
haxe::HaxeVariableDeclarationFragment_strategy = st.builds(
    haxe::HaxeVariableDeclarationFragment,
)
haxe::HaxeAbstractMethodInvocation_strategy = st.builds(
    haxe::HaxeAbstractMethodInvocation,
)
HaxePathReference_strategy = st.builds(
    HaxePathReference,
)
haxe::HaxeDependencyDeclaration_strategy = st.builds(
    haxe::HaxeDependencyDeclaration,
)
haxe::HaxeClassifierAccess_strategy = st.builds(
    haxe::HaxeClassifierAccess,
)
HaxeMethodInvocation_strategy = st.builds(
    HaxeMethodInvocation,
)
haxe::HaxeSuperConstructorInvocation_strategy = st.builds(
    haxe::HaxeSuperConstructorInvocation,
)
HaxeAbstractMethodInvocation_strategy = st.builds(
    HaxeAbstractMethodInvocation,
)
HaxeTypedElement_strategy = st.builds(
    HaxeTypedElement,
)
haxe::HaxeOperation_strategy = st.builds(
    haxe::HaxeOperation,
    macro=
        st.booleans()
)
haxe::HaxeVariableDeclarationGroup_strategy = st.builds(
    haxe::HaxeVariableDeclarationGroup,
)
HaxeAbstractFunction_strategy = st.builds(
    HaxeAbstractFunction,
)
haxe::HaxeAbstractOperation_strategy = st.builds(
    haxe::HaxeAbstractOperation,
    overrides=
        st.booleans(),
    isInline=
        st.booleans()
)
HaxeConstant_strategy = st.builds(
    HaxeConstant,
)
haxe::HaxeBooleanLiteral_strategy = st.builds(
    haxe::HaxeBooleanLiteral,
    value=
        st.booleans()
)
haxe::HaxeNumberLiteral_strategy = st.builds(
    haxe::HaxeNumberLiteral,
    value=
        safe_text
)
haxe::HaxeNullLiteral_strategy = st.builds(
    haxe::HaxeNullLiteral,
)
haxe::HaxeRegexLiteral_strategy = st.builds(
    haxe::HaxeRegexLiteral,
    pattern=
        safe_text,
    options=
        safe_text
)
haxe::HaxeIdentifierLiteral_strategy = st.builds(
    haxe::HaxeIdentifierLiteral,
    value=
        safe_text
)
haxe::HaxeStringLiteral_strategy = st.builds(
    haxe::HaxeStringLiteral,
    escapedValue=
        safe_text
)
HaxeExpressionStatement_strategy = st.builds(
    HaxeExpressionStatement,
)
haxe::HaxeThrowExpression_strategy = st.builds(
    haxe::HaxeThrowExpression,
)
haxe::HaxeReturn_strategy = st.builds(
    haxe::HaxeReturn,
)
HaxeBinaryExpression_strategy = st.builds(
    HaxeBinaryExpression,
)
haxe::HaxeAssignment_strategy = st.builds(
    haxe::HaxeAssignment,
    operator=
        safe_text
)
haxe::HaxeInfixExpression_strategy = st.builds(
    haxe::HaxeInfixExpression,
    operator=
        safe_text
)
HaxeUnaryExpression_strategy = st.builds(
    HaxeUnaryExpression,
)
haxe::HaxePostfixExpression_strategy = st.builds(
    haxe::HaxePostfixExpression,
    isIncrement=
        st.booleans()
)
haxe::HaxePrefixExpression_strategy = st.builds(
    haxe::HaxePrefixExpression,
    operator=
        safe_text
)
haxe::HaxeSingleVariableDeclaration_strategy = st.builds(
    haxe::HaxeSingleVariableDeclaration,
    isOptional=
        st.booleans()
)
HaxeLoopStatement_strategy = st.builds(
    HaxeLoopStatement,
)
haxe::HaxeDoWhileStatement_strategy = st.builds(
    haxe::HaxeDoWhileStatement,
)
haxe::HaxeWhileStatement_strategy = st.builds(
    haxe::HaxeWhileStatement,
)
haxe::HaxeForStatement_strategy = st.builds(
    haxe::HaxeForStatement,
)
HaxeConditionalExpression_strategy = st.builds(
    HaxeConditionalExpression,
)
haxe::HaxeTernaryExpression_strategy = st.builds(
    haxe::HaxeTernaryExpression,
)
haxe::HaxeIfStatement_strategy = st.builds(
    haxe::HaxeIfStatement,
)
HaxeExpression_strategy = st.builds(
    HaxeExpression,
)
haxe::HaxeObjectDeclaration_strategy = st.builds(
    haxe::HaxeObjectDeclaration,
)
haxe::HaxeSuperMethodInvocation_strategy = st.builds(
    haxe::HaxeSuperMethodInvocation,
)
haxe::HaxeConditionalExpression_strategy = st.builds(
    haxe::HaxeConditionalExpression,
)
haxe::HaxeSingleVariableAccess_strategy = st.builds(
    haxe::HaxeSingleVariableAccess,
)
haxe::HaxeSwitch_strategy = st.builds(
    haxe::HaxeSwitch,
)
haxe::HaxeBinaryExpression_strategy = st.builds(
    haxe::HaxeBinaryExpression,
)
haxe::HaxeArrayInitializer_strategy = st.builds(
    haxe::HaxeArrayInitializer,
)
haxe::HaxeConstant_strategy = st.builds(
    haxe::HaxeConstant,
)
haxe::HaxeExpressionStatement_strategy = st.builds(
    haxe::HaxeExpressionStatement,
)
haxe::HaxeVariableDeclarationExpression_strategy = st.builds(
    haxe::HaxeVariableDeclarationExpression,
)
haxe::HaxeFieldAccess_strategy = st.builds(
    haxe::HaxeFieldAccess,
)
haxe::HaxeCase_strategy = st.builds(
    haxe::HaxeCase,
)
haxe::HaxeBreak_strategy = st.builds(
    haxe::HaxeBreak,
)
haxe::HaxeContinue_strategy = st.builds(
    haxe::HaxeContinue,
)
haxe::HaxeUnsafeCastExpression_strategy = st.builds(
    haxe::HaxeUnsafeCastExpression,
)
haxe::HaxeInExpression_strategy = st.builds(
    haxe::HaxeInExpression,
)
haxe::HaxeArrayCreation_strategy = st.builds(
    haxe::HaxeArrayCreation,
)
haxe::HaxeBlock_strategy = st.builds(
    haxe::HaxeBlock,
)
haxe::HaxeTypeAccess_strategy = st.builds(
    haxe::HaxeTypeAccess,
)
haxe::HaxeCatchClause_strategy = st.builds(
    haxe::HaxeCatchClause,
)
haxe::HaxeParenthizedExpression_strategy = st.builds(
    haxe::HaxeParenthizedExpression,
)
haxe::HaxeMethodInvocation_strategy = st.builds(
    haxe::HaxeMethodInvocation,
)
haxe::HaxeFunctionExpression_strategy = st.builds(
    haxe::HaxeFunctionExpression,
)
haxe::HaxePackageAccess_strategy = st.builds(
    haxe::HaxePackageAccess,
)
haxe::HaxeThisExpression_strategy = st.builds(
    haxe::HaxeThisExpression,
)
haxe::HaxeTypeCheckExpression_strategy = st.builds(
    haxe::HaxeTypeCheckExpression,
)
haxe::HaxeTryExpression_strategy = st.builds(
    haxe::HaxeTryExpression,
)
haxe::HaxeCallExpression_strategy = st.builds(
    haxe::HaxeCallExpression,
)
haxe::HaxeUnaryExpression_strategy = st.builds(
    haxe::HaxeUnaryExpression,
)
haxe::HaxeEmptyStatement_strategy = st.builds(
    haxe::HaxeEmptyStatement,
)
haxe::HaxeCastingExpression_strategy = st.builds(
    haxe::HaxeCastingExpression,
)
haxe::HaxeArrayAccess_strategy = st.builds(
    haxe::HaxeArrayAccess,
)
haxe::HaxeLoopStatement_strategy = st.builds(
    haxe::HaxeLoopStatement,
)
haxe::HaxeExpression_strategy = st.builds(
    haxe::HaxeExpression,
)
haxe::HaxeFieldContainer_strategy = st.builds(
    haxe::HaxeFieldContainer,
)
haxe::HaxePathReference_strategy = st.builds(
    haxe::HaxePathReference,
)
haxe::HaxePackage_strategy = st.builds(
    haxe::HaxePackage,
)
HaxeNamedElement_strategy = st.builds(
    HaxeNamedElement,
)
haxe::HaxeMetadata_strategy = st.builds(
    haxe::HaxeMetadata,
    compilerMetadata=
        st.booleans()
)
haxe::HaxePathReferentiable_strategy = st.builds(
    haxe::HaxePathReferentiable,
)
haxe::HaxeField_strategy = st.builds(
    haxe::HaxeField,
    isPrivate=
        st.booleans(),
    isStatic=
        st.booleans()
)
haxe::HaxeFieldDeclaration_strategy = st.builds(
    haxe::HaxeFieldDeclaration,
)
haxe::HaxeVariableDeclaration_strategy = st.builds(
    haxe::HaxeVariableDeclaration,
)
haxe::HaxeModule_strategy = st.builds(
    haxe::HaxeModule,
)

@given(instance=HaxeComment_strategy)
@settings(max_examples=50)
def test_haxecomment_instantiation(instance):
    assert isinstance(instance, HaxeComment)

@given(instance=haxe::HaxeHaxedocComment_strategy)
@settings(max_examples=50)
def test_haxe::haxehaxedoccomment_instantiation(instance):
    assert isinstance(instance, haxe::HaxeHaxedocComment)

@given(instance=HaxeASTNode_strategy)
@settings(max_examples=50)
def test_haxeastnode_instantiation(instance):
    assert isinstance(instance, HaxeASTNode)

@given(instance=haxe::HaxeTextElement_strategy)
@settings(max_examples=50)
def test_haxe::haxetextelement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTextElement)

@given(instance=haxe::HaxeTextElement_strategy)
def test_haxe::haxetextelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=haxe::HaxeTextElement_strategy)
def test_haxe::haxetextelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=haxe::HaxeTagElement_strategy)
@settings(max_examples=50)
def test_haxe::haxetagelement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTagElement)

@given(instance=haxe::HaxeTagElement_strategy)
def test_haxe::haxetagelement_tagName_type(instance):
    assert isinstance(instance.tagName, str)


@given(instance=haxe::HaxeTagElement_strategy)
def test_haxe::haxetagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=haxe::HaxeNamedElement_strategy)
@settings(max_examples=50)
def test_haxe::haxenamedelement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeNamedElement)

@given(instance=haxe::HaxeNamedElement_strategy)
def test_haxe::haxenamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=haxe::HaxeNamedElement_strategy)
def test_haxe::haxenamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=haxe::HaxeComment_strategy)
@settings(max_examples=50)
def test_haxe::haxecomment_instantiation(instance):
    assert isinstance(instance, haxe::HaxeComment)

@given(instance=haxe::HaxeComment_strategy)
def test_haxe::haxecomment_prefixOfParent_type(instance):
    assert isinstance(instance.prefixOfParent, bool)


@given(instance=haxe::HaxeComment_strategy)
def test_haxe::haxecomment_prefixOfParent_setter(instance):
    original = instance.prefixOfParent
    instance.prefixOfParent = original
    assert instance.prefixOfParent == original

@given(instance=haxe::HaxeComment_strategy)
def test_haxe::haxecomment_enclosedByParent_type(instance):
    assert isinstance(instance.enclosedByParent, bool)


@given(instance=haxe::HaxeComment_strategy)
def test_haxe::haxecomment_enclosedByParent_setter(instance):
    original = instance.enclosedByParent
    instance.enclosedByParent = original
    assert instance.enclosedByParent == original

@given(instance=haxe::HaxeComment_strategy)
def test_haxe::haxecomment_lineComment_type(instance):
    assert isinstance(instance.lineComment, bool)


@given(instance=haxe::HaxeComment_strategy)
def test_haxe::haxecomment_lineComment_setter(instance):
    original = instance.lineComment
    instance.lineComment = original
    assert instance.lineComment == original

@given(instance=haxe::HaxeComment_strategy)
def test_haxe::haxecomment_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=haxe::HaxeComment_strategy)
def test_haxe::haxecomment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=HaxeModelElement_strategy)
@settings(max_examples=50)
def test_haxemodelelement_instantiation(instance):
    assert isinstance(instance, HaxeModelElement)

@given(instance=haxe::HaxeASTNode_strategy)
@settings(max_examples=50)
def test_haxe::haxeastnode_instantiation(instance):
    assert isinstance(instance, haxe::HaxeASTNode)

@given(instance=haxe::HaxeModelElement_strategy)
@settings(max_examples=50)
def test_haxe::haxemodelelement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeModelElement)

@given(instance=haxe::HaxeModel_strategy)
@settings(max_examples=50)
def test_haxe::haxemodel_instantiation(instance):
    assert isinstance(instance, haxe::HaxeModel)

@given(instance=haxe::HaxeModel_strategy)
def test_haxe::haxemodel_sourceFolder_type(instance):
    assert isinstance(instance.sourceFolder, str)


@given(instance=haxe::HaxeModel_strategy)
def test_haxe::haxemodel_sourceFolder_setter(instance):
    original = instance.sourceFolder
    instance.sourceFolder = original
    assert instance.sourceFolder == original

@given(instance=haxe::HaxeModel_strategy)
def test_haxe::haxemodel_targetFolder_type(instance):
    assert isinstance(instance.targetFolder, str)


@given(instance=haxe::HaxeModel_strategy)
def test_haxe::haxemodel_targetFolder_setter(instance):
    original = instance.targetFolder
    instance.targetFolder = original
    assert instance.targetFolder == original

@given(instance=haxe::HaxeModel_strategy)
def test_haxe::haxemodel_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=haxe::HaxeModel_strategy)
def test_haxe::haxemodel_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=haxe::HaxeModel_strategy)
def test_haxe::haxemodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=haxe::HaxeModel_strategy)
def test_haxe::haxemodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=haxe::HaxeMetadataContainer_strategy)
@settings(max_examples=50)
def test_haxe::haxemetadatacontainer_instantiation(instance):
    assert isinstance(instance, haxe::HaxeMetadataContainer)

@given(instance=HaxeDependencyDeclaration_strategy)
@settings(max_examples=50)
def test_haxedependencydeclaration_instantiation(instance):
    assert isinstance(instance, HaxeDependencyDeclaration)

@given(instance=haxe::HaxeUsingDeclaration_strategy)
@settings(max_examples=50)
def test_haxe::haxeusingdeclaration_instantiation(instance):
    assert isinstance(instance, haxe::HaxeUsingDeclaration)

@given(instance=haxe::HaxeImportDeclaration_strategy)
@settings(max_examples=50)
def test_haxe::haxeimportdeclaration_instantiation(instance):
    assert isinstance(instance, haxe::HaxeImportDeclaration)

@given(instance=HaxeAbstractOperation_strategy)
@settings(max_examples=50)
def test_haxeabstractoperation_instantiation(instance):
    assert isinstance(instance, HaxeAbstractOperation)

@given(instance=haxe::HaxeAbstractFunction_strategy)
@settings(max_examples=50)
def test_haxe::haxeabstractfunction_instantiation(instance):
    assert isinstance(instance, haxe::HaxeAbstractFunction)

@given(instance=HaxeSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_haxesinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, HaxeSingleVariableDeclaration)

@given(instance=HaxeField_strategy)
@settings(max_examples=50)
def test_haxefield_instantiation(instance):
    assert isinstance(instance, HaxeField)

@given(instance=HaxeClassifier_strategy)
@settings(max_examples=50)
def test_haxeclassifier_instantiation(instance):
    assert isinstance(instance, HaxeClassifier)

@given(instance=haxe::HaxeEnum_strategy)
@settings(max_examples=50)
def test_haxe::haxeenum_instantiation(instance):
    assert isinstance(instance, haxe::HaxeEnum)

@given(instance=haxe::HaxeClass_strategy)
@settings(max_examples=50)
def test_haxe::haxeclass_instantiation(instance):
    assert isinstance(instance, haxe::HaxeClass)

@given(instance=haxe::HaxeClass_strategy)
def test_haxe::haxeclass_isInterface_type(instance):
    assert isinstance(instance.isInterface, bool)


@given(instance=haxe::HaxeClass_strategy)
def test_haxe::haxeclass_isInterface_setter(instance):
    original = instance.isInterface
    instance.isInterface = original
    assert instance.isInterface == original

@given(instance=haxe::HaxeAbstract_strategy)
@settings(max_examples=50)
def test_haxe::haxeabstract_instantiation(instance):
    assert isinstance(instance, haxe::HaxeAbstract)

@given(instance=haxe::HaxeTypedElement_strategy)
@settings(max_examples=50)
def test_haxe::haxetypedelement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTypedElement)

@given(instance=HaxeTypeAccess_strategy)
@settings(max_examples=50)
def test_haxetypeaccess_instantiation(instance):
    assert isinstance(instance, HaxeTypeAccess)

@given(instance=haxe::HaxeFunctionTypeAccess_strategy)
@settings(max_examples=50)
def test_haxe::haxefunctiontypeaccess_instantiation(instance):
    assert isinstance(instance, haxe::HaxeFunctionTypeAccess)

@given(instance=haxe::HaxeConstructor_strategy)
@settings(max_examples=50)
def test_haxe::haxeconstructor_instantiation(instance):
    assert isinstance(instance, haxe::HaxeConstructor)

@given(instance=haxe::HaxeAttribute_strategy)
@settings(max_examples=50)
def test_haxe::haxeattribute_instantiation(instance):
    assert isinstance(instance, haxe::HaxeAttribute)

@given(instance=haxe::HaxeAttribute_strategy)
def test_haxe::haxeattribute_getterProperty_type(instance):
    assert isinstance(instance.getterProperty, str)


@given(instance=haxe::HaxeAttribute_strategy)
def test_haxe::haxeattribute_getterProperty_setter(instance):
    original = instance.getterProperty
    instance.getterProperty = original
    assert instance.getterProperty == original

@given(instance=haxe::HaxeAttribute_strategy)
def test_haxe::haxeattribute_setterProperty_type(instance):
    assert isinstance(instance.setterProperty, str)


@given(instance=haxe::HaxeAttribute_strategy)
def test_haxe::haxeattribute_setterProperty_setter(instance):
    original = instance.setterProperty
    instance.setterProperty = original
    assert instance.setterProperty == original

@given(instance=HaxeMetadataContainer_strategy)
@settings(max_examples=50)
def test_haxemetadatacontainer_instantiation(instance):
    assert isinstance(instance, HaxeMetadataContainer)

@given(instance=HaxeFieldContainer_strategy)
@settings(max_examples=50)
def test_haxefieldcontainer_instantiation(instance):
    assert isinstance(instance, HaxeFieldContainer)

@given(instance=HaxeType_strategy)
@settings(max_examples=50)
def test_haxetype_instantiation(instance):
    assert isinstance(instance, HaxeType)

@given(instance=haxe::HaxeTypedef_strategy)
@settings(max_examples=50)
def test_haxe::haxetypedef_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTypedef)

@given(instance=haxe::HaxeClassifier_strategy)
@settings(max_examples=50)
def test_haxe::haxeclassifier_instantiation(instance):
    assert isinstance(instance, haxe::HaxeClassifier)

@given(instance=haxe::HaxeTypeParameter_strategy)
@settings(max_examples=50)
def test_haxe::haxetypeparameter_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTypeParameter)

@given(instance=HaxePathReferentiable_strategy)
@settings(max_examples=50)
def test_haxepathreferentiable_instantiation(instance):
    assert isinstance(instance, HaxePathReferentiable)

@given(instance=haxe::HaxeType_strategy)
@settings(max_examples=50)
def test_haxe::haxetype_instantiation(instance):
    assert isinstance(instance, haxe::HaxeType)

@given(instance=haxe::HaxeType_strategy)
def test_haxe::haxetype_private_type(instance):
    assert isinstance(instance.private, bool)


@given(instance=haxe::HaxeType_strategy)
def test_haxe::haxetype_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=haxe::HaxeType_strategy)
def test_haxe::haxetype_extern_type(instance):
    assert isinstance(instance.extern, bool)


@given(instance=haxe::HaxeType_strategy)
def test_haxe::haxetype_extern_setter(instance):
    original = instance.extern
    instance.extern = original
    assert instance.extern == original

@given(instance=HaxeVariableDeclaration_strategy)
@settings(max_examples=50)
def test_haxevariabledeclaration_instantiation(instance):
    assert isinstance(instance, HaxeVariableDeclaration)

@given(instance=haxe::HaxeEnumConstructor_strategy)
@settings(max_examples=50)
def test_haxe::haxeenumconstructor_instantiation(instance):
    assert isinstance(instance, haxe::HaxeEnumConstructor)

@given(instance=haxe::HaxeVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_haxe::haxevariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, haxe::HaxeVariableDeclarationFragment)

@given(instance=haxe::HaxeAbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxe::haxeabstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, haxe::HaxeAbstractMethodInvocation)

@given(instance=HaxePathReference_strategy)
@settings(max_examples=50)
def test_haxepathreference_instantiation(instance):
    assert isinstance(instance, HaxePathReference)

@given(instance=haxe::HaxeDependencyDeclaration_strategy)
@settings(max_examples=50)
def test_haxe::haxedependencydeclaration_instantiation(instance):
    assert isinstance(instance, haxe::HaxeDependencyDeclaration)

@given(instance=haxe::HaxeClassifierAccess_strategy)
@settings(max_examples=50)
def test_haxe::haxeclassifieraccess_instantiation(instance):
    assert isinstance(instance, haxe::HaxeClassifierAccess)

@given(instance=HaxeMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxemethodinvocation_instantiation(instance):
    assert isinstance(instance, HaxeMethodInvocation)

@given(instance=haxe::HaxeSuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_haxe::haxesuperconstructorinvocation_instantiation(instance):
    assert isinstance(instance, haxe::HaxeSuperConstructorInvocation)

@given(instance=HaxeAbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxeabstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, HaxeAbstractMethodInvocation)

@given(instance=HaxeTypedElement_strategy)
@settings(max_examples=50)
def test_haxetypedelement_instantiation(instance):
    assert isinstance(instance, HaxeTypedElement)

@given(instance=haxe::HaxeOperation_strategy)
@settings(max_examples=50)
def test_haxe::haxeoperation_instantiation(instance):
    assert isinstance(instance, haxe::HaxeOperation)

@given(instance=haxe::HaxeOperation_strategy)
def test_haxe::haxeoperation_macro_type(instance):
    assert isinstance(instance.macro, bool)


@given(instance=haxe::HaxeOperation_strategy)
def test_haxe::haxeoperation_macro_setter(instance):
    original = instance.macro
    instance.macro = original
    assert instance.macro == original

@given(instance=haxe::HaxeVariableDeclarationGroup_strategy)
@settings(max_examples=50)
def test_haxe::haxevariabledeclarationgroup_instantiation(instance):
    assert isinstance(instance, haxe::HaxeVariableDeclarationGroup)

@given(instance=HaxeAbstractFunction_strategy)
@settings(max_examples=50)
def test_haxeabstractfunction_instantiation(instance):
    assert isinstance(instance, HaxeAbstractFunction)

@given(instance=haxe::HaxeAbstractOperation_strategy)
@settings(max_examples=50)
def test_haxe::haxeabstractoperation_instantiation(instance):
    assert isinstance(instance, haxe::HaxeAbstractOperation)

@given(instance=haxe::HaxeAbstractOperation_strategy)
def test_haxe::haxeabstractoperation_overrides_type(instance):
    assert isinstance(instance.overrides, bool)


@given(instance=haxe::HaxeAbstractOperation_strategy)
def test_haxe::haxeabstractoperation_overrides_setter(instance):
    original = instance.overrides
    instance.overrides = original
    assert instance.overrides == original

@given(instance=haxe::HaxeAbstractOperation_strategy)
def test_haxe::haxeabstractoperation_isInline_type(instance):
    assert isinstance(instance.isInline, bool)


@given(instance=haxe::HaxeAbstractOperation_strategy)
def test_haxe::haxeabstractoperation_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original

@given(instance=HaxeConstant_strategy)
@settings(max_examples=50)
def test_haxeconstant_instantiation(instance):
    assert isinstance(instance, HaxeConstant)

@given(instance=haxe::HaxeBooleanLiteral_strategy)
@settings(max_examples=50)
def test_haxe::haxebooleanliteral_instantiation(instance):
    assert isinstance(instance, haxe::HaxeBooleanLiteral)

@given(instance=haxe::HaxeBooleanLiteral_strategy)
def test_haxe::haxebooleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=haxe::HaxeBooleanLiteral_strategy)
def test_haxe::haxebooleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=haxe::HaxeNumberLiteral_strategy)
@settings(max_examples=50)
def test_haxe::haxenumberliteral_instantiation(instance):
    assert isinstance(instance, haxe::HaxeNumberLiteral)

@given(instance=haxe::HaxeNumberLiteral_strategy)
def test_haxe::haxenumberliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=haxe::HaxeNumberLiteral_strategy)
def test_haxe::haxenumberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=haxe::HaxeNullLiteral_strategy)
@settings(max_examples=50)
def test_haxe::haxenullliteral_instantiation(instance):
    assert isinstance(instance, haxe::HaxeNullLiteral)

@given(instance=haxe::HaxeRegexLiteral_strategy)
@settings(max_examples=50)
def test_haxe::haxeregexliteral_instantiation(instance):
    assert isinstance(instance, haxe::HaxeRegexLiteral)

@given(instance=haxe::HaxeRegexLiteral_strategy)
def test_haxe::haxeregexliteral_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=haxe::HaxeRegexLiteral_strategy)
def test_haxe::haxeregexliteral_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=haxe::HaxeRegexLiteral_strategy)
def test_haxe::haxeregexliteral_options_type(instance):
    assert isinstance(instance.options, str)


@given(instance=haxe::HaxeRegexLiteral_strategy)
def test_haxe::haxeregexliteral_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original

@given(instance=haxe::HaxeIdentifierLiteral_strategy)
@settings(max_examples=50)
def test_haxe::haxeidentifierliteral_instantiation(instance):
    assert isinstance(instance, haxe::HaxeIdentifierLiteral)

@given(instance=haxe::HaxeIdentifierLiteral_strategy)
def test_haxe::haxeidentifierliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=haxe::HaxeIdentifierLiteral_strategy)
def test_haxe::haxeidentifierliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=haxe::HaxeStringLiteral_strategy)
@settings(max_examples=50)
def test_haxe::haxestringliteral_instantiation(instance):
    assert isinstance(instance, haxe::HaxeStringLiteral)

@given(instance=haxe::HaxeStringLiteral_strategy)
def test_haxe::haxestringliteral_escapedValue_type(instance):
    assert isinstance(instance.escapedValue, str)


@given(instance=haxe::HaxeStringLiteral_strategy)
def test_haxe::haxestringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=HaxeExpressionStatement_strategy)
@settings(max_examples=50)
def test_haxeexpressionstatement_instantiation(instance):
    assert isinstance(instance, HaxeExpressionStatement)

@given(instance=haxe::HaxeThrowExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxethrowexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeThrowExpression)

@given(instance=haxe::HaxeReturn_strategy)
@settings(max_examples=50)
def test_haxe::haxereturn_instantiation(instance):
    assert isinstance(instance, haxe::HaxeReturn)

@given(instance=HaxeBinaryExpression_strategy)
@settings(max_examples=50)
def test_haxebinaryexpression_instantiation(instance):
    assert isinstance(instance, HaxeBinaryExpression)

@given(instance=haxe::HaxeAssignment_strategy)
@settings(max_examples=50)
def test_haxe::haxeassignment_instantiation(instance):
    assert isinstance(instance, haxe::HaxeAssignment)

@given(instance=haxe::HaxeAssignment_strategy)
def test_haxe::haxeassignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=haxe::HaxeAssignment_strategy)
def test_haxe::haxeassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=haxe::HaxeInfixExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeinfixexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeInfixExpression)

@given(instance=haxe::HaxeInfixExpression_strategy)
def test_haxe::haxeinfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=haxe::HaxeInfixExpression_strategy)
def test_haxe::haxeinfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=HaxeUnaryExpression_strategy)
@settings(max_examples=50)
def test_haxeunaryexpression_instantiation(instance):
    assert isinstance(instance, HaxeUnaryExpression)

@given(instance=haxe::HaxePostfixExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxepostfixexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxePostfixExpression)

@given(instance=haxe::HaxePostfixExpression_strategy)
def test_haxe::haxepostfixexpression_isIncrement_type(instance):
    assert isinstance(instance.isIncrement, bool)


@given(instance=haxe::HaxePostfixExpression_strategy)
def test_haxe::haxepostfixexpression_isIncrement_setter(instance):
    original = instance.isIncrement
    instance.isIncrement = original
    assert instance.isIncrement == original

@given(instance=haxe::HaxePrefixExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeprefixexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxePrefixExpression)

@given(instance=haxe::HaxePrefixExpression_strategy)
def test_haxe::haxeprefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=haxe::HaxePrefixExpression_strategy)
def test_haxe::haxeprefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=haxe::HaxeSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_haxe::haxesinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, haxe::HaxeSingleVariableDeclaration)

@given(instance=haxe::HaxeSingleVariableDeclaration_strategy)
def test_haxe::haxesinglevariabledeclaration_isOptional_type(instance):
    assert isinstance(instance.isOptional, bool)


@given(instance=haxe::HaxeSingleVariableDeclaration_strategy)
def test_haxe::haxesinglevariabledeclaration_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=HaxeLoopStatement_strategy)
@settings(max_examples=50)
def test_haxeloopstatement_instantiation(instance):
    assert isinstance(instance, HaxeLoopStatement)

@given(instance=haxe::HaxeDoWhileStatement_strategy)
@settings(max_examples=50)
def test_haxe::haxedowhilestatement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeDoWhileStatement)

@given(instance=haxe::HaxeWhileStatement_strategy)
@settings(max_examples=50)
def test_haxe::haxewhilestatement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeWhileStatement)

@given(instance=haxe::HaxeForStatement_strategy)
@settings(max_examples=50)
def test_haxe::haxeforstatement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeForStatement)

@given(instance=HaxeConditionalExpression_strategy)
@settings(max_examples=50)
def test_haxeconditionalexpression_instantiation(instance):
    assert isinstance(instance, HaxeConditionalExpression)

@given(instance=haxe::HaxeTernaryExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeternaryexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTernaryExpression)

@given(instance=haxe::HaxeIfStatement_strategy)
@settings(max_examples=50)
def test_haxe::haxeifstatement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeIfStatement)

@given(instance=HaxeExpression_strategy)
@settings(max_examples=50)
def test_haxeexpression_instantiation(instance):
    assert isinstance(instance, HaxeExpression)

@given(instance=haxe::HaxeObjectDeclaration_strategy)
@settings(max_examples=50)
def test_haxe::haxeobjectdeclaration_instantiation(instance):
    assert isinstance(instance, haxe::HaxeObjectDeclaration)

@given(instance=haxe::HaxeSuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxe::haxesupermethodinvocation_instantiation(instance):
    assert isinstance(instance, haxe::HaxeSuperMethodInvocation)

@given(instance=haxe::HaxeConditionalExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeconditionalexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeConditionalExpression)

@given(instance=haxe::HaxeSingleVariableAccess_strategy)
@settings(max_examples=50)
def test_haxe::haxesinglevariableaccess_instantiation(instance):
    assert isinstance(instance, haxe::HaxeSingleVariableAccess)

@given(instance=haxe::HaxeSwitch_strategy)
@settings(max_examples=50)
def test_haxe::haxeswitch_instantiation(instance):
    assert isinstance(instance, haxe::HaxeSwitch)

@given(instance=haxe::HaxeBinaryExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxebinaryexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeBinaryExpression)

@given(instance=haxe::HaxeArrayInitializer_strategy)
@settings(max_examples=50)
def test_haxe::haxearrayinitializer_instantiation(instance):
    assert isinstance(instance, haxe::HaxeArrayInitializer)

@given(instance=haxe::HaxeConstant_strategy)
@settings(max_examples=50)
def test_haxe::haxeconstant_instantiation(instance):
    assert isinstance(instance, haxe::HaxeConstant)

@given(instance=haxe::HaxeExpressionStatement_strategy)
@settings(max_examples=50)
def test_haxe::haxeexpressionstatement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeExpressionStatement)

@given(instance=haxe::HaxeVariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxevariabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeVariableDeclarationExpression)

@given(instance=haxe::HaxeFieldAccess_strategy)
@settings(max_examples=50)
def test_haxe::haxefieldaccess_instantiation(instance):
    assert isinstance(instance, haxe::HaxeFieldAccess)

@given(instance=haxe::HaxeCase_strategy)
@settings(max_examples=50)
def test_haxe::haxecase_instantiation(instance):
    assert isinstance(instance, haxe::HaxeCase)

@given(instance=haxe::HaxeBreak_strategy)
@settings(max_examples=50)
def test_haxe::haxebreak_instantiation(instance):
    assert isinstance(instance, haxe::HaxeBreak)

@given(instance=haxe::HaxeContinue_strategy)
@settings(max_examples=50)
def test_haxe::haxecontinue_instantiation(instance):
    assert isinstance(instance, haxe::HaxeContinue)

@given(instance=haxe::HaxeUnsafeCastExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeunsafecastexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeUnsafeCastExpression)

@given(instance=haxe::HaxeInExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeinexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeInExpression)

@given(instance=haxe::HaxeArrayCreation_strategy)
@settings(max_examples=50)
def test_haxe::haxearraycreation_instantiation(instance):
    assert isinstance(instance, haxe::HaxeArrayCreation)

@given(instance=haxe::HaxeBlock_strategy)
@settings(max_examples=50)
def test_haxe::haxeblock_instantiation(instance):
    assert isinstance(instance, haxe::HaxeBlock)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=haxe::HaxeBlock_strategy)
@settings(max_examples=30)
def test_haxe::haxeblock_isempty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isEmpty()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isEmpty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isEmpty' in haxe::HaxeBlock is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEmpty' in haxe::HaxeBlock did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEmpty' in haxe::HaxeBlock is not implemented or raised an error")

@given(instance=haxe::HaxeTypeAccess_strategy)
@settings(max_examples=50)
def test_haxe::haxetypeaccess_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTypeAccess)

@given(instance=haxe::HaxeCatchClause_strategy)
@settings(max_examples=50)
def test_haxe::haxecatchclause_instantiation(instance):
    assert isinstance(instance, haxe::HaxeCatchClause)

@given(instance=haxe::HaxeParenthizedExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeparenthizedexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeParenthizedExpression)

@given(instance=haxe::HaxeMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxe::haxemethodinvocation_instantiation(instance):
    assert isinstance(instance, haxe::HaxeMethodInvocation)

@given(instance=haxe::HaxeFunctionExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxefunctionexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeFunctionExpression)

@given(instance=haxe::HaxePackageAccess_strategy)
@settings(max_examples=50)
def test_haxe::haxepackageaccess_instantiation(instance):
    assert isinstance(instance, haxe::HaxePackageAccess)

@given(instance=haxe::HaxeThisExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxethisexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeThisExpression)

@given(instance=haxe::HaxeTypeCheckExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxetypecheckexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTypeCheckExpression)

@given(instance=haxe::HaxeTryExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxetryexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeTryExpression)

@given(instance=haxe::HaxeCallExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxecallexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeCallExpression)

@given(instance=haxe::HaxeUnaryExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeunaryexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeUnaryExpression)

@given(instance=haxe::HaxeEmptyStatement_strategy)
@settings(max_examples=50)
def test_haxe::haxeemptystatement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeEmptyStatement)

@given(instance=haxe::HaxeCastingExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxecastingexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeCastingExpression)

@given(instance=haxe::HaxeArrayAccess_strategy)
@settings(max_examples=50)
def test_haxe::haxearrayaccess_instantiation(instance):
    assert isinstance(instance, haxe::HaxeArrayAccess)

@given(instance=haxe::HaxeLoopStatement_strategy)
@settings(max_examples=50)
def test_haxe::haxeloopstatement_instantiation(instance):
    assert isinstance(instance, haxe::HaxeLoopStatement)

@given(instance=haxe::HaxeExpression_strategy)
@settings(max_examples=50)
def test_haxe::haxeexpression_instantiation(instance):
    assert isinstance(instance, haxe::HaxeExpression)

@given(instance=haxe::HaxeFieldContainer_strategy)
@settings(max_examples=50)
def test_haxe::haxefieldcontainer_instantiation(instance):
    assert isinstance(instance, haxe::HaxeFieldContainer)

@given(instance=haxe::HaxePathReference_strategy)
@settings(max_examples=50)
def test_haxe::haxepathreference_instantiation(instance):
    assert isinstance(instance, haxe::HaxePathReference)

@given(instance=haxe::HaxePackage_strategy)
@settings(max_examples=50)
def test_haxe::haxepackage_instantiation(instance):
    assert isinstance(instance, haxe::HaxePackage)

@given(instance=HaxeNamedElement_strategy)
@settings(max_examples=50)
def test_haxenamedelement_instantiation(instance):
    assert isinstance(instance, HaxeNamedElement)

@given(instance=haxe::HaxeMetadata_strategy)
@settings(max_examples=50)
def test_haxe::haxemetadata_instantiation(instance):
    assert isinstance(instance, haxe::HaxeMetadata)

@given(instance=haxe::HaxeMetadata_strategy)
def test_haxe::haxemetadata_compilerMetadata_type(instance):
    assert isinstance(instance.compilerMetadata, bool)


@given(instance=haxe::HaxeMetadata_strategy)
def test_haxe::haxemetadata_compilerMetadata_setter(instance):
    original = instance.compilerMetadata
    instance.compilerMetadata = original
    assert instance.compilerMetadata == original

@given(instance=haxe::HaxePathReferentiable_strategy)
@settings(max_examples=50)
def test_haxe::haxepathreferentiable_instantiation(instance):
    assert isinstance(instance, haxe::HaxePathReferentiable)

@given(instance=haxe::HaxeField_strategy)
@settings(max_examples=50)
def test_haxe::haxefield_instantiation(instance):
    assert isinstance(instance, haxe::HaxeField)

@given(instance=haxe::HaxeField_strategy)
def test_haxe::haxefield_isPrivate_type(instance):
    assert isinstance(instance.isPrivate, bool)


@given(instance=haxe::HaxeField_strategy)
def test_haxe::haxefield_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original

@given(instance=haxe::HaxeField_strategy)
def test_haxe::haxefield_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=haxe::HaxeField_strategy)
def test_haxe::haxefield_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=haxe::HaxeFieldDeclaration_strategy)
@settings(max_examples=50)
def test_haxe::haxefielddeclaration_instantiation(instance):
    assert isinstance(instance, haxe::HaxeFieldDeclaration)

@given(instance=haxe::HaxeVariableDeclaration_strategy)
@settings(max_examples=50)
def test_haxe::haxevariabledeclaration_instantiation(instance):
    assert isinstance(instance, haxe::HaxeVariableDeclaration)

@given(instance=haxe::HaxeModule_strategy)
@settings(max_examples=50)
def test_haxe::haxemodule_instantiation(instance):
    assert isinstance(instance, haxe::HaxeModule)
